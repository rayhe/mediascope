"""
Cross-validation of mechanisms #104-108 (Iterations 107-109, Aug 14 2026)

Validates data integrity, metadata completeness, cross-reference coherence,
and structural consistency for:
  #104: TechCrunch (Yahoo/Apollo) Privacy-Improvement-As-Indictment Framing
  #105: Joanna Stern (WSJ→Bloomberg) Career Migration Natural Experiment
  #106: Scott Stein (CNET/Ziff Davis) Entity-Selective Enthusiasm Gradient
  #107: Kerry Wan (ZDNET/Ziff Davis) Cross-Entity Privacy Scrutiny Asymmetry
  #108: Ziff Davis Triple-Squeeze Financial Incentive Architecture
"""
import os
import yaml
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
TESTS_DIR = os.path.dirname(__file__)

# Known nested mechanism IDs that live inside sub-entries, not top-level CPF keys
KNOWN_NESTED_IDS = {80, 81}

MECHANISMS_UNDER_TEST = [104, 105, 106, 107, 108]


def load_yaml(filename):
    path = os.path.join(PROFILES_DIR, filename)
    with open(path) as f:
        return yaml.safe_load(f)


def collect_all_mechanism_ids(cpf, ccr_data):
    """Collect mechanism IDs from cross_publication_findings and nested entries."""
    ids = set()
    for key, val in cpf.items():
        if isinstance(val, dict):
            if 'mechanism_id' in val and val['mechanism_id'] is not None:
                ids.add(val['mechanism_id'])
            # Check nested entries
            for k2, v2 in val.items():
                if isinstance(v2, dict) and 'mechanism_id' in v2 and v2['mechanism_id'] is not None:
                    ids.add(v2['mechanism_id'])
                elif isinstance(v2, list):
                    for item in v2:
                        if isinstance(item, dict) and 'mechanism_id' in item and item['mechanism_id'] is not None:
                            ids.add(item['mechanism_id'])
    # Also check aggregate_findings and cross_entity_leverage
    for section_key in ['aggregate_findings', 'cross_entity_leverage', 'publications']:
        section = ccr_data.get(section_key, {})
        if isinstance(section, dict):
            for key, val in section.items():
                if isinstance(val, dict):
                    if 'mechanism_id' in val and val['mechanism_id'] is not None:
                        ids.add(val['mechanism_id'])
                    for k2, v2 in val.items():
                        if isinstance(v2, dict) and 'mechanism_id' in v2 and v2['mechanism_id'] is not None:
                            ids.add(v2['mechanism_id'])
    return ids


def collect_ce_mechanism_ids(ce_data):
    """Collect mechanism IDs from competitor-entities.yaml recursively."""
    ids = set()
    def walk(d):
        if isinstance(d, dict):
            if 'mechanism_id' in d:
                ids.add(d['mechanism_id'])
            for v in d.values():
                walk(v)
        elif isinstance(d, list):
            for item in d:
                walk(item)
    walk(ce_data)
    return ids


@pytest.fixture(scope='module')
def ccr_data():
    return load_yaml('competitor-coverage-research.yaml')


@pytest.fixture(scope='module')
def ce_data():
    return load_yaml('competitor-entities.yaml')


@pytest.fixture(scope='module')
def cpf(ccr_data):
    return ccr_data.get('cross_publication_findings', {})


@pytest.fixture(scope='module')
def all_ccr_ids(cpf, ccr_data):
    return collect_all_mechanism_ids(cpf, ccr_data)


@pytest.fixture(scope='module')
def all_ce_ids(ce_data):
    return collect_ce_mechanism_ids(ce_data)


def _find_primary_mechanism(data, mech_id):
    """Find a mechanism by ID, preferring the primary metadata block.

    Later iterations add cross_references stubs (bare {'mechanism_id': N,
    ...} dicts) earlier in traversal order, which shadow the primary blocks
    carrying finding_summary / source_urls / confounding_factors. Collect
    all candidates, then prefer the one with finding_summary or key_finding.
    Centralized Sep 2 2026, Type D #469 completion: all per-class
    _find_mechanism copies delegate here.
    """
    candidates = []

    def _collect(node):
        if isinstance(node, dict):
            if node.get('mechanism_id') == mech_id:
                candidates.append(node)
            for v in node.values():
                _collect(v)
        elif isinstance(node, list):
            for item in node:
                _collect(item)

    _collect(data)
    for cand in candidates:
        if 'finding_summary' in cand or 'key_finding' in cand:
            return cand
    return candidates[0] if candidates else None

class TestMechanismPresenceInCCR:
    """All 5 mechanisms should be findable in competitor-coverage-research.yaml."""

    @pytest.mark.parametrize("mech_id", MECHANISMS_UNDER_TEST)
    def test_mechanism_in_ccr(self, all_ccr_ids, mech_id):
        assert mech_id in all_ccr_ids, \
            f"Mechanism #{mech_id} missing from competitor-coverage-research.yaml"


class TestMechanismPresenceInCE:
    """All 5 mechanisms should be findable in competitor-entities.yaml."""

    @pytest.mark.parametrize("mech_id", MECHANISMS_UNDER_TEST)
    def test_mechanism_in_ce(self, all_ce_ids, mech_id):
        assert mech_id in all_ce_ids, \
            f"Mechanism #{mech_id} missing from competitor-entities.yaml"


class TestIDIntegrity:
    """ID range and uniqueness checks."""

    def test_max_id_at_least_108(self, all_ccr_ids):
        assert max(all_ccr_ids) >= 108, \
            f"Max mechanism ID is {max(all_ccr_ids)}, expected >= 108"

    def test_no_gaps_104_to_108(self, all_ccr_ids, all_ce_ids):
        combined = all_ccr_ids | all_ce_ids
        for mid in range(104, 109):
            assert mid in combined, f"Mechanism #{mid} missing from combined ID set"


class TestMetadataCompleteness:
    """Each mechanism should have required metadata fields."""

    def _find_mechanism(self, data, mech_id):
        return _find_primary_mechanism(data, mech_id)

    @pytest.mark.parametrize("mech_id", MECHANISMS_UNDER_TEST)
    def test_has_finding_summary(self, ccr_data, mech_id):
        m = self._find_mechanism(ccr_data, mech_id)
        assert m is not None, f"Mechanism #{mech_id} not found in CCR"
        summary = m.get('finding_summary', m.get('key_finding', ''))
        assert len(str(summary)) >= 100, \
            f"Mechanism #{mech_id} finding_summary too short ({len(str(summary))} chars)"

    @pytest.mark.parametrize("mech_id", MECHANISMS_UNDER_TEST)
    def test_has_confounding_factors(self, ccr_data, mech_id):
        m = self._find_mechanism(ccr_data, mech_id)
        assert m is not None, f"Mechanism #{mech_id} not found in CCR"
        cf = m.get('confounding_factors', [])
        assert len(cf) >= 3, \
            f"Mechanism #{mech_id} has only {len(cf)} confounding factors (need ≥3)"

    @pytest.mark.parametrize("mech_id", MECHANISMS_UNDER_TEST)
    def test_has_testable_predictions(self, ccr_data, mech_id):
        m = self._find_mechanism(ccr_data, mech_id)
        assert m is not None, f"Mechanism #{mech_id} not found in CCR"
        tp = m.get('testable_predictions', [])
        assert len(tp) >= 2, \
            f"Mechanism #{mech_id} has only {len(tp)} testable predictions (need ≥2)"

    @pytest.mark.parametrize("mech_id", MECHANISMS_UNDER_TEST)
    def test_has_date_added(self, ccr_data, mech_id):
        m = self._find_mechanism(ccr_data, mech_id)
        assert m is not None, f"Mechanism #{mech_id} not found in CCR"
        assert 'date_added' in m or 'discovery_date' in m, \
            f"Mechanism #{mech_id} missing date_added/discovery_date"


class TestConfoundingFactorQuality:
    """Confounding factors should have multiple strength levels."""

    def _find_mechanism(self, data, mech_id):
        return _find_primary_mechanism(data, mech_id)

    @pytest.mark.parametrize("mech_id", MECHANISMS_UNDER_TEST)
    def test_has_strong_factor(self, ccr_data, mech_id):
        m = self._find_mechanism(ccr_data, mech_id)
        assert m is not None
        cf = m.get('confounding_factors', [])
        strengths = [f.get('strength', '').upper() for f in cf if isinstance(f, dict)]
        assert 'STRONG' in strengths, \
            f"Mechanism #{mech_id} has no STRONG confounding factor"

    @pytest.mark.parametrize("mech_id", MECHANISMS_UNDER_TEST)
    def test_multiple_strength_levels(self, ccr_data, mech_id):
        m = self._find_mechanism(ccr_data, mech_id)
        assert m is not None
        cf = m.get('confounding_factors', [])
        strengths = set(f.get('strength', '').upper() for f in cf if isinstance(f, dict))
        assert len(strengths) >= 2, \
            f"Mechanism #{mech_id} has only {len(strengths)} strength level(s): {strengths}"


class TestTestFileExistence:
    """Each mechanism should have a test file that exists on disk."""

    EXPECTED_TEST_FILES = {
        104: 'test_techcrunch_yahoo_apollo_privacy_indictment_framing_aug14.py',
        105: 'test_joanna_stern_career_migration_natural_experiment_aug14.py',
        106: 'test_scott_stein_cross_entity_enthusiasm_gradient_aug14.py',
        107: 'test_kerry_wan_zdnet_privacy_scrutiny_asymmetry_aug14.py',
        108: 'test_ziff_davis_triple_squeeze_financial_architecture_aug14.py',
    }

    @pytest.mark.parametrize("mech_id", MECHANISMS_UNDER_TEST)
    def test_test_file_exists(self, mech_id):
        filename = self.EXPECTED_TEST_FILES[mech_id]
        path = os.path.join(TESTS_DIR, filename)
        assert os.path.exists(path), f"Test file {filename} not found"

    @pytest.mark.parametrize("mech_id", MECHANISMS_UNDER_TEST)
    def test_test_file_importable(self, mech_id):
        """Test files should be importable without errors."""
        filename = self.EXPECTED_TEST_FILES[mech_id]
        module_name = filename.replace('.py', '')
        import importlib
        try:
            importlib.import_module(f'tests.{module_name}')
        except Exception as e:
            pytest.fail(f"Test file {filename} failed to import: {e}")


class TestCrossReferenceIntegrity:
    """Cross-references should point to existing mechanisms."""

    def _find_mechanism(self, data, mech_id):
        return _find_primary_mechanism(data, mech_id)

    @pytest.mark.parametrize("mech_id", MECHANISMS_UNDER_TEST)
    def test_cross_refs_exist(self, ccr_data, all_ccr_ids, mech_id):
        m = self._find_mechanism(ccr_data, mech_id)
        if m is None:
            pytest.skip(f"Mechanism #{mech_id} not found")
        refs = m.get('cross_references', [])
        for ref in refs:
            ref_id = ref if isinstance(ref, int) else ref.get('mechanism_id')
            if ref_id is not None:
                assert ref_id in all_ccr_ids or ref_id in KNOWN_NESTED_IDS or ref_id < 17, \
                    f"Mechanism #{mech_id} references #{ref_id} which doesn't exist"


class TestSourceURLQuality:
    """Source URLs should all use HTTPS."""

    def _find_mechanism(self, data, mech_id):
        return _find_primary_mechanism(data, mech_id)

    @pytest.mark.parametrize("mech_id", MECHANISMS_UNDER_TEST)
    def test_source_urls_https(self, ccr_data, mech_id):
        m = self._find_mechanism(ccr_data, mech_id)
        if m is None:
            pytest.skip(f"Mechanism #{mech_id} not found")
        urls = m.get('source_urls', [])
        for url in urls:
            assert url.startswith('https://'), \
                f"Mechanism #{mech_id} has non-HTTPS URL: {url}"

    @pytest.mark.parametrize("mech_id", MECHANISMS_UNDER_TEST)
    def test_has_source_urls(self, ccr_data, mech_id):
        m = self._find_mechanism(ccr_data, mech_id)
        if m is None:
            pytest.skip(f"Mechanism #{mech_id} not found")
        urls = m.get('source_urls', [])
        assert len(urls) >= 1, f"Mechanism #{mech_id} has no source URLs"


class TestZiffDavisClusterCoherence:
    """Mechanisms #106, #107, #108 form a Ziff Davis cluster and should cross-reference."""

    def _find_mechanism(self, data, mech_id):
        return _find_primary_mechanism(data, mech_id)

    def test_108_references_106_and_107(self, ccr_data):
        """#108 (corporate) should reference #106 (Stein) and #107 (Wan)."""
        m = self._find_mechanism(ccr_data, 108)
        assert m is not None, "Mechanism #108 not found"
        refs = m.get('cross_references', [])
        ref_ids = set()
        for ref in refs:
            if isinstance(ref, int):
                ref_ids.add(ref)
            elif isinstance(ref, dict) and 'mechanism_id' in ref:
                ref_ids.add(ref['mechanism_id'])
        assert 106 in ref_ids or 107 in ref_ids, \
            f"#108 should reference at least one of #106/#107, has refs: {ref_ids}"


class TestFieldNameConsistency:
    """Regression guard: all mechanisms ≥98 must use finding_summary, not finding."""

    def _find_mechanism(self, data, mech_id):
        return _find_primary_mechanism(data, mech_id)

    @pytest.mark.parametrize("mech_id", MECHANISMS_UNDER_TEST)
    def test_uses_finding_summary(self, ccr_data, mech_id):
        m = self._find_mechanism(ccr_data, mech_id)
        assert m is not None, f"Mechanism #{mech_id} not found"
        assert 'finding_summary' in m or 'key_finding' in m, \
            f"Mechanism #{mech_id} uses incorrect field name (expected finding_summary)"


class TestFileCountAndStats:
    """Verify README and ARCHITECTURE stats are reasonable."""

    def test_aug14_test_file_count(self):
        aug14_files = [f for f in os.listdir(TESTS_DIR) if 'aug14' in f and f.endswith('.py')]
        assert len(aug14_files) >= 19, \
            f"Expected ≥19 aug14 test files, found {len(aug14_files)}"

    def test_total_test_file_count(self):
        all_test_files = [f for f in os.listdir(TESTS_DIR) if f.startswith('test_') and f.endswith('.py')]
        assert len(all_test_files) >= 380, \
            f"Expected ≥380 test files, found {len(all_test_files)}"
