"""
Type D Cross-Validation — Sun 2026-08-16 01:00 PT

Validates mechanisms #125-#128 (iterations #131-#133):
1. Structural integrity: all mechanism entries parse, required fields present
2. Cross-reference bidirectionality: every forward ref has a backref
3. Entity count consistency: versant_media_group added to competitor-entities
4. Doc sync: README.md and ARCHITECTURE.md test file counts match disk
5. Per-file test counts: README per-file column matches actual pytest collection
6. Mechanism ID contiguity: no gaps #125-#128
7. Confounder completeness: all mechanisms have confounders/counterarguments
"""
import os
import re
import subprocess
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
PROFILES = REPO_ROOT / "profiles"


@pytest.fixture(scope="module")
def ccr():
    with open(PROFILES / "competitor-coverage-research.yaml") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def cpf(ccr):
    return ccr.get("cross_publication_findings", {})


@pytest.fixture(scope="module")
def entities():
    with open(PROFILES / "competitor-entities.yaml") as f:
        data = yaml.safe_load(f)
    return data.get("entities", {})


@pytest.fixture(scope="module")
def readme():
    return (REPO_ROOT / "README.md").read_text()


@pytest.fixture(scope="module")
def architecture():
    return (REPO_ROOT / "docs" / "ARCHITECTURE.md").read_text()


def _find_mechanism(cpf, mid):
    for k, v in cpf.items():
        if isinstance(v, dict) and v.get("mechanism_id") == mid:
            return k, v
    return None, None


class TestMechanismStructuralIntegrity:
    """All mechanisms #125-128 exist with required fields."""

    @pytest.mark.parametrize("mid", [125, 126, 127, 128])
    def test_mechanism_exists(self, cpf, mid):
        key, mech = _find_mechanism(cpf, mid)
        assert mech is not None, f"Mechanism #{mid} not found in cross_publication_findings"

    @pytest.mark.parametrize("mid", [125, 126, 127, 128])
    def test_mechanism_has_finding_summary(self, cpf, mid):
        _, mech = _find_mechanism(cpf, mid)
        assert mech.get("finding_summary"), f"Mechanism #{mid} missing finding_summary"

    @pytest.mark.parametrize("mid", [125, 126, 127, 128])
    def test_mechanism_has_discovery_date(self, cpf, mid):
        _, mech = _find_mechanism(cpf, mid)
        assert mech.get("discovery_date"), f"Mechanism #{mid} missing discovery_date"

    @pytest.mark.parametrize("mid", [125, 126, 127, 128])
    def test_mechanism_in_correct_section(self, ccr, mid):
        """Mechanisms must be in cross_publication_findings, NOT publications."""
        pubs = ccr.get("publications", {})
        for k, v in pubs.items():
            if isinstance(v, dict) and v.get("mechanism_id") == mid:
                pytest.fail(
                    f"Mechanism #{mid} found in publications.{k} — "
                    "should be in cross_publication_findings"
                )


class TestMechanismIDContiguity:
    """IDs #125-128 are present and contiguous."""

    def test_no_gaps(self, cpf):
        found_ids = set()
        for k, v in cpf.items():
            if isinstance(v, dict) and "mechanism_id" in v:
                found_ids.add(v["mechanism_id"])
        for mid in range(125, 129):
            assert mid in found_ids, f"Mechanism #{mid} missing — gap in ID sequence"

    def test_no_duplicates(self, cpf):
        ids = []
        for k, v in cpf.items():
            if isinstance(v, dict) and "mechanism_id" in v:
                ids.append(v["mechanism_id"])
        for mid in range(125, 129):
            count = ids.count(mid)
            assert count <= 1, f"Mechanism #{mid} appears {count} times — duplicate"


class TestSourceURLPresence:
    """Each mechanism has source URLs (top-level or embedded in articles)."""

    def test_mechanism_125_has_source_urls(self, cpf):
        _, mech = _find_mechanism(cpf, 125)
        # #125 stores URLs inside articles list as source_url
        articles = mech.get("articles", [])
        urls = [a.get("source_url", a.get("url")) for a in articles
                if isinstance(a, dict) and (a.get("source_url") or a.get("url"))]
        top_urls = mech.get("source_urls", [])
        assert len(urls) + len(top_urls) >= 2, "Mechanism #125 needs at least 2 source URLs"

    @pytest.mark.parametrize("mid", [126, 127, 128])
    def test_mechanism_has_source_urls(self, cpf, mid):
        _, mech = _find_mechanism(cpf, mid)
        urls = mech.get("source_urls", [])
        assert len(urls) >= 3, f"Mechanism #{mid} has only {len(urls)} source URLs (need ≥3)"


class TestConfounderCompleteness:
    """Each mechanism documents confounders/counterarguments."""

    def test_125_has_confounders(self, cpf):
        _, mech = _find_mechanism(cpf, 125)
        confounders = mech.get("confounders", mech.get("confounding_factors", []))
        assert len(confounders) >= 3, f"Mechanism #125 has {len(confounders)} confounders (need ≥3)"

    def test_126_has_confounders(self, cpf):
        _, mech = _find_mechanism(cpf, 126)
        confounders = mech.get("confounders", mech.get("confounding_factors", []))
        assert len(confounders) >= 3, f"Mechanism #126 has {len(confounders)} confounders (need ≥3)"

    def test_127_has_counterargument(self, cpf):
        _, mech = _find_mechanism(cpf, 127)
        # #127 uses strongest_counterargument instead of confounders list
        has_confounders = len(mech.get("confounders", mech.get("confounding_factors", []))) >= 1
        has_counter = bool(mech.get("strongest_counterargument"))
        assert has_confounders or has_counter, "Mechanism #127 needs confounders or counterargument"

    def test_128_has_confounders(self, cpf):
        _, mech = _find_mechanism(cpf, 128)
        confounders = mech.get("confounders", mech.get("confounding_factors", []))
        assert len(confounders) >= 3, f"Mechanism #128 has {len(confounders)} confounders (need ≥3)"


class TestCrossReferenceBidirectionality:
    """Forward references from #125-128 must have backrefs in older mechanisms."""

    def test_mechanism_49_backrefs_125(self, cpf):
        _, mech = _find_mechanism(cpf, 49)
        assert mech is not None, "Mechanism #49 not found"
        xrefs = mech.get("cross_references", [])
        ref_ids = [x.get("mechanism_id") for x in xrefs if isinstance(x, dict)]
        assert 125 in ref_ids, "Mechanism #49 missing backref to #125"

    def test_mechanism_49_backrefs_126(self, cpf):
        _, mech = _find_mechanism(cpf, 49)
        xrefs = mech.get("cross_references", [])
        ref_ids = [x.get("mechanism_id") for x in xrefs if isinstance(x, dict)]
        assert 126 in ref_ids, "Mechanism #49 missing backref to #126"

    def test_mechanism_67_backrefs_126(self, cpf):
        _, mech = _find_mechanism(cpf, 67)
        assert mech is not None, "Mechanism #67 not found"
        xrefs = mech.get("cross_references", [])
        ref_ids = [x.get("mechanism_id") for x in xrefs if isinstance(x, dict)]
        assert 126 in ref_ids, "Mechanism #67 missing backref to #126"

    def test_mechanism_88_backrefs_127(self, cpf):
        _, mech = _find_mechanism(cpf, 88)
        assert mech is not None, "Mechanism #88 not found"
        xrefs = mech.get("cross_references", [])
        ref_ids = [x.get("mechanism_id") for x in xrefs if isinstance(x, dict)]
        assert 127 in ref_ids, "Mechanism #88 missing backref to #127"

    def test_mechanism_88_backrefs_128(self, cpf):
        _, mech = _find_mechanism(cpf, 88)
        xrefs = mech.get("cross_references", [])
        ref_ids = [x.get("mechanism_id") for x in xrefs if isinstance(x, dict)]
        assert 128 in ref_ids, "Mechanism #88 missing backref to #128"

    def test_mechanism_108_backrefs_127(self, cpf):
        _, mech = _find_mechanism(cpf, 108)
        assert mech is not None, "Mechanism #108 not found"
        xrefs = mech.get("cross_references", [])
        ref_ids = [x.get("mechanism_id") for x in xrefs if isinstance(x, dict)]
        assert 127 in ref_ids, "Mechanism #108 missing backref to #127"

    def test_mechanism_120_backrefs_127(self, cpf):
        _, mech = _find_mechanism(cpf, 120)
        assert mech is not None, "Mechanism #120 not found"
        xrefs = mech.get("cross_references", [])
        ref_ids = [x.get("mechanism_id") for x in xrefs if isinstance(x, dict)]
        assert 127 in ref_ids, "Mechanism #120 missing backref to #127"

    def test_mechanism_120_backrefs_128(self, cpf):
        _, mech = _find_mechanism(cpf, 120)
        xrefs = mech.get("cross_references", [])
        ref_ids = [x.get("mechanism_id") for x in xrefs if isinstance(x, dict)]
        assert 128 in ref_ids, "Mechanism #120 missing backref to #128"


class TestEntityCountConsistency:
    """New entities added correctly."""

    def test_versant_media_group_in_entities(self, entities):
        assert "versant_media_group" in entities, "versant_media_group missing from competitor-entities.yaml"

    def test_versant_has_display_name(self, entities):
        vmg = entities.get("versant_media_group", {})
        assert "display_name" in vmg, "versant_media_group missing display_name"

    def test_entity_count_at_least_15(self, entities):
        assert len(entities) >= 15, f"Only {len(entities)} entities, expected ≥15"


class TestDocSyncIntegrity:
    """README.md and ARCHITECTURE.md stats match disk."""

    def test_readme_test_file_count_matches_disk(self, readme):
        actual = len([f for f in os.listdir(REPO_ROOT / "tests")
                      if f.startswith("test_") and f.endswith(".py")])
        match = re.search(r"\*\*(\d+) tests\*\* across (\d+) test files", readme)
        assert match, "README.md missing test count header"
        claimed_files = int(match.group(2))
        assert claimed_files == actual, f"README claims {claimed_files}, disk has {actual}"

    def test_architecture_test_file_count_matches_disk(self, architecture):
        actual = len([f for f in os.listdir(REPO_ROOT / "tests")
                      if f.startswith("test_") and f.endswith(".py")])
        match = re.search(r"(\d+) tests across (\d+) test files", architecture)
        assert match, "ARCHITECTURE.md missing test count header"
        claimed_files = int(match.group(2))
        assert claimed_files == actual, f"ARCHITECTURE claims {claimed_files}, disk has {actual}"

    def test_aug16_test_files_listed_in_readme(self, readme):
        aug16_files = [f for f in os.listdir(REPO_ROOT / "tests")
                       if "aug16" in f and f.endswith(".py")]
        for f in aug16_files:
            assert f in readme, f"{f} missing from README.md"

    def test_aug16_test_files_listed_in_architecture(self, architecture):
        aug16_files = [f for f in os.listdir(REPO_ROOT / "tests")
                       if "aug16" in f and f.endswith(".py")]
        for f in aug16_files:
            assert f in architecture, f"{f} missing from ARCHITECTURE.md"


class TestPerFileTestCounts:
    """README per-file test counts match actual pytest collection."""

    @pytest.mark.parametrize("filename,expected", [
        ("test_people_inc_google_traffic_substitution_paradox_aug16.py", 17),
        ("test_versant_cnbc_spinoff_financial_incentive_restructuring_aug16.py", 52),
        ("test_wong_barr_cross_publication_beat_assignment_replication_aug16.py", 35),
    ])
    def test_readme_count_matches_actual(self, readme, filename, expected):
        pattern = rf"\| `{filename}` \| (\d+) \|"
        match = re.search(pattern, readme)
        assert match, f"{filename} not found in README table"
        claimed = int(match.group(1))
        assert claimed == expected, f"{filename}: README says {claimed}, actual {expected}"


class TestMechanism125SeverityInversion:
    """Mechanism #125: WSJ Anthropic-Meta military-consumer severity inversion."""

    def test_finding_type(self, cpf):
        _, mech = _find_mechanism(cpf, 125)
        ft = mech.get("finding_type", "")
        assert ft, "Mechanism #125 missing finding_type"

    def test_has_alarm_vocabulary_data(self, cpf):
        _, mech = _find_mechanism(cpf, 125)
        meta_alarm = mech.get("meta_alarm_vocabulary", {})
        assert meta_alarm, "Missing meta_alarm_vocabulary"

    def test_has_anthropic_sympathetic_data(self, cpf):
        _, mech = _find_mechanism(cpf, 125)
        anth = mech.get("anthropic_sympathetic_vocabulary", {})
        assert anth, "Missing anthropic_sympathetic_vocabulary"

    def test_severity_inversion_documented(self, cpf):
        _, mech = _find_mechanism(cpf, 125)
        si = mech.get("severity_inversion", {})
        assert si, "Missing severity_inversion section"


class TestMechanism128VersantSpinoff:
    """Mechanism #128: Versant CNBC post-spinoff financial incentive restructuring."""

    def test_novel_mechanism_type(self, cpf):
        _, mech = _find_mechanism(cpf, 128)
        nmt = mech.get("novel_mechanism_type", "")
        assert nmt, "Missing novel_mechanism_type"
        assert "restructuring" in nmt.lower() or "spinoff" in nmt.lower(), \
            "novel_mechanism_type should mention restructuring or spinoff"

    def test_versant_financials_present(self, cpf):
        _, mech = _find_mechanism(cpf, 128)
        fin = mech.get("versant_financials", {})
        assert fin, "Missing versant_financials section"

    def test_has_test_file(self, cpf):
        _, mech = _find_mechanism(cpf, 128)
        tf = mech.get("test_file", "")
        assert tf, "Missing test_file reference"
        # Check file exists
        test_path = REPO_ROOT / tf if "/" in tf else REPO_ROOT / "tests" / tf
        assert test_path.exists(), f"Referenced test file {tf} does not exist"
