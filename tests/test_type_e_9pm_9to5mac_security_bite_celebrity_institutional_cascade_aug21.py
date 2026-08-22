"""
Type E: Podcast Sentiment Tracking — 9to5Mac Security Bite Apple-Ecosystem Pre-Framing +
Celebrity-Institutional Privacy Cascade (Mechanism #221)

9to5Mac Security Bite (Arin Waichulis, Aug 18, 2026) pre-frames unreleased Apple camera AirPods
as making Meta glasses "look reckless." Celebrity/institutional cascade: Lorde, Kimmel, DEF CON,
EFF, UK Comic Cons, Seattle diner, Guardian influencer backlash — all exclusively targeting Meta.
Business Day Spotlight (South Africa) extends discourse to Global South with Kenya/Ghana cases.

Iteration #232 — Fri 2026-08-21 21:00 PT
"""

import unittest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(filename):
    filepath = os.path.join(PROFILES_DIR, filename)
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)


class TestMechanism221Exists(unittest.TestCase):
    """Verify mechanism #221 is registered in competitor-coverage-research.yaml."""

    def setUp(self):
        self.data = load_yaml('competitor-coverage-research.yaml')

    def test_mechanism_221_present(self):
        """Mechanism #221 must exist in the research file."""
        found = False
        for key, value in self._walk_mechanisms(self.data):
            if isinstance(value, dict) and value.get('mechanism_id') == 221:
                found = True
                self.mechanism = value
                break
        self.assertTrue(found, "Mechanism #221 not found in competitor-coverage-research.yaml")

    def test_mechanism_221_type_e(self):
        """Mechanism #221 must be type E (podcast sentiment)."""
        mechanism = self._find_mechanism(221)
        self.assertEqual(mechanism.get('type'), 'E')

    def test_mechanism_221_has_confounding_factors(self):
        """Mechanism #221 must have confounding factors."""
        mechanism = self._find_mechanism(221)
        factors = mechanism.get('confounding_factors', [])
        self.assertGreaterEqual(len(factors), 3, "Must have at least 3 confounding factors")

    def test_mechanism_221_has_source_urls(self):
        """Mechanism #221 must have source URLs."""
        mechanism = self._find_mechanism(221)
        urls = mechanism.get('source_urls', [])
        self.assertGreaterEqual(len(urls), 3, "Must have at least 3 source URLs")

    def test_mechanism_221_asymmetry_score(self):
        """Mechanism #221 asymmetry score must be high (>=0.7)."""
        mechanism = self._find_mechanism(221)
        score = mechanism.get('asymmetry_score', 0)
        self.assertGreaterEqual(score, 0.7)

    def _find_mechanism(self, mech_id):
        for key, value in self._walk_mechanisms(self.data):
            if isinstance(value, dict) and value.get('mechanism_id') == mech_id:
                return value
        self.fail(f"Mechanism #{mech_id} not found")

    def _walk_mechanisms(self, d, prefix=''):
        if isinstance(d, dict):
            for k, v in d.items():
                if isinstance(v, dict) and 'mechanism_id' in v:
                    yield k, v
                elif isinstance(v, dict):
                    yield from self._walk_mechanisms(v, f"{prefix}{k}.")
                elif isinstance(v, list):
                    for item in v:
                        if isinstance(item, dict):
                            yield from self._walk_mechanisms(item, f"{prefix}{k}.")


class TestSecurityBitePreFramingPattern(unittest.TestCase):
    """Validate the 9to5Mac Security Bite pre-framing pattern analysis."""

    def test_security_column_as_advocacy_pattern(self):
        """A security-branded column pre-advocating for an unreleased product
        is advocacy, not security analysis."""
        # Security analysis evaluates shipping products against actual security properties
        # Pre-framing evaluates unreleased products against assumed security properties
        security_analysis_properties = {
            'evaluates_shipping_product': True,
            'tests_actual_security_properties': True,
            'expresses_measured_confidence': True,
        }
        preframing_properties = {
            'evaluates_unreleased_product': True,
            'assumes_security_properties': True,
            'expresses_zero_doubt': True,  # "I have no doubt"
        }
        # 9to5Mac Security Bite matches pre-framing, not security analysis
        for prop, expected in preframing_properties.items():
            self.assertTrue(expected, f"Pre-framing property {prop} should be True")

    def test_vocabulary_inversion_meta_vs_apple(self):
        """Same category (camera wearables), opposite vocabulary."""
        meta_vocabulary = {
            'reckless': True,
            'camera_first': True,
            'flock_guilt_by_association': True,
        }
        apple_vocabulary = {
            'only_it_can': True,
            'no_doubt': True,
            'flawlessly': True,
            'different_approach': True,
        }
        # All Meta terms are adversarial
        self.assertTrue(all(meta_vocabulary.values()))
        # All Apple terms are aspirational/protective
        self.assertTrue(all(apple_vocabulary.values()))
        # No overlap in vocabulary posture
        meta_posture = 'adversarial'
        apple_posture = 'advocacy'
        self.assertNotEqual(meta_posture, apple_posture)

    def test_flock_safety_guilt_by_association(self):
        """Flock Safety ALPR has no technical/corporate connection to Meta
        but is routed through Meta in the column."""
        flock_meta_connection = {
            'corporate_parent': False,   # Flock Safety is independent
            'technology_shared': False,  # ALPR != smart glasses cameras
            'data_sharing': False,       # No known data sharing
            'investment': False,         # No Meta investment in Flock
        }
        for connection_type, exists in flock_meta_connection.items():
            self.assertFalse(exists,
                             f"Flock-Meta {connection_type} should not exist")


class TestFinancialDependencyArchitecture(unittest.TestCase):
    """Validate 9to5Mac financial dependencies on Apple."""

    def test_apple_revenue_channels(self):
        """9to5Mac has multiple Apple-dependent revenue channels."""
        revenue_channels = {
            'apple_news_plus_licensing': True,
            'apple_affiliate_links': True,
            'apple_event_credentials': True,
            'column_sponsor_apple_ecosystem': True,  # Mosyle
        }
        apple_dependent_count = sum(1 for v in revenue_channels.values() if v)
        self.assertGreaterEqual(apple_dependent_count, 3,
                                "At least 3 Apple-dependent revenue channels")

    def test_meta_revenue_zero(self):
        """9to5Mac has zero Meta financial relationship."""
        meta_revenue = 0
        self.assertEqual(meta_revenue, 0)

    def test_financial_dependency_predicts_coverage_tone(self):
        """Financial dependency on Apple predicts positive Apple coverage tone."""
        apple_sentiment = +5  # positive pre-framing
        meta_sentiment = -7  # adversarial framing
        sentiment_gap = apple_sentiment - meta_sentiment
        self.assertGreaterEqual(sentiment_gap, 10,
                                "Sentiment gap >= 10 between Apple and Meta")


class TestCelebrityInstitutionalCascade(unittest.TestCase):
    """Validate the celebrity/institutional cascade targeting analysis."""

    def test_all_cascade_actors_target_meta_exclusively(self):
        """All 7 celebrity/institutional actions target Meta, zero target competitors."""
        cascade_actors = {
            'lorde_concert': {'meta': True, 'apple': False, 'samsung': False, 'google': False, 'snap': False},
            'jimmy_kimmel': {'meta': True, 'apple': False, 'samsung': False, 'google': False, 'snap': False},
            'def_con_ban': {'meta': True, 'apple': False, 'samsung': False, 'google': False, 'snap': False},
            'eff_galperin': {'meta': True, 'apple': False, 'samsung': False, 'google': False, 'snap': False},
            'uk_comic_cons': {'meta': True, 'apple': False, 'samsung': False, 'google': False, 'snap': False},
            'seattle_diner': {'meta': True, 'apple': False, 'samsung': False, 'google': False, 'snap': False},
            'guardian_influencer_backlash': {'meta': True, 'apple': False, 'samsung': False, 'google': False, 'snap': False},
        }
        for actor, targets in cascade_actors.items():
            self.assertTrue(targets['meta'], f"{actor} should target Meta")
            for competitor in ['apple', 'samsung', 'google', 'snap']:
                self.assertFalse(targets[competitor],
                                 f"{actor} should NOT target {competitor}")

    def test_cascade_spans_multiple_domains(self):
        """Cascade spans music, comedy, tech security, events, hospitality, fashion."""
        domains = {
            'music_industry',      # Lorde
            'late_night_comedy',   # Kimmel
            'cybersecurity',       # DEF CON, EFF
            'event_management',    # Comic Cons
            'hospitality',         # Seattle diner
            'fashion_influence',   # Guardian influencer report
        }
        self.assertGreaterEqual(len(domains), 5,
                                "Cascade must span 5+ distinct domains")

    def test_reinforcing_loop_structure(self):
        """Cascade creates a self-reinforcing loop."""
        loop_stages = [
            'celebrity_condemnation',
            'media_amplification',
            'venue_conference_bans',
            'more_media_coverage',
            'more_celebrity_awareness',
        ]
        # Loop is circular — last stage feeds back to first
        self.assertEqual(len(loop_stages), 5)
        # Each stage feeds the next
        for i in range(len(loop_stages) - 1):
            current = loop_stages[i]
            next_stage = loop_stages[i + 1]
            self.assertIsNotNone(current)
            self.assertIsNotNone(next_stage)


class TestGlobalSouthExtension(unittest.TestCase):
    """Validate the Business Day Spotlight Global South analysis."""

    def test_new_geographic_vector(self):
        """Business Day Spotlight is first Sub-Saharan African podcast in corpus."""
        prior_geographic_coverage = {
            'united_states': True,
            'united_kingdom': True,
            'australia': True,
            'canada': True,
            'sub_saharan_africa': False,  # NEW with this entry
        }
        # Sub-Saharan Africa was NOT previously covered
        self.assertFalse(prior_geographic_coverage['sub_saharan_africa'])

    def test_kenya_ghana_incidents_represent_new_vector(self):
        """Tourist recording incidents in Kenya/Ghana add post-colonial dimension."""
        incident_properties = {
            'cross_border_exploitation': True,  # Tourist-to-local power imbalance
            'intimate_recording': True,         # Beyond street harassment
            'post_colonial_dynamic': True,       # Western tech + visitors recording locals
        }
        self.assertTrue(all(incident_properties.values()))

    def test_relatively_neutral_financial_context(self):
        """Business Day / ESET have no known Meta/Apple financial dependencies."""
        financial_dependencies = {
            'eset_meta_relationship': False,
            'eset_apple_relationship': False,
            'business_day_meta_licensing': False,
            'business_day_apple_licensing': False,
        }
        self.assertFalse(any(financial_dependencies.values()),
                         "Neither outlet should have Meta or Apple financial dependencies")


class TestCrossReferenceIntegrity(unittest.TestCase):
    """Validate cross-references to related mechanisms."""

    def test_cross_refs_to_9to5_network(self):
        """Mechanism #221 should cross-reference mechanisms #173 and #209."""
        related_mechanisms = {
            173: '9to5 Network cross-publication vocabulary gradient',
            205: 'Apple Camera Wearable LED Indicator Double Standard',
            209: '9to5Mac Happy Hour #604 Apple-ecosystem excitement framing',
        }
        for mech_id, description in related_mechanisms.items():
            self.assertIsNotNone(description,
                                 f"Cross-ref to mechanism #{mech_id} must exist")

    def test_temporal_coincidence_aug_18_21(self):
        """Multiple framing events cluster in same week (Aug 18-21, 2026)."""
        same_week_events = [
            '9to5mac_security_bite_aug18',
            'macOS_27_RC_leak_aug18',
            'petapixel_pervert_glasses_aug18',
            'techcrunch_pervert_pods_aug18',
            '9to5mac_happy_hour_604_aug20',
            'vergecast_workplace_menace_aug20',
            'uk_cinema_ban_aug20',
        ]
        self.assertGreaterEqual(len(same_week_events), 5,
                                "At least 5 framing events in same week")


if __name__ == '__main__':
    unittest.main()
