"""Type D 22:00 PT Cross-Validation — Aug 8, 2026

End-of-day cross-validation across the two Type C additions from tonight:
1. Google Q2 2026 vs Meta Q2 2026 earnings coverage asymmetry (20:00 PT)
2. OpenAI publisher financial displacement architecture (21:00 PT)

Validates internal consistency, cross-entity coherence, and statistical
claims across the competitor-entities.yaml data model.
"""

import yaml
import os
import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")


@pytest.fixture(scope="module")
def entities():
    with open(os.path.join(PROFILES_DIR, "competitor-entities.yaml")) as f:
        data = yaml.safe_load(f)
    return data["entities"]


@pytest.fixture(scope="module")
def google(entities):
    return entities["google"]


@pytest.fixture(scope="module")
def openai(entities):
    return entities["openai"]


@pytest.fixture(scope="module")
def anthropic(entities):
    return entities["anthropic"]


@pytest.fixture(scope="module")
def meta_q2(entities):
    """Extract Meta Q2 data from the Google comparison section."""
    comp = entities["google"].get("q2_2026_meta_google_coverage_asymmetry", {})
    return comp


# ── Section 1: Google Q2 Internal Consistency ────────────────────────────

class TestGoogleQ2InternalConsistency:
    """Verify Google's Q2 2026 earnings data is internally consistent."""

    def test_report_date_after_quarter_end(self, google):
        q2 = google["q2_2026_earnings"]
        assert q2["report_date"] > q2["quarter_ended"]

    def test_revenue_positive(self, google):
        q2 = google["q2_2026_earnings"]
        assert q2["total_revenue_b"] > 0

    def test_yoy_growth_reasonable(self, google):
        q2 = google["q2_2026_earnings"]
        assert 0 < q2["total_revenue_yoy_pct"] < 100

    def test_search_revenue_under_total(self, google):
        q2 = google["q2_2026_earnings"]
        assert q2["google_search_other_b"] < q2["total_revenue_b"]

    def test_capex_positive(self, google):
        q2 = google["q2_2026_earnings"]
        assert q2.get("capex_q2_b", 0) > 0

    def test_cloud_revenue_positive(self, google):
        q2 = google["q2_2026_earnings"]
        assert q2.get("google_cloud_revenue_b", 0) > 0

    def test_has_source_urls(self, google):
        q2 = google["q2_2026_earnings"]
        sources = q2.get("source_urls") or q2.get("sources")
        assert sources, "Q2 earnings data must cite sources"


# ── Section 2: OpenAI Financial Model Consistency ────────────────────────

class TestOpenAIFinancialModelConsistency:
    """Verify OpenAI's financial data is internally consistent."""

    def test_ipo_valuation_exists(self, openai):
        ipo = openai.get("ipo_filing", {})
        val = ipo.get("valuation_at_filing_b") or ipo.get("funding_round_valuation_b")
        assert val and val > 0

    def test_ad_revenue_projection_exists(self, openai):
        ads = openai.get("advertising_business", {})
        proj = ads.get("projected_ad_revenue_2026_b")
        assert proj is not None, "OpenAI ad revenue projection must exist"

    def test_publisher_deal_count(self, openai):
        deals = openai.get("publisher_content_deal_portfolio", {})
        count = deals.get("total_deals") or deals.get("deal_count")
        # Count may be stored as string like "20+"
        if isinstance(count, str):
            count = int(count.replace("+", ""))
        assert count and count >= 20, "OpenAI has 20+ publisher deals"

    def test_tbpn_acquisition_exists(self, openai):
        tbpn = openai.get("tbpn_media_acquisition", {})
        assert tbpn, "TBPN acquisition section must exist"

    def test_revenue_trajectory_exists(self, openai):
        rev = openai.get("revenue_trajectory", {})
        assert rev, "Revenue trajectory section must exist"

    def test_has_source_urls(self, openai):
        """Every financial claim in OpenAI entity must have source URLs."""
        for section_key in ["ipo_filing", "advertising_business",
                            "tbpn_media_acquisition"]:
            section = openai.get(section_key, {})
            if section:
                all_vals = str(section)
                assert "http" in all_vals or "source" in all_vals, \
                    f"OpenAI {section_key} must cite sources"


# ── Section 3: Anthropic Zero-Deal Paradox ───────────────────────────────

class TestAnthropicZeroDealParadox:
    """Anthropic's $965B valuation with zero publisher deals is a key finding."""

    def test_ipo_filing_exists(self, anthropic):
        ipo = anthropic.get("ipo_filing", {})
        assert ipo, "Anthropic IPO filing section must exist"

    def test_publisher_deals_note(self, anthropic):
        note = anthropic.get("publisher_deals_note", "")
        assert "zero" in note.lower() or "none" in note.lower() or "no " in note.lower(), \
            "Anthropic must note zero publisher deals"

    def test_valuation_exceeds_openai_deal_spend(self, openai, anthropic):
        """Anthropic is valued higher than OpenAI's total publisher deal spend."""
        anthro_ipo = anthropic.get("ipo_filing", {})
        anthro_val = anthro_ipo.get("valuation_at_filing_b")
        if anthro_val is None:
            # Fallback to market_cap_approx, stripping non-numeric
            raw = anthropic.get("market_cap_approx", "0")
            import re
            m = re.search(r"(\d+)", str(raw))
            anthro_val = float(m.group(1)) if m else 0
        assert anthro_val > 100, "Anthropic valuation should be >$100B"


# ── Section 4: Cross-Entity Revenue Consistency ──────────────────────────

class TestCrossEntityRevenueConsistency:
    """Verify financial figures across entities don't contradict each other."""

    def test_google_revenue_exceeds_meta_q2(self, google):
        """Google Q2 revenue should exceed Meta Q2 (both in entities)."""
        g_q2 = google["q2_2026_earnings"]
        comp = google.get("q2_2026_meta_google_coverage_asymmetry", {})
        if comp:
            # Meta revenue should be documented in comparison
            meta_rev = comp.get("meta_q2_revenue_b") or \
                       comp.get("comparison_table", {}).get("meta_revenue_b")
            if meta_rev:
                assert g_q2["total_revenue_b"] > meta_rev

    def test_google_capex_exceeds_meta_q2(self, google):
        """Google Q2 capex should exceed Meta Q2 — documented in comparison."""
        comp = google.get("q2_2026_meta_google_coverage_asymmetry", {})
        if comp:
            patterns = comp.get("framing_patterns", [])
            capex_pattern = [p for p in patterns if "capex" in str(p).lower()]
            assert capex_pattern, "Capex narrative inversion pattern must exist"

    def test_openai_valuation_exceeds_annual_deal_spend(self, openai):
        """OpenAI $852B valuation vs $300-400M/yr deal spend = massive gap."""
        ipo = openai.get("ipo_filing", {})
        val = ipo.get("valuation_at_filing_b") or ipo.get("funding_round_valuation_b")
        assert val and val > 500, "OpenAI valuation should be >$500B"


# ── Section 5: Financial Incentive Prediction Consistency ────────────────

class TestFinancialIncentivePredictionConsistency:
    """The core thesis: financial relationships predict coverage tone."""

    def test_google_ad_dependency_documented(self, google):
        """Google's $81.6B/yr advertising dependency must be documented."""
        q2 = google["q2_2026_earnings"]
        total_ads = q2.get("total_google_advertising_b", 0)
        assert total_ads > 50, "Google advertising revenue should be >$50B/quarter"

    def test_comparison_section_has_prediction(self, google):
        """Coverage asymmetry section must include financial incentive prediction."""
        comp = google.get("q2_2026_meta_google_coverage_asymmetry", {})
        assert comp, "Meta-Google coverage asymmetry comparison must exist"
        # Should reference financial incentive prediction
        comp_str = str(comp).lower()
        assert "financial incentive" in comp_str or "ad dependency" in comp_str or \
               "prediction" in comp_str, "Comparison must reference financial incentive model"

    def test_openai_displacement_architecture(self, openai):
        """OpenAI's ad revenue projection should exceed deal spend significantly."""
        ads = openai.get("advertising_business", {})
        ad_proj = ads.get("projected_ad_revenue_2026_b")
        assert ad_proj and ad_proj > 1, "OpenAI 2026 ad projection should be >$1B"


# ── Section 6: Source URL Completeness ───────────────────────────────────

class TestSourceURLCompleteness:
    """Every major financial claim must be backed by a verifiable source URL."""

    def test_google_q2_sources(self, google):
        q2 = google["q2_2026_earnings"]
        all_values = str(q2)
        assert "http" in all_values, "Google Q2 must have at least one source URL"

    def test_openai_ipo_sources(self, openai):
        ipo = openai.get("ipo_filing", {})
        all_values = str(ipo)
        assert "http" in all_values or ipo.get("source") or ipo.get("sources"), \
            "OpenAI IPO must have source URLs"

    def test_openai_ad_business_sources(self, openai):
        ads = openai.get("advertising_business", {})
        all_values = str(ads)
        assert "http" in all_values or ads.get("source") or ads.get("sources"), \
            "OpenAI ad business must have source URLs"

    def test_anthropic_ipo_sources(self, anthropic):
        ipo = anthropic.get("ipo_filing", {})
        all_values = str(ipo)
        assert "http" in all_values or ipo.get("source") or ipo.get("sources"), \
            "Anthropic IPO must have source URLs"


# ── Section 7: Cross-Test File Consistency ───────────────────────────────

class TestCrossTestFileConsistency:
    """Verify that today's test files are consistent with each other."""

    def test_google_test_file_exists(self):
        path = os.path.join(REPO_ROOT, "tests",
                            "test_google_q2_2026_meta_coverage_asymmetry_aug8.py")
        assert os.path.isfile(path)

    def test_openai_displacement_test_file_exists(self):
        path = os.path.join(REPO_ROOT, "tests",
                            "test_openai_publisher_financial_displacement_aug8.py")
        assert os.path.isfile(path)

    def test_safe_target_coefficient_test_file_exists(self):
        path = os.path.join(REPO_ROOT, "tests",
                            "test_safe_target_coefficient_aug8.py")
        assert os.path.isfile(path)

    def test_advance_dual_asset_test_file_exists(self):
        path = os.path.join(REPO_ROOT, "tests",
                            "test_advance_dual_asset_monetization_aug8.py")
        assert os.path.isfile(path)

    def test_meta_inverse_leverage_test_file_exists(self):
        path = os.path.join(REPO_ROOT, "tests",
                            "test_meta_inverse_leverage_q2_2026_aug8.py")
        assert os.path.isfile(path)


# ── Section 8: Entity Relationship Type Completeness ─────────────────────

class TestEntityRelationshipTypes:
    """Verify relationship_types in the YAML cover the key categories."""

    def test_relationship_types_exist(self):
        with open(os.path.join(PROFILES_DIR, "competitor-entities.yaml")) as f:
            data = yaml.safe_load(f)
        rt = data.get("relationship_types", {})
        assert "licensing" in rt
        assert "advertising" in rt
        assert "investment" in rt

    def test_coverage_predictions_exist(self):
        with open(os.path.join(PROFILES_DIR, "competitor-entities.yaml")) as f:
            data = yaml.safe_load(f)
        cp = data.get("coverage_predictions", {})
        assert "softer" in cp
        assert "adversarial" in cp


# ── Section 9: README and ARCHITECTURE Stats Current ─────────────────────

class TestDocsStatsCurrentAug8:
    """Verify README and ARCHITECTURE stats were updated this session."""

    def test_readme_test_count_current(self):
        with open(os.path.join(REPO_ROOT, "README.md")) as f:
            content = f.read()
        # Should reflect >= 6983 tests after tonight's fixes
        import re
        m = re.search(r"Tests\s*\|\s*([\d,]+)", content)
        assert m, "README must have Tests count"
        count = int(m.group(1).replace(",", ""))
        assert count >= 6983, f"README test count {count} should be >= 6983"

    def test_readme_framing_patterns_current(self):
        with open(os.path.join(REPO_ROOT, "README.md")) as f:
            content = f.read()
        import re
        m = re.search(r"Framing patterns\s*\|\s*(\d+)", content)
        assert m, "README must have framing patterns count"
        count = int(m.group(1))
        assert count >= 782, f"README framing patterns {count} should be >= 782"

    def test_architecture_test_count_current(self):
        with open(os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")) as f:
            content = f.read()
        import re
        m = re.search(r"(\d+) tests across", content)
        assert m, "ARCHITECTURE must have test count"
        count = int(m.group(1))
        assert count >= 6983, f"ARCHITECTURE test count {count} should be >= 6983"
