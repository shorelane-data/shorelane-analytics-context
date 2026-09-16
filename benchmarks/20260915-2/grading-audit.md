# Grading-input audit

The initial blinded packet omitted top-level as_of_date metadata present in both subject artifacts. Both subjects explicitly declare 2026-09-15. The grader was asked to reassess date-anchor findings with this shared context supplied; no answers, rubrics, or condition mappings changed. Initial grades preserved as grades-blinded.initial.json.

## Audit outcome

- S11 candidate A changed fail to pass because shared metadata supplies the explicit as-of date.
- S01 candidate B removed the account-hygiene omission; its exclusive endpoint still fails.
- S20 both candidates removed an unwarranted immutable-load-pinning requirement; remaining failures retained. Grader flagged the ambiguous phrase instead.
- No unrelated judgments changed; condition identities remained hidden.
