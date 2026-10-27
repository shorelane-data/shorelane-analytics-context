# Company Overview

<!-- status: draft — simulated-analyst answers (company-001), not human-confirmed.
     Source: analyst interview + https://shorelane-data.github.io/shorelane/ -->

## What This Covers
What Shorelane Commerce does, how it makes money, and the unit of value it counts
most. Drafted from the interview; awaiting analyst confirmation.

## Business model
Shorelane Commerce (Long Beach, CA; founded 2019) sells an office-supply catalog
in a B2B2C model: consumers and small businesses buy one-off on the storefront,
companies buy seat-based annual subscriptions, and third-party sellers list on a
marketplace Shorelane operates.

## Revenue model
Three channels (canonical `channel` values):

- **Shop Direct** (`d2c`) — one-off storefront orders paid at checkout; refunds
  occur. Raw data labels this channel `direct` before 2022-06-01.
- **Shorelane for Business** (`business_subscription`) — seat-based annual
  subscriptions, invoiced for the full year up front on net-30 terms and
  recognized ratably (one twelfth per month); terms renew annually and some
  churn at renewal. Subscriptions dominate gross dollars.
- **Shorelane Marketplace** (`marketplace`) — buyers pay sellers full retail;
  Shorelane keeps a commission (its "take"). Refunds occur.

"Revenue" has five distinct measures (recognized, GMV, net, billed, collected
cash) owned by different teams; the headline official number is recognized
revenue. _To be confirmed — see terminology._

## Core unit of value
No single unit across the business — each domain has its own:

- Revenue: dollars by measure and activity date (`fct_revenue`).
- Customers / subscribers: the canonical customer (`app_db_customer_id`).
- Subscription starts, renewals, churn: the 12-month term (`fct_subscriptions`).
- Order volume: the order from a real customer (`fct_orders`).
- Catalog and margin: the order line (`fct_order_lines`).
