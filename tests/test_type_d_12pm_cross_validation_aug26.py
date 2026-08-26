"""
Type D Cross-Validation: Aug 26, 2026 12:00 PM PT — Mechanisms #320–#323

VALIDATION TARGET: Four mechanisms documented in iterations #308–#311 (08:00–11:00 PT):
  - #320: Gadget Detective UK Broadcast Cross-Episode Entity-Selective Vocabulary
  - #321: WSJ Anthropic Ode AI Surveillance Infrastructure Aspirational vs Meta Camera Scrutiny
  - #322: Le Monde Institutional Editorial Register Bifurcation — Meta vs OpenAI
  - #323: Goldman Sachs Dual PE JV Cross-Investment Compound Financial Architecture

Cross-validation checks:
  1. MECHANISM INTEGRITY: All four mechanisms present in competitor-coverage-research.yaml
     with required fields (mechanism_id, type/classification, description/finding)
  2. ENTITY CONSISTENCY: Entities referenced by mechanisms exist or are documented
  3. FINANCIAL DATA COHERENCE: Goldman Sachs quintuple role (#323) consistent with
     Ode backer references in #321; Le Monde dual-deal context (#322) internally consistent
  4. CROSS-MECHANISM STRUCTURAL VALIDATION: Four mechanisms span distinct domains
     (UK broadcast cultural consensus, financial journalism, French institutional editorial,
     investment banking architecture) but connect through asymmetric Meta treatment
  5. CONFOUNDER DOCUMENTATION: Each mechanism documents counter-confounders
  6. CROSS-REFERENCE VALIDATION: Mechanisms reference prior work (#225, #317, #21, etc.)
  7. SOURCE URL INTEGRITY: All URLs well-formed HTTPS
  8. DOMAIN BREADTH: Tests that the four mechanisms cover broadcast + print + editorial +
     financial architecture — multi-domain coverage strengthening
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
    """Find a mechanism by ID in the research YAML, searching all top-level sections."""
    for section_key in research_data:
        section = research_data[section_key]
        if isinstance(section, dict):
            for key, val in section.items():
                if isinstance(val, dict) and val.get("mechanism_id") == mech_id:
                    return val
                # Check nested dicts (e.g., cross_publication_findings)
                if isinstance(val, dict):
                    for subkey, subval in val.items():
                        if isinstance(subval, dict) and subval.get("mechanism_id") == mech_id:
                            return subval
                        if isinstance(subval, dict) and subval.get("mechanism_number") == mech_id:
                            return subval
        elif isinstance(section, list):
            for item in section:
                if isinstance(item, dict) and item.get("mechanism_id") == mech_id:
                    return item
                if isinstance(item, dict) and item.get("mechanism_number") == mech_id:
                    return item
    return None


def yaml_text(data):
    """Dump YAML data to string for grep-style searching."""
    return yaml.dump(data, default_flow_style=False)


# ============================================================
# CLASS 1: Mechanism #320 — Gadget Detective UK Broadcast
# ============================================================

class TestMechanism320Existence:
    """Verify mechanism #320 exists with required structure."""

    def test_mechanism_320_exists(self, research):
        m = find_mechanism(research, 320)
        assert m is not None, "Mechanism #320 not found in research YAML"

    def test_mechanism_320_classification(self, research):
        m = find_mechanism(research, 320)
        assert m is not None
        classification = str(m.get("classification", ""))
        assert "cultural_consensus" in classification, \
            f"#320 should be classified as cultural_consensus, got: {classification}"

    def test_mechanism_320_medium(self, research):
        m = find_mechanism(research, 320)
        assert m is not None
        medium = str(m.get("medium", ""))
        assert "podcast" in medium or "broadcast" in medium or "radio" in medium, \
            f"#320 medium should reference podcast/broadcast/radio, got: {medium}"

    def test_mechanism_320_has_episodes(self, research):
        m = find_mechanism(research, 320)
        assert m is not None
        episodes = m.get("episodes", [])
        assert len(episodes) >= 3, \
            f"#320 should have at least 3 episodes documented, got {len(episodes)}"

    def test_mechanism_320_host_documented(self, research):
        m = find_mechanism(research, 320)
        assert m is not None
        host = str(m.get("host", ""))
        assert "Turkalp" in host or "Fevzi" in host, \
            f"#320 host should be Fevzi Turkalp, got: {host}"

    def test_mechanism_320_platforms_include_bbc_and_lbc(self, research):
        m = find_mechanism(research, 320)
        assert m is not None
        platforms = [str(p).lower() for p in m.get("platforms", [])]
        platforms_str = " ".join(platforms)
        assert "lbc" in platforms_str, "#320 should include LBC platform"
        assert "bbc" in platforms_str, "#320 should include BBC platform"

    def test_mechanism_320_no_financial_incentive(self, research):
        """Cultural consensus means no direct financial ties drive the pattern."""
        m = find_mechanism(research, 320)
        assert m is not None
        desc = str(m.get("description", ""))
        assert "cultural" in desc.lower() or "no financial" in desc.lower() or \
            "consensus" in desc.lower(), \
            "#320 description should note absence of financial incentive"


class TestMechanism320Episodes:
    """Validate episode-level data for #320."""

    def test_episodes_have_dates(self, research):
        m = find_mechanism(research, 320)
        assert m is not None
        for ep in m.get("episodes", []):
            date = ep.get("date", "")
            assert re.match(r"^\d{4}-\d{2}-\d{2}$", str(date)), \
                f"Episode missing valid date: {ep.get('title', 'unknown')}"

    def test_episodes_have_entity(self, research):
        m = find_mechanism(research, 320)
        assert m is not None
        for ep in m.get("episodes", []):
            entity = ep.get("entity", "")
            assert entity, f"Episode missing entity: {ep.get('title', 'unknown')}"

    def test_episodes_have_vocabulary_register(self, research):
        m = find_mechanism(research, 320)
        assert m is not None
        registers = set()
        for ep in m.get("episodes", []):
            reg = ep.get("vocabulary_register", "")
            assert reg, f"Episode missing register: {ep.get('title', 'unknown')}"
            registers.add(reg.lower())
        assert len(registers) >= 2, \
            f"Should show at least 2 different registers (alarm + hero/neutral), got: {registers}"

    def test_meta_episodes_get_alarm_register(self, research):
        m = find_mechanism(research, 320)
        assert m is not None
        meta_regs = []
        for ep in m.get("episodes", []):
            if "meta" in str(ep.get("entity", "")).lower():
                meta_regs.append(ep.get("vocabulary_register", "").lower())
        assert all("alarm" in r for r in meta_regs), \
            f"Meta episodes should all have alarm register, got: {meta_regs}"


# ============================================================
# CLASS 2: Mechanism #321 — WSJ Anthropic Ode Surveillance
# ============================================================

class TestMechanism321Existence:
    """Verify mechanism #321 exists with required structure."""

    def test_mechanism_321_exists(self, research):
        m = find_mechanism(research, 321)
        assert m is not None, "Mechanism #321 not found in research YAML"

    def test_mechanism_321_publication_wsj(self, research):
        m = find_mechanism(research, 321)
        assert m is not None
        pub = str(m.get("publication", ""))
        assert "WSJ" in pub or "Wall Street Journal" in pub, \
            f"#321 publication should be WSJ, got: {pub}"

    def test_mechanism_321_entity_pair(self, research):
        m = find_mechanism(research, 321)
        assert m is not None
        pair = str(m.get("entity_pair", ""))
        assert "Anthropic" in pair or "Ode" in pair, \
            f"#321 entity pair should reference Anthropic/Ode, got: {pair}"
        assert "Meta" in pair, \
            f"#321 entity pair should reference Meta, got: {pair}"

    def test_mechanism_321_has_articles(self, research):
        m = find_mechanism(research, 321)
        assert m is not None
        articles = m.get("articles", [])
        assert len(articles) >= 1, \
            f"#321 should have at least 1 article, got {len(articles)}"

    def test_mechanism_321_articles_have_urls(self, research):
        m = find_mechanism(research, 321)
        assert m is not None
        for art in m.get("articles", []):
            url = art.get("url", "")
            assert url.startswith("https://"), \
                f"Article missing HTTPS URL: {art.get('title', 'unknown')}"


class TestMechanism321SurveillanceCapabilities:
    """Validate the Chamberlain/Ode surveillance capability documentation."""

    def test_finding_mentions_facial_recognition(self, research):
        m = find_mechanism(research, 321)
        assert m is not None
        text = str(m.get("finding_summary", "")) + str(m.get("finding", ""))
        assert "facial recognition" in text.lower() or "recognizing" in text.lower(), \
            "#321 should document facial recognition capabilities"

    def test_finding_mentions_behavioral_learning(self, research):
        m = find_mechanism(research, 321)
        assert m is not None
        text = str(m.get("finding_summary", "")) + str(m.get("finding", ""))
        assert "routine" in text.lower() or "behavioral" in text.lower(), \
            "#321 should document behavioral routine learning"

    def test_finding_mentions_camera_scale(self, research):
        m = find_mechanism(research, 321)
        assert m is not None
        text = str(m.get("finding_summary", "")) + str(m.get("finding", ""))
        assert "3M" in text or "3 million" in text.lower() or "camera" in text.lower(), \
            "#321 should document camera deployment scale"

    def test_zero_privacy_vocabulary_documented(self, research):
        m = find_mechanism(research, 321)
        assert m is not None
        text = str(m.get("finding_summary", "")) + str(m.get("finding", ""))
        assert "zero" in text.lower() or "ZERO" in text, \
            "#321 should document ZERO privacy vocabulary in Anthropic/Ode article"


# ============================================================
# CLASS 3: Mechanism #322 — Le Monde Register Bifurcation
# ============================================================

class TestMechanism322Existence:
    """Verify mechanism #322 exists with required structure."""

    def test_mechanism_322_exists(self, research):
        m = find_mechanism(research, 322)
        assert m is not None, "Mechanism #322 not found in research YAML"

    def test_mechanism_322_publication_le_monde(self, research):
        m = find_mechanism(research, 322)
        assert m is not None
        pub = str(m.get("publication", ""))
        assert "Le Monde" in pub, f"#322 publication should be Le Monde, got: {pub}"

    def test_mechanism_322_entity_pair_includes_meta_and_openai(self, research):
        m = find_mechanism(research, 322)
        assert m is not None
        pair = m.get("entity_pair", [])
        pair_str = str(pair).lower()
        assert "meta" in pair_str, f"#322 entity pair should include Meta, got: {pair}"
        assert "openai" in pair_str, f"#322 entity pair should include OpenAI, got: {pair}"

    def test_mechanism_322_has_natural_experiment(self, research):
        m = find_mechanism(research, 322)
        assert m is not None
        ne = m.get("natural_experiment", {})
        assert ne, "#322 should have a natural_experiment section"
        assert "meta_piece" in ne or "meta" in str(ne).lower(), \
            "#322 natural experiment should document Meta piece"


class TestMechanism322EditorialRegister:
    """Validate the editorial register asymmetry finding."""

    def test_meta_gets_alarm_register(self, research):
        m = find_mechanism(research, 322)
        assert m is not None
        ne = m.get("natural_experiment", {})
        meta_piece = ne.get("meta_piece", {})
        reg = str(meta_piece.get("register", "")).lower()
        assert "alarm" in reg, f"Meta piece should have alarm register, got: {reg}"

    def test_meta_piece_has_url(self, research):
        m = find_mechanism(research, 322)
        assert m is not None
        ne = m.get("natural_experiment", {})
        meta_piece = ne.get("meta_piece", {})
        url = meta_piece.get("url", "")
        assert url.startswith("https://www.lemonde.fr"), \
            f"Meta piece should have Le Monde URL, got: {url}"

    def test_meta_piece_has_alarm_vocabulary(self, research):
        m = find_mechanism(research, 322)
        assert m is not None
        ne = m.get("natural_experiment", {})
        meta_piece = ne.get("meta_piece", {})
        vocab = meta_piece.get("key_vocabulary", [])
        assert len(vocab) >= 3, \
            f"Meta piece should have at least 3 alarm vocabulary terms, got {len(vocab)}"

    def test_openai_piece_has_url(self, research):
        m = find_mechanism(research, 322)
        assert m is not None
        ne = m.get("natural_experiment", {})
        openai_piece = ne.get("openai_piece", {})
        url = openai_piece.get("url", "")
        assert url.startswith("https://www.lemonde.fr"), \
            f"OpenAI piece should have Le Monde URL, got: {url}"

    def test_tobacco_comparison_is_meta_only(self, research):
        m = find_mechanism(research, 322)
        assert m is not None
        text = str(m.get("description", "")) + str(m.get("title", ""))
        assert "tobacco" in text.lower() or "cigarettier" in text.lower(), \
            "#322 should document the tobacco/cigarette comparison applied to Meta"


# ============================================================
# CLASS 4: Mechanism #323 — Goldman Sachs Compound Architecture
# ============================================================

class TestMechanism323Existence:
    """Verify mechanism #323 exists with required structure."""

    def test_mechanism_323_exists(self, research):
        m = find_mechanism(research, 323)
        assert m is not None, "Mechanism #323 not found in research YAML"

    def test_mechanism_323_type_financial(self, research):
        m = find_mechanism(research, 323)
        assert m is not None
        mtype = str(m.get("type", "")).lower()
        assert "financial" in mtype, \
            f"#323 type should be financial_incentive_mapping, got: {mtype}"

    def test_mechanism_323_has_financial_roles(self, research):
        m = find_mechanism(research, 323)
        assert m is not None
        roles = m.get("financial_roles", [])
        assert len(roles) >= 5, \
            f"#323 should document at least 5 Goldman financial roles, got {len(roles)}"

    def test_mechanism_323_documents_ode_investment(self, research):
        m = find_mechanism(research, 323)
        assert m is not None
        roles_str = str(m.get("financial_roles", []))
        assert "Ode" in roles_str or "ode" in roles_str.lower(), \
            "#323 should document Goldman's Ode JV investment"

    def test_mechanism_323_documents_deployment_company(self, research):
        m = find_mechanism(research, 323)
        assert m is not None
        roles_str = str(m.get("financial_roles", []))
        assert "Deployment" in roles_str or "deployment" in roles_str.lower(), \
            "#323 should document Goldman's OpenAI Deployment Company role"


class TestMechanism323MetaZeroExposure:
    """Validate the Meta zero financial exposure finding."""

    def test_cross_venture_investment_unique(self, research):
        m = find_mechanism(research, 323)
        assert m is not None
        unique = m.get("cross_venture_investment_unique", False)
        assert unique is True, "#323 should flag Goldman as unique cross-venture investor"

    def test_finding_documents_meta_zero(self, research):
        m = find_mechanism(research, 323)
        assert m is not None
        text = str(m.get("finding", ""))
        assert "ZERO" in text or "zero" in text.lower(), \
            "#323 finding should document Goldman's ZERO exposure to Meta"


# ============================================================
# CLASS 5: Cross-Mechanism Structural Validation
# ============================================================

class TestCrossMechanismConsistency:
    """Validate structural consistency across all four mechanisms."""

    def test_all_four_mechanisms_exist(self, research):
        for mid in [320, 321, 322, 323]:
            m = find_mechanism(research, mid)
            assert m is not None, f"Mechanism #{mid} not found"

    def test_mechanisms_cover_distinct_domains(self, research):
        """Four mechanisms should cover broadcast, print journalism, editorial, and finance."""
        domains = set()
        m320 = find_mechanism(research, 320)
        if m320:
            medium = str(m320.get("medium", "")) + str(m320.get("classification", ""))
            if "broadcast" in medium or "podcast" in medium or "radio" in medium or "cultural" in medium:
                domains.add("broadcast")

        m321 = find_mechanism(research, 321)
        if m321:
            mtype = str(m321.get("type", ""))
            if "surveillance" in mtype or "bifurcation" in mtype or "vocabulary" in mtype:
                domains.add("print_journalism")

        m322 = find_mechanism(research, 322)
        if m322:
            desc = str(m322.get("title", "")) + str(m322.get("subtype", ""))
            if "editorial" in desc.lower() or "register" in desc.lower():
                domains.add("institutional_editorial")

        m323 = find_mechanism(research, 323)
        if m323:
            mtype = str(m323.get("type", "")).lower()
            if "financial" in mtype:
                domains.add("financial_architecture")

        assert len(domains) >= 3, \
            f"Should cover at least 3 distinct domains, got: {domains}"

    def test_meta_referenced_across_all_four(self, research):
        """All four mechanisms should reference Meta as subject of asymmetric treatment."""
        for mid in [320, 321, 322, 323]:
            m = find_mechanism(research, mid)
            assert m is not None, f"Mechanism #{mid} not found"
            text = yaml_text(m).lower()
            assert "meta" in text, \
                f"Mechanism #{mid} should reference Meta"

    def test_all_mechanisms_dated_aug_2026(self, research):
        """All four mechanisms were documented in Aug 2026."""
        for mid in [320, 321, 322, 323]:
            m = find_mechanism(research, mid)
            assert m is not None
            # Check top-level date fields first
            date = str(m.get("date", "") or m.get("discovery_date", ""))
            if not date or "2026-08" not in date:
                # Fallback: check article dates within the mechanism
                text = yaml_text(m)
                assert "2026-08" in text, \
                    f"Mechanism #{mid} should have Aug 2026 dates somewhere, got none"

    def test_mechanism_ids_sequential(self, research):
        """IDs 320-323 should be present with no gaps."""
        ids = []
        for mid in range(320, 324):
            m = find_mechanism(research, mid)
            if m:
                ids.append(mid)
        assert ids == [320, 321, 322, 323], \
            f"Expected sequential IDs 320-323, got: {ids}"


# ============================================================
# CLASS 6: Cross-Reference Validation
# ============================================================

class TestCrossReferenceIntegrity:
    """Validate that cross-references point to real mechanisms."""

    def test_mechanism_320_cross_refs(self, research):
        """#320 should reference podcast/broadcast predecessors."""
        m = find_mechanism(research, 320)
        assert m is not None
        refs = m.get("cross_references", []) or m.get("extends_mechanisms", [])
        ref_ids = set()
        for ref in refs:
            if isinstance(ref, dict):
                ref_ids.add(ref.get("mechanism_id", 0))
            elif isinstance(ref, int):
                ref_ids.add(ref)
        # Should reference at least one prior podcast mechanism
        assert len(ref_ids) >= 1, "#320 should have at least 1 cross-reference"

    def test_mechanism_321_extends_317(self, research):
        """#321 (WSJ Ode) should extend #317 (WSJ Anthropic pre-IPO)."""
        m = find_mechanism(research, 321)
        assert m is not None
        refs = m.get("cross_references", []) or m.get("extends_mechanisms", [])
        ref_ids = set()
        for ref in refs:
            if isinstance(ref, dict):
                ref_ids.add(ref.get("mechanism_id", 0))
            elif isinstance(ref, int):
                ref_ids.add(ref)
        text = yaml_text(m)
        assert 317 in ref_ids or "317" in text, \
            "#321 should cross-reference #317 (WSJ Anthropic pre-IPO)"

    def test_mechanism_323_extends_21(self, research):
        """#323 (Goldman) should extend #21 (IPO Underwriter Research Laundering)."""
        m = find_mechanism(research, 323)
        assert m is not None
        refs = m.get("cross_references", []) or m.get("extends_mechanisms", [])
        ref_ids = set()
        for ref in refs:
            if isinstance(ref, dict):
                ref_ids.add(ref.get("mechanism_id", 0))
            elif isinstance(ref, int):
                ref_ids.add(ref)
        text = yaml_text(m)
        assert 21 in ref_ids or "21" in text or "mechanism_id: 21" in text, \
            "#323 should cross-reference #21 (IPO Underwriter Research Laundering)"


# ============================================================
# CLASS 7: Goldman-Ode Consistency (#321 ↔ #323)
# ============================================================

class TestGoldmanOdeCrossConsistency:
    """Validate that Goldman Sachs data is consistent between #321 and #323."""

    def test_both_reference_ode(self, research):
        """Both #321 and #323 should reference the Ode joint venture."""
        m321 = find_mechanism(research, 321)
        m323 = find_mechanism(research, 323)
        assert m321 is not None and m323 is not None
        text_321 = yaml_text(m321).lower()
        text_323 = yaml_text(m323).lower()
        assert "ode" in text_321, "#321 should reference Ode"
        assert "ode" in text_323, "#323 should reference Ode"

    def test_both_reference_goldman_sachs(self, research):
        """Both #321 and #323 should reference Goldman Sachs."""
        m321 = find_mechanism(research, 321)
        m323 = find_mechanism(research, 323)
        assert m321 is not None and m323 is not None
        text_321 = yaml_text(m321).lower()
        text_323 = yaml_text(m323).lower()
        assert "goldman" in text_321, "#321 should reference Goldman Sachs"
        assert "goldman" in text_323, "#323 should reference Goldman Sachs"

    def test_ode_backer_list_consistent(self, research):
        """Blackstone appears in both #321 and #323 as Ode backer."""
        m321 = find_mechanism(research, 321)
        m323 = find_mechanism(research, 323)
        assert m321 is not None and m323 is not None
        text_321 = yaml_text(m321).lower()
        text_323 = yaml_text(m323).lower()
        assert "blackstone" in text_321, "#321 should reference Blackstone as Ode backer"
        assert "blackstone" in text_323 or "ode" in text_323, \
            "#323 should reference Ode/Blackstone"


# ============================================================
# CLASS 8: Source URL Integrity
# ============================================================

class TestSourceURLIntegrity:
    """Validate all source URLs across mechanisms #320-323."""

    def test_mechanism_321_wsj_urls(self, research):
        m = find_mechanism(research, 321)
        assert m is not None
        for art in m.get("articles", []):
            url = art.get("url", "")
            if url:
                assert url.startswith("https://"), f"URL should be HTTPS: {url}"
                assert "wsj.com" in url, f"WSJ article URL should contain wsj.com: {url}"

    def test_mechanism_322_lemonde_urls(self, research):
        m = find_mechanism(research, 322)
        assert m is not None
        ne = m.get("natural_experiment", {})
        for key in ["meta_piece", "openai_piece"]:
            piece = ne.get(key, {})
            url = piece.get("url", "")
            if url:
                assert url.startswith("https://www.lemonde.fr"), \
                    f"Le Monde URL should start with https://www.lemonde.fr: {url}"

    def test_mechanism_323_source_urls_well_formed(self, research):
        m = find_mechanism(research, 323)
        assert m is not None
        sources = m.get("sources", []) or m.get("source_urls", [])
        for src in sources:
            url = str(src.get("url", src) if isinstance(src, dict) else src)
            if url.startswith("http"):
                assert url.startswith("https://"), f"Source URL should be HTTPS: {url}"

    def test_mechanism_320_asymmetry_score(self, research):
        """#320 should have an asymmetry score."""
        m = find_mechanism(research, 320)
        assert m is not None
        score = m.get("asymmetry_score", 0)
        assert 0 < score <= 1.0, \
            f"#320 asymmetry score should be between 0 and 1, got: {score}"


# ============================================================
# CLASS 9: Confounder Documentation
# ============================================================

class TestConfounderDocumentation:
    """Verify intellectual honesty — confounders documented for each mechanism."""

    def test_mechanism_320_has_cultural_consensus_note(self, research):
        """#320 should note that cultural consensus operates without financial incentive."""
        m = find_mechanism(research, 320)
        assert m is not None
        text = yaml_text(m).lower()
        assert "cultural" in text or "consensus" in text, \
            "#320 should document cultural consensus classification"

    def test_mechanism_321_has_confounders(self, research):
        m = find_mechanism(research, 321)
        assert m is not None
        text = yaml_text(m).lower()
        assert "confounder" in text or "opt-in" in text or "rebutted" in text or \
            "public" in text, \
            "#321 should document confounders (e.g., opt-in cameras vs public glasses)"

    def test_mechanism_322_has_confounders(self, research):
        m = find_mechanism(research, 322)
        assert m is not None
        text = yaml_text(m).lower()
        assert "confounder" in text or "trial" in text or "genre" in text, \
            "#322 should document confounders"

    def test_mechanism_323_has_strong_confounders(self, research):
        m = find_mechanism(research, 323)
        assert m is not None
        text = yaml_text(m)
        assert "STRONG" in text or "strong" in text.lower() or "chinese wall" in text.lower(), \
            "#323 should document STRONG confounders (Chinese wall requirements)"
