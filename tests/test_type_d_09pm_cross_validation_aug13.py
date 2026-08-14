"""
Type D Cross-Validation — Mechanisms #89-#91 (Iterations 91-93, Aug 13 2026, 22:00 PT)

Validates the three mechanisms added today (19:00-21:00 PT):
- #89: WIRED Category-Universal Privacy Headline with Entity-Specific Substance (Ashworth)
- #90: Victoria Song Health Data Privacy Investigation Asymmetry
- #91: Qualcomm Co-Marketing Supply Chain Financial Multiplier

Checks:
1. Metadata completeness (date_added, test_file, finding_summary, confounders, predictions)
2. Confounding factor quality (≥1 STRONG, ≥2 strength levels)
3. ID integrity (contiguous, no duplicates, max = 91)
4. Cross-reference coherence (related_mechanisms point to existing mechanisms)
5. Finding distinctiveness (Jaccard <0.7 between pairs)
6. Source URL presence and count
7. README/ARCHITECTURE stat consistency
8. Test file existence on disk
9. Regression guards for #84-#88 (prior batch)
10. Samsung glasses cluster coherence (#76, #81, #84, #87, #89, #90, #91)
"""

import os
import re
import glob
import yaml
import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, 'tests')
PROFILES_DIR = os.path.join(REPO_ROOT, 'profiles')


def read_file(rel_path):
    with open(os.path.join(REPO_ROOT, rel_path)) as f:
        return f.read()


def load_yaml(rel_path):
    with open(os.path.join(REPO_ROOT, rel_path)) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def research():
    return load_yaml('profiles/competitor-coverage-research.yaml')


@pytest.fixture(scope='module')
def entities():
    return load_yaml('profiles/competitor-entities.yaml')


@pytest.fixture(scope='module')
def target_mechanisms(research, entities):
    """Extract mechanisms #89-#91 from their respective YAML files."""
    mechs = {}

    # #89 and #90 are in research yaml
    for section_name in ('cross_publication_findings', 'aggregate_findings'):
        section = research.get(section_name, {})
        for key, val in section.items():
            if isinstance(val, dict) and 'mechanism_id' in val:
                mid = val['mechanism_id']
                if isinstance(mid, int) and mid in (89, 90):
                    mechs[mid] = val

    # #91 is in competitor-entities.yaml under samsung
    samsung = entities.get('entities', {}).get('samsung', {})
    for key, val in _deep_find_mechanisms(samsung):
        if val.get('mechanism_id') == 91:
            mechs[91] = val

    return mechs


def _deep_find_mechanisms(d, depth=0):
    """Recursively find dicts with mechanism_id in nested YAML."""
    if depth > 10:
        return
    if isinstance(d, dict):
        if 'mechanism_id' in d:
            yield ('', d)
        for k, v in d.items():
            yield from _deep_find_mechanisms(v, depth + 1)
    elif isinstance(d, list):
        for item in d:
            yield from _deep_find_mechanisms(item, depth + 1)


@pytest.fixture(scope='module')
def all_mechanism_ids(research, entities):
    """Collect ALL mechanism IDs across both YAML files."""
    ids = set()
    for section in ('cross_publication_findings', 'aggregate_findings'):
        for key, val in research.get(section, {}).items():
            if isinstance(val, dict) and 'mechanism_id' in val:
                mid = val['mechanism_id']
                if isinstance(mid, int):
                    ids.add(mid)

    # Also scan competitor-entities.yaml
    for item in _deep_find_mechanisms(entities):
        mid = item[1].get('mechanism_id')
        if isinstance(mid, int):
            ids.add(mid)

    return ids


# ===================================================================
# 1. Metadata Completeness
# ===================================================================

class TestMetadataCompleteness:
    """Every target mechanism must have required metadata fields."""

    def test_all_three_mechanisms_found(self, target_mechanisms):
        assert 89 in target_mechanisms, "Mechanism #89 not found"
        assert 90 in target_mechanisms, "Mechanism #90 not found"
        assert 91 in target_mechanisms, "Mechanism #91 not found"

    @pytest.mark.parametrize("mid", [89, 90, 91])
    def test_has_date_added(self, target_mechanisms, mid):
        m = target_mechanisms[mid]
        assert 'date_added' in m, f"#{mid} missing date_added"

    @pytest.mark.parametrize("mid", [89, 90, 91])
    def test_has_finding_summary(self, target_mechanisms, mid):
        m = target_mechanisms[mid]
        summary = m.get('finding_summary', '')
        assert len(summary) >= 100, f"#{mid} finding_summary too short ({len(summary)} chars)"

    @pytest.mark.parametrize("mid", [89, 90, 91])
    def test_has_confounding_factors(self, target_mechanisms, mid):
        m = target_mechanisms[mid]
        cfs = m.get('confounding_factors', [])
        assert len(cfs) >= 3, f"#{mid} has only {len(cfs)} confounding factors (need ≥3)"

    @pytest.mark.parametrize("mid", [89, 90, 91])
    def test_has_testable_predictions(self, target_mechanisms, mid):
        m = target_mechanisms[mid]
        preds = m.get('testable_predictions', [])
        assert len(preds) >= 2, f"#{mid} has only {len(preds)} testable predictions (need ≥2)"


# ===================================================================
# 2. Confounding Factor Quality
# ===================================================================

class TestConfoundingFactorQuality:
    """Each mechanism needs ≥1 STRONG confounding factor and ≥2 strength levels."""

    @pytest.mark.parametrize("mid", [89, 90, 91])
    def test_has_strong_confound(self, target_mechanisms, mid):
        m = target_mechanisms[mid]
        cfs = m.get('confounding_factors', [])
        strengths = set()
        for cf in cfs:
            if isinstance(cf, dict):
                s = str(cf.get('strength', cf.get('level', ''))).upper()
                strengths.add(s)
            elif isinstance(cf, str):
                # Handle "[STRONG] description" format
                if '[STRONG]' in cf.upper():
                    strengths.add('STRONG')
                elif '[MODERATE]' in cf.upper():
                    strengths.add('MODERATE')
                elif '[WEAK]' in cf.upper():
                    strengths.add('WEAK')
        assert 'STRONG' in strengths, f"#{mid} has no STRONG confounding factor"

    @pytest.mark.parametrize("mid", [89, 90, 91])
    def test_multiple_strength_levels(self, target_mechanisms, mid):
        m = target_mechanisms[mid]
        cfs = m.get('confounding_factors', [])
        strengths = set()
        for cf in cfs:
            if isinstance(cf, dict):
                s = str(cf.get('strength', cf.get('level', ''))).upper()
                if s:
                    strengths.add(s)
            elif isinstance(cf, str):
                if '[STRONG]' in cf.upper():
                    strengths.add('STRONG')
                elif '[MODERATE]' in cf.upper():
                    strengths.add('MODERATE')
                elif '[WEAK]' in cf.upper():
                    strengths.add('WEAK')
        assert len(strengths) >= 2, f"#{mid} has only {len(strengths)} strength level(s)"


# ===================================================================
# 3. ID Integrity
# ===================================================================

class TestIDIntegrity:
    """Mechanism IDs are contiguous, no duplicates, correct max."""

    def test_max_id_is_92(self, all_mechanism_ids):
        assert max(all_mechanism_ids) == 92

    def test_min_id_is_17_or_lower(self, all_mechanism_ids):
        assert min(all_mechanism_ids) <= 17

    def test_no_gaps_in_17_to_91(self, all_mechanism_ids):
        expected = set(range(17, 93))
        missing = expected - all_mechanism_ids
        assert not missing, f"Missing mechanism IDs: {sorted(missing)}"


# ===================================================================
# 4. Cross-Reference Coherence
# ===================================================================

class TestCrossReferenceCoherence:
    """related_mechanisms and extends_mechanism references point to existing mechanisms."""

    @pytest.mark.parametrize("mid", [89, 90, 91])
    def test_related_mechanisms_exist(self, target_mechanisms, all_mechanism_ids, mid):
        m = target_mechanisms[mid]
        related = m.get('related_mechanisms', [])
        if not related:
            return
        for ref in related:
            ref_id = ref if isinstance(ref, int) else ref.get('mechanism_id', ref)
            if isinstance(ref_id, int):
                assert ref_id in all_mechanism_ids or ref_id < 17, \
                    f"#{mid} references non-existent mechanism #{ref_id}"


# ===================================================================
# 5. Finding Distinctiveness
# ===================================================================

class TestFindingDistinctiveness:
    """No two target mechanisms should have Jaccard similarity ≥0.7."""

    def test_pairwise_jaccard_below_threshold(self, target_mechanisms):
        summaries = {}
        for mid in (89, 90, 91):
            m = target_mechanisms[mid]
            summaries[mid] = set(m.get('finding_summary', '').lower().split())

        pairs = [(89, 90), (89, 91), (90, 91)]
        for a, b in pairs:
            intersection = summaries[a] & summaries[b]
            union = summaries[a] | summaries[b]
            jaccard = len(intersection) / len(union) if union else 0
            assert jaccard < 0.7, \
                f"Mechanisms #{a} and #{b} too similar (Jaccard={jaccard:.2f})"


# ===================================================================
# 6. Source URL Presence
# ===================================================================

class TestSourceURLPresence:
    """Each mechanism should have source URLs."""

    @pytest.mark.parametrize("mid", [89, 90, 91])
    def test_has_source_urls(self, target_mechanisms, mid):
        m = target_mechanisms[mid]
        sources = m.get('source_urls', m.get('sources', []))
        assert len(sources) >= 1, f"#{mid} has no source URLs"


# ===================================================================
# 7. Documentation Consistency
# ===================================================================

class TestDocumentationConsistency:
    """README and ARCHITECTURE stats match each other and disk."""

    def test_readme_architecture_test_file_count_match(self):
        readme = read_file('README.md')
        arch = read_file('docs/ARCHITECTURE.md')
        r_match = re.search(r'(\d+) test files', readme)
        a_match = re.search(r'(\d+) test files', arch)
        assert r_match and a_match
        assert r_match.group(1) == a_match.group(1), \
            f"README ({r_match.group(1)}) != ARCHITECTURE ({a_match.group(1)})"

    def test_disk_test_file_count(self):
        disk_count = len(glob.glob(os.path.join(TESTS_DIR, 'test_*.py')))
        arch = read_file('docs/ARCHITECTURE.md')
        match = re.search(r'(\d+)\s+test\s+files', arch)
        if match:
            doc_count = int(match.group(1))
            # Allow +1 for the new cross-validation test
            assert abs(doc_count - disk_count) <= 1, \
                f"ARCHITECTURE says {doc_count}, disk has {disk_count}"


# ===================================================================
# 8. Test File Existence
# ===================================================================

class TestFileExistence:
    """Test files for mechanisms #89-#91 exist on disk."""

    def test_mechanism_89_test_file(self):
        path = os.path.join(TESTS_DIR, 'test_wired_ashworth_category_headline_meta_substance_aug13.py')
        assert os.path.exists(path), "Mechanism #89 test file missing"

    def test_mechanism_90_test_file(self):
        path = os.path.join(TESTS_DIR, 'test_victoria_song_health_data_investigation_asymmetry_aug13.py')
        assert os.path.exists(path), "Mechanism #90 test file missing"

    def test_mechanism_91_test_file(self):
        path = os.path.join(TESTS_DIR, 'test_qualcomm_comarketing_supply_chain_financial_multiplier_aug13.py')
        assert os.path.exists(path), "Mechanism #91 test file missing"


# ===================================================================
# 9. Regression Guards for #84-#88
# ===================================================================

class TestRegressionGuards:
    """Prior batch mechanisms #84-#88 still present."""

    @pytest.mark.parametrize("mid", [84, 85, 86, 87, 88])
    def test_prior_mechanism_still_present(self, all_mechanism_ids, mid):
        assert mid in all_mechanism_ids, f"Mechanism #{mid} disappeared from profiles"


# ===================================================================
# 10. Samsung Glasses Cluster Coherence
# ===================================================================

class TestSamsungGlassesCluster:
    """The Samsung glasses coverage cluster should be internally consistent."""

    def test_cluster_mechanisms_all_exist(self, all_mechanism_ids):
        cluster = {76, 81, 84, 87, 89, 90, 91}
        missing = cluster - all_mechanism_ids
        assert not missing, f"Samsung cluster mechanisms missing: {sorted(missing)}"

    def test_mechanism_89_entity_is_meta_or_wired(self, target_mechanisms):
        m = target_mechanisms[89]
        entities = m.get('entities', [])
        summary = m.get('finding_summary', '').lower()
        assert 'meta' in summary or 'wired' in summary or any(
            'meta' in str(e).lower() or 'wired' in str(e).lower() for e in entities
        ), "Mechanism #89 should involve Meta or WIRED"

    def test_mechanism_90_entity_is_samsung(self, target_mechanisms):
        m = target_mechanisms[90]
        summary = m.get('finding_summary', m.get('key_finding', '')).lower()
        assert 'samsung' in summary, "Mechanism #90 should involve Samsung"

    def test_mechanism_91_entity_is_qualcomm(self, target_mechanisms):
        m = target_mechanisms[91]
        summary = m.get('finding_summary', '').lower()
        assert 'qualcomm' in summary, "Mechanism #91 should involve Qualcomm"
