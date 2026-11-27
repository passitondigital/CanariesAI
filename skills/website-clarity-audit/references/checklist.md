# Audit checklist and scoring

Use this to decide what to look at and how to score. These are prompts for your judgement, not boxes to tick mechanically. A local café and an accountancy firm need different things, so weigh each point by how much it matters for *this* business and its customers.

## Scoring rubric (applies to every area)

| Score | Meaning |
|---|---|
| 9–10 | Excellent. Only small polish needed. |
| 7–8 | Good. A couple of clear improvements would help. |
| 5–6 | Mixed. The basics are partly there but some important gaps are costing them. |
| 3–4 | Weak. Several important gaps; visitors or AI tools are likely confused or put off. |
| 1–2 | Largely missing. |

If you couldn't check part of an area (e.g. from screenshots), score on what you could see and say so.

---

## 1. Clarity of message

The five-second test: imagine a stranger landing on the homepage from a search.

- **What** do they do? Is it stated in plain words in the main headline or just below, not hidden behind a slogan ("Passion meets excellence")?
- **Who** is it for? Homeowners, small businesses, families, dog owners?
- **Where**? Town, area or "UK-wide / online". This is essential for local businesses.
- **What next?** Is there one obvious call to action (call, book, get a quote) visible without scrolling? Is the phone number clickable on mobile?
- **Services and prices**: is it easy to find what they offer and roughly what it costs, or at least how pricing works?
- **Language**: written for customers, not insiders? Short sentences? Does it talk about the customer's problem, not only about the business?
- **Navigation**: a simple menu with obvious labels.

Good example rewrite pattern: *"[What you do] for [who] in [where]"*, e.g. "Friendly, fully insured boiler servicing for homes across South Bristol".

## 2. AI search visibility

AI assistants build their answers from text they can read and facts they can trust. Check:

- **Plain facts in text, not images**: business name, what they do, location/service area, opening hours, phone, email, all as real text. Text baked into images or logos is often invisible to these tools.
- **Consistency**: name, address and phone (often called "NAP") written the same way everywhere on the site.
- **Page title and meta description** (from raw HTML): does the homepage `<title>` say what and where (e.g. "Boiler Servicing in Bristol | Smith Heating"), or just "Home"?
- **Structured data**: is there a `LocalBusiness` (or more specific type, e.g. `Restaurant`, `Dentist`) JSON-LD block with name, address, phone, opening hours, and ideally `sameAs` links to their Google Business Profile and social profiles? Explain it to the owner as "a small hidden label that tells search engines and AI tools your key details in a format they can't misread".
- **FAQ content**: does the site answer the questions real customers ask ("Do you cover Clevedon?", "How much is a standard service?") in a question-and-answer format? This is one of the most useful things for AI answers.
- **Service pages**: does each main service have its own section or page with a clear description, rather than one long list?
- **About page**: who's behind it, how long they've traded, qualifications. AI tools and people both lean on this.
- **robots.txt**: does it block AI crawlers (e.g. `GPTBot`, `ClaudeBot`, `PerplexityBot`, `Google-Extended`) or everything (`Disallow: /`)? If so, flag it. If robots.txt is missing or permissive, that's fine.
- **Freshness**: obvious signs the site is abandoned (copyright 2019, an events page from years ago).

Be honest about uncertainty. Nobody fully controls what AI tools say, so frame advice as "making it easy for them to get it right", not as a guarantee. `llms.txt` files are not yet widely relied on; mention one only as a minor, optional extra, if at all.

## 3. Trust signals

- **Reviews and testimonials**: real names or initials, recent, ideally linked to Google or Trustpilot.
- **Real photos**: the actual team, premises and work, not only stock images.
- **Credentials**: relevant accreditations, memberships, insurance, registrations (e.g. Gas Safe, a professional body), shown where relevant to the trade.
- **Contact details**: a phone number, a physical address or service area, and a named person, not just a contact form.
- **Policies**: privacy policy, and where relevant terms, cancellation or refund policy.
- **Pricing transparency**: prices, "from" prices or a clear explanation of how quotes work.
- **Security and polish**: the site loads over https, has no broken links or placeholder text ("Lorem ipsum") and works on mobile.
- **Company details**: for limited companies, the registered company name and number are usually expected on the website. Mention it gently if it's clearly absent.

## 4. Time-saving automation

Look for clues about where the owner spends time on repetitive tasks, then suggest 2–3 simple, affordable fixes. Typical clues and ideas:

| Clue on the site | Idea |
|---|---|
| "Call to book", no online booking | Online booking or appointment tool with automatic reminders |
| Contact form only, no reply promise | Auto-reply email confirming receipt, setting expectations and answering top FAQs |
| Same questions likely asked repeatedly | An FAQ page; optionally a simple website chat assistant trained on those answers |
| "Request a quote" with no detail | A quote form that collects the details needed up front (photos, postcode, job type) |
| No review link | Automatic follow-up email after a job asking for a Google review |
| Newsletter mentioned but rarely sent | A simple monthly email template |

Score this area on how much easy time-saving is already in place (10 = they already use sensible tools, 3 = everything seems manual). Give a rough sense of time saved ("could save a few hours a week answering the same questions") but don't invent precise figures.
