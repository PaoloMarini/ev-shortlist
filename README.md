# EV Shortlist Dashboard

Private single source of truth for choosing the next EV.

The repo now supports **Option C**: structured vehicle data plus a static dashboard that can be updated by ChatGPT/Codex and reviewed in GitHub.

## Current decision rules

### Non-negotiables

- **Tesla is excluded.**
- **Kia is not a live candidate**, but the Kia EV6 GT remains the benchmark/reference point.
- Chinese-brand cars are **not automatically excluded** anymore, but quality, support, software, safety and security evidence must be stronger than normal.
- Subscription-gated hardware features are a serious red flag, especially comfort features such as heated seats.
- A repeat of the stolen EV6 experience is unacceptable: theft resistance, key security, tracking/immobilisation options and insurance implications are first-class criteria.

### What matters most

1. Sound/audio quality and cabin noise isolation.
2. Strong performance, ideally with comfort-oriented suspension/drive modes for normal driving.
3. Comfort and ride configurability.
4. Integrated dashboard design, not a tablet stuck on the dash.
5. Useful physical controls for core functions.
6. Flawless mobile phone integration: CarPlay/Android Auto/Bluetooth/app/key behaviour must be reliable.
7. Premium feel, build quality and long-term confidence.
8. Range, charging curve and real-world practicality.
9. Salary-sacrifice value versus the EV6 GT benchmark.
10. Software/ADAS annoyance factor.

## Structure

```text
docs/
  index.html              Static dashboard entry point
  app.js                  Dashboard logic
  styles.css              Dashboard styling
  data/
    vehicles.json         Authoritative vehicle data for the dashboard
    criteria.json         Criteria, weights and red-flag definitions
    change-log.json       Human-readable update history
notes/
  security-and-theft.md   Security-specific notes and evaluation checklist
prompts/
  weekly-update.md        Prompt for the Friday market refresh
shortlist.csv             Legacy flat master table retained for continuity
shortlist.md              Legacy human-readable table retained for continuity
```

## Operating model

Every vehicle has one status:

- `benchmark` — not a candidate, used for comparison.
- `shortlist` — serious candidate.
- `watchlist` — interesting, but waiting for price, launch, reviews, NCAP, lease data or reliability evidence.
- `research` — mentioned but not yet assessed properly.
- `rejected` — considered and ruled out, with reason.

Each weekly update should:

1. Check UK pricing, lease/salary-sacrifice availability, trims and launch timing.
2. Check reviews for sound quality, ride, dashboard/controls, software, phone integration and ADAS behaviour.
3. Check safety and security: Euro NCAP, theft/keyless-entry concerns, tracker/immobiliser options and insurance notes.
4. Update scores only when there is evidence. Unknowns should stay `null`/`TBD` rather than being guessed.
5. Add a change-log entry explaining what moved and why.

## Publishing

The dashboard is designed to work as a GitHub Pages static site from the `/docs` folder.

Keep the repo private until the data and notes are clean enough to expose publicly. If publishing later, review for personal lease costs, notes about theft/security, and anything that should remain private.

## Accuracy rule

Prefer a blank, `null`, `TBD` or `unknown` value over fake precision. The dashboard should make uncertainty visible rather than hide it.
