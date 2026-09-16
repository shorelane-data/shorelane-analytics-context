# Shorelane simulation session

**Simulation test artifacts only.** All authored definitions and eval seeds remain draft; no simulated response constitutes human confirmation.

## Scope
Full first-domain round: Executive Revenue. Customers, Marketing and Subscriptions are discovered dashboard domains saved as draft follow-up work. Company glossary captures ten terms.

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
Only the simulated-analyst subagent reads the responses brief. Each question and response is recorded in the configured, gitignored transcript. No commits or pushes. `.codex/config.toml` preserved byte-for-byte. Generated context uses only elicited answers and explicitly tagged draft extraction candidates.

## Live verification
Capture: `benchmarks/20260915/executive-revenue.capture.json`.
The dashboard’s active Last 12 Months window is 2025-09-01 through 2026-08-31; data as of 2026-09-15. Context-off/on comparison completed: identical values in all three cases, two dashboard numerical matches and one observed order-population mismatch. Current snapshot blessing and dashboard-defect ownership review await the human. No verified SQL sidecar or blessed snapshot seed has been minted.
