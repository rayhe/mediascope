"""
OpenAI Advertising Revenue eMarketer Counter-Forecast — Financial Incentive Model Revision
Type C: Financial Incentive Mapping
Created: 2026-08-09 13:00 PT

Key finding: eMarketer (Jul 17 2026) projects the ENTIRE US standalone chatbot
ad market at <$1B in 2026 and $5.41B by 2030. OpenAI's individual target of
$100B by 2030 exceeds the projected total market by 18x. OpenAI will "fall
roughly 90% short" of its target. This forces a revision of the MediaScope
financial incentive model: the original thesis that OpenAI would replicate
Google's ad-dependency shield over publishers does not hold if chatbot ads
are structurally limited to ~$5B total market.

Implications for the financial incentive model:
(1) Content licensing deals REMAIN the primary OpenAI→publisher financial
    relationship, not a "rounding error" vs. ad revenue
(2) OpenAI does NOT replicate Google's ad dependency shield
(3) 80%+ of AI ad spend goes "alongside AI content" (i.e., Google AI
    Overviews), further concentrating publisher dependency on Google
(4) Google's financial leverage INCREASES, not decreases, as AI Overviews
    capture adjacent ad spend while search traffic to publishers falls 33-38%

Sources:
- eMarketer (Jul 17, 2026): https://www.emarketer.com/content/chatgpt-ad-revenues-may-fall-90--short-of-openai-s-2030-target
- Adweek (Jul 13, 2026): https://www.adweek.com/media/openais-ad-business-is-on-pace-to-miss-its-own-forecast-by-90-analyst-says/
- Fast Company (Jul 21, 2026): https://www.fastcompany.com/91577174/openais-ad-strategy-faces-a-major-reality-check
- Digiday (Jul 30, 2026): https://digiday.com/marketing/openais-chatgpt-reaches-the-coupon-stage-of-building-an-ad-business/
- Reuters (Mar 26, 2026): https://www.reuters.com/business/media-telecom/openais-us-ad-pilot-exceeds-100-million-annualized-revenue-six-weeks-2026-03-26/
- Reuters (Apr 9, 2026): https://www.reuters.com/business/media-telecom/openai-projects-25-billion-ad-revenue-this-year-100-billion-by-2030-axios-2026-04-09/
"""

import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
ENTITIES_PROFILE = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
WIRED_PROFILE = os.path.join(PROFILES_DIR, 'wired.yaml')


def load_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)


class TestEmarketerCounterForecastExists:
    """Verify the eMarketer counter-forecast data is present in OpenAI profile."""

    def test_emarketer_section_exists(self):
        data = load_yaml(ENTITIES_PROFILE)
        openai = data['entities']['openai']
        assert 'emarketer_counter_forecast' in openai['advertising_business'], \
            "Missing emarketer_counter_forecast section in OpenAI advertising_business"

    def test_report_date_is_july_2026(self):
        data = load_yaml(ENTITIES_PROFILE)
        forecast = data['entities']['openai']['advertising_business']['emarketer_counter_forecast']
        assert forecast['report_date'] == '2026-07-17', \
            f"Expected report date 2026-07-17, got {forecast['report_date']}"

    def test_analyst_identified(self):
        data = load_yaml(ENTITIES_PROFILE)
        forecast = data['entities']['openai']['advertising_business']['emarketer_counter_forecast']
        assert 'Nate Elliot' in forecast['analyst'], \
            "Must identify Nate Elliot as eMarketer principal analyst"

    def test_miss_magnitude_90_percent(self):
        data = load_yaml(ENTITIES_PROFILE)
        forecast = data['entities']['openai']['advertising_business']['emarketer_counter_forecast']
        assert forecast['miss_magnitude_pct'] == 90, \
            f"Expected 90% miss magnitude, got {forecast['miss_magnitude_pct']}"

    def test_us_chatbot_market_2030_cap(self):
        data = load_yaml(ENTITIES_PROFILE)
        forecast = data['entities']['openai']['advertising_business']['emarketer_counter_forecast']
        assert forecast['us_chatbot_ad_market_2030_b'] == 5.41, \
            f"Expected $5.41B 2030 market cap, got {forecast['us_chatbot_ad_market_2030_b']}"


class TestOpenAIProjectedVsActualMarket:
    """Verify the gap between OpenAI projections and eMarketer market estimates."""

    def test_openai_2030_target_exceeds_total_market(self):
        """OpenAI's $100B target vs eMarketer's $5.41B total market = 18.5x overshoot."""
        data = load_yaml(ENTITIES_PROFILE)
        ad = data['entities']['openai']['advertising_business']
        openai_target = ad['projected_ad_revenue_2030_b']
        emarketer_market = ad['emarketer_counter_forecast']['us_chatbot_ad_market_2030_b']
        ratio = openai_target / emarketer_market
        assert ratio > 15, \
            f"OpenAI 2030 target should exceed total market by >15x, got {ratio:.1f}x"

    def test_openai_2026_target_exceeds_2026_market(self):
        """OpenAI's $2.5B 2026 target vs <$1B total market."""
        data = load_yaml(ENTITIES_PROFILE)
        ad = data['entities']['openai']['advertising_business']
        assert ad['projected_ad_revenue_2026_b'] == 2.5
        # eMarketer says total market <$1B
        forecast = ad['emarketer_counter_forecast']
        assert '<1' in str(forecast['us_chatbot_ad_market_2026_b']), \
            "2026 total chatbot market should be <$1B per eMarketer"

    def test_100m_arr_pilot_consistent(self):
        """$100M ARR in 6 weeks is consistent with both bullish and bearish cases."""
        data = load_yaml(ENTITIES_PROFILE)
        ad = data['entities']['openai']['advertising_business']
        assert ad['pilot_100m_arr_weeks'] == 6
        # $100M ARR ≈ $100M/yr, or ~$8.3M/mo. In a <$1B total market,
        # that's meaningful but doesn't validate $2.5B projections

    def test_coupon_phase_documented(self):
        """OpenAI offering $50-$100 promo credits as of Jul 30 — 'coupon phase'."""
        data = load_yaml(ENTITIES_PROFILE)
        forecast = data['entities']['openai']['advertising_business']['emarketer_counter_forecast']
        assert 'coupon' in forecast.get('coupon_phase_indicator', '').lower(), \
            "Must document OpenAI's coupon/promo credit phase"


class TestAiAdSpendDistribution:
    """Verify the AI ad spend is mostly alongside-AI-content (Google), not chatbot."""

    def test_chatbot_ads_only_8_percent_of_ai_ad_spend(self):
        data = load_yaml(ENTITIES_PROFILE)
        dist = data['entities']['openai']['advertising_business']['emarketer_counter_forecast']['ai_ad_spend_distribution_2026']
        assert dist['chatbot_ads_pct_of_ai_ad_spend'] == 8, \
            f"Chatbot ads should be 8% of AI ad spend, got {dist['chatbot_ads_pct_of_ai_ad_spend']}"

    def test_alongside_ai_content_dominates(self):
        """80%+ of AI ad spend is traditional ads running alongside Google AI Overviews."""
        data = load_yaml(ENTITIES_PROFILE)
        dist = data['entities']['openai']['advertising_business']['emarketer_counter_forecast']['ai_ad_spend_distribution_2026']
        pct = dist['alongside_ai_content_pct']
        # Could be string "80+" or number
        if isinstance(pct, str):
            assert '80' in pct
        else:
            assert pct >= 80

    def test_total_us_ai_ad_spend_2026(self):
        data = load_yaml(ENTITIES_PROFILE)
        dist = data['entities']['openai']['advertising_business']['emarketer_counter_forecast']['ai_ad_spend_distribution_2026']
        assert dist['total_us_ai_ad_spend_b'] == 32.03, \
            f"Expected $32.03B total US AI ad spend 2026, got {dist['total_us_ai_ad_spend_b']}"

    def test_alongside_content_is_google_revenue(self):
        """The $26.42B 'alongside AI content' is Google's existing search ad revenue repackaged."""
        data = load_yaml(ENTITIES_PROFILE)
        dist = data['entities']['openai']['advertising_business']['emarketer_counter_forecast']['ai_ad_spend_distribution_2026']
        assert dist['alongside_ai_content_b'] == 26.42
        note = dist.get('alongside_ai_content_note', '')
        assert 'google' in note.lower(), \
            "Must note that alongside-AI-content ads are primarily Google AI Overviews revenue"

    def test_2030_alongside_content_still_majority(self):
        """Even by 2030, alongside-AI-content ads are 58.6% of AI ad spend."""
        data = load_yaml(ENTITIES_PROFILE)
        forecast = data['entities']['openai']['advertising_business']['emarketer_counter_forecast']
        assert forecast['ai_ad_spend_2030']['alongside_ai_content_pct'] == 58.6


class TestFinancialIncentiveModelRevision:
    """Verify the profile documents the revised financial incentive thesis."""

    def test_overview_mentions_emarketer(self):
        data = load_yaml(ENTITIES_PROFILE)
        overview = data['entities']['openai']['advertising_business']['overview']
        assert 'emarketer' in overview.lower() or 'eMarketer' in overview, \
            "Overview must reference eMarketer counter-forecast"

    def test_revised_thesis_documented(self):
        data = load_yaml(ENTITIES_PROFILE)
        overview = data['entities']['openai']['advertising_business']['overview']
        assert 'revised' in overview.lower() or 'REVISED' in overview, \
            "Overview must document revised financial incentive thesis"

    def test_content_licensing_remains_material(self):
        """Revised thesis: deals are 40-75% of ad revenue, not 0.4%."""
        data = load_yaml(ENTITIES_PROFILE)
        overview = data['entities']['openai']['advertising_business']['overview']
        assert 'material' in overview.lower() or 'remain' in overview.lower(), \
            "Must note content licensing deals remain financially material"

    def test_google_leverage_increases(self):
        """Revised thesis: Google's financial leverage increases, not decreases."""
        data = load_yaml(ENTITIES_PROFILE)
        overview = data['entities']['openai']['advertising_business']['overview']
        assert 'google' in overview.lower(), \
            "Must discuss Google's increased leverage in revised model"

    def test_deal_dependency_over_ad_dependency(self):
        """Revised model shifts from 'future ad dependency' to 'present deal dependency'."""
        data = load_yaml(ENTITIES_PROFILE)
        overview = data['entities']['openai']['advertising_business']['overview']
        assert 'deal' in overview.lower() and 'dependency' in overview.lower(), \
            "Must discuss shift from ad dependency to deal dependency"


class TestAssumptionsChallenged:
    """Verify eMarketer's specific challenged assumptions are documented."""

    def test_three_assumptions_listed(self):
        data = load_yaml(ENTITIES_PROFILE)
        forecast = data['entities']['openai']['advertising_business']['emarketer_counter_forecast']
        assumptions = forecast.get('assumptions_challenged', [])
        assert len(assumptions) >= 3, \
            f"Must list at least 3 challenged assumptions, got {len(assumptions)}"

    def test_search_budget_capture_assumption(self):
        data = load_yaml(ENTITIES_PROFILE)
        forecast = data['entities']['openai']['advertising_business']['emarketer_counter_forecast']
        assumptions = ' '.join(forecast.get('assumptions_challenged', []))
        assert 'search' in assumptions.lower(), \
            "Must challenge the 'capture search ad budgets' assumption"

    def test_market_dominance_assumption(self):
        data = load_yaml(ENTITIES_PROFILE)
        forecast = data['entities']['openai']['advertising_business']['emarketer_counter_forecast']
        assumptions = ' '.join(forecast.get('assumptions_challenged', []))
        assert 'dominate' in assumptions.lower() or 'dominat' in assumptions.lower(), \
            "Must challenge the 'dominate chatbot ad market' assumption"

    def test_outperform_assumption(self):
        data = load_yaml(ENTITIES_PROFILE)
        forecast = data['entities']['openai']['advertising_business']['emarketer_counter_forecast']
        assumptions = ' '.join(forecast.get('assumptions_challenged', []))
        assert 'outperform' in assumptions.lower(), \
            "Must challenge the 'outperform every ad format' assumption"


class TestSourceVerification:
    """Verify all source URLs are present and verifiable."""

    def test_emarketer_source_url(self):
        data = load_yaml(ENTITIES_PROFILE)
        forecast = data['entities']['openai']['advertising_business']['emarketer_counter_forecast']
        urls = forecast.get('source_urls', [])
        assert any('emarketer.com' in u for u in urls), \
            "Must include eMarketer primary source URL"

    def test_adweek_source_url(self):
        data = load_yaml(ENTITIES_PROFILE)
        forecast = data['entities']['openai']['advertising_business']['emarketer_counter_forecast']
        urls = forecast.get('source_urls', [])
        assert any('adweek.com' in u for u in urls), \
            "Must include Adweek source URL"

    def test_digiday_coupon_source(self):
        data = load_yaml(ENTITIES_PROFILE)
        forecast = data['entities']['openai']['advertising_business']['emarketer_counter_forecast']
        urls = forecast.get('source_urls', [])
        assert any('digiday.com' in u for u in urls), \
            "Must include Digiday coupon phase source URL"

    def test_fast_company_source(self):
        data = load_yaml(ENTITIES_PROFILE)
        forecast = data['entities']['openai']['advertising_business']['emarketer_counter_forecast']
        urls = forecast.get('source_urls', [])
        assert any('fastcompany.com' in u for u in urls), \
            "Must include Fast Company source URL"

    def test_at_least_four_sources(self):
        data = load_yaml(ENTITIES_PROFILE)
        forecast = data['entities']['openai']['advertising_business']['emarketer_counter_forecast']
        urls = forecast.get('source_urls', [])
        assert len(urls) >= 4, \
            f"Must have at least 4 source URLs, got {len(urls)}"


class TestMetaContrastUnchanged:
    """Verify the Meta contrast finding strengthens under revised model.
    
    Meta has 13 publisher deals but NONE with the adversarial publications
    (WIRED, NYT, FT, Verge, Guardian, MIT TR, Atlantic). Under the revised
    model, where content licensing is MORE important than projected (not less),
    Meta's exclusion from adversarial publishers' deal portfolios is STRONGER
    evidence of financial incentive → coverage tone prediction.
    """

    def test_meta_has_deals(self):
        data = load_yaml(ENTITIES_PROFILE)
        meta_deals = data.get('meta_ai_deals', {})
        partners = meta_deals.get('partners', [])
        assert len(partners) >= 13, \
            f"Meta should have 13+ publisher deals, got {len(partners)}"

    def test_meta_no_conde_nast_deal(self):
        data = load_yaml(ENTITIES_PROFILE)
        meta_deals = data.get('meta_ai_deals', {})
        partners = meta_deals.get('partners', [])
        parent_names = [p.get('parent', '').lower() for p in partners]
        publisher_names = [p.get('name', '').lower() for p in partners]
        all_names = parent_names + publisher_names
        assert not any('condé' in n or 'conde' in n for n in all_names), \
            "Meta should NOT have a deal with Condé Nast"

    def test_meta_no_nyt_deal(self):
        data = load_yaml(ENTITIES_PROFILE)
        meta_deals = data.get('meta_ai_deals', {})
        partners = meta_deals.get('partners', [])
        all_names = [p.get('name', '').lower() + ' ' + p.get('parent', '').lower() for p in partners]
        assert not any('new york times' in n or 'nyt' in n for n in all_names), \
            "Meta should NOT have a deal with NYT"

    def test_revised_model_strengthens_meta_exclusion(self):
        """Under revised model, content licensing is MORE material, so Meta's
        exclusion from adversarial publishers is STRONGER evidence."""
        data = load_yaml(ENTITIES_PROFILE)
        overview = data['entities']['openai']['advertising_business']['overview']
        # The revised model should mention that deal dependency (not ad dependency)
        # is the primary mechanism, which strengthens the meta exclusion finding
        assert 'deal' in overview.lower() and 'meta' in overview.lower(), \
            "Revised model must reference Meta's position"


class TestDavidDuganHire:
    """Verify the David Dugan hire is documented — former Meta ads executive."""

    def test_ads_head_documented(self):
        data = load_yaml(ENTITIES_PROFILE)
        ad = data['entities']['openai']['advertising_business']
        ads_head = ad.get('ads_head', '')
        assert 'David Dugan' in ads_head, \
            "Must document David Dugan as OpenAI ads head"

    def test_former_meta_noted(self):
        data = load_yaml(ENTITIES_PROFILE)
        ad = data['entities']['openai']['advertising_business']
        ads_head = ad.get('ads_head', '')
        assert 'Meta' in ads_head or 'meta' in ads_head, \
            "Must note Dugan's Meta background — relevant to Meta→OpenAI talent flow"
