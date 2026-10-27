# Subscriptions — Known Issues

## What This Covers
Data-quality issues and analytical gotchas — the silent-failure modes. Each issue
here also appears as an `IF … DO NOT …` routing trigger in `reference.md`
and as an eval seed.

- **status = 'active' as liveness** — drops terms that later renewed or churned; historical counts collapse. <!-- status: draft (simulated, company-003) -> seed -->
- **is_current as liveness** — drops every grandfathered subscriber. <!-- status: draft (simulated, company-003) -> seed -->
- **Renewal rate shapes** — renewals ÷ active subscribers, renewal starts as numerator, or terms started as base are all wrong. <!-- status: draft (simulated, subscriptions-001) -> seed -->
- **Timestamped as-of** — compares past `term_end_date` and drops terms ending that day. <!-- status: draft (simulated, subscriptions-001) -->
- **Live-warehouse windows** — windows reaching today lose recently ending terms from the renewal denominator. <!-- status: draft (simulated, subscriptions-001) -->
- **Current-plan lookup** — grouping by today's plan misattributes ACV; use the term row. <!-- status: draft (simulated, subscriptions-001) -->
- **Renewals in new ACV per seat** — grandfathered renewal prices pull the figure down. <!-- status: draft (simulated, subscriptions-001) -> seed -->
- **Staging subscriptions** — `stg_subscriptions` includes test/internal accounts and lacks `is_first_term`. <!-- status: draft (simulated, subscriptions-001) -->
- **No parity check** — nothing reconciles `fct_subscriptions` against the FP&A dashboard module. <!-- status: draft (simulated, subscriptions-001) -->
