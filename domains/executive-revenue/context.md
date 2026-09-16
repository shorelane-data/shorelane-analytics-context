# Executive Revenue

> Simulation test artifact; human review pending. <!-- status: draft -->

Use fct_revenue for period revenue totals: exactly one measure_name, explicit activity_date bounds, SUM(signed amount). Rows are dated contributions to measures, not orders or customers; measures are non-additive and row counts have no business meaning. fct_orders is one eligible order per row, for counts, canonical channels/customers and order-date gross/net amounts; these do not replace recognized, billed or collected events. stg_orders includes test/internal accounts. Refunds are negative rows where applicable in fct_revenue; do not subtract them twice.
