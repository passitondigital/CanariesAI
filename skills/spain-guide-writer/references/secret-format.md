# Secret format

These match the fields in the Expat Legacy Secrets site's `secrets` table, so a draft can go straight into the admin page.

## Fields and how to write them

| Field | What it holds | Guidance |
|---|---|---|
| `title` | The reader's question | A real question in plain words, ideally under 70 characters. |
| `seoTitle` | Search title | Up to about 60 characters; include "Spain" or "Canary Islands" and the key term. |
| `metaDescription` | Search snippet | 140–160 characters; say who it's for and what they'll learn. |
| `keywords` | Search terms | 5–12, comma-separated in the site; include the Spanish term where readers search for it (e.g. "TIE", "empadronamiento"). |
| `category` | Topic area | Suggest one (e.g. Residency, Tax and money, Wills and inheritance, Health, Driving, Property, Scams and safety, Moving and settling in) for Sue to confirm. |
| `country` | Where it applies | "Spain", "Canary Islands" or "Spain (rules vary by region)". |
| `introduction` | Opening | 1–2 short paragraphs: why this matters to the reader, and what the guide covers. |
| *Who this applies to* | Who the guide is for | Goes at the start of `mainContent` as a `## Who this applies to` section: bullet list of who's affected, who isn't, and any regional, Canary Islands or UK-side differences. |
| `quickAnswer` | Direct answer | 2–4 short paragraphs answering the title, including "it depends" points. |
| `mainContent` | The guide | Markdown with `##` headings, short paragraphs and bullets. Start with "Who this applies to". Include "In the Canary Islands", "If you live in another region" and "The UK side" sections only where relevant. |
| `importantWarning` | The one thing worth remembering | 1–2 short paragraphs in a gentle tone, starting with "Remember…" or "Be aware…", usually about deadlines, scams, or when to get professional help. Show it on the page under a soft heading such as "Worth remembering". |
| `steps` | What to do | 4–10 complete sentences, in order, no bullet symbols. |
| `mistakes` | Common mistakes | 3–8 complete sentences, no bullet symbols. |
| `checklist` | Tick-list | 6–12 complete sentences, no bullet symbols. |
| `faqs` | FAQs | 4–8 items as `{"question": "...", "answer": "..."}`; real follow-up questions readers ask. |
| `furtherReading` | Related Secrets | 2–4 items as `{"title": "...", "url": "/secret/<slug>"}`, from the list below only. |
| `nextSecretId` | Read next | One `ELS-00NN` from the list below. |
| `officialSources` | Sources | Items as `{"title": "...", "publisher": "...", "url": "...", "checked": "YYYY-MM-DD", "confirms": "..."}`. Real pages actually checked only. |
| `summary` | Closing | 1–2 short paragraphs, ending with the reader's one next step. |
| `sueThoughts` | Sue's personal note | Always leave as an empty string. |

`steps`, `mistakes`, `checklist`, `faqs`, `furtherReading` and `officialSources` are stored as JSON arrays.

## `secret-draft.json` shape

```json
{
  "title": "",
  "seoTitle": "",
  "metaDescription": "",
  "keywords": "",
  "category": "",
  "country": "",
  "introduction": "",
  "quickAnswer": "",
  "mainContent": "",
  "importantWarning": "",
  "steps": [],
  "mistakes": [],
  "checklist": [],
  "faqs": [],
  "furtherReading": [],
  "nextSecretId": "",
  "officialSources": [],
  "summary": "",
  "sueThoughts": "",
  "status": "draft",
  "extras": {
    "promotion": {"linkedinPost": "", "facebookPost": "", "shortPost": "", "newsletterTeaser": "", "socialIdeas": [], "hashtags": []},
    "affiliateIdeas": [{"category": "", "where": "", "why": "", "decision": "For Sue to decide"}],
    "downloadableChecklist": {"title": "", "forWho": "", "items": []},
    "toVerify": [{"statement": "", "check": "", "where": ""}],
    "assumptions": [],
    "sourcesCheckedOn": ""
  }
}
```

Validate it's well-formed JSON before handing it over. Anything marked [To verify] in the text must also appear in `extras.toVerify`.

## Existing Secrets (for related links)

If the site's code is available, check `lib/existing-secrets.ts` for the latest list. Otherwise use this list (correct as of 27 November 2026). Only link to `published` ones.

| ID | Title | Slug |
|---|---|---|
| ELS-0001 | Do I Need a Spanish Will If I Live in Spain? | do-i-need-a-spanish-will-if-i-live-in-spain |
| ELS-0002 | What Should My Family Know If I Live Abroad? | what-should-my-family-know-if-i-live-abroad |
| ELS-0003 | What happens if I become seriously ill abroad? | what-happens-if-i-become-seriously-ill-abroad |
| ELS-0004 | What happens if an expat dies abroad? | what-happens-if-an-expat-dies-abroad |
| ELS-0005 | Who should have copies of my residency and identity documents? | who-should-have-copies-of-my-residency-and-identity-documents |
| ELS-0006 | What information will my family need to travel out and help me? | what-information-will-my-family-need-to-travel-out-and-help-me |
| ELS-0007 | How will my family access my property if I cannot help them? | how-will-my-family-access-my-property-if-i-cannot-help-them |
| ELS-0008 | Where to record my doctors, medication and insurance details? | where-to-record-my-doctors-medication-and-insurance-details |
| ELS-0009 | What happens to my overseas property when I die? | what-happens-to-my-overseas-property-when-i-die |
| ELS-0010 | Do I need wills in both countries? | do-i-need-wills-in-both-countries |
| ELS-0011 | What should be included in an expat emergency file? | what-should-be-included-in-an-an-expat-emergency-file |
| ELS-0012 | UK & Spanish Phone Scams Every Expat Should Know About | uk-spanish-phone-scams-every-expat-should-know-about |
| ELS-0013 | What should be included in a Canary islands expat medical file? | what-should-be-included-in-an-expat-medical-file |
| ELS-0014 | What should every Canary Island expat leave in an emergency folder? | what-should-every-expat-leave-in-an-emergency-folder |
| ELS-0015 | How Do I Choose the Right Town or Neighbourhood Abroad? | how-do-i-choose-the-right-town-or-neighbourhood-abroad |
| ELS-0016 | How Do I Choose the Right Country to Retire To? | how-do-i-choose-the-right-country-to-retire-to |
| ELS-0017 | Is Moving Abroad the Right Choice for Me? | is-moving-abroad-the-right-choice-for-me |
| ELS-0018 | Holiday Lets Are Concentrated in Just Nine Canary Islands Municipalities | holiday-lets-are-concentrated-in-just-nine-canary-islands-municipalities-what-does-this-mean-for-expats |
| ELS-0019 | High UV Levels in the Canary Islands | high-uv-levels-in-the-canary-islands-what-expats-and-visitors-need-to-know |
| ELS-0020 | Spanish Police Break Up €140 Million Cyber-Fraud Network | spanish-police-break-up-140-million-cyber-fraud-network-a-warning-for-expats |
| ELS-0021 | The Great Wealth Transfer Is Not Guaranteed | the-great-wealth-transfer-is-not-guaranteed-what-expat-families-need-to-understand |
| ELS-0022 | Digital Wallet Scams | digital-wallet-scams-how-one-telephone-call-can-give-criminals-access-to-your-money |
| ELS-0023 | Could You Retire Abroad Without Speaking Another Language? | could-you-retire-abroad-without-speaking-another-language-what-uk-retirees-should-consider |
| ELS-0024 | Spain's National Short-Term Rental Register Has Been Overturned | spain-s-national-short-term-rental-register-has-been-overturned-what-expats-buyers-and-property-owners-need-to-know |
| ELS-0025 | Where Are British People Moving Abroad? | where-are-british-people-moving-abroad-and-which-country-is-right-for-you |
| ELS-0026 | Canary Islands raises IGIC exemption threshold to €50,000 | canary-islands-raises-igic-exemption-threshold-to-50-000-what-aut-nomos-need-to-know |
| ELS-0027 | What Are the New Rules for Expats Living in Spain in 2026? | what-are-the-new-rules-for-expats-living-in-spain-in-2026 |
| ELS-0028 | How to Get Your TIE Number in Spain | tie-number-spain |
| ELS-0029 | Can You Drive in Spain with a UK Licence? 2026 Rules | uk-driving-licence-spain |
| ELS-0030 | Holiday Let Tax Rules in Spain | holiday-let-tax-spain |
| ELS-0031 | Living in Spain After Brexit: Legal Requirements *(draft, don't link)* | brexit-residency-spain |
| ELS-0032 | How to Open a Bank Account in Spain as a British Expat | bank-account-spain |
| ELS-0033 | The Expat Moving Checklist You Really Need | preparing-for-your-overseas-relocation-the-expat-moving-checklist-you-really-need |
| ELS-0034 | Received a Speeding Fine in Spain? | received-a-speeding-fine-in-spain-here-s-what-every-british-expat-needs-to-know |
| ELS-0035 | What Is Cl@ve? | what-is-clave-a-simple-guide-for-british-expats-in-spain |
| ELS-0036 | Do Official Documents Need Certified Translations in Spain? | do-official-documents-need-certified-translations-in-spain |
| ELS-0037 | UK Pension Inheritance Tax Changes: What to Review Before 2027 | uk-pension-inheritance-tax-changes-expats-spain-2027 |
| ELS-0038 | Digital Nomad Visa Spain: Which Documents Need Translation? | digital-nomad-visa-spain-which-documents-need-translation |
| ELS-0039 | Your First 72 Hours in Spain | your-first-72-hours-in-spain-how-to-arrive-calm-prepared-and-ready-to-settle-in |
| ELS-0040 | Do I need private health insurance for my visa? | do-i-need-private-health-insurance-for-my-visa |
| ELS-0041 | The Amazon "iPhone in Your Basket" Scam | the-amazon-iphone-in-your-basket-scam-what-you-need-to-know |
| ELS-0042 | Where Is the Cheapest Place to Buy a Home in the Canary Islands in 2026? | where-is-the-cheapest-place-to-buy-a-home-in-the-canary-islands-in-2026 |
| ELS-0043 | How do I deal with UK banks from overseas? | how-do-i-deal-with-uk-banks-from-overseas |
| ELS-0044 | Should You Buy Car Hire Excess Insurance Before You Travel? | should-you-buy-car-hire-excess-insurance-before-you-travel |
