# Subscriptions Reference

<!-- status: draft — simulated-analyst answers (company-003/004, subscriptions-001); owner human-decided. -->

## Quick Reference
- **Business context** — the business-subscription book (Shorelane for Business): subscribers, seats and ACV under contract, and how new first terms, renewals and churn move it.
- **Entity grain** — `fct_subscriptions`: one row per 12-month term from a real customer. A renewal adds a new row (`renewed_from_subscription_id`).
- **Standard hygiene filter** — use `fct_subscriptions` (real customers; has `is_first_term`). Compare DATEs, never timestamps.
- **Canonical table** — `nodal-shorelane.shorelane.fct_subscriptions`

## Routing triggers
- IF active subscribers / "how many subscribers" at D → `active_subscribers`: distinct customers with a term containing D (`term_start_date <= D <= term_end_date`). DO NOT filter `status = 'active'` or `is_current`.
- IF ACV under contract at D → `acv_under_contract`: SUM(`acv`) over terms containing D; group by the term row's plan, never today's plan.
- IF new subscriptions → `new_subscriptions`: first terms (`is_first_term`) started in the period. Later terms are renewal starts.
- IF renewal rate → `renewal_rate` = `renewed_terms` ÷ `decided_terms`, placed by term END date, counted in terms. DO NOT divide by active subscribers or use terms started as the base.
- IF churned ACV → `acv_churned`: SUM(`acv`) over churned decided terms ending in the period.
- IF ACV per seat on new subscriptions → `acv_per_seat_new`: SUM(acv) ÷ SUM(seats) over first terms started in the period; not a mean of ratios. ACV under contract ÷ active seats is the stock version — label it.
- IF grandfathered / plan generation → cut by `plan_generation` on the term row; every generation is live.
- IF the question cuts subscriptions by sales channel, acquisition channel, promo code, seat bucket or status → DO NOT; every term is `business_subscription`, those attributes live on orders/customers, and status is an outcome.
- IF invoices are proposed as the subscription book → DO NOT; invoices answer billed / collected revenue (revenue domain).
- IF `stg_subscriptions` or raw tables → DO NOT; they include test/internal accounts and lack `is_first_term`.

## Dimensions
- `status` — term outcome: renewed / active (fate unknown at load) / churned. Not liveness. `cancelled_date` appears only on churned terms and equals `term_end_date` (warehouse-checked) — no mid-term cancellations.
- `plan_generation` (1–3), `plan_name`, `tier`, `segment` (smb / enterprise for subscription customers).
- `seats`, `price_per_seat` (locked at term start), `acv` = seats × price_per_seat.

## Key tables
### fct_subscriptions   ← canonical
- **Grain**: one 12-month term  ·  **Use for**: every subscription metric
- **Join keys**: `customer_id` → canonical customer; `order_id` → the business_subscription order billing the term

### dim_plans
- One row per plan across three generations; `is_current` marks the generation still sold — never a liveness filter.

## Gotchas
- A term ending on a month's last day is in that month's active count *and* its renewed/churned flow — correct, don't "fix" it.
- Live-warehouse windows reaching today show recently ending terms as `active`, deflating the renewal denominator; use fully elapsed windows.
- Over windows longer than twelve months a customer can contribute two decided terms; renewal rate stays at term grain.
- Terms started ≠ terms ended in a period: a term ending on the 31st renews on the 1st.
- Grandfathered means a generation retired on or before the as-of date — not simply "generation ≠ 3".

## Common query patterns
- Active subscribers / ACV under contract at D: filter terms containing D, count distinct customers / sum ACV.
- Renewal rate: among terms ending in the period with status renewed or churned, renewed ÷ all.

## Cross-references
- `domains/revenue/reference.md` — subscription billed / recognized / collected revenue.
- `domains/customers/reference.md` — canonical customers.
