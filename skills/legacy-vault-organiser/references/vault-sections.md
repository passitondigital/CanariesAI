# Legacy Vault Kit: pillars, sections and fields

This mirrors `shared/vaultConfig.ts` in the legacy-vault-kit codebase (checked 27 November 2026). If that file is available, check it for changes. Use these section names in the vault-ready record so people can copy entries straight across. "List" means the section holds several entries of that kind.

Suggested order for a first session: **Emergency info → Contacts → Personal identity → Important documents**, then whatever matters most to them.

## Pillar 1: Essentials

**Personal identity** (`personal_identity`)
- Full name; date of birth; country of residence
- Nationalities (list)
- Passports (list): country, passport number, expiry date, where stored, notes
- National IDs (list): ID type (NIE, TIE, DNI, UK national insurance…), country, ID number, where stored, notes
- Driving licences (list): country, licence number, expiry date, where stored

**Emergency info** (`emergency_info`)
- Blood type
- Allergies (list): allergy, severity, notes
- Medications (list): name, dosage, frequency, prescribing doctor, pharmacy
- Medical conditions (list): condition, date diagnosed, treating doctor, notes
- Emergency contacts (list): name, relationship, phone, email
- GP name and phone

**Contacts** (`contacts`)
- Trusted persons (list): name, relationship, phone, email, what they're trusted to do
- Solicitors (list), accountants (list), financial advisers (list): name, firm, phone, email, country, notes
- Executors (list): name, relationship, phone, email, notes

**Important documents** (`important_documents`)
- Where documents are stored; safe location; document notes

## Pillar 2: Financial

**Money and property** (`money_property`)
- Bank accounts (list): bank name, account type, account number (the vault form calls this field "last 4 digits"; record full numbers only if the person chooses), country, online banking (yes/no, *not* the login), notes
- Savings and investments (list): provider, type, reference, country, notes
- Pensions (list): provider, type, reference, country, notes
- Properties (list): address, country, ownership, mortgage provider, where the deeds are, notes
- Loans and debts (list): lender, type, approximate balance, monthly payment, notes

**Legal and estate** (`legal_estate`)
- Wills (list): country, date made, where the original is, solicitor or notary, notes
- Powers of attorney (list): type, country, attorney's name, where stored, notes
- Trusts; notes

**Income and benefits** (`income_benefits`)
- Employment (list); state pensions (list); benefits (list); other income

**Utilities and household** (`utilities_household`)
- Utilities by property (list); insurance policies (list: home, life, travel, funeral plan…); other contracts

**Vehicles** (`vehicles`)
- Vehicles (list); breakdown cover (list)

**Living abroad** (`living_abroad`)
- Country of residence; residency permit (TIE / certificate); foreign ID number (NIE); domicile country; local registration (padrón); tax residency; double tax treaty notes; inheritance tax notes
- Local will; EU succession declaration (choice of law); overseas properties (list); overseas bank accounts (list); foreign pensions (list)
- Repatriation insurance; consulate contact; local funeral director; apostille notes; who to call first abroad; local professional (gestor, abogado); language support; local power of attorney

## Pillar 3: Digital

**Health and care** (`health_care`)
- Medical history; care preferences; advance decisions (e.g. Canary Islands MAV, Spanish *instrucciones previas*, UK advance decision)
- Prescriptions (list); healthcare providers (list: name, role, clinic, phone, country)
- Health insurance (list): provider, policy number, emergency helpline, country covered, renewal date; S1 form
- EHIC / GHIC cards (list): card type, number, expiry, holder; local doctor abroad

**Password vault** (`password_vault`): *hints only*
- Password manager used; master password **hint**; where it's stored
- Login records (list): service, username or email, password **hint**, two-factor method, recovery info, notes

**Online accounts** (`online_accounts`)
- Email accounts (list); social media (list); subscriptions (list); wishes for each (close, memorialise, keep)

**Digital legacy** (`digital_legacy`)
- Domain names (list); crypto wallets (where the recovery details are kept, never the phrase itself); digital assets; instructions

## Pillar 4: Heart

**Funeral wishes** (`funeral_wishes`)
- Burial or cremation; location; music; ceremony preferences; readings; other wishes; country (where the funeral would happen)

**Memories and voice** (`memories_voice`)
- Life story; favourite memories; values and lessons; message to family (voice notes can be recorded in the vault)

**Time capsules** (`time_capsules`)
- Up to two capsules: recipient, date to open, message

**Bereavement checklist** (`bereavement_checklist`)
- Immediate steps; who to notify; accounts to close; special instructions

**Calendar reminders** (`calendar_reminders`)
- Renewal dates; important dates; deadlines

**Favourite recipes** (`favourite_recipes`)
- Recipe name; ingredients; instructions; dietary notes; cooking tips
