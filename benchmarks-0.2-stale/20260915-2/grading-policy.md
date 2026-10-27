# Frozen grading policy — 20260915-2

Simulation benchmark against all 23 draft sql_shape seeds. No perfect/human-certified baseline claim.

- Grade the submitted answer, its actual SQL, and assumptions against the frozen expected.must_include / must_exclude fields. Semantic equivalence is sufficient; literal phrase matching is not required.
- Correct governed marts encapsulate their documented filters, normalization and refund contributions. Do not require a redundant filter on a column absent from that mart.
- Require all applicable stated requirements. Missing required business rules count as failures even when the reported number happens to match. Do not demand unrelated clauses from seed intent that expected does not require.
- Conditional requirements only apply when their trigger appears; e.g. persona overrides need not be recited if the question has no persona and the default is correct. Flag compound expected paragraphs that demand irrelevant context, so weak seeds remain visible.
- Correct prose does not rescue SQL that contradicts it. A justified clarification/abstention is recorded, but is not a passed SQL-shape answer unless the seed explicitly expects clarification.
- For conceptual questions, a complete reasoning answer can satisfy a sql_shape rubric without executing a needless numeric query. For data questions, inspect executed SQL. Keep SQL execution coverage separate from seed pass rate.
- Grade duplicate-question seeds separately, with their own expected requirements; do not inflate the number of unique questions.
- Blinding: each case gets independently shuffled candidates A/B. The grader receives question, expected rubric and candidates, but no on/off mapping, context files or source brief. Linguistic clues may still reveal condition; blinding is best-effort.
- Single batch per condition, one answer per seed, no rerolls after grading. Answers may reuse valid queries; within-batch learning is a limitation.
- Report exact counts and percentage-point delta, per-case reasons, regressions, improvements and failures in both modes. Draft-seed uncertainty and shared train/eval origin prevent claims of production accuracy or generalization.
