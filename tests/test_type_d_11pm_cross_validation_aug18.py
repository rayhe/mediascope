"""
Type D Cross-Validation — Tue 2026-08-18 23:00 PT

Validates the mechanism section-placement fix applied this iteration:
  - 8 mechanisms (#164-169, #171, #172) were misplaced in the `publications`
    section instead of `cross_publication_findings` (same bug as #152 in iter #153)
  - All 8 moved to `cross_publication_findings`
  - README body text synced with table (16763/461)
  - Earlier cross-validation tests updated for new section locations
  - Guard test: no mechanism entries should exist as top-level keys in `publications`

Mechanisms validated:
  #164: Tom's Guide Camera Count Paradox (Snap Specs)
  #165: Amanda Caswell Coverage Scope Asymmetry
  #166: Kali Hays BBC Natural Experiment
  #167: Condé Nast "Google Zero" Distribution Dependency
  #168: TWiT 1058 Victoria Song Cross-Medium Privacy Vocabulary Portability
  #169: Guardian Samsung Galaxy Glasses London Geographic Proximity
  #170: Gizmodo OpenAI Companion Surveillance Vocabulary Inversion
  #171: Daniel Bader 9to5Google Career-Ecosystem Capture
  #172: OpenAI CPA Advertising Maturation
"""

import os
import re
import glob
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
def cpf(ccr):
    return ccr.get("cross_publication_findings", {})


@pytest.fixture(scope="module")
def pubs(ccr):
    return ccr.get("publications", {})


@pytest.fixture(scope="module")
def agg(ccr):
    return ccr.get("aggregate_findings", {})


@pytest.fixture(scope="module")
def readme():
    with open(os.path.join(REPO_ROOT, "README.md")) as f:
        return f.read()


@pytest.fixture(scope="module")
def architecture():
    with open(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")) as f:
        return f.read()


@pytest.fixture(scope="module")
def test_file_count():
    return len(glob.glob(os.path.join(TESTS_DIR, "test_*.py")))


# IDs that were misplaced in publications and moved to cpf this iteration
MOVED_IDS = [164, 165, 166, 167, 168, 169, 171, 172]

# All mechanisms that should now be in cpf (>= 163, excluding 161-162 which are in agg)
CPF_HIGH_IDS = [163, 164, 165, 166, 167, 168, 169, 170, 171, 172]


# ── Class 1: Section Placement Guard ────────────────────────────────


class TestSectionPlacementGuard:
    """No mechanism entries should exist as top-level keys in publications."""

    def test_no_mechanisms_in_publications(self, pubs):
        """Regression guard: mechanisms must NOT be stored in publications section."""
        for key, val in pubs.items():
            if isinstance(val, dict) and "mechanism_id" in val:
                # Allow nested references (like wwdc_2026_pcc_omission_ref inside mit-tech-review)
                # but NOT top-level mechanism entries
                if "finding_summary" in val or "finding_type" in val or "finding" in val:
                    pytest.fail(
                        f"Mechanism #{val['mechanism_id']} ({key}) is a top-level entry "
                        f"in publications — should be in cross_publication_findings"
                    )

    def test_publications_are_publication_profiles(self, pubs):
        """Publications section should contain publication profiles, not mechanisms."""
        expected_profiles = {"wired", "nytimes", "guardian", "atlantic", "financial-times",
                             "gizmodo", "the-verge", "mit-tech-review", "news-corp"}
        actual = set(pubs.keys())
        overlap = expected_profiles & actual
        assert len(overlap) >= 7, f"Expected >= 7 publication profiles, found {len(overlap)}: {overlap}"

    @pytest.mark.parametrize("mid", MOVED_IDS)
    def test_moved_mechanism_in_cpf(self, cpf, mid):
        """Each moved mechanism should now exist in cross_publication_findings."""
        found = any(
            isinstance(v, dict) and v.get("mechanism_id") == mid
            for v in cpf.values()
        )
        assert found, f"Mechanism #{mid} not found in cross_publication_findings after move"

    @pytest.mark.parametrize("mid", MOVED_IDS)
    def test_moved_mechanism_not_in_pubs(self, pubs, mid):
        """Each moved mechanism should NOT exist as a top-level in publications."""
        found = any(
            isinstance(v, dict) and v.get("mechanism_id") == mid
            for v in pubs.values()
        )
        assert not found, f"Mechanism #{mid} still found in publications after move"


# ── Class 2: CPF Completeness ────────────────────────────────────────


class TestCPFCompleteness:
    """cross_publication_findings has all expected mechanisms >= 163."""

    @pytest.mark.parametrize("mid", CPF_HIGH_IDS)
    def test_mechanism_in_cpf(self, cpf, mid):
        found = any(
            isinstance(v, dict) and v.get("mechanism_id") == mid
            for v in cpf.values()
        )
        assert found, f"Mechanism #{mid} not found in cross_publication_findings"

    def test_cpf_count_at_least_145(self, cpf):
        count = sum(1 for v in cpf.values() if isinstance(v, dict) and "mechanism_id" in v)
        assert count >= 145, f"Expected >= 145 CPF mechanisms, got {count}"

    def test_max_cpf_id_is_172(self, cpf):
        ids = [v["mechanism_id"] for v in cpf.values() if isinstance(v, dict) and "mechanism_id" in v]
        assert max(ids) >= 172, f"Expected max CPF mechanism >= 172, got {max(ids)}"

    def test_aggregate_has_161_162(self, agg):
        """Mechanisms #161 and #162 should be in aggregate_findings, not cpf."""
        agg_ids = [v["mechanism_id"] for v in agg.values() if isinstance(v, dict) and "mechanism_id" in v]
        assert 161 in agg_ids, "#161 missing from aggregate_findings"
        assert 162 in agg_ids, "#162 missing from aggregate_findings"


# ── Class 3: Mechanism ID Integrity ──────────────────────────────────


class TestMechanismIDIntegrity:
    """Global mechanism ID uniqueness and contiguity."""

    def test_no_duplicate_ids_globally(self, ccr):
        all_ids = []
        for section_val in ccr.values():
            if isinstance(section_val, dict):
                for val in section_val.values():
                    if isinstance(val, dict) and "mechanism_id" in val:
                        all_ids.append(val["mechanism_id"])
        dupes = [x for x in all_ids if all_ids.count(x) > 1]
        assert not dupes, f"Duplicate mechanism IDs: {set(dupes)}"

    def test_total_mechanism_count(self, ccr):
        all_ids = set()
        for section_val in ccr.values():
            if isinstance(section_val, dict):
                for val in section_val.values():
                    if isinstance(val, dict) and "mechanism_id" in val:
                        all_ids.add(val["mechanism_id"])
        assert len(all_ids) >= 155, f"Expected >= 155 total mechanisms, got {len(all_ids)}"

    def test_contiguity_excluding_known_gaps(self, ccr):
        all_ids = set()
        for section_val in ccr.values():
            if isinstance(section_val, dict):
                for val in section_val.values():
                    if isinstance(val, dict) and "mechanism_id" in val:
                        all_ids.add(val["mechanism_id"])
        KNOWN_GAPS = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,139}
        expected = set(range(17, max(all_ids)+1))
        missing = expected - all_ids - KNOWN_GAPS
        assert not missing, f"Missing mechanism IDs (not in known gaps): {sorted(missing)}"


# ── Class 4: Doc Sync Verification ───────────────────────────────────


class TestDocSyncVerification:
    """README and ARCHITECTURE counts match each other and disk."""

    def test_readme_table_body_agree(self, readme):
        table_match = re.search(r'\| Tests \| ~([\d,]+)', readme)
        body_match = re.search(r'\*\*(\d+) tests\*\*', readme)
        assert table_match and body_match, "README missing table or body test count"
        table_count = int(table_match.group(1).replace(',', ''))
        body_count = int(body_match.group(1))
        assert table_count == body_count, \
            f"README table ({table_count}) != body ({body_count})"

    def test_readme_file_count_matches_disk(self, readme, test_file_count):
        body_match = re.search(r'across (\d+) test files', readme)
        assert body_match, "README missing file count"
        claimed = int(body_match.group(1))
        assert claimed >= test_file_count - 1, \
            f"README claims {claimed} files, disk has {test_file_count} (drift > 1)"

    def test_readme_architecture_test_count_agree(self, readme, architecture):
        readme_match = re.search(r'\*\*(\d+) tests\*\*', readme)
        arch_match = re.search(r'(\d+) tests across', architecture)
        assert readme_match and arch_match
        assert readme_match.group(1) == arch_match.group(1), \
            f"README ({readme_match.group(1)}) != ARCHITECTURE ({arch_match.group(1)})"


# ── Class 5: Test File Existence ─────────────────────────────────────


class TestTestFileExistence:
    """Every mechanism #164-172 has a test file on disk."""

    EXPECTED_FILES = {
        164: "test_tomsguide_snap_specs_camera_count_paradox_privacy_vocabulary_inversion_aug18.py",
        165: "test_amanda_caswell_tomsguide_cross_entity_coverage_scope_asymmetry_aug18.py",
        166: "test_kali_hays_bbc_cross_entity_coverage_selection_natural_experiment_aug18.py",
        167: "test_conde_nast_google_zero_distribution_dependency_compound_incentive_aug18.py",
        168: "test_twit_1058_victoria_song_cross_medium_privacy_vocabulary_portability_aug18.py",
        169: "test_guardian_samsung_galaxy_glasses_london_geographic_proximity_privacy_parity_aug18.py",
        170: "test_gizmodo_openai_companion_surveillance_vocabulary_inversion_aug18.py",
        171: "test_daniel_bader_9to5google_career_ecosystem_capture_explicit_trust_differential_aug18.py",
        172: "test_openai_cpa_advertising_maturation_meta_displacement_publisher_compounding_aug18.py",
    }

    @pytest.mark.parametrize("mid,fname", list(EXPECTED_FILES.items()))
    def test_file_exists(self, mid, fname):
        path = os.path.join(TESTS_DIR, fname)
        assert os.path.exists(path), f"Test file for #{mid} not found: {fname}"


# ── Class 6: Asymmetry Score Distribution ────────────────────────────


class TestAsymmetryScoreDistribution:
    """Asymmetry scores for mechanisms #164-172 are within expected ranges."""

    def test_all_recent_have_scores(self, cpf):
        for mid in range(164, 173):
            if mid in (161, 162):  # in agg
                continue
            found = False
            for v in cpf.values():
                if isinstance(v, dict) and v.get("mechanism_id") == mid:
                    assert "asymmetry_score" in v, f"#{mid} missing asymmetry_score"
                    score = v["asymmetry_score"]
                    assert 0.5 <= score <= 0.95, f"#{mid} score {score} outside [0.5, 0.95]"
                    found = True
                    break
            assert found, f"Mechanism #{mid} not found in CPF"

    def test_mean_score_reasonable(self, cpf):
        scores = []
        for v in cpf.values():
            if isinstance(v, dict) and v.get("mechanism_id", 0) >= 164:
                if "asymmetry_score" in v:
                    scores.append(v["asymmetry_score"])
        assert len(scores) >= 8, f"Expected >= 8 scores for mechanisms >= 164, got {len(scores)}"
        mean = sum(scores) / len(scores)
        assert 0.65 <= mean <= 0.90, f"Mean score {mean:.2f} outside expected range [0.65, 0.90]"
