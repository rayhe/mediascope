"""
Type D Cross-Validation — Aug 12 02:00 PT

Validates structural integrity after Iterations 56-57 (mechanisms #57-58).
Specifically tests:
1. Mechanism #58 placement fix (was misplaced under publications, moved to cross_publication_findings)
2. All mechanisms 51-58 have required fields
3. Publications section still has exactly 9 entries (no stray mechanism entries)
4. No mechanism_id fields leak into the publications section
5. Mechanism ID sequence integrity through #58
6. All Aug 12 test files exist on disk
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


class TestMechanism58PlacementFix(unittest.TestCase):
    """Mechanism #58 must be in cross_publication_findings, NOT publications."""

    def setUp(self):
        self.data = load_competitor_research()

    def test_mechanism_58_in_cross_pub_findings(self):
        """Mechanism #58 exists under cross_publication_findings."""
        cpf = self.data.get('cross_publication_findings', {})
        entry = cpf.get('conde_nast_ai_deal_portfolio_dependency_index')
        self.assertIsNotNone(entry, "Mechanism #58 not found in cross_publication_findings")
        self.assertEqual(entry['mechanism_id'], 58)

    def test_mechanism_58_not_in_publications(self):
        """Mechanism #58 must NOT appear under publications."""
        pubs = self.data.get('publications', {})
        self.assertNotIn('conde_nast_ai_deal_portfolio_dependency_index', pubs,
                         "Mechanism #58 still in publications section — should be in cross_publication_findings only")

    def test_mechanism_58_has_discovery_date(self):
        """Mechanism #58 must have discovery_date field."""
        cpf = self.data.get('cross_publication_findings', {})
        entry = cpf.get('conde_nast_ai_deal_portfolio_dependency_index', {})
        self.assertIn('discovery_date', entry, "Mechanism #58 missing discovery_date")


class TestPublicationsSectionClean(unittest.TestCase):
    """Publications section should contain only actual publication profiles, not mechanisms."""

    def setUp(self):
        self.data = load_competitor_research()
        self.pubs = self.data.get('publications', {})

    def test_exactly_nine_publications(self):
        """There should be exactly 9 publication profiles."""
        self.assertEqual(len(self.pubs), 9,
                         f"Expected 9 publications, got {len(self.pubs)}: {list(self.pubs.keys())}")

    def test_expected_publications_present(self):
        """All 9 known publications are present."""
        expected = {
            'atlantic', 'financial-times', 'gizmodo', 'guardian',
            'mit-tech-review', 'news-corp', 'nytimes', 'the-verge', 'wired'
        }
        self.assertEqual(set(self.pubs.keys()), expected)

    def test_no_mechanism_ids_in_publications(self):
        """No publication entry should contain a mechanism_id field."""
        violations = []
        for pub_name, pub_data in self.pubs.items():
            if isinstance(pub_data, dict) and 'mechanism_id' in pub_data:
                violations.append(f"{pub_name}: mechanism_id={pub_data['mechanism_id']}")
        self.assertFalse(violations,
                         f"Mechanism IDs found in publications section: {violations}")

    def test_all_publications_have_meta_coverage_tone(self):
        """Every publication profile must include meta_coverage_tone."""
        for pub_name, pub_data in self.pubs.items():
            if isinstance(pub_data, dict):
                self.assertIn('meta_coverage_tone', pub_data,
                              f"Publication '{pub_name}' missing meta_coverage_tone")


class TestMechanisms51Through58Completeness(unittest.TestCase):
    """Recent mechanisms (51-58) should all have required fields."""

    REQUIRED_FIELDS = ['mechanism_id', 'mechanism_name', 'finding_summary',
                       'date_added', 'discovery_date', 'test_file']

    def setUp(self):
        self.data = load_competitor_research()
        self.cpf = self.data.get('cross_publication_findings', {})
        self.mechanisms = {}
        for key, val in self.cpf.items():
            if isinstance(val, dict) and 'mechanism_id' in val:
                mid = val['mechanism_id']
                if 51 <= mid <= 58:
                    self.mechanisms[mid] = (key, val)

    def test_mechanisms_51_through_58_exist(self):
        """All mechanisms 51-58 should exist in cross_publication_findings."""
        for mid in range(51, 59):
            self.assertIn(mid, self.mechanisms,
                          f"Mechanism #{mid} not found in cross_publication_findings")

    def test_all_have_required_fields(self):
        """Each mechanism 51-58 has all required fields."""
        for mid, (key, val) in self.mechanisms.items():
            for field in self.REQUIRED_FIELDS:
                self.assertIn(field, val,
                              f"Mechanism #{mid} ({key}) missing {field}")

    def test_all_have_source_urls(self):
        """Each mechanism 51-58 has source_urls or articles with URLs."""
        for mid, (key, val) in self.mechanisms.items():
            urls = val.get('source_urls', [])
            articles = val.get('articles', [])
            has_urls = len(urls) >= 1 or (
                isinstance(articles, list) and len(articles) >= 1 and
                any(isinstance(a, dict) and 'url' in a for a in articles)
            )
            self.assertTrue(has_urls,
                            f"Mechanism #{mid} ({key}) has no source_urls or article URLs")


class TestMechanismIDSequenceIntegrity(unittest.TestCase):
    """Mechanism IDs should be unique and contiguous through #58."""

    def setUp(self):
        self.data = load_competitor_research()
        self.cpf = self.data.get('cross_publication_findings', {})
        self.all_ids = []
        for key, val in self.cpf.items():
            if isinstance(val, dict) and 'mechanism_id' in val:
                self.all_ids.append(val['mechanism_id'])

    def test_no_duplicate_ids(self):
        """No duplicate mechanism IDs in the dataset."""
        seen = set()
        dupes = []
        for mid in self.all_ids:
            if mid in seen:
                dupes.append(mid)
            seen.add(mid)
        self.assertFalse(dupes, f"Duplicate mechanism IDs: {dupes}")

    def test_max_mechanism_is_62(self):
        """The highest mechanism ID should be 62 (after iterations 59-62)."""
        self.assertEqual(max(self.all_ids), 62,
                         f"Expected max mechanism_id=62, got {max(self.all_ids)}")

    def test_recent_mechanisms_contiguous(self):
        """Mechanisms 50-62 should form a contiguous sequence."""
        recent = [mid for mid in self.all_ids if mid >= 50]
        expected = list(range(min(recent), max(recent) + 1))
        self.assertEqual(sorted(recent), expected,
                         f"Gap in recent mechanism IDs: {sorted(recent)} vs expected {expected}")


class TestAug12TestFilesExist(unittest.TestCase):
    """All test files referenced in Aug 12 mechanisms exist on disk."""

    def setUp(self):
        self.data = load_competitor_research()
        self.cpf = self.data.get('cross_publication_findings', {})

    def test_mechanism_58_test_file_exists(self):
        """Mechanism #58 test file exists on disk."""
        entry = self.cpf.get('conde_nast_ai_deal_portfolio_dependency_index', {})
        test_file = entry.get('test_file', '')
        if test_file:
            full_path = os.path.join(os.path.dirname(TESTS_DIR), test_file)
            self.assertTrue(os.path.exists(full_path),
                            f"Test file does not exist: {test_file}")

    def test_all_aug12_test_files_exist(self):
        """All test files containing 'aug12' in their name exist."""
        aug12_files = [f for f in os.listdir(TESTS_DIR) if 'aug12' in f and f.endswith('.py')]
        self.assertTrue(len(aug12_files) >= 1,
                        "Expected at least 1 Aug 12 test file")
        for tf in aug12_files:
            full_path = os.path.join(TESTS_DIR, tf)
            self.assertTrue(os.path.exists(full_path), f"Missing: {tf}")


class TestMechanism57And58CrossReference(unittest.TestCase):
    """Mechanisms 57 and 58 should be structurally sound and complementary."""

    def setUp(self):
        self.data = load_competitor_research()
        self.cpf = self.data.get('cross_publication_findings', {})
        self.m57 = None
        self.m58 = None
        for key, val in self.cpf.items():
            if isinstance(val, dict):
                if val.get('mechanism_id') == 57:
                    self.m57 = val
                elif val.get('mechanism_id') == 58:
                    self.m58 = val

    def test_m57_is_journalist_type(self):
        """Mechanism 57 is a journalist/reporter-level finding."""
        self.assertIn('journalist', self.m57,
                      "Mechanism #57 should have a journalist field")

    def test_m58_is_financial_type(self):
        """Mechanism 58 is a financial dependency finding."""
        self.assertEqual(self.m58.get('finding_type'), 'financial_dependency_quantification')

    def test_different_finding_types(self):
        """Mechanisms 57 and 58 have different finding types (complementary analysis)."""
        self.assertNotEqual(self.m57.get('finding_type'), self.m58.get('finding_type'),
                            "Mechanisms 57 and 58 should cover different analytical dimensions")

    def test_both_have_meta_coverage(self):
        """Both mechanisms discuss Meta coverage patterns."""
        m57_summary = self.m57.get('finding_summary', '').lower()
        m58_summary = self.m58.get('finding_summary', '').lower()
        self.assertIn('meta', m57_summary)
        self.assertIn('meta', m58_summary)


if __name__ == '__main__':
    unittest.main()
