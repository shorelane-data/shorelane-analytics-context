# Customers — Context

<!-- status: draft — simulated-analyst answers; not human-confirmed. -->

Shorelane's customers show up in four systems — the app database, Stripe, Shopify
and Salesforce — each with its own IDs. The canonical customer is the app
database ID; a crosswalk links source IDs to it, but a 2021 migration left some
older Shopify and Salesforce profiles permanently unlinked, and new links arrive
with a sync lag. Recreated Stripe accounts give one customer several Stripe IDs.
That is why raw source counts are wrong and why every count goes through the
canonical customer.

The marts already exclude test and internal accounts; the internal ones are
Shorelane's own office buying, not trivial QA noise. Staging tables don't apply
that rule, and the BI customer pages currently read staging — the source of the
known gap between the dashboard and the governed figures.
