# Deliverables

Paying clients get the fixes, not just the findings. Everything here should be usable as it is: copy-paste ready, in their voice, with their real details.

## Rewrites pack

Write in the business's own tone (match how they already talk: chatty café, calm clinic, no-nonsense trades), in British English.

- **Homepage headline + subheading**: what + who + where, plus a benefit. Offer 2 options.
- **Page titles** (around 50–60 characters) and **meta descriptions** (around 140–155 characters) for every page checked, as a table: page · current · suggested.
- **About text**: 120–200 words, using only facts from the site or the client. Don't invent history, awards or numbers. Where a strong detail is missing, add a short note suggesting what they could add ("If you have a favourite customer story, it would fit well here").
- **FAQ**: 8–12 questions real customers ask, with answers. Only answer from known facts. Where you don't know the answer (prices, policies), write the question with a note such as *"Answer needed: your current price for a 6-inch cake"*. This is a request to the client, not a placeholder in finished copy, so make it visibly different (italics, labelled).
- **Service descriptions**: for the top 2–4 services, 60–100 words each: who it's for, what happens, how long, price or "from" price if known.

## Business label code (structured data)

Fill in `assets/local-business-schema.json`:
- Use the most specific schema.org type that fits (`Bakery`, `Plumber`, `Physiotherapy`, `Dentist`, `Restaurant`; otherwise `LocalBusiness`).
- Include only facts you know. **Remove any field you can't fill** rather than leaving it blank or guessed.
- Validate it's well-formed JSON before saving (`python -m json.tool business-label.jsonld`).
- Tell the developer to paste it inside a `<script type="application/ld+json">` tag on the homepage, and to test it with Google's Rich Results Test and the Schema Markup Validator.

## llms.txt draft (optional)

A short Markdown file at the site root: an H1 with the business name, a one-paragraph summary in a blockquote, then sections linking to key pages with one-line descriptions. Label it in the report as **optional and low priority**, since few AI tools rely on it yet, so it's never sold as a fix.

## Week-by-week action plan

Turn every fix into an action, grouped by time:

- **This week**: quick wins with the biggest effect (unblocking AI crawlers, headline, phone number, page titles)
- **This month**: content work (FAQ, service pages, review requests, Google profile tidy-up)
- **Next 3 months**: bigger jobs (structured data, speed fixes, booking system, automation)

Each action gets a table row: **action · why · who** (**You can do this** / **Web developer** / **Canaries AI can help**) · **time** (rough) · **area**. Put the one next step first. Keep "This week" to 3–5 actions so it feels doable.

## Automation plan

2–4 automations, each with:
- **The problem** it solves, in their terms ("answering the same cake price emails")
- **What it does**: the tool *type* (online booking, form auto-reply, review request, chat assistant), with 1–2 common examples where helpful, without pushing any brand
- **Rough cost**: free / under £20 a month / more. Mark these as estimates; prices change.
- **Time it could save**, as a range ("roughly 1–3 hours a week"). Don't invent precise figures.
- **Effort to set up**: an afternoon / a few days / needs help
