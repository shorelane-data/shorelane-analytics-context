# Catalog-Margin — Known Issues

## What This Covers
Data-quality issues and analytical gotchas — the silent-failure modes. Each issue
here also appears as an `IF … DO NOT …` routing trigger in `reference.md`
and as an eval seed.

- **Marketplace lines in margin** — no cost basis; margin is d2c only. <!-- human-decided 2026-10-27 (catalog-001) -> seed -->
- **Averaging line margins** — weights small lines like large ones; use the ratio of totals. <!-- human-decided 2026-10-27 (catalog-001) -> seed -->
- **Line revenue as total revenue** — lines are consumer GMV only; subscriptions have no lines. <!-- status: draft (simulated, catalog-001) -->
- **Seller questions** — no seller identifier. <!-- status: draft (simulated, catalog-001) -->
- **Mix drift from SKU introductions / March 2023 paper outage** — supply-side, not demand. <!-- status: draft (simulated, catalog-001) -->
