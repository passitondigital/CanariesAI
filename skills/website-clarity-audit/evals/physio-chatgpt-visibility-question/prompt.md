---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Quick one - a client of mine runs Riverside Physio in Exeter. They reckon their site is pretty good but when they ask ChatGPT for "a sports physio in Exeter" they never come up. Here's what's on the site, can you work out why and what they should do?

Home page:
"Sports injury physiotherapy in Exeter. Get back to running, cycling and the sport you love. Book online today or call 01392 000000."
Book online button (uses an online booking system with text reminders).
Google rating 4.9 from 212 reviews shown with a link to Google.
Photos of the clinic and the team.

Treatments page: one long list - sports massage, injury rehab, acupuncture, running gait analysis, post-surgery rehab, pilates. No descriptions or prices.

About page: "Founded in 2015 by Priya Shah MCSP, HCPC registered." Team of 4 named physios with photos.

Footer: Riverside Physio Ltd, 12 Quay Road, Exeter EX2 4AN. Company no. 09999999. Privacy policy link.

There's no FAQ page. I checked the page source - the title is "Riverside Physio | Sports Physiotherapy Exeter" and there's no schema / structured data at all. robots.txt just has "User-agent: * Allow: /".
