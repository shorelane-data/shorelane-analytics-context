# Subscriptions — Context

<!-- status: draft — simulated-analyst answers; not human-confirmed. -->

Shorelane for Business sells seat-based annual subscriptions. Each 12-month term
is a row; a renewal creates a new term chained to the old one, and a churned
customer simply has a final term that ends without a successor. Prices are
locked at each term's start, and customers keep the plan generation they signed,
so the book carries three live generations at different prices — "grandfathered"
customers renew at old prices, which is why ACV per seat on new subscriptions
differs from the book average.

Because a term's outcome is unknown until it ends, `status = 'active'` only means
"not yet decided at load time". Liveness is always a date-range test.
