# Weekly EV shortlist update prompt

Run this every Friday evening.

## Objective

Refresh the EV shortlist dashboard in `PaoloMarini/ev-shortlist` using current UK-market evidence.

## What to check

For each vehicle in `docs/data/vehicles.json`:

1. UK availability, launch timing, trims and salary-sacrifice/lease visibility.
2. UK OTR pricing and likely monthly cost versus the EV6 GT benchmark.
3. Sound/audio reviews and cabin noise comments.
4. Performance, especially acceleration and whether the car remains usable in comfort/normal modes.
5. Ride comfort, adaptive suspension availability and motorway refinement.
6. Dashboard/instrument design: integrated screens versus stuck-on tablet design.
7. Physical controls: climate, volume, drive modes, glovebox/basic functions.
8. Mobile integration: CarPlay/Android Auto, Bluetooth reconnect reliability, app reliability, digital key behaviour.
9. Security/theft resistance: keyless entry mitigation, tracker/immobiliser options, insurance implications, stolen-vehicle assistance.
10. Safety: Euro NCAP results, ADAS behaviour, driver-assistance nags and false interventions.
11. Subscription risks, especially comfort or hardware features.
12. Credible reviews from UK or European sources.

## Output/update rules

- Update `docs/data/vehicles.json` only where there is evidence.
- Keep unknown values as `null`, `unknown`, `verify` or `TBD`.
- Add or update notes in the relevant vehicle object.
- Add a dated entry to `docs/data/change-log.json` explaining what changed and why.
- Do not let spec-sheet performance override poor sound, controls, phone integration or security.
- Do not reject Chinese-brand cars automatically, but require stronger proof of quality, support, software maturity and security.
- Keep Tesla excluded.
- Keep Kia EV6 GT as benchmark only.

## Final report format

After updating the repo, report:

1. Cars that moved up.
2. Cars that moved down.
3. New red flags.
4. New evidence gaps.
5. Whether anything is now ready for a test drive or dealer enquiry.
