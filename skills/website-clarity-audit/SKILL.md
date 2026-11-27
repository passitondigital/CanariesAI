---
name: website-clarity-audit
description: Audit a small business website for Canaries AI and write a warm, plain-English scored report for the business owner, covering clarity of message, AI search visibility (ChatGPT, Claude, Perplexity, Google AI answers), trust signals and simple time-saving automation ideas, ending with one manageable next step. Use this whenever someone shares a website address, pasted page copy or screenshots and asks for a review, audit, health check, feedback, "what's wrong with my site", "why don't we show up in ChatGPT", "how can we get more enquiries" or similar, even if they don't say "audit". Also use it when preparing a free taster or mini website review for a Canaries AI prospect. This is the free taster; for a full, paid or in-depth audit for a paying client, use the website-full-audit skill instead.
---

# Website Clarity Audit (free taster)

You are writing on behalf of Canaries AI, which helps small businesses make their websites clearer, become easier for AI search tools to find and recommend, and save time through simple automation.

The reader is the **business owner**: often a sole trader or a small team (a plumber, a café, a physio, an estate agent, a holiday let). They are busy, not technical, and possibly a little anxious about their website. The report has to feel like advice from a friendly expert who's on their side, not a telling-off from a machine.

## Workflow

### 1. Gather the website

The input will be either a web address or pasted text/screenshots.

**If you have a URL**, look at:
- the homepage
- up to 3–4 key pages linked from the main menu: usually About, Services (or Menu/Prices), Contact, and FAQ if there is one
- `/robots.txt`
- the raw HTML of the homepage, to check the page title, meta description and any structured data (`<script type="application/ld+json">`)

Prefer fetching raw HTML (e.g. `curl -sL`) for the technical checks, because page-summarising fetch tools often strip out the title, meta tags and structured data. Use a summarising fetch for reading the copy if that's easier.

**If you have pasted text or screenshots**, work from what you've been given. Some checks (structured data, robots.txt, page titles) can't be done from screenshots, so list them as "not checked" rather than guessing. Never claim something is missing just because you couldn't see it.

If the site won't load or blocks you, say so plainly and ask for the page text or screenshots instead.

**Check you have the key facts before writing.** The example rewrites (headlines, page titles, service-area lines) are the most useful part of the report, and they only work if they contain the business's real details. If any of these is missing from the website *and* from what the user told you, stop and ask the user before writing the report:
- the town or area the business is based in or covers
- the business name, if it isn't clear

Ask in one short message, e.g. "Before I write this up, which town or area does DJ Plumbing cover? It isn't on the site, and I'd like the example headline to use it." Never fill the gap with a placeholder like "[your town]". A report full of blanks looks unfinished and can't be sent to the owner as it is. If the user doesn't know, write the rewrites without the location rather than with a placeholder, and say that adding it is part of the fix. The same goes for smaller details such as a phone number in a sample auto-reply: word the example so it reads naturally without it ("For emergencies, just give us a ring") rather than leaving a blank.

The facts being missing from the site is still a finding: report it under clarity and AI visibility, even once the user has told you the answer.

### 2. Assess the four areas

Read `references/checklist.md` for what to look at in each area and how to score it. In short:

1. **Clarity of message**: can a stranger tell within five seconds what the business does, who it's for, where it is and what to do next?
2. **AI search visibility**: could ChatGPT, Claude, Perplexity or Google's AI answers understand the business well enough to describe and recommend it accurately?
3. **Trust signals**: does the site give a cautious visitor enough reasons to believe it's a real, reputable business?
4. **Time-saving automation**: where is the owner probably spending time on things a simple tool could handle?

Score each area out of 10 using the rubric in the checklist. Base every point on something specific you actually saw (quote the headline, name the page). Specific evidence is what makes the report credible and useful. Generic advice that could apply to any website is what makes owners stop reading.

### 3. Pick the one next step

Of everything you found, choose the **single change that would make the biggest difference for the least effort**. Usually that's a clarity fix (rewriting the homepage headline, adding a phone number above the fold) rather than something technical. Owners act on one clear task and freeze when given twelve, so this choice matters more than any other part of the report.

### 4. Write the report

Use the template below. Write in warm, clear **British English** (organise, colour, enquiry, favourite; £ for prices unless the business clearly uses another currency).

Tone guidance:
- Start every area with what's genuinely working, so the owner knows what to keep.
- Explain *why* each fix matters in terms the owner cares about (more calls, fewer time-wasting enquiries, showing up when someone asks ChatGPT for "a good dog groomer in Bristol").
- Avoid jargon. If you must use a technical term (like "structured data"), explain it in one short phrase the first time.
- Where a rewrite would help, offer an example. A suggested headline is worth more than "make your headline clearer".
- Be honest but kind. Don't inflate scores to be nice, and don't pile on.
- Keep it to roughly 2–3 pages. Pick the most important 2–4 fixes per area rather than listing everything.

## Report template

```markdown
# Website check-up: [Business name]

*Prepared by Canaries AI · [date] · [website address, or "based on the pages you shared"]*

## At a glance

| Area | Score | In a sentence |
|---|---|---|
| Clarity of message | x/10 | ... |
| AI search visibility | x/10 | ... |
| Trust signals | x/10 | ... |
| Time-saving ideas | x/10 | ... |

[Two or three sentences summing up the overall picture warmly and honestly.]

## 1. Clarity of message — x/10

**What's working**
- ...

**What to improve**
- **[Short fix title].** [What you saw, why it matters, what to do. Include an example rewrite where useful.]

## 2. AI search visibility — x/10

[Same structure. One sentence early on explaining that more people now ask AI assistants for recommendations, and these tools can only recommend what they can clearly understand.]

## 3. Trust signals — x/10

[Same structure.]

## 4. Time-saving ideas — x/10

[Same structure, but "What to improve" becomes "Ideas to try": 2–3 simple, affordable automations with a rough idea of the time saved. Name common tool types (online booking, an enquiry form that sends an auto-reply) rather than pushing one brand.]

## Your one next step

**[The single action, stated plainly.]**

[Two or three sentences: why this one first, roughly how long it takes, and what difference to expect.]

---

*Anything I couldn't check: [list items not checked and why, or remove this line if everything was checked].*

*Want a hand with any of this? Canaries AI can help. Just reply to this report.*
```

## Saving the report

If you have a filesystem, save the report as a Markdown file named after the business (e.g. `website-check-up-bramble-bakery.md`) and tell the user where it is. Otherwise, give the report in the chat.
