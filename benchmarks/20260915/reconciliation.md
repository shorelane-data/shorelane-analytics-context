# Executive Revenue — simulation reconciliation

**Window:** 2025-09-01–2026-08-31, both endpoints inclusive. **Dashboard as of:** 2026-09-15. Active control: Last 12 Months. Monthly grain; current partial month excluded. Warehouse tables loaded September 15; this is a current-table comparison, not an immutable historical snapshot.

| Widget / measure | Dashboard (tier 1.5) | Context off | Context on | On − dashboard | Observation |
|---|---:|---:|---:|---:|---|
| Orders | 15,787 | 15,571 | 15,571 | −216 (−1.37%) | Value mismatch; windows agree |
| Recognized revenue | 33,888,811.17 | 33,888,811.17 | 33,888,811.17 | 0 | Exact agreement at cents; human blessing pending |
| Collected cash | 35,337,042.60 | 35,337,042.60 | 35,337,042.60 | 0 | Exact agreement at cents; human blessing pending |

All dashboard totals above are derived by summing decoded embedded monthly Plotly series from the visible panel. No decimals were invented from rounded headline tiles. The page displays currency with a dollar symbol; this interview has not established a currency code. Tolerance remains for the human analyst to accept; matches are observations, not blessed truth.

## Order discrepancy
A separate read-only staging census returned 15,571 customer orders, 139 test orders, and 77 internal orders. The latter two account for the complete 216-order excess. The simulated analyst supports the eligible-order rule but its brief does not establish this specific chart defect. Preserve the rule and retain the observed defect for owner review.

## Off → on result
The independent agents returned identical values for all three cases. Both agree numerically with two of three dashboard series; **there was no numeric uplift from context in this sample**. The context-on trace grounds defaults, hygiene, event dates and refund handling in elicited definitions; context-off states those as assumptions. Dashboard agreement is not an accuracy score, particularly where the dashboard appears to include excluded accounts.

## Review state
Three comparisons executed: two numerical matches and one mismatch. Current revenue/cash snapshots and the specific order-chart defect are unblessed. The brief covers older dashboard references, not these current figures. No value_at_snapshot seed or verified SQL answer key was created. All context and seeds remain draft simulation artifacts, excluded from the perfect baseline.

See the six agent traces, preflight checks and order-population reconciliation in this directory.
