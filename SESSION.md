# Shorelane simulation session

**Simulation test artifacts only.** All authored definitions and eval seeds remain draft; no simulated response constitutes human confirmation.

## Scope
Executive Revenue interview round complete, with its work and clarification queue preserved. Customers full flow resumed in place on 2026-10-01: domain routing, metrics, entities, caveats and three live off/on comparisons captured; human clarifications and snapshot blessings remain pending. Marketing full interview and live comparisons were captured on 2026-10-02; acquisition tie policy, snapshot review and a new-customer headline discrepancy remain pending. Subscriptions remains the next untouched domain. Company glossary captures ten terms.

## Stage 0 disposition
- **dbt: extracted** — source fallback, 30 documented models; no dbt executable, manifest or exposures. The local dbt directory disappeared after extraction; saved findings remain available. Manifest drift baseline is deferred.
- **Warehouse schema probe: ok** — BigQuery project `nodal-shorelane`, dataset `shorelane`, US region, read-only MCP.
- **Query history: mined** — 4,565 rows within the requested 90-day window; 17 admitted clusters and two candidate conflict groups before service-account clarification. These are extraction hints, not accepted metric conflicts. BI roles for `sa-bi-dashboards` and automation roles for `datahub-ingestion` still need confirmation before reclassification. Raw SQL remains gitignored.
- **Dashboard browser: ok** — Executive Revenue Pages dashboard opened using the existing local Chrome MCP. Visible-period embedded Plotly arrays and DOM tiles captured with extraction tiers.
- No `.nodal.local.json` found from the working directory upward at startup; live capabilities were probed directly.

## Human clarification queue
- Whether the discovered dbt remote is durable or a simulation fixture; `repo` omitted until answered.
- Query-history identity classification.
- Owners for the four dashboard domains; all remain `To be confirmed` in the roster and domain metadata.
- Recognized and billed revenue refund-event implementation; do not infer either from the brief’s silence.
- Interview depth and live-check preferences were offered; default scope follows the requested full interview and authorized read-only verification.

## Simulation boundaries
Only the simulated-analyst subagent reads the responses brief. Each question and response is recorded in the configured, gitignored transcript. No commits or pushes during the interview; the user subsequently authorized GitHub publication for review. `.codex/config.toml` preserved byte-for-byte. Generated context uses only elicited answers and explicitly tagged draft extraction candidates.

## Live verification
Capture: `benchmarks/20260915/executive-revenue.capture.json`.
The dashboard’s active Last 12 Months window is 2025-09-01 through 2026-08-31; data as of 2026-09-15. Context-off/on comparison completed: identical values in all three cases, two dashboard numerical matches and one observed order-population mismatch. Current snapshot blessing and dashboard-defect ownership review await the human. No verified SQL sidecar or blessed snapshot seed has been minted.


## Customers resume — 2026-10-01

**Simulation test artifacts only.** Seventeen responder prompts handled this round (the three-item entity batch counted individually). Automated semantic responses are not human approval. All Customers metrics/entities/seeds remain draft, including simulation-supported definitions. Full interview flow was traversed; unresolved choices were escalated asynchronously and must not be inferred from silence.

### Refreshed source disposition
- **dbt: extracted, source fallback** — current project found at `/Users/ronpotok/nodal_code/shorelane-dbt`; 30 documented models, 23 with grain evidence. The existing manifest was generated 2026-09-15; it was not regenerated. Current source was read directly to avoid treating an old manifest as current. Extractor reports exposures unavailable despite an exposures-named source file; no exposure catalog assumed. Findings saved locally under `evals/runs/customers-resume/dbt-findings.json`. Observed remote `https://github.com/shorelane-data/shorelane-dbt.git` remains unratified; no local path or remote added to durable lineage.
- **Warehouse schema probe: ok** — existing BigQuery MCP, read-only SELECT. Observed order/subscription `customer_id` maps to canonical `app_db_customer_id`. Empirical uniqueness holds for inspected customer/order/qualified-alias/source-system keys; this is evidence, not owner confirmation. Statistics stay in local traces, not definitions.
- **Query history: mined, capped coverage** — initial tool output truncated at 50 rows. Reissued emitted extraction inside a single JSON aggregation to obtain the latest 5,000 SELECT jobs from the 90-day request; cap reached. Re-clustering admits zero clusters under existing rules. Do not treat this as absence of BI activity or accepted conflict resolution. Prior `.query-findings.json` and raw rows are preserved; fresh artifacts under `evals/runs/customers-resume/`. Existing service-identity classification queue remains open.
- **Dashboard browser: ok** — existing local Chrome MCP, Customers page. Captured visible Plotly arrays at tier 1.5 and DOM integer tiles at tier 2. Active All / Last 12 Months resolves to 2025-10-01 through 2026-09-30; data as of 2026-10-01. No login/configuration changes.

### Captured Customers work
- Fourteen metric records, including explicit unresolved stubs. Structured ACF 0.1 expressions for current, active, new, current-subscriber and ordered-customer counts. Complex multi-channel grouped eligibility retained as prose; do not flatten it into row filters. First-order channel expression waits for tie policy; alias expressions wait for population scope.
- Subject entities in `entities/customer-subjects.yaml`; no invented Customers-only fact status values. Existing revenue entities unchanged.
- Retrieval routing, human narrative, caveats, lineage (including subscription facts), semantic/correction seeds and a reusable Customers dashboard capture playbook.
- Owner remains `To be confirmed` consistently in domain metadata and company roster.

### Additional human clarification queue — pending
1. Identity bridge grain and identity-quality mart grain/population contract; source suggests qualified alias and source-system grains respectively.
2. Whether current/active customer metrics permit segment breakdowns.
3. Cross-channel tie-breaker for orders sharing the earliest order date.
4. Inclusive pairwise versus exclusive channel-combination buckets.
5. Override if trailing-order current-customer membership differs from subscription-term coverage; preserve separate measures meanwhile.
6. Alias-quality source systems/date/account populations and average IDs/customer numerator/denominator.
7. Returning-share numerator, denominator, prior-order cutoff and disjointness with new customers.
8. Human acceptance of schema-evidenced physical joins/date columns and existing dbt_core lineage. Semantic rules were supported, implementation names were outside responder knowledge.
9. Three live numeric snapshot reconciliations and dashboard-defect ownership review (current, new, multi-channel). No snapshot blessed.

Additional blank-value meanings were not specified by the responder and are not invented. Detailed ticket fallback policy remains outside this Customers capture; use the existing qualified identity routing and clarify any unresolved fallback.

### Customers live verification
- Capture and reconciliation: `evals/captures/20261001-customers/customers.capture.json` and `reconciliation.md`.
- Independent context-off/on traces: `evals/runs/customers-resume/context-off.md` and `context-on.md`. Off began while context capture finished; on ran after context was available. No claim of synchronized execution.
- Current: off 26,033 cumulative purchasers (ambiguity flagged), on 9,812, dashboard 9,906. Difference decomposes into 89 test + 5 internal accounts.
- New: off 4,782, on 4,718, dashboard 4,782. Difference decomposes into 64 test accounts.
- Multi-channel: off/on 2,898, dashboard 2,921. Difference decomposes into 18 test + 5 internal accounts.
- All windows aligned. Literal dashboard equality off 1/3, on 0/3 is not an accuracy score because dashboard eligibility is defective. Responder supports the general hygiene explanation for all three but cannot independently bless current numeric values. Draft correction seeds capture the rule; no blessed snapshot seeds or verified SQL sidecars created.

### Resume next
Collect pending human answers and review the Customers draft, then resolve/verify only affected metrics and snapshots. Preserve the earlier Executive Revenue clarification queue. Marketing and Subscriptions are the remaining untouched domain interviews. Do not silently promote simulation drafts or change configuration. GitHub review publication was subsequently authorized by the user.


## Dashboard repair rerun — 2026-10-02 UTC

User reported fixing the dashboards and requested reevaluation. Fresh local Chrome captures and BigQuery SELECT checks use the dashboards’ active 2025-10-01 through 2026-09-30 window, data as of 2026-10-02.

- Customers: fresh independent off/on agents ran concurrently. Context-on matches all three exact dashboard totals: current 9,812; new 4,718; multi-channel 2,898. Former hygiene discrepancies are resolved for these tested totals.
- Context-off led with account-based current/new interpretations (28,925 / 5,349), but flagged ambiguity and supplied the correct purchase-based alternatives. Primary mapping improves 1/3 to 3/3; do not claim off could not find the right values.
- Executive regression: reran existing SQL forms at refreshed bounds. Orders 15,732; recognized revenue 34,676,505.38; collected cash 35,763,274.81. All match embedded dashboard series at integer/cents precision. This was deterministic regression, not a fresh executive off/on experiment.
- Report: `evals/captures/20261002-rerun/reconciliation.md`; captures alongside it. Query/agent traces: `evals/runs/20261002-rerun/`. Prior reports retained as historical evidence.
- Scoped Customers hygiene caveats and regression seeds to the historical defect; no persistent claim that the repaired tested totals still include excluded accounts. Sigma, other slices, identity-health formulas and returning share remain unverified.
- Numerical dashboard discrepancy items are resolved for tested measures; unrelated human clarification queues and simulation draft status remain. No confirmed snapshot seeds, verified answer-key sidecars, commits, pushes or configuration edits.


## GitHub review handoff

The user authorized committing these additions and publishing to GitHub for review. All simulation definitions and seeds remain draft. Generated captures, run traces, raw query history, the analyst transcript, simulation marker and local MCP configuration remain gitignored; SESSION.md carries the durable evaluation summary.


## Marketing full interview — 2026-10-02

User selected Marketing after completed Executive Revenue and Customers rounds. Resume in place; preserve all prior definitions and queues. The current instruction prohibits commits, pushes and global configuration changes, superseding the earlier review-publication authorization for this round.

### Source disposition
- **dbt: extracted, source fallback**. Rechecked `/Users/ronpotok/nodal_code/shorelane-dbt`; it is present, with remote `https://github.com/shorelane-data/shorelane-dbt.git`. The previously deferred remote-durability question remains unchanged. Current source fallback reports 30 documented models and 23 with grain evidence; exposures unavailable to extractor. Findings in `evals/runs/20261002-marketing/dbt-findings.json`. No dbt build/parse or source edits performed.
- **Warehouse schema probe: deferred, auth**. Existing BigQuery MCP SELECT 1 fails due to expired reauthentication. User was told to run `gcloud auth application-default login`. Reprobed during domain work and before live verification; still unavailable. Physical fields are source-derived drafts, not live schema-confirmed this round.
- **Query history: deferred, auth**. Emitted BigQuery regional JOBS extraction SQL, but could not execute while connection unavailable. Run immediately when probe succeeds, then cluster; prior findings and service-identity clarification queue preserved. No claim of fresh mining.
- **Browser: captured**. Existing local Chrome MCP selected tab was closed; opened the named Marketing dashboard in a new local tab. Last 12 Months, 2025-10-01 through 2026-09-30, data as of 2026-10-02. Visible Plotly arrays tier 1.5; DOM integer/rounded tiles tier 2. No setup/global changes. No local `.nodal.local.json` present at repo root.

### Interview coverage
Fourteen responder questions (including the three-item entity batch), with exact topics and answers used appended to the existing local simulation transcript. The interviewer did not read the configured brief; only the isolated Marketing responder did. No human replies to this round’s escalations have been received.

Captured domain routes, thirteen metric records, subject entities, caveats, retrieval doc, pattern prose, thirteen new eval seeds and a reusable dashboard playbook. All remain simulation drafts. Simple settled aggregation shapes have draft ACF 0.1 expressions; unresolved cross-grain CAC/acquisition, rate and promotion policies are not forced into incorrect row-filter expressions. No schema/version upgrade or edits to prior domain definitions.

Key rules: Marketing revenue means GMV; consumer orders/AOV exclude subscriptions and use period ratios; CAC uses first-ever real d2c acquisitions, not platform claims or repeated platform-row totals; category lines are consumer retail value; marketplace line margin is not Shorelane economic margin; promotion count/GMV are order-level and discounts line-level. Ad platforms differ from commerce channels. Source coverage, incomplete periods, SKU introduction and synthetic intervention limits are explicit.

### Marketing clarification queue
1. Additional Marketing measures beyond the surfaced catalog; observed dashboard adds gross margin by category. Owner remains To be confirmed in domain and roster; preserve prior owner queue.
2. Product/promotion unique keys and safe lookup joins; live schema and key checks deferred.
3. CAC zero-denominator convention and any separate customer-to-platform attribution method. No governed platform CAC without attribution.
4. Human acceptance of consumer AOV implementation mapping; supported by brief examples and labels, not independent dashboard SQL.
5. New-customer order-share numerator: first-ever orders, first-date orders or all period orders from newly acquired customers. Preserve Customers earliest-date/cross-channel tie queue.
6. Category-mix denominator, margin-rate aggregation and d2c-only economic margin scope; dashboard channel filter not established.
7. Blank/unmatched promotion codes, tags outside validity dates, actual-date policy for promotion counts/discounts, exact date bounds and discount fraction encoding.
8. Historical category stability/recategorization and any extra promotion eligibility, stacking or redemption rules.
9. Separate causal/counterfactual or seasonality-adjusted ROI method/source; synthetic paid-media intervention does not define a general estimator.

### Live verification state
Dashboard captured at `evals/captures/20261002-marketing/marketing.capture.json`; dashboard-only arithmetic and limits in adjacent `reconciliation.md`. Internal AOV and CAC arithmetic agrees with rounded tiles, but no warehouse answers were executed and no off/on delta exists. New-customer headline differs from the prior Customers capture; snapshot alignment and order-row versus distinct-customer counting require live investigation, not an inferred correction.

Three pending cases (consumer AOV, CAC, new d2c customers) and resume steps are in `evals/runs/20261002-marketing/verification-plan.json`. Do not mark Stage 5 complete, mint blessed snapshots or verified SQL, or interpret missing authentication as a failed metric. Reauthenticate, re-mine history, verify schema/grain/ties, run isolated parallel off/on agents, refresh capture, then obtain human snapshot review. Subscriptions remains the next domain after Marketing verification/clarifications.


## Marketing authentication recovery and live checks — 2026-10-02

This supersedes the earlier Marketing authentication deferral. User reported renewed credentials. Existing long-lived BigQuery MCP retained stale credentials; a fresh application-default credential probe succeeded. Read-only queries then ran via fresh instances of the same `/opt/homebrew/bin/toolbox --prebuilt bigquery --stdio` MCP configuration and project, with no global/local configuration edits. Tokens were never printed or saved in artifacts.

- **Query history: mined**. Latest 5,000 successful SELECT jobs within requested90-day window; cap reached. Zero admitted clusters under existing classification/thresholds. Prior service-identity classification queue remains; do not infer absence of Marketing BI usage. Artifacts under `evals/runs/20261002-marketing/`.
- **Schema/key checks: executed**. Physical Marketing columns verified from INFORMATION_SCHEMA. Current SKU, promo-code and platform-day keys are empirically unique; no semantic/historical contract inferred. Full SQL and results saved in `evals/runs/20261002-marketing/live/`.
- **Independent off/on runs: executed concurrently**. Off had warehouse/schema only; on read Marketing context and seeds. Neither accessed the analyst brief or dashboard. Only the separate responder consulted the brief.
- **Browser: refreshed**. `evals/captures/20261002-marketing-live/marketing.capture.json`; same Last12Months window2025-10-01 through2026-09-30, dashboard as of2026-10-02.

### Findings
1. Consumer AOV: context-off291.8972 using consumer segment; on292.9154 using real d2c+marketplace orders regardless segment. On matches dashboard embedded components3,539,882.41/12,085 and rounded293 tile. Responder supports channel scope; numeric acceptance escalated and pending.
2. New d2c acquisition:2,428 unambiguous customers plus two first-date cross-channel ties. Inclusive count2,430 matches dashboard acquisition series. Both agents noticed the ties; on did not invent a unique allocation. Owner must choose policy; neither exclusion nor inclusion is automatically approved.
3. CAC: spend1,598,744.59 /2,430 =657.9196 inclusive; /2,428 =658.4615 excluding ties. Both round to dashboard tile658; exact component agreement supports observed inclusive behavior but cannot establish policy.
4. Additional headline discrepancy: Marketing new-customer tile4,720 matches first-date order rows; distinct real first purchasers total4,718. Count-grain explanation is strongly consistent with data, not independently proven from dashboard code. Added a draft correction seed preserving canonical customer grain.
5. Repeated daily acquisition counts agree across platforms for all365 days in window and reconcile to2,430 first-date d2c rows/distinct inclusive customers. Snapshot equivalence does not remove cross-channel ambiguity.

### Remaining work
- Human acquisition tie decision: count in every first-day channel versus uniquely attribute using an agreed first-order/timestamp rule (or leave open). Source/timestamp suitability must be verified before implementing a new rule. This is shared with the preserved Customers tie queue.
- Human AOV snapshot acceptance and review/fix of the Marketing new-customer headline grain.
- Earlier Marketing policy questions remain unless explicitly answered; no replies received as of this update.
- No blessed snapshot seeds or verified SQL sidecars minted. One numerical AOV agreement plus two policy-conditional comparisons; no3/3 accuracy claim.
- Marketing now has14 draft seeds. Report: `evals/captures/20261002-marketing-live/reconciliation.md`. Simulation transcript appended. No commits, pushes or configuration changes; previous domain files remain unchanged. Subscriptions remains next untouched interview domain.


## Human review decisions — 2026-10-02

- User explicitly accepted the consumer AOV reconciliation: consumer GMV divided by real d2c+marketplace orders for the captured period. This resolves the pending numeric acceptance and consumer-channel scope question for that case.
- User explicitly directed distinct counting for the total new-customer metric: each canonical customer once, regardless of multiple first-date orders. The observed total is4,718, not4,720 first-date order rows.
- These decisions do not yet settle which channel receives acquisition credit when first-date orders span channels. The CAC denominator’s d2c attribution remains open.
- Preserve simulation-artifact labeling and draft status under the session instructions; do not infer approval of other definitions, snapshots or production use.


## Human CAC timestamp rule and follow-up verification — 2026-10-02

- Human chose earliest purchase timestamp across all channels for CAC first-time acquisition. Count distinct canonical customers whose first order is d2c; determine first purchase over all history before period/channel restrictions. This supersedes the prior open first-date versus timestamp policy for CAC, without closing unrelated Customers questions.
- Rechecked local dbt staging source and live raw-source metadata. Original `shorelane_raw.app_db__orders.order_date` retains timestamps; staging casts to date. Joined raw timestamps to eligible fact orders by order_id. Raw order IDs unique; no eligible orders missing timestamps.
- Timestamp verification for the same Oct 2025–Sep 2026 window still finds two exact cross-channel ties: cust_024587 at 2025-11-20T00:00:00Z (d2c/subscription); cust_029216 at 2026-09-30T00:00:00Z (d2c/marketplace). Therefore the chosen timestamp rule does not yet determine their acquisition channel.
- Distinct total new customers remains 4,718; unambiguous first-channel d2c acquisitions remain 2,428. Spend remains 1,598,744.59. The 658.4615 CAC excluding unresolved cases is diagnostic, not a final approved CAC; do not silently exclude ties.
- Responder is NOT_CONFIDENT: permitted brief supplies neither secondary ordering nor higher-resolution source, and does not establish order_id chronology. Escalate that remaining atom to human. No arbitrary ID/channel priority adopted.
- Updated Marketing definitions, retrieval routing and existing eval seeds together; simulation labels/draft status retained. AOV acceptance and distinct-count decision retained. No other domain files changed.
- Evidence: `evals/runs/20261002-marketing/live/marketing-timestamp-cac.{sql,json}` plus timestamp schema probes. No new approved snapshots or 3/3 correctness claim. Remaining work: resolve exact-time ties, rerun final CAC/acquisition and reconcile dashboard; retain earlier Marketing clarification queue and untouched Subscriptions next. No commits, pushes or configuration changes.


## Human deterministic tie assignment — 2026-10-02

- User accepted deterministic random assignment for identical earliest purchase timestamps. Fixed implementation before evaluation: lowest lowercase SHA-256 hex over compact UTF-8 JSON array `["shorelane-cac-first-order-v1", canonical customer_id, order_id]`; order_id ascending is collision-only fallback. Timestamp remains primary; rank all-channel lifetime orders before period/channel filters. Preserve a tie-assigned flag. This closes the CAC tie-policy queue; it does not infer purchase chronology or resolve unrelated Customers attribution questions.
- BigQuery MCP read-only rerun for 2025-10-01 through 2026-09-30: distinct total new customers 4,718; new d2c 2,429; spend $1,598,744.59; CAC $658.190444627. cust_024587 selects d2c order ord_0066997; cust_029216 selects marketplace order ord_0080637. Independent Python SHA-256 reproduction agrees with both BigQuery selections.
- Compared with the existing captured dashboard: acquisition count 2,430 differs by one; rounded CAC tile 658 conceals the difference. Dashboard/dbt implementation has not been changed by this context task. AOV acceptance and distinct total-customer policy remain accepted.
- Updated Marketing context, metrics and seeds; added dedicated timestamp-tie seed (15 Marketing seeds). Simulation test artifact labels and draft status retained. Evidence: `evals/runs/20261002-marketing/live/marketing-deterministic-cac.{sql,json}`. No newly blessed snapshots, no fresh independent off/on rerun claimed.
- Remaining work: downstream dashboard/dbt adoption and numeric review of revised CAC, CAC zero-denominator behavior, and the existing unrelated Marketing clarification queue. Subscriptions remains next domain. No commits, pushes or global configuration changes.


## Review publication authorization — 2026-10-02

User requested committing the current Marketing additions to a new branch and sending them to GitHub for review. This supersedes the earlier no-commit/no-push restriction for this publication only. Simulation draft labels and remaining clarification queues are preserved. Local transcript, query results and captures remain gitignored. Repository validation passed with 70 documents and no schema errors; no dashboard/dbt implementation changes are included.


## Subscriptions full interview — 2026-10-02 (in progress)

User confirmed in-place continuation at `/Users/ronpotok/codex-demo`, with Executive Revenue, Customers and Marketing rounds complete and their outstanding queues preserved. Current main includes merged Marketing PR #7. No commit/push/global configuration changes authorized for this round.

### Sources
- dbt: rechecked `/Users/ronpotok/nodal_code/shorelane-dbt`, present, remote `https://github.com/shorelane-data/shorelane-dbt.git`. Source-fallback extraction found 30 documented models, 23 with grain evidence; exposures unavailable to extractor. Prior durable-remote confirmation queue remains; no dbt code/build/parse changes.
- Warehouse: long-lived MCP still had stale reauthentication state; fresh instance of the same BigQuery toolbox MCP/project succeeded. Schema, grain, eligibility and renewal-link checks executed read-only. No new authentication or configuration changes required.
- Query history: mined latest 5,000 successful SELECT jobs within requested 90 days, row cap reached. 794 clustered shapes, zero admitted clusters and no BI-service pool under current classification. Prior service-identity question preserved; zero admission does not establish absent BI usage.
- Browser: existing local Chrome MCP opened the named Subscriptions dashboard. Visible Plotly embedded arrays captured at tier 1.5 and DOM tiles at tier 2; Last 12 Months resolved to 2025-10-01 through 2026-09-30, stock date 2026-09-30, dashboard freshness 2026-10-02. Raw capture and normalized capture under `evals/captures/20261002-subscriptions/`. Direct browser file-save was unavailable under its declared roots; tool result saved through workspace file tooling, no browser config changed.

### Interview capture
Eleven responder questions cover domain, canonical term fact, stock/flow metrics, new seat pricing, renewal/churn, lifecycle and plan entities, as-of grandfathering, pricing, timing, source routing and read-back. Only isolated `subscriptions_responder` read the configured brief. Answers and escalations appended to the existing local simulation transcript. Twelve metric definitions and twelve new seeds plus subject/status entities and dashboard playbook are simulation drafts. Earlier domain files/seeds are preserved.

### Open human clarifications
1. Named accountable Subscriptions owner (FP&A audience does not establish owner).
2. Zero-denominator convention for subscription ratios.
3. Observed leap-day date exception: sub_0004780 ends 2024-02-27 and linked sub_0007097 starts 2024-02-29 for cust_002694. Honor stored dates with flagged gap versus upstream correction. No date mutation authorized or performed.
4. Historical reports based on currently loaded outcomes versus a historical knowledge-as-of contract; the latter is not supported by established history.
Other limitations retained: exact tier mapping semantic review; previous dbt durability/service-identity queues; no per-ticket causal attribution/general causal estimator for the documented synthetic billing incident.

### Live checks
All 15,321 term IDs unique; no null key/date fields, overlapping terms, multiple renewal successors, ineligible customers or ACV formula discrepancies found. One next-day renewal boundary exception above. These are observed properties, not production contracts.
Four question cases dispatched concurrently to isolated context-off/on agents: active book, new subscriptions/seat pricing, renewal/churn and grandfathered share. Neither agent can read brief/dashboard/other outputs; off has warehouse evidence only. Results and human numerical review pending. No confirmed snapshots or blessed SQL minted.


### Subscriptions live verification outcome — 2026-10-02
- Independent context-off/on agents completed all four cases with identical values: active subscribers 3,647; ACV 35,572,445.28; new subscriptions 1,151; new ACV/seat 236.920793813; ending renewed terms 2,498; churned 550; renewal rate 81.9553805774%; churned ACV 3,823,645.44; grandfathered 960/3,647 = 26.3230052098%. No context-on improvement claim. Subagent MCP instances worked directly; interviewer used fresh same-config MCP as recorded above.
- Dashboard: three exact comparisons, three agreements at displayed precision; grandfathered share has only indirect generation-count support (no direct visible tile). Human acceptance/tolerance remains pending, so zero of four cases are human-reviewed and no snapshots/verified SQL blessed.
- Monthly renewal bars total 2,496; separate warehouse read finds 2,496 renewal starts versus 2,498 renewed ending terms. Ending cohort has zero undecided terms or status/link conflicts. Cohort difference is evidence-backed, but the responder cannot confirm the chart's intended anchor; human question remains pending. Added a clarification seed without changing the governed ending-term rate.
- Responder numeric reference is pinned to December2025 and cannot approve the current October2026 snapshot. Current numerical and chart-anchor escalations appended to existing transcript. Earlier ownership, zero-denominator, leap-day gap and historical-knowledge questions remain pending; no human replies received as of this update.
- Round has 12 metric drafts and 13 new seed drafts. Final report: `evals/captures/20261002-subscriptions/reconciliation.md`; resume state: `evals/runs/20261002-subscriptions/verification-plan.json`; independent traces in `off/` and `on/`. Interview capture and live execution complete; human review/deferred clarification remain. Do not label fully verified.
- Remaining work: resolve the six human clarification groups, reconcile monthly renewal presentation, obtain direct grandfathered benchmark if desired, then rerun only affected checks. Prior Executive Revenue, Customers and Marketing queues remain untouched. No new domain automatically selected. No commits, pushes or global configuration changes.


### Subscriptions human acceptance — 2026-10-02
- User accepted the compared values for October2025–September2026: active subscribers and book ACV, new subscriptions and new ACV/seat, renewal rate and churned ACV, with exact versus displayed precision as shown. Three of four verification cases are now human-reviewed; grandfathered share remains pending by explicit request. Acceptance does not upgrade all simulation definitions to production-confirmed status.
- User selected monthly renewal starts for Renewals bars, while renewal rate uses ending-term decisions. Context, a separate renewal_starts metric, existing chart-anchor seed and capture playbook now state both cohorts explicitly. In the tested window, 2,496 renewal starts and 2,498 renewed endings are intentionally different counts; no data correction is implied.
- Subscriptions now has13 metric drafts and13 new seed drafts. Grandfathered numeric review, owner, zero denominators, leap-day gap and historical-knowledge policy remain pending; unrelated prior queues preserved. Simulation labels/draft status retained. No warehouse, dbt, dashboard, commit, push or configuration changes.


### Subscriptions review publication authorization — 2026-10-02
User requested committing the current Subscriptions additions on a new branch and sending them to GitHub for review. This supersedes the prior no-commit/no-push instruction for this publication only. Simulation draft labels and outstanding queues are retained. Local transcript, captures and raw query artifacts remain gitignored. Validation passed for 84 documents with zero errors.
