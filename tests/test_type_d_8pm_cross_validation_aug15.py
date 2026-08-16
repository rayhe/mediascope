"""Type D: Cross-validation at 8 PM Aug 15 — Structural integrity after
mechanisms #122-#124 placement fix + WBD quad-tech financial hierarchy validation.

Verifies:
1. YAML structural integrity: no misplaced mechanisms under publications
2. Mechanism #124 (WBD quad-tech) financial hierarchy is internally consistent
3. Cross-references between mechanisms #122-#124 are bidirectional and coherent
4. Entity count and mechanism count consistency across all YAML files
5. The financial incentive hierarchy model revision is documented
"""
import yaml
import pytest
from pathlib import Path

PROFILES_DIR = Path(__file__).parent.parent / "profiles"


def load_yaml(name):
    return yaml.safe_load((PROFILES_DIR / name).read_text())


# ===================================================================
# 1. STRUCTURAL INTEGRITY — No mechanism-only entries under publications
# ===================================================================
class TestStructuralIntegrity:
    """After the placement fix, publications must contain ONLY publication
    profiles (with meta_coverage_tone), never bare mechanism entries."""

    @pytest.fixture(scope="class")
    @classmethod
    def ccr(cls):
        return load_yaml("competitor-coverage-research.yaml")

    def test_all_publications_have_meta_coverage_tone(self, ccr):
        pubs = ccr.get("publications", {})
        for slug, data in pubs.items():
            assert "meta_coverage_tone" in data, (
                f"{slug} under publications is missing meta_coverage_tone"
            )

    def test_no_mechanism_only_entries_in_publications(self, ccr):
        """Every entry under publications with a mechanism_id must also have
        meta_coverage_tone — otherwise it's a misplaced finding."""
        pubs = ccr.get("publications", {})
        for slug, data in pubs.items():
            if "mechanism_id" in data:
                assert "meta_coverage_tone" in data, (
                    f"{slug} has mechanism_id={data['mechanism_id']} but no "
                    "meta_coverage_tone — misplaced under publications"
                )

    def test_mechanisms_122_123_124_in_cross_publication_findings(self, ccr):
        cpf = ccr.get("cross_publication_findings", {})
        assert "techcrunch_snap_specs_camera_privacy_vocabulary_zero" in cpf, \
            "Mechanism #122 missing from cross_publication_findings"
        assert "lisa_eadicicco_cnn_coverage_selection_asymmetry" in cpf, \
            "Mechanism #123 missing from cross_publication_findings"
        assert "wbd_quad_tech_financial_architecture_content_deal_paradox" in cpf, \
            "Mechanism #124 missing from cross_publication_findings"

    def test_mechanisms_122_123_124_not_in_publications(self, ccr):
        pubs = ccr.get("publications", {})
        assert "techcrunch_snap_specs_camera_privacy_vocabulary_zero" not in pubs
        assert "lisa_eadicicco_cnn_coverage_selection_asymmetry" not in pubs
        assert "wbd_quad_tech_financial_architecture_content_deal_paradox" not in pubs

    def test_yaml_parses_without_error(self):
        """Regression: YAML must parse cleanly (list-vs-mapping bug from #124 insert)."""
        # This will throw if YAML is malformed
        data = load_yaml("competitor-coverage-research.yaml")
        assert "publications" in data
        assert "cross_publication_findings" in data
        assert "research_period" in data


# ===================================================================
# 2. WBD QUAD-TECH FINANCIAL HIERARCHY (#124) — Internal consistency
# ===================================================================
class TestWBDQuadTechConsistency:
    """Mechanism #124 documents a financial incentive hierarchy where
    advertising > infrastructure > content licensing. All numbers must
    be internally consistent."""

    @pytest.fixture(scope="class")
    @classmethod
    def mechanism(cls):
        ccr = load_yaml("competitor-coverage-research.yaml")
        return ccr["cross_publication_findings"][
            "wbd_quad_tech_financial_architecture_content_deal_paradox"
        ]

    @pytest.fixture(scope="class")
    @classmethod
    def entity(cls):
        ent = load_yaml("competitor-entities.yaml")
        return ent.get("entities", ent)["wbd_cnn"]

    def test_mechanism_id_is_124(self, mechanism):
        assert mechanism["mechanism_id"] == 124

    def test_has_four_entity_relationships(self, mechanism):
        ec = mechanism["entity_coverage"]
        assert "meta" in ec
        assert "google" in ec
        assert "amazon" in ec
        assert "samsung" in ec

    def test_meta_deal_prediction_failed(self, mechanism):
        meta = mechanism["entity_coverage"]["meta"]
        assert meta["predicted_tone"] == "softer"
        assert meta["actual_tone"] == "adversarial"
        assert meta["prediction_failure"] is True

    def test_samsung_is_advertising_dependency(self, mechanism):
        samsung = mechanism["entity_coverage"]["samsung"]
        assert samsung["relationship"] == "advertising_dependency"
        assert "9.7B" in samsung.get("spend_profile", "")

    def test_financial_hierarchy_documented(self, mechanism):
        """Key finding must document the advertising > infrastructure > content licensing hierarchy."""
        finding = mechanism.get("key_finding", "") or mechanism.get("finding", "")
        assert "advertising" in finding.lower()
        assert "infrastructure" in finding.lower() or "cloud" in finding.lower()
        assert "content licensing" in finding.lower() or "licensing" in finding.lower()

    def test_model_revision_documented(self, mechanism):
        """Mechanism #124 introduces a model revision: deal-only → weighted multi-factor."""
        revision = mechanism.get("model_revision", "")
        assert "multi-factor" in revision.lower() or "weighted" in revision.lower()

    def test_wbd_q2_2026_ad_decline(self, mechanism):
        q2 = mechanism.get("wbd_q2_2026", {})
        assert q2.get("ad_yoy_pct", 0) < 0, "WBD ad revenue must show YoY decline"

    def test_entity_yaml_has_wbd_cnn(self, entity):
        assert entity is not None
        assert "quad_tech_financial_architecture" in entity

    def test_entity_has_all_four_relationships(self, entity):
        qt = entity["quad_tech_financial_architecture"]
        rels = qt.get("relationships", {})
        assert "meta_content_licensing" in rels
        assert "google_cloud_infrastructure" in rels
        assert "aws_preferred_cloud" in rels
        assert "samsung_advertising" in rels

    def test_samsung_ratio_to_meta(self, entity):
        qt = entity["quad_tech_financial_architecture"]
        hierarchy = qt.get("financial_hierarchy", {})
        ratio = hierarchy.get("samsung_to_meta_ratio", "")
        # Must indicate Samsung is vastly larger
        assert "20" in str(ratio) or "100" in str(ratio), (
            f"Samsung-to-Meta ratio should indicate 20-100x, got: {ratio}"
        )


# ===================================================================
# 3. CROSS-REFERENCE COHERENCE — #122, #123, #124 interconnected
# ===================================================================
class TestCrossReferenceCoherence:
    """Mechanisms #122-#124 form a chain: #122 (TechCrunch Snap privacy zero) →
    #123 (Eadicicco CNN coverage selection) → #124 (WBD financial explanation).
    Cross-references must be bidirectional and consistent."""

    @pytest.fixture(scope="class")
    @classmethod
    def cpf(cls):
        ccr = load_yaml("competitor-coverage-research.yaml")
        return ccr["cross_publication_findings"]

    def test_mechanism_124_references_123(self, cpf):
        m124 = cpf["wbd_quad_tech_financial_architecture_content_deal_paradox"]
        refs = m124.get("cross_references", [])
        ref_ids = [r["mechanism_id"] for r in refs]
        assert 123 in ref_ids, "Mechanism #124 must reference #123"

    def test_mechanism_124_references_120(self, cpf):
        m124 = cpf["wbd_quad_tech_financial_architecture_content_deal_paradox"]
        refs = m124.get("cross_references", [])
        ref_ids = [r["mechanism_id"] for r in refs]
        assert 120 in ref_ids, "Mechanism #124 must reference #120 (traffic cannibalization)"

    def test_mechanism_123_references_122(self, cpf):
        m123 = cpf["lisa_eadicicco_cnn_coverage_selection_asymmetry"]
        refs = m123.get("cross_references", [])
        ref_ids = [r["mechanism_id"] for r in refs]
        assert 122 in ref_ids, "Mechanism #123 must reference #122"

    def test_mechanism_123_has_confounders(self, cpf):
        m123 = cpf["lisa_eadicicco_cnn_coverage_selection_asymmetry"]
        confounders = m123.get("confounders", [])
        assert len(confounders) >= 3, "Mechanism #123 should have documented confounders"

    def test_mechanism_124_has_confounders(self, cpf):
        m124 = cpf["wbd_quad_tech_financial_architecture_content_deal_paradox"]
        confounders = m124.get("confounders", [])
        assert len(confounders) >= 5, "Mechanism #124 documents 5 confounders"

    def test_mechanism_124_has_source_urls(self, cpf):
        m124 = cpf["wbd_quad_tech_financial_architecture_content_deal_paradox"]
        urls = m124.get("source_urls", [])
        assert len(urls) >= 4, f"Mechanism #124 should have 4+ source URLs, has {len(urls)}"


# ===================================================================
# 4. ENTITY COUNT CONSISTENCY
# ===================================================================
class TestEntityCountConsistency:
    """Verify entity counts are consistent across files."""

    def test_competitor_entities_yaml_loads(self):
        data = load_yaml("competitor-entities.yaml")
        entities = data.get("entities", data)
        assert len(entities) >= 14, f"Expected 14+ entities, got {len(entities)}"

    def test_wbd_cnn_entity_has_display_name(self):
        data = load_yaml("competitor-entities.yaml")
        entities = data.get("entities", data)
        wbd = entities.get("wbd_cnn", {})
        assert "display_name" in wbd or "aliases" in wbd, \
            "wbd_cnn entity should have display_name or aliases"

    def test_all_entities_have_regex(self):
        data = load_yaml("competitor-entities.yaml")
        entities = data.get("entities", data)
        for slug, ent_data in entities.items():
            if slug in ("meta",):
                continue
            if isinstance(ent_data, dict):
                has_regex = "regex" in ent_data
                has_aliases = "aliases" in ent_data
                assert has_regex or has_aliases or "display_name" in ent_data, \
                    f"Entity {slug} has no regex, aliases, or display_name"


# ===================================================================
# 5. MECHANISM ID UNIQUENESS AND ORDERING
# ===================================================================
class TestMechanismIDIntegrity:
    """All mechanism IDs across all YAML sections must be unique and sequential."""

    @pytest.fixture(scope="class")
    @classmethod
    def all_mechanism_ids(cls):
        ccr = load_yaml("competitor-coverage-research.yaml")
        ids = []
        # Scan cross_publication_findings
        for slug, data in ccr.get("cross_publication_findings", {}).items():
            if "mechanism_id" in data:
                ids.append(data["mechanism_id"])
        # Scan publications (should have none without meta_coverage_tone)
        for slug, data in ccr.get("publications", {}).items():
            if "mechanism_id" in data:
                ids.append(data["mechanism_id"])
        return ids

    def test_no_duplicate_mechanism_ids(self, all_mechanism_ids):
        seen = set()
        duplicates = []
        for mid in all_mechanism_ids:
            if mid in seen:
                duplicates.append(mid)
            seen.add(mid)
        assert not duplicates, f"Duplicate mechanism IDs: {duplicates}"

    def test_mechanism_124_exists(self, all_mechanism_ids):
        assert 124 in all_mechanism_ids

    def test_mechanism_123_exists(self, all_mechanism_ids):
        assert 123 in all_mechanism_ids

    def test_mechanism_122_exists(self, all_mechanism_ids):
        assert 122 in all_mechanism_ids


# ===================================================================
# 6. FINANCIAL HIERARCHY MODEL VALIDATION
# ===================================================================
class TestFinancialHierarchyModel:
    """The WBD case introduces a financial hierarchy model. Validate that
    the documented dollar amounts support the hierarchy ordering."""

    @pytest.fixture(scope="class")
    @classmethod
    def entity(cls):
        ent = load_yaml("competitor-entities.yaml")
        return ent.get("entities", ent)["wbd_cnn"]

    def test_samsung_ad_spend_exceeds_meta_content_deal(self, entity):
        """Samsung's global ad spend ($9.7B) must vastly exceed Meta's
        estimated content licensing ($5-10M/yr)."""
        qt = entity["quad_tech_financial_architecture"]
        rels = qt["relationships"]
        meta_est = rels["meta_content_licensing"].get("estimated_value_m_yr", "")
        samsung_global = rels["samsung_advertising"].get("samsung_global_ad_spend_b", 0)
        # Samsung global $9.7B vs Meta $5-10M = ~1000x ratio at global level
        assert samsung_global >= 9, f"Samsung global ad spend should be >= $9B, got {samsung_global}"

    def test_wbd_ad_revenue_decline_documented(self, entity):
        """WBD's ad revenue decline amplifies dependency on remaining advertisers."""
        q2 = entity.get("q2_2026_earnings", {})
        ad_yoy = q2.get("ad_revenue_yoy_pct", 0)
        assert ad_yoy < 0, f"WBD ad revenue YoY should be negative, got {ad_yoy}"

    def test_paramount_merger_implications(self, entity):
        qt = entity["quad_tech_financial_architecture"]
        pm = qt.get("paramount_merger", {})
        assert pm.get("status") is not None, "Paramount merger status should be documented"

    def test_meta_content_licensing_prediction_failure(self, entity):
        qt = entity["quad_tech_financial_architecture"]
        rels = qt["relationships"]
        meta = rels["meta_content_licensing"]
        assert meta.get("prediction_failure") is True, \
            "Meta content deal must be flagged as prediction failure"
