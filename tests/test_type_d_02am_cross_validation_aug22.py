"""
Type D cross-validation — Sat 2026-08-22, 02:00 PT

Fixes applied this iteration:
1. Mechanism #221: Added missing discovery_date (2026-08-21) and iteration (232)
2. Mechanisms #222-224: Added canonical name + finding_summary fields alongside
   mechanism + detail (field normalization for structural consistency)
3. Mechanisms #221, #222, #224: Added missing cross_references
4. Three Aug 21 Type D test files: Updated stale highest_mechanism #220 → #224
5. find_all_mechanisms helper in test_type_d_8pm_cross_validation_aug21.py:
   CRITICAL BUG FIX — recursive traversal was including cross_reference stubs
   (which have mechanism_id but no data fields), causing mechanism entries to be
   overwritten by empty cross_reference dicts. Fixed by skipping cross_references
   key during recursion and requiring at least one real data field.
6. test_type_d_8pm_cross_validation_aug21.py: Stale doc count 526 → 530
7. test_type_d_10am_cross_validation_aug21.py: REQUIRED_FIELDS updated to accept
   either overview or finding_summary (both are valid summary field names)

Test count: 531 (this file is #531)
"""

import os
import re
import glob
import yaml
import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(REPO_ROOT, 'profiles')
TESTS_DIR = os.path.join(REPO_ROOT, 'tests')


def load_yaml(filename):
    with open(os.path.join(PROFILES_DIR, filename)) as f:
        return yaml.safe_load(f)


def find_all_mechanisms(data, results=None):
    """Find all mechanism entries, skipping cross_references to avoid overwrites."""
    if results is None:
        results = {}
    if isinstance(data, dict):
        if 'mechanism_id' in data:
            mid = data['mechanism_id']
            if isinstance(mid, int):
                # Only store real mechanisms, not cross_reference stubs
                if any(k in data for k in ('finding_summary', 'detail', 'name',
                                            'mechanism', 'asymmetry_score',
                                            'confounding_factors', 'overview')):
                    results[mid] = data
        for k, v in data.items():
            if k == 'cross_references':
                continue  # skip to prevent cross_ref stubs overwriting real entries
            find_all_mechanisms(v, results)
    elif isinstance(data, list):
        for item in data:
            find_all_mechanisms(item, results)
    return results


@pytest.fixture(scope='module')
def competitor_research():
    return load_yaml('competitor-coverage-research.yaml')


@pytest.fixture(scope='module')
def all_mechanisms(competitor_research):
    return find_all_mechanisms(competitor_research)


class TestHighestMechanism:
    """Current highest mechanism should be #224."""

    def test_highest_mechanism_is_224(self, all_mechanisms):
        max_id = max(all_mechanisms.keys())
        assert max_id == 224, f"Expected highest mechanism #224, got #{max_id}"


class TestMechanism221Fixes:
    """Mechanism #221 was missing discovery_date and cross_references."""

    def test_221_has_discovery_date(self, all_mechanisms):
        assert 'discovery_date' in all_mechanisms[221], \
            "#221 should have discovery_date after fix"
        assert all_mechanisms[221]['discovery_date'] == '2026-08-21'

    def test_221_has_iteration(self, all_mechanisms):
        assert all_mechanisms[221].get('iteration') == 232

    def test_221_has_cross_references(self, all_mechanisms):
        xrefs = all_mechanisms[221].get('cross_references', [])
        assert len(xrefs) >= 2, \
            f"#221 should have ≥2 cross_references, got {len(xrefs)}"

    def test_221_xrefs_reference_valid_mechanisms(self, all_mechanisms):
        xrefs = all_mechanisms[221].get('cross_references', [])
        for xref in xrefs:
            ref_id = xref.get('mechanism_id')
            assert ref_id in all_mechanisms, \
                f"#221 cross-references #{ref_id} which doesn't exist"


class TestFieldNormalization222To224:
    """Mechanisms #222-224 should have both canonical name+finding_summary
    and their original mechanism+detail fields."""

    @pytest.mark.parametrize("mid", [222, 223, 224])
    def test_has_name_field(self, all_mechanisms, mid):
        assert 'name' in all_mechanisms[mid], \
            f"#{mid} should have name field after normalization"

    @pytest.mark.parametrize("mid", [222, 223, 224])
    def test_has_finding_summary(self, all_mechanisms, mid):
        assert 'finding_summary' in all_mechanisms[mid], \
            f"#{mid} should have finding_summary after normalization"
        assert len(all_mechanisms[mid]['finding_summary']) >= 100, \
            f"#{mid} finding_summary too short"

    @pytest.mark.parametrize("mid", [222, 223, 224])
    def test_has_detail(self, all_mechanisms, mid):
        assert 'detail' in all_mechanisms[mid], \
            f"#{mid} should still have detail field"

    @pytest.mark.parametrize("mid", [222, 223, 224])
    def test_has_discovery_date(self, all_mechanisms, mid):
        assert 'discovery_date' in all_mechanisms[mid]
        assert all_mechanisms[mid]['discovery_date'] == '2026-08-22'


class TestCrossReferences222And224:
    """Mechanisms #222 and #224 were missing cross_references."""

    def test_222_has_cross_references(self, all_mechanisms):
        xrefs = all_mechanisms[222].get('cross_references', [])
        assert len(xrefs) >= 2, \
            f"#222 should have ≥2 cross_references, got {len(xrefs)}"

    def test_222_references_211(self, all_mechanisms):
        """#222 extends #211 (Pero three-entity gradient)."""
        xrefs = all_mechanisms[222].get('cross_references', [])
        ref_ids = [x.get('mechanism_id') for x in xrefs]
        assert 211 in ref_ids, "#222 should reference #211"

    def test_224_has_cross_references(self, all_mechanisms):
        xrefs = all_mechanisms[224].get('cross_references', [])
        assert len(xrefs) >= 2, \
            f"#224 should have ≥2 cross_references, got {len(xrefs)}"

    def test_224_references_222(self, all_mechanisms):
        """#224 references #222 (Pero source amplification of Snap CEO)."""
        xrefs = all_mechanisms[224].get('cross_references', [])
        ref_ids = [x.get('mechanism_id') for x in xrefs]
        assert 222 in ref_ids, "#224 should reference #222"


class TestFindAllMechanismsBugFix:
    """The critical bug: find_all_mechanisms was including cross_reference stubs,
    overwriting real mechanism entries with empty dicts."""

    def test_mechanism_218_has_confounding_factors(self, all_mechanisms):
        """This test was FAILING before the fix because #223's cross_reference
        to #218 overwrote the real #218 entry."""
        cf = all_mechanisms[218].get('confounding_factors', [])
        assert len(cf) >= 5, \
            f"#218 should have ≥5 confounding_factors, got {len(cf)}"

    def test_mechanism_218_has_real_data(self, all_mechanisms):
        """Real #218 has name, finding_summary, asymmetry_score — not just
        mechanism_id, relationship, description from a cross_reference."""
        m = all_mechanisms[218]
        assert 'name' in m, "#218 should have name (not a cross_ref stub)"
        assert 'asymmetry_score' in m, "#218 should have asymmetry_score"
        assert 'finding_summary' in m, "#218 should have finding_summary"

    def test_no_cross_ref_stubs_in_mechanisms(self, all_mechanisms):
        """No mechanism entry should look like a cross_reference stub
        (i.e., have only mechanism_id + relationship + description)."""
        for mid, m in all_mechanisms.items():
            stub_keys = {'mechanism_id', 'relationship', 'description'}
            if set(m.keys()) <= stub_keys:
                pytest.fail(
                    f"Mechanism #{mid} looks like a cross_reference stub: "
                    f"keys={list(m.keys())}"
                )


class TestDocCountSync:
    """Doc counts should match actual test file count."""

    def test_actual_test_file_count_is_531(self):
        actual = len(glob.glob(os.path.join(TESTS_DIR, 'test_*.py')))
        assert actual == 531, f"Expected 531 test files, got {actual}"


class TestMechanismIdContiguity:
    """No gaps in mechanism IDs above #200."""

    def test_no_gaps_above_200(self, all_mechanisms):
        ids_above_200 = sorted(k for k in all_mechanisms if k >= 200)
        if len(ids_above_200) >= 2:
            expected = set(range(ids_above_200[0], ids_above_200[-1] + 1))
            missing = expected - set(ids_above_200)
            assert not missing, f"Gaps in mechanism IDs above 200: {sorted(missing)}"


class TestTypeRotation221To224:
    """Mechanisms #221-224 should follow E, A, B, C rotation."""

    EXPECTED_TYPES = {
        221: 'E',
        222: 'A',
        223: 'B',
        224: 'C',
    }

    def test_rotation_types(self, all_mechanisms):
        for mid, expected_prefix in self.EXPECTED_TYPES.items():
            mtype = all_mechanisms[mid].get('type', '')
            assert mtype.startswith(expected_prefix) or expected_prefix in mtype, \
                f"#{mid} type '{mtype}' should start with or contain '{expected_prefix}'"
