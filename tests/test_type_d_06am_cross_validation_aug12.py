"""
Type D Cross-Validation — Aug 12 06:00 PT

Validates structural integrity after Iterations 59-61 (mechanisms #59-61).
Specifically tests:
1. Mechanism #60 data integrity fix — confounding_factors/testable_predictions/cross_references
   were missing from competitor-coverage-research.yaml (accidentally placed under #61)
2. Mechanism #61 data integrity fix — Karen Hao content replaced with correct Apple News+ content
3. All mechanisms 59-61 have required fields in competitor-coverage-research.yaml
4. Mechanism #60 cross-references match expected targets (#57, #49, #17)
5. Mechanism #61 cross-references match expected targets (#30, #43, #47, #55)
6. No Karen Hao content leaks into Apple News+ mechanism
7. All Aug 12 test files exist on disk
8. Mechanism ID sequence contiguous through #61
"""

import os
import unittest

import yaml

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
TESTS_DIR = os.path.dirname(__file__)


def load_competitor_research():
    path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


def load_competitor_entities():
    path = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


def get_mechanism(data, mechanism_id):
    cpf = data.get('cross_publication_findings', {})
    for key, val in cpf.items():
        if isinstance(val, dict) and val.get('mechanism_id') == mechanism_id:
            return key, val
    return None, None


class TestMechanism60DataIntegrityFix(unittest.TestCase):
    """Mechanism #60 (Karen Hao) must have its own confounding_factors, not be empty."""

    def setUp(self):
        self.data = load_competitor_research()
        _, self.m60 = get_mechanism(self.data, 60)

    def test_m60_exists(self):
        self.assertIsNotNone(self.m60, "Mechanism #60 not found")

    def test_m60_has_confounding_factors(self):
        cf = self.m60.get('confounding_factors', [])
        self.assertGreaterEqual(len(cf), 5, f"Expected 5+ confounding factors, got {len(cf)}")

    def test_m60_has_testable_predictions(self):
        tp = self.m60.get('testable_predictions', [])
        self.assertGreaterEqual(len(tp), 3, f"Expected 3+ predictions, got {len(tp)}")

    def test_m60_has_cross_references(self):
        xr = self.m60.get('cross_references', [])
        self.assertGreaterEqual(len(xr), 3, f"Expected 3+ cross-references, got {len(xr)}")

    def test_m60_confounding_factors_mention_hao(self):
        """Confounding factors should be about Karen Hao, not Apple News+."""
        cf_text = str(self.m60.get('confounding_factors', []))
        self.assertTrue('hao' in cf_text.lower() or 'facebook' in cf_text.lower()
                        or 'investigation' in cf_text.lower(),
                        "Confounding factors should reference Hao/Facebook investigation")

    def test_m60_xrefs_reference_57(self):
        """Should cross-reference mechanism #57 (Seetharaman frame-lock)."""
        xr_text = str(self.m60.get('cross_references', []))
        self.assertIn('57', xr_text, "Should reference mechanism #57")

    def test_m60_xrefs_reference_49(self):
        """Should cross-reference mechanism #49 (entity targeting)."""
        xr_text = str(self.m60.get('cross_references', []))
        self.assertIn('49', xr_text, "Should reference mechanism #49")

    def test_m60_xrefs_reference_mit(self):
        """Should cross-reference MIT TR profile."""
        xr_text = str(self.m60.get('cross_references', []))
        self.assertIn('MIT', xr_text, "Should reference MIT TR profile")


class TestMechanism61DataIntegrityFix(unittest.TestCase):
    """Mechanism #61 (Apple News+) must have Apple-specific content, not Karen Hao's."""

    def setUp(self):
        self.data = load_competitor_research()
        _, self.m61 = get_mechanism(self.data, 61)

    def test_m61_exists(self):
        self.assertIsNotNone(self.m61, "Mechanism #61 not found")

    def test_m61_has_confounding_factors(self):
        cf = self.m61.get('confounding_factors', [])
        self.assertGreaterEqual(len(cf), 7, f"Expected 7+ confounding factors, got {len(cf)}")

    def test_m61_has_testable_predictions(self):
        tp = self.m61.get('testable_predictions', [])
        self.assertGreaterEqual(len(tp), 4, f"Expected 4+ predictions, got {len(tp)}")

    def test_m61_has_cross_references(self):
        xr = self.m61.get('cross_references', [])
        self.assertGreaterEqual(len(xr), 3, f"Expected 3+ cross-references, got {len(xr)}")

    def test_m61_confounding_factors_not_hao(self):
        """Apple News+ confounding factors must NOT contain Karen Hao content."""
        cf_text = str(self.m61.get('confounding_factors', []))
        self.assertNotIn('Hao', cf_text,
                         "Karen Hao content leaked into Apple News+ confounding factors")
        self.assertNotIn('Gebru', cf_text,
                         "Gebru crisis content leaked into Apple News+ confounding factors")

    def test_m61_confounding_factors_are_apple_specific(self):
        """Confounding factors should reference Apple/privacy/glasses."""
        cf_text = str(self.m61.get('confounding_factors', []))
        self.assertTrue('privacy' in cf_text.lower() or 'apple' in cf_text.lower()
                        or 'glasses' in cf_text.lower(),
                        "Confounding factors should reference Apple/privacy/glasses")

    def test_m61_predictions_reference_wired(self):
        """Testable predictions should mention WIRED."""
        tp_text = str(self.m61.get('testable_predictions', []))
        self.assertIn('WIRED', tp_text, "Should predict WIRED's N50 coverage")

    def test_m61_predictions_reference_ft(self):
        """Testable predictions should mention FT as control case."""
        tp_text = str(self.m61.get('testable_predictions', []))
        self.assertTrue('FT' in tp_text or 'Financial Times' in tp_text,
                        "Should predict FT as control case")

    def test_m61_xrefs_target_mechanisms(self):
        """Cross-references should target mechanisms #30, #43, #47, #55."""
        xr = self.m61.get('cross_references', [])
        xr_ids = [x.get('mechanism_id') for x in xr if isinstance(x, dict)]
        for expected_id in [30, 43, 47, 55]:
            self.assertIn(expected_id, xr_ids,
                          f"Mechanism #{expected_id} should be cross-referenced")

    def test_m61_source_urls_no_karen_hao_wikipedia(self):
        """Apple News+ source URLs should not include Karen Hao's Wikipedia page."""
        urls = self.m61.get('source_urls', [])
        for url in urls:
            self.assertNotIn('Karen_Hao', url,
                             "Karen Hao Wikipedia link should not be in Apple News+ sources")


class TestMechanism59Structure(unittest.TestCase):
    """Mechanism #59 (Guardian dual-role paradox) structural check."""

    def setUp(self):
        self.data = load_competitor_research()
        _, self.m59 = get_mechanism(self.data, 59)

    def test_m59_exists(self):
        self.assertIsNotNone(self.m59, "Mechanism #59 not found")

    def test_m59_has_required_fields(self):
        required = ['mechanism_id', 'finding_summary', 'source_urls']
        for field in required:
            self.assertIn(field, self.m59, f"Mechanism #59 missing {field}")

    def test_m59_has_testable_predictions(self):
        tp = self.m59.get('testable_predictions', [])
        self.assertGreaterEqual(len(tp), 3, f"Expected 3+ predictions, got {len(tp)}")

    def test_m59_discovery_date(self):
        self.assertEqual(self.m59.get('discovery_date'), '2026-08-12')


class TestMechanismIDSequenceThrough61(unittest.TestCase):
    """Mechanism IDs 1-61 should be contiguous with no gaps in the 50-61 range."""

    def setUp(self):
        data = load_competitor_research()
        cpf = data.get('cross_publication_findings', {})
        self.all_ids = []
        for key, val in cpf.items():
            if isinstance(val, dict) and 'mechanism_id' in val:
                self.all_ids.append(val['mechanism_id'])

    def test_max_mechanism_is_61(self):
        self.assertEqual(max(self.all_ids), 61,
                         f"Expected max mechanism_id=61, got {max(self.all_ids)}")

    def test_no_duplicate_ids(self):
        seen = set()
        dupes = []
        for mid in self.all_ids:
            if mid in seen:
                dupes.append(mid)
            seen.add(mid)
        self.assertFalse(dupes, f"Duplicate mechanism IDs: {dupes}")

    def test_50_through_61_contiguous(self):
        recent = sorted(mid for mid in self.all_ids if mid >= 50)
        expected = list(range(50, 62))
        self.assertEqual(recent, expected,
                         f"Gap in mechanisms 50-61: {recent} vs expected {expected}")


class TestAug12TestFilesCoverage(unittest.TestCase):
    """All Aug 12 test files exist and match expected set."""

    def test_expected_aug12_test_files_exist(self):
        expected = [
            'test_guardian_google_dual_role_paradox_aug12.py',  # mechanism 59
            'test_karen_hao_cross_entity.py',  # mechanism 60 (no date suffix)
            'test_apple_news_plus_glasses_prelaunch_alignment_aug12.py',  # mechanism 61
            'test_conde_nast_ai_deal_portfolio_dependency_index_aug12.py',  # mechanism 58
            'test_type_d_02am_cross_validation_aug12.py',
            'test_type_d_06am_cross_validation_aug12.py',
        ]
        for tf in expected:
            full_path = os.path.join(TESTS_DIR, tf)
            self.assertTrue(os.path.exists(full_path), f"Missing test file: {tf}")


class TestEntityYAMLConsistencyWithResearch(unittest.TestCase):
    """Mechanism data in competitor-entities.yaml should be consistent with
    competitor-coverage-research.yaml after the fix."""

    def setUp(self):
        self.research = load_competitor_research()
        self.entities = load_competitor_entities()

    def test_apple_entity_has_mechanism_61(self):
        apple = self.entities['entities']['apple']
        alignment = apple.get('apple_news_glasses_prelaunch_alignment', {})
        self.assertTrue(len(alignment) > 0, "Apple entity missing mechanism #61 data")

    def test_apple_entity_confounding_factors_match_count(self):
        """Both YAML files should have the same number of confounding factors for #61."""
        apple = self.entities['entities']['apple']
        entity_cf = apple.get('apple_news_glasses_prelaunch_alignment', {}).get('confounding_factors', [])
        _, m61 = get_mechanism(self.research, 61)
        research_cf = m61.get('confounding_factors', [])
        self.assertEqual(len(entity_cf), len(research_cf),
                         f"Confounding factor count mismatch: entities={len(entity_cf)}, research={len(research_cf)}")


if __name__ == '__main__':
    unittest.main()
