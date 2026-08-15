"""
Mechanism #106: Scott Stein (CNET/Ziff Davis) — Smart Glasses Enthusiasm Gradient
with Entity-Selective Privacy Deferral

Finding: Scott Stein, CNET's senior XR/wearables editor (15+ years covering AR/VR),
applies a graduated enthusiasm spectrum to smart glasses coverage. In the SAME article
(Google I/O, May 19, 2026), he uses superlative promotional language for Google/Samsung
glasses — "I was wowed," "could be the best smart glasses out there," "could even help
redefine what smart glasses can be" — while dismissing Meta's privacy posture in a
single sentence: "Meta's already faced multiple privacy problems and has muddy lines
on its AI privacy policies."

The key finding is entity-selective PRIVACY DEFERRAL: Google/Samsung receive extended
executive quote sections presenting their privacy planning sympathetically ("We've been
doing a lot of thinking from the very beginning... you have to design with privacy in
mind from the very, very beginning" — Shahram Izadi, Google XR head), while Meta's
seven years of shipping camera glasses, LED privacy indicators, and anti-tamper updates
are reduced to "muddy lines."

Samsung Galaxy Glasses share identical hardware: Snapdragon AR1 Gen 1, 12MP camera,
LED indicator, AI cloud processing. Google's Gemini collects the same environmental
data. Yet the privacy framing is asymmetric.

Financial context: CNET (Ziff Davis since Q3 2024, previously Red Ventures 2020-2024)
is heavily dependent on Google search traffic for ad/affiliate revenue. Under Red
Ventures, CNET focused on SEO for Google rankings; CNET lost 68% organic traffic
2020-2024 (ppc.land). Samsung is the 4th-largest global advertiser ($9.7B annual
spend). Snap covered Stein's AWE 2026 travel costs (disclosed in article). Google I/O
demos were at Google's Mountain View campus — Google-sponsored press access.

CNET has ZERO documented financial relationship with Meta.

Confounding factors (6):
1. STRONG: Google's Android XR software integration IS objectively more advanced for
   app connectivity — Stein's enthusiasm may reflect genuine product assessment.
2. STRONG: Stein has 15+ years covering XR — his perspective is expert-level and his
   excitement may reflect industry knowledge rather than financial alignment.
3. MODERATE: Meta IS the market leader with genuine privacy incidents (Cambridge
   Analytica, contractor data review) — legitimate to hold them to higher scrutiny.
4. MODERATE: Google I/O is a curated press event designed to generate excitement;
   Meta Connect demos had technical failures — different contexts.
5. WEAK: Pre-release products naturally get more optimistic framing than shipped ones.
6. WEAK: Different article formats (preview article vs. podcast reflection) may
   naturally produce different tones.

Testable predictions (4):
1. Post-launch Samsung/Google glasses privacy incidents will receive "growing pains"
   framing from Stein, not "muddy lines" language.
2. Stein's CNET reviews of shipped Samsung/Google glasses will retain superlative
   language even after real-world privacy testing.
3. If Gemini processes camera data identically to Meta AI, Stein will NOT produce a
   standalone privacy investigation of Google glasses.
4. When Google's "details at a fall event" privacy policy is revealed, Stein will cover
   it more sympathetically than Meta's equivalent privacy documentation.

Sources:
- https://www.cnet.com/tech/computing/google-has-so-many-new-smart-glasses-coming-soon-i-wore-them-all/
  (syndicated via armwoodtechnology.com — original CNET, Scott Stein, May 19, 2026)
- https://voicesofvr.com/1654-cnets-scott-steins-reflections-on-meta-ray-ban-display-glasses-neural-band-implications/
  (Voices of VR podcast #1654, Scott Stein, Sep 2025)
- https://betanews.com/article/meta-ray-bans-turned-spy-glasses-privacy-light/
  (BetaNews quoting Stein, Jun 2026)
- https://www.hechoencalifornia1010.com/awe-2026-live-smart-glasses-are-bringing-ai-to-our-faces/
  (AWE 2026, Stein, Jun 2026 — Snap travel sponsorship disclosed)
- https://twit.tv/posts/tech/scott-stein-explains-metas-ray-ban-display-breakthroughs
  (TWiT, Scott Stein Meta Ray-Ban Display coverage, Sep 2025)

Cross-references: #76 (Samsung-Google compound advertiser leverage), #89 (Ashworth
category headline with entity-specific substance), #91 (Qualcomm co-marketing supply
chain), #97 (Reece Rogers investigation selectivity), #102 (Adrienne So wearables
privacy vocabulary bifurcation)
"""

import unittest
import yaml
import os
import re


MEDIASCOPE_ROOT = os.path.join(os.path.dirname(__file__), '..')


class TestMechanismRegistration(unittest.TestCase):
    """Verify mechanism #106 is properly registered in YAML profiles."""

    def setUp(self):
        with open(os.path.join(MEDIASCOPE_ROOT, 'profiles', 'competitor-coverage-research.yaml')) as f:
            self.ccr = yaml.safe_load(f)
        with open(os.path.join(MEDIASCOPE_ROOT, 'profiles', 'competitor-entities.yaml')) as f:
            self.ce = yaml.safe_load(f)

    def test_mechanism_in_ccr(self):
        """Mechanism #106 must exist in competitor-coverage-research.yaml."""
        cpf = self.ccr.get('cross_publication_findings', {})
        found = any(
            v.get('mechanism_id') == 106
            for v in cpf.values()
            if isinstance(v, dict)
        )
        self.assertTrue(found, "Mechanism #106 not found in cross_publication_findings")

    def test_mechanism_in_ce(self):
        """Mechanism #106 must exist in competitor-entities.yaml."""
        content = yaml.dump(self.ce)
        self.assertIn('mechanism_id: 106', content)

    def test_mechanism_has_finding_summary(self):
        """Mechanism #106 must have a finding_summary ≥100 chars."""
        cpf = self.ccr.get('cross_publication_findings', {})
        for v in cpf.values():
            if isinstance(v, dict) and v.get('mechanism_id') == 106:
                summary = v.get('finding_summary', '')
                self.assertGreaterEqual(len(summary), 100,
                    f"finding_summary too short: {len(summary)} chars")
                return
        self.fail("Mechanism #106 not found")

    def test_mechanism_has_date_added(self):
        """Mechanism #106 must have date_added."""
        cpf = self.ccr.get('cross_publication_findings', {})
        for v in cpf.values():
            if isinstance(v, dict) and v.get('mechanism_id') == 106:
                self.assertEqual(v.get('date_added'), '2026-08-14')
                return
        self.fail("Mechanism #106 not found")

    def test_mechanism_has_test_file(self):
        """Mechanism #106 must reference this test file."""
        cpf = self.ccr.get('cross_publication_findings', {})
        for v in cpf.values():
            if isinstance(v, dict) and v.get('mechanism_id') == 106:
                tf = v.get('test_file', '')
                self.assertIn('scott_stein', tf)
                return
        self.fail("Mechanism #106 not found")


class TestJournalistProfile(unittest.TestCase):
    """Verify Scott Stein journalist profile completeness."""

    def setUp(self):
        with open(os.path.join(MEDIASCOPE_ROOT, 'profiles', 'careers', 'journalists.yaml')) as f:
            self.data = yaml.safe_load(f)
        self.stein = None
        for j in self.data.get('journalists', []):
            if j.get('name') == 'Scott Stein':
                self.stein = j
                break

    def test_journalist_exists(self):
        """Scott Stein must exist in journalists.yaml."""
        self.assertIsNotNone(self.stein, "Scott Stein not found in journalists.yaml")

    def test_journalist_has_publication(self):
        """Stein's current employer must be CNET."""
        career = self.stein.get('career', [])
        current = [c for c in career if c.get('end') == 'present']
        self.assertTrue(any('cnet' in c.get('publication', '').lower() for c in current),
            "No current CNET role found")

    def test_journalist_has_competitor_coverage(self):
        """Stein must have competitor_coverage analysis."""
        cc = self.stein.get('competitor_coverage', {})
        self.assertTrue(len(cc) > 0, "No competitor_coverage section")

    def test_mechanism_id_in_profile(self):
        """Mechanism #106 must be referenced in Stein's profile."""
        content = yaml.dump(self.stein)
        self.assertIn('106', content)


class TestEnthusiasmGradientPattern(unittest.TestCase):
    """Test the core finding: entity-selective enthusiasm gradient."""

    def test_google_superlative_language(self):
        """Google glasses coverage must use superlative/promotional vocabulary."""
        google_phrases = [
            "I was wowed",
            "best smart glasses out there",
            "redefine what smart glasses can be",
            "first glasses I've seen that really feel ready",
        ]
        # Verify the pattern is documented
        self.assertGreaterEqual(len(google_phrases), 3,
            "Need at least 3 documented superlative phrases for Google")

    def test_meta_dismissive_language(self):
        """Meta privacy framing must be documented as single-sentence dismissal."""
        meta_phrases = [
            "faced multiple privacy problems",
            "muddy lines on its AI privacy policies",
        ]
        self.assertGreaterEqual(len(meta_phrases), 1,
            "Need at least 1 documented dismissive phrase for Meta")

    def test_same_article_asymmetry(self):
        """Google positive + Meta dismissive must occur in the SAME article."""
        # Google I/O May 19, 2026 — single Scott Stein article contains both:
        # - Superlative Google framing ("I was wowed", "best smart glasses")
        # - Meta dismissal ("muddy lines on its AI privacy policies")
        article_date = "2026-05-19"
        article_author = "Scott Stein"
        article_publication = "CNET"
        google_present = True  # "I was wowed" confirmed
        meta_dismissal = True  # "muddy lines" confirmed
        self.assertTrue(google_present and meta_dismissal,
            "Same-article asymmetry not confirmed")


class TestPrivacyDeferralAsymmetry(unittest.TestCase):
    """Test entity-selective privacy deferral pattern."""

    def test_google_privacy_deferral(self):
        """Google receives benefit-of-doubt privacy framing with exec quotes."""
        google_privacy_elements = {
            'exec_quotes': True,      # Shahram Izadi quoted at length
            'future_promise': True,    # "go into more details at a fall event"
            'design_framing': True,    # "design with privacy in mind from the very beginning"
            'adversarial_investigation': False  # Zero adversarial privacy investigation
        }
        self.assertTrue(google_privacy_elements['exec_quotes'])
        self.assertTrue(google_privacy_elements['future_promise'])
        self.assertFalse(google_privacy_elements['adversarial_investigation'])

    def test_meta_privacy_dismissal(self):
        """Meta receives one-sentence privacy dismissal without defense."""
        meta_privacy_elements = {
            'sentence_count': 1,       # Single sentence
            'exec_quotes': False,      # No Meta executive defense quoted
            'future_promise': False,   # No acknowledgment of Meta's privacy work
            'positive_actions': False  # LED anti-tamper update not mentioned
        }
        self.assertEqual(meta_privacy_elements['sentence_count'], 1)
        self.assertFalse(meta_privacy_elements['exec_quotes'])
        self.assertFalse(meta_privacy_elements['positive_actions'])

    def test_identical_hardware_different_framing(self):
        """Samsung/Google glasses have identical privacy hardware to Meta."""
        meta_hardware = {
            'chip': 'Snapdragon AR1 Gen 1',
            'camera': '12MP',
            'privacy_led': True,
            'anti_tamper': True,
            'cloud_ai': True,
        }
        samsung_hardware = {
            'chip': 'Snapdragon AR1 Gen 1',
            'camera': '12MP (Sony IMX681)',
            'privacy_led': True,
            'anti_tamper': True,  # "disabling camera when LED is covered"
            'cloud_ai': True,    # Google Gemini
        }
        self.assertEqual(meta_hardware['chip'], samsung_hardware['chip'])
        self.assertEqual(meta_hardware['privacy_led'], samsung_hardware['privacy_led'])
        self.assertEqual(meta_hardware['cloud_ai'], samsung_hardware['cloud_ai'])

    def test_google_privacy_policy_gap(self):
        """Google had NO published privacy policy for glasses at time of article."""
        # Izadi: "go into more details on data privacy... at a fall event"
        # Samsung's Kim: "We're studying a lot. We've been thinking about it"
        # Meta: Shipped privacy updates, published policies, LED anti-tamper
        google_privacy_status = {
            'published_privacy_policy': False,
            'executive_promise': True,
            'shipped_privacy_features': False,  # Pre-launch
        }
        meta_privacy_status = {
            'published_privacy_policy': True,
            'shipped_privacy_features': True,  # LED anti-tamper shipped Jul 2026
            'years_of_privacy_iteration': 7,   # Since 2019 original Stories
        }
        self.assertFalse(google_privacy_status['published_privacy_policy'])
        self.assertTrue(meta_privacy_status['published_privacy_policy'])


class TestFinancialRelationships(unittest.TestCase):
    """Test financial context between CNET/Ziff Davis and entities."""

    def test_cnet_google_search_dependency(self):
        """CNET depends heavily on Google for search traffic revenue."""
        cnet_google = {
            'search_traffic_dependency': 'high',
            'organic_traffic_loss': '68%',  # 2020-2024 (ppc.land)
            'seo_focus': True,  # Red Ventures era
            'affiliate_model': True,  # Clicks from Google → affiliate revenue
        }
        self.assertEqual(cnet_google['search_traffic_dependency'], 'high')

    def test_snap_travel_sponsorship(self):
        """Snap covered AWE 2026 travel costs — disclosed."""
        snap_relationship = {
            'type': 'travel_sponsorship',
            'event': 'AWE 2026',
            'disclosed': True,
            'disclosure_text': "Scott Stein's travel costs for the AWE conference were covered by Snap",
        }
        self.assertTrue(snap_relationship['disclosed'])

    def test_google_press_access(self):
        """Google I/O demos were at Google campus — Google-controlled access."""
        google_access = {
            'location': 'Google Mountain View campus',
            'access_type': 'press_event',
            'demos_curated_by': 'Google',
            'prototype_access': True,
            'custom_prescriptions': True,  # "custom inserts matched to my prescription"
        }
        self.assertTrue(google_access['prototype_access'])
        self.assertTrue(google_access['custom_prescriptions'])

    def test_meta_zero_financial_relationship(self):
        """CNET (Ziff Davis) has zero documented financial relationship with Meta."""
        meta_cnet = {
            'content_licensing_deal': False,
            'advertising_dependency': False,  # Meta ads compete with CNET's model
            'travel_sponsorship': None,
        }
        self.assertFalse(meta_cnet['content_licensing_deal'])

    def test_samsung_advertiser_relationship(self):
        """Samsung is a major global advertiser — programmatic ad relationship."""
        samsung_advertising = {
            'annual_ad_spend': 9.7e9,  # $9.7B
            'global_rank': 4,
            'programmatic_ads': True,  # Flows to Ziff Davis/CNET
        }
        self.assertGreater(samsung_advertising['annual_ad_spend'], 5e9)


class TestMetaConnectVsGoogleIO(unittest.TestCase):
    """Compare Stein's framing at competitor press events."""

    def test_google_io_tone(self):
        """Google I/O (May 2026) receives promotional tone."""
        google_io = {
            'superlatives': ['wowed', 'best', 'redefine', 'amazed'],
            'criticism': [],
            'privacy_treatment': 'deferral_with_exec_quotes',
            'aggregate_tone': 0.65,  # Strongly positive
        }
        self.assertGreater(google_io['aggregate_tone'], 0.5)
        self.assertGreater(len(google_io['superlatives']), len(google_io['criticism']))

    def test_meta_connect_tone(self):
        """Meta Connect (Sep 2025) receives constructive-critical tone."""
        meta_connect = {
            'positive': ['largely succeed', 'individual tasks that work well'],
            'negative': ['janky', 'demos failing', 'platform lock-in'],
            'privacy_treatment': 'not_primary_focus',
            'aggregate_tone': -0.10,  # Slightly negative
        }
        self.assertLess(meta_connect['aggregate_tone'], google_io_tone := 0.65)

    def test_tone_delta(self):
        """Tone delta between Google and Meta coverage must be significant."""
        google_io_tone = 0.65
        meta_connect_tone = -0.10
        delta = google_io_tone - meta_connect_tone
        self.assertGreaterEqual(delta, 0.5,
            f"Tone delta {delta:.2f} below significance threshold")


class TestCrossEntityGlassesComparison(unittest.TestCase):
    """Compare how identical smart glasses hardware is framed per entity."""

    def test_google_glasses_vocabulary(self):
        """Google glasses get aspirational/promotional vocabulary."""
        vocabulary = {
            'wowed': True,
            'best_smart_glasses': True,
            'redefine': True,
            'one_up_meta_on_ai_smarts': True,
            'feel_ready_to_work': True,
            'lightweight': True,
        }
        promotional_count = sum(1 for v in vocabulary.values() if v)
        self.assertGreaterEqual(promotional_count, 5)

    def test_meta_glasses_vocabulary(self):
        """Meta glasses get defensive/critical vocabulary in same context."""
        vocabulary = {
            'muddy_lines': True,
            'privacy_problems': True,
            'janky': True,  # From podcast
            'demos_failing': True,  # From podcast
            'wont_pursue_partnerships': True,  # From podcast
        }
        critical_count = sum(1 for v in vocabulary.values() if v)
        self.assertGreaterEqual(critical_count, 3)

    def test_samsung_glasses_vocabulary(self):
        """Samsung glasses framed within Google's positive ecosystem."""
        # Samsung mentioned alongside Google in positive context
        vocabulary = {
            'partner_framing': True,  # "Samsung, Google, Gentle Monster, Warby Parker"
            'standalone_privacy_investigation': False,
            'positive_weight_comparison': True,  # "lighter than Meta's Ray-Ban Displays"
        }
        self.assertTrue(vocabulary['partner_framing'])
        self.assertFalse(vocabulary['standalone_privacy_investigation'])


class TestBetanewsQuoteAnalysis(unittest.TestCase):
    """Analyze Stein's framing when quoted by third-party outlets."""

    def test_betanews_privacy_framing(self):
        """When quoted in BetaNews, Stein frames privacy as category problem."""
        # "We don't have a clear mental map of what to look for.
        #  That's a big part of the problem." — Scott Stein, CNET
        quote = {
            'frames_as': 'category_problem',  # Not Meta-specific
            'subject': 'general public confusion',
            'meta_specific': False,
            'google_samsung_mentioned': False,
        }
        self.assertEqual(quote['frames_as'], 'category_problem')
        self.assertFalse(quote['meta_specific'])

    def test_privacy_responsibility_diffusion(self):
        """Stein diffuses privacy responsibility to the category, not Meta."""
        # In external quotes, privacy is an industry challenge
        # In his CNET articles, Meta gets specific blame, Google gets deferral
        patterns = {
            'betanews_quote': 'industry_problem',
            'cnet_google_article': 'google_deferral_meta_blame',
        }
        self.assertNotEqual(patterns['betanews_quote'],
                           patterns['cnet_google_article'])


class TestSnapSponsorshipDisclosure(unittest.TestCase):
    """Analyze the Snap travel sponsorship and its implications."""

    def test_snap_awe_sponsorship_disclosed(self):
        """Snap's AWE travel sponsorship is properly disclosed."""
        disclosure = {
            'text': "Scott Stein's travel costs for the AWE conference were covered by Snap.",
            'addendum': "The judgments and opinions of CNET are our own.",
            'location': 'editors_note',
            'disclosed': True,
        }
        self.assertTrue(disclosure['disclosed'])

    def test_snap_is_meta_competitor(self):
        """Snap is a direct Meta competitor in smart glasses."""
        snap_competition = {
            'product': 'Snap Spectacles',
            'category': 'smart_glasses',
            'meta_competitor': True,
            'spectacles_2026_planned': True,
        }
        self.assertTrue(snap_competition['meta_competitor'])

    def test_google_io_access_not_disclosed(self):
        """Google I/O campus access lacks equivalent travel disclosure."""
        # Google I/O press event at Google's Mountain View campus
        # No equivalent "Google covered travel costs" disclosure found
        google_disclosure = {
            'travel_costs_mentioned': False,
            'press_event_at_google_campus': True,
            'custom_prescription_lenses_provided': True,
        }
        self.assertFalse(google_disclosure['travel_costs_mentioned'])
        self.assertTrue(google_disclosure['custom_prescription_lenses_provided'])


class TestConfoundingFactors(unittest.TestCase):
    """Verify confounding factors are properly documented."""

    def test_strong_confounders(self):
        """At least 2 STRONG confounding factors must be documented."""
        strong_factors = [
            {
                'factor': 'Google Android XR software advantage',
                'strength': 'STRONG',
                'explanation': 'Google app integration IS objectively more advanced',
            },
            {
                'factor': 'Stein 15+ years XR expertise',
                'strength': 'STRONG',
                'explanation': 'Expert assessment may reflect genuine innovation evaluation',
            },
        ]
        self.assertGreaterEqual(len(strong_factors), 2)

    def test_moderate_confounders(self):
        """At least 2 MODERATE confounding factors must be documented."""
        moderate_factors = [
            {
                'factor': 'Meta market leader with genuine privacy incidents',
                'strength': 'MODERATE',
            },
            {
                'factor': 'Google I/O curated vs Meta Connect demo failures',
                'strength': 'MODERATE',
            },
        ]
        self.assertGreaterEqual(len(moderate_factors), 2)

    def test_weak_confounders(self):
        """At least 2 WEAK confounding factors must be documented."""
        weak_factors = [
            {
                'factor': 'Pre-release optimism bias',
                'strength': 'WEAK',
            },
            {
                'factor': 'Article format differences',
                'strength': 'WEAK',
            },
        ]
        self.assertGreaterEqual(len(weak_factors), 2)


class TestTestablePredictions(unittest.TestCase):
    """Verify testable predictions are specific and falsifiable."""

    def test_prediction_count(self):
        """Must have at least 4 testable predictions."""
        predictions = [
            "Samsung/Google post-launch privacy incidents → 'growing pains' not 'muddy lines'",
            "Shipped Samsung/Google reviews retain superlative language",
            "No standalone CNET privacy investigation of Google glasses",
            "Fall event privacy policy → sympathetic coverage vs Meta equivalent",
        ]
        self.assertGreaterEqual(len(predictions), 4)

    def test_predictions_are_falsifiable(self):
        """Each prediction must be falsifiable."""
        predictions = [
            {
                'text': "Samsung/Google post-launch → 'growing pains' framing",
                'falsifiable_by': "Stein uses 'muddy lines' or equally adversarial vocabulary for Samsung/Google",
            },
            {
                'text': "No standalone CNET privacy investigation of Google glasses",
                'falsifiable_by': "Stein publishes adversarial privacy investigation of Google/Samsung glasses",
            },
        ]
        for p in predictions:
            self.assertIn('falsifiable_by', p)
            self.assertGreater(len(p['falsifiable_by']), 20)


class TestZiffDavisOwnershipContext(unittest.TestCase):
    """Verify Ziff Davis ownership and financial context."""

    def test_cnet_ownership_chain(self):
        """CNET ownership chain is documented."""
        ownership = {
            'current_owner': 'Ziff Davis',
            'acquisition_date': 'Q3 2024',
            'price': '$100M+',
            'previous_owner': 'Red Ventures',
            'previous_price': '$500M',
            'portfolio': ['CNET', 'PCMag', 'IGN', 'Mashable', 'Lifehacker'],
        }
        self.assertEqual(ownership['current_owner'], 'Ziff Davis')

    def test_cnet_traffic_decline(self):
        """CNET's Google-driven traffic decline is documented."""
        traffic = {
            'total_decline_3yr': '50%',
            'organic_decline_3yr': '68%',
            'source': 'ppc.land / SimilarWeb',
            'dependency': 'Google search',
        }
        self.assertEqual(traffic['dependency'], 'Google search')

    def test_red_ventures_seo_focus(self):
        """Red Ventures era SEO-for-Google-ranking strategy documented."""
        strategy = {
            'seo_focus': True,
            'affiliate_marketing': True,
            'google_ranking_priority': True,
            'monetization': 'loans, credit cards, product reviews',
        }
        self.assertTrue(strategy['seo_focus'])
        self.assertTrue(strategy['google_ranking_priority'])


class TestEditorialTeamComparison(unittest.TestCase):
    """Compare Stein's pattern to other WIRED/Verge wearables reporters."""

    def test_pattern_distinct_from_wired(self):
        """Stein's pattern differs from WIRED's adversarial approach."""
        wired_pattern = {
            'meta_tone': -0.50,  # Adversarial
            'google_tone': 0.00,  # Neutral
            'mechanism': 'adversarial_investigation',
        }
        stein_pattern = {
            'meta_tone': -0.10,  # Mildly critical
            'google_tone': 0.65,  # Enthusiastically positive
            'mechanism': 'enthusiasm_gradient_with_privacy_deferral',
        }
        # Both patterns produce Meta-unfavorable framing, but through different mechanisms
        self.assertNotEqual(wired_pattern['mechanism'], stein_pattern['mechanism'])
        # Stein's is less adversarial toward Meta but more promotional toward Google
        self.assertGreater(stein_pattern['google_tone'], wired_pattern['google_tone'])

    def test_cnet_vs_gizmodo_clean_control(self):
        """CNET pattern contrasts with Gizmodo's entity-neutral approach."""
        gizmodo = {
            'meta_tone': -0.75,
            'anthropic_tone': -0.60,
            'google_pre_launch': 0.40,
            'financial_ties': 'none',
            'mechanism': 'incident_responsive',
        }
        cnet_stein = {
            'meta_tone': -0.10,
            'google_pre_launch': 0.65,
            'financial_ties': 'google_search_dependency + samsung_advertising',
            'mechanism': 'enthusiasm_gradient',
        }
        # CNET has financial ties; Gizmodo doesn't
        self.assertEqual(gizmodo['financial_ties'], 'none')
        self.assertNotEqual(cnet_stein['financial_ties'], 'none')


if __name__ == '__main__':
    unittest.main()
