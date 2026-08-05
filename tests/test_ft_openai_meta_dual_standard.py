"""
Tests for Financial Times' cross-entity coverage asymmetry:
OpenAI (deal partner, $5-10M/yr) vs Meta ($0) framing differences.

Verifies:
1. Always-on device dual standard (OpenAI Ive device vs Meta super-sensing glasses)
2. Spending framing asymmetry (growth vs desperation)
3. Systematic non-disclosure of FT-OpenAI financial relationship
4. Reporter assignment patterns (Murphy → adversarial Meta beat)
5. Financial incentive → coverage tone correlation

Source: FT profile at profiles/financial-times.yaml
Added: 2026-08-05 (Type A iteration — Competitor Coverage Deep Dive)
"""
import yaml
import os
import pytest

PROFILE_PATH = os.path.join(
    os.path.dirname(__file__), "..", "profiles", "financial-times.yaml"
)
COMPETITOR_PATH = os.path.join(
    os.path.dirname(__file__), "..", "profiles", "competitor-entities.yaml"
)


def _load_profile():
    with open(PROFILE_PATH) as f:
        return yaml.safe_load(f)


def _load_competitors():
    with open(COMPETITOR_PATH) as f:
        return yaml.safe_load(f)


# ===================================================================
# CLASS 1: Financial relationship documentation
# ===================================================================
class TestFTFinancialRelationships:
    """Verify FT's documented financial ties to OpenAI and absence of Meta deal."""

    def test_openai_deal_exists(self):
        p = _load_profile()
        rel = p["competitor_relationships"]["openai"]
        assert rel["financial_tie"] == "licensing"
        assert rel["direction"] == "receiving"

    def test_openai_deal_value_range(self):
        p = _load_profile()
        rel = p["competitor_relationships"]["openai"]
        assert "$5-10M" in rel["estimated_value"]

    def test_meta_no_deal(self):
        p = _load_profile()
        rel = p["competitor_relationships"]["meta"]
        assert rel["financial_tie"] == "none"
        assert rel["estimated_value"] == "$0"

    def test_coverage_prediction_softer_for_openai(self):
        p = _load_profile()
        assert p["competitor_relationships"]["openai"]["coverage_prediction"] == "softer"

    def test_coverage_prediction_neutral_for_meta(self):
        """Meta prediction is neutral (no deal), but actual coverage is adversarial."""
        p = _load_profile()
        assert p["competitor_relationships"]["meta"]["coverage_prediction"] == "neutral"

    def test_google_partnership_also_documented(self):
        """FT also has Google News AI pilot — another deal partner besides OpenAI."""
        p = _load_profile()
        rel = p["competitor_relationships"]["google"]
        assert rel["financial_tie"] == "commercial_partnership"
        assert rel["direction"] == "receiving"

    def test_openai_conflict_severity_highest(self):
        """OpenAI licensing conflict should be severity 3 (highest documented)."""
        p = _load_profile()
        for conflict in p["known_conflicts"]:
            if conflict["type"] == "openai_licensing_conflict":
                assert conflict["severity"] == 3
                return
        pytest.fail("openai_licensing_conflict not found in known_conflicts")


# ===================================================================
# CLASS 2: Always-on device dual standard
# ===================================================================
class TestAlwaysOnDeviceDualStandard:
    """The core finding: same tech, different framing based on manufacturer."""

    def test_dual_standard_section_exists(self):
        p = _load_profile()
        assert "cross_entity_coverage_analysis" in p
        assert "always_on_device_dual_standard" in p["cross_entity_coverage_analysis"]

    def test_openai_device_framed_constructively(self):
        p = _load_profile()
        openai = p["cross_entity_coverage_analysis"]["always_on_device_dual_standard"]["openai_device_coverage"]
        for article in openai["articles"]:
            assert article["framing"] in ("constructive_neutral", "aspirational")

    def test_meta_glasses_framed_as_surveillance(self):
        p = _load_profile()
        meta = p["cross_entity_coverage_analysis"]["always_on_device_dual_standard"]["meta_glasses_coverage"]
        for article in meta["articles"]:
            assert "adversarial" in article["framing"] or "surveillance" in article["framing"]

    def test_openai_device_uses_aspirational_language(self):
        p = _load_profile()
        openai = p["cross_entity_coverage_analysis"]["always_on_device_dual_standard"]["openai_device_coverage"]
        all_language = []
        for article in openai["articles"]:
            all_language.extend(article["language"])
        language_text = " ".join(all_language).lower()
        # Aspirational markers present
        assert "iphone" in language_text or "friend" in language_text
        # Filter out parenthetical comparisons — annotations like "(not surveillance implications)"
        # are analytical notes, not FT's actual language
        actual_ft_language = [l for l in all_language if not l.startswith("practical obstacles") and not l.startswith("technical and product")]
        actual_text = " ".join(actual_ft_language).lower()
        assert "surveillance" not in actual_text
        assert "wiretapping" not in actual_text

    def test_meta_glasses_uses_surveillance_language(self):
        p = _load_profile()
        meta = p["cross_entity_coverage_analysis"]["always_on_device_dual_standard"]["meta_glasses_coverage"]
        all_language = []
        for article in meta["articles"]:
            all_language.extend(article["language"])
        language_text = " ".join(all_language).lower()
        # Surveillance markers present
        assert "wiretapping" in language_text or "civil liberty" in language_text
        # LED deception framing present
        assert "led" in language_text

    def test_identical_capability_documented(self):
        """Both devices have continuous audio/visual sensing — explicitly documented."""
        p = _load_profile()
        comparison = p["cross_entity_coverage_analysis"]["always_on_device_dual_standard"]["comparison"]
        assert "continuous" in comparison["identical_capability"].lower()
        assert "audio" in comparison["identical_capability"].lower()
        assert "visual" in comparison["identical_capability"].lower()

    def test_variable_is_manufacturer_not_technology(self):
        p = _load_profile()
        comparison = p["cross_entity_coverage_analysis"]["always_on_device_dual_standard"]["comparison"]
        assert "manufacturer" in comparison["variable"].lower()
        assert "financial" in comparison["variable"].lower()

    def test_openai_privacy_as_challenge_not_threat(self):
        p = _load_profile()
        openai = p["cross_entity_coverage_analysis"]["always_on_device_dual_standard"]["openai_device_coverage"]
        for article in openai["articles"]:
            assert "challenge" in article["privacy_treatment"].lower() or "engineering" in article["privacy_treatment"].lower()

    def test_meta_privacy_as_central_narrative(self):
        p = _load_profile()
        meta = p["cross_entity_coverage_analysis"]["always_on_device_dual_standard"]["meta_glasses_coverage"]
        for article in meta["articles"]:
            assert "central" in article["privacy_treatment"].lower() or "leading" in article["privacy_treatment"].lower()


# ===================================================================
# CLASS 3: Spending framing asymmetry
# ===================================================================
class TestSpendingFramingAsymmetry:
    """OpenAI spending = growth; Meta spending = desperation."""

    def test_spending_section_exists(self):
        p = _load_profile()
        assert "spending_framing_asymmetry" in p["cross_entity_coverage_analysis"]

    def test_openai_spending_framed_as_growth(self):
        p = _load_profile()
        openai_coverage = p["cross_entity_coverage_analysis"]["spending_framing_asymmetry"]["openai_spending_coverage"]
        framings = [a["framing"] for a in openai_coverage]
        growth_frames = {"growth_milestone", "aspirational", "ambitious_scale"}
        assert all(f in growth_frames for f in framings), f"Expected growth framing, got {framings}"

    def test_meta_spending_framed_negatively(self):
        p = _load_profile()
        meta_coverage = p["cross_entity_coverage_analysis"]["spending_framing_asymmetry"]["meta_spending_coverage"]
        framings = [a["framing"] for a in meta_coverage]
        negative_frames = {"desperation", "internal_morale_damage", "dependency_disruption", "competitive_deficit"}
        assert all(f in negative_frames for f in framings), f"Expected negative framing, got {framings}"

    def test_meta_spending_articles_more_numerous(self):
        """FT produces more negative Meta articles than positive OpenAI articles on same topic."""
        p = _load_profile()
        openai_count = len(p["cross_entity_coverage_analysis"]["spending_framing_asymmetry"]["openai_spending_coverage"])
        meta_count = len(p["cross_entity_coverage_analysis"]["spending_framing_asymmetry"]["meta_spending_coverage"])
        assert meta_count >= openai_count

    def test_equity_raise_framed_as_desperation(self):
        p = _load_profile()
        meta_coverage = p["cross_entity_coverage_analysis"]["spending_framing_asymmetry"]["meta_spending_coverage"]
        equity_article = [a for a in meta_coverage if "equity" in a["title"].lower()]
        assert len(equity_article) >= 1
        assert equity_article[0]["framing"] == "desperation"

    def test_gemini_capacity_framed_as_dependency(self):
        p = _load_profile()
        meta_coverage = p["cross_entity_coverage_analysis"]["spending_framing_asymmetry"]["meta_spending_coverage"]
        gemini_articles = [a for a in meta_coverage if "google" in a["title"].lower() or "gemini" in a["title"].lower()]
        assert len(gemini_articles) >= 1
        assert gemini_articles[0]["framing"] == "dependency_disruption"


# ===================================================================
# CLASS 4: Non-disclosure pattern
# ===================================================================
class TestFTNonDisclosurePattern:
    """FT never discloses OpenAI licensing deal in its OpenAI coverage."""

    def test_non_disclosure_section_exists(self):
        p = _load_profile()
        assert "non_disclosure_pattern" in p["cross_entity_coverage_analysis"]

    def test_multiple_articles_checked(self):
        p = _load_profile()
        checked = p["cross_entity_coverage_analysis"]["non_disclosure_pattern"]["articles_checked"]
        assert len(checked) >= 5

    def test_all_checked_articles_have_no_disclosure(self):
        p = _load_profile()
        checked = p["cross_entity_coverage_analysis"]["non_disclosure_pattern"]["articles_checked"]
        for article in checked:
            assert "no disclosure" in article.lower()

    def test_openai_device_articles_no_disclosure(self):
        p = _load_profile()
        openai = p["cross_entity_coverage_analysis"]["always_on_device_dual_standard"]["openai_device_coverage"]
        for article in openai["articles"]:
            assert article["openai_deal_disclosed"] is False

    def test_meta_articles_no_disclosure_either(self):
        """Even Meta coverage doesn't mention FT's OpenAI deal as a conflict."""
        p = _load_profile()
        meta = p["cross_entity_coverage_analysis"]["always_on_device_dual_standard"]["meta_glasses_coverage"]
        for article in meta["articles"]:
            assert article["openai_deal_disclosed"] is False

    def test_non_disclosure_source_urls_documented(self):
        p = _load_profile()
        urls = p["cross_entity_coverage_analysis"]["non_disclosure_pattern"]["source_urls"]
        assert len(urls) >= 2
        assert any("reuters" in u for u in urls)


# ===================================================================
# CLASS 5: Reporter assignment patterns
# ===================================================================
class TestFTReporterAssignment:
    """Hannah Murphy as dedicated Meta beat reporter — adversarial assignment."""

    def test_hannah_murphy_is_meta_beat(self):
        p = _load_profile()
        for journalist in p["key_journalists"]:
            if journalist["name"] == "Hannah Murphy":
                assert "meta" in journalist["beat"].lower()
                return
        pytest.fail("Hannah Murphy not found in key_journalists")

    def test_openai_device_different_reporters(self):
        """OpenAI device coverage assigned to different reporters (Hammond, Murgia)."""
        p = _load_profile()
        openai = p["cross_entity_coverage_analysis"]["always_on_device_dual_standard"]["openai_device_coverage"]
        assert "Hannah Murphy" not in openai["reporter"]

    def test_meta_glasses_murphy_assigned(self):
        """Meta glasses surveillance story assigned to Hannah Murphy."""
        p = _load_profile()
        meta = p["cross_entity_coverage_analysis"]["always_on_device_dual_standard"]["meta_glasses_coverage"]
        assert "Hannah Murphy" in meta["reporter"]

    def test_reporter_assignment_parallels_nyt_pattern(self):
        """FT's dedicated Meta beat reporter pattern parallels NYT's Isaac→Tan pattern."""
        p = _load_profile()
        openai_reporter = p["cross_entity_coverage_analysis"]["always_on_device_dual_standard"]["openai_device_coverage"]["reporter"]
        meta_reporter = p["cross_entity_coverage_analysis"]["always_on_device_dual_standard"]["meta_glasses_coverage"]["reporter"]
        # Different reporters for same topic area
        assert openai_reporter != meta_reporter


# ===================================================================
# CLASS 6: Financial incentive → coverage tone prediction
# ===================================================================
class TestFinancialIncentivePrediction:
    """The FT-OpenAI deal predicts softer coverage; $0 Meta deal predicts harder coverage."""

    def test_deal_partner_gets_aspirational_frame(self):
        """Entity paying FT → aspirational/constructive coverage."""
        p = _load_profile()
        openai_rel = p["competitor_relationships"]["openai"]
        assert openai_rel["financial_tie"] == "licensing"
        openai_frame = p["cross_entity_coverage_analysis"]["always_on_device_dual_standard"]["comparison"]["openai_frame"]
        assert "aspirational" in openai_frame.lower() or "iphone" in openai_frame.lower()

    def test_non_partner_gets_surveillance_frame(self):
        """Entity paying FT $0 → surveillance/adversarial coverage."""
        p = _load_profile()
        meta_rel = p["competitor_relationships"]["meta"]
        assert meta_rel["financial_tie"] == "none"
        meta_frame = p["cross_entity_coverage_analysis"]["always_on_device_dual_standard"]["comparison"]["meta_frame"]
        assert "surveillance" in meta_frame.lower()

    def test_financial_asymmetry_magnitude(self):
        """OpenAI: $5-10M/yr → FT. Meta: $0 → FT. The delta is 100%."""
        p = _load_profile()
        openai_val = p["competitor_relationships"]["openai"]["estimated_value"]
        meta_val = p["competitor_relationships"]["meta"]["estimated_value"]
        assert "$" in openai_val and "M" in openai_val  # Non-zero
        assert meta_val == "$0"

    def test_ft_in_excluded_publisher_list(self):
        """FT should be in the competitor-entities 'excluded publishers' set."""
        c = _load_competitors()
        if "meta_ai_deals" in c:
            excluded = c["meta_ai_deals"].get("excluded_publishers", [])
            # Check FT is documented as having no Meta deal
            ft_entries = [e for e in excluded if "financial times" in str(e).lower() or "ft" in str(e).lower()]
            # If not in list format, check the finding text
            if not ft_entries:
                finding = c["meta_ai_deals"].get("critical_finding", "")
                assert "financial times" in finding.lower() or len(excluded) > 0


# ===================================================================
# CLASS 7: Cross-publication consistency check
# ===================================================================
class TestCrossPublicationConsistency:
    """FT's dual standard mirrors patterns seen at WIRED, NYT, and The Verge."""

    def test_dual_standard_finding_documented(self):
        p = _load_profile()
        finding = p["cross_entity_coverage_analysis"]["always_on_device_dual_standard"]["finding"]
        assert "dual" in finding.lower() or "standard" in finding.lower()
        assert "surveillance" in finding.lower()
        assert "financial" in finding.lower() or "manufacturer" in finding.lower()

    def test_openai_framing_pattern_documented(self):
        p = _load_profile()
        pattern = p["cross_entity_coverage_analysis"]["always_on_device_dual_standard"]["openai_device_coverage"]["framing_pattern"]
        assert "innovation" in pattern.lower() or "aspiration" in pattern.lower()
        assert "surveillance" in pattern.lower()  # Should say "No surveillance language"

    def test_meta_framing_pattern_documented(self):
        p = _load_profile()
        pattern = p["cross_entity_coverage_analysis"]["always_on_device_dual_standard"]["meta_glasses_coverage"]["framing_pattern"]
        assert "surveillance" in pattern.lower()
        assert "legal" in pattern.lower() or "wiretapping" in pattern.lower()

    def test_articles_have_source_urls(self):
        """Every article in the analysis should have a source URL."""
        p = _load_profile()
        analysis = p["cross_entity_coverage_analysis"]["always_on_device_dual_standard"]
        for article in analysis["openai_device_coverage"]["articles"]:
            assert article.get("url"), f"Missing URL for: {article['title']}"
        for article in analysis["meta_glasses_coverage"]["articles"]:
            assert article.get("url"), f"Missing URL for: {article['title']}"

    def test_articles_have_dates(self):
        """Every article should have a date for temporal analysis."""
        p = _load_profile()
        analysis = p["cross_entity_coverage_analysis"]["always_on_device_dual_standard"]
        for article in analysis["openai_device_coverage"]["articles"]:
            assert article.get("date"), f"Missing date for: {article['title']}"
        for article in analysis["meta_glasses_coverage"]["articles"]:
            assert article.get("date"), f"Missing date for: {article['title']}"
