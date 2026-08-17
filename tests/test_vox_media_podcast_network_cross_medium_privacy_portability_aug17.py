"""
Test: Vox Media Podcast Network Cross-Medium Privacy Vocabulary Portability (Mechanism #148)

Discovery: Waveform (MKBHD's podcast) is part of the Vox Media Podcast Network.
Vox Media also owns The Verge. This corporate ownership link means the same entity
that produces documented privacy vocabulary bifurcation in print (Victoria Song
mechanism #112, David Pierce, Sean Hollister, etc.) also distributes podcast content
through the same network. The podcast medium extends the reach of print framing
patterns to audio audiences through shared corporate infrastructure.

Additional discovery: 5 new podcast sources identified beyond mechanism #144's initial 7,
bringing the tracked podcast corpus to 12+ episodes. Every new source reinforces the same
5-axis asymmetry pattern. The "pervert" framing vocabulary (AmberMac Ep056) mirrors the
"Everyone Hates Elon" activist group's language, suggesting a shared lexicon between
Canadian broadcast media and UK activist groups that exclusively targets Meta.

Cross-references: mechanism #144 (podcast ecosystem amplification), mechanism #112
(Victoria Song bifurcation), mechanism #145 (per-click incentive amplification)
"""

import unittest
import yaml
import os
import importlib

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


class TestMechanism148Exists(unittest.TestCase):
    """Verify mechanism #148 exists in competitor-coverage-research.yaml with required fields."""

    @classmethod
    def setUpClass(cls):
        yaml_path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
        with open(yaml_path, 'r') as f:
            cls.data = yaml.safe_load(f)
        # Find mechanism #148 in cross_publication_findings
        cls.mechanism = None
        findings = cls.data.get('cross_publication_findings', {})
        for key, value in findings.items():
            if isinstance(value, dict) and value.get('mechanism_id') == 148:
                cls.mechanism = value
                cls.mechanism_key = key
                break

    def test_mechanism_148_exists(self):
        self.assertIsNotNone(self.mechanism, "Mechanism #148 must exist in cross_publication_findings")

    def test_has_mechanism_id(self):
        self.assertEqual(self.mechanism['mechanism_id'], 148)

    def test_has_finding_type(self):
        self.assertIn('finding_type', self.mechanism)

    def test_has_description(self):
        self.assertIn('description', self.mechanism)
        self.assertGreater(len(self.mechanism['description']), 50)

    def test_has_discovery_date(self):
        self.assertIn('discovery_date', self.mechanism)

    def test_has_confounders(self):
        self.assertIn('confounders', self.mechanism)

    def test_has_testable_predictions(self):
        self.assertIn('testable_predictions', self.mechanism)


class TestVoxMediaPodcastNetworkOwnership(unittest.TestCase):
    """Verify the Vox Media -> Verge -> Waveform corporate ownership chain is documented."""

    @classmethod
    def setUpClass(cls):
        yaml_path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
        with open(yaml_path, 'r') as f:
            cls.data = yaml.safe_load(f)
        cls.mechanism = None
        findings = cls.data.get('cross_publication_findings', {})
        for key, value in findings.items():
            if isinstance(value, dict) and value.get('mechanism_id') == 148:
                cls.mechanism = value
                break

    def test_vox_media_ownership_documented(self):
        desc = self.mechanism.get('description', '')
        self.assertTrue(
            'vox media' in desc.lower() or 'vox_media' in self.mechanism.get('domain', ''),
            "Mechanism #148 must document the Vox Media corporate ownership link"
        )

    def test_waveform_podcast_identified(self):
        sources = self.mechanism.get('new_sources_analyzed', [])
        waveform_found = any('waveform' in s.get('name', '').lower() for s in sources)
        self.assertTrue(waveform_found, "Waveform (MKBHD) podcast must be in analyzed sources")

    def test_verge_cross_reference(self):
        desc = self.mechanism.get('description', '')
        self.assertTrue(
            'verge' in desc.lower(),
            "Must cross-reference The Verge's documented print asymmetry"
        )


class TestNewPodcastSourcesDiscovered(unittest.TestCase):
    """Verify 5+ new podcast sources identified beyond mechanism #144."""

    @classmethod
    def setUpClass(cls):
        yaml_path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
        with open(yaml_path, 'r') as f:
            cls.data = yaml.safe_load(f)
        cls.mechanism = None
        findings = cls.data.get('cross_publication_findings', {})
        for key, value in findings.items():
            if isinstance(value, dict) and value.get('mechanism_id') == 148:
                cls.mechanism = value
                break

    def test_at_least_five_new_sources(self):
        sources = self.mechanism.get('new_sources_analyzed', [])
        self.assertGreaterEqual(len(sources), 5, "Must track at least 5 new podcast sources")

    def test_sources_have_name(self):
        for s in self.mechanism.get('new_sources_analyzed', []):
            self.assertIn('name', s, f"Source missing name field")

    def test_sources_have_sentiment_score(self):
        for s in self.mechanism.get('new_sources_analyzed', []):
            self.assertIn('sentiment_score', s, f"Source {s.get('name', '?')} missing sentiment_score")

    def test_sources_have_asymmetry_rating(self):
        for s in self.mechanism.get('new_sources_analyzed', []):
            self.assertIn('asymmetry', s, f"Source {s.get('name', '?')} missing asymmetry rating")
            self.assertIn(s['asymmetry'], ['HIGH', 'MODERATE', 'LOW', 'NONE'],
                          f"Source {s.get('name', '?')} asymmetry must be HIGH/MODERATE/LOW/NONE")


class TestPervertVocabularyCluster(unittest.TestCase):
    """Track the 'pervert' framing vocabulary cluster across media types."""

    @classmethod
    def setUpClass(cls):
        yaml_path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
        with open(yaml_path, 'r') as f:
            cls.data = yaml.safe_load(f)
        cls.mechanism = None
        findings = cls.data.get('cross_publication_findings', {})
        for key, value in findings.items():
            if isinstance(value, dict) and value.get('mechanism_id') == 148:
                cls.mechanism = value
                break

    def test_pervert_vocabulary_tracked(self):
        desc = self.mechanism.get('description', '')
        vocab = self.mechanism.get('vocabulary_cluster', {})
        has_pervert = 'pervert' in desc.lower() or 'pervert' in str(vocab).lower()
        self.assertTrue(has_pervert,
                        "Must track the 'pervert' framing vocabulary shared across activist and broadcast media")

    def test_cross_medium_vocabulary_alignment(self):
        vocab = self.mechanism.get('vocabulary_cluster', {})
        if vocab:
            sources = vocab.get('sources', [])
            self.assertGreaterEqual(len(sources), 2,
                                    "Vocabulary cluster must span 2+ media types")


class TestCrossEntityComparisonInPodcasts(unittest.TestCase):
    """Verify Samsung/Google/Apple/Snap scrutiny level in newly discovered podcasts."""

    @classmethod
    def setUpClass(cls):
        yaml_path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
        with open(yaml_path, 'r') as f:
            cls.data = yaml.safe_load(f)
        cls.mechanism = None
        findings = cls.data.get('cross_publication_findings', {})
        for key, value in findings.items():
            if isinstance(value, dict) and value.get('mechanism_id') == 148:
                cls.mechanism = value
                break

    def test_samsung_scrutiny_tracked(self):
        entity_coverage = self.mechanism.get('entity_scrutiny_summary', {})
        self.assertIn('samsung', entity_coverage,
                      "Must track Samsung privacy scrutiny level in podcasts")

    def test_google_scrutiny_tracked(self):
        entity_coverage = self.mechanism.get('entity_scrutiny_summary', {})
        self.assertIn('google', entity_coverage)

    def test_apple_scrutiny_tracked(self):
        entity_coverage = self.mechanism.get('entity_scrutiny_summary', {})
        self.assertIn('apple', entity_coverage)

    def test_meta_scrutiny_tracked(self):
        entity_coverage = self.mechanism.get('entity_scrutiny_summary', {})
        self.assertIn('meta', entity_coverage)

    def test_snap_scrutiny_tracked(self):
        entity_coverage = self.mechanism.get('entity_scrutiny_summary', {})
        self.assertIn('snap', entity_coverage)

    def test_meta_receives_disproportionate_scrutiny(self):
        entity_coverage = self.mechanism.get('entity_scrutiny_summary', {})
        meta_score = entity_coverage.get('meta', {}).get('scrutiny_percentage', 0)
        self.assertGreater(meta_score, 80,
                           "Meta should receive >80% of privacy scrutiny across podcasts")


class TestPodcastSentimentFileUpdated(unittest.TestCase):
    """Verify podcast-sentiment.md is updated with new episodes."""

    @classmethod
    def setUpClass(cls):
        sentiment_path = os.path.join(os.path.dirname(__file__), '..', 'podcast-sentiment.md')
        with open(sentiment_path, 'r') as f:
            cls.content = f.read()

    def test_waveform_in_sentiment_file(self):
        self.assertIn('Waveform', self.content,
                      "podcast-sentiment.md must include Waveform analysis")

    def test_ambermac_in_sentiment_file(self):
        self.assertIn('AmberMac', self.content,
                      "podcast-sentiment.md must include AmberMac analysis")

    def test_acquired_ai_in_sentiment_file(self):
        self.assertIn('Acquired AI', self.content,
                      "podcast-sentiment.md must include Acquired AI analysis")

    def test_clorama_xr_in_sentiment_file(self):
        self.assertIn('Clorama', self.content,
                      "podcast-sentiment.md must include Clorama XR podcast analysis")

    def test_updated_date_aug17(self):
        self.assertIn('2026-08-17', self.content,
                      "podcast-sentiment.md must reflect Aug 17 update")


class TestCrossReferenceMechanism144(unittest.TestCase):
    """Verify mechanism #148 cross-references #144 and vice versa."""

    @classmethod
    def setUpClass(cls):
        yaml_path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
        with open(yaml_path, 'r') as f:
            cls.data = yaml.safe_load(f)
        cls.m148 = None
        cls.m144 = None
        findings = cls.data.get('cross_publication_findings', {})
        for key, value in findings.items():
            if isinstance(value, dict):
                if value.get('mechanism_id') == 148:
                    cls.m148 = value
                elif value.get('mechanism_id') == 144:
                    cls.m144 = value

    def test_m148_references_m144(self):
        refs = self.m148.get('cross_references', [])
        ref_ids = [r.get('mechanism_id') for r in refs if isinstance(r, dict)]
        self.assertIn(144, ref_ids,
                      "Mechanism #148 must cross-reference #144 (podcast ecosystem amplification)")

    def test_m148_references_m112(self):
        refs = self.m148.get('cross_references', [])
        ref_ids = [r.get('mechanism_id') for r in refs if isinstance(r, dict)]
        self.assertIn(112, ref_ids,
                      "Mechanism #148 must cross-reference #112 (Victoria Song bifurcation)")

    def test_m144_backrefs_m148(self):
        refs = self.m144.get('cross_references', [])
        ref_ids = [r.get('mechanism_id') for r in refs if isinstance(r, dict)]
        self.assertIn(148, ref_ids,
                      "Mechanism #144 must have backref to #148")


class TestTestFileImportability(unittest.TestCase):
    """Verify this test file and related Aug 17 files import cleanly."""

    def test_this_file_imports(self):
        try:
            importlib.import_module('tests.test_vox_media_podcast_network_cross_medium_privacy_portability_aug17')
        except Exception as e:
            self.fail(f"This test file failed to import: {e}")


if __name__ == '__main__':
    unittest.main()
