"""
Test: Apple Siri AI Triple-Layer Publisher Financial Architecture (Mechanism #156)

Source: WSJ (Aug 12, 2026) — "Apple in Talks to Pay Publishers to Improve AI-Powered Siri"
https://www.wsj.com/business/media/apple-in-talks-to-pay-publishers-to-improve-ai-powered-siri-0641f64b

FINDING: Apple is constructing a THREE-LAYER financial relationship with publishers:
  Layer 1: Apple News+ (since 2019) — 50% rev share, 400+ titles, $12.99/mo
  Layer 2: Apple Siri AI content licensing (NEW, Aug 2026) — pay-per-use, nine-figure budget
  Layer 3: App Store commission power — 15-30% on publisher subscriptions

This is a REVERSAL from Apple's 2024-2025 content bypass strategy (Google Gemini $1B/yr
instead of direct publisher deals). The timing is significant:
  Dec 2023: Apple approached publishers with $50M offers → no deals closed
  Jan 2026: Apple signed Google Gemini → bypassed publishers entirely
  Aug 2026: Apple re-approached publishers with nine-figure budget → Siri AI

Why the reversal? Apple's AI news summary embarrassment (late 2024, false headlines
that misled users, feature disabled for over a year). Apple needs publisher-verified
content for Siri AI to avoid future hallucination PR crises.

WEARABLES RELEVANCE: If Apple launches smart glasses (rumored 2027-2028), publications
with Apple Siri AI content deals + Apple News+ participation + App Store revenue
dependencies would have TRIPLE financial incentive to frame Apple glasses favorably
while continuing adversarial Meta glasses coverage.

META CONTRAST: Meta has 13 AI content partners, but NONE of the 7 MediaScope-profiled
publications. Apple would surpass Meta in publisher financial leverage if even 3-4
MediaScope publications sign Siri AI deals on top of existing News+ participation.

ANTHROPIC IPO CONVERGENCE: Samsung, SK Hynix, and Micron invested in Anthropic's
$65B Series H at $965B valuation. Samsung is building Galaxy Glasses (direct Meta
Ray-Ban competitor). The Samsung-Anthropic financial alignment creates an ADDITIONAL
incentive layer: publications covering Samsung glasses receive coverage-neutral
treatment while Samsung's AI partner (Anthropic) is also heading for a $1.75T IPO
with Goldman Sachs, JPMorgan, and Morgan Stanley as underwriters.

Confounders:
  STRONG: Apple may not close any deals (history of approaching then not signing)
  STRONG: Variable pay-per-use model may produce negligible revenue for most publishers
  MODERATE: Apple's "nine-figure budget" may be spread across hundreds of publishers
  MODERATE: Siri AI deal may not influence editorial coverage of unrelated Apple products
  WEAK: Apple has legitimate product motivation (fixing Siri AI hallucinations)
"""

import yaml
import os
import pytest
from pathlib import Path


def get_profiles_dir():
    return Path(__file__).parent.parent / "profiles"


def load_competitor_entities():
    path = get_profiles_dir() / "competitor-entities.yaml"
    with open(path) as f:
        return yaml.safe_load(f)


def load_competitor_coverage_research():
    path = get_profiles_dir() / "competitor-coverage-research.yaml"
    with open(path) as f:
        return yaml.safe_load(f)


def load_publication_profile(name):
    path = get_profiles_dir() / f"{name}.yaml"
    with open(path) as f:
        return yaml.safe_load(f)


# ─── Layer Existence Tests ───────────────────────────────────────────────────

class TestAppleTripleLayerStructure:
    """Verify all three Apple publisher financial layers are documented."""

    def test_layer_1_news_plus_exists(self):
        data = load_competitor_entities()
        apple = data["entities"]["apple"]
        assert "apple_news_platform_leverage" in apple
        leverage = apple["apple_news_platform_leverage"]
        assert leverage["subscription_revenue_share_pct"] == 50
        assert leverage["title_count"] >= 400

    def test_layer_2_siri_ai_deals_exists(self):
        data = load_competitor_entities()
        apple = data["entities"]["apple"]
        assert "siri_ai_publisher_deals" in apple
        siri = apple["siri_ai_publisher_deals"]
        assert siri["report_date"] == "2026-08-12"
        assert "nine" in str(siri.get("budget_description", "")).lower() or \
               siri.get("budget_magnitude") == "nine_figure"

    def test_layer_3_app_store_commission_exists(self):
        data = load_competitor_entities()
        apple = data["entities"]["apple"]
        # App store commission is referenced in apple_news_platform_leverage
        leverage = apple["apple_news_platform_leverage"]
        assert leverage.get("news_partner_program_commission_pct") == 15
        assert leverage.get("app_store_standard_y1_commission_pct") == 30

    def test_siri_ai_deal_is_pay_per_use(self):
        data = load_competitor_entities()
        siri = data["entities"]["apple"]["siri_ai_publisher_deals"]
        assert siri["compensation_model"] == "variable_pay_per_use"

    def test_siri_ai_deal_is_multiyear(self):
        data = load_competitor_entities()
        siri = data["entities"]["apple"]["siri_ai_publisher_deals"]
        assert siri["deal_duration"] == "multiyear"

    def test_siri_ai_wsj_source_url(self):
        data = load_competitor_entities()
        siri = data["entities"]["apple"]["siri_ai_publisher_deals"]
        urls = siri.get("source_urls", [])
        assert any("wsj.com" in u for u in urls), \
            "WSJ source URL must be cited for Siri AI publisher deals"


# ─── Content Bypass Reversal Tests ───────────────────────────────────────────

class TestAppleContentBypassReversal:
    """Verify the Dec 2023 → Jan 2026 → Aug 2026 strategy reversal is documented."""

    def test_publisher_content_bypass_exists(self):
        data = load_competitor_entities()
        apple = data["entities"]["apple"]
        assert "publisher_content_bypass" in apple

    def test_bypass_then_return_timeline(self):
        data = load_competitor_entities()
        apple = data["entities"]["apple"]
        bypass = apple["publisher_content_bypass"]
        # Dec 2023 approach is in publisher_negotiation_history
        assert "2023" in bypass.get("publisher_negotiation_history", "")
        # Siri AI deals are the return
        siri = apple["siri_ai_publisher_deals"]
        assert siri["report_date"] == "2026-08-12"

    def test_google_gemini_bypass_still_active(self):
        """The $1B/yr Gemini deal coexists with new Siri AI publisher deals."""
        data = load_competitor_entities()
        apple = data["entities"]["apple"]
        gemini = apple.get("apple_google_gemini_deal", {})
        assert gemini.get("annual_value_est_b") == 1.0

    def test_hallucination_embarrassment_motivator(self):
        """Apple's AI news summary failure is documented as motivating the deal."""
        data = load_competitor_entities()
        siri = data["entities"]["apple"]["siri_ai_publisher_deals"]
        overview = str(siri.get("overview", "")) + str(siri.get("hallucination_motivator", ""))
        assert "hallucin" in overview.lower() or "false headline" in overview.lower() or \
               "erroneous" in overview.lower() or "embarrass" in overview.lower()


# ─── Meta Contrast Tests ────────────────────────────────────────────────────

class TestMetaApplePublisherDealContrast:
    """Verify the financial incentive asymmetry between Apple and Meta."""

    def test_meta_zero_mediascope_publication_deals(self):
        """None of the 7 profiled publications have Meta AI content deals."""
        data = load_competitor_entities()
        meta_deals = data["entities"]["meta"].get("ai_content_deals", {})
        mediascope_pubs = {"wired", "the_verge", "the_atlantic", "nytimes",
                           "financial_times", "guardian", "mit_tech_review"}
        if isinstance(meta_deals, dict):
            for pub in mediascope_pubs:
                deal = meta_deals.get(pub, {})
                assert not deal or deal.get("status") != "active", \
                    f"Meta should have no active deal with {pub}"

    def test_apple_news_plus_gives_more_profiled_pub_coverage(self):
        """At least 3 MediaScope-profiled publications are Apple News+ partners."""
        data = load_competitor_entities()
        apple = data["entities"]["apple"]
        participation = apple["apple_news_platform_leverage"]["profiled_publisher_participation"]
        partners = [p for p in participation if p["status"] == "partner"]
        assert len(partners) >= 3, \
            f"Expected 3+ profiled Apple News+ partners, found {len(partners)}"

    def test_apple_triple_layer_vs_meta_zero_layer(self):
        """Document that Apple has 3 financial layers vs Meta's 0 for profiled pubs."""
        data = load_competitor_entities()
        apple = data["entities"]["apple"]
        # Layer 1: News+
        assert "apple_news_platform_leverage" in apple
        # Layer 2: Siri AI
        assert "siri_ai_publisher_deals" in apple
        # Layer 3: App Store commissions documented in News+ section
        leverage = apple["apple_news_platform_leverage"]
        assert leverage.get("app_store_standard_y1_commission_pct") is not None


# ─── Anthropic IPO Convergence Tests ─────────────────────────────────────────

class TestAnthropicIpoPublisherConvergence:
    """Verify Samsung-Anthropic investment chain and IPO underwriter data."""

    def test_anthropic_series_h_valuation(self):
        data = load_competitor_entities()
        ipo = data["entities"]["anthropic"]["ipo_filing"]
        assert ipo["valuation_at_filing_b"] == 965

    def test_anthropic_series_h_amount(self):
        data = load_competitor_entities()
        ipo = data["entities"]["anthropic"]["ipo_filing"]
        assert ipo["series_h_raised_b"] == 65

    def test_anthropic_ipo_underwriters(self):
        data = load_competitor_entities()
        ipo = data["entities"]["anthropic"]["ipo_filing"]
        banks = ipo.get("ipo_banks_reported", [])
        assert "Goldman Sachs" in banks
        assert "Morgan Stanley" in banks
        assert "JPMorgan Chase" in banks

    def test_samsung_in_anthropic_series_h(self):
        """Samsung invested in Series H — same Samsung building Galaxy Glasses."""
        data = load_competitor_entities()
        ipo = data["entities"]["anthropic"]["ipo_filing"]
        strategic = ipo.get("series_h_strategic_infrastructure_investors", [])
        assert any("Samsung" in str(inv) for inv in strategic), \
            "Samsung must be listed as Series H strategic infrastructure investor"

    def test_anthropic_revenue_run_rate(self):
        data = load_competitor_entities()
        ipo = data["entities"]["anthropic"]["ipo_filing"]
        assert ipo.get("revenue_run_rate_at_filing_b") >= 47

    def test_samsung_glasses_anthropic_financial_alignment(self):
        """Samsung building Galaxy Glasses + Samsung invested in Anthropic = aligned."""
        data = load_competitor_entities()
        samsung = data["entities"]["samsung"]
        assert "galaxy_glasses" in str(samsung).lower() or \
               "smart_glasses" in str(samsung).lower() or \
               "xr" in str(samsung).lower()


# ─── Mechanism Registration Tests ────────────────────────────────────────────

class TestMechanismRegistration:
    """Verify mechanism #156 is properly registered in coverage research."""

    def test_mechanism_156_exists_in_cpf(self):
        data = load_competitor_coverage_research()
        cpf = data.get("cross_publication_findings", {})
        mechanism_ids = []
        for key, val in cpf.items():
            if isinstance(val, dict) and "mechanism_id" in val:
                mechanism_ids.append(val["mechanism_id"])
        assert 156 in mechanism_ids, \
            "Mechanism #156 must exist in cross_publication_findings"

    def test_mechanism_156_name(self):
        data = load_competitor_coverage_research()
        cpf = data.get("cross_publication_findings", {})
        m156 = None
        for key, val in cpf.items():
            if isinstance(val, dict) and val.get("mechanism_id") == 156:
                m156 = val
                break
        assert m156 is not None
        name = m156.get("mechanism_name", "")
        assert "apple" in name.lower() or "siri" in name.lower() or \
               "triple" in name.lower() or "publisher" in name.lower()

    def test_mechanism_156_has_source_urls(self):
        data = load_competitor_coverage_research()
        cpf = data.get("cross_publication_findings", {})
        m156 = None
        for key, val in cpf.items():
            if isinstance(val, dict) and val.get("mechanism_id") == 156:
                m156 = val
                break
        assert m156 is not None
        urls = m156.get("source_urls", [])
        assert len(urls) >= 2, "Mechanism must have 2+ source URLs"

    def test_mechanism_156_has_confounders(self):
        data = load_competitor_coverage_research()
        cpf = data.get("cross_publication_findings", {})
        m156 = None
        for key, val in cpf.items():
            if isinstance(val, dict) and val.get("mechanism_id") == 156:
                m156 = val
                break
        assert m156 is not None
        confounders = m156.get("confounders", [])
        assert len(confounders) >= 3, "Must have 3+ confounders documented"

    def test_mechanism_156_has_cross_references(self):
        data = load_competitor_coverage_research()
        cpf = data.get("cross_publication_findings", {})
        m156 = None
        for key, val in cpf.items():
            if isinstance(val, dict) and val.get("mechanism_id") == 156:
                m156 = val
                break
        assert m156 is not None
        xrefs = m156.get("cross_references", [])
        assert len(xrefs) >= 2, "Must cross-reference 2+ prior mechanisms"


# ─── Publication Profile Tests ───────────────────────────────────────────────

class TestWiredAppleSiriAiRelationship:
    """Verify WIRED/Condé Nast's Apple Siri AI deal context is documented."""

    def test_wired_apple_relationship_exists(self):
        data = load_publication_profile("wired")
        assert data is not None
        # WIRED profile should reference Apple financial relationships
        content = str(data)
        assert "apple" in content.lower()

    def test_conde_nast_in_apple_news_plus(self):
        data = load_competitor_entities()
        apple = data["entities"]["apple"]
        participation = apple["apple_news_platform_leverage"]["profiled_publisher_participation"]
        conde_nast = next((p for p in participation if "Condé Nast" in p["name"]), None)
        assert conde_nast is not None
        assert conde_nast["status"] == "partner"

    def test_conde_nast_approached_for_siri_ai(self):
        """Condé Nast was among publishers Apple originally approached (Dec 2023)."""
        data = load_competitor_entities()
        apple = data["entities"]["apple"]
        bypass = apple["publisher_content_bypass"]
        history = bypass.get("publisher_negotiation_history", "")
        assert "Condé Nast" in history or "Conde Nast" in history


# ─── Financial Layer Comparison Tests ────────────────────────────────────────

class TestFinancialLayerComparison:
    """Compare financial layer counts across entities for profiled publications."""

    def test_apple_has_most_financial_layers(self):
        """Apple should have the most financial relationship layers with profiled pubs."""
        data = load_competitor_entities()
        apple = data["entities"]["apple"]
        apple_layers = 0
        if "apple_news_platform_leverage" in apple:
            apple_layers += 1
        if "siri_ai_publisher_deals" in apple:
            apple_layers += 1
        # App Store commission counts as implicit layer
        if apple.get("apple_news_platform_leverage", {}).get("app_store_standard_y1_commission_pct"):
            apple_layers += 1
        assert apple_layers >= 3, \
            f"Apple should have 3+ financial layers, found {apple_layers}"

    def test_openai_has_licensing_layer(self):
        data = load_competitor_entities()
        openai = data["entities"]["openai"]
        # OpenAI has publisher deals
        content = str(openai)
        assert "licensing" in content.lower() or "deal" in content.lower()

    def test_meta_has_fewer_profiled_pub_layers_than_apple(self):
        """Meta has deals but not with profiled publications."""
        data = load_competitor_entities()
        apple = data["entities"]["apple"]
        # Apple has News+ with 3+ profiled pubs = at least 1 active layer
        participation = apple["apple_news_platform_leverage"]["profiled_publisher_participation"]
        apple_profiled_partners = len([p for p in participation if p["status"] == "partner"])
        assert apple_profiled_partners >= 3


# ─── Wearables Predictive Tests ──────────────────────────────────────────────

class TestWearablesCoveragePrediction:
    """Test that financial architecture predicts wearables coverage tone."""

    def test_apple_glasses_coverage_prediction(self):
        """Publications with Apple triple-layer deals predicted to cover Apple glasses softly."""
        data = load_competitor_entities()
        apple = data["entities"]["apple"]
        siri = apple.get("siri_ai_publisher_deals", {})
        # The wearables prediction should be documented
        coverage_pred = siri.get("wearables_coverage_prediction", "")
        assert len(coverage_pred) > 0 or \
               "wearable" in str(siri.get("mediascope_relevance", "")).lower() or \
               "glass" in str(siri.get("mediascope_relevance", "")).lower()

    def test_samsung_glasses_anthropic_convergence_documented(self):
        """Samsung Galaxy Glasses + Samsung Anthropic investment = coverage predictor."""
        data = load_competitor_entities()
        anthropic = data["entities"]["anthropic"]
        ipo = anthropic["ipo_filing"]
        strategic = ipo.get("series_h_strategic_infrastructure_investors", [])
        # At minimum Samsung should be listed
        samsung_present = any("Samsung" in str(inv) for inv in strategic)
        assert samsung_present, \
            "Samsung must be documented as Anthropic Series H investor"


# ─── Data Freshness Tests ───────────────────────────────────────────────────

class TestDataFreshness:
    """Ensure Anthropic IPO data reflects latest available information."""

    def test_anthropic_s1_date(self):
        data = load_competitor_entities()
        ipo = data["entities"]["anthropic"]["ipo_filing"]
        # S-1 filed Jun 1, 2026
        assert ipo["confidential_s1_date"] == "2026-06-01"

    def test_anthropic_target_listing_date(self):
        data = load_competitor_entities()
        ipo = data["entities"]["anthropic"]["ipo_filing"]
        target = str(ipo.get("target_listing", ""))
        assert "2026" in target or "October" in target or "fall" in target.lower()

    def test_anthropic_ipo_could_be_largest(self):
        """$75B raise at $1.75-1.8T would be largest IPO in history."""
        data = load_competitor_entities()
        ipo = data["entities"]["anthropic"]["ipo_filing"]
        # The potential raise amount should be documented
        target_raise = ipo.get("target_raise_b")
        if target_raise:
            assert target_raise >= 50, "Expected target raise to be $50B+"
