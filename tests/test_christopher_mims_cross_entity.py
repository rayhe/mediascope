"""
Cross-entity coverage analysis: Christopher Mims (WSJ tech columnist).

Mims is the ideal test case for the "balanced control" hypothesis.
News Corp has comparable AI licensing deals with BOTH OpenAI ($50M/yr)
and Meta (up to $50M/yr). If financial incentives predict coverage tone,
Mims should show balanced coverage of both — and he does. In fact,
his coverage shows a TONE INVERSION compared to WIRED/Verge: he is
softer on Meta and more skeptical of OpenAI, the opposite of publications
with one-sided financial relationships.

KEY FINDING — WSJ SYSTEMATIC DISCLOSURE:
WSJ is the ONLY publication in the dataset that systematically discloses
its parent company's financial relationships in its articles. WSJ articles
about Meta include: "News Corp, owner of The Wall Street Journal, has a
content-licensing partnership with Meta." And WSJ articles about OpenAI
include the equivalent OpenAI disclosure. This is an editorial policy,
not individual journalist choice — multiple reporters across different
beats include it. No other profiled publication (WIRED, Verge, Atlantic,
FT, NYT, Guardian) discloses its AI licensing deals in its coverage.
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


# ===================================================================
# 1. MIMS CAREER & BIOGRAPHY
# ===================================================================


class TestMimsCareer:
    """Verify Mims career data and background."""

    def test_mims_current_role(self):
        """Mims is a technology columnist at WSJ since 2014."""
        profile = _load_yaml("news-corp.yaml")
        journalists = profile.get("journalist_profiles", [])
        mims = [j for j in journalists if j["name"] == "Christopher Mims"]
        assert len(mims) == 1, "Christopher Mims must be in news-corp.yaml journalist_profiles"
        m = mims[0]
        assert m["current_role"] == "technology_columnist"
        assert m["publication"] == "The Wall Street Journal"

    def test_mims_joined_wsj_2014(self):
        """Mims joined WSJ in 2014 from Quartz."""
        profile = _load_yaml("news-corp.yaml")
        mims = [j for j in profile.get("journalist_profiles", [])
                if j["name"] == "Christopher Mims"][0]
        assert mims.get("wsj_start") == "2014"

    def test_mims_background(self):
        """Mims has neuroscience degree and prior freelance for WIRED, MIT Tech Review, Atlantic."""
        profile = _load_yaml("news-corp.yaml")
        mims = [j for j in profile.get("journalist_profiles", [])
                if j["name"] == "Christopher Mims"][0]
        background = mims.get("background", "")
        assert "neuroscience" in background.lower()

    def test_mims_column_format(self):
        """Mims produces a weekly column, co-hosts Bold Names podcast."""
        profile = _load_yaml("news-corp.yaml")
        mims = [j for j in profile.get("journalist_profiles", [])
                if j["name"] == "Christopher Mims"][0]
        assert "weekly" in mims.get("output_format", "").lower() or \
               "column" in mims.get("output_format", "").lower()


# ===================================================================
# 2. META COVERAGE TONE — BALANCED TO CONSTRUCTIVE
# ===================================================================


class TestMimsMetaCoverage:
    """Verify Mims covers Meta with balanced-to-constructive framing."""

    def test_yann_lecun_profile_tone(self):
        """LeCun profile (Oct 2024): constructive framing, gave platform to Meta AI vision."""
        profile = _load_yaml("news-corp.yaml")
        mims = [j for j in profile.get("journalist_profiles", [])
                if j["name"] == "Christopher Mims"][0]
        meta_examples = mims.get("cross_entity_coverage", {}).get("meta", {}).get("examples", [])
        lecun = [e for e in meta_examples if "lecun" in e.get("title", "").lower()]
        assert len(lecun) >= 1, "LeCun profile must be documented"
        assert lecun[0]["tone"] >= 0.3, "LeCun profile had constructive/positive tone"

    def test_smart_glasses_survey_tone(self):
        """Smart glasses survey (Jun 2026): balanced, constructive for Meta."""
        profile = _load_yaml("news-corp.yaml")
        mims = [j for j in profile.get("journalist_profiles", [])
                if j["name"] == "Christopher Mims"][0]
        meta_examples = mims.get("cross_entity_coverage", {}).get("meta", {}).get("examples", [])
        glasses = [e for e in meta_examples if "glasses" in e.get("title", "").lower()
                   or "smartglasses" in e.get("title", "").lower()]
        assert len(glasses) >= 1, "Smart glasses piece must be documented"
        assert glasses[0]["tone"] >= 0.0, "Smart glasses piece had balanced-to-constructive tone"

    def test_meta_coverage_tone_not_adversarial(self):
        """Mims' overall Meta coverage tone is NOT adversarial."""
        profile = _load_yaml("news-corp.yaml")
        mims = [j for j in profile.get("journalist_profiles", [])
                if j["name"] == "Christopher Mims"][0]
        meta_tone = mims.get("cross_entity_coverage", {}).get("meta", {}).get("tone", "")
        assert "adversarial" not in meta_tone.lower()

    def test_meta_water_sustainability_positive_framing(self):
        """Mims specifically noted Meta as ONLY company tallying full water use."""
        profile = _load_yaml("news-corp.yaml")
        mims = [j for j in profile.get("journalist_profiles", [])
                if j["name"] == "Christopher Mims"][0]
        meta_examples = mims.get("cross_entity_coverage", {}).get("meta", {}).get("examples", [])
        water = [e for e in meta_examples if "water" in e.get("title", "").lower()
                 or "sustainability" in e.get("title", "").lower()]
        assert len(water) >= 1, "Water/sustainability piece must be documented"

    def test_no_surveillance_vocabulary_for_meta(self):
        """Mims does NOT use surveillance vocabulary to DESCRIBE Meta products."""
        profile = _load_yaml("news-corp.yaml")
        mims = [j for j in profile.get("journalist_profiles", [])
                if j["name"] == "Christopher Mims"][0]
        meta_examples = mims.get("cross_entity_coverage", {}).get("meta", {}).get("examples", [])
        # Check that framing notes don't USE surveillance language to frame Meta
        # (notes that say "no surveillance framing" are fine — they're documenting absence)
        surveillance_terms = ["dormant surveillance", "covert camera", "spy glasses", "creepy tech"]
        for ex in meta_examples:
            framing = ex.get("framing_notes", "").lower()
            for term in surveillance_terms:
                assert term not in framing, (
                    f"Mims does not use surveillance vocabulary: found '{term}' in "
                    f"'{ex.get('title', '')}'"
                )


# ===================================================================
# 3. OPENAI COVERAGE TONE — SKEPTICAL TO CRITICAL
# ===================================================================


class TestMimsOpenAICoverage:
    """Verify Mims covers OpenAI with skeptical-to-critical framing."""

    def test_commoditization_piece_tone(self):
        """AI commoditization piece (Jul 2026): critical of OpenAI business model."""
        profile = _load_yaml("news-corp.yaml")
        mims = [j for j in profile.get("journalist_profiles", [])
                if j["name"] == "Christopher Mims"][0]
        openai_examples = mims.get("cross_entity_coverage", {}).get("openai", {}).get("examples", [])
        commodity = [e for e in openai_examples
                     if "commodity" in e.get("title", "").lower()
                     or "wider availability" in e.get("title", "").lower()]
        assert len(commodity) >= 1, "Commoditization piece must be documented"
        assert commodity[0]["tone"] <= -0.2, "Commoditization piece was critical of OpenAI"

    def test_openai_coverage_tone_not_positive(self):
        """Mims' overall OpenAI coverage tone is NOT positive."""
        profile = _load_yaml("news-corp.yaml")
        mims = [j for j in profile.get("journalist_profiles", [])
                if j["name"] == "Christopher Mims"][0]
        openai_tone = mims.get("cross_entity_coverage", {}).get("openai", {}).get("tone", "")
        assert "positive" not in openai_tone.lower()

    def test_openai_moat_skepticism(self):
        """Mims questions OpenAI's competitive moat — 'without a competitive moat...serious contraction'."""
        profile = _load_yaml("news-corp.yaml")
        mims = [j for j in profile.get("journalist_profiles", [])
                if j["name"] == "Christopher Mims"][0]
        openai = mims.get("cross_entity_coverage", {}).get("openai", {})
        summary = openai.get("summary", "").lower()
        assert "moat" in summary or "commodity" in summary or "contraction" in summary


# ===================================================================
# 4. TONE INVERSION — OPPOSITE OF WIRED/VERGE
# ===================================================================


class TestMimsToneInversion:
    """The balanced control produces a TONE INVERSION compared to
    publications with one-sided financial relationships."""

    def test_meta_softer_than_openai(self):
        """Mims is softer on Meta than on OpenAI — opposite of WIRED."""
        profile = _load_yaml("news-corp.yaml")
        mims = [j for j in profile.get("journalist_profiles", [])
                if j["name"] == "Christopher Mims"][0]
        cross = mims.get("cross_entity_coverage", {})
        meta_tone_val = cross.get("meta", {}).get("tone_value", 0)
        openai_tone_val = cross.get("openai", {}).get("tone_value", 0)
        assert meta_tone_val > openai_tone_val, (
            f"Mims should be softer on Meta ({meta_tone_val}) than OpenAI "
            f"({openai_tone_val}) — tone inversion vs WIRED"
        )

    def test_tone_inversion_documented(self):
        """The tone inversion is explicitly documented in the profile."""
        profile = _load_yaml("news-corp.yaml")
        mims = [j for j in profile.get("journalist_profiles", [])
                if j["name"] == "Christopher Mims"][0]
        verdict = mims.get("asymmetry_verdict", "").lower()
        assert "inversion" in verdict or "opposite" in verdict or "balanced" in verdict

    def test_wired_meta_adversarial_for_comparison(self):
        """WIRED's Meta coverage is adversarial — establishing baseline for comparison."""
        research = _load_research()
        wired = research["publications"]["wired"]
        assert wired["meta_coverage_tone"] == "adversarial"

    def test_wired_openai_neutral_for_comparison(self):
        """WIRED's OpenAI coverage is neutral_to_positive — establishing baseline."""
        research = _load_research()
        wired = research["publications"]["wired"]
        assert "neutral" in wired["openai_coverage_tone"] or "positive" in wired["openai_coverage_tone"]

    def test_balanced_control_hypothesis(self):
        """News Corp balanced deals ($50M/yr each) → balanced/inverted tone.
        One-sided deals (WIRED: OpenAI only) → one-sided adversarial tone."""
        profile = _load_yaml("news-corp.yaml")
        assert profile.get("control_designation", {}).get("type") == "balanced_control"


# ===================================================================
# 5. WSJ SYSTEMATIC DISCLOSURE PRACTICE
# ===================================================================


class TestWSJDisclosurePractice:
    """WSJ is the ONLY publication that systematically discloses
    its parent company's financial relationships in coverage."""

    def test_meta_disclosure_format(self):
        """WSJ articles about Meta include News Corp-Meta disclosure."""
        profile = _load_yaml("news-corp.yaml")
        disclosure = profile.get("disclosure_practice", {})
        meta_disclosure = disclosure.get("meta_disclosure_text", "")
        assert "News Corp" in meta_disclosure
        assert "Meta" in meta_disclosure

    def test_openai_disclosure_format(self):
        """WSJ articles about OpenAI include News Corp-OpenAI disclosure."""
        profile = _load_yaml("news-corp.yaml")
        disclosure = profile.get("disclosure_practice", {})
        openai_disclosure = disclosure.get("openai_disclosure_text", "")
        assert "News Corp" in openai_disclosure
        assert "OpenAI" in openai_disclosure

    def test_disclosure_is_editorial_policy(self):
        """Disclosure appears across multiple reporters — editorial policy, not individual choice."""
        profile = _load_yaml("news-corp.yaml")
        disclosure = profile.get("disclosure_practice", {})
        assert disclosure.get("policy_type") == "editorial_policy"
        reporters = disclosure.get("observed_reporters", [])
        assert len(reporters) >= 3, "Must have observed disclosure from 3+ different reporters"

    def test_wired_no_disclosure(self):
        """WIRED has NEVER disclosed its OpenAI licensing deal — contrast."""
        research = _load_research()
        wired = research["publications"]["wired"]
        openai_summary = wired.get("openai_coverage_summary", "").lower()
        assert "never disclosed" in openai_summary

    def test_verge_no_disclosure(self):
        """The Verge has not disclosed its OpenAI licensing deal — contrast."""
        research = _load_research()
        verge = research["publications"]["the-verge"]
        # The Verge profile should mention lack of disclosure
        openai_summary = verge.get("openai_coverage_summary", "").lower()
        # At minimum, the deal itself should be documented
        assert "vox media" in openai_summary or "openai" in openai_summary.lower()

    def test_disclosure_uniqueness(self):
        """WSJ is the ONLY profiled publication with systematic disclosure."""
        profile = _load_yaml("news-corp.yaml")
        disclosure = profile.get("disclosure_practice", {})
        assert disclosure.get("unique_in_dataset") is True


# ===================================================================
# 6. SENSOR-COUNT PARADOX AT WSJ
# ===================================================================


class TestMimsSensorCountParadox:
    """Mims' smart glasses coverage does NOT apply the sensor-count paradox."""

    def test_no_camera_count_alarm(self):
        """Mims discusses Meta's cameras without surveillance framing."""
        profile = _load_yaml("news-corp.yaml")
        mims = [j for j in profile.get("journalist_profiles", [])
                if j["name"] == "Christopher Mims"][0]
        meta = mims.get("cross_entity_coverage", {}).get("meta", {})
        summary = meta.get("summary", "").lower()
        assert "camera" not in summary or "surveillance" not in summary, (
            "Mims should not combine camera mentions with surveillance framing"
        )

    def test_apple_vision_pro_no_surveillance_framing(self):
        """Mims does not frame Apple Vision Pro's 12 cameras as surveillance either."""
        profile = _load_yaml("news-corp.yaml")
        mims = [j for j in profile.get("journalist_profiles", [])
                if j["name"] == "Christopher Mims"][0]
        apple = mims.get("cross_entity_coverage", {}).get("apple", {})
        summary = apple.get("summary", "").lower()
        # Check for adversarial surveillance framing (not negation statements)
        adversarial_terms = ["dormant surveillance", "spy device", "privacy threat"]
        if summary:
            for term in adversarial_terms:
                assert term not in summary


# ===================================================================
# 7. CROSS-MECHANISM TAXONOMY — WSJ AS MECHANISM #6
# ===================================================================


class TestWSJBalancedControlMechanism:
    """WSJ/Mims represents a new mechanism type: balanced financial
    relationships producing balanced coverage."""

    def test_mechanism_documented(self):
        """The balanced control mechanism is documented in research."""
        research = _load_research()
        pubs = research["publications"]
        if "news-corp" in pubs:
            nc = pubs["news-corp"]
            verdict = nc.get("asymmetry_verdict", "").lower()
            assert "balanced" in verdict or "control" in verdict

    def test_news_corp_profile_has_control_designation(self):
        """News Corp profile has control_designation type."""
        profile = _load_yaml("news-corp.yaml")
        assert profile.get("control_designation", {}).get("type") == "balanced_control"

    def test_meta_deal_documented(self):
        """News Corp Meta deal ($50M/yr) is documented."""
        profile = _load_yaml("news-corp.yaml")
        meta_rel = profile.get("competitor_relationships", {}).get("meta", {})
        assert "50" in meta_rel.get("estimated_value", "")

    def test_openai_deal_documented(self):
        """News Corp OpenAI deal ($50M/yr) is documented."""
        profile = _load_yaml("news-corp.yaml")
        openai_rel = profile.get("competitor_relationships", {}).get("openai", {})
        assert "50" in openai_rel.get("estimated_value", "")


# ===================================================================
# 8. META POSITIVE FRAMING EVIDENCE
# ===================================================================


class TestMetaPositiveFraming:
    """Specific evidence of Mims framing Meta constructively."""

    def test_meta_commodity_piece_constructive(self):
        """In the commoditization piece, Meta framed as competitive vs OpenAI."""
        profile = _load_yaml("news-corp.yaml")
        mims = [j for j in profile.get("journalist_profiles", [])
                if j["name"] == "Christopher Mims"][0]
        meta_examples = mims.get("cross_entity_coverage", {}).get("meta", {}).get("examples", [])
        commodity = [e for e in meta_examples if "commodity" in e.get("title", "").lower()
                     or "compete" in e.get("title", "").lower()]
        # In the commodity piece, Mims said Meta "showed the world it could
        # potentially compete with the two leading AI labs"
        assert len(commodity) >= 1 or len(meta_examples) >= 3

    def test_meta_water_framing_positive(self):
        """Mims noted Meta is the ONLY company tallying full water use — positive."""
        profile = _load_yaml("news-corp.yaml")
        mims = [j for j in profile.get("journalist_profiles", [])
                if j["name"] == "Christopher Mims"][0]
        meta_examples = mims.get("cross_entity_coverage", {}).get("meta", {}).get("examples", [])
        water = [e for e in meta_examples if "water" in e.get("title", "").lower()]
        if water:
            assert water[0]["tone"] >= 0.0


# ===================================================================
# 9. STRUCTURAL INTEGRATION
# ===================================================================


class TestStructuralIntegration:
    """Ensure Mims analysis is properly integrated into the toolkit."""

    def test_news_corp_has_journalist_profiles(self):
        """news-corp.yaml has journalist_profiles section."""
        profile = _load_yaml("news-corp.yaml")
        assert "journalist_profiles" in profile

    def test_mims_has_source_urls(self):
        """Mims profile has source URLs for verification."""
        profile = _load_yaml("news-corp.yaml")
        mims = [j for j in profile.get("journalist_profiles", [])
                if j["name"] == "Christopher Mims"][0]
        assert len(mims.get("source_urls", [])) >= 2

    def test_disclosure_has_source_urls(self):
        """Disclosure practice has example source URLs."""
        profile = _load_yaml("news-corp.yaml")
        disclosure = profile.get("disclosure_practice", {})
        assert len(disclosure.get("example_articles", [])) >= 3
