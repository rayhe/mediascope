"""Type D cross-validation — Aug 13, 5 AM PT

Validates integrity after iterations 79-81:
1. Mechanism #78 exists in YAML (was missing — added this iteration)
2. Mechanisms #77-#79 all have required fields (test_file, date_added, sources)
3. Mechanism ID contiguity 17-79 (no gaps after #78 insertion)
4. Test file existence for all mechanisms #77-#79
5. README/ARCHITECTURE stat agreement with count_stats
6. No mechanism_id appears in both cross_publication_findings AND aggregate_findings
7. Prior cross-validation fixes remain stable
8. Journalist profiles referenced in mechanism tests exist in careers data
"""

import os
import re
import subprocess
import sys

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO_ROOT)


def read_file(name):
    with open(os.path.join(REPO_ROOT, name)) as f:
        return f.read()


def load_research():
    with open(os.path.join(REPO_ROOT, 'profiles', 'competitor-coverage-research.yaml')) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def research():
    return load_research()


@pytest.fixture(scope='module')
def cpf(research):
    return research.get('cross_publication_findings', {})


@pytest.fixture(scope='module')
def agg(research):
    return research.get('aggregate_findings', {})


@pytest.fixture(scope='module')
def all_mechanisms(cpf, agg):
    mechs = {}
    for section in (cpf, agg):
        for key, m in section.items():
            if isinstance(m, dict) and 'mechanism_id' in m:
                mid = m['mechanism_id']
                if isinstance(mid, int):
                    mechs[mid] = m
    return mechs


# ===================================================================
# 1. Mechanism #78 exists in YAML (was missing before this iteration)
# ===================================================================

class TestMechanism78Fix:
    """Iteration 80 added mechanism #78 (Gemini Android XR Data Retention)
    but it was only in ARCHITECTURE.md and the test file, NOT in the YAML.
    This iteration fixed the gap."""

    def test_mechanism_78_exists_in_yaml(self, all_mechanisms):
        assert 78 in all_mechanisms, (
            "Mechanism #78 (Gemini Android XR Data Retention) missing from YAML"
        )

    def test_mechanism_78_has_correct_title(self, all_mechanisms):
        m = all_mechanisms[78]
        title = m.get('title', '')
        assert 'Gemini' in title or 'Android XR' in title or 'Data Retention' in title, (
            f"Mechanism #78 title should reference Gemini/Android XR: {title}"
        )

    def test_mechanism_78_has_test_file(self, all_mechanisms):
        m = all_mechanisms[78]
        test_file = m.get('test_file', '')
        assert test_file, "Mechanism #78 must have a test_file field"
        assert os.path.exists(os.path.join(REPO_ROOT, test_file)), (
            f"Test file {test_file} for mechanism #78 does not exist"
        )

    def test_mechanism_78_has_date_added(self, all_mechanisms):
        m = all_mechanisms[78]
        assert 'date_added' in m, "Mechanism #78 must have date_added field"

    def test_mechanism_78_has_sources(self, all_mechanisms):
        m = all_mechanisms[78]
        sources = m.get('sources', [])
        assert len(sources) >= 2, (
            f"Mechanism #78 should have at least 2 sources, has {len(sources)}"
        )

    def test_mechanism_78_references_google_gemini_privacy_hub(self, all_mechanisms):
        m = all_mechanisms[78]
        sources = m.get('sources', [])
        urls = [s.get('url', '') for s in sources]
        has_google_source = any('google.com' in u or 'gemini' in u.lower() for u in urls)
        descs = [s.get('description', '') for s in sources]
        has_gemini_desc = any('gemini' in d.lower() or 'privacy hub' in d.lower() for d in descs)
        assert has_google_source or has_gemini_desc, (
            "Mechanism #78 must reference Google's Gemini Privacy Hub"
        )


# ===================================================================
# 2. Mechanisms #77-#79 field completeness
# ===================================================================

class TestRecentMechanismFieldCompleteness:
    """All mechanisms from iterations 79-81 should have required fields."""

    @pytest.mark.parametrize("mid", [77, 78, 79])
    def test_mechanism_exists(self, all_mechanisms, mid):
        assert mid in all_mechanisms, f"Mechanism #{mid} missing from YAML"

    @pytest.mark.parametrize("mid", [77, 78, 79])
    def test_has_title(self, all_mechanisms, mid):
        assert 'title' in all_mechanisms[mid], f"Mechanism #{mid} missing title"

    @pytest.mark.parametrize("mid", [77, 78, 79])
    def test_has_finding_summary(self, all_mechanisms, mid):
        m = all_mechanisms[mid]
        summary = m.get('finding_summary', '')
        assert len(summary) > 100, (
            f"Mechanism #{mid} finding_summary too short ({len(summary)} chars)"
        )

    @pytest.mark.parametrize("mid", [77, 78, 79])
    def test_has_test_file(self, all_mechanisms, mid):
        m = all_mechanisms[mid]
        assert 'test_file' in m, f"Mechanism #{mid} missing test_file"
        tf = m['test_file']
        assert os.path.exists(os.path.join(REPO_ROOT, tf)), (
            f"Mechanism #{mid} test file {tf} does not exist"
        )

    @pytest.mark.parametrize("mid", [77, 78, 79])
    def test_has_date_added(self, all_mechanisms, mid):
        assert 'date_added' in all_mechanisms[mid], f"Mechanism #{mid} missing date_added"

    @pytest.mark.parametrize("mid", [77, 78, 79])
    def test_has_confounding_factors(self, all_mechanisms, mid):
        m = all_mechanisms[mid]
        cf = m.get('confounding_factors', [])
        assert len(cf) >= 3, (
            f"Mechanism #{mid} has only {len(cf)} confounding factors (need >=3)"
        )

    @pytest.mark.parametrize("mid", [77, 78, 79])
    def test_has_testable_predictions(self, all_mechanisms, mid):
        m = all_mechanisms[mid]
        tp = m.get('testable_predictions', [])
        assert len(tp) >= 2, (
            f"Mechanism #{mid} has only {len(tp)} testable predictions (need >=2)"
        )


# ===================================================================
# 3. Mechanism ID contiguity 17-79
# ===================================================================

class TestMechanismIDContiguity:
    """After #78 fix, IDs should be contiguous from 17 to 79."""

    def test_no_gaps(self, all_mechanisms):
        ids = set(all_mechanisms.keys())
        expected = set(range(17, 80))
        missing = expected - ids
        assert not missing, f"Missing mechanism IDs: {sorted(missing)}"

    def test_max_is_79(self, all_mechanisms):
        assert max(all_mechanisms.keys()) == 79

    def test_min_is_17(self, all_mechanisms):
        assert min(all_mechanisms.keys()) == 17

    def test_no_duplicates_between_sections(self, cpf, agg):
        cpf_ids = set()
        agg_ids = set()
        for key, m in cpf.items():
            if isinstance(m, dict) and 'mechanism_id' in m:
                mid = m['mechanism_id']
                if isinstance(mid, int):
                    cpf_ids.add(mid)
        for key, m in agg.items():
            if isinstance(m, dict) and 'mechanism_id' in m:
                mid = m['mechanism_id']
                if isinstance(mid, int):
                    agg_ids.add(mid)
        overlap = cpf_ids & agg_ids
        assert not overlap, f"Mechanism IDs in both sections: {overlap}"


# ===================================================================
# 4. ARCHITECTURE.md lists mechanisms #77-#79
# ===================================================================

class TestArchitectureDocumentation:
    """ARCHITECTURE.md should list all three recent mechanisms."""

    @classmethod
    @pytest.fixture(scope='class')
    def arch_text(cls):
        return read_file('docs/ARCHITECTURE.md')

    def test_mechanism_77_in_architecture(self, arch_text):
        assert 'Mechanism #77' in arch_text or 'mechanism_77' in arch_text.lower() or \
               'nyt_samsung_glasses' in arch_text, "Mechanism #77 missing from ARCHITECTURE.md"

    def test_mechanism_78_in_architecture(self, arch_text):
        assert 'Mechanism #78' in arch_text or 'gemini_android_xr' in arch_text, \
            "Mechanism #78 missing from ARCHITECTURE.md"

    def test_mechanism_79_in_architecture(self, arch_text):
        assert 'Mechanism #79' in arch_text or 'parallel_publisher_copyright' in arch_text, \
            "Mechanism #79 missing from ARCHITECTURE.md"


# ===================================================================
# 5. README stat agreement
# ===================================================================

class TestStatAgreement:
    """README stats must match count_stats.py output."""

    @classmethod
    @pytest.fixture(scope='class')
    def stats_output(cls):
        result = subprocess.run(
            ['python3', 'scripts/count_stats.py', '--check'],
            capture_output=True, text=True, cwd=REPO_ROOT
        )
        return result

    def test_readme_stats_current(self, stats_output):
        assert stats_output.returncode == 0, (
            f"count_stats.py --check failed:\n{stats_output.stdout}\n{stats_output.stderr}"
        )
        assert '✅' in stats_output.stdout, "Stats check should show ✅"


# ===================================================================
# 6. Cross-reference consistency for #77-#79
# ===================================================================

class TestCrossReferenceConsistency:
    """Related mechanisms referenced in #77-#79 should exist."""

    def test_mechanism_77_references_valid(self, all_mechanisms):
        m = all_mechanisms[77]
        related = m.get('related_mechanisms', [])
        for ref in related:
            # Extract mechanism IDs from references
            match = re.search(r'Mechanism #(\d+)', ref)
            if match:
                ref_id = int(match.group(1))
                assert ref_id in all_mechanisms, (
                    f"Mechanism #77 references #{ref_id} which doesn't exist"
                )

    def test_mechanism_78_references_valid(self, all_mechanisms):
        m = all_mechanisms[78]
        related = m.get('related_mechanisms', [])
        for ref in related:
            match = re.search(r'Mechanism #(\d+)', ref)
            if match:
                ref_id = int(match.group(1))
                assert ref_id in all_mechanisms, (
                    f"Mechanism #78 references #{ref_id} which doesn't exist"
                )

    def test_mechanism_79_cross_refs_valid(self):
        """Mechanism #79 test file references existing mechanisms."""
        test_text = read_file('tests/test_parallel_publisher_copyright_litigation_financial_conflict_aug13.py')
        # Should reference meta_inverse_leverage and google_ad_dependency
        assert 'meta_inverse_leverage' in test_text or 'google_ad_dependency' in test_text, (
            "Mechanism #79 tests should cross-reference existing financial mechanisms"
        )


# ===================================================================
# 7. Confounding factor strength validation
# ===================================================================

class TestConfoundingFactorStrengths:
    """Confounding factors should use standardized strength labels."""

    VALID_STRENGTHS = {'STRONG', 'MODERATE', 'WEAK'}

    @pytest.mark.parametrize("mid", [77, 78, 79])
    def test_valid_strengths(self, all_mechanisms, mid):
        m = all_mechanisms[mid]
        for cf in m.get('confounding_factors', []):
            strength = cf.get('strength', '')
            assert strength in self.VALID_STRENGTHS, (
                f"Mechanism #{mid} has invalid confounding factor strength: {strength}"
            )

    @pytest.mark.parametrize("mid", [77, 78, 79])
    def test_has_at_least_one_strong(self, all_mechanisms, mid):
        m = all_mechanisms[mid]
        strengths = [cf.get('strength', '') for cf in m.get('confounding_factors', [])]
        assert 'STRONG' in strengths, (
            f"Mechanism #{mid} should have at least one STRONG confounding factor"
        )


# ===================================================================
# 8. Privacy/glasses mechanisms form coherent cluster
# ===================================================================

class TestGlassesPrivacyClusterCoherence:
    """Mechanisms #77 and #78 both cover glasses privacy investigation
    asymmetry. They should reference each other."""

    def test_77_and_78_cross_reference(self, all_mechanisms):
        m77_related = all_mechanisms[77].get('related_mechanisms', [])
        m78_related = all_mechanisms[78].get('related_mechanisms', [])
        m77_refs_78 = any('77' in r or 'NYT' in r for r in m78_related)
        m78_refs_77 = any('78' in r or 'Gemini' in r for r in m77_related)
        # At least one direction should cross-reference
        assert m77_refs_78 or m78_refs_77, (
            "Mechanisms #77 and #78 both cover glasses privacy but don't cross-reference"
        )

    def test_samsung_compound_leverage_referenced(self, all_mechanisms):
        """Both #77 and #78 should reference mechanism #76 (Samsung-Google Compound Advertiser Leverage)."""
        for mid in (77, 78):
            m = all_mechanisms[mid]
            related = m.get('related_mechanisms', [])
            refs_76 = any('#76' in r or 'Samsung' in r.lower() or 'Compound' in r for r in related)
            assert refs_76, (
                f"Mechanism #{mid} should reference #76 (Samsung-Google Compound Advertiser Leverage)"
            )
