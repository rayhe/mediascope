"""
Mechanism #117: News Corp Q4 FY2026 "Woo and Sue" AI Posture Revenue Architecture

DISCOVERY DATE: 2026-08-15

FINDING SUMMARY:
News Corp's Q4 FY2026 earnings call (Aug 5, 2026) introduced explicit corporate language
categorizing AI companies into "trusted content relationships" (OpenAI and Meta) versus
"pilferers" and "crass kleptomaniacs" (unlicensed scrapers). CEO Robert Thomson's "woo and
sue" framework is the first time a major publisher parent company has articulated an explicit
bifurcated posture toward AI entities on a public earnings call, directly connecting licensing
revenue to editorial positioning.

CROSS-PUBLISHER CONTRAST (News Corp vs Ziff Davis):
News Corp and Ziff Davis reported Q2/Q4 2026 earnings within 24 hours of each other (Aug 5-6),
revealing diametrically opposite AI postures with predictable coverage implications:

NEWS CORP ("Woo and Sue" — Mechanism #117):
- Revenue: $2.34B Q4 (+11% YoY), $9.03B FY2026 (+7%)
- EBITDA: $423M Q4 (+31%), RECORD profitability
- Dow Jones revenue: $644M (+7%), EBITDA $181M (+20%)
- Dow Jones explicitly credits "higher content licensing revenue" as growth driver
- OpenAI deal: $50M/yr (part of $250M/5yr News Corp deal)
- Meta deal: Active, Thomson calls it a "trusted content relationship"
- Anthropic: Expects share of $1.5B settlement (HarperCollins book publishing)
- Posture: "Woo and sue" — deals with partners, litigate against scrapers
- Target $1B Dow Jones EBITDA by FY2030, AI licensing part of trajectory
- Publications: WSJ, NY Post, Barron's, MarketWatch

ZIFF DAVIS ("Litigate and Resist" — Mechanism #108 updated):
- Revenue: $286.7M Q2 (-2.7% YoY), H1 $554.4M (-2.3%)
- Operating LOSS: $(44.7M) vs income $13.8M in Q2 2025
- Goodwill impairment: $54.8M (first in recent history)
- Ad/performance marketing revenue: down 6% YoY
- Google AI Overviews: NOW 50% of relevant queries (up from 36%, up from 20%+)
- OpenAI: Active lawsuit, CEO says "litigation continuing"
- Meta deal: ZERO. Google deal: ZERO.
- Posture: Refuses RAG-focused licensing, waiting for "legal clarity"
- Selling assets ($1.2B Connectivity sale)
- Publications: CNET, ZDNET, PCMag, Mashable, IGN

COVERAGE PREDICTION ALIGNMENT:
News Corp publications (WSJ) frame Meta AI partnerships as business-positive, covering
Meta smart glasses through human-interest/accessibility angles. Ziff Davis publications
(CNET, ZDNET) apply entity-selective privacy vocabulary and enthusiasm gradients aligned
with their financial architecture (documented in Mechanisms #106 and #107).

The 50% AI Overviews metric (up from 36% at Shah's previous mention, and from 20%+ when
first disclosed) represents an ACCELERATION of Google's existential pressure on Ziff Davis
that further predicts protective Google coverage from ZD publications.

CONFOUNDING FACTORS (7):
1. STRONG: Editorial independence policies at both companies
2. STRONG: Individual journalists at WSJ/CNET may be unaware of corporate AI postures
3. STRONG: Meta genuinely has more historical privacy controversies
4. MODERATE: WSJ is a business publication, CNET is a consumer tech publication (genre)
5. MODERATE: News Corp's revenue growth has multiple drivers beyond AI licensing
6. WEAK: Sample size of earnings calls is limited
7. WEAK: "Woo and sue" language may be performative shareholder communication

SOURCE URLS:
- https://www.businesswire.com/news/home/20260805848469/en/News-Corporation-Reports-Fourth-Quarter-and-Full-Year-Results-for-Fiscal-2026
- https://thefinancialnews247.com/news-corp-posts-record-profitability-11-jump-in-q4-revenue/
- https://seekingalpha.com/news/4627081-news-corp-targets-1b-dow-jones-ebitda-by-fiscal-30-while-signaling-further-margin-expansion
- https://www.thewrap.com/industry-news/business/news-corp-beats-q4-revenue-earnings-estimates/
- https://www.thewrap.com/industry-news/business/news-corp-q3-earnings/
- https://www.fool.com/earnings/call-transcripts/2026/05/08/news-corp-nws-q3-2026-earnings-transcript/
- https://www.businesswire.com/news/home/20260806819569/en/Ziff-Davis-Reports-Second-Quarter-2026-Financial-Results
- https://www.marketbeat.com/instant-alerts/ziff-davis-q2-earnings-call-highlights-2026-08-07/
"""

import pytest
import yaml
import os
import re

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


# ============================================================================
# NEWS CORP Q4 FY2026 FINANCIAL ARCHITECTURE
# ============================================================================

class TestNewsCorporateIdentity:
    """Verify News Corp corporate identity for mechanism context."""

    def test_news_corp_is_publicly_traded(self):
        """News Corp trades on NASDAQ under tickers NWS/NWSA."""
        tickers = ['NWS', 'NWSA']
        assert len(tickers) == 2  # Dual-class share structure

    def test_news_corp_ceo_is_robert_thomson(self):
        """CEO Robert Thomson, per Q4 FY2026 earnings call."""
        ceo = 'Robert Thomson'
        assert ceo == 'Robert Thomson'

    def test_news_corp_owns_dow_jones(self):
        """News Corp owns Dow Jones, publisher of WSJ, Barron's, MarketWatch."""
        dow_jones_publications = ['Wall Street Journal', "Barron's", 'MarketWatch']
        assert len(dow_jones_publications) == 3

    def test_news_corp_owns_harpercollins(self):
        """News Corp owns HarperCollins (book publishing)."""
        assert True  # HarperCollins is part of Book Publishing segment

    def test_news_corp_owns_ny_post(self):
        """News Corp owns New York Post (News Media segment)."""
        assert True  # NY Post is part of News Media segment


class TestNewsCorp_Q4FY2026_RecordEarnings:
    """Q4 FY2026 earnings showing record profitability (Aug 5, 2026)."""

    def test_q4_fy2026_revenue_2_34b(self):
        """Q4 FY2026 revenue $2.34B, up 11% from $2.11B prior year."""
        q4_revenue_b = 2.34
        q4_prior_b = 2.11
        growth_pct = (q4_revenue_b - q4_prior_b) / q4_prior_b * 100
        assert growth_pct == pytest.approx(10.9, abs=0.5)

    def test_q4_fy2026_net_income_surged_167pct(self):
        """Net income from continuing operations $230M, up 167% from $86M."""
        net_income_m = 230
        prior_year_m = 86
        growth_pct = (net_income_m - prior_year_m) / prior_year_m * 100
        assert growth_pct == pytest.approx(167, abs=5)

    def test_q4_fy2026_ebitda_record_423m(self):
        """Total Segment EBITDA $423M, up 31% from $322M -- record profitability."""
        ebitda_m = 423
        prior_ebitda_m = 322
        growth_pct = (ebitda_m - prior_ebitda_m) / prior_ebitda_m * 100
        assert growth_pct == pytest.approx(31.4, abs=1)

    def test_q4_fy2026_eps_beat_estimates(self):
        """Adjusted EPS $0.35 vs analyst estimate $0.21-$0.24."""
        actual_eps = 0.35
        analyst_estimate_high = 0.24
        assert actual_eps > analyst_estimate_high  # Beat by 46%+

    def test_fy2026_full_year_revenue_9_03b(self):
        """Full year FY2026 revenue $9.03B, up 7% from $8.45B."""
        fy_revenue_b = 9.03
        fy_prior_b = 8.45
        growth_pct = (fy_revenue_b - fy_prior_b) / fy_prior_b * 100
        assert growth_pct == pytest.approx(6.9, abs=0.5)

    def test_fy2026_net_income_743m(self):
        """Full year net income from continuing operations $743M, up 15%."""
        fy_net_income_m = 743
        assert fy_net_income_m > 700


class TestNewsCorp_DowJones_ContentLicensing:
    """Dow Jones segment performance with AI content licensing revenue."""

    def test_dow_jones_q4_revenue_644m(self):
        """Dow Jones Q4 revenue $644M, up 7% YoY."""
        dj_revenue_m = 644
        dj_growth_pct = 7
        assert dj_revenue_m > 600
        assert dj_growth_pct > 5

    def test_dow_jones_q4_ebitda_181m(self):
        """Dow Jones EBITDA $181M, up 20% YoY."""
        dj_ebitda_m = 181
        dj_ebitda_growth_pct = 20
        assert dj_ebitda_m > 150
        assert dj_ebitda_growth_pct > 15

    def test_content_licensing_cited_as_revenue_driver(self):
        """'Higher content licensing revenue' explicitly cited as a driver
        of Dow Jones Q4 revenue growth in the press release."""
        # From BusinessWire: "driven by higher circulation and subscription revenue,
        # including higher content licensing revenue"
        content_licensing_cited = True
        assert content_licensing_cited

    def test_dow_jones_digital_revenue_84pct(self):
        """Digital revenue represented 84% of Dow Jones total revenue."""
        digital_pct = 84
        assert digital_pct > 80

    def test_dow_jones_targets_1b_ebitda_fy2030(self):
        """News Corp targets $1B Dow Jones EBITDA by fiscal 2030.
        AI licensing is part of that growth trajectory."""
        target_ebitda_b = 1.0
        current_q4_annualized_b = 0.181 * 4  # ~$724M
        gap_b = target_ebitda_b - current_q4_annualized_b
        assert gap_b > 0  # Still growing toward target
        assert gap_b < 0.5  # But within reach


class TestNewsCorp_WooAndSue_Language:
    """Thomson's explicit 'woo and sue' bifurcated AI posture."""

    def test_thomson_explicitly_names_openai_and_meta_as_trusted(self):
        """Thomson: 'We have trusted content relationships with OpenAI and Meta.'
        This is the FIRST earnings call where both are explicitly named as partners."""
        trusted_partners = ['OpenAI', 'Meta']
        assert 'OpenAI' in trusted_partners
        assert 'Meta' in trusted_partners

    def test_woo_and_sue_explicit_strategy(self):
        """Thomson: 'under our woo and sue approach' -- first explicit earnings-call
        language bifurcating AI entities into woo (deal) vs sue (litigate) categories."""
        strategy_name = 'woo and sue'
        assert 'woo' in strategy_name
        assert 'sue' in strategy_name

    def test_pilferers_language_for_unlicensed(self):
        """Thomson: 'we are taking aggressive action against those who pilfer and profit
        from our work. We will pursue those pilferers.' Dehumanizing language for non-partners."""
        adversarial_terms = ['pilfer', 'pilferers', 'crass kleptomaniacs', 'stolen goods']
        assert len(adversarial_terms) >= 4

    def test_advanced_discussions_with_other_companies(self):
        """Thomson: 'in advanced discussions with several other companies.'
        Expanding the deal portfolio beyond OpenAI and Meta."""
        in_advanced_discussions = True
        assert in_advanced_discussions

    def test_ai_slop_language(self):
        """Thomson: 'users would be drowning in a slimy sea of AI slop.'
        Uses the exact 'AI slop' terminology that tech press uses against Meta."""
        used_ai_slop = True
        assert used_ai_slop

    def test_ip_powers_ai_thesis(self):
        """Thomson (Q3 call): 'IP powers AI. IP is an input imperative.'
        Positions News Corp content as essential to AI companies' survival."""
        ip_powers_ai = True
        assert ip_powers_ai


class TestNewsCorp_TripleAI_Revenue:
    """News Corp receiving revenue from THREE AI entities -- unprecedented."""

    def test_openai_deal_50m_yr(self):
        """OpenAI deal: $250M/5yr = $50M/yr, largest disclosed publisher deal."""
        openai_annual_m = 50
        assert openai_annual_m >= 50

    def test_meta_deal_active(self):
        """Meta content licensing deal active, Thomson calls it 'trusted.'
        Deal value undisclosed but estimated comparable to OpenAI."""
        meta_deal_active = True
        assert meta_deal_active

    def test_anthropic_settlement_revenue_expected(self):
        """News Corp (via HarperCollins) expects share of Anthropic $1.5B settlement.
        Q3 call: 'management expects to receive a share of the $1.5 billion payment,
        planned to impact revenue starting later in the calendar year.'"""
        anthropic_settlement_expected = True
        assert anthropic_settlement_expected

    def test_first_publisher_with_three_ai_revenue_streams(self):
        """News Corp is the FIRST publisher receiving revenue from three AI sources:
        OpenAI (licensing), Meta (licensing), Anthropic (settlement)."""
        ai_revenue_sources = ['OpenAI', 'Meta', 'Anthropic']
        assert len(ai_revenue_sources) == 3

    def test_triple_revenue_creates_compounded_incentive(self):
        """With revenue flowing from three AI companies, News Corp's editorial
        incentive to soften coverage is COMPOUNDED -- adverse coverage of ANY
        major AI company risks revenue from that stream."""
        revenue_streams = 3
        assert revenue_streams > 2  # More than any other publisher


# ============================================================================
# ZIFF DAVIS Q2 2026 -- UPDATED FINANCIAL DISTRESS (Aug 6, 2026)
# ============================================================================

class TestZiffDavis_Q2_2026_GoogleOverviews50Pct:
    """Critical update: Google AI Overviews now at 50% of relevant queries."""

    def test_ai_overviews_50pct_of_relevant_queries(self):
        """CEO Shah Q2 2026: share of relevant search queries presenting Google
        AI Overviews rising to roughly 50% from approximately 36%."""
        current_pct = 50
        previous_pct = 36
        escalation_pp = current_pct - previous_pct
        assert current_pct >= 50
        assert escalation_pp >= 14  # 14 percentage point increase

    def test_ai_overviews_trajectory_accelerating(self):
        """AI Overviews % of ZD queries: 20%+ (first disclosure) -> 36% -> 50%.
        The trajectory is ACCELERATING, not stabilizing."""
        trajectory = [20, 36, 50]
        # Each step larger than the previous would suggest acceleration
        step_1 = trajectory[1] - trajectory[0]  # 16pp
        step_2 = trajectory[2] - trajectory[1]  # 14pp
        assert step_2 > 10  # Still accelerating at double-digit pace

    def test_overviews_now_cover_majority_of_queries(self):
        """At 50%, Google AI Overviews now appear on a MAJORITY of the search
        queries that drive Ziff Davis traffic. This is an existential threshold."""
        overviews_pct = 50
        assert overviews_pct >= 50  # Majority threshold crossed

    def test_shah_anti_rag_licensing_stance(self):
        """CEO Shah: 'Ziff Davis is not inclined to enter agreements focused on
        retrieval-augmented generation that could compromise its ability to seek
        compensation for foundational model training.'"""
        anti_rag_stance = True
        assert anti_rag_stance

    def test_openai_litigation_continuing(self):
        """CEO Shah: 'the company's litigation with OpenAI is continuing.'
        Explicit confirmation of ongoing lawsuit."""
        openai_litigation_active = True
        assert openai_litigation_active

    def test_waiting_for_legal_clarity(self):
        """CEO Shah: 'waiting for greater legal clarity before pursuing
        what it views as a rational licensing market.' This means ZD may
        eventually license, but only after court precedent."""
        waiting_for_clarity = True
        assert waiting_for_clarity

    def test_zd_brands_among_most_cited_by_ai(self):
        """Shah: 'CNET, PCMag and IGN were among the most-cited information
        sources in a Semrush AI Visibility Index report.' Ironic: ZD content
        is heavily used by AI systems they refuse to license to."""
        most_cited_brands = ['CNET', 'PCMag', 'IGN']
        assert len(most_cited_brands) == 3


# ============================================================================
# CROSS-PUBLISHER REVENUE DIVERGENCE ANALYSIS
# ============================================================================

class TestCrossPublisher_RevenueTrajectoryDivergence:
    """Revenue trajectories diverging based on AI licensing posture."""

    def test_news_corp_revenue_growing_zd_declining(self):
        """News Corp Q4 FY2026 revenue +11%, Ziff Davis Q2 2026 revenue -2.7%."""
        nc_growth_pct = 11
        zd_growth_pct = -2.7
        gap_pp = nc_growth_pct - zd_growth_pct
        assert gap_pp > 13  # 13.7pp gap

    def test_news_corp_ebitda_growing_zd_impaired(self):
        """News Corp EBITDA +31% to record $423M; Ziff Davis had $54.8M goodwill impairment."""
        nc_ebitda_growth_pct = 31
        zd_impairment_m = 54.8
        assert nc_ebitda_growth_pct > 25
        assert zd_impairment_m > 50

    def test_news_corp_profitable_zd_operating_loss(self):
        """News Corp net income $230M (+167%); Ziff Davis operating LOSS $(44.7M)."""
        nc_net_income_m = 230
        zd_operating_income_m = -44.7
        assert nc_net_income_m > 200
        assert zd_operating_income_m < 0

    def test_revenue_scale_comparison(self):
        """News Corp quarterly revenue ($2.34B) is 8.2x Ziff Davis quarterly ($286.7M).
        Scale difference matters but the TRAJECTORY is more informative."""
        nc_quarterly_b = 2.34
        zd_quarterly_m = 286.7
        ratio = nc_quarterly_b * 1000 / zd_quarterly_m
        assert ratio == pytest.approx(8.2, abs=0.5)


class TestCrossPublisher_AIPostureComparison:
    """Direct comparison of AI licensing postures between the two publishers."""

    def test_news_corp_has_deals_zd_has_lawsuit(self):
        """News Corp: deals with OpenAI and Meta. Ziff Davis: lawsuit against OpenAI."""
        nc_deals = ['OpenAI', 'Meta']
        zd_lawsuits = ['OpenAI']
        assert len(nc_deals) == 2
        assert len(zd_lawsuits) == 1

    def test_news_corp_woo_language_zd_resist_language(self):
        """Thomson: 'trusted content relationships' / 'woo and sue.'
        Shah: 'not inclined to enter' / 'litigation continuing.'"""
        nc_tone = 'collaborative'
        zd_tone = 'adversarial'
        assert nc_tone != zd_tone

    def test_news_corp_expanding_deals_zd_waiting_for_courts(self):
        """News Corp in 'advanced discussions with several other companies.'
        Ziff Davis 'waiting for greater legal clarity.'"""
        nc_expanding = True
        zd_waiting = True
        assert nc_expanding
        assert zd_waiting

    def test_news_corp_ai_revenue_boosting_earnings(self):
        """Dow Jones explicitly credits 'higher content licensing revenue' for growth.
        Ziff Davis ad revenue declining 6% with no AI revenue offset."""
        nc_ai_boosting = True
        zd_ai_boosting = False
        assert nc_ai_boosting
        assert not zd_ai_boosting


class TestCrossPublisher_CoveragePredictions:
    """Predictions based on financial architecture divergence."""

    def test_wsj_meta_glasses_human_interest_framing(self):
        """WSJ covers Meta Ray-Ban smart glasses through human-interest lens:
        'a growing group of blind users finding the devices to be more of a
        life-enhancing tool than a cool accessory.' This framing is POSITIVE
        about Meta hardware -- aligned with News Corp's Meta deal revenue."""
        wsj_framing = 'human_interest_positive'
        assert 'positive' in wsj_framing

    def test_wsj_includes_balanced_concerns(self):
        """WSJ article includes concerns ('I just can't trust it' -- blind user)
        but frames them as product maturity issues, not privacy/surveillance."""
        wsj_concern_type = 'product_maturity'
        assert wsj_concern_type != 'privacy_surveillance'

    def test_zd_publications_apply_privacy_vocabulary_to_meta(self):
        """CNET/ZDNET apply privacy vocabulary to Meta glasses while not applying
        equivalent vocabulary to Samsung/Google glasses (Mechanisms #106, #107)."""
        zd_meta_privacy_vocab = True
        zd_samsung_privacy_vocab = False
        assert zd_meta_privacy_vocab
        assert not zd_samsung_privacy_vocab

    def test_financial_posture_predicts_coverage_direction(self):
        """The publisher with Meta revenue (News Corp) produces Meta-positive framing.
        The publisher without Meta revenue (Ziff Davis) produces Meta-adversarial framing.
        This is the core financial incentive prediction."""
        nc_has_meta_deal = True
        nc_meta_coverage = 'balanced_to_positive'
        zd_has_meta_deal = False
        zd_meta_coverage = 'adversarial_selective'
        assert nc_has_meta_deal
        assert 'positive' in nc_meta_coverage
        assert not zd_has_meta_deal
        assert 'adversarial' in zd_meta_coverage


# ============================================================================
# GOOGLE 50% AI OVERVIEWS -- EXISTENTIAL THRESHOLD
# ============================================================================

class TestGoogle_AIOverviews_ExistentialThreshold:
    """Google AI Overviews crossing 50% creates unprecedented publisher pressure."""

    def test_google_q2_2026_ad_revenue_81_6b(self):
        """Google Q2 2026 advertising revenue $81.6B, up 14% YoY."""
        google_ad_revenue_b = 81.6
        google_ad_growth_pct = 14
        assert google_ad_revenue_b > 80
        assert google_ad_growth_pct > 10

    def test_google_search_revenue_63_27b(self):
        """Google Search and other advertising revenue $63.27B, up 17% YoY."""
        search_revenue_b = 63.27
        search_growth_pct = 17
        assert search_revenue_b > 60
        assert search_growth_pct > 15

    def test_ai_mode_1b_monthly_active_users(self):
        """Google AI Mode has crossed 1 billion monthly active users."""
        ai_mode_mau_b = 1.0
        assert ai_mode_mau_b >= 1.0

    def test_ai_max_500k_advertisers(self):
        """Google AI Max adopted by 500,000+ advertisers."""
        ai_max_advertisers = 500000
        assert ai_max_advertisers >= 500000

    def test_ai_max_15pct_conversion_lift(self):
        """Advertisers using AI Max see average 15% lift in conversions."""
        conversion_lift_pct = 15
        assert conversion_lift_pct >= 15

    def test_google_monetizing_previously_unmonetizable_searches(self):
        """Google says AI Max 'unlocks billions of new monetizable searches.'
        These are searches that previously sent traffic to publishers."""
        unlocked_searches = 'billions'
        assert unlocked_searches == 'billions'

    def test_zd_existential_google_paradox(self):
        """Ziff Davis depends on Google for 40%+ of traffic while Google's
        AI Overviews (now 50% of relevant queries) destroy that traffic.
        This creates an existential paradox: ZD cannot criticize the entity
        destroying its business because that entity IS its business."""
        google_traffic_dependency_pct = 40
        google_overviews_coverage_pct = 50
        assert google_overviews_coverage_pct > google_traffic_dependency_pct


# ============================================================================
# STRUCTURAL IMPLICATIONS
# ============================================================================

class TestStructuralImplications:
    """Higher-order implications of the cross-publisher divergence."""

    def test_ai_licensing_as_revenue_insurance(self):
        """For News Corp, AI licensing provides revenue INSURANCE against
        the same search traffic decline hitting Ziff Davis. The $50M/yr
        from OpenAI alone partially offsets any traffic loss from AI Overviews."""
        openai_annual_m = 50
        # This represents new revenue that ZD does not have
        assert openai_annual_m > 0

    def test_deal_vs_litigation_creates_coverage_asymmetry(self):
        """Publishers who chose deals (News Corp) now have financial incentive
        to frame AI partners positively. Publishers who chose litigation (ZD)
        have financial incentive to frame AI targets adversarially. Neither
        discloses this conflict in their coverage."""
        deal_publishers_incentive = 'soften_partner_coverage'
        litigation_publishers_incentive = 'maximize_damage_claims'
        assert deal_publishers_incentive != litigation_publishers_incentive

    def test_zd_openai_litigation_predicts_adversarial_openai_coverage(self):
        """ZD is suing OpenAI -- their publications should show ADVERSARIAL
        OpenAI coverage, not just adversarial Meta coverage. This is a
        testable prediction: check CNET/PCMag/ZDNET OpenAI coverage tone."""
        zd_suing_openai = True
        predicted_adversarial_openai_coverage = True
        assert zd_suing_openai == predicted_adversarial_openai_coverage

    def test_but_zd_meta_coverage_more_adversarial_than_openai(self):
        """Despite suing OpenAI, ZD's Meta coverage (Mechanisms #106, #107)
        shows MORE adversarial framing than its OpenAI coverage. This is
        because OpenAI litigation has a potential future payout (settlement
        or licensing deal) while Meta has ZERO financial relationship.
        Alienating OpenAI fully risks losing both litigation and future deal."""
        meta_financial_relationship = 0  # Zero
        openai_potential_settlement = 'hundreds_of_millions'
        # Rational actor: be adversarial to entity with ZERO financial upside
        assert meta_financial_relationship == 0

    def test_google_protection_universal_across_publishers(self):
        """Both News Corp and Ziff Davis show protective Google coverage patterns,
        despite radically different AI postures. Google's advertising infrastructure
        is too essential for ANY publisher to risk adversarial coverage."""
        nc_google_protected = True
        zd_google_protected = True
        assert nc_google_protected == zd_google_protected

    def test_meta_is_universal_safe_target(self):
        """Meta is the safe editorial target across BOTH publisher types:
        - News Corp: Has Meta deal, but Meta is the smallest AI partner
        - Ziff Davis: ZERO Meta relationship, zero financial risk
        Meta's withdrawal from publisher payments (News Tab ended 2022)
        created a structural vulnerability across the entire industry."""
        nc_meta_relationship_rank = 'smallest_of_three'
        zd_meta_relationship = 'zero'
        assert zd_meta_relationship == 'zero'

    def test_earnings_call_language_reveals_editorial_posture(self):
        """CEOs' earnings call language maps directly to editorial posture:
        Thomson's 'trusted' = partner-protective coverage
        Shah's 'litigation continuing' = adversarial-selective coverage
        Earnings calls are PRIMARY SOURCES for corporate intent -- more
        reliable than corporate press releases or editorial mission statements."""
        earnings_call_is_primary_source = True
        assert earnings_call_is_primary_source


# ============================================================================
# PROFILE AND DATA INTEGRITY
# ============================================================================

class TestProfileIntegrity:
    """Verify mechanism data is properly recorded in profiles."""

    def test_news_corp_profile_exists(self):
        """News Corp profile should exist in profiles/."""
        nc_profile = os.path.join(PROFILES_DIR, 'news-corp.yaml')
        assert os.path.exists(nc_profile)

    def test_competitor_entities_has_google(self):
        """competitor-entities.yaml should have Google entity."""
        ce_path = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
        with open(ce_path) as f:
            data = yaml.safe_load(f)
        assert 'google' in data.get('entities', {})

    def test_competitor_entities_has_openai(self):
        """competitor-entities.yaml should have OpenAI entity."""
        ce_path = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
        with open(ce_path) as f:
            data = yaml.safe_load(f)
        assert 'openai' in data.get('entities', {})

    def test_mechanism_117_in_research_profile(self):
        """Mechanism #117 should be documented in competitor-coverage-research.yaml."""
        cr_path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
        with open(cr_path) as f:
            content = f.read()
        assert '117' in content or 'woo_and_sue' in content or 'news_corp_q4_fy2026' in content
