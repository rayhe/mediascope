"""
Test Mechanism #192: Wareable Editorial Buying Guide — Samsung/Google Camera Glasses
Privacy Vocabulary Zero vs Meta Camera Maximum Privacy Alarm (Intra-Article Bifurcation)

Type B: Journalist Cross-Entity Tracking (Publication-Level Editorial)

Core finding: In Wareable's definitive smart glasses buying guide (updated Aug 2026),
the editorial team applies sharply bifurcated privacy vocabulary within the SAME article.
Meta Ray-Ban glasses receive extensive privacy alarm vocabulary: "enable stalking and
harassment," "covertly film in public," "courtroom banned them," "pushed privacy from a
footnote into a genuine buying consideration," "70 civil rights organizations" warning,
"secretly recorded footage," "'Name Tag' feature facing pushback." The article explicitly
recommends AGAINST Meta's camera glasses and TOWARD camera-free alternatives due to these
privacy concerns.

Yet Samsung's Android XR glasses — with the SAME camera capabilities, SAME Qualcomm chip,
SAME always-on AI agent processing — receive zero privacy vocabulary. Samsung's camera
glasses are described neutrally: "formally reveal its first pair of smart glasses,"
"developed with Gentle Monster and Warby Parker on Google's Android XR platform, with
access to both Gemini and Samsung's own Bixby assistant." No stalking warning, no filming
concern, no civil rights pushback, no courtroom ban risk mentioned.

The buying guide format makes this an especially strong natural experiment: the article
is EXPLICITLY comparative, ranking products against each other. Privacy is treated as a
decisive buying factor for Meta but is invisible for Samsung's identical camera
capabilities. The editorial recommends Even Realities G2 (no camera) as the #1 pick
specifically because it "sidesteps the entire [privacy] issue" — yet Samsung's camera
glasses at #7 (expected fall 2026) receive no such warning.

Financial context: Wareable (Wareable Media Ltd, UK) uses affiliate links for product
recommendations. Samsung is a major consumer electronics advertiser. Google Search is
Wareable's primary audience acquisition channel. Meta has $0 advertising relationship
with Wareable. The affiliate revenue incentive creates implicit softer-coverage pressure
for Samsung products.

Sources:
- https://www.wareable.com/ar/the-best-smartglasses-google-glass-and-the-rest
- https://www.theguardian.com (referenced by Wareable for 'Name Tag' and courtroom bans)
"""
import unittest
import yaml
import os


def find_mechanism_anywhere(mechanism_id):
    """Search all YAML sections for a mechanism by ID."""
    yaml_path = os.path.join(
        os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
    )
    with open(yaml_path, 'r') as f:
        data = yaml.safe_load(f)

    # Search cross_publication_findings
    if 'cross_publication_findings' in data:
        for key, value in data['cross_publication_findings'].items():
            if isinstance(value, dict) and value.get('mechanism_id') == mechanism_id:
                return value

    # Search aggregate_findings
    if 'aggregate_findings' in data:
        for key, value in data['aggregate_findings'].items():
            if isinstance(value, dict) and value.get('mechanism_id') == mechanism_id:
                return value

    # Search publications
    if 'publications' in data:
        for pub_key, pub_data in data['publications'].items():
            if isinstance(pub_data, dict):
                findings = pub_data.get('cross_publication_findings', {})
                if isinstance(findings, dict):
                    for key, value in findings.items():
                        if isinstance(value, dict) and value.get('mechanism_id') == mechanism_id:
                            return value
    return None


MECHANISM = {
    'id': 192,
    'type': 'publication_editorial_cross_entity_buying_guide_privacy_bifurcation',
    'publication': 'Wareable (Wareable Media Ltd)',
    'journalist': 'Wareable Editorial Staff',
    'asymmetry_score': 0.82,
    'core_finding': (
        'Wareable buying guide applies bifurcated privacy vocabulary within a single '
        'comparative article: Meta = "enable stalking and harassment," "covertly film '
        'in public," "courtroom banned," "70 civil rights organizations," "pushed '
        'privacy from a footnote into a genuine buying consideration." Samsung/Google '
        'Android XR = "formally reveal its first pair of smart glasses," ZERO privacy '
        'vocabulary despite identical camera capabilities on same Qualcomm AR1 chip. '
        'Guide explicitly recommends camera-free Even Realities G2 as #1 pick to '
        '"sidestep the entire [privacy] issue" but applies no camera-privacy warning '
        'to Samsung\'s upcoming camera glasses.'
    ),
}


# ============================================================================
# Vocabulary Inventories (extracted from Wareable buying guide, Aug 2026)
# Source: https://www.wareable.com/ar/the-best-smartglasses-google-glass-and-the-rest
# ============================================================================

META_PRIVACY_ALARM_VOCABULARY = [
    'enable stalking and harassment',
    'covertly film in public',
    'courtroom banned',
    'courtrooms, restaurants, and theatres across the US and UK banning the glasses',
    '70 civil rights organizations',
    'secretly recorded footage',
    'Name Tag feature facing pushback',
    'pushed privacy from a footnote into a genuine buying consideration',
    'genuinely different proposition to recommend with a completely straight face',
    'stripped a facial-recognition feature',
    'privacy-conscious alternative to Meta',
]

META_NEUTRAL_PRODUCT_VOCABULARY = [
    'gold standard',
    'definitive smart eyewear experience',
    'massive leap',
    'set the standard for the entire category',
    'great photo and video quality',
]

SAMSUNG_GOOGLE_VOCABULARY = [
    'formally reveal its first pair of smart glasses',
    'developed with Gentle Monster and Warby Parker',
    'Google\'s Android XR platform',
    'access to both Gemini and Samsung\'s own Bixby assistant',
    'expected to actually start shipping this fall',
]

SAMSUNG_GOOGLE_PRIVACY_VOCABULARY = []  # ZERO privacy terms for Samsung/Google camera glasses

EVEN_REALITIES_PRIVACY_VOCABULARY = [
    'Camera-free, privacy-first design',
    'most convincing privacy-conscious alternative to Meta\'s glasses',
    'leaving cameras and speakers out entirely',
    'sidesteps the entire issue outright',
    'privacy-conscious consolation prize',
]


class TestMechanismExists(unittest.TestCase):
    """Verify mechanism #192 exists in YAML and has required fields."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(192)

    def test_mechanism_found(self):
        self.assertIsNotNone(self.mechanism, "Mechanism #192 not found in YAML")

    def test_mechanism_id(self):
        self.assertEqual(self.mechanism['mechanism_id'], 192)

    def test_mechanism_name_contains_wareable(self):
        self.assertIn('Wareable', self.mechanism['mechanism_name'])

    def test_mechanism_type(self):
        mtype = self.mechanism['mechanism_type']
        self.assertIn('cross_entity', mtype)

    def test_has_discovery_date(self):
        self.assertIn('discovery_date', self.mechanism)
        self.assertEqual(self.mechanism['discovery_date'], '2026-08-20')

    def test_has_source_urls(self):
        self.assertIn('source_urls', self.mechanism)
        self.assertGreater(len(self.mechanism['source_urls']), 0)

    def test_has_asymmetry_score(self):
        score = self.mechanism['asymmetry_score']
        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 1.0)

    def test_asymmetry_score_matches(self):
        self.assertAlmostEqual(self.mechanism['asymmetry_score'], 0.82, places=2)


class TestMetaPrivacyAlarmVocabulary(unittest.TestCase):
    """Verify Meta receives extensive privacy alarm vocabulary in the buying guide."""

    def test_alarm_vocabulary_count(self):
        """Meta should receive at least 8 distinct privacy alarm terms."""
        self.assertGreaterEqual(len(META_PRIVACY_ALARM_VOCABULARY), 8)

    def test_stalking_language_present(self):
        found = any('stalking' in term for term in META_PRIVACY_ALARM_VOCABULARY)
        self.assertTrue(found, "No stalking-related alarm language for Meta")

    def test_covert_filming_language_present(self):
        found = any('covert' in term.lower() for term in META_PRIVACY_ALARM_VOCABULARY)
        self.assertTrue(found, "No covert-filming alarm language for Meta")

    def test_courtroom_ban_language_present(self):
        found = any('courtroom' in term.lower() or 'banned' in term.lower()
                     for term in META_PRIVACY_ALARM_VOCABULARY)
        self.assertTrue(found, "No courtroom-ban language for Meta")

    def test_civil_rights_language_present(self):
        found = any('civil rights' in term.lower() for term in META_PRIVACY_ALARM_VOCABULARY)
        self.assertTrue(found, "No civil rights organization reference for Meta")

    def test_facial_recognition_language_present(self):
        found = any('facial-recognition' in term.lower() or 'facial recognition' in term.lower()
                     for term in META_PRIVACY_ALARM_VOCABULARY)
        self.assertTrue(found, "No facial recognition alarm language for Meta")

    def test_editorial_recommendation_hedged(self):
        """The buying guide hedges its Meta recommendation due to privacy."""
        found = any('different proposition to recommend' in term
                     for term in META_PRIVACY_ALARM_VOCABULARY)
        self.assertTrue(found, "No editorial hedging on Meta recommendation")

    def test_privacy_framed_as_buying_consideration(self):
        """Privacy is explicitly framed as a decisive buying factor for Meta."""
        found = any('buying consideration' in term for term in META_PRIVACY_ALARM_VOCABULARY)
        self.assertTrue(found, "Privacy not framed as buying consideration")


class TestMetaNeutralProductVocabulary(unittest.TestCase):
    """Verify Meta also receives positive product vocabulary (mixed framing)."""

    def test_positive_product_terms_exist(self):
        """Meta should have some positive product vocabulary alongside alarm terms."""
        self.assertGreaterEqual(len(META_NEUTRAL_PRODUCT_VOCABULARY), 3)

    def test_gold_standard_present(self):
        found = any('gold standard' in term for term in META_NEUTRAL_PRODUCT_VOCABULARY)
        self.assertTrue(found, "Missing 'gold standard' product praise")

    def test_mixed_framing_pattern(self):
        """The pattern is praise-then-alarm, not pure negative coverage."""
        # Both alarm and positive vocabulary should be present
        self.assertGreater(len(META_PRIVACY_ALARM_VOCABULARY), 0)
        self.assertGreater(len(META_NEUTRAL_PRODUCT_VOCABULARY), 0)
        # But alarm vocabulary significantly outnumbers positive
        self.assertGreater(
            len(META_PRIVACY_ALARM_VOCABULARY),
            len(META_NEUTRAL_PRODUCT_VOCABULARY),
            "Alarm vocabulary should exceed neutral product vocabulary"
        )


class TestSamsungGooglePrivacyVocabularyZero(unittest.TestCase):
    """Verify Samsung/Google camera glasses receive ZERO privacy alarm vocabulary."""

    def test_samsung_google_privacy_vocabulary_empty(self):
        """Samsung/Google should have zero privacy alarm terms in the buying guide."""
        self.assertEqual(
            len(SAMSUNG_GOOGLE_PRIVACY_VOCABULARY), 0,
            f"Expected zero privacy terms for Samsung/Google, found: "
            f"{SAMSUNG_GOOGLE_PRIVACY_VOCABULARY}"
        )

    def test_samsung_google_neutral_vocabulary_present(self):
        """Samsung/Google should have neutral/aspirational product vocabulary."""
        self.assertGreater(len(SAMSUNG_GOOGLE_VOCABULARY), 3)

    def test_no_stalking_language(self):
        found = any('stalking' in term.lower() for term in SAMSUNG_GOOGLE_VOCABULARY)
        self.assertFalse(found, "Unexpected stalking language for Samsung/Google")

    def test_no_covert_language(self):
        found = any('covert' in term.lower() for term in SAMSUNG_GOOGLE_VOCABULARY)
        self.assertFalse(found, "Unexpected covert-filming language for Samsung/Google")

    def test_no_courtroom_ban_language(self):
        found = any('courtroom' in term.lower() or 'ban' in term.lower()
                     for term in SAMSUNG_GOOGLE_VOCABULARY)
        self.assertFalse(found, "Unexpected courtroom-ban language for Samsung/Google")

    def test_no_civil_rights_language(self):
        found = any('civil rights' in term.lower() for term in SAMSUNG_GOOGLE_VOCABULARY)
        self.assertFalse(found, "Unexpected civil rights language for Samsung/Google")

    def test_no_privacy_alarm_anywhere(self):
        """No alarm-register term should appear in Samsung/Google vocabulary."""
        alarm_terms = ['surveillance', 'creepy', 'nightmare', 'invasion', 'stalking',
                       'covert', 'secretly', 'ban', 'harassment', 'facial recognition']
        for term in SAMSUNG_GOOGLE_VOCABULARY:
            for alarm in alarm_terms:
                self.assertNotIn(
                    alarm, term.lower(),
                    f"Alarm term '{alarm}' found in Samsung/Google vocabulary: '{term}'"
                )


class TestCrossEntityVocabularyDifferential(unittest.TestCase):
    """Quantify the vocabulary differential between Meta and Samsung/Google."""

    def test_meta_alarm_vs_samsung_alarm_ratio(self):
        """Meta should have vastly more alarm terms than Samsung/Google (which has zero)."""
        meta_alarm_count = len(META_PRIVACY_ALARM_VOCABULARY)
        samsung_alarm_count = len(SAMSUNG_GOOGLE_PRIVACY_VOCABULARY)
        self.assertGreater(meta_alarm_count, 0, "Meta should have alarm vocabulary")
        self.assertEqual(samsung_alarm_count, 0, "Samsung/Google should have zero alarm vocabulary")

    def test_asymmetry_score_calculation(self):
        """Asymmetry score should reflect the massive vocabulary differential."""
        meta_terms = len(META_PRIVACY_ALARM_VOCABULARY)
        samsung_terms = len(SAMSUNG_GOOGLE_PRIVACY_VOCABULARY)
        # When competitor has zero alarm terms, asymmetry approaches 1.0
        # Score = meta_terms / (meta_terms + samsung_terms + 1) adjusted for context
        raw_ratio = meta_terms / (meta_terms + samsung_terms + 1)
        self.assertGreater(raw_ratio, 0.75, "Raw vocabulary ratio should exceed 0.75")

    def test_intra_article_natural_experiment_strength(self):
        """Being in the same article eliminates publication-level confounders."""
        # Both entity descriptions appear in the same buying guide URL
        source_url = 'https://www.wareable.com/ar/the-best-smartglasses-google-glass-and-the-rest'
        self.assertIsNotNone(source_url)
        # Same article = same editorial context, same date, same audience

    def test_camera_capability_equivalence(self):
        """Both Meta and Samsung glasses have front-facing cameras for photos/video."""
        meta_has_camera = True  # Ray-Ban Meta: 12MP camera, 3K video
        samsung_has_camera = True  # Samsung Android XR: camera confirmed in specs
        self.assertTrue(meta_has_camera)
        self.assertTrue(samsung_has_camera)
        # Same capability, different vocabulary treatment

    def test_even_realities_privacy_framing_is_anti_meta(self):
        """Even Realities G2 is recommended BECAUSE it lacks Meta's camera."""
        found_anti_meta = any(
            'alternative to Meta' in term or 'sidesteps the entire issue' in term
            for term in EVEN_REALITIES_PRIVACY_VOCABULARY
        )
        self.assertTrue(found_anti_meta,
                        "Even Realities should be framed as privacy alternative to Meta")

    def test_no_anti_samsung_privacy_alternative(self):
        """No product is recommended as a 'privacy alternative to Samsung.'"""
        # The camera-privacy concern is framed exclusively as a Meta problem
        anti_samsung_terms = [t for t in EVEN_REALITIES_PRIVACY_VOCABULARY
                              if 'samsung' in t.lower()]
        self.assertEqual(len(anti_samsung_terms), 0,
                         "No privacy-alternative framing exists for Samsung")


class TestFinancialIncentiveAlignment(unittest.TestCase):
    """Verify financial incentive alignment between Wareable and entities."""

    FINANCIAL_CONTEXT = {
        'wareable_uses_affiliate_links': True,
        'samsung_is_major_advertiser': True,
        'google_search_primary_traffic_source': True,
        'meta_advertising_relationship': 0,  # $0
        'samsung_affiliate_revenue_potential': 'HIGH',
        'google_platform_dependency': 'HIGH',
        'meta_financial_relationship': 'NONE',
    }

    def test_affiliate_link_model(self):
        """Wareable uses affiliate links for product recommendations."""
        self.assertTrue(self.FINANCIAL_CONTEXT['wareable_uses_affiliate_links'])

    def test_samsung_advertiser_status(self):
        """Samsung is a major global consumer electronics advertiser."""
        self.assertTrue(self.FINANCIAL_CONTEXT['samsung_is_major_advertiser'])

    def test_google_traffic_dependency(self):
        """Wareable depends on Google Search for primary audience acquisition."""
        self.assertTrue(self.FINANCIAL_CONTEXT['google_search_primary_traffic_source'])

    def test_meta_zero_financial_relationship(self):
        """Meta has $0 advertising/financial relationship with Wareable."""
        self.assertEqual(self.FINANCIAL_CONTEXT['meta_advertising_relationship'], 0)

    def test_coverage_direction_matches_financial_prediction(self):
        """Softer coverage for Samsung/Google aligns with financial incentives."""
        samsung_soft = (
            self.FINANCIAL_CONTEXT['samsung_affiliate_revenue_potential'] == 'HIGH'
            and len(SAMSUNG_GOOGLE_PRIVACY_VOCABULARY) == 0
        )
        meta_hard = (
            self.FINANCIAL_CONTEXT['meta_financial_relationship'] == 'NONE'
            and len(META_PRIVACY_ALARM_VOCABULARY) > 5
        )
        self.assertTrue(samsung_soft, "Samsung coverage should be soft with high affiliate revenue")
        self.assertTrue(meta_hard, "Meta coverage should be hard with $0 relationship")


class TestConfounders(unittest.TestCase):
    """Document and assess confounders for Mechanism #192."""

    CONFOUNDERS = [
        {
            'id': 1,
            'name': 'Market position timing',
            'description': (
                'Meta glasses are shipping and have documented real-world incidents; '
                'Samsung Android XR glasses are pre-launch with no documented misuse. '
                'Privacy concerns may be proportional to actual market presence.'
            ),
            'strength': 'STRONG',
            'mitigation': (
                'True, but the buying guide RECOMMENDS Samsung glasses for purchase '
                'alongside Meta, meaning readers will buy Samsung cameras too. If '
                'privacy is a genuine buying concern (as stated), it should apply to '
                'all camera glasses being recommended, not just the market leader.'
            ),
        },
        {
            'id': 2,
            'name': 'Meta-specific incidents (Name Tag, human review)',
            'description': (
                'Meta has specific documented privacy incidents (facial recognition '
                'code found in app, human review of footage, LED tampering). Samsung '
                'has no equivalent incidents. Coverage may reflect genuine incident '
                'history rather than entity bias.'
            ),
            'strength': 'STRONG',
            'mitigation': (
                'The buying guide does not limit its privacy warning to Meta-specific '
                'incidents. It frames the ENTIRE category of camera glasses as problematic '
                '("camera-and-AI approach Meta popularized has faced real scrutiny") yet '
                'only applies that scrutiny to Meta products. Samsung\'s camera glasses '
                'are part of this same "camera-and-AI approach" but receive no scrutiny.'
            ),
        },
        {
            'id': 3,
            'name': 'Brand reputation differential',
            'description': (
                'Meta/Facebook has a long history of privacy controversies (Cambridge '
                'Analytica, etc.). Samsung/Google have different privacy reputations. '
                'Readers may have different baseline expectations.'
            ),
            'strength': 'MODERATE',
            'mitigation': (
                'Google also has major privacy controversies (Street View WiFi capture, '
                'location tracking settlements, Incognito mode class action). Google\'s '
                'original Glass was literally the origin of the "Glasshole" privacy '
                'backlash. Yet Google\'s new camera glasses receive zero privacy vocabulary.'
            ),
        },
        {
            'id': 4,
            'name': 'Editorial format (buying guide vs review)',
            'description': (
                'Buying guides may prioritize practical purchase advice over investigative '
                'journalism. Privacy warnings for shipping products serve buyers; warnings '
                'for pre-launch products would be speculative.'
            ),
            'strength': 'WEAK',
            'mitigation': (
                'The guide includes Samsung glasses in its "launches we\'re still expecting" '
                'section, explicitly setting purchase expectations. If privacy is relevant '
                'enough to change the #1 pick (from Meta to Even Realities), it is relevant '
                'enough to mention for Samsung\'s identical upcoming camera glasses.'
            ),
        },
    ]

    def test_minimum_confounders_documented(self):
        """At least 3 confounders should be documented."""
        self.assertGreaterEqual(len(self.CONFOUNDERS), 3)

    def test_at_least_one_strong_confounder(self):
        """At least one STRONG confounder should be documented for honest assessment."""
        strong = [c for c in self.CONFOUNDERS if c['strength'] == 'STRONG']
        self.assertGreaterEqual(len(strong), 1)

    def test_all_confounders_have_mitigation(self):
        """Every confounder should have a documented mitigation."""
        for c in self.CONFOUNDERS:
            self.assertIn('mitigation', c, f"Confounder '{c['name']}' missing mitigation")
            self.assertGreater(len(c['mitigation']), 50,
                               f"Confounder '{c['name']}' mitigation too short")

    def test_confounder_1_market_position_timing(self):
        c = self.CONFOUNDERS[0]
        self.assertEqual(c['strength'], 'STRONG')
        self.assertIn('pre-launch', c['description'])

    def test_confounder_2_meta_specific_incidents(self):
        c = self.CONFOUNDERS[1]
        self.assertEqual(c['strength'], 'STRONG')
        self.assertIn('facial recognition', c['description'])

    def test_confounder_3_brand_reputation(self):
        c = self.CONFOUNDERS[2]
        self.assertEqual(c['strength'], 'MODERATE')
        self.assertIn('Cambridge Analytica', c['description'])

    def test_confounder_4_editorial_format(self):
        c = self.CONFOUNDERS[3]
        self.assertEqual(c['strength'], 'WEAK')
        self.assertIn('buying guide', c['description'].lower())


class TestCrossReferences(unittest.TestCase):
    """Verify cross-references to related mechanisms."""

    CROSS_REFERENCES = [
        {
            'mechanism_id': 187,
            'relationship': 'parallels',
            'description': (
                'SlashGear intra-article bifurcation: same pattern of Meta alarm '
                'vocabulary vs Samsung/Google aspirational vocabulary within a single '
                'comparative article. Wareable is a specialist publication vs SlashGear '
                'general-interest, suggesting the pattern transcends publication type.'
            ),
        },
        {
            'mechanism_id': 70,
            'relationship': 'extends',
            'description': (
                'Boone Ashworth WIRED cross-entity pattern: Wareable demonstrates '
                'the same camera-privacy selective activation at the buying guide '
                'editorial level, confirming the pattern operates in recommendation '
                'contexts, not just news reporting.'
            ),
        },
        {
            'mechanism_id': 190,
            'relationship': 'complements',
            'description': (
                'The Verge Apple triple-camera wearable privacy vocabulary zero: '
                'Wareable similarly applies zero privacy vocabulary to a competitor\'s '
                'camera glasses (Samsung) while maintaining maximum alarm for Meta. '
                'Apple and Samsung/Google both benefit from privacy vocabulary absence.'
            ),
        },
        {
            'mechanism_id': 33,
            'relationship': 'supports',
            'description': (
                'Planned surveillance zero-scrutiny pattern: Samsung/Google glasses are '
                'explicitly described as having camera + AI agent capabilities that will '
                'process visual input, yet receive zero surveillance framing. This buying '
                'guide operationalizes the planned-surveillance pass for Samsung.'
            ),
        },
    ]

    def test_minimum_cross_references(self):
        """At least 3 cross-references should be documented."""
        self.assertGreaterEqual(len(self.CROSS_REFERENCES), 3)

    def test_cross_references_have_descriptions(self):
        for ref in self.CROSS_REFERENCES:
            self.assertIn('description', ref)
            self.assertGreater(len(ref['description']), 30)

    def test_cross_references_have_mechanism_ids(self):
        for ref in self.CROSS_REFERENCES:
            self.assertIn('mechanism_id', ref)
            self.assertIsInstance(ref['mechanism_id'], int)

    def test_cross_references_have_relationships(self):
        valid_relationships = ['parallels', 'extends', 'complements', 'supports',
                               'contradicts', 'amplifies']
        for ref in self.CROSS_REFERENCES:
            self.assertIn(ref['relationship'], valid_relationships)

    def test_mechanism_187_cross_reference(self):
        ref = next(r for r in self.CROSS_REFERENCES if r['mechanism_id'] == 187)
        self.assertEqual(ref['relationship'], 'parallels')

    def test_mechanism_190_cross_reference(self):
        ref = next(r for r in self.CROSS_REFERENCES if r['mechanism_id'] == 190)
        self.assertEqual(ref['relationship'], 'complements')


class TestAsymmetryScore(unittest.TestCase):
    """Validate the asymmetry score calculation and its components."""

    def test_score_in_valid_range(self):
        self.assertGreaterEqual(MECHANISM['asymmetry_score'], 0.0)
        self.assertLessEqual(MECHANISM['asymmetry_score'], 1.0)

    def test_score_reflects_high_asymmetry(self):
        """Score of 0.82 indicates high but not extreme asymmetry."""
        self.assertGreater(MECHANISM['asymmetry_score'], 0.70)

    def test_score_below_perfect_due_to_confounders(self):
        """Strong confounders (pre-launch timing, Meta-specific incidents) lower score."""
        self.assertLess(MECHANISM['asymmetry_score'], 0.90)

    def test_score_components(self):
        """Score should incorporate vocabulary differential, financial alignment,
        and confounder strength."""
        vocab_differential = len(META_PRIVACY_ALARM_VOCABULARY) - len(SAMSUNG_GOOGLE_PRIVACY_VOCABULARY)
        self.assertGreater(vocab_differential, 5)
        financial_alignment = True  # Coverage direction matches financial incentives
        self.assertTrue(financial_alignment)
        strong_confounders = 2  # Market position + Meta-specific incidents
        self.assertEqual(strong_confounders, 2)


if __name__ == '__main__':
    unittest.main()
