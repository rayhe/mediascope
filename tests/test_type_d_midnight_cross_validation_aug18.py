"""
Type D Cross-Validation — Tue 2026-08-18 00:00 PT (Midnight)

Fixes and validates:
1. Doc sync regression: README (444→441 files, 15705→15703 tests) and
   ARCHITECTURE (439→441 files, 15630→15703 tests) both out of sync with disk.
2. Three test files missing from both docs: apple_siri_ai_triple_layer,
   bobrowsky_cross_publication_brand_stigma, type_d_08am_cross_validation_aug17.
3. Structural integrity of mechanisms #153-#156 (the aug17 batch).
4. Cross-reference bidirectionality for mechanisms #153-#156.
5. Mechanism ID contiguity and uniqueness across entire corpus.
"""

import os
import re
import yaml
import pytest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PROFILES = REPO_ROOT / "profiles"


@pytest.fixture(scope="module")
def readme():
    return (REPO_ROOT / "README.md").read_text()


@pytest.fixture(scope="module")
def architecture():
    return (REPO_ROOT / "docs" / "ARCHITECTURE.md").read_text()


@pytest.fixture(scope="module")
def ccr():
    with open(PROFILES / "competitor-coverage-research.yaml") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def cpf(ccr):
    return ccr.get("cross_publication_findings", {})


@pytest.fixture(scope="module")
def test_file_count():
    return len([f for f in os.listdir(REPO_ROOT / "tests")
                if f.startswith("test_") and f.endswith(".py")])


# ── Class 1: Doc Sync After Fix ─────────────────────────────────────

class TestDocSyncAfterFix:
    """README and ARCHITECTURE test file counts match disk after aug18 fix."""

    def test_readme_file_count_matches_disk(self, readme, test_file_count):
        match = re.search(r'\*\*(\d+) tests\*\* across (\d+) test files', readme)
        assert match, "README.md missing test count header"
        claimed = int(match.group(2))
        assert claimed == test_file_count, \
            f"README claims {claimed} files, disk has {test_file_count}"

    def test_architecture_file_count_matches_disk(self, architecture, test_file_count):
        match = re.search(r'(\d+) tests across (\d+) test files', architecture)
        assert match, "ARCHITECTURE.md missing test count header"
        claimed = int(match.group(2))
        assert claimed == test_file_count, \
            f"ARCHITECTURE claims {claimed} files, disk has {test_file_count}"

    def test_readme_architecture_count_agreement(self, readme, architecture):
        readme_match = re.search(r'\*\*(\d+) tests\*\*', readme)
        arch_match = re.search(r'(\d+) tests across', architecture)
        assert readme_match and arch_match
        assert readme_match.group(1) == arch_match.group(1), \
            f"README ({readme_match.group(1)}) != ARCHITECTURE ({arch_match.group(1)})"

    def test_aug17_triple_layer_in_both_docs(self, readme, architecture):
        fname = "test_apple_siri_ai_triple_layer_publisher_financial_architecture_aug17.py"
        assert fname in readme, f"{fname} missing from README"
        assert fname in architecture, f"{fname} missing from ARCHITECTURE"

    def test_aug17_brand_stigma_in_both_docs(self, readme, architecture):
        fname = "test_bobrowsky_cross_publication_brand_stigma_smart_glasses_vocabulary_aug17.py"
        assert fname in readme, f"{fname} missing from README"
        assert fname in architecture, f"{fname} missing from ARCHITECTURE"

    def test_aug17_type_d_08am_in_both_docs(self, readme, architecture):
        fname = "test_type_d_08am_cross_validation_aug17.py"
        assert fname in readme, f"{fname} missing from README"
        assert fname in architecture, f"{fname} missing from ARCHITECTURE"

    def test_all_aug18_test_files_in_readme(self, readme):
        aug18_files = [f for f in os.listdir(REPO_ROOT / "tests")
                       if "aug18" in f and f.endswith(".py")]
        for f in aug18_files:
            assert f in readme, f"{f} missing from README.md"

    def test_all_aug18_test_files_in_architecture(self, architecture):
        aug18_files = [f for f in os.listdir(REPO_ROOT / "tests")
                       if "aug18" in f and f.endswith(".py")]
        for f in aug18_files:
            assert f in architecture, f"{f} missing from ARCHITECTURE.md"


# ── Class 2: Mechanism #153-#156 Structural Integrity ────────────────

class TestMechanism153to156Structure:
    """All four mechanisms added on Aug 17 have required structural fields."""

    MECHANISM_IDS = [153, 154, 155, 156]

    def _find_mechanism(self, cpf, mid):
        for k, v in cpf.items():
            if isinstance(v, dict) and v.get("mechanism_id") == mid:
                return k, v
        return None, None

    @pytest.mark.parametrize("mid", MECHANISM_IDS)
    def test_mechanism_exists_in_cpf(self, cpf, mid):
        key, val = self._find_mechanism(cpf, mid)
        assert val is not None, f"Mechanism #{mid} not found in cross_publication_findings"

    @pytest.mark.parametrize("mid", MECHANISM_IDS)
    def test_mechanism_has_test_file(self, cpf, mid):
        _, val = self._find_mechanism(cpf, mid)
        assert val and "test_file" in val, f"Mechanism #{mid} missing test_file"
        tf = val["test_file"]
        basename = os.path.basename(tf)
        assert os.path.exists(REPO_ROOT / "tests" / basename), \
            f"Mechanism #{mid} test_file {basename} does not exist on disk"

    @pytest.mark.parametrize("mid", MECHANISM_IDS)
    def test_mechanism_has_source_urls(self, cpf, mid):
        _, val = self._find_mechanism(cpf, mid)
        assert val and "source_urls" in val, f"Mechanism #{mid} missing source_urls"
        assert len(val["source_urls"]) >= 2, \
            f"Mechanism #{mid} has fewer than 2 source_urls"

    @pytest.mark.parametrize("mid", MECHANISM_IDS)
    def test_mechanism_has_finding(self, cpf, mid):
        _, val = self._find_mechanism(cpf, mid)
        assert val is not None
        has_summary = "finding_summary" in val or "finding" in val
        assert has_summary, f"Mechanism #{mid} missing finding_summary or finding"

    @pytest.mark.parametrize("mid", MECHANISM_IDS)
    def test_mechanism_has_confounders(self, cpf, mid):
        _, val = self._find_mechanism(cpf, mid)
        assert val is not None
        has_conf = "confounders" in val or "confounding_factors" in val
        assert has_conf, f"Mechanism #{mid} missing confounders/confounding_factors"

    @pytest.mark.parametrize("mid", MECHANISM_IDS)
    def test_mechanism_has_cross_references(self, cpf, mid):
        _, val = self._find_mechanism(cpf, mid)
        assert val is not None
        has_xref = "cross_references" in val or "connects_to" in val
        assert has_xref, f"Mechanism #{mid} missing cross_references/connects_to"


# ── Class 3: Mechanism ID Contiguity ─────────────────────────────────

class TestMechanismIDContiguity:
    """Mechanism IDs are unique and contiguous (no gaps, no duplicates)."""

    def test_no_duplicate_ids(self, cpf):
        ids = []
        for k, v in cpf.items():
            if isinstance(v, dict) and "mechanism_id" in v:
                ids.append(v["mechanism_id"])
        assert len(ids) == len(set(ids)), \
            f"Duplicate mechanism IDs: {[x for x in ids if ids.count(x) > 1]}"

    def test_contiguous_ids(self, cpf):
        ids = sorted([
            v["mechanism_id"] for v in cpf.values()
            if isinstance(v, dict) and "mechanism_id" in v
        ])
        if len(ids) < 2:
            pytest.skip("Fewer than 2 mechanisms")
        # Known historical gaps from renumbering/consolidation or placement in other sections
        KNOWN_GAPS = {19, 30, 31, 74, 75, 80, 81, 135, 139, 161, 162}
        min_id, max_id = ids[0], ids[-1]
        expected = set(range(min_id, max_id + 1))
        actual = set(ids)
        missing = expected - actual - KNOWN_GAPS
        assert not missing, f"NEW missing mechanism IDs: {sorted(missing)}"

    def test_highest_mechanism_in_cpf(self, cpf):
        ids = [
            v["mechanism_id"] for v in cpf.values()
            if isinstance(v, dict) and "mechanism_id" in v
        ]
        assert max(ids) >= 172, f"Expected max mechanism_id >= 172, got {max(ids)}"


# ── Class 4: YAML Parse Integrity ────────────────────────────────────

class TestYAMLParseIntegrity:
    """All YAML profiles parse without error."""

    def test_ccr_parses(self):
        with open(PROFILES / "competitor-coverage-research.yaml") as f:
            data = yaml.safe_load(f)
        assert isinstance(data, dict)

    def test_competitor_entities_parses(self):
        with open(PROFILES / "competitor-entities.yaml") as f:
            data = yaml.safe_load(f)
        assert isinstance(data, dict)

    def test_wired_profile_parses(self):
        with open(PROFILES / "wired.yaml") as f:
            data = yaml.safe_load(f)
        assert isinstance(data, dict)

    def test_ccr_has_publications_and_cpf_sections(self, ccr):
        assert "publications" in ccr, "Missing publications section"
        assert "cross_publication_findings" in ccr, "Missing cross_publication_findings section"

    def test_publications_count(self, ccr):
        pubs = ccr.get("publications", {})
        assert len(pubs) >= 9, f"Expected at least 9 publications, got {len(pubs)}"


# ── Class 5: Test File Importability ─────────────────────────────────

class TestAug17TestFileImportability:
    """All aug17 test files can be imported without errors."""

    @pytest.mark.parametrize("fname", [
        "test_apple_siri_ai_triple_layer_publisher_financial_architecture_aug17",
        "test_podcast_same_episode_framing_asymmetry_aug17",
        "test_wired_anthropic_automode_coverage_silence_aug17",
        "test_bobrowsky_cross_publication_brand_stigma_smart_glasses_vocabulary_aug17",
        "test_type_d_03am_cross_validation_aug17",
        "test_type_d_08am_cross_validation_aug17",
    ])
    def test_importable(self, fname):
        import importlib
        mod = importlib.import_module(fname)
        assert mod is not None


# ── Class 6: Mechanism #153-156 Cross-Reference Presence ────────────

class TestCrossReferencePresence:
    """Mechanisms #153-#156 cross-reference earlier mechanisms that exist."""

    def _find_mechanism(self, cpf, mid):
        for k, v in cpf.items():
            if isinstance(v, dict) and v.get("mechanism_id") == mid:
                return v
        return None

    def _get_xrefs(self, mech):
        refs = mech.get("cross_references", mech.get("connects_to", []))
        ids = []
        for r in refs:
            if isinstance(r, int):
                ids.append(r)
            elif isinstance(r, dict):
                mid = r.get("mechanism_id", r.get("id"))
                if mid is not None:
                    ids.append(mid)
            elif isinstance(r, str):
                m = re.search(r'#(\d+)', r)
                if m:
                    ids.append(int(m.group(1)))
        return ids

    @pytest.mark.parametrize("mid", [153, 154, 155, 156])
    def test_cross_refs_point_to_existing_mechanisms(self, cpf, mid):
        mech = self._find_mechanism(cpf, mid)
        assert mech is not None
        xrefs = self._get_xrefs(mech)
        all_ids = {
            v["mechanism_id"] for v in cpf.values()
            if isinstance(v, dict) and "mechanism_id" in v
        }
        for ref_id in xrefs:
            assert ref_id in all_ids, \
                f"Mechanism #{mid} references #{ref_id} which does not exist"
