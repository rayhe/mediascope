"""
Test Mechanism #191: Kif Leswing (CNBC / NBCUniversal / Comcast) Cross-Entity
CEO-Attribution vs Product-Capability Vocabulary Asymmetry

Type B: Journalist Cross-Entity Tracking

Core finding: CNBC senior technology correspondent Kif Leswing frames Meta smart glasses
coverage through CEO-attribution vocabulary ("Zuckerberg keeps pushing wearables,"
"continues his push") that personalizes product strategy as executive stubbornness,
while Samsung/Google smart glasses coverage uses product-capability vocabulary
("AI-powered," "premium," "reasonable") with zero CEO personalization and zero privacy
vocabulary. CNBC broke the Samsung Galaxy Glasses specifications at MWC 2026 (March 6)
with exclusive executive access (Jay Kim EVP interview, James Choi quote on pricing),
signaling preferential Samsung source access that parallels aspirational framing.

Key vocabulary asymmetry:
- Meta headline: "as Zuckerberg keeps pushing wearables" — personalizes company
  strategy to CEO, implies persistence despite doubt
- Samsung coverage: "premium product," "reasonable" pricing, "AI-powered" —
  product-capability frame, zero CEO personalization
- Both have cameras: Samsung 12MP eye-level + Qualcomm AR1, Meta 12MP + LED
  privacy enforcement. Samsung receives zero privacy vocabulary.
- CNBC cited "Meta controlled 69.2% of smart-glasses market" — frames Meta as
  dominant incumbent to be challenged, not innovator to be praised

Financial context: CNBC is owned by NBCUniversal (Comcast). Google and Samsung are
among CNBC's largest advertisers. Google is the direct PLATFORM PARTNER for Samsung's
Android XR glasses (providing the OS and Gemini AI). Comcast/NBCUniversal's Peacock
streaming competes with Meta's video distribution ambitions. Meta has $0 parent-company
financial relationship with Comcast/NBCUniversal.

Sources:
- https://muckrack.com/kif-leswing/articles (Kif Leswing article archive)
- https://www.eweek.com/news/samsung-google-first-android-xr-smart-glasses/ (CNBC citation)
- https://www.eweek.com/news/samsung-galaxy-glasses-ai-smart-glasses-launch/ (CNBC broke specs)
- https://www.wareable.com/wearable-tech/samsungs-smart-galaxy-glasses-camera-phone-tether-ar-display-confirmation (CNBC Jay Kim interview)
"""
import unittest
import yaml
import os


PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def find_mechanism_anywhere(mechanism_id):
    """Search all YAML sections for a mechanism by ID."""
    yaml_path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
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
    'id': 191,
    'type': 'journalist_cross_entity_ceo_attribution_vocabulary_asymmetry',
    'publication': 'CNBC (NBCUniversal / Comcast)',
    'journalist': 'Kif Leswing',
    'asymmetry_score': 0.72,
    'core_finding': (
        'Kif Leswing applies CEO-attribution vocabulary to Meta smart glasses coverage '
        '("Zuckerberg keeps pushing wearables," "continues his push") personalizing '
        'product strategy as executive stubbornness, while Samsung/Google coverage uses '
        'product-capability vocabulary ("premium," "reasonable," "AI-powered") with '
        'zero CEO personalization and zero privacy terms. CNBC broke Samsung specs '
        'at MWC with exclusive EVP access (Jay Kim interview), signaling preferential '
        'source relationship that parallels aspirational framing.'
    ),
}


class TestMechanismExists(unittest.TestCase):
    """Verify mechanism #191 exists and has required fields."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(191)

    def test_mechanism_found(self):
        self.assertIsNotNone(self.mechanism, "Mechanism #191 not found in YAML")

    def test_mechanism_id(self):
        self.assertEqual(self.mechanism['mechanism_id'], 191)

    def test_mechanism_name_contains_kif_leswing(self):
        self.assertIn('Kif Leswing', self.mechanism['mechanism_name'])

    def test_mechanism_name_contains_cnbc(self):
        self.assertIn('CNBC', self.mechanism['mechanism_name'])

    def test_mechanism_type(self):
        mtype = self.mechanism['mechanism_type']
        self.assertIn('journalist', mtype)
        self.assertIn('cross_entity', mtype)

    def test_has_discovery_date(self):
        self.assertIn('discovery_date', self.mechanism)
        self.assertEqual(self.mechanism['discovery_date'], '2026-08-20')

    def test_has_source_urls(self):
        self.assertIn('source_urls', self.mechanism)
        self.assertGreaterEqual(len(self.mechanism['source_urls']), 3)

    def test_has_asymmetry_score(self):
        self.assertIn('asymmetry_score', self.mechanism)
        score = self.mechanism['asymmetry_score']
        self.assertGreaterEqual(score, 0.5)
        self.assertLessEqual(score, 1.0)

    def test_asymmetry_score_value(self):
        self.assertEqual(self.mechanism['asymmetry_score'], 0.72)


class TestJournalistProfile(unittest.TestCase):
    """Verify journalist profile captures Kif Leswing's role at CNBC."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(191)
        cls.journalist = cls.mechanism.get('journalist', {})

    def test_journalist_name(self):
        self.assertEqual(self.journalist['name'], 'Kif Leswing')

    def test_primary_publication_cnbc(self):
        self.assertIn('CNBC', self.journalist['publication'])

    def test_role_documented(self):
        role = self.journalist.get('role', '').lower()
        self.assertTrue(
            'senior' in role or 'technology' in role or 'correspondent' in role,
            f"Role should capture senior tech correspondent: {role}"
        )

    def test_beat_documented(self):
        beat = self.journalist.get('beat', '').lower()
        self.assertTrue(
            'tech' in beat or 'silicon valley' in beat or 'apple' in beat or 'chip' in beat,
            f"Beat should document tech/Silicon Valley coverage: {beat}"
        )

    def test_parent_company_documented(self):
        parent = self.journalist.get('parent_company', '').lower()
        self.assertTrue(
            'nbcuniversal' in parent or 'comcast' in parent,
            f"Parent company should document NBCUniversal/Comcast: {parent}"
        )

    def test_samsung_exclusive_access(self):
        access = self.journalist.get('samsung_source_access', '')
        self.assertTrue(
            len(access) > 0,
            "Should document CNBC's exclusive Samsung executive access at MWC"
        )


class TestMetaCoverageVocabulary(unittest.TestCase):
    """Verify Meta CEO-attribution vocabulary from Kif Leswing's smart glasses article."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(191)
        cls.meta_vocab = cls.mechanism.get('meta_vocabulary', {})

    def test_ceo_attribution_terms_documented(self):
        terms = self.meta_vocab.get('ceo_attribution_terms', [])
        self.assertGreaterEqual(len(terms), 2)

    def test_keeps_pushing_term(self):
        terms = self.meta_vocab.get('ceo_attribution_terms', [])
        pushing = [t for t in terms if 'keeps pushing' in t.lower() or 'push' in t.lower()]
        self.assertGreater(len(pushing), 0, "Should include 'keeps pushing wearables'")

    def test_continues_his_push_term(self):
        terms = self.meta_vocab.get('ceo_attribution_terms', [])
        continues = [t for t in terms if 'continues' in t.lower()]
        self.assertGreater(len(continues), 0, "Should include 'continues his push'")

    def test_zuckerberg_personalization(self):
        personalization = self.meta_vocab.get('ceo_personalization', '')
        self.assertIn('Zuckerberg', personalization)

    def test_headline_frame(self):
        headline = self.meta_vocab.get('headline', '')
        self.assertIn('Zuckerberg', headline)
        self.assertIn('pushing', headline.lower())

    def test_product_price_framing(self):
        price_frame = self.meta_vocab.get('price_framing', '').lower()
        self.assertTrue(
            '$299' in price_frame or 'less than' in price_frame or '$80 less' in price_frame,
            f"Should document competitive price framing: {price_frame}"
        )

    def test_market_dominance_framing(self):
        dominance = self.meta_vocab.get('market_dominance_framing', '').lower()
        self.assertTrue(
            '69.2%' in dominance or 'controlled' in dominance or 'market' in dominance,
            f"Should document Meta market share framing: {dominance}"
        )

    def test_article_url(self):
        url = self.meta_vocab.get('source_article_url', '')
        self.assertIn('cnbc.com', url)


class TestSamsungGoogleCoverageVocabulary(unittest.TestCase):
    """Verify Samsung/Google aspirational product-capability vocabulary."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(191)
        cls.samsung_vocab = cls.mechanism.get('samsung_google_vocabulary', {})

    def test_aspirational_terms_documented(self):
        terms = self.samsung_vocab.get('aspirational_terms', [])
        self.assertGreaterEqual(len(terms), 3)

    def test_premium_term(self):
        terms = self.samsung_vocab.get('aspirational_terms', [])
        premium = [t for t in terms if 'premium' in t.lower()]
        self.assertGreater(len(premium), 0, "Should include 'premium product'")

    def test_reasonable_term(self):
        terms = self.samsung_vocab.get('aspirational_terms', [])
        reasonable = [t for t in terms if 'reasonable' in t.lower()]
        self.assertGreater(len(reasonable), 0, "Should include 'reasonable' pricing")

    def test_ai_powered_term(self):
        terms = self.samsung_vocab.get('aspirational_terms', [])
        ai = [t for t in terms if 'ai' in t.lower() or 'gemini' in t.lower()]
        self.assertGreater(len(ai), 0, "Should include AI-powered/Gemini framing")

    def test_zero_ceo_personalization(self):
        ceo = self.samsung_vocab.get('ceo_personalization_count', 99)
        self.assertEqual(ceo, 0,
                         "Samsung coverage should have zero CEO personalization")

    def test_zero_privacy_terms(self):
        privacy = self.samsung_vocab.get('privacy_alarm_terms', 99)
        self.assertEqual(privacy, 0,
                         "Samsung coverage should have zero privacy alarm terms")

    def test_exclusive_exec_access(self):
        access = self.samsung_vocab.get('exclusive_exec_access', {})
        self.assertIn('jay_kim', access)

    def test_pricing_aspirational_frame(self):
        pricing = self.samsung_vocab.get('pricing_frame', '').lower()
        self.assertTrue(
            'reasonable' in pricing or 'premium' in pricing or 'not crazy expensive' in pricing,
            f"Samsung pricing should have aspirational framing: {pricing}"
        )


class TestCEOAttributionDifferential(unittest.TestCase):
    """Verify the CEO personalization asymmetry between entities."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(191)
        cls.differential = cls.mechanism.get('ceo_attribution_differential', {})

    def test_meta_ceo_mentions(self):
        count = self.differential.get('meta_ceo_mentions', 0)
        self.assertGreaterEqual(count, 2,
                                "Meta coverage should mention Zuckerberg 2+ times")

    def test_samsung_ceo_mentions(self):
        count = self.differential.get('samsung_ceo_mentions', 0)
        self.assertEqual(count, 0,
                         "Samsung coverage should have zero top-exec personalization")

    def test_meta_strategy_personalized(self):
        personalized = self.differential.get('meta_strategy_personalized', False)
        self.assertTrue(personalized,
                        "Meta strategy should be personalized to Zuckerberg")

    def test_samsung_strategy_institutional(self):
        institutional = self.differential.get('samsung_strategy_institutional', False)
        self.assertTrue(institutional,
                        "Samsung strategy should be framed as institutional/company")

    def test_framing_effect_documented(self):
        effect = self.differential.get('framing_effect', '').lower()
        self.assertTrue(
            'stubbornness' in effect or 'persistence' in effect or 'personal' in effect,
            f"Should document CEO personalization creating stubbornness frame: {effect}"
        )


class TestCapabilityParity(unittest.TestCase):
    """Verify both products have equivalent camera capabilities."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(191)
        cls.parity = cls.mechanism.get('capability_parity', {})

    def test_samsung_has_camera(self):
        cam = self.parity.get('samsung_camera', '')
        self.assertTrue(len(cam) > 0, "Should document Samsung camera capability")

    def test_meta_has_camera(self):
        cam = self.parity.get('meta_camera', '')
        self.assertTrue(len(cam) > 0, "Should document Meta camera capability")

    def test_both_qualcomm(self):
        chip = self.parity.get('processor_comparison', '').lower()
        self.assertTrue(
            'qualcomm' in chip or 'snapdragon' in chip,
            f"Should document Qualcomm chip in both: {chip}"
        )

    def test_samsung_led_indicator(self):
        led = self.parity.get('samsung_privacy_led', '').lower()
        self.assertTrue(
            'led' in led or 'indicator' in led,
            f"Should document Samsung LED indicator: {led}"
        )

    def test_meta_privacy_enforcement(self):
        enforcement = self.parity.get('meta_privacy_enforcement', '').lower()
        self.assertTrue(
            'led' in enforcement or 'tamper' in enforcement or 'v26' in enforcement,
            f"Should document Meta LED tamper enforcement: {enforcement}"
        )

    def test_samsung_privacy_alarm_zero(self):
        count = self.parity.get('samsung_privacy_alarm_count', 99)
        self.assertEqual(count, 0,
                         "Samsung camera coverage should have zero privacy alarm terms")


class TestFinancialContext(unittest.TestCase):
    """Verify financial context documents CNBC / Comcast advertising dependency."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(191)
        cls.financial = cls.mechanism.get('financial_context', {})

    def test_cnbc_owner_documented(self):
        owner = self.financial.get('cnbc_owner', '')
        self.assertTrue(
            'NBCUniversal' in owner or 'Comcast' in owner,
            f"Should document NBCUniversal/Comcast ownership: {owner}"
        )

    def test_google_advertising_relationship(self):
        google = self.financial.get('google_advertising_relationship', '').lower()
        self.assertTrue(
            'advertiser' in google or 'advertising' in google,
            f"Should document Google as CNBC advertiser: {google}"
        )

    def test_samsung_advertising_relationship(self):
        samsung = self.financial.get('samsung_advertising_relationship', '').lower()
        self.assertTrue(
            'advertiser' in samsung or 'advertising' in samsung,
            f"Should document Samsung as CNBC advertiser: {samsung}"
        )

    def test_google_android_xr_platform_partner(self):
        partner = self.financial.get('google_android_xr_partnership', '')
        self.assertTrue(len(partner) > 0,
                        "Should document Google as Android XR platform partner")

    def test_meta_zero_financial_relationship(self):
        meta = self.financial.get('meta_financial_relationship', '')
        self.assertIn('$0', meta)

    def test_peacock_competition(self):
        peacock = self.financial.get('peacock_meta_competition', '').lower()
        self.assertTrue(
            'peacock' in peacock or 'streaming' in peacock or 'video' in peacock,
            f"Should document Peacock/video competition: {peacock}"
        )


class TestConfounders(unittest.TestCase):
    """Verify confounders are documented with rebuttals."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(191)
        cls.confounders = cls.mechanism.get('confounders', [])

    def test_at_least_4_confounders(self):
        self.assertGreaterEqual(len(self.confounders), 4)

    def test_at_least_1_strong_confounder(self):
        strong = [c for c in self.confounders if c.get('strength') == 'STRONG']
        self.assertGreaterEqual(len(strong), 1)

    def test_at_least_2_moderate_confounders(self):
        moderate = [c for c in self.confounders if c.get('strength') == 'MODERATE']
        self.assertGreaterEqual(len(moderate), 2)

    def test_at_least_1_weak_confounder(self):
        weak = [c for c in self.confounders if c.get('strength') == 'WEAK']
        self.assertGreaterEqual(len(weak), 1)

    def test_all_confounders_have_rebuttals(self):
        for c in self.confounders:
            self.assertIn('rebuttal', c,
                          f"Confounder missing rebuttal: {c.get('description', '')[:50]}")
            self.assertGreater(len(c['rebuttal']), 30)

    def test_meta_market_dominance_confounder_exists(self):
        descriptions = [c.get('description', '').lower() for c in self.confounders]
        dom = any('market' in d and ('domin' in d or 'share' in d or 'leader' in d) for d in descriptions)
        self.assertTrue(dom, "Should have a Meta market dominance confounder")

    def test_beat_specialization_confounder_exists(self):
        descriptions = [c.get('description', '').lower() for c in self.confounders]
        beat = any('beat' in d or 'chip' in d or 'specializ' in d or 'primary' in d for d in descriptions)
        self.assertTrue(beat, "Should have a beat specialization confounder")

    def test_cnbc_financial_journalism_confounder_exists(self):
        descriptions = [c.get('description', '').lower() for c in self.confounders]
        fin = any('financial' in d or 'business' in d or 'investor' in d for d in descriptions)
        self.assertTrue(fin, "Should have a financial journalism frame confounder")


class TestCrossReferences(unittest.TestCase):
    """Verify cross-references to related mechanisms."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(191)
        cls.cross_refs = cls.mechanism.get('cross_references', [])

    def test_at_least_3_cross_references(self):
        self.assertGreaterEqual(len(self.cross_refs), 3)

    def test_mechanism_187_referenced(self):
        """Mechanism #187 = Sumukh Rao SlashGear cross-entity vocabulary bifurcation"""
        ref_ids = [r.get('mechanism_id') for r in self.cross_refs]
        self.assertIn(187, ref_ids)

    def test_mechanism_183_referenced(self):
        """Mechanism #183 = Hadlee Simons Android Authority cross-entity"""
        ref_ids = [r.get('mechanism_id') for r in self.cross_refs]
        self.assertIn(183, ref_ids)

    def test_mechanism_160_referenced(self):
        """Mechanism #160 = Nadeem Sarwar Digital Trends managing editor cross-entity"""
        ref_ids = [r.get('mechanism_id') for r in self.cross_refs]
        self.assertIn(160, ref_ids)

    def test_all_cross_refs_have_relationships(self):
        for ref in self.cross_refs:
            self.assertIn('relationship', ref)
            self.assertGreater(len(ref['relationship']), 20)


class TestDocSync(unittest.TestCase):
    """Verify documentation references this mechanism."""

    def test_readme_mentions_test_file(self):
        readme_path = os.path.join(os.path.dirname(__file__), '..', 'README.md')
        with open(readme_path, 'r') as f:
            content = f.read()
        self.assertIn('test_kif_leswing_cnbc', content)

    def test_architecture_lists_test_file(self):
        arch_path = os.path.join(os.path.dirname(__file__), '..', 'docs', 'ARCHITECTURE.md')
        with open(arch_path, 'r') as f:
            content = f.read()
        self.assertIn('test_kif_leswing_cnbc', content)

    def test_test_file_path_in_mechanism(self):
        mechanism = find_mechanism_anywhere(191)
        test_file = mechanism.get('test_file', '')
        self.assertIn('kif_leswing_cnbc', test_file)

    def test_test_count_in_mechanism(self):
        mechanism = find_mechanism_anywhere(191)
        count = mechanism.get('test_count', 0)
        self.assertGreater(count, 0)


if __name__ == '__main__':
    unittest.main()
