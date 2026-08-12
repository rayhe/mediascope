"""
Type D Cross-Validation: 5pm Aug 11, 2026

Validates:
1. Financial Times publication entry is unified (no duplicate financial_times/financial-times)
2. All mechanisms 42-50 have required fields (mechanism_id, date_added, discovery_date)
3. No duplicate mechanism IDs across cross_publication_findings
4. Heikkilä cross-entity data is accessible under canonical financial-times key
5. Publications count is exactly 9 (no duplicates)
6. All Aug 11 mechanisms have test files
"""

import os
import yaml
import unittest
from pathlib import Path
from collections import Counter

PROFILES_DIR = Path(__file__).parent.parent / "profiles"
TESTS_DIR = Path(__file__).parent


def load_yaml(filename):
    with open(PROFILES_DIR / filename) as f:
        return yaml.safe_load(f)


class TestFTUnification(unittest.TestCase):
    """Verify the Financial Times entry is unified under one canonical key."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_yaml("competitor-coverage-research.yaml")
        cls.pubs = cls.data.get("publications", {})

    def test_no_financial_underscore_key(self):
        """financial_times (underscore) should NOT exist as a separate key."""
        self.assertNotIn(
            "financial_times", self.pubs,
            "Duplicate 'financial_times' key found — should be merged into 'financial-times'"
        )

    def test_financial_hyphen_key_exists(self):
        """financial-times (hyphen) is the canonical key."""
        self.assertIn("financial-times", self.pubs)

    def test_ft_has_heikkila_data(self):
        """Heikkilä cross-entity data should be in the canonical FT entry."""
        ft = self.pubs["financial-times"]
        self.assertIn("heikkila_cross_entity", ft)

    def test_ft_has_google_data(self):
        """Google coverage analysis should be in the canonical FT entry."""
        ft = self.pubs["financial-times"]
        self.assertIn("google_coverage_summary", ft)
        self.assertIn("google_coverage_tone", ft)

    def test_ft_has_openai_data(self):
        """OpenAI deal analysis should be in the canonical FT entry."""
        ft = self.pubs["financial-times"]
        self.assertIn("openai_coverage_summary", ft)
        self.assertIn("openai_deal_source", ft)

    def test_ft_has_murgia_data(self):
        """Murgia cross-entity analysis should be in the canonical FT entry."""
        ft = self.pubs["financial-times"]
        self.assertIn("murgia_cross_entity", ft)

    def test_ft_has_meta_coverage_tone(self):
        """Meta coverage tone should exist."""
        ft = self.pubs["financial-times"]
        self.assertIn("meta_coverage_tone", ft)
        self.assertIsNotNone(ft["meta_coverage_tone"])

    def test_heikkila_has_coverage_by_entity(self):
        """Heikkilä cross-entity should have coverage breakdown by entity."""
        ft = self.pubs["financial-times"]
        heikkila = ft["heikkila_cross_entity"]
        self.assertIn("coverage_by_entity", heikkila)
        entities = heikkila["coverage_by_entity"]
        for entity in ["google", "openai", "meta", "anthropic"]:
            self.assertIn(entity, entities, f"Missing entity: {entity}")

    def test_heikkila_has_asymmetry_score(self):
        """Heikkilä analysis should have a quantified asymmetry score."""
        ft = self.pubs["financial-times"]
        heikkila = ft["heikkila_cross_entity"]
        self.assertIn("asymmetry_score", heikkila)
        score = heikkila["asymmetry_score"]
        self.assertGreater(score, 0.5, "FT asymmetry should be above neutral baseline")


class TestPublicationsCount(unittest.TestCase):
    """Verify exactly 9 unique publications (no duplicates)."""

    def test_exactly_nine_publications(self):
        data = load_yaml("competitor-coverage-research.yaml")
        pubs = data.get("publications", {})
        self.assertEqual(len(pubs), 9)

    def test_expected_publications_present(self):
        data = load_yaml("competitor-coverage-research.yaml")
        pubs = data.get("publications", {})
        expected = {
            "wired", "the-verge", "atlantic", "nytimes", "financial-times",
            "guardian", "mit-tech-review", "gizmodo", "news-corp"
        }
        self.assertEqual(set(pubs.keys()), expected)


class TestMechanism42to50Completeness(unittest.TestCase):
    """All mechanisms 42-50 should have required fields."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_yaml("competitor-coverage-research.yaml")
        cls.cpf = cls.data.get("cross_publication_findings", {})
        cls.mechanisms = {}
        for key, val in cls.cpf.items():
            if isinstance(val, dict):
                mid = val.get("mechanism_id")
                if mid and mid >= 42:
                    cls.mechanisms[mid] = (key, val)

    def test_mechanisms_42_through_50_exist(self):
        """All mechanism IDs 42-50 should be present."""
        for mid in range(42, 51):
            self.assertIn(mid, self.mechanisms, f"Mechanism #{mid} missing")

    def test_all_have_date_added(self):
        """Every mechanism should have date_added."""
        for mid, (key, val) in self.mechanisms.items():
            self.assertIn(
                "date_added", val,
                f"Mechanism #{mid} ({key}) missing date_added"
            )

    def test_all_have_discovery_date(self):
        """Every mechanism should have discovery_date."""
        for mid, (key, val) in self.mechanisms.items():
            self.assertIn(
                "discovery_date", val,
                f"Mechanism #{mid} ({key}) missing discovery_date"
            )

    def test_all_have_mechanism_name(self):
        """Every mechanism should have a mechanism_name."""
        for mid, (key, val) in self.mechanisms.items():
            self.assertIn(
                "mechanism_name", val,
                f"Mechanism #{mid} ({key}) missing mechanism_name"
            )

    def test_all_have_finding_summary(self):
        """Every mechanism should have a finding_summary."""
        for mid, (key, val) in self.mechanisms.items():
            self.assertIn(
                "finding_summary", val,
                f"Mechanism #{mid} ({key}) missing finding_summary"
            )

    def test_all_have_test_file(self):
        """Every mechanism should reference its test file."""
        for mid, (key, val) in self.mechanisms.items():
            self.assertIn(
                "test_file", val,
                f"Mechanism #{mid} ({key}) missing test_file reference"
            )


class TestNoDuplicateMechanismIDs(unittest.TestCase):
    """No two findings should share the same mechanism_id."""

    def test_unique_mechanism_ids(self):
        data = load_yaml("competitor-coverage-research.yaml")
        cpf = data.get("cross_publication_findings", {})
        ids = []
        for key, val in cpf.items():
            if isinstance(val, dict) and "mechanism_id" in val:
                ids.append(val["mechanism_id"])
        dupes = [k for k, v in Counter(ids).items() if v > 1]
        self.assertEqual(dupes, [], f"Duplicate mechanism IDs: {dupes}")


class TestAug11TestFilesExist(unittest.TestCase):
    """Every Aug 11 mechanism should have a corresponding test file on disk."""

    AUG11_TEST_FILES = [
        "test_chokkattu_wired_compound_competitor_silence_aug11.py",
        "test_dual_client_litigation_entanglement_index_aug11.py",
        "test_wired_apple_pcc_privacy_pivot_coverage_asymmetry_aug11.py",
        "test_ashworth_wwdc_pcc_privacy_framing_aug11.py",
        "test_pre_ipo_underwriter_client_publisher_convergence_aug11.py",
        "test_meta_ad_competitor_structural_antagonism_aug11.py",
        "test_wired_openai_ad_coverage_selection_gap_aug11.py",
        "test_bobrowsky_smart_glasses_entity_targeting_aug11.py",
        "test_google_news_ai_prisoner_dilemma_aug11.py",
    ]

    def test_all_aug11_test_files_exist(self):
        for tf in self.AUG11_TEST_FILES:
            path = TESTS_DIR / tf
            self.assertTrue(
                path.exists(),
                f"Test file missing: {tf}"
            )


class TestMechanismIDSequenceIntegrity(unittest.TestCase):
    """Mechanism IDs should be unique and monotonically assigned."""

    def test_no_duplicate_ids(self):
        data = load_yaml("competitor-coverage-research.yaml")
        cpf = data.get("cross_publication_findings", {})
        ids = []
        for key, val in cpf.items():
            if isinstance(val, dict) and "mechanism_id" in val:
                ids.append(val["mechanism_id"])
        dupes = [k for k, v in Counter(ids).items() if v > 1]
        self.assertEqual(dupes, [], f"Duplicate mechanism IDs: {dupes}")

    def test_recent_mechanisms_contiguous(self):
        """Mechanisms 42-50 (Aug 11 batch) should have no gaps."""
        data = load_yaml("competitor-coverage-research.yaml")
        cpf = data.get("cross_publication_findings", {})
        ids = set()
        for key, val in cpf.items():
            if isinstance(val, dict) and "mechanism_id" in val:
                mid = val["mechanism_id"]
                if mid >= 42:
                    ids.add(mid)
        expected = set(range(42, 51))
        missing = expected - ids
        self.assertEqual(
            missing, set(),
            f"Missing recent mechanism IDs: {sorted(missing)}"
        )
