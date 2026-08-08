"""
Type D Cross-Validation — 11:00 PT Aug 8, 2026

Validates:
1. Three bug fixes from this run:
   - Meta showcase_coercive_cycle section isolation (not naive string match)
   - Atlantic silence day count resilience (>= 27, not hardcoded)
   - Amazon marketplace source_urls plural key acceptance
2. 10:00 PT Type C finding: Meta Q2 2026 inverse financial leverage
3. Today's Aug 8 test file integrity (all 8+ aug8 files present)
4. Entity set growth stability (>= 11 entities)
5. Structural consistency of fixed tests
"""

import pathlib
import re
import unittest

import yaml

_REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
_PROFILES = _REPO_ROOT / "profiles"


def _load_yaml(name: str) -> dict:
    with open(_PROFILES / name) as f:
        return yaml.safe_load(f)


class TestShowcaseIsolationFix(unittest.TestCase):
    """Meta may reference Showcase comparatively but must not OWN a
    showcase_coercive_cycle section — only Google does."""

    @classmethod
    def setUpClass(cls):
        cls.entities = _load_yaml("competitor-entities.yaml")

    def test_google_has_showcase_coercive_cycle(self):
        google = self.entities['entities']['google']
        self.assertIn('showcase_coercive_cycle', google)

    def test_meta_lacks_showcase_coercive_cycle(self):
        meta = self.entities['entities']['meta']
        self.assertNotIn('showcase_coercive_cycle', meta)

    def test_meta_may_reference_showcase_comparatively(self):
        """Meta's inverse leverage or other sections may mention Showcase
        in a comparative context — this is expected and correct."""
        meta = self.entities['entities']['meta']
        meta_str = str(meta).lower()
        # Presence of 'showcase' is fine as long as it's not a dedicated section
        if 'showcase' in meta_str:
            self.assertNotIn('showcase_coercive_cycle', meta,
                             "Meta references Showcase comparatively, "
                             "which is fine, but must not own the section")

    def test_google_coercive_stages_present(self):
        google = self.entities['entities']['google']
        cycle = google['showcase_coercive_cycle']
        stage_keys = [k for k in cycle if k.startswith('stage_')]
        self.assertGreaterEqual(len(stage_keys), 3,
                                "Google should have >= 3 coercive stages")


class TestAtlanticSilenceDayCountResilience(unittest.TestCase):
    """Atlantic silence day count grows over time — tests must use
    >= floor checks, not hardcoded exact values."""

    @classmethod
    def setUpClass(cls):
        cls.research = _load_yaml("competitor-coverage-research.yaml")

    def test_atlantic_silence_exists(self):
        atlantic = self.research['publications']['atlantic']
        self.assertIn('apple_v_openai_editorial_silence', atlantic)

    def test_silence_day_count_at_least_27(self):
        """Silence started Jul 10 and only grows. Must be >= 27."""
        silence = self.research['publications']['atlantic']['apple_v_openai_editorial_silence']
        desc = str(silence.get('description', ''))
        day_counts = [int(m) for m in re.findall(r'(\d+)\s*days?', desc)]
        self.assertTrue(any(d >= 27 for d in day_counts),
                        f"Expected silence >= 27 days, found: {day_counts}")

    def test_silence_day_count_not_hardcoded_27(self):
        """Verify the fixed test file no longer uses hardcoded '27' assertion."""
        test_file = _REPO_ROOT / "tests" / "test_type_d_7pm_cross_validation_aug6.py"
        content = test_file.read_text()
        # Should NOT contain assertIn('27', ...) for silence
        self.assertNotIn("assertIn('27'", content,
                         "Hardcoded '27' assertion should have been replaced")


class TestAmazonMarketplaceSourceFix(unittest.TestCase):
    """Amazon marketplace uses source_urls (plural), not source_url."""

    @classmethod
    def setUpClass(cls):
        cls.entities = _load_yaml("competitor-entities.yaml")

    def test_amazon_marketplace_has_source_urls(self):
        summary = self.entities['meta_ai_deals']['cross_platform_summary']
        am = summary['amazon_marketplace_emerging']
        urls = am.get('source_urls', [])
        self.assertTrue(len(urls) > 0,
                        "Amazon marketplace should have source_urls list")

    def test_amazon_marketplace_source_contains_wsj(self):
        summary = self.entities['meta_ai_deals']['cross_platform_summary']
        am = summary['amazon_marketplace_emerging']
        urls = am.get('source_urls', [])
        urls_str = str(urls).lower()
        self.assertIn('wsj', urls_str)

    def test_fixed_test_handles_both_keys(self):
        """The fixed test file should handle source_urls or source_url."""
        test_file = _REPO_ROOT / "tests" / "test_nyt_project_giraffe_xai_absence.py"
        content = test_file.read_text()
        # Should reference source_urls (plural)
        self.assertIn("source_urls", content)


class TestMetaQ2InverseLeverage(unittest.TestCase):
    """Validates the 10:00 PT Type C finding: Meta Q2 2026 earnings
    and inverse financial leverage paradox."""

    @classmethod
    def setUpClass(cls):
        cls.entities = _load_yaml("competitor-entities.yaml")

    def test_meta_has_q2_2026_earnings(self):
        meta = self.entities['entities']['meta']
        self.assertIn('q2_2026_earnings', meta)

    def test_q2_revenue(self):
        q2 = self.entities['entities']['meta']['q2_2026_earnings']
        self.assertAlmostEqual(q2['total_revenue_b'], 60.8, places=1)

    def test_q2_yoy_growth(self):
        q2 = self.entities['entities']['meta']['q2_2026_earnings']
        self.assertEqual(q2['total_revenue_yoy_pct'], 28)

    def test_q2_report_date(self):
        q2 = self.entities['entities']['meta']['q2_2026_earnings']
        self.assertEqual(q2['report_date'], '2026-07-29')

    def test_meta_has_inverse_financial_leverage(self):
        meta = self.entities['entities']['meta']
        self.assertIn('inverse_financial_leverage', meta)

    def test_inverse_leverage_has_overview(self):
        inv = self.entities['entities']['meta']['inverse_financial_leverage']
        self.assertIn('overview', inv)

    def test_inverse_leverage_has_mechanisms(self):
        inv = self.entities['entities']['meta']['inverse_financial_leverage']
        self.assertIn('mechanism_count', inv)
        self.assertIn('mechanisms_meta_lacks', inv)

    def test_inverse_leverage_has_sources(self):
        inv = self.entities['entities']['meta']['inverse_financial_leverage']
        urls = inv.get('source_urls', [])
        self.assertTrue(len(urls) > 0)

    def test_inverse_leverage_comparison_table(self):
        inv = self.entities['entities']['meta']['inverse_financial_leverage']
        self.assertIn('comparison_table', inv)

    def test_meta_inverse_leverage_test_file_exists(self):
        test_file = _REPO_ROOT / "tests" / "test_meta_inverse_leverage_q2_2026_aug8.py"
        self.assertTrue(test_file.exists(),
                        "Type C 10:00 PT test file should exist")


class TestAug8FileIntegrity(unittest.TestCase):
    """All Aug 8 test files should exist and be non-empty."""

    EXPECTED_AUG8_FILES = [
        "test_type_d_03am_cross_validation_aug8.py",
        "test_type_d_07am_cross_validation_aug8.py",
        "test_type_d_11am_cross_validation_aug8.py",
        "test_atlantic_wong_cross_entity_framing_aug8.py",
        "test_advance_dual_asset_monetization_aug8.py",
        "test_google_showcase_coercive_cycle_aug8.py",
        "test_nyt_google_traffic_cannibalization_paradox_aug8.py",
        "test_wired_amazon_surveillance_parity_paradox_aug8.py",
        "test_meta_inverse_leverage_q2_2026_aug8.py",
    ]

    def test_all_aug8_files_exist(self):
        tests_dir = _REPO_ROOT / "tests"
        missing = [f for f in self.EXPECTED_AUG8_FILES
                   if not (tests_dir / f).exists()]
        self.assertEqual(missing, [],
                         f"Missing Aug 8 test files: {missing}")

    def test_aug8_files_not_empty(self):
        tests_dir = _REPO_ROOT / "tests"
        for fname in self.EXPECTED_AUG8_FILES:
            path = tests_dir / fname
            if path.exists():
                self.assertGreater(path.stat().st_size, 100,
                                   f"{fname} should not be empty")


class TestEntitySetStability(unittest.TestCase):
    """Entity set should be >= 11 (8 original + Samsung + Microsoft + Snowflake)."""

    @classmethod
    def setUpClass(cls):
        cls.entities = _load_yaml("competitor-entities.yaml")

    def test_entity_count_floor(self):
        count = len(self.entities['entities'])
        self.assertGreaterEqual(count, 11,
                                f"Entity count {count} below floor of 11")

    def test_required_entities_present(self):
        required = ['meta', 'openai', 'google', 'apple', 'amazon',
                     'anthropic', 'xai', 'samsung', 'microsoft', 'snowflake']
        entities = self.entities['entities']
        missing = [e for e in required if e not in entities]
        self.assertEqual(missing, [],
                         f"Missing required entities: {missing}")


class TestTestFileCountIntegrity(unittest.TestCase):
    """Overall test file count should be >= 228."""

    def test_minimum_file_count(self):
        tests_dir = _REPO_ROOT / "tests"
        count = len(list(tests_dir.glob("test_*.py")))
        self.assertGreaterEqual(count, 228,
                                f"Test file count {count} below expected floor")


class TestAllSourceURLsHTTPS(unittest.TestCase):
    """Regression: all source URLs across profiles should use HTTPS."""

    def test_no_http_urls_in_entities(self):
        content = (_PROFILES / "competitor-entities.yaml").read_text()
        http_urls = re.findall(r'http://[^\s\'"]+', content)
        self.assertEqual(http_urls, [],
                         f"HTTP URLs found (should be HTTPS): {http_urls[:5]}")

    def test_no_http_urls_in_research(self):
        content = (_PROFILES / "competitor-coverage-research.yaml").read_text()
        http_urls = re.findall(r'http://[^\s\'"]+', content)
        self.assertEqual(http_urls, [],
                         f"HTTP URLs found (should be HTTPS): {http_urls[:5]}")


if __name__ == "__main__":
    unittest.main()
