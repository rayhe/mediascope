"""
Type D Cross-Validation — Tue 2026-08-18 14:00 PT

Validates mechanisms #164-167 structural integrity across publications
and cross_publication_findings sections. Fixes applied this iteration:
  - YAML parse fix: mechanism #165 was list item instead of named mapping entry
  - Cross-ref overwrite fix: mechanism #33 had mechanism_name in a cross-reference
    that caused find_all_mechanisms to overwrite its real entry with empty refs
  - Stale assertion fixes: updated hardcoded counts in earlier Type D tests

Mechanisms validated:
  #164: Tom's Guide Camera Count Paradox (Snap Specs 4-cam vs Meta 1-cam)
  #165: Amanda Caswell Coverage Scope Asymmetry (dual-register, Meta-only)
  #166: Kali Hays BBC Natural Experiment (public broadcaster control signal)
  #167: Condé Nast "Google Zero" Distribution Dependency (3-dimension incentive)
"""

import os
import yaml
import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")


@pytest.fixture(scope="module")
def ccr():
    with open(os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml")) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def pubs(ccr):
    return ccr.get("publications", {})


@pytest.fixture(scope="module")
def cpf(ccr):
    return ccr.get("cross_publication_findings", {})


@pytest.fixture(scope="module")
def all_mechanisms(ccr):
    """Extract all mechanisms from all sections."""
    mechanisms = {}

    def _walk(obj):
        if isinstance(obj, dict):
            if "mechanism_id" in obj and (
                "mechanism_name" in obj or "finding_summary" in obj
                or "finding" in obj or "finding_type" in obj
                or "name" in obj or "type" in obj
            ):
                mid = obj["mechanism_id"]
                refs = []
                for key in ["related_mechanisms", "cross_references"]:
                    if key in obj:
                        for ref in obj[key]:
                            if isinstance(ref, dict) and "mechanism_id" in ref:
                                refs.append(ref["mechanism_id"])
                            elif isinstance(ref, int):
                                refs.append(ref)
                # Only set if not already set (prevent cross-ref overwrites)
                if mid not in mechanisms:
                    mechanisms[mid] = {"refs": refs, "data": obj}
            for v in obj.values():
                _walk(v)
        elif isinstance(obj, list):
            for v in obj:
                _walk(v)

    _walk(ccr)
    return mechanisms


TARGET_IDS = [164, 165, 166, 167]


# ── Class 1: YAML Structural Integrity ───────────────────────────────


class TestYAMLStructure:
    """Verify the YAML file parses correctly and sections exist."""

    def test_yaml_parses(self, ccr):
        assert ccr is not None

    def test_publications_section_exists(self, ccr):
        assert "publications" in ccr

    def test_publications_count_at_least_9(self, pubs):
        assert len(pubs) >= 9, f"Expected >= 9 publications, got {len(pubs)}"

    def test_no_list_items_in_publications(self, pubs):
        """Publications section should be a mapping, not contain list items at top level."""
        assert isinstance(pubs, dict), "Publications should be a dict/mapping"
        for key in pubs:
            assert isinstance(key, str), f"Publication key should be string, got {type(key)}: {key}"

    def test_mechanism_165_is_named_entry(self, cpf):
        """Regression: mechanism 165 was previously a list item (- mechanism_id: 165)
        instead of a named mapping entry. Verify it's properly keyed."""
        assert "amanda_caswell_tomsguide_cross_entity_coverage_scope_asymmetry" in cpf


# ── Class 2: Mechanism Existence ─────────────────────────────────────


class TestMechanismExistence:
    """All target mechanisms exist and have required fields."""

    @pytest.mark.parametrize("mid", TARGET_IDS)
    def test_mechanism_exists(self, all_mechanisms, mid):
        assert mid in all_mechanisms, f"Mechanism #{mid} not found"

    @pytest.mark.parametrize("mid", TARGET_IDS)
    def test_mechanism_has_finding_type(self, all_mechanisms, mid):
        data = all_mechanisms[mid]["data"]
        assert "finding_type" in data, f"#{mid} missing finding_type"

    @pytest.mark.parametrize("mid", TARGET_IDS)
    def test_mechanism_has_date(self, all_mechanisms, mid):
        data = all_mechanisms[mid]["data"]
        has_date = "date" in data or "date_added" in data
        assert has_date, f"#{mid} missing date/date_added"

    @pytest.mark.parametrize("mid", TARGET_IDS)
    def test_mechanism_has_asymmetry_score(self, all_mechanisms, mid):
        data = all_mechanisms[mid]["data"]
        assert "asymmetry_score" in data, f"#{mid} missing asymmetry_score"

    @pytest.mark.parametrize("mid", TARGET_IDS)
    def test_asymmetry_score_range(self, all_mechanisms, mid):
        score = all_mechanisms[mid]["data"]["asymmetry_score"]
        assert 0 <= score <= 1, f"#{mid} asymmetry_score {score} out of range [0, 1]"


# ── Class 3: Mechanism-Specific Validation ───────────────────────────


class TestMechanism164CameraCountParadox:
    """Tom's Guide camera count paradox: 4 cameras → 0 alarm; 1 camera → alarm."""

    def test_in_cpf(self, cpf):
        assert "tomsguide_snap_specs_camera_count_paradox" in cpf

    def test_finding_type(self, cpf):
        m = cpf["tomsguide_snap_specs_camera_count_paradox"]
        assert m["finding_type"] == "camera_count_privacy_vocabulary_inversion"

    def test_competitor_is_snap(self, cpf):
        m = cpf["tomsguide_snap_specs_camera_count_paradox"]
        assert "Snap" in m.get("competitor", "")

    def test_asymmetry_score(self, cpf):
        m = cpf["tomsguide_snap_specs_camera_count_paradox"]
        assert m["asymmetry_score"] == 0.82

    def test_has_source_urls(self, cpf):
        m = cpf["tomsguide_snap_specs_camera_count_paradox"]
        assert len(m.get("source_urls", [])) >= 3

    def test_has_test_file(self, cpf):
        m = cpf["tomsguide_snap_specs_camera_count_paradox"]
        tf = m.get("test_file", "")
        assert tf
        assert os.path.exists(os.path.join(REPO_ROOT, tf)), f"Test file {tf} not found"


class TestMechanism165CaswellCoverageScope:
    """Amanda Caswell dual-register coverage exclusively targets Meta."""

    def test_in_cpf(self, cpf):
        assert "amanda_caswell_tomsguide_cross_entity_coverage_scope_asymmetry" in cpf

    def test_journalist(self, cpf):
        m = cpf["amanda_caswell_tomsguide_cross_entity_coverage_scope_asymmetry"]
        assert m.get("journalist") == "Amanda Caswell"

    def test_journalist_role(self, cpf):
        m = cpf["amanda_caswell_tomsguide_cross_entity_coverage_scope_asymmetry"]
        assert m.get("journalist_role") == "AI Editor"

    def test_asymmetry_score(self, cpf):
        m = cpf["amanda_caswell_tomsguide_cross_entity_coverage_scope_asymmetry"]
        assert m["asymmetry_score"] == 0.78

    def test_competitor_articles_zero(self, cpf):
        m = cpf["amanda_caswell_tomsguide_cross_entity_coverage_scope_asymmetry"]
        assert m.get("caswell_competitor_articles") == 0

    def test_cross_references_include_164(self, cpf):
        m = cpf["amanda_caswell_tomsguide_cross_entity_coverage_scope_asymmetry"]
        ref_ids = [r["mechanism_id"] for r in m.get("cross_references", []) if isinstance(r, dict)]
        assert 164 in ref_ids


class TestMechanism166KaliHaysBBC:
    """BBC natural experiment: public broadcaster with $0 financial ties."""

    def test_in_cpf(self, cpf):
        assert "kali_hays_bbc_cross_entity_coverage_selection_natural_experiment" in cpf

    def test_publication_type(self, cpf):
        m = cpf["kali_hays_bbc_cross_entity_coverage_selection_natural_experiment"]
        assert m.get("publication_type") == "independent_public_broadcaster"

    def test_funding_model(self, cpf):
        m = cpf["kali_hays_bbc_cross_entity_coverage_selection_natural_experiment"]
        assert "licence fee" in m.get("funding_model", "").lower()

    def test_thesis_impact_structure(self, cpf):
        m = cpf["kali_hays_bbc_cross_entity_coverage_selection_natural_experiment"]
        ti = m.get("thesis_impact", {})
        assert "weakens" in ti
        assert "strengthens" in ti

    def test_weakens_financial_thesis(self, cpf):
        m = cpf["kali_hays_bbc_cross_entity_coverage_selection_natural_experiment"]
        assert "financial" in m["thesis_impact"]["weakens"].lower()

    def test_strengthens_cultural_thesis(self, cpf):
        m = cpf["kali_hays_bbc_cross_entity_coverage_selection_natural_experiment"]
        assert "brand" in m["thesis_impact"]["strengthens"].lower() or \
               "cultural" in m["thesis_impact"]["strengthens"].lower()

    def test_camera_count_paradox(self, cpf):
        m = cpf["kali_hays_bbc_cross_entity_coverage_selection_natural_experiment"]
        assert m.get("snap_cameras", 0) > m.get("meta_cameras", 0)

    def test_competitor_investigation_all_zero(self, cpf):
        m = cpf["kali_hays_bbc_cross_entity_coverage_selection_natural_experiment"]
        counts = m.get("competitor_bbc_investigation_count", {})
        for entity in ["snap", "google", "openai", "samsung"]:
            assert counts.get(entity, -1) == 0, f"BBC {entity} investigation count should be 0"


class TestMechanism167GoogleZero:
    """Condé Nast 3-dimension compound incentive."""

    def test_in_cpf(self, cpf):
        assert "conde_nast_google_zero_distribution_dependency_compound_incentive" in cpf

    def test_has_three_entities_plus(self, cpf):
        m = cpf["conde_nast_google_zero_distribution_dependency_compound_incentive"]
        entities = m.get("entities", [])
        assert len(entities) >= 5, f"Expected >= 5 entities, got {len(entities)}"

    def test_meta_in_entities(self, cpf):
        m = cpf["conde_nast_google_zero_distribution_dependency_compound_incentive"]
        assert "Meta" in m.get("entities", [])

    def test_openai_in_entities(self, cpf):
        m = cpf["conde_nast_google_zero_distribution_dependency_compound_incentive"]
        assert "OpenAI" in m.get("entities", [])

    def test_has_confounding_factors(self, cpf):
        m = cpf["conde_nast_google_zero_distribution_dependency_compound_incentive"]
        cf = m.get("confounding_factors", [])
        assert len(cf) >= 4, f"Expected >= 4 confounders, got {len(cf)}"

    def test_has_strong_confounders(self, cpf):
        m = cpf["conde_nast_google_zero_distribution_dependency_compound_incentive"]
        strong = [c for c in m.get("confounding_factors", []) if c.get("strength") == "STRONG"]
        assert len(strong) >= 2

    def test_has_source_urls(self, cpf):
        m = cpf["conde_nast_google_zero_distribution_dependency_compound_incentive"]
        urls = m.get("source_urls", [])
        assert len(urls) >= 5, f"Expected >= 5 source URLs, got {len(urls)}"

    def test_has_testable_predictions(self, cpf):
        m = cpf["conde_nast_google_zero_distribution_dependency_compound_incentive"]
        tp = m.get("testable_predictions", [])
        assert len(tp) >= 3

    def test_cross_references_include_58(self, cpf):
        """Should reference mechanism #58 (original CN AI deal revenue)."""
        m = cpf["conde_nast_google_zero_distribution_dependency_compound_incentive"]
        ref_ids = [r["mechanism_id"] for r in m.get("cross_references", []) if isinstance(r, dict)]
        assert 58 in ref_ids


# ── Class 4: Cross-Reference Integrity ───────────────────────────────


class TestCrossReferenceIntegrity:
    """Cross-references from #164-167 point to real mechanisms."""

    @pytest.mark.parametrize("mid", TARGET_IDS)
    def test_all_refs_exist(self, all_mechanisms, mid):
        m = all_mechanisms[mid]
        for ref_id in m["refs"]:
            assert ref_id in all_mechanisms, \
                f"#{mid} references #{ref_id} which doesn't exist as a mechanism"

    def test_mechanism_33_not_overwritten(self, all_mechanisms):
        """Regression: a cross-reference to #33 with mechanism_name caused
        find_all_mechanisms to overwrite mechanism 33's real entry.
        Verify mechanism 33 has its real refs (130, 131, 132)."""
        assert 33 in all_mechanisms
        refs = all_mechanisms[33]["refs"]
        for expected in [130, 131, 132]:
            assert expected in refs, \
                f"Mechanism 33 missing ref to #{expected} (cross-ref overwrite regression)"

    def test_no_mechanism_name_in_cross_references(self, ccr):
        """No cross-reference entry should have mechanism_name — that key is reserved
        for top-level mechanism entries and causes find_all_mechanisms to overwrite."""
        def check(obj, path=""):
            issues = []
            if isinstance(obj, dict):
                for key in ["cross_references", "related_mechanisms"]:
                    if key in obj and isinstance(obj[key], list):
                        for i, ref in enumerate(obj[key]):
                            if isinstance(ref, dict) and "mechanism_name" in ref:
                                issues.append(f"{path}.{key}[{i}] (mechanism_id={ref.get('mechanism_id')})")
                for k, v in obj.items():
                    issues.extend(check(v, f"{path}.{k}"))
            elif isinstance(obj, list):
                for i, v in enumerate(obj):
                    issues.extend(check(v, f"{path}[{i}]"))
            return issues

        issues = check(ccr)
        assert not issues, f"Cross-references with mechanism_name (causes overwrite): {issues}"


# ── Class 5: Test File Existence ─────────────────────────────────────


class TestTestFileExistence:
    """Each mechanism's test_file exists and is importable."""

    @pytest.mark.parametrize("mid", TARGET_IDS)
    def test_test_file_exists(self, all_mechanisms, mid):
        data = all_mechanisms[mid]["data"]
        tf = data.get("test_file", "")
        assert tf, f"#{mid} missing test_file"
        full_path = os.path.join(REPO_ROOT, tf)
        assert os.path.exists(full_path), f"Test file for #{mid} not found: {tf}"

    @pytest.mark.parametrize("mid", TARGET_IDS)
    def test_test_count_positive(self, all_mechanisms, mid):
        data = all_mechanisms[mid]["data"]
        tc = data.get("test_count", 0)
        assert tc > 0, f"#{mid} test_count should be positive, got {tc}"


# ── Class 6: Asymmetry Score Distribution ────────────────────────────


class TestAsymmetryScoreDistribution:
    """Validate asymmetry score patterns across #164-167."""

    def test_bbc_lower_than_financial(self, all_mechanisms):
        """BBC (public broadcaster, no financial conflict) should score lower
        than financially-conflicted publications."""
        bbc_score = all_mechanisms[166]["data"]["asymmetry_score"]
        cn_score = all_mechanisms[167]["data"]["asymmetry_score"]
        assert bbc_score < cn_score, \
            f"BBC ({bbc_score}) should score lower than Condé Nast ({cn_score})"

    def test_caswell_lower_than_institutional(self, all_mechanisms):
        """Individual journalist (#165) should score <= institutional finding (#164)."""
        caswell = all_mechanisms[165]["data"]["asymmetry_score"]
        institutional = all_mechanisms[164]["data"]["asymmetry_score"]
        assert caswell <= institutional, \
            f"Individual ({caswell}) should score <= institutional ({institutional})"

    def test_all_scores_meaningful(self, all_mechanisms):
        """All scores should be above 0.5 (meaningful asymmetry)."""
        for mid in TARGET_IDS:
            score = all_mechanisms[mid]["data"]["asymmetry_score"]
            assert score >= 0.5, f"#{mid} score {score} below meaningful threshold"
