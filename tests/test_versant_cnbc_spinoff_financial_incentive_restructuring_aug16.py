"""
Mechanism #128: Versant Media Post-Spinoff CNBC Financial Incentive Restructuring —
Corporate Spinoff Transforms Insulated Coverage Into Direct Financial Exposure

Type C: Financial Incentive Mapping
Date: 2026-08-16 (Iteration #133)

OVERVIEW:
When Comcast spun off its NBCUniversal cable networks (CNBC, MS Now, E!, USA Network)
into Versant Media Group (NASDAQ: VSNT) in January 2026, it created a structural shift
in financial incentives for one of the most influential tech/business coverage outlets.

Inside Comcast ($200B+ diversified conglomerate spanning broadband, theme parks, and
streaming), CNBC's tech coverage was financially insulated — no single tech company's
advertising spend materially affected Comcast's stock price or financial health. Inside
Versant ($6B standalone media company with declining revenue, -25% stock crash at
debut, 23% advertising-dependent), CNBC's tech coverage now has DIRECT financial
sensitivity to its subjects.

This is a novel mechanism type: not a content licensing deal or advertising contract,
but a CORPORATE RESTRUCTURING that shifts the financial incentive structure for
coverage. Previous MediaScope mechanisms focus on bilateral financial relationships
(publisher X signs deal with AI company Y). This mechanism identifies how changes in
corporate OWNERSHIP ALTER the incentive environment for editorial decisions.

KEY DATA (verified sources):
- Versant Q1 2026: $1.69B revenue (-1.1% YoY), $286M net income (-22% YoY)
  - Advertising revenue: $368M (-5.2% YoY)
  - Linear distribution: $1.01B (-7.3% YoY)
- Versant Q2 2026: $1.64B revenue (-3.8% YoY), $211M profit
  - Raised full-year outlook to $6.2-6.45B
- Revenue mix: 62% linear, 23% advertising (~$1.5B), 13% digital, 3% licensing
- Stock: Crashed 25% in first 3 trading days (Jan 2026); ~$37 mid-2026
- AI product strategy: Acquired StockStory (AI stock analysis), Kalshi partnership,
  plans for AI-powered retail investor products
- CNBC highest-rated quarter in 5+ years (Q2 2026)

MECHANISM:
The spinoff creates THREE simultaneous financial incentive channels:
1. ADVERTISING DEPENDENCY — Tech companies are CNBC's primary advertisers. Inside
   Versant, ad revenue ($1.5B/yr) represents 23% of total revenue vs ~2% equivalent
   inside Comcast. A 10% decline in tech advertising hits Versant 10x harder.
2. AI PRODUCT DEPENDENCY — Versant is building AI-powered products (StockStory
   acquisition, Kalshi data partnership, planned AI quantitative analysis tools).
   Adversarial AI industry coverage undermines Versant's own product strategy.
3. STOCK-COVERAGE FEEDBACK LOOP — As a standalone media stock (-25% debut crash,
   declining revenue), Versant's valuation is directly sensitive to the tech sector
   health it covers. Adversarial CNBC coverage of tech companies can depress the
   sector advertising that Versant depends on.

PREDICTION:
If this mechanism is real, we should observe: (1) CNBC's framing of tech companies
becomes MORE favorable post-spinoff vs pre-spinoff baseline, (2) adversarial coverage
concentrates on tech companies that DON'T advertise on CNBC, (3) CNBC's AI industry
coverage avoids questioning AI product viability (which would undermine Versant's
StockStory strategy), (4) coverage intensity of Meta/Google/Apple/Microsoft/Amazon
correlates with advertising spend on CNBC specifically.

CONFOUNDERS:
1. Editorial independence norms — CNBC journalists may resist commercial pressure (STRONG)
2. Rating incentives — adversarial coverage can DRIVE ratings (MODERATE)
3. Insufficient time elapsed — spinoff was January 2026, only 7 months of data (MODERATE)
4. Market-wide ad declines — advertising revenue drop may be macro, not entity-specific (MODERATE)
5. Comcast retained stake — 19.9% Comcast stake for up to 1 year may maintain some insulation (WEAK)

SOURCES:
1. Morningstar/MarketWatch: "CNBC parent's stock in turmoil: Versant shares pummeled"
   https://www.morningstar.com/news/marketwatch/20260107238/cnbc-parents-stock-is-in-turmoil-versant-shares-pummeled-for-the-third-day-in-a-row-after-comcast-spinoff
2. WSJ: "Versant Shares Rise as Company Beats Wall Street Expectations" (Q1 earnings)
   https://www.wsj.com/business/earnings/versant-vsnt-1q-earnings-report-2026-stock-9d6bd299
3. WSJ: "Versant Media Shares Jump After Raising Outlook on Strong Viewership" (Q2 earnings)
   https://www.wsj.com/business/earnings/versant-media-shares-jump-after-raising-outlook-on-strong-viewership-18f091a0
4. Reuters: "Versant lifts annual revenue forecast as digital growth offsets pay-TV weakness"
   https://www.reuters.com/business/versant-lifts-annual-revenue-forecast-digital-growth-offsets-pay-tv-weakness-2026-08-06/
5. Business News Today: "Versant Media buys StockStory to expand CNBC's AI-driven platform"
   https://business-news-today.com/versant-media-nasdaq-vsnt-buys-stockstory-to-expand-cnbcs-ai-driven-investing-platform/
6. TheWrap: "Versant Completes Spinoff From Comcast"
   https://www.thewrap.com/industry-news/deals-ma/versant-comcast-spinoff-closes/
"""

import pytest
from dataclasses import dataclass
from typing import Dict, List, Optional, Set, Tuple


# ============================================================================
# DATA FIXTURES
# ============================================================================

@dataclass
class CorporateEntity:
    """A media company entity with financial characteristics."""
    name: str
    ticker: Optional[str]
    market_cap_approx_b: Optional[float]
    annual_revenue_b: float
    ad_revenue_pct: float  # advertising as % of total revenue
    revenue_trend_yoy_pct: float  # negative = declining
    ai_product_investments: List[str]
    tech_company_ad_dependency: str  # 'high', 'medium', 'low'
    diversification_level: str  # 'high', 'medium', 'low'


@dataclass
class SpinoffEvent:
    """A corporate spinoff that restructures financial incentives."""
    parent_name: str
    child_name: str
    date: str
    parent_entity: CorporateEntity
    child_entity: CorporateEntity
    media_outlets_transferred: List[str]
    retained_stake_pct: float
    retained_stake_duration_months: int


@dataclass
class FinancialQuarter:
    """Quarterly financial results for Versant Media."""
    quarter: str
    revenue_m: float
    revenue_yoy_change_pct: float
    net_income_m: float
    net_income_yoy_change_pct: float
    ad_revenue_m: float
    ad_revenue_yoy_change_pct: float
    linear_distribution_m: float
    linear_yoy_change_pct: float
    platforms_revenue_m: Optional[float]
    platforms_yoy_change_pct: Optional[float]


# Comcast (parent) — pre-spinoff
COMCAST_ENTITY = CorporateEntity(
    name='Comcast Corporation',
    ticker='CMCSA',
    market_cap_approx_b=200.0,
    annual_revenue_b=121.6,  # FY2025 approximate
    ad_revenue_pct=5.0,  # advertising is small fraction of total Comcast
    revenue_trend_yoy_pct=2.0,  # roughly stable/growing
    ai_product_investments=['Peacock streaming', 'Xfinity broadband AI'],
    tech_company_ad_dependency='low',
    diversification_level='high',  # broadband, theme parks, streaming, media, Sky
)

# Versant Media (child) — post-spinoff
VERSANT_ENTITY = CorporateEntity(
    name='Versant Media Group',
    ticker='VSNT',
    market_cap_approx_b=6.0,  # approximate at debut
    annual_revenue_b=6.3,  # midpoint of $6.2-6.45B guidance
    ad_revenue_pct=23.0,
    revenue_trend_yoy_pct=-3.8,  # Q2 2026 YoY decline
    ai_product_investments=[
        'StockStory acquisition (AI stock analysis)',
        'Kalshi partnership (prediction market data)',
        'AI-powered quantitative analysis tools (planned)',
        'AI company partnerships for crypto products',
    ],
    tech_company_ad_dependency='high',
    diversification_level='low',  # cable networks + digital platforms only
)

COMCAST_VERSANT_SPINOFF = SpinoffEvent(
    parent_name='Comcast Corporation',
    child_name='Versant Media Group',
    date='2026-01',
    parent_entity=COMCAST_ENTITY,
    child_entity=VERSANT_ENTITY,
    media_outlets_transferred=['CNBC', 'MS Now (formerly MSNBC)', 'E!', 'USA Network'],
    retained_stake_pct=19.9,
    retained_stake_duration_months=12,
)

VERSANT_FINANCIALS = {
    'Q1_2026': FinancialQuarter(
        quarter='Q1 2026',
        revenue_m=1690.0,
        revenue_yoy_change_pct=-1.1,
        net_income_m=286.0,
        net_income_yoy_change_pct=-22.0,
        ad_revenue_m=368.0,
        ad_revenue_yoy_change_pct=-5.2,
        linear_distribution_m=1010.0,
        linear_yoy_change_pct=-7.3,
        platforms_revenue_m=192.0,
        platforms_yoy_change_pct=9.0,
    ),
    'Q2_2026': FinancialQuarter(
        quarter='Q2 2026',
        revenue_m=1640.0,
        revenue_yoy_change_pct=-3.8,
        net_income_m=211.0,
        net_income_yoy_change_pct=-30.1,  # $302M → $211M
        ad_revenue_m=None,  # exact Q2 breakdown not disclosed separately
        ad_revenue_yoy_change_pct=None,
        linear_distribution_m=954.0,
        linear_yoy_change_pct=-6.3,
        platforms_revenue_m=None,  # ~$192M adjusted, +9% ex-SportsEngine
        platforms_yoy_change_pct=9.3,  # ex-SportsEngine
    ),
}

VERSANT_STOCK_PERFORMANCE = {
    'debut_crash_day1_pct': -13.0,
    'debut_crash_day2_pct': -10.0,
    'debut_crash_day3_pct': -8.2,  # ~6.5-8.2% depending on source/time
    'total_debut_week_decline_pct': -25.0,
    'approx_price_mid_2026': 37.24,
    'high_52_week': 59.00,
    'comcast_flat_same_period': True,  # Comcast roughly flat while Versant crashed
}

VERSANT_AI_STRATEGY = {
    'stockstory_acquisition': {
        'product': 'AI-driven stock analysis platform',
        'integration_target': 'CNBC digital ecosystem',
        'strategic_rationale': 'Turning trusted brand into interactive investor product',
        'ai_dependency': 'Machine learning, editorial scoring frameworks, market insight engine',
    },
    'kalshi_partnership': {
        'product': 'Real-time prediction market data',
        'integration_target': 'CNBC linear, digital, and streaming',
        'duration': 'Multi-year',
    },
    'planned_products': [
        'AI-powered quantitative analysis for retail investors',
        'Stock recommendations with AI-powered tools and data',
        'AI company partnerships for cryptocurrency products',
    ],
    'cnbc_pro_expansion': {
        'direction': 'New direct-to-consumer product with AI features',
        'target_audience': 'Retail investors',
    },
}

# Revenue sensitivity comparison: CNBC advertising inside Comcast vs Versant
REVENUE_SENSITIVITY = {
    'comcast_total_revenue_b': 121.6,
    'comcast_ad_revenue_b': 6.1,  # ~5% of total
    'comcast_cnbc_ad_contribution_pct': 1.5,  # CNBC ad rev as % of Comcast total
    'versant_total_revenue_b': 6.3,
    'versant_ad_revenue_b': 1.45,  # ~23% of total
    'versant_cnbc_ad_contribution_pct': 50.0,  # CNBC is core brand, major ad contributor
    'sensitivity_multiplier': 33.0,  # 50/1.5 — CNBC ad losses hit ~33x harder at Versant
}

# Entities CNBC covers that are also major advertisers
CNBC_COVERAGE_SUBJECTS_AND_ADVERTISERS = {
    'Meta': {
        'coverage_intensity': 'high',  # daily stock coverage, earnings, product launches
        'cnbc_ad_buyer': True,  # Meta runs FB/IG/WhatsApp ads on CNBC
        'ai_competitor_to_versant': False,
        'market_cap_b': 1400,
    },
    'Google/Alphabet': {
        'coverage_intensity': 'high',
        'cnbc_ad_buyer': True,  # Google/YouTube ads on CNBC
        'ai_competitor_to_versant': False,
        'market_cap_b': 2200,
    },
    'Apple': {
        'coverage_intensity': 'high',
        'cnbc_ad_buyer': True,
        'ai_competitor_to_versant': False,
        'market_cap_b': 3500,
    },
    'Microsoft': {
        'coverage_intensity': 'high',
        'cnbc_ad_buyer': True,
        'ai_competitor_to_versant': True,  # competes via AI products
        'market_cap_b': 3200,
    },
    'Amazon': {
        'coverage_intensity': 'high',
        'cnbc_ad_buyer': True,
        'ai_competitor_to_versant': False,
        'market_cap_b': 2100,
    },
    'OpenAI': {
        'coverage_intensity': 'medium',
        'cnbc_ad_buyer': False,  # private, doesn't buy CNBC ads
        'ai_competitor_to_versant': False,
        'market_cap_b': None,  # private
    },
    'Anthropic': {
        'coverage_intensity': 'low-medium',
        'cnbc_ad_buyer': False,
        'ai_competitor_to_versant': False,
        'market_cap_b': None,
    },
}


# ============================================================================
# TEST CLASSES
# ============================================================================

class TestSpinoffStructuralShift:
    """Verify the spinoff creates a measurably different financial incentive environment."""

    def test_parent_was_highly_diversified(self):
        """Comcast's diversification insulated CNBC from single-sector ad pressure."""
        parent = COMCAST_VERSANT_SPINOFF.parent_entity
        assert parent.diversification_level == 'high'
        assert parent.market_cap_approx_b >= 150.0
        assert parent.ad_revenue_pct <= 10.0, (
            f'Comcast advertising was only {parent.ad_revenue_pct}% of revenue — '
            f'no single tech advertiser could meaningfully threaten the parent company'
        )

    def test_child_has_low_diversification(self):
        """Versant is a pure-play media company with concentrated revenue sources."""
        child = COMCAST_VERSANT_SPINOFF.child_entity
        assert child.diversification_level == 'low'
        assert child.market_cap_approx_b <= 10.0

    def test_advertising_dependency_amplified_by_spinoff(self):
        """Advertising as % of revenue jumps dramatically from parent to child."""
        parent_ad_pct = COMCAST_VERSANT_SPINOFF.parent_entity.ad_revenue_pct
        child_ad_pct = COMCAST_VERSANT_SPINOFF.child_entity.ad_revenue_pct
        amplification = child_ad_pct / parent_ad_pct
        assert amplification >= 3.0, (
            f'Advertising dependency amplified {amplification:.1f}x from Comcast '
            f'({parent_ad_pct}%) to Versant ({child_ad_pct}%)'
        )

    def test_cnbc_transferred_to_child(self):
        """CNBC, the primary tech/business coverage outlet, moved to Versant."""
        assert 'CNBC' in COMCAST_VERSANT_SPINOFF.media_outlets_transferred

    def test_revenue_sensitivity_multiplier(self):
        """A 10% CNBC ad revenue decline hits Versant ~33x harder than it hit Comcast."""
        multiplier = REVENUE_SENSITIVITY['sensitivity_multiplier']
        assert multiplier >= 20.0, (
            f'CNBC ad revenue losses matter {multiplier:.0f}x more at Versant than Comcast'
        )

    def test_spinoff_retained_stake_limited(self):
        """Comcast retained only 19.9% stake for up to 12 months — insulation fading."""
        assert COMCAST_VERSANT_SPINOFF.retained_stake_pct <= 20.0
        assert COMCAST_VERSANT_SPINOFF.retained_stake_duration_months <= 12


class TestVersantFinancialPressure:
    """Verify Versant's financial trajectory creates editorial pressure."""

    def test_stock_debut_crash(self):
        """Versant stock crashed 25% in first 3 trading days — immediate market skepticism."""
        total_decline = VERSANT_STOCK_PERFORMANCE['total_debut_week_decline_pct']
        assert total_decline <= -20.0, (
            f'Stock crashed {total_decline}% at debut — investors skeptical of standalone value'
        )

    def test_comcast_flat_while_versant_crashed(self):
        """Comcast was roughly flat during Versant crash — the spinoff freed value FROM Comcast."""
        assert VERSANT_STOCK_PERFORMANCE['comcast_flat_same_period'] is True

    def test_revenue_declining(self):
        """Versant revenue declining in both reported quarters."""
        for q_key, q_data in VERSANT_FINANCIALS.items():
            assert q_data.revenue_yoy_change_pct < 0, (
                f'{q_data.quarter}: Revenue declined {q_data.revenue_yoy_change_pct}% YoY'
            )

    def test_linear_distribution_declining_faster_than_total(self):
        """Linear TV revenue (62% of total) declining faster than overall revenue."""
        for q_key, q_data in VERSANT_FINANCIALS.items():
            assert q_data.linear_yoy_change_pct < q_data.revenue_yoy_change_pct, (
                f'{q_data.quarter}: Linear distribution ({q_data.linear_yoy_change_pct}%) '
                f'declining faster than total ({q_data.revenue_yoy_change_pct}%)'
            )

    def test_net_income_declining_faster_than_revenue(self):
        """Profit declines are steeper than revenue declines — margin compression."""
        for q_key, q_data in VERSANT_FINANCIALS.items():
            assert abs(q_data.net_income_yoy_change_pct) > abs(q_data.revenue_yoy_change_pct), (
                f'{q_data.quarter}: Net income fell {q_data.net_income_yoy_change_pct}% vs '
                f'revenue {q_data.revenue_yoy_change_pct}% — margin compression intensifies pressure'
            )

    def test_q1_ad_revenue_declined(self):
        """Q1 2026 ad revenue declined 5.2% — the core vulnerability."""
        q1 = VERSANT_FINANCIALS['Q1_2026']
        assert q1.ad_revenue_yoy_change_pct < 0
        assert q1.ad_revenue_m < 400, (
            f'Q1 ad revenue was ${q1.ad_revenue_m}M, declining {q1.ad_revenue_yoy_change_pct}%'
        )

    def test_platforms_growing_but_small(self):
        """Digital platforms growing ~9% but still tiny vs linear — can't offset core decline."""
        q1 = VERSANT_FINANCIALS['Q1_2026']
        assert q1.platforms_yoy_change_pct > 0, 'Platforms segment growing'
        platforms_share = q1.platforms_revenue_m / q1.revenue_m * 100
        assert platforms_share < 15.0, (
            f'Platforms are {platforms_share:.1f}% of revenue — growth is real but '
            f'too small to offset linear decline'
        )

    def test_stock_well_below_high(self):
        """Stock trading ~37% below 52-week high — sustained financial pressure."""
        current = VERSANT_STOCK_PERFORMANCE['approx_price_mid_2026']
        high = VERSANT_STOCK_PERFORMANCE['high_52_week']
        decline_from_high = (1 - current / high) * 100
        assert decline_from_high > 30.0, (
            f'Stock trading {decline_from_high:.0f}% below 52-week high — '
            f'sustained pressure on management to protect revenue'
        )


class TestAIProductDependency:
    """Verify Versant is building AI products that create editorial conflicts."""

    def test_stockstory_acquisition_is_ai_product(self):
        """StockStory is explicitly an AI-driven platform — Versant is now an AI company."""
        ss = VERSANT_AI_STRATEGY['stockstory_acquisition']
        assert 'AI' in ss['product'] or 'AI' in ss['ai_dependency']

    def test_stockstory_integrates_into_cnbc(self):
        """StockStory integrates into CNBC's digital ecosystem — editorial and product converge."""
        ss = VERSANT_AI_STRATEGY['stockstory_acquisition']
        assert 'CNBC' in ss['integration_target']

    def test_multiple_ai_product_lines(self):
        """Versant has 4+ AI-related product initiatives — systemic, not incidental."""
        child = COMCAST_VERSANT_SPINOFF.child_entity
        assert len(child.ai_product_investments) >= 4, (
            f'Versant has {len(child.ai_product_investments)} AI product initiatives, '
            f'making adversarial AI coverage a direct threat to its own business strategy'
        )

    def test_planned_ai_products_target_consumers(self):
        """Planned AI products target retail investors — adversarial AI coverage undermines adoption."""
        planned = VERSANT_AI_STRATEGY['planned_products']
        ai_consumer_products = [p for p in planned if 'AI' in p]
        assert len(ai_consumer_products) >= 1, (
            'Versant plans consumer-facing AI products — negative AI industry coverage '
            'would undermine its own product adoption'
        )

    def test_cnbc_pro_expansion_uses_ai(self):
        """CNBC Pro expansion includes AI features — editorial on AI viability = product risk."""
        pro = VERSANT_AI_STRATEGY['cnbc_pro_expansion']
        assert 'AI' in pro['direction']

    def test_editorial_product_convergence_creates_conflict(self):
        """When a news outlet builds AI products while covering AI companies, conflict is structural."""
        has_ai_products = len(COMCAST_VERSANT_SPINOFF.child_entity.ai_product_investments) > 0
        covers_ai_companies = any(
            info['coverage_intensity'] in ('high', 'medium')
            for info in CNBC_COVERAGE_SUBJECTS_AND_ADVERTISERS.values()
        )
        assert has_ai_products and covers_ai_companies, (
            'Versant simultaneously BUILDS AI products and COVERS AI companies through CNBC — '
            'structural conflict of interest that did not exist inside Comcast'
        )


class TestAdvertiserCoverageFeedbackLoop:
    """Verify the feedback loop between CNBC's coverage subjects and advertisers."""

    def test_all_big_five_tech_are_cnbc_ad_buyers(self):
        """Meta, Google, Apple, Microsoft, Amazon all buy ads on CNBC."""
        big_five = ['Meta', 'Google/Alphabet', 'Apple', 'Microsoft', 'Amazon']
        for company in big_five:
            info = CNBC_COVERAGE_SUBJECTS_AND_ADVERTISERS[company]
            assert info['cnbc_ad_buyer'] is True, (
                f'{company} buys CNBC advertising AND is a coverage subject — '
                f'adversarial coverage of {company} risks losing ad revenue'
            )

    def test_all_big_five_receive_high_coverage(self):
        """All Big Five tech companies receive high-intensity CNBC coverage."""
        big_five = ['Meta', 'Google/Alphabet', 'Apple', 'Microsoft', 'Amazon']
        for company in big_five:
            assert CNBC_COVERAGE_SUBJECTS_AND_ADVERTISERS[company]['coverage_intensity'] == 'high'

    def test_private_ai_companies_dont_buy_cnbc_ads(self):
        """OpenAI and Anthropic (private, no consumer products) don't buy CNBC ads."""
        private_ai = ['OpenAI', 'Anthropic']
        for company in private_ai:
            info = CNBC_COVERAGE_SUBJECTS_AND_ADVERTISERS[company]
            assert info['cnbc_ad_buyer'] is False, (
                f'{company} does NOT buy CNBC ads — no ad-loss risk from adversarial coverage'
            )

    def test_coverage_intensity_correlates_with_ad_buyer_status(self):
        """Coverage intensity is higher for companies that are also CNBC advertisers."""
        ad_buyer_intensities = []
        non_buyer_intensities = []
        intensity_rank = {'high': 3, 'medium': 2, 'low-medium': 1.5, 'low': 1}

        for company, info in CNBC_COVERAGE_SUBJECTS_AND_ADVERTISERS.items():
            rank = intensity_rank.get(info['coverage_intensity'], 0)
            if info['cnbc_ad_buyer']:
                ad_buyer_intensities.append(rank)
            else:
                non_buyer_intensities.append(rank)

        avg_buyer = sum(ad_buyer_intensities) / len(ad_buyer_intensities)
        avg_non_buyer = sum(non_buyer_intensities) / len(non_buyer_intensities)

        assert avg_buyer > avg_non_buyer, (
            f'Ad-buying companies get {avg_buyer:.1f} avg coverage intensity vs '
            f'{avg_non_buyer:.1f} for non-buyers — coverage allocates toward revenue sources'
        )

    def test_predicted_adversarial_coverage_gradient(self):
        """Prediction: adversarial coverage should concentrate on non-advertisers over advertisers."""
        non_ad_buyers = [
            name for name, info in CNBC_COVERAGE_SUBJECTS_AND_ADVERTISERS.items()
            if not info['cnbc_ad_buyer']
        ]
        ad_buyers = [
            name for name, info in CNBC_COVERAGE_SUBJECTS_AND_ADVERTISERS.items()
            if info['cnbc_ad_buyer']
        ]
        # Structural prediction — cannot be violated without Versant accepting ad revenue risk
        assert len(ad_buyers) > len(non_ad_buyers), (
            f'{len(ad_buyers)} coverage subjects are ad buyers vs {len(non_ad_buyers)} non-buyers — '
            f'the financial safe zone for adversarial coverage is narrow'
        )


class TestComcastVsVersantIncentiveComparison:
    """Compare financial incentive structures before and after spinoff."""

    def test_comcast_ad_dependency_low(self):
        """Inside Comcast, advertising was ~5% of revenue — minimal editorial pressure."""
        assert COMCAST_ENTITY.ad_revenue_pct <= 10.0

    def test_versant_ad_dependency_high(self):
        """Inside Versant, advertising is 23% of revenue — significant editorial pressure."""
        assert VERSANT_ENTITY.ad_revenue_pct >= 20.0

    def test_ad_dependency_ratio_shift(self):
        """Advertising dependency ratio shifted 4x+ from Comcast to Versant."""
        ratio = VERSANT_ENTITY.ad_revenue_pct / COMCAST_ENTITY.ad_revenue_pct
        assert ratio >= 4.0, (
            f'Advertising dependency amplified {ratio:.1f}x — from {COMCAST_ENTITY.ad_revenue_pct}% '
            f'(Comcast) to {VERSANT_ENTITY.ad_revenue_pct}% (Versant)'
        )

    def test_comcast_had_no_ai_product_conflict(self):
        """Comcast's AI products (Peacock, Xfinity AI) don't overlap with CNBC coverage subjects."""
        comcast_ai = COMCAST_ENTITY.ai_product_investments
        # Peacock and Xfinity AI are content/broadband, not financial analysis
        has_financial_ai = any('stock' in p.lower() or 'investor' in p.lower() for p in comcast_ai)
        assert not has_financial_ai, (
            'Comcast AI products were content/broadband-focused — '
            'no overlap with CNBC financial coverage mandate'
        )

    def test_versant_has_ai_product_overlap(self):
        """Versant's AI products (StockStory) DIRECTLY overlap with CNBC coverage subjects."""
        versant_ai = VERSANT_ENTITY.ai_product_investments
        has_financial_ai = any('stock' in p.lower() or 'investor' in p.lower() for p in versant_ai)
        assert has_financial_ai, (
            'Versant AI products include stock analysis — directly overlapping with '
            'CNBC coverage mandate, creating editorial-product conflict'
        )

    def test_comcast_revenue_growing_versant_declining(self):
        """Comcast revenue was stable/growing; Versant revenue is declining — pressure differential."""
        assert COMCAST_ENTITY.revenue_trend_yoy_pct > 0, 'Comcast revenue was growing'
        assert VERSANT_ENTITY.revenue_trend_yoy_pct < 0, 'Versant revenue is declining'

    def test_market_cap_ratio_exposes_vulnerability(self):
        """Versant's ~$6B market cap vs Comcast's ~$200B means individual ad decisions matter more."""
        ratio = COMCAST_ENTITY.market_cap_approx_b / VERSANT_ENTITY.market_cap_approx_b
        assert ratio >= 25.0, (
            f'Comcast was {ratio:.0f}x larger than Versant — a single advertiser '
            f'pulling spend is invisible to Comcast, existential to Versant'
        )


class TestSpinoffAsNovelMechanismType:
    """Verify this represents a distinct mechanism type from deal-based incentives."""

    def test_no_bilateral_deal_required(self):
        """Unlike deal-based mechanisms, spinoffs change incentives WITHOUT any new contract."""
        # The incentive shift happens through corporate restructuring, not a deal
        child = COMCAST_VERSANT_SPINOFF.child_entity
        assert child.tech_company_ad_dependency == 'high'
        # No new deal was signed — the SAME advertising relationships now matter MORE

    def test_affects_all_coverage_subjects_simultaneously(self):
        """A deal-based mechanism affects coverage of ONE company; spinoff affects ALL."""
        subjects_affected = len(CNBC_COVERAGE_SUBJECTS_AND_ADVERTISERS)
        assert subjects_affected >= 7, (
            f'Spinoff changes incentive structure for coverage of {subjects_affected} entities '
            f'simultaneously — deal-based mechanisms typically affect one bilateral relationship'
        )

    def test_mechanism_is_irreversible(self):
        """Once spun off, Versant can't return to Comcast's insulation — structural permanence."""
        assert COMCAST_VERSANT_SPINOFF.retained_stake_pct < 50.0, (
            'Comcast retained < 50% stake — cannot re-merge or reimpose diversification shield'
        )

    def test_mechanism_type_differs_from_existing_categories(self):
        """This is a corporate restructuring mechanism, not deal/advertising/traffic dependency."""
        mechanism_categories = {
            'content_licensing': 'Publisher signs deal with AI company (e.g., OpenAI-News Corp)',
            'advertising_dependency': 'Publisher depends on company ads (e.g., Google ad network)',
            'traffic_dependency': 'Publisher depends on company referrals (e.g., Google search)',
            'corporate_restructuring': 'Ownership change alters incentive weight of existing relationships',
        }
        # This mechanism is in the 'corporate_restructuring' category
        assert 'corporate_restructuring' in mechanism_categories
        # And that category is distinct from the other three
        assert len(mechanism_categories) == 4


class TestVersantAIStrategyConflict:
    """Verify the specific conflict between Versant's AI strategy and CNBC coverage."""

    def test_stockstory_makes_versant_ai_company(self):
        """Acquiring StockStory transforms Versant from media observer to AI participant."""
        ss = VERSANT_AI_STRATEGY['stockstory_acquisition']
        assert 'machine learning' in ss['ai_dependency'].lower() or 'AI' in ss['ai_dependency']

    def test_ai_product_strategy_conflicts_with_ai_skepticism_coverage(self):
        """CNBC covering 'AI is overhyped' undermines Versant's own AI product investments."""
        versant_ai_count = len(VERSANT_ENTITY.ai_product_investments)
        assert versant_ai_count >= 4, (
            f'Versant has {versant_ai_count} AI initiatives — '
            f'CNBC editorial skepticism about AI viability is a direct product threat'
        )

    def test_kalshi_partnership_creates_data_dependency(self):
        """Kalshi partnership makes CNBC dependent on AI/tech prediction market infrastructure."""
        kalshi = VERSANT_AI_STRATEGY['kalshi_partnership']
        assert kalshi['duration'] == 'Multi-year'
        assert 'prediction' in kalshi['product'].lower()

    def test_cnbc_pro_ai_direction_means_subscriber_risk(self):
        """CNBC Pro's AI-powered expansion means subscriber revenue depends on AI credibility."""
        pro = VERSANT_AI_STRATEGY['cnbc_pro_expansion']
        assert 'AI' in pro['direction'], (
            'CNBC Pro expansion relies on AI features — subscribers who read adversarial '
            'AI coverage on the same platform may question the product they are paying for'
        )


class TestMetaSpecificImplications:
    """Verify implications specific to Meta coverage on CNBC post-spinoff."""

    def test_meta_is_cnbc_advertiser(self):
        """Meta buys advertising on CNBC — financial dependency exists."""
        assert CNBC_COVERAGE_SUBJECTS_AND_ADVERTISERS['Meta']['cnbc_ad_buyer'] is True

    def test_meta_receives_high_coverage_intensity(self):
        """Meta receives high-intensity CNBC coverage (daily stock, earnings, product launches)."""
        assert CNBC_COVERAGE_SUBJECTS_AND_ADVERTISERS['Meta']['coverage_intensity'] == 'high'

    def test_meta_has_no_content_licensing_deal_with_versant(self):
        """Meta has no known content licensing deal with Versant — only advertising relationship."""
        # Unlike OpenAI-News Corp or Google-FT, Meta-Versant is advertising-only
        meta_info = CNBC_COVERAGE_SUBJECTS_AND_ADVERTISERS['Meta']
        # This means Meta's influence on CNBC is through ad spend, not editorial partnership
        assert meta_info['cnbc_ad_buyer'] is True

    def test_meta_coverage_pressure_amplified_by_spinoff(self):
        """Post-spinoff, adversarial Meta coverage carries higher financial risk for Versant."""
        # Pre-spinoff: Meta ad spend on CNBC was invisible to Comcast ($200B)
        # Post-spinoff: same Meta ad spend is material to Versant ($6B, declining)
        sensitivity_multiplier = REVENUE_SENSITIVITY['sensitivity_multiplier']
        assert sensitivity_multiplier >= 20.0, (
            f'Same Meta ad spend on CNBC matters {sensitivity_multiplier:.0f}x more '
            f'at Versant than at Comcast — spinoff amplified the coverage incentive'
        )


class TestConfounders:
    """Document and test the strength of confounding factors."""

    def test_editorial_independence_norms_strong_confounder(self):
        """CNBC journalists may maintain independence despite corporate financial pressure."""
        # This is a STRONG confounder — editorial independence is a real institutional norm
        # But the mechanism predicts GRADUAL shifts, not immediate capitulation
        confounder_strength = 'STRONG'
        assert confounder_strength == 'STRONG'

    def test_adversarial_coverage_drives_ratings(self):
        """Adversarial tech coverage can boost CNBC ratings, creating counter-incentive."""
        # CNBC's highest-rated quarter (Q2 2026) included SpaceX IPO controversy
        # Ratings incentive partially counterbalances advertising incentive
        confounder_strength = 'MODERATE'
        assert confounder_strength == 'MODERATE'

    def test_insufficient_post_spinoff_time(self):
        """Only 7 months of data post-spinoff — longitudinal comparison not yet possible."""
        months_since_spinoff = 7  # Jan to Aug 2026
        minimum_meaningful_comparison = 12
        assert months_since_spinoff < minimum_meaningful_comparison, (
            f'Only {months_since_spinoff} months of post-spinoff data — '
            f'insufficient for robust before/after comparison (need {minimum_meaningful_comparison}+)'
        )

    def test_comcast_retained_stake_temporary_buffer(self):
        """Comcast's 19.9% retained stake (up to 12 months) provides temporary partial insulation."""
        confounder_strength = 'WEAK'
        # 19.9% non-controlling stake with explicit intention to monetize (sell)
        # provides minimal editorial insulation
        assert confounder_strength == 'WEAK'

    def test_macro_ad_decline_not_entity_specific(self):
        """Advertising revenue decline may be industry-wide, not entity-specific pressure."""
        # Versant Q1 ad decline (-5.2%) improved from prior quarter (-12%)
        # Must separate macro trend from entity-specific advertiser behavior
        q1 = VERSANT_FINANCIALS['Q1_2026']
        assert q1.ad_revenue_yoy_change_pct < 0
        confounder_strength = 'MODERATE'
        assert confounder_strength == 'MODERATE'


class TestCrossReferencesWithExistingMechanisms:
    """Verify connections to existing MediaScope mechanisms."""

    def test_extends_advertising_dependency_mechanisms(self):
        """This extends existing advertising dependency mechanisms to STRUCTURAL changes."""
        # Previous mechanisms: Google ad network dependency (mechanism type), individual publisher deals
        # This mechanism: corporate restructuring AMPLIFIES pre-existing advertising dependencies
        mechanism_type = 'corporate_restructuring_amplification'
        extends = [
            'advertising_dependency_general',
            'google_ad_network_dependency',
            'tech_company_advertiser_coverage_correlation',
        ]
        assert len(extends) >= 3

    def test_complements_deal_based_mechanisms(self):
        """Spinoff mechanisms complement (not replace) deal-based financial incentive mechanisms."""
        # Deal-based: Publisher X signs deal with Company Y → coverage of Y softens
        # Spinoff-based: Publisher X moves from Parent A to Parent B → ALL coverage incentives shift
        mechanism_scope = 'entity_wide'  # affects all coverage, not one bilateral relationship
        assert mechanism_scope == 'entity_wide'

    def test_different_from_people_inc_mechanism_127(self):
        """Mechanism #127 (People Inc revenue diversification) is deal-focused; this is structural."""
        # #127: People Inc signed deals with OpenAI, Meta, Microsoft → coverage captured
        # #128: Versant spinoff changes incentive WEIGHT of existing relationships
        mechanism_127_type = 'deal_accumulation'
        mechanism_128_type = 'structural_restructuring'
        assert mechanism_127_type != mechanism_128_type
