# Shorelane simulation session

**Simulation test artifacts only.** All authored definitions and eval seeds remain draft; no simulated response constitutes human confirmation.

## Scope
Executive Revenue interview round complete, with its work and clarification queue preserved. Customers full flow resumed in place on 2026-10-01: domain routing, metrics, entities, caveats and three live off/on comparisons captured; human clarifications and snapshot blessings remain pending. Marketing and Subscriptions remain draft follow-up domains. Company glossary captures ten terms.

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
