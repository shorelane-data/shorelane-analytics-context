# Revenue — Known Issues

## What This Covers
Data-quality issues and analytical gotchas — the silent-failure modes. Each issue
here also appears as an `IF … DO NOT …` routing trigger in `reference.md`
and as an eval seed.

- **Revenue from staging views** — `stg_*` tables include test and internal accounts; a sum over them overstates revenue. Use the marts. <!-- status: draft (simulated, revenue-001) -> seed -->
- **Sigma revenue-by-channel donut** — joins staging tables without the test/internal exclusion; does not reconcile to the headline. Treat as unreconciled. <!-- status: draft (simulated, revenue-001); query-history-derived (Sigma Business donut) -> seed -->
- **Summing across measures** — the five measures are not additive. <!-- status: draft -> seed -->
- **Double-subtracting refunds** — refunds are already negative rows. <!-- status: draft -> seed -->
- **Channel splits by order date** — recognized / billed / collected "by channel" via `fct_orders` filtered on order date silently returns GMV or net. Join the measure's own event rows on `order_id` at its activity date; reconcile to the `fct_revenue` total. <!-- status: draft (simulated, revenue-002) -> seed -->
- **"GMV minus refunds"** — refunds carry the order's *net* amount (only the take on marketplace orders), so this mixes bases and is neither GMV nor net. <!-- status: draft (simulated, revenue-002) -> seed -->
- **Recognized above GMV is not a bug** — ratable subscription recognition can push recognized revenue above GMV in a period. Don't "fix" it. <!-- status: draft (simulated, revenue-002) -->
- **Churned subscriptions still recognize** — recognition runs to term end regardless of billing, collection or churn. <!-- status: draft (simulated, revenue-002) -->
- **Null `collected_date`** — means pending *or* bad debt; use `is_bad_debt` to tell them apart. Bad debt never collects but is still recognized. <!-- status: draft (simulated, revenue-002) -> seed -->
- **Live-warehouse windows** — trailing or partial windows move daily and won't match the dashboard, which uses fully elapsed months; future updates are masked. <!-- status: draft (simulated, revenue-002) -->
- **Latest recognized month ≠ latest order month** — recognition rows run up to a year past the order. <!-- status: draft (simulated, revenue-002) -->
- **Identity fan-out** — joining orders to the customer-ID crosswalk inflates revenue (recreated Stripe accounts); inner-joining drops unresolved aliases. Reach customers through `order_id` → `fct_orders.customer_id`. <!-- status: draft (simulated, revenue-002) -> seed -->
- **Order lines are not revenue** — summing `line_amount` gives consumer GMV only (no subscriptions), and marketplace lines carry the seller's retail price. <!-- status: draft (simulated, revenue-002) -->
- **Marketplace earnings gross of refunds** — "how much did we make from the marketplace" means take net of refunds; summing `fct_orders.net_amount` alone overstates it. Subtract marketplace refunds (joined on `order_id`, at refund date). <!-- human-decided 2026-10-27 (Stage 5 correction) -> seed revenue-marketplace-earnings -->
- **Collected-cash refund date** — refund rows inside collected cash are dated at the refund date (same as net revenue), not the order date. <!-- human-decided 2026-10-27 (revenue-002) -->
