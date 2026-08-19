"""
Mechanism #173: 9to5 Network Cross-Publication Smart Glasses Privacy Vocabulary Gradient

Discovery: The 9to5Mac Inc. network (parent of 9to5Mac and 9to5Google) applies a
systematic THREE-TIER privacy vocabulary gradient across its podcast/newsletter
output that correlates with financial dependencies:

Tier 1 — Even Realities (no camera, no financial relationship):
  9to5Mac Overtime Ep077 (~Aug 18, 2026): CEO Will Wang interview. Chapter
  "Addressing the privacy problem" (28:58) frames privacy as solvable design
  challenge. Aspirational framing. Zero alarm vocabulary.
  Source: https://www.youtube.com/watch?v=mcz5ZnH_YPY

Tier 2 — Samsung/Google (camera, financial partner):
  9to5Google Pixelated #81 (~Jul 2026): "surprisingly impressive," zero privacy vocab.
  9to5Google Sideload #37 (Jun 22, 2026): "nailing the basics," zero privacy vocab.
  9to5Google article (Jul 23): "got it right out of the gate" on identical privacy LED.

Tier 3 — Meta (camera, no financial relationship):
  9to5Google Inbox Newsletter (Jul 23, 2026): "perv glasses" in headline.
  Daniel Bader explicit trust differential: "I trust Google with far more than Meta."
  9to5Mac privacy archive: "Meta Ray-Ban smart glasses send 'sensitive' videos to
  human data annotators."

Financial Architecture:
  9to5Google: Digiday (2018) writers paid via Google AdSense per-article. Google
  Preferred Source badge. Google Ad Exchange partner.
  9to5Mac: Apple affiliate links (Amazon Associates + Apple partnerships).
  Neither publication has any financial relationship with Meta or Even Realities.

Key Quote: "You just cannot have a camera; it's irresponsible." — Will Wang, Even
Realities CEO (9to5Mac Overtime podcast, via Gizmodo article)

Confounders: 5 documented (2 STRONG, 2 MODERATE, 1 WEAK)
Asymmetry Score: 0.77
Cross-references: #131 (Ben Schoon control), #163 (9to5Google dual-framing paradox),
  #171 (Daniel Bader career-ecosystem capture), #144 (Podcast Ecosystem Amplification),
  #148 (Vox Media Cross-Medium Portability)
"""

import unittest
import yaml
import os


YAML_PATH = os.path.join(os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml')


def _load_yaml():
    with open(YAML_PATH, 'r') as f:
        return yaml.safe_load(f)


def _get_cpf():
    data = _load_yaml()
    return data.get('cross_publication_findings', {})


def _get_mechanism_173():
    cpf = _get_cpf()
    for v in cpf.values():
        if isinstance(v, dict) and v.get('mechanism_id') == 173:
            return v
    return None


class TestMechanism173Existence(unittest.TestCase):
    """Verify mechanism #173 exists in competitor-coverage-research.yaml with correct fields."""

    @classmethod
    def setUpClass(cls):
        cls.cpf = _get_cpf()
        cls.mechanism = _get_mechanism_173()

    def test_mechanism_173_exists(self):
        self.assertIsNotNone(self.mechanism, "Mechanism #173 not found in cross_publication_findings")

    def test_mechanism_173_key_name(self):
        found_key = None
        for k, v in self.cpf.items():
            if isinstance(v, dict) and v.get('mechanism_id') == 173:
                found_key = k
                break
        self.assertEqual(found_key, 'nine_to_five_network_cross_publication_privacy_vocabulary_gradient')

    def test_mechanism_173_has_finding_summary(self):
        self.assertIn('finding_summary', self.mechanism)
        self.assertGreater(len(self.mechanism['finding_summary']), 100)

    def test_mechanism_173_has_discovery_date(self):
        self.assertEqual(self.mechanism.get('discovery_date'), '2026-08-19')

    def test_mechanism_173_has_test_file(self):
        tf = self.mechanism.get('test_file', '')
        self.assertIn('9to5_network_cross_publication_privacy_vocabulary_gradient', tf)
        self.assertIn('aug19', tf)

    def test_mechanism_173_has_test_count(self):
        tc = self.mechanism.get('test_count')
        self.assertIsNotNone(tc)
        self.assertGreaterEqual(tc, 35)


class TestMechanism173AsymmetryScore(unittest.TestCase):
    """Verify asymmetry score 0.77 is in expected range."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = _get_mechanism_173()

    def test_asymmetry_score_exists(self):
        self.assertIn('asymmetry_score', self.mechanism)

    def test_asymmetry_score_value(self):
        score = self.mechanism['asymmetry_score']
        self.assertAlmostEqual(score, 0.77, places=2)

    def test_asymmetry_score_in_valid_range(self):
        score = self.mechanism['asymmetry_score']
        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 1.0)

    def test_asymmetry_score_above_moderate_threshold(self):
        """0.77 is well above the 0.5 moderate asymmetry threshold."""
        score = self.mechanism['asymmetry_score']
        self.assertGreater(score, 0.5)


class TestMechanism173CrossReferences(unittest.TestCase):
    """Verify bidirectional cross-references with #131, #163, #171, #144, #148."""

    @classmethod
    def setUpClass(cls):
        cls.cpf = _get_cpf()
        cls.mechanism = _get_mechanism_173()

    def test_cross_references_exist(self):
        self.assertIn('cross_references', self.mechanism)
        self.assertIsInstance(self.mechanism['cross_references'], list)

    def test_cross_reference_mechanism_131(self):
        ref_ids = [r.get('mechanism_id') for r in self.mechanism['cross_references']]
        self.assertIn(131, ref_ids, "Missing cross-reference to mechanism #131 (Ben Schoon control)")

    def test_cross_reference_mechanism_163(self):
        ref_ids = [r.get('mechanism_id') for r in self.mechanism['cross_references']]
        self.assertIn(163, ref_ids, "Missing cross-reference to mechanism #163 (9to5Google dual-framing paradox)")

    def test_cross_reference_mechanism_171(self):
        ref_ids = [r.get('mechanism_id') for r in self.mechanism['cross_references']]
        self.assertIn(171, ref_ids, "Missing cross-reference to mechanism #171 (Daniel Bader career-ecosystem capture)")

    def test_cross_reference_mechanism_144(self):
        ref_ids = [r.get('mechanism_id') for r in self.mechanism['cross_references']]
        self.assertIn(144, ref_ids, "Missing cross-reference to mechanism #144 (Podcast Ecosystem Amplification)")

    def test_cross_reference_mechanism_148(self):
        ref_ids = [r.get('mechanism_id') for r in self.mechanism['cross_references']]
        self.assertIn(148, ref_ids, "Missing cross-reference to mechanism #148 (Vox Media Cross-Medium Portability)")

    def test_cross_references_have_connections(self):
        for ref in self.mechanism['cross_references']:
            self.assertIn('connection', ref, f"Cross-reference to #{ref.get('mechanism_id')} missing 'connection' field")


class TestEvenRealitiesZeroAlarmVocabulary(unittest.TestCase):
    """Verify Even Realities coverage contains zero alarm terms."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = _get_mechanism_173()

    def test_primary_evidence_includes_even_realities(self):
        evidence = self.mechanism.get('primary_evidence', {})
        tier1 = evidence.get('tier_1_even_realities', {})
        self.assertIsNotNone(tier1, "Tier 1 (Even Realities) evidence missing")

    def test_even_realities_framing_aspirational(self):
        evidence = self.mechanism.get('primary_evidence', {})
        tier1 = evidence.get('tier_1_even_realities', {})
        framing = str(tier1.get('framing', '')).lower()
        self.assertTrue(
            'aspirational' in framing or 'solvable' in framing or 'design challenge' in framing,
            f"Even Realities framing should be aspirational, got: {framing}"
        )

    def test_even_realities_zero_alarm_vocabulary(self):
        evidence = self.mechanism.get('primary_evidence', {})
        tier1 = evidence.get('tier_1_even_realities', {})
        alarm_count = tier1.get('alarm_vocabulary_count', -1)
        self.assertEqual(alarm_count, 0, "Even Realities should have zero alarm vocabulary")

    def test_even_realities_source_url(self):
        evidence = self.mechanism.get('primary_evidence', {})
        tier1 = evidence.get('tier_1_even_realities', {})
        source = tier1.get('source_url', '')
        self.assertIn('youtube.com', source)


class TestMetaAlarmVocabularyConcentration(unittest.TestCase):
    """Verify Meta coverage uses alarm vocabulary ('perv glasses', 'pervert', 'surveillance')."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = _get_mechanism_173()

    def test_primary_evidence_includes_meta(self):
        evidence = self.mechanism.get('primary_evidence', {})
        tier3 = evidence.get('tier_3_meta', {})
        self.assertIsNotNone(tier3, "Tier 3 (Meta) evidence missing")

    def test_meta_alarm_vocabulary_present(self):
        evidence = self.mechanism.get('primary_evidence', {})
        tier3 = evidence.get('tier_3_meta', {})
        alarm_terms = tier3.get('alarm_terms', [])
        self.assertGreaterEqual(len(alarm_terms), 1, "Meta tier should have alarm vocabulary terms")

    def test_meta_perv_glasses_documented(self):
        evidence = self.mechanism.get('primary_evidence', {})
        tier3 = evidence.get('tier_3_meta', {})
        alarm_terms = [t.lower() for t in tier3.get('alarm_terms', [])]
        self.assertTrue(
            any('perv' in t for t in alarm_terms),
            f"Meta tier should include 'perv glasses' term, got: {alarm_terms}"
        )

    def test_meta_explicit_distrust(self):
        evidence = self.mechanism.get('primary_evidence', {})
        tier3 = evidence.get('tier_3_meta', {})
        summary = str(tier3.get('framing', ''))
        self.assertTrue(
            'distrust' in summary.lower() or 'perv' in summary.lower() or 'alarm' in summary.lower(),
            f"Meta tier should document distrust/alarm framing"
        )


class TestSamsungGoogleZeroAlarmVocabulary(unittest.TestCase):
    """Verify Samsung/Google podcast coverage zero alarm terms."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = _get_mechanism_173()

    def test_primary_evidence_includes_samsung_google(self):
        evidence = self.mechanism.get('primary_evidence', {})
        tier2 = evidence.get('tier_2_samsung_google', {})
        self.assertIsNotNone(tier2, "Tier 2 (Samsung/Google) evidence missing")

    def test_samsung_google_zero_alarm_vocabulary(self):
        evidence = self.mechanism.get('primary_evidence', {})
        tier2 = evidence.get('tier_2_samsung_google', {})
        alarm_count = tier2.get('alarm_vocabulary_count', -1)
        self.assertEqual(alarm_count, 0, "Samsung/Google should have zero alarm vocabulary")

    def test_samsung_google_aspirational_framing(self):
        evidence = self.mechanism.get('primary_evidence', {})
        tier2 = evidence.get('tier_2_samsung_google', {})
        framing = str(tier2.get('framing', '')).lower()
        self.assertTrue(
            'impressive' in framing or 'excited' in framing or 'nailing' in framing or 'positive' in framing,
            f"Samsung/Google should have positive framing, got: {framing}"
        )

    def test_samsung_google_same_hardware_documented(self):
        """Samsung/Google glasses use the same Snapdragon AR1 Gen 1 chip and same camera."""
        finding = str(self.mechanism.get('finding_summary', '')).lower()
        self.assertTrue(
            'identical' in finding or 'same' in finding,
            "Finding should note Samsung/Google use identical/same hardware"
        )


class TestFinancialDependencyCorrelation(unittest.TestCase):
    """Verify AdSense/Ad Exchange dependency documented."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = _get_mechanism_173()

    def test_financial_architecture_exists(self):
        self.assertIn('financial_architecture', self.mechanism)

    def test_google_adsense_documented(self):
        fa = self.mechanism.get('financial_architecture', {})
        nine_to_five_google = fa.get('nine_to_five_google', {})
        deps = str(nine_to_five_google).lower()
        self.assertTrue(
            'adsense' in deps,
            "9to5Google AdSense dependency should be documented"
        )

    def test_google_ad_exchange_documented(self):
        fa = self.mechanism.get('financial_architecture', {})
        nine_to_five_google = fa.get('nine_to_five_google', {})
        deps = str(nine_to_five_google).lower()
        self.assertTrue(
            'ad exchange' in deps or 'ad_exchange' in deps or 'preferred source' in deps or 'preferred_source' in deps,
            "9to5Google Ad Exchange/Preferred Source should be documented"
        )

    def test_meta_zero_financial_relationship(self):
        fa = self.mechanism.get('financial_architecture', {})
        meta_rel = fa.get('meta_relationship', '')
        self.assertTrue(
            'zero' in str(meta_rel).lower() or 'none' in str(meta_rel).lower() or '$0' in str(meta_rel),
            "Meta should have zero/no financial relationship documented"
        )

    def test_digiday_source_cited(self):
        urls = self.mechanism.get('source_urls', [])
        all_text = ' '.join(str(u) for u in urls) + ' ' + str(self.mechanism.get('financial_architecture', ''))
        self.assertTrue(
            'digiday' in all_text.lower(),
            "Digiday (2018) source for AdSense writer payment should be cited"
        )


class TestThreeTierGradientStructure(unittest.TestCase):
    """Verify all three tiers documented with distinct vocabulary."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = _get_mechanism_173()

    def test_three_tiers_in_evidence(self):
        evidence = self.mechanism.get('primary_evidence', {})
        self.assertIn('tier_1_even_realities', evidence)
        self.assertIn('tier_2_samsung_google', evidence)
        self.assertIn('tier_3_meta', evidence)

    def test_tiers_have_distinct_entities(self):
        evidence = self.mechanism.get('primary_evidence', {})
        t1_entities = evidence.get('tier_1_even_realities', {}).get('entity', '')
        t2_entities = evidence.get('tier_2_samsung_google', {}).get('entity', '')
        t3_entities = evidence.get('tier_3_meta', {}).get('entity', '')
        self.assertNotEqual(t1_entities, t2_entities)
        self.assertNotEqual(t2_entities, t3_entities)
        self.assertNotEqual(t1_entities, t3_entities)

    def test_vocabulary_severity_increases_tier1_to_tier3(self):
        """Vocabulary severity should increase from tier 1 (zero alarm) to tier 3 (alarm)."""
        evidence = self.mechanism.get('primary_evidence', {})
        t1_alarm = evidence.get('tier_1_even_realities', {}).get('alarm_vocabulary_count', 0)
        t2_alarm = evidence.get('tier_2_samsung_google', {}).get('alarm_vocabulary_count', 0)
        t3_alarm = evidence.get('tier_3_meta', {}).get('alarm_vocabulary_count', -1)
        self.assertEqual(t1_alarm, 0, "Tier 1 should have 0 alarm terms")
        self.assertEqual(t2_alarm, 0, "Tier 2 should have 0 alarm terms")
        self.assertGreater(t3_alarm, 0, "Tier 3 should have >0 alarm terms")


class TestCrossPublicationNetworkOwnership(unittest.TestCase):
    """Verify 9to5Mac and 9to5Google share parent 9to5Mac Inc."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = _get_mechanism_173()

    def test_publications_field_exists(self):
        pubs = self.mechanism.get('publications', [])
        self.assertIsInstance(pubs, list)
        self.assertGreaterEqual(len(pubs), 2)

    def test_nine_to_five_mac_in_publications(self):
        pubs = [str(p).lower() for p in self.mechanism.get('publications', [])]
        self.assertTrue(
            any('9to5mac' in p for p in pubs),
            f"9to5Mac should be in publications list: {pubs}"
        )

    def test_nine_to_five_google_in_publications(self):
        pubs = [str(p).lower() for p in self.mechanism.get('publications', [])]
        self.assertTrue(
            any('9to5google' in p for p in pubs),
            f"9to5Google should be in publications list: {pubs}"
        )

    def test_shared_parent_documented(self):
        finding = str(self.mechanism.get('finding_summary', '')).lower()
        self.assertTrue(
            '9to5mac inc' in finding or 'parent' in finding or 'network' in finding,
            "Shared parent (9to5Mac Inc.) should be documented in finding summary"
        )


class TestPodcastSourceDocumentation(unittest.TestCase):
    """Verify source URLs, episode numbers, dates present."""

    @classmethod
    def setUpClass(cls):
        cls.mechanism = _get_mechanism_173()

    def test_source_urls_exist(self):
        urls = self.mechanism.get('source_urls', [])
        self.assertGreaterEqual(len(urls), 3, f"Expected >=3 source URLs, got {len(urls)}")

    def test_overtime_youtube_url(self):
        urls = self.mechanism.get('source_urls', [])
        self.assertTrue(
            any('mcz5ZnH_YPY' in str(u) for u in urls),
            "9to5Mac Overtime Ep077 YouTube URL should be in sources"
        )

    def test_pixelated_youtube_url(self):
        urls = self.mechanism.get('source_urls', [])
        self.assertTrue(
            any('EWOvH-BDWe8' in str(u) for u in urls),
            "9to5Google Pixelated #81 YouTube URL should be in sources"
        )

    def test_sideload_url(self):
        urls = self.mechanism.get('source_urls', [])
        self.assertTrue(
            any('sideload' in str(u).lower() for u in urls),
            "9to5Google Sideload #37 URL should be in sources"
        )

    def test_inbox_newsletter_url(self):
        urls = self.mechanism.get('source_urls', [])
        self.assertTrue(
            any('inbox' in str(u).lower() or '9to5google' in str(u).lower() for u in urls),
            "9to5Google Inbox newsletter URL should be in sources"
        )

    def test_mechanism_has_confounders(self):
        confounders = self.mechanism.get('confounders', [])
        self.assertEqual(len(confounders), 5, f"Expected 5 confounders, got {len(confounders)}")

    def test_confounders_have_strength(self):
        for c in self.mechanism.get('confounders', []):
            self.assertIn('strength', c, f"Confounder missing strength: {c}")

    def test_confounder_strengths_distribution(self):
        """Should be 2 STRONG, 2 MODERATE, 1 WEAK."""
        strengths = [c.get('strength', '') for c in self.mechanism.get('confounders', [])]
        self.assertEqual(strengths.count('STRONG'), 2)
        self.assertEqual(strengths.count('MODERATE'), 2)
        self.assertEqual(strengths.count('WEAK'), 1)


if __name__ == '__main__':
    unittest.main()
