# Customers known issues

> SIMULATION TEST ARTIFACT; all entries draft and require human review.

## Account hygiene
The historical Customers dashboard omitted test/internal exclusions; the repaired dashboard reconciles for tested current/new/multi-channel totals. Sigma queries and other slices remain unverified. Preserve governed account_type customer eligibility. <!-- status: draft -->

## Window and unit mismatch
Current, active, new, subscriber, term and seat counts are different measures. <!-- status: draft -->

## Identity fanout and missing mappings
Qualified LEFT JOIN; unresolved aliases are quality, not customers; count systems for source coverage and deduplicate canonical IDs before facts. <!-- status: draft -->

## Attribution ties
Earliest-date cross-channel ties need a human tie-breaker; dbt flags all earliest-date orders. <!-- status: draft -->

## Channel overlap
Per-channel counts overlap; exact pairwise-bucket exclusivity is unconfirmed. <!-- status: draft -->

## Identity populations
Source/date/account populations and average-ID formula await owner review. <!-- status: draft -->

## Unspecified dimensions and returning share
Segment slicing approval and returning-share numerator/cutoff remain open. <!-- status: draft -->

## Unavailable questions
NPS, store visits, customer shipping cost and return reasons are not available. <!-- status: draft -->

## Subscription equivalence
The brief says trailing orders and term coverage coincide; no override is defined if they diverge. <!-- status: draft -->
