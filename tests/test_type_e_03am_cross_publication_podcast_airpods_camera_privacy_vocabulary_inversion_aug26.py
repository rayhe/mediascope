"""
MediaScope Type E Podcast Sentiment Analysis — Mechanism #316:
Cross-Publication Podcast AirPods Camera Privacy Vocabulary Inversion:
9to5Mac Overtime 078 + AppleInsider Podcast Same-Day Entity-Selective Framing

On Aug 21, 2026, two independent Apple-ecosystem podcasts covered the same
technological event (Apple AirPods camera leak) with identical entity-selective
vocabulary bifurcation:

9to5Mac Overtime 078 (Jeff Benjamin & Fernando Silva):
  Apple: "pretty big deal," "privacy-centric," "alternative"
  Meta: "often-criticized," "controversial"

AppleInsider Podcast (Wesley Hilliard & William Gallagher):
  Apple: "praise," "won't take photos at all," "not fear them"
  Meta: "creepy actions," "perpetrated"

KEY FINDING: "Perpetrated" is criminal-legal register — you don't "perpetrate"
with a camera, you "perpetrate" crimes. This implicitly criminalizes normal
Meta glasses use. AppleInsider applies this vocabulary while simultaneously
pivoting to reassurance for Apple's identical technology.

CROSS-MEDIUM PIPELINE: This is the FOURTH 9to5Mac channel to cover the AirPods
leak in 72 hours (extending mechanism #250):
  1. Security Bite print (Aug 18, Waichulis)
  2. Happy Hour #604 podcast (Aug 20, Mayo + Miller)
  3. 9to5Mac Daily podcast (Aug 21, Miller)
  4. Overtime #078 podcast (Aug 21, Benjamin + Silva) ← NEW

Plus AppleInsider as a cross-publication comparison point.

Financial Architecture:
  9to5Mac: 100% Apple affiliate revenue, Google Preferred Source, zero Meta
  AppleInsider: 100% Apple affiliate revenue, Apple Podcasts+, zero Meta

CONFOUNDERS (4):
1. STRONG: AirPods cameras are 1MP AI-only (non-recording) vs Meta 12MP photo/video
2. STRONG: AirPods pre-release, no documented misuse incidents
3. MODERATE: Both publications are Apple-focused by design
4. MODERATE: Different form factor (earbuds vs glasses)
"""

import unittest
import yaml
import os


def load_competitor_coverage():
    """Load competitor-coverage-research.yaml."""
    path = os.path.join(
        os.path.dirname(__file__), "..", "profiles", "competitor-coverage-research.yaml"
    )
    with open(path) as f:
        return yaml.safe_load(f)


def find_mechanism(data, mechanism_id):
    """Search across all sections for a mechanism by ID."""
    sections = ["publications", "cross_publication_findings", "aggregate_findings", "cross_entity_leverage"]
    for section_name in sections:
        section = data.get(section_name, {})
        if isinstance(section, dict):
            for key, value in section.items():
                if isinstance(value, dict):
                    mid = value.get("mechanism_id") or value.get("mechanism_number")
                    if mid == mechanism_id:
                        return value
                    # Check nested mechanisms lists
                    for sub_key in ["mechanisms", "findings"]:
                        nested = value.get(sub_key, [])
                        if isinstance(nested, list):
                            for item in nested:
                                if isinstance(item, dict):
                                    nmid = item.get("mechanism_id") or item.get("mechanism_number")
                                    if nmid == mechanism_id:
                                        return item
        elif isinstance(section, list):
            for item in section:
                if isinstance(item, dict):
                    mid = item.get("mechanism_id") or item.get("mechanism_number")
                    if mid == mechanism_id:
                        return item
    return None


def load_podcast_sentiment():
    """Load podcast-sentiment.md as text."""
    path = os.path.join(
        os.path.dirname(__file__), "..", "podcast-sentiment.md"
    )
    with open(path) as f:
        return f.read()


class TestMechanism316Exists(unittest.TestCase):
    """Verify mechanism #316 exists with correct metadata."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_coverage()
        cls.mech = find_mechanism(cls.data, 316)

    def test_mechanism_316_exists(self):
        """Mechanism #316 must exist in the data model."""
        self.assertIsNotNone(self.mech, "Mechanism #316 not found")

    def test_mechanism_type(self):
        """Type must be cross_medium_privacy_vocabulary_inversion."""
        self.assertEqual(
            self.mech.get("type"),
            "cross_medium_privacy_vocabulary_inversion"
        )

    def test_mechanism_domain(self):
        """Domain must be podcast_sentiment."""
        self.assertEqual(self.mech.get("domain"), "podcast_sentiment")

    def test_mechanism_finding_type(self):
        """Finding type must be cross_publication_podcast_natural_experiment."""
        self.assertEqual(
            self.mech.get("finding_type"),
            "cross_publication_podcast_natural_experiment"
        )


class TestPodcastEpisodeProfiles(unittest.TestCase):
    """Verify both podcast episodes are properly documented."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_coverage()
        cls.mech = find_mechanism(cls.data, 316)
        cls.episodes = cls.mech.get("podcast_episodes", []) if cls.mech else []

    def test_two_episodes_documented(self):
        """Must have exactly 2 podcast episodes."""
        self.assertEqual(len(self.episodes), 2)

    def test_9to5mac_overtime_078(self):
        """9to5Mac Overtime 078 must be present."""
        overtime = [e for e in self.episodes if "Overtime" in e.get("show", "")]
        self.assertTrue(len(overtime) > 0, "9to5Mac Overtime 078 not found")
        self.assertEqual(overtime[0]["episode"], "078")
        self.assertEqual(overtime[0]["date"], "2026-08-21")

    def test_appleinsider_podcast(self):
        """AppleInsider Podcast must be present."""
        ai = [e for e in self.episodes if "AppleInsider" in e.get("show", "")]
        self.assertTrue(len(ai) > 0, "AppleInsider Podcast not found")
        self.assertEqual(ai[0]["date"], "2026-08-21")

    def test_both_same_date(self):
        """Both episodes must be on the same date (natural experiment)."""
        dates = {e["date"] for e in self.episodes}
        self.assertEqual(len(dates), 1, f"Episodes on different dates: {dates}")
        self.assertIn("2026-08-21", dates)


class TestEntityVocabularyBifurcation(unittest.TestCase):
    """Verify entity-selective vocabulary is documented for each episode."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_coverage()
        cls.mech = find_mechanism(cls.data, 316)
        cls.episodes = cls.mech.get("podcast_episodes", []) if cls.mech else []

    def test_overtime_078_apple_positive_vocabulary(self):
        """9to5Mac Overtime 078 must have positive Apple vocabulary."""
        overtime = [e for e in self.episodes if "Overtime" in e.get("show", "")]
        apple_vocab = overtime[0].get("apple_vocabulary", [])
        self.assertTrue(len(apple_vocab) >= 2, "Insufficient Apple vocabulary")
        # Check for key aspirational terms
        combined = " ".join(apple_vocab).lower()
        self.assertIn("privacy-centric", combined)

    def test_overtime_078_meta_negative_vocabulary(self):
        """9to5Mac Overtime 078 must have negative Meta vocabulary."""
        overtime = [e for e in self.episodes if "Overtime" in e.get("show", "")]
        meta_vocab = overtime[0].get("meta_vocabulary", [])
        self.assertTrue(len(meta_vocab) >= 2, "Insufficient Meta vocabulary")
        combined = " ".join(meta_vocab).lower()
        self.assertIn("controversial", combined)

    def test_appleinsider_perpetrated_vocabulary(self):
        """AppleInsider must use 'perpetrated' for Meta — criminal-legal register."""
        ai = [e for e in self.episodes if "AppleInsider" in e.get("show", "")]
        meta_vocab = ai[0].get("meta_vocabulary", [])
        combined = " ".join(meta_vocab).lower()
        self.assertIn("perpetrated", combined)

    def test_appleinsider_apple_reassurance(self):
        """AppleInsider must have reassurance vocabulary for Apple."""
        ai = [e for e in self.episodes if "AppleInsider" in e.get("show", "")]
        apple_vocab = ai[0].get("apple_vocabulary", [])
        combined = " ".join(apple_vocab).lower()
        self.assertIn("praise", combined)


class TestFinancialArchitecture(unittest.TestCase):
    """Verify financial dependency documentation."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_coverage()
        cls.mech = find_mechanism(cls.data, 316)
        cls.fin = cls.mech.get("financial_architecture", []) if cls.mech else []

    def test_two_entities_documented(self):
        """Must document financial architecture for both publications."""
        self.assertEqual(len(self.fin), 2)

    def test_9to5mac_apple_dependency(self):
        """9to5Mac must show 100% Apple dependency."""
        m = [e for e in self.fin if e.get("entity") == "9to5Mac"]
        self.assertTrue(len(m) > 0, "9to5Mac financial entry not found")
        self.assertEqual(str(m[0]["apple_dependency"]), "100%")

    def test_appleinsider_apple_dependency(self):
        """AppleInsider must show 100% Apple dependency."""
        ai = [e for e in self.fin if e.get("entity") == "AppleInsider"]
        self.assertTrue(len(ai) > 0, "AppleInsider financial entry not found")
        self.assertEqual(str(ai[0]["apple_dependency"]), "100%")

    def test_both_zero_meta_relationship(self):
        """Both publications must have zero Meta financial relationship."""
        for entry in self.fin:
            self.assertEqual(
                entry.get("meta_relationship"),
                "none",
                f"{entry.get('entity')} should have no Meta relationship"
            )


class TestVocabularyLists(unittest.TestCase):
    """Verify aggregate vocabulary lists are populated."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_coverage()
        cls.mech = find_mechanism(cls.data, 316)

    def test_meta_alarm_vocabulary_count(self):
        """Must have at least 4 Meta alarm vocabulary terms."""
        vocab = self.mech.get("vocabulary_meta_alarm", [])
        self.assertGreaterEqual(len(vocab), 4)

    def test_apple_aspirational_vocabulary_count(self):
        """Must have at least 5 Apple aspirational vocabulary terms."""
        vocab = self.mech.get("vocabulary_apple_aspirational", [])
        self.assertGreaterEqual(len(vocab), 5)

    def test_perpetrated_in_alarm_list(self):
        """'perpetrated' must be in Meta alarm vocabulary."""
        vocab = self.mech.get("vocabulary_meta_alarm", [])
        self.assertIn("perpetrated", vocab)

    def test_privacy_centric_in_aspirational_list(self):
        """'privacy-centric' must be in Apple aspirational vocabulary."""
        vocab = self.mech.get("vocabulary_apple_aspirational", [])
        self.assertIn("privacy-centric", vocab)


class TestCrossReferences(unittest.TestCase):
    """Verify mechanism extends and cross-references correct predecessors."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_coverage()
        cls.mech = find_mechanism(cls.data, 316)

    def test_extends_mechanism_250(self):
        """Must extend mechanism #250 (9to5Mac three-channel pipeline)."""
        extends = self.mech.get("extends_mechanisms", [])
        self.assertIn(250, extends)

    def test_extends_mechanism_173(self):
        """Must extend mechanism #173 (9to5 network privacy vocabulary gradient)."""
        extends = self.mech.get("extends_mechanisms", [])
        self.assertIn(173, extends)

    def test_extends_mechanism_242(self):
        """Must extend mechanism #242 (pervertpods label containment)."""
        extends = self.mech.get("extends_mechanisms", [])
        self.assertIn(242, extends)


class TestConfounders(unittest.TestCase):
    """Verify confounders are documented with correct strength levels."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_coverage()
        cls.mech = find_mechanism(cls.data, 316)
        cls.confounders = cls.mech.get("confounders", [])

    def test_at_least_four_confounders(self):
        """Must document at least 4 confounders."""
        self.assertGreaterEqual(len(self.confounders), 4)

    def test_has_strong_confounders(self):
        """Must have at least 2 STRONG confounders."""
        strong = [c for c in self.confounders if c.get("strength") == "STRONG"]
        self.assertGreaterEqual(len(strong), 2)

    def test_has_moderate_confounders(self):
        """Must have at least 2 MODERATE confounders."""
        moderate = [c for c in self.confounders if c.get("strength") == "MODERATE"]
        self.assertGreaterEqual(len(moderate), 2)


class TestPodcastSentimentMd(unittest.TestCase):
    """Verify podcast-sentiment.md has been updated with the new episodes."""

    @classmethod
    def setUpClass(cls):
        cls.text = load_podcast_sentiment()

    def test_overtime_078_in_podcast_sentiment(self):
        """9to5Mac Overtime 078 must appear in podcast-sentiment.md."""
        self.assertIn("Overtime Ep078", self.text)
        self.assertIn("AirPods with cameras, a pretty big deal", self.text)

    def test_appleinsider_podcast_in_podcast_sentiment(self):
        """AppleInsider Podcast Aug 21 must appear in podcast-sentiment.md."""
        self.assertIn("AppleInsider Podcast", self.text)
        self.assertIn("perpetrated", self.text)

    def test_cross_publication_comparison_table(self):
        """Cross-publication comparison must exist in podcast-sentiment.md."""
        self.assertIn("Cross-Publication Podcast Comparison", self.text)

    def test_natural_experiment_framing(self):
        """Natural experiment framing must be described."""
        self.assertIn("Natural Experiment", self.text)


class TestSourceURLIntegrity(unittest.TestCase):
    """Verify all source URLs are documented."""

    @classmethod
    def setUpClass(cls):
        cls.data = load_competitor_coverage()
        cls.mech = find_mechanism(cls.data, 316)
        cls.sources = cls.mech.get("sources", [])

    def test_has_at_least_three_sources(self):
        """Must have at least 3 source URLs."""
        self.assertGreaterEqual(len(self.sources), 3)

    def test_9to5mac_overtime_url(self):
        """Must include 9to5Mac Overtime 078 URL."""
        urls = [s["url"] for s in self.sources]
        self.assertTrue(
            any("overtime-078" in u for u in urls),
            "9to5Mac Overtime 078 URL not found"
        )

    def test_appleinsider_url(self):
        """Must include AppleInsider podcast URL."""
        urls = [s["url"] for s in self.sources]
        self.assertTrue(
            any("appleinsider.com" in u for u in urls),
            "AppleInsider URL not found"
        )


if __name__ == "__main__":
    unittest.main()
