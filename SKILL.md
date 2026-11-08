---
name: lionchase-neighborhood-scoring
description: Research and screen individual properties with neighborhood context using six categories and a twelve-column result. Apply fresh regional evidence; keep as-is value, renovation profit and marketability distinct.
---

# Lionchase Property Screening

Use this AI-assisted workflow for preliminary property research, reasoned valuation opinions and prioritization. One row represents one property. The six-category framework is reusable; observations and conclusions require local research. The current Albany application is described separately in [the regional profile](regions/albany-ny.md).

## Scope and setup

Define the analyst, selected region and municipal scope, property IDs, property type/condition cohorts, as-of date, observation window and intended exit strategy before scoring. Accept the actual input count; there is no fixed 40-property requirement. Do not change boundaries to make a comparable fit. For another region, replace the local evidence plan rather than merely relabeling Albany observations.

Read [the rubric](references/model-and-rubric.md) and [research guidance](references/research-and-sources.md). The model's six categories, maxima and tier thresholds are in `assets/model.json`. Keep the baseline weights and boundaries consistent within an analysis. They are judgment choices, not validated universal constants.

## Research and judgment

Verify municipality and neighborhood membership, preserve boundary overlaps, and distinguish provider markets from official areas. Use comparable housing products, conditions, dates and price bands. Assigned-property counts do not measure buyer depth. Asking prices do not establish closed-sale value. Rental gross income is not net operating income.

Retain traceable facts, actual observation dates, source scope, limitations, rationale and analyst assumptions for every rating. Explicit, evidence-informed estimates are allowed. Do not require a completed appraisal before offering a provisional coursework opinion, and do not invent inspections, contractor quotes, source facts or precise unsupported adjustments. Unknown diligence is uncertainty rather than a confirmed defect to deduct repeatedly.

Acquisition economics compares entry against a reasoned **as-is value band**. Use `scripts/value_entry.py` after documenting the reconciliation and coverage judgment. It calculates a rating from supplied values; it does not estimate values or verify the market. Keep conditional after-repair value, repair/transaction/holding costs and project profit separate. A thin flip margin does not mechanically make fair-entry value poor.

Ratings are integers 0–5. Points equal category maximum × rating /5. Marketability contributes /70 internally; acquisition economics and renovation execution contribute /15 each separately. The combined /100 is a preliminary investment-and-execution screen, not pure desirability or a return forecast. Preserve actual water damage, financing restrictions and other established constraints.

Unsupported categories remain missing; do not rebase the denominator. Confirmed material contradictions require a hold until resolved. Apply adjacent-rating and weight sensitivity internally and mention material tier sensitivity in the visible caution paragraph.

## Calculate and deliver

Use [the input guide](references/input-guide.md), `assets/input-template.json` and `scripts/score_neighborhoods.py`. The scripts check schema/evidence fields and arithmetic, not source truth. Fictional examples must stay explicitly fictional. Run the behavioral tests after changes to calculation rules.

Deliver one results worksheet with exactly twelve columns in model order: Name; Area / neighborhood label; the six scores; Total /100; Screening tier; Investment notes; Caution / validation required. Include community, municipality and full property address in Area for an actual property. Keep the two visible narrative cells to one short English paragraph each. Retain detailed sources and budgets in separate internal research records; do not add cell comments or hidden annotations without a request.

Write skill materials and result documents in English. Conversation may follow the user's preferred language. Preserve source facts, existing destination formatting and unrelated work. Shared-file writes require an explicit instruction identifying the destination and scope. Verify any authorized write by reading back values and affected formatting.

Maintain only the current model in this package. The public demonstration contains no real parcel, private assignment document, personal path or account credential. Public examples do not authorize sharing private research inputs.
