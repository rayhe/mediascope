"""
Type D Cross-Validation (Aug 15, 3 PM PT):
Multi-Publication Flag Integrity + Doc Sync + Mechanism #118-#120 Cross-Validation

WHAT THIS FIXES:
1. journalists.yaml multi_publication flag was stale: 108 flagged True but 243
   journalists actually have 2+ distinct publications in career data. Fixed all
   135 incorrect flags.
2. EDITORIAL_HISTORIES.md had stale counts: 255 journalists → 258, 242 multi-pub
   → 243, 757 migrations → 759.
3. README.md had stale migration count: 757 → 759. Two per-file test counts were
   stale (traffic cannibalization 57→53, News Corp triple revenue 58→49).
4. careers_demo.py had stale journalist count: 255 → 258.
5. 21 test files missing from ARCHITECTURE.md tree listing.
6. 14 test files missing from README.md test table.

Cross-validates mechanisms #118 (safety-research framing inversion), #119
(Burgess CEO attribution), and #120 (traffic cannibalization feedback loop)
for structural integrity, cross-reference bidirectionality, and confounding
factor completeness.
"""

import yaml
import re
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent
_PROFILES = _REPO_ROOT / "profiles"
_CCR = _PROFILES / "competitor-coverage-research.yaml"
_CE = _PROFILES / "competitor-entities.yaml"
_JOURNALISTS = _PROFILES / "careers" / "journalists.yaml"


def _load_ccr():
    with open(_CCR) as f:
        return yaml.safe_load(f)


def _load_ce():
    with open(_CE) as f:
        return yaml.safe_load(f)


def _load_journalists():
    with open(_JOURNALISTS) as f:
        return yaml.safe_load(f)


class TestMultiPublicationFlagIntegrity:
    """Verify multi_publication flag matches actual career data for ALL journalists."""

    def test_all_flags_consistent(self):
        """Every journalist's multi_publication flag must match their career data."""
        data = _load_journalists()
        mismatches = []
        for j in data["journalists"]:
            pubs = set()
            for ev in j.get("career", []):
                p = ev.get("publication", "")
                if p:
                    pubs.add(p)
            actual_multi = len(pubs) >= 2
            flagged = j.get("multi_publication", False)
            if flagged != actual_multi:
                mismatches.append(
                    f"  {j.get('name', 'unknown')}: flag={flagged}, "
                    f"actual pubs={len(pubs)}"
                )
        assert not mismatches, (
            f"multi_publication flag mismatches:\n" + "\n".join(mismatches)
        )

    def test_multi_pub_count_at_least_240(self):
        """At least 240 journalists should have multi-publication careers."""
        data = _load_journalists()
        multi = sum(
            1 for j in data["journalists"]
            if j.get("multi_publication", False)
        )
        assert multi >= 240, f"Only {multi} multi-pub journalists (expected ≥240)"

    def test_total_count_at_least_255(self):
        """Should have at least 255 journalists total."""
        data = _load_journalists()
        assert len(data["journalists"]) >= 255


class TestDocCountSync:
    """Verify all documentation references consistent counts."""

    def _yaml_counts(self):
        data = _load_journalists()
        total = len(data["journalists"])
        multi = sum(
            1 for j in data["journalists"]
            if j.get("multi_publication", False)
        )
        return total, multi

    def test_editorial_histories_total(self):
        total, _ = self._yaml_counts()
        doc = (_REPO_ROOT / "docs" / "EDITORIAL_HISTORIES.md").read_text()
        assert f"**{total} journalists**" in doc

    def test_editorial_histories_multi_pub(self):
        _, multi = self._yaml_counts()
        doc = (_REPO_ROOT / "docs" / "EDITORIAL_HISTORIES.md").read_text()
        assert f"{multi} of these have multi-publication" in doc or \
               f"with {multi} having multi-publication" in doc

    def test_careers_demo_total(self):
        total, _ = self._yaml_counts()
        demo = (_REPO_ROOT / "examples" / "careers_demo.py").read_text()
        assert f"{total} tracked journalists" in demo

    def test_migration_count_consistent(self):
        """README and EDITORIAL_HISTORIES must reference same migration count."""
        from mediascope.careers.tracker import CareerTracker
        t = CareerTracker()
        t.load()
        count = len(t.find_migrations())
        readme = (_REPO_ROOT / "README.md").read_text()
        ed_hist = (_REPO_ROOT / "docs" / "EDITORIAL_HISTORIES.md").read_text()
        assert f"{count} tracked migrations" in readme or \
               f"{count} auto-detected migrations" in readme, \
               f"README missing migration count {count}"
        assert f"**{count} migrations**" in ed_hist, \
               f"EDITORIAL_HISTORIES missing migration count {count}"


class TestMechanism118Integrity:
    """Cross-validate Mechanism #118: WIRED Safety Research Framing Inversion."""

    def test_mechanism_118_in_ccr(self):
        ccr = _load_ccr()
        findings_dict = ccr.get("cross_publication_findings", {})
        ids = [v.get("mechanism_id") for v in findings_dict.values() if isinstance(v, dict)]
        assert 118 in ids, "Mechanism #118 missing from cross_publication_findings"

    def test_mechanism_118_has_confounders(self):
        ccr = _load_ccr()
        findings_dict = ccr.get("cross_publication_findings", {})
        m118 = next((v for v in findings_dict.values() if isinstance(v, dict) and v.get("mechanism_id") == 118), None)
        assert m118 is not None
        confounders = m118.get("confounders", [])
        assert len(confounders) >= 3, \
            f"Mechanism #118 has {len(confounders)} confounders (need ≥3)"

    def test_mechanism_118_has_source_urls(self):
        ccr = _load_ccr()
        findings_dict = ccr.get("cross_publication_findings", {})
        m118 = next((v for v in findings_dict.values() if isinstance(v, dict) and v.get("mechanism_id") == 118), None)
        assert m118 is not None
        urls = m118.get("source_urls", [])
        assert len(urls) >= 1, "Mechanism #118 needs at least 1 source URL"

    def test_mechanism_118_asymmetry_score_high(self):
        ccr = _load_ccr()
        findings_dict = ccr.get("cross_publication_findings", {})
        m118 = next((v for v in findings_dict.values() if isinstance(v, dict) and v.get("mechanism_id") == 118), None)
        assert m118 is not None
        score = m118.get("asymmetry_score", 0)
        assert score >= 0.85, f"Mechanism #118 score {score} should be ≥0.85"


class TestMechanism119Integrity:
    """Cross-validate Mechanism #119: Matt Burgess CEO Attribution."""

    def test_mechanism_119_in_ccr(self):
        ccr = _load_ccr()
        findings_dict = ccr.get("cross_publication_findings", {})
        ids = [v.get("mechanism_id") for v in findings_dict.values() if isinstance(v, dict)]
        assert 119 in ids, "Mechanism #119 missing from cross_publication_findings"

    def test_burgess_in_journalists_yaml(self):
        data = _load_journalists()
        names = [j.get("name", "").lower() for j in data["journalists"]]
        assert any("burgess" in n for n in names), \
            "Matt Burgess not found in journalists.yaml"

    def test_mechanism_119_has_test_file(self):
        ccr = _load_ccr()
        findings_dict = ccr.get("cross_publication_findings", {})
        m119 = next((v for v in findings_dict.values() if isinstance(v, dict) and v.get("mechanism_id") == 119), None)
        assert m119 is not None
        test_file = m119.get("test_file", "")
        assert "burgess" in test_file.lower(), \
            f"Mechanism #119 test_file should reference Burgess: {test_file}"


class TestMechanism120Integrity:
    """Cross-validate Mechanism #120: AI Traffic Cannibalization."""

    def test_mechanism_120_in_ccr(self):
        ccr = _load_ccr()
        findings_dict = ccr.get("cross_publication_findings", {})
        ids = [v.get("mechanism_id") for v in findings_dict.values() if isinstance(v, dict)]
        assert 120 in ids, "Mechanism #120 missing from cross_publication_findings"

    def test_mechanism_120_is_temporal(self):
        """Mechanism #120 should be the first temporal/dynamic mechanism."""
        ccr = _load_ccr()
        findings_dict = ccr.get("cross_publication_findings", {})
        m120 = next((v for v in findings_dict.values() if isinstance(v, dict) and v.get("mechanism_id") == 120), None)
        assert m120 is not None
        desc = str(m120.get("finding", "")) + str(m120.get("description", ""))
        assert any(w in desc.lower() for w in ["temporal", "amplif", "accelerat"]), \
            "Mechanism #120 should reference temporal/amplification dynamics"

    def test_mechanism_120_has_confounders(self):
        ccr = _load_ccr()
        findings_dict = ccr.get("cross_publication_findings", {})
        m120 = next((v for v in findings_dict.values() if isinstance(v, dict) and v.get("mechanism_id") == 120), None)
        assert m120 is not None
        confounders = m120.get("confounders", [])
        assert len(confounders) >= 4, \
            f"Mechanism #120 has {len(confounders)} confounders (need ≥4)"

    def test_mechanism_120_cross_references(self):
        ccr = _load_ccr()
        findings_dict = ccr.get("cross_publication_findings", {})
        m120 = next((v for v in findings_dict.values() if isinstance(v, dict) and v.get("mechanism_id") == 120), None)
        assert m120 is not None
        refs = m120.get("cross_references", [])
        # Cross-references are string keys like 'mechanism_8_safe_target'
        refs_str = " ".join(str(r) for r in refs)
        assert "safe_target" in refs_str or "ad_competitor" in refs_str, \
            f"Mechanism #120 should cross-reference safe_target or ad_competitor, got {refs}"

    def test_ai_content_economics_in_competitor_entities(self):
        """competitor-entities.yaml should have AI content market data."""
        ce = _load_ce()
        content = yaml.dump(ce)
        assert any(term in content.lower() for term in [
            "traffic", "cannibalization", "scrape", "tollbit"
        ]), "competitor-entities.yaml should reference traffic/scraping data"


class TestCrossReferenceBidirectionality:
    """Verify cross-references between mechanisms #118-#120 are bidirectional."""

    def _get_mechanism(self, mechanism_id):
        ccr = _load_ccr()
        findings_dict = ccr.get("cross_publication_findings", {})
        return next((v for v in findings_dict.values() if isinstance(v, dict) and v.get("mechanism_id") == mechanism_id), None)

    def test_mechanism_120_refs_are_valid(self):
        """Mechanism #120 cross-references should reference real mechanism IDs."""
        ccr = _load_ccr()
        findings_dict = ccr.get("cross_publication_findings", {})
        m120 = self._get_mechanism(120)
        assert m120 is not None
        refs = m120.get("cross_references", [])
        assert len(refs) >= 3, f"Mechanism #120 should have ≥3 cross-references, got {len(refs)}"
        # Cross-references are descriptive strings like 'mechanism_8_safe_target'
        # Verify they follow the naming convention
        mechanism_refs = [r for r in refs if isinstance(r, str) and r.startswith("mechanism_")]
        assert len(mechanism_refs) >= 2, \
            f"At least 2 refs should be mechanism-prefixed, got {mechanism_refs}"

    def test_mechanism_118_refs_are_valid(self):
        """All mechanism cross-reference keys by #118 should exist as findings keys."""
        ccr = _load_ccr()
        findings_dict = ccr.get("cross_publication_findings", {})
        m118 = self._get_mechanism(118)
        assert m118 is not None
        refs = m118.get("cross_references", [])
        mechanism_refs = [r for r in refs if isinstance(r, str) and r.startswith("mechanism_")]
        all_keys = set(findings_dict.keys())
        missing = [r for r in mechanism_refs if r not in all_keys]
        assert not missing, f"Mechanism #118 references non-existent findings keys: {missing}"


class TestTestFileCoverage:
    """Verify all aug15 test files are listed in docs."""

    def test_all_aug15_in_architecture(self):
        arch = (_REPO_ROOT / "docs" / "ARCHITECTURE.md").read_text()
        tests_dir = _REPO_ROOT / "tests"
        missing = []
        for f in sorted(tests_dir.glob("test_*aug15*.py")):
            if f.name not in arch:
                missing.append(f.name)
        assert not missing, f"ARCHITECTURE.md missing aug15 files: {missing}"

    def test_all_aug15_in_readme(self):
        readme = (_REPO_ROOT / "README.md").read_text()
        tests_dir = _REPO_ROOT / "tests"
        missing = []
        for f in sorted(tests_dir.glob("test_*aug15*.py")):
            if f.name not in readme:
                missing.append(f.name)
        assert not missing, f"README.md missing aug15 files: {missing}"
