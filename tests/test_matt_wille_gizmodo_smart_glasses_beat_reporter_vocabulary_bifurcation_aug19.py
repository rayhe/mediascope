"""
Test Mechanism #179: Matt Wille (Gizmodo) Smart Glasses Beat Reporter —
8+ Solo Meta Adversarial Articles vs Zero Solo Samsung Privacy Investigation

Type B: Journalist Cross-Entity Tracking

Core finding: Matt Wille, Gizmodo's dedicated smart glasses beat reporter, has published
8+ solo-bylined Meta smart glasses articles with heavy adversarial privacy vocabulary
(Glasshole 2.0, stalk, surveillance, liability, torpedoed, fumbling) while publishing
ZERO solo-bylined Samsung Galaxy Glasses privacy investigations. His only Samsung
coverage is a co-authored Galaxy Unpacked live update where his contribution uses
aspirational vocabulary ("corner the market on fashionable consumers"). Same journalist,
same hardware capabilities, opposite editorial registers.

This is the first documented case of a BEAT REPORTER — someone who has self-selected
into the smart glasses category as their editorial specialty — showing systematic zero
cross-entity privacy investigation over 11+ months and 8+ articles. Previous journalist
mechanisms documented individual articles or career-arc patterns. This mechanism documents
a COMPLETE BEAT-LEVEL EDITORIAL AGENDA.

Sources:
- https://gizmodo.com/meta-has-smart-glasses-spiraling-towards-glasshole-2-0-2000733361
- https://gizmodo.com/meta-thinks-its-smart-glasses-could-stalk-people-in-a-thoughtful-way-2000746222
- https://gizmodo.com/did-meta-just-accidentally-prove-smart-glasses-are-a-liability-2000725585
- https://gizmodo.com/buckle-up-the-smart-glasses-backlash-is-coming-2000668213
- https://gizmodo.com/we-need-to-talk-about-smart-glasses-2000661487
- https://gizmodo.com/can-smart-glasses-ever-be-privacy-friendly-these-companies-think-so-2000746927
- https://gizmodo.com/smart-glasses-are-a-hit-even-as-privacy-concerns-pile-up-2000792911
- https://gizmodo.com/metas-ray-bans-arent-the-only-smart-glasses-with-a-glasshole-problem-2000770193
- https://gizmodo.com/live-updates-from-samsungs-july-2026-galaxy-unpacked-2000785539
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
    """Verify mechanism #179 exists and has required fields."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(179)

    def test_mechanism_found(self):
        self.assertIsNotNone(self.mechanism, "Mechanism #179 not found in YAML")

    def test_mechanism_id(self):
        self.assertEqual(self.mechanism['mechanism_id'], 179)

    def test_mechanism_name_contains_matt_wille(self):
        self.assertIn('Matt Wille', self.mechanism['mechanism_name'])

    def test_mechanism_name_contains_gizmodo(self):
        self.assertIn('Gizmodo', self.mechanism['mechanism_name'])

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


class TestJournalistProfile(unittest.TestCase):
    """Verify journalist profile captures beat reporter status."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(179)
        cls.journalist = cls.mechanism.get('journalist', {})

    def test_journalist_name(self):
        self.assertEqual(self.journalist['name'], 'Matt Wille')

    def test_publication_gizmodo(self):
        self.assertIn('Gizmodo', self.journalist['publication'])

    def test_beat_smart_glasses(self):
        beat = self.journalist['beat'].lower()
        self.assertTrue(
            'smart glasses' in beat or 'wearable' in beat,
            f"Beat should reference smart glasses/wearables: {beat}"
        )

    def test_role_describes_beat_reporter(self):
        role = self.journalist['role'].lower()
        self.assertTrue(
            'beat' in role or 'dedicated' in role or 'prolific' in role,
            f"Role should describe dedicated beat coverage: {role}"
        )


class TestMetaCoverageInventory(unittest.TestCase):
    """Verify Meta coverage inventory has 8+ articles with adversarial framing."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(179)
        cls.meta = cls.mechanism.get('meta_coverage', {})

    def test_meta_article_count_at_least_8(self):
        count = self.meta.get('article_count', '')
        # Accept string like "8+" or integer >= 8
        if isinstance(count, str):
            num = int(re.search(r'\d+', count).group())
        else:
            num = count
        self.assertGreaterEqual(num, 8)

    def test_meta_framing_adversarial(self):
        framing = self.meta.get('framing', '').lower()
        self.assertTrue(
            'adversarial' in framing or 'alarm' in framing,
            f"Meta framing should be adversarial/alarm: {framing}"
        )

    def test_meta_articles_have_urls(self):
        articles = self.meta.get('articles', [])
        self.assertGreater(len(articles), 0)
        for article in articles:
            self.assertIn('url', article)
            self.assertTrue(article['url'].startswith('http'))

    def test_meta_articles_have_vocabulary(self):
        articles = self.meta.get('articles', [])
        for article in articles:
            self.assertTrue(
                'vocabulary' in article or 'framing_note' in article,
                f"Article {article.get('title', 'unknown')} should have vocabulary or framing_note"
            )

    def test_meta_aggregate_alarm_terms_exist(self):
        terms = self.meta.get('aggregate_alarm_terms', [])
        self.assertGreater(len(terms), 10, "Should have 10+ aggregate alarm terms")

    def test_glasshole_in_alarm_terms(self):
        terms = self.meta.get('aggregate_alarm_terms', [])
        glasshole_found = any('glasshole' in t.lower() for t in terms)
        self.assertTrue(glasshole_found, "Glasshole should be in alarm terms")

    def test_stalk_in_alarm_terms(self):
        terms = self.meta.get('aggregate_alarm_terms', [])
        stalk_found = any('stalk' in t.lower() for t in terms)
        self.assertTrue(stalk_found, "'stalk' should be in alarm terms")

    def test_surveillance_in_alarm_terms(self):
        terms = self.meta.get('aggregate_alarm_terms', [])
        surv_found = any('surveillance' in t.lower() for t in terms)
        self.assertTrue(surv_found, "'surveillance' should be in alarm terms")

    def test_average_tone_score_negative(self):
        score = self.meta.get('average_tone_score', 0)
        self.assertLess(score, 0, "Average tone for Meta should be negative")


class TestSamsungCoverageAbsence(unittest.TestCase):
    """Verify Samsung coverage documents the zero-investigation pattern."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(179)
        cls.samsung = cls.mechanism.get('samsung_coverage', {})

    def test_samsung_solo_article_count_zero(self):
        self.assertEqual(self.samsung.get('solo_article_count'), 0)

    def test_samsung_privacy_investigation_false(self):
        self.assertFalse(self.samsung.get('samsung_privacy_investigation'))

    def test_samsung_mentions_in_meta_articles_documented(self):
        self.assertIn('samsung_mentions_in_meta_articles', self.samsung)
        mentions = self.samsung['samsung_mentions_in_meta_articles'].lower()
        self.assertIn('zero', mentions)

    def test_co_authored_coverage_exists(self):
        co_auth = self.samsung.get('co_authored_coverage', {})
        self.assertIn('samsung_unpacked_live_updates', co_auth)

    def test_co_authored_tone_aspirational(self):
        co_auth = self.samsung.get('co_authored_coverage', {})
        unpacked = co_auth.get('samsung_unpacked_live_updates', {})
        self.assertEqual(unpacked.get('tone'), 'aspirational')

    def test_co_authored_privacy_alarm_terms_zero(self):
        co_auth = self.samsung.get('co_authored_coverage', {})
        unpacked = co_auth.get('samsung_unpacked_live_updates', {})
        self.assertEqual(unpacked.get('privacy_alarm_terms'), 0)

    def test_wille_samsung_contribution_documented(self):
        co_auth = self.samsung.get('co_authored_coverage', {})
        unpacked = co_auth.get('samsung_unpacked_live_updates', {})
        contrib = unpacked.get('wille_contribution', '')
        self.assertIn('fashionable', contrib.lower())


class TestVocabularyBifurcation(unittest.TestCase):
    """Verify the vocabulary bifurcation is documented with evidence."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(179)
        cls.bifurcation = cls.mechanism.get('vocabulary_bifurcation', {})

    def test_meta_register_adversarial(self):
        self.assertEqual(self.bifurcation.get('meta_register'), 'adversarial')

    def test_samsung_register_aspirational(self):
        self.assertEqual(self.bifurcation.get('samsung_register'), 'aspirational')

    def test_meta_vocabulary_class_has_alarm_terms(self):
        vocab = self.bifurcation.get('meta_vocabulary_class', '').lower()
        self.assertTrue(
            'alarm' in vocab or 'stigmatiz' in vocab or 'glasshole' in vocab,
            f"Meta vocabulary class should reference alarm/stigmatization: {vocab}"
        )

    def test_samsung_vocabulary_class_has_aspiration_terms(self):
        vocab = self.bifurcation.get('samsung_vocabulary_class', '').lower()
        self.assertTrue(
            'aspiration' in vocab or 'fashion' in vocab,
            f"Samsung vocabulary class should reference aspiration/fashion: {vocab}"
        )

    def test_delta_documents_contrast(self):
        delta = self.bifurcation.get('delta', '')
        self.assertIn('0', delta, "Delta should mention zero Samsung articles")


class TestRokidExtensionParadox(unittest.TestCase):
    """Verify the Rokid extension paradox is documented — extending to small Chinese brand but not Samsung."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(179)

    def test_rokid_paradox_documented(self):
        self.assertIn('rokid_extension_paradox', self.mechanism)

    def test_rokid_paradox_mentions_samsung(self):
        paradox = self.mechanism['rokid_extension_paradox'].lower()
        self.assertIn('samsung', paradox)

    def test_rokid_paradox_mentions_rokid(self):
        paradox = self.mechanism['rokid_extension_paradox'].lower()
        self.assertIn('rokid', paradox)

    def test_rokid_paradox_contrasts_market_presence(self):
        paradox = self.mechanism['rokid_extension_paradox'].lower()
        self.assertTrue(
            'market' in paradox or '100x' in paradox,
            "Should contrast Rokid vs Samsung market presence"
        )


class TestFinancialContext(unittest.TestCase):
    """Verify financial context is documented — Gizmodo has no direct financial incentive."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(179)
        cls.financial = cls.mechanism.get('financial_context', {})

    def test_gizmodo_ownership_documented(self):
        self.assertIn('gizmodo_ownership', self.financial)
        self.assertIn('Keleops', self.financial['gizmodo_ownership'])

    def test_meta_zero_financial_relationship(self):
        meta_rel = self.financial.get('meta_financial_relationship', '')
        self.assertIn('$0', meta_rel)

    def test_no_direct_financial_incentive_noted(self):
        note = self.financial.get('note', '').lower()
        self.assertTrue(
            'cultural' in note or 'consensus' in note or 'no documented' in note,
            "Note should reference cultural consensus rather than financial capture"
        )


class TestConfounders(unittest.TestCase):
    """Verify confounders are documented with rebuttals."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(179)
        cls.confounders = cls.mechanism.get('confounders', [])

    def test_at_least_4_confounders(self):
        self.assertGreaterEqual(len(self.confounders), 4)

    def test_at_least_2_strong_confounders(self):
        strong = [c for c in self.confounders if c.get('strength') == 'STRONG']
        self.assertGreaterEqual(len(strong), 2)

    def test_all_confounders_have_rebuttals(self):
        for c in self.confounders:
            self.assertIn('rebuttal', c, f"Confounder missing rebuttal: {c.get('description', '')[:50]}")
            self.assertGreater(len(c['rebuttal']), 20)

    def test_meta_track_record_confounder_exists(self):
        descriptions = [c['description'].lower() for c in self.confounders]
        track_record = any('track record' in d or 'incidents' in d or 'kenya' in d for d in descriptions)
        self.assertTrue(track_record, "Should have a Meta track record confounder")

    def test_market_share_confounder_exists(self):
        descriptions = [c['description'].lower() for c in self.confounders]
        market = any('market' in d or 'leader' in d or '80%' in d for d in descriptions)
        self.assertTrue(market, "Should have a market share confounder")


class TestCrossReferences(unittest.TestCase):
    """Verify cross-references to related mechanisms."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(179)
        cls.cross_refs = cls.mechanism.get('cross_references', [])

    def test_at_least_3_cross_references(self):
        self.assertGreaterEqual(len(self.cross_refs), 3)

    def test_mechanism_170_referenced(self):
        """Mechanism #170 = Gizmodo OpenAI companion vocabulary inversion"""
        ref_ids = [r.get('mechanism_id') for r in self.cross_refs]
        self.assertIn(170, ref_ids)

    def test_mechanism_160_referenced(self):
        """Mechanism #160 = Nadeem Sarwar editorial hierarchy"""
        ref_ids = [r.get('mechanism_id') for r in self.cross_refs]
        self.assertIn(160, ref_ids)

    def test_all_cross_refs_have_relationships(self):
        for ref in self.cross_refs:
            self.assertIn('relationship', ref)
            self.assertGreater(len(ref['relationship']), 10)


class TestDocSync(unittest.TestCase):
    """Verify documentation references this mechanism."""

    def test_readme_test_count_reflects_addition(self):
        readme_path = os.path.join(os.path.dirname(__file__), '..', 'README.md')
        with open(readme_path, 'r') as f:
            content = f.read()
        # Check test file is listed
        self.assertIn('test_matt_wille_gizmodo', content)

    def test_architecture_lists_test_file(self):
        arch_path = os.path.join(os.path.dirname(__file__), '..', 'docs', 'ARCHITECTURE.md')
        with open(arch_path, 'r') as f:
            content = f.read()
        self.assertIn('test_matt_wille_gizmodo', content)

    def test_test_file_path_in_mechanism(self):
        mechanism = find_mechanism_anywhere(179)
        test_file = mechanism.get('test_file', '')
        self.assertIn('matt_wille_gizmodo', test_file)

    def test_test_count_in_mechanism(self):
        mechanism = find_mechanism_anywhere(179)
        count = mechanism.get('test_count', 0)
        self.assertGreater(count, 0)


if __name__ == '__main__':
    unittest.main()
