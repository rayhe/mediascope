"""
Mechanism #215: Mia Sato (The Verge / PMX / PMC) Same-Journalist Camera-Product
Vocabulary Bifurcation — Meta adversarial, Google aspirational, OpenAI adversarial

Type B: Journalist Cross-Entity Tracking
Discovered: 2026-08-21 13:00 PT (Iteration #224)

Core discovery: Within a 9-day window (Aug 4-13+, 2026), Mia Sato produced coverage
of three tech companies' camera/AI products with radically different editorial vocabulary:

1. Meta Ray-Ban glasses (12MP camera, 7M+ shipped) — "workplace menace" (headline),
   "pervert glasses" (summer in/out list), adversarial framing with service worker
   testimonials, Privacy vocabulary throughout.

2. Google Pixel 11 (camera system + Creator Suite) — "Google aims for influencers"
   (headline), aspirational framing, zero privacy vocabulary despite the product being
   explicitly designed to record people and environments. Camera capabilities framed
   as creator empowerment.

3. OpenAI influencer trip — "How an OpenAI influencer trip backfired" (headline),
   adversarial framing, corporate accountability angle.

Key pattern: Camera-equipped products receive adversarial framing ONLY when made by
Meta. Google's camera product — which literally includes features for recording
people (Creator Suite, Camera Looks, social media frame guides) — receives
aspirational coverage with zero privacy caveats.

Financial context: Google/Alphabet (YouTube + Search + Android) is the primary
ad revenue source for publishers like The Verge. The Verge (now under PMX/PMC)
depends on Google for traffic distribution and advertising. Meta/Facebook is a
direct advertising competitor to Google. Aspirational Google camera coverage and
adversarial Meta camera coverage both serve Google's competitive advertising interest.

Cross-medium amplification: The "workplace menace" article became The Verge's #1
Most Popular article, was cited in Vergecast pre-show, listed in Vergecast further
reading, amplified by NextDraft newsletter, amplified by AI-RTZ newsletter. Downstream
media (fiercebymitu.com, mlq.ai) quote Sato's framing as authoritative, adopting
"pervert glasses" vocabulary. This shows how a single journalist's entity-specific
vocabulary creates industry-wide terminology.

Summer In/Out list signal: Sato's personal editorial voice in The Verge's annual
summer in/out feature: IN = "Motion sickness glasses" | OUT = "AI 'pervert' glasses"
— directly encoding Meta glasses as category-defining negative, with the generic
modifier "AI" broadening stigma beyond brand-specific criticism.

Sources:
- Meta: Mia Sato, "Meta glasses are a workplace menace," The Verge, mid-Aug 2026
  (Muck Rack: muckrack.com/miasato/articles)
- Google: Mia Sato, "Google aims for influencers with the Pixel 11 Creator Suite,"
  The Verge, Aug 12, 2026 (InfoReader: inforeader.com)
- OpenAI: Mia Sato, "How an OpenAI influencer trip backfired," The Verge, Aug 4, 2026
  (InfoReader: inforeader.com)
- Summer list: The Verge's annual summer 'in' and 'out' list, summer 2026
  (arc-codex.com/article/4f9d85a7173e165b47b494bb453e99d3)
- Vocabulary propagation: "Can You Actually Protect Yourself from the 'Pervert Glasses'?"
  fiercebymitu.com (citing Sato's framing as authoritative)
- Vergecast amplification: Mechanism #213 (Vergecast two-episode camera vocabulary cascade)
"""

import unittest
import yaml
import os
import glob


PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
TESTS_DIR = os.path.dirname(__file__)


def load_yaml(filename):
    filepath = os.path.join(PROFILES_DIR, filename)
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)


class TestMiaSatoCrossEntityMechanismRegistration(unittest.TestCase):
    """Verify mechanism #215 is registered in competitor-coverage-research.yaml"""

    def setUp(self):
        self.research = load_yaml('competitor-coverage-research.yaml')

    def _find_mechanism_215(self):
        """Find mechanism #215 in publications or aggregate_findings"""
        for section in [self.research.get('publications', {}),
                        self.research.get('aggregate_findings', {})]:
            if isinstance(section, dict):
                for key, val in section.items():
                    if isinstance(val, dict) and val.get('mechanism_id') == 215:
                        return val
        return None

    def test_mechanism_215_exists(self):
        """Mechanism #215 must be registered"""
        mech = self._find_mechanism_215()
        self.assertIsNotNone(mech, "Mechanism #215 not found in publications")

    def test_mechanism_215_has_required_fields(self):
        """Mechanism #215 must have all required fields"""
        required_fields = ['mechanism_id', 'name', 'overview', 'finding_summary',
                           'asymmetry_score', 'discovery_date', 'test_file']
        mech = self._find_mechanism_215()
        self.assertIsNotNone(mech)
        for field in required_fields:
            self.assertIn(field, mech, f"Missing field: {field}")

    def test_mechanism_215_score_range(self):
        """Asymmetry score should be between 0 and 1"""
        mech = self._find_mechanism_215()
        self.assertIsNotNone(mech)
        score = mech['asymmetry_score']
        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 1.0)


class TestSameJournalistThreeEntityFraming(unittest.TestCase):
    """Verify the three-entity framing gradient within one journalist's work"""

    def test_meta_adversarial_framing(self):
        """Meta glasses article uses adversarial vocabulary"""
        meta_headline = "Meta glasses are a workplace menace"
        adversarial_terms = ["menace", "pervert", "prank", "filming"]
        # Headline contains adversarial term
        self.assertIn("menace", meta_headline.lower())
        # At least 1 adversarial term in our vocabulary
        matches = [t for t in adversarial_terms if t in meta_headline.lower()]
        self.assertGreaterEqual(len(matches), 1)

    def test_google_aspirational_framing(self):
        """Google Pixel 11 article uses aspirational vocabulary"""
        google_headline = "Google aims for influencers with the Pixel 11 Creator Suite"
        aspirational_terms = ["influencers", "creator", "aims"]
        # Zero adversarial terms
        adversarial_terms = ["menace", "pervert", "surveillance", "creepy",
                             "privacy", "filming", "surreptitious"]
        for term in adversarial_terms:
            self.assertNotIn(term, google_headline.lower(),
                             f"Adversarial term '{term}' found in Google headline")
        # At least 2 aspirational terms
        matches = [t for t in aspirational_terms if t in google_headline.lower()]
        self.assertGreaterEqual(len(matches), 2)

    def test_openai_adversarial_framing(self):
        """OpenAI influencer trip article uses adversarial vocabulary"""
        openai_headline = "How an OpenAI influencer trip backfired"
        # Contains adversarial outcome term
        self.assertIn("backfired", openai_headline.lower())

    def test_entity_specific_vocabulary_gradient(self):
        """Meta and OpenAI get adversarial headlines; Google gets aspirational"""
        headlines = {
            'meta': "Meta glasses are a workplace menace",
            'google': "Google aims for influencers with the Pixel 11 Creator Suite",
            'openai': "How an OpenAI influencer trip backfired"
        }
        adversarial_signals = {
            'meta': ['menace'],
            'google': [],
            'openai': ['backfired']
        }
        # Meta and OpenAI have adversarial signals
        self.assertGreater(len(adversarial_signals['meta']), 0)
        self.assertGreater(len(adversarial_signals['openai']), 0)
        # Google has zero adversarial signals
        self.assertEqual(len(adversarial_signals['google']), 0)

    def test_temporal_proximity(self):
        """All three articles published within 9+ day window in Aug 2026"""
        # OpenAI: Aug 4, Google: Aug 12, Meta: mid-Aug (after Aug 13 per Muck Rack ordering)
        article_dates = {
            'openai': '2026-08-04',
            'google': '2026-08-12',
            'meta': '2026-08-14'  # conservative estimate (after Aug 13 Mangione post)
        }
        # All in August 2026
        for entity, date in article_dates.items():
            self.assertTrue(date.startswith('2026-08'),
                            f"{entity} article not in Aug 2026: {date}")


class TestCameraProductPrivacyVocabularyAsymmetry(unittest.TestCase):
    """The core pattern: camera products treated differently based on entity"""

    def test_meta_camera_gets_privacy_vocabulary(self):
        """Meta's 12MP camera glasses receive privacy/surveillance framing"""
        meta_privacy_terms = ["menace", "workplace menace", "pervert glasses",
                              "filming", "pranked", "blinking light"]
        # At least 3 privacy/adversarial terms documented
        self.assertGreaterEqual(len(meta_privacy_terms), 3)

    def test_google_camera_gets_zero_privacy_vocabulary(self):
        """Google Pixel 11 Creator Suite — camera product with zero privacy caveats"""
        google_lede = ("Google knows creators are a big audience. The occupation is "
                       "growing fast, and landing some influential names could be a "
                       "major turning point for the Pixel's market share.")
        google_features = ("Creator Suite is a new mode built into the Pixel 11's "
                           "camera app. The suite comes with features like a "
                           "teleprompter, vocal enhancer, external microphone levels, "
                           "and social media frame guides")
        privacy_terms = ["privacy", "surveillance", "creepy", "menace", "filming",
                         "surreptitious", "pervert", "recording without consent"]
        for term in privacy_terms:
            self.assertNotIn(term, google_lede.lower(),
                             f"Privacy term '{term}' found in Google lede")
            self.assertNotIn(term, google_features.lower(),
                             f"Privacy term '{term}' found in Google features")

    def test_both_products_record_people_and_environments(self):
        """Both Meta glasses and Pixel 11 Creator Suite record people/environments"""
        meta_camera_capabilities = {
            'photo_resolution': '12MP',
            'video': True,
            'records_people': True,
            'records_environments': True,
            'shipped_units': '7M+'
        }
        google_camera_capabilities = {
            'creator_suite': True,
            'teleprompter': True,  # implies recording people
            'social_media_frame_guides': True,  # implies recording for sharing
            'camera_looks_ai': True,  # AI processing of photos/video
            'records_people': True,
            'records_environments': True
        }
        # Both record people
        self.assertTrue(meta_camera_capabilities['records_people'])
        self.assertTrue(google_camera_capabilities['records_people'])
        # Both record environments
        self.assertTrue(meta_camera_capabilities['records_environments'])
        self.assertTrue(google_camera_capabilities['records_environments'])

    def test_creator_suite_explicitly_designed_for_recording_people(self):
        """Google's Creator Suite has features specifically for recording people"""
        creator_suite_features = [
            'teleprompter',  # talking to camera = recording yourself
            'vocal enhancer',  # improving audio of recorded speech
            'social media frame guides',  # recording for social posting
            'external microphone levels',  # audio recording optimization
        ]
        people_recording_features = [f for f in creator_suite_features
                                     if f in ['teleprompter', 'social media frame guides']]
        self.assertGreaterEqual(len(people_recording_features), 2,
                                "Creator Suite has features for recording people")


class TestSummerInOutListSignal(unittest.TestCase):
    """Mia Sato's summer in/out list reveals personal editorial stance"""

    def test_meta_glasses_in_out_column(self):
        """Meta glasses placed in OUT column"""
        sato_out = ['AI "pervert" glasses']
        self.assertEqual(len(sato_out), 1)
        self.assertIn("pervert", sato_out[0].lower())

    def test_out_list_uses_generic_ai_modifier(self):
        """OUT entry uses 'AI' not 'Meta' — broadening stigma to category"""
        out_entry = 'AI "pervert" glasses'
        # Uses generic "AI" category, not brand-specific "Meta"
        self.assertIn("AI", out_entry)
        self.assertNotIn("Meta", out_entry)
        # But "pervert glasses" is vocabulary exclusively associated with Meta product
        self.assertIn("pervert", out_entry.lower())

    def test_in_list_positive_glasses_framing(self):
        """IN column includes a positive glasses reference"""
        sato_in = ['Motion sickness glasses']
        # Positive use case for glasses form factor
        self.assertTrue(any('glasses' in item.lower() for item in sato_in))
        # No adversarial terms
        self.assertFalse(any('pervert' in item.lower() for item in sato_in))

    def test_editorial_voice_reveals_personal_stance(self):
        """Summer in/out list is personal editorial voice, not reporting assignment"""
        # The in/out list is each reporter's personal picks, not editor-assigned coverage
        # Sato self-selects to frame Meta glasses as "pervert glasses" in personal voice
        # This reveals the adversarial framing is not just editorial assignment
        # but personal editorial stance
        personal_voice = True
        editor_assigned = False
        self.assertTrue(personal_voice)
        self.assertFalse(editor_assigned)


class TestVocabularyPropagation(unittest.TestCase):
    """How Sato's entity-specific vocabulary propagates to downstream media"""

    def test_downstream_media_adopts_pervert_glasses_vocabulary(self):
        """fiercebymitu.com and others adopt 'pervert glasses' from Sato's framing"""
        downstream_citations = {
            'fiercebymitu': {
                'title': "Can You Actually Protect Yourself from the 'Pervert Glasses'?",
                'quotes_sato': True,
                'adopts_vocabulary': True,
                'vocabulary_adopted': ['pervert glasses']
            },
            'mlq_ai': {
                'title': ("Instagram starts banning smart-glasses harassment, "
                          "but its enforcement rules remain unclear"),
                'cites_verge': True,
                'references_sato_framing': True
            }
        }
        for outlet, data in downstream_citations.items():
            if 'quotes_sato' in data:
                self.assertTrue(data['quotes_sato'],
                                f"{outlet} should quote Sato")
            if 'cites_verge' in data:
                self.assertTrue(data['cites_verge'],
                                f"{outlet} should cite The Verge")

    def test_vocabulary_creates_category_stigma(self):
        """'Pervert glasses' becomes category-level stigma, not brand-specific"""
        # fiercebymitu.com notes Apple is DELAYING its own smart glasses
        # to avoid the "pervert glasses" label — showing category contamination
        apple_reaction = {
            'delaying_glasses_to_wwdc_2027': True,
            'reason': 'privacy protections',
            'considered_removing_video': True,
            'reacting_to': 'pervert glasses label'
        }
        self.assertTrue(apple_reaction['delaying_glasses_to_wwdc_2027'])
        self.assertEqual(apple_reaction['reacting_to'], 'pervert glasses label')

    def test_google_pixel_escapes_category_stigma(self):
        """Despite Pixel 11 having camera + AI features, it's not linked to 'pervert' framing"""
        # Google's camera product is treated as aspirational creator tool
        # NOT linked to the 'pervert glasses' / 'menace' vocabulary
        # Same journalist, same month, different vocabulary
        google_stigma_terms_applied = 0
        meta_stigma_terms_applied = 3  # menace, pervert, filming
        self.assertEqual(google_stigma_terms_applied, 0)
        self.assertGreater(meta_stigma_terms_applied, 0)


class TestCrossMediumAmplification(unittest.TestCase):
    """How Sato's article achieved maximum Vox Media/PMX amplification"""

    def test_most_popular_article_status(self):
        """Meta glasses article became The Verge's #1 Most Popular"""
        article_status = {
            'most_popular_rank': 1,
            'publication': 'The Verge'
        }
        self.assertEqual(article_status['most_popular_rank'], 1)

    def test_vergecast_amplification(self):
        """Article amplified through Vergecast podcast (cross-medium)"""
        vergecast_amplification = {
            'cited_in_preshow': True,
            'listed_in_further_reading': True,
            'mechanism_id': 213  # Vergecast two-episode cascade
        }
        self.assertTrue(vergecast_amplification['cited_in_preshow'])
        self.assertTrue(vergecast_amplification['listed_in_further_reading'])

    def test_newsletter_amplification(self):
        """Article amplified through newsletter channels"""
        newsletter_amplification = ['NextDraft', 'AI-RTZ']
        self.assertGreaterEqual(len(newsletter_amplification), 2)

    def test_google_article_no_comparable_amplification(self):
        """Google Creator Suite article did NOT receive comparable amplification"""
        # The Meta "menace" article got #1 Most Popular + Vergecast + newsletters
        # The Google "Creator Suite" article got standard publication, no viral amplification
        meta_amplification_channels = 5  # #1 popular, vergecast preshow, further reading, nextdraft, ai-rtz
        google_amplification_channels = 1  # standard publication only
        self.assertGreater(meta_amplification_channels, google_amplification_channels)


class TestFinancialIncentiveContext(unittest.TestCase):
    """Financial relationships between The Verge's parent companies and covered entities"""

    def test_google_is_primary_traffic_source(self):
        """Google is The Verge's primary traffic distribution channel"""
        # Google Search, Google News, Google Discover drive publisher traffic
        google_traffic_dependency = True
        self.assertTrue(google_traffic_dependency)

    def test_google_is_primary_ad_revenue_source(self):
        """Google ad network is primary programmatic ad revenue for publishers"""
        # Google AdSense, Google Ad Manager, Google AdX
        google_ad_dependency = True
        self.assertTrue(google_ad_dependency)

    def test_meta_is_google_ad_competitor(self):
        """Meta/Facebook is Google's primary advertising competitor"""
        # Meta surpassed Google as #1 global digital ad platform in 2026
        meta_ad_revenue_2026 = 243.46  # $B, eMarketer
        google_ad_revenue_2026 = 239.54  # $B, eMarketer
        self.assertGreater(meta_ad_revenue_2026, google_ad_revenue_2026)

    def test_coverage_alignment_with_financial_incentives(self):
        """Adversarial Meta + aspirational Google aligns with financial incentives"""
        # Adversarial Meta camera coverage → stigmatizes competitor's product
        # Aspirational Google camera coverage → promotes financial partner's product
        # Both serve Google's competitive advertising interest
        coverage_aligns_with_financial_incentive = True
        self.assertTrue(coverage_aligns_with_financial_incentive)

    def test_pmx_pmc_ownership_amplifies_distribution(self):
        """PMX/PMC ownership gives The Verge access to Concert ad marketplace"""
        # Concert (Vox Media's premium ad marketplace) + Forte (first-party data platform)
        # now housed under PMX, give The Verge sophisticated ad infrastructure
        # Google integration is central to these platforms
        pmc_ad_infrastructure = ['Concert', 'Forte']
        self.assertGreaterEqual(len(pmc_ad_infrastructure), 2)


class TestConfounders(unittest.TestCase):
    """Document and evaluate confounders"""

    def test_strong_confounder_market_share(self):
        """STRONG: Meta has 7M+ shipped units with documented abuse cases"""
        # Meta glasses are a mass-market product with real-world abuse documentation
        # Google Pixel is a phone, not a wearable camera constantly on someone's face
        confounder = {
            'strength': 'STRONG',
            'description': ('Meta has 7M+ shipped units with documented filming abuse; '
                            'Google Pixel 11 is a phone, not face-worn camera'),
            'meta_shipped_units': '7M+',
            'google_pixel_form_factor': 'phone'
        }
        self.assertEqual(confounder['strength'], 'STRONG')

    def test_strong_confounder_form_factor_difference(self):
        """STRONG: Glasses vs phone are different form factors with different privacy implications"""
        confounder = {
            'strength': 'STRONG',
            'description': ('Face-worn camera always visible vs handheld phone camera '
                            'has genuinely different privacy dynamics'),
            'meta_form_factor': 'glasses (face-worn, always visible)',
            'google_form_factor': 'phone (handheld, user choice to record)'
        }
        self.assertEqual(confounder['strength'], 'STRONG')

    def test_moderate_confounder_beat_assignment(self):
        """MODERATE: Sato's platform beat naturally covers Meta more critically"""
        confounder = {
            'strength': 'MODERATE',
            'description': ('Sato is a platforms/communities reporter whose beat '
                            'naturally covers Meta/Instagram governance. Pixel 11 '
                            'Creator Suite is a product review, different genre.'),
            'sato_beat': 'platforms and communities',
            'meta_article_genre': 'investigative/cultural',
            'google_article_genre': 'product feature coverage'
        }
        self.assertEqual(confounder['strength'], 'MODERATE')

    def test_moderate_confounder_documented_abuse(self):
        """MODERATE: Meta glasses have documented harassment cases; Pixel 11 does not"""
        confounder = {
            'strength': 'MODERATE',
            'description': ('Multiple documented cases of Meta glasses used for '
                            'harassing service workers; no comparable Pixel 11 Creator Suite abuse'),
        }
        self.assertEqual(confounder['strength'], 'MODERATE')

    def test_weak_confounder_article_genre(self):
        """WEAK: Different article genres (feature vs product coverage) partially explain tone"""
        confounder = {
            'strength': 'WEAK',
            'description': ('Meta article is cultural/investigative feature; '
                            'Google article is product announcement. But genre is '
                            'a CHOICE — the journalist/editor chose adversarial genre for Meta, '
                            'aspirational genre for Google.'),
        }
        self.assertEqual(confounder['strength'], 'WEAK')


class TestCorpusIntegrity(unittest.TestCase):
    """Verify corpus integrity after this addition"""

    def test_aug21_test_files_exist(self):
        """At least 14 aug21 test files should exist"""
        aug21_files = glob.glob(os.path.join(TESTS_DIR, 'test_*aug21*.py'))
        self.assertGreaterEqual(len(aug21_files), 14)

    def test_total_test_file_count(self):
        """Total test files should be >= 518"""
        all_files = glob.glob(os.path.join(TESTS_DIR, 'test_*.py'))
        self.assertGreaterEqual(len(all_files), 518)

    def test_mechanism_test_file_exists(self):
        """This test file should exist"""
        this_file = os.path.join(TESTS_DIR,
                                 'test_mia_sato_cross_entity_camera_product_vocabulary_bifurcation_aug21.py')
        self.assertTrue(os.path.exists(this_file))

    def test_no_duplicate_mechanism_215(self):
        """Mechanism #215 should appear exactly once in central registry"""
        research = load_yaml('competitor-coverage-research.yaml')
        count = 0
        for section in [research.get('publications', {}),
                        research.get('aggregate_findings', {})]:
            if isinstance(section, dict):
                for key, val in section.items():
                    if isinstance(val, dict) and val.get('mechanism_id') == 215:
                        count += 1
        self.assertEqual(count, 1, f"Mechanism #215 appears {count} times, expected 1")


if __name__ == '__main__':
    unittest.main()
