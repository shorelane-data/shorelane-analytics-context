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
