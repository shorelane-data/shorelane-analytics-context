# Observed order-count discrepancy

Dashboard tier-1.5 monthly series sum: 15,787. Off/on governed results: 15,571. Same Sep 2025–Aug 2026 window, as of 2026-09-15.

Follow-up executed read-only SQL:
```sql
SELECT c.account_type, COUNT(*) AS order_count FROM `nodal-shorelane.shorelane.stg_orders` o LEFT JOIN `nodal-shorelane.shorelane.stg_app_customers` c ON o.customer_id = c.app_db_customer_id WHERE o.order_date >= DATE '2025-09-01' AND o.order_date < DATE '2026-09-01' GROUP BY c.account_type ORDER BY c.account_type
```

Result: customer 15,571; internal 77; test 139. Staging total 15,787. The 216 excess equals test/internal orders. Rule supported by simulated analyst; this particular dashboard defect awaits human owner review.
