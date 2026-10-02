# Customers

> SIMULATION TEST ARTIFACT. All definitions are draft and require human owner review.

This domain separates the customer base from activity, acquisition and identity quality. The canonical customer is an app customer, not a source-system profile or alias. A real customer can buy through several channels, so channel customer counts overlap.

Current customers use a trailing twelve-complete-month order window; active customers use the selected period. New customers enter on their first-ever order across all channels. Subscription customer counts use inclusive term coverage at month end, while term and seat counts answer different questions.

Identity reporting retains unresolved aliases as quality findings. Migration gaps and recent synchronization delays have different meanings; neither creates additional customers. Recreated Stripe accounts can create multiple aliases for one customer.

The Customers dashboard previously omitted test/internal hygiene; repaired current/new/multi-channel totals now reconcile. Sigma customer queries and untested dashboard measures still require verification. Governed marts are the proposed authority from the simulation; live captures are not human approval.

Owner, durable dbt remote, attribution tie-breaks, segment slicing, channel-combination exclusivity, alias metric populations, average IDs/customer and returning-share definitions remain open. See SESSION.md.
