"""
Tests for Financial Times' Google vs Meta coverage asymmetry.

FT has financial relationships with BOTH Google (News AI pilot, Feb 2026)
and OpenAI ($5-10M/yr licensing, Apr 2024) but ZERO with Meta. This test
suite verifies that FT's Google coverage uses business/technology framing
while its Meta coverage uses adversarial/surveillance framing — and that
this pattern correlates with the financial relationship structure.

KEY FINDING: FT treats Google's AI glasses (Android XR, cameras, always-on
Gemini integration) with business/product framing, while treating Meta's
AI glasses (single camera, always-on sensing) with surveillance/legal-threat
framing. Same product category, different manufacturer, different coverage
tone — correlated with whether the manufacturer pays FT.

ADDITIONAL: FT's adversarial Google posture stays in regulatory filings
(CMA response demanding AI content opt-in controls), NOT in coverage.
FT's adversarial Meta posture IS the coverage (surveillance language,
privacy alarm, legal threat framing).

Source: profiles/financial-times.yaml, profiles/competitor-coverage-research.yaml
Added: 2026-08-05 (Type A iteration — Competitor Coverage Deep Dive: FT × Google)
"""
import yaml
import os
import pytest

PROFILE_PATH = os.path.join(
    os.path.dirname(__file__), "..", "profiles", "financial-times.yaml"
)
RESEARCH_PATH = os.path.join(
    os.path.dirname(__file__), "..", "profiles", "competitor-coverage-research.yaml"
)


@pytest.fixture(scope="module")
def ft_profile():
    with open(PROFILE_PATH) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def research():
    with open(RESEARCH_PATH) as f:
        return yaml.safe_load(f)


# ===================================================================
# 1. Google Financial Relationship Exists
# ===================================================================
class TestGoogleFinancialRelationship:
    """FT has a documented Google financial relationship."""

    def test_google_relationship_exists(self, ft_profile):
        rels = ft_profile.get("competitor_relationships", {})
        assert "google" in rels, "FT profile must document Google relationship"

    def test_google_relationship_type(self, ft_profile):
        google = ft_profile["competitor_relationships"]["google"]
        assert google["financial_tie"] in (
            "commercial_partnership",
            "licensing",
        ), "Google tie must be commercial_partnership or licensing"

    def test_google_direction_is_receiving(self, ft_profile):
        google = ft_profile["competitor_relationships"]["google"]
        assert google["direction"] == "receiving", "FT receives from Google, not vice versa"

    def test_meta_relationship_is_none(self, ft_profile):
        meta = ft_profile["competitor_relationships"]["meta"]
        assert meta["financial_tie"] == "none", "FT has zero Meta deal"

    def test_google_coverage_prediction_softer(self, ft_profile):
        google = ft_profile["competitor_relationships"]["google"]
        assert google["coverage_prediction"] == "softer"


# ===================================================================
# 2. Reporter Assignment Asymmetry — Google vs Meta
# ===================================================================
class TestReporterAssignmentAsymmetry:
    """FT assigns different reporters to Google vs Meta coverage,
    creating different narrative frames by default."""

    def test_murphy_covers_meta(self, ft_profile):
        journalists = ft_profile.get("key_journalists", [])
        murphy = next((j for j in journalists if j["name"] == "Hannah Murphy"), None)
        assert murphy is not None, "Hannah Murphy must be in FT profile"
        assert "meta" in murphy["beat"].lower() or "Meta" in murphy["beat"]

    def test_murphy_does_not_cover_google(self, ft_profile):
        journalists = ft_profile.get("key_journalists", [])
        murphy = next((j for j in journalists if j["name"] == "Hannah Murphy"), None)
        entities_not_covered = murphy.get("cross_entity_coverage_analysis", {}).get(
            "entities_not_covered_by_murphy", {}
        )
        desc = entities_not_covered.get("description", "")
        assert "google" in desc.lower() or "Google" in desc

    def test_google_coverage_uses_different_reporters(self, ft_profile):
        google_analysis = ft_profile.get("google_coverage_analysis", {})
        reporters = google_analysis.get("reporters", [])
        reporter_names = [r["name"] for r in reporters]
        assert "Hannah Murphy" not in reporter_names, (
            "Murphy should NOT be the Google reporter"
        )
        assert len(reporter_names) >= 1, "At least one Google reporter must be documented"

    def test_reporter_separation_creates_frame_divergence(self, ft_profile):
        google_analysis = ft_profile.get("google_coverage_analysis", {})
        finding = google_analysis.get("reporter_assignment_finding", "")
        assert "different" in finding.lower() or "separate" in finding.lower()


# ===================================================================
# 3. Smart Glasses Coverage Double Standard
# ===================================================================
class TestSmartGlassesDoubleStandard:
    """FT covers Google/Samsung Android XR glasses with business framing
    and Meta glasses with surveillance framing — same product category."""

    def test_google_glasses_coverage_exists(self, ft_profile):
        google_analysis = ft_profile.get("google_coverage_analysis", {})
        glasses = google_analysis.get("smart_glasses_coverage", {})
        assert len(glasses.get("articles", [])) >= 1

    def test_google_glasses_no_surveillance_language(self, ft_profile):
        google_analysis = ft_profile.get("google_coverage_analysis", {})
        glasses = google_analysis.get("smart_glasses_coverage", {})
        for article in glasses.get("articles", []):
            lang = " ".join(article.get("language", []))
            for term in ["surveillance", "wiretapping", "biometric data laws"]:
                assert term not in lang.lower(), (
                    f"Google glasses coverage should not use '{term}'"
                )

    def test_meta_glasses_has_surveillance_language(self, ft_profile):
        murphy = None
        for j in ft_profile.get("key_journalists", []):
            if j["name"] == "Hannah Murphy":
                murphy = j
                break
        analysis = murphy.get("cross_entity_coverage_analysis", {})
        meta_portfolio = analysis.get("meta_coverage_portfolio", [])
        glasses_articles = [
            a for a in meta_portfolio if "glass" in a.get("article", "").lower()
            or "record" in a.get("article", "").lower()
        ]
        assert len(glasses_articles) >= 1
        found_surveillance = False
        for art in glasses_articles:
            lang = " ".join(art.get("language", []))
            if "wiretapping" in lang.lower() or "surveillance" in lang.lower():
                found_surveillance = True
        assert found_surveillance, "Meta glasses coverage must contain surveillance language"

    def test_google_glasses_framing_is_business(self, ft_profile):
        google_analysis = ft_profile.get("google_coverage_analysis", {})
        glasses = google_analysis.get("smart_glasses_coverage", {})
        for article in glasses.get("articles", []):
            assert article.get("framing", "").startswith(("business", "technology", "product", "neutral"))

    def test_surveillance_term_asymmetry(self, ft_profile):
        google_analysis = ft_profile.get("google_coverage_analysis", {})
        glasses = google_analysis.get("smart_glasses_coverage", {})
        google_surveillance_count = 0
        for article in glasses.get("articles", []):
            for term in article.get("language", []):
                if any(s in term.lower() for s in ["surveillance", "wiretapping", "biometric"]):
                    google_surveillance_count += 1

        murphy = next(
            (j for j in ft_profile.get("key_journalists", []) if j["name"] == "Hannah Murphy"),
            None,
        )
        analysis = murphy.get("cross_entity_coverage_analysis", {})
        diag = analysis.get("diagnostic_comparison_ar_glasses", {})
        meta_surv = diag.get("surveillance_term_count_meta", 0)

        assert meta_surv > google_surveillance_count, (
            f"Meta surveillance terms ({meta_surv}) must exceed Google ({google_surveillance_count})"
        )


# ===================================================================
# 4. Capex / Business Coverage Framing Asymmetry
# ===================================================================
class TestCapexFramingAsymmetry:
    """FT covers Alphabet capex as business milestone, Meta capex as crisis."""

    def test_google_capex_coverage_exists(self, ft_profile):
        google_analysis = ft_profile.get("google_coverage_analysis", {})
        capex = google_analysis.get("capex_coverage", {})
        assert len(capex.get("articles", [])) >= 1

    def test_google_capex_not_crisis_framing(self, ft_profile):
        google_analysis = ft_profile.get("google_coverage_analysis", {})
        capex = google_analysis.get("capex_coverage", {})
        for article in capex.get("articles", []):
            framing = article.get("framing", "")
            assert "crisis" not in framing and "desperation" not in framing

    def test_meta_spending_has_negative_framing(self, ft_profile):
        cross = ft_profile.get("cross_entity_coverage_analysis", {})
        meta_spending = cross.get("spending_framing_asymmetry", {}).get(
            "meta_spending_coverage", []
        )
        negative_count = sum(
            1 for a in meta_spending
            if a.get("framing", "") in ("desperation", "internal_morale_damage",
                                         "dependency_disruption", "competitive_deficit")
        )
        assert negative_count >= 2, (
            f"Meta spending coverage must have 2+ negative framings, got {negative_count}"
        )


# ===================================================================
# 5. Regulatory vs Coverage Split
# ===================================================================
class TestRegulatoryVsCoverageSplit:
    """FT's adversarial Google posture lives in regulatory filings,
    NOT in public coverage. The opposite is true for Meta."""

    def test_google_regulatory_adversarial(self, ft_profile):
        google_analysis = ft_profile.get("google_coverage_analysis", {})
        reg = google_analysis.get("regulatory_posture", {})
        assert reg.get("stance") in ("adversarial", "assertive")

    def test_google_coverage_not_adversarial(self, ft_profile):
        google_analysis = ft_profile.get("google_coverage_analysis", {})
        overall_tone = google_analysis.get("overall_coverage_tone", "")
        assert "adversarial" not in overall_tone.lower(), (
            "FT's Google coverage tone should NOT be adversarial"
        )

    def test_meta_coverage_is_adversarial(self, research):
        ft = research["publications"]["financial-times"]
        meta_tone = ft.get("meta_coverage_tone", "")
        assert "adversarial" in meta_tone.lower()

    def test_split_documented(self, ft_profile):
        google_analysis = ft_profile.get("google_coverage_analysis", {})
        reg = google_analysis.get("regulatory_posture", {})
        finding = reg.get("split_finding", "")
        assert "regulatory" in finding.lower() or "coverage" in finding.lower()


# ===================================================================
# 6. Financial Relationship Predicts Coverage Tone (Google)
# ===================================================================
class TestFinancialPredictsTone:
    """Google (deal partner) gets softer coverage than Meta (no deal)
    at FT — consistent with the financial-incentive hypothesis."""

    def test_google_tone_softer_than_meta(self, ft_profile):
        google_analysis = ft_profile.get("google_coverage_analysis", {})
        google_tone = google_analysis.get("overall_coverage_tone", "")
        # Meta tone is "balanced_adversarial" per research yaml
        # Google tone should be neutral/business
        assert any(t in google_tone.lower() for t in ["neutral", "business", "balanced"])

    def test_both_have_camera_products(self, ft_profile):
        """Both Google and Meta ship camera glasses — framing should be comparable
        if it were technology-driven, but it isn't."""
        google_analysis = ft_profile.get("google_coverage_analysis", {})
        glasses = google_analysis.get("smart_glasses_coverage", {})
        assert glasses.get("cameras_present", False) is True

    def test_asymmetry_score_documented(self, ft_profile):
        google_analysis = ft_profile.get("google_coverage_analysis", {})
        score = google_analysis.get("asymmetry_score", {})
        assert "google_meta_delta" in score or "delta" in str(score).lower()

    def test_three_deal_portfolio_documented(self, ft_profile):
        """FT has deals with OpenAI, Google, AND ProRata — three entities that
        compete with Meta in AI — while having zero Meta deal."""
        rels = ft_profile.get("competitor_relationships", {})
        deal_count = sum(
            1 for k, v in rels.items()
            if v.get("financial_tie", "none") != "none" and k != "meta"
        )
        assert deal_count >= 2, f"FT should have 2+ non-Meta deals, got {deal_count}"
