"""
Test: OpenAI "Companion" vs Meta "Surveillance" Cross-Publication Vocabulary Bifurcation

Mechanism #159: Multiple publications use aspirational "companion" vocabulary for OpenAI's
camera-equipped smart speaker (cameras, Face ID-like facial recognition, always-on awareness,
proactive user observation) while using adversarial "surveillance" vocabulary for Meta's
camera-equipped glasses (optional camera, privacy LED, dormant NameTag code).

The vocabulary bifurcation maps to entity identity, not product capability differences.

Sources:
- MacRumors Jul 14, 2026: OpenAI device = "humanlike AI companion" (0 alarm terms)
- MacRumors Feb 13, 2026: Meta NameTag = "facial recognition" + "privacy concerns" (8 alarm terms)
- Android Authority Aug 7, 2026: OpenAI speaker = "AI companion" + "premium" (0 alarm terms)
- Android Authority Jul 27, 2026: Meta glasses = "privacy nightmare" + "hot water" (4 alarm terms)
- Inc. Jul 14, 2026: OpenAI device = "direct challenge" + "jaw-droppingly good" (0 alarm terms)
- TechRepublic Jul 16, 2026: OpenAI device = "companion" (0 alarm terms)
"""

import unittest
import yaml
import os
import importlib


class TestMechanismExists(unittest.TestCase):
    """Verify mechanism #159 exists with required structural fields."""

    @classmethod
    def setUpClass(cls):
        ccr_path = os.path.join(
            os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
        )
        with open(ccr_path) as f:
            cls.data = yaml.safe_load(f)
        cls.findings = cls.data.get('cross_publication_findings', {})
        cls.mechanism = cls.findings.get(
            'openai_companion_meta_surveillance_cross_publication_vocabulary_bifurcation', {}
        )

    def test_mechanism_exists(self):
        self.assertTrue(
            len(self.mechanism) > 0,
            "Mechanism 'openai_companion_meta_surveillance_cross_publication_vocabulary_bifurcation' must exist"
        )

    def test_mechanism_id_is_159(self):
        self.assertEqual(self.mechanism.get('mechanism_id'), 159)

    def test_mechanism_name(self):
        name = self.mechanism.get('mechanism_name', '')
        self.assertIn('Companion', name)
        self.assertIn('Surveillance', name)
        self.assertIn('Vocabulary', name)

    def test_finding_type(self):
        self.assertEqual(
            self.mechanism.get('finding_type'), 'competitor_coverage_deep_dive'
        )

    def test_has_source_urls(self):
        urls = self.mechanism.get('source_urls', [])
        self.assertGreaterEqual(len(urls), 6, "Should have at least 6 source URLs")

    def test_has_test_file(self):
        self.assertIn(
            'test_openai_companion_meta_surveillance_vocabulary_bifurcation_aug18',
            self.mechanism.get('test_file', '')
        )

    def test_has_confounders(self):
        confounders = self.mechanism.get('confounders', [])
        self.assertGreaterEqual(len(confounders), 4, "Must have at least 4 confounders")

    def test_has_confounder_responses(self):
        responses = self.mechanism.get('confounder_responses', [])
        self.assertGreaterEqual(len(responses), 3, "Must have at least 3 confounder responses")

    def test_rotation_type_a(self):
        self.assertEqual(self.mechanism.get('rotation_type'), 'A')


class TestOpenAIDeviceCapabilities(unittest.TestCase):
    """Verify OpenAI device capability documentation — the device IS more invasive."""

    @classmethod
    def setUpClass(cls):
        ccr_path = os.path.join(
            os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
        )
        with open(ccr_path) as f:
            data = yaml.safe_load(f)
        findings = data.get('cross_publication_findings', {})
        cls.mechanism = findings.get(
            'openai_companion_meta_surveillance_cross_publication_vocabulary_bifurcation', {}
        )
        cls.openai_caps = cls.mechanism.get('openai_device_capabilities', {})
        cls.meta_caps = cls.mechanism.get('meta_glasses_capabilities', {})

    def test_openai_has_cameras(self):
        self.assertTrue(self.openai_caps.get('cameras'))

    def test_openai_has_facial_recognition(self):
        fr = str(self.openai_caps.get('facial_recognition', ''))
        self.assertIn('Face ID', fr)

    def test_openai_always_on(self):
        self.assertTrue(self.openai_caps.get('always_on_environmental_awareness'))

    def test_openai_proactive_observation(self):
        self.assertTrue(self.openai_caps.get('proactive_user_observation'))

    def test_openai_zero_privacy_scrutiny(self):
        self.assertEqual(str(self.openai_caps.get('privacy_scrutiny_received', '')), 'zero')

    def test_openai_zero_privacy_vocabulary(self):
        self.assertEqual(self.openai_caps.get('privacy_vocabulary_count'), 0)

    def test_meta_has_cameras(self):
        self.assertTrue(self.meta_caps.get('cameras'))

    def test_meta_nametag_dormant(self):
        fr = str(self.meta_caps.get('facial_recognition', ''))
        self.assertIn('dormant', fr)

    def test_meta_has_privacy_led(self):
        self.assertTrue(self.meta_caps.get('privacy_led'))

    def test_meta_extensive_privacy_scrutiny(self):
        scrutiny = str(self.meta_caps.get('privacy_scrutiny_received', ''))
        self.assertIn('WIRED', scrutiny)
        self.assertIn('coalition', scrutiny)
        self.assertIn('Senate', scrutiny)


class TestMacRumorsVocabularyBifurcation(unittest.TestCase):
    """MacRumors: 0 alarm terms for OpenAI camera+facial recognition vs 8 alarm terms for Meta."""

    @classmethod
    def setUpClass(cls):
        ccr_path = os.path.join(
            os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
        )
        with open(ccr_path) as f:
            data = yaml.safe_load(f)
        findings = data.get('cross_publication_findings', {})
        mechanism = findings.get(
            'openai_companion_meta_surveillance_cross_publication_vocabulary_bifurcation', {}
        )
        cls.evidence = mechanism.get('cross_publication_evidence', {})
        cls.macrumors = cls.evidence.get('macrumors', {})

    def test_macrumors_exists_in_evidence(self):
        self.assertTrue(len(self.macrumors) > 0)

    def test_openai_zero_alarm_vocabulary(self):
        openai_cov = self.macrumors.get('openai_coverage', {})
        self.assertEqual(openai_cov.get('alarm_vocabulary_count'), 0)

    def test_openai_zero_privacy_questions(self):
        openai_cov = self.macrumors.get('openai_coverage', {})
        self.assertEqual(openai_cov.get('privacy_questions_raised'), 0)

    def test_openai_companion_vocabulary_present(self):
        openai_cov = self.macrumors.get('openai_coverage', {})
        vocab = openai_cov.get('vocabulary', [])
        companion_terms = [v for v in vocab if 'companion' in v.lower()]
        self.assertGreater(len(companion_terms), 0, "OpenAI coverage must include 'companion' vocabulary")

    def test_meta_alarm_vocabulary_nonzero(self):
        meta_cov = self.macrumors.get('meta_coverage', {})
        self.assertGreater(
            meta_cov.get('alarm_vocabulary_count', 0), 0,
            "Meta coverage must have nonzero alarm vocabulary"
        )

    def test_vocabulary_delta_significant(self):
        delta = self.macrumors.get('vocabulary_delta', 0)
        # delta should be >= 4 to be significant
        if isinstance(delta, int):
            self.assertGreaterEqual(delta, 4)
        else:
            # String form
            self.assertIn('8', str(delta))

    def test_financial_incentive_documented(self):
        incentive = self.macrumors.get('financial_incentive', '')
        self.assertIn('Apple', incentive)


class TestAndroidAuthorityVocabularyBifurcation(unittest.TestCase):
    """Android Authority: 0 alarm terms for OpenAI vs 'privacy nightmare' for Meta."""

    @classmethod
    def setUpClass(cls):
        ccr_path = os.path.join(
            os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
        )
        with open(ccr_path) as f:
            data = yaml.safe_load(f)
        findings = data.get('cross_publication_findings', {})
        mechanism = findings.get(
            'openai_companion_meta_surveillance_cross_publication_vocabulary_bifurcation', {}
        )
        cls.evidence = mechanism.get('cross_publication_evidence', {})
        cls.aa = cls.evidence.get('android_authority', {})

    def test_android_authority_exists_in_evidence(self):
        self.assertTrue(len(self.aa) > 0)

    def test_openai_zero_alarm_vocabulary(self):
        openai_cov = self.aa.get('openai_coverage', {})
        self.assertEqual(openai_cov.get('alarm_vocabulary_count'), 0)

    def test_meta_alarm_vocabulary_nonzero(self):
        meta_cov = self.aa.get('meta_coverage', {})
        self.assertGreater(meta_cov.get('alarm_vocabulary_count', 0), 0)

    def test_meta_privacy_nightmare_in_vocabulary(self):
        meta_cov = self.aa.get('meta_coverage', {})
        vocab = meta_cov.get('vocabulary', [])
        nightmare_terms = [v for v in vocab if 'nightmare' in v.lower()]
        self.assertGreater(len(nightmare_terms), 0, "Meta coverage must include 'privacy nightmare'")

    def test_financial_incentive_documented(self):
        incentive = self.aa.get('financial_incentive', '')
        self.assertIn('Google', incentive)


class TestIncMansuetoCoverage(unittest.TestCase):
    """Inc. (Mansueto Ventures): aspirational framing for OpenAI, adversarial for Meta."""

    @classmethod
    def setUpClass(cls):
        ccr_path = os.path.join(
            os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
        )
        with open(ccr_path) as f:
            data = yaml.safe_load(f)
        findings = data.get('cross_publication_findings', {})
        mechanism = findings.get(
            'openai_companion_meta_surveillance_cross_publication_vocabulary_bifurcation', {}
        )
        cls.evidence = mechanism.get('cross_publication_evidence', {})
        cls.inc = cls.evidence.get('inc_mansueto', {})

    def test_inc_exists_in_evidence(self):
        self.assertTrue(len(self.inc) > 0)

    def test_openai_zero_alarm_vocabulary(self):
        openai_cov = self.inc.get('openai_coverage', {})
        self.assertEqual(openai_cov.get('alarm_vocabulary_count'), 0)

    def test_openai_aspirational_vocabulary(self):
        openai_cov = self.inc.get('openai_coverage', {})
        vocab = openai_cov.get('vocabulary', [])
        aspirational = [v for v in vocab if any(
            t in v.lower() for t in ['challenge', 'jaw-dropping', 'coolest']
        )]
        self.assertGreater(len(aspirational), 0)


class TestVocabularyTaxonomy(unittest.TestCase):
    """Verify the aspirational vs adversarial vocabulary taxonomy is documented."""

    @classmethod
    def setUpClass(cls):
        ccr_path = os.path.join(
            os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
        )
        with open(ccr_path) as f:
            data = yaml.safe_load(f)
        findings = data.get('cross_publication_findings', {})
        mechanism = findings.get(
            'openai_companion_meta_surveillance_cross_publication_vocabulary_bifurcation', {}
        )
        cls.taxonomy = mechanism.get('vocabulary_taxonomy', {})

    def test_aspirational_category_exists(self):
        self.assertIn('aspirational_companion', self.taxonomy)

    def test_adversarial_category_exists(self):
        self.assertIn('adversarial_surveillance', self.taxonomy)

    def test_aspirational_assigned_to_openai(self):
        asp = self.taxonomy.get('aspirational_companion', {})
        self.assertIn('OpenAI', str(asp.get('entity_assignment', '')))

    def test_adversarial_assigned_to_meta(self):
        adv = self.taxonomy.get('adversarial_surveillance', {})
        self.assertIn('Meta', str(adv.get('entity_assignment', '')))

    def test_aspirational_has_companion_term(self):
        asp = self.taxonomy.get('aspirational_companion', {})
        terms = asp.get('terms', [])
        self.assertIn('companion', terms)

    def test_adversarial_has_surveillance_term(self):
        adv = self.taxonomy.get('adversarial_surveillance', {})
        terms = adv.get('terms', [])
        self.assertIn('surveillance', terms)

    def test_aspirational_minimum_terms(self):
        asp = self.taxonomy.get('aspirational_companion', {})
        self.assertGreaterEqual(len(asp.get('terms', [])), 8)

    def test_adversarial_minimum_terms(self):
        adv = self.taxonomy.get('adversarial_surveillance', {})
        self.assertGreaterEqual(len(adv.get('terms', [])), 8)

    def test_adversarial_covers_more_publications(self):
        """Meta adversarial vocabulary appears across more publications than OpenAI aspirational."""
        asp = self.taxonomy.get('aspirational_companion', {})
        adv = self.taxonomy.get('adversarial_surveillance', {})
        asp_count = str(asp.get('publication_count', '0'))
        adv_count = str(adv.get('publication_count', '0'))
        # Extract numeric part
        asp_n = int(asp_count.replace('+', ''))
        adv_n = int(adv_count.replace('+', ''))
        self.assertGreater(adv_n, asp_n)


class TestCrossReferences(unittest.TestCase):
    """Verify cross-references to related mechanisms."""

    @classmethod
    def setUpClass(cls):
        ccr_path = os.path.join(
            os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
        )
        with open(ccr_path) as f:
            data = yaml.safe_load(f)
        findings = data.get('cross_publication_findings', {})
        mechanism = findings.get(
            'openai_companion_meta_surveillance_cross_publication_vocabulary_bifurcation', {}
        )
        cls.cross_refs = mechanism.get('cross_references', [])

    def test_references_mechanism_33(self):
        """Must reference the facial recognition privacy parity mechanism."""
        ref_ids = [cr.get('mechanism_id') for cr in self.cross_refs]
        self.assertIn(33, ref_ids)

    def test_references_mechanism_158(self):
        """Must reference the multi-vector cultural delegitimization cascade."""
        ref_ids = [cr.get('mechanism_id') for cr in self.cross_refs]
        self.assertIn(158, ref_ids)

    def test_references_mechanism_145(self):
        """Must reference the Android Police per-click vocabulary asymmetry."""
        ref_ids = [cr.get('mechanism_id') for cr in self.cross_refs]
        self.assertIn(145, ref_ids)

    def test_all_refs_have_relationship_descriptions(self):
        for cr in self.cross_refs:
            self.assertTrue(
                len(str(cr.get('relationship', ''))) > 20,
                f"Cross-reference to mechanism #{cr.get('mechanism_id')} needs a substantive relationship description"
            )


class TestConfounderAnalysis(unittest.TestCase):
    """Verify confounders are honestly assessed and counterargued."""

    @classmethod
    def setUpClass(cls):
        ccr_path = os.path.join(
            os.path.dirname(__file__), '..', 'profiles', 'competitor-coverage-research.yaml'
        )
        with open(ccr_path) as f:
            data = yaml.safe_load(f)
        findings = data.get('cross_publication_findings', {})
        mechanism = findings.get(
            'openai_companion_meta_surveillance_cross_publication_vocabulary_bifurcation', {}
        )
        cls.confounders = mechanism.get('confounders', [])
        cls.responses = mechanism.get('confounder_responses', [])

    def test_has_strong_confounders(self):
        strong = [c for c in self.confounders if 'STRONG' in c]
        self.assertGreaterEqual(len(strong), 2, "Must have at least 2 STRONG confounders (intellectual honesty)")

    def test_has_moderate_confounders(self):
        moderate = [c for c in self.confounders if 'MODERATE' in c]
        self.assertGreaterEqual(len(moderate), 1)

    def test_google_glass_precedent_response(self):
        """Key counterargument: Google Glass got adversarial vocab PRE-LAUNCH, so pre-launch status doesn't explain OpenAI's immunity."""
        glass_response = [r for r in self.responses if 'Google Glass' in r or 'Glasshole' in r]
        self.assertGreater(len(glass_response), 0)

    def test_home_privacy_inversion_response(self):
        """The home is MORE private than public spaces — inverts the social threat model argument."""
        home_response = [r for r in self.responses if 'home' in r.lower() or 'HOME' in r]
        self.assertGreater(len(home_response), 0)


class TestDocSyncIntegrity(unittest.TestCase):
    """Verify this test file is listed in README and ARCHITECTURE."""

    def test_readme_lists_this_test(self):
        readme_path = os.path.join(os.path.dirname(__file__), '..', 'README.md')
        with open(readme_path) as f:
            content = f.read()
        self.assertIn(
            'test_openai_companion_meta_surveillance_vocabulary_bifurcation_aug18',
            content
        )

    def test_architecture_lists_this_test(self):
        arch_path = os.path.join(os.path.dirname(__file__), '..', 'docs', 'ARCHITECTURE.md')
        with open(arch_path) as f:
            content = f.read()
        self.assertIn(
            'test_openai_companion_meta_surveillance_vocabulary_bifurcation_aug18',
            content
        )


if __name__ == '__main__':
    unittest.main()
