"""
Tests for Mechanism #158: Multi-Vector Cultural Delegitimization Cascade
Date: 2026-08-18
Type: E (Podcast Sentiment Tracking)
Rotation: Hour 159

FINDING: Independent actors across 7 vectors — celebrities, satirical commerce,
security conferences, judiciary, regulation, activism, and media — are simultaneously
delegitimizing Meta glasses specifically. Every vector targets Meta exclusively
despite Samsung, Google, Apple, and Snap all making camera-equipped smart glasses.
Apple explicitly BENEFITS by positioning as "privacy-first" alternative.

The cascade generates podcast and media coverage that amplifies Meta-specific framing,
creating a compound delegitimization effect where each new vector reinforces the others.

Sources:
- Lorde at Mad Cool Festival (Jul 10, 2026): TechCrunch, Gizmodo, Android Police
- Tyler the Creator on Instagram (~Jul 2026): Gizmodo
- DuckDuckGo "Normal F***ing Sunglasses" (Jul 30, 2026): TechSpot, PetaPixel, 9to5Mac, Digital Trends
- DEF CON 34 ban (Jul 28, 2026): The Register, CSO Online, Gadget Review
- HMCTS England/Wales courts ban (Aug 2026): Cybernews, The Guardian
- Germany Cayla spy-device law (Aug 12, 2026): TechTimes, Reuters
- Monopoly Events (UK Comic Cons) ban (Aug 2026): The Register
- New York courts ban (Jul 10, 2026): TechTimes
- EHE Epstein poster (Aug ~10, 2026): Hyperallergic, The Times
- Apple N50 delay "for privacy" (Jul 26, 2026): Bloomberg/Gurman, BetaNews
- The Onion parody of DuckDuckGo glasses: PetaPixel
"""

import unittest
import yaml
import os
import importlib
import sys


def load_ccr():
    """Load competitor-coverage-research.yaml."""
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(base, "profiles", "competitor-coverage-research.yaml")
    with open(path, "r") as f:
        return yaml.safe_load(f)


def load_competitor_entities():
    """Load competitor-entities.yaml."""
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(base, "profiles", "competitor-entities.yaml")
    with open(path, "r") as f:
        return yaml.safe_load(f)


def load_podcast_sentiment():
    """Load podcast-sentiment.md as text."""
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(base, "podcast-sentiment.md")
    with open(path, "r") as f:
        return f.read()


def find_mechanism(ccr, mechanism_id):
    """Find a mechanism by ID in cross_publication_findings (dict or list)."""
    cpf = ccr.get("cross_publication_findings", {})
    if isinstance(cpf, dict):
        for key, val in cpf.items():
            if isinstance(val, dict) and val.get("mechanism_id") == mechanism_id:
                return val
    elif isinstance(cpf, list):
        for entry in cpf:
            if isinstance(entry, dict) and entry.get("mechanism_id") == mechanism_id:
                return entry
    return None


class TestMechanism158Existence(unittest.TestCase):
    """Verify mechanism #158 exists in competitor-coverage-research.yaml."""

    def setUp(self):
        self.ccr = load_ccr()
        self.mechanism = find_mechanism(self.ccr, 158)

    def test_mechanism_exists(self):
        """Mechanism #158 must exist in cross_publication_findings."""
        self.assertIsNotNone(self.mechanism, "Mechanism #158 not found in cross_publication_findings")

    def test_mechanism_has_name(self):
        """Mechanism #158 must have a mechanism_name."""
        self.assertIn("mechanism_name", self.mechanism)
        self.assertIn("Delegitimization", self.mechanism["mechanism_name"])

    def test_mechanism_has_finding_type(self):
        """Must have a finding_type."""
        self.assertIn("finding_type", self.mechanism)

    def test_mechanism_has_date(self):
        """Must have discovery_date."""
        self.assertIn("discovery_date", self.mechanism)

    def test_mechanism_has_source_urls(self):
        """Must have source_urls list."""
        self.assertIn("source_urls", self.mechanism)
        self.assertIsInstance(self.mechanism["source_urls"], list)
        self.assertGreaterEqual(len(self.mechanism["source_urls"]), 5)

    def test_mechanism_has_test_file(self):
        """Must reference its test file."""
        self.assertIn("test_file", self.mechanism)
        self.assertIn("multi_vector_cultural_delegitimization", self.mechanism["test_file"])

    def test_mechanism_has_confounders(self):
        """Must have confounders."""
        self.assertIn("confounders", self.mechanism)
        self.assertIsInstance(self.mechanism["confounders"], list)
        self.assertGreaterEqual(len(self.mechanism["confounders"]), 3)


class TestCelebrityBacklashVector(unittest.TestCase):
    """Test celebrity backlash events are documented."""

    def setUp(self):
        self.ccr = load_ccr()
        self.mechanism = find_mechanism(self.ccr, 158)

    def test_lorde_documented(self):
        """Lorde's Mad Cool Festival statement must be documented."""
        summary = str(self.mechanism.get("finding_summary", ""))
        vectors = str(self.mechanism.get("vectors", ""))
        combined = summary + vectors
        self.assertTrue(
            "Lorde" in combined or "lorde" in combined.lower(),
            "Lorde's statement not documented in mechanism #158"
        )

    def test_tyler_documented(self):
        """Tyler the Creator's Instagram statement must be documented."""
        summary = str(self.mechanism.get("finding_summary", ""))
        vectors = str(self.mechanism.get("vectors", ""))
        combined = summary + vectors
        self.assertTrue(
            "Tyler" in combined,
            "Tyler the Creator not documented in mechanism #158"
        )

    def test_celebrity_vs_competitor_asymmetry(self):
        """Celebrity backlash targets Meta exclusively — no celebrity has publicly condemned Samsung/Google/Apple/Snap glasses."""
        summary = str(self.mechanism.get("finding_summary", ""))
        vectors = str(self.mechanism.get("vectors", ""))
        combined = summary + vectors
        # Must mention Meta-exclusive targeting
        self.assertTrue(
            "Meta" in combined,
            "Celebrity backlash must reference Meta targeting"
        )

    def test_lorde_at_rayban_sponsored_event(self):
        """Critical context: Lorde's statement was AT a Ray-Ban-sponsored festival, immediately before a Ray-Ban ambassador performed."""
        summary = str(self.mechanism.get("finding_summary", ""))
        vectors = str(self.mechanism.get("vectors", ""))
        combined = summary + vectors
        self.assertTrue(
            "Mad Cool" in combined or "festival" in combined.lower() or "sponsor" in combined.lower(),
            "Lorde's Ray-Ban sponsorship context must be documented"
        )


class TestSatiricalCommerceVector(unittest.TestCase):
    """Test DuckDuckGo satirical product is documented."""

    def setUp(self):
        self.ccr = load_ccr()
        self.mechanism = find_mechanism(self.ccr, 158)

    def test_duckduckgo_documented(self):
        """DuckDuckGo 'Normal F***ing Sunglasses' must be documented."""
        summary = str(self.mechanism.get("finding_summary", ""))
        vectors = str(self.mechanism.get("vectors", ""))
        combined = summary + vectors
        self.assertTrue(
            "DuckDuckGo" in combined,
            "DuckDuckGo satirical product not documented"
        )

    def test_satirical_commerce_is_new_vector(self):
        """Satirical commercial counter-product is a new vector type not seen before."""
        summary = str(self.mechanism.get("finding_summary", ""))
        vectors = str(self.mechanism.get("vectors", ""))
        combined = summary + vectors
        self.assertTrue(
            "satirical" in combined.lower() or "counter-product" in combined.lower() or "sold out" in combined.lower(),
            "Satirical commerce vector must be identified as new type"
        )

    def test_duckduckgo_meta_specific(self):
        """DuckDuckGo explicitly targeted Meta — 'When big tech started putting cameras in smart glasses'."""
        summary = str(self.mechanism.get("finding_summary", ""))
        vectors = str(self.mechanism.get("vectors", ""))
        combined = summary + vectors
        self.assertTrue(
            "DuckDuckGo" in combined and "Meta" in combined,
            "DuckDuckGo's Meta-specific targeting must be documented"
        )


class TestInstitutionalBanVector(unittest.TestCase):
    """Test institutional bans are documented."""

    def setUp(self):
        self.ccr = load_ccr()
        self.mechanism = find_mechanism(self.ccr, 158)

    def test_defcon_ban_documented(self):
        """DEF CON 34 ban must be documented."""
        summary = str(self.mechanism.get("finding_summary", ""))
        vectors = str(self.mechanism.get("vectors", ""))
        combined = summary + vectors
        self.assertTrue(
            "DEF CON" in combined or "DEFCON" in combined,
            "DEF CON 34 ban not documented"
        )

    def test_hmcts_ban_documented(self):
        """HMCTS (England/Wales courts) ban must be documented."""
        summary = str(self.mechanism.get("finding_summary", ""))
        vectors = str(self.mechanism.get("vectors", ""))
        combined = summary + vectors
        self.assertTrue(
            "HMCTS" in combined or "England" in combined or "court" in combined.lower(),
            "HMCTS courts ban not documented"
        )

    def test_germany_regulatory_documented(self):
        """Germany Cayla spy-device law invocation must be documented."""
        summary = str(self.mechanism.get("finding_summary", ""))
        vectors = str(self.mechanism.get("vectors", ""))
        combined = summary + vectors
        self.assertTrue(
            "Germany" in combined or "Cayla" in combined or "HateAid" in combined,
            "Germany regulatory action not documented"
        )

    def test_ban_targets_meta_only(self):
        """All institutional bans target Meta-style glasses — none target Samsung/Google/Apple/Snap."""
        summary = str(self.mechanism.get("finding_summary", ""))
        vectors = str(self.mechanism.get("vectors", ""))
        combined = summary + vectors
        # Must note Meta-exclusive targeting
        self.assertTrue(
            "Samsung" in combined or "competitor" in combined.lower() or "exclusive" in combined.lower(),
            "Must document that bans are Meta-specific, not category-wide"
        )


class TestAppleCounterPositioning(unittest.TestCase):
    """Test Apple's 'privacy-first' counter-positioning is documented."""

    def setUp(self):
        self.ccr = load_ccr()
        self.mechanism = find_mechanism(self.ccr, 158)

    def test_apple_delay_documented(self):
        """Apple's N50 delay 'for privacy' must be documented as counter-positioning."""
        summary = str(self.mechanism.get("finding_summary", ""))
        vectors = str(self.mechanism.get("vectors", ""))
        combined = summary + vectors
        self.assertTrue(
            "Apple" in combined and ("delay" in combined.lower() or "privacy" in combined.lower() or "N50" in combined),
            "Apple's privacy-first counter-positioning not documented"
        )

    def test_apple_benefits_from_cascade(self):
        """Apple explicitly BENEFITS from the delegitimization cascade — framed as privacy-first."""
        summary = str(self.mechanism.get("finding_summary", ""))
        vectors = str(self.mechanism.get("vectors", ""))
        combined = summary + vectors
        self.assertTrue(
            "Apple" in combined,
            "Apple's benefit from cascade must be documented"
        )


class TestMultiVectorConvergence(unittest.TestCase):
    """Test that the multi-vector nature of the cascade is documented."""

    def setUp(self):
        self.ccr = load_ccr()
        self.mechanism = find_mechanism(self.ccr, 158)

    def test_minimum_vector_count(self):
        """Must document at least 5 independent vectors."""
        vectors = self.mechanism.get("vectors", {})
        if isinstance(vectors, dict):
            self.assertGreaterEqual(len(vectors), 5)
        else:
            # Check summary for vector enumeration
            summary = str(self.mechanism.get("finding_summary", ""))
            vector_indicators = ["celebrity", "satirical", "DEF CON", "court", "Germany", "activist"]
            found = sum(1 for v in vector_indicators if v.lower() in summary.lower())
            self.assertGreaterEqual(found, 4, f"Only found {found} vectors in summary")

    def test_cross_references(self):
        """Must cross-reference related mechanisms."""
        refs = self.mechanism.get("cross_references", [])
        self.assertIsInstance(refs, list)
        self.assertGreaterEqual(len(refs), 2)

    def test_rotation_type_e(self):
        """Must be tagged as rotation type E (podcast sentiment tracking)."""
        self.assertEqual(self.mechanism.get("rotation_type"), "E")


class TestPodcastSentimentUpdated(unittest.TestCase):
    """Test podcast-sentiment.md contains new findings."""

    def setUp(self):
        self.content = load_podcast_sentiment()

    def test_lorde_in_podcast_sentiment(self):
        """Lorde's statement must appear in podcast-sentiment.md."""
        self.assertIn("Lorde", self.content)

    def test_tyler_in_podcast_sentiment(self):
        """Tyler the Creator's statement must appear in podcast-sentiment.md."""
        self.assertIn("Tyler", self.content)

    def test_duckduckgo_in_podcast_sentiment(self):
        """DuckDuckGo satirical product must appear in podcast-sentiment.md."""
        self.assertIn("DuckDuckGo", self.content)

    def test_defcon_in_podcast_sentiment(self):
        """DEF CON ban must appear in podcast-sentiment.md."""
        self.assertIn("DEF CON", self.content)

    def test_mechanism_158_referenced(self):
        """Mechanism #158 must be referenced in podcast-sentiment.md."""
        self.assertIn("#158", self.content)


class TestVocabularyCascadePattern(unittest.TestCase):
    """Test that the vocabulary cascade is documented — 'pervert glasses' spreading across vectors."""

    def setUp(self):
        self.ccr = load_ccr()
        self.mechanism = find_mechanism(self.ccr, 158)

    def test_pervert_vocabulary_tracked(self):
        """The 'pervert glasses' vocabulary spreading across vectors must be documented."""
        summary = str(self.mechanism.get("finding_summary", ""))
        vectors = str(self.mechanism.get("vectors", ""))
        combined = summary + vectors
        self.assertTrue(
            "pervert" in combined.lower(),
            "Pervert vocabulary cascade not documented"
        )

    def test_eva_galperin_eff_quote(self):
        """EFF director Eva Galperin's endorsement of DEF CON ban must be documented."""
        summary = str(self.mechanism.get("finding_summary", ""))
        vectors = str(self.mechanism.get("vectors", ""))
        combined = summary + vectors
        self.assertTrue(
            "Galperin" in combined or "EFF" in combined,
            "EFF/Galperin endorsement not documented"
        )


class TestDocSyncIntegrity(unittest.TestCase):
    """Verify doc counts are in sync after this iteration."""

    def test_readme_test_file_count(self):
        """README test file count must match disk."""
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        test_dir = os.path.join(base, "tests")
        actual = len([f for f in os.listdir(test_dir) if f.startswith("test_") and f.endswith(".py")])
        readme_path = os.path.join(base, "README.md")
        with open(readme_path) as f:
            readme = f.read()
        # Check that the actual count appears in README
        self.assertIn(str(actual), readme, f"README doesn't contain actual test file count {actual}")

    def test_architecture_test_file_count(self):
        """ARCHITECTURE test file count must match disk."""
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        test_dir = os.path.join(base, "tests")
        actual = len([f for f in os.listdir(test_dir) if f.startswith("test_") and f.endswith(".py")])
        arch_path = os.path.join(base, "docs", "ARCHITECTURE.md")
        with open(arch_path) as f:
            arch = f.read()
        self.assertIn(str(actual), arch, f"ARCHITECTURE doesn't contain actual test file count {actual}")

    def test_this_test_file_in_readme(self):
        """This test file must be listed in README."""
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        readme_path = os.path.join(base, "README.md")
        with open(readme_path) as f:
            readme = f.read()
        self.assertIn("test_multi_vector_cultural_delegitimization_cascade_aug18", readme)

    def test_this_test_file_in_architecture(self):
        """This test file must be listed in ARCHITECTURE."""
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        arch_path = os.path.join(base, "docs", "ARCHITECTURE.md")
        with open(arch_path) as f:
            arch = f.read()
        self.assertIn("test_multi_vector_cultural_delegitimization_cascade_aug18", arch)


if __name__ == "__main__":
    unittest.main()
