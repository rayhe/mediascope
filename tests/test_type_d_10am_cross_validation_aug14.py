"""
Type D: Test & Verify — Fri 2026-08-14 10:00 PT

Cross-validation of mechanism database integrity after iterations 99-101
added mechanisms #98-100 and brought total to 372 test files / 12,682 tests.

Fixes applied this iteration:
1. Samsung framing inversion test (#93) — search function hit cross-reference
   stubs instead of full mechanism entries. Added find_mechanism() helper that
   prefers the most complete match (by key count).
2. Stale max-ID assertions — 3 cross-validation tests hardcoded old max IDs
   (91, 93, 94) that were overtaken by new mechanisms. Fixed to >= or updated.
3. HTTP→HTTPS source URL fixes — 5 URLs in competitor-entities.yaml used http://
   instead of https:// (OpenAI, EFF, Fool, AndroidAuthority).
"""
import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
RESEARCH_FILE = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
ENTITIES_FILE = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')


def load_yaml(filepath):
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)


def collect_mechanisms(data, require_finding_summary=True):
    """Collect all mechanism dicts from nested YAML."""
    mechanisms = {}

    def _walk(obj):
        if isinstance(obj, dict):
            mid = obj.get('mechanism_id')
            if mid is not None:
                has_summary = 'finding_summary' in obj or 'key_finding' in obj
                if not require_finding_summary or has_summary:
                    if mid not in mechanisms or len(obj) > len(mechanisms[mid]):
                        mechanisms[mid] = obj
            for v in obj.values():
                _walk(v)
        elif isinstance(obj, list):
            for item in obj:
                _walk(item)

    _walk(data)
    return mechanisms


def collect_cross_references(data):
    """Collect all cross-referenced mechanism IDs."""
    refs = set()

    def _walk(obj, path=''):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k in ('cross_references', 'related_mechanisms'):
                    if isinstance(v, list):
                        for item in v:
                            if isinstance(item, int):
                                refs.add(item)
                            elif isinstance(item, dict) and 'mechanism_id' in item:
                                refs.add(item['mechanism_id'])
                else:
                    _walk(v, f'{path}.{k}')
        elif isinstance(obj, list):
            for item in obj:
                _walk(item, path)

    _walk(data)
    return refs


@pytest.fixture(scope='module')
def ccr_data():
    return load_yaml(RESEARCH_FILE)


@pytest.fixture(scope='module')
def ce_data():
    return load_yaml(ENTITIES_FILE)


@pytest.fixture(scope='module')
def all_mechanisms(ccr_data, ce_data):
    mechs = collect_mechanisms(ccr_data)
    ce_mechs = collect_mechanisms(ce_data)
    # Merge, preferring the version with more keys (more complete)
    for mid, mech in ce_mechs.items():
        if mid not in mechs or len(mech) > len(mechs[mid]):
            mechs[mid] = mech
    return mechs


@pytest.fixture(scope='module')
def all_cross_refs(ccr_data, ce_data):
    refs = collect_cross_references(ccr_data)
    refs.update(collect_cross_references(ce_data))
    return refs


# ── Mechanism Count and ID Range ──


class TestMechanismInventory:
    """Verify the mechanism database is consistent and growing."""

    def test_mechanism_count_at_least_80(self, all_mechanisms):
        assert len(all_mechanisms) >= 80, \
            f"Expected ≥80 mechanisms, found {len(all_mechanisms)}"

    def test_max_mechanism_id_is_103(self, all_mechanisms):
        assert max(all_mechanisms.keys()) >= 108, \
            f"Max mechanism ID is {max(all_mechanisms.keys())}, expected 103"

    def test_min_mechanism_id_is_17_or_lower(self, all_mechanisms):
        assert min(all_mechanisms.keys()) <= 17

    def test_no_duplicate_mechanism_ids(self, ccr_data):
        """Each mechanism_id appears exactly once as a full mechanism."""
        findings = ccr_data.get('cross_publication_findings', {})
        ids = []
        for key, val in findings.items():
            if isinstance(val, dict) and 'mechanism_id' in val:
                ids.append(val['mechanism_id'])
        dupes = [x for x in ids if ids.count(x) > 1]
        assert not dupes, f"Duplicate mechanism IDs in research file: {set(dupes)}"


# ── Cross-Reference Integrity ──


class TestCrossReferenceIntegrity:
    """All cross-references should point to existing mechanisms."""

    # Known pre-existing dangling references — mechanisms that existed
    # before the current finding_summary convention or were reorganized.
    # These are acceptable; new dangling refs are not.
    KNOWN_DANGLING = {6, 11, 12, 14, 15, 66, 67, 76}

    def test_no_new_dangling_references(self, all_mechanisms, all_cross_refs):
        """No NEW dangling references beyond the known set."""
        dangling = all_cross_refs - set(all_mechanisms.keys())
        new_dangling = dangling - self.KNOWN_DANGLING
        assert not new_dangling, \
            f"New dangling cross-references found: {new_dangling}"

    def test_known_dangling_count_stable(self, all_mechanisms, all_cross_refs):
        """The known dangling set shouldn't grow without investigation."""
        dangling = all_cross_refs - set(all_mechanisms.keys())
        assert dangling <= self.KNOWN_DANGLING, \
            f"Dangling refs grew beyond known set: new = {dangling - self.KNOWN_DANGLING}"


# ── Source URL Quality ──


class TestSourceURLQuality:
    """All source URLs must use HTTPS."""

    def test_no_http_urls_in_entities(self, ce_data):
        """All source URLs in competitor-entities.yaml use HTTPS."""
        http_urls = []

        def _walk(obj, path=''):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if k == 'source_urls' and isinstance(v, list):
                        for url in v:
                            if isinstance(url, str) and url.startswith('http://'):
                                http_urls.append((f'{path}.{k}', url))
                    else:
                        _walk(v, f'{path}.{k}')
            elif isinstance(obj, list):
                for i, item in enumerate(obj):
                    _walk(item, f'{path}[{i}]')

        _walk(ce_data)
        assert not http_urls, \
            f"Non-HTTPS source URLs found: {http_urls}"

    def test_no_http_urls_in_research(self, ccr_data):
        """All source URLs in research file use HTTPS."""
        http_urls = []

        def _walk(obj, path=''):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if 'source' in k.lower() and 'url' in k.lower() and isinstance(v, list):
                        for url in v:
                            if isinstance(url, str) and url.startswith('http://'):
                                http_urls.append((f'{path}.{k}', url))
                    elif isinstance(v, str) and 'url' in k.lower() and v.startswith('http://'):
                        http_urls.append((f'{path}.{k}', v))
                    else:
                        _walk(v, f'{path}.{k}')
            elif isinstance(obj, list):
                for i, item in enumerate(obj):
                    _walk(item, f'{path}[{i}]')

        _walk(ccr_data)
        assert not http_urls, \
            f"Non-HTTPS source URLs found in research: {http_urls}"


# ── Search Function Robustness ──


class TestSearchFunctionRobustness:
    """Verify the find_mechanism pattern correctly handles cross-reference stubs."""

    def test_cross_ref_stubs_dont_shadow_full_mechanisms(self, ccr_data):
        """When a mechanism_id appears in both a full mechanism and a
        cross_reference dict, the full mechanism should be returned."""
        # Mechanism 93 is referenced in gizmodo_samsung_same_chip's cross_references
        # as a dict {mechanism_id: 93, relationship: ...}
        candidates = []

        def _search(obj):
            if isinstance(obj, dict):
                if obj.get('mechanism_id') == 93:
                    candidates.append(obj)
                for v in obj.values():
                    _search(v)
            elif isinstance(obj, list):
                for item in obj:
                    _search(item)

        _search(ccr_data)
        assert len(candidates) >= 2, \
            f"Expected ≥2 dicts with mechanism_id=93 (full + cross-ref), found {len(candidates)}"

        # The full mechanism should have finding_summary
        full = max(candidates, key=lambda c: len(c))
        assert 'finding_summary' in full
        assert 'confounding_factors' in full
        assert len(full) > 5, "Full mechanism should have many keys"

        # The stub should have only 2-3 keys
        stub = min(candidates, key=lambda c: len(c))
        assert len(stub) <= 3, f"Cross-reference stub has too many keys: {list(stub.keys())}"

    def test_all_mechanisms_98_through_100_accessible(self, ccr_data, ce_data):
        """Mechanisms 98-100 (added in iterations 99-101 today) are findable."""
        for mid in [98, 99, 100]:
            candidates = []

            def _search(obj):
                if isinstance(obj, dict):
                    if obj.get('mechanism_id') == mid and 'finding_summary' in obj:
                        candidates.append(obj)
                    for v in obj.values():
                        _search(v)
                elif isinstance(obj, list):
                    for item in obj:
                        _search(item)

            _search(ccr_data)
            _search(ce_data)
            assert len(candidates) >= 1, \
                f"Mechanism #{mid} not found as full mechanism in either profile"


# ── README Stats Freshness ──


class TestREADMEStats:
    """Verify README stats match actual codebase counts."""

    def test_test_file_count(self):
        """Test file count in README matches filesystem."""
        tests_dir = os.path.join(os.path.dirname(__file__))
        test_files = [f for f in os.listdir(tests_dir)
                      if f.startswith('test_') and f.endswith('.py')]
        # Should be ≥372 (may grow)
        assert len(test_files) >= 372, \
            f"Expected ≥372 test files, found {len(test_files)}"

    def test_mechanism_count_matches_range(self, all_mechanisms):
        """Mechanism count should be roughly consistent with ID range."""
        id_range = max(all_mechanisms.keys()) - min(all_mechanisms.keys()) + 1
        # Allow for some gaps (we have 4 known gaps)
        assert len(all_mechanisms) >= id_range - 10, \
            f"Too many gaps: {len(all_mechanisms)} mechanisms in range {id_range}"


# ── Confounding Factor Quality ──


class TestConfoundingFactorPresence:
    """Recent mechanisms (≥95) should all have confounding factors."""

    def test_mechanisms_95_plus_have_confounding_factors(self, all_mechanisms):
        missing = []
        for mid, mech in sorted(all_mechanisms.items()):
            if mid >= 95:
                if 'confounding_factors' not in mech:
                    missing.append(mid)
        assert not missing, \
            f"Mechanisms ≥95 missing confounding_factors: {missing}"

    def test_recent_mechanisms_have_testable_predictions(self, all_mechanisms):
        missing = []
        for mid, mech in sorted(all_mechanisms.items()):
            if mid >= 95:
                if 'testable_predictions' not in mech:
                    missing.append(mid)
        assert not missing, \
            f"Mechanisms ≥95 missing testable_predictions: {missing}"
