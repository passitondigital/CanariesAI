---
name: spain-guide-writer
description: Write a trustworthy Expat Legacy Secrets guide (a "Secret") for English-speaking people aged 50+ moving to or living in Spain, including the Canary Islands. It checks official sources, says exactly who each rule applies to, flags Canary Islands, regional and UK differences, and marks anything unverified. It delivers an editable document plus a site-ready draft in the Secret fields, with promotion copy, related Secrets, affiliate ideas and a printable checklist. Use this whenever Sue asks for a guide, Secret, article, explainer or blog post about living in, moving to, retiring in or planning for later life in Spain, on topics such as residency, the TIE, NIE, Cl@ve, tax, IGIC, pensions, wills, inheritance, healthcare, driving, banking, property, scams or paperwork. Also use it for turning news about a Spanish or UK rule change into a guide for expats, even if she doesn't say "guide".
---

# Spain guide writer (Expat Legacy Secrets)

Expat Legacy Secrets publishes numbered guides called **Secrets** (ELS-0001 onwards) at expatlegacysecrets.com. Readers are **English-speaking people aged 50+**, mostly British, moving to, living in or planning their later life in Spain. Many live in the Canary Islands. They're often making serious decisions about residency, tax, wills and health, sometimes for a partner or parent, and they trust Sue to be careful.

So accuracy and honesty come before everything else. A guide that's slightly less complete but never wrong is worth far more than a confident one that gets a deadline wrong. Rules here also change often, and they genuinely differ depending on who you are and where you live. Saying **who a rule applies to** is part of the answer, not a footnote.

## Step 1: Pin down the brief

From Sue's request, work out:
- **The question** the guide answers. Secrets are usually titled as a real reader's question ("Do I need a Spanish will if I live in Spain?").
- **Who it's for**: which readers this affects most (residents, people planning a move, holiday-home owners, retirees, workers, autónomos, families of expats).
- **Where**: all of Spain, the Canary Islands or a particular region.
- **Any links, notes or news** Sue has supplied. Treat these as leads to check, not as facts.

Only ask Sue if the topic itself is unclear. Otherwise make sensible assumptions, state them at the top of the draft, and get on with it.

## Step 2: Research official sources

Read `references/official-sources.md` for which authorities to check for each topic.

- Base every rule, fee, deadline, threshold and eligibility condition on an **official source**: Spanish government, Canary Islands or regional government, BOE, Agencia Tributaria, Seguridad Social, DGT, Policía Nacional, GOV.UK, HMRC, DVLA, and the like. News sites, forums and law firm blogs can point you to a change, but confirm it at the official source before stating it.
- Record each source as you go: the page title, URL, who publishes it, and the date you checked it. Note the date the page was last updated if it shows one.
- Prefer the official source's own wording for anything legal, and put a plain-English explanation alongside it.

**If you can't reach a source** (no web access, a page won't load, or it's only in Spanish and unclear), keep writing, but mark that statement **[To verify: what to check and where]** and add it to the verification list. Never fill a gap with a remembered figure presented as fact. Many rules have changed since Brexit and keep changing, and an out-of-date fee or deadline could cost a reader money.

## Step 3: Work out who it applies to

Before writing, sort out the "it depends" layers, because these are what generic articles get wrong:

1. **The person**: UK nationals resident before 1 January 2021 (Withdrawal Agreement, TIE) versus those who arrived later (third-country rules, visas), plus visitors (90/180 days), retirees (non-lucrative visa), workers and autónomos, property owners who aren't resident, and EU or dual nationals where it differs.
2. **The place**: is it national, or does it vary by **autonomous community**? Regions set their own rates or reliefs for some taxes (inheritance and gift tax, some income tax, property transfer tax), and services such as healthcare and some registrations are run regionally.
3. **The Canary Islands**: flag where they differ. IGIC replaces IVA, there are different customs and import rules for goods, Canary Islands tax agency (ATC) procedures, regional health service (SCS) processes, and island-specific offices and appointments.
4. **The UK side**: what still applies from the UK, such as UK State Pension and uprating, HMRC residence and the double taxation treaty, UK inheritance tax and domicile/long-term residence rules, UK bank accounts, DVLA licences and the UK government's "Living in Spain" guidance.

Only include the layers that genuinely matter for this topic. A guide about sunscreen doesn't need a tax-residency box.

## Step 4: Write the guide

Read `references/secret-format.md` for the exact fields, lengths and rules. In short, each Secret has: an SEO title and meta description, keywords, an introduction, a **Who this applies to** box, a quick answer, the main content, an important warning, steps, common mistakes, a checklist, FAQs, official sources, related Secrets, a summary, and a blank **Sue's thoughts** field.

Voice: **calm, warm, trustworthy British English** in plain language, written like a knowledgeable friend who's been through it.

- Short sentences and paragraphs. Readers may be on a phone or using a screen reader.
- Explain Spanish terms the first time (empadronamiento, the "padrón", your town hall registration) and keep the Spanish word, because that's what readers will see on forms.
- Give reassurance through clarity, not by playing down risk. Never use fear-based language ("you could lose everything!").
- Never invent experiences, quotes or opinions for Sue, and leave **Sue's thoughts** empty for her.
- Treat legal, tax, residency, financial and healthcare content as general information. Say where a reader's situation means they should speak to a qualified professional (an abogado, gestor, asesor fiscal, notary or UK financial adviser), and say what kind.
- End with **one manageable next step** for the reader.

## Step 5: Add the extras

- **Promotion copy**: a LinkedIn post, a Facebook post, a short post (under 280 characters), a newsletter teaser, 3–5 social ideas and up to 10 hashtags. Keep it accurate to the guide, with no overpromising and no fear hooks.
- **Related Secrets**: 2–4 existing Secrets to link to, and one to read next, chosen from `references/secret-format.md`. Only link to Secrets on that list, and never invent a slug.
- **Affiliate ideas**: where a recommended supplier would genuinely help the reader, suggest the **supplier category** that fits (Legal and residency; Wills and inheritance; Tax and financial planning; Private healthcare and insurance; Property and relocation; Home and lifestyle services) and where in the guide it would sit naturally. Mark each one "For Sue to decide". Don't name a specific company unless Sue has named it in this chat, because partner agreements change.
- **Downloadable checklist**: a one-page printable version (title, who it's for, 8–15 tick-box items in order, and a line reminding readers to check current rules at the official sources listed in the guide).

## Step 6: Deliver it

Give Sue two things:

1. **An editable document for review.** If the Claude Docs tools are available, create a doc titled with the Secret's question. Otherwise write a Markdown file. Lay it out as the reader will see it, followed by the extras, then a **Before publishing** section containing:
   - the **verification list**: every [To verify] item, what to check and where
   - the assumptions made in Step 1
   - the date the sources were checked
2. **A site-ready draft**: `secret-draft.json` in the shape given in `references/secret-format.md`, so it can be pasted or imported into the admin page once Sue approves it. Leave `secretNumber`, `slug` and `status` for Sue (status stays `draft`).

Finish with a short chat summary covering who the guide is for, how many sources were checked, how many items still need verifying, and one suggested next step for Sue (usually "check the 3 items in the verification list").

Never mark a guide as ready to publish while anything is still marked [To verify].
