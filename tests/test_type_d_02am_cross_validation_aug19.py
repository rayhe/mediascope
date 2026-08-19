"""
Type D cross-validation — Aug 19 2026, 02:00 AM PT

Validates:
1. Doc sync fix: README table/body/ARCHITECTURE test counts agree
2. Mechanism #174 (OpenAI zero-ad-revenue-share) structural integrity
3. Section placement: no mechanisms in publications section
4. Mechanism ID contiguity (known gaps only)
5. Aug 19 test file existence and registration
6. Publication section cleanliness post iteration #173 fix
"""

import os
import re

import pytest
import yaml


REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES = os.path.join(REPO, "profiles")
TESTS = os.path.join(REPO, "tests")


@pytest.fixture(scope="module")
def readme():
    with open(os.path.join(REPO, "README.md")) as f:
        return f.read()


@pytest.fixture(scope="module")
def architecture():
    with open(os.path.join(REPO, "docs", "ARCHITECTURE.md")) as f:
        return f.read()


@pytest.fixture(scope="module")
def ccr():
    with open(os.path.join(PROFILES, "competitor-coverage-research.yaml")) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def test_file_count():
    return len([f for f in os.listdir(TESTS) if f.startswith("test_") and f.endswith(".py")])


# ── Class 1: Doc Sync Verification ──────────────────────────────────


class TestDocSyncAfterIteration174:
    """README table, body, and ARCHITECTURE must agree after doc sync fix."""

    def test_readme_table_has_count(self, readme):
        match = re.search(r"\| Tests \| ~([\d,]+)", readme)
        assert match, "README missing table test count"

    def test_readme_body_has_count(self, readme):
        match = re.search(r"\*\*(\d+) tests\*\*", readme)
        assert match, "README missing body test count"

    def test_readme_table_body_agree(self, readme):
        table_match = re.search(r"\| Tests \| ~([\d,]+)", readme)
        body_match = re.search(r"\*\*(\d+) tests\*\*", readme)
        assert table_match and body_match
        table_count = int(table_match.group(1).replace(",", ""))
        body_count = int(body_match.group(1))
        assert table_count == body_count, \
            f"README table ({table_count}) != body ({body_count})"

    def test_readme_body_file_count_matches_disk(self, readme, test_file_count):
        match = re.search(r"across (\d+) test files", readme)
        assert match, "README missing file count"
        claimed = int(match.group(1))
        assert claimed >= test_file_count - 1, \
            f"README claims {claimed} files, disk has {test_file_count}"

    def test_readme_architecture_test_count_agree(self, readme, architecture):
        readme_match = re.search(r"\*\*(\d+) tests\*\*", readme)
        arch_match = re.search(r"(\d+) tests across", architecture)
        assert readme_match and arch_match, "Missing test count in README body or ARCHITECTURE"
        assert readme_match.group(1) == arch_match.group(1), \
            f"README ({readme_match.group(1)}) != ARCHITECTURE ({arch_match.group(1)})"

    def test_architecture_file_count_matches_disk(self, architecture, test_file_count):
        match = re.search(r"tests across (\d+) test files", architecture)
        assert match, "ARCHITECTURE missing file count"
        claimed = int(match.group(1))
        assert claimed >= test_file_count - 1, \
            f"ARCHITECTURE claims {claimed} files, disk has {test_file_count}"


# ── Class 2: Mechanism 174 Structural Integrity ─────────────────────


class TestMechanism174Structure:
    """Mechanism #174 (OpenAI zero-ad-revenue-share) must have all required fields."""

    @pytest.fixture
    def m174(self, ccr):
        cpf = ccr["cross_publication_findings"]
        for key, val in cpf.items():
            if isinstance(val, dict) and val.get("mechanism_id") == 174:
                return val
        pytest.fail("Mechanism 174 not found in cross_publication_findings")

    def test_mechanism_name(self, m174):
        assert "zero" in m174.get("mechanism_name", "").lower() or \
               "revenue" in m174.get("mechanism_name", "").lower()

    def test_mechanism_has_score(self, m174):
        score = m174.get("asymmetry_score", 0)
        assert 0.5 <= score <= 1.0, f"Score {score} out of expected range"

    def test_mechanism_has_entities(self, m174):
        entities = m174.get("entities_involved", [])
        assert len(entities) >= 3, f"Expected 3+ entities, got {len(entities)}"
        entity_str = " ".join(str(e) for e in entities).lower()
        assert "openai" in entity_str

    def test_mechanism_has_source_urls(self, m174):
        urls = m174.get("source_urls", [])
        assert len(urls) >= 2, f"Expected 2+ source URLs, got {len(urls)}"

    def test_mechanism_has_cross_references(self, m174):
        xrefs = m174.get("cross_references", [])
        assert len(xrefs) >= 1, "Expected cross-references"

    def test_mechanism_has_test_file(self, m174):
        tf = m174.get("test_file", "")
        assert "aug19" in tf, f"Expected aug19 test file, got {tf}"

    def test_mechanism_type_financial(self, m174):
        mtype = m174.get("mechanism_type", "")
        assert "financial" in mtype.lower() or "captivity" in mtype.lower(), \
            f"Expected financial-related type, got {mtype}"

    def test_shetty_evidence_present(self, m174):
        evidence = m174.get("primary_evidence", {})
        assert "shetty" in str(evidence).lower(), \
            "Expected Varun Shetty evidence in primary_evidence"

    def test_confounding_factors_present(self, m174):
        cfs = m174.get("confounding_factors", [])
        assert len(cfs) >= 3, f"Expected 3+ confounders, got {len(cfs)}"


# ── Class 3: Section Placement Guard ────────────────────────────────


class TestSectionPlacementGuard:
    """No mechanism entries should exist in the publications section."""

    def test_publications_have_no_mechanisms(self, ccr):
        pubs = ccr.get("publications", {})
        violations = []
        for pub_name, pub_data in pubs.items():
            if isinstance(pub_data, dict) and "mechanism_id" in pub_data:
                violations.append(f"{pub_name} (id={pub_data['mechanism_id']})")
        assert not violations, \
            f"Mechanisms in publications section: {violations}"

    def test_cpf_has_at_least_145_mechanisms(self, ccr):
        cpf = ccr.get("cross_publication_findings", {})
        count = sum(
            1 for val in cpf.values()
            if isinstance(val, dict) and "mechanism_id" in val
        )
        assert count >= 145, f"CPF has only {count} mechanisms, expected 145+"

    def test_aggregate_findings_mechanism_ids_valid(self, ccr):
        agg = ccr.get("aggregate_findings", {})
        for key, val in agg.items():
            if isinstance(val, dict) and "mechanism_id" in val:
                mid = val["mechanism_id"]
                assert isinstance(mid, int), f"{key} has non-int mechanism_id"
                assert mid >= 17, f"{key} has suspiciously low mechanism_id {mid}"


# ── Class 4: Mechanism ID Contiguity ────────────────────────────────


class TestMechanismIDContiguity:
    """All mechanism IDs from 17 to max should be present, except known gaps."""

    KNOWN_GAPS = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 139}

    def test_contiguity(self, ccr):
        all_ids = set()
        for section_val in ccr.values():
            if isinstance(section_val, dict):
                for val in section_val.values():
                    if isinstance(val, dict) and "mechanism_id" in val:
                        all_ids.add(val["mechanism_id"])
        expected = set(range(17, max(all_ids) + 1))
        missing = expected - all_ids - self.KNOWN_GAPS
        assert not missing, \
            f"Missing mechanism IDs: {sorted(missing)}"

    def test_max_id_at_least_174(self, ccr):
        all_ids = set()
        for section_val in ccr.values():
            if isinstance(section_val, dict):
                for val in section_val.values():
                    if isinstance(val, dict) and "mechanism_id" in val:
                        all_ids.add(val["mechanism_id"])
        assert max(all_ids) >= 174, \
            f"Max mechanism ID is {max(all_ids)}, expected >= 174"

    def test_no_duplicate_ids(self, ccr):
        all_ids = []
        for section_val in ccr.values():
            if isinstance(section_val, dict):
                for val in section_val.values():
                    if isinstance(val, dict) and "mechanism_id" in val:
                        all_ids.append(val["mechanism_id"])
        duplicates = [x for x in set(all_ids) if all_ids.count(x) > 1]
        assert not duplicates, f"Duplicate mechanism IDs: {duplicates}"


# ── Class 5: Aug 19 Test File Verification ──────────────────────────


class TestAug19TestFiles:
    """Verify test files added in aug19 iterations exist and are registered."""

    AUG19_FILES = [
        "test_openai_zero_ad_revenue_share_publisher_financial_captivity_aug19.py",
        "test_type_d_02am_cross_validation_aug19.py",
    ]

    @pytest.mark.parametrize("filename", AUG19_FILES)
    def test_file_exists(self, filename):
        path = os.path.join(TESTS, filename)
        assert os.path.exists(path), f"{filename} missing from tests/"

    def test_mechanism_174_test_file_in_readme(self, readme):
        fname = "test_openai_zero_ad_revenue_share_publisher_financial_captivity_aug19.py"
        assert fname in readme, f"{fname} not in README"

    def test_mechanism_174_test_file_in_architecture(self, architecture):
        fname = "test_openai_zero_ad_revenue_share_publisher_financial_captivity_aug19.py"
        assert fname in architecture, f"{fname} not in ARCHITECTURE"


# ── Class 6: Asymmetry Score Distribution ───────────────────────────


class TestAsymmetryScoreDistribution:
    """Recent mechanisms should have scores in the expected range."""

    def test_recent_mechanisms_have_scores(self, ccr):
        cpf = ccr.get("cross_publication_findings", {})
        recent = []
        for key, val in cpf.items():
            if isinstance(val, dict) and val.get("mechanism_id", 0) >= 170:
                score = val.get("asymmetry_score")
                if score is None:
                    recent.append(f"#{val['mechanism_id']} missing score")
                elif not (0.5 <= score <= 1.0):
                    recent.append(f"#{val['mechanism_id']} score={score}")
        assert not recent, f"Score issues: {recent}"

    def test_mean_score_reasonable(self, ccr):
        cpf = ccr.get("cross_publication_findings", {})
        scores = [
            val["asymmetry_score"]
            for val in cpf.values()
            if isinstance(val, dict) and "asymmetry_score" in val
        ]
        assert scores, "No asymmetry scores found"
        mean = sum(scores) / len(scores)
        assert 0.55 <= mean <= 0.95, \
            f"Mean asymmetry score {mean:.3f} outside expected range"
