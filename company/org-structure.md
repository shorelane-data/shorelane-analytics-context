# Org Structure

## What This Covers
Who owns which analytical domain, so the agent can route ambiguous questions and
PRs to the right owner. This is a **living roster**: the interview adds one row per
domain as that domain's owner is confirmed in Stage 2, and updates the row if
ownership changes. Keep it in sync with each `domains/<domain>/domain.yaml: owner`.

## Domain Ownership

| Domain | Owner | Team | Status |
|---|---|---|---|
| revenue | Finance (CFO) | Finance | confirmed |  <!-- owner human-confirmed 2026-10-27 (domains-001) -->
| customers | Marketing (VP Marketing) | Marketing | confirmed |  <!-- owner human-confirmed 2026-10-27 (customers-001) -->
| subscriptions | FP&A | FP&A | confirmed |  <!-- owner human-confirmed 2026-10-27 (subscriptions-001) -->
| marketing | Marketing (VP Marketing) | Marketing | confirmed |  <!-- owner human-confirmed 2026-10-27 (marketing-001) -->
| catalog-margin | Ops (COO) | Operations | confirmed |  <!-- owner human-confirmed 2026-10-27 (catalog-001) -->

<!--
One row per domain. `Status` is `draft` until the analyst confirms the owner, then
`confirmed` (mirrors the domain's draft/confirmed discipline). Leave the owner as
`_To be confirmed._` rather than guessing.
-->

## Notes
_Anything about ownership that doesn't fit a row — shared domains, escalation paths,
who to ask when an owner is out._
