# Input and calculation guide

`scripts/score_neighborhoods.py` uses the Python standard library and reads the model relative to its own location. It does not fetch web pages, authenticate to services, edit spreadsheets or estimate values automatically.

## Dataset fields

- `model_id`: `lionchase-six-category`.
- `data_kind`: `observed` for actual researched inputs, `fictional` for demonstration data, or `unresearched` for a blank working template.
- `as_of`, `window_start`, `window_end`: ISO dates. The declared common window must end no later than the as-of date. Evidence retains its own actual dates; broad context outside a matched window needs explicit explanation and is not silently pooled.
- `records`: one object per property, with unique IDs. The code accepts any record count.

## Record fields

Each record supplies `id`, analyst `name`, `area`, `municipality`, `property_cohort` and `comparison_group`. For real work, area contains the verified community and full property address. A comparison group must not mix different product cohorts or municipalities. Separate groups do not prove the resulting scores are cross-market comparable.

Set `geography_verified` only after checking boundaries and provide `boundary_source`. Set `comparability_verified` only after reviewing the reference cohort and disclosing its limitations; it does not certify that a formal appraisal grid is complete. `in_scope:false` creates an Outside selected scope hold. A property outside the central city can remain in scope when the assignment explicitly includes it and its actual municipality and market are used.

`material_evidence_holds` is an array of unresolved substantive conflicts. `investment_notes` and `caution` are short visible paragraphs. The final result contains only the twelve output columns; diagnostic fields in the JSON are internal research material.

## Category observations

Use the six category IDs in `assets/model.json`. Each supported observation includes:

- `rating`: integer 0–5, or null when unsupported.
- `rationale`: why the evidence supports this category's rubric anchor.
- `rating_basis`: `observed` or `analyst_estimate`. An estimate requires a nonempty `assumptions` list.
- `evidence`: at least one dated record with `source`, `definition`, `geography`, `cohort`, `summary`, `data_start`, `data_end` and `accessed_on`.

A source must be a traceable HTTP(S) URL or an absolute path. Published demonstrations use explicitly fictional URLs; actual analysis needs real accessible evidence. The helper checks field presence and date ordering only. It does not retrieve a URL, prove source independence, validate the observation window's comparability or confirm the analyst's claims.

## Acquisition calculation

`value_entry.rate_entry(entry, lower, upper, coverage)` receives independently reasoned positive finite values. All three monetary values must use the same currency. Coverage is limited, moderate or strong; its favorable-score cap is 3, 4 or 5 respectively. Coverage caps never improve an overpriced entry score. The function does not decide which coverage label is appropriate.

Record the as-is band, comparable reconciliation, coverage and returned rating in the acquisition observation. Do not substitute a repaired resale estimate or net project profit for as-is value. Zero requires separate verified no-viable-use analysis and is never inferred merely from missing inputs.

## Outputs and verification

All six supported categories and no unresolved holds are required for a total. Estimates receive provisional labels. Fictional data receives `FICTIONAL_DEMONSTRATION` and a visible fictional notice. `results[].row` contains exactly twelve fields. The remaining JSON fields expose evidence links, assumptions and the distinct /70, /15 and /15 contributions for internal review.

The checked-in example output is generated from the fictional example input, not manually fitted to a preferred tier. Run tests and the example again after changing the model. Passed tests establish deterministic behavior, not empirical investment accuracy.
