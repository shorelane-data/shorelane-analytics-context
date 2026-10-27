# Customers Reference

<!-- status: draft — simulated-analyst answers (company-002, customers-001); owner and new-customer counting human-decided. -->

## Quick Reference
- **Business context** — who counts as a Shorelane customer: real, deduplicated, canonical customers, and how healthy identity resolution is.
- **Entity grain** — the canonical real customer (`app_db_customer_id`). `dim_customers` = one row per canonical profile (incl. never-ordered); `fct_orders` = one row per order from a real customer.
- **Standard hygiene filter** — real customers only: marts already exclude test/internal (`dim_customers` still carries `account_type` — filter `account_type = 'customer'` there). Count distinct `customer_id`.
- **Canonical table** — `nodal-shorelane.shorelane.dim_customers` (profiles); counts over a period come from `fct_orders`.

## Routing triggers
- IF "how many customers do we have" → `current_customers`: orderers in any channel (including business subscriptions) in the trailing twelve calendar months ending at the snapshot month; state the window. <!-- channel scope human-decided 2026-10-27 at Stage 5 (dashboard match) -->
- IF returning customers / returning share → `returning_customers` (active − new) and `returning_share` (returning ÷ active).
- IF multi-channel customers → active customers in the period whose orders span ≥2 canonical channels (merge raw `direct` into d2c); drawn from period actives, not current customers.
- IF active customers in a period → `active_customers` (distinct customers with any order in the period).
- IF new customers → `new_customers`: COUNT(DISTINCT customer_id) where `is_first_order`; DO NOT count flagged rows (some customers have two flagged first orders).
- IF new customers by channel → the channel of the customer's first-ever order; a first order in a new channel after ordering elsewhere is NOT new.
- IF "customers who have ever ordered" → `ordered_customers` (`dim_customers`, `has_order`, `account_type = 'customer'`).
- IF all `dim_customers` rows are proposed as a customer count → DO NOT; never-ordered profiles are not customers.
- IF source IDs / aliases (`int_customer_identity`, Stripe/Shopify/Salesforce IDs) are proposed as a customer count → DO NOT; aliases are an identity-quality figure only.
- IF any `stg_*` table (e.g. `stg_orders`) is the source → DO NOT; it includes test and internal accounts.
- IF joining source-system tables to customers → LEFT join the crosswalk on (`source_system`, `source_customer_id`); never inner join; deduplicate to the canonical customer before joining orders (recreated Stripe accounts fan out).
- IF identity health / unresolved aliases → `fct_identity_resolution_quality` (per source system); unresolved means unknown, never an extra customer.

## Dimensions
- `channel` — canonical (`fct_orders.channel`); per-channel counts overlap and sum to more than the total. See `entities/channel.yaml`.
- `segment` — consumer / smb / enterprise; on both `fct_orders` and `dim_customers` (identical — warehouse-checked); fixed per customer; not the same as channel.
- `acquisition_channel` (`dim_customers`) — canonical channel of the first order, or `signup` for never-ordered accounts.
- `resolution_status` (`int_customer_identity`) — see `entities.yaml`.

## Key tables
### dim_customers   ← canonical
- **Grain**: one canonical app customer profile  ·  **Scope**: includes never-ordered profiles and test/internal account types
- **Use for**: ever-ordered counts, segment / acquisition attributes, multi-source flags  ·  **Required filters**: `account_type = 'customer'`; `has_order` for customer counts
- Use `resolved_source_system_count` (not alias count) for multi-source eligibility.

### fct_orders
- **Grain**: one order from a real customer at canonical channel  ·  **Use for**: active / new / current customer counts over a period
- **Join keys**: `customer_id` → `dim_customers.app_db_customer_id`

### int_customer_identity, fct_identity_resolution_quality
- Identity bridge (one row per observed source alias, left-joined) and its per-source-system rollup. Quality figures only — never customer counts.

## Gotchas
- Raw source-ID counts several times overstate real customers.
- Unresolved aliases: migration-gap ones are permanent (pre-2021-07-01 Shopify/Salesforce profiles with no crosswalk row); sync-lag ones resolve late. Neither is a new customer.
- Per-channel active counts overlap; don't sum channels for a total.
- Subscription rows are terms, not customers; "subscribers" means canonical customers.
- Invoices, refunds and Zendesk tickets carry source-native IDs (Stripe / Salesforce) — reach the customer via `order_id`, or the crosswalk for tickets.
- Rolling "last 12 months as of today" moves daily; use explicit bounds ending at a completed month.

## Common query patterns
- Current customers: distinct `customer_id` on `fct_orders` (all channels), `order_date` in the twelve calendar months ending at the snapshot month.
- New customers in a period: distinct `customer_id` on `fct_orders` with `is_first_order` and `order_date` in the period.

## Cross-references
- `domains/revenue/reference.md` — revenue by customer routes through `order_id` → `fct_orders.customer_id`.
