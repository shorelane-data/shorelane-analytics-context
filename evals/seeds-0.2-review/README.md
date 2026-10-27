# v0.2 seeds awaiting v0.3 review — not active

These 46 seeds came over from ACF v0.2 (2026-10-27) but don't yet meet the v0.3
seed contract. The validator, the eval harness and the regression tools only read
`evals/seeds/*.seed.yaml`, so nothing in this folder is graded or used.

- **31 seeds have no `ir` block.** v0.2 let draft seeds skip it; v0.3 requires it.
- **15 seeds have a `# MIGRATION REVIEW (v0.3)` note.** Their `ir.metric` doesn't
  resolve in v0.3, or (for `marketing-margin-scope`) their meaning conflicts with
  the v0.3 definition.

To bring a seed back, fix it here, `git mv` it into `evals/seeds/`, and run
`python .ci/validate.py --branch-test --require-ready`. To drop a seed, delete it.
Every seed's legacy `status: draft` now lives in `review_history`; that history
never grants approval.
