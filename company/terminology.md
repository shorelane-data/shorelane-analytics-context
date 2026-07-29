# Terminology

## What This Covers
The cross-domain terms a new analyst gets wrong in their first month. For each:
what it means here, and what people wrongly assume it means. No statistics.

## The five revenues

- **revenue (unqualified)** — defaults to **recognized_revenue** (the accounting
  view). When a stakeholder says just "revenue", answer with recognized_revenue
  and name the measure used. Commonly confused with net_revenue (what Shorelane
  earns at order time) and gmv (topline). There is no single "revenue" — five
  measures exist. <!-- status: confirmed 2026-07-28 -->
- **gmv** — gross merchandise value: the buyer's **full ticket** across all
  channels (marketplace included at full price, not Shorelane's take), **gross
  of refunds**, attributed to order date. Measures demand at order time.
  Commonly confused with net_revenue (Shorelane's earnings).
  <!-- status: confirmed 2026-07-28 -->
- **net_revenue** — what Shorelane actually earns: full amount on d2c and
  business subscriptions, **commission only** on marketplace. Refunds appear as
  **negative rows on the refund's own date** (order dollars stay on order_date).
  <!-- status: confirmed 2026-07-28 -->
- **recognized_revenue** — the accounting view, at **net** (what Shorelane
  earns): business subscriptions spread **ratably over the term** on the
  recognition schedule; d2c and marketplace recognize **immediately** at order.
  Because old subscriptions keep recognizing, recognized can exceed GMV in a
  period. This is what unqualified "revenue" means.
  <!-- status: confirmed 2026-07-28 -->
- **billed_revenue** — what Shorelane billed: **all channels**, dated at
  order/invoice time (subscriptions are billed up front), at **net**
  (marketplace at commission-only) so it's comparable to collected_cash.
  Distinct from gmv, which is full-ticket. <!-- status: confirmed 2026-07-29 -->
- **collected_cash** — cash actually received, dated on the **collection date**
  (not the invoice date). Pending net-30 invoices and bad debt contribute
  nothing — collected_cash only ever counts dollars that arrived.
  <!-- status: confirmed 2026-07-28 -->

## Channel terms

- **d2c** — direct-to-consumer shop orders; the consumer pays up front at order
  time, so billing, cash, and recognition all happen at once.
  <!-- status: confirmed 2026-07-28 (site + revenue-model review) -->
- **business_subscription** — "Shorelane for Business" orders: billed up front
  on net-30 invoicing, cash collected later (or never — bad debt), revenue
  recognized ratably over the subscription term.
  <!-- status: confirmed 2026-07-28 (site + revenue-model review) -->
- **marketplace** — third-party sellers list products, Shorelane fulfills.
  Shorelane's earnings are the per-sale commission only; the full ticket counts
  in gmv but never in net/billed/recognized/collected measures.
  <!-- status: confirmed 2026-07-28 (site + revenue-model review) -->
- **take rate / commission** — the per-sale commission Shorelane keeps on
  marketplace orders, 15–25% by category (a contract term, not a statistic);
  no listing fees. <!-- status: confirmed 2026-07-28 (site) -->

## Billing terms

- **net-30** — business-subscription billing terms: invoice issued up front at
  order, payment due within 30 days. The reason billed ≠ collected in any
  given period. <!-- status: confirmed 2026-07-28 (site) -->
- **bad debt** — an invoice Shorelane no longer expects to collect
  (`is_bad_debt` on the invoice; `collected_date` stays NULL). Never enters
  collected_cash. Flagged by a **manual finance write-off, case by case** —
  there is no fixed aging threshold. <!-- status: confirmed 2026-07-29 -->
- **pending collection** — an invoice whose `collected_date` is still NULL and
  is *not* flagged bad debt: billed, not yet paid, inside or past its net-30
  window. <!-- status: confirmed 2026-07-28 -->
- **refund** — a negative revenue event lagged after its original order, dated
  on the refund's own date; enters net_revenue and collected_cash as negative
  rows, never reduces gmv. <!-- status: confirmed 2026-07-28 -->
