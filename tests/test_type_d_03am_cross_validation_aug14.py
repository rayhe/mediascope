"""
Type D Cross-Validation: Mechanisms #92-#94 (Iterations 95-97)
Fri 2026-08-14 03:00 PT

Validates:
  #92: WIRED AISI Accountability Report Coverage Trajectory Break
  #93: Samsung Privacy Feature Framing Inversion
  #94: Apple Advertising Revenue Structural Opacity

Checks: metadata completeness, confounding factor quality, ID integrity,
cross-reference coherence, finding distinctiveness, regression guards,
source URL presence, test file importability, YAML consistency.
"""

import importlib
import os
import re

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CCR_PATH = os.path.join(REPO_ROOT, "profiles", "competitor-coverage-research.yaml")
CE_PATH = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")

VALIDATED_IDS = [92, 93, 94]

# Known-nested mechanism IDs (parsed as sub-entries, not top-level CPF keys)
KNOWN_NESTED_IDS = {80, 81}


@pytest.fixture(scope="module")
def ccr_data():
    with open(CCR_PATH) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def ce_data():
    with open(CE_PATH) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def cpf(ccr_data):
    return ccr_data.get("cross_publication_findings", {})


def find_mechanism_in_cpf(cpf, mid):
    """Find a mechanism by ID in cross_publication_findings (top-level or nested)."""
    for key, val in cpf.items():
        if isinstance(val, dict):
            if val.get("mechanism_id") == mid:
                return val
            for subkey, subval in val.items():
                if isinstance(subval, dict) and subval.get("mechanism_id") == mid:
                    return subval
    return None


def find_mechanism_in_ce(ce, mid, path=""):
    """Recursively find a mechanism in competitor-entities.yaml."""
    results = []
    if isinstance(ce, dict):
        if ce.get("mechanism_id") == mid:
            results.append((path, ce))
        for k, v in ce.items():
            results.extend(find_mechanism_in_ce(v, mid, f"{path}.{k}"))
    elif isinstance(ce, list):
        for i, item in enumerate(ce):
            results.extend(find_mechanism_in_ce(item, mid, f"{path}[{i}]"))
    return results


def collect_all_mechanism_ids_from_section(section):
    """Collect all mechanism IDs from a YAML section (recursive)."""
    ids = set()
    if isinstance(section, dict):
        mid = section.get("mechanism_id")
        if isinstance(mid, int):
            ids.add(mid)
        for val in section.values():
            ids.update(collect_all_mechanism_ids_from_section(val))
    elif isinstance(section, list):
        for item in section:
            ids.update(collect_all_mechanism_ids_from_section(item))
    return ids


def collect_all_mechanism_ids(cpf, ccr_data=None):
    """Collect all mechanism IDs from cross_publication_findings + aggregate_findings."""
    ids = collect_all_mechanism_ids_from_section(cpf)
    if ccr_data:
        agg = ccr_data.get("aggregate_findings", {})
        ids.update(collect_all_mechanism_ids_from_section(agg))
        cel = ccr_data.get("cross_entity_leverage", {})
        ids.update(collect_all_mechanism_ids_from_section(cel))
    return ids


# ── Metadata Completeness ──


class TestMetadataCompleteness:
    """Every validated mechanism has all required metadata fields."""

    @pytest.mark.parametrize("mid", VALIDATED_IDS)
    def test_mechanism_exists_in_ccr(self, cpf, mid):
        m = find_mechanism_in_cpf(cpf, mid)
        assert m is not None, f"Mechanism #{mid} not found in competitor-coverage-research.yaml"

    @pytest.mark.parametrize("mid", VALIDATED_IDS)
    def test_date_added(self, cpf, mid):
        m = find_mechanism_in_cpf(cpf, mid)
        assert m and m.get("date_added"), f"Mechanism #{mid} missing date_added"

    @pytest.mark.parametrize("mid", VALIDATED_IDS)
    def test_finding_summary_length(self, cpf, mid):
        m = find_mechanism_in_cpf(cpf, mid)
        fs = m.get("finding_summary", "") if m else ""
        assert len(fs) >= 100, f"Mechanism #{mid} finding_summary too short ({len(fs)} chars, need ≥100)"

    @pytest.mark.parametrize("mid", VALIDATED_IDS)
    def test_test_file_field(self, cpf, mid):
        m = find_mechanism_in_cpf(cpf, mid)
        tf = m.get("test_file", "") if m else ""
        assert tf, f"Mechanism #{mid} missing test_file field"

    @pytest.mark.parametrize("mid", VALIDATED_IDS)
    def test_test_file_exists_on_disk(self, cpf, mid):
        m = find_mechanism_in_cpf(cpf, mid)
        tf = m.get("test_file", "") if m else ""
        if tf:
            assert os.path.isfile(os.path.join(REPO_ROOT, tf)), f"Mechanism #{mid} test_file {tf} not on disk"


# ── Confounding Factor Quality ──


class TestConfoundingFactorQuality:
    """Every mechanism has ≥3 confounding factors, ≥1 STRONG, ≥2 strength levels."""

    @pytest.mark.parametrize("mid", VALIDATED_IDS)
    def test_confounding_factor_count(self, cpf, mid):
        m = find_mechanism_in_cpf(cpf, mid)
        cf = m.get("confounding_factors", []) if m else []
        assert len(cf) >= 3, f"Mechanism #{mid} has {len(cf)} confounding factors (need ≥3)"

    @pytest.mark.parametrize("mid", VALIDATED_IDS)
    def test_has_strong_factor(self, cpf, mid):
        m = find_mechanism_in_cpf(cpf, mid)
        cf = m.get("confounding_factors", []) if m else []
        strong = sum(1 for c in cf if isinstance(c, dict) and c.get("strength") == "STRONG")
        assert strong >= 1, f"Mechanism #{mid} has {strong} STRONG confounding factors (need ≥1)"

    @pytest.mark.parametrize("mid", VALIDATED_IDS)
    def test_multiple_strength_levels(self, cpf, mid):
        m = find_mechanism_in_cpf(cpf, mid)
        cf = m.get("confounding_factors", []) if m else []
        strengths = set(c.get("strength", "") for c in cf if isinstance(c, dict))
        assert len(strengths) >= 2, f"Mechanism #{mid} has {len(strengths)} strength levels (need ≥2)"


# ── Testable Predictions ──


class TestTestablePredictions:
    """Every mechanism has ≥2 testable predictions."""

    @pytest.mark.parametrize("mid", VALIDATED_IDS)
    def test_prediction_count(self, cpf, mid):
        m = find_mechanism_in_cpf(cpf, mid)
        tp = m.get("testable_predictions", []) if m else []
        assert len(tp) >= 2, f"Mechanism #{mid} has {len(tp)} testable predictions (need ≥2)"


# ── Source URL Presence ──


class TestSourceURLPresence:
    """Every mechanism has ≥1 source URL."""

    @pytest.mark.parametrize("mid", VALIDATED_IDS)
    def test_source_urls_present(self, cpf, mid):
        m = find_mechanism_in_cpf(cpf, mid)
        su = m.get("source_urls", []) if m else []
        assert len(su) >= 1, f"Mechanism #{mid} has {len(su)} source URLs (need ≥1)"


# ── ID Integrity ──


class TestIDIntegrity:
    """No duplicate IDs, max ID = 94."""

    def test_no_duplicate_ids_in_cpf_top_level(self, cpf):
        """Top-level CPF keys should have unique mechanism IDs (nested sub-entries excluded)."""
        ids = []
        for key, val in cpf.items():
            if isinstance(val, dict) and "mechanism_id" in val:
                ids.append(val["mechanism_id"])
        assert len(ids) == len(set(ids)), f"Duplicate top-level CPF IDs: {[x for x in ids if ids.count(x) > 1]}"

    def test_max_id_is_94(self, ccr_data, cpf):
        all_ids = collect_all_mechanism_ids(cpf, ccr_data)
        assert max(all_ids) == 94, f"Max mechanism ID is {max(all_ids)}, expected 94"


# ── Cross-Reference Coherence ──


class TestCrossReferenceCoherence:
    """All cross-references point to existing mechanisms."""

    @pytest.mark.parametrize("mid", VALIDATED_IDS)
    def test_cross_references_valid(self, ccr_data, cpf, mid):
        m = find_mechanism_in_cpf(cpf, mid)
        if not m:
            pytest.skip(f"Mechanism #{mid} not found")
        refs = m.get("cross_references", m.get("related_mechanisms", []))
        all_ids = collect_all_mechanism_ids(cpf, ccr_data)
        for ref in refs:
            ref_id = ref if isinstance(ref, int) else ref.get("mechanism_id") if isinstance(ref, dict) else None
            if ref_id is not None and ref_id >= 17:
                assert ref_id in all_ids or ref_id in KNOWN_NESTED_IDS, (
                    f"Mechanism #{mid} references #{ref_id} which doesn't exist"
                )


# ── Finding Distinctiveness ──


class TestFindingDistinctiveness:
    """Jaccard similarity between validated mechanisms < 0.7."""

    def _tokenize(self, text):
        return set(re.findall(r"\w+", text.lower()))

    def _jaccard(self, a, b):
        if not a or not b:
            return 0.0
        return len(a & b) / len(a | b)

    def test_pairwise_distinctiveness(self, cpf):
        summaries = {}
        for mid in VALIDATED_IDS:
            m = find_mechanism_in_cpf(cpf, mid)
            if m:
                summaries[mid] = self._tokenize(m.get("finding_summary", ""))

        for i, id_a in enumerate(VALIDATED_IDS):
            for id_b in VALIDATED_IDS[i + 1 :]:
                if id_a in summaries and id_b in summaries:
                    sim = self._jaccard(summaries[id_a], summaries[id_b])
                    assert sim < 0.7, (
                        f"Mechanisms #{id_a} and #{id_b} are too similar (Jaccard={sim:.3f})"
                    )


# ── Regression Guards ──


class TestRegressionGuards:
    """Mechanisms #89-#91 (previous batch) still present with test_file fields."""

    @pytest.mark.parametrize("mid", [89, 90, 91])
    def test_previous_batch_present(self, cpf, mid):
        m = find_mechanism_in_cpf(cpf, mid)
        assert m is not None, f"Previous mechanism #{mid} has disappeared"

    @pytest.mark.parametrize("mid", [89, 90, 91])
    def test_previous_batch_has_test_file(self, cpf, mid):
        m = find_mechanism_in_cpf(cpf, mid)
        if m:
            tf = m.get("test_file", "")
            assert tf, f"Previous mechanism #{mid} lost its test_file field"


# ── Competitor Entities YAML Consistency ──


class TestCEConsistency:
    """All validated mechanisms also exist in competitor-entities.yaml."""

    @pytest.mark.parametrize("mid", VALIDATED_IDS)
    def test_mechanism_in_ce(self, ce_data, mid):
        locs = find_mechanism_in_ce(ce_data, mid)
        assert locs, f"Mechanism #{mid} not found in competitor-entities.yaml"


# ── Test File Importability ──


class TestFileImportability:
    """All mechanism test files import without errors."""

    TEST_FILES = {
        92: "test_wired_aisi_accountability_coverage_trajectory_break_aug14",
        93: "test_samsung_privacy_feature_framing_inversion_aug14",
        94: "test_apple_ad_revenue_opacity_coverage_accountability_asymmetry_aug14",
    }

    @pytest.mark.parametrize("mid", VALIDATED_IDS)
    def test_import(self, mid):
        module_name = self.TEST_FILES[mid]
        try:
            importlib.import_module(f"tests.{module_name}")
        except Exception as e:
            pytest.fail(f"Failed to import tests/{module_name}.py: {e}")


# ── Entity-Specific Targeting ──


class TestEntityTargeting:
    """Each mechanism targets its expected entity/pattern."""

    def test_92_targets_wired_anthropic(self, cpf):
        m = find_mechanism_in_cpf(cpf, 92)
        fs = m.get("finding_summary", "").lower()
        assert "wired" in fs, "#92 should mention WIRED"
        assert "anthropic" in fs or "aisi" in fs, "#92 should mention Anthropic or AISI"

    def test_93_targets_samsung(self, cpf):
        m = find_mechanism_in_cpf(cpf, 93)
        fs = m.get("finding_summary", "").lower()
        assert "samsung" in fs, "#93 should mention Samsung"
        assert "meta" in fs, "#93 should mention Meta (for comparison)"

    def test_94_targets_apple(self, cpf):
        m = find_mechanism_in_cpf(cpf, 94)
        fs = m.get("finding_summary", "").lower()
        assert "apple" in fs, "#94 should mention Apple"
        assert "advertising" in fs or "ad revenue" in fs, "#94 should mention advertising"


# ── Samsung Cluster Coherence ──


class TestSamsungClusterCoherence:
    """Mechanism #93 references existing Samsung cluster members."""

    SAMSUNG_CLUSTER_IDS = {30, 74, 76, 80, 81, 89, 90, 91}

    def test_93_references_cluster(self, cpf):
        m = find_mechanism_in_cpf(cpf, 93)
        refs = m.get("cross_references", m.get("related_mechanisms", []))
        ref_ids = set()
        for ref in refs:
            if isinstance(ref, int):
                ref_ids.add(ref)
            elif isinstance(ref, dict) and "mechanism_id" in ref:
                ref_ids.add(ref["mechanism_id"])
        overlap = ref_ids & self.SAMSUNG_CLUSTER_IDS
        assert overlap, f"#93 should reference at least one Samsung cluster member, refs={ref_ids}"


# ── WIRED Investigation Cluster Coherence ──


class TestWIREDClusterCoherence:
    """Mechanism #92 references existing WIRED investigation mechanisms."""

    WIRED_INVESTIGATION_IDS = {34, 48, 58, 82, 84}

    def test_92_references_wired_cluster(self, cpf):
        m = find_mechanism_in_cpf(cpf, 92)
        refs = m.get("cross_references", m.get("related_mechanisms", []))
        ref_ids = set()
        for ref in refs:
            if isinstance(ref, int):
                ref_ids.add(ref)
            elif isinstance(ref, dict) and "mechanism_id" in ref:
                ref_ids.add(ref["mechanism_id"])
            elif isinstance(ref, str):
                # Parse "Mechanism #34: ..." format
                match = re.search(r"#(\d+)", ref)
                if match:
                    ref_ids.add(int(match.group(1)))
        overlap = ref_ids & self.WIRED_INVESTIGATION_IDS
        assert overlap, f"#92 should reference WIRED investigation cluster, refs={ref_ids}"
