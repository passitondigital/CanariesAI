# Full audit checklist and scoring

Use judgement, not box-ticking: weigh each point by how much it matters for *this* business and its customers.

## Scoring rubric (every area)

| Score | Meaning |
|---|---|
| 9–10 | Excellent. Only polish needed. |
| 7–8 | Good. A couple of clear improvements would help. |
| 5–6 | Mixed. Important gaps are costing them. |
| 3–4 | Weak. Visitors or AI tools are likely confused or put off. |
| 1–2 | Largely missing. |

If part of an area couldn't be checked, score on what you could and say so.

---

## 1. Clarity of message
*(The same as the taster, applied across every page checked.)*
- Five-second test on the homepage: **what** they do, **who** it's for, **where**, and **what next**, in plain words, not a slogan.
- One obvious call to action above the fold; a clickable phone number on mobile.
- Services and prices are easy to find, or how quotes work is explained.
- Each key page has one clear purpose and one clear H1 (main heading).
- Customer-focused language: their problem first, short sentences.
- Simple navigation; no dead ends, "coming soon" pages or empty sections.

## 2. AI search & LLM readiness
AI assistants (ChatGPT, Claude, Perplexity, Gemini, Google AI Overviews) answer questions using text they can read and facts they can trust. Check:

**Can they read it?**
- robots.txt: are AI crawlers blocked? `crawl.json → robots_summary.ai_crawlers_blocked`. Note that `Google-Extended` only controls use in Google's AI training and Gemini, not normal Google Search.
- Is the important content in the page HTML as text? A low `word_count` on a page that looks full in a browser suggests content loaded by JavaScript, or text inside images, which many AI crawlers can't see.
- Key facts as text, not inside images (logos, banners).

**Can they understand it?**
- Page titles and meta descriptions say what and where, uniquely per page.
- Clean heading structure: one H1 per page, logical H2s.
- Structured data: a `LocalBusiness` (or specific subtype) block with name, address, phone, opening hours, `areaServed`, `sameAs` links. FAQ pages can carry `FAQPage` markup.
- Consistent name, address and phone on every page.

**Can they answer questions with it?**
- An FAQ page answering real customer questions in plain question-and-answer form. This is one of the highest-value fixes.
- A dedicated page or section per main service, describing who it's for, what happens and the price or price range.
- An About page with real people, credentials and history.
- Up-to-date content (copyright year, recent news or offers).

**Extras (low priority, mention honestly)**
- `llms.txt`: a proposed, not widely adopted, standard for giving AI tools a plain summary of a site. Cheap to add, but don't oversell it.

Frame everything as "making it easy for AI tools to get it right". Nobody can guarantee recommendations.

## 3. Trust signals
- Reviews: number, recency, rating, linked to Google or Trustpilot; shown on key pages.
- Real photos of the people, premises and work.
- Credentials relevant to the trade (Gas Safe, HCPC, professional bodies, insurance), ideally with verifiable numbers.
- Contact details: phone, address or service area, a named person.
- Policies: privacy policy (required if the site collects personal data through forms), plus terms, cancellation or refunds where relevant.
- For limited companies: registered company name and number, registered office address.
- https; no broken links, placeholder text or "coming soon" pages.

## 4. Local presence: Google & listings
See `competitors-and-listings.md` for how to check.
- Google Business Profile exists, is claimed, and has the correct category, hours, photos, website link and recent reviews, with replies.
- Name, address and phone **match exactly** across the website, Google and main directories.
- Present on the 2–4 directories that matter for this trade (e.g. Checkatrade or TrustATrader for trades, TripAdvisor for hospitality, Treatwell for beauty, NHS or professional registers for health).
- Social profiles linked from the site and active.

## 5. Mobile, speed & accessibility
Use `speed.json` where available, plus the crawl data.
- **Mobile**: viewport setting present (`has_viewport_meta`), tap-to-call phone, buttons big enough to tap, no sideways scrolling.
- **Speed**: PageSpeed mobile performance score; largest contentful paint (aim for under 2.5s). Big unoptimised images are the usual culprit for small business sites.
- **Accessibility** (also good for AI readability):
  - images have meaningful descriptions (alt text). `images_missing_alt` means none at all; an empty alt is fine for purely decorative images but not for photos that carry meaning.
  - form fields have labels, not just placeholder text (`forms[].fields_with_labels` < `fields`)
  - one H1 per page and headings in order
  - page language set (`lang`)
  - readable text size and colour contrast (from the PageSpeed accessibility checks)
  - link text that makes sense out of context (not "click here")
- **Usability**: is it easy to complete the main task (book, call, buy, enquire) in three taps or fewer?

Explain accessibility as both the right thing to do and good business: around 1 in 4 UK adults has a disability, and older customers benefit too.

## 6. Time-saving automation
Look for clues to repetitive work, then build the automation plan (see `deliverables.md`).

| Clue | Idea |
|---|---|
| "Call to book" only | Online booking with reminders |
| Contact form with no reply promise | Auto-reply that confirms, sets expectations and links to the FAQ |
| Repeated questions likely | FAQ page; optionally a website chat assistant trained on it |
| Vague quote requests | Structured quote form (postcode, job type, photos, urgency) |
| No review requests | Automatic post-job review request |
| Manual invoicing or reminders | Accounting tool with automatic invoices and payment reminders |

Score on how much sensible automation is already in place.
