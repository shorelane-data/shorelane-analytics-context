# Context-on simulation trace

```json
{
  "mode": "context_on",
  "simulation_only": true,
  "as_of_date": "2026-09-15",
  "question": "How many orders did we have?",
  "metric": "orders",
  "value": 15571,
  "sql": "SELECT COUNT(*) AS orders\nFROM `nodal-shorelane.shorelane.fct_orders`\nWHERE order_date >= DATE '2025-09-01'\n  AND order_date < DATE '2026-09-01'",
  "assumptions": [
    "Count one eligible order per fct_orders row.",
    "Governed orders exclude test/internal accounts and retain real customers.",
    "No additional mandatory order-status exclusion is specified.",
    "Count orders placed during the period.",
    "Draft elicited definitions are authorized for this simulation comparison only."
  ],
  "tables": [
    "nodal-shorelane.shorelane.fct_orders"
  ],
  "time_window": {
    "field": "order_date",
    "start_inclusive": "2025-09-01",
    "end_exclusive": "2026-09-01"
  }
}
```

## Method
Read the specified context and relevant seeds; inspected both table schemas using BigQuery MCP; executed three separate read-only aggregates without joins. The period ends at the last fully elapsed calendar month before September 15.

## Verification
Both measures have zero null amounts and activity in all 12 months, September 1 through August 31. Orders have 15,571 rows, 15,571 distinct IDs, zero null IDs, and the same date coverage.

## Limitations / WARN
Simulation drafts without human approval; recognized refund internals unresolved; currency not established in inspected context (amounts returned without symbols). Current tables, not immutable historical snapshots. No dashboard/independent trusted result accessed. Coverage is not proof of source completeness. Metadata loads: revenue 2026-09-15T07:16:10.289-04:00; orders 2026-09-15T07:16:10.388-04:00. Agent review WARN; medium overall confidence, uncalibrated heuristic plan support 0.675 and post-query support 0.90 (not probabilities). Human review needed for production.
