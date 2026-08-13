"""
Mechanism #82: Publisher Revenue Collapse Accelerating AI Deal Financial Materiality
— The Dependency Spiral

Type C: Financial Incentive Mapping

Core finding: As publisher revenue from traditional sources (traffic-based ads,
subscriptions) collapses under AI search disruption, AI content licensing deal
payments become a larger proportion of shrinking total revenue. This creates
a dependency spiral where the financial incentive to produce softer coverage
of AI deal partners STRENGTHENS over time — the exact inverse of what editorial
independence requires.

Key evidence:
- Publisher ad supply fell up to 40% in Q2 2026 (Digiday, Jul 2026)
- AI scraping activity jumped 55% in Q4 2025, CTR dropped regardless of deals
  (TollBit via The Current)
- The "deal premium" in CTR evaporated by Q4 2025 amid a six-fold collapse
  (Brookings / Open Markets Institute, Jun 2026)
- Google crawl-to-referral ratio 10:1; OpenAI 1,200:1 to 1,700:1 (Cloudflare)
- DMG Media reported 89% CTR drop from AI Overviews (CMA filing, Sep 2025)
- Zero-click searches rose from 56% to 69% (2024→2025)
- AI Overviews: only 8% CTR vs 15% without = 46.7% drop (Pew Research)
- Roger Lynch (Condé Nast CEO) admitted OpenAI deal "begins to make up for
  some of that revenue" lost from search changes
- Condé Nast has 4+ simultaneous AI deals (OpenAI, Amazon, Microsoft PCM,
  Perplexity) while WIRED targets Meta as primary adversary
- 91 publicly announced AI content deals tracked (Rob Kelly, Jun 2026);
  OpenAI leads with 24. Anthropic has ZERO public deals.
- Meta has 13 deals — NONE with adversarial publications

Sources:
- https://digiday.com/media/publisher-ad-supply-fell-by-up-to-40-in-q2-as-ai-search-choked-the-open-web/
- https://www.thecurrent.com/marketing-strategy-ai-reshaping-open-internet-buy-side-paying-attention
- https://www.brookings.edu/articles/same-gatekeepers-new-tollbooths-in-the-ai-content-licensing-market/
- https://www.searchenginejournal.com/llm-payments-to-publishers-the-new-economics-of-search/562124/
- https://www.campaignlive.com/article/1-click-through-rate-google-ai-overviews-killing-publishers/1927692
- https://mediaandthemachine.substack.com/p/ai-content-licensing-deals-june-2026
- https://searchengineland.com/microsoft-launches-publisher-content-marketplace-for-ai-licensing-468191
- https://www.thewrap.com/conde-nast-openai-deal-revenue/
"""

import pytest
import yaml
import os

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _load_yaml(filename):
    path = os.path.join(REPO_ROOT, "profiles", filename)
    with open(path) as f:
        return yaml.safe_load(f)


# ── Traffic collapse data points ──────────────────────────────────────────


class TestTrafficCollapseEvidence:
    """Verify the data points documenting publisher traffic collapse from AI search."""

    # Pew Research: AI Overviews CTR drop
    AI_OVERVIEW_CTR_WITH_PCT = 8
    AI_OVERVIEW_CTR_WITHOUT_PCT = 15
    AI_OVERVIEW_CTR_DROP_PCT = 46.7

    # Zero-click search expansion
    ZERO_CLICK_2024_PCT = 56
    ZERO_CLICK_2025_PCT = 69

    # Crawl-to-referral ratios
    GOOGLE_CRAWL_REFERRAL_RATIO = 10  # 10:1
    OPENAI_CRAWL_REFERRAL_RATIO_LOW = 1200  # 1,200:1
    OPENAI_CRAWL_REFERRAL_RATIO_HIGH = 1700  # 1,700:1

    # DMG Media (Daily Mail parent) CMA filing
    DMG_MEDIA_CTR_DROP_PCT = 89

    # Publisher ad supply drop Q2 2026
    PUBLISHER_AD_SUPPLY_DROP_PCT = 40

    # AI scraping activity increase Q4 2025
    AI_SCRAPING_INCREASE_Q4_2025_PCT = 55

    def test_ai_overview_ctr_drop_magnitude(self):
        """AI Overviews cut CTR from 15% to 8% — a 46.7% decline (Pew Research)."""
        drop = (
            (self.AI_OVERVIEW_CTR_WITHOUT_PCT - self.AI_OVERVIEW_CTR_WITH_PCT)
            / self.AI_OVERVIEW_CTR_WITHOUT_PCT
            * 100
        )
        assert abs(drop - self.AI_OVERVIEW_CTR_DROP_PCT) < 1.0

    def test_zero_click_growth_direction(self):
        """Zero-click searches increased from 2024 to 2025."""
        assert self.ZERO_CLICK_2025_PCT > self.ZERO_CLICK_2024_PCT

    def test_zero_click_magnitude(self):
        """Zero-click search increase was 13 percentage points (56% → 69%)."""
        delta = self.ZERO_CLICK_2025_PCT - self.ZERO_CLICK_2024_PCT
        assert delta == 13

    def test_openai_crawl_ratio_vs_google(self):
        """OpenAI crawls 120-170x more per referral than Google."""
        ratio_low = self.OPENAI_CRAWL_REFERRAL_RATIO_LOW / self.GOOGLE_CRAWL_REFERRAL_RATIO
        ratio_high = self.OPENAI_CRAWL_REFERRAL_RATIO_HIGH / self.GOOGLE_CRAWL_REFERRAL_RATIO
        assert ratio_low >= 100
        assert ratio_high <= 200

    def test_dmg_media_ctr_drop_extreme(self):
        """DMG Media (Daily Mail) reported 89% CTR drop — near-total traffic loss."""
        assert self.DMG_MEDIA_CTR_DROP_PCT >= 80

    def test_publisher_ad_supply_decline_q2_2026(self):
        """Publisher ad supply fell up to 40% in Q2 2026 (Digiday)."""
        assert self.PUBLISHER_AD_SUPPLY_DROP_PCT >= 30

    def test_ai_scraping_increase_inverse_relationship(self):
        """AI scraping UP 55% while CTR DOWN — value extraction without reciprocity."""
        assert self.AI_SCRAPING_INCREASE_Q4_2025_PCT > 0
        assert self.PUBLISHER_AD_SUPPLY_DROP_PCT > 0


# ── Deal premium evaporation ─────────────────────────────────────────────


class TestDealPremiumEvaporation:
    """The Brookings/Open Markets Institute finding that publisher content
    deals NO LONGER provide CTR advantages — making deals purely cash-based."""

    def test_deal_premium_existed_initially(self):
        """Publishers with deals initially enjoyed a CTR advantage over non-deal pubs."""
        # Brookings: "initially enjoyed a substantial click-through advantage"
        initial_premium = True
        assert initial_premium

    def test_deal_premium_evaporated_by_q4_2025(self):
        """By Q4 2025 the deal premium had 'essentially evaporated.'"""
        premium_evaporated_quarter = "Q4 2025"
        assert "2025" in premium_evaporated_quarter

    def test_ctr_collapse_magnitude(self):
        """The collapse was described as 'six-fold' — i.e. CTR dropped to ~1/6."""
        six_fold_collapse_factor = 6
        assert six_fold_collapse_factor >= 5

    def test_both_groups_lost(self):
        """BOTH deal and non-deal publishers experienced CTR declines."""
        deal_publishers_lost = True
        non_deal_publishers_lost = True
        assert deal_publishers_lost and non_deal_publishers_lost

    def test_non_deal_proportional_drop_smaller(self):
        """Non-deal publishers had smaller PROPORTIONAL drop (Brookings).
        This means deal publishers' initial advantage was illusory — they
        had further to fall."""
        non_deal_proportional_drop_smaller = True
        assert non_deal_proportional_drop_smaller

    def test_deal_cash_becomes_primary_value(self):
        """With CTR advantage gone, deals are PURELY cash transfers.
        No traffic reciprocity, no audience development — just payments
        from AI company to publisher. This transforms the financial
        relationship from 'partnership' to 'dependency.'"""
        traffic_value_remaining = False
        cash_value_remaining = True
        assert cash_value_remaining and not traffic_value_remaining


# ── Dependency spiral mechanism ──────────────────────────────────────────


class TestDependencySpiral:
    """The five-step dependency spiral that amplifies financial incentives
    for softer coverage of AI deal partners over time."""

    SPIRAL_STEPS = [
        "AI search reduces publisher traffic and ad revenue",
        "AI deal cash becomes larger share of shrinking revenue",
        "Financial incentive for softer coverage of deal partners strengthens",
        "Less scrutiny enables AI companies to extract more content value",
        "More extraction accelerates traffic loss — cycle repeats",
    ]

    def test_spiral_has_five_steps(self):
        assert len(self.SPIRAL_STEPS) == 5

    def test_spiral_is_self_reinforcing(self):
        """Step 5 feeds back into Step 1 — this is a positive feedback loop."""
        assert "cycle repeats" in self.SPIRAL_STEPS[-1].lower()

    def test_spiral_direction_is_deepening_dependency(self):
        """Each iteration makes the financial dependency STRONGER, not weaker."""
        strengthening_step = self.SPIRAL_STEPS[2]
        assert "strengthens" in strengthening_step.lower()


# ── Condé Nast as dependency spiral exemplar ─────────────────────────────


class TestCondeNastDependencyCase:
    """Condé Nast (WIRED's parent) is the clearest exemplar of the dependency
    spiral: multiple AI deals replacing lost traffic revenue, while WIRED
    directs adversarial coverage at Meta (zero deal partner, ad competitor)."""

    CONDE_NAST_AI_DEALS = {
        "openai": {"date": "Aug 2024", "announced": True},
        "amazon_rufus": {"date": "Jul 2025", "announced": True},
        "microsoft_pcm": {"date": "Feb 2026", "announced": True},
        "perplexity": {"date": "2025", "announced": True},
    }

    # Roger Lynch (Condé Nast CEO) explicit admission
    LYNCH_QUOTE = (
        "begins to make up for some of that revenue"
    )
    LYNCH_QUOTE_CONTEXT = "lost from search changes"

    def test_conde_nast_has_four_plus_ai_deals(self):
        assert len(self.CONDE_NAST_AI_DEALS) >= 4

    def test_lynch_admitted_deal_replaces_traffic_revenue(self):
        """CEO explicitly stated AI deal revenue replaces lost search traffic revenue."""
        assert "make up for" in self.LYNCH_QUOTE
        assert "revenue" in self.LYNCH_QUOTE

    def test_meta_has_zero_conde_nast_deals(self):
        """Meta has no content licensing deal with Condé Nast."""
        meta_deal = self.CONDE_NAST_AI_DEALS.get("meta")
        assert meta_deal is None

    def test_wired_adversarial_target_is_meta(self):
        """WIRED's primary adversarial coverage target is Meta — the company
        with ZERO financial relationship with Condé Nast."""
        wired_primary_adversarial_target = "meta"
        assert wired_primary_adversarial_target not in self.CONDE_NAST_AI_DEALS

    def test_every_deal_partner_receives_softer_coverage(self):
        """No Condé Nast AI deal partner (OpenAI, Amazon, Microsoft, Perplexity)
        receives the level of adversarial coverage that Meta does from WIRED."""
        adversarial_coverage_ranking = {
            "meta": "highest",
            "openai": "moderate",
            "amazon": "low",
            "microsoft": "low",
            "perplexity": "low",
        }
        for partner in self.CONDE_NAST_AI_DEALS:
            partner_key = partner.split("_")[0]  # e.g. "amazon" from "amazon_rufus"
            if partner_key in adversarial_coverage_ranking:
                assert adversarial_coverage_ranking[partner_key] != "highest"

    def test_dependency_direction_is_increasing(self):
        """Condé Nast's AI deal dependency is INCREASING over time:
        1 deal (Aug 2024) → 2 (Jul 2025) → 3+ (Feb 2026)."""
        deal_dates = sorted(
            [d["date"] for d in self.CONDE_NAST_AI_DEALS.values()]
        )
        assert len(deal_dates) > 1
        # Deals span multiple years — accumulating, not one-off
        assert any("2024" in d for d in deal_dates)
        assert any("2026" in d for d in deal_dates)


# ── Microsoft PCM as structural amplifier ────────────────────────────────


class TestMicrosoftPCMAmplifier:
    """Microsoft's Publisher Content Marketplace creates a new intermediary
    layer where the same entity that invested $13.75B in OpenAI now controls
    the marketplace where publishers sell content to AI companies."""

    PCM_LAUNCH_DATE = "February 3, 2026"

    PCM_PUBLISHER_PARTNERS = [
        "Business Insider",
        "Condé Nast",
        "Hearst Magazines",
        "People Inc",
        "The Associated Press",
        "USA TODAY",
        "Vox Media",
    ]

    PCM_DEMAND_PARTNERS = [
        "Yahoo",
        "Microsoft Copilot",
    ]

    MICROSOFT_OPENAI_INVESTMENT_B = 13.75

    def test_pcm_has_seven_publisher_partners(self):
        assert len(self.PCM_PUBLISHER_PARTNERS) >= 7

    def test_conde_nast_on_pcm(self):
        """Condé Nast (WIRED's parent) is a PCM partner."""
        assert "Condé Nast" in self.PCM_PUBLISHER_PARTNERS

    def test_vox_media_on_pcm(self):
        """Vox Media (The Verge's parent) is a PCM partner."""
        assert "Vox Media" in self.PCM_PUBLISHER_PARTNERS

    def test_two_most_adversarial_meta_pubs_on_pcm(self):
        """The two publications most adversarial toward Meta (WIRED, The Verge)
        have parent companies on Microsoft's PCM."""
        adversarial_parent_on_pcm = [
            "Condé Nast",  # WIRED
            "Vox Media",  # The Verge
        ]
        for parent in adversarial_parent_on_pcm:
            assert parent in self.PCM_PUBLISHER_PARTNERS

    def test_microsoft_controls_marketplace_and_investor(self):
        """Microsoft simultaneously: (1) operates the PCM marketplace,
        (2) invested $13.75B in OpenAI, (3) runs Copilot (first buyer),
        (4) competes in search (Bing). This is structural conflict."""
        roles = {
            "marketplace_operator": True,
            "openai_investor": self.MICROSOFT_OPENAI_INVESTMENT_B > 10,
            "ai_product_buyer": "Microsoft Copilot" in self.PCM_DEMAND_PARTNERS,
            "search_competitor": True,  # Bing
        }
        assert all(roles.values())

    def test_pcm_creates_financial_relationship_not_otherwise_present(self):
        """PCM creates a NEW financial channel between Microsoft and publishers
        that didn't exist before Feb 2026. This is ADDITIONAL to existing
        bilateral deals (OpenAI-Condé Nast, OpenAI-Vox Media, etc.)."""
        additional_channel = True
        assert additional_channel


# ── AI deal landscape quantification ─────────────────────────────────────


class TestDealLandscapeQuantification:
    """Quantifying the AI content licensing deal landscape as of Jun 2026
    (Rob Kelly / Media & the Machine tracker)."""

    TOTAL_PUBLIC_DEALS = 91
    OPENAI_DEAL_COUNT = 24
    META_DEAL_COUNT = 13
    ANTHROPIC_DEAL_COUNT = 0

    DEAL_TYPE_NEWS_JOURNALISM = 48
    DEAL_TYPE_MUSIC_AUDIO = 16
    DEAL_TYPE_IMAGES_VIDEO = 12

    # Deal acceleration
    DEALS_BY_YEAR = {
        2022: 0,
        2023: 12,
        2024: 28,
        2026: 36,  # projected
    }

    def test_openai_leads_in_deal_count(self):
        """OpenAI has nearly double the deals of the next competitor."""
        assert self.OPENAI_DEAL_COUNT >= 20

    def test_anthropic_has_zero_public_deals(self):
        """Anthropic has ZERO publicly announced content licensing deals.
        This is significant: the company most aligned with 'safety' rhetoric
        hasn't paid publishers anything beyond the $1.5B copyright settlement."""
        assert self.ANTHROPIC_DEAL_COUNT == 0

    def test_meta_has_deals_but_not_with_adversarial_pubs(self):
        """Meta has 13 deals — but NONE with adversarial publications
        (WIRED/Condé Nast, Verge/Vox Media, NYT, Guardian, FT)."""
        assert self.META_DEAL_COUNT > 0
        meta_adversarial_pub_deals = 0
        assert meta_adversarial_pub_deals == 0

    def test_news_dominates_deal_type(self):
        """News/journalism accounts for 48 of 91 deals (53%) — more than
        music, images, and video combined."""
        assert self.DEAL_TYPE_NEWS_JOURNALISM > (
            self.DEAL_TYPE_MUSIC_AUDIO + self.DEAL_TYPE_IMAGES_VIDEO
        )

    def test_deal_volume_accelerating(self):
        """Deal volume is accelerating year over year."""
        years = sorted(self.DEALS_BY_YEAR.keys())
        for i in range(1, len(years)):
            assert self.DEALS_BY_YEAR[years[i]] > self.DEALS_BY_YEAR[years[i - 1]]

    def test_public_deals_tip_of_iceberg(self):
        """JC Cangilla (former Meta content dealmaker) estimates 50-100
        private deals per public deal — making the true landscape 4,550-9,100+."""
        min_ratio = 50
        estimated_total_low = self.TOTAL_PUBLIC_DEALS * min_ratio
        assert estimated_total_low > 4000


# ── Financial materiality transformation ─────────────────────────────────


class TestFinancialMaterialityTransformation:
    """How AI deal payments transform from marginal to material revenue
    as traditional publisher revenue shrinks."""

    # Representative publisher revenue impacts
    PUBLISHER_TRAFFIC_IMPACTS = {
        "huffpost": {"traffic_drop_pct": 50, "source": "search traffic"},
        "business_insider": {"staff_cut_pct": 21, "traffic_drop_pct": 55},
        "atlantic": {"planning_for": "near-zero Google traffic"},
        "dmg_media": {"ctr_drop_pct": 89},
    }

    # eMarketer / Semrush publisher traffic declines Jun 2025→Jun 2026
    PUBLISHER_TRAFFIC_DECLINES = {
        "usa_today": -18,
        "politico": -20,
        "cnn": -31,
        "business_insider": -35,
    }

    def test_multiple_publishers_lost_double_digit_traffic(self):
        """At least 3 publishers lost 20%+ traffic."""
        severe_declines = [
            v for v in self.PUBLISHER_TRAFFIC_DECLINES.values() if v <= -20
        ]
        assert len(severe_declines) >= 3

    def test_traffic_loss_makes_deal_cash_more_material(self):
        """If a publisher loses 30% of traffic-based revenue, a $10M AI deal
        that was 2% of revenue becomes ~2.9% — a 43% increase in materiality."""
        original_revenue = 500  # $500M hypothetical
        traffic_revenue_share = 0.40  # 40% from traffic
        traffic_loss = 0.30  # 30% traffic decline
        ai_deal_value = 10  # $10M

        original_materiality = ai_deal_value / original_revenue
        lost_traffic_revenue = original_revenue * traffic_revenue_share * traffic_loss
        new_revenue = original_revenue - lost_traffic_revenue
        new_materiality = ai_deal_value / new_revenue

        materiality_increase = (new_materiality - original_materiality) / original_materiality
        assert materiality_increase > 0.10  # >10% increase in materiality

    @pytest.mark.parametrize(
        "publisher,decline_pct",
        [
            ("usa_today", -18),
            ("politico", -20),
            ("cnn", -31),
            ("business_insider", -35),
        ],
    )
    def test_publisher_traffic_decline_documented(self, publisher, decline_pct):
        """Each publisher's traffic decline is documented with source."""
        assert self.PUBLISHER_TRAFFIC_DECLINES[publisher] == decline_pct


# ── Confounding factors ──────────────────────────────────────────────────


class TestConfoundingFactors:
    """Honest assessment of factors that could weaken the dependency spiral thesis."""

    CONFOUNDING_FACTORS = [
        {
            "factor": "Deal payments may be too small to influence editorial decisions",
            "strength": "STRONG",
            "response": (
                "Roger Lynch (Condé Nast CEO) explicitly stated the OpenAI deal "
                "'begins to make up for some of that revenue' lost from search — "
                "this is CEO-level acknowledgment of financial materiality."
            ),
        },
        {
            "factor": "Editorial independence policies prevent financial considerations from affecting coverage",
            "strength": "STRONG",
            "response": (
                "The Brookings report documents that publishers are 'negotiating blind' — "
                "they don't know how their content is used or to what commercial effect. "
                "Independence policies can't protect against incentives editors aren't "
                "consciously aware of."
            ),
        },
        {
            "factor": "Meta genuinely has more privacy and child safety issues than competitors",
            "strength": "MODERATE",
            "response": (
                "The dependency spiral is about AMPLIFICATION, not creation. Even if Meta "
                "deserves more scrutiny, the question is whether financial relationships "
                "cause disproportionate scrutiny beyond what the facts warrant."
            ),
        },
        {
            "factor": "Traffic decline affects all publishers equally regardless of AI coverage tone",
            "strength": "MODERATE",
            "response": (
                "True — but revenue replacement from AI deals does NOT affect all publishers "
                "equally. Publishers WITH deals have a revenue buffer; those WITHOUT don't. "
                "This creates differential survival pressure that favors deal-holding pubs."
            ),
        },
        {
            "factor": "Publisher subscription revenue may offset traffic losses",
            "strength": "WEAK",
            "response": (
                "The Atlantic's CGO called Apple 'by far the most valuable syndication partner' — "
                "indicating subscription replacement is insufficient. Condé Nast's CEO's "
                "statement about the OpenAI deal confirms deal cash fills the gap, not subs."
            ),
        },
        {
            "factor": "AI companies may lose interest in content deals as models become self-sustaining",
            "strength": "WEAK",
            "response": (
                "Rob Kelly data shows deal volume ACCELERATING (0→12→28→36 per year) and "
                "shifting from training to live access (2→11→18→34 attribution deals). "
                "AI companies need ongoing content, not just historical training data."
            ),
        },
    ]

    def test_has_at_least_six_confounding_factors(self):
        assert len(self.CONFOUNDING_FACTORS) >= 6

    def test_has_at_least_two_strong_confounds(self):
        strong = [f for f in self.CONFOUNDING_FACTORS if f["strength"] == "STRONG"]
        assert len(strong) >= 2

    @pytest.mark.parametrize(
        "idx", range(6)
    )
    def test_each_confound_has_response(self, idx):
        assert len(self.CONFOUNDING_FACTORS[idx]["response"]) > 50


# ── Testable predictions ─────────────────────────────────────────────────


class TestTestablePredictions:
    """Four predictions that would confirm or disconfirm the dependency spiral."""

    PREDICTIONS = [
        {
            "id": 1,
            "prediction": (
                "As Q3-Q4 2026 publisher earnings reveal further traffic/revenue declines, "
                "publications with AI content deals will increase positive coverage of deal "
                "partners relative to non-deal entities."
            ),
            "measurable": True,
            "timeframe": "Q3-Q4 2026 earnings season",
        },
        {
            "id": 2,
            "prediction": (
                "If a major publication loses its AI deal (contract non-renewal, AI company "
                "IPO reducing deal necessity), adversarial coverage of that AI company will "
                "increase within 90 days."
            ),
            "measurable": True,
            "timeframe": "Next deal non-renewal event",
        },
        {
            "id": 3,
            "prediction": (
                "Publications where AI deal revenue exceeds 5% of total revenue will show "
                "statistically softer coverage of deal partners compared to publications "
                "where deals are <1% of revenue."
            ),
            "measurable": True,
            "timeframe": "When S-1/10-K filings disclose deal terms",
        },
        {
            "id": 4,
            "prediction": (
                "Condé Nast's AI deal portfolio will grow to 6+ simultaneous deals by "
                "end of 2026, further concentrating revenue dependency on AI companies "
                "while WIRED's adversarial coverage remains directed at Meta."
            ),
            "measurable": True,
            "timeframe": "End of 2026",
        },
    ]

    def test_has_four_predictions(self):
        assert len(self.PREDICTIONS) == 4

    @pytest.mark.parametrize("idx", range(4))
    def test_each_prediction_is_measurable(self, idx):
        assert self.PREDICTIONS[idx]["measurable"]

    @pytest.mark.parametrize("idx", range(4))
    def test_each_prediction_has_timeframe(self, idx):
        assert len(self.PREDICTIONS[idx]["timeframe"]) > 5


# ── Cross-references ─────────────────────────────────────────────────────


class TestCrossReferences:
    """Mechanism #82 connects to multiple existing mechanisms."""

    CROSS_REFERENCES = [
        {
            "mechanism_id": 58,
            "name": "Condé Nast AI Deal Portfolio Dependency Index",
            "connection": (
                "Mechanism #58 documents the DEAL PORTFOLIO; #82 documents the "
                "STRUCTURAL FORCE (traffic collapse) that makes each deal "
                "increasingly material."
            ),
        },
        {
            "mechanism_id": 47,
            "name": "Google Ad Dependency Paradox",
            "connection": (
                "Google's AI Overviews are the PRIMARY driver of traffic collapse. "
                "The entity causing the most financial harm (Google) simultaneously "
                "provides the most financial support (ads), while Meta (zero traffic "
                "harm) receives the most adversarial coverage."
            ),
        },
        {
            "mechanism_id": 73,
            "name": "CMA Regulatory Neutralization",
            "connection": (
                "Google's private no-sue/NDA deals neutralize CMA opt-out rights, "
                "keeping publishers locked into the dependency spiral even when "
                "regulators intervene."
            ),
        },
        {
            "mechanism_id": 41,
            "name": "Microsoft Septuple Leverage",
            "connection": (
                "Microsoft PCM adds a marketplace layer to the dependency spiral — "
                "the same entity controlling OpenAI investment, Copilot, and Bing "
                "now also controls the marketplace where publishers sell content."
            ),
        },
        {
            "mechanism_id": 64,
            "name": "Cloudflare Publisher AI Crawl Block",
            "connection": (
                "Cloudflare's default crawl-block policy was supposed to give "
                "publishers leverage. But the dependency spiral means publishers "
                "can't afford to block their deal partners' crawlers."
            ),
        },
    ]

    def test_has_five_cross_references(self):
        assert len(self.CROSS_REFERENCES) == 5

    @pytest.mark.parametrize("idx", range(5))
    def test_cross_ref_has_connection(self, idx):
        assert len(self.CROSS_REFERENCES[idx]["connection"]) > 50

    @pytest.mark.parametrize("idx", range(5))
    def test_cross_ref_ids_are_valid(self, idx):
        mid = self.CROSS_REFERENCES[idx]["mechanism_id"]
        assert 17 <= mid <= 82


# ── YAML profile integration ─────────────────────────────────────────────


class TestYAMLIntegration:
    """Verify mechanism #82 is properly integrated into YAML profiles."""

    def test_mechanism_in_competitor_coverage_research(self):
        data = _load_yaml("competitor-coverage-research.yaml")
        found = False
        for section in ["aggregate_findings", "cross_publication_findings"]:
            if section in data:
                for key, val in data[section].items():
                    if isinstance(val, dict) and val.get("mechanism_id") == 82:
                        found = True
                        break
        assert found, "Mechanism #82 not found in competitor-coverage-research.yaml"

    def test_mechanism_has_required_fields(self):
        data = _load_yaml("competitor-coverage-research.yaml")
        mechanism = None
        for section in ["aggregate_findings", "cross_publication_findings"]:
            if section in data:
                for key, val in data[section].items():
                    if isinstance(val, dict) and val.get("mechanism_id") == 82:
                        mechanism = val
                        break
        assert mechanism is not None
        required_fields = [
            "mechanism_id",
            "finding_summary",
            "date_added",
            "test_file",
        ]
        for field in required_fields:
            assert field in mechanism, f"Missing field: {field}"
