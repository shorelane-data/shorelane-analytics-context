# Executive Revenue caveat queue

> Simulation test artifact; human review required.

## Wrong event date

Use the selected measure’s activity date. Order date does not replace invoice billed/collected dates or recognition dates.

_Supported by earlier simulated interview responses; human review pending._ <!-- status: draft -->

## Revenue-row counts or nonexistent dimensions

Revenue rows are signed measure contributions, not orders. fct_revenue has no customer/channel join key; route slicing through source events and eligible orders.

_Supported by earlier simulated interview responses; human review pending._ <!-- status: draft -->

## Month-start recognition instead of anniversaries

Subscription recognition uses cent-rounded monthly installments starting on order date, stepped on anniversaries and clamped to month end.

_Supported by earlier simulated interview responses; human review pending._ <!-- status: draft -->

## Recognition tied to collection or churn

Subscription recognition is independent of collection, billing and churn.

_Supported by earlier simulated interview responses; human review pending._ <!-- status: draft -->

## Null collection date treated as bad debt

A null collected_date may be pending or bad debt; distinguish using is_bad_debt. Bad debt contributes no collected cash.

_Supported by earlier simulated interview responses; human review pending._ <!-- status: draft -->

## Recognized revenue can exceed GMV

Ratable recognition from earlier subscription orders can fall in a later period independently of current order bookings; do not treat recognized revenue greater than period GMV as proof of an error.

_Supported by earlier simulated interview responses; human review pending._ <!-- status: draft -->

## Inflated executive channel breakdown

The executive channel chart omits test/internal exclusion and must not be used as a reconciliation target. fct_revenue supports date grouping and measure selection only. Use fct_orders for order-date GMV/earnings splits. For recognized, billed or collected splits, join the corresponding event rows to eligible fct_orders on order_id, use measure-specific activity dates, and attribute refunds to original orders. Reconcile every split to its fct_revenue total.

_Simulation response; human review pending._ <!-- status: draft -->

## Partial live periods versus elapsed dashboard months

Align explicit period bounds and as-of load; compare fully elapsed months and exclude the current partial month.

_Supported by earlier simulated interview responses; human review pending._ <!-- status: draft -->

## Latest recognition month versus latest order month

Subscription recognition continues for twelve monthly installments, so recognition activity can extend beyond the last order month. Compare identical explicit bounds ending at a fully elapsed calendar month; exclude the current partial month and pin the as-of load.

_Simulation response; human review pending._ <!-- status: draft -->

## Order lines as total company revenue

Order lines exist only for d2c and marketplace orders, sum to consumer gross value, and exclude subscriptions. Marketplace line value is retail, not Shorelane take. Use fct_order_lines for consumer product/category mix, quantities and line margin. Marketplace retail line margin does not establish Shorelane economic margin; marketplace/subscription cost basis is not provided.

_Simulation response; human review pending._ <!-- status: draft -->


## Observed executive order-chart hygiene discrepancy

The live comparison found the executive order chart consistent with an unfiltered staging population. Governed reporting must continue to exclude test/internal accounts. This specific chart defect is an observed hypothesis supported by warehouse reconciliation, awaiting owner review; it is not established by the simulated analyst’s brief. Snapshot counts and SQL are only in local verification artifacts. <!-- status: draft -->
