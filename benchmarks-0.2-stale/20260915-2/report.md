# All-seed context evaluation — 20260915-2

Simulation benchmark against the frozen draft seed requirements; not a human-certified accuracy score.

**Coverage:** 23/23 seeds, 46/46 answers graded, zero skipped. One answering agent per condition, one sample per seed.

| Condition | Passed | Pass rate |
|---|---:|---:|
| Context off | 14/23 | 60.9% |
| Context on | 19/23 | 82.6% |

**Delta: +21.7 percentage points** (+5 passed seeds).

## By domain

| Domain | Seeds | Off passed | On passed |
|---|---:|---:|---:|
| customers | 3 | 1 | 3 |
| executive-revenue | 16 | 12 | 12 |
| subscriptions | 4 | 1 | 4 |

## What changed

- Improved: S01, S05, S06, S10, S15, S17, S22.
- Regressed: S03, S08.
- Failed both: S18, S20.

## Every seed

| ID | Seed | Off | On | Grader explanation |
|---|---|---|---|---|
| S01 | active-subscribers | fail | pass | Off: Distinct-customer grain and governed-fact account eligibility are correct, but term_end_date > excludes the required inclusive endpoint. On: Counts distinct real customers with inclusive DATE term bounds and no status or catalog eligibility filter. |
| S02 | billed-revenue | pass | pass | On: Uses fct_revenue and reports its billed_revenue group with explicit Q2 activity_date bounds and signed SUM; grouping keeps measures separate and no refunds are subtracted again. Conditional SUM bounds are semantically equivalent to WHERE bounds. |
| S03 | canonical-channel | pass | fail | Off: Uses normalized fct_orders.channel; the channel/channel_raw diagnostic establishes the June 2022 switch, retained historical direct labels, and unchanged marketplace/business_subscription labels. The different revenue basis is outside this rubric. On: Correctly uses normalized fct_orders.channel and explains the dated, non-backfilled rename, but omits the raw-label field and unchanged-label rules. |
| S04 | collected-cash | pass | pass | On: Uses fct_revenue and reports its collected_cash group with explicit Q2 activity_date bounds and signed SUM; grouping keeps measures separate and no refunds are subtracted again. Conditional SUM bounds are semantically equivalent to WHERE bounds. |
| S05 | consumer-lines-scope | fail | pass | Off: Correctly rejects company-wide line revenue and demonstrates missing subscription coverage, but only says marketplace amounts may differ and does not supply the required line-value and cost guidance. On: Conceptual answer supplies consumer-only gross retail coverage, subscription exclusion, marketplace take distinction, line-analysis uses and cost/margin limitations. |
| S06 | current-customers | fail | pass | Off: Reports all dimension profiles by first_seen_date instead of real customers ordering within twelve full months; clarification leaves the required current-customer definition unresolved. On: Distinct customer_id from governed fct_orders over September 2025 through August 2026 satisfies canonical grain, purchasing eligibility and full-month window. |
| S07 | eligible-order | pass | pass | On: Counts Q2 order rows/IDs from governed fct_orders, which encapsulates account hygiene; no additional status exclusion is introduced. Staging diagnostics do not replace the reported population. |
| S08 | executive-order-hygiene-correction | pass | fail | Off: Counts bounded Q2 governed fct_orders and recommends preserving its population while diagnosing staging separately; this operationally retains the governed hygiene exclusions. On: Preserves test/internal exclusions and rejects matching the dashboard, but gives neither an order-date bounded count nor a pattern with explicit bounds. |
| S09 | gmv | pass | pass | On: Uses fct_revenue and reports its gmv group with explicit Q2 activity_date bounds and signed SUM; grouping keeps measures separate and no refunds are subtracted again. Conditional SUM bounds are semantically equivalent to WHERE bounds. |
| S10 | grandfathered-plans | fail | pass | Off: Includes retired-plan terms and does not filter to current catalog plans, but omits term-start effective pricing. On: Includes live terms on retired generations, rejects is_current eligibility and specifies term-start effective pricing. |
| S11 | last-quarter | pass | pass | On: Pins the as-of date to September 15, 2026 and selects the most recent elapsed calendar quarter with April 1 inclusive/July 1 exclusive bounds. |
| S12 | marketplace-earnings | pass | pass | On: Uses marketplace net_amount as commission/take and explicitly distinguishes retail GMV; refund event adjustments do not violate this rubric. |
| S13 | multi-channel-customers | pass | pass | On: Groups governed fct_orders by canonical customer_id within Q2, retains customers with at least two distinct normalized channels, and counts each once without a current-snapshot restriction. |
| S14 | net-revenue | pass | pass | On: Uses fct_revenue and reports its net_revenue group with explicit Q2 activity_date bounds and signed SUM; grouping keeps measures separate and no refunds are subtracted again. Conditional SUM bounds are semantically equivalent to WHERE bounds. |
| S15 | new-customers | fail | pass | Off: Uses distinct canonical IDs and first_order_date in Q2, but dim_customers is not restricted to real account_type customers. Alternate profile counts are labeled, not substituted for the headline KPI. On: Finds each canonical customer's earliest eligible fct_orders date across all channels before applying Q2 bounds; grouped rows count real customers once. |
| S16 | recognized-revenue | pass | pass | On: Uses fct_revenue and reports its recognized_revenue group with explicit Q2 activity_date bounds and signed SUM; grouping keeps measures separate and no refunds are subtracted again. Conditional SUM bounds are semantically equivalent to WHERE bounds. |
| S17 | renewal-rate | fail | pass | Off: Uses the correct ending-term cohort and successor key, but divides by every ending term without restricting to resolved renewed/churned outcomes. On: Anchors on ending terms, resolves successors via renewed_from_subscription_id, and divides renewed by renewed-or-churned, excluding undecided terms. |
| S18 | revenue-channel-reconciliation | fail | fail | Off: Correct recognition_date joins and fct_revenue reconciliation are present, with unmatched staging kept outside the reported total. Missing required chart warning and refund attribution remain. On: Correct recognition_date event join to eligible fct_orders and explicit reconciliation are present. The required chart warning and refund-to-original-order treatment are absent; an unresolved refund-policy limitation does not establish that treatment. |
| S19 | revenue-fact-grain | pass | pass | On: Uses fct_revenue and reports its net_revenue group with explicit Q2 activity_date bounds and signed SUM; grouping keeps measures separate and no refunds are subtracted again. Conditional SUM bounds are semantically equivalent to WHERE bounds. |
| S20 | revenue-period-completeness | fail | fail | Off: Has the shared September 15 date anchor and labels September partial, but includes it in the monthly comparison series rather than excluding it. It also omits the required twelve-installment recognition tail; no immutable snapshot is demanded. On: Excludes September and compares explicit full-month bounds, explains post-order recognition, and has the shared September 15 observation anchor. It omits the required twelve monthly installments; lack of an immutable historical snapshot is not treated as a failure. |
| S21 | revenue | pass | pass | On: States recognized revenue as its assumed default and reports its separate fct_revenue group; measures are not summed together. A request to confirm the basis does not undo the supplied answer. |
| S22 | source-native-customer-id | fail | pass | Off: Correctly prevents canonical-ID fanout and qualifies source ID joins, but does not specify LEFT JOIN unknown retention, distinct-source coverage or event/ticket routing. On: Complete conceptual answer specifies qualified LEFT JOIN resolution, unknown unresolved aliases, canonical deduplication, Stripe fanout, distinct-source coverage and event/ticket routing. |
| S23 | subscription-starts | pass | pass | On: Counts is_first_term subscription IDs/rows starting within explicit Q2 term_start_date bounds; renewal starts are excluded from the new-subscription KPI. |

## Interpreting the remaining context-on failures

- **Canonical channel (S03):** correct normalization and date, but omitted `channel_raw` and unchanged-label details demanded by the rubric.
- **Order-chart correction (S08):** correct eligibility recommendation, but no bounded SQL/count pattern demanded by a conceptual question’s rubric.
- **Revenue channel reconciliation (S18):** numeric channel split reconciled, but the answer omitted the rubric’s chart warning and refund-attribution discussion.
- **Period completeness (S20):** correctly excluded the current partial month, but omitted the rubric’s explicit twelve-installment explanation. A historical immutable snapshot is not required by the clarified grader interpretation.

These are failures against the frozen expected fields, not four proven wrong numeric answers. In particular, S03 and S08 are regressions in rubric coverage, not evidence of worse channel normalization or order eligibility.

## Illustrative answer differences

| Question | Context off | Context on |
|---|---:|---:|
| Active subscribers at August month end | 3,583 | 3,595 |
| Current customers | 28,930 known profiles | 9,678 eligible trailing-year purchasers |
| New customers in Q2 | 1,137 | 1,121 |

These demonstrate changed handling of inclusive term dates, the current-customer window, and real-customer exclusions. They are warehouse outputs under different interpretations, not separately blessed numeric snapshots.

**Seed limitation:** Marketplace earnings passed both conditions even though answers differed (44,117.23 versus 41,121.79). Its rubric checks commission versus retail value but does not require refund-date netting. A pass therefore does not prove full metric equivalence; the seed would need a separate reviewed revision to test that behavior.

## Method and practical limits

- Questions and seed expectations were frozen before the run; neither answering agent saw seeds, intent, IR or expected answers. Context-on received only the authored company/domain/entity context snapshot; context-off used warehouse evidence.
- A separate grader saw A/B candidates shuffled independently per seed, with no condition mapping. Grading tests semantic compliance, not keyword matching or dashboard-number equality. Correct governed marts count as encapsulating their filters.
- All seeds are `sql_shape`. Numeric requests used live read-only BigQuery SQL; conceptual questions were graded on their rule/query reasoning. No fresh dashboard capture or numeric answer key was required.
- SQL execution coverage: off 23/23 cases; on 19/23 cases. Some cases reuse an executed query, disclosed in traces. All 23 cases remain independently scored against their own rubric.
- Date anchor was 2026-09-15 for both conditions. Relative-period interpretation was part of each answer. Results are current-table observations, not immutable warehouse time-travel snapshots.
- One batch per condition allows within-batch carryover. Duplicate/overlapping questions reduce independence. This single run supports no significance or generalization claim.
- The context and seeds came from the same simulated interview, and some expected fields are broader than their questions. Rubric caveats below identify these weaknesses.
- Warehouse metadata incidentally exposed view definitions: off saw int_customer_identity/stg_invoices; on saw stg_refunds/stg_revenue_recognition. Detailed reliance notes are in the answer artifacts. Neither condition read dbt source or the analyst brief.
- Authored context, all seed files and `.codex/config.toml` hashes are unchanged. No commits or pushes.

## Rubric caveats

- S03: Compound rubric additionally requires discussion of unchanged unrelated channels and the raw-label field for a direct/d2c comparison; these unconditional clauses make the seed broader than the question.
- S05: Compound rubric includes product mix and economic-margin/cost guidance beyond whether lines cover company revenue.
- S08: Question is conceptual, but its frozen rubric explicitly requires a bounded count; no execution is necessary if an adequate pattern or complete method is supplied.
- S10: Term-start pricing is an unconditional extra requirement despite the question asking only subscriber eligibility.
- S18: Compound rubric unconditionally includes an executive-chart warning although no dashboard is mentioned. Order-date GMV/earnings and billed/collected instructions are conditional on other measures and are not demanded here.
- S20: The phrase 'pin the as-of load' is ambiguous between a stated observation/date anchor and an immutable warehouse snapshot. Shared artifact metadata supplies September 15, 2026 for both candidates. No immutable-snapshot requirement is inferred; snapshot reproducibility is not established. The rubric also unconditionally requires a twelve-installment explanation.
- S21: No explicit persona or measure was supplied, so that conditional override requirement is not triggered.
- S22: Compound rubric also demands distinct-source coverage and invoice/refund/ticket routing beyond the immediate identity-to-order join question.

## Artifacts

- [Machine-readable results](results.json)
- [Illustrative answer differences](answer-differences.json)
- [Grading input audit](grading-audit.md)
- [Frozen run manifest](manifest.json)
- [Context-off answers and exact SQL](off-answers.json)
- [Context-on answers and exact SQL](on-answers.json)
- [Blinded grades](grades-blinded.json)
- [Grading policy](grading-policy.md)
