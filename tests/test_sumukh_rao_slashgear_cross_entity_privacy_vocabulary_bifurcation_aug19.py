"""
Test Mechanism #187: Sumukh Rao (SlashGear / Static Media) Intra-Article Cross-Entity
Privacy Vocabulary Bifurcation — Google/Samsung "Hopeful" vs Meta "Massive Breach"

Type B: Journalist Cross-Entity Tracking

Core finding: In a single article ("Google Just May One Up Meta With These 5 Smart Glasses
Features," Jun 2026), SlashGear freelancer Sumukh Rao applies sharply bifurcated privacy
vocabulary within the SAME piece. Meta receives alarm-register language: "massive breach
of privacy," "huge red flag," "bad reputation when it comes to privacy," "good reason to
not wear the Meta Ray-Ban glasses." Google and Samsung receive aspirational-register
language: "better reputation," "hopeful," "promising safety feature," "more secure
privacy." Samsung's camera — identical 12MP, same Qualcomm AR1 chip — is normalized as
"expected to follow a similar approach" with ZERO alarm vocabulary, despite doing the
exact same recording that triggers alarm vocabulary when Meta does it.

This single-article bifurcation is amplified by publication-level patterns at SlashGear:
Nadeem Sarwar's Meta article (Oct 2025) uses "demon of privacy scares," "$8 billion
fine," "the future seems bleak," "a whole new world of risks." Zohaib Ahmed's Samsung
article (Aug 2026) describes the camera as a "bone of contention" immediately neutralized
by LED compliance framing, with ZERO alarm terms about Samsung privacy.

Financial context: SlashGear (Static Media, Fishers, IN) depends on Google Search traffic
as its primary audience acquisition channel. Google is the direct PLATFORM PARTNER for
Samsung's Android XR glasses. Meta has $0 financial relationship with Static Media. Sumukh
Rao is based in Bengaluru, India, where Android (Google/Samsung) holds ~97% mobile market
share, and simultaneously works as Editor at BGR (Penske Media).

Sources:
- https://www.slashgear.com/2196157/google-smart-glasses-features-one-up-meta-ray-ban/
- https://www.slashgear.com/1972038/ray-ban-meta-ai-glasses-display-look-great-smart-reason-not-buy/
- https://www.slashgear.com/2229699/samsung-smart-glasses-vs-meta-ray-ban-battery-life/
- https://Www.Slashgear.com/author/sumukhrao/
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
    'id': 187,
    'type': 'journalist_cross_entity_intra_article_vocabulary_bifurcation',
    'publication': 'SlashGear (Static Media)',
    'journalist': 'Sumukh Rao',
    'asymmetry_score': 0.79,
    'core_finding': (
        'Sumukh Rao applies bifurcated privacy vocabulary within a single article: '
        'Meta = "massive breach of privacy," "huge red flag," "bad reputation" '
        'vs Google/Samsung = "better reputation," "hopeful," "promising safety feature." '
        'Samsung camera (identical 12MP, same Qualcomm AR1) normalized as '
        '"expected to follow a similar approach" with ZERO alarm terms.'
    ),
}


class TestMechanismExists(unittest.TestCase):
    """Verify mechanism #187 exists and has required fields."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(187)

    def test_mechanism_found(self):
        self.assertIsNotNone(self.mechanism, "Mechanism #187 not found in YAML")

    def test_mechanism_id(self):
        self.assertEqual(self.mechanism['mechanism_id'], 187)

    def test_mechanism_name_contains_sumukh_rao(self):
        self.assertIn('Sumukh Rao', self.mechanism['mechanism_name'])

    def test_mechanism_name_contains_slashgear(self):
        self.assertIn('SlashGear', self.mechanism['mechanism_name'])

    def test_mechanism_type(self):
        mtype = self.mechanism['mechanism_type']
        self.assertIn('journalist', mtype)
        self.assertIn('cross_entity', mtype)

    def test_has_discovery_date(self):
        self.assertIn('discovery_date', self.mechanism)
        self.assertEqual(self.mechanism['discovery_date'], '2026-08-19')

    def test_has_source_urls(self):
        self.assertIn('source_urls', self.mechanism)
        self.assertGreater(len(self.mechanism['source_urls']), 3)

    def test_has_asymmetry_score(self):
        self.assertIn('asymmetry_score', self.mechanism)
        score = self.mechanism['asymmetry_score']
        self.assertGreaterEqual(score, 0.5)
        self.assertLessEqual(score, 1.0)

    def test_asymmetry_score_value(self):
        self.assertEqual(self.mechanism['asymmetry_score'], 0.79)


class TestJournalistProfile(unittest.TestCase):
    """Verify journalist profile captures Sumukh Rao's role and multi-publication reach."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(187)
        cls.journalist = cls.mechanism.get('journalist', {})

    def test_journalist_name(self):
        self.assertEqual(self.journalist['name'], 'Sumukh Rao')

    def test_primary_publication_slashgear(self):
        self.assertIn('SlashGear', self.journalist['publication'])

    def test_location_documented(self):
        location = self.journalist.get('location', '').lower()
        self.assertIn('bengaluru', location)

    def test_multi_publication_reach(self):
        pubs = self.journalist.get('other_publications', [])
        self.assertGreaterEqual(len(pubs), 2)

    def test_bgr_in_other_publications(self):
        pubs = self.journalist.get('other_publications', [])
        bgr = [p for p in pubs if 'BGR' in p or 'bgr' in p.lower()]
        self.assertGreater(len(bgr), 0)

    def test_xda_in_other_publications(self):
        pubs = self.journalist.get('other_publications', [])
        xda = [p for p in pubs if 'XDA' in p or 'xda' in p.lower()]
        self.assertGreater(len(xda), 0)

    def test_qualcomm_summit_attendance(self):
        bio = self.journalist.get('bio_notes', '').lower()
        self.assertTrue(
            'qualcomm' in bio or 'snapdragon summit' in bio,
            f"Bio should note Qualcomm Snapdragon Summit attendance: {bio}"
        )


class TestIntraArticleMetaVocabulary(unittest.TestCase):
    """Verify Meta alarm vocabulary from Sumukh Rao's Google smart glasses article."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(187)
        cls.meta_vocab = cls.mechanism.get('meta_vocabulary', {})

    def test_alarm_terms_documented(self):
        terms = self.meta_vocab.get('alarm_terms', [])
        self.assertGreaterEqual(len(terms), 4)

    def test_massive_breach_term(self):
        terms = self.meta_vocab.get('alarm_terms', [])
        breach = [t for t in terms if 'massive breach' in t.lower()]
        self.assertGreater(len(breach), 0, "Should include 'massive breach of privacy'")

    def test_huge_red_flag_term(self):
        terms = self.meta_vocab.get('alarm_terms', [])
        flag = [t for t in terms if 'red flag' in t.lower()]
        self.assertGreater(len(flag), 0, "Should include 'huge red flag'")

    def test_bad_reputation_term(self):
        terms = self.meta_vocab.get('alarm_terms', [])
        rep = [t for t in terms if 'bad reputation' in t.lower()]
        self.assertGreater(len(rep), 0, "Should include 'bad reputation'")

    def test_good_reason_not_to_wear_term(self):
        terms = self.meta_vocab.get('alarm_terms', [])
        wear = [t for t in terms if 'not wear' in t.lower() or 'good reason' in t.lower()]
        self.assertGreater(len(wear), 0, "Should include 'good reason to not wear'")

    def test_alarm_term_count(self):
        count = self.meta_vocab.get('total_alarm_terms', 0)
        self.assertGreaterEqual(count, 4)

    def test_article_url(self):
        url = self.meta_vocab.get('source_article_url', '')
        self.assertIn('slashgear.com', url)
        self.assertIn('google-smart-glasses', url)


class TestIntraArticleGoogleVocabulary(unittest.TestCase):
    """Verify Google/Samsung aspirational vocabulary from the same article."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(187)
        cls.google_vocab = cls.mechanism.get('google_samsung_vocabulary', {})

    def test_aspirational_terms_documented(self):
        terms = self.google_vocab.get('aspirational_terms', [])
        self.assertGreaterEqual(len(terms), 3)

    def test_better_reputation_term(self):
        terms = self.google_vocab.get('aspirational_terms', [])
        rep = [t for t in terms if 'better reputation' in t.lower()]
        self.assertGreater(len(rep), 0, "Should include 'better reputation'")

    def test_hopeful_term(self):
        terms = self.google_vocab.get('aspirational_terms', [])
        hopeful = [t for t in terms if 'hopeful' in t.lower()]
        self.assertGreater(len(hopeful), 0, "Should include 'hopeful'")

    def test_promising_term(self):
        terms = self.google_vocab.get('aspirational_terms', [])
        promising = [t for t in terms if 'promising' in t.lower()]
        self.assertGreater(len(promising), 0, "Should include 'promising safety feature'")

    def test_samsung_camera_normalization(self):
        norm = self.google_vocab.get('samsung_camera_normalization', '').lower()
        self.assertIn('follow', norm,
                      f"Samsung camera should be normalized as 'follow similar approach': {norm}")

    def test_zero_alarm_terms_about_google(self):
        count = self.google_vocab.get('alarm_terms_about_google', 99)
        self.assertEqual(count, 0)

    def test_zero_alarm_terms_about_samsung(self):
        count = self.google_vocab.get('alarm_terms_about_samsung', 99)
        self.assertEqual(count, 0)


class TestCapabilityParity(unittest.TestCase):
    """Verify the article documents that Samsung/Google have equivalent camera capabilities."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(187)
        cls.parity = cls.mechanism.get('capability_parity', {})

    def test_same_camera_resolution(self):
        cam = self.parity.get('camera_resolution', '')
        self.assertIn('12MP', cam)

    def test_same_chip(self):
        chip = self.parity.get('processor', '').lower()
        self.assertTrue(
            'snapdragon ar1' in chip or 'qualcomm' in chip,
            f"Should document same Qualcomm chip: {chip}"
        )

    def test_led_indicator_both(self):
        led = self.parity.get('led_indicator', '').lower()
        self.assertTrue(
            'both' in led or 'same' in led or 'meta' in led,
            f"Should note both Meta and Samsung have LED indicators: {led}"
        )

    def test_parity_note(self):
        note = self.parity.get('note', '').lower()
        self.assertTrue(
            'identical' in note or 'same' in note or 'equivalent' in note,
            f"Parity note should reference identical capabilities: {note}"
        )


class TestPublicationLevelPattern(unittest.TestCase):
    """Verify same-publication Meta-negative / Samsung-neutral pattern from other authors."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(187)
        cls.pub_pattern = cls.mechanism.get('publication_level_pattern', {})

    def test_nadeem_sarwar_meta_article(self):
        nadeem = self.pub_pattern.get('nadeem_sarwar', {})
        self.assertIn('title', nadeem)
        title = nadeem['title'].lower()
        self.assertTrue('smart reason not to buy' in title or 'meta' in title)

    def test_nadeem_sarwar_alarm_vocabulary(self):
        nadeem = self.pub_pattern.get('nadeem_sarwar', {})
        vocab = nadeem.get('alarm_vocabulary', [])
        self.assertGreaterEqual(len(vocab), 3)

    def test_nadeem_demon_of_privacy_scares(self):
        nadeem = self.pub_pattern.get('nadeem_sarwar', {})
        vocab = nadeem.get('alarm_vocabulary', [])
        demon = [v for v in vocab if 'demon' in v.lower() or 'privacy scares' in v.lower()]
        self.assertGreater(len(demon), 0)

    def test_nadeem_future_seems_bleak(self):
        nadeem = self.pub_pattern.get('nadeem_sarwar', {})
        vocab = nadeem.get('alarm_vocabulary', [])
        bleak = [v for v in vocab if 'bleak' in v.lower()]
        self.assertGreater(len(bleak), 0)

    def test_zohaib_ahmed_samsung_article(self):
        zohaib = self.pub_pattern.get('zohaib_ahmed', {})
        self.assertIn('title', zohaib)
        title = zohaib['title'].lower()
        self.assertTrue('samsung' in title and 'battery' in title)

    def test_zohaib_ahmed_zero_alarm_terms(self):
        zohaib = self.pub_pattern.get('zohaib_ahmed', {})
        count = zohaib.get('privacy_alarm_terms', 99)
        self.assertEqual(count, 0)

    def test_zohaib_camera_bone_of_contention_framing(self):
        zohaib = self.pub_pattern.get('zohaib_ahmed', {})
        framing = zohaib.get('camera_framing', '').lower()
        self.assertTrue(
            'bone of contention' in framing or 'neutralized' in framing,
            f"Samsung camera framing should be neutralized: {framing}"
        )


class TestFinancialContext(unittest.TestCase):
    """Verify financial context documents Static Media / Google dependency."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(187)
        cls.financial = cls.mechanism.get('financial_context', {})

    def test_slashgear_owner_documented(self):
        owner = self.financial.get('slashgear_owner', '')
        self.assertIn('Static Media', owner)

    def test_google_search_dependency(self):
        dep = self.financial.get('google_search_dependency', '').lower()
        self.assertTrue(
            'traffic' in dep or 'search' in dep or 'audience' in dep,
            f"Should document Google Search traffic dependency: {dep}"
        )

    def test_google_android_xr_partnership(self):
        xr = self.financial.get('google_android_xr_partnership', '')
        self.assertIn('Samsung', xr)

    def test_meta_zero_financial_relationship(self):
        meta_rel = self.financial.get('meta_financial_relationship', '')
        self.assertIn('$0', meta_rel)

    def test_author_market_context(self):
        market = self.financial.get('author_market_context', '').lower()
        self.assertTrue(
            'india' in market or 'android' in market or '97%' in market,
            f"Should note Indian market Android dominance: {market}"
        )


class TestConfounders(unittest.TestCase):
    """Verify confounders are documented with rebuttals."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(187)
        cls.confounders = cls.mechanism.get('confounders', [])

    def test_at_least_5_confounders(self):
        self.assertGreaterEqual(len(self.confounders), 5)

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

    def test_meta_track_record_confounder_exists(self):
        descriptions = [c.get('description', '').lower() for c in self.confounders]
        track = any('track record' in d or 'kenya' in d or 'sama' in d or 'contractor' in d for d in descriptions)
        self.assertTrue(track, "Should have a Meta contractor/track record confounder")

    def test_pre_launch_confounder_exists(self):
        descriptions = [c.get('description', '').lower() for c in self.confounders]
        pre = any('pre-launch' in d or 'pre-ship' in d or 'not yet shipped' in d or 'unreleased' in d for d in descriptions)
        self.assertTrue(pre, "Should have a pre-launch timing confounder")

    def test_google_data_collection_confounder_exists(self):
        descriptions = [c.get('description', '').lower() for c in self.confounders]
        google = any('google' in d and ('data' in d or 'track record' in d or 'collection' in d) for d in descriptions)
        self.assertTrue(google, "Should have a Google data collection track record confounder")


class TestCrossReferences(unittest.TestCase):
    """Verify cross-references to related mechanisms."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = find_mechanism_anywhere(187)
        cls.cross_refs = cls.mechanism.get('cross_references', [])

    def test_at_least_3_cross_references(self):
        self.assertGreaterEqual(len(self.cross_refs), 3)

    def test_mechanism_186_referenced(self):
        """Mechanism #186 = Engadget triple device vocabulary bifurcation"""
        ref_ids = [r.get('mechanism_id') for r in self.cross_refs]
        self.assertIn(186, ref_ids)

    def test_mechanism_183_referenced(self):
        """Mechanism #183 = Hadlee Simons Android Authority cross-entity"""
        ref_ids = [r.get('mechanism_id') for r in self.cross_refs]
        self.assertIn(183, ref_ids)

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
        self.assertIn('test_sumukh_rao_slashgear', content)

    def test_architecture_lists_test_file(self):
        arch_path = os.path.join(os.path.dirname(__file__), '..', 'docs', 'ARCHITECTURE.md')
        with open(arch_path, 'r') as f:
            content = f.read()
        self.assertIn('test_sumukh_rao_slashgear', content)

    def test_test_file_path_in_mechanism(self):
        mechanism = find_mechanism_anywhere(187)
        test_file = mechanism.get('test_file', '')
        self.assertIn('sumukh_rao_slashgear', test_file)

    def test_test_count_in_mechanism(self):
        mechanism = find_mechanism_anywhere(187)
        count = mechanism.get('test_count', 0)
        self.assertGreater(count, 0)


if __name__ == '__main__':
    unittest.main()
