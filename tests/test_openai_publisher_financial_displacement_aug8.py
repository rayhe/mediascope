"""
OpenAI Publisher Financial Displacement Architecture — Type C Financial Incentive Mapping (Aug 8, 21:00 PT)

Tests validating the emerging three-track publisher financial displacement:
1. Advertising business ($2.5B 2026, projecting $100B by 2030)
2. TBPN media acquisition (Apr 2026, "low hundreds of millions")
3. Dual IPO transparency inflection (OpenAI S-1 Jun 8, Anthropic S-1 Jun 1)

Core finding: OpenAI's projected 2026 ad revenue ($2.5B) ALREADY EXCEEDS its
total publisher content licensing spending (~$300-400M/yr), meaning content deals
are becoming a loss leader. Simultaneously, Anthropic heads to IPO at $965B with
ZERO publisher deals — validating the model of building a trillion-dollar AI
company without paying publishers anything.
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_entities():
    path = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


class TestOpenAIAdvertisingBusiness:
    """Validate OpenAI's advertising revenue data and projections."""

    def setup_method(self):
        data = load_entities()
        self.openai = data['entities']['openai']
        self.ad_biz = self.openai.get('advertising_business', {})

    def test_advertising_section_exists(self):
        assert 'advertising_business' in self.openai, \
            "OpenAI entity must have advertising_business section"

    def test_pilot_launch_date(self):
        assert self.ad_biz.get('launched') == '2026-01', \
            "Ads pilot launched January 2026"

    def test_ads_manager_launch_date(self):
        assert self.ad_biz.get('ads_manager_launched') == '2026-04', \
            "Self-serve Ads Manager launched April 2026"

    def test_pilot_100m_arr_within_6_weeks(self):
        weeks = self.ad_biz.get('pilot_100m_arr_weeks', 0)
        assert weeks <= 6, \
            f"Pilot crossed $100M ARR within 6 weeks, got {weeks}"

    def test_initial_advertiser_count(self):
        count = self.ad_biz.get('advertisers_at_launch', 0)
        assert count >= 600, \
            f"600+ advertisers at launch, got {count}"

    def test_2026_ad_revenue_projection(self):
        rev = self.ad_biz.get('projected_ad_revenue_2026_b', 0)
        assert rev >= 2.0, \
            f"Projected 2026 ad revenue >= $2B, got ${rev}B"

    def test_2030_ad_revenue_projection(self):
        rev = self.ad_biz.get('projected_ad_revenue_2030_b', 0)
        assert rev >= 100, \
            f"Projected 2030 ad revenue >= $100B, got ${rev}B"

    def test_ad_revenue_growth_trajectory(self):
        """Ad revenue projections should monotonically increase."""
        years = [
            self.ad_biz.get('projected_ad_revenue_2026_b', 0),
            self.ad_biz.get('projected_ad_revenue_2027_b', 0),
            self.ad_biz.get('projected_ad_revenue_2028_b', 0),
            self.ad_biz.get('projected_ad_revenue_2029_b', 0),
            self.ad_biz.get('projected_ad_revenue_2030_b', 0),
        ]
        for i in range(1, len(years)):
            assert years[i] > years[i-1], \
                f"Ad revenue should increase: {years[i-1]} -> {years[i]}"

    def test_strategy_chief_is_lehane(self):
        chief = self.ad_biz.get('strategy_chief', '')
        assert 'Lehane' in chief, \
            "Chris Lehane runs both advertising and global affairs"

    def test_ad_format_is_intent_based(self):
        fmt = self.ad_biz.get('ad_format', '')
        assert 'intent' in fmt.lower() or 'Intent' in fmt, \
            "Ad format should be described as intent-based conversational"

    def test_source_urls_present(self):
        urls = self.ad_biz.get('source_urls', [])
        assert len(urls) >= 1, \
            "Advertising business must have source URLs"
        assert any('reuters.com' in u for u in urls), \
            "Should include Reuters source for ad revenue projections"


class TestOpenAIAdRevenueVsPublisherDeals:
    """Core finding: ad revenue already exceeds publisher deal spending."""

    def setup_method(self):
        data = load_entities()
        self.openai = data['entities']['openai']
        self.ad_biz = self.openai.get('advertising_business', {})
        self.deals = self.openai.get('publisher_content_deal_portfolio', {})

    def test_deal_portfolio_section_exists(self):
        assert 'publisher_content_deal_portfolio' in self.openai, \
            "OpenAI must have publisher_content_deal_portfolio section"

    def test_total_deals_count(self):
        total = self.deals.get('total_deals', '')
        assert '20' in str(total), \
            f"OpenAI has 20+ publisher deals, got {total}"

    def test_total_outlets_count(self):
        outlets = self.deals.get('total_outlets', '')
        assert '160' in str(outlets), \
            f"OpenAI deals cover 160+ outlets, got {outlets}"

    def test_largest_deal_is_news_corp(self):
        largest = self.deals.get('largest_deal', '')
        assert 'News Corp' in largest, \
            "Largest deal should be News Corp"
        assert '250' in largest or '50M' in largest, \
            "News Corp deal should reference $250M/5yr or $50M/yr"

    def test_estimated_annual_value(self):
        val = str(self.deals.get('estimated_total_annual_value_m', ''))
        assert '300' in val or '400' in val, \
            f"Estimated annual value ~$300-400M, got {val}"

    def test_ad_revenue_exceeds_deal_spending_2026(self):
        """OpenAI's 2026 ad revenue ($2.5B) exceeds total deal spending ($300-400M)."""
        ad_rev_b = self.ad_biz.get('projected_ad_revenue_2026_b', 0)
        # Conservative upper bound of deal spending
        max_deal_spending_b = 0.4  # $400M
        assert ad_rev_b > max_deal_spending_b, \
            f"2026 ad revenue (${ad_rev_b}B) should exceed deal spending ($0.4B)"

    def test_ad_revenue_ratio_documented(self):
        """The deal-vs-ad ratio should be explicitly documented."""
        ratio = self.deals.get('deal_vs_ad_revenue_ratio', '')
        assert 'less than' in ratio.lower() or '<' in ratio or 'rounding error' in ratio.lower() \
            or 'loss leader' in ratio.lower(), \
            "Should document that deals are becoming a loss leader relative to ad revenue"

    def test_2030_deal_insignificance(self):
        """By 2030, deals would be <0.4% of ad revenue."""
        ad_rev_2030_b = self.ad_biz.get('projected_ad_revenue_2030_b', 0)
        max_deal_b = 0.4
        ratio = max_deal_b / ad_rev_2030_b if ad_rev_2030_b > 0 else 1
        assert ratio < 0.01, \
            f"By 2030, deals should be <1% of ad revenue, got {ratio:.2%}"

    def test_notable_partners_list(self):
        partners = self.deals.get('notable_partners', [])
        assert len(partners) >= 10, \
            f"Should list at least 10 notable partners, got {len(partners)}"
        partner_text = ' '.join(str(p) for p in partners)
        for required in ['News Corp', 'Condé Nast', 'Financial Times',
                         'Guardian', 'Washington Post']:
            assert required in partner_text, \
                f"{required} should be in notable partners list"


class TestTBPNMediaAcquisition:
    """Validate TBPN acquisition data and MediaScope implications."""

    def setup_method(self):
        data = load_entities()
        self.openai = data['entities']['openai']
        self.tbpn = self.openai.get('tbpn_media_acquisition', {})

    def test_tbpn_section_exists(self):
        assert 'tbpn_media_acquisition' in self.openai, \
            "OpenAI entity must have tbpn_media_acquisition section"

    def test_acquisition_date(self):
        assert self.tbpn.get('acquisition_date') == '2026-04-02', \
            "TBPN acquired April 2, 2026"

    def test_team_size(self):
        assert self.tbpn.get('team_size') == 11, \
            "TBPN was an 11-person team"

    def test_daily_viewers(self):
        viewers = self.tbpn.get('daily_viewers', 0)
        assert viewers >= 70000, \
            f"TBPN averaged ~70K daily viewers, got {viewers}"

    def test_pre_acquisition_revenue(self):
        rev = self.tbpn.get('pre_acquisition_revenue_m', 0)
        assert rev >= 30, \
            f"TBPN was generating ~$30M/yr before acquisition, got ${rev}M"

    def test_reports_to_lehane(self):
        reports = self.tbpn.get('reports_to', '')
        assert 'Lehane' in reports, \
            "TBPN reports to Chris Lehane (same person running ad business)"

    def test_editorial_independence_claim(self):
        assert self.tbpn.get('editorial_independence_claim') is True, \
            "TBPN claims editorial independence"

    def test_cofounders_documented(self):
        cofounders = self.tbpn.get('cofounders', [])
        assert len(cofounders) >= 2, \
            "Should document both TBPN co-founders"

    def test_source_urls_present(self):
        urls = self.tbpn.get('source_urls', [])
        assert len(urls) >= 3, \
            f"TBPN should have at least 3 source URLs, got {len(urls)}"
        assert any('wsj.com' in u for u in urls), \
            "Should include WSJ source (primary reporting)"

    def test_narrative_control_mechanism(self):
        """TBPN overview should document narrative control implications."""
        overview = self.tbpn.get('overview', '')
        assert 'narrative' in overview.lower() or 'bypass' in overview.lower() \
            or 'displacement' in overview.lower(), \
            "Should document TBPN as narrative control / publisher bypass mechanism"

    def test_lehane_dual_role_documented(self):
        """Chris Lehane runs BOTH OpenAI's ad business AND TBPN — same person."""
        overview = self.tbpn.get('overview', '')
        ad_chief = self.openai.get('advertising_business', {}).get('strategy_chief', '')
        tbpn_reports = self.tbpn.get('reports_to', '')
        assert 'Lehane' in ad_chief and 'Lehane' in tbpn_reports, \
            "Lehane's dual role (ads + TBPN) should be documented in both sections"


class TestOpenAIIPOFiling:
    """Validate OpenAI IPO filing data."""

    def setup_method(self):
        data = load_entities()
        self.openai = data['entities']['openai']
        self.ipo = self.openai.get('ipo_filing', {})

    def test_ipo_section_exists(self):
        assert 'ipo_filing' in self.openai, \
            "OpenAI entity must have ipo_filing section"

    def test_s1_filing_date(self):
        assert self.ipo.get('confidential_s1_date') == '2026-06-08', \
            "OpenAI filed confidential S-1 on June 8, 2026"

    def test_valuation(self):
        val = self.ipo.get('valuation_at_filing_b', 0)
        assert val >= 852, \
            f"OpenAI valuation at filing >= $852B, got ${val}B"

    def test_funding_round(self):
        funding = self.ipo.get('funding_round_mar_2026_b', 0)
        assert funding >= 122, \
            f"March 2026 funding round >= $122B, got ${funding}B"

    def test_transparency_inflection_documented(self):
        """IPO section should document the transparency inflection point."""
        inflection = self.ipo.get('transparency_inflection', '')
        assert 'publisher' in inflection.lower() and 'disclose' in inflection.lower(), \
            "Should document that IPO will force publisher deal value disclosure"

    def test_source_urls(self):
        urls = self.ipo.get('source_urls', [])
        assert len(urls) >= 2, \
            "IPO section needs source URLs"


class TestAnthropicIPOFiling:
    """Validate Anthropic IPO filing data and zero-deal paradox."""

    def setup_method(self):
        data = load_entities()
        self.anthropic = data['entities']['anthropic']
        self.ipo = self.anthropic.get('ipo_filing', {})

    def test_ipo_section_exists(self):
        assert 'ipo_filing' in self.anthropic, \
            "Anthropic entity must have ipo_filing section"

    def test_s1_filing_date(self):
        assert self.ipo.get('confidential_s1_date') == '2026-06-01', \
            "Anthropic filed S-1 on June 1, 2026 — before OpenAI"

    def test_valuation(self):
        val = self.ipo.get('valuation_at_filing_b', 0)
        assert val >= 965, \
            f"Anthropic valuation >= $965B, got ${val}B"

    def test_series_h_amount(self):
        raised = self.ipo.get('series_h_raised_b', 0)
        assert raised >= 65, \
            f"Series H raised >= $65B, got ${raised}B"

    def test_revenue_run_rate_at_filing(self):
        arr = self.ipo.get('revenue_run_rate_at_filing_b', 0)
        assert arr >= 47, \
            f"Revenue run rate at filing >= $47B, got ${arr}B"

    def test_revenue_trajectory_documented(self):
        traj = self.ipo.get('revenue_trajectory_note', '')
        assert '$1B' in traj and '$47B' in traj, \
            "Should document $1B → $47B trajectory"

    def test_zero_publisher_deal_paradox(self):
        paradox = self.ipo.get('zero_publisher_deal_ipo_paradox', '')
        assert 'zero' in paradox.lower() and 'publisher' in paradox.lower(), \
            "Should document zero-publisher-deal IPO paradox"

    def test_anthropic_valuation_exceeds_openai(self):
        """Anthropic ($965B) is valued HIGHER than OpenAI ($852B) with ZERO publisher deals."""
        openai_data = load_entities()['entities']['openai']
        openai_val = openai_data.get('ipo_filing', {}).get('valuation_at_filing_b', 0)
        anthropic_val = self.ipo.get('valuation_at_filing_b', 0)
        assert anthropic_val > openai_val, \
            f"Anthropic (${anthropic_val}B) should be valued higher than OpenAI (${openai_val}B)"

    def test_zero_deal_model_implications(self):
        """The paradox should discuss implications for publisher leverage."""
        paradox = self.ipo.get('zero_publisher_deal_ipo_paradox', '')
        assert 'leverage' in paradox.lower() or 'validates' in paradox.lower() \
            or 'capital-efficient' in paradox.lower(), \
            "Should discuss implications: validates zero-deal model, undermines publisher leverage"

    def test_target_listing_date(self):
        target = self.ipo.get('target_listing', '')
        assert 'october' in target.lower() or '2026' in target.lower(), \
            "Should document target listing as early as October 2026"

    def test_source_urls(self):
        urls = self.ipo.get('source_urls', [])
        assert len(urls) >= 3, \
            f"Anthropic IPO section needs >= 3 source URLs, got {len(urls)}"


class TestDualIPOTransparencyInflection:
    """Validate the dual IPO transparency event analysis."""

    def setup_method(self):
        data = load_entities()
        self.openai = data['entities']['openai']
        self.anthropic = data['entities']['anthropic']

    def test_both_have_ipo_sections(self):
        assert 'ipo_filing' in self.openai, "OpenAI must have IPO section"
        assert 'ipo_filing' in self.anthropic, "Anthropic must have IPO section"

    def test_anthropic_filed_first(self):
        """Anthropic filed June 1, OpenAI June 8 — Anthropic first."""
        a_date = self.anthropic['ipo_filing']['confidential_s1_date']
        o_date = self.openai['ipo_filing']['confidential_s1_date']
        assert a_date < o_date, \
            f"Anthropic ({a_date}) should have filed before OpenAI ({o_date})"

    def test_combined_valuation_exceeds_1_8_trillion(self):
        """Combined valuation of both companies exceeds $1.8T."""
        a_val = self.anthropic['ipo_filing']['valuation_at_filing_b']
        o_val = self.openai['ipo_filing']['valuation_at_filing_b']
        combined = a_val + o_val
        assert combined >= 1800, \
            f"Combined valuation should exceed $1.8T, got ${combined}B"

    def test_zero_deal_vs_max_deal_valuation_paradox(self):
        """Company with ZERO deals (Anthropic) is valued HIGHER than one with 20+ deals."""
        a_val = self.anthropic['ipo_filing']['valuation_at_filing_b']
        o_val = self.openai['ipo_filing']['valuation_at_filing_b']
        # Confirm Anthropic has zero publisher deals
        a_note = self.anthropic.get('publisher_deals_note', '')
        assert 'ZERO' in a_note, "Anthropic should be documented as having ZERO publisher deals"
        assert a_val > o_val, \
            "Zero-deal company valued higher than max-deal company"

    def test_openai_transparency_inflection_addresses_publisher_deals(self):
        inflection = self.openai['ipo_filing'].get('transparency_inflection', '')
        assert 'publisher' in inflection.lower(), \
            "Transparency inflection should address publisher deal disclosure"
        assert 'undisclosed' in inflection.lower() or 'verifiable' in inflection.lower(), \
            "Should note that most deal values are currently undisclosed"


class TestOpenAIRevenueTrajectory:
    """Validate OpenAI revenue data."""

    def setup_method(self):
        data = load_entities()
        self.openai = data['entities']['openai']
        self.rev = self.openai.get('revenue_trajectory', {})

    def test_revenue_section_exists(self):
        assert 'revenue_trajectory' in self.openai, \
            "OpenAI must have revenue_trajectory section"

    def test_arr_growth(self):
        """ARR should show growth from $10B to $25B+."""
        jun_2025 = self.rev.get('arr_jun_2025_b', 0)
        feb_2026 = self.rev.get('arr_feb_2026_b', 0)
        assert jun_2025 >= 10, f"Jun 2025 ARR >= $10B, got ${jun_2025}B"
        assert feb_2026 >= 25, f"Feb 2026 ARR >= $25B, got ${feb_2026}B"

    def test_chatgpt_weekly_users(self):
        users = self.rev.get('chatgpt_weekly_active_users_m', 0)
        assert users >= 900, \
            f"ChatGPT WAU >= 900M, got {users}M"

    def test_cash_burn_documented(self):
        burn = self.rev.get('projected_cash_burn_2026_b', 0)
        assert burn >= 20, \
            f"2026 cash burn should be documented >= $20B, got ${burn}B"


class TestGoogleAdComparisonContext:
    """Validate the Google ad comparison that underpins the displacement thesis."""

    def setup_method(self):
        data = load_entities()
        self.openai = data['entities']['openai']
        self.google = data['entities']['google']
        self.ad_biz = self.openai.get('advertising_business', {})

    def test_openai_ad_overview_references_google(self):
        """OpenAI ad business overview should reference Google comparison."""
        overview = self.ad_biz.get('overview', '')
        assert 'google' in overview.lower() or 'Google' in overview, \
            "Ad business overview should compare to Google's ad dependency mechanism"

    def test_google_has_q2_ad_data(self):
        """Google's advertising data should be current for comparison."""
        q2 = self.google.get('q2_2026_earnings', {})
        google_ads = q2.get('total_google_advertising_b', 0)
        assert google_ads >= 80, \
            f"Google Q2 2026 advertising >= $80B, got ${google_ads}B"

    def test_openai_2030_approaches_google_scale(self):
        """OpenAI's $100B/yr 2030 projection approaches Google's current ad revenue."""
        openai_2030 = self.ad_biz.get('projected_ad_revenue_2030_b', 0)
        # Google's Q2 2026 ads annualized ~ $326B
        # OpenAI's $100B would be ~31% of Google's current scale
        assert openai_2030 >= 100, \
            f"OpenAI 2030 ad projection should be $100B+, got ${openai_2030}B"

    def test_ad_dependency_prediction(self):
        """If financial incentive → coverage tone holds, OpenAI will become 'untouchable'."""
        overview = self.ad_biz.get('overview', '')
        assert 'shield' in overview.lower() or 'untouchable' in overview.lower() \
            or 'too big to criticize' in overview.lower() \
            or 'same' in overview.lower(), \
            "Overview should predict OpenAI gaining Google-like coverage protection"


class TestCrossValidation:
    """Cross-validation with existing MediaScope findings."""

    def setup_method(self):
        data = load_entities()
        self.entities = data['entities']

    def test_leverage_count_comparison_still_valid(self):
        """Meta should still have fewest leverage mechanisms."""
        meta = self.entities.get('meta', {})
        inverse = meta.get('inverse_financial_leverage', {})
        comparison = inverse.get('comparison_table', {})
        if comparison:
            assert comparison.get('meta', 99) <= comparison.get('microsoft', 0), \
                "Meta should have fewer mechanisms than Microsoft"
            assert comparison.get('meta', 99) <= comparison.get('amazon', 0), \
                "Meta should have fewer mechanisms than Amazon"

    def test_openai_now_has_additional_mechanisms(self):
        """OpenAI now has advertising + media ownership + content licensing."""
        openai = self.entities['openai']
        assert 'advertising_business' in openai, "OpenAI has advertising mechanism"
        assert 'tbpn_media_acquisition' in openai, "OpenAI has media ownership mechanism"
        assert 'publisher_content_deal_portfolio' in openai, "OpenAI has content licensing"

    def test_anthropic_still_zero_publisher_deals(self):
        """Anthropic should still have zero publisher deals."""
        anthropic = self.entities['anthropic']
        note = anthropic.get('publisher_deals_note', '')
        assert 'ZERO' in note, \
            "Anthropic should still have ZERO publisher deals"

    def test_openai_valuation_updated(self):
        """OpenAI valuation should reflect $852B, not the old $300B."""
        openai = self.entities['openai']
        cap = openai.get('market_cap_approx', '')
        assert '852' in cap or '300' not in cap.split('(')[0], \
            f"OpenAI market cap should be updated to $852B, got: {cap}"

    def test_anthropic_valuation_updated(self):
        """Anthropic valuation should reflect $965B, not the old $183B."""
        anthropic = self.entities['anthropic']
        cap = anthropic.get('market_cap_approx', '')
        assert '965' in cap, \
            f"Anthropic market cap should be updated to $965B, got: {cap}"
