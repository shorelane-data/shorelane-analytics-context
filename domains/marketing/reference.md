# Marketing Reference

<!-- status: draft — simulated-analyst answers (marketing-001); owner, AOV scope and dashboard defect human-decided. -->

## Quick Reference
- **Business context** — how much Shorelane sells (GMV by channel, consumer orders, AOV) and what acquiring new customers costs.
- **Entity grain** — `fct_orders`: one order from a real customer at canonical channel. `fct_marketing_spend`: one row per platform-day (google / meta / tiktok).
- **Standard hygiene filter** — marts only (real customers); canonical `channel`; fully elapsed months.
- **Canonical table** — `nodal-shorelane.shorelane.fct_orders`

## Routing triggers
- IF marketing asks for "revenue" → GMV (`order_gmv` for slices; `revenue.gmv` for totals); state it.
- IF GMV by channel / segment → `order_gmv` (SUM `gross_amount` on `fct_orders` at order date); reconcile to `revenue.gmv`.
- IF AOV → `aov` = `consumer_gmv` ÷ `consumer_orders` (d2c + marketplace) by default; an all-channel AOV must be labelled.
- IF CAC → `cac` = `ad_spend` ÷ `new_d2c_customers` (distinct first-ever d2c customers). DO NOT sum `attributed_new_d2c_customers_day_total` across platform rows; DO NOT use `reported_conversions`.
- IF CAC per platform → no warehouse attribution exists per platform; report blended CAC and say so (platform-reported CAC is inflated by the platforms' own conversion claims).
- IF "how much did we make from the marketplace" → take net of refunds (revenue domain), not marketplace GMV.
- IF promotions → `promo_code` on the order (consumer channels only); discount dollars = quantity × unit price × `discount_pct` on lines. DO NOT judge promos by AOV (they lower it while raising volume).
- IF category or margin → consumer order lines only (`fct_order_lines`); subscriptions have no lines.
- IF seller / third-party merchant questions → decline: no seller identifier exists.

## Dimensions
- `channel` (canonical; see `entities/channel.yaml`), `segment`, `promo_code` (WELCOME10 — d2c only; SPRING5, BTB15 — d2c + marketplace).
- `platform` on `fct_marketing_spend`: google, meta, tiktok. `spend_usd`, `impressions`, `clicks`, `reported_conversions`.

## Key tables
### fct_orders   ← canonical
- **Grain**: one order from a real customer  ·  **Use for**: GMV slices, consumer orders, AOV, new customers, promo orders

### fct_marketing_spend
- **Grain**: platform-day  ·  **Use for**: ad spend by platform / day
- **Do NOT use for**: new-customer counts — its `attributed_new_d2c_customers_day_total` repeats the day total on every platform row and counts flagged first-order rows, not distinct customers.

## Gotchas
- The Marketing Dashboard's "New customers" tile counts flagged first-order rows (double-flagged customers counted twice) — a known defect; the governed figure is distinct customers (customers domain).
- Feb–Apr 2026 paid-media cut lowered new d2c customers; existing customers kept ordering — not falling demand.
- Rolling "last 12 months / this quarter" moves daily on the live warehouse; use fully elapsed months.
- "How many orders" is order volume; "how many new customers" is distinct canonical customers — don't mix units.

## Common query patterns
- Blended CAC for a period: total `spend_usd` over the period ÷ distinct first-ever d2c customers in `fct_orders` over the same period.

## Cross-references
- `domains/revenue/reference.md` (GMV totals, take), `domains/customers/reference.md` (new customers).
