# Marketing — Known Issues

## What This Covers
Data-quality issues and analytical gotchas — the silent-failure modes. Each issue
here also appears as an `IF … DO NOT …` routing trigger in `reference.md`
and as an eval seed.

- **Marketing Dashboard new-customer tile** — counts flagged first-order rows, so double-flagged customers count twice; don't reconcile against it. <!-- human-decided 2026-10-27 (marketing-001) -> seed -->
- **Summing the day-total column** — `attributed_new_d2c_customers_day_total` repeats per platform row; summing overcounts (and it counts flagged rows). <!-- status: draft (simulated, marketing-001); dbt-derived (model.fct_marketing_spend) -> seed -->
- **Platform-reported conversions** — inflated; CAC on them comes out too low. <!-- status: draft (simulated, marketing-001) -> seed -->
- **All-channel AOV** — including subscription orders inflates AOV enormously; default is consumer only. <!-- human-decided 2026-10-27 (marketing-001) -> seed -->
- **AOV as promo success** — promos lower AOV while raising volume. <!-- status: draft (simulated, marketing-001) -->
- **Seller questions** — no seller identifier; decline. <!-- status: draft (simulated, marketing-001) -->
