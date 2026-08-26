"""
Type D Cross-Validation: Regent LP Ownership Correction Propagation — Aug 26, 2026, 02:00 AM PT

VALIDATION TARGET: Mechanism #315 (Regent LP PE Media Empire Ownership Correction)

This cross-validation test verifies that the TechCrunch ownership correction from
Yahoo/Apollo to Regent LP (March 2025 acquisition) is properly propagated across
the MediaScope data model. Three verification layers:

1. ENTITY DATA INTEGRITY: competitor-entities.yaml correctly reflects TechCrunch
   under Regent LP (not Yahoo/Apollo) with proper alias/regex updates
2. MECHANISM CONSISTENCY: Mechanism #315 properly documents the correction and
   cross-references affected mechanisms (#104, #142)
3. CROSS-ENTITY FRAMING REATTRIBUTION: TechCrunch applies privacy/surveillance
   vocabulary to Meta glasses but neutral/product vocabulary to Snap Specs —
   a framing asymmetry that must now be explained through Regent LP's three-layer
   financial architecture (Apple affiliate dependency → cross-publication PE
   alignment → AI investment conflict) rather than Yahoo/Apollo's AI infrastructure
   financing chain

Evidence articles (all published 2026, under Regent LP ownership):
  - TechCrunch Mar 5, 2026: "Meta sued over AI smart glasses' privacy concerns,
    after workers reviewed nudity, sex, and other footage" — surveillance vocabulary
  - TechCrunch Mar 2, 2026: "A new app alerts you if someone nearby is wearing
    smart glasses" — quotes "luxury surveillance devices", "intolerable intrusion"
  - TechCrunch Jun 16, 2026: "Snap finally debuts its long-awaited AR glasses,
    Specs, and, oof, they aren't cheap" — zero privacy vocabulary despite cameras

Sources:
  - https://techcrunch.com/2026/03/05/meta-sued-over-ai-smartglasses-privacy-concerns-after-workers-reviewed-nudity-sex-and-other-footage/
  - https://techcrunch.com/2026/03/02/nearby-glasses-new-app-alerts-you-wearing-smart-glasses-surveillance-meta-snap-bluetooth/
  - https://techcrunch.com/2026/06/16/snap-finally-debuts-its-long-awaited-ar-glasses-specs-and-oof-they-arent-cheap/
  - https://techcrunch.com/2025/03/21/techcrunch-has-personal-news/ (Regent acquisition announcement)
  - https://siliconcanals.com/regent-acquires-techcrunch/
"""

import yaml
import os
import re
import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_yaml(rel_path):
    with open(os.path.join(REPO_ROOT, rel_path)) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def entities():
    return load_yaml("profiles/competitor-entities.yaml")


@pytest.fixture(scope="module")
def research():
    return load_yaml("profiles/competitor-coverage-research.yaml")


def find_mechanism(research_data, mech_id):
    """Search all sections of competitor-coverage-research.yaml for a mechanism by ID."""
    for section in ["publications", "aggregate_findings", "cross_publication_findings", "cross_entity_leverage"]:
        for key, val in research_data.get(section, {}).items():
            if isinstance(val, dict) and val.get("mechanism_id") == mech_id:
                return val
    return None


def all_mechanisms(research_data):
    """Yield all mechanism dicts from all sections."""
    for section in ["publications", "aggregate_findings", "cross_publication_findings", "cross_entity_leverage"]:
        for key, val in research_data.get(section, {}).items():
            if isinstance(val, dict) and "mechanism_id" in val:
                yield val


# ── Layer 1: Entity Data Integrity ─────────────────────────────────────

class TestRegentLPOwnssTechCrunch:
    """Verify competitor-entities.yaml correctly places TechCrunch under Regent LP."""

    def test_regent_lp_entity_exists(self, entities):
        assert "regent_lp" in entities["entities"]

    def test_techcrunch_in_regent_aliases(self, entities):
        regent = entities["entities"]["regent_lp"]
        aliases = regent.get("aliases", [])
        assert "TechCrunch" in aliases, \
            "TechCrunch must be listed in Regent LP aliases after ownership correction"

    def test_techcrunch_in_regent_regex(self, entities):
        regent = entities["entities"]["regent_lp"]
        regex = regent.get("regex", "")
        assert re.search(r"TechCrunch", regex), \
            "TechCrunch must appear in Regent LP regex pattern"

    def test_techcrunch_acquisition_in_history(self, entities):
        regent = entities["entities"]["regent_lp"]
        acquisitions = regent.get("acquisition_history", [])
        tc_acq = [a for a in acquisitions if a.get("entity") == "TechCrunch"]
        assert len(tc_acq) == 1, "Regent LP must have one TechCrunch acquisition entry"
        assert tc_acq[0]["year"] == 2025
        assert "March" in str(tc_acq[0].get("month", ""))

    def test_foundry_acquisition_in_history(self, entities):
        """Foundry (Macworld, PCWorld) acquisition should be documented too."""
        regent = entities["entities"]["regent_lp"]
        acquisitions = regent.get("acquisition_history", [])
        foundry_acq = [a for a in acquisitions if "Foundry" in str(a.get("entity", ""))]
        assert len(foundry_acq) >= 1


class TestYahooApolloNoLongerOwnsTechCrunch:
    """Verify TechCrunch has been removed from Yahoo/Apollo entity."""

    def test_yahoo_entity_exists(self, entities):
        assert "yahoo_apollo" in entities["entities"]

    def test_techcrunch_not_in_yahoo_aliases(self, entities):
        yahoo = entities["entities"]["yahoo_apollo"]
        aliases = yahoo.get("aliases", [])
        assert "TechCrunch" not in aliases, \
            "TechCrunch must NOT be in Yahoo/Apollo aliases after ownership correction"

    def test_techcrunch_not_in_yahoo_regex(self, entities):
        yahoo = entities["entities"]["yahoo_apollo"]
        regex = yahoo.get("regex", "")
        assert not re.search(r"TechCrunch", regex), \
            "TechCrunch must NOT appear in Yahoo/Apollo regex pattern"

    def test_engadget_still_in_yahoo(self, entities):
        """Engadget remains under Yahoo/Apollo — the correction only applies to TechCrunch."""
        yahoo = entities["entities"]["yahoo_apollo"]
        aliases = yahoo.get("aliases", [])
        assert "Engadget" in aliases, \
            "Engadget must remain in Yahoo/Apollo aliases (not affected by correction)"

    def test_yahoo_has_ownership_correction_note(self, entities):
        yahoo = entities["entities"]["yahoo_apollo"]
        yaml_str = yaml.dump(yahoo)
        assert "ownership_correction" in yaml_str.lower() or "correction" in yaml_str.lower(), \
            "Yahoo/Apollo entity should document the TechCrunch ownership correction"


# ── Layer 2: Mechanism Consistency ─────────────────────────────────────

class TestMechanism315OwnershipCorrection:
    """Verify mechanism #315 properly documents the ownership correction."""

    def test_mechanism_315_exists(self, research):
        m = find_mechanism(research, 315)
        assert m is not None, "Mechanism #315 must exist"

    def test_mechanism_315_is_correction_type(self, research):
        m = find_mechanism(research, 315)
        assert m is not None
        m_type = str(m.get("type", "")) + str(m.get("finding_type", ""))
        assert "correction" in m_type.lower(), \
            f"Mechanism #315 must be flagged as a correction type, got: {m_type}"

    def test_mechanism_315_references_affected_mechanisms(self, research):
        m = find_mechanism(research, 315)
        assert m is not None
        finding = str(m.get("finding", ""))
        assert "104" in finding or "142" in finding, \
            "Mechanism #315 must reference affected mechanisms #104 and/or #142"

    def test_mechanism_315_mentions_regent(self, research):
        m = find_mechanism(research, 315)
        assert m is not None
        finding = str(m.get("finding", ""))
        assert "Regent" in finding, \
            "Mechanism #315 must mention Regent LP as the correct owner"

    def test_mechanism_315_has_date(self, research):
        m = find_mechanism(research, 315)
        assert m is not None
        date = m.get("date_analyzed", m.get("date_added", ""))
        assert "2026-08-26" in str(date)


# ── Layer 3: Cross-Entity Framing Reattribution ────────────────────────

class TestTechCrunchFramingUnderRegentOwnership:
    """Verify that TechCrunch's Meta-vs-Snap framing asymmetry is consistent
    with Regent LP's financial architecture rather than Yahoo/Apollo's."""

    def test_regent_has_three_layer_architecture(self, entities):
        """Regent LP's financial incentive architecture must document three layers."""
        regent = entities["entities"]["regent_lp"]
        arch = regent.get("financial_incentive_architecture", {})
        arch_str = yaml.dump(arch)
        # Three layers: Apple ecosystem, cross-publication PE, AI investment
        assert "apple" in arch_str.lower(), "Layer 1: Apple ecosystem dependency"
        assert "cross" in arch_str.lower() and "publication" in arch_str.lower(), \
            "Layer 2: Cross-publication PE alignment"
        assert "investment" in arch_str.lower() or "lovable" in arch_str.lower(), \
            "Layer 3: AI investment conflict"

    def test_regent_has_disclosure_asymmetry_documented(self, entities):
        """The Lovable Series C disclosure asymmetry is a concrete proof of
        differential editorial standards within the Regent PE portfolio."""
        regent = entities["entities"]["regent_lp"]
        arch = regent.get("financial_incentive_architecture", {})
        disclosure = arch.get("disclosure_asymmetry", {})
        desc = str(disclosure.get("description", ""))
        assert "TechCrunch" in desc, "Disclosure asymmetry must mention TechCrunch"
        assert "Computerworld" in desc or "Military Times" in desc, \
            "Disclosure asymmetry must mention at least one other Regent publication"

    def test_regent_techcrunch_correction_explains_editorial_patterns(self, entities):
        """The correction section must offer alternative explanations for
        TechCrunch's adversarial Meta coverage under Regent (not Apollo)."""
        regent = entities["entities"]["regent_lp"]
        arch = regent.get("financial_incentive_architecture", {})
        correction = arch.get("techcrunch_ownership_correction", {})
        desc = str(correction.get("description", ""))
        # Should mention editorial inertia as a possible explanation
        assert "inertia" in desc.lower() or "editorial" in desc.lower(), \
            "Correction should discuss editorial inertia as alternative explanation"

    def test_meta_zero_financial_relationship_to_regent(self, entities):
        """Meta has no financial relationship to Regent LP, making the
        framing asymmetry harder to explain through financial incentives alone."""
        regent = entities["entities"]["regent_lp"]
        arch = regent.get("financial_incentive_architecture", {})
        arch_str = yaml.dump(arch).lower()
        assert "meta" in arch_str and "zero" in arch_str, \
            "Architecture should note Meta's zero financial relationship with Regent"


class TestCrossValidationWithExistingTests:
    """Verify that the ownership correction doesn't break consistency
    with existing test assertions about TechCrunch mechanisms."""

    def test_existing_yahoo_tests_still_valid_as_framing_tests(self, research):
        """The Yahoo/Apollo tests (#104) test FRAMING PATTERNS that are
        real and documented. The framing asymmetry exists regardless of who owns
        TechCrunch. The tests remain valid as evidence of differential coverage;
        only the causal attribution changes."""
        m = find_mechanism(research, 104)
        assert m is not None, "Mechanism #104 must still exist (framing patterns are valid)"
        assert "finding" in m or "finding_summary" in m

    def test_mechanism_count_consistency(self, research):
        """After adding #315, total mechanism count should be at least 315."""
        max_id = max(
            (m.get("mechanism_id", 0) for m in all_mechanisms(research)),
            default=0
        )
        assert max_id >= 315, \
            f"Highest mechanism ID should be >= 315, got {max_id}"


class TestRegentLPCategoryAndMetadata:
    """Verify Regent LP entity has proper categorical metadata for
    the asymmetry scoring system to process it correctly."""

    def test_category_is_pe_or_media(self, entities):
        regent = entities["entities"]["regent_lp"]
        category = regent.get("category", "")
        assert "pe" in category.lower() or "media" in category.lower(), \
            f"Regent LP category should indicate PE/media, got: {category}"

    def test_has_ai_investments(self, entities):
        regent = entities["entities"]["regent_lp"]
        assert "ai_investments" in regent, "Regent LP must have ai_investments section"
        assert "lovable" in regent["ai_investments"], "Lovable investment must be documented"

    def test_lovable_valuation(self, entities):
        regent = entities["entities"]["regent_lp"]
        lovable = regent["ai_investments"]["lovable"]
        assert lovable.get("valuation_b") == 13.3 or str(lovable.get("valuation_b", "")) == "13.3"

    def test_lovable_round_size(self, entities):
        regent = entities["entities"]["regent_lp"]
        lovable = regent["ai_investments"]["lovable"]
        assert lovable.get("round_size_m") == 400 or str(lovable.get("round_size_m", "")) == "400"

    def test_has_sources_for_lovable(self, entities):
        regent = entities["entities"]["regent_lp"]
        lovable = regent["ai_investments"]["lovable"]
        sources = lovable.get("sources", [])
        assert len(sources) >= 3, "Lovable investment should have at least 3 sources"
        source_urls = [s.get("url", "") for s in sources]
        tc_source = any("techcrunch.com" in u for u in source_urls)
        assert tc_source, "TechCrunch's own Lovable disclosure article must be cited"
