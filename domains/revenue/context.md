# Revenue — Context

<!-- status: draft — simulated-analyst answers; not human-confirmed. -->

Shorelane has no single "revenue". Five teams each own a measure — Finance
recognized revenue (GAAP, the official number), Marketing GMV, Ops net revenue,
FP&A billed revenue, Treasury collected cash — and the same question returns
different correct numbers depending on who asks. The measures differ in what
they count (full ticket vs Shorelane's take), when they count it (order,
recognition, invoice or collection date), and how refunds enter.

Subscriptions dominate gross dollars and are billed a year up front but
recognized monthly, which is why billed, recognized and collected diverge most
around subscription-heavy periods. `fct_revenue` is deliberately dimensionless:
it answers "how much, under which measure" and nothing else; any slice goes
through the originating order.
