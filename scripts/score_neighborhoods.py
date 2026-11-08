#!/usr/bin/env python3
"""Check six-category evidence fields and calculate points; no network or external writes."""
import argparse
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def load_model():
    model = json.loads((ROOT / 'assets/model.json').read_text())
    cats = model['categories']
    require(len(cats) == 6 and len({c['id'] for c in cats}) == 6, 'Six unique categories required')
    require([c['maximum'] for c in cats] == [20, 20, 15, 15, 15, 15], 'Reference maxima disagree')
    require(model['headers'][2:8] == [c['header'] for c in cats] and len(model['headers']) == 12,
            'Reference columns disagree')
    return model


def score_dataset(data):
    model = load_model()
    require(data.get('model_id') == model['model_id'], 'Wrong model')
    kind = data.get('data_kind')
    require(kind in ('observed', 'fictional', 'unresearched'), 'Explicit data_kind required')
    as_of = date.fromisoformat(data['as_of'])
    start, end = date.fromisoformat(data['window_start']), date.fromisoformat(data['window_end'])
    require(start <= end <= as_of, 'Invalid common observation window')
    records = data.get('records')
    require(isinstance(records, list), 'records must be a list')
    cats = model['categories']; keys = {c['id'] for c in cats}
    ids, groups, results = set(), {}, []
    for record in records:
        rid = record.get('id')
        require(nonempty(rid) and rid not in ids, 'Record ID missing or duplicate'); ids.add(rid)
        for key in ('name', 'area', 'municipality', 'property_cohort', 'comparison_group'):
            require(nonempty(record.get(key)), f'{rid}: {key} required')
        group = record['comparison_group']
        signature = (record['property_cohort'], record['municipality'])
        require(group not in groups or groups[group] == signature, 'Incompatible cohorts share a group')
        groups[group] = signature
        holds = record.get('material_evidence_holds', [])
        require(isinstance(holds, list) and all(nonempty(h) for h in holds), 'Invalid material holds')
        holds = list(holds)
        if record.get('geography_verified') is not True or not nonempty(record.get('boundary_source')):
            holds.append('Neighborhood geography not verified')
        if record.get('comparability_verified') is not True:
            holds.append('Comparable cohort not verified')
        if kind == 'unresearched':
            holds.append('Unresearched template')
        outside = record.get('in_scope') is False
        if outside:
            holds.append('Outside the selected municipal scope')
        obs = record.get('category_observations', {})
        require(isinstance(obs, dict) and not (set(obs) - keys), f'{rid}: unknown category IDs')
        points, missing, sources, assumptions = {}, [], [], {}
        for cat in cats:
            cid = cat['id']; entry = obs.get(cid, {})
            require(isinstance(entry, dict), f'{cid}: observation object required')
            rating = entry.get('rating')
            if rating is None:
                points[cid] = None; missing.append(cid); continue
            require(type(rating) is int and 0 <= rating <= 5, f'{cid}: integer rating 0..5 required')
            require(nonempty(entry.get('rationale')), f'{cid}: rating rationale required')
            basis = entry.get('rating_basis', 'observed')
            require(basis in ('observed', 'analyst_estimate'), f'{cid}: invalid rating basis')
            if basis == 'analyst_estimate':
                declared = entry.get('assumptions')
                require(isinstance(declared, list) and bool(declared) and all(nonempty(a) for a in declared),
                        f'{cid}: analyst estimates require explicit assumptions')
                assumptions[cid] = declared
            evidence = entry.get('evidence')
            require(isinstance(evidence, list) and bool(evidence), f'{cid}: evidence required')
            for item in evidence:
                require(isinstance(item, dict), f'{cid}: evidence object required')
                for key in ('source', 'definition', 'geography', 'cohort', 'summary'):
                    require(nonempty(item.get(key)), f'{cid}: evidence {key} required')
                require(item['source'].startswith(('https://', 'http://', '/')), f'{cid}: traceable source required')
                ds, de = date.fromisoformat(item['data_start']), date.fromisoformat(item['data_end'])
                accessed = date.fromisoformat(item['accessed_on'])
                require(ds <= de <= as_of and de <= accessed <= as_of, f'{cid}: invalid evidence dates')
                if item['source'] not in sources:
                    sources.append(item['source'])
            points[cid] = cat['maximum'] * rating / 5
        known = sum(v for v in points.values() if v is not None)
        missing_weight = sum(c['maximum'] for c in cats if points[c['id']] is None)
        eligible = not missing and not holds
        total = known if eligible else None
        tier = (next(t['label'] for t in model['tiers'] if total >= t['minimum']) if eligible
                else 'Outside selected scope' if outside else 'Pending evidence' if missing else 'Review hold')
        if eligible and assumptions:
            tier += ' (provisional)'
        sectors = {}
        for sector in ('marketability', 'financial', 'execution'):
            values = [points[c['id']] for c in cats if c['sector'] == sector]
            sectors[sector] = sum(values) if all(v is not None for v in values) else None
        notes = (record['investment_notes'] if nonempty(record.get('investment_notes'))
                 else 'Preliminary six-category analyst screen.' if assumptions
                 else 'Six-category investment and execution screen.')
        notes = ' '.join(notes.split())
        caution = []
        if missing:
            caution.append('Missing category evidence: ' + ', '.join(c['header'] for c in cats if c['id'] in missing))
        caution.extend(holds)
        if nonempty(record.get('caution')):
            caution.append(record['caution'])
        if kind == 'fictional':
            notes = 'FICTIONAL DEMONSTRATION. ' + notes
        row = [record['name'], record['area'], *[points[c['id']] for c in cats], total, tier, notes, ' '.join(caution)]
        require(len(row) == 12, 'Output row must contain exactly 12 columns')
        results.append({'id': rid, 'comparison_group': group, 'status': 'PROVISIONAL' if eligible and assumptions else 'COMPLETE' if eligible else 'INCOMPLETE' if missing else 'HOLD',
                        'category_points': points, 'total': total, 'tier': tier, 'subsectors': sectors,
                        'analyst_assumptions': assumptions, 'source_urls': sources,
                        'known_points': known, 'missing_weight': missing_weight,
                        'possible_completion_range': [known, known + missing_weight], 'row': row})
    return {'model_id': model['model_id'], 'data_kind': kind, 'headers': model['headers'],
            'result_type': 'FICTIONAL_DEMONSTRATION' if kind == 'fictional' else 'UNRESEARCHED_TEMPLATE' if kind == 'unresearched' else 'ANALYST_PRELIMINARY_ESTIMATE' if any(r['analyst_assumptions'] for r in results) else 'EVIDENCE_BASED_JUDGMENT_SCREEN',
            'notice': 'Field/arithmetic checks only; source truth and rating adequacy require research review. Deliver only the 12-column rows; diagnostics are internal.',
            'results': results}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    args = parser.parse_args()
    try:
        output = score_dataset(json.loads(args.input.read_text()))
    except (ValueError, TypeError, KeyError) as error:
        parser.exit(2, f'Input error: {error}\n')
    print(json.dumps(output, indent=2, ensure_ascii=False, allow_nan=False))
