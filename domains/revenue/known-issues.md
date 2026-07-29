# Revenue — Known Issues

## What This Covers
Data-quality issues and analytical gotchas — the silent-failure modes. Each issue
here should also appear as an `IF … DO NOT …` routing trigger in `reference.md`
and as an eval seed.

- **No seller ID for marketplace sellers** — the data has no seller identifier,
  so seller-level questions (top sellers, seller mix, per-seller take) cannot
  be answered. The agent must say so plainly and NOT proxy (e.g. via
  category). <!-- -> seed: seller-questions-unanswerable -->
- **Bad debt is manual** — `is_bad_debt` is a case-by-case finance write-off
  with no fixed aging threshold. Never infer bad debt from invoice age, and
  never treat NULL `collected_date` alone as bad debt (it usually means
  pending). <!-- -> seed: outstanding-receivables -->
- **Customer ID pool over-counts** — customer IDs exist before any order or
  with only a voided invoice; count customers from orders, never from the raw
  pool. <!-- -> seed: customer-count-from-orders -->
