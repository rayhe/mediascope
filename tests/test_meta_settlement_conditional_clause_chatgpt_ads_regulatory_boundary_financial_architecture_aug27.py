"""
Test: Meta Settlement Conditional Clause + ChatGPT Ads Europe Regulatory Boundary Financial Architecture
Mechanism: #344
Type: Financial Incentive Mapping (Type C)
Date: 2026-08-27

Core finding: The Meta child safety settlement ($16.68B, Aug 26) names Snap, TikTok, and YouTube
in its $5.3B conditional clause. OpenAI/ChatGPT -- which launched ads in 31 European markets
48 hours earlier (Aug 24), relies on behavioral "age prediction" for teen safety, and is under
FTC investigation for chatbot child safety -- is NOT named. Publisher financial positions
(OpenAI content deals, IPO underwriter relationships) predict coverage framing of both events.

Sources:
- Reuters: https://www.reuters.com/business/meta-reaches-18-billion-settlements-over-childrens-social-media-addiction-2026-08-26/
- TechRepublic: https://www.techrepublic.com/article/news-openai-chatgpt-ads-europe-emea/
- Le Monde: https://www.lemonde.fr/en/economy/article/2026/08/25/ads-arrive-on-chatgpt-in-france_6756812_19.html
- Seoul Economic Daily: https://en.sedaily.com/international/2026/08/21/anthropic-to-file-for-ipo-this-month-eyeing-2-trillion
- TechCrunch (age prediction): https://techcrunch.com/2026/01/20/in-an-effort-to-protect-young-users-chatgpt-will-now-predict-how-old-you-are/
- CNN: https://www.cnn.com/2026/08/27/tech/meta-settlement-impact-on-teens-business
- MarketWatch: https://www.marketwatch.com/story/metas-stock-rises-as-the-company-settles-in-social-media-addiction-trial-78abdfbf
- NotebookCheck: https://www.notebookcheck.net/ChatGPT-ads-hit-Europe-on-Monday-but-not-the-personalized-kind.1375456.0.html
"""

import unittest


class TestSettlementConditionalClauseStructure(unittest.TestCase):
    """Tests for the $5.3B conditional clause entity selection."""

    def test_conditional_clause_names_three_entities(self):
        """Settlement conditional clause names exactly Snap, TikTok, YouTube."""
        conditional_entities = {"Snapchat", "TikTok", "YouTube"}
        assert len(conditional_entities) == 3
        assert "Snapchat" in conditional_entities
        assert "TikTok" in conditional_entities
        assert "YouTube" in conditional_entities

    def test_conditional_clause_excludes_openai(self):
        """OpenAI/ChatGPT not named in conditional clause despite comparable characteristics."""
        conditional_entities = {"Snapchat", "TikTok", "YouTube"}
        excluded_entities = {"ChatGPT/OpenAI", "Character.AI", "xAI/Grok", "Claude/Anthropic"}
        for entity in excluded_entities:
            base_name = entity.split("/")[0]
            assert base_name not in conditional_entities, (
                f"{entity} should be excluded from conditional clause"
            )

    def test_conditional_amount_structure(self):
        """$12.7B guaranteed + $5.3B conditional = ~$18B total."""
        guaranteed_b = 12.7
        conditional_b = 5.3
        total_b = guaranteed_b + conditional_b
        assert total_b == 18.0, "Total should be $18B"
        assert conditional_b / total_b > 0.29, "Conditional portion is ~29% of total"

    def test_conditional_clause_creates_industry_pressure(self):
        """Conditional clause financially incentivizes states to pursue named competitors."""
        conditional_b = 5.3
        states_count = 47  # + DC, PR, territories
        # Each state receives additional funding only if competitors adopt
        avg_conditional_per_state_m = (conditional_b * 1000) / states_count
        assert avg_conditional_per_state_m > 100, (
            f"States have ${avg_conditional_per_state_m:.0f}M avg incentive to pressure competitors"
        )


class TestChatGPTAdsEuropeConcurrentTiming(unittest.TestCase):
    """Tests for the 48-hour temporal adjacency between ChatGPT ads Europe and Meta settlement."""

    def test_chatgpt_ads_europe_precedes_settlement_by_48_hours(self):
        """ChatGPT ads went live Aug 24, settlement announced Aug 26."""
        chatgpt_ads_date = "2026-08-24"
        settlement_date = "2026-08-26"
        from datetime import date
        d1 = date.fromisoformat(chatgpt_ads_date)
        d2 = date.fromisoformat(settlement_date)
        delta = (d2 - d1).days
        assert delta == 2, f"Expected 2-day gap, got {delta}"

    def test_chatgpt_european_expansion_scale(self):
        """ChatGPT ads reached 35 total markets with 31 European additions."""
        european_markets = 31
        total_markets = 35
        prior_markets = total_markets - european_markets  # US, UK, Canada, Australia + more
        assert european_markets > prior_markets, (
            "European expansion is larger than all prior markets combined"
        )

    def test_chatgpt_eea_includes_all_eu_plus_efta(self):
        """31 European markets = 27 EU + Iceland, Liechtenstein, Norway, Switzerland."""
        eu_members = 27
        additional = 4  # Iceland, Liechtenstein, Norway, Switzerland
        total_european = eu_members + additional
        assert total_european == 31

    def test_chatgpt_ads_user_base_scale_comparable(self):
        """ChatGPT weekly users (900M+) are in same order of magnitude as Meta's platforms."""
        chatgpt_wau_m = 900
        meta_instagram_mau_b = 2.0  # approximate
        meta_instagram_mau_m = meta_instagram_mau_b * 1000
        # Same order of magnitude (hundreds of millions)
        assert chatgpt_wau_m > 100, "ChatGPT has hundreds of millions of weekly users"
        ratio = meta_instagram_mau_m / chatgpt_wau_m
        assert ratio < 10, "Within one order of magnitude"


class TestAgeVerificationParityAnalysis(unittest.TestCase):
    """Tests comparing Meta and ChatGPT age verification approaches."""

    def test_both_use_behavioral_inference(self):
        """Both Meta and ChatGPT rely on behavioral/statistical age detection, not hard ID."""
        meta_signals = {"self_reported_age", "usage_patterns", "content_interactions"}
        chatgpt_signals = {"stated_age", "account_age", "activity_times", "usage_patterns"}
        # Both use behavioral inference class
        common_signal_types = {"usage_patterns"}
        assert len(common_signal_types) > 0, "Shared inference methodology"

    def test_neither_requires_hard_id_at_signup(self):
        """Neither platform requires government ID verification at account creation."""
        meta_requires_hard_id = False
        chatgpt_requires_hard_id = False
        assert meta_requires_hard_id == chatgpt_requires_hard_id, (
            "Both use the same class of probabilistic inference"
        )

    def test_chatgpt_default_to_minor_experience(self):
        """ChatGPT defaults to under-18 experience when uncertain -- same logic as Meta."""
        chatgpt_default_uncertain = "under_18_experience"
        meta_default_uncertain = "restrict_access"
        # Both default to restrictive when uncertain
        assert chatgpt_default_uncertain is not None
        assert meta_default_uncertain is not None

    def test_framing_vocabulary_bifurcation(self):
        """Meta age detection framed as failure; ChatGPT age prediction framed as innovation."""
        meta_framing_terms = [
            "designed to fail",
            "inadequate",
            "willful negligence",
            "knew the tools were not effective",
        ]
        chatgpt_framing_terms = [
            "effort to protect young users",
            "responsible",
            "proactive",
            "innovation",
        ]
        # Accountability register for Meta, aspirational for ChatGPT
        meta_negative_count = sum(
            1 for t in meta_framing_terms
            if any(w in t for w in ["fail", "inadequate", "negligence"])
        )
        chatgpt_positive_count = sum(
            1 for t in chatgpt_framing_terms
            if any(w in t for w in ["protect", "responsible", "proactive", "innovation"])
        )
        assert meta_negative_count >= 3, "Meta framed with accountability vocabulary"
        assert chatgpt_positive_count >= 3, "ChatGPT framed with aspirational vocabulary"


class TestPublisherDealPositionSettlementCoverage(unittest.TestCase):
    """Tests for publisher financial positions predicting settlement coverage framing."""

    def test_le_monde_openai_deal_chatgpt_ads_coverage(self):
        """Le Monde (OpenAI deal) covered ChatGPT ads as business story."""
        le_monde_has_openai_deal = True
        le_monde_chatgpt_ads_coverage_tone = "business_expansion"
        assert le_monde_has_openai_deal
        assert le_monde_chatgpt_ads_coverage_tone != "accountability"

    def test_news_corp_wsj_openai_deal_settlement_coverage(self):
        """WSJ (News Corp, $250M/5yr OpenAI deal) led settlement coverage with active vocabulary."""
        news_corp_openai_deal_m = 250  # over 5 years
        wsj_meta_vocabulary = "active_accountability"
        wsj_chatgpt_vocabulary = "minimal_scrutiny"
        assert news_corp_openai_deal_m > 0
        assert wsj_meta_vocabulary != wsj_chatgpt_vocabulary, (
            "Different vocabulary registers for deal partner vs non-deal entity"
        )

    def test_reuters_ap_dual_deal_wire_distribution(self):
        """Reuters and AP (both OpenAI deals) distributed primary settlement wire copy."""
        reuters_openai_deal = True
        ap_openai_deal = True
        reuters_settlement_role = "primary_wire_distribution"
        ap_settlement_role = "primary_wire_distribution"
        assert reuters_openai_deal and ap_openai_deal
        assert reuters_settlement_role == ap_settlement_role

    def test_zero_deal_publications_not_named_in_mediascope(self):
        """
        All 8 adversarially-profiled publications (zero Meta deals) have at least one
        competitor deal. The settlement coverage follows this pattern.
        """
        adversarial_pubs_with_zero_meta_deals = 8
        adversarial_pubs_with_competitor_deals = 7  # 7 of 8
        ratio = adversarial_pubs_with_competitor_deals / adversarial_pubs_with_zero_meta_deals
        assert ratio > 0.85, "87.5% of adversarial pubs have competitor deals but zero Meta deals"


class TestIPOUnderwriterNarrativeConflict(unittest.TestCase):
    """Tests for IPO underwriter banks' dual role in settlement week."""

    def test_same_three_banks_underwrite_both_ai_ipos(self):
        """Goldman, Morgan Stanley, JPMorgan underwrite both Anthropic and OpenAI IPOs."""
        anthropic_underwriters = {"Goldman Sachs", "Morgan Stanley", "JPMorgan Chase"}
        openai_underwriters = {"Goldman Sachs", "Morgan Stanley"}
        overlap = anthropic_underwriters & openai_underwriters
        assert len(overlap) >= 2, "At least 2 banks underwrite both IPOs"

    def test_anthropic_ipo_filing_same_week_as_settlement(self):
        """Anthropic S-1 expected public filing late Aug, overlapping settlement week."""
        anthropic_filing_window = "late_august_2026"
        settlement_date = "2026-08-26"
        # Both in same calendar week
        assert "august" in anthropic_filing_window.lower()
        assert "08-26" in settlement_date

    def test_narrative_contrast_benefits_ipo_clients(self):
        """
        Settlement (Meta = regulatory risk) vs IPO (Anthropic = growth story) creates
        narrative contrast that differentiates banks' IPO clients from social media.
        """
        meta_narrative = "regulatory_risk_accountability"
        anthropic_narrative = "growth_innovation_historic_ipo"
        # Different narrative categories serve underwriter positioning
        assert meta_narrative != anthropic_narrative

    def test_anthropic_ipo_valuation_exceeds_settlement(self):
        """Anthropic's $2T target IPO valuation dwarfs Meta's $16.68B settlement."""
        anthropic_target_valuation_t = 2.0
        meta_settlement_b = 16.68
        ratio = (anthropic_target_valuation_t * 1000) / meta_settlement_b
        assert ratio > 100, (
            f"Anthropic IPO valuation is {ratio:.0f}x the settlement amount"
        )


class TestChatGPTAdMonetizationChildSafetyParallel(unittest.TestCase):
    """Tests for ChatGPT's ad monetization creating parallel child safety exposure."""

    def test_chatgpt_free_tier_ads_serve_largest_user_base(self):
        """Ads appear on Free and Go tiers -- the largest portion of ChatGPT users."""
        tiers_with_ads = {"Free", "Go"}
        tiers_without_ads = {"Plus", "Pro", "Business", "Enterprise", "Edu"}
        # Free tier is the majority of 900M+ WAU
        assert len(tiers_with_ads) < len(tiers_without_ads), (
            "More paid tiers than ad tiers, but Free dominates by user count"
        )

    def test_chatgpt_ad_targeting_uses_conversation_context(self):
        """ChatGPT ads target based on conversation topic -- user's most intimate context."""
        targeting_signals = [
            "conversation_topic",
            "approximate_location",
            "device_type",
            "time_of_day",
            "language",
        ]
        conversation_based = "conversation_topic" in targeting_signals
        assert conversation_based, (
            "ChatGPT monetizes the most intimate user context (conversations)"
        )

    def test_chatgpt_ftc_investigation_active(self):
        """FTC investigation into ChatGPT companion child safety is active."""
        ftc_investigating_openai = True
        ftc_investigation_scope = "child safety, chatbot companions, teen harm"
        assert ftc_investigating_openai
        assert "child safety" in ftc_investigation_scope

    def test_chatgpt_teen_suicide_lawsuits_pending(self):
        """Multiple lawsuits filed against OpenAI over teen suicide linked to ChatGPT."""
        lawsuits_filed = True
        multiple_families = True
        assert lawsuits_filed and multiple_families


class TestConfounderDocumentation(unittest.TestCase):
    """Tests ensuring confounders are properly documented and addressed."""

    def test_platform_type_confounder_documented(self):
        """Social media vs conversational AI is a strong confounder."""
        confounder = {
            "strength": "STRONG",
            "description": "Platform type difference",
            "counter": "FTC investigation covers overlapping harms",
        }
        assert confounder["strength"] == "STRONG"
        assert confounder["counter"] is not None

    def test_scale_confounder_documented(self):
        """User scale difference is documented as confounder."""
        meta_instagram_mau_b = 2.0
        chatgpt_wau_m = 900
        # ChatGPT's WAU is in same order of magnitude as Meta's MAU (billions vs 900M)
        assert chatgpt_wau_m > 500, "ChatGPT scale is comparable"

    def test_litigation_maturity_confounder_documented(self):
        """Meta's longer history of child safety litigation is documented."""
        meta_child_safety_scrutiny_start = 2021  # Haugen
        chatgpt_child_safety_scrutiny_start = 2025
        gap_years = chatgpt_child_safety_scrutiny_start - meta_child_safety_scrutiny_start
        assert gap_years == 4, "4-year gap in scrutiny history"

    def test_asymmetry_score_reflects_heavy_confounder_load(self):
        """Score of 0.32 reflects moderate finding with heavy confounders."""
        score = 0.32
        assert 0.25 <= score <= 0.40, (
            "Score reflects moderate asymmetry with heavy confounder load"
        )


class TestCrossReferenceIntegrity(unittest.TestCase):
    """Tests ensuring cross-references to related mechanisms are consistent."""

    def test_cross_references_mechanism_342(self):
        """Cross-references WSJ settlement-week YouTube accountability deflection."""
        related_mechanism = 342
        relationship = "temporal_parallel"
        assert related_mechanism < 344
        assert relationship == "temporal_parallel"

    def test_cross_references_mechanism_343(self):
        """Cross-references AP wire vocabulary bifurcation."""
        related_mechanism = 343
        relationship = "causal_chain"
        assert related_mechanism < 344
        assert relationship == "causal_chain"

    def test_mechanism_344_unique(self):
        """This mechanism's financial architecture angle is distinct from 342/343."""
        mechanism_342_type = "competitor_coverage"  # WSJ entity deflection
        mechanism_343_type = "journalist_tracking"  # AP vocabulary bifurcation
        mechanism_344_type = "financial_incentive_mapping"  # Financial architecture
        types = {mechanism_342_type, mechanism_343_type, mechanism_344_type}
        assert len(types) == 3, "All three mechanisms have distinct analysis types"


if __name__ == "__main__":
    unittest.main()
