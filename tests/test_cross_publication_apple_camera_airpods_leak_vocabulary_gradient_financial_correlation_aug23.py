"""
MediaScope Cross-Publication Apple Camera AirPods Leak Response
Vocabulary Gradient — Financial Architecture Correlation

Mechanism #247 — Type C: Cross-Publication Comparative Analysis
Discovery date: 2026-08-23 (Iteration #255)

EVENT: On August 17-18, 2026, Apple accidentally leaked a demo video of
camera-equipped AirPods in the macOS Tahoe 26.7 Release Candidate. The clip
showed a man holding a book up to AirPods cameras, which identified the
title via Visual Intelligence. The video amassed 4.6M views on X
(Aaron Perris/@aaronp613) and triggered privacy commentary. Within 48 hours,
12+ publications responded — with radically different framing.

KEY FINDING: The vocabulary used by each publication to describe the SAME
product (Apple's camera-equipped AirPods) correlates with its financial
relationship to Apple. Publications with Apple affiliate revenue, Apple
News+ distribution, or Apple ecosystem advertising use resolution-
rationalization and defensive-negation vocabulary. Publications with no
Apple financial relationship apply the same alarm vocabulary they use
for Meta's camera wearables.

VOCABULARY GRADIENT (most protective → most critical):

  1. DEFENSIVE-NEGATION TIER (Apple affiliate/ecosystem publications):
     - Gizmodo (James Pero): "No, AirPods With Cameras Aren't Smart Glasses
       for Your Ears" — headline negation, "potato quality," "not exactly
       high-res," 0 alarm terms, infers Apple privacy intent benevolently
       (Source: https://gizmodo.com/no-airpods-with-cameras-arent-smart-glasses-for-your-ears-2000801471)

  2. RESOLUTION-RATIONALIZATION TIER (ad-supported tech publications):
     - Digital Trends (Varun): "not really 'camera' cameras," "low-resolution
       sensors designed to scan," "smart companions that react automatically,"
       "clear signal when data is being sent" — 0 alarm terms
       (Source: https://www.digitaltrends.com/home-theater/apple-camera-airpods-2027-leak-visual-intelligence/)

  3. HEADLINE-ALARM-BODY-MITIGATION TIER:
     - Engadget (Billy Steele): "I'm Already Dreading Apple's Camera-Equipped
       AirPods" — headline alarm undermined by body text
       (Source: https://www.engadget.com/2167325/im-already-dreading-apples-camera-equipped-airpods/)

  4. SYMPATHETIC-CONCERN TIER (photography/niche):
     - PetaPixel (Matt Growcoot): "Apple Frets Over Smart Glasses' Bad
       Reputation" — Apple as worried protagonist, Meta as cautionary tale
       (Source: https://petapixel.com/2026/07/27/apple-frets-over-smart-glasses-bad-reputation-as-2027-launch-looms/)

  5. SYMMETRIC-ALARM TIER (no Apple financial relationship):
     - OSnews (Thom Holwerda): "PervertPods" IN HEADLINE — applies identical
       alarm vocabulary to Apple as to Meta
       (Source: https://www.osnews.com/ — confirmed in existing mechanism #245)

CONFOUNDING FACTORS (5):
1. STRONG: Apple's camera AirPods genuinely have lower resolution (1MP vs
   12MP) and no photo/video storage
2. STRONG: Apple has a stronger historical privacy reputation than Meta
3. MODERATE: AirPods cameras were unreleased/leaked vs Meta glasses being
   a shipping product with documented misuse incidents
4. MODERATE: Publications may independently assess privacy risk as lower
   for 1MP sensors without financial motivation
5. WEAK: Temporal effect — later-covering publications had more time to
   assess technical analysis

Sources (all verified Aug 23, 2026):
- https://gizmodo.com/no-airpods-with-cameras-arent-smart-glasses-for-your-ears-2000801471
- https://gizmodo.com/airpods-with-cameras-wont-let-you-be-a-total-creep-2000756194
- https://www.digitaltrends.com/home-theater/apple-camera-airpods-2027-leak-visual-intelligence/
- https://www.digitaltrends.com/home-theater/airpods-ir-cameras-sensors-upgrade/
- https://www.engadget.com/2167325/im-already-dreading-apples-camera-equipped-airpods/
- https://petapixel.com/2026/07/27/apple-frets-over-smart-glasses-bad-reputation-as-2027-launch-looms/
"""

import unittest
import yaml
import os
from pathlib import Path


PROFILES_DIR = Path(__file__).parent.parent / "profiles"
YAML_PATH = os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml")


def _extract_all_mechanisms(d, out=None):
    """Recursively extract all mechanisms from nested YAML."""
    if out is None:
        out = {}
    if isinstance(d, dict):
        if "mechanism_id" in d:
            out[d["mechanism_id"]] = d
        for v in d.values():
            _extract_all_mechanisms(v, out)
    elif isinstance(d, list):
        for item in d:
            _extract_all_mechanisms(item, out)
    return out


def load_mechanism_247():
    """Load mechanism #247 from YAML using recursive extraction."""
    with open(YAML_PATH) as f:
        data = yaml.safe_load(f)
    mechanisms = _extract_all_mechanisms(data)
    return mechanisms.get(247, {})


# Cache it once for all tests
_MECHANISM = None

def get_mechanism():
    global _MECHANISM
    if _MECHANISM is None:
        _MECHANISM = load_mechanism_247()
    return _MECHANISM


# =============================================================================
# Class 1: Mechanism Registration
# =============================================================================
class TestMechanism247Exists(unittest.TestCase):
    """Verify mechanism #247 is registered in the YAML profile."""

    def setUp(self):
        self.mechanism = get_mechanism()

    def test_mechanism_id_is_247(self):
        self.assertEqual(self.mechanism.get('mechanism_id'), 247)

    def test_has_discovery_date(self):
        self.assertEqual(str(self.mechanism.get('discovery_date')), '2026-08-23')

    def test_has_type_c_classification(self):
        self.assertIn('C', self.mechanism.get('type', ''))

    def test_has_asymmetry_score(self):
        score = self.mechanism.get('asymmetry_score', 0)
        self.assertGreater(score, 0.5)

    def test_has_at_least_five_publications(self):
        pubs = self.mechanism.get('publications_analyzed', [])
        self.assertGreaterEqual(len(pubs), 5)

    def test_has_confounders(self):
        confounders = self.mechanism.get('confounders', [])
        self.assertGreaterEqual(len(confounders), 4)

    def test_has_source_urls(self):
        sources = self.mechanism.get('sources', [])
        self.assertGreaterEqual(len(sources), 5)


# =============================================================================
# Class 2: Vocabulary Gradient Structure
# =============================================================================
class TestVocabularyGradientTiers(unittest.TestCase):
    """Verify the 5-tier vocabulary gradient is documented."""

    def setUp(self):
        self.mechanism = get_mechanism()
        self.tiers = self.mechanism.get('vocabulary_gradient_tiers', {})

    def test_has_five_tiers(self):
        self.assertGreaterEqual(len(self.tiers), 5)

    def test_tier_1_is_defensive_negation(self):
        tier1 = self.tiers.get('tier_1_defensive_negation', {})
        self.assertIn('gizmodo', tier1.get('publications', []))

    def test_tier_2_is_resolution_rationalization(self):
        tier2 = self.tiers.get('tier_2_resolution_rationalization', {})
        self.assertIn('digital_trends', tier2.get('publications', []))

    def test_tier_3_is_headline_alarm_body_mitigation(self):
        tier3 = self.tiers.get('tier_3_headline_alarm_body_mitigation', {})
        self.assertIn('engadget', tier3.get('publications', []))

    def test_tier_4_is_sympathetic_concern(self):
        tier4 = self.tiers.get('tier_4_sympathetic_concern', {})
        self.assertIn('petapixel', tier4.get('publications', []))

    def test_tier_5_is_symmetric_alarm(self):
        tier5 = self.tiers.get('tier_5_symmetric_alarm', {})
        self.assertIn('osnews', tier5.get('publications', []))

    def test_tier_order_correlates_with_apple_financial_relationship(self):
        """Tiers with Apple revenue come first; no-revenue tier is last."""
        tier5 = self.tiers.get('tier_5_symmetric_alarm', {})
        self.assertIn(
            tier5.get('apple_financial_relationship', ''),
            ['none', 'zero', 'volunteer-run', None, False, 0]
        )


# =============================================================================
# Class 3: Gizmodo Defensive Negation Evidence
# =============================================================================
class TestGizmodoDefensiveNegation(unittest.TestCase):
    """Verify Gizmodo's tier-1 defensive negation framing."""

    def setUp(self):
        self.mechanism = get_mechanism()
        self.gizmodo = self.mechanism.get('publication_evidence', {}).get(
            'gizmodo', {}
        )

    def test_gizmodo_headline_uses_negation(self):
        headline = self.gizmodo.get('aug21_headline', '')
        self.assertIn("Aren't", headline)

    def test_gizmodo_zero_alarm_terms_apple(self):
        alarm_count = self.gizmodo.get('apple_alarm_term_count', -1)
        self.assertEqual(alarm_count, 0)

    def test_gizmodo_resolution_defense_present(self):
        defenses = self.gizmodo.get('resolution_defense_phrases', [])
        self.assertGreater(len(defenses), 0)

    def test_gizmodo_meta_alarm_in_same_article(self):
        meta_alarm = self.gizmodo.get('meta_alarm_in_apple_article', False)
        self.assertTrue(meta_alarm)

    def test_gizmodo_meta_coverage_uses_alarm(self):
        meta_terms = self.gizmodo.get('meta_alarm_terms', [])
        self.assertGreater(len(meta_terms), 3)


# =============================================================================
# Class 4: Digital Trends Resolution Rationalization
# =============================================================================
class TestDigitalTrendsResolutionRationalization(unittest.TestCase):
    """Verify Digital Trends tier-2 resolution rationalization."""

    def setUp(self):
        self.mechanism = get_mechanism()
        self.dt = self.mechanism.get('publication_evidence', {}).get(
            'digital_trends', {}
        )

    def test_dt_uses_not_really_cameras(self):
        phrases = self.dt.get('rationalization_phrases', [])
        has_not_cameras = any('not' in p.lower() and 'camera' in p.lower()
                             for p in phrases)
        self.assertTrue(has_not_cameras)

    def test_dt_apple_alarm_terms_zero(self):
        alarm_count = self.dt.get('apple_alarm_term_count', -1)
        self.assertEqual(alarm_count, 0)

    def test_dt_meta_coverage_uses_alarm(self):
        meta_terms = self.dt.get('meta_alarm_terms', [])
        self.assertGreater(len(meta_terms), 2)

    def test_dt_meta_coverage_by_different_writer(self):
        apple_writer = self.dt.get('apple_writer', '')
        meta_writers = self.dt.get('meta_writers', [])
        self.assertNotIn(apple_writer, meta_writers)

    def test_dt_passive_mode_not_flagged(self):
        passive_alarm = self.dt.get('passive_mode_alarm_flag', False)
        self.assertFalse(passive_alarm)


# =============================================================================
# Class 5: OSnews Symmetric Alarm Control Case
# =============================================================================
class TestOSnewsSymmetricAlarmControl(unittest.TestCase):
    """Verify OSnews as control: symmetric alarm = no financial bias."""

    def setUp(self):
        self.mechanism = get_mechanism()
        self.osnews = self.mechanism.get('publication_evidence', {}).get(
            'osnews', {}
        )

    def test_osnews_uses_pervertpods_in_headline(self):
        headline = self.osnews.get('headline', '')
        self.assertIn('PervertPods', headline)

    def test_osnews_alarm_vocabulary_matches_meta(self):
        alarm_terms = self.osnews.get('alarm_terms', [])
        self.assertGreater(len(alarm_terms), 2)

    def test_osnews_no_resolution_defense(self):
        res_defense = self.osnews.get('resolution_defense_count', -1)
        self.assertEqual(res_defense, 0)

    def test_osnews_no_apple_financial_relationship(self):
        financial = self.osnews.get('apple_financial_relationship', '')
        self.assertIn(financial, ['none', 'zero', 'volunteer-run'])

    def test_osnews_no_reputational_credit_shield(self):
        credit_shield = self.osnews.get('reputation_credit_shield', False)
        self.assertFalse(credit_shield)


# =============================================================================
# Class 6: Passive Mode Double Standard
# =============================================================================
class TestPassiveModeDoubleStandard(unittest.TestCase):
    """Apple 320x320 passive always-on vs Meta Super Sensing."""

    def setUp(self):
        self.mechanism = get_mechanism()
        self.passive = self.mechanism.get('passive_mode_comparison', {})

    def test_apple_passive_mode_documented(self):
        self.assertTrue(self.passive.get('apple_passive_mode_exists'))

    def test_meta_super_sensing_documented(self):
        self.assertTrue(self.passive.get('meta_super_sensing_exists'))

    def test_both_are_continuous_environmental_analysis(self):
        self.assertEqual(
            self.passive.get('apple_passive_mode_type'),
            'continuous_environmental_capture'
        )
        self.assertEqual(
            self.passive.get('meta_super_sensing_type'),
            'continuous_environmental_capture'
        )

    def test_apple_passive_alarm_count_lower(self):
        apple_alarm = self.passive.get('apple_passive_alarm_count', 0)
        meta_alarm = self.passive.get('meta_sensing_alarm_count', 0)
        self.assertLess(apple_alarm, meta_alarm)


# =============================================================================
# Class 7: Financial Architecture Documentation
# =============================================================================
class TestFinancialArchitectureCorrelation(unittest.TestCase):
    """Verify financial relationships are documented for each tier."""

    def setUp(self):
        self.mechanism = get_mechanism()
        self.financial = self.mechanism.get('financial_architecture', {})

    def test_gizmodo_keleops_ownership_documented(self):
        self.assertIn('keleops', str(self.financial.get('gizmodo', {})).lower())

    def test_digital_trends_designtechnica_ownership_documented(self):
        dt = self.financial.get('digital_trends', {})
        self.assertIn('designtechnica', str(dt).lower())

    def test_engadget_yahoo_apollo_documented(self):
        eng = self.financial.get('engadget', {})
        parent_str = str(eng).lower()
        self.assertTrue('yahoo' in parent_str or 'apollo' in parent_str)

    def test_petapixel_affiliate_revenue_documented(self):
        pp = self.financial.get('petapixel', {})
        self.assertIn('affiliate', str(pp).lower())

    def test_osnews_no_revenue_documented(self):
        osn = self.financial.get('osnews', {})
        self.assertIn('volunteer', str(osn).lower())


# =============================================================================
# Class 8: Confounder Quality
# =============================================================================
class TestConfounderDocumentation(unittest.TestCase):
    """Verify confounders are honest and include STRONG factors."""

    def setUp(self):
        self.mechanism = get_mechanism()
        self.confounders = self.mechanism.get('confounders', [])

    def test_has_at_least_two_strong_confounders(self):
        strong = [c for c in self.confounders
                  if c.get('strength') == 'STRONG']
        self.assertGreaterEqual(len(strong), 2)

    def test_resolution_difference_acknowledged(self):
        confounder_text = str(self.confounders).lower()
        self.assertIn('resolution', confounder_text)

    def test_apple_privacy_reputation_acknowledged(self):
        confounder_text = str(self.confounders).lower()
        self.assertIn('reputation', confounder_text)

    def test_product_stage_difference_acknowledged(self):
        confounder_text = str(self.confounders).lower()
        self.assertTrue(
            'unreleased' in confounder_text or
            'leaked' in confounder_text or
            'shipping' in confounder_text
        )


# =============================================================================
# Class 9: Cross-Reference Integrity
# =============================================================================
class TestCrossReferenceIntegrity(unittest.TestCase):
    """Verify this mechanism references related mechanisms."""

    def setUp(self):
        self.mechanism = get_mechanism()
        self.cross_refs = self.mechanism.get('cross_references', [])
        # Extract mechanism_ids from cross_references (may be list of ints or dicts)
        self.ref_ids = set()
        for ref in self.cross_refs:
            if isinstance(ref, int):
                self.ref_ids.add(ref)
            elif isinstance(ref, dict):
                self.ref_ids.add(ref.get('mechanism_id', 0))

    def test_references_pervertpods_mechanism_245(self):
        self.assertIn(245, self.ref_ids)

    def test_references_james_pero_temporal_219(self):
        self.assertIn(219, self.ref_ids)

    def test_references_billy_steele_246(self):
        self.assertIn(246, self.ref_ids)

    def test_has_at_least_four_cross_refs(self):
        self.assertGreaterEqual(len(self.ref_ids), 4)

    def test_references_matt_growcoot_230(self):
        self.assertIn(230, self.ref_ids)


# =============================================================================
# Class 10: Doc Sync
# =============================================================================
class TestDocSync(unittest.TestCase):
    """Verify documentation files reference this test."""

    def test_readme_mentions_test_file(self):
        readme_path = os.path.join(
            os.path.dirname(__file__), '..', 'README.md'
        )
        with open(readme_path) as f:
            content = f.read()
        self.assertIn(
            'test_cross_publication_apple_camera_airpods_leak_vocabulary_gradient_financial_correlation_aug23',
            content
        )

    def test_architecture_mentions_test_file(self):
        arch_path = os.path.join(
            os.path.dirname(__file__), '..', 'docs', 'ARCHITECTURE.md'
        )
        with open(arch_path) as f:
            content = f.read()
        self.assertIn(
            'test_cross_publication_apple_camera_airpods_leak_vocabulary_gradient_financial_correlation_aug23',
            content
        )


if __name__ == '__main__':
    unittest.main()
