"""Fictional behavioral checks for the current six-category model."""
import copy
import json
from pathlib import Path
import unittest

from score_neighborhoods import load_model, score_dataset
from value_entry import rate_entry


def fixture(rating=4):
    model = load_model()
    evidence = {'source': '/tmp/FICTIONAL-evidence.txt', 'definition': 'Fictional category observation',
                'geography': 'Fictional neighborhood', 'cohort': 'Fictional two-family cohort',
                'summary': 'Fictional observations for arithmetic tests only',
                'data_start': '2025-11-01', 'data_end': '2026-10-31', 'accessed_on': '2026-11-07'}
    return {'model_id': model['model_id'], 'data_kind': 'fictional', 'as_of': '2026-11-07',
            'window_start': '2025-11-01', 'window_end': '2026-10-31', 'records': [{
                'id': 'fictional-1', 'name': 'FICTIONAL', 'area': 'Fictional neighborhood',
                'municipality': 'Fictional municipality', 'property_cohort': 'Fictional two-family cohort',
                'comparison_group': 'fictional-group', 'geography_verified': True,
                'boundary_source': '/tmp/FICTIONAL-boundary.json', 'comparability_verified': True,
                'category_observations': {c['id']: {'rating': rating, 'rationale': 'Fictional rubric test',
                                                  'evidence': [copy.deepcopy(evidence)]}
                                          for c in model['categories']}}]}


def result(data):
    return score_dataset(data)['results'][0]


class ScoringTests(unittest.TestCase):
    def test_endpoints_and_tiers(self):
        for rating, total, tier in [(0, 0, 'Low priority'), (1, 20, 'Low priority'), (2, 40, 'Low priority'),
                                    (3, 60, 'Selective'), (4, 80, 'Priority'), (5, 100, 'Priority')]:
            with self.subTest(rating=rating):
                r = result(fixture(rating)); self.assertEqual(r['total'], total); self.assertEqual(r['tier'], tier)

    def test_reference_layout_and_maxima(self):
        output = score_dataset(fixture(5)); r = output['results'][0]
        self.assertEqual(len(output['headers']), 12); self.assertEqual(len(r['row']), 12)
        self.assertEqual(r['row'][2:8], [20, 20, 15, 15, 15, 15])
        self.assertEqual(output['headers'][8:10], ['Total /100', 'Screening tier'])

    def test_finance_does_not_change_marketability(self):
        data = fixture(); before = result(data)
        data['records'][0]['category_observations']['acquisition_economics']['rating'] = 0
        after = result(data)
        self.assertEqual(before['subsectors']['marketability'], 56)
        self.assertEqual(after['subsectors']['marketability'], 56)
        self.assertEqual(after['total'], 68)

    def test_renovation_does_not_change_marketability(self):
        data = fixture(); data['records'][0]['category_observations']['renovation_repeatability']['rating'] = 0
        r = result(data); self.assertEqual(r['subsectors']['marketability'], 56)
        self.assertEqual(r['subsectors']['execution'], 0)

    def test_missing_finance_not_zero_or_rebased(self):
        data = fixture(); data['records'][0]['category_observations']['acquisition_economics']['rating'] = None
        r = result(data)
        self.assertIsNone(r['total']); self.assertEqual(r['known_points'], 68)
        self.assertEqual(r['possible_completion_range'], [68, 83])
        self.assertIsNone(r['row'][5]); self.assertIsNone(r['row'][8]); self.assertEqual(r['tier'], 'Pending evidence')

    def test_material_hold(self):
        data = fixture(); data['records'][0]['material_evidence_holds'] = ['Unresolved sample representativeness']
        r = result(data); self.assertIsNone(r['total']); self.assertEqual(r['tier'], 'Review hold')

    def test_outside_scope(self):
        data = fixture(); data['records'][0]['in_scope'] = False
        r = result(data); self.assertIsNone(r['total']); self.assertEqual(r['tier'], 'Outside selected scope')

    def test_unresearched_never_gets_total(self):
        data = fixture(); data['data_kind'] = 'unresearched'
        self.assertIsNone(result(data)['total'])

    def test_invalid_ratings(self):
        for rating in (-1, 6, True, 2.5, '4'):
            with self.subTest(rating=rating):
                with self.assertRaises(ValueError): result(fixture(rating))

    def test_evidence_required(self):
        data = fixture(); data['records'][0]['category_observations']['buyer_depth']['evidence'] = []
        with self.assertRaises(ValueError): result(data)

    def test_future_evidence_rejected(self):
        data = fixture(); data['records'][0]['category_observations']['buyer_depth']['evidence'][0]['data_end'] = '2026-11-08'
        with self.assertRaises(ValueError): result(data)

    def test_unknown_category_rejected(self):
        data = fixture(); data['records'][0]['category_observations']['alternative_score'] = {'rating': 5}
        with self.assertRaises(ValueError): result(data)

    def test_incompatible_cohorts_rejected(self):
        data = fixture(); other = copy.deepcopy(data['records'][0]); other['id'] = 'fictional-2'
        other['property_cohort'] = 'Different product'; data['records'].append(other)
        with self.assertRaises(ValueError): score_dataset(data)

    def test_fictional_results_labeled(self):
        output = score_dataset(fixture())
        self.assertEqual(output['result_type'], 'FICTIONAL_DEMONSTRATION')
        self.assertIn('FICTIONAL DEMONSTRATION', output['results'][0]['row'][10])

    def test_estimate_requires_assumptions(self):
        data = fixture(); entry = data['records'][0]['category_observations']['acquisition_economics']
        entry['rating_basis'] = 'analyst_estimate'
        with self.assertRaises(ValueError): result(data)

    def test_estimate_is_provisional_not_verified(self):
        data = fixture(); data['data_kind'] = 'observed'
        entry = data['records'][0]['category_observations']['acquisition_economics']
        entry.update(rating_basis='analyst_estimate', assumptions=['Illustrative work allowance, not a quote'])
        output = score_dataset(data); row = output['results'][0]
        self.assertEqual(row['total'], 80)
        self.assertEqual(row['status'], 'PROVISIONAL')
        self.assertEqual(row['tier'], 'Priority (provisional)')
        self.assertEqual(output['result_type'], 'ANALYST_PRELIMINARY_ESTIMATE')
        self.assertIn('acquisition_economics', row['analyst_assumptions'])

    def test_short_paragraphs_keep_sources_out_of_prose(self):
        data = fixture(); data['records'][0]['investment_notes'] = 'Short analyst view.\nOne paragraph.'
        row = result(data)
        self.assertNotIn('\n', row['row'][10])
        self.assertNotIn('/tmp/FICTIONAL', row['row'][10])
        self.assertTrue(row['source_urls'])

    def test_fair_entry_boundaries_and_coverage(self):
        for entry, expected in [(80000, 5), (80001, 4), (95000, 4), (95001, 3),
                                (120000, 3), (120001, 2), (138000, 2), (138001, 1)]:
            self.assertEqual(rate_entry(entry, 100000, 120000, 'strong')['rating'], expected)
        self.assertEqual(rate_entry(80000, 100000, 120000, 'limited')['rating'], 3)
        self.assertEqual(rate_entry(80000, 100000, 120000, 'moderate')['rating'], 4)
        self.assertEqual(rate_entry(150000, 100000, 120000, 'limited')['rating'], 1)

    def test_invalid_value_bands(self):
        for entry, low, high in [(True, 100, 120), (0, 100, 120), (100, 120, 110),
                                  (100, float('nan'), 120), (100, 90, float('inf'))]:
            with self.assertRaises(ValueError): rate_entry(entry, low, high)

    def test_tier_boundaries_are_anchor_based(self):
        model = load_model()
        for total, expected in [(44, 'Low priority'), (45, 'Watchlist'), (59, 'Watchlist'),
                                (60, 'Selective'), (74, 'Selective'), (75, 'Priority')]:
            actual = next(t['label'] for t in model['tiers'] if total >= t['minimum'])
            self.assertEqual(actual, expected)

    def test_another_region_uses_same_arithmetic(self):
        data = fixture(3)
        data['records'][0]['municipality'] = 'FICTIONAL municipality outside New York'
        data['records'][0]['area'] = 'FICTIONAL region; locally researched scenario assumed'
        self.assertEqual(result(data)['total'], 60)
        data['records'][0]['in_scope'] = False
        self.assertEqual(result(data)['tier'], 'Outside selected scope')

    def test_no_fixed_property_count(self):
        data = fixture(3)
        other = copy.deepcopy(data['records'][0]); other['id'] = 'fictional-2'
        data['records'].append(other)
        output = score_dataset(data)
        self.assertEqual(len(output['results']), 2)
        self.assertTrue(all(r['total'] == 60 for r in output['results']))

    def test_public_example_is_reproducible_and_fictional(self):
        root = Path(__file__).resolve().parents[1]
        source = json.loads((root / 'examples/albany-demo-input.json').read_text())
        expected = json.loads((root / 'examples/albany-demo-output.json').read_text())
        actual = score_dataset(source)
        self.assertEqual(actual, expected)
        self.assertEqual(actual['result_type'], 'FICTIONAL_DEMONSTRATION')
        self.assertEqual(actual['results'][0]['row'][2:9], [12,8,9,9,9,9,56])


if __name__ == '__main__':
    unittest.main()
