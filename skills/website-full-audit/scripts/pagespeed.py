#!/usr/bin/env python3
"""Get mobile speed and accessibility scores from Google PageSpeed Insights.

Usage:
  python pagespeed.py https://example.co.uk [--strategy mobile|desktop] [--out speed.json]

Uses Google's free public PageSpeed Insights API. Light use works without a key;
if the API returns a quota error, set PAGESPEED_API_KEY. Needs live web access,
so it won't work on a saved copy of a site.
"""
import argparse
import json
import os
import sys
import urllib.parse
import urllib.request

API = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"


def run(url, strategy):
    params = [("url", url), ("strategy", strategy)]
    params += [("category", c) for c in ("performance", "accessibility", "seo", "best-practices")]
    key = os.environ.get("PAGESPEED_API_KEY")
    if key:
        params.append(("key", key))
    with urllib.request.urlopen(f"{API}?{urllib.parse.urlencode(params)}", timeout=120) as r:
        data = json.load(r)
    lh = data["lighthouseResult"]
    audits = lh["audits"]

    def disp(k):
        return audits.get(k, {}).get("displayValue")

    failing = [
        {"id": k, "title": a.get("title")}
        for k, a in audits.items()
        if a.get("score") is not None and a.get("score") < 0.9
        and a.get("scoreDisplayMode") in ("binary", "numeric")
    ]
    return {
        "url": url,
        "strategy": strategy,
        "scores": {k: round((v.get("score") or 0) * 100) for k, v in lh["categories"].items()},
        "largest_contentful_paint": disp("largest-contentful-paint"),
        "cumulative_layout_shift": disp("cumulative-layout-shift"),
        "total_blocking_time": disp("total-blocking-time"),
        "failing_checks": failing[:40],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--strategy", default="mobile", choices=["mobile", "desktop"])
    ap.add_argument("--out", default="-")
    a = ap.parse_args()
    try:
        out = json.dumps(run(a.url, a.strategy), indent=2)
    except Exception as e:  # noqa: BLE001
        print(f"PageSpeed check failed: {e}", file=sys.stderr)
        sys.exit(1)
    if a.out == "-":
        print(out)
    else:
        open(a.out, "w").write(out)


if __name__ == "__main__":
    main()
