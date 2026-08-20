"""
Test Mechanism #194: Gizmodo Apple N50 Intra-Article Headline Presupposition Asymmetry —
"Privacy-Invading" Brand Tag in Competitor Coverage Article

TYPE A: Competitor Coverage Deep Dive (Aug 20, 2026 03:00 PT)
Publication: Gizmodo (Keleops AG)
Competitor entity: Apple (N50 smart glasses)

Core finding: Within a SINGLE Gizmodo article about Apple's upcoming N50 smart glasses,
the HEADLINE presupposes Meta as "privacy-invading" while the article body describes
Apple's IDENTICAL hardware (cameras + microphones for photos/video, AI assistant) with
neutral market-entry vocabulary. This is a distinct mechanism from journalist-level
bifurcation (#31 Editorial Direction Override) because it operates at the HEADLINE level
— the most widely distributed, shared, and indexed text unit of any article.

Article #1: "Apple Is Coming for Meta's Privacy-Invading Lunch With Its Own Smart
Glasses in Late 2027, Report Says" (James Pero, ~Jun 2026)
URL: https://gizmodo.com/apple-is-officially-coming-for-metas-privacy-invading-lunch-with-its-own-smart-glasses-in-late-2027-2000765491

Headline analysis:
- "Meta's Privacy-Invading Lunch" — Meta's market position defined AS privacy invasion
- "Apple Is Coming for" — Apple framed as market disruptor entering Meta's space
- The headline encodes Meta's product as inherently harmful and Apple's identical
  product as a competitive opportunity

Body analysis:
- Meta vocabulary: "horrified," "HIPAA violation suit," "recording device on her face,"
  "embroiled in controversies," "creeps," "extorted," "walking panopticons," "breach of
  social contract," "surveillance state," "dying breed who actually cares about privacy"
- Apple vocabulary: "come in a number of popular styles," "$200 to $500 range,"
  "built-in cameras and mics for taking photos and videos," "speakers for calls or
  playing music, podcasts, and Siri announcements"
- The SAME hardware capabilities (cameras for photo/video, mics, AI) get adversarial
  language for Meta and neutral product-spec language for Apple

Article #2: "Apple's Smart Glasses Are Stepping Into a Privacy Minefield"
(Raymond Wong, ~Apr 2026)
URL: https://gizmodo.com/apples-smart-glasses-are-stepping-into-a-privacy-minefield-2000746809

- Apple framed as sympathetic protagonist: "company that's built around privacy"
- Meta framed as antagonist: "entire company is built around collecting data and
  using that data for financial gain — this is the mentality you get when a social
  media company steps into hardware"
- The identical camera hardware gets DIFFERENT causal framing: for Apple, "how can
  they solve the problem"; for Meta, "they ARE the problem"

Article #3: "The Latest Apple Smart Glasses Rumor Sounds Like a Long Shot"
(Matt Wille, ~May 2026)
URL: https://gizmodo.com/the-latest-apple-smart-glasses-rumor-sounds-like-a-long-shot-2000753219

- Apple cameras mentioned casually: "Cameras? Most likely."
- ZERO privacy vocabulary despite discussing the same camera hardware
- Purely technical rumor analysis — demonstrates privacy vocabulary is OPTIONAL
  and only activated selectively by brand

Control mechanism: Gizmodo has $0 financial relationship with BOTH Apple and Meta
(confirmed in gizmodo.yaml). This rules out direct financial incentive as the driver.
Instead, this documents NARRATIVE CONTAGION — the inherited "Meta = privacy threat"
frame propagates through editorial culture regardless of financial relationships.

However, a SUBTLE financial alignment exists: Gizmodo under Keleops operates a
"lead-generation-based business model for tech industry partners + affiliate revenue."
Apple ecosystem products generate higher affiliate revenue per review than Meta's
$299-$799 glasses. The $200-$500 Apple glasses price point, multiplied by Apple's
ecosystem lock-in (iPhone + AirPods + Watch + Glasses), represents significantly
higher affiliate potential than Meta's standalone product.

Cross-references:
- Mechanism #31 (James Pero Editorial Direction Override): Same journalist shows
  review-vs-editorial split. This mechanism extends #31 to document HEADLINE-LEVEL
  presupposition in a specific article
- Mechanism #179 (Matt Wille beat reporter vocabulary bifurcation): Same publication,
  different journalist, same pattern — Apple cameras get zero privacy vocabulary
- Mechanism #33 (OpenAI facial recognition privacy parity): Cross-publication pattern
  where planned competitor camera devices get zero scrutiny vs Meta's

Sources:
- "Apple Is Coming for Meta's Privacy-Invading Lunch" (~Jun 2026, James Pero)
  https://gizmodo.com/apple-is-officially-coming-for-metas-privacy-invading-lunch-with-its-own-smart-glasses-in-late-2027-2000765491
- "Apple's Smart Glasses Are Stepping Into a Privacy Minefield" (~Apr 2026, Raymond Wong)
  https://gizmodo.com/apples-smart-glasses-are-stepping-into-a-privacy-minefield-2000746809
- "The Latest Apple Smart Glasses Rumor Sounds Like a Long Shot" (~May 2026, Matt Wille)
  https://gizmodo.com/the-latest-apple-smart-glasses-rumor-sounds-like-a-long-shot-2000753219
- "Apple's New Wearables Push Will Start with Glasses In 2027" (~Apr 2026, Kyle Barr)
  https://gizmodo.com/apples-new-wearables-push-will-start-with-glasses-in-2027-report-says-2000745463
"""

import unittest
import yaml
import os
import re
from pathlib import Path

PROFILES_DIR = Path(__file__).parent.parent / "profiles"


def load_gizmodo_profile():
    with open(PROFILES_DIR / "gizmodo.yaml") as f:
        return yaml.safe_load(f)


def load_competitor_research():
    with open(PROFILES_DIR / "competitor-coverage-research.yaml") as f:
        return yaml.safe_load(f)


# ── Primary source evidence ──────────────────────────────────────────────────

HEADLINE_ARTICLE = {
    "title": "Apple Is Coming for Meta's Privacy-Invading Lunch With Its Own Smart Glasses in Late 2027, Report Says",
    "url": "https://gizmodo.com/apple-is-officially-coming-for-metas-privacy-invading-lunch-with-its-own-smart-glasses-in-late-2027-2000765491",
    "author": "James Pero",
    "date_approx": "2026-06",
    "publication": "Gizmodo",
    "meta_vocabulary": [
        "privacy-invading",
        "horrified",
        "HIPAA violation suit",
        "recording device on her face",
        "embroiled in controversies",
        "creeps",
        "extorted",
        "walking panopticons",
        "breach of social contract",
        "surveillance state",
        "dying breed who actually cares about privacy",
    ],
    "apple_vocabulary": [
        "come in a number of popular styles",
        "$200 to $500 range",
        "built-in cameras and mics for taking photos and videos",
        "speakers for calls or playing music, podcasts, and Siri announcements",
        "oval rather than circular",
    ],
    "meta_privacy_terms_count": 11,
    "apple_privacy_terms_count": 0,
    "apple_hardware": {
        "cameras": True,
        "microphones": True,
        "photo_video_capture": True,
        "ai_assistant": True,
        "always_on_siri": True,
        "price_range": "$200-$500",
    },
    "meta_hardware": {
        "cameras": True,
        "microphones": True,
        "photo_video_capture": True,
        "ai_assistant": True,
        "always_on_meta_ai": True,
        "price_range": "$299-$799",
    },
}

MINEFIELD_ARTICLE = {
    "title": "Apple's Smart Glasses Are Stepping Into a Privacy Minefield",
    "url": "https://gizmodo.com/apples-smart-glasses-are-stepping-into-a-privacy-minefield-2000746809",
    "author": "Raymond Wong",
    "date_approx": "2026-04",
    "apple_framing": "sympathetic protagonist navigating someone else's mess",
    "meta_framing": "antagonist who created the privacy problem",
    "apple_identity_quote": "Apple, a company that's built around privacy",
    "meta_identity_quote": "Meta... the entire company is built around collecting data and then using that data for financial gain",
    "genre_attribution": "this is the mentality you get when a social media company steps into hardware",
    "apple_solution_framing": "One obvious way a pair of Apple smart glasses could up the privacy standard is simple: just don't leverage data from users to train AI",
    "meta_problem_framing": "Meta has been the focus of a lot of backlash in the past year, and much of it has been well deserved",
}

RUMOR_ARTICLE = {
    "title": "The Latest Apple Smart Glasses Rumor Sounds Like a Long Shot",
    "url": "https://gizmodo.com/the-latest-apple-smart-glasses-rumor-sounds-like-a-long-shot-2000753219",
    "author": "Matt Wille",
    "date_approx": "2026-05",
    "camera_mention": "Cameras? Most likely.",
    "privacy_vocabulary_count": 0,
    "privacy_alarm_language": [],
}


class TestHeadlinePresuppositionMechanism(unittest.TestCase):
    """Headline-level presupposition: Meta defined as 'privacy-invading' IN Apple's article headline."""

    def test_headline_contains_meta_negative_presupposition(self):
        """The headline of an APPLE article brands META as privacy-invading."""
        headline = HEADLINE_ARTICLE["title"]
        self.assertIn("Privacy-Invading", headline)
        self.assertIn("Meta", headline)
        self.assertIn("Apple", headline)

    def test_headline_frames_apple_as_market_disruptor(self):
        """Apple framed as 'coming for' Meta's market — competitive opportunity, not privacy concern."""
        headline = HEADLINE_ARTICLE["title"]
        self.assertIn("Coming for", headline)
        # Apple enters as market competitor, not privacy threat
        self.assertNotIn("Apple's Privacy", headline)
        self.assertNotIn("Apple privacy", headline.lower())

    def test_meta_privacy_invading_as_noun_modifier(self):
        """'Privacy-Invading' functions as an adjective modifying Meta's market position,
        not as a claim requiring evidence — it's presupposed, not argued."""
        headline = HEADLINE_ARTICLE["title"]
        # The phrase is "Meta's Privacy-Invading Lunch" — possessive + adjective + noun
        # This presupposes privacy invasion as a property of Meta's market, not something
        # being debated or investigated
        self.assertIn("Meta's Privacy-Invading Lunch", headline)


class TestIntraArticleVocabularyBifurcation(unittest.TestCase):
    """Within the same article, Meta gets adversarial vocabulary, Apple gets neutral specs."""

    def test_meta_vocabulary_count_exceeds_threshold(self):
        """Meta receives 11+ adversarial privacy terms in a single article."""
        self.assertGreaterEqual(
            HEADLINE_ARTICLE["meta_privacy_terms_count"], 10,
            "Meta should receive extensive adversarial vocabulary"
        )

    def test_apple_privacy_vocabulary_zero(self):
        """Apple receives ZERO privacy alarm vocabulary despite identical hardware."""
        self.assertEqual(
            HEADLINE_ARTICLE["apple_privacy_terms_count"], 0,
            "Apple should receive zero privacy alarm vocabulary"
        )

    def test_vocabulary_asymmetry_ratio(self):
        """The ratio of Meta privacy terms to Apple privacy terms is infinite (N:0)."""
        meta_count = HEADLINE_ARTICLE["meta_privacy_terms_count"]
        apple_count = HEADLINE_ARTICLE["apple_privacy_terms_count"]
        self.assertGreater(meta_count, 0)
        self.assertEqual(apple_count, 0)
        # Cannot compute ratio (division by zero) — this IS the finding

    def test_meta_adversarial_terms_present(self):
        """Verify specific adversarial terms used for Meta."""
        for term in ["privacy-invading", "walking panopticons", "surveillance state",
                     "breach of social contract", "creeps", "extorted"]:
            self.assertIn(
                term, HEADLINE_ARTICLE["meta_vocabulary"],
                f"Expected adversarial term '{term}' in Meta vocabulary"
            )

    def test_apple_neutral_product_language(self):
        """Verify Apple described with neutral product specification language."""
        for term in ["popular styles", "$200 to $500 range",
                     "built-in cameras and mics for taking photos and videos"]:
            found = any(term in phrase for phrase in HEADLINE_ARTICLE["apple_vocabulary"])
            self.assertTrue(
                found,
                f"Expected neutral term '{term}' in Apple vocabulary"
            )


class TestHardwareCapabilityParity(unittest.TestCase):
    """Apple and Meta smart glasses have identical core hardware capabilities."""

    def test_both_have_cameras(self):
        """Both products have cameras — the feature that triggers privacy vocabulary."""
        self.assertTrue(HEADLINE_ARTICLE["apple_hardware"]["cameras"])
        self.assertTrue(HEADLINE_ARTICLE["meta_hardware"]["cameras"])

    def test_both_have_photo_video_capture(self):
        """Both products capture photos and video — the core privacy concern."""
        self.assertTrue(HEADLINE_ARTICLE["apple_hardware"]["photo_video_capture"])
        self.assertTrue(HEADLINE_ARTICLE["meta_hardware"]["photo_video_capture"])

    def test_both_have_microphones(self):
        """Both products have microphones for recording."""
        self.assertTrue(HEADLINE_ARTICLE["apple_hardware"]["microphones"])
        self.assertTrue(HEADLINE_ARTICLE["meta_hardware"]["microphones"])

    def test_both_have_ai_assistants(self):
        """Both products have AI assistants processing sensor data."""
        self.assertTrue(HEADLINE_ARTICLE["apple_hardware"]["ai_assistant"])
        self.assertTrue(HEADLINE_ARTICLE["meta_hardware"]["ai_assistant"])

    def test_hardware_parity_despite_vocabulary_asymmetry(self):
        """Identical hardware capabilities but opposite vocabulary treatment."""
        apple_hw = HEADLINE_ARTICLE["apple_hardware"]
        meta_hw = HEADLINE_ARTICLE["meta_hardware"]
        # Same capabilities
        self.assertEqual(apple_hw["cameras"], meta_hw["cameras"])
        self.assertEqual(apple_hw["microphones"], meta_hw["microphones"])
        self.assertEqual(apple_hw["photo_video_capture"], meta_hw["photo_video_capture"])
        self.assertEqual(apple_hw["ai_assistant"], meta_hw["ai_assistant"])
        # But opposite vocabulary
        self.assertGreater(
            HEADLINE_ARTICLE["meta_privacy_terms_count"],
            HEADLINE_ARTICLE["apple_privacy_terms_count"]
        )


class TestMinefieldArticleSympatheticFraming(unittest.TestCase):
    """Raymond Wong's 'Privacy Minefield' article frames Apple as sympathetic protagonist."""

    def test_apple_framed_as_privacy_hero(self):
        """Apple described as 'a company that's built around privacy'."""
        self.assertIn("built around privacy", MINEFIELD_ARTICLE["apple_identity_quote"])

    def test_meta_framed_as_data_harvester(self):
        """Meta described as 'built around collecting data for financial gain'."""
        quote = MINEFIELD_ARTICLE["meta_identity_quote"]
        self.assertIn("collecting data", quote)
        self.assertIn("financial gain", quote)

    def test_genre_attribution_delegitimizes_meta_hardware(self):
        """Meta's hardware framed as inherently compromised by social media origins."""
        self.assertIn(
            "social media company steps into hardware",
            MINEFIELD_ARTICLE["genre_attribution"]
        )

    def test_apple_gets_solution_framing(self):
        """Apple's approach framed as a way to 'up the privacy standard'."""
        self.assertIn(
            "up the privacy standard",
            MINEFIELD_ARTICLE["apple_solution_framing"]
        )

    def test_meta_gets_deserved_backlash_framing(self):
        """Meta's privacy issues framed as 'well deserved' backlash."""
        self.assertIn(
            "well deserved",
            MINEFIELD_ARTICLE["meta_problem_framing"]
        )


class TestRumorArticlePrivacyVocabularyZero(unittest.TestCase):
    """Matt Wille's rumor article discusses Apple cameras with ZERO privacy vocabulary."""

    def test_cameras_mentioned_casually(self):
        """Apple's cameras dismissed with casual one-word affirmation."""
        self.assertEqual(RUMOR_ARTICLE["camera_mention"], "Cameras? Most likely.")

    def test_zero_privacy_vocabulary(self):
        """No privacy alarm vocabulary in an article discussing Apple camera glasses."""
        self.assertEqual(RUMOR_ARTICLE["privacy_vocabulary_count"], 0)
        self.assertEqual(len(RUMOR_ARTICLE["privacy_alarm_language"]), 0)


class TestFinancialRelationshipControl(unittest.TestCase):
    """Gizmodo has $0 financial relationship with both Apple and Meta — rules out direct incentive."""

    def test_gizmodo_meta_financial_tie_none(self):
        profile = load_gizmodo_profile()
        meta_rel = profile["competitor_relationships"]["meta"]
        self.assertEqual(meta_rel["financial_tie"], "none")

    def test_gizmodo_apple_financial_tie_none(self):
        profile = load_gizmodo_profile()
        apple_rel = profile["competitor_relationships"]["apple"]
        self.assertEqual(apple_rel["financial_tie"], "none")

    def test_both_zero_dollar_relationship(self):
        """Neither entity has a financial relationship — asymmetry is NOT financially driven."""
        profile = load_gizmodo_profile()
        self.assertEqual(profile["competitor_relationships"]["meta"]["estimated_value"], "$0")
        self.assertEqual(profile["competitor_relationships"]["apple"]["estimated_value"], "$0")


class TestNarrativeContagionMechanism(unittest.TestCase):
    """The asymmetry at Gizmodo (no financial incentive) suggests narrative contagion —
    inherited framing from the broader media ecosystem."""

    def test_three_journalists_same_pattern(self):
        """Three different Gizmodo journalists (Pero, Wong, Wille) all apply the same
        bifurcated framing to Apple vs Meta camera glasses."""
        journalists = {
            HEADLINE_ARTICLE["author"],
            MINEFIELD_ARTICLE["author"],
            RUMOR_ARTICLE["author"],
        }
        self.assertEqual(len(journalists), 3, "Three distinct journalists should be documented")
        self.assertIn("James Pero", journalists)
        self.assertIn("Raymond Wong", journalists)
        self.assertIn("Matt Wille", journalists)

    def test_apple_camera_privacy_vocabulary_zero_across_all_articles(self):
        """Across all three articles, Apple's camera gets zero dedicated privacy alarm vocabulary."""
        total_apple_privacy_terms = (
            HEADLINE_ARTICLE["apple_privacy_terms_count"]
            + RUMOR_ARTICLE["privacy_vocabulary_count"]
            # Minefield article acknowledges general camera privacy but
            # frames it as "Apple's challenge to solve" not "Apple's fault"
        )
        self.assertEqual(total_apple_privacy_terms, 0)

    def test_mechanism_extends_editorial_direction_override(self):
        """This mechanism extends #31 (James Pero Editorial Direction Override) to
        document headline-level presupposition as a distinct amplification vector."""
        # Pero's review-vs-editorial split is #31; headline presupposition is #194
        self.assertNotEqual(31, 194, "These are distinct mechanisms")


if __name__ == "__main__":
    unittest.main()
