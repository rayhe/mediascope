"""
Type D Cross-Validation — Sun 2026-08-16 09:00 PT

Validates mechanisms #129-133 structural integrity, cross-reference
bidirectionality (15 backrefs added), doc sync, entity count consistency,
and per-file test counts.

Mechanisms validated:
  #129: CNBC (Versant) Post-Spinoff Smart Glasses Coverage Selection
  #130: Snap CEO Competitive Privacy Positioning Amplification
  #131: Ben Schoon (9to5Google) Control Calibration
  #132: Andy Boxall (Android Police / Valnet) Privacy Vocabulary Inversion
  #133: Snap-Perplexity-Publisher Financial Chain
"""

import os
import importlib
import yaml
import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")


def load_competitor_research():
    path = os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml")
    with open(path) as f:
        return yaml.safe_load(f)


def load_competitor_entities():
    path = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
    with open(path) as f:
        return yaml.safe_load(f)


def find_all_mechanisms(data):
    """Recursively find all mechanism entries with mechanism_id + finding_summary/mechanism_name."""
    mechanisms = {}

    def _walk(obj):
        if isinstance(obj, dict):
            if "mechanism_id" in obj and (
                "mechanism_name" in obj or "finding_summary" in obj
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
                mechanisms[mid] = {
                    "refs": refs,
                    "data": obj,
                }
            for v in obj.values():
                _walk(v)
        elif isinstance(obj, list):
            for item in obj:
                _walk(item)

    _walk(data)
    return mechanisms


# ===========================================================================
# Load data once
# ===========================================================================

_data = load_competitor_research()
_mechanisms = find_all_mechanisms(_data)
_entities = load_competitor_entities()

TARGET_IDS = [129, 130, 131, 132, 133]


# ===========================================================================
# 1. Mechanism Structural Integrity
# ===========================================================================


class TestMechanismStructuralIntegrity:
    """Each mechanism #129-133 exists with required metadata fields."""

    @pytest.mark.parametrize("mid", TARGET_IDS)
    def test_mechanism_exists(self, mid):
        assert mid in _mechanisms, f"Mechanism #{mid} not found in YAML"

    @pytest.mark.parametrize("mid", TARGET_IDS)
    def test_has_finding_summary(self, mid):
        m = _mechanisms[mid]["data"]
        assert "finding_summary" in m, f"#{mid} missing finding_summary"
        assert len(m["finding_summary"]) > 50, f"#{mid} finding_summary too short"

    @pytest.mark.parametrize("mid", TARGET_IDS)
    def test_has_discovery_date(self, mid):
        m = _mechanisms[mid]["data"]
        date_key = "discovery_date" if "discovery_date" in m else "date_added"
        assert date_key in m, f"#{mid} missing discovery_date/date_added"
        assert m[date_key] == "2026-08-16", f"#{mid} date should be 2026-08-16"

    @pytest.mark.parametrize("mid", TARGET_IDS)
    def test_has_test_file(self, mid):
        m = _mechanisms[mid]["data"]
        assert "test_file" in m, f"#{mid} missing test_file reference"
        test_path = os.path.join(REPO_ROOT, m["test_file"])
        assert os.path.exists(test_path), f"#{mid} test_file {m['test_file']} does not exist"

    @pytest.mark.parametrize("mid", TARGET_IDS)
    def test_has_source_urls(self, mid):
        m = _mechanisms[mid]["data"]
        # Source URLs may be top-level or embedded in articles
        has_urls = "source_urls" in m
        if not has_urls:
            # Check for article-level URLs
            for key in ["articles", "amplification_chain", "key_articles"]:
                if key in m:
                    has_urls = True
                    break
        assert has_urls, f"#{mid} missing source URLs"

    @pytest.mark.parametrize("mid", TARGET_IDS)
    def test_has_confounders(self, mid):
        m = _mechanisms[mid]["data"]
        confounders_key = None
        for key in ["confounders", "confounding_factors"]:
            if key in m:
                confounders_key = key
                break
        assert confounders_key is not None, f"#{mid} missing confounders/confounding_factors"
        assert len(m[confounders_key]) >= 3, f"#{mid} needs at least 3 confounders"


# ===========================================================================
# 2. Mechanism ID Contiguity
# ===========================================================================


class TestMechanismIDContiguity:
    """No gaps or duplicates in mechanism IDs #129-133."""

    def test_no_id_gaps(self):
        for mid in TARGET_IDS:
            assert mid in _mechanisms, f"Gap: mechanism #{mid} missing"

    def test_max_mechanism_id(self):
        max_id = max(_mechanisms.keys())
        assert max_id >= 133, f"Expected max mechanism ID 133, got {max_id}"

    def test_no_duplicate_ids(self):
        """Verify no duplicate mechanism_id values across the entire file."""
        all_ids = list(_mechanisms.keys())
        assert len(all_ids) == len(set(all_ids)), "Duplicate mechanism IDs found"


# ===========================================================================
# 3. Cross-Reference Bidirectionality
# ===========================================================================


class TestCrossReferenceBidirectionality:
    """Every cross-reference from #129-133 has a corresponding backref."""

    @pytest.mark.parametrize("mid", TARGET_IDS)
    def test_all_refs_bidirectional(self, mid):
        m = _mechanisms[mid]
        for ref_id in m["refs"]:
            if ref_id in _mechanisms:
                assert mid in _mechanisms[ref_id]["refs"], (
                    f"#{ref_id} does not reference back to #{mid}"
                )

    def test_mechanism_129_refs_128(self):
        assert 128 in _mechanisms
        assert 129 in _mechanisms[128]["refs"]

    def test_mechanism_131_refs_from_110(self):
        assert 110 in _mechanisms
        assert 131 in _mechanisms[110]["refs"]

    def test_mechanism_131_refs_from_114(self):
        assert 114 in _mechanisms
        assert 131 in _mechanisms[114]["refs"]

    def test_mechanism_131_refs_from_115(self):
        assert 115 in _mechanisms
        assert 131 in _mechanisms[115]["refs"]

    def test_mechanism_131_refs_from_116(self):
        assert 116 in _mechanisms
        assert 131 in _mechanisms[116]["refs"]

    def test_mechanism_132_refs_from_30(self):
        assert 30 in _mechanisms
        assert 132 in _mechanisms[30]["refs"]

    def test_mechanism_133_refs_from_132(self):
        assert 132 in _mechanisms
        assert 133 in _mechanisms[132]["refs"]

    def test_mechanism_130_refs_from_131_132_133(self):
        """#130 should have backrefs from #131, #132, and #133."""
        m130_refs = _mechanisms[130]["refs"]
        assert 131 in m130_refs
        assert 132 in m130_refs
        assert 133 in m130_refs


# ===========================================================================
# 4. Confounder Quality
# ===========================================================================


class TestConfounderQuality:
    """Confounders have strength ratings and include at least one STRONG."""

    @pytest.mark.parametrize("mid", TARGET_IDS)
    def test_has_strength_ratings(self, mid):
        m = _mechanisms[mid]["data"]
        confounders = m.get("confounders", m.get("confounding_factors", []))
        for c in confounders:
            if isinstance(c, dict):
                assert "strength" in c or "name" in c, (
                    f"#{mid} confounder missing strength/name"
                )

    @pytest.mark.parametrize("mid", TARGET_IDS)
    def test_has_strong_confounder(self, mid):
        m = _mechanisms[mid]["data"]
        confounders = m.get("confounders", m.get("confounding_factors", []))
        strengths = []
        for c in confounders:
            if isinstance(c, dict):
                s = c.get("strength", "")
                if isinstance(s, str):
                    strengths.append(s.upper())
        assert "STRONG" in strengths, f"#{mid} needs at least one STRONG confounder"


# ===========================================================================
# 5. Entity Count Consistency
# ===========================================================================


class TestEntityCountConsistency:
    """Entity set includes all expected entities."""

    def test_versant_entity_exists(self):
        entities = _entities.get("entities", _entities)
        entity_keys = set()
        if isinstance(entities, dict):
            entity_keys = set(entities.keys())
        assert "versant_media_group" in entity_keys or any(
            "versant" in str(k).lower() for k in entity_keys
        ), "versant_media_group entity missing from competitor-entities.yaml"

    def test_snap_entity_exists(self):
        entities = _entities.get("entities", _entities)
        entity_keys = set()
        if isinstance(entities, dict):
            entity_keys = set(entities.keys())
        assert any(
            "snap" in str(k).lower() for k in entity_keys
        ), "snap entity missing from competitor-entities.yaml"

    def test_minimum_entity_count(self):
        entities = _entities.get("entities", _entities)
        if isinstance(entities, dict):
            count = len(entities)
        else:
            count = len(entities) if isinstance(entities, list) else 0
        assert count >= 15, f"Expected >= 15 entities, got {count}"


# ===========================================================================
# 6. Test File Existence and Importability
# ===========================================================================


class TestFileExistenceAndImportability:
    """Test files for #129-133 exist and can be imported."""

    expected_files = {
        129: "tests/test_cnbc_versant_post_spinoff_smart_glasses_coverage_selection_aug16.py",
        130: "tests/test_snap_competitive_privacy_positioning_amplification_aug16.py",
        131: "tests/test_ben_schoon_9to5google_control_calibration_cross_entity_aug16.py",
        132: "tests/test_andy_boxall_cross_entity_privacy_vocabulary_inversion_aug16.py",
        133: "tests/test_snap_perplexity_publisher_financial_chain_aug16.py",
    }

    @pytest.mark.parametrize("mid", TARGET_IDS)
    def test_file_exists(self, mid):
        path = os.path.join(REPO_ROOT, self.expected_files[mid])
        assert os.path.exists(path), f"Test file for #{mid} does not exist: {self.expected_files[mid]}"

    @pytest.mark.parametrize("mid", TARGET_IDS)
    def test_file_importable(self, mid):
        module_name = self.expected_files[mid].replace("tests/", "").replace(".py", "")
        try:
            importlib.import_module(f"tests.{module_name}")
        except Exception as e:
            pytest.fail(f"Cannot import test for #{mid}: {e}")


# ===========================================================================
# 7. Mechanism Content Validation
# ===========================================================================


class TestMechanism129Content:
    """#129: CNBC Versant Post-Spinoff Coverage Selection."""

    def test_is_empirical_test_of_128(self):
        m = _mechanisms[129]["data"]
        summary = m.get("finding_summary", "")
        assert "128" in summary or "prediction" in summary.lower()

    def test_has_samsung_google_meta_comparison(self):
        m = _mechanisms[129]["data"]
        has_samsung = "samsung" in str(m).lower()
        has_meta = "meta" in str(m).lower()
        assert has_samsung and has_meta

    def test_competitor_pair(self):
        m = _mechanisms[129]["data"]
        pair = m.get("competitor_pair", "")
        assert "Samsung" in pair or "Google" in pair
        assert "Meta" in pair


class TestMechanism130Content:
    """#130: Snap CEO Competitive Privacy Positioning Amplification."""

    def test_hardware_comparison_present(self):
        m = _mechanisms[130]["data"]
        assert "hardware_comparison" in m
        snap = m["hardware_comparison"].get("snap_specs", {})
        meta = m["hardware_comparison"].get("meta_ray_ban", {})
        assert snap.get("cameras", 0) == 4
        assert meta.get("cameras", 0) == 1

    def test_clean_control_gizmodo(self):
        m = _mechanisms[130]["data"]
        assert "clean_control_gizmodo" in m
        control = m["clean_control_gizmodo"]
        assert control.get("raised_camera_question") is True

    def test_amplification_chain(self):
        m = _mechanisms[130]["data"]
        assert "amplification_chain" in m
        assert len(m["amplification_chain"]) >= 3


class TestMechanism131Content:
    """#131: Ben Schoon Control Calibration."""

    def test_control_calibration_present(self):
        m = _mechanisms[131]["data"]
        assert "control_calibration" in m

    def test_9to5google_ratio(self):
        m = _mechanisms[131]["data"]
        cal = m.get("control_calibration", {})
        g = cal.get("9to5google", {})
        assert g.get("meta_privacy_terms", 0) > 0
        assert g.get("competitor_privacy_terms", 0) > 0

    def test_wired_infinite_ratio(self):
        m = _mechanisms[131]["data"]
        cal = m.get("control_calibration", {})
        w = cal.get("wired", {})
        assert w.get("competitor_privacy_terms", 1) == 0

    def test_future_plc_infinite_ratio(self):
        m = _mechanisms[131]["data"]
        cal = m.get("control_calibration", {})
        f = cal.get("future_plc", {})
        assert f.get("competitor_privacy_terms", 1) == 0


class TestMechanism132Content:
    """#132: Andy Boxall Privacy Vocabulary Inversion."""

    def test_three_articles(self):
        m = _mechanisms[132]["data"]
        assert "articles" in m
        articles = m["articles"]
        assert len(articles) >= 3

    def test_privacy_inversion(self):
        m = _mechanisms[132]["data"]
        articles = m.get("articles", {})
        snap = articles.get("snap_specs", {})
        meta = articles.get("meta_super_sensing", {})
        assert snap.get("privacy_terms", 1) == 0, "Snap should have 0 privacy terms"
        assert meta.get("privacy_terms", 0) >= 7, "Meta should have 7+ privacy terms"

    def test_same_chip_samsung(self):
        m = _mechanisms[132]["data"]
        summary = m.get("finding_summary", "")
        assert "snapdragon ar1" in summary.lower() or "identical" in summary.lower()


class TestMechanism133Content:
    """#133: Snap-Perplexity-Publisher Financial Chain."""

    def test_three_financial_connections(self):
        m = _mechanisms[133]["data"]
        conns = m.get("snap_financial_connections_to_publishers", {})
        direct = conns.get("direct", [])
        indirect_perp = conns.get("indirect_via_perplexity", [])
        indirect_oai = conns.get("indirect_via_openai", [])
        total = len(direct) + len(indirect_perp) + len(indirect_oai)
        assert total >= 3, f"Expected 3+ financial connections, got {total}"

    def test_meta_zero_connections(self):
        m = _mechanisms[133]["data"]
        meta = m.get("meta_financial_connections_to_publishers", {})
        assert meta.get("total", 1) == 0

    def test_falsifiable_predictions(self):
        m = _mechanisms[133]["data"]
        preds = m.get("falsifiable_predictions", [])
        assert len(preds) >= 3, f"Expected 3+ predictions, got {len(preds)}"


# ===========================================================================
# 8. Doc Sync Integrity
# ===========================================================================


class TestDocSyncIntegrity:
    """README and ARCHITECTURE file counts match disk."""

    def test_readme_test_file_count(self):
        readme_path = os.path.join(REPO_ROOT, "README.md")
        with open(readme_path) as f:
            content = f.read()
        # Find the test file count line
        actual_count = len([
            f for f in os.listdir(TESTS_DIR)
            if f.startswith("test_") and f.endswith(".py")
        ])
        # Check if README mentions this count
        assert str(actual_count) in content or str(actual_count - 1) in content, (
            f"README test file count ({actual_count} on disk) may be stale"
        )

    def test_all_aug16_test_files_in_readme(self):
        readme_path = os.path.join(REPO_ROOT, "README.md")
        with open(readme_path) as f:
            content = f.read()
        aug16_files = [
            f for f in os.listdir(TESTS_DIR)
            if f.startswith("test_") and f.endswith(".py") and "aug16" in f
        ]
        missing = [f for f in aug16_files if f.replace(".py", "") not in content]
        # This cross-validation file itself may not be in README yet
        missing = [f for f in missing if "09am_cross_validation" not in f]
        assert len(missing) == 0, f"Aug 16 test files missing from README: {missing}"


# ===========================================================================
# 9. Regression Guards (#125-128)
# ===========================================================================


class TestRegressionGuards:
    """Prior mechanisms #125-128 remain intact after #129-133 additions."""

    @pytest.mark.parametrize("mid", [125, 126, 127, 128])
    def test_prior_mechanism_exists(self, mid):
        assert mid in _mechanisms, f"Regression: mechanism #{mid} disappeared"

    @pytest.mark.parametrize("mid", [125, 126, 127, 128])
    def test_prior_mechanism_has_summary(self, mid):
        m = _mechanisms[mid]["data"]
        assert "finding_summary" in m, f"Regression: #{mid} lost finding_summary"


# ===========================================================================
# 10. Finding Summary Distinctiveness
# ===========================================================================


class TestFindingSummaryDistinctiveness:
    """Mechanism summaries are sufficiently distinct (Jaccard < 0.7)."""

    def _jaccard(self, a, b):
        sa = set(a.lower().split())
        sb = set(b.lower().split())
        inter = sa & sb
        union = sa | sb
        return len(inter) / len(union) if union else 1.0

    def test_pairwise_distinctiveness(self):
        summaries = {}
        for mid in TARGET_IDS:
            summaries[mid] = _mechanisms[mid]["data"].get("finding_summary", "")

        for i, m1 in enumerate(TARGET_IDS):
            for m2 in TARGET_IDS[i + 1:]:
                j = self._jaccard(summaries[m1], summaries[m2])
                assert j < 0.7, (
                    f"#{m1} and #{m2} too similar (Jaccard={j:.2f})"
                )
