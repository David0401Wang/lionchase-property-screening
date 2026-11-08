# Six-category model and rubric

This coursework model uses six supported category ratings from 0 (weakest) to 5 (strongest), multiplied by each category's maximum /5. Weights and tier thresholds live in `../assets/model.json`. The anchors below are judgment criteria, not measured probabilities or fitted coefficients. Record actual statistics and explain the rating, rather than treating a general impression as evidence.

## Comparable scoring unit

Score each assigned property using its verified neighborhood and a predefined comparable housing-product cohort: property type, condition, target resale-price band, as-of date and observation window. Define these before judging outcomes and use them consistently across the comparison group. Retain parcel exceptions and overlapping boundaries. Shared neighborhood evidence is context, not an automatically copied property score. Do not average incompatible property types, dates, geographies or financial plans to produce an apparently comparable score.

Use the most recent coherent period actually available. Sales ordinarily use the preceding 12 complete months and active/pending measures the same snapshot. A shorter-window public market statistic may support an explicitly exploratory judgment if the same definition and period are used across its comparison group. It is not an annual sales count. Preserve provider geography and window; do not blend dated narratives and differently dated summary cards.

## Buyer depth /20

Assess closed comparable-sale volume, the identifiable buyer pool at the target exit price and relevant rental demand for landlord buyers. Preserve counts and denominators. Candidate-list counts, low asking prices, LLC names or investor-oriented descriptions do not establish buyer depth.

| Rating | Supported condition |
|---:|---|
| 0 | A sufficiently complete market review establishes effectively absent viable demand for the defined product and price. |
| 1 | Verified transactions are sporadic and the viable buyer pool is highly specialized. |
| 2 | One narrow buyer segment is identifiable, with limited or inconsistent activity. |
| 3 | One substantial buyer segment and recurring comparable demand are supported. |
| 4 | A substantial primary segment and meaningful second exit-buyer segment are supported by observed demand. |
| 5 | Several independently evidenced buyer segments and sustained comparable demand are supported, including landlord demand where relevant. |

## Resale liquidity /20

Assess comparable median marketing duration, same-day competing inventory relative to a correctly defined sales pace, price-reduction prevalence and sale-to-list outcomes. Preserve original-versus-final-list distinctions and relisting limitations. Report sample counts. One active listing's elapsed duration is not neighborhood median DOM; pending stock is not the same as pending events.

| Rating | Supported condition |
|---:|---|
| 0 | A complete review demonstrates stalled absorption and severe resale obstruction. |
| 1 | Very slow absorption, substantial competing inventory and widespread pricing concessions. |
| 2 | Slow absorption or recurrent reductions materially restrict resale. |
| 3 | Normal, workable absorption for the defined local product, with ordinary concessions. |
| 4 | Relatively quick absorption, manageable competing stock and limited concessions. |
| 5 | Consistently rapid absorption and little competing supply, with corroborating transaction evidence. |

Define quantitative comparison benchmarks in advance from the common cohort. Explain conflicting liquidity measures rather than choosing the most favorable one. A small sample may support exploratory notes but cannot establish consistent liquidity.

## Trajectory /15

Assess direction of like-for-like values and demand, residential vacancy/maintenance distress, employment/service access and completed neighborhood improvements. Use comparable periods and denominators. Raw mixed-property median price changes, overlapping ACS releases, announced projects and a single news article do not establish a neighborhood trend. Existing high amenities are not automatically improvement.

| Rating | Supported condition |
|---:|---|
| 0 | Broad, sustained deterioration across comparable demand and neighborhood fundamentals. |
| 1 | Several material indicators deteriorate, with little verified offset. |
| 2 | Weakening indicators outweigh limited improvements. |
| 3 | Broadly stable or mixed trends without a clear directional advantage. |
| 4 | Several compatible indicators improve, with identifiable limitations. |
| 5 | Sustained improvement is corroborated across market activity and independently measured neighborhood fundamentals. |

## Acquisition economics /15 — financial sub-sector

Assess the recorded acquisition price against a reasoned **as-is fair-value range** for the subject's actual product and condition. Establish that range from the best available closed-sale evidence, disclosing size, condition, occupancy, legal-use, location and timing differences. Listings and pending contracts are context, not completed sales. Record the supporting references, analyst reconciliation and coverage before calculating the rating. Do not build a range around the asking price to obtain a desired rating. This classroom opinion is not a formal appraisal, validated automated valuation or evidence of an executable offer.

Keep as-is value, conditional after-repair value and net project profit separate. Do not subtract an entire hypothetical renovation budget and round-trip transaction costs from mixed-condition sales and treat the result as as-is market value. Construction expense is not automatically its contributory market value. Retain itemized repair, closing, holding, selling and contingency allowances, timing and adverse scenarios internally when considering a project. A fair acquisition can still be an unattractive immediate flip, and occupied rental utility is not zero because no flip is planned. Do not assert rental returns without supported net operating income.

| Rating | Supported condition |
|---:|---|
| 0 | Verified facts establish no viable lawful economic use or value; unknowns alone never qualify. |
| 1 | Entry exceeds the estimated as-is upper bound by more than 15%, without a supported premium. |
| 2 | Entry exceeds the estimated as-is upper bound by up to 15%. |
| 3 | Entry lies within the as-is band, or less than 5% below its lower bound: broadly fair entry, not a demonstrated bargain. |
| 4 | Entry is 5% to less than 20% below the lower bound, supported by a credible comparison and explanation for the gap. |
| 5 | Entry is at least 20% below the lower bound, with strong comparable/condition support and no unexplained price contradiction. |

Calculate lower-bound discount as (lower bound minus entry) / lower bound, and upper-bound premium as (entry minus upper bound) / upper bound. At the upper bound the rating remains 3; at exactly 5% below the lower bound it becomes 4; at exactly 20% below it becomes 5; exactly 15% above the upper bound remains 2. `scripts/value_entry.py` implements these boundaries. Limited or cross-product coverage, stale/conflicting terms or unresolved material condition assumptions cap a favorable rating at 3; moderate support caps it at 4, strong support permits 5. The cap never improves an overpriced rating. Document the coverage judgment; two broad sales are not a completed appraisal grid. With no meaningful value basis, use Pending rather than inventing a range. This category never enters the marketability /70 subtotal.

## Renovation repeatability /15 — execution sub-sector

Evaluate whether representative target properties support repeatable scopes, building systems, legal configurations, permitting paths and local contractor execution. Use project or scoped-quote evidence and documented variability in time/cost. Age alone does not imply a routine scope; similarity of exterior photographs does not establish structural or interior consistency.

| Rating | Supported condition |
|---:|---|
| 0 | Verified widespread obstacles prevent a practical repeatable program. |
| 1 | Bespoke structural, use or approval problems dominate the representative stock. |
| 2 | Frequent complex exceptions make standard scopes unreliable. |
| 3 | Common scopes are identifiable, but material exceptions and execution variability remain. |
| 4 | Most representative projects fit documented standard scopes and feasible approvals, with limited exceptions. |
| 5 | Repeated comparable project evidence supports standard scopes, predictable delivery and a verified execution path. |

Uninspected listings do not prove repeatability. An analyst may nevertheless give a conditional preliminary rating based on the known product, visible or described features and a stated work-scope scenario. Identify structural, legal-use, access, capacity and approval assumptions; do not claim completed inspections or project outcomes. Reserve a final evidence claim for verified information. This category never enters the marketability /70 subtotal.

## Downside resilience /15

Assess comparable-product price stability and dispersion, mapped physical exposure, legal/functional fit, financing/insurance restrictions and dependence on a narrow demand driver. Keep specific parcel failures attached to that parcel unless representative evidence supports wider inference. Use effective FEMA layers for mapped flood risk; absence from a mapped zone is not proof of no flood risk. Do not score reputation or protected demographic characteristics.

| Rating | Supported condition |
|---:|---|
| 0 | Representative evidence shows severe unresolved risks that obstruct ordinary use or resale. |
| 1 | Several widespread major risks with little mitigation or viable fallback demand. |
| 2 | Material recurring vulnerabilities, restrictive transactions or unstable comparable outcomes. |
| 3 | Ordinary exposure with identifiable, property-specific checks and workable mitigants. |
| 4 | Relatively stable comparable outcomes and limited, documented exposure with credible mitigants. |
| 5 | Representative evidence corroborates stable outcomes, ordinary transaction access and multiple viable demand/use fallbacks. |

## Evidence, missingness and totals

A category requires traceable supporting facts, a reason tied to its anchor, consistent scope and disclosed limitations. The user permits the analyst's own views and estimates. A declared assumption is not a factual observation, but can support a conditional preliminary rating if its basis and consequences are explained. Do not turn every incomplete diligence item into Pending. Use null when neither the evidence nor a reasonable explicit scenario supports an opinion; never fabricate facts or copy another category's score.

For an estimated rating, set `rating_basis` to `analyst_estimate` and record a nonempty `assumptions` list alongside the rationale and evidence. The helper labels any resulting total and tier provisional. Uncertainty alone does not automatically prohibit an analyst estimate; confirmed material contradictions, incompatible property cohorts or a scenario with no meaningful basis still require a hold. Stress adjacent anchors and disclose sensitive outcomes without presenting them as statistical confidence intervals.

The helper accepts a category rating only with a rationale and dated evidence records. Those checks verify field presence and arithmetic, not source truth or research adequacy. A numerical point value must always be traceable to the actual six-category rubric.

- Marketability subtotal /70 = Buyer depth + Resale liquidity + Trajectory + Downside resilience.
- Financial sub-sector /15 = Acquisition economics.
- Execution sub-sector /15 = Renovation repeatability.
- Six-category Total /100 = those three distinct contributions, only when all six categories are supported and there is no unresolved material hold.

Label the /100 result a preliminary six-category investment-and-execution screen in the concise Investment notes paragraph. Do not call it a pure desirability score, projected return or buy recommendation. Keep sub-sector calculations internal; the paragraph need not repeat every subtotal.

Incomplete results retain any supported category scores but no total or investment tier. The internal known-points range is arithmetic missingness information, not a confidence interval; do not add it as an output column.

Provisional coursework tiers: at least 75 Priority;60 to below 75 Selective;45 to below 60 Watchlist; below 45 Low priority. The anchors mean strong, ordinary workable, mixed and predominantly weak profiles respectively: uniform 3/5 yields 60 Selective and uniform 4/5 yields 80 Priority. These judgment thresholds are fixed before scoring, not calibrated to achieve a desired distribution and not empirically validated. Keep category weights and point scales unchanged. These are prioritization labels, not investment instructions. Use Pending evidence if incomplete, Review hold if complete but materially held, and Outside selected scope for an out-of-scope municipality. Do not import the reference example's tier as an regional judgment.

Order only complete, comparable, same-period results by total; exact ties remain ties. Keep incomplete and outside-city rows labeled rather than assigning them an apparent last-place score. No extra rank column is delivered.

## Coverage and sensitivity

The ten suggested hard-to-sell factors are covered as follows: sales volume and buyer price band by Buyer depth; duration, inventory and reductions by Resale liquidity; surrounding distress and weak fundamentals by Trajectory and Downside resilience; functional fit by Buyer depth, Renovation repeatability and Downside resilience; flood, legal use, financing and insurance by Downside resilience; inconsistent comparable values by Downside resilience and the financial sub-sector's conservative exit-value analysis. Explain overlap and avoid counting the same weak fact twice without distinct implications.

Incomplete inspections, tenancy, building age or a possible unapproved conversion do not themselves establish damage, illegal current use or an absent exit market. Exclude unsupported conversion value and state the condition/possession assumptions. Assign adverse anchors for observed constraints; preserve disclosed water damage, cash-only terms, financing restrictions and documented marketing resistance. A fact may affect more than one category only through separately explained consequences. Neutral conditional judgments remain provisional and are not declarations that a property is defect-free.

Test each uncertain category one rating level higher/lower within 0–5. Separately change each category weight by plus/minus20% and renormalize to100 for internal sensitivity only. Keep the delivered baseline column maxima unchanged. Mention material reversals or close outcomes in Caution / validation required; do not deliver a separate scenario page. No empirical predictive accuracy is established.
