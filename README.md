# Lionchase Property Screening

**A reusable, AI-assisted workflow for researching and ranking individual properties with neighborhood context.** Developed by David Wang from an Albany, New York coursework application covering 40 properties.

## Start here — a one-minute overview

The workflow combines local property research, explicit analyst judgment and deterministic score calculations. It helps a reviewer see why one property deserves further work before another, with the supporting assumptions retained for inspection.

1. Identify the property, municipality, neighborhood and comparable housing product.
2. Gather dated property, transaction and neighborhood evidence.
3. Reconcile an **as-is value range** and assess six categories.
4. Calculate category points, a provisional total and a screening tier.
5. Deliver one property per row with concise investment and caution paragraphs.

**As-is value, after-repair value and net project profit remain separate.** A fairly priced rental property can still be a poor immediate flip. Missing diligence is disclosed as uncertainty rather than repeatedly treated as a confirmed defect.

The scripts calculate and check supplied research inputs. They do not browse for data, estimate value bands automatically, inspect buildings or verify that sources are true. An AI agent or analyst performs the research and valuation reconciliation.

## What is reusable, and what is region-specific?

| Component | Reusable part | What must be supplied or reviewed locally |
|---|---|---|
| Research workflow | Property-level analysis with neighborhood context; traceable facts and assumptions | Available public records, access rights, local source coverage and observation dates |
| Geography | Verify boundaries, retain overlaps, distinguish mailing address from municipality | Actual municipal/neighborhood polygons and parcel or address matching |
| Comparable selection | Match product, condition, size, use, price band and time | Closed sales and active/pending context for the target market |
| Six-category rubric | The category definitions and separation of marketability, entry value and execution | Whether the anchors fit the local property product and investment strategy |
| Arithmetic | Ratings from 0–5; points = category maximum × rating /5 | Evidence-backed input ratings and any deliberately approved model configuration |
| Acquisition economics | Compare entry with a reasoned **as-is** value band; cap unsupported bargain claims | Local comparable evidence, condition reconciliation and actual acquisition terms |
| Project feasibility | Keep renovation, transaction, holding and contingency scenarios separate | Local work scopes, contractor costs, taxes, insurance, financing and timing |
| Legal and physical exposure | Identify use, financing, insurance and physical constraints | Jurisdiction-specific rules, permits, hazards and building records |
| Output | One property per row; the same twelve columns | Analyst name, property identity, location, scores and short explanations |

**Portability status:** the scoring code supports any number of records and has no Albany-only eligibility label. The [Albany profile](regions/albany-ny.md) contains local context separately. A new region still requires fresh research and an explicit scope; changing the city name does not make the model locally validated. Cross-city scores are not automatically comparable.

## Six categories

| Category | Maximum |
|---|---:|
| Buyer depth | 20 |
| Resale liquidity | 20 |
| Trajectory | 15 |
| Acquisition economics | 15 |
| Renovation repeatability | 15 |
| Downside resilience | 15 |
| **Total** | **100** |

The four marketability categories total **70** internally. Acquisition economics contributes **15** separately, and renovation execution contributes **15** separately. The combined /100 is an **investment-and-execution screen**, not a pure neighborhood-desirability score or projected return.

The current judgment-based tiers are Priority ≥75, Selective ≥60, Watchlist ≥45, and Low priority <45. Estimated results are labeled provisional. These weights, valuation-discount bands and tier cutoffs are model choices, not universal market constants or empirically fitted thresholds.

Read the [full scoring and valuation rubric](references/model-and-rubric.md) for anchors, evidence limits and the fair-entry calculation.

## A small worked example

The included [Albany demonstration](examples/albany-demo.md) is **fictional and deliberately labeled**. It illustrates a four-bedroom single-family case with ratings of 3, 2, 3, 3, 3 and 3. Points are 12 + 8 + 9 + 9 + 9 + 9 = **56 /100**, or **Watchlist (provisional)**.

The demo's $199,000 entry and $200,000–$245,000 as-is band are illustrative inputs. The calculation shows how the workflow behaves; it does not establish a real property's value or validate the model's investment performance. The original 40-property research files and shared team documents are not included.

## Run the example — Python 3.10 or later

No third-party Python packages, credentials, local personal paths or network connection are required for the calculations.

```bash
python3 scripts/score_neighborhoods.py examples/albany-demo-input.json
python3 -m unittest discover -s scripts -p 'test_*.py'
```

The first command produces JSON containing the exact twelve-column row and internal evidence/assumption diagnostics. A checked-in [example result](examples/albany-demo-output.json) makes the outcome inspectable without running code. No spreadsheet or external account is changed.

For a new analysis, copy [the blank input template](assets/input-template.json), define the selected region, supply actual research, and run the same script. Unresearched inputs intentionally receive no total or investment tier. [The input guide](references/input-guide.md) explains the fields and their limits.

## Use as an AI skill

The repository root contains [SKILL.md](SKILL.md), its model, references and scripts. A compatible agent can load it as `lionchase-neighborhood-scoring`. Read SKILL.md for the operating workflow. For manual review, start with this README and then the rubric; the agent metadata is optional for a human reviewer.

## Review map

- **Principal:** this README → the short worked example.
- **Analyst:** the rubric → the Albany profile or a replacement regional research plan.
- **Technical reviewer:** input guide → calculation scripts → behavioral tests.

Tests cover arithmetic, thresholds, missing evidence, material holds, cohort consistency and estimate labeling. They do **not** establish source accuracy, valuation accuracy, predictive performance or investment suitability. Independent market research and property diligence remain necessary before a real transaction.
