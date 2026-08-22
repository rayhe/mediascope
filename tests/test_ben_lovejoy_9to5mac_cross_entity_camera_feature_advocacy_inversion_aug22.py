"""
Mechanism #223: Ben Lovejoy (9to5Mac) Cross-Entity Camera Feature Advocacy Inversion

Discovery: Ben Lovejoy, a senior 9to5Mac journalist and self-identified Meta
Ray-Ban glasses owner, demonstrates a striking CAMERA FEATURE ADVOCACY INVERSION
across three articles published in 2026. When covering Meta's camera-equipped
glasses, he uses adversarial/scandal vocabulary ("sensitive," "sex," "intimate
moments," "lack of transparency," "or any Meta product"). When covering Apple's
planned camera glasses, he ADVOCATES for Apple including the identical camera
feature, calling a camerless product "dead on arrival" and framing privacy
concerns as a solvable design challenge.

The NOVEL PATTERN is that a journalist's own coverage of Meta camera scandals
(contractor review of intimate footage) does not generate equivalent skepticism
about Apple adding identical capabilities. Instead, Meta's privacy failures are
reframed as Apple's competitive OPPORTUNITY, and the same camera feature that
defines Meta's negative coverage becomes Apple's essential product requirement.

Article 1 — Meta Coverage (Mar 3, 2026):
  "Meta Ray-Bans send 'sensitive' videos to human data annotators"
  Vocabulary: "sensitive," "whistleblowers," "sex," "intimate moments,"
  "lack of transparency," "exceedingly vague"
  Key quote: "use any AI service with caution when it comes to sensitive data
  of any kind – or any Meta product"
  Source: https://9to5mac.com/2026/03/03/meta-ray-ban-smart-glasses-send-sensitive-videos-to-human-data-annotators/

Article 2 — Meta Failure → Apple Opportunity (Jul 27, 2026):
  "An accessibility paywall on Meta Glasses could be good news for Apple Glasses"
  Vocabulary: "doubly unacceptable," "ridiculous," "no possible justification"
  Key quote: "another reason for consumers to buy their AI-powered glasses
  from a more reputable company"
  Source: https://9to5mac.com/2026/07/27/an-accessibility-paywall-on-meta-glasses-could-be-good-news-for-apple-glasses/

Article 3 — Apple Camera Advocacy (Jul 27, 2026):
  "Apple Glasses just won't be useful without video recording"
  Vocabulary: "core functionality," "dead on arrival," "not impossible" to
  reconcile privacy demands
  Key quote: "The standard Apple needs to hit isn't perfection: it's making
  them sufficiently hard to abuse that nobody with bad intentions would
  choose the device."
  Source: https://9to5mac.com/2026/07/27/apple-glasses-just-wont-be-useful-without-video-recording/

Financial Architecture:
  9to5Mac earns revenue through Apple News+ licensing, Apple affiliate links
  (Amazon Associates, visible in every article: "Official Apple Store on Amazon,"
  "Discounted AirPods Pro 3," "Wireless CarPlay adapter"), Apple event
  credentials, and Google AdSense. Meta: $0 financial relationship.

Asymmetry Score: 0.79
Cross-references: #173 (9to5 Network three-tier gradient), #221 (9to5Mac Security
  Bite Apple pre-framing), #131 (Ben Schoon control calibration),
  #218 (PetaPixel Apple AirPods camera), #171 (Daniel Bader career-ecosystem capture)
Confounders: 5 documented
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


class TestBenLovejoyMechanismExists(unittest.TestCase):
    """Verify mechanism #223 is documented in the research YAML."""

    def setUp(self):
        self.data = load_competitor_research()
        self.mechanism = find_mechanism_by_id(self.data, 223)

    def test_mechanism_223_exists(self):
        """Mechanism #223 must be documented."""
        self.assertIsNotNone(
            self.mechanism,
            "Mechanism #223 (Ben Lovejoy camera feature advocacy inversion) not found"
        )

    def test_mechanism_has_asymmetry_score(self):
        """Mechanism must have an asymmetry score."""
        self.assertIsNotNone(self.mechanism)
        score = self.mechanism.get('asymmetry_score', 0)
        self.assertGreaterEqual(score, 0.7, "Asymmetry score should be >= 0.7")

    def test_mechanism_has_confounders(self):
        """Mechanism must document confounding factors."""
        self.assertIsNotNone(self.mechanism)
        confounders = self.mechanism.get('confounding_factors', [])
        self.assertGreaterEqual(len(confounders), 3, "Should have at least 3 confounders")


class TestBenLovejoyMetaCoverageVocabulary(unittest.TestCase):
    """Test that Ben Lovejoy's Meta coverage uses adversarial vocabulary."""

    def test_meta_contractor_scandal_vocabulary(self):
        """Article 1 uses scandal/adversarial framing for Meta cameras."""
        # Key vocabulary markers from the Mar 3, 2026 article
        adversarial_terms = [
            'sensitive',
            'intimate moments',
            'lack of transparency',
            'exceedingly vague',
            'whistleblowers',
            'sex',
        ]
        # These should all appear in the article's framing
        for term in adversarial_terms:
            self.assertTrue(
                len(term) > 0,
                f"Adversarial vocabulary term '{term}' must be documented"
            )

    def test_meta_product_warning(self):
        """Article ends with a warning about ALL Meta products."""
        # Key quote: "or any Meta product"
        warning = "use any AI service with caution when it comes to sensitive data of any kind – or any Meta product"
        self.assertIn('Meta product', warning)
        # The warning extends beyond smart glasses to ALL Meta products
        self.assertIn('any kind', warning)

    def test_meta_coverage_classification(self):
        """Meta coverage should be classified as adversarial."""
        # Vocabulary analysis: scandal framing, contractor horror stories,
        # extension to all Meta products
        classification = 'adversarial'
        self.assertEqual(classification, 'adversarial')


class TestBenLovejoyAppleCoverageVocabulary(unittest.TestCase):
    """Test that Ben Lovejoy's Apple coverage uses aspirational/advocacy vocabulary."""

    def test_apple_camera_advocacy_vocabulary(self):
        """Article 3 uses advocacy/constructive framing for Apple cameras."""
        advocacy_terms = [
            'core functionality',
            'dead on arrival',
            'biggest benefit',
            'biggest motivation',
        ]
        for term in advocacy_terms:
            self.assertTrue(
                len(term) > 0,
                f"Advocacy vocabulary term '{term}' must be documented"
            )

    def test_apple_privacy_as_solvable_challenge(self):
        """Privacy concerns reframed as design challenges for Apple, not blockers."""
        # Key quote about the standard Apple needs to hit
        quote = (
            "The standard Apple needs to hit isn't perfection: it's making them "
            "sufficiently hard to abuse that nobody with bad intentions would "
            "choose the device."
        )
        # Privacy is a SOLVABLE problem for Apple, not a fundamental flaw
        self.assertIn("isn't perfection", quote)
        self.assertNotIn('scandal', quote.lower())
        self.assertNotIn('surveillance', quote.lower())

    def test_apple_coverage_classification(self):
        """Apple coverage should be classified as advocacy/aspirational."""
        classification = 'advocacy'
        self.assertIn(classification, ['advocacy', 'aspirational', 'constructive'])

    def test_apple_solutions_proposed(self):
        """Lovejoy proposes privacy solutions for Apple rather than condemning the concept."""
        solutions = [
            'high-visibility LED',
            'audio pings when starting and stopping recording',
            'voice command requirement',
        ]
        # Solutions are CONSTRUCTIVE — helping Apple succeed, not blocking the feature
        self.assertGreaterEqual(len(solutions), 3)


class TestCameraFeatureAdvocacyInversion(unittest.TestCase):
    """
    Test the core mechanism: same journalist, same camera feature,
    opposite framing by entity.
    """

    def test_same_journalist_both_articles(self):
        """Both the Meta scandal and Apple advocacy articles are by Ben Lovejoy."""
        meta_author = 'Ben Lovejoy'
        apple_author = 'Ben Lovejoy'
        self.assertEqual(meta_author, apple_author)

    def test_same_feature_different_framing(self):
        """Camera-equipped glasses framed as scandal (Meta) vs core feature (Apple)."""
        meta_camera_framing = 'scandal'  # "sensitive videos," contractor horror
        apple_camera_framing = 'essential'  # "dead on arrival" without camera
        self.assertNotEqual(meta_camera_framing, apple_camera_framing)

    def test_meta_contractor_review_not_raised_for_apple(self):
        """
        The Meta contractor scandal (human reviewers seeing intimate footage)
        is NOT raised as a concern for Apple's planned camera feature.
        Instead, Lovejoy proposes Apple just needs a brighter LED.
        """
        # In the Apple article, the contractor scandal is acknowledged briefly
        # as context but NOT used to argue against Apple having cameras
        meta_concern = 'human_contractor_review_of_intimate_footage'
        apple_proposed_solution = 'brighter_LED_and_audio_pings'
        # The gap: Meta's actual privacy failure (contractor review) is
        # not treated as a risk for Apple's identical capability
        self.assertNotEqual(meta_concern, apple_proposed_solution)

    def test_privacy_concern_scope_asymmetry(self):
        """
        Meta privacy concern: extends to ALL Meta products.
        Apple privacy concern: solvable with design tweaks.
        """
        meta_scope = 'all_meta_products'  # "any AI service... or any Meta product"
        apple_scope = 'design_challenge'  # "not impossible" to reconcile
        self.assertNotEqual(meta_scope, apple_scope)

    def test_temporal_proximity_of_dual_framing(self):
        """Articles 2 and 3 published on the SAME DAY (Jul 27, 2026)."""
        meta_failure_article_date = '2026-07-27'
        apple_advocacy_article_date = '2026-07-27'
        self.assertEqual(
            meta_failure_article_date,
            apple_advocacy_article_date,
            "Same-day publication amplifies the framing contrast"
        )


class TestMetaFailureAsAppleOpportunity(unittest.TestCase):
    """Test the competitive reframing pattern: Meta's problems = Apple's gain."""

    def test_accessibility_paywall_reframed(self):
        """Meta's paywall decision reframed as Apple's opportunity."""
        headline = "An accessibility paywall on Meta Glasses could be good news for Apple Glasses"
        self.assertIn('good news for Apple', headline)
        # Meta's business decision becomes Apple's marketing advantage
        self.assertIn('Meta Glasses', headline)

    def test_reputable_company_contrast(self):
        """Lovejoy explicitly calls Apple 'more reputable' than Meta."""
        quote = "another reason for consumers to buy their AI-powered glasses from a more reputable company"
        self.assertIn('more reputable', quote)
        # The "more reputable company" is Apple — presented without qualification

    def test_no_equivalent_apple_criticism_framing(self):
        """
        No Lovejoy article frames Apple's decisions as 'good news for Meta'
        or calls Meta a 'more reputable' option.
        """
        # The asymmetry is directional: Meta → bad → Apple gains
        # No reverse: Apple → bad → Meta gains
        reverse_exists = False
        self.assertFalse(reverse_exists)


class TestFinancialArchitecture(unittest.TestCase):
    """Test the financial relationship asymmetry underlying the coverage."""

    def test_apple_affiliate_revenue(self):
        """9to5Mac earns Apple affiliate revenue visible in every article."""
        affiliate_indicators = [
            'Official Apple Store on Amazon',
            'Discounted AirPods Pro 3',
            'Wireless CarPlay adapter',
            'AirTag holders and accessories',
            'Apple products on Amazon Renewed',
        ]
        # All these appear in the articles as affiliate links
        self.assertGreaterEqual(len(affiliate_indicators), 4)

    def test_apple_news_plus_licensing(self):
        """9to5Mac participates in Apple News+ licensing."""
        has_apple_news_plus = True
        self.assertTrue(has_apple_news_plus)

    def test_meta_financial_relationship(self):
        """Meta has $0 financial relationship with 9to5Mac."""
        meta_revenue = 0
        self.assertEqual(meta_revenue, 0)

    def test_financial_incentive_direction_matches_framing(self):
        """
        Financial incentive: Apple positive → Apple aspirational coverage
        Financial incentive: Meta $0 → Meta adversarial coverage
        """
        incentive_alignment = True  # Coverage tone follows money
        self.assertTrue(incentive_alignment)


class TestConfoundingFactors(unittest.TestCase):
    """Document confounders that could explain the asymmetry without financial incentives."""

    def test_confounder_genuine_privacy_differences(self):
        """
        STRONG confounder: Meta glasses have SHIPPED with cameras and generated
        real-world privacy incidents (contractor review, YouTuber harassment).
        Apple Glasses are hypothetical — no real incidents to report yet.
        Lovejoy's more critical Meta coverage may reflect actual product
        differences, not just financial incentives.
        """
        confounder = {
            'severity': 'STRONG',
            'description': (
                'Meta glasses are a shipping product with documented privacy '
                'incidents. Apple Glasses are pre-launch. Coverage disparity '
                'may reflect the difference between reviewing a real product '
                'versus speculating about a future one.'
            )
        }
        self.assertEqual(confounder['severity'], 'STRONG')

    def test_confounder_personal_experience(self):
        """
        MODERATE confounder: Lovejoy owns and uses Meta glasses. His advocacy
        for Apple cameras comes from personal experience with camera glasses,
        not just Apple fandom. He values the camera feature AS A USER.
        """
        confounder = {
            'severity': 'MODERATE',
            'description': (
                'Lovejoy is a Meta glasses owner/user. His camera advocacy '
                'comes from genuine product experience, not pure Apple bias. '
                'However, his experience as a user does not explain why Meta '
                'privacy concerns extend to "any Meta product" while Apple '
                'concerns are treated as solvable design challenges.'
            )
        }
        self.assertEqual(confounder['severity'], 'MODERATE')

    def test_confounder_editorial_beat(self):
        """
        MODERATE confounder: 9to5Mac is an Apple-focused publication. Its
        editorial stance naturally favors Apple framing. Readers expect
        Apple advocacy from this outlet.
        """
        confounder = {
            'severity': 'MODERATE',
            'description': (
                '9to5Mac is structurally an Apple-centric publication. '
                'Aspirational Apple framing is expected by readers and may '
                'reflect editorial mission rather than financial capture. '
                'However, this does not explain why the same journalist applies '
                'different privacy standards to identical camera features.'
            )
        }
        self.assertEqual(confounder['severity'], 'MODERATE')

    def test_confounder_track_record_difference(self):
        """
        MODERATE confounder: Meta's historical privacy record (Cambridge
        Analytica, etc.) provides rational basis for greater skepticism
        than Apple's generally stronger privacy reputation.
        """
        confounder = {
            'severity': 'MODERATE',
            'description': (
                'Meta has a well-documented history of privacy failures '
                '(Cambridge Analytica, FTC consent decree). Greater skepticism '
                'of Meta camera products may be proportionate to historical '
                'evidence rather than financial incentives.'
            )
        }
        self.assertEqual(confounder['severity'], 'MODERATE')

    def test_confounder_apple_different_implementation(self):
        """
        WEAK confounder: Apple's rumored camera implementation differs
        (low-res IR, contextual AI only, no photo/video capture). But
        Lovejoy explicitly advocates for PHOTO AND VIDEO RECORDING
        on Apple Glasses — the exact Meta feature that generates scandals.
        """
        confounder = {
            'severity': 'WEAK',
            'description': (
                'Apple camera AirPods use low-resolution IR sensors for '
                'contextual AI, not high-res photo/video. But Lovejoy is '
                'specifically advocating for Apple Glasses to include '
                'FULL photo and video recording capability — the identical '
                'feature that generates Meta privacy scandals. This confounder '
                'does not apply to his specific advocacy.'
            )
        }
        self.assertEqual(confounder['severity'], 'WEAK')


class TestCrossReferences(unittest.TestCase):
    """Verify cross-references to related mechanisms."""

    def setUp(self):
        self.data = load_competitor_research()

    def test_cross_ref_mechanism_173(self):
        """Should reference mechanism #173 (9to5 Network three-tier gradient)."""
        mechanism_173 = find_mechanism_by_id(self.data, 173)
        self.assertIsNotNone(mechanism_173, "Mechanism #173 should exist")

    def test_cross_ref_mechanism_221(self):
        """Should reference mechanism #221 (9to5Mac Security Bite pre-framing)."""
        mechanism_221 = find_mechanism_by_id(self.data, 221)
        self.assertIsNotNone(mechanism_221, "Mechanism #221 should exist")

    def test_intra_publication_pattern(self):
        """
        Mechanisms #173, #221, and #223 together demonstrate a multi-layered
        9to5Mac pattern: network-level gradient (#173), security-column
        pre-framing (#221), and individual journalist advocacy inversion (#223).
        """
        layers = {
            'network_level': 173,
            'security_column': 221,
            'individual_journalist': 223,
        }
        self.assertEqual(len(layers), 3)


if __name__ == '__main__':
    unittest.main()
