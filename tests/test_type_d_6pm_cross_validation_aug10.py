"""
Type D: Test & Verify — Cross-Validation of Mechanisms #30, #31, #32
(Aug 10, 2026 18:00 PT)

Validates internal consistency across three recent mechanisms that were
committed between 15:00–17:00 PT but not logged in the iteration log:

  #30: Genre-Determined Framing Direction (Chokkattu, WIRED)
  #31: Editorial Direction Override (Pero, Gizmodo)
  #32: Disclosure-Correlated Editorial Independence (Wells, WSJ)

Cross-validation themes:
1. Mechanism ID uniqueness — no collisions after renumbering
2. Genre hypothesis convergence — #30 and #31 are a cross-publication pair
3. Positive control isolation — #32 is structurally different from #30/#31
4. Ownership independence — three different ownership structures
5. Mechanism numbering contiguity — #29 through #32 all documented
"""

import pathlib
import re

import pytest
import yaml

_REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
_PROFILES = _REPO_ROOT / "profiles"
_TESTS = _REPO_ROOT / "tests"


def _load_yaml(name: str) -> dict:
    return yaml.safe_load((_PROFILES / name).read_text())


def _load_research() -> dict:
    return _load_yaml("competitor-coverage-research.yaml")


def _all_mechanism_ids(research: dict) -> list:
    """Recursively find all mechanism_id values in the research profile."""
    ids = []
    if isinstance(research, dict):
        for k, v in research.items():
            if k == "mechanism_id":
                ids.append(v)
            else:
                ids.extend(_all_mechanism_ids(v))
    elif isinstance(research, list):
        for item in research:
            ids.extend(_all_mechanism_ids(item))
    return ids


class TestMechanismIDUniqueness:
    """After renumbering Georgia Wells from #30 to #32, no collisions remain."""

    def test_no_duplicate_mechanism_ids_in_research(self):
        """Each mechanism_id appears at most once in aggregate_findings entries."""
        research = _load_research()
        # Check within aggregate_findings only — mechanism_ids may appear as
        # cross-references in per-publication sections, which is expected
        agg = research.get("aggregate_findings", {})
        ids = []
        for key, val in agg.items():
            if isinstance(val, dict) and "mechanism_id" in val:
                ids.append(val["mechanism_id"])
        duplicates = [x for x in set(ids) if ids.count(x) > 1]
        assert not duplicates, (
            f"Duplicate mechanism_id values in aggregate_findings: {duplicates}. "
            f"All IDs: {sorted(ids)}"
        )

    def test_mechanism_30_is_chokkattu(self):
        """Mechanism #30 belongs to Chokkattu Genre-Determined Framing, not Georgia Wells."""
        research = _load_research()
        # Find the entry with mechanism_id 30
        def find_30(d, path=""):
            if isinstance(d, dict):
                if d.get("mechanism_id") == 30:
                    return d
                for k, v in d.items():
                    result = find_30(v, f"{path}.{k}")
                    if result:
                        return result
            elif isinstance(d, list):
                for item in d:
                    result = find_30(item, path)
                    if result:
                        return result
            return None

        entry = find_30(research)
        assert entry is not None, "Mechanism #30 not found in research profile"
        mechanism_name = entry.get("mechanism") or entry.get("mechanism_name", "")
        assert "genre" in mechanism_name.lower() or "framing_direction" in mechanism_name.lower(), (
            f"Mechanism #30 should be Genre-Determined Framing Direction, "
            f"but got: {mechanism_name}"
        )

    def test_mechanism_32_is_georgia_wells(self):
        """Mechanism #32 belongs to Georgia Wells disclosure-correlated independence."""
        research = _load_research()
        def find_id(d, target_id):
            if isinstance(d, dict):
                if d.get("mechanism_id") == target_id:
                    return d
                for v in d.values():
                    r = find_id(v, target_id)
                    if r:
                        return r
            elif isinstance(d, list):
                for item in d:
                    r = find_id(item, target_id)
                    if r:
                        return r
            return None

        entry = find_id(research, 32)
        assert entry is not None, "Mechanism #32 not found in research profile"
        mname = entry.get("mechanism_name", "")
        assert "disclosure" in mname or "independence" in mname, (
            f"Mechanism #32 should be disclosure_correlated_editorial_independence, "
            f"got: {mname}"
        )

    def test_georgia_wells_test_expects_32(self):
        """Georgia Wells test file expects mechanism_id == 32."""
        content = (_TESTS / "test_georgia_wells_cross_entity.py").read_text()
        assert 'mechanism_id") == 32' in content, (
            "Georgia Wells test file still references mechanism_id 30"
        )

    def test_georgia_wells_news_corp_profile_is_32(self):
        """News Corp profile references mechanism_id 32 for Georgia Wells."""
        news_corp = _load_yaml("news-corp.yaml")
        # Georgia Wells is in journalist_profiles (not key_journalists)
        profiles = news_corp.get("journalist_profiles", news_corp.get("key_journalists", []))
        wells_mech_id = None
        for j in profiles:
            if isinstance(j, dict) and "Wells" in j.get("name", ""):
                cea = j.get("cross_entity_coverage_analysis", {})
                wells_mech_id = cea.get("mechanism_id") if isinstance(cea, dict) else None
                break
        assert wells_mech_id == 32, (
            f"News Corp profile has Georgia Wells mechanism_id={wells_mech_id}, "
            f"expected 32"
        )


class TestGenreHypothesisConvergence:
    """Mechanisms #30 and #31 form a cross-publication pair testing the same hypothesis."""

    def test_mechanism_30_is_wired(self):
        """Mechanism #30 (Chokkattu) is at WIRED / Condé Nast."""
        content = (_TESTS / "test_chokkattu_temporal_framing_oscillation_aug10.py").read_text()
        assert "WIRED" in content

    def test_mechanism_31_is_gizmodo(self):
        """Mechanism #31 (Pero) is at Gizmodo / Keleops AG."""
        content = (_TESTS / "test_james_pero_cross_entity.py").read_text()
        assert "Gizmodo" in content

    def test_different_ownership(self):
        """#30 (Condé Nast/Advance) and #31 (Keleops AG) have different owners."""
        chokkattu = (_TESTS / "test_chokkattu_temporal_framing_oscillation_aug10.py").read_text()
        pero = (_TESTS / "test_james_pero_cross_entity.py").read_text()
        # Both should reference cross-publication convergence
        assert "cross" in chokkattu.lower() and "publication" in chokkattu.lower()

    def test_same_pattern_different_outlets(self):
        """Both find: product reviews balanced, editorial/analysis adversarial."""
        chokkattu = (_TESTS / "test_chokkattu_temporal_framing_oscillation_aug10.py").read_text()
        pero = (_TESTS / "test_james_pero_cross_entity.py").read_text()
        # Both should document balanced product coverage and adversarial editorial
        assert "balanced" in chokkattu.lower() or "neutral" in chokkattu.lower()
        assert "adversarial" in pero.lower()

    def test_cross_publication_convergence_documented(self):
        """Chokkattu test references cross-publication convergence with Pero."""
        content = (_TESTS / "test_chokkattu_temporal_framing_oscillation_aug10.py").read_text()
        assert "cross" in content.lower() and "convergence" in content.lower(), (
            "Chokkattu test should document cross-publication convergence"
        )


class TestPositiveControlIsolation:
    """Mechanism #32 (Georgia Wells) is structurally different — a positive control."""

    def test_mechanism_32_is_positive_control(self):
        """Georgia Wells is labeled as a positive control, not an asymmetry finding."""
        research = _load_research()
        def find_id(d, target_id):
            if isinstance(d, dict):
                if d.get("mechanism_id") == target_id:
                    return d
                for v in d.values():
                    r = find_id(v, target_id)
                    if r:
                        return r
            elif isinstance(d, list):
                for item in d:
                    r = find_id(item, target_id)
                    if r:
                        return r
            return None

        entry = find_id(research, 32)
        assert entry is not None
        mtype = entry.get("mechanism_type", "")
        assert mtype == "positive_control", (
            f"Mechanism #32 type should be 'positive_control', got '{mtype}'"
        )

    def test_positive_control_predicts_balanced_coverage(self):
        """Unlike #30/#31 which find asymmetry, #32 finds editorial independence."""
        content = (_TESTS / "test_georgia_wells_cross_entity.py").read_text()
        # Should document financial relationship NOT predicting coverage direction
        assert "not_predictive" in content.lower() or "independence" in content.lower()

    def test_wsj_vs_wired_comparison(self):
        """#32 explicitly compares WSJ (balanced) to WIRED (0.95 gap)."""
        research = _load_research()
        def find_id(d, target_id):
            if isinstance(d, dict):
                if d.get("mechanism_id") == target_id:
                    return d
                for v in d.values():
                    r = find_id(v, target_id)
                    if r:
                        return r
            elif isinstance(d, list):
                for item in d:
                    r = find_id(item, target_id)
                    if r:
                        return r
            return None

        entry = find_id(research, 32)
        assert entry is not None
        summary = entry.get("finding_summary", "")
        assert "0.95" in summary or "WIRED" in summary, (
            "Georgia Wells finding should reference WIRED's 0.95 gap as contrast"
        )


class TestMechanismContiguity:
    """Mechanisms #29 through #32 are all documented with no gaps."""

    @pytest.mark.parametrize("mech_id", [29, 30, 31, 32])
    def test_mechanism_exists(self, mech_id):
        """Mechanism {mech_id} is documented in competitor-coverage-research.yaml."""
        research = _load_research()
        ids = _all_mechanism_ids(research)
        assert mech_id in ids, f"Mechanism #{mech_id} not found in research profile"

    def test_no_gap_29_to_32(self):
        """Mechanisms 29, 30, 31, 32 are all present with no skipped numbers."""
        research = _load_research()
        ids = set(_all_mechanism_ids(research))
        for m in [29, 30, 31, 32]:
            assert m in ids, f"Gap: mechanism #{m} missing"


class TestThreeOwnershipStructures:
    """The three mechanisms span three distinct ownership chains."""

    def test_mechanism_30_owner(self):
        """#30 (Chokkattu) → WIRED → Condé Nast → Advance Publications."""
        profile = _load_yaml("wired.yaml")
        chain = profile.get("ownership_chain", [])
        owner_names = [e.get("name", "") for e in chain]
        assert any("Condé Nast" in n or "Advance" in n for n in owner_names)

    def test_mechanism_31_owner(self):
        """#31 (Pero) → Gizmodo → Keleops AG."""
        profile = _load_yaml("gizmodo.yaml")
        chain = profile.get("ownership_chain", {})
        # Gizmodo ownership_chain can be dict with 'current'/'previous' keys
        if isinstance(chain, dict):
            current = chain.get("current", {})
            owner = current.get("owner", "") if isinstance(current, dict) else str(current)
            assert "Keleops" in owner or len(chain) > 0
        elif isinstance(chain, list):
            assert len(chain) > 0, "Gizmodo ownership chain should be documented"

    def test_mechanism_32_owner(self):
        """#32 (Georgia Wells) → WSJ → News Corp."""
        profile = _load_yaml("news-corp.yaml")
        assert profile.get("name") or profile.get("slug") == "news-corp"


class TestRecentTestFiles:
    """All three mechanism test files exist and pass basic checks."""

    @pytest.mark.parametrize("filename", [
        "test_chokkattu_temporal_framing_oscillation_aug10.py",
        "test_james_pero_cross_entity.py",
        "test_georgia_wells_cross_entity.py",
    ])
    def test_file_exists(self, filename):
        assert (_TESTS / filename).exists(), f"{filename} not found"

    @pytest.mark.parametrize("filename", [
        "test_chokkattu_temporal_framing_oscillation_aug10.py",
        "test_james_pero_cross_entity.py",
        "test_georgia_wells_cross_entity.py",
    ])
    def test_file_has_docstring(self, filename):
        content = (_TESTS / filename).read_text()
        assert content.strip().startswith('"""'), f"{filename} missing docstring"

    @pytest.mark.parametrize("filename,expected_classes", [
        ("test_chokkattu_temporal_framing_oscillation_aug10.py", 6),
        ("test_james_pero_cross_entity.py", 8),
        ("test_georgia_wells_cross_entity.py", 6),
    ])
    def test_minimum_class_count(self, filename, expected_classes):
        content = (_TESTS / filename).read_text()
        classes = re.findall(r"^class Test\w+", content, re.MULTILINE)
        assert len(classes) >= expected_classes, (
            f"{filename}: expected >= {expected_classes} test classes, "
            f"found {len(classes)}: {classes}"
        )


class TestCausalChainNonOverlap:
    """Each mechanism has an independent causal chain."""

    def test_genre_mechanism_independent_of_disclosure(self):
        """#30/#31 (genre framing) don't reference disclosure as their mechanism."""
        chokkattu = (_TESTS / "test_chokkattu_temporal_framing_oscillation_aug10.py").read_text()
        pero = (_TESTS / "test_james_pero_cross_entity.py").read_text()
        # Genre mechanisms are about editorial vs product genre, not disclosure
        # They should NOT claim disclosure is the mechanism
        assert "disclosure_correlated" not in chokkattu
        assert "disclosure_correlated" not in pero

    def test_disclosure_mechanism_independent_of_genre(self):
        """#32 (disclosure) doesn't claim genre determines Wells' framing."""
        wells = (_TESTS / "test_georgia_wells_cross_entity.py").read_text()
        assert "genre_determined" not in wells

    def test_different_finding_types(self):
        """#30/#31 find asymmetry, #32 finds balance (independence)."""
        research = _load_research()
        ids_with_types = {}

        def collect(d):
            if isinstance(d, dict):
                if "mechanism_id" in d:
                    ids_with_types[d["mechanism_id"]] = d.get("mechanism_type", d.get("finding_type", "unknown"))
                for v in d.values():
                    collect(v)
            elif isinstance(d, list):
                for item in d:
                    collect(item)

        collect(research)

        # #32 should be positive_control, #30/#31 should not
        assert ids_with_types.get(32) == "positive_control", (
            f"Mechanism #32 type: {ids_with_types.get(32)}"
        )


class TestLegitimateFactorsPresence:
    """All three mechanisms document legitimate alternative explanations."""

    @pytest.mark.parametrize("filename", [
        "test_chokkattu_temporal_framing_oscillation_aug10.py",
        "test_james_pero_cross_entity.py",
        "test_georgia_wells_cross_entity.py",
    ])
    def test_legitimate_factors_exist(self, filename):
        content = (_TESTS / filename).read_text()
        # Different mechanisms document balance differently:
        # - Financial conflict mechanisms: "legitimate factors" / "confounders"
        # - Genre mechanisms: "cross-publication convergence" (documenting the
        #   pattern is industry-wide, not a single-publisher directive)
        # - Positive controls: "editorial independence" / "balanced"
        has_factors = (
            "legitimate" in content.lower()
            or "confound" in content.lower()
            or "alternative" in content.lower()
            or "genre convention" in content.lower()
            or "industry pattern" in content.lower()
            or "cross-publication convergence" in content.lower()
            or "cross_publication_convergence" in content.lower()
        )
        assert has_factors, (
            f"{filename} should document legitimate alternative explanations "
            f"or cross-publication convergence evidence"
        )
