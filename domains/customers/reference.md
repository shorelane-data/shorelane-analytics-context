# Customers Reference

> SIMULATION TEST ARTIFACT — status: draft throughout; no human confirmation. Apply only as a labeled simulation hypothesis until reviewed.

## Quick Reference
- **Entity grain:** dim_customers has one row per canonical app_db_customer_id. A profile may never order.
- **Canonical customer table:** dim_customers. Use fct_orders for dated order activity and channels; fct_subscriptions for term coverage.
- **Hygiene:** account_type = customer; exclude test/internal. Customer-count metrics require the relevant order activity, except subscriber eligibility which follows term coverage.
- **Aliases:** live schema/dbt map fct_orders.customer_id and fct_subscriptions.customer_id to dim_customers.app_db_customer_id. These physical column spellings are extraction evidence, not new business definitions.

## Routing triggers
- IF asked for current customers → count distinct canonical customers with orders in twelve complete calendar months ending with the reporting month; DO NOT count profiles or use a partial month/rolling day window.
- IF asked for active customers → use orders within the selected period; DO NOT substitute current-customer snapshot membership.
- IF asked for new customers → use first-ever order across all channels; DO NOT use profile creation, profile acquisition_channel or first purchase in each channel. For channel attribution, unresolved cross-channel earliest-date ties require clarification.
- IF asked for multi-channel customers → count distinct canonical customers with orders in at least two canonical channels within the selected period; DO NOT require current-customer membership. Pairwise bucket exclusivity remains unconfirmed.
- IF comparing channels → normalize direct to d2c and deduplicate the overall total; DO NOT sum overlapping channel counts.
- IF asked for current subscribers → use distinct real customer IDs with term_start_date <= month-end <= term_end_date; DO NOT count terms or seats or filter subscription status, plan is_current or Stripe is_active.
- IF trailing-order eligibility and subscription coverage disagree → report the separate metrics and clarify the override; DO NOT invent a hybrid current total.
- IF matching dashboard counts → preserve governed eligibility and compare aligned windows. The historical Customers hygiene discrepancy is repaired for the tested current/new/multi-channel totals; Sigma and other slices have not been revalidated. DO NOT assume every surface shares the repaired filters.
- IF resolving source IDs → LEFT JOIN on (source_system, source_customer_id), preserve unresolved aliases as unknown quality findings; DO NOT count them as new customers or join on raw ID text alone.
- IF measuring source coverage → count distinct source systems, not aliases; DO NOT treat an inactive historical Stripe alias as an inactive customer. Deduplicate canonical IDs before joining order facts.
- IF asked for alias-quality rates or average IDs/customer → clarify source/date/account population and formula; DO NOT inherit ordered-customer filters silently.
- IF asked for returning share, segment slices or exact channel-combination buckets → consult the open clarification queue; DO NOT invent missing definitions.
- IF asked for NPS, store visits, customer shipping cost or return reasons → state that available data cannot answer it.

## Key tables and dimensions
- dim_customers: canonical customer profiles, account type, segment, first-order and has_order fields. Filter eligibility explicitly when using this dimension. Current dimension is not proven to reconstruct historical snapshots.
- fct_orders: one order per real customer, canonical channel and order date. `is_first_order` flags earliest-date orders; it is not a proven unique first-order selector for channel ties.
- fct_subscriptions: one subscription term per row; customer_id links canonical customer. Use date coverage at customer grain.
- int_customer_identity: qualified source alias bridge. dbt-derived candidate grain is one (source_system, source_customer_id); human contract confirmation pending.
- fct_identity_resolution_quality: dbt-derived candidate grain is source_system with observed/resolved/unresolved alias counts and unresolved/observed ratio; human population and grain confirmation pending.
- Canonical channels: d2c (including historical direct), business_subscription, marketplace. Segments consumer/smb/enterprise are not eligibility substitutes and do not imply exclusive purchasing channels.

## Gotchas
- Some Shopify/Salesforce profiles before 2021-07-01 permanently lack crosswalk mappings; recent aliases can take up to thirty days to link.
- All-time multi-channel customers can exceed the current snapshot; the metrics use different windows.
- Invoice/refund attribution follows order_id to fct_orders. Ticket resolution needs a qualified identity path; detailed fallback policy is not captured in this domain.

## Common query patterns
- Current: select eligible orders in the twelve full months ending reporting month; deduplicate canonical IDs at each output month.
- New: establish earliest order across all channels before filtering the acquisition period; do not rank separately within each channel.
- Multi-channel: filter eligible orders to the requested period, normalize channels, group by canonical ID, retain customers with at least two distinct channels, then count customers.
- Identity joins: retain unresolved aliases for quality; reduce resolved aliases to distinct canonical IDs before facts to prevent fanout.

## Cross-references
- [Metrics](metrics.yaml), [issues](known-issues.md), [customer entities](../../entities/customer-subjects.yaml).
- [Executive Revenue](../executive-revenue/reference.md) owns revenue and detailed order attribution.
- [Subscriptions](../subscriptions/reference.md) remains a later interview domain; do not assume its drafts are settled.
