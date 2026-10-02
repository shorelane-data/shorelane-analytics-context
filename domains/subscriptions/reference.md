# Subscriptions Reference

> SIMULATION TEST ARTIFACT — all definitions remain draft; human review required.

## Quick reference
- Canonical route: fct_subscriptions, one real-customer subscription term. Raw/staging include test/internal accounts. Canonical customer IDs differ from source identities.
- Stock grain: distinct customers for subscribers, term sums for seats and locked ACV. Flow grain: terms, not customers or seats.
- Use explicit dates and full elapsed calendar windows. Stock uses window end; flow uses specified start or end cohort.

## Routing triggers
- IF active subscribers at D → distinct customer_id where term_start_date <= D <= term_end_date, inclusive date comparisons; DO NOT filter stored status or plan is_current.
- IF seats or ACV under contract → SUM seats or locked term acv on the same date-contained terms; DO NOT substitute distinct customer count or current list price. Investigate overlaps before summing.
- IF new subscriptions/new ACV → first terms (is_first_term), selected by term_start_date; DO NOT include renewals. Final-day starts count in full.
- IF ACV per seat on new subscriptions → SUM first-term acv / SUM first-term seats in start-date cohort; DO NOT average individual prices or ratios. Zero-denominator policy remains pending.
- IF monthly Renewals bars or renewal starts → count renewal successor terms (is_first_term = false) by term_start_date and calendar start month; DO NOT count ending predecessors or include first terms.
- IF renewed ending terms/churn/rates → ending predecessor term cohort with decided outcomes renewed/churned; exclude active undecided. Renewal rate = renewed/(renewed+churned), churn rate its complement. DO NOT cohort by successor start date or count distinct customers.
- IF verifying renewed status → use successor renewed_from_subscription_id to identify ending predecessor; DO NOT require successor start inside the report period. A link does not authorize altering service dates.
- IF ACV churned → SUM locked acv of churned terms ending in period; DO NOT interpret as a refund or recognized-revenue adjustment.
- IF grandfathered share at D → distinct active customers whose plan retired_date <= D / all active distinct customers; DO NOT hard-code generation != 3 for all history. A retirement exactly on D qualifies.
- IF current plan → sale eligibility only; DO NOT exclude older generations from the live book. Generation comes from the term; plan/tier are distinct concepts.
- IF pricing → term-start effective price, frozen on the term. Renewals refresh pricing. The generation-3 increase effective 2025-05-01 affects starts/renewals from then; older generations and existing locked terms are unchanged.
- IF quarterly churn chart → calendar-quarter bucket of term_end_date after window selection; DO NOT call a clipped quarter a full quarter.
- IF reporting through current load date → disclose future-row/outcome masking and undecided terms; DO NOT claim final rates or historical knowledge-as-of reconstruction. Report-cohort date differs from what was known at that time.
- IF invoices/order lines → invoices measure billed/collected, subscription terms measure book; subscription composition is seats/plan and has no order lines. ACV is not recognized revenue.
- IF Q4 2022 enterprise churn explanation → document the synthetic billing incident, canonicalize Salesforce requester IDs for support evidence; DO NOT assert per-ticket causality or a general causal estimate.
- IF pauses/midterm cancellation/upgrades/plan switches → unavailable in this fixture; DO NOT invent analyses. Undefined seat buckets and unsupported dimensions require clarification.
- IF source dates violate next-day renewal invariant → flag the discrepancy and preserve observed date containment; DO NOT silently repair dates. Owner disposition remains pending.

- IF comparing monthly renewal bars to renewal rate → use the human-selected separate anchors: bars count renewal starts by term_start_date; rate counts decided ending predecessors by term_end_date. DO NOT force the totals to agree or derive the rate from monthly renewal-start bars.

## Supported dimensions
Term plan, plan_generation and customer segment are supported dashboard slices. Tier and locked seat price are available but not rendered. Segment is immutable in this fixture, not an inferred general SCD contract. Status is an outcome, not a generic slicing choice; acquisition channel, promotions and source-native IDs are inappropriate subscription dimensions. Sales channel is uninformative here.

## Common query patterns
- Stock: inclusive date containment before distinct customer count or term sums; do not select stored active status.
- New seat pricing: first-term/start-date cohort, aggregate ACV and seats separately then divide.
- Monthly Renewals bars: select non-first terms by term_start_date, bucket by calendar start month and count each renewal term once.
- Renewal rate: select ending predecessor terms, classify decided outcomes with successor linkage, aggregate terms once; successor start need not be inside the window.
- Grandfathering: attach plan retirement to active terms at explicit D; classify retirement as of D and deduplicate numerator and denominator independently.

## Cross-references
[Metrics](metrics.yaml), [issues](known-issues.md), [plan entities](../../entities/subscription-plans.yaml), [Customers](../customers/reference.md) for canonical identity, [Executive Revenue](../executive-revenue/reference.md) for billed/recognized/collected measures.
