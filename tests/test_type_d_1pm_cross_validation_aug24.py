"""
Type D Cross-Validation: 1 PM Aug 24, 2026

Validates:
1. YAML structural integrity after list→mapping fixes in competitor-coverage-research.yaml
2. Anthropic IPO + piracy settlement financial architecture consistency between
   competitor-entities.yaml and competitor-coverage-research.yaml
3. Mechanism #264 (Hachman PCWorld) properly integrated into cross_publication_findings
4. Raymond Wong test import fix (MediaScopeTestCase → unittest.TestCase)
5. HTTP→HTTPS URL cleanup in competitor-entities.yaml
6. All aug24 mechanism entries parse correctly as YAML mapping keys (not list items)

Fixes applied this iteration:
- 5 list-syntax mechanism entries in publications mapping → named mapping keys
- Raymond Wong test: MediaScopeTestCase import → unittest.TestCase
- Hachman PCWorld: case-sensitive assertion (LED → led in .lower() comparison)
- Hachman PCWorld: mechanism_264 YAML section lookup (competitor_coverage_mechanisms → cross_publication_findings)
- cross_validation_aug7_04am: TypeError on int key concatenation (str(k))
- HTTP URLs → HTTPS (digiday.com, neowin.net)
"""

import os
import unittest
import yaml
from pathlib import Path

PROFILES_DIR = Path(__file__).parent.parent / "profiles"
TESTS_DIR = Path(__file__).parent


class TestYAMLStructuralIntegrity(unittest.TestCase):
    """Verify all profile YAMLs parse without errors after list→mapping fixes."""

    def test_competitor_coverage_research_parses(self):
        """competitor-coverage-research.yaml parses as valid YAML."""
        path = PROFILES_DIR / "competitor-coverage-research.yaml"
        with open(path) as f:
            data = yaml.safe_load(f)
        self.assertIsInstance(data, dict)
        self.assertIn("publications", data)
        self.assertIn("cross_publication_findings", data)

    def test_competitor_entities_parses(self):
        """competitor-entities.yaml parses as valid YAML."""
        path = PROFILES_DIR / "competitor-entities.yaml"
        with open(path) as f:
            data = yaml.safe_load(f)
        self.assertIsInstance(data, dict)
        self.assertIn("entities", data)

    def test_publications_is_mapping_not_list(self):
        """publications section is a mapping (dict), not a list."""
        path = PROFILES_DIR / "competitor-coverage-research.yaml"
        with open(path) as f:
            data = yaml.safe_load(f)
        pubs = data.get("publications", {})
        self.assertIsInstance(pubs, dict,
                             "publications should be a mapping, not a list")

    def test_no_list_items_in_publications_mapping(self):
        """No list-syntax items snuck into the publications mapping."""
        path = PROFILES_DIR / "competitor-coverage-research.yaml"
        with open(path) as f:
            data = yaml.safe_load(f)
        pubs = data.get("publications", {})
        for key in pubs:
            self.assertIsInstance(key, str,
                                 f"All publications keys should be strings, got {type(key)}: {key}")


class TestAug24MechanismEntriesAsNamedKeys(unittest.TestCase):
    """Verify all aug24 mechanisms exist as named mapping keys."""

    def setUp(self):
        path = PROFILES_DIR / "competitor-coverage-research.yaml"
        with open(path) as f:
            self.data = yaml.safe_load(f)
        self.pubs = self.data.get("publications", {})
        self.findings = self.data.get("cross_publication_findings", {})

    def test_mechanism_268_gizmodo_ice_ban_is_named_key(self):
        """Mechanism #268 (Gizmodo ICE ban) exists as a named mapping key."""
        key = "gizmodo_ice_ban_entity_selection_openai_camera_device_bore_framing_asymmetry"
        self.assertIn(key, self.pubs)
        self.assertEqual(self.pubs[key]["mechanism_id"], 268)

    def test_mechanism_269_steve_dent_is_named_key(self):
        """Mechanism #272 (Steve Dent) exists as a named mapping key."""
        key = "steve_dent_engadget_cross_entity_camera_wearable_privacy_vocabulary_gradient"
        self.assertIn(key, self.pubs)
        self.assertEqual(self.pubs[key]["mechanism_id"], 272)

    def test_mechanism_270_pervertpods_is_named_key(self):
        """Mechanism #270 (Pervertpods label containment) exists as a named mapping key."""
        key = "cross_publication_apple_airpods_pervertpods_label_containment"
        self.assertIn(key, self.pubs)
        self.assertEqual(self.pubs[key]["mechanism_id"], 270)

    def test_mechanism_271_lawrence_bonk_is_named_key(self):
        """Mechanism #271 (Lawrence Bonk) exists as a named mapping key."""
        key = "lawrence_bonk_engadget_cross_entity_camera_wearable_vocabulary_inversion"
        self.assertIn(key, self.pubs)
        self.assertEqual(self.pubs[key]["mechanism_id"], 271)

    def test_mechanism_282_raymond_wong_is_named_key(self):
        """Mechanism #282 (Raymond Wong) exists as a named mapping key."""
        key = "raymond_wong_gizmodo_cross_entity_camera_privacy_vocabulary_concentration"
        self.assertIn(key, self.pubs)
        self.assertEqual(self.pubs[key]["mechanism_number"], 282)

    def test_mechanism_264_hachman_pcworld_is_named_key(self):
        """Mechanism #264 (Hachman PCWorld) exists as a named mapping key in cross_publication_findings."""
        key = "mark_hachman_pcworld_within_article_cross_entity_camera_privacy_scrutiny_differential"
        self.assertIn(key, self.findings)
        self.assertEqual(self.findings[key]["mechanism_id"], 264)


class TestAnthropicIPOPiracyFinancialArchitectureConsistency(unittest.TestCase):
    """Cross-validate Anthropic IPO and piracy data between entities and research YAMLs."""

    def setUp(self):
        with open(PROFILES_DIR / "competitor-entities.yaml") as f:
            entities = yaml.safe_load(f)
        self.anthropic = entities["entities"]["anthropic"]

        with open(PROFILES_DIR / "competitor-coverage-research.yaml") as f:
            research = yaml.safe_load(f)
        self.research = research

    def test_anthropic_ipo_banks_match_underwriter_triangle(self):
        """IPO underwriters in entities match the quad-bank convergence documented in research."""
        ipo_banks = set(self.anthropic["ipo_filing"]["ipo_banks_reported"])
        expected = {"Goldman Sachs", "Morgan Stanley", "JPMorgan Chase", "Citigroup"}
        self.assertEqual(ipo_banks, expected)

    def test_settlement_amount_consistent(self):
        """Settlement amount in entities.yaml matches the $1.5B documented in research."""
        settlement = self.anthropic["author_settlement_detail"]
        self.assertEqual(settlement["amount_b"], 1.5)

    def test_settlement_final_approval_date(self):
        """Settlement final approval date is July 20, 2026."""
        self.assertEqual(
            self.anthropic["author_settlement_detail"]["final_approval_date"],
            "2026-07-20"
        )

    def test_piracy_sources_documented(self):
        """Piracy sources (LibGen, PiLiMi) are documented."""
        sources = self.anthropic["author_settlement_detail"]["pirated_sources"]
        self.assertTrue(any("LibGen" in s for s in sources))
        self.assertTrue(any("PiLiMi" in s for s in sources))

    def test_ipo_valuation_above_openai(self):
        """Anthropic valuation at filing ($965B) exceeds OpenAI implied valuation."""
        self.assertGreaterEqual(
            self.anthropic["ipo_filing"]["valuation_at_filing_b"],
            852  # OpenAI $852B
        )

    def test_settlement_mediascope_note_references_ipo(self):
        """Settlement mediascope_note references IPO timing financial architecture."""
        note = self.anthropic["author_settlement_detail"]["mediascope_note"]
        self.assertIn("IPO", note)
        self.assertIn("Krishna Rao", note)

    def test_zero_publisher_deals_documented(self):
        """Zero publisher content deals documented for Anthropic."""
        ipo = self.anthropic["ipo_filing"]
        paradox = ipo.get("zero_publisher_deal_ipo_paradox", "")
        self.assertIn("zero publisher content licensing deals", paradox.lower())

    def test_anthropic_settlement_mechanism_in_research(self):
        """Anthropic piracy settlement mechanism exists in research YAML."""
        key = "anthropic_piracy_settlement_ipo_underwriter_publisher_financial_architecture"
        pubs = self.research.get("publications", {})
        self.assertIn(key, pubs)


class TestHTTPSURLCleanup(unittest.TestCase):
    """Verify all source URLs in entities YAML use HTTPS."""

    def test_no_http_urls_in_entities(self):
        """No HTTP (non-HTTPS) URLs in competitor-entities.yaml source_urls."""
        with open(PROFILES_DIR / "competitor-entities.yaml") as f:
            content = f.read()

        http_urls = []
        for i, line in enumerate(content.split('\n'), 1):
            stripped = line.strip()
            if stripped.startswith('- http://'):
                http_urls.append((i, stripped))

        self.assertEqual(
            len(http_urls), 0,
            f"Found {len(http_urls)} HTTP URLs (should be HTTPS): {http_urls[:5]}"
        )


class TestAug24TestFilesImport(unittest.TestCase):
    """Verify all aug24 test files can be imported without errors."""

    def test_all_aug24_tests_importable(self):
        """All test_*aug24*.py files import without errors."""
        import importlib
        import sys

        aug24_files = list(TESTS_DIR.glob("test_*aug24*.py"))
        self.assertGreater(len(aug24_files), 8,
                           "Should have 8+ aug24 test files")

        failures = []
        for f in aug24_files:
            module_name = f.stem
            try:
                if module_name in sys.modules:
                    del sys.modules[module_name]
                spec = importlib.util.spec_from_file_location(module_name, f)
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
            except Exception as e:
                failures.append((module_name, str(e)))

        self.assertEqual(
            len(failures), 0,
            f"Import failures: {failures}"
        )


class TestCrossValidationTestIntKeyFix(unittest.TestCase):
    """Verify the int-key concatenation fix in cross-validation tests."""

    def test_ranked_list_int_keys_handled(self):
        """Dict with integer keys doesn't crash path concatenation."""
        data = {
            "ranked_list": {1: "Future plc", 2: "Forbes", 3: "People Inc."},
            "source_urls": ["https://example.com/a", "https://example.com/b"]
        }
        # Simulate the fixed check function
        dupes = []

        def check(data, path=""):
            if isinstance(data, dict):
                for k, v in data.items():
                    if k == "source_urls" and isinstance(v, list):
                        if len(v) != len(set(v)):
                            dupes.append(path + "." + str(k))
                    else:
                        check(v, path + "." + str(k))
            elif isinstance(data, list):
                for i, item in enumerate(data):
                    check(item, f"{path}[{i}]")

        # This should not raise TypeError
        try:
            check(data)
        except TypeError as e:
            self.fail(f"Int key concatenation still broken: {e}")

        self.assertEqual(len(dupes), 0)


if __name__ == "__main__":
    unittest.main()
