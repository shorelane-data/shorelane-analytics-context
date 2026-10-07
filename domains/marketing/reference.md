# Marketing Reference

> SIMULATION TEST ARTIFACT — draft throughout, human owner review required.

## Quick reference
- **Grain:** fct_marketing_spend is platform-day; fct_orders is one real-customer order; fct_order_lines is one consumer line; new acquisitions are canonical customers.
- **Canonical routes:** paid spend → fct_marketing_spend; channel GMV/orders/AOV → fct_orders; category/discount → fct_order_lines. There is no safe universal joined fact grain.
- **Hygiene:** real customers only, account_type = customer. Governed commerce facts apply this; raw/staging retain test/internal accounts. Normalize direct to d2c.
- **Dates:** explicit fully elapsed calendar windows, matched populations and bounds. Live snapshots can omit future events and mask future updates.

## Routing triggers
- IF Marketing asks for revenue → use GMV and state that interpretation; DO NOT substitute recognized revenue silently. Undimensioned GMV can use fct_revenue with measure_name gmv; channel/customer queries require fct_orders.
- IF headline GMV → include all canonical channels, gross_amount, gross of refunds; DO NOT substitute net_amount or marketplace commission.
- IF consumer orders/AOV → include d2c and marketplace only; DO NOT include subscriptions. Divide whole-period consumer gross by whole-period order count, not average monthly AOV. Do not subtract refunds or discounts again.
- IF CAC → divide all-platform period spend by warehouse first-ever real d2c acquisitions; DO NOT use platform reported_conversions. Aggregate numerator and denominator independently.
- IF using attributed_new_d2c_customers_day_total → count one copy per spend_date, never sum across platform rows. dbt counts first-date order rows; verify equivalence to distinct customers and investigate ties before relying on that shortcut.
- IF asked for CAC by ad platform → clarify attribution; DO NOT treat the shared day total as platform-specific acquisition. Zero-acquisition display behavior remains unconfirmed.
- IF headline new customers → count distinct real canonical first purchasers; DO NOT count first-date order flags as customers. Live comparison found the headline consistent with order-row counting; see local reconciliation.
- IF new d2c customers → determine first-ever order across all channels before restricting acquisition period/channel. DO NOT count first d2c purchase by an existing customer as new. For the CAC first-time purchase rule, assign acquisition using the earliest purchase timestamp across all channels. Use raw app_db__orders.order_date linked by order_id to eligible fct_orders; staging date truncation cannot establish intra-day order. Resolve identical earliest timestamps with the fixed hash convention below; order IDs do not imply purchase chronology.
- IF new-customer share of d2c orders → clarify order-level numerator; DO NOT silently substitute distinct customer count. Denominator is eligible d2c order volume.
- IF category GMV → SUM consumer line_amount; DO NOT imply subscription coverage. Category mix denominator and historical recategorization remain unconfirmed.
- IF gross margin by category, or which categories carry margin → use every consumer order line, d2c and marketplace, and divide summed margin by summed line_amount per category, as the Marketing dashboard does; state that marketplace lines are at retail. DO NOT drop marketplace lines unless the question asks for d2c only.
- IF asked what margin Shorelane itself earns → marketplace orders contribute commission (net_amount), not line margin; DO NOT call marketplace line margin Shorelane earnings. No governed economic margin by category exists; say so.
- IF promotions → count/sum orders at order grain and discounts at line grain; DO NOT multiply order GMV by joined lines. Actual order date governs promotion GMV; count/discount date policy and invalid/blank-code treatment remain pending.
- IF BTB15 → consumer Back to Business promotion, not business subscriptions; DO NOT infer WELCOME10 is new-customer-only from its name.
- IF comparing paid-media platforms → respect Google/Meta coverage from June 2019 and TikTok from January 2021; DO NOT interpret earlier absence as zero performance.
- IF interpreting the known synthetic paid-media cut → separate acquisition from existing-customer ordering; DO NOT generalize a fixture intervention into a causal ROI estimator.
- IF seller ranking → no seller identifier is established; DO NOT invent seller-level results. Gift cards, NPS, store visits, headcount, customer shipping cost and return reasons are unavailable.
- IF last quarter → compute explicit previous full calendar quarter from an as-of date; DO NOT substitute a dashboard 6/12/24-month preset or trailing days.

## Key tables and dimensions
- fct_orders: real-customer order, gross_amount, canonical channel, order_date, promo_code and first-date marker. The first-date marker is not proven unique first-order attribution.
- fct_marketing_spend: platform-day spend and repeated daily acquisitions. Current dbt source exposes spend_usd, impressions, clicks and reported_conversions; physical fields were checked through live schema metadata.
- fct_order_lines: real consumer lines with line_amount, quantity, unit_price, discount_pct, category and cost. Subscriptions have no lines. Verify discount fraction encoding before calculation.
- dim_products: product/category lookup; dbt candidate grain one SKU, human uniqueness/history contract pending. Later SKU introductions can alter mix.
- stg_promotions: promotion definitions, not transaction totals. Candidate key promo_code and exact-date rules need confirmation.
- dim_customers: canonical identity and eligibility. Ad platforms (Google/Meta/TikTok) are not commerce channels (d2c/marketplace/business_subscription).

## CAC exact-timestamp assignment
For identical earliest purchase timestamps, select the order with the lowest lowercase hexadecimal SHA-256 digest of the UTF-8 JSON array ["shorelane-cac-first-order-v1", canonical customer_id, order_id], serialized compactly with no spaces (BigQuery TO_JSON_STRING). Use order_id ascending only if digests collide. Freeze this versioned salt and encoding; never use RAND(), channel alphabetical priority, or fractional credit. Flag timestamp-tied selections as assigned by convention, not observed chronology.

Apply timestamp ordering first, then this tie-breaker within each canonical customer, over all eligible all-channel history. Only then filter acquisition period and d2c. Preserve real-customer hygiene through eligible fact orders.

## Common query patterns
- Spend/acquisition: aggregate paid spend independently; compute distinct eligible first-ever d2c customers independently; align date bounds and divide. No spend-row-to-order-row join.
- Repeated daily acquisition: reduce repeated totals to one agreed value per spend_date before period summation; first verify duplicate totals agree and reconcile against the approved timestamp-based distinct-customer denominator.
- Promotions: aggregate discount lines to order_id before attaching to the one-row-per-order count/value relation. Do not sum order amount on the expanded line join.

## Cross-references
- [Marketing metrics](metrics.yaml), [issues](known-issues.md), [entities](../../entities/marketing-subjects.yaml).
- [Customers](../customers/reference.md) owns canonical lifecycle; its other attribution questions remain separate from the human-selected CAC timestamp rule.
- [Executive Revenue](../executive-revenue/reference.md) owns other revenue measures and signed refund semantics.

## Live-check qualification
Consumer AOV reconciles with the dashboard using commerce-channel scope, not customer segment. The human selected earliest purchase timestamp for CAC acquisition; inclusive first-day-channel matching is no longer the target definition. Current key uniqueness and repeated daily-total agreement are observed data properties, not semantic approval.
