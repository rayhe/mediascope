"""
Mechanism #219: James Pero (Gizmodo) Apple AirPods Camera Temporal Intensification —
Reputational Credit Shield Strengthening Despite Hardware Confirmation (May–Aug 2026)

Type B: Journalist Cross-Entity Tracking

EXTENDS mechanism #211 (Three-Entity Privacy Vocabulary Gradient) with temporal dimension.

FINDING: James Pero's Apple camera AirPods coverage INTENSIFIES protection across 3 articles
over 3.5 months, despite each successive article revealing MORE evidence of surveillance
capability:

  Article 1 — May 8, 2026:
    "AirPods With Cameras Won't Let You Be a Total Creep"
    URL: https://gizmodo.com/airpods-with-cameras-wont-let-you-be-a-total-creep-2000756194
    Stage: RUMOR (pre-leaked-video, Bloomberg reporting only)
    Frame: PROACTIVE DEFENSE (raises alarm, dismisses it, credits Apple intent)
    Privacy alarm terms: ZERO
    Key language: "Won't Let You Be a Total Creep" (headline negation), "far less intrusive,"
      "Apple upholds its longstanding reputation"

  Article 2 — Aug 17, 2026:
    "Unearthed Video Seems to Reveal Apple AirPods That Can 'See'"
    URL: https://gizmodo.com/unearthed-video-seems-to-reveal-apple-airpods-that-can-see-2000799688
    Stage: VIDEO CONFIRMATION (macOS 26.7 RC leak, product existence confirmed)
    Frame: NEUTRAL CURIOSITY (scare quotes, no alarm, Apple's concern framed sympathetically)
    Privacy alarm terms: ZERO
    Key language: "Can 'See'" (scare-quoted, gentle), "a sensitive matter for Apple"

  Article 3 — Aug 21, 2026:
    "No, AirPods With Cameras Aren't Smart Glasses for Your Ears"
    URL: https://gizmodo.com/no-airpods-with-cameras-arent-smart-glasses-for-your-ears-2000801471
    Stage: TECHNICAL SPECS REVEALED (640×640 active, 320×320 passive always-on mode)
    Frame: ACTIVE DEFENSE (distinguishes from Meta, credits Apple, dismisses alarm)
    Privacy alarm terms: ZERO for Apple; "icky consequences" for Meta
    Key language: "While Meta has no issue collating user data...I can't imagine that Apple,
      a company that stakes its reputation on being a cut above in terms of user privacy,
      will want to tread down the route."
    Key detail: Acknowledges 320×320 passive always-on mode ("should have your alarm bells
      sounding") then IMMEDIATELY redirects to on-device processing as mitigation.

SAME JOURNALIST, SAME WEEK — Meta coverage:
  Jul 30: "Smart Glasses Are a Hit Even as Privacy Concerns Pile Up"
  Aug 11: "Smart Glasses Are Catching on With U.S. Police"
  Meta vocabulary: "pile up," "surveillance," "catching on with police" (adversarial)

TEMPORAL PATTERN: Reputation shields don't weaken as evidence accumulates — they strengthen.
The MORE confirmed Apple's camera wearable becomes (rumor → video → specs), the MORE
protective the coverage. This inverts the expected journalism pattern where confirmation
of capabilities should INCREASE scrutiny.

ATTRIBUTION NOTE: James Pero attribution for Aug 17 and Aug 21 articles is based on:
  1. "icky consequences" vocabulary match (May 8 #211 uses "icky results")
  2. "[As I wrote last month]" self-reference in Aug 17 article
  3. Self-described "resident smart glasses guy" role at Gizmodo
  4. Defensive negation headline pattern ("Won't Let You" → "Aren't Smart Glasses")
  5. Beat continuity across all three articles

Sources:
- https://gizmodo.com/airpods-with-cameras-wont-let-you-be-a-total-creep-2000756194
- https://gizmodo.com/unearthed-video-seems-to-reveal-apple-airpods-that-can-see-2000799688
- https://gizmodo.com/no-airpods-with-cameras-arent-smart-glasses-for-your-ears-2000801471
- https://gizmodo.com/smart-glasses-are-a-hit-even-as-privacy-concerns-pile-up-2000792911
"""

import unittest
import yaml
import os
import re


def load_yaml(filename):
    """Load a YAML profile from the profiles directory."""
    yaml_path = os.path.join(
        os.path.dirname(__file__), '..', 'profiles', filename
    )
    with open(yaml_path, 'r') as f:
        return yaml.safe_load(f)


def find_mechanism_in_research(mechanism_id):
    """Search competitor-coverage-research.yaml for a mechanism by ID."""
    data = load_yaml('competitor-coverage-research.yaml')
    for section_name in ['cross_publication_findings', 'aggregate_findings', 'publications']:
        section = data.get(section_name, {})
        if isinstance(section, dict):
            for key, value in section.items():
                if isinstance(value, dict) and value.get('mechanism_id') == mechanism_id:
                    return value
    return None


class TestMechanism219Exists(unittest.TestCase):
    """Mechanism #219 must exist in competitor-coverage-research.yaml."""

    def setUp(self):
        self.mechanism = find_mechanism_in_research(219)

    def test_mechanism_exists(self):
        self.assertIsNotNone(self.mechanism, "Mechanism #219 must exist")

    def test_mechanism_name_contains_temporal(self):
        name = self.mechanism.get('name', '')
        self.assertIn('Temporal', name)

    def test_mechanism_name_contains_pero(self):
        name = self.mechanism.get('name', '')
        self.assertIn('Pero', name)

    def test_mechanism_type_is_B(self):
        self.assertEqual(self.mechanism.get('type'), 'B')

    def test_journalist_is_james_pero(self):
        self.assertEqual(self.mechanism.get('journalist'), 'James Pero')

    def test_publication_is_gizmodo(self):
        pub = self.mechanism.get('publication', '')
        self.assertIn('Gizmodo', pub)

    def test_asymmetry_score_above_0_8(self):
        score = self.mechanism.get('asymmetry_score', 0)
        self.assertGreaterEqual(score, 0.8)

    def test_has_confounding_factors(self):
        cf = self.mechanism.get('confounding_factors', [])
        self.assertGreater(len(cf), 0)

    def test_confounding_factors_are_strings(self):
        cf = self.mechanism.get('confounding_factors', [])
        for factor in cf:
            self.assertIsInstance(factor, str)

    def test_confounding_factors_have_severity_prefix(self):
        cf = self.mechanism.get('confounding_factors', [])
        for factor in cf:
            self.assertRegex(factor, r'^\[(?:STRONG|MODERATE|WEAK)\]')

    def test_has_source_urls(self):
        urls = self.mechanism.get('source_urls', [])
        self.assertGreater(len(urls), 0)

    def test_source_urls_include_aug_17_article(self):
        urls = self.mechanism.get('source_urls', [])
        aug17_url = 'https://gizmodo.com/unearthed-video-seems-to-reveal-apple-airpods-that-can-see-2000799688'
        self.assertIn(aug17_url, urls)

    def test_source_urls_include_aug_21_article(self):
        urls = self.mechanism.get('source_urls', [])
        aug21_url = 'https://gizmodo.com/no-airpods-with-cameras-arent-smart-glasses-for-your-ears-2000801471'
        self.assertIn(aug21_url, urls)

    def test_source_urls_include_may_8_article(self):
        urls = self.mechanism.get('source_urls', [])
        may8_url = 'https://gizmodo.com/airpods-with-cameras-wont-let-you-be-a-total-creep-2000756194'
        self.assertIn(may8_url, urls)

    def test_cross_references_include_211(self):
        refs = self.mechanism.get('cross_references', [])
        self.assertIn(211, refs)

    def test_cross_references_include_179(self):
        refs = self.mechanism.get('cross_references', [])
        self.assertIn(179, refs)

    def test_has_test_file(self):
        self.assertIn('test_file', self.mechanism)

    def test_has_finding_summary(self):
        summary = self.mechanism.get('finding_summary', '')
        self.assertGreater(len(summary), 50)


class TestTemporalIntensificationPattern(unittest.TestCase):
    """Validate the temporal intensification pattern documented in #219."""

    def setUp(self):
        self.mechanism = find_mechanism_in_research(219)

    def test_overview_documents_three_articles(self):
        overview = self.mechanism.get('overview', '')
        self.assertIn('May 8', overview)
        self.assertIn('Aug 17', overview)
        self.assertIn('Aug 21', overview)

    def test_overview_documents_escalation(self):
        overview = self.mechanism.get('overview', '')
        self.assertIn('INTENSIF', overview.upper())

    def test_overview_documents_passive_mode(self):
        """Aug 21 article reveals 320×320 passive always-on mode — key privacy capability."""
        overview = self.mechanism.get('overview', '')
        self.assertIn('passive', overview.lower())

    def test_overview_documents_icky_consequences(self):
        """The 'icky consequences' vocabulary link is the attribution evidence."""
        overview = self.mechanism.get('overview', '')
        self.assertIn('icky', overview.lower())

    def test_overview_documents_meta_contrast(self):
        overview = self.mechanism.get('overview', '')
        # Must reference the same-paragraph Apple vs Meta contrast
        self.assertIn("can't imagine", overview.lower())

    def test_finding_summary_documents_three_articles(self):
        summary = self.mechanism.get('finding_summary', '')
        self.assertIn('May 8', summary)
        self.assertIn('Aug 17', summary)
        self.assertIn('Aug 21', summary)


class TestGizmodoProfileUpdated(unittest.TestCase):
    """Gizmodo profile must include the new Aug 17 and Aug 21 articles."""

    def setUp(self):
        self.gizmodo = load_yaml('gizmodo.yaml')

    def test_gizmodo_profile_exists(self):
        self.assertIsNotNone(self.gizmodo)

    def test_apple_cross_entity_section_exists(self):
        cross = self.gizmodo.get('cross_entity_coverage', {})
        self.assertIn('apple', cross)

    def test_aug_17_article_in_profile(self):
        cross = self.gizmodo.get('cross_entity_coverage', {})
        apple = cross.get('apple', {})
        examples = apple.get('examples', [])
        aug17_found = any(
            '2026-08-17' in str(ex.get('date', '')) or
            'Unearthed Video' in str(ex.get('title', ''))
            for ex in examples
        )
        self.assertTrue(aug17_found, "Aug 17 AirPods article must be in gizmodo.yaml apple examples")

    def test_aug_21_article_in_profile(self):
        cross = self.gizmodo.get('cross_entity_coverage', {})
        apple = cross.get('apple', {})
        examples = apple.get('examples', [])
        aug21_found = any(
            '2026-08-21' in str(ex.get('date', '')) or
            "Aren't Smart Glasses" in str(ex.get('title', ''))
            for ex in examples
        )
        self.assertTrue(aug21_found, "Aug 21 AirPods article must be in gizmodo.yaml apple examples")


class TestVocabularyBifurcationEvidence(unittest.TestCase):
    """Test the specific vocabulary asymmetry documented in mechanism #219."""

    def setUp(self):
        self.mechanism = find_mechanism_in_research(219)

    def test_apple_zero_alarm_terms_documented(self):
        """Apple coverage across all 3 articles must show zero privacy alarm terms."""
        summary = self.mechanism.get('finding_summary', '')
        self.assertIn('zero alarm', summary.lower())

    def test_meta_adversarial_vocabulary_documented(self):
        summary = self.mechanism.get('finding_summary', '')
        self.assertIn('icky', summary.lower())

    def test_same_paragraph_contrast_documented(self):
        """The Aug 21 article's direct same-paragraph contrast is the key evidence."""
        summary = self.mechanism.get('finding_summary', '')
        self.assertIn('same paragraph', summary.lower())

    def test_reputation_shield_strengthening_pattern(self):
        """Core finding: shields strengthen over time, don't weaken with evidence."""
        summary = self.mechanism.get('finding_summary', '')
        self.assertIn('strengthen', summary.lower())


class TestCrossReferenceIntegrity(unittest.TestCase):
    """Mechanism #219 cross-references must be valid."""

    def test_mechanism_211_exists(self):
        m = find_mechanism_in_research(211)
        self.assertIsNotNone(m, "Referenced mechanism #211 must exist")

    def test_mechanism_179_exists(self):
        m = find_mechanism_in_research(179)
        self.assertIsNotNone(m, "Referenced mechanism #179 must exist")

    def test_mechanism_31_exists(self):
        m = find_mechanism_in_research(31)
        self.assertIsNotNone(m, "Referenced mechanism #31 must exist")

    def test_mechanism_99_exists(self):
        m = find_mechanism_in_research(99)
        self.assertIsNotNone(m, "Referenced mechanism #99 must exist")

    def test_mechanism_211_covers_james_pero(self):
        m = find_mechanism_in_research(211)
        journalist = m.get('journalist', '')
        self.assertIn('Pero', journalist)


if __name__ == '__main__':
    unittest.main()
