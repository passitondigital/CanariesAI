#!/usr/bin/env python3
"""Crawl up to N pages of a small business website and summarise each page.

Works on a live site (https://...) or a local folder of saved HTML files.
Uses only the Python standard library so it runs anywhere.

Usage:
  python crawl_site.py https://example.co.uk --max-pages 20 --out crawl.json
  python crawl_site.py ./saved-site-folder --out crawl.json

The JSON output has one entry per page with the facts the audit needs:
title, meta description, headings, visible word count, images missing alt
text, structured data types, forms and whether their fields have labels,
phone/email links, and internal links. It also records robots.txt,
sitemap.xml and llms.txt where available.
"""
import argparse
import json
import os
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

USER_AGENT = "Mozilla/5.0 (compatible; WebsiteAuditBot/1.0)"
AI_CRAWLERS = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot",
               "PerplexityBot", "Google-Extended", "CCBot", "Applebot-Extended"]
SKIP_EXT = re.compile(r"\.(jpg|jpeg|png|gif|webp|svg|pdf|zip|mp4|mp3|css|js|ico|xml|txt|docx?)$", re.I)


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.meta = {}
        self.lang = None
        self.headings = []  # (level, text)
        self.links = []
        self.images = []  # (src, alt or None)
        self.jsonld = []
        self.forms = []  # list of {"inputs": n, "labelled": n}
        self.text_parts = []
        self._stack = []
        self._in_title = False
        self._in_script = None
        self._script_buf = []
        self._heading = None
        self._heading_buf = []
        self._label_for = set()
        self._input_ids = []
        self._in_label = 0
        self._form = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "title":
            self._in_title = True
        elif tag == "meta":
            key = (a.get("name") or a.get("property") or "").lower()
            if key:
                self.meta[key] = a.get("content", "")
        elif tag in ("script", "style", "noscript"):
            self._in_script = (tag, a.get("type", ""))
            self._script_buf = []
        elif tag in ("h1", "h2", "h3"):
            self._heading = tag
            self._heading_buf = []
        elif tag == "a" and a.get("href"):
            self.links.append(a["href"])
        elif tag == "img":
            self.images.append((a.get("src", ""), a.get("alt")))
        elif tag == "form":
            self._form = {"inputs": 0, "labelled": 0, "ids": [], "aria": 0, "in_label": 0}
        elif tag == "label":
            self._in_label += 1
            if a.get("for"):
                self._label_for.add(a["for"])
        elif tag in ("input", "textarea", "select") and self._form is not None:
            if a.get("type", "").lower() in ("hidden", "submit", "button"):
                return
            self._form["inputs"] += 1
            if a.get("aria-label") or a.get("aria-labelledby"):
                self._form["aria"] += 1
            elif self._in_label:
                self._form["in_label"] += 1
            elif a.get("id"):
                self._form["ids"].append(a["id"])

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag in ("script", "style", "noscript") and self._in_script:
            if self._in_script[0] == "script" and "ld+json" in self._in_script[1]:
                self.jsonld.append("".join(self._script_buf))
            self._in_script = None
        elif tag == self._heading:
            self.headings.append((tag, " ".join("".join(self._heading_buf).split())))
            self._heading = None
        elif tag == "label":
            self._in_label = max(0, self._in_label - 1)
        elif tag == "form" and self._form is not None:
            self.forms.append(self._form)
            self._form = None

    def handle_data(self, data):
        if self._in_script:
            self._script_buf.append(data)
            return
        if self._in_title:
            self.title += data
        if self._heading:
            self._heading_buf.append(data)
        self.text_parts.append(data)

    def finish_forms(self):
        out = []
        for f in self.forms:
            labelled = f["aria"] + f["in_label"] + sum(1 for i in f["ids"] if i in self._label_for)
            out.append({"fields": f["inputs"], "fields_with_labels": labelled})
        return out


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=20) as r:
        raw = r.read()
        charset = r.headers.get_content_charset() or "utf-8"
        return r.geturl(), r.status, raw.decode(charset, errors="replace")


def jsonld_types(blocks):
    types, errors = [], 0
    def walk(o):
        if isinstance(o, dict):
            t = o.get("@type")
            if t:
                types.extend(t if isinstance(t, list) else [t])
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    for b in blocks:
        try:
            walk(json.loads(b))
        except ValueError:
            errors += 1
    return sorted(set(types)), errors


def summarise(url, html):
    p = PageParser()
    p.feed(html)
    text = " ".join(" ".join(p.text_parts).split())
    types, ld_errors = jsonld_types(p.jsonld)
    tel = sorted({l[4:] for l in p.links if l.lower().startswith("tel:")})
    mail = sorted({l[7:].split("?")[0] for l in p.links if l.lower().startswith("mailto:")})
    return {
        "url": url,
        "title": " ".join(p.title.split()),
        "meta_description": p.meta.get("description", ""),
        "has_viewport_meta": "viewport" in p.meta,
        "lang": p.lang,
        "h1": [t for lvl, t in p.headings if lvl == "h1"],
        "headings": [f"{lvl}: {t}" for lvl, t in p.headings][:30],
        "word_count": len(text.split()),
        "text_excerpt": text[:1500],
        "images": len(p.images),
        "images_missing_alt": [s for s, alt in p.images if alt is None],
        "images_empty_alt": [s for s, alt in p.images if alt is not None and not alt.strip()],
        "structured_data_types": types,
        "structured_data_parse_errors": ld_errors,
        "forms": p.finish_forms(),
        "phone_links": tel,
        "email_links": mail,
        "_links": p.links,
    }


def robots_summary(text):
    """Which known AI crawlers are blocked from the whole site."""
    groups, current, rules = [], [], []
    for line in text.splitlines():
        line = line.split("#")[0].strip()
        if not line or ":" not in line:
            continue
        k, v = [x.strip() for x in line.split(":", 1)]
        k = k.lower()
        if k == "user-agent":
            if rules:
                groups.append((current, rules))
                current, rules = [], []
            current.append(v)
        elif k in ("allow", "disallow"):
            rules.append((k, v))
    if current:
        groups.append((current, rules))

    def blocked(agent):
        specific = [r for ua, r in groups if any(u.lower() == agent.lower() for u in ua)]
        rule_sets = specific or [r for ua, r in groups if "*" in ua]
        for r in rule_sets:
            if ("disallow", "/") in r and ("allow", "/") not in r:
                return True
        return False

    return {
        "all_crawlers_blocked": blocked("SomeOtherBot"),
        "ai_crawlers_blocked": [a for a in AI_CRAWLERS if blocked(a)],
    }


def crawl_url(start, max_pages):
    start = start if "://" in start else "https://" + start
    final, _, _ = fetch(start)
    base = urllib.parse.urlsplit(final)
    root = f"{base.scheme}://{base.netloc}"
    result = {"source": final, "mode": "live", "pages": [], "errors": []}

    for name in ("robots.txt", "llms.txt", "sitemap.xml"):
        try:
            _, status, body = fetch(f"{root}/{name}")
            result[name] = body[:5000]
        except Exception as e:  # noqa: BLE001 - report, don't crash
            result[name] = None
            if "404" not in str(e):
                result["errors"].append(f"{name}: {e}")
    if result["robots.txt"]:
        result["robots_summary"] = robots_summary(result["robots.txt"])

    queue, seen = [final], set()
    # Seed from the sitemap so key pages are found even if the menu is JS-driven.
    if result.get("sitemap.xml"):
        try:
            tree = ET.fromstring(result["sitemap.xml"])
            for loc in tree.iter():
                if loc.tag.endswith("loc") and loc.text and loc.text.startswith(root):
                    queue.append(loc.text.strip())
        except ET.ParseError:
            pass

    while queue and len(result["pages"]) < max_pages:
        url = urllib.parse.urldefrag(queue.pop(0))[0].rstrip("/") or root
        if url in seen or SKIP_EXT.search(urllib.parse.urlsplit(url).path):
            continue
        seen.add(url)
        try:
            got, status, html = fetch(url)
        except Exception as e:  # noqa: BLE001
            result["errors"].append(f"{url}: {e}")
            continue
        page = summarise(got, html)
        page["status"] = status
        for href in page.pop("_links"):
            full = urllib.parse.urljoin(got, href)
            if full.startswith(root) and full not in seen:
                queue.append(full)
        result["pages"].append(page)
    return result


def crawl_dir(folder, max_pages):
    result = {"source": os.path.abspath(folder), "mode": "local folder", "pages": [], "errors": []}
    for name in ("robots.txt", "llms.txt", "sitemap.xml"):
        path = os.path.join(folder, name)
        result[name] = open(path, encoding="utf-8", errors="replace").read()[:5000] if os.path.exists(path) else None
    if result["robots.txt"]:
        result["robots_summary"] = robots_summary(result["robots.txt"])
    files = []
    for dp, _, fns in os.walk(folder):
        files += [os.path.join(dp, f) for f in fns if f.lower().endswith((".html", ".htm"))]
    files.sort(key=lambda f: (os.path.basename(f) != "index.html", f))
    for f in files[:max_pages]:
        page = summarise(os.path.relpath(f, folder), open(f, encoding="utf-8", errors="replace").read())
        page.pop("_links")
        result["pages"].append(page)
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source", help="Website address or local folder of HTML files")
    ap.add_argument("--max-pages", type=int, default=20)
    ap.add_argument("--out", default="-")
    args = ap.parse_args()
    if os.path.isdir(args.source):
        data = crawl_dir(args.source, args.max_pages)
    else:
        data = crawl_url(args.source, args.max_pages)
    data["pages_checked"] = len(data["pages"])
    out = json.dumps(data, indent=2, ensure_ascii=False)
    if args.out == "-":
        print(out)
    else:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(out)
        print(f"Checked {data['pages_checked']} pages -> {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
