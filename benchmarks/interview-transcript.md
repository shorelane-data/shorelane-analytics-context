# Shorelane simulated interview transcript

Simulation test artifacts only; automated answers are not human confirmations. Copied from the interview session log; two local identifiers redacted. See `benchmarks/README.md`.

## Q1 — Stage 0 / warehouse — auto

**Question:** Which data platforms do your dashboards run on — just one warehouse, or a mix (e.g. Snowflake + BigQuery + Postgres)?

**Answer used:** CONFIDENT: Just one warehouse: BigQuery, project `nodal-shorelane`. It has two datasets: `shorelane_raw` for unfiltered source tables and `shorelane` for staging views, the identity bridge, and governed marts.

## Q2 — Stage 0 / lineage remote — escalated (pending)

**Question:** I found the dbt project at a local checkout of shorelane-dbt; its origin is https://github.com/shorelane-data/shorelane-dbt.git and branch is main. What source should CI clone for Shorelane’s lineage: is this the durable dbt repository and production branch, or is this a local simulation fixture whose remote should not be treated as cloneable?

**Simulated answer:** NOT_CONFIDENT: The brief describes Shorelane’s dbt layer but does not identify a durable dbt repository, production branch, or cloneable CI source. It does not establish whether that local project or remote is a simulation fixture.

**Human reply:** Pending.

## Q3 — Stage 0 / query-history identities — escalated (pending)

**Question:** Which service users do your dashboards run as? Live BigQuery history shows the sa-bi-dashboards service account with plotly_dashboard labels, and the sa-dbt-runner service account with dbt labels. Identify BI versus automation accounts from the brief.

**Simulated answer:** NOT_CONFIDENT: The brief does not identify dashboard service users or automation service accounts, so I cannot confirm either account’s role from it.

**Human follow-up:** Classify sa-bi-dashboards, sigma-bigquery, sa-dbt-runner and datahub-ingestion.

**Human reply:** Pending.

## Q4 — Stage 0 / depth — escalated (pending)

**Question:** Full interview for the first domain, or a 30-minute test drive — five core questions, a live check, and the rest drafted for later?

**Simulated answer:** NOT_CONFIDENT: The brief does not establish a preference between a full interview and a 30-minute test drive.

**Human reply:** Pending.

## Q5 — Stage 1 / business — auto

**Question:** In one sentence, what does Shorelane actually sell, and who pays?

**Answer used:** CONFIDENT: Shorelane sells office supplies to consumers and small businesses through Shop Direct, annual seat-based subscriptions to companies through Shorelane for Business, and third-party goods through its marketplace, where buyers pay the retail price and Shorelane keeps a commission.

## Q6 — Stage 1 / terminology list — auto

**Question:** Name the 5–10 terms a new Shorelane analyst always gets wrong in their first month — just name them; we will define them a few at a time.

**Answer used:** CONFIDENT: Revenue; Marketplace earnings; Current customers; New customers; Active subscribers; Subscription starts; Renewal rate; Grandfathered plans; Multi-channel customers; Last quarter.

## Q7 — Stage 1 / Revenue — auto

**Question:** dbt fct_revenue documents five revenue measures and query history has SUM(amount) with measure_name filters. When a stakeholder says 'revenue', which measure should win, or what must be clarified?

**Answer used:** CONFIDENT: Unqualified revenue means recognized revenue (GAAP); state the assumption. Persona defaults: CFO Dana → recognized; Marketing Marcus → GMV; FP&A Priya → billed; Controller Theo → collected cash; COO Sam → net revenue. The five measures are not additive.

## Q8 — Stage 1 / Marketplace earnings — auto

**Question:** For 'marketplace earnings', are we counting the buyer's retail spend or Shorelane's commission, and what terminology distinguishes them?

**Answer used:** CONFIDENT: Marketplace earnings mean Shorelane’s commission or take, represented by net_amount. Buyer retail spend is GMV (gross_amount). Refunds carry the take, not the full retail amount.

## Q9 — Stage 1 / Current customers — auto

**Question:** For 'current customers', which identity or lifecycle rule makes someone count, given source-native customer identities and canonical app_db_customer_id in dim_customers?

**Answer used:** CONFIDENT: Distinct canonical app_db_customer_id values with at least one order in the trailing twelve full calendar months, at month grain. Include only account_type = customer, excluding test/internal and never-ordered profiles; deduplicate across source identities and channels. The customer dashboard omits the test/internal exclusion; governed marts are authoritative.

## Q10 — Stage 1 / New customers — auto

**Question:** What qualifies a 'new customer' here, and what common alternative definition is wrong?

**Answer used:** CONFIDENT: A new customer’s first-ever order across all channels falls in the period. Count distinct real canonical customers, not newly created profiles or a first purchase in an additional channel. Attribute new customers by channel to the canonical channel of their first-ever order.

## Q11 — Stage 1 / Active subscribers — auto

**Question:** dbt fct_subscriptions describes one row per term while its active-subscriber description says customer grain. Does 'active subscribers' count terms, seats, or distinct customers, and what time rule determines eligibility?

**Answer used:** CONFIDENT: Distinct real customers with term_start_date <= D <= term_end_date, both inclusive. Compare dates to dates. Terms and seats are different units; status = active and plan is_current do not determine eligibility.

## Q12 — Stage 1 / Subscription starts — auto

**Question:** What does 'subscription starts' count, particularly renewals versus first starts?

**Answer used:** CONFIDENT: Subscription starts are counted in terms, with renewals creating new term rows. The new subscriptions KPI counts first terms (is_first_term) starting in the period and excludes renewal terms.

## Q13 — Stage 1 / Renewal rate — auto

**Question:** For renewal rate, which terms belong in the denominator and how is renewal decided?

**Answer used:** CONFIDENT: Renewed terms divided by renewed plus churned terms whose term end falls in the period. A subsequent term linked by renewed_from_subscription_id identifies renewal. Without renewal, churn occurs at term end. Exclude undecided active terms; count terms, anchored on the ending term’s end date.

## Q14 — Stage 1 / Grandfathered plans — auto

**Question:** dbt dim_plans describes current sold generation while older generations remain live. What does grandfathered plans mean for pricing and active subscriber counts?

**Answer used:** CONFIDENT: Grandfathered means the generation was retired from sale by the as-of date. Customers retain the original plan and retired generations remain eligible for active-subscriber counts. Term prices use the price effective at term start. The May 2025 increase affected generation 3 only, leaving older generations unchanged.

## Q15 — Stage 1 / Multi-channel customers — auto

**Question:** What makes a customer multi-channel, and can channel-level customer counts be added together?

**Answer used:** CONFIDENT: A customer with orders in at least two canonical channels within the selected period. Normalize historical direct to d2c. This is a period metric over active customers, not a subset of current customers. Channel customer counts overlap; deduplicate the total.

## Q16 — Stage 1 / Last quarter — auto

**Question:** When a Shorelane stakeholder asks for 'last quarter', what exact calendar and data-completeness convention applies?

**Answer used:** CONFIDENT: The most recent fully elapsed calendar quarter as of an explicit as-of date; state the assumption. No separate fiscal calendar. Use explicit quarter bounds, not trailing days or months or the current partial quarter. The live warehouse loads daily; the full fixture alone has no defined today.

## Q17 — Stage 2 / dashboard catalog — auto + escalated (owners pending)

**Question:** List the dashboards your team maintains and who owns each. Include their business grouping and URLs/BI tool if the brief provides them.

**Answer used:** CONFIDENT: Executive Revenue (executive revenue, customers, orders, AOV, refunds), Customers (customer lifecycle, channels, identity health), Marketing (GMV by channel, AOV, paid media, CAC, categories, promotions), Subscriptions (FP&A: subscribers, ACV, starts, renewals, churn, plans). URLs: https://shorelane-data.github.io/shorelane/{business,customers,marketing,subscriptions}/. Sigma workbooks cover only executive and customers views.

**Simulated escalation:** NOT_CONFIDENT: No dashboard owners or Sigma workbook URLs. Stakeholder personas establish metric preferences, not dashboard ownership.

**Human reply:** Pending for dashboard owners. Sigma URLs optional, not needed for Pages verification.

## Setup assumption

Depth preference remains unanswered; interviewer proceeds with default full first-domain interview after allowing reply time. This is not analyst confirmation. CI remote stays omitted; account classifications remain unconfirmed.

## Q18 — Stage 2 / canonical revenue grain — auto

**Question:** For period revenue totals, should the agent use fct_revenue’s signed measure rows (dbt and recurring dashboard queries filter measure_name and SUM(amount)), or order-grain gross/net amounts from fct_orders/stg_orders (also present in schema and Sigma history)? State the canonical table, what one row represents, and the role of the other table so the agent cannot accidentally sum unlike measures.

**Answer used:** CONFIDENT: Use fct_revenue for period revenue totals: exactly one measure_name, explicit activity_date bounds, SUM(signed amount). Rows are dated contributions to measures, not orders or customers; measures are non-additive and row counts have no business meaning. fct_orders is one eligible order per row, for counts, canonical channels/customers and order-date gross/net amounts; these do not replace recognized, billed or collected events. stg_orders includes test/internal accounts. Refunds are negative rows where applicable in fct_revenue; do not subtract them twice.

## Q19 — Stage 2/4 / measures — auto + escalated

**Question:** Recognized revenue versus GMV: which events/dates and refund treatment belong to each, including subscriptions and marketplace?

**Answer used:** CONFIDENT (covered portions): Full-ticket order value at order date, including full subscription contract value and marketplace retail spend; gross of refunds. Earnings basis: marketplace take, not retail GMV. Subscriptions recognize net amount in twelve equal cent-rounded monthly installments beginning on order date, anniversary-stepped and clamped to month end; other orders recognize fully on order date. Recognition is independent of billing, collection and churn. Refund-event implementation remains unconfirmed.

**Simulated escalation:** NOT_CONFIDENT: Recognized revenue refund-event implementation is not explicitly covered by the brief.

**Human reply:** Pending; no implementation assumed.

## Q20 — Stage 2/4 / measures — auto

**Question:** For net revenue, what events/dates and amounts enter the measure, including marketplace refunds?

**Answer used:** CONFIDENT (covered portions): Full d2c and subscription fees plus marketplace commission on order date, less refunds on refund date. Marketplace refunds reverse the take. Refunds occur only on d2c/marketplace and are already negative fct_revenue rows.

## Q21 — Stage 2/4 / measures — auto + escalated

**Question:** For billed revenue versus collected cash, which invoice events/dates count, and are refunds netted into either?

**Answer used:** CONFIDENT (covered portions): Non-subscription activity on order date; subscription invoices on billed_date, with full annual subscription billed upfront. Refund adjustments remain unconfirmed. Non-subscription activity on order date; subscriptions on actual collected_date, less refunds paid out. Bad-debt invoices never contribute cash. Null collection date can mean pending or bad debt, distinguished by is_bad_debt.

**Simulated escalation:** NOT_CONFIDENT: Whether billed revenue includes refund adjustments is not explicitly covered by the brief.

**Human reply:** Pending; no implementation assumed.

## Q22 — Stage 3 / entity list — auto

**Question:** For Executive Revenue, list the ambiguous entity/status terms that still need disambiguation, beyond the glossary already captured. Just name them; we will work through at most three at a time.

**Answer used:** CONFIDENT: Eligible order; Real customer; Marketplace take; Pending versus bad-debt invoice; Collected date; Recognition date; Canonical channel; Source-native customer ID.

## Q23 — Stage 3 / eligible_order — auto

**Question:** Does 'eligible order' mean any order except test/internal customers, or are there additional mandatory status exclusions?

**Answer used:** CONFIDENT: Eligible orders belong to account_type = customer; exclude test and internal. No additional mandatory order-status exclusion is specified. Governed facts apply eligibility; raw/staging retain all accounts.

## Q24 — Stage 3 / canonical_channel — auto

**Question:** For canonical channel, how should historical direct and current d2c be treated in comparisons, and what are the business_subscription and marketplace mappings?

**Answer used:** CONFIDENT: Normalize historical direct to d2c; rename effective 2022-06-01 was not backfilled. business_subscription and marketplace retain labels. Use fct_orders.channel for comparisons; channel_raw preserves original labels.

## Q25 — Stage 3 / source_native_customer_id — auto

**Question:** The identity bridge has source_system, source_customer_id and nullable app_db_customer_id. What exact join/dedup rule should an agent use to attribute source-native activity without multiplying revenue or silently dropping unresolved identities?

**Answer used:** CONFIDENT: Resolve aliases by LEFT JOIN on (source_system, source_customer_id). Unresolved aliases remain unknown and a quality metric, never new customers. Deduplicate canonical IDs before joining order facts; recreated Stripe aliases can multiply revenue. Count distinct source systems for identity coverage. Attribute invoices/refunds through order_id to fct_orders; tickets require qualified crosswalk resolution.

## Q26 — Stage 4 / caveat list — auto

**Question:** If a new analyst wrote the obvious Executive Revenue query, what remaining plausible-but-wrong failure modes should we capture beyond measure selection, customer hygiene, refund double-subtraction, channel normalization and identity fanout? Just name the remaining caveats first.

**Answer used:** CONFIDENT: Wrong event date; Revenue-row counts or nonexistent dimensions; Month-start recognition instead of anniversaries; Recognition tied to collection or churn; Null collection date treated as bad debt; Recognized revenue can exceed GMV; Inflated executive channel breakdown; Partial live periods versus elapsed dashboard months; Latest recognition month versus latest order month; Order lines as total company revenue.

## Q27 — Stage 4 / Inflated executive channel breakdown — auto

**Question:** What inflates the executive dashboard's revenue-by-channel chart, and what governed source or handling should replace it? fct_revenue schema exposes only activity_date, measure_name, amount—can it be sliced by anything beyond date, and where should unsupported slicing be routed?

**Answer used:** CONFIDENT: The executive channel chart omits test/internal exclusion and must not be used as a reconciliation target. fct_revenue supports date grouping and measure selection only. Use fct_orders for order-date GMV/earnings splits. For recognized, billed or collected splits, join the corresponding event rows to eligible fct_orders on order_id, use measure-specific activity dates, and attribute refunds to original orders. Reconcile every split to its fct_revenue total.

**Additional answer detail (snapshot, log only):** For 2025 the channel chart totals $28,333,671.42, exceeding the correct headline by $27,573.83. Not used as a live truth anchor.

## Q28 — Stage 4 / Latest recognition month versus latest order month — auto

**Question:** Why can latest recognition month differ from latest order month, and what cutoff should a live comparison use?

**Answer used:** CONFIDENT: Subscription recognition continues for twelve monthly installments, so recognition activity can extend beyond the last order month. Compare identical explicit bounds ending at a fully elapsed calendar month; exclude the current partial month and pin the as-of load.

## Q29 — Stage 4 / Order lines as total company revenue — auto

**Question:** Why can't consumer order lines be summed as total company revenue, and when are order lines the correct grain?

**Answer used:** CONFIDENT: Order lines exist only for d2c and marketplace orders, sum to consumer gross value, and exclude subscriptions. Marketplace line value is retail, not Shorelane take. Use fct_order_lines for consumer product/category mix, quantities and line margin. Marketplace retail line margin does not establish Shorelane economic margin; marketplace/subscription cost basis is not provided.

## Q30 — Stage 4 / expression assembly — auto

**Question:** For each named revenue measure, SUM(amount) on fct_revenue with mandatory measure_name, explicit activity_date bounds and date-only grouping; dated signed contribution grain; no second refund subtraction. Orders use COUNT(*) on eligible fct_orders within order_date bounds. Recognized/billed refund internals remain unconfirmed. Is this faithful?

**Answer used:** CONFIDENT: Faithful. Filter exactly one measure and explicit activity-date bounds, sum as-is, and group by date when needed. Rows are contributions, not orders or unique date/measure keys. Count eligible fct_orders within order-date bounds. Keep recognized/billed refund internals explicitly unconfirmed.

## Q31 — Stage 5 / live-check preference — escalated

**Question:** Would you like the promised live comparison on revenue, collected cash and order counts against the Executive Revenue dashboard?

**Simulated answer:** NOT_CONFIDENT: The brief identifies the dashboard as a verification source but does not establish a preference.

**Human reply:** Pending. Existing user instruction authorizes read-only warehouse/dashboard work; proposed default is to proceed unless deferred.

## Q32 — Stage 5 / revenue truth — escalated (pending)

**Question:** For Last 12 Months, 2025-09-01 through 2026-08-31, as of 2026-09-15, the tier-1.5 recognized monthly series sums to 33,888,811.17. Can the brief independently establish the value/window as trusted truth and specify tolerance? Do not endorse solely from my reported match.

**Simulated answer:** NOT_CONFIDENT: Brief dashboard references are pinned to 2025-12; current value/window and tolerance are not covered.

**Human prompt:** Accept capture and query (SUM(amount), recognized_revenue, matching bounds, signed rows as-is) to cents, or leave unblessed.

**Human reply:** Pending.

## Q33 — Stage 5 / cash truth — escalated (pending)

**Question:** Same window and as-of date; tier-1.5 collected-cash series totals 35,337,042.60 and off/on SQL matches. Does the brief independently support blessing the capture and query, with what tolerance?

**Simulated answer:** NOT_CONFIDENT: No collected cash for this window or tolerance in the brief. Query follows documented rule but does not independently validate the number.

**Human reply:** Pending.

## Q34 — Stage 5 / order discrepancy — auto rule + escalated snapshot

**Question:** Same window and as-of: dashboard orders 15,787, both warehouse agents 15,571. Follow-up staging census: 15,571 customer + 77 internal + 139 test. Which business handling should context encode, and does the brief explicitly establish this executive order-chart defect? Distinguish rule confidence from current-value confidence.

**Answer used:** CONFIDENT: Count only orders with account_type = customer using eligible one-row-per-order fct_orders. Exclude test/internal orders; dashboard disagreement does not change the governed definition.

**Simulated escalation:** NOT_CONFIDENT: The brief does not explicitly document an executive order-chart defect or these counts. Its executive defect concerns revenue by channel. Record an observed issue requiring verification, not an analyst-confirmed defect or trusted numeric answer key.

**Human prompt:** Record defect, or keep observed discrepancy pending owner review.

**Human reply:** Pending.

## Current stopping point

Interviewer completed company glossary and first-domain capture, ran independent context-off/on verification, and logged all 34 numbered questions. Human replies to escalations remain pending. All context and seeds are simulation drafts. Schema validation and scaffold checks passed. Configuration hash unchanged; no commit, push, or verified SQL sidecars.
