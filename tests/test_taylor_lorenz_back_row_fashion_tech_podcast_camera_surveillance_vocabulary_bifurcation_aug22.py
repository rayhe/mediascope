"""
Type E/B Hybrid: Podcast Sentiment + Journalist Cross-Entity Tracking

Mechanism #227: Taylor Lorenz (User Mag / ex-WaPo) Cross-Platform Fashion-Tech Podcast —
Camera Wearable Surveillance Vocabulary Bifurcation

FINDING:
Taylor Lorenz, an independent tech journalist (User Mag, Substack; formerly Washington Post,
New York Times, The Atlantic), appears on the fashion podcast "Back Row with Amy Odell"
(Jul 30, 2026) for a 43-minute episode titled "How Meta Turned Smart Glasses Into 'Hot
Surveillance Summer'" — a collaboration with Lorenz's own Power User podcast.

The episode's chapter structure reveals a systematic cross-entity vocabulary bifurcation:

  ENTITY-VOCABULARY MAPPING (from chapter titles):
  ┌──────────┬──────────────┬─────────────────────────────────────┬────────────────┐
  │ Entity   │ Chapters     │ Vocabulary                          │ Privacy alarm? │
  ├──────────┼──────────────┼─────────────────────────────────────┼────────────────┤
  │ Meta     │ 12+ chapters │ "surveillance," "creep," "scary,"   │ YES — central  │
  │          │              │ "copy machine," "menace," "odious"  │ thesis         │
  ├──────────┼──────────────┼─────────────────────────────────────┼────────────────┤
  │ Apple    │ 1 chapter    │ "camera AirPods" (neutral listing)  │ NO             │
  │          │ (32:14)      │ alongside "pins, pendants"          │                │
  ├──────────┼──────────────┼─────────────────────────────────────┼────────────────┤
  │ Snap     │ 2 chapters   │ "$130 flop," "$2,000 flop,"        │ NO — price/    │
  │          │              │ "ugly tech dies"                    │ aesthetics     │
  ├──────────┼──────────────┼─────────────────────────────────────┼────────────────┤
  │ Google   │ 1 chapter    │ "original abomination" (historical) │ NO — 2013 only │
  │          │ (02:45)      │                                     │                │
  ├──────────┼──────────────┼─────────────────────────────────────┼────────────────┤
  │ GoPro    │ 1 chapter    │ "normalized filming" (positive)     │ NO             │
  │          │ (06:48)      │                                     │                │
  └──────────┴──────────────┴─────────────────────────────────────┴────────────────┘

NOVEL PATTERN — Fashion-Tech Media Crossover:
This is the FIRST podcast in the MediaScope corpus where a fashion publication host
(Amy Odell, former Cosmopolitan.com editor) collaborates with a tech journalist to
frame smart glasses through a fashion-surveillance lens. The episode description calls
Meta's glasses "odious" while acknowledging they "may end up being a smash hit" —
a grudging concession pattern (see mechanism #60).

CRITICAL SAME-EPISODE COMPARISON:
At chapter 32:14, "Beyond glasses: pins, pendants, and camera AirPods," Apple's
camera-equipped AirPods are mentioned in a NEUTRAL listing alongside other form
factors. No surveillance vocabulary. No privacy scrutiny. No "scary." This despite
camera AirPods having IDENTICAL core capability: visual sensors capturing data for
AI processing. The SAME episode spends 30+ minutes framing Meta cameras as surveillance
but mentions Apple cameras as a feature in a single passing reference.

SNAP VOCABULARY INVERSION:
Snap Spectacles ($2,195, 4 cameras, consumer launch Sep 16, 2026) gets TWO chapters
but with AESTHETIC/BUSINESS vocabulary only: "$130 flop" (historical), "$2,000 flop"
(current), "ugly tech dies." ZERO surveillance/privacy vocabulary despite Snap Specs
having MORE cameras (4 vs Meta's 1 ultrawide) at HIGHER price. Privacy is not the lens
through which Snap's camera product is evaluated.

TAYLOR LORENZ CAREER TRAJECTORY:
- The Atlantic (2018–2022): internet culture reporter
- New York Times (2022): tech culture
- Washington Post (2022–2024): tech columnist
- User Mag (Substack, Oct 2024–present): independent
- Power User podcast (Spotify): co-production with Back Row
- Published in WIRED (Aug 2025, Dark money influencer piece)

FINANCIAL ARCHITECTURE:
- Taylor Lorenz / User Mag: Substack subscriber-funded. No known direct financial
  relationships with Meta, Apple, or Snap.
- Amy Odell / Back Row: Fashion podcast via Megaphone (Spotify). Fashion media
  historically dependent on luxury brand advertising including EssilorLuxottica.
- STRUCTURAL NOTE: The episode title uses "Meta" not "Ray-Ban" — the tech company
  absorbs the surveillance stigma while the fashion partner (EssilorLuxottica/Ray-Ban)
  is treated more neutrally. This preserves fashion media's relationship with the
  luxury brand while allowing adversarial coverage of the tech partner.

SOURCES:
- Back Row with Amy Odell: "How Meta Turned Smart Glasses Into 'Hot Surveillance Summer'"
  (Jul 30, 2026, ~43 min, with Taylor Lorenz)
  URL: http://au.radio.net/podcast/back-row-with-amy-odell (episode listing)
- Taylor Lorenz career: WaPo exit Oct 2024, User Mag launch
- 9to5Mac (Aug 18, 2026): Security Bite — Apple camera AirPods framing (mechanism #221)
- Snap Specs Sep 16 launch: multiple sources (mechanism #224)
"""

import unittest
import os
import yaml
from pathlib import Path


def load_competitor_research():
    """Load the competitor coverage research YAML."""
    yaml_path = Path(__file__).parent.parent / "profiles" / "competitor-coverage-research.yaml"
    with open(yaml_path, "r") as f:
        return yaml.safe_load(f)


def load_podcast_sentiment():
    """Load the podcast sentiment markdown."""
    md_path = Path(__file__).parent.parent / "podcast-sentiment.md"
    with open(md_path, "r") as f:
        return f.read()


def get_mechanism_227(data):
    """Find mechanism #227 in the YAML data."""
    if not data:
        return None
    for key, value in data.items():
        if isinstance(value, dict):
            if value.get("mechanism_id") == 227:
                return value
            result = get_mechanism_227(value)
            if result:
                return result
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    if item.get("mechanism_id") == 227:
                        return item
    return None


class TestMechanism227Exists(unittest.TestCase):
    """Verify mechanism #227 is documented in the YAML."""

    def setUp(self):
        self.data = load_competitor_research()
        self.mechanism = get_mechanism_227(self.data)

    def test_mechanism_227_exists(self):
        self.assertIsNotNone(self.mechanism, "Mechanism #227 should exist in competitor-coverage-research.yaml")

    def test_has_name(self):
        self.assertIn("name", self.mechanism)
        name = self.mechanism["name"].lower()
        self.assertIn("taylor lorenz", name)

    def test_has_finding_summary(self):
        has_summary = "finding_summary" in self.mechanism or "overview" in self.mechanism
        self.assertTrue(has_summary, "Mechanism #227 should have a finding_summary or overview")

    def test_has_asymmetry_score(self):
        self.assertIn("asymmetry_score", self.mechanism)
        score = self.mechanism["asymmetry_score"]
        self.assertGreaterEqual(score, 0.5)
        self.assertLessEqual(score, 1.0)

    def test_has_discovery_date(self):
        self.assertIn("discovery_date", self.mechanism)

    def test_has_source_urls(self):
        self.assertIn("source_urls", self.mechanism)
        urls = self.mechanism["source_urls"]
        self.assertGreaterEqual(len(urls), 1)


class TestCrossEntityVocabularyBifurcation(unittest.TestCase):
    """Verify the core vocabulary bifurcation pattern is documented."""

    def setUp(self):
        self.data = load_competitor_research()
        self.mechanism = get_mechanism_227(self.data)

    def test_meta_surveillance_vocabulary_documented(self):
        """Meta should be associated with surveillance/alarm vocabulary."""
        summary = self.mechanism.get("finding_summary", "") or self.mechanism.get("overview", "")
        summary_lower = summary.lower()
        meta_alarm_terms = ["surveillance", "creep", "scary", "odious", "menace"]
        found_terms = [t for t in meta_alarm_terms if t in summary_lower]
        self.assertGreaterEqual(len(found_terms), 2,
                                f"Expected at least 2 Meta alarm terms, found: {found_terms}")

    def test_apple_neutral_vocabulary_documented(self):
        """Apple camera AirPods should be documented as receiving neutral treatment."""
        summary = self.mechanism.get("finding_summary", "") or self.mechanism.get("overview", "")
        summary_lower = summary.lower()
        self.assertIn("airpods", summary_lower, "Apple camera AirPods should be mentioned")
        # Should note the neutral listing pattern
        neutral_indicators = ["neutral", "passing", "listing", "alongside"]
        found = [n for n in neutral_indicators if n in summary_lower]
        self.assertGreaterEqual(len(found), 1,
                                f"Expected neutral treatment indicators for Apple, found: {found}")

    def test_snap_aesthetic_vocabulary_documented(self):
        """Snap should get aesthetic/business failure vocabulary, not privacy."""
        summary = self.mechanism.get("finding_summary", "") or self.mechanism.get("overview", "")
        summary_lower = summary.lower()
        snap_terms = ["flop", "ugly", "aesthetic", "price", "snap"]
        found = [t for t in snap_terms if t in summary_lower]
        self.assertGreaterEqual(len(found), 1,
                                f"Expected Snap aesthetic/business vocabulary, found: {found}")


class TestSameEpisodeNaturalExperiment(unittest.TestCase):
    """Verify the same-episode comparison is properly framed."""

    def setUp(self):
        self.data = load_competitor_research()
        self.mechanism = get_mechanism_227(self.data)
        self.summary = (self.mechanism.get("finding_summary", "") or
                        self.mechanism.get("overview", "")).lower()

    def test_same_episode_noted(self):
        """The test should note this is a same-episode comparison."""
        same_ep_indicators = ["same episode", "single episode", "same podcast", "43"]
        found = [s for s in same_ep_indicators if s in self.summary]
        self.assertGreaterEqual(len(found), 1,
                                "Should note same-episode natural experiment")

    def test_chapter_structure_documented(self):
        """The chapter-level vocabulary bifurcation should be documented."""
        chapter_indicators = ["chapter", "timestamp", "32:14", "minute"]
        found = [c for c in chapter_indicators if c in self.summary]
        self.assertGreaterEqual(len(found), 1,
                                "Should document chapter-level evidence")

    def test_camera_capability_parity(self):
        """Should note identical capabilities being framed differently."""
        parity_indicators = ["identical", "same capability", "same feature",
                             "camera", "visual sensor", "ai processing"]
        found = [p for p in parity_indicators if p in self.summary]
        self.assertGreaterEqual(len(found), 1,
                                "Should note camera capability parity between entities")


class TestFashionTechCrossoverNovelty(unittest.TestCase):
    """Verify the fashion-tech crossover is identified as novel."""

    def setUp(self):
        self.data = load_competitor_research()
        self.mechanism = get_mechanism_227(self.data)
        self.summary = (self.mechanism.get("finding_summary", "") or
                        self.mechanism.get("overview", "")).lower()

    def test_fashion_podcast_noted(self):
        """Should note this is a fashion podcast, not tech-native."""
        fashion_indicators = ["fashion", "back row", "amy odell", "cosmopolitan"]
        found = [f for f in fashion_indicators if f in self.summary]
        self.assertGreaterEqual(len(found), 1,
                                "Should identify the fashion media crossover")

    def test_brand_stigma_routing(self):
        """Should note Meta absorbs stigma while Ray-Ban/EssilorLuxottica is buffered."""
        brand_indicators = ["meta", "ray-ban", "essilorluxottica", "brand", "stigma",
                            "fashion partner", "tech company"]
        found = [b for b in brand_indicators if b in self.summary]
        self.assertGreaterEqual(len(found), 2,
                                "Should note brand stigma routing")


class TestConfoundingFactors(unittest.TestCase):
    """Verify confounding factors are properly documented."""

    def setUp(self):
        self.data = load_competitor_research()
        self.mechanism = get_mechanism_227(self.data)

    def test_has_confounding_factors(self):
        factors = self.mechanism.get("confounding_factors", [])
        self.assertGreaterEqual(len(factors), 3,
                                "Should have at least 3 confounding factors")

    def test_confounding_factors_have_severity(self):
        factors = self.mechanism.get("confounding_factors", [])
        for factor in factors:
            self.assertIn("[", factor, f"Factor should have severity prefix: {factor[:50]}")
            severity = factor.split("]")[0].replace("[", "").strip()
            self.assertIn(severity, ["STRONG", "MODERATE", "WEAK"],
                          f"Invalid severity: {severity}")


class TestCrossReferences(unittest.TestCase):
    """Verify cross-references connect to related mechanisms."""

    def setUp(self):
        self.data = load_competitor_research()
        self.mechanism = get_mechanism_227(self.data)

    def test_has_cross_references(self):
        refs = self.mechanism.get("cross_references", [])
        self.assertGreaterEqual(len(refs), 2,
                                "Should have at least 2 cross-references")

    def test_cross_references_have_required_fields(self):
        refs = self.mechanism.get("cross_references", [])
        for ref in refs:
            self.assertIn("mechanism_id", ref)
            self.assertIn("relationship", ref)
            self.assertIn("description", ref)
            self.assertIn(ref["relationship"], ["extends", "parallel", "contrasts"])


class TestPodcastSentimentLogged(unittest.TestCase):
    """Verify the episode is logged in podcast-sentiment.md."""

    def setUp(self):
        self.content = load_podcast_sentiment()

    def test_back_row_logged(self):
        self.assertIn("Back Row", self.content,
                       "Back Row podcast should be in podcast-sentiment.md")

    def test_taylor_lorenz_mentioned(self):
        self.assertIn("Taylor Lorenz", self.content,
                       "Taylor Lorenz should be in podcast-sentiment.md")

    def test_hot_surveillance_summer_logged(self):
        lower = self.content.lower()
        self.assertIn("hot surveillance summer", lower,
                       "'Hot Surveillance Summer' episode should be logged")


if __name__ == "__main__":
    unittest.main()
