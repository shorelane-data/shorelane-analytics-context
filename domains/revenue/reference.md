# Revenue Reference

> Agent-facing retrieval doc. Routing, grain, filters, gotchas — no narrative.

## Quick Reference
- **Business context** — Shorelane (office-supplies commerce, three channels)
  tracks five distinct revenue measures; there is no single "revenue".
- **Entity grain** — `fct_revenue`: one row per revenue **event**.
  `activity_date × measure_name` is NOT unique — always `SUM(amount)`.
- **Standard hygiene filter** — every query filters exactly one
  `measure_name` (or groups by it); never sum across measures.
- **Canonical table** — `nodal-shorelane.shorelane.fct_revenue`.

## Routing triggers
- IF the question says unqualified "revenue" → use `measure_name =
  'recognized_revenue'` and say which measure was used.
- IF the question is "how much did we sell / demand / topline" → `gmv`
  (full ticket, gross of refunds).
- IF the question is "what did we earn" → `net_revenue`.
- IF the question is about cash / collections → `collected_cash` (dated on
  collection date — never invoice date).
- IF the question is about billing / invoicing → `billed_revenue` (all
  channels, at net).
- IF the question slices revenue by **channel, customer, or product** → DO NOT
  use `fct_revenue` (it has no channel/customer columns); go to `stg_orders`
  (grain: one row per order_id) and derive, or join through `order_id` on the
  staging models.
- IF two revenue numbers disagree across measures → explain the timing/valuation
  wedge (see context.md table); it is not a data bug.
- IF asked to SUM `amount` across all measures → refuse; a cross-measure total
  double-counts the same dollars five ways.

## Dimensions
- `fct_revenue` carries only `activity_date`, `measure_name`, `amount`.
  Channel (`d2c` / `business_subscription` / `marketplace`), customer, and
  product live on `stg_orders` and the other staging models, keyed by
  `order_id`.
- `activity_date` means a different thing per measure: order date (gmv,
  net_revenue, billed_revenue), refund date (refund rows in
  net_revenue/collected_cash), collection date (collected_cash),
  recognition date (recognized_revenue).

## Key tables
### nodal-shorelane.shorelane.fct_revenue   ← canonical
- **Grain**: one row per revenue event · **Scope**: all five measures, all channels
- **Use for**: any "<measure> over <period>" question
- **Do NOT use for**: channel/customer/product slicing (no such columns)
- **Required filters**: `measure_name = '<measure>'` · **Join keys**: none (aggregate-only)

### nodal-shorelane.shorelane.stg_orders
- **Grain**: one row per `order_id` · **Scope**: all channels
- **Use for**: order counts, channel mix, gross-vs-net wedge (`gross_amount` vs `net_amount`)
- **Join keys**: `order_id` → stg_invoices / stg_refunds / stg_revenue_recognition

### nodal-shorelane.shorelane.stg_invoices
- **Grain**: one row per `invoice_id` (business subscriptions only)
- **Use for**: net-30 collection status; `collected_date` NULL = pending or bad
  debt (`is_bad_debt` disambiguates)

### nodal-shorelane.shorelane.stg_refunds
- **Grain**: one row per `refund_id` · lagged after the original order
- **Use for**: refund analysis; the negative rows in net_revenue/collected_cash

### nodal-shorelane.shorelane.stg_revenue_recognition
- **Grain**: one row per (`order_id`, `recognition_date`)
- **Use for**: how recognized_revenue spreads subscriptions ratably

## Gotchas
- `activity_date × measure_name` is not unique — taking `amount` without SUM
  silently returns one event, not the day's total.
- gmv is full-ticket and gross of refunds; every other measure is at net.
  Marketplace at full price only ever appears in gmv.
- Refunds land on the **refund's own date** — a period's net_revenue includes
  refunds processed that period for older orders.
- collected_cash is dated on collection date; pending net-30 and bad-debt
  invoices contribute nothing.
- recognized_revenue can exceed gmv in a period (ratable slices of past
  subscription orders) — not a bug.
- Bad debt is a manual finance write-off (no aging rule) — never infer it from
  invoice age; NULL `collected_date` alone means pending, not bad debt.
- Customer counts come from `stg_orders`, never the raw customer ID pool
  (over-counts pre-order and voided-invoice IDs). Always show channel mix.
- AOV is `AVG(gross_amount)` per channel, never blended; order counts may be
  blended but always show the channel mix.
- No seller ID exists — seller-level marketplace questions cannot be answered;
  say so instead of proxying.

## Common query patterns

### Period total for one measure
Without this: summing across measures (double-counts dollars five ways) or
taking `amount` without SUM (returns one event, not the total).
```sql
-- pattern, not paste
SELECT ROUND(SUM(amount), 2) AS <measure>
FROM `nodal-shorelane.shorelane.fct_revenue`
WHERE measure_name = '<measure>'
  AND activity_date BETWEEN <start_date> AND <end_date>
```

## Cross-references
- `company/terminology.md` — the five revenues, channel and billing terms.
