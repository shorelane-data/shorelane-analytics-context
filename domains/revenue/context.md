# Revenue — Context

## What This Covers
Narrative business context for a human onboarding to this domain. (The agent
reads `reference.md`, not this.)

Shorelane sells office supplies through three channels with deliberately
different money timing:

- **d2c** — the consumer pays at order time: billing, cash, and recognition
  coincide.
- **business_subscription** — billed up front on net-30 invoicing; cash arrives
  later (or never — bad debt), and revenue is recognized ratably over the
  subscription term.
- **marketplace** — third-party sellers list, Shorelane fulfills and keeps a
  per-sale commission (15–25% by category, a contract term). The buyer's full
  ticket counts in GMV; only the commission enters the earnings measures.

Because of that timing wedge, there is **no single "revenue"** — the company
tracks five measures in one tidy long fact (`fct_revenue`):

| measure | what it is | valued at | dated on |
|---|---|---|---|
| gmv | demand: buyer's full ticket, gross of refunds | full ticket | order date |
| net_revenue | what Shorelane earns; refunds negative | net | order date (refunds: refund date) |
| billed_revenue | what was billed, all channels | net | order/invoice date |
| collected_cash | cash that actually arrived | net | collection date |
| recognized_revenue | accounting revenue (subs ratable, rest immediate) | net | recognition date |

Unqualified "revenue" means **recognized_revenue**. In any period the five
disagree — that's the point of tracking five, not a reconciliation bug.

Owner: Ron Potok.
