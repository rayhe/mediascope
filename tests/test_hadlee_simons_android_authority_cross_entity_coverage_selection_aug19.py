"""
Test Mechanism #183: Hadlee Simons (Android Authority) Smart Glasses Cross-Entity
Coverage Selection — Samsung Privacy Problem-Solving + Google Advocacy + Zero Meta
Privacy Investigation

Type B: Journalist Cross-Entity Tracking

Core finding: Hadlee Simons, a senior editor at Android Authority, has covered smart
glasses across 6+ entities (Samsung, Google, Snap, Halliday, HTC, TECNO) with
neutral-to-aspirational framing while publishing ZERO dedicated Meta Ray-Ban privacy
investigation articles. His Samsung coverage (Jul 31, 2026) frames Samsung as SOLVING
the privacy problem with headline vocabulary "keep perverts away," presenting Samsung's
privacy features as solutions and contrasting them favorably against Meta. His Google
coverage (Feb 2026) is explicitly advocacy-positioned ("I'd buy Google's AI glasses
over Apple's AI pin any day") framing Google's mass data collection as a POSITIVE
("that data also translates into real-world understanding") while never raising privacy
concerns about Google glasses' identical camera capabilities. Meanwhile, at the SAME
publication, other journalists (Aamir Siddiqui, Chethan Rao) produce adversarial Meta
coverage with vocabulary like "spy gear," "controversial," "pervert."

Financial context: Android Authority (Jeronimo Media Group BV) depends structurally on
Google Search traffic, Google News inclusion, Google Display ads, and covers the
Google/Android ecosystem as its editorial mandate. Google is the direct PLATFORM PARTNER
for Samsung's Android XR glasses. Meta has $0 financial relationship with the publication.

Sources:
- https://www.androidauthority.com/samsung-smart-glasses-perverts-3693148/
- https://www.androidauthority.com/samsung-ar-glasses-launch-timeline-3636208/
- https://www.androidauthority.com/google-smart-glasses-vs-apple-ai-pin-3636278/
- https://www.androidauthority.com/halliday-ai-glasses-hands-on-3513126/
- https://www.androidauthority.com/cool-tech-mwc-2025-3532293/
- https://www.androidauthority.com/ray-ban-meta-stealth-mode-mod-3674350/
- https://www.androidauthority.com/author/HadleeSimons/
"""
import unittest
import yaml
import os
import re


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


class TestMechanismExists(unittest.TestCase):
    """Verify mechanism #183 exists and has required fields."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(183)

    def test_mechanism_found(self):
        self.assertIsNotNone(self.mechanism, "Mechanism #183 not found in YAML")

    def test_mechanism_id(self):
        self.assertEqual(self.mechanism['mechanism_id'], 183)

    def test_mechanism_name_contains_hadlee_simons(self):
        self.assertIn('Hadlee Simons', self.mechanism['mechanism_name'])

    def test_mechanism_name_contains_android_authority(self):
        self.assertIn('Android Authority', self.mechanism['mechanism_name'])

    def test_mechanism_type(self):
        mtype = self.mechanism['mechanism_type']
        self.assertIn('journalist', mtype)
        self.assertIn('cross_entity', mtype)

    def test_has_discovery_date(self):
        self.assertIn('discovery_date', self.mechanism)
        self.assertEqual(self.mechanism['discovery_date'], '2026-08-19')

    def test_has_source_urls(self):
        self.assertIn('source_urls', self.mechanism)
        self.assertGreater(len(self.mechanism['source_urls']), 5)

    def test_has_asymmetry_score(self):
        self.assertIn('asymmetry_score', self.mechanism)
        score = self.mechanism['asymmetry_score']
        self.assertGreaterEqual(score, 0.5)
        self.assertLessEqual(score, 1.0)

    def test_asymmetry_score_value(self):
        self.assertEqual(self.mechanism['asymmetry_score'], 0.78)


class TestJournalistProfile(unittest.TestCase):
    """Verify journalist profile captures Hadlee Simons' role and beat."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(183)
        cls.journalist = cls.mechanism.get('journalist', {})

    def test_journalist_name(self):
        self.assertEqual(self.journalist['name'], 'Hadlee Simons')

    def test_publication_android_authority(self):
        self.assertIn('Android Authority', self.journalist['publication'])

    def test_beat_includes_smart_glasses(self):
        beat = self.journalist['beat'].lower()
        self.assertTrue(
            'smart glasses' in beat or 'ar' in beat or 'xr' in beat,
            f"Beat should reference smart glasses/AR/XR: {beat}"
        )

    def test_role_describes_senior_position(self):
        role = self.journalist['role'].lower()
        self.assertTrue(
            'senior' in role or 'editor' in role,
            f"Role should describe senior editorial position: {role}"
        )

    def test_tenure_documented(self):
        self.assertIn('tenure_years', self.journalist)
        self.assertGreaterEqual(self.journalist['tenure_years'], 5)


class TestSamsungCoverageInventory(unittest.TestCase):
    """Verify Samsung coverage documents solution-oriented framing."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(183)
        cls.samsung = cls.mechanism.get('samsung_coverage', {})

    def test_samsung_articles_exist(self):
        articles = self.samsung.get('articles', [])
        self.assertGreaterEqual(len(articles), 2)

    def test_samsung_perverts_article_exists(self):
        articles = self.samsung.get('articles', [])
        perverts = [a for a in articles if 'perverts' in a.get('title', '').lower()]
        self.assertEqual(len(perverts), 1)

    def test_samsung_perverts_article_url(self):
        articles = self.samsung.get('articles', [])
        perverts = [a for a in articles if 'perverts' in a.get('title', '').lower()]
        self.assertIn('androidauthority.com', perverts[0]['url'])

    def test_samsung_perverts_framing_solution(self):
        articles = self.samsung.get('articles', [])
        perverts = [a for a in articles if 'perverts' in a.get('title', '').lower()]
        framing = perverts[0].get('framing', '').lower()
        self.assertTrue('solution' in framing, f"Samsung perverts article framing should be solution-oriented: {framing}")

    def test_samsung_zero_privacy_alarm_terms(self):
        articles = self.samsung.get('articles', [])
        for article in articles:
            alarm = article.get('privacy_alarm_terms_about_samsung', 99)
            self.assertEqual(alarm, 0, f"Samsung article should have 0 privacy alarm terms: {article.get('title', '')}")

    def test_samsung_aggregate_framing(self):
        framing = self.samsung.get('aggregate_framing', '').lower()
        self.assertIn('solution', framing)

    def test_samsung_privacy_investigations_zero(self):
        self.assertEqual(self.samsung.get('privacy_investigations'), 0)

    def test_samsung_meta_contrast_documented(self):
        articles = self.samsung.get('articles', [])
        perverts = [a for a in articles if 'perverts' in a.get('title', '').lower()]
        contrast = perverts[0].get('meta_contrast', '').lower()
        self.assertTrue('ire' in contrast or 'privacy advocates' in contrast,
                        f"Meta contrast should reference privacy advocates: {contrast}")


class TestGoogleCoverageInventory(unittest.TestCase):
    """Verify Google coverage documents explicit advocacy framing."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(183)
        cls.google = cls.mechanism.get('google_coverage', {})

    def test_google_articles_exist(self):
        articles = self.google.get('articles', [])
        self.assertGreaterEqual(len(articles), 1)

    def test_google_advocacy_article_exists(self):
        articles = self.google.get('articles', [])
        advocacy = [a for a in articles if "I'd buy" in a.get('title', '') or 'advocacy' in a.get('framing', '').lower()]
        self.assertGreater(len(advocacy), 0)

    def test_google_advocacy_framing(self):
        articles = self.google.get('articles', [])
        advocacy_articles = [a for a in articles if 'advocacy' in a.get('framing', '').lower()]
        self.assertGreater(len(advocacy_articles), 0)

    def test_google_zero_privacy_alarm_terms(self):
        articles = self.google.get('articles', [])
        for article in articles:
            alarm = article.get('privacy_alarm_terms_about_google', 99)
            self.assertEqual(alarm, 0, f"Google article should have 0 privacy alarm terms")

    def test_google_data_collection_framed_positive(self):
        articles = self.google.get('articles', [])
        advocacy = [a for a in articles if 'advocacy' in a.get('framing', '').lower()]
        if advocacy:
            dc_framing = advocacy[0].get('data_collection_framing', '').lower()
            self.assertIn('positive', dc_framing)

    def test_google_aggregate_framing_advocacy(self):
        framing = self.google.get('aggregate_framing', '').lower()
        self.assertIn('advocacy', framing)

    def test_google_privacy_investigations_zero(self):
        self.assertEqual(self.google.get('privacy_investigations'), 0)


class TestMetaCoverageAbsence(unittest.TestCase):
    """Verify Meta coverage documents the zero-article pattern."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(183)
        cls.meta = cls.mechanism.get('meta_coverage', {})

    def test_meta_solo_articles_zero(self):
        self.assertEqual(self.meta.get('solo_meta_privacy_articles'), 0)

    def test_meta_privacy_investigation_zero(self):
        self.assertEqual(self.meta.get('meta_privacy_investigation_articles'), 0)

    def test_meta_mentions_documented(self):
        self.assertIn('meta_mentions_in_samsung_articles', self.meta)
        mentions = self.meta['meta_mentions_in_samsung_articles'].lower()
        self.assertTrue('contrast' in mentions or 'ire' in mentions)

    def test_coverage_void_note(self):
        note = self.meta.get('note', '').lower()
        self.assertTrue('zero' in note or '0' in note,
                        f"Meta coverage note should document zero articles: {note}")


class TestSamePublicationMetaCoverage(unittest.TestCase):
    """Verify other Android Authority journalists' adversarial Meta coverage is documented."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(183)
        cls.same_pub = cls.mechanism.get('same_publication_meta_coverage', {})

    def test_other_journalists_documented(self):
        journalists = self.same_pub.get('journalists', [])
        self.assertGreaterEqual(len(journalists), 2)

    def test_aamir_siddiqui_documented(self):
        journalists = self.same_pub.get('journalists', [])
        aamir = [j for j in journalists if 'Aamir' in j.get('name', '') or 'Siddiqui' in j.get('name', '')]
        self.assertGreater(len(aamir), 0)

    def test_spy_gear_vocabulary_documented(self):
        journalists = self.same_pub.get('journalists', [])
        all_vocab = []
        for j in journalists:
            all_vocab.extend(j.get('vocabulary', []))
        spy_found = any('spy' in v.lower() for v in all_vocab)
        self.assertTrue(spy_found, "Should document 'spy gear' vocabulary from same-publication Meta coverage")

    def test_adversarial_vocabulary_present(self):
        journalists = self.same_pub.get('journalists', [])
        all_vocab = []
        for j in journalists:
            all_vocab.extend(j.get('vocabulary', []))
        self.assertGreater(len(all_vocab), 3, "Should have 3+ adversarial vocabulary terms from same-publication colleagues")


class TestVocabularyBifurcation(unittest.TestCase):
    """Verify the vocabulary bifurcation across entities is documented."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(183)
        cls.bifurcation = cls.mechanism.get('vocabulary_bifurcation', {})

    def test_samsung_register_solution(self):
        register = self.bifurcation.get('samsung_register', '').lower()
        self.assertIn('solution', register)

    def test_google_register_advocacy(self):
        register = self.bifurcation.get('google_register', '').lower()
        self.assertIn('advocacy', register)

    def test_meta_register_absent(self):
        register = self.bifurcation.get('meta_register', '').lower()
        self.assertTrue('absent' in register or 'void' in register or 'zero' in register,
                        f"Meta register should note absence: {register}")

    def test_delta_documents_contrast(self):
        delta = self.bifurcation.get('delta', '')
        self.assertTrue('0' in delta or 'zero' in delta,
                        f"Delta should document zero Meta articles: {delta}")

    def test_samsung_vocabulary_class_documented(self):
        vocab = self.bifurcation.get('samsung_vocabulary_class', '')
        self.assertGreater(len(vocab), 20)

    def test_google_vocabulary_class_documented(self):
        vocab = self.bifurcation.get('google_vocabulary_class', '')
        self.assertGreater(len(vocab), 20)


class TestFinancialContext(unittest.TestCase):
    """Verify financial context documents Google ecosystem dependency."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(183)
        cls.financial = cls.mechanism.get('financial_context', {})

    def test_android_authority_owner_documented(self):
        self.assertIn('android_authority_owner', self.financial)
        self.assertIn('Jeronimo', self.financial['android_authority_owner'])

    def test_google_relationship_documented(self):
        google_rel = self.financial.get('google_relationship', '')
        self.assertGreater(len(google_rel), 20)
        self.assertTrue('ecosystem' in google_rel.lower() or 'search' in google_rel.lower() or 'traffic' in google_rel.lower())

    def test_meta_zero_financial_relationship(self):
        meta_rel = self.financial.get('meta_financial_relationship', '')
        self.assertIn('$0', meta_rel)

    def test_android_xr_partnership_documented(self):
        xr = self.financial.get('google_android_xr_partnership', '')
        self.assertIn('Android XR', xr)
        self.assertIn('Samsung', xr)

    def test_note_references_structural_dependency(self):
        note = self.financial.get('note', '').lower()
        self.assertTrue(
            'structural' in note or 'dependency' in note or 'triple' in note,
            f"Financial note should reference structural dependency: {note}"
        )


class TestConfounders(unittest.TestCase):
    """Verify confounders are documented with rebuttals — 5 total, proper strength distribution."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(183)
        cls.confounders = cls.mechanism.get('confounders', [])

    def test_exactly_5_confounders(self):
        self.assertEqual(len(self.confounders), 5)

    def test_at_least_2_strong_confounders(self):
        strong = [c for c in self.confounders if c.get('strength') == 'STRONG']
        self.assertGreaterEqual(len(strong), 2)

    def test_at_least_2_moderate_confounders(self):
        moderate = [c for c in self.confounders if c.get('strength') == 'MODERATE']
        self.assertGreaterEqual(len(moderate), 2)

    def test_at_least_1_weak_confounder(self):
        weak = [c for c in self.confounders if c.get('strength') == 'WEAK']
        self.assertGreaterEqual(len(weak), 1)

    def test_all_confounders_have_rebuttals(self):
        for c in self.confounders:
            self.assertIn('rebuttal', c, f"Confounder missing rebuttal: {c.get('description', '')[:50]}")
            self.assertGreater(len(c['rebuttal']), 30)

    def test_android_ecosystem_confounder_exists(self):
        descriptions = [c.get('description', '').lower() for c in self.confounders]
        ecosystem = any('android' in d or 'ecosystem' in d or 'mandate' in d for d in descriptions)
        self.assertTrue(ecosystem, "Should have an Android ecosystem focus confounder")

    def test_meta_track_record_confounder_exists(self):
        descriptions = [c.get('description', '').lower() for c in self.confounders]
        track_record = any('track record' in d or 'cambridge' in d or 'kenya' in d for d in descriptions)
        self.assertTrue(track_record, "Should have a Meta track record confounder")


class TestCrossReferences(unittest.TestCase):
    """Verify cross-references to related mechanisms."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(183)
        cls.cross_refs = cls.mechanism.get('cross_references', [])

    def test_at_least_3_cross_references(self):
        self.assertGreaterEqual(len(self.cross_refs), 3)

    def test_mechanism_179_referenced(self):
        """Mechanism #179 = Matt Wille/Gizmodo beat reporter vocabulary bifurcation"""
        ref_ids = [r.get('mechanism_id') for r in self.cross_refs]
        self.assertIn(179, ref_ids)

    def test_mechanism_109_referenced(self):
        """Mechanism #109 = Engadget/Yahoo Google partnership financial dependency"""
        ref_ids = [r.get('mechanism_id') for r in self.cross_refs]
        self.assertIn(109, ref_ids)

    def test_mechanism_76_referenced(self):
        """Mechanism #76 = Samsung-Google Compound Advertiser Leverage"""
        ref_ids = [r.get('mechanism_id') for r in self.cross_refs]
        self.assertIn(76, ref_ids)

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
        self.assertIn('test_hadlee_simons_android_authority', content)

    def test_architecture_lists_test_file(self):
        arch_path = os.path.join(os.path.dirname(__file__), '..', 'docs', 'ARCHITECTURE.md')
        with open(arch_path, 'r') as f:
            content = f.read()
        self.assertIn('test_hadlee_simons_android_authority', content)

    def test_test_file_path_in_mechanism(self):
        mechanism = find_mechanism_anywhere(183)
        test_file = mechanism.get('test_file', '')
        self.assertIn('hadlee_simons_android_authority', test_file)

    def test_test_count_in_mechanism(self):
        mechanism = find_mechanism_anywhere(183)
        count = mechanism.get('test_count', 0)
        self.assertGreater(count, 0)


if __name__ == '__main__':
    unittest.main()
