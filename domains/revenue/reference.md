# Revenue Reference

<!-- status: draft — simulated-analyst answers (company-002, company-004, revenue-001); not human-confirmed. -->

## Quick Reference
- **Business context** — how much money Shorelane made in a period, under five non-additive measures; recognized revenue is Finance's official number.
- **Entity grain** — `fct_revenue`: one row per underlying money movement (order, invoice, refund or recognition slice) with identifiers dropped. Row counts mean nothing; one order fans out into a row per measure it feeds, a subscription order into twelve recognition rows.
- **Standard hygiene filter** — exactly one `measure_name`, plus an explicit `activity_date` range. Test and internal accounts are already excluded in the marts.
- **Canonical table** — `nodal-shorelane.shorelane.fct_revenue`

## Routing triggers
- IF the question says "revenue" with no qualifier → use `recognized_revenue` and state the assumption.
- IF the asker says GMV / gross / "what crossed the platform" (Marketing) → `gmv`.
- IF net / "what we earn" (Ops) → `net_revenue`; IF billings / invoiced (FP&A) → `billed_revenue`; IF cash / collections (Treasury) → `collected_cash`.
- IF the question is "how much did we make from the marketplace" → marketplace take **net of refunds**: `fct_orders.net_amount` on marketplace orders at order date, minus marketplace refunds (joined to `fct_orders` on `order_id`, dated at refund date). NOT GMV, and NOT take before refunds. <!-- human-decided 2026-10-27 (Stage 5 correction) -->
- IF a period total → `fct_revenue`, one measure, sum `amount`.
- IF revenue by channel / customer / product → DO NOT use `fct_revenue` (it has no dimensions). GMV/net: `fct_orders` at order date (`gross_amount` / `net_amount`). Recognized/billed/collected: join that measure's own event rows to `fct_orders` on `order_id` and group at the measure's own activity date.
- IF any `stg_*` table is the proposed revenue source → DO NOT; staging includes test and internal accounts.
- IF revenue by customer → reach the customer through `order_id` → `fct_orders.customer_id`; DO NOT join the identity crosswalk or use source-system IDs on invoices/refunds.
- IF bad debt / uncollected → use `is_bad_debt`; a null `collected_date` alone means pending OR bad debt.
- IF segment (consumer / smb / enterprise) → it is NOT channel; business customers also order in consumer channels.
- IF "last quarter" → most recent completed calendar quarter (no fiscal calendar); not trailing 90 days, not the current partial quarter.
- NEVER add measures together, and never subtract refunds — they are already negative rows.

## Dimensions
- `measure_name` — one of `gmv`, `net_revenue`, `recognized_revenue`, `billed_revenue`, `collected_cash` (see `entities.yaml`).
- `activity_date` — the date the dollar is attributed to, which differs by measure:
  - `gmv`: order date. `net_revenue`: order date; refunds at refund date.
  - `recognized_revenue`: recognition date (subscriptions monthly from the order date over the 12-month term; others in full on the order date).
  - `billed_revenue`: order date; subscriptions at invoice billed date (= order date).
  - `collected_cash`: order date; subscriptions at invoice collected date. Refund rows at refund date.
- `channel` — not in `fct_revenue`; comes from `fct_orders.channel` (see `entities/channel.yaml`).

## Key tables
### fct_revenue   ← canonical
- **Grain**: one money movement, identifiers dropped  ·  **Scope**: real customers only (test/internal excluded)
- **Use for**: period totals of a single measure  ·  **Do NOT use for**: any split by channel, customer or product
- **Required filters**: one `measure_name`; explicit `activity_date` bounds

### fct_orders
- **Grain**: one order from a real customer, canonical channel  ·  **Use for**: GMV / net by channel or customer at order date; the eligibility join for event-level splits
- **Do NOT use for**: recognized, billed or collected totals (filtering on order date and summing an amount silently returns GMV or net)
- **Join keys**: `order_id`

### stg_revenue_recognition, stg_invoices, stg_refunds
- Event rows for recognized, billed/collected and refunds. Unfiltered staging — usable only joined to `fct_orders` on `order_id`, which supplies the real-customer filter and canonical channel.

## Gotchas
- The five measures are non-additive; recognized revenue can exceed GMV in a period because subscriptions recognize ratably.
- Refunds are separate negative rows in net and collected — subtracting refunds again double-counts them.
- The Sigma "Business" revenue-by-channel donut joins `stg_revenue_recognition` to `stg_orders` (unfiltered) — it skips the test/internal exclusion and does not reconcile to the headline.
- Collected cash lags billing for subscriptions (net-30); bad-debt invoices never collect.
- "GMV minus refunds" mixes bases — refunds carry the order's net amount (only the take on marketplace orders).
- Churned subscriptions keep recognizing to term end; recognized revenue can legitimately exceed GMV.
- Trailing or partial windows on the live warehouse move daily; the dashboard uses fully elapsed months.
- Summing `line_amount` from order lines is consumer GMV only — not revenue.
- A channel split must sum to the `fct_revenue` total for the same measure and period — use it as a check.

## Common query patterns
- Period total: one measure from `fct_revenue`, explicit date bounds.
- GMV / net by channel: `fct_orders` grouped by canonical `channel` at order date.
- Recognized / billed / collected by channel: the measure's own event rows joined to `fct_orders`, grouped at the measure's activity date; reconcile to the `fct_revenue` total.

## Cross-references
- Customers (canonical customer counts), subscriptions (ACV, renewal), marketing (AOV, CAC) — not yet captured.
