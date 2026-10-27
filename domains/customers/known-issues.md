# Customers — Known Issues

## What This Covers
Data-quality issues and analytical gotchas — the silent-failure modes. Each issue
here also appears as an `IF … DO NOT …` routing trigger in `reference.md`
and as an eval seed.

- **Counting source aliases** — rows of `int_customer_identity` (or per-system profile counts) overstate customers several times. <!-- status: draft (simulated, customers-001) -> seed -->
- **Counting never-ordered profiles** — all `dim_customers` rows include profiles that never ordered; those are not customers. <!-- status: draft (simulated, customers-001) -> seed -->
- **Double-flagged first orders** — some customers have two orders with `is_first_order`; count distinct customers. <!-- human-decided 2026-10-27 (customers-001) -> seed -->
- **New to channel ≠ new customer** — only the channel of the first-ever order gets the new customer. <!-- status: draft (simulated, customers-001) -->
- **Crosswalk joins** — inner joins drop unresolved aliases; joining orders through the alias bridge fans out on recreated Stripe accounts. <!-- status: draft (simulated, customers-001) -> seed -->
