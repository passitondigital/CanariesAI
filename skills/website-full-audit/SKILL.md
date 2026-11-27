---
name: website-full-audit
description: Run the full, paid Canaries AI website audit for a paying client. It checks up to 20 pages for clarity, AI search and LLM readiness, trust, local presence (Google Business Profile and directory listings), mobile, speed, accessibility and usability, and time-saving automation, and compares the site with local competitors. It delivers a scored report, paste-ready rewrites, business label (structured data) code, a week-by-week action plan, an automation plan and a portal-ready data file. Use this whenever the user asks for a full, paid, complete, in-depth or premium website audit, review or report for a client or customer, or mentions a client portal audit, even if they don't say "full". For a free taster, mini audit or prospect check-up, use the website-clarity-audit skill instead.
---

# Website Full Audit (paid)

This is Canaries AI's paid audit. The free taster (the `website-clarity-audit` skill) diagnoses; this one **diagnoses and hands over the fixes**. A paying client should finish reading it knowing exactly what to do this week, with the wording and code ready to use.

The reader is the **business owner**: busy, not technical, and paying for this. Write warmly, in clear **British English** (organise, colour, enquiry; £), with no unexplained jargon. When a technical term is unavoidable, explain it in a short phrase the first time ("structured data, a hidden label that tells search engines your key details"). Technical detail meant for their web developer goes in clearly marked "For your web developer" boxes or the appendix, so the owner can skip it.

## Step 1: Intake (ask before you start)

The rewrites, competitor comparison and listings check only work with real details, so before any analysis check you have:

1. **Business name** and **website** (address, saved HTML folder, or pasted text)
2. **Town or area** they serve
3. **Main services or products**, and which ones make the most money or they most want more of
4. **Their goal**: more calls, more bookings, fewer time-wasting enquiries, and so on
5. **Competitors**: 2–3 local businesses they see as rivals (optional; you'll find some if they don't know)

Take whatever the website and the user have already told you, then ask for the rest in **one short message**. Never use placeholders like "[your town]" in the deliverables. If the user doesn't know something, work around it and say so.

## Step 2: Gather the evidence

**Crawl the site** with the bundled script. It works on a live address or a folder of saved HTML files, checks up to 20 pages, and also picks up robots.txt, sitemap.xml and llms.txt:

```bash
python <skill-dir>/scripts/crawl_site.py <url-or-folder> --max-pages 20 --out crawl.json
```

Read `crawl.json`, then read the full text of the 4–6 most important pages (home, services, about, contact, FAQ, top service pages) yourself. The script gives you facts; your judgement comes from reading the pages like a customer would. If the client has more than 20 pages, prioritise pages that bring in customers, and say in the report which pages were and weren't checked.

**Mobile, speed and accessibility scores** (live sites only):

```bash
python <skill-dir>/scripts/pagespeed.py <homepage-url> --out speed.json
```

Run it on the homepage and one key service page. If it fails or there's no web access, fall back to what the crawl shows (missing image descriptions, unlabelled form fields, missing mobile viewport setting, heading structure) and say the speed test wasn't run.

**Competitors and listings** need web search. See `references/competitors-and-listings.md` for exactly what to look up.

If something can't be checked (no web access, a site that blocks bots, screenshots only), **say so in the report's "What I couldn't check" section**. Never present a guess as a finding. A paying client may act on every line, so accuracy matters more here than in the taster.

## Step 3: Assess and score

Read `references/checklist.md`. It covers all six scored areas, the scoring rubric and what to look for. The areas are:

1. Clarity of message
2. AI search & LLM readiness
3. Trust signals
4. Local presence (Google & listings)
5. Mobile, speed & accessibility
6. Time-saving automation

Score each out of 10, backing every score with specific evidence: quote the headline, name the page, give the number.

The first four areas use the same names and rubric as the taster, so a client who had a taster sees how their scores have moved.

## Step 4: Produce the deliverables

Read `references/deliverables.md` for how to write each one:

- **Rewrites pack**: paste-ready headline, page titles, meta descriptions, About text and FAQ answers
- **Business label code**: filled-in structured data from `assets/local-business-schema.json`
- **llms.txt draft**: optional, clearly flagged as a low-priority extra
- **Week-by-week action plan**: every fix, each marked "You can do this" or "Web developer"
- **Automation plan**: tool types, rough costs, hours saved

Then write **`audit-data.json`** for the client portal, following `references/portal-data.md` exactly, because a portal will read it automatically.

## Step 5: Write the report

Use this structure. Aim for about 8–12 pages; depth is what they're paying for, but every line should earn its place.

```markdown
# Full website audit: [Business name]

*Prepared by Canaries AI · [date] · [website] · [N] pages checked*

## Summary
[Score table: six areas, score, one sentence each. Then 3–4 sentences: the overall picture, the biggest opportunity, and what the first week looks like.]

## Your one next step
**[The single most valuable action this week.]** [Why, how long, what to expect.]

## 1. Clarity of message — x/10
## 2. AI search & LLM readiness — x/10
## 3. Trust signals — x/10
## 4. Local presence: Google & listings — x/10
## 5. Mobile, speed & accessibility — x/10
## 6. Time-saving automation — x/10
[Each: **What's working** · **What to improve** (specific evidence → why it matters to them → the fix, pointing to the rewrites pack where relevant) · optional **For your web developer** box]

## How you compare locally
[Competitor table and 3–4 lessons. See references/competitors-and-listings.md]

## Page-by-page notes
[Table: page · main issue · fix · priority. Every page checked, one row each.]

## Your action plan
[From deliverables.md: This week / This month / Next 3 months]

## Your automation plan
[From deliverables.md]

## Ready-to-use rewrites
[The rewrites pack]

## Appendix: for your web developer
[Business label code, robots.txt changes, llms.txt draft, accessibility fixes in technical terms]

---
*What I couldn't check: [...]*
*Questions about anything in this audit? Reply here or message us in your Canaries AI portal.*
```

The one next step goes near the top on purpose. Owners who read only the first page should still know what to do.

## Step 6: Save the files

Save these files in a folder named after the business (e.g. `full-audit-bramble-bakery/`):
- `full-audit-report.md`: the report
- `audit-data.json`: the portal data
- `business-label.jsonld` and, if drafted, `llms.txt`

Tell the user where the files are, and give a 3–4 line summary in the chat: scores, the biggest finding and the one next step.
