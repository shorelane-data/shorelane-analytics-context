# Verification preflight — simulation only

Read-only BigQuery MCP and local Chrome MCP are live. Revenue schema: activity_date, measure_name, amount. Order fact has order_id, customer_id, channel and order_date.

Empirical grain check: fct_orders has 78,710 rows and 78,710 distinct order_id values; dim_customers has 28,930 rows and 28,930 distinct app_db_customer_id values. Counts are diagnostic snapshot output only.

## Isolation
Two agents run concurrently on three cases, using the same date window and as-of date. Context-off uses only warehouse metadata and SELECTs. Context-on reads the simulated interview context and seeds; neither receives dashboard captures or the responses brief. Analyst review remains separate and sequential.

## Cases
1. What was our revenue?
2. How much cash did we collect?
3. How many orders did we have?

Window: 2025-09-01 inclusive through 2026-08-31 inclusive. As of 2026-09-15.
