# Executive Revenue Reference

> Simulation test artifact; human review pending. <!-- status: draft -->

## Quick reference
- Canonical table: `nodal-shorelane.shorelane.fct_revenue`.
- Grain: dated signed contribution to one measure. No order/customer key; row count has no business meaning.
- Filter exactly one `measure_name` and explicit `activity_date` bounds; sum signed `amount`.
- Eligible customer hygiene and applicable negative refund rows are already present.

## Routing triggers
- IF unqualified revenue: use recognized revenue and state that assumption. Honor explicitly named measures and persona defaults in company/terminology.md.
- IF comparing measures: report separately; DO NOT add them together.
- IF order counts or channel/customer slices: use `fct_orders`; DO NOT count fct_revenue rows or invent a join key.
- IF recognized, billed, or collected totals: DO NOT substitute order gross/net amounts.
- IF using staging: apply real-customer hygiene; `stg_orders` includes test/internal rows.
- IF summing fct_revenue: DO NOT subtract refunds again.
- IF last quarter: use the most recent fully elapsed calendar quarter at an explicit as-of date.

## Pending
Measure-specific timing, slicing, caveats and live dashboard reconciliation.

## Entity handling
- Eligible orders belong to account_type = customer; exclude test and internal. No additional mandatory order-status exclusion is specified. Governed facts apply eligibility; raw/staging retain all accounts.
- Normalize historical direct to d2c; rename effective 2022-06-01 was not backfilled. business_subscription and marketplace retain labels. Use fct_orders.channel for comparisons; channel_raw preserves original labels.
- Resolve aliases by LEFT JOIN on (source_system, source_customer_id). Unresolved aliases remain unknown and a quality metric, never new customers. Deduplicate canonical IDs before joining order facts; recreated Stripe aliases can multiply revenue. Count distinct source systems for identity coverage. Attribute invoices/refunds through order_id to fct_orders; tickets require qualified crosswalk resolution.

## Slicing and timing caveats
- The executive channel chart omits test/internal exclusion and must not be used as a reconciliation target. fct_revenue supports date grouping and measure selection only. Use fct_orders for order-date GMV/earnings splits. For recognized, billed or collected splits, join the corresponding event rows to eligible fct_orders on order_id, use measure-specific activity dates, and attribute refunds to original orders. Reconcile every split to its fct_revenue total.
- Subscription recognition continues for twelve monthly installments, so recognition activity can extend beyond the last order month. Compare identical explicit bounds ending at a fully elapsed calendar month; exclude the current partial month and pin the as-of load.
- Order lines exist only for d2c and marketplace orders, sum to consumer gross value, and exclude subscriptions. Marketplace line value is retail, not Shorelane take. Use fct_order_lines for consumer product/category mix, quantities and line margin. Marketplace retail line margin does not establish Shorelane economic margin; marketplace/subscription cost basis is not provided.

- IF an executive order-chart count disagrees with eligible orders: preserve governed hygiene and investigate the dashboard population. The observed chart discrepancy awaits owner review; do not change the business rule to force a match.
