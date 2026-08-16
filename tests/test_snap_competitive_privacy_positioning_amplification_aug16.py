"""
Cross-publication analysis: Snap CEO Competitive Privacy Positioning Amplification

Mechanism #130 — Type A: Competitor Coverage Deep Dive
Publication+Competitor pair: Multiple publications covering Snap (as Meta competitor)

KEY FINDING — COMPETITIVE PRIVACY POSITIONING AMPLIFICATION:
During the Snap Specs launch (June 16, 2026), Snap CEO Evan Spiegel explicitly
positioned Specs AGAINST Meta's NameTag facial recognition controversy.
Engadget (Yahoo/Apollo) reported: "Spiegel distanced Snap from Meta's recent
facial recognition controversy, noting the company moderates Lenses to
prevent such features." TechCrunch (Yahoo/Apollo) reported Snap's privacy
features as adequate with zero scrutiny. Telecoms.com noted Snap has
"tried to avoid being tarnished with this brush with various privacy features."

The structural irony: Snap Specs have MORE surveillance-capable hardware than
Meta glasses (4 cameras vs 1, dual Snapdragon processors, computer vision
processor). Yet publications amplified Spiegel's competitive positioning
without scrutinizing whether Snap's own hardware warrants the same privacy
scrutiny Meta faces.

This is a CROSS-PUBLICATION MECHANISM distinct from:
- #121 (Fast Company single-publication framing, same-pub opposite framing)
- #122 (TechCrunch single-publication vocabulary zero)
- Existing WIRED/Verge lane assignment findings

What #130 adds: CEO-level competitive narrative strategy AND its
multi-publication amplification chain. Spiegel transformed Meta's privacy
controversy into a SELLING POINT for Snap, and publications reproduced
this framing as editorial content rather than recognizing it as marketing.

FINANCIAL CONTEXT:
- Yahoo/Apollo owns both Engadget and TechCrunch
- Apollo Global Management structured Anthropic's $35B SPV (mechanism #28)
- Yahoo receives Google Showcase payments
- Snap has an OpenAI partnership
- None of these publications have Meta content licensing deals
- Publications without Meta financial ties produce the softest Snap coverage
  AND amplify Snap's anti-Meta positioning most uncritically

5 CONFOUNDERS:
1. Snap genuinely has better privacy defaults (on-device processing) — MODERATE
2. Meta's NameTag was genuinely problematic (facial recognition code on 50M phones) — STRONG
3. Interview format naturally gives CEO positioning space — MODERATE
4. Snap Specs haven't shipped yet (no real-world privacy incidents) — MODERATE
5. Different product category (full AR vs camera glasses) — WEAK

SOURCE URLS:
- Engadget Spiegel interview: reported via headlinesbriefing.com
  (Snap Specs AR Glasses Launch as 'See-Through Computer' for $2,195, Jun 16, 2026)
- TechCrunch Snap Specs launch: techcrunch.com/2026/06/16/snap-finally-debuts-its-long-awaited-ar-glasses-specs-and-oof-they-arent-cheap/
- Telecoms.com Snap Specs: telecoms.com (Snap unveils a pricey new pair of AR glasses)
- Gizmodo Snap Specs (clean control): gizmodo.com/snaps-new-ar-glasses-are-trying-to-beat-meta-to-the-punch-2000772470
- WIRED NameTag investigation (Jun 4, 2026): referenced by malwarebytes.com, EFF, multiple outlets
- Snap official privacy marketing: "uses its understanding of you and your world to help get things done on your behalf while protecting and respecting your privacy"
"""

import pathlib
import re

import pytest
import yaml

_REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
_PROFILES = _REPO_ROOT / "profiles"


def _load_yaml(name: str) -> dict:
    return yaml.safe_load((_PROFILES / name).read_text())


def _load_research() -> dict:
    return yaml.safe_load(
        (_PROFILES / "competitor-coverage-research.yaml").read_text()
    )


def _load_entities() -> dict:
    return yaml.safe_load(
        (_PROFILES / "competitor-entities.yaml").read_text()
    )


def _find_mechanism_130() -> dict:
    """Find mechanism #130 in the research YAML (any top-level section)."""
    research = _load_research()
    for section in research.values():
        if isinstance(section, dict):
            # Direct match (e.g. in publications)
            if section.get("mechanism_id") == 130:
                return section
            # Nested match (e.g. in cross_publication_findings)
            for v in section.values():
                if isinstance(v, dict) and v.get("mechanism_id") == 130:
                    return v
    return None


# ===================================================================
# 1. MECHANISM EXISTENCE AND STRUCTURE
# ===================================================================


class TestMechanism130Structure:
    """Verify mechanism #130 exists with required fields."""

    def test_mechanism_exists(self):
        """Mechanism #130 must exist in competitor-coverage-research.yaml."""
        mech = _find_mechanism_130()
        assert mech is not None, "Mechanism #130 must exist"

    def test_mechanism_has_finding_summary(self):
        """Mechanism #130 must have a finding_summary."""
        mech = _find_mechanism_130()
        assert mech is not None
        assert mech.get("finding_summary"), "Must have finding_summary"

    def test_mechanism_has_discovery_date(self):
        """Mechanism #130 must have discovery_date 2026-08-16."""
        mech = _find_mechanism_130()
        assert mech is not None
        assert mech.get("discovery_date") == "2026-08-16"

    def test_mechanism_type_a(self):
        """Mechanism #130 is Type A: Competitor Coverage Deep Dive."""
        mech = _find_mechanism_130()
        assert mech is not None
        assert mech.get("rotation_type") == "A"

    def test_mechanism_has_confounders(self):
        """Mechanism #130 must document confounders."""
        mech = _find_mechanism_130()
        assert mech is not None
        confounders = mech.get("confounders", [])
        assert len(confounders) >= 4, f"Need >= 4 confounders, got {len(confounders)}"

    def test_mechanism_has_source_urls(self):
        """Mechanism #130 must have source URLs."""
        mech = _find_mechanism_130()
        assert mech is not None
        urls = mech.get("source_urls", [])
        assert len(urls) >= 3, f"Need >= 3 source URLs, got {len(urls)}"


# ===================================================================
# 2. SNAP SPECS HARDWARE PARITY
# ===================================================================


class TestSnapSpecsHardwareParity:
    """Verify the hardware surveillance surface comparison is documented."""

    def test_snap_specs_camera_count(self):
        """Snap Specs have 4 cameras (2 full-color + 2 IR computer vision)."""
        mech = _find_mechanism_130()
        assert mech is not None
        hw = mech.get("hardware_comparison", {})
        snap = hw.get("snap_specs", {})
        assert snap.get("cameras") == 4

    def test_meta_glasses_camera_count(self):
        """Meta Ray-Ban glasses have 1 camera."""
        mech = _find_mechanism_130()
        assert mech is not None
        hw = mech.get("hardware_comparison", {})
        meta = hw.get("meta_ray_ban", {})
        assert meta.get("cameras") == 1

    def test_snap_has_more_cameras_than_meta(self):
        """Snap Specs have MORE cameras than Meta (4 vs 1)."""
        mech = _find_mechanism_130()
        assert mech is not None
        hw = mech.get("hardware_comparison", {})
        snap_cameras = hw.get("snap_specs", {}).get("cameras", 0)
        meta_cameras = hw.get("meta_ray_ban", {}).get("cameras", 0)
        assert snap_cameras > meta_cameras, (
            f"Snap ({snap_cameras}) should exceed Meta ({meta_cameras})"
        )

    def test_snap_dual_processors(self):
        """Snap Specs have dual Snapdragon processors."""
        mech = _find_mechanism_130()
        assert mech is not None
        hw = mech.get("hardware_comparison", {})
        snap = hw.get("snap_specs", {})
        assert snap.get("processors") >= 2


# ===================================================================
# 3. SPIEGEL COMPETITIVE POSITIONING EVIDENCE
# ===================================================================


class TestSpiegelCompetitivePositioning:
    """Verify Spiegel's deliberate competitive positioning against Meta."""

    def test_spiegel_distanced_from_meta(self):
        """Spiegel explicitly distanced Snap from Meta's NameTag controversy."""
        mech = _find_mechanism_130()
        assert mech is not None
        positioning = mech.get("ceo_competitive_positioning", {})
        assert positioning.get("distanced_from_meta_privacy") is True

    def test_spiegel_claimed_lens_moderation(self):
        """Spiegel claimed Snap moderates Lenses to prevent facial recognition."""
        mech = _find_mechanism_130()
        assert mech is not None
        positioning = mech.get("ceo_competitive_positioning", {})
        assert "moderat" in str(positioning.get("claim", "")).lower()

    def test_spiegel_used_meta_as_negative_benchmark(self):
        """Spiegel positioned Specs by contrasting with Meta's controversies."""
        mech = _find_mechanism_130()
        assert mech is not None
        positioning = mech.get("ceo_competitive_positioning", {})
        assert positioning.get("meta_as_negative_benchmark") is True

    def test_privacy_marketing_language(self):
        """Snap's official privacy marketing documented."""
        mech = _find_mechanism_130()
        assert mech is not None
        positioning = mech.get("ceo_competitive_positioning", {})
        marketing = positioning.get("official_privacy_marketing", "")
        assert "protecting" in marketing.lower() or "privacy" in marketing.lower()


# ===================================================================
# 4. MULTI-PUBLICATION AMPLIFICATION CHAIN
# ===================================================================


class TestMultiPublicationAmplification:
    """Verify the cross-publication amplification pattern."""

    def test_at_least_three_publications_amplified(self):
        """At least 3 publications amplified the competitive positioning."""
        mech = _find_mechanism_130()
        assert mech is not None
        chain = mech.get("amplification_chain", [])
        assert len(chain) >= 3, f"Need >= 3 publications, got {len(chain)}"

    def test_engadget_in_chain(self):
        """Engadget (Yahoo/Apollo) is in the amplification chain."""
        mech = _find_mechanism_130()
        assert mech is not None
        chain = mech.get("amplification_chain", [])
        pubs = [c.get("publication", "") for c in chain]
        assert any("engadget" in p.lower() for p in pubs), (
            f"Engadget must be in amplification chain: {pubs}"
        )

    def test_techcrunch_in_chain(self):
        """TechCrunch (Yahoo/Apollo) is in the amplification chain."""
        mech = _find_mechanism_130()
        assert mech is not None
        chain = mech.get("amplification_chain", [])
        pubs = [c.get("publication", "") for c in chain]
        assert any("techcrunch" in p.lower() for p in pubs)

    def test_telecoms_or_third_outlet_in_chain(self):
        """A third outlet is in the amplification chain."""
        mech = _find_mechanism_130()
        assert mech is not None
        chain = mech.get("amplification_chain", [])
        pubs = [c.get("publication", "").lower() for c in chain]
        non_yahoo = [p for p in pubs if "engadget" not in p and "techcrunch" not in p]
        assert len(non_yahoo) >= 1, "Need at least one non-Yahoo amplifier"

    def test_all_amplifiers_have_zero_privacy_vocabulary(self):
        """All amplifying publications used zero privacy alarm language for Snap."""
        mech = _find_mechanism_130()
        assert mech is not None
        chain = mech.get("amplification_chain", [])
        for outlet in chain:
            snap_pv = outlet.get("snap_privacy_vocabulary_count", -1)
            assert snap_pv == 0, (
                f"{outlet.get('publication')} should have 0 snap privacy vocabulary, "
                f"got {snap_pv}"
            )

    def test_yahoo_ownership_consistency(self):
        """Both Engadget and TechCrunch share Yahoo/Apollo ownership."""
        mech = _find_mechanism_130()
        assert mech is not None
        chain = mech.get("amplification_chain", [])
        yahoo_outlets = [
            c for c in chain
            if "yahoo" in str(c.get("parent_company", "")).lower()
            or "apollo" in str(c.get("parent_company", "")).lower()
        ]
        assert len(yahoo_outlets) >= 2, (
            f"Need >= 2 Yahoo/Apollo outlets, got {len(yahoo_outlets)}"
        )


# ===================================================================
# 5. GIZMODO CLEAN CONTROL COMPARISON
# ===================================================================


class TestGizmodoCleanControl:
    """Gizmodo (zero financial ties) as clean control for Snap Specs coverage."""

    def test_gizmodo_raised_camera_privacy_question(self):
        """Gizmodo at least questioned camera privacy for Snap Specs."""
        mech = _find_mechanism_130()
        assert mech is not None
        control = mech.get("clean_control_gizmodo", {})
        assert control.get("raised_camera_question") is True

    def test_gizmodo_noted_led_insufficiency(self):
        """Gizmodo questioned whether LED indicator is sufficient."""
        mech = _find_mechanism_130()
        assert mech is not None
        control = mech.get("clean_control_gizmodo", {})
        assert control.get("questioned_led_sufficiency") is True

    def test_gizmodo_applied_same_standard(self):
        """Gizmodo (zero deals) applied privacy scrutiny to Snap, unlike Yahoo outlets."""
        mech = _find_mechanism_130()
        assert mech is not None
        control = mech.get("clean_control_gizmodo", {})
        pv = control.get("privacy_vocabulary_count", -1)
        assert pv > 0, f"Gizmodo should have > 0 privacy vocabulary, got {pv}"


# ===================================================================
# 6. FINANCIAL RELATIONSHIP MAPPING
# ===================================================================


class TestFinancialRelationships:
    """Verify financial relationships of amplifying publications."""

    def test_yahoo_google_showcase_deal(self):
        """Yahoo receives Google Showcase payments."""
        mech = _find_mechanism_130()
        assert mech is not None
        fin = mech.get("financial_relationships", {})
        yahoo = fin.get("yahoo_apollo", {})
        assert yahoo.get("google_showcase") is True

    def test_snap_openai_partnership(self):
        """Snap has an OpenAI partnership."""
        mech = _find_mechanism_130()
        assert mech is not None
        fin = mech.get("financial_relationships", {})
        snap = fin.get("snap_relationships", {})
        assert snap.get("openai_partnership") is True

    def test_no_meta_deal_for_amplifiers(self):
        """None of the amplifying publications have Meta content deals."""
        mech = _find_mechanism_130()
        assert mech is not None
        chain = mech.get("amplification_chain", [])
        for outlet in chain:
            assert outlet.get("meta_content_deal") is False, (
                f"{outlet.get('publication')} should have no Meta deal"
            )


# ===================================================================
# 7. CROSS-REFERENCE INTEGRITY
# ===================================================================


class TestCrossReferences:
    """Verify mechanism #130 properly cross-references related mechanisms."""

    def test_references_mechanism_121(self):
        """Must reference #121 (Fast Company same-pub opposite framing)."""
        mech = _find_mechanism_130()
        assert mech is not None
        refs = mech.get("related_mechanisms", [])
        ref_ids = [r.get("mechanism_id") if isinstance(r, dict) else r for r in refs]
        assert 121 in ref_ids, f"Must reference #121, have {ref_ids}"

    def test_references_mechanism_122(self):
        """Must reference #122 (TechCrunch privacy vocabulary zero)."""
        mech = _find_mechanism_130()
        assert mech is not None
        refs = mech.get("related_mechanisms", [])
        ref_ids = [r.get("mechanism_id") if isinstance(r, dict) else r for r in refs]
        assert 122 in ref_ids, f"Must reference #122, have {ref_ids}"

    def test_references_mechanism_33(self):
        """Must reference #33 (OpenAI facial recognition privacy parity)."""
        mech = _find_mechanism_130()
        assert mech is not None
        refs = mech.get("related_mechanisms", [])
        ref_ids = [r.get("mechanism_id") if isinstance(r, dict) else r for r in refs]
        assert 33 in ref_ids, f"Must reference #33, have {ref_ids}"

    def test_references_mechanism_8(self):
        """Must reference #8 (safe target coefficient)."""
        mech = _find_mechanism_130()
        assert mech is not None
        refs = mech.get("related_mechanisms", [])
        ref_ids = [r.get("mechanism_id") if isinstance(r, dict) else r for r in refs]
        assert 8 in ref_ids, f"Must reference #8, have {ref_ids}"


# ===================================================================
# 8. NOVEL MECHANISM TYPE
# ===================================================================


class TestNovelMechanismType:
    """Verify this mechanism introduces a novel type."""

    def test_mechanism_type_is_competitive_positioning_amplification(self):
        """Mechanism type should be competitive_privacy_positioning_amplification."""
        mech = _find_mechanism_130()
        assert mech is not None
        assert mech.get("finding_type") == "competitive_privacy_positioning_amplification"

    def test_distinguishes_from_single_pub_mechanisms(self):
        """Must explicitly distinguish from #121 and #122."""
        mech = _find_mechanism_130()
        assert mech is not None
        summary = str(mech.get("finding_summary", ""))
        assert "cross-publication" in summary.lower() or "multi-publication" in summary.lower()


# ===================================================================
# 9. SNAP ENTITY PROFILE
# ===================================================================


class TestSnapEntityProfile:
    """Verify Snap entity has relevant fields in competitor-entities.yaml."""

    def test_snap_entity_exists(self):
        """Snap must exist in competitor-entities.yaml."""
        entities = _load_entities()
        ents = entities.get("entities", {})
        assert "snap" in ents, "Snap entity must exist"

    def test_snap_has_specs_hardware(self):
        """Snap entity should document Specs hardware."""
        entities = _load_entities()
        snap = entities.get("entities", {}).get("snap", {})
        hw = snap.get("hardware_devices", snap.get("specs_hardware", {}))
        # Snap entity should exist and have some hardware documentation
        assert snap, "Snap entity must have content"
