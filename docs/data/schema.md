# Vehicle data schema

Authoritative file: `docs/data/vehicles.json`.

## Top-level fields

- `version`: schema version.
- `lastUpdated`: date the data file was last materially updated.
- `benchmark`: vehicle id used as the comparison baseline.
- `vehicles`: list of vehicle objects.

## Vehicle fields

- `id`: stable slug, e.g. `audi-a6-etron-sportback`.
- `make`: manufacturer.
- `model`: model/trim label.
- `bodyType`: broad body type.
- `status`: one of `benchmark`, `shortlist`, `watchlist`, `research`, `rejected`.
- `candidate`: boolean.
- `exclusionReason`: reason if not a candidate.
- `origin`: country/brand/manufacturing context where relevant.
- `estimatedMonthlyCostGbp`: salary-sacrifice or lease estimate when known.
- `availabilityUk`: short status note.
- `scores`: map of criterion id to 0-10 score, or `null` if unknown.
- `flags`: red-flag tracking object.
- `notes`: short evidence/judgement notes.
- `evidenceConfidence`: e.g. `low until refreshed`, `medium`, `high`, `personal benchmark`.
- `lastChecked`: date last checked.

## Score ids

Must match `docs/data/criteria.json`:

- `sound`
- `performance`
- `comfort`
- `dashboard_controls`
- `phone_integration`
- `security`
- `quality`
- `range_charging`
- `value`
- `software_adas`

## Important rule

Do not fabricate scores. A dashboard full of `TBD`s is better than fake precision. Add scores only when there is personal experience, dealer confirmation, credible review consensus or manufacturer documentation.
