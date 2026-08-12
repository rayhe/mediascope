"""
Type D Cross-Validation — 10am Aug 12 2026

Validates mechanisms #63 (Maxwell Zeff Source Access Framing Shift) and #64
(Cloudflare Publisher AI Crawl Default-Block Google-OpenAI Asymmetry Accelerator)
for internal consistency, cross-reference integrity, and integration with
existing publication/entity profiles.

Focus areas:
1. Mechanism profile completeness (required fields, source URLs, confounding factors)
2. Cross-reference graph integrity (bidirectional references, no orphans)
3. Entity profile integration (new mechanisms reflected in entity YAML)
4. Journalist career tracking consistency (Zeff career path in journalists.yaml)
5. Publication profile consistency (WIRED, FT, Atlantic reflect new findings)
"""

import os
import re
import unittest

import yaml

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(filename):
    path = os.path.join(PROFILES_DIR, filename)
    with open(path) as f:
        return yaml.safe_load(f)


class TestMechanism63ProfileCompleteness(unittest.TestCase):
    """Validate mechanism #63 has all required fields and correct metadata."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml('competitor-coverage-research.yaml')
        cpf = cls.research.get('cross_publication_findings', {})
        cls.mech63 = None
        for key, val in cpf.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 63:
                cls.mech63 = val
                cls.mech63_key = key
                break
        if cls.mech63 is None:
            # Search in aggregate_findings too
            for key, val in cls.research.get('aggregate_findings', {}).items():
                if isinstance(val, dict) and val.get('mechanism_id') == 63:
                    cls.mech63 = val
                    cls.mech63_key = key
                    break

    def test_mechanism_63_exists(self):
        self.assertIsNotNone(self.mech63, "Mechanism #63 not found in research profiles")

    def test_has_required_fields(self):
        required = ['mechanism_id', 'title', 'date_added', 'finding_type',
                     'entities', 'publications', 'finding_summary']
        for field in required:
            self.assertIn(field, self.mech63, f"Missing required field: {field}")

    def test_finding_type_is_journalist(self):
        self.assertEqual(self.mech63['finding_type'], 'journalist_cross_entity_tracking')

    def test_entities_include_meta_openai_anthropic(self):
        entities = self.mech63['entities']
        for entity in ['meta', 'openai', 'anthropic']:
            self.assertIn(entity, entities, f"Expected entity '{entity}' in mechanism #63")

    def test_publications_include_wired_gizmodo_techcrunch(self):
        pubs = self.mech63['publications']
        for pub in ['wired', 'gizmodo', 'techcrunch']:
            self.assertIn(pub, pubs, f"Expected publication '{pub}' in mechanism #63")

    def test_has_source_urls(self):
        urls = self.mech63.get('source_urls', [])
        self.assertGreaterEqual(len(urls), 5, "Mechanism #63 should have at least 5 source URLs")

    def test_has_confounding_factors(self):
        factors = self.mech63.get('confounding_factors', [])
        self.assertGreaterEqual(len(factors), 4, "Mechanism #63 should have at least 4 confounding factors")

    def test_confounding_factors_have_strength(self):
        for factor in self.mech63.get('confounding_factors', []):
            self.assertIn('strength', factor,
                          f"Confounding factor missing strength: {factor.get('factor', 'unknown')}")

    def test_has_testable_predictions(self):
        preds = self.mech63.get('testable_predictions', [])
        self.assertGreaterEqual(len(preds), 3, "Should have at least 3 testable predictions")

    def test_has_cross_references(self):
        xrefs = self.mech63.get('cross_references', [])
        self.assertGreaterEqual(len(xrefs), 2, "Should cross-reference at least 2 other mechanisms")

    def test_cross_references_valid_ids(self):
        """Cross-referenced mechanism IDs should exist in the research profile."""
        all_ids = set()
        for section in ['cross_publication_findings', 'aggregate_findings']:
            for key, val in self.research.get(section, {}).items():
                if isinstance(val, dict) and 'mechanism_id' in val:
                    all_ids.add(val['mechanism_id'])
        for xref in self.mech63.get('cross_references', []):
            ref_id = xref.get('mechanism_id')
            self.assertIn(ref_id, all_ids,
                          f"Cross-reference to mechanism #{ref_id} but it doesn't exist")


class TestMechanism64ProfileCompleteness(unittest.TestCase):
    """Validate mechanism #64 has all required fields and correct metadata."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml('competitor-coverage-research.yaml')
        cpf = cls.research.get('cross_publication_findings', {})
        cls.mech64 = None
        for key, val in cpf.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 64:
                cls.mech64 = val
                cls.mech64_key = key
                break

    def test_mechanism_64_exists(self):
        self.assertIsNotNone(self.mech64, "Mechanism #64 not found in research profiles")

    def test_has_required_fields(self):
        required = ['mechanism_id', 'title', 'date_added', 'finding_type',
                     'entities', 'publications', 'finding_summary']
        for field in required:
            self.assertIn(field, self.mech64, f"Missing required field: {field}")

    def test_finding_type_is_financial(self):
        self.assertEqual(self.mech64['finding_type'], 'financial_incentive_mapping')

    def test_entities_include_google_openai(self):
        entities = self.mech64['entities']
        for entity in ['google', 'openai']:
            self.assertIn(entity, entities, f"Expected entity '{entity}' in mechanism #64")

    def test_has_source_urls(self):
        urls = self.mech64.get('source_urls', [])
        self.assertGreaterEqual(len(urls), 8, "Mechanism #64 should have at least 8 source URLs")

    def test_has_confounding_factors(self):
        factors = self.mech64.get('confounding_factors', [])
        self.assertGreaterEqual(len(factors), 5, "Mechanism #64 should have at least 5 confounding factors")

    def test_has_cross_references(self):
        xrefs = self.mech64.get('cross_references', [])
        self.assertGreaterEqual(len(xrefs), 3, "Should cross-reference at least 3 other mechanisms")

    def test_cross_references_include_key_mechanisms(self):
        """Should reference the Google ad dependency and OpenAI publisher displacement mechanisms."""
        xref_ids = {xr['mechanism_id'] for xr in self.mech64.get('cross_references', [])}
        # Should reference at least one of: #35 (Google ad dependency), #41, #47, #55
        key_refs = {35, 41, 47, 55}
        overlap = xref_ids & key_refs
        self.assertGreaterEqual(len(overlap), 2,
                                f"Should cross-ref at least 2 of {key_refs}, got {overlap}")


class TestZeffJournalistProfile(unittest.TestCase):
    """Validate Maxwell Zeff's career tracking in journalists.yaml."""

    @classmethod
    def setUpClass(cls):
        cls.journalists = load_yaml('careers/journalists.yaml')
        cls.zeff = None
        for j in cls.journalists.get('journalists', []):
            if 'zeff' in j.get('name', '').lower():
                cls.zeff = j
                break

    def test_zeff_exists_in_profiles(self):
        self.assertIsNotNone(self.zeff, "Maxwell Zeff not found in journalists.yaml")

    def test_has_career_history(self):
        # Zeff profile uses 'career' key, not 'career_history'
        history = self.zeff.get('career', self.zeff.get('career_history',
                   self.zeff.get('positions', [])))
        self.assertGreaterEqual(len(history), 2, "Should have at least 2 career positions")

    def test_has_competitor_coverage(self):
        cc = self.zeff.get('competitor_coverage', {})
        self.assertTrue(len(cc) > 0, "Should have competitor_coverage data")

    def test_has_cross_entity_analysis(self):
        cc = self.zeff.get('competitor_coverage', {})
        xea = cc.get('cross_entity_analysis', cc.get('entity_analysis', {}))
        self.assertTrue(len(xea) > 0 if isinstance(xea, dict) else xea is not None,
                        "Should have cross_entity_analysis in competitor_coverage")


class TestEntityProfileIntegration(unittest.TestCase):
    """Verify that new mechanisms are reflected in competitor-entities.yaml."""

    @classmethod
    def setUpClass(cls):
        cls.entities = load_yaml('competitor-entities.yaml')

    def test_google_has_cloudflare_section(self):
        """Mechanism #64 should add cloudflare-related data to google entity."""
        google = self.entities.get('entities', {}).get('google', {})
        # Check for cloudflare reference in any nested key
        google_str = yaml.dump(google).lower()
        self.assertIn('cloudflare', google_str,
                      "Google entity should reference Cloudflare crawl block")

    def test_openai_has_content_licensing_deals(self):
        """OpenAI entity should document publisher content licensing deals."""
        openai = self.entities.get('entities', {}).get('openai', {})
        openai_str = yaml.dump(openai).lower()
        self.assertIn('content', openai_str,
                      "OpenAI entity should reference content licensing")


class TestMechanismSequenceIntegrity(unittest.TestCase):
    """Verify mechanism IDs 1-64 form a valid sequence."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml('competitor-coverage-research.yaml')
        cls.all_ids = []
        for section in ['cross_publication_findings', 'aggregate_findings']:
            for key, val in cls.research.get(section, {}).items():
                if isinstance(val, dict) and 'mechanism_id' in val:
                    cls.all_ids.append(val['mechanism_id'])

    def test_no_duplicate_ids(self):
        seen = set()
        dupes = []
        for mid in self.all_ids:
            if mid in seen:
                dupes.append(mid)
            seen.add(mid)
        self.assertFalse(dupes, f"Duplicate mechanism IDs: {dupes}")

    def test_max_mechanism_at_least_64(self):
        self.assertGreaterEqual(max(self.all_ids), 64,
                                f"Expected max mechanism_id>=64, got {max(self.all_ids)}")

    def test_recent_mechanisms_contiguous(self):
        """Mechanisms 50 through max should form a contiguous sequence."""
        recent = sorted(mid for mid in self.all_ids if mid >= 50)
        expected = list(range(50, max(recent) + 1))
        self.assertEqual(recent, expected,
                         f"Gap in mechanisms 50+: {recent} vs expected {expected}")

    def test_mechanisms_63_and_64_present(self):
        self.assertIn(63, self.all_ids, "Mechanism #63 missing")
        self.assertIn(64, self.all_ids, "Mechanism #64 missing")


class TestCrossReferenceGraphIntegrity(unittest.TestCase):
    """Validate the cross-reference graph is connected and consistent."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml('competitor-coverage-research.yaml')
        cls.mechanisms = {}
        for section in ['cross_publication_findings', 'aggregate_findings']:
            for key, val in cls.research.get(section, {}).items():
                if isinstance(val, dict) and 'mechanism_id' in val:
                    cls.mechanisms[val['mechanism_id']] = val

    def test_all_cross_refs_point_to_existing_mechanisms(self):
        all_ids = set(self.mechanisms.keys())
        for mid, mech in self.mechanisms.items():
            for xref in mech.get('cross_references', []):
                if isinstance(xref, dict):
                    ref_id = xref.get('mechanism_id')
                    if ref_id is not None:
                        self.assertIn(ref_id, all_ids,
                                      f"Mechanism #{mid} references non-existent #{ref_id}")
                # String cross-refs are legacy format — skip validation

    def test_cross_refs_have_connection_text(self):
        for mid, mech in self.mechanisms.items():
            for xref in mech.get('cross_references', []):
                if isinstance(xref, dict):
                    conn = xref.get('connection', '') or xref.get('relationship', '')
                    self.assertTrue(len(conn) > 10,
                                    f"Mechanism #{mid} cross-ref to #{xref.get('mechanism_id')} "
                                    f"has empty/short connection text")
                elif isinstance(xref, str):
                    self.assertTrue(len(xref) > 10,
                                    f"Mechanism #{mid} has empty/short string cross-ref")

    def test_mechanism_63_references_62(self):
        """#63 (Zeff) should reference #62 (WIRED Anthropic framing)."""
        mech63 = self.mechanisms.get(63)
        if mech63:
            xref_ids = {xr['mechanism_id'] for xr in mech63.get('cross_references', [])}
            self.assertIn(62, xref_ids,
                          "Mechanism #63 should cross-reference #62 (WIRED Anthropic)")

    def test_mechanism_64_references_35_or_41(self):
        """#64 (Cloudflare) should reference Google ad dependency mechanisms."""
        mech64 = self.mechanisms.get(64)
        if mech64:
            xref_ids = {xr['mechanism_id'] for xr in mech64.get('cross_references', [])}
            self.assertTrue(xref_ids & {35, 41, 47, 55},
                            f"Mechanism #64 should reference Google/OpenAI financial mechanisms, "
                            f"got refs to {xref_ids}")


class TestFindingSummaryQuality(unittest.TestCase):
    """Validate that finding summaries meet MediaScope quality standards."""

    @classmethod
    def setUpClass(cls):
        cls.research = load_yaml('competitor-coverage-research.yaml')
        cls.mechanisms = {}
        for section in ['cross_publication_findings', 'aggregate_findings']:
            for key, val in cls.research.get(section, {}).items():
                if isinstance(val, dict) and 'mechanism_id' in val:
                    cls.mechanisms[val['mechanism_id']] = val

    def test_mechanism_63_summary_mentions_gizmodo_wired_shift(self):
        mech = self.mechanisms.get(63, {})
        summary = mech.get('finding_summary', '')
        self.assertIn('Gizmodo', summary)
        self.assertIn('WIRED', summary)

    def test_mechanism_63_summary_mentions_source_access(self):
        mech = self.mechanisms.get(63, {})
        summary = mech.get('finding_summary', '')
        # Should mention source access as a mechanism
        self.assertTrue('source' in summary.lower() or 'access' in summary.lower(),
                        "Should discuss source access asymmetry")

    def test_mechanism_64_summary_mentions_cloudflare(self):
        mech = self.mechanisms.get(64, {})
        summary = mech.get('finding_summary', '')
        self.assertIn('Cloudflare', summary)

    def test_mechanism_64_summary_mentions_crawler(self):
        mech = self.mechanisms.get(64, {})
        summary = mech.get('finding_summary', '')
        self.assertTrue('crawler' in summary.lower() or 'crawl' in summary.lower(),
                        "Should mention crawler blocking mechanism")

    def test_mechanism_64_summary_mentions_api_based_deals(self):
        mech = self.mechanisms.get(64, {})
        summary = mech.get('finding_summary', '')
        self.assertTrue('api' in summary.lower() or 'API' in summary,
                        "Should contrast API-based deals vs crawler-based access")

    def test_no_weasel_words_in_recent_summaries(self):
        """Recent mechanisms should avoid vague hedging language."""
        weasel_patterns = [r'\bsome say\b', r'\binteresting\b', r'\bperhaps\b',
                           r'\bit seems\b', r'\bone could argue\b']
        for mid in [63, 64]:
            mech = self.mechanisms.get(mid, {})
            summary = mech.get('finding_summary', '')
            for pattern in weasel_patterns:
                self.assertIsNone(re.search(pattern, summary, re.IGNORECASE),
                                  f"Mechanism #{mid} uses weasel language: {pattern}")
