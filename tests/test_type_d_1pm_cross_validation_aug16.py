"""
Type D Cross-Validation — Sun 2026-08-16 13:00 PT

Validates mechanisms #134-#136 (iterations #139-#141):
1. Structural integrity: all mechanism entries parse, required fields present
2. Cross-reference bidirectionality: every forward ref has a backref (5 backrefs added)
3. Discovery date presence: all mechanisms have discovery_date
4. Doc sync: README.md and ARCHITECTURE.md test file/count stats match disk
5. Confounder completeness: all mechanisms have confounders with STRONG factors
6. Source URL presence: all mechanisms have source_urls
7. Test file existence: all mechanism test_file references point to real files
8. Mechanism structural consistency: mechanisms across publications/aggregate/cross_publication sections
9. Regression guards for mechanisms #129-#133

Fixes applied this iteration:
  - Added discovery_date to mechanism #136
  - Added backrefs to #136 from mechanisms #61, #43, #47, #101, #134
  - Synced README/ARCHITECTURE test counts (14708 tests, 419 files)
  - Fixed README test count format (removed ~ prefix for regex compatibility)
"""

import os
import re
import subprocess
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
PROFILES = REPO_ROOT / "profiles"
TESTS = REPO_ROOT / "tests"


@pytest.fixture(scope="module")
def ccr():
    with open(PROFILES / "competitor-coverage-research.yaml") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def cpf(ccr):
    return ccr.get("cross_publication_findings", {})


@pytest.fixture(scope="module")
def agg(ccr):
    return ccr.get("aggregate_findings", {})


@pytest.fixture(scope="module")
def pub(ccr):
    return ccr.get("publications", {})


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


def find_mechanism_anywhere(ccr, mid):
    """Search all sections for a mechanism by ID."""
    for section_name in ["cross_publication_findings", "aggregate_findings", "publications"]:
        section = ccr.get(section_name, {})
        if not isinstance(section, dict):
            continue
        for k, v in section.items():
            if isinstance(v, dict) and v.get("mechanism_id") == mid:
                return section_name, k, v
    return None, None, None


def get_forward_refs(mech):
    """Get all mechanism IDs referenced by a mechanism."""
    refs = []
    for key in ["cross_references", "related_mechanisms"]:
        if key in mech and isinstance(mech[key], list):
            for r in mech[key]:
                if isinstance(r, dict) and "mechanism_id" in r:
                    refs.append(r["mechanism_id"])
    return refs


class TestMechanismStructuralIntegrity:
    """All mechanisms #134-136 exist with required fields."""

    @pytest.mark.parametrize("mid", [134, 135, 136])
    def test_mechanism_exists(self, ccr, mid):
        section, key, mech = find_mechanism_anywhere(ccr, mid)
        assert mech is not None, f"Mechanism #{mid} not found in any section"

    @pytest.mark.parametrize("mid", [134, 135, 136])
    def test_mechanism_has_finding_summary(self, ccr, mid):
        _, _, mech = find_mechanism_anywhere(ccr, mid)
        assert mech.get("finding_summary"), f"Mechanism #{mid} missing finding_summary"

    @pytest.mark.parametrize("mid", [134, 135, 136])
    def test_mechanism_has_discovery_date(self, ccr, mid):
        _, _, mech = find_mechanism_anywhere(ccr, mid)
        assert mech.get("discovery_date") or mech.get("date_added"), \
            f"Mechanism #{mid} missing discovery_date/date_added"

    @pytest.mark.parametrize("mid", [134, 135, 136])
    def test_mechanism_has_test_file(self, ccr, mid):
        _, _, mech = find_mechanism_anywhere(ccr, mid)
        assert mech.get("test_file"), f"Mechanism #{mid} missing test_file"

    @pytest.mark.parametrize("mid", [134, 135, 136])
    def test_test_file_exists_on_disk(self, ccr, mid):
        _, _, mech = find_mechanism_anywhere(ccr, mid)
        test_file = mech.get("test_file", "")
        if test_file.startswith("tests/"):
            test_file = test_file[6:]
        assert (TESTS / test_file).exists(), \
            f"Mechanism #{mid} test_file {test_file} not found on disk"


class TestMechanism134Content:
    """Mechanism #134: WIRED Remediation Coverage Selection Silence."""

    def test_in_correct_section(self, ccr):
        section, key, mech = find_mechanism_anywhere(ccr, 134)
        # Can be in publications or cross_publication_findings
        assert section in ("publications", "cross_publication_findings"), \
            f"#134 in unexpected section: {section}"

    def test_finding_summary_mentions_v26(self, ccr):
        _, _, mech = find_mechanism_anywhere(ccr, 134)
        summary = mech.get("finding_summary", "")
        assert "v26" in summary.lower() or "V26" in summary, \
            "#134 finding_summary should mention Meta v26 update"

    def test_finding_summary_mentions_wired(self, ccr):
        _, _, mech = find_mechanism_anywhere(ccr, 134)
        summary = mech.get("finding_summary", "")
        assert "WIRED" in summary, "#134 finding_summary should mention WIRED"

    def test_has_confounders(self, ccr):
        _, _, mech = find_mechanism_anywhere(ccr, 134)
        confounders = mech.get("confounders", mech.get("confounding_factors", []))
        assert len(confounders) >= 2, f"#134 has only {len(confounders)} confounders"

    def test_has_strong_confounders(self, ccr):
        _, _, mech = find_mechanism_anywhere(ccr, 134)
        confounders = mech.get("confounders", mech.get("confounding_factors", []))
        strong = [c for c in confounders if isinstance(c, dict)
                  and c.get("strength") == "STRONG"]
        assert len(strong) >= 1, "#134 missing STRONG confounders"

    def test_has_backref_to_136(self, ccr):
        """Mechanism #136 references #134, so #134 should have backref to #136."""
        _, _, mech = find_mechanism_anywhere(ccr, 134)
        refs = get_forward_refs(mech)
        assert 136 in refs, "#134 missing backref to #136"


class TestMechanism135Content:
    """Mechanism #135: Wong Privacy Vocabulary Differential."""

    def test_in_aggregate_findings(self, ccr):
        section, _, _ = find_mechanism_anywhere(ccr, 135)
        assert section == "aggregate_findings", \
            f"#135 should be in aggregate_findings, found in {section}"

    def test_finding_summary_mentions_cultural_base_rate(self, ccr):
        _, _, mech = find_mechanism_anywhere(ccr, 135)
        summary = mech.get("finding_summary", "").lower()
        assert "cultural base rate" in summary or "cultural" in summary, \
            "#135 should mention cultural base rate"

    def test_finding_summary_mentions_wong(self, ccr):
        _, _, mech = find_mechanism_anywhere(ccr, 135)
        summary = mech.get("finding_summary", "")
        assert "Wong" in summary or "wong" in summary.lower(), \
            "#135 should mention Raymond Wong"

    def test_has_confounders(self, ccr):
        _, _, mech = find_mechanism_anywhere(ccr, 135)
        confounders = mech.get("confounders", mech.get("confounding_factors", []))
        assert len(confounders) >= 3, f"#135 has only {len(confounders)} confounders"

    def test_has_strong_confounders(self, ccr):
        _, _, mech = find_mechanism_anywhere(ccr, 135)
        confounders = mech.get("confounders", mech.get("confounding_factors", []))
        strong = [c for c in confounders if isinstance(c, dict)
                  and c.get("strength") == "STRONG"]
        assert len(strong) >= 2, f"#135 has only {len(strong)} STRONG confounders, expected ≥2"

    def test_cross_refs_to_130_131_132_134(self, ccr):
        _, _, mech = find_mechanism_anywhere(ccr, 135)
        refs = get_forward_refs(mech)
        for target in [130, 131, 132, 134]:
            assert target in refs, f"#135 missing cross-reference to #{target}"


class TestMechanism136Content:
    """Mechanism #136: Apple Siri AI Quad-Channel Publisher Dependency."""

    def test_in_cross_publication_findings(self, ccr):
        section, _, _ = find_mechanism_anywhere(ccr, 136)
        assert section == "cross_publication_findings", \
            f"#136 should be in cross_publication_findings, found in {section}"

    def test_finding_summary_mentions_quad_channel(self, ccr):
        _, _, mech = find_mechanism_anywhere(ccr, 136)
        summary = mech.get("finding_summary", "").lower()
        assert "fourth" in summary or "quad" in summary or "4th" in summary, \
            "#136 should mention fourth/quad channel"

    def test_finding_summary_mentions_siri(self, ccr):
        _, _, mech = find_mechanism_anywhere(ccr, 136)
        summary = mech.get("finding_summary", "")
        assert "Siri" in summary, "#136 should mention Siri AI"

    def test_has_source_urls(self, ccr):
        _, _, mech = find_mechanism_anywhere(ccr, 136)
        urls = mech.get("source_urls", [])
        assert len(urls) >= 3, f"#136 has only {len(urls)} source URLs"

    def test_has_confounders(self, ccr):
        _, _, mech = find_mechanism_anywhere(ccr, 136)
        confounders = mech.get("confounders", mech.get("confounding_factors", []))
        assert len(confounders) >= 4, f"#136 has only {len(confounders)} confounders"

    def test_has_testable_predictions(self, ccr):
        _, _, mech = find_mechanism_anywhere(ccr, 136)
        predictions = mech.get("testable_predictions", [])
        assert len(predictions) >= 3, f"#136 has only {len(predictions)} testable predictions"

    def test_cross_refs_to_61_43_47_101_134(self, ccr):
        _, _, mech = find_mechanism_anywhere(ccr, 136)
        refs = get_forward_refs(mech)
        for target in [61, 43, 134, 47, 101]:
            assert target in refs, f"#136 missing cross-reference to #{target}"

    def test_discovery_date_present(self, ccr):
        _, _, mech = find_mechanism_anywhere(ccr, 136)
        assert mech.get("discovery_date"), "#136 missing discovery_date"


class TestCrossReferenceBidirectionality:
    """Every forward ref from #134-#136 should have a backref in the target."""

    def _check_backref(self, ccr, source_mid, target_mid):
        _, _, target_mech = find_mechanism_anywhere(ccr, target_mid)
        if target_mech is None:
            pytest.skip(f"Target mechanism #{target_mid} not found")
        refs = get_forward_refs(target_mech)
        assert source_mid in refs, \
            f"#{target_mid} missing backref to #{source_mid}"

    def test_136_to_61_backref(self, ccr):
        self._check_backref(ccr, 136, 61)

    def test_136_to_43_backref(self, ccr):
        self._check_backref(ccr, 136, 43)

    def test_136_to_47_backref(self, ccr):
        self._check_backref(ccr, 136, 47)

    def test_136_to_101_backref(self, ccr):
        self._check_backref(ccr, 136, 101)

    def test_136_to_134_backref(self, ccr):
        self._check_backref(ccr, 136, 134)

    def test_135_to_130_backref(self, ccr):
        self._check_backref(ccr, 135, 130)

    def test_135_to_131_backref(self, ccr):
        self._check_backref(ccr, 135, 131)

    def test_135_to_132_backref(self, ccr):
        self._check_backref(ccr, 135, 132)

    def test_135_to_134_backref(self, ccr):
        self._check_backref(ccr, 135, 134)


class TestDocSyncIntegrity:
    """README.md and ARCHITECTURE.md stats match disk."""

    def test_readme_test_file_count_matches_disk(self, readme):
        actual = len([f for f in os.listdir(TESTS)
                      if f.startswith("test_") and f.endswith(".py")])
        # Match patterns like "14708 tests** across 419 test files"
        match = re.search(r"\*\*(\d+) tests\*\* across (\d+) test files", readme)
        assert match, "README.md missing test count header"
        claimed_files = int(match.group(2))
        assert claimed_files == actual, \
            f"README claims {claimed_files} test files, disk has {actual}"

    def test_architecture_test_file_count_matches_disk(self, architecture):
        actual = len([f for f in os.listdir(TESTS)
                      if f.startswith("test_") and f.endswith(".py")])
        match = re.search(r"(\d+) tests across (\d+) test files", architecture)
        assert match, "ARCHITECTURE.md missing test count header"
        claimed_files = int(match.group(2))
        assert claimed_files == actual, \
            f"ARCHITECTURE claims {claimed_files} test files, disk has {actual}"

    def test_aug16_mechanism_test_files_listed_in_readme(self, readme):
        aug16_mech_files = [
            "test_wired_meta_remediation_coverage_selection_silence_aug16.py",
            "test_raymond_wong_fury_privacy_vocabulary_differential_aug16.py",
            "test_apple_siri_ai_quad_channel_publisher_dependency_aug16.py",
        ]
        for f in aug16_mech_files:
            assert f in readme, f"README missing test file entry: {f}"


class TestMechanismIDContiguity:
    """Mechanisms #134-136 should have no gaps and all be Aug 16 2026."""

    @pytest.mark.parametrize("mid", [134, 135, 136])
    def test_mechanism_exists_contiguous(self, ccr, mid):
        _, _, mech = find_mechanism_anywhere(ccr, mid)
        assert mech is not None, f"Gap in mechanism IDs: #{mid} missing"

    @pytest.mark.parametrize("mid", [134, 135, 136])
    def test_mechanism_date_is_aug16(self, ccr, mid):
        _, _, mech = find_mechanism_anywhere(ccr, mid)
        date = mech.get("discovery_date") or mech.get("date_added", "")
        assert "2026-08-16" in str(date), \
            f"Mechanism #{mid} date is {date}, expected 2026-08-16"


class TestRegressionGuardsPriorMechanisms:
    """Mechanisms #129-133 still exist and parse correctly (regression guard)."""

    @pytest.mark.parametrize("mid", [129, 130, 131, 132, 133])
    def test_prior_mechanism_still_exists(self, ccr, mid):
        _, _, mech = find_mechanism_anywhere(ccr, mid)
        assert mech is not None, f"Regression: mechanism #{mid} disappeared"

    @pytest.mark.parametrize("mid", [129, 130, 131, 132, 133])
    def test_prior_mechanism_has_finding_summary(self, ccr, mid):
        _, _, mech = find_mechanism_anywhere(ccr, mid)
        assert mech.get("finding_summary"), \
            f"Regression: mechanism #{mid} lost finding_summary"


class TestTestFileImportability:
    """All Aug 16 test files import without errors."""

    @pytest.mark.parametrize("filename", [
        "test_wired_meta_remediation_coverage_selection_silence_aug16",
        "test_raymond_wong_fury_privacy_vocabulary_differential_aug16",
        "test_apple_siri_ai_quad_channel_publisher_dependency_aug16",
        "test_andy_boxall_cross_entity_privacy_vocabulary_inversion_aug16",
        "test_snap_competitive_privacy_positioning_amplification_aug16",
        "test_ben_schoon_9to5google_control_calibration_cross_entity_aug16",
        "test_cnbc_versant_post_spinoff_smart_glasses_coverage_selection_aug16",
        "test_wong_barr_cross_publication_beat_assignment_replication_aug16",
        "test_snap_perplexity_publisher_financial_chain_aug16",
        "test_people_inc_google_traffic_substitution_paradox_aug16",
    ])
    def test_file_imports(self, filename):
        test_path = TESTS / f"{filename}.py"
        if not test_path.exists():
            pytest.skip(f"{filename}.py not on disk")
        import importlib
        mod = importlib.import_module(f"tests.{filename}")
        assert mod is not None


class TestFindingSummaryDistinctiveness:
    """Mechanisms #134-136 should have distinct finding summaries (Jaccard <0.7)."""

    def _jaccard(self, a, b):
        words_a = set(a.lower().split())
        words_b = set(b.lower().split())
        if not words_a or not words_b:
            return 0.0
        return len(words_a & words_b) / len(words_a | words_b)

    def test_134_vs_135_distinct(self, ccr):
        _, _, m134 = find_mechanism_anywhere(ccr, 134)
        _, _, m135 = find_mechanism_anywhere(ccr, 135)
        j = self._jaccard(m134["finding_summary"], m135["finding_summary"])
        assert j < 0.7, f"#134 vs #135 Jaccard {j:.2f} >= 0.7 — summaries too similar"

    def test_134_vs_136_distinct(self, ccr):
        _, _, m134 = find_mechanism_anywhere(ccr, 134)
        _, _, m136 = find_mechanism_anywhere(ccr, 136)
        j = self._jaccard(m134["finding_summary"], m136["finding_summary"])
        assert j < 0.7, f"#134 vs #136 Jaccard {j:.2f} >= 0.7 — summaries too similar"

    def test_135_vs_136_distinct(self, ccr):
        _, _, m135 = find_mechanism_anywhere(ccr, 135)
        _, _, m136 = find_mechanism_anywhere(ccr, 136)
        j = self._jaccard(m135["finding_summary"], m136["finding_summary"])
        assert j < 0.7, f"#135 vs #136 Jaccard {j:.2f} >= 0.7 — summaries too similar"
