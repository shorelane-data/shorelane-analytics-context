# Catalog-Margin Reference

<!-- status: draft — simulated (catalog-001); owner, d2c-only margin and ratio-of-totals human-decided. -->

## Quick Reference
- **Business context** — consumer sales by category / SKU, and gross margin on Shorelane-owned (d2c) inventory.
- **Entity grain** — `fct_order_lines`: one consumer order line from a real customer. Subscription orders have no lines.
- **Standard hygiene filter** — the mart (real customers); margin restricted to `channel = 'd2c'`.
- **Canonical table** — `nodal-shorelane.shorelane.fct_order_lines`

## Routing triggers
- IF gross margin / margin % → `gross_margin` / `gross_margin_pct` (= `gross_margin` ÷ `d2c_line_revenue`) on d2c lines only; ratio of totals. DO NOT average per-line margin %; DO NOT include marketplace lines.
- IF category revenue / product mix → `line_revenue` (d2c + marketplace consumer lines); say it is consumer GMV at line grain, not total revenue, and that marketplace lines are seller retail.
- IF "total revenue by category" → only consumer channels have categories; subscriptions have none — say so.
- IF supplier → one supplier per category, so a supplier cut repeats the category cut.
- IF seller / merchant → decline: no seller identifier exists; category is not a seller proxy.
- IF refunds by category → refunds attach to orders (net amount), not lines; line figures are gross of refunds.

## Dimensions
- `category` (paper, writing, office_tech, furniture, breakroom, storage), `sku`, `supplier_id`, `channel` (d2c / marketplace only).
- `line_amount` is net of `discount_pct` (warehouse-checked); discount dollars = quantity × unit_price × discount_pct.

## Key tables
### fct_order_lines   ← canonical
- **Grain**: one consumer order line  ·  **Use for**: category / SKU revenue, margin, discounts  ·  **Join keys**: `order_id` → `fct_orders`

### dim_products
- One row per SKU with category and unit cost (a single cost per SKU; no cost history).

## Gotchas
- Category mix drifts as SKUs were added after founding — not a demand shift.
- March 2023 paper outage: paper's share fell because no stock arrived (supplier shipments), not demand.
- Staging / raw order lines include test and internal accounts; the mart excludes them.

## Common query patterns
- Margin % by category: SUM(gross_margin) ÷ SUM(line_amount) over d2c lines, grouped by category.

## Cross-references
- `domains/marketing/reference.md` (category charts), `domains/revenue/reference.md` (marketplace take).
