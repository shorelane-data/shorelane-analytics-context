> **SIMULATION TEST ARTIFACT:** These benchmarks were run against context produced by a simulated-analyst interview. Seeds are `status: draft`; automated grades are not human approval.

# Benchmarks

Published evaluation runs for this context repo. Each run answers the same business
questions twice — once with the authored context loaded (**context on**) and once with
only the raw warehouse available (**context off**) — so the uplift from the context
layer is measured, not asserted. Every artifact that produced a number is committed
alongside it.

## Headline: all-seed blinded benchmark (`20260915-2/`)

23 seeds, 46 answers graded, zero skipped. One answering agent per condition, one
sample per seed, read-only BigQuery, date anchor 2026-09-15.

| Condition | Passed | Pass rate |
|---|---:|---:|
| Context off | 14/23 | 60.9% |
| Context on | 19/23 | 82.6% |

**Delta: +21.7 percentage points** (+5 passed seeds).

| Domain | Seeds | Off passed | On passed |
|---|---:|---:|---:|
| customers | 3 | 1 | 3 |
| executive-revenue | 16 | 12 | 12 |
| subscriptions | 4 | 1 | 4 |

Read [`20260915-2/report.md`](./20260915-2/report.md) for the per-seed grader
explanations, the two regressions, the two seeds that failed under both conditions,
and the illustrative answer differences (for example, "current customers": 28,930
known profiles with context off versus 9,678 eligible trailing-year purchasers with
context on).

## Dashboard reconciliation (`20260915/`)

A separate three-question round compared context-off and context-on answers against
the public
[Shorelane executive dashboard](https://shorelane-data.github.io/shorelane/business/)
over its Last 12 Months window (2025-09-01 to 2026-08-31, as of 2026-09-15).
Recognized revenue and collected cash matched the dashboard to the cent. Orders did
not: the dashboard showed 15,787 and the governed answer 15,571. A read-only staging
census in [`order-discrepancy.md`](./20260915/order-discrepancy.md) traced the
216-order excess exactly to 139 test orders and 77 internal orders that the
dashboard includes and the governed mart excludes. That dashboard defect awaits
owner review. See [`reconciliation.md`](./20260915/reconciliation.md).

Note this round found **no numeric uplift from context**: both conditions returned
identical values on all three questions. The uplift shows up in the harder all-seed
benchmark above.

## How the all-seed benchmark was run

- Questions and expected fields were frozen before the run
  ([`frozen-seeds.json`](./20260915-2/frozen-seeds.json), [`cases.json`](./20260915-2/cases.json)).
- Neither answering agent could read seeds, intent, expected answers, previous traces,
  the transcript, or the responses brief. Only context-on received the frozen
  `company/`, `domains/`, `entities/` files. Both received the same as-of date and
  warehouse.
- An independent grader saw the two candidates per seed shuffled A/B with no
  condition mapping ([`blind-mapping.json`](./20260915-2/blind-mapping.json)), and
  graded semantic compliance against the frozen fields under a pre-registered
  [`grading-policy.md`](./20260915-2/grading-policy.md).
- One re-grade pass was needed after the blinded packet omitted the shared as-of
  date; the pre-audit grades are preserved in
  [`grades-blinded.initial.json`](./20260915-2/grades-blinded.initial.json) and the
  change is documented in [`grading-audit.md`](./20260915-2/grading-audit.md).
- Exact executed SQL for every answer is in
  [`off-answers.json`](./20260915-2/off-answers.json) and
  [`on-answers.json`](./20260915-2/on-answers.json).

## Reproducibility

[`manifest.json`](./20260915-2/manifest.json) records a SHA-256 hash of every context
file the context-on agent received. Those hashes match the files committed to this
repo at commit `a203714` (28 of 28), so the benchmark is verifiably against the
published context. Re-check from the repo root:

```bash
python3 - <<'PY'
import hashlib, json
m = json.load(open('benchmarks/20260915-2/manifest.json'))
bad = [p for p, h in m['source_hashes'].items()
       if hashlib.sha256(open(p, 'rb').read()).hexdigest() != h]
print(f"{len(m['source_hashes'])} files checked, {len(bad)} mismatches", bad)
PY
```

The two helper scripts in `20260915-2/` (`prepare_grading.py`, `build_report.py`)
are committed as frozen artifacts and still reference the original working paths
(`evals/runs/...`, `evals/captures/...`) from which this directory was assembled.

## Limitations

Stated in the manifest and report, and repeated here so the headline is not read
without them:

- One sample per seed per condition; no statistical significance claim.
- Questions run as a batch within each condition, so within-condition context can
  carry between cases.
- Draft seed expectations are provisional simulation rubrics, not human-certified
  ground truth.
- Some seeds contain overlapping questions and broad multi-clause expectations.
- The context and the seeds came from the same simulated interview; the report's
  "Rubric caveats" section names the seeds whose expected fields are broader than
  their questions.
- Results are current-table observations, not immutable warehouse snapshots.
- Warehouse metadata incidentally exposed some view definitions to both conditions;
  the per-answer artifacts record that reliance.

## Contents

| Path | What it is |
|---|---|
| [`20260915-2/`](./20260915-2/) | All-seed blinded benchmark: report, results, manifest, grading policy and audit, blinded grades, frozen seeds, grader input, full on/off answers with SQL, helper scripts. |
| [`20260915/`](./20260915/) | Dashboard reconciliation: capture, reconciliation report, preflight grain checks, order-discrepancy census, six per-question agent traces (on/off). |
| [`interview-transcript.md`](./interview-transcript.md) | The 34-question simulated-analyst interview (Stages 0–5) that produced this context, showing which answers were confident and which were escalated. Two local identifiers redacted. |
