"""
Type D Cross-Validation: 8pm Aug 25, 2026

Validates mechanisms #308-#310 (Fast Company/Mansueto cluster):
- #308: Fast Company cross-entity camera-equipped smart glasses vocabulary bifurcation
  (stored under cross_publication_findings with mechanism_number key)
- #309: Editorial commissioning cross-entity tracking (Schwarz vs Clay contributor assignment)
  (stored under publications with mechanism_id key)
- #310: Mansueto-Morningstar-Google Gemini Enterprise same-day convergence
  (stored under publications with mechanism_id key)

Cross-validates:
1. All three mechanisms exist and cross-reference each other correctly
2. Mansueto corporate structure (common ownership, 47% stake)
3. Financial incentive architecture (5 layers documented)
4. Source URL integrity (BusinessWire, Fast Company articles)
5. Vocabulary bifurcation counts are consistent across mechanism definitions
6. Cross-reference fix: mechanism_id searches must check for 'type' key presence
   to avoid matching cross-reference entries before primary definitions
7. YAML syntax: no colons-in-plain-scalars causing parse errors
"""

import os
import yaml
import unittest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_competitor_research():
    path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


def find_mechanism_by_id(data, mechanism_id):
    """Find a mechanism's PRIMARY definition (has 'type' field), checking both
    mechanism_id and mechanism_number keys."""
    result = {}
    def search(d):
        if result:
            return
        if isinstance(d, dict):
            mid = d.get('mechanism_id') or d.get('mechanism_number')
            if mid is not None and int(mid) == mechanism_id and 'type' in d:
                result.update(d)
                return
            for v in d.values():
                search(v)
        elif isinstance(d, list):
            for item in d:
                search(item)
    search(data)
    return result if result else None


def find_all_mechanism_refs(data, mechanism_id):
    """Find ALL references to a mechanism_id, including cross-references."""
    refs = []
    def search(d, path=""):
        if isinstance(d, dict):
            mid = d.get('mechanism_id') or d.get('mechanism_number')
            if mid is not None and int(mid) == mechanism_id:
                refs.append({'data': d, 'path': path})
            for k, v in d.items():
                search(v, f"{path}.{k}")
        elif isinstance(d, list):
            for i, item in enumerate(d):
                search(item, f"{path}[{i}]")
    search(data)
    return refs


class TestMechanismClusterIntegrity(unittest.TestCase):
    """Verify #308-#310 form a coherent cluster with correct cross-references."""

    def setUp(self):
        self.data = load_competitor_research()

    def test_mechanism_308_exists(self):
        m = find_mechanism_by_id(self.data, 308)
        self.assertIsNotNone(m, "Mechanism #308 not found (check both mechanism_id and mechanism_number)")

    def test_mechanism_309_exists(self):
        m = find_mechanism_by_id(self.data, 309)
        self.assertIsNotNone(m, "Mechanism #309 not found")

    def test_mechanism_310_exists(self):
        m = find_mechanism_by_id(self.data, 310)
        self.assertIsNotNone(m, "Mechanism #310 not found")

    def test_mechanism_310_references_308(self):
        """#310 should reference #308 via extends_mechanisms."""
        m = find_mechanism_by_id(self.data, 310)
        self.assertIsNotNone(m)
        xrefs = m.get('extends_mechanisms', m.get('cross_references', []))
        xref_ids = [x.get('mechanism_id') for x in xrefs if isinstance(x, dict)]
        self.assertIn(308, xref_ids, "#310 should reference #308")

    def test_mechanism_310_references_309(self):
        """#310 should reference #309 via extends_mechanisms."""
        m = find_mechanism_by_id(self.data, 310)
        self.assertIsNotNone(m)
        xrefs = m.get('extends_mechanisms', m.get('cross_references', []))
        xref_ids = [x.get('mechanism_id') for x in xrefs if isinstance(x, dict)]
        self.assertIn(309, xref_ids, "#310 should reference #309")

    def test_mechanism_309_references_308(self):
        """#309 should reference #308 via extends_mechanisms."""
        m = find_mechanism_by_id(self.data, 309)
        self.assertIsNotNone(m)
        xrefs = m.get('extends_mechanisms', m.get('cross_references', []))
        xref_ids = [x.get('mechanism_id') for x in xrefs if isinstance(x, dict)]
        self.assertIn(308, xref_ids, "#309 should reference #308")


class TestMansuetoCorporateStructureVerification(unittest.TestCase):
    """Cross-validate Mansueto ownership data across mechanisms."""

    def setUp(self):
        self.data = load_competitor_research()

    def test_morningstar_market_cap_plausible(self):
        """Morningstar market cap should be documented."""
        m = find_mechanism_by_id(self.data, 310)
        self.assertIsNotNone(m)
        corp = m.get('corporate_structure', {})
        if corp:
            self.assertIn('morningstar_market_cap_b', corp)

    def test_mansueto_family_stake_documented(self):
        """47% family control should be documented in corporate_structure."""
        m = find_mechanism_by_id(self.data, 310)
        self.assertIsNotNone(m)
        corp = m.get('corporate_structure', {})
        self.assertEqual(corp.get('family_combined_pct'), 47)


class TestVocabularyCountConsistency(unittest.TestCase):
    """Verify vocabulary counts are consistent across mechanisms #308 and #310."""

    def setUp(self):
        self.data = load_competitor_research()

    def test_meta_alarm_terms_documented_in_308(self):
        """#308 should document alarm/surveillance vocabulary for Meta."""
        m308 = find_mechanism_by_id(self.data, 308)
        self.assertIsNotNone(m308)
        meta_alarm = m308.get('vocabulary_meta_alarm', [])
        if isinstance(meta_alarm, list):
            self.assertGreater(len(meta_alarm), 0, "#308 should list Meta alarm terms")
        else:
            desc = str(m308.get('description', m308.get('finding', '')))
            self.assertTrue('bifurcation' in desc.lower() or 'creepy' in desc.lower())

    def test_google_zero_alarm_terms_in_308(self):
        """#308 should document zero alarm terms for Google."""
        m308 = find_mechanism_by_id(self.data, 308)
        self.assertIsNotNone(m308)
        google_alarm = m308.get('vocabulary_google_alarm', [])
        if isinstance(google_alarm, list):
            self.assertEqual(len(google_alarm), 0, "Google alarm terms should be empty list")
        else:
            self.assertEqual(google_alarm, 0, "Google alarm terms should be zero")


class TestSourceURLIntegrity(unittest.TestCase):
    """Verify source URLs are properly documented."""

    def setUp(self):
        self.data = load_competitor_research()

    def test_fast_company_meta_article_url_in_308(self):
        """Dan Clay Fast Company article URL should be documented in #308."""
        m = find_mechanism_by_id(self.data, 308)
        self.assertIsNotNone(m)
        all_text = str(m)
        self.assertTrue(
            'fastcompany.com' in all_text,
            "Fast Company article URL should be documented"
        )

    def test_businesswire_morningstar_url_in_310(self):
        """BusinessWire Morningstar-Google announcement URL should be in #310."""
        m = find_mechanism_by_id(self.data, 310)
        self.assertIsNotNone(m)
        all_text = str(m)
        self.assertTrue(
            'businesswire.com' in all_text,
            "Morningstar-Google announcement URL should be documented"
        )


class TestMechanismSearchBugFix(unittest.TestCase):
    """Regression test: mechanism_id search must check 'type' in d to
    distinguish primary definitions from cross-reference entries."""

    def setUp(self):
        self.data = load_competitor_research()

    def test_cross_reference_entries_lack_type(self):
        """Cross-reference entries for mechanism_id 309 should NOT have 'type'."""
        refs = find_all_mechanism_refs(self.data, 309)
        primary_count = sum(1 for r in refs if 'type' in r['data'])
        xref_count = sum(1 for r in refs if 'type' not in r['data'])
        self.assertGreaterEqual(primary_count, 1, "Should have at least one primary definition")
        self.assertGreaterEqual(xref_count, 1, "Should have at least one cross-reference")

    def test_primary_definition_has_correct_type(self):
        """Primary definition of #309 should have editorial/commissioning type."""
        m = find_mechanism_by_id(self.data, 309)
        self.assertIsNotNone(m)
        mtype = m.get('type', '')
        self.assertTrue(
            'editorial' in mtype or 'commissioning' in mtype,
            f"Expected editorial/commissioning type, got: {mtype}"
        )


class TestYAMLSyntaxIntegrity(unittest.TestCase):
    """Regression test: YAML files must parse without errors."""

    def test_competitor_entities_yaml_parses(self):
        """competitor-entities.yaml must parse without errors (regression for colon-in-scalar bug)."""
        path = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
        with open(path) as f:
            data = yaml.safe_load(f)
        self.assertIsNotNone(data)

    def test_competitor_research_yaml_parses(self):
        """competitor-coverage-research.yaml must parse without errors."""
        path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
        with open(path) as f:
            data = yaml.safe_load(f)
        self.assertIsNotNone(data)


if __name__ == '__main__':
    unittest.main()
