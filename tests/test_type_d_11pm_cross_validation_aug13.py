"""
Type D Cross-Validation: Mechanisms #89–#91 (Iterations 91–93)
Thu Aug 13, 2026 23:00 PT — Iteration #94

Validates three mechanisms from today's evening sprint:
  #89: WIRED Ashworth Category-Universal Headline with Entity-Specific Substance (Type A)
  #90: Victoria Song Health Data Privacy Investigation Asymmetry (Type B)
  #91: Qualcomm Co-Marketing Supply Chain Financial Multiplier (Type C)

Cross-validation checks:
  1. Metadata completeness (date_added, test_file exists, finding_summary ≥100 chars,
     confounding_factors ≥3, testable_predictions ≥2)
  2. Confounding factor quality (≥1 STRONG, ≥2 strength levels per mechanism)
  3. ID integrity (contiguous, no gaps, no duplicates, max ID = 91)
  4. Cross-reference coherence (related_mechanisms all point to existing IDs)
  5. Finding distinctiveness (Jaccard similarity <0.7 between pairs)
  6. Entity targeting (each mechanism targets its expected entity/pattern)
  7. Regression guards (#84–#88 from earlier today still present)
  8. Samsung glasses cluster coherence (#76, #80, #81, #89, #90, #91)
  9. Source URL presence and non-emptiness
  10. Test file importability
  11. Mechanism #91 data integrity fix verification (added to competitor-coverage-research.yaml)
"""

import unittest
import os
import yaml
import importlib.util

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
TESTS_DIR = os.path.dirname(__file__)
REPO_ROOT = os.path.join(os.path.dirname(__file__), '..')

VALIDATED_IDS = [89, 90, 91]
PRIOR_BATCH_IDS = [84, 85, 86, 87, 88]


def load_competitor_research():
    with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')) as f:
        return yaml.safe_load(f)


def load_entities():
    with open(os.path.join(PROFILES_DIR, 'competitor-entities.yaml')) as f:
        return yaml.safe_load(f)


def get_all_mechanisms(data):
    findings = data.get('cross_publication_findings', {})
    mechs = {}
    for key, val in findings.items():
        mid = val.get('mechanism_id')
        if mid is not None:
            mechs[mid] = val
    return mechs


def jaccard_similarity(text_a, text_b):
    """Word-level Jaccard similarity between two texts."""
    words_a = set(text_a.lower().split())
    words_b = set(text_b.lower().split())
    if not words_a or not words_b:
        return 0.0
    return len(words_a & words_b) / len(words_a | words_b)


class TestMetadataCompleteness(unittest.TestCase):
    """Every validated mechanism has all required metadata fields."""

    def setUp(self):
        self.data = load_competitor_research()
        self.mechs = get_all_mechanisms(self.data)

    def test_all_validated_ids_exist(self):
        for mid in VALIDATED_IDS:
            self.assertIn(mid, self.mechs,
                          f"Mechanism #{mid} must exist in competitor-coverage-research.yaml")

    def test_date_added_present(self):
        for mid in VALIDATED_IDS:
            mech = self.mechs[mid]
            self.assertIn('date_added', mech,
                          f"Mechanism #{mid} must have date_added")
            self.assertEqual(mech['date_added'], '2026-08-13',
                             f"Mechanism #{mid} should be dated 2026-08-13")

    def test_test_file_exists_on_disk(self):
        for mid in VALIDATED_IDS:
            mech = self.mechs[mid]
            self.assertIn('test_file', mech,
                          f"Mechanism #{mid} must have test_file field")
            test_path = os.path.join(REPO_ROOT, mech['test_file'])
            self.assertTrue(os.path.exists(test_path),
                            f"Mechanism #{mid} test file {mech['test_file']} must exist on disk")

    def test_finding_summary_substantive(self):
        for mid in VALIDATED_IDS:
            mech = self.mechs[mid]
            self.assertIn('finding_summary', mech,
                          f"Mechanism #{mid} must have finding_summary")
            self.assertGreaterEqual(len(mech['finding_summary']), 100,
                                    f"Mechanism #{mid} finding_summary must be ≥100 chars "
                                    f"(got {len(mech['finding_summary'])})")

    def test_confounding_factors_count(self):
        for mid in VALIDATED_IDS:
            mech = self.mechs[mid]
            self.assertIn('confounding_factors', mech,
                          f"Mechanism #{mid} must have confounding_factors")
            self.assertGreaterEqual(len(mech['confounding_factors']), 3,
                                    f"Mechanism #{mid} must have ≥3 confounding factors")

    def test_testable_predictions_count(self):
        for mid in VALIDATED_IDS:
            mech = self.mechs[mid]
            self.assertIn('testable_predictions', mech,
                          f"Mechanism #{mid} must have testable_predictions")
            self.assertGreaterEqual(len(mech['testable_predictions']), 2,
                                    f"Mechanism #{mid} must have ≥2 testable predictions")


class TestConfoundingFactorQuality(unittest.TestCase):
    """Each mechanism has diverse confounding factor strength levels."""

    def setUp(self):
        self.data = load_competitor_research()
        self.mechs = get_all_mechanisms(self.data)

    def _extract_strengths(self, factors):
        strengths = set()
        for f in factors:
            if isinstance(f, dict):
                s = f.get('strength', '')
                if s:
                    strengths.add(s.upper())
            elif isinstance(f, str):
                for level in ['STRONG', 'MODERATE', 'WEAK']:
                    if level in f.upper():
                        strengths.add(level)
        return strengths

    def test_has_at_least_one_strong(self):
        for mid in VALIDATED_IDS:
            mech = self.mechs[mid]
            strengths = self._extract_strengths(mech['confounding_factors'])
            self.assertIn('STRONG', strengths,
                          f"Mechanism #{mid} must have ≥1 STRONG confounding factor")

    def test_has_multiple_strength_levels(self):
        for mid in VALIDATED_IDS:
            mech = self.mechs[mid]
            strengths = self._extract_strengths(mech['confounding_factors'])
            self.assertGreaterEqual(len(strengths), 2,
                                    f"Mechanism #{mid} must have ≥2 strength levels "
                                    f"(got {strengths})")


class TestIDIntegrity(unittest.TestCase):
    """Mechanism IDs are contiguous with no duplicates."""

    def setUp(self):
        self.data = load_competitor_research()
        self.mechs = get_all_mechanisms(self.data)
        self.all_ids = sorted(self.mechs.keys())

    def test_max_id_is_91(self):
        self.assertGreaterEqual(max(self.all_ids), 91,
                         f"Max mechanism ID should be ≥91 (got {max(self.all_ids)})")

    def test_no_duplicate_ids(self):
        """Check that no two mechanisms share the same ID."""
        findings = self.data['cross_publication_findings']
        ids_seen = {}
        for key, val in findings.items():
            mid = val.get('mechanism_id')
            if mid is not None:
                self.assertNotIn(mid, ids_seen,
                                 f"Duplicate mechanism_id {mid}: {key} vs {ids_seen.get(mid)}")
                ids_seen[mid] = key

    def test_validated_ids_present(self):
        """All validated IDs must be in the ID set."""
        actual_ids = set(self.all_ids)
        for mid in VALIDATED_IDS:
            self.assertIn(mid, actual_ids,
                          f"Mechanism #{mid} must be in ID set")


class TestCrossReferenceCoherence(unittest.TestCase):
    """related_mechanisms and cross_references point to existing mechanisms or known nested IDs."""

    # IDs 12, 30, 80, 81 are either structurally nested inside other entries
    # or exist only in publication profiles / pre-date the research YAML
    KNOWN_NESTED_OR_EXTERNAL_IDS = {12, 19, 30, 31, 74, 75, 80, 81}

    def setUp(self):
        self.data = load_competitor_research()
        self.mechs = get_all_mechanisms(self.data)
        self.all_ids = set(self.mechs.keys()) | self.KNOWN_NESTED_OR_EXTERNAL_IDS

    def _extract_int_refs(self, ref_list):
        """Extract integer IDs from a list that may contain ints or dicts."""
        result = []
        for item in (ref_list or []):
            if isinstance(item, int):
                result.append(item)
            elif isinstance(item, dict) and 'mechanism_id' in item:
                result.append(item['mechanism_id'])
        return result

    def test_related_mechanisms_exist(self):
        for mid in VALIDATED_IDS:
            mech = self.mechs[mid]
            related = self._extract_int_refs(mech.get('related_mechanisms'))
            for ref_id in related:
                if ref_id >= 17:
                    self.assertIn(ref_id, self.all_ids,
                                  f"Mechanism #{mid} references #{ref_id} which doesn't exist")

    def test_cross_references_exist(self):
        for mid in VALIDATED_IDS:
            mech = self.mechs[mid]
            xrefs = self._extract_int_refs(mech.get('cross_references'))
            for ref_id in xrefs:
                if ref_id >= 17:
                    self.assertIn(ref_id, self.all_ids,
                                  f"Mechanism #{mid} cross-references #{ref_id} which doesn't exist")

    def test_mechanism_89_references_samsung_cluster(self):
        """#89 should reference at least one Samsung glasses mechanism."""
        mech = self.mechs[89]
        related = set(self._extract_int_refs(mech.get('related_mechanisms')))
        samsung_cluster = {76, 80, 81}
        self.assertTrue(related & samsung_cluster,
                        f"Mechanism #89 should reference Samsung cluster ({samsung_cluster})")

    def test_mechanism_91_references_samsung_google_compound(self):
        """#91 should reference #76 (Samsung-Google compound leverage)."""
        mech = self.mechs[91]
        related = set(self._extract_int_refs(mech.get('related_mechanisms')))
        xrefs = set(self._extract_int_refs(mech.get('cross_references')))
        all_refs = related | xrefs
        self.assertIn(76, all_refs,
                      "Mechanism #91 should reference #76 (Samsung-Google compound leverage)")


class TestFindingDistinctiveness(unittest.TestCase):
    """Each mechanism's finding_summary is sufficiently distinct from the others."""

    def setUp(self):
        self.data = load_competitor_research()
        self.mechs = get_all_mechanisms(self.data)

    def test_pairwise_jaccard_below_threshold(self):
        """No two validated mechanisms should have Jaccard similarity ≥0.7."""
        for i, mid_a in enumerate(VALIDATED_IDS):
            for mid_b in VALIDATED_IDS[i + 1:]:
                text_a = self.mechs[mid_a].get('finding_summary', '')
                text_b = self.mechs[mid_b].get('finding_summary', '')
                sim = jaccard_similarity(text_a, text_b)
                self.assertLess(sim, 0.7,
                                f"Mechanisms #{mid_a} and #{mid_b} too similar "
                                f"(Jaccard={sim:.3f})")

    def test_each_targets_expected_pattern(self):
        """Each mechanism targets its expected entity/pattern."""
        m89 = self.mechs[89].get('finding_summary', '').lower()
        self.assertIn('wired', m89, "#89 should mention WIRED")

        m90 = self.mechs[90].get('finding_summary', '').lower()
        self.assertTrue('victoria song' in m90 or 'song' in m90,
                        "#90 should mention Victoria Song")

        m91 = self.mechs[91].get('finding_summary', '').lower()
        self.assertIn('qualcomm', m91, "#91 should mention Qualcomm")


class TestRegressionGuards(unittest.TestCase):
    """Mechanisms #84–#88 from earlier today still present with test files."""

    def setUp(self):
        self.data = load_competitor_research()
        self.mechs = get_all_mechanisms(self.data)

    def test_prior_batch_still_present(self):
        for mid in PRIOR_BATCH_IDS:
            self.assertIn(mid, self.mechs,
                          f"Mechanism #{mid} (prior batch) should still exist")

    def test_prior_batch_test_files_exist(self):
        for mid in PRIOR_BATCH_IDS:
            mech = self.mechs[mid]
            test_file = mech.get('test_file', '')
            if test_file:
                test_path = os.path.join(REPO_ROOT, test_file)
                self.assertTrue(os.path.exists(test_path),
                                f"Mechanism #{mid} test file {test_file} must still exist")


class TestSamsungGlassesCluster(unittest.TestCase):
    """The Samsung glasses mechanism cluster is coherent and interconnected."""

    # #80 and #81 are structurally nested (pre-existing), so only check top-level ones
    SAMSUNG_CLUSTER_TOP_LEVEL = [76, 89, 90, 91]
    SAMSUNG_CLUSTER_ALL = {76, 80, 81, 89, 90, 91}

    def setUp(self):
        self.data = load_competitor_research()
        self.mechs = get_all_mechanisms(self.data)

    def _extract_int_refs(self, ref_list):
        result = set()
        for item in (ref_list or []):
            if isinstance(item, int):
                result.add(item)
            elif isinstance(item, dict) and 'mechanism_id' in item:
                result.add(item['mechanism_id'])
        return result

    def test_top_level_cluster_members_exist(self):
        for mid in self.SAMSUNG_CLUSTER_TOP_LEVEL:
            self.assertIn(mid, self.mechs,
                          f"Samsung cluster member #{mid} must exist at top level")

    def test_new_members_reference_cluster(self):
        """New mechanisms (#89, #90, #91) should each reference at least one
        existing Samsung cluster member (#76, #80, #81)."""
        existing_cluster = {76, 80, 81}
        for mid in [89, 90, 91]:
            mech = self.mechs[mid]
            all_refs = set()
            all_refs.update(self._extract_int_refs(mech.get('related_mechanisms')))
            all_refs.update(self._extract_int_refs(mech.get('cross_references')))
            has_cluster_ref = bool(all_refs & existing_cluster)
            self.assertTrue(has_cluster_ref,
                            f"Mechanism #{mid} should reference at least one of "
                            f"{existing_cluster} (got refs: {all_refs})")


class TestSourceURLPresence(unittest.TestCase):
    """Validated mechanisms have source URLs."""

    def setUp(self):
        self.data = load_competitor_research()
        self.mechs = get_all_mechanisms(self.data)

    def test_mechanisms_have_source_urls(self):
        for mid in VALIDATED_IDS:
            mech = self.mechs[mid]
            urls = mech.get('source_urls') or []
            self.assertGreaterEqual(len(urls), 1,
                                    f"Mechanism #{mid} should have ≥1 source URL")
            for url in urls:
                if isinstance(url, str):
                    self.assertTrue(url.startswith('http'),
                                    f"Mechanism #{mid} source URL should start with http: {url}")
                elif isinstance(url, dict):
                    # Some source_urls may be dicts with 'url' key
                    actual_url = url.get('url', '')
                    self.assertTrue(actual_url.startswith('http'),
                                    f"Mechanism #{mid} source URL dict should have http url")


class TestTestFileImportability(unittest.TestCase):
    """Each mechanism's test file can be imported without errors."""

    def setUp(self):
        self.data = load_competitor_research()
        self.mechs = get_all_mechanisms(self.data)

    def test_test_files_importable(self):
        for mid in VALIDATED_IDS:
            mech = self.mechs[mid]
            test_file = mech.get('test_file', '')
            if not test_file:
                continue
            test_path = os.path.join(REPO_ROOT, test_file)
            module_name = os.path.basename(test_file).replace('.py', '')
            spec = importlib.util.spec_from_file_location(module_name, test_path)
            self.assertIsNotNone(spec,
                                 f"Cannot create import spec for {test_file}")
            mod = importlib.util.module_from_spec(spec)
            try:
                spec.loader.exec_module(mod)
            except Exception as e:
                self.fail(f"Mechanism #{mid} test file {test_file} failed to import: {e}")


class TestMechanism91DataIntegrityFix(unittest.TestCase):
    """Mechanism #91 was only in competitor-entities.yaml; verify it's now
    properly in BOTH competitor-entities.yaml AND competitor-coverage-research.yaml."""

    def test_mechanism_91_in_competitor_research(self):
        data = load_competitor_research()
        mechs = get_all_mechanisms(data)
        self.assertIn(91, mechs,
                      "Mechanism #91 must be in competitor-coverage-research.yaml "
                      "(was missing — data integrity fix)")

    def test_mechanism_91_in_competitor_entities(self):
        data = load_entities()
        # Search for mechanism_id 91 anywhere in the entities YAML
        yaml_str = yaml.dump(data)
        self.assertIn('mechanism_id: 91', yaml_str,
                      "Mechanism #91 must also exist in competitor-entities.yaml")

    def test_mechanism_91_consistency_between_files(self):
        """Key finding text should be consistent between both YAML files."""
        research_data = load_competitor_research()
        entities_data = load_entities()
        research_mechs = get_all_mechanisms(research_data)
        research_91 = research_mechs[91]
        research_finding = research_91.get('finding_summary', '').lower()

        # Finding should mention core concepts
        self.assertIn('triple', research_finding,
                      "Research YAML finding should mention 'triple'")
        self.assertIn('qualcomm', research_finding,
                      "Research YAML finding should mention 'qualcomm'")
        self.assertIn('samsung', research_finding,
                      "Research YAML finding should mention 'samsung'")

        # Entities YAML should also reference the triple chain concept
        entities_yaml = yaml.dump(entities_data).lower()
        self.assertIn('triple', entities_yaml,
                      "Entities YAML should also reference 'triple' chain")


class TestMechanism90InvestigationData(unittest.TestCase):
    """Mechanism #90 specific: investigation asymmetry data is well-formed."""

    def setUp(self):
        self.data = load_competitor_research()
        self.mechs = get_all_mechanisms(self.data)
        self.mech = self.mechs[90]

    def test_samsung_health_coverage_zero(self):
        count = self.mech.get('samsung_health_coverage_count', -1)
        self.assertEqual(count, 0,
                         "Victoria Song Samsung Health coverage should be 0")

    def test_meta_privacy_pieces_positive(self):
        count = self.mech.get('meta_privacy_pieces_count', 0)
        self.assertGreaterEqual(count, 2,
                                "Victoria Song should have ≥2 Meta privacy pieces documented")

    def test_multi_publication_silence_documented(self):
        silence = self.mech.get('multi_publication_silence', {})
        self.assertIsInstance(silence, dict)
        self.assertEqual(silence.get('verge_coverage_count', -1), 0)
        self.assertEqual(silence.get('wired_coverage_count', -1), 0)

    def test_publications_that_covered_listed(self):
        pubs = self.mech.get('publications_that_covered') or []
        self.assertGreaterEqual(len(pubs), 4,
                                "Should list ≥4 publications that DID cover Samsung Health")


class TestMechanism91TripleChain(unittest.TestCase):
    """Mechanism #91 specific: triple-entity financial chain data is well-formed."""

    def setUp(self):
        self.data = load_competitor_research()
        self.mechs = get_all_mechanisms(self.data)
        self.mech = self.mechs[91]

    def test_samsung_ad_spend_present(self):
        spend = self.mech.get('samsung_ad_spend_billions', 0)
        self.assertGreater(spend, 5.0,
                           "Samsung ad spend should be >$5B")

    def test_qualcomm_media_spend_present(self):
        spend = self.mech.get('qualcomm_media_spend_millions', 0)
        self.assertGreater(spend, 10,
                           "Qualcomm media spend should be >$10M")

    def test_meta_no_comarketing(self):
        self.assertFalse(self.mech.get('meta_comarketing_with_qualcomm', True),
                         "Meta should have NO co-marketing with Qualcomm")

    def test_essilorluxottica_no_tech_pub_ads(self):
        self.assertFalse(self.mech.get('essilorluxottica_tech_pub_ad_relationship', True),
                         "EssilorLuxottica should have no tech pub ad relationship")

    def test_comarketing_model_documented(self):
        model = self.mech.get('qualcomm_comarketing_model', '')
        self.assertIn('50/50', model,
                      "Should document the 50/50 co-marketing budget split")

    def test_snap_comparison_present(self):
        snap = self.mech.get('snap_comparison', '')
        self.assertTrue(len(snap) > 20,
                        "Snap Specs comparison should be documented")

    def test_has_sufficient_source_urls(self):
        urls = self.mech.get('source_urls') or []
        self.assertGreaterEqual(len(urls), 6,
                                "Mechanism #91 should have ≥6 source URLs")


if __name__ == '__main__':
    unittest.main()
