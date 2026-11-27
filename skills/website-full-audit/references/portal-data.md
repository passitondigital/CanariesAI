# Portal data file (`audit-data.json`)

The client portal reads this file to show scores, track progress on each action, and compare audits over time. Software reads it, not a person, so follow the shape exactly: same field names, valid JSON, no comments.

```json
{
  "schema_version": "1.0",
  "audit_type": "full",
  "business": {
    "name": "Bramble Bakery",
    "website": "https://bramblebakery.example",
    "town": "Frome"
  },
  "audit_date": "2026-11-27",
  "pages_checked": ["/", "/our-story", "/shop", "/contact"],
  "scores": [
    {"area": "clarity", "label": "Clarity of message", "score": 4, "summary": "One sentence."},
    {"area": "ai_readiness", "label": "AI search & LLM readiness", "score": 2, "summary": "..."},
    {"area": "trust", "label": "Trust signals", "score": 4, "summary": "..."},
    {"area": "local_presence", "label": "Local presence", "score": 3, "summary": "..."},
    {"area": "mobile_speed_access", "label": "Mobile, speed & accessibility", "score": 5, "summary": "..."},
    {"area": "automation", "label": "Time-saving automation", "score": 3, "summary": "..."}
  ],
  "one_next_step": "Plain-English action.",
  "findings": [
    {
      "id": "F01",
      "area": "ai_readiness",
      "severity": "high",
      "page": "/robots.txt",
      "title": "ChatGPT and Claude are blocked from reading the site",
      "evidence": "robots.txt disallows GPTBot and ClaudeBot",
      "fix": "Remove the GPTBot and ClaudeBot Disallow lines."
    }
  ],
  "actions": [
    {
      "id": "A01",
      "finding_ids": ["F01"],
      "title": "Unblock AI crawlers in robots.txt",
      "timeframe": "this_week",
      "owner": "web_developer",
      "effort": "10 minutes",
      "status": "todo"
    }
  ],
  "deliverables": [
    {"type": "report", "file": "full-audit-report.md"},
    {"type": "structured_data", "file": "business-label.jsonld"}
  ],
  "not_checked": ["Competitor comparison: no web access during this audit"]
}
```

## Allowed values

- `area`: `clarity`, `ai_readiness`, `trust`, `local_presence`, `mobile_speed_access`, `automation`
- `severity`: `high` (costing them customers now), `medium`, `low`
- `timeframe`: `this_week`, `this_month`, `next_3_months`
- `owner`: `client`, `web_developer`, `canaries_ai`
- `status`: always `todo` in a new audit (the portal updates it later)
- `deliverables[].type`: `report`, `structured_data`, `llms_txt`, `rewrites`
- `scores`: all six areas in this order. Add `"partial": true` when part of an area couldn't be checked. If an area couldn't be checked at all, set `"score": null` (the portal shows "Not yet checked"); never invent a number.

Every action should link to at least one finding through `finding_ids`, and every high-severity finding should have an action. Check the file parses (`python -m json.tool audit-data.json`) before finishing.
