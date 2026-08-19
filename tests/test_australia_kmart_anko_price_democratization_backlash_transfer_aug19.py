"""
Mechanism #175: Australia Kmart Anko Price Democratization Backlash Transfer —
Non-Meta Brand Receives Partial Scrutiny With Gravitational Meta Reframing

Type E: Podcast/Broadcast Sentiment Tracking (cross-entity natural experiment)
Iteration #176 (Aug 19, 2026)

In August 2026, Kmart Australia launched $89 Anko camera glasses — the first
documented natural experiment where a non-Meta brand receives substantial privacy
scrutiny for camera-equipped smart glasses. Despite Kmart having objectively worse
privacy safeguards at a lower price, extreme-alarm vocabulary ("pervert," "surveillance,"
celebrity condemnation, institutional bans) applies exclusively to Meta. Kmart receives
moderate-alarm vocabulary ("privacy concerns," "privacy storm") and government investigation
but none of the cultural delegitimization vectors.

10 test classes, ~40 tests.
"""

import unittest
import yaml
import os


def _load_data():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(base, 'profiles', 'competitor-coverage-research.yaml')) as f:
        return yaml.safe_load(f)


class TestMechanism175Structure(unittest.TestCase):
    """Verify mechanism #175 exists with correct structural fields."""

    @classmethod
    def setUpClass(cls):
        cls.data = _load_data()
        cls.cpf = cls.data.get('cross_publication_findings', {})
        cls.mechanism = cls.cpf.get('australia_kmart_anko_price_democratization_backlash_transfer', {})

    def test_mechanism_id(self):
        self.assertEqual(self.mechanism.get('mechanism_id'), 175)

    def test_mechanism_name_contains_kmart(self):
        name = self.mechanism.get('mechanism_name', '')
        self.assertIn('Kmart', name)

    def test_mechanism_name_contains_price_democratization(self):
        name = self.mechanism.get('mechanism_name', '')
        self.assertIn('Price Democratization', name)

    def test_mechanism_type(self):
        mtype = self.mechanism.get('mechanism_type', '')
        self.assertIn('podcast', mtype.lower())

    def test_entities_meta(self):
        entities = self.mechanism.get('entities_involved', [])
        self.assertIn('Meta', entities)

    def test_entities_kmart(self):
        entities = self.mechanism.get('entities_involved', [])
        self.assertTrue(any('Kmart' in e or 'Anko' in e for e in entities))

    def test_entities_samsung(self):
        entities = self.mechanism.get('entities_involved', [])
        self.assertIn('Samsung', entities)

    def test_entities_google(self):
        entities = self.mechanism.get('entities_involved', [])
        self.assertIn('Google', entities)

    def test_entities_apple(self):
        entities = self.mechanism.get('entities_involved', [])
        self.assertIn('Apple', entities)

    def test_asymmetry_score(self):
        self.assertAlmostEqual(self.mechanism.get('asymmetry_score', 0), 0.68, places=2)

    def test_discovery_date(self):
        self.assertEqual(self.mechanism.get('discovery_date'), '2026-08-19')

    def test_sources_non_empty(self):
        sources = self.mechanism.get('source_urls', [])
        self.assertGreater(len(sources), 0)

    def test_confounders_count(self):
        confounders = self.mechanism.get('confounding_factors', [])
        self.assertEqual(len(confounders), 5)


class TestKmartVocabularyGradient(unittest.TestCase):
    """Verify moderate-alarm vocabulary documented for Kmart vs extreme-alarm for Meta."""

    @classmethod
    def setUpClass(cls):
        cls.data = _load_data()
        cls.cpf = cls.data.get('cross_publication_findings', {})
        cls.mechanism = cls.cpf.get('australia_kmart_anko_price_democratization_backlash_transfer', {})
        cls.vocab = cls.mechanism.get('vocabulary_comparison', {})

    def test_kmart_vocabulary_exists(self):
        self.assertIn('kmart_anko', self.vocab)

    def test_meta_vocabulary_exists(self):
        self.assertIn('meta_ray_ban', self.vocab)

    def test_kmart_includes_privacy_concerns(self):
        kmart_vocab = self.vocab.get('kmart_anko', {}).get('vocabulary', [])
        self.assertIn('privacy concerns', kmart_vocab)

    def test_meta_includes_pervert_glasses(self):
        meta_vocab = self.vocab.get('meta_ray_ban', {}).get('vocabulary', [])
        self.assertIn('pervert glasses', meta_vocab)

    def test_kmart_severity_moderate(self):
        severity = self.vocab.get('kmart_anko', {}).get('severity', '')
        self.assertIn('moderate', severity.lower())

    def test_meta_severity_extreme(self):
        severity = self.vocab.get('meta_ray_ban', {}).get('severity', '')
        self.assertIn('extreme', severity.lower())


class TestNonMetaBrandScrutinyValidation(unittest.TestCase):
    """Verify Kmart receives government investigation, petition, and broadcast coverage."""

    @classmethod
    def setUpClass(cls):
        cls.data = _load_data()
        cls.cpf = cls.data.get('cross_publication_findings', {})
        cls.mechanism = cls.cpf.get('australia_kmart_anko_price_democratization_backlash_transfer', {})
        cls.receives = cls.mechanism.get('what_kmart_does_receive', [])

    def test_government_investigation(self):
        text = ' '.join(self.receives).lower()
        self.assertIn('government', text)

    def test_petition_signatures(self):
        text = ' '.join(self.receives)
        self.assertIn('43,000', text)

    def test_broadcast_coverage(self):
        text = ' '.join(self.receives).lower()
        self.assertTrue('7news' in text or 'sunrise' in text or 'broadcast' in text)

    def test_efa_ban_call(self):
        text = ' '.join(self.receives)
        self.assertTrue(any('EFA' in r or 'both' in r.lower() for r in self.receives))


class TestGravitationalMetaReframing(unittest.TestCase):
    """Verify Meta serves as reference point even in Kmart coverage."""

    @classmethod
    def setUpClass(cls):
        cls.data = _load_data()
        cls.cpf = cls.data.get('cross_publication_findings', {})
        cls.mechanism = cls.cpf.get('australia_kmart_anko_price_democratization_backlash_transfer', {})

    def test_finding_mentions_gravitational(self):
        finding = self.mechanism.get('finding', '')
        self.assertIn('Gravitational Meta Reframing', finding)

    def test_finding_mentions_reference_point(self):
        finding = self.mechanism.get('finding', '')
        self.assertIn('reference point', finding.lower())

    def test_finding_mentions_aap_quote(self):
        finding = self.mechanism.get('finding', '')
        self.assertIn('companies including Meta', finding)

    def test_finding_mentions_cheaper_comparison(self):
        finding = self.mechanism.get('finding', '')
        self.assertIn('81% cheaper', finding)


class TestVocabularySeverityDifferential(unittest.TestCase):
    """Kmart gets 'privacy concerns' (5/10), Meta gets 'pervert glasses' (9/10)."""

    @classmethod
    def setUpClass(cls):
        cls.data = _load_data()
        cls.cpf = cls.data.get('cross_publication_findings', {})
        cls.mechanism = cls.cpf.get('australia_kmart_anko_price_democratization_backlash_transfer', {})
        cls.vocab = cls.mechanism.get('vocabulary_comparison', {})

    def test_kmart_severity_five(self):
        severity = self.vocab.get('kmart_anko', {}).get('severity', '')
        self.assertIn('5/10', severity)

    def test_meta_severity_nine(self):
        severity = self.vocab.get('meta_ray_ban', {}).get('severity', '')
        self.assertIn('9/10', severity)

    def test_severity_gap(self):
        # Kmart 5/10, Meta 9/10 => gap of 4
        kmart = self.vocab.get('kmart_anko', {}).get('severity', '0/10')
        meta = self.vocab.get('meta_ray_ban', {}).get('severity', '0/10')
        kmart_score = int(kmart.split('/')[0])
        meta_score = int(meta.split('/')[0])
        self.assertGreaterEqual(meta_score - kmart_score, 3)


class TestMissingExtremeBacklashForKmart(unittest.TestCase):
    """Verify Kmart does NOT receive celebrity condemnation, satirical commerce,
    criminal complaints, or institutional bans."""

    @classmethod
    def setUpClass(cls):
        cls.data = _load_data()
        cls.cpf = cls.data.get('cross_publication_findings', {})
        cls.mechanism = cls.cpf.get('australia_kmart_anko_price_democratization_backlash_transfer', {})
        cls.does_not_receive = cls.mechanism.get('what_kmart_does_not_receive', [])

    def test_no_celebrity_condemnation(self):
        text = ' '.join(self.does_not_receive).lower()
        self.assertIn('celebrity', text)

    def test_no_satirical_products(self):
        text = ' '.join(self.does_not_receive).lower()
        self.assertIn('satirical', text)

    def test_no_pervert_vocabulary(self):
        text = ' '.join(self.does_not_receive).lower()
        self.assertIn('pervert', text)

    def test_no_institutional_bans(self):
        text = ' '.join(self.does_not_receive).lower()
        self.assertIn('institutional ban', text)

    def test_no_criminal_complaints(self):
        text = ' '.join(self.does_not_receive).lower()
        self.assertIn('criminal', text)

    def test_no_activist_campaigns(self):
        text = ' '.join(self.does_not_receive).lower()
        self.assertIn('activist', text)


class TestPrivacyFeatureComparison(unittest.TestCase):
    """Kmart has worse privacy features (no documented LED) than Meta (mandatory tamper-enforced LED)."""

    @classmethod
    def setUpClass(cls):
        cls.data = _load_data()
        cls.cpf = cls.data.get('cross_publication_findings', {})
        cls.mechanism = cls.cpf.get('australia_kmart_anko_price_democratization_backlash_transfer', {})
        cls.features = cls.mechanism.get('privacy_feature_comparison', {})

    def test_meta_has_mandatory_led(self):
        meta = self.features.get('meta_ray_ban', {})
        led = meta.get('privacy_led', '')
        self.assertIn('tamper', led.lower())

    def test_kmart_led_not_documented(self):
        kmart = self.features.get('kmart_anko', {})
        led = kmart.get('privacy_led', '')
        self.assertIn('not documented', led.lower())

    def test_meta_camera_12mp(self):
        meta = self.features.get('meta_ray_ban', {})
        self.assertIn('12MP', meta.get('camera', ''))

    def test_kmart_camera_8mp(self):
        kmart = self.features.get('kmart_anko', {})
        self.assertIn('8MP', kmart.get('camera', ''))


class TestPriceAccessibilityParadox(unittest.TestCase):
    """$89 Kmart vs $469+ Meta — cheaper with worse privacy gets less scrutiny."""

    @classmethod
    def setUpClass(cls):
        cls.data = _load_data()
        cls.cpf = cls.data.get('cross_publication_findings', {})
        cls.mechanism = cls.cpf.get('australia_kmart_anko_price_democratization_backlash_transfer', {})
        cls.features = cls.mechanism.get('privacy_feature_comparison', {})

    def test_kmart_price_89(self):
        kmart = self.features.get('kmart_anko', {})
        self.assertIn('89', kmart.get('price', ''))

    def test_meta_price_469_plus(self):
        meta = self.features.get('meta_ray_ban', {})
        self.assertIn('469', meta.get('price', ''))

    def test_cheaper_product_lower_scrutiny(self):
        """Asymmetry score < 1.0 confirms non-proportional scrutiny."""
        score = self.mechanism.get('asymmetry_score', 0)
        self.assertLess(score, 1.0)
        self.assertGreater(score, 0.0)

    def test_finding_mentions_price_paradox(self):
        finding = self.mechanism.get('finding', '')
        self.assertIn('worse privacy safeguards', finding.lower())


class TestCrossReferenceIntegrity(unittest.TestCase):
    """Cross-references to mechanisms #137, #144, #157, #158, #173 exist in corpus."""

    @classmethod
    def setUpClass(cls):
        cls.data = _load_data()
        cls.cpf = cls.data.get('cross_publication_findings', {})
        cls.mechanism = cls.cpf.get('australia_kmart_anko_price_democratization_backlash_transfer', {})
        cls.cross_refs = cls.mechanism.get('cross_references', [])
        cls.ref_ids = [r.get('mechanism_id') for r in cls.cross_refs]

    def test_references_mechanism_137(self):
        self.assertIn(137, self.ref_ids)

    def test_references_mechanism_144(self):
        self.assertIn(144, self.ref_ids)

    def test_references_mechanism_157(self):
        self.assertIn(157, self.ref_ids)

    def test_references_mechanism_158(self):
        self.assertIn(158, self.ref_ids)

    def test_references_mechanism_173(self):
        self.assertIn(173, self.ref_ids)

    def test_all_cross_refs_have_connection(self):
        for ref in self.cross_refs:
            self.assertIn('connection', ref, f"Missing connection for mechanism {ref.get('mechanism_id')}")

    def test_cross_ref_count(self):
        self.assertEqual(len(self.cross_refs), 5)


class TestPredictionUpdate(unittest.TestCase):
    """Verify testable prediction about non-Meta scrutiny intensity documented."""

    @classmethod
    def setUpClass(cls):
        cls.data = _load_data()
        cls.cpf = cls.data.get('cross_publication_findings', {})
        cls.mechanism = cls.cpf.get('australia_kmart_anko_price_democratization_backlash_transfer', {})

    def test_finding_mentions_prediction(self):
        finding = self.mechanism.get('finding', '')
        self.assertIn('PREDICTION UPDATE', finding)

    def test_finding_mentions_samsung_prediction(self):
        finding = self.mechanism.get('finding', '')
        self.assertIn('Samsung will receive', finding)

    def test_finding_mentions_40_percent(self):
        finding = self.mechanism.get('finding', '')
        self.assertIn('40%', finding)

    def test_finding_mentions_partial_validation(self):
        finding = self.mechanism.get('finding', '').lower()
        self.assertIn('partially validates', finding)


if __name__ == '__main__':
    unittest.main()
