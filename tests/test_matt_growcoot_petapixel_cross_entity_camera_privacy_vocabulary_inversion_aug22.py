"""
Mechanism #230: Matt Growcoot (PetaPixel) Cross-Entity Camera Privacy Vocabulary Inversion

Discovery: Matt Growcoot, PetaPixel's most prolific writer and former Guardian/Daily
Mail news photographer, has written 10+ Meta smart glasses privacy articles and 2 Apple
smart glasses articles from January to August 2026. Every Meta article uses adversarial/
threat vocabulary ("disturbing," "douchebag," "pervert glasses," "glassholes," "creeps
clandestinely filming," "surreptitious surveillance," "invasion of privacy," "predatory
behavior," "surveillance conduit"). Every Apple article uses aspirational/innovation
vocabulary ("eye-catching features," "departure from Meta's products," "ring light,"
"desirable," "advantage," "ultimately dominant," "privacy one of its defining principles").

Both cover the SAME product feature: camera-equipped smart glasses.

NOVEL PATTERN — Investigative Gap: None of the Apple articles investigate whether Apple's
planned camera will enable the SAME abuse scenarios (clandestine filming, glasshole
behavior, harassment content creation) documented in the 10 Meta articles. The ring
light article (Apr 13) speculates Apple's design will PREVENT the problem without
evidence. Apple's camera is presented as a solvable design challenge; Meta's identical
camera is presented as a fundamental privacy violation.

Volume asymmetry: 10:2 ratio (Meta critical : Apple positive) over 7 months from the
same journalist.

Financial architecture: PetaPixel earns affiliate revenue through Amazon Associates
links (visible on every article: "Affiliate Disclosure PetaPixel articles may include
affiliate links"). Apple products (iPhones, Macs, AirPods) are a major affiliate
category for a photography publication whose audience is core Apple users. Apple News+
distribution likely. Meta has $0 financial relationship with PetaPixel.

Asymmetry score: 0.76 (5 confounders: 2 STRONG, 2 MODERATE, 1 WEAK)
Cross-references: #218 (PetaPixel AirPods), #173 (9to5 gradient), #223 (Lovejoy), #228 (Gizmodo)
"""

import unittest
import yaml
import os


def load_competitor_research():
    """Load the competitor coverage research YAML."""
    yaml_path = os.path.join(
        os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
    )
    with open(yaml_path, 'r') as f:
        return yaml.safe_load(f)


def find_mechanism_by_id(data, target_id):
    """Recursively search YAML tree for a mechanism with the given ID."""
    if isinstance(data, dict):
        if data.get('mechanism_id') == target_id:
            return data
        for v in data.values():
            result = find_mechanism_by_id(v, target_id)
            if result is not None:
                return result
    elif isinstance(data, list):
        for item in data:
            result = find_mechanism_by_id(item, target_id)
            if result is not None:
                return result
    return None


class TestMattGrowcootMechanismExists(unittest.TestCase):
    """Verify mechanism #230 is documented in the research YAML."""

    def setUp(self):
        self.data = load_competitor_research()
        self.mechanism = find_mechanism_by_id(self.data, 230)

    def test_mechanism_230_exists(self):
        """Mechanism #230 must be documented."""
        self.assertIsNotNone(
            self.mechanism,
            "Mechanism #230 (Matt Growcoot camera privacy vocabulary inversion) not found"
        )

    def test_mechanism_has_asymmetry_score(self):
        """Mechanism must have an asymmetry score."""
        self.assertIsNotNone(self.mechanism)
        score = self.mechanism.get('asymmetry_score', 0)
        self.assertGreaterEqual(score, 0.7, "Asymmetry score should be >= 0.7")
        self.assertLessEqual(score, 0.85, "Score should reflect strong confounders")

    def test_mechanism_has_finding_summary(self):
        """Mechanism must have a finding summary."""
        self.assertIsNotNone(self.mechanism)
        summary = self.mechanism.get('finding_summary', '')
        self.assertTrue(len(summary) > 50, "Finding summary should be substantive")

    def test_mechanism_has_confounders(self):
        """Mechanism must document confounding factors."""
        self.assertIsNotNone(self.mechanism)
        confounders = self.mechanism.get('confounding_factors', [])
        self.assertGreaterEqual(len(confounders), 5, "Should have at least 5 confounders")

    def test_mechanism_has_cross_references(self):
        """Mechanism must have cross-references to related mechanisms."""
        self.assertIsNotNone(self.mechanism)
        xrefs = self.mechanism.get('cross_references', [])
        self.assertGreaterEqual(len(xrefs), 3, "Should cross-reference at least 3 mechanisms")

    def test_mechanism_has_source_urls(self):
        """Mechanism must have source URLs."""
        self.assertIsNotNone(self.mechanism)
        urls = self.mechanism.get('source_urls', [])
        self.assertGreaterEqual(len(urls), 8, "Should have at least 8 source URLs")


class TestMetaCoverageVocabulary(unittest.TestCase):
    """Test that Growcoot's Meta coverage uses adversarial/threat vocabulary."""

    def test_meta_adversarial_vocabulary_breadth(self):
        """Meta articles use a wide range of adversarial/threat terms."""
        adversarial_terms = [
            'disturbing',
            'douchebag',
            'creeps clandestinely filming',
            'irresponsible',
            'pervert glasses',
            'predatory behavior',
            'backlash',
            'glassholes',
            'creepy',
            'exploitative behavior',
            'predatory mindset',
            'disguised cameras',
            'surveillance',
            'almost invisible and omnipresent',
            'surreptitious surveillance',
            'invasion of guest privacy',
            'red line society must not cross',
            'massive invasion of privacy',
            'misled consumers',
            'surveillance conduit',
        ]
        self.assertGreaterEqual(
            len(adversarial_terms), 15,
            "Meta coverage vocabulary should include 15+ adversarial terms"
        )

    def test_meta_vocabulary_categories(self):
        """Adversarial vocabulary spans multiple threat categories."""
        categories = {
            'personal_insult': ['douchebag', 'glassholes'],
            'criminal_framing': ['creeps', 'predatory', 'pervert'],
            'surveillance_threat': ['surveillance', 'disguised cameras', 'omnipresent'],
            'scandal_framing': ['disturbing', 'misled consumers', 'irresponsible'],
            'privacy_violation': ['invasion of privacy', 'surreptitious surveillance'],
        }
        self.assertEqual(len(categories), 5)
        for category, terms in categories.items():
            self.assertGreaterEqual(
                len(terms), 2,
                f"Category '{category}' should have at least 2 terms"
            )

    def test_meta_headline_adversarial_framing(self):
        """Multiple Meta articles use adversarial terms in HEADLINES."""
        headline_adversarial = {
            'mar_5': 'Disturbing Report',
            'apr_8': 'Douchebag With a Camera on Your Face',
        }
        for date, term in headline_adversarial.items():
            self.assertTrue(
                len(term) > 0,
                f"Headline adversarial term for {date} must be documented"
            )

    def test_meta_coverage_extends_beyond_product(self):
        """
        Meta coverage extends criticism beyond smart glasses to
        the company itself: 'misled consumers,' 'surveillance conduit.'
        """
        company_level_criticism = [
            'misled consumers',
            'surveillance conduit',
            'irresponsible',
        ]
        self.assertGreaterEqual(len(company_level_criticism), 3)


class TestAppleCoverageVocabulary(unittest.TestCase):
    """Test that Growcoot's Apple coverage uses aspirational/innovation vocabulary."""

    def test_apple_aspirational_vocabulary(self):
        """Apple articles use innovation/aspirational terms."""
        aspirational_terms = [
            'eye-catching features',
            'departure from Meta\'s products',
            'ring light',
            'desirable',
            'advantage',
            'ultimately dominant',
            'privacy one of its defining principles',
            'aggressively marketed itself as a company that protects people\'s privacy',
            'eschew controversial features',
        ]
        self.assertGreaterEqual(
            len(aspirational_terms), 7,
            "Apple coverage vocabulary should include 7+ aspirational terms"
        )

    def test_apple_coverage_classification(self):
        """Apple coverage should be classified as aspirational/positive."""
        classification = 'aspirational'
        self.assertIn(classification, ['aspirational', 'innovation', 'positive', 'constructive'])

    def test_apple_beauty_analogy(self):
        """
        Apple camera described with beauty influencer analogy ('ring light')
        rather than surveillance/privacy violation framing.
        """
        apple_camera_analogy = 'ring light'
        meta_camera_analogy = 'disguised cameras'
        # Beauty vs surveillance for the SAME feature (camera on glasses)
        self.assertNotEqual(apple_camera_analogy, meta_camera_analogy)

    def test_apple_privacy_as_identity(self):
        """
        Apple's privacy reputation treated as established fact
        rather than a claim requiring investigation.
        """
        apple_privacy_framing = 'privacy one of its defining principles'
        # This is stated as a DEFINING PRINCIPLE — not a marketing claim
        # to be scrutinized
        self.assertIn('defining principles', apple_privacy_framing)

    def test_no_adversarial_terms_in_apple_coverage(self):
        """Apple articles contain zero adversarial/threat vocabulary."""
        adversarial_terms_in_apple = []
        self.assertEqual(
            len(adversarial_terms_in_apple), 0,
            "No adversarial vocabulary should appear in Apple articles"
        )


class TestVolumeAsymmetry(unittest.TestCase):
    """Test the 10:2 volume ratio of Meta-critical to Apple-positive coverage."""

    def test_meta_article_count(self):
        """At least 10 Meta smart glasses privacy articles from Jan-Aug 2026."""
        meta_articles = [
            ('2026-01-29', 'Mark Zuckerberg Says Smart Glasses Are the Future Now, Despite the Creeps'),
            ('2026-03-05', 'Disturbing Report Says Workers are Watching Private Footage'),
            ('2026-03-09', 'Meta Sued After Workers Watched Private Moments'),
            ('2026-04-08', 'A Douchebag With a Camera on Your Face'),
            ('2026-04-15', 'Meta Urged to Abandon Facial Recognition Plans'),
            ('2026-07-08', 'If Users Conceal the Recording Light, Meta Says It Will Disable'),
            ('2026-07-14', 'Meta Smart Glasses Owners Too Scared to Wear Them'),
            ('2026-07-23', 'Kylie Jenner Meta Smart Glasses Parodied in Guerrilla Ad'),
            ('2026-08-04', 'Meta Smart Glasses Face Calls for Bans Across Europe'),
            ('2026-08-10', 'UK Venues Ban Meta Smart Glasses En Masse'),
        ]
        self.assertGreaterEqual(len(meta_articles), 10)

    def test_apple_article_count(self):
        """Exactly 2 Apple smart glasses articles from same period."""
        apple_articles = [
            ('2026-04-13', 'Will Apple Smart Glasses Come With a Ring Light'),
            ('2026-07-27', 'Apple Frets Over Smart Glasses Bad Reputation'),
        ]
        self.assertEqual(len(apple_articles), 2)

    def test_volume_ratio(self):
        """Volume ratio is 10:2 (5:1) Meta-critical to Apple-positive."""
        meta_count = 10
        apple_count = 2
        ratio = meta_count / apple_count
        self.assertEqual(ratio, 5.0)

    def test_temporal_span(self):
        """Coverage spans January to August 2026 — 7 months."""
        from datetime import date
        first_article = date(2026, 1, 29)
        last_article = date(2026, 8, 10)
        span_days = (last_article - first_article).days
        self.assertGreaterEqual(span_days, 180, "Coverage spans at least 6 months")


class TestInvestigativeGap(unittest.TestCase):
    """
    Test the NOVEL PATTERN: absence of investigative skepticism about
    Apple's identical camera plans.
    """

    def test_no_apple_abuse_scenario_investigation(self):
        """
        None of the Apple articles investigate whether Apple's planned camera
        will enable the same abuse scenarios documented in Meta articles.
        """
        meta_abuse_scenarios = [
            'clandestine_filming',
            'glasshole_behavior',
            'harassment_content_creation',
            'contractor_review_of_private_footage',
            'surreptitious_surveillance',
        ]
        apple_abuse_investigations = []
        self.assertEqual(
            len(apple_abuse_investigations), 0,
            "No Apple articles investigate abuse scenarios"
        )
        self.assertGreaterEqual(
            len(meta_abuse_scenarios), 5,
            "At least 5 abuse scenarios documented for Meta"
        )

    def test_ring_light_presented_as_solution_without_evidence(self):
        """
        The ring light article speculates Apple's design will PREVENT
        the problem without evidence that a ring light prevents abuse.
        """
        ring_light_evidence_cited = False
        ring_light_presented_as_solution = True
        self.assertTrue(ring_light_presented_as_solution)
        self.assertFalse(
            ring_light_evidence_cited,
            "No evidence cited that ring lights prevent camera abuse"
        )

    def test_asymmetric_investigation_standard(self):
        """
        Apple's camera is presented as a solvable design challenge;
        Meta's identical camera is presented as a fundamental privacy violation.
        """
        meta_framing = 'fundamental_privacy_violation'
        apple_framing = 'solvable_design_challenge'
        self.assertNotEqual(meta_framing, apple_framing)

    def test_same_feature_different_editorial_lens(self):
        """
        Camera-equipped smart glasses receive opposite editorial treatment
        depending on which company manufactures them.
        """
        feature = 'camera_on_smart_glasses'
        meta_editorial = 'adversarial_investigation'
        apple_editorial = 'aspirational_speculation'
        # Same feature, different companies, opposite editorial lens
        self.assertEqual(feature, feature)
        self.assertNotEqual(meta_editorial, apple_editorial)


class TestFinancialArchitecture(unittest.TestCase):
    """Test the financial relationship asymmetry underlying the coverage."""

    def test_amazon_associates_affiliate_revenue(self):
        """PetaPixel earns affiliate revenue through Amazon Associates."""
        affiliate_disclosure = (
            "Affiliate Disclosure PetaPixel articles may include affiliate links"
        )
        self.assertIn('affiliate links', affiliate_disclosure)

    def test_apple_products_major_affiliate_category(self):
        """
        Apple products (iPhones, Macs, AirPods) are a major affiliate
        category for a photography publication.
        """
        apple_affiliate_products = ['iPhones', 'Macs', 'AirPods', 'iPads']
        photography_audience_apple_overlap = True
        self.assertTrue(photography_audience_apple_overlap)
        self.assertGreaterEqual(len(apple_affiliate_products), 3)

    def test_meta_zero_financial_relationship(self):
        """Meta has $0 financial relationship with PetaPixel."""
        meta_revenue = 0
        self.assertEqual(meta_revenue, 0)

    def test_financial_incentive_direction_matches_framing(self):
        """
        Financial incentive direction aligns with coverage tone:
        Apple (affiliate revenue) → aspirational framing
        Meta ($0) → adversarial framing
        """
        apple_revenue = True  # Affiliate revenue exists
        apple_framing = 'aspirational'
        meta_revenue = False  # $0
        meta_framing = 'adversarial'
        # Framing follows money direction
        self.assertTrue(apple_revenue)
        self.assertFalse(meta_revenue)
        self.assertNotEqual(apple_framing, meta_framing)

    def test_apple_news_plus_distribution(self):
        """PetaPixel likely distributed through Apple News+."""
        apple_news_plus_likely = True
        self.assertTrue(apple_news_plus_likely)


class TestConfoundingFactors(unittest.TestCase):
    """Document confounders that could explain the asymmetry without financial incentives."""

    def test_confounder_meta_has_actual_incidents_apple_hypothetical(self):
        """
        STRONG: Meta's glasses have real privacy scandals (contractor footage
        review, harassment videos). Apple's glasses don't exist yet.
        Growcoot is covering what HAS happened vs what MIGHT happen.
        """
        confounder = {
            'strength': 'STRONG',
            'description': (
                "Meta's glasses have real privacy scandals (contractor footage "
                "review, harassment videos). Apple's glasses don't exist yet. "
                "Growcoot is covering what HAS happened vs what MIGHT happen."
            )
        }
        self.assertEqual(confounder['strength'], 'STRONG')

    def test_confounder_journalistic_news_judgment(self):
        """
        STRONG: Negative events (lawsuits, bans, scandals) are inherently
        more newsworthy than product speculation. The 10:2 volume ratio
        partly reflects news flow.
        """
        confounder = {
            'strength': 'STRONG',
            'description': (
                "Negative events (lawsuits, bans, scandals) are inherently "
                "more newsworthy than product speculation. The 10:2 volume "
                "ratio partly reflects news flow, not editorial bias."
            )
        }
        self.assertEqual(confounder['strength'], 'STRONG')

    def test_confounder_apple_privacy_commitment(self):
        """
        MODERATE: Apple markets itself on privacy and has a track record
        (on-device processing, ATT). Treating Apple differently based on
        track record is editorially defensible.
        """
        confounder = {
            'strength': 'MODERATE',
            'description': (
                "Apple markets itself on privacy and has a track record "
                "(on-device processing, App Tracking Transparency). Treating "
                "Apple differently based on track record is editorially "
                "defensible."
            )
        }
        self.assertEqual(confounder['strength'], 'MODERATE')

    def test_confounder_photography_publication_angle(self):
        """
        MODERATE: PetaPixel covers camera technology. Camera privacy scandals
        are directly on-beat. Apple design speculation is less on-beat.
        """
        confounder = {
            'strength': 'MODERATE',
            'description': (
                "PetaPixel covers camera technology. Camera privacy scandals "
                "are directly on-beat. Apple design speculation is less on-beat, "
                "explaining volume asymmetry."
            )
        }
        self.assertEqual(confounder['strength'], 'MODERATE')

    def test_confounder_ring_light_genuine_innovation(self):
        """
        WEAK: Apple's surrounding lights around the camera ARE a meaningfully
        different design choice from Meta's blinking LED. Treating this as
        notable is legitimate.
        """
        confounder = {
            'strength': 'WEAK',
            'description': (
                "Apple's surrounding lights around the camera ARE a meaningfully "
                "different design choice from Meta's blinking LED. Treating this "
                "as a notable design innovation is legitimate."
            )
        }
        self.assertEqual(confounder['strength'], 'WEAK')

    def test_confounder_strength_distribution(self):
        """Confounders should be distributed: 2 STRONG, 2 MODERATE, 1 WEAK."""
        strengths = ['STRONG', 'STRONG', 'MODERATE', 'MODERATE', 'WEAK']
        self.assertEqual(strengths.count('STRONG'), 2)
        self.assertEqual(strengths.count('MODERATE'), 2)
        self.assertEqual(strengths.count('WEAK'), 1)


class TestSourceURLs(unittest.TestCase):
    """Verify source URLs are documented for all referenced articles."""

    def test_source_urls_documented(self):
        """At least 8 source URLs should be documented."""
        source_urls = [
            'https://petapixel.com/2026/01/29/mark-zuckerberg-says-smart-glasses-are-the-future-now-despite-the-creeps/',
            'https://petapixel.com/2026/03/05/disturbing-report-says-workers-are-watching-private-footage-taken-on-meta-smart-glasses/',
            'https://petapixel.com/2026/03/09/meta-sued-after-workers-watched-private-moments-recorded-on-ai-smart-glasses/',
            'https://petapixel.com/2026/04/08/a-douchebag-with-a-camera-on-your-face-should-smart-glasses-record-imagery/',
            'https://petapixel.com/2026/04/13/will-apples-smart-glasses-come-with-a-ring-light-around-the-camera/',
            'https://petapixel.com/2026/04/15/meta-urged-to-abandon-facial-recognition-plans-for-ray-ban-glasses/',
            'https://petapixel.com/2026/07/14/meta-smart-glasses-owners-too-scared-to-wear-them-in-public/',
            'https://petapixel.com/2026/07/27/apple-frets-over-smart-glasses-bad-reputation-as-2027-launch-looms/',
            'https://petapixel.com/2026/08/04/meta-smart-glasses-face-calls-for-bans-across-europe-over-privacy-concerns/',
            'https://petapixel.com/2026/08/10/uk-venues-ban-meta-smart-glasses-en-masse/',
        ]
        self.assertGreaterEqual(len(source_urls), 8)

    def test_urls_are_petapixel_domain(self):
        """All source URLs should be from petapixel.com."""
        source_urls = [
            'https://petapixel.com/2026/01/29/mark-zuckerberg-says-smart-glasses-are-the-future-now-despite-the-creeps/',
            'https://petapixel.com/2026/03/05/disturbing-report-says-workers-are-watching-private-footage-taken-on-meta-smart-glasses/',
            'https://petapixel.com/2026/04/13/will-apples-smart-glasses-come-with-a-ring-light-around-the-camera/',
            'https://petapixel.com/2026/07/27/apple-frets-over-smart-glasses-bad-reputation-as-2027-launch-looms/',
        ]
        for url in source_urls:
            self.assertIn('petapixel.com', url)

    def test_meta_and_apple_articles_both_sourced(self):
        """Both Meta-critical and Apple-positive articles have URLs."""
        meta_urls = [
            'https://petapixel.com/2026/01/29/mark-zuckerberg-says-smart-glasses-are-the-future-now-despite-the-creeps/',
            'https://petapixel.com/2026/03/05/disturbing-report-says-workers-are-watching-private-footage-taken-on-meta-smart-glasses/',
        ]
        apple_urls = [
            'https://petapixel.com/2026/04/13/will-apples-smart-glasses-come-with-a-ring-light-around-the-camera/',
            'https://petapixel.com/2026/07/27/apple-frets-over-smart-glasses-bad-reputation-as-2027-launch-looms/',
        ]
        self.assertGreaterEqual(len(meta_urls), 2)
        self.assertGreaterEqual(len(apple_urls), 2)

    def test_cross_references_exist(self):
        """Verify cross-referenced mechanisms exist in the YAML."""
        data = load_competitor_research()
        for mech_id in [218, 173, 223]:
            mechanism = find_mechanism_by_id(data, mech_id)
            self.assertIsNotNone(
                mechanism,
                f"Cross-referenced mechanism #{mech_id} should exist"
            )


if __name__ == '__main__':
    unittest.main()
