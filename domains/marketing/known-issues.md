# Marketing known issues

> SIMULATION TEST ARTIFACT; all entries draft.

## Acquisition attribution
Repeated day totals, platform claims, first-date order counts and canonical customer counts are not interchangeable. The human selected earliest purchase timestamp across all channels for CAC, with distinct canonical customers. Live raw-source checks still find exact-timestamp cross-channel ties; the human approved deterministic hash assignment for these cases; see reference.md for the frozen convention. <!-- status: draft -->

## Mixed scope and grain
All-channel GMV differs from consumer AOV/order scope. Ratio-of-totals and preaggregated joins prevent plausible errors. <!-- status: draft -->

## Category/margin
Subscription lines absent. Category margin covers d2c and marketplace lines, as the Marketing dashboard reports it; marketplace lines are at retail, so their margin is not Shorelane earnings (those are the commission). A d2c-only margin understates category margin and can reorder categories. No governed economic margin by category exists. Historical categories need review. <!-- status: draft -->

## Promotion exceptions
Blank/unmatched codes, validity-window exceptions, count/discount period rules, exact dates and encoding require human or live source checks. <!-- status: draft -->

## Coverage and visibility
Platform start dates differ; incomplete/future activity is not final zero. Use fully elapsed matched windows. <!-- status: draft -->

## Synthetic intervention
The brief describes a paid-media cut from 2026-02-01 through 2026-04-30. Separate acquisition from existing ordering. This fixture fact does not define a general causal estimator. <!-- status: draft -->

## Unsupported questions
Platform attribution, causal ROI, seller ranking and named absent entities require additional sources or definitions. <!-- status: draft -->

## Verification pending
Authentication was recovered through fresh instances of the existing MCP server. Schema/key checks and off/on comparisons ran. AOV matches and is human-accepted; acquisition/CAC use earliest purchase timestamps, with exact-timestamp ties assigned deterministically by the approved convention. The Marketing new-customer headline matches first-date order rows rather than distinct first purchasers. Total new-customer distinct grain is human-accepted; The timestamp/hash CAC rerun is complete; dashboard/dbt adoption and human numeric review remain pending. <!-- status: draft -->

## Human-reviewed customer grain
The user explicitly confirmed distinct canonical customers for total new-customer counting. Multiple first-date order rows do not create additional customers. CAC attribution uses earliest purchase timestamp; exact-time cross-channel ties use the fixed hash convention and remain flagged as assigned, not observed chronology. Simulation artifact labeling and draft status are retained. <!-- status: draft -->
