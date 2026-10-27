# Frozen authored context — simulation inputs only

## FILE: company/org-structure.md

# Dashboard domain ownership

> Simulation test artifact. Owners are not inferred from stakeholder personas.

| Domain | Owner | Team | Status |
|---|---|---|---|
| Executive Revenue | To be confirmed | To be confirmed | draft |
| Customers | To be confirmed | To be confirmed | draft |
| Marketing | To be confirmed | To be confirmed | draft |
| Subscriptions | To be confirmed | To be confirmed | draft |


## FILE: company/overview.md

# Shorelane

> Simulation test artifact; simulated-analyst response, awaiting human review.

Shorelane sells office supplies to consumers and small businesses through Shop Direct, annual seat-based subscriptions to companies through Shorelane for Business, and third-party goods through its marketplace, where buyers pay the retail price and Shorelane keeps a commission. <!-- status: draft -->


## FILE: company/terminology.md

# Shorelane terminology

> Simulation test artifact. Definitions require human review.

## Revenue

Unqualified revenue means recognized revenue (GAAP); state the assumption. Persona defaults: CFO Dana → recognized; Marketing Marcus → GMV; FP&A Priya → billed; Controller Theo → collected cash; COO Sam → net revenue. The five measures are not additive.

_Simulation answer captured; human review pending._ <!-- status: draft -->

## Marketplace earnings

Marketplace earnings mean Shorelane’s commission or take, represented by net_amount. Buyer retail spend is GMV (gross_amount). Refunds carry the take, not the full retail amount.

_Simulation answer captured; human review pending._ <!-- status: draft -->

## Current customers

Distinct canonical app_db_customer_id values with at least one order in the trailing twelve full calendar months, at month grain. Include only account_type = customer, excluding test/internal and never-ordered profiles; deduplicate across source identities and channels. The customer dashboard omits the test/internal exclusion; governed marts are authoritative.

_Simulation answer captured; human review pending._ <!-- status: draft -->

## New customers

A new customer’s first-ever order across all channels falls in the period. Count distinct real canonical customers, not newly created profiles or a first purchase in an additional channel. Attribute new customers by channel to the canonical channel of their first-ever order.

_Simulation answer captured; human review pending._ <!-- status: draft -->

## Active subscribers

Distinct real customers with term_start_date <= D <= term_end_date, both inclusive. Compare dates to dates. Terms and seats are different units; status = active and plan is_current do not determine eligibility.

_Simulation answer captured; human review pending._ <!-- status: draft -->

## Subscription starts

Subscription starts are counted in terms, with renewals creating new term rows. The new subscriptions KPI counts first terms (is_first_term) starting in the period and excludes renewal terms.

_Simulation answer captured; human review pending._ <!-- status: draft -->

## Renewal rate

Renewed terms divided by renewed plus churned terms whose term end falls in the period. A subsequent term linked by renewed_from_subscription_id identifies renewal. Without renewal, churn occurs at term end. Exclude undecided active terms; count terms, anchored on the ending term’s end date.

_Simulation answer captured; human review pending._ <!-- status: draft -->

## Grandfathered plans

Grandfathered means the generation was retired from sale by the as-of date. Customers retain the original plan and retired generations remain eligible for active-subscriber counts. Term prices use the price effective at term start. The May 2025 increase affected generation 3 only, leaving older generations unchanged.

_Simulation answer captured; human review pending._ <!-- status: draft -->

## Multi-channel customers

A customer with orders in at least two canonical channels within the selected period. Normalize historical direct to d2c. This is a period metric over active customers, not a subset of current customers. Channel customer counts overlap; deduplicate the total.

_Simulation answer captured; human review pending._ <!-- status: draft -->

## Last quarter

The most recent fully elapsed calendar quarter as of an explicit as-of date; state the assumption. No separate fiscal calendar. Use explicit quarter bounds, not trailing days or months or the current partial quarter. The live warehouse loads daily; the full fixture alone has no defined today.

_Simulation answer captured; human review pending._ <!-- status: draft -->


## FILE: domains/customers/context.md

# Customers

> Simulation test artifact.

_To be confirmed by the domain owner._ <!-- status: draft -->

## Captured company-level terms
See company/terminology.md and this domain’s draft eval seeds. Domain-specific table selection, complete metrics, owner review and live verification remain pending.


## FILE: domains/customers/domain.yaml

# SIMULATION TEST ARTIFACT; table/lineage candidates are dbt-derived, not yet ratified.
name: Customers
summary: Customer lifecycle, channels, identity health
status: draft
owner: To be confirmed
grain: To be confirmed by the domain owner.
tables:
  canonical: nodal-shorelane.shorelane.dim_customers
dashboards:
- name: Customers
  canonical_question: To be confirmed
  url: https://shorelane-data.github.io/shorelane/customers/
lineage:
- source: dbt_core
  models:
  - dim_customers
  - fct_orders
  - int_customer_identity
  - fct_identity_resolution_quality
  - dim_date


## FILE: domains/customers/entities.yaml

# SIMULATION TEST ARTIFACT; status/type interview pending.
entities: []


## FILE: domains/customers/known-issues.md

# Customers

> Simulation test artifact.

_To be confirmed by the domain owner._ <!-- status: draft -->


## FILE: domains/customers/metrics.yaml

# SIMULATION TEST ARTIFACT; metric interview pending.
metrics: []


## FILE: domains/customers/reference.md

# Customers

> Simulation test artifact.

_To be confirmed by the domain owner._ <!-- status: draft -->


## FILE: domains/executive-revenue/context.md

# Executive Revenue

> Simulation test artifact; human review pending. <!-- status: draft -->

Use fct_revenue for period revenue totals: exactly one measure_name, explicit activity_date bounds, SUM(signed amount). Rows are dated contributions to measures, not orders or customers; measures are non-additive and row counts have no business meaning. fct_orders is one eligible order per row, for counts, canonical channels/customers and order-date gross/net amounts; these do not replace recognized, billed or collected events. stg_orders includes test/internal accounts. Refunds are negative rows where applicable in fct_revenue; do not subtract them twice.


## FILE: domains/executive-revenue/domain.yaml

# SIMULATION TEST ARTIFACT
name: Executive Revenue
summary: Executive revenue, customers, orders, AOV, refunds
status: draft
owner: To be confirmed
grain: One dated signed contribution to one revenue measure; not an order/customer
  and not a unique date-measure key.
tables:
  canonical: nodal-shorelane.shorelane.fct_revenue
  others:
  - nodal-shorelane.shorelane.fct_orders
  - nodal-shorelane.shorelane.stg_orders
dashboards:
- name: Executive Revenue
  canonical_question: What were recognized revenue and the separately reported revenue
    measures for the selected period?
  url: https://shorelane-data.github.io/shorelane/business/
  tool: plotly-static
lineage:
- source: dbt_core
  models:
  - fct_revenue
  - fct_orders
  - stg_orders
  - stg_refunds
  - stg_invoices
  - stg_revenue_recognition
  - dim_customers
  - stg_app_customers
  - dim_date
  - int_customer_identity
  - fct_order_lines


## FILE: domains/executive-revenue/entities.yaml

# SIMULATION TEST ARTIFACT — enumerations supported by dbt and interview.
entities:
- name: revenue_measure
  description: Distinct non-additive revenue measures on fct_revenue.
  status: draft
  mappings:
    gmv: Full-ticket order value at order date, including full subscription contract
      value and marketplace retail spend; gross of refunds.
    recognized_revenue: 'Earnings basis: marketplace take, not retail GMV. Subscriptions
      recognize net amount in twelve equal cent-rounded monthly installments beginning
      on order date, anniversary-stepped and clamped to month end; other orders recognize
      fully on order date. Recognition is independent of billing, collection and churn.
      Refund-event implementation remains unconfirmed.'
    net_revenue: Full d2c and subscription fees plus marketplace commission on order
      date, less refunds on refund date. Marketplace refunds reverse the take. Refunds
      occur only on d2c/marketplace and are already negative fct_revenue rows.
    billed_revenue: Non-subscription activity on order date; subscription invoices
      on billed_date, with full annual subscription billed upfront. Refund adjustments
      remain unconfirmed.
    collected_cash: Non-subscription activity on order date; subscriptions on actual
      collected_date, less refunds paid out. Bad-debt invoices never contribute cash.
      Null collection date can mean pending or bad debt, distinguished by is_bad_debt.
  important: Select exactly one measure for a total; an unqualified revenue request
    defaults to recognized revenue with the assumption stated.
  lineage:
  - source: dbt_core
    models:
    - fct_revenue


## FILE: domains/executive-revenue/known-issues.md

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


## FILE: domains/executive-revenue/metrics.yaml

# SIMULATION TEST ARTIFACT — assembly accepted by simulated analyst, not human-approved.
metrics:
- name: gmv
  definition: Full-ticket order value at order date, including full subscription contract
    value and marketplace retail spend; gross of refunds.
  grain: Dated signed measure contribution, aggregated over the reporting window.
  status: draft
  parameters:
  - name: time_window
    note: Explicit inclusive start and exclusive end dates.
  - name: as_of_date
    note: Anchor relative time to the stated as-of date.
  caveats:
  - Simulation test artifact; not human-approved.
  - Select one measure; never sum all measures.
  - Do not subtract refunds again from fct_revenue.
  lineage: &id001
  - source: dbt_core
    models:
    - fct_revenue
  expression:
    measure: SUM(amount)
    mandatory_filters:
    - field: measure_name
      op: '='
      value: gmv
      reason: Measures are distinct and cannot be added together.
    - field: activity_date
      op: '>='
      value: <period_start>
      reason: "Use the selected measure\u2019s event date."
    - field: activity_date
      op: <
      value: <period_end_exclusive>
      reason: Explicit aligned bounds prevent mixing partial and fully elapsed periods.
    allowed_dimensions:
    - activity_date
- name: recognized_revenue
  definition: 'Earnings basis: marketplace take, not retail GMV. Subscriptions recognize
    net amount in twelve equal cent-rounded monthly installments beginning on order
    date, anniversary-stepped and clamped to month end; other orders recognize fully
    on order date. Recognition is independent of billing, collection and churn. Refund-event
    implementation remains unconfirmed.'
  grain: Dated signed measure contribution, aggregated over the reporting window.
  status: draft
  parameters:
  - name: time_window
    note: Explicit inclusive start and exclusive end dates.
  - name: as_of_date
    note: Anchor relative time to the stated as-of date.
  caveats:
  - Simulation test artifact; not human-approved.
  - Select one measure; never sum all measures.
  - Do not subtract refunds again from fct_revenue.
  - Recognized and billed refund internals remain unresolved; use the governed fact
    as-is.
  lineage: *id001
  expression:
    measure: SUM(amount)
    mandatory_filters:
    - field: measure_name
      op: '='
      value: recognized_revenue
      reason: Measures are distinct and cannot be added together.
    - field: activity_date
      op: '>='
      value: <period_start>
      reason: "Use the selected measure\u2019s event date."
    - field: activity_date
      op: <
      value: <period_end_exclusive>
      reason: Explicit aligned bounds prevent mixing partial and fully elapsed periods.
    allowed_dimensions:
    - activity_date
- name: net_revenue
  definition: Full d2c and subscription fees plus marketplace commission on order
    date, less refunds on refund date. Marketplace refunds reverse the take. Refunds
    occur only on d2c/marketplace and are already negative fct_revenue rows.
  grain: Dated signed measure contribution, aggregated over the reporting window.
  status: draft
  parameters:
  - name: time_window
    note: Explicit inclusive start and exclusive end dates.
  - name: as_of_date
    note: Anchor relative time to the stated as-of date.
  caveats:
  - Simulation test artifact; not human-approved.
  - Select one measure; never sum all measures.
  - Do not subtract refunds again from fct_revenue.
  lineage: *id001
  expression:
    measure: SUM(amount)
    mandatory_filters:
    - field: measure_name
      op: '='
      value: net_revenue
      reason: Measures are distinct and cannot be added together.
    - field: activity_date
      op: '>='
      value: <period_start>
      reason: "Use the selected measure\u2019s event date."
    - field: activity_date
      op: <
      value: <period_end_exclusive>
      reason: Explicit aligned bounds prevent mixing partial and fully elapsed periods.
    allowed_dimensions:
    - activity_date
- name: billed_revenue
  definition: Non-subscription activity on order date; subscription invoices on billed_date,
    with full annual subscription billed upfront. Refund adjustments remain unconfirmed.
  grain: Dated signed measure contribution, aggregated over the reporting window.
  status: draft
  parameters:
  - name: time_window
    note: Explicit inclusive start and exclusive end dates.
  - name: as_of_date
    note: Anchor relative time to the stated as-of date.
  caveats:
  - Simulation test artifact; not human-approved.
  - Select one measure; never sum all measures.
  - Do not subtract refunds again from fct_revenue.
  - Recognized and billed refund internals remain unresolved; use the governed fact
    as-is.
  lineage: *id001
  expression:
    measure: SUM(amount)
    mandatory_filters:
    - field: measure_name
      op: '='
      value: billed_revenue
      reason: Measures are distinct and cannot be added together.
    - field: activity_date
      op: '>='
      value: <period_start>
      reason: "Use the selected measure\u2019s event date."
    - field: activity_date
      op: <
      value: <period_end_exclusive>
      reason: Explicit aligned bounds prevent mixing partial and fully elapsed periods.
    allowed_dimensions:
    - activity_date
- name: collected_cash
  definition: Non-subscription activity on order date; subscriptions on actual collected_date,
    less refunds paid out. Bad-debt invoices never contribute cash. Null collection
    date can mean pending or bad debt, distinguished by is_bad_debt.
  grain: Dated signed measure contribution, aggregated over the reporting window.
  status: draft
  parameters:
  - name: time_window
    note: Explicit inclusive start and exclusive end dates.
  - name: as_of_date
    note: Anchor relative time to the stated as-of date.
  caveats:
  - Simulation test artifact; not human-approved.
  - Select one measure; never sum all measures.
  - Do not subtract refunds again from fct_revenue.
  lineage: *id001
  expression:
    measure: SUM(amount)
    mandatory_filters:
    - field: measure_name
      op: '='
      value: collected_cash
      reason: Measures are distinct and cannot be added together.
    - field: activity_date
      op: '>='
      value: <period_start>
      reason: "Use the selected measure\u2019s event date."
    - field: activity_date
      op: <
      value: <period_end_exclusive>
      reason: Explicit aligned bounds prevent mixing partial and fully elapsed periods.
    allowed_dimensions:
    - activity_date
- name: orders
  definition: Count eligible orders placed in the reporting window.
  grain: One eligible order per row.
  status: draft
  lineage:
  - source: dbt_core
    models:
    - fct_orders
  expression:
    measure: COUNT(*)
    mandatory_filters:
    - field: order_date
      op: '>='
      value: <period_start>
      reason: Count orders placed in the selected period.
    - field: order_date
      op: <
      value: <period_end_exclusive>
      reason: Align the reporting window.
    allowed_dimensions:
    - order_date
    - channel
    - customer_id
  caveats:
  - fct_orders applies real-customer hygiene and canonical channel labels; staging
    does not.
  - Do not count fct_revenue rows as orders.


## FILE: domains/executive-revenue/reference.md

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


## FILE: domains/marketing/context.md

# Marketing

> Simulation test artifact.

_To be confirmed by the domain owner._ <!-- status: draft -->


## FILE: domains/marketing/domain.yaml

# SIMULATION TEST ARTIFACT; table/lineage candidates are dbt-derived, not yet ratified.
name: Marketing
summary: GMV by channel, AOV, paid media, CAC, categories, promotions
status: draft
owner: To be confirmed
grain: To be confirmed by the domain owner.
tables:
  canonical: nodal-shorelane.shorelane.fct_marketing_spend
dashboards:
- name: Marketing
  canonical_question: To be confirmed
  url: https://shorelane-data.github.io/shorelane/marketing/
lineage:
- source: dbt_core
  models:
  - fct_marketing_spend
  - fct_order_lines
  - fct_orders
  - dim_products
  - dim_date


## FILE: domains/marketing/entities.yaml

# SIMULATION TEST ARTIFACT; status/type interview pending.
entities: []


## FILE: domains/marketing/known-issues.md

# Marketing

> Simulation test artifact.

_To be confirmed by the domain owner._ <!-- status: draft -->


## FILE: domains/marketing/metrics.yaml

# SIMULATION TEST ARTIFACT; metric interview pending.
metrics: []


## FILE: domains/marketing/reference.md

# Marketing

> Simulation test artifact.

_To be confirmed by the domain owner._ <!-- status: draft -->


## FILE: domains/subscriptions/context.md

# Subscriptions

> Simulation test artifact.

_To be confirmed by the domain owner._ <!-- status: draft -->

## Captured company-level terms
See company/terminology.md and this domain’s draft eval seeds. Domain-specific table selection, complete metrics, owner review and live verification remain pending.


## FILE: domains/subscriptions/domain.yaml

# SIMULATION TEST ARTIFACT; table/lineage candidates are dbt-derived, not yet ratified.
name: Subscriptions
summary: 'FP&A: subscribers, ACV, starts, renewals, churn, plans'
status: draft
owner: To be confirmed
grain: To be confirmed by the domain owner.
tables:
  canonical: nodal-shorelane.shorelane.fct_subscriptions
dashboards:
- name: Subscriptions
  canonical_question: To be confirmed
  url: https://shorelane-data.github.io/shorelane/subscriptions/
lineage:
- source: dbt_core
  models:
  - fct_subscriptions
  - dim_plans
  - stg_plan_prices
  - dim_date


## FILE: domains/subscriptions/entities.yaml

# SIMULATION TEST ARTIFACT; status/type interview pending.
entities: []


## FILE: domains/subscriptions/known-issues.md

# Subscriptions

> Simulation test artifact.

_To be confirmed by the domain owner._ <!-- status: draft -->


## FILE: domains/subscriptions/metrics.yaml

# SIMULATION TEST ARTIFACT; metric interview pending.
metrics: []


## FILE: domains/subscriptions/reference.md

# Subscriptions

> Simulation test artifact.

_To be confirmed by the domain owner._ <!-- status: draft -->


## FILE: entities/revenue-subjects.yaml

# SIMULATION TEST ARTIFACT — human review required.
entities:
- name: real_customer
  description: Eligible orders belong to account_type = customer; exclude test and
    internal. No additional mandatory order-status exclusion is specified. Governed
    facts apply eligibility; raw/staging retain all accounts.
  status: draft
  lineage:
  - source: dbt_core
    models:
    - fct_orders
    - stg_app_customers
  mappings:
    customer: Eligible for business reporting
    test: Excluded
    internal: Excluded
- name: canonical_channel
  description: Normalize historical direct to d2c; rename effective 2022-06-01 was
    not backfilled. business_subscription and marketplace retain labels. Use fct_orders.channel
    for comparisons; channel_raw preserves original labels.
  status: draft
  lineage:
  - source: dbt_core
    models:
    - fct_orders
  mappings:
    direct: Historical alias of d2c
    d2c: Shop Direct
    business_subscription: Shorelane for Business
    marketplace: Third-party marketplace
- name: source_native_customer_id
  description: Resolve aliases by LEFT JOIN on (source_system, source_customer_id).
    Unresolved aliases remain unknown and a quality metric, never new customers. Deduplicate
    canonical IDs before joining order facts; recreated Stripe aliases can multiply
    revenue. Count distinct source systems for identity coverage. Attribute invoices/refunds
    through order_id to fct_orders; tickets require qualified crosswalk resolution.
  status: draft
  lineage:
  - source: dbt_core
    models:
    - int_customer_identity
    - dim_customers
    - fct_orders
