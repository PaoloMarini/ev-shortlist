# ev-shortlist (private)

A single source of truth for your EV shortlist, owned in GitHub and easy to query/update via ChatGPT.

## Files
- `shortlist.csv` ← **Master data** (authoritative)
- `shortlist.md` ← Human-readable view of the above (generated manually as needed)
- `/notes/*.md` ← Per-vehicle free-form notes
- `/history/` ← Optional area for notable change logs

## Schema (`shortlist.csv`)
| column | type | description |
|---|---|---|
| model | text | e.g., "EX30 Ultra" |
| make | text | e.g., "Volvo" |
| body_type | text | SUV, Hatchback, Saloon, etc. |
| battery_kWh | number | usable battery capacity |
| range_WLTP_km | number | WLTP range in km |
| fast_charge_kW | number | peak DC charge rate |
| zeroTo100_kmh_sec | number | 0–100 km/h time |
| price_GBP | number | OTR price in GBP |
| towing_kg | number | braked towing capacity |
| boot_l | number | boot volume (seats up) |
| euro_ncap | text/number | rating or year |
| heated_seat_subscription | yes/no/TBD | whether heated seats require subscription |
| software_subscriptions_notes | text | free-form |
| availability_UK | text/date | e.g., "On sale", "Q2 2026", date |
| status | enum | shortlisted / watchlist / research / comparison_only / dismissed |
| brief_notes | text | quick context |
| last_updated | date | ISO date of last change |

## How to update via ChatGPT
Use clear, patch-style instructions. Examples:

> Update **Volvo EX30**: set `heated_seat_subscription` to `no`; add note "confirmed by dealer 2025-11-10".  
> Add new row **Audi Q6 e-tron**: price 68,000; WLTP 625; battery 100; fast_charge 270; status watchlist.

ChatGPT will prepare either:
1) a **diff** (unified patch) you can paste into GitHub, **or**
2) an **updated `shortlist.csv` file** to upload via the GitHub web UI.

## Commit message convention
- `feat(data): add Audi Q6 e-tron initial row`
- `chore(data): update EX30 heated-seat subscription=no`
- `docs(notes): add Smart #5 Brabus notes with ADAS details`

## Safety / accuracy
Many fields are `TBD` initially. As we confirm specs (with citations), we update the CSV and notes. When uncertain, prefer `TBD` + a note instead of guessing.

---

*Initialized on 2025-11-02.*
