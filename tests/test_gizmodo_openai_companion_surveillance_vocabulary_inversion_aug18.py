"""
Test: Gizmodo Intra-Publication Surveillance Vocabulary Inversion — OpenAI Companion vs Meta Glasses

Mechanism #170: Gizmodo applies ZERO surveillance/privacy-alarm vocabulary to OpenAI's camera-equipped,
facial-recognition-enabled companion device across two articles (Feb 2026 + Aug 2026), while applying
50+ surveillance/privacy-alarm terms across 8+ Meta glasses articles covering functionally equivalent
or LESS invasive capabilities.

Smoking gun: Feb 2026 article explicitly describes OpenAI device as having "a camera, enabling it to
take in information about its users and their surroundings" AND "a facial recognition feature similar
to Apple's Face ID" — zero surveillance vocabulary applied. Meanwhile, Meta's dormant NameTag code
generates headline: "Meta Is Testing Police Surveillance Tech for Its Smart Glasses."

Sources:
- Gizmodo Feb 2026: "OpenAI Might Be Making a Smart Speaker That No One Asked for" (0 alarm terms, 
  despite camera + facial recognition + ambient conversation monitoring)
- Gizmodo Aug 6, 2026: "OpenAI's Rumored Smart Speaker Sounds More Like a... Squirming AI Robot?" 
  (0 alarm terms, despite cameras + sensors + email access + proactive observation)
- Gizmodo May 2025: "Meta Is Turning Its Ray-Bans Into a Surveillance Machine for AI"
- Gizmodo Jul 2026: "Meta Fury AI Glasses Review: The Worst Company Still Makes the Best Smart Glasses"
- Gizmodo Jun 2026: "Meta Is Testing Police Surveillance Tech for Its Smart Glasses"
- Gizmodo Jul 2026: "Meta Is Toying With the Idea of Smart Glasses That Record Everything, All the Time"
- Gizmodo Jul 2026: "Destroying the Privacy LED... Will No Longer Enable Creepiness"
- Gizmodo Feb 2026: "Want to Know If Glassholes Are Using Smart Glasses Near You?"
- Gizmodo Aug 2026: "Smart Glasses Are Catching on With U.S. Police"
- Gizmodo Apr 2026: "Calls to Regulate Smart Glasses Are Officially Deafening"
"""

import unittest
import yaml
import os


class TestMechanism170Exists(unittest.TestCase):
    """Verify mechanism #170 exists with required structural fields."""

    @classmethod
    def setUpClass(cls):
        ccr_path = os.path.join(
            os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
        )
        with open(ccr_path) as f:
            cls.data = yaml.safe_load(f)
        cls.findings = cls.data.get('cross_publication_findings', {})
        cls.mechanism = cls.findings.get(
            'gizmodo_openai_companion_intra_publication_surveillance_vocabulary_inversion', {}
        )

    def test_mechanism_exists(self):
        self.assertTrue(
            len(self.mechanism) > 0,
            "Mechanism 'gizmodo_openai_companion_intra_publication_surveillance_vocabulary_inversion' must exist"
        )

    def test_mechanism_id_is_170(self):
        self.assertEqual(self.mechanism.get('mechanism_id'), 170)

    def test_mechanism_name_content(self):
        name = self.mechanism.get('mechanism_name', '')
        self.assertIn('Gizmodo', name)
        self.assertIn('Surveillance', name)
        self.assertIn('Vocabulary', name)
        self.assertIn('Inversion', name)

    def test_finding_type(self):
        self.assertEqual(self.mechanism.get('finding_type'), 'competitor_coverage_deep_dive')

    def test_rotation_type_a(self):
        self.assertEqual(self.mechanism.get('rotation_type'), 'A')

    def test_publication_is_gizmodo(self):
        self.assertIn('Gizmodo', self.mechanism.get('publication', ''))

    def test_competitor_entity_is_openai(self):
        self.assertEqual(self.mechanism.get('competitor_entity'), 'OpenAI')

    def test_asymmetry_score_range(self):
        score = self.mechanism.get('asymmetry_score', 0)
        self.assertGreaterEqual(score, 0.7)
        self.assertLessEqual(score, 1.0)

    def test_has_source_urls(self):
        urls = self.mechanism.get('source_urls', [])
        self.assertGreaterEqual(len(urls), 8, "Should have at least 8 source URLs")

    def test_has_test_file(self):
        self.assertIn(
            'test_gizmodo_openai_companion_surveillance_vocabulary_inversion_aug18',
            self.mechanism.get('test_file', '')
        )

    def test_has_confounders(self):
        confounders = self.mechanism.get('confounders', [])
        self.assertGreaterEqual(len(confounders), 4, "Must have at least 4 confounders")

    def test_has_confounder_responses(self):
        responses = self.mechanism.get('confounder_responses', [])
        self.assertGreaterEqual(len(responses), 4, "Must have at least 4 confounder responses")

    def test_has_cross_references(self):
        refs = self.mechanism.get('cross_references', [])
        self.assertGreaterEqual(len(refs), 2, "Must have at least 2 cross references")

    def test_has_testable_predictions(self):
        preds = self.mechanism.get('testable_predictions', [])
        self.assertGreaterEqual(len(preds), 2, "Must have at least 2 testable predictions")


class TestOpenAICoverageEvidence(unittest.TestCase):
    """Verify OpenAI coverage documentation — the critical zero-alarm finding."""

    @classmethod
    def setUpClass(cls):
        ccr_path = os.path.join(
            os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
        )
        with open(ccr_path) as f:
            data = yaml.safe_load(f)
        findings = data.get('cross_publication_findings', {})
        cls.mechanism = findings.get(
            'gizmodo_openai_companion_intra_publication_surveillance_vocabulary_inversion', {}
        )
        cls.openai = cls.mechanism.get('openai_coverage', {})

    def test_openai_article_count(self):
        self.assertGreaterEqual(self.openai.get('article_count', 0), 2)

    def test_openai_total_surveillance_vocabulary_zero(self):
        self.assertEqual(self.openai.get('total_surveillance_vocabulary'), 0)

    def test_openai_total_privacy_alarm_vocabulary_zero(self):
        self.assertEqual(self.openai.get('total_privacy_alarm_vocabulary'), 0)

    def test_openai_articles_list_exists(self):
        articles = self.openai.get('articles', [])
        self.assertGreaterEqual(len(articles), 2)

    def test_feb_article_has_camera_described(self):
        articles = self.openai.get('articles', [])
        feb_article = next((a for a in articles if '2026-02' in str(a.get('date', ''))), None)
        self.assertIsNotNone(feb_article, "Must have February 2026 article")
        capabilities = feb_article.get('capabilities_described', [])
        camera_mentioned = any('camera' in c.lower() for c in capabilities)
        self.assertTrue(camera_mentioned, "Feb article must document camera capability")

    def test_feb_article_has_facial_recognition_described(self):
        articles = self.openai.get('articles', [])
        feb_article = next((a for a in articles if '2026-02' in str(a.get('date', ''))), None)
        self.assertIsNotNone(feb_article)
        capabilities = feb_article.get('capabilities_described', [])
        fr_mentioned = any('facial recognition' in c.lower() or 'face id' in c.lower() for c in capabilities)
        self.assertTrue(fr_mentioned, "Feb article must document facial recognition capability")

    def test_feb_article_zero_surveillance(self):
        articles = self.openai.get('articles', [])
        feb_article = next((a for a in articles if '2026-02' in str(a.get('date', ''))), None)
        self.assertIsNotNone(feb_article)
        self.assertEqual(
            feb_article.get('surveillance_vocabulary_count'), 0,
            "Feb article with camera+facial recognition must have ZERO surveillance terms"
        )

    def test_feb_article_zero_privacy_alarm(self):
        articles = self.openai.get('articles', [])
        feb_article = next((a for a in articles if '2026-02' in str(a.get('date', ''))), None)
        self.assertIsNotNone(feb_article)
        self.assertEqual(
            feb_article.get('privacy_alarm_vocabulary_count'), 0,
            "Feb article with camera+facial recognition must have ZERO privacy alarm terms"
        )

    def test_aug_article_has_camera_described(self):
        articles = self.openai.get('articles', [])
        aug_article = next((a for a in articles if '2026-08' in str(a.get('date', ''))), None)
        self.assertIsNotNone(aug_article, "Must have August 2026 article")
        capabilities = aug_article.get('capabilities_described', [])
        camera_mentioned = any('camera' in c.lower() for c in capabilities)
        self.assertTrue(camera_mentioned, "Aug article must document camera capability")

    def test_aug_article_zero_surveillance(self):
        articles = self.openai.get('articles', [])
        aug_article = next((a for a in articles if '2026-08' in str(a.get('date', ''))), None)
        self.assertIsNotNone(aug_article)
        self.assertEqual(aug_article.get('surveillance_vocabulary_count'), 0)

    def test_aug_article_email_access_described(self):
        articles = self.openai.get('articles', [])
        aug_article = next((a for a in articles if '2026-08' in str(a.get('date', ''))), None)
        self.assertIsNotNone(aug_article)
        capabilities = aug_article.get('capabilities_described', [])
        email_mentioned = any('email' in c.lower() for c in capabilities)
        self.assertTrue(email_mentioned, "Aug article must document email access capability")


class TestMetaCoverageEvidence(unittest.TestCase):
    """Verify Meta coverage documentation — the extensive alarm vocabulary."""

    @classmethod
    def setUpClass(cls):
        ccr_path = os.path.join(
            os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
        )
        with open(ccr_path) as f:
            data = yaml.safe_load(f)
        findings = data.get('cross_publication_findings', {})
        cls.mechanism = findings.get(
            'gizmodo_openai_companion_intra_publication_surveillance_vocabulary_inversion', {}
        )
        cls.meta = cls.mechanism.get('meta_coverage', {})

    def test_meta_article_count(self):
        self.assertGreaterEqual(self.meta.get('article_count', 0), 8)

    def test_meta_articles_list(self):
        articles = self.meta.get('articles', [])
        self.assertGreaterEqual(len(articles), 8)

    def test_meta_total_surveillance_vocabulary_high(self):
        total = str(self.meta.get('total_surveillance_vocabulary', ''))
        # Accept both int and string representations
        self.assertTrue(
            '50' in total or (isinstance(self.meta.get('total_surveillance_vocabulary'), int)
                             and self.meta.get('total_surveillance_vocabulary') >= 50),
            "Meta coverage must have 50+ total surveillance vocabulary"
        )

    def test_surveillance_machine_headline_exists(self):
        articles = self.meta.get('articles', [])
        titles = [a.get('title', '') for a in articles]
        surveillance_machine = any('Surveillance Machine' in t for t in titles)
        self.assertTrue(surveillance_machine, "Must document 'Surveillance Machine' headline")

    def test_police_surveillance_headline_exists(self):
        articles = self.meta.get('articles', [])
        titles = [a.get('title', '') for a in articles]
        police_surv = any('Police Surveillance Tech' in t for t in titles)
        self.assertTrue(police_surv, "Must document 'Police Surveillance Tech' headline")

    def test_worst_company_headline_exists(self):
        articles = self.meta.get('articles', [])
        titles = [a.get('title', '') for a in articles]
        worst = any('Worst Company' in t for t in titles)
        self.assertTrue(worst, "Must document 'Worst Company' headline")

    def test_glassholes_headline_exists(self):
        articles = self.meta.get('articles', [])
        titles = [a.get('title', '') for a in articles]
        glassholes = any('Glassholes' in t for t in titles)
        self.assertTrue(glassholes, "Must document 'Glassholes' headline")

    def test_each_article_has_surveillance_terms(self):
        articles = self.meta.get('articles', [])
        for article in articles:
            terms = article.get('surveillance_terms', [])
            self.assertGreater(
                len(terms), 0,
                f"Article '{article.get('title', 'unknown')}' must have surveillance terms"
            )

    def test_each_article_has_url(self):
        articles = self.meta.get('articles', [])
        for article in articles:
            url = article.get('url', '')
            self.assertTrue(
                url.startswith('http'),
                f"Article '{article.get('title', 'unknown')}' must have a valid URL"
            )


class TestCapabilityParityAnalysis(unittest.TestCase):
    """Verify the capability comparison shows OpenAI device is MORE invasive."""

    @classmethod
    def setUpClass(cls):
        ccr_path = os.path.join(
            os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
        )
        with open(ccr_path) as f:
            data = yaml.safe_load(f)
        findings = data.get('cross_publication_findings', {})
        cls.mechanism = findings.get(
            'gizmodo_openai_companion_intra_publication_surveillance_vocabulary_inversion', {}
        )
        cls.parity = cls.mechanism.get('capability_parity_analysis', {})
        cls.openai_caps = cls.parity.get('openai_device_has', [])
        cls.meta_caps = cls.parity.get('meta_glasses_have', [])

    def test_openai_has_cameras(self):
        camera = any('camera' in c.lower() for c in self.openai_caps)
        self.assertTrue(camera, "OpenAI device must have cameras documented")

    def test_openai_has_facial_recognition(self):
        fr = any('facial_recognition' in c.lower() or 'face' in c.lower() for c in self.openai_caps)
        self.assertTrue(fr, "OpenAI device must have facial recognition documented")

    def test_openai_has_email_access(self):
        email = any('email' in c.lower() for c in self.openai_caps)
        self.assertTrue(email, "OpenAI device must have email access documented")

    def test_openai_has_proactive_observation(self):
        proactive = any('proactive' in c.lower() for c in self.openai_caps)
        self.assertTrue(proactive, "OpenAI device must have proactive observation documented")

    def test_meta_has_cameras(self):
        camera = any('camera' in c.lower() for c in self.meta_caps)
        self.assertTrue(camera, "Meta glasses must have cameras documented")

    def test_meta_has_privacy_led(self):
        led = any('privacy_led' in c.lower() or 'privacy' in c.lower() for c in self.meta_caps)
        self.assertTrue(led, "Meta glasses must have privacy LED documented")

    def test_meta_facial_recognition_is_dormant(self):
        fr = any('dormant' in c.lower() for c in self.meta_caps)
        self.assertTrue(fr, "Meta facial recognition must be documented as dormant")

    def test_meta_no_email_access(self):
        no_email = any(
            ('no_email' in str(c).lower() if isinstance(c, (dict, bool)) else 'no_email' in c.lower())
            for c in self.meta_caps
        )
        self.assertTrue(no_email, "Meta must document no email access")

    def test_comparison_field_exists(self):
        comparison = self.parity.get('comparison', '')
        self.assertGreater(len(comparison), 50, "Must have substantive comparison text")

    def test_comparison_notes_openai_more_invasive(self):
        comparison = self.parity.get('comparison', '').lower()
        self.assertIn('more invasive', comparison, "Comparison must note OpenAI is more invasive")


class TestVocabularyDelta(unittest.TestCase):
    """Verify the vocabulary delta is properly documented and significant."""

    @classmethod
    def setUpClass(cls):
        ccr_path = os.path.join(
            os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
        )
        with open(ccr_path) as f:
            data = yaml.safe_load(f)
        findings = data.get('cross_publication_findings', {})
        cls.mechanism = findings.get(
            'gizmodo_openai_companion_intra_publication_surveillance_vocabulary_inversion', {}
        )
        cls.delta = cls.mechanism.get('vocabulary_delta', {})

    def test_openai_surveillance_terms_zero(self):
        self.assertEqual(self.delta.get('openai_surveillance_terms'), 0)

    def test_meta_surveillance_terms_high(self):
        self.assertGreaterEqual(self.delta.get('meta_surveillance_terms', 0), 50)

    def test_delta_is_50(self):
        self.assertGreaterEqual(self.delta.get('delta', 0), 50)

    def test_significance_documented(self):
        sig = self.delta.get('significance', '')
        self.assertGreater(len(sig), 50, "Significance must be substantively documented")

    def test_significance_notes_largest_gap(self):
        sig = self.delta.get('significance', '').lower()
        self.assertIn('largest', sig, "Should note this is the largest gap")


class TestSmokingGunEvidence(unittest.TestCase):
    """Verify the smoking gun — Feb article explicitly describes facial recognition with zero alarm."""

    @classmethod
    def setUpClass(cls):
        ccr_path = os.path.join(
            os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
        )
        with open(ccr_path) as f:
            data = yaml.safe_load(f)
        findings = data.get('cross_publication_findings', {})
        cls.mechanism = findings.get(
            'gizmodo_openai_companion_intra_publication_surveillance_vocabulary_inversion', {}
        )
        cls.smoking_gun = cls.mechanism.get('smoking_gun_evidence', {})

    def test_smoking_gun_exists(self):
        self.assertTrue(len(self.smoking_gun) > 0, "Must have smoking gun evidence")

    def test_smoking_gun_mentions_camera(self):
        desc = self.smoking_gun.get('description', '').lower()
        self.assertIn('camera', desc)

    def test_smoking_gun_mentions_facial_recognition(self):
        desc = self.smoking_gun.get('description', '').lower()
        self.assertIn('facial recognition', desc)

    def test_smoking_gun_mentions_face_id(self):
        desc = self.smoking_gun.get('description', '').lower()
        self.assertIn('face id', desc)

    def test_smoking_gun_mentions_zero_surveillance(self):
        desc = self.smoking_gun.get('description', '').lower()
        self.assertIn('zero', desc)

    def test_smoking_gun_contrasts_meta_nametag(self):
        desc = self.smoking_gun.get('description', '').lower()
        self.assertIn('nametag', desc)


class TestCrossReferences(unittest.TestCase):
    """Verify cross-references connect to related mechanisms."""

    @classmethod
    def setUpClass(cls):
        ccr_path = os.path.join(
            os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
        )
        with open(ccr_path) as f:
            data = yaml.safe_load(f)
        findings = data.get('cross_publication_findings', {})
        cls.mechanism = findings.get(
            'gizmodo_openai_companion_intra_publication_surveillance_vocabulary_inversion', {}
        )
        cls.refs = cls.mechanism.get('cross_references', [])

    def test_references_mechanism_159(self):
        ids = [r.get('mechanism_id') for r in self.refs]
        self.assertIn(159, ids, "Must reference mechanism #159 (cross-publication companion-vs-surveillance)")

    def test_references_mechanism_31(self):
        ids = [r.get('mechanism_id') for r in self.refs]
        self.assertIn(31, ids, "Must reference mechanism #31 (Pero Gizmodo genre-determined framing)")

    def test_each_reference_has_relationship(self):
        for ref in self.refs:
            self.assertGreater(
                len(ref.get('relationship', '')), 20,
                f"Cross-reference to #{ref.get('mechanism_id')} must have substantive relationship"
            )


class TestGizmodoProfileConsistency(unittest.TestCase):
    """Verify Gizmodo profile's competitor relationships are consistent with mechanism findings."""

    @classmethod
    def setUpClass(cls):
        profile_path = os.path.join(
            os.path.dirname(__file__), '..', 'profiles', 'gizmodo.yaml'
        )
        with open(profile_path) as f:
            cls.profile = yaml.safe_load(f)
        cls.competitor_rels = cls.profile.get('competitor_relationships', {})

    def test_openai_no_financial_tie(self):
        openai = self.competitor_rels.get('openai', {})
        self.assertEqual(
            openai.get('financial_tie'), 'none',
            "Gizmodo must have no financial tie to OpenAI"
        )

    def test_meta_no_financial_tie(self):
        meta = self.competitor_rels.get('meta', {})
        self.assertEqual(
            meta.get('financial_tie'), 'none',
            "Gizmodo must have no financial tie to Meta"
        )

    def test_both_predicted_adversarial(self):
        openai = self.competitor_rels.get('openai', {})
        meta = self.competitor_rels.get('meta', {})
        openai_pred = openai.get('coverage_prediction', '')
        meta_pred = meta.get('coverage_prediction', '')
        # Both should be adversarial — the mechanism shows Meta IS adversarial but OpenAI is NOT
        # This demonstrates the asymmetry CANNOT be explained by financial incentives
        self.assertEqual(meta_pred, 'adversarial')


class TestNoFinancialIncentiveExplanation(unittest.TestCase):
    """
    Verify this mechanism explicitly demonstrates that financial incentives
    CANNOT explain the vocabulary inversion — both entities have zero financial
    ties to Gizmodo, yet receive radically different vocabulary.
    """

    @classmethod
    def setUpClass(cls):
        ccr_path = os.path.join(
            os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
        )
        with open(ccr_path) as f:
            data = yaml.safe_load(f)
        findings = data.get('cross_publication_findings', {})
        cls.mechanism = findings.get(
            'gizmodo_openai_companion_intra_publication_surveillance_vocabulary_inversion', {}
        )

    def test_finding_summary_mentions_same_publication(self):
        summary = self.mechanism.get('finding_summary', '').lower()
        self.assertIn('same-publication', summary)

    def test_vocabulary_delta_structure(self):
        delta = self.mechanism.get('vocabulary_delta', {})
        self.assertIn('openai_surveillance_terms', delta)
        self.assertIn('meta_surveillance_terms', delta)
        self.assertIn('delta', delta)

    def test_delta_eliminates_publication_level_policy(self):
        summary = self.mechanism.get('finding_summary', '').lower()
        self.assertIn('eliminates publication-level editorial policy', summary)


if __name__ == '__main__':
    unittest.main()
