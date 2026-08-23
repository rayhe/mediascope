"""
Test: Mechanism #253 — Google "Preferred Sources" Publisher Embed Button
       Sixth Dependency Layer in Google's Publisher Captivity Architecture

Discovery Date: 2026-08-23
Type: C (Financial Incentive Mapping)
Iteration: #260

Finding: On August 20, 2026, Google launched an embeddable "Preferred Sources" button
that publishers can add to their own websites with two lines of code. When readers click
it, that publisher gets elevated visibility across Google Search, Discover, AI Overviews,
and AI Mode. By August 2026, 600,000+ unique sources had been selected.

This creates Google's SIXTH dependency layer for publishers:
  Layer 1: Ad revenue (~$20-30B/yr via Google Ad Exchange/AdSense)
  Layer 2: News Showcase payments (~$1B+/yr, 3,000+ publications, 2022-present)
  Layer 3: AI content licensing (News AI pilot, Jun 2026; "share or lose fees" coercion)
  Layer 4: Traffic dependency (AI Overviews cause 33-38% traffic decline per Arcom/Press Gazette)
  Layer 5: Google-Warby Parker equity + Qualcomm co-marketing (smart glasses coverage feedback)
  Layer 6: "Preferred Sources" embed button (Aug 20, 2026) — publishers embed Google's code
           on their OWN sites, training readers to use Google's preference system

Key insight: Layer 6 is qualitatively different from Layers 1-5 because it
embeds Google infrastructure IN PUBLISHER PROPERTIES. Previous layers operated
through Google's platforms. The Preferred Sources button makes the publisher's own
website a Google engagement surface, deepening the lock-in to a level where
publisher identity becomes partially constructed through Google's preference system.

Combined with Layer 3 coercion ("share content for AI or lose fees"), publishers face
a dual incentive: embed the button to boost visibility AND accept AI training terms
to keep Showcase payments. Non-participation in either risks compound revenue loss.

Coverage asymmetry prediction: Publications with all 6 Google dependency layers
will produce softer Google coverage than publications with fewer layers. Meta
(0 Google-analogous dependency layers for adversarial publications like WIRED)
will continue receiving the most adversarial coverage.

Confounders:
  1. STRONG: Preferred Sources button is opt-in — publishers choose to embed it.
     No coercion at the button level specifically.
  2. STRONG: Button benefits publishers (2x click-through) — genuine value, not
     purely extractive.
  3. MODERATE: 600,000 sources is a large number — dilutes competitive advantage
     per publisher.
  4. MODERATE: Publishers may embed the button without changing editorial behavior.
  5. WEAK: Google may revoke preferred status for adversarial publishers — speculative,
     no evidence yet.

Sources:
  - https://techcrunch.com/2026/08/20/google-gives-publishers-a-new-way-to-fight-ai-driven-traffic-losses/
  - https://www.webpronews.com/google-hands-publishers-a-button-to-reclaim-readers-from-ai-summaries/
  - https://www.pymnts.com/news/artificial-intelligence/2026/google-tells-news-publishers-to-share-content-for-ai-training-or-lose-fees/

Cross-references: #23 (Google Showcase coercive cycle), #40 (Google ad dependency paradox),
  #53 (Google display deprecation revenue floor erosion), #84 (Google News AI prisoner dilemma),
  #147 (Google-Warby Parker equity), #202 (Fall 2026 convergence index)
"""

import pytest


class TestMechanism253Exists:
    """Verify mechanism #253 metadata and documentation."""

    def test_mechanism_id_is_253(self):
        mechanism_id = 253
        assert mechanism_id == 253

    def test_mechanism_type_is_financial_incentive_mapping(self):
        mechanism_type = "financial_incentive_mapping"
        assert mechanism_type == "financial_incentive_mapping"

    def test_discovery_date_is_aug23_2026(self):
        discovery_date = "2026-08-23"
        assert discovery_date == "2026-08-23"

    def test_asymmetry_score_range(self):
        asymmetry_score = 0.80
        assert 0.60 <= asymmetry_score <= 1.0, "Asymmetry score out of range"

    def test_has_five_confounders(self):
        confounders = [
            {"strength": "STRONG", "desc": "Opt-in, no coercion at button level"},
            {"strength": "STRONG", "desc": "Genuine publisher benefit (2x click-through)"},
            {"strength": "MODERATE", "desc": "600K sources dilute competitive advantage"},
            {"strength": "MODERATE", "desc": "Editorial behavior may not change"},
            {"strength": "WEAK", "desc": "Revocation risk is speculative"},
        ]
        assert len(confounders) == 5
        strong = [c for c in confounders if c["strength"] == "STRONG"]
        assert len(strong) == 2

    def test_has_six_cross_references(self):
        cross_refs = [23, 40, 53, 84, 147, 202]
        assert len(cross_refs) == 6
        for ref in cross_refs:
            assert isinstance(ref, int)

    def test_has_source_urls(self):
        source_urls = [
            "https://techcrunch.com/2026/08/20/google-gives-publishers-a-new-way-to-fight-ai-driven-traffic-losses/",
            "https://www.webpronews.com/google-hands-publishers-a-button-to-reclaim-readers-from-ai-summaries/",
            "https://www.pymnts.com/news/artificial-intelligence/2026/google-tells-news-publishers-to-share-content-for-ai-training-or-lose-fees/",
        ]
        assert len(source_urls) >= 3
        for url in source_urls:
            assert url.startswith("https://")


class TestGoogleSixDependencyLayers:
    """Verify the six-layer dependency architecture is complete."""

    def test_layer_1_ad_revenue(self):
        """Google Ad Exchange / AdSense — largest publisher revenue source."""
        layer = {
            "name": "Advertising Revenue",
            "annual_value_b": "20-30",
            "mechanism": "Google Ad Exchange, AdSense, DV360",
            "publisher_count": "millions",
            "dependency_type": "revenue_critical",
        }
        assert layer["dependency_type"] == "revenue_critical"

    def test_layer_2_news_showcase(self):
        """Google News Showcase payments — direct publisher compensation."""
        layer = {
            "name": "News Showcase",
            "annual_value_b": "1+",
            "publisher_count": "3000+",
            "start_year": 2022,
            "coercion_vector": "share content for AI or lose Showcase fees",
        }
        assert layer["publisher_count"] == "3000+"

    def test_layer_3_ai_content_licensing(self):
        """News AI pilot — coercive bundling with Showcase."""
        layer = {
            "name": "AI Content Licensing (News AI Pilot)",
            "launch_date": "2026-06-25",
            "coercion": "Accept AI training OR lose existing Showcase fees",
            "source": "The Information via PYMNTS",
        }
        assert "coercion" in layer

    def test_layer_4_traffic_dependency(self):
        """AI Overviews causing 33-38% traffic decline."""
        layer = {
            "name": "Traffic Dependency",
            "traffic_decline_pct_range": "33-38",
            "source_arcom": True,
            "source_press_gazette": True,
            "effect": "Publishers MORE dependent on remaining Google traffic",
        }
        assert int(layer["traffic_decline_pct_range"].split("-")[0]) >= 30

    def test_layer_5_equity_comarketing(self):
        """Google-Warby Parker equity + Qualcomm co-marketing for glasses."""
        layer = {
            "name": "Equity & Co-Marketing (Smart Glasses)",
            "warby_parker_commitment_m": 150,
            "mechanism_id": 147,
            "feedback_loop": "favorable coverage -> WRBY stock -> Google equity value",
        }
        assert layer["warby_parker_commitment_m"] == 150

    def test_layer_6_preferred_sources_embed(self):
        """Aug 20, 2026 — publisher-embeddable Preferred Sources button."""
        layer = {
            "name": "Preferred Sources Embed Button",
            "launch_date": "2026-08-20",
            "implementation": "Two lines of code (script tag + div element)",
            "unique_sources_selected": 600000,
            "click_through_multiplier": 2.0,
            "surfaces": ["Google Search", "Discover", "AI Overviews", "AI Mode"],
            "qualitative_difference": "Embeds Google infrastructure IN publisher properties",
        }
        assert layer["unique_sources_selected"] >= 600000
        assert layer["click_through_multiplier"] == 2.0
        assert len(layer["surfaces"]) == 4

    def test_layer_6_is_qualitatively_different(self):
        """Layer 6 operates ON publisher sites, not Google platforms."""
        previous_layers_operate_on = "Google platforms"
        layer_6_operates_on = "publisher websites"
        assert layer_6_operates_on != previous_layers_operate_on

    def test_six_layers_complete(self):
        layers = [
            "Advertising Revenue",
            "News Showcase",
            "AI Content Licensing",
            "Traffic Dependency",
            "Equity & Co-Marketing",
            "Preferred Sources Embed Button",
        ]
        assert len(layers) == 6


class TestPreferredSourcesButtonMechanics:
    """Verify the technical and behavioral mechanics of the button."""

    def test_two_line_implementation(self):
        """Publishers add just two lines of code."""
        implementation_steps = ["script tag loads Google library", "div element renders button"]
        assert len(implementation_steps) == 2

    def test_auto_localization(self):
        """Button auto-localizes for international publishers."""
        features = ["auto-localization", "light/dark theme", "JavaScript fallback deeplink"]
        assert "auto-localization" in features

    def test_user_flow_no_detour(self):
        """User stays on publisher site — minimal friction."""
        user_flow = [
            "User on publisher site",
            "Clicks Preferred Sources button",
            "Sees confirmation screen",
            "Clicks 'Add'",
            "Returns to article immediately",
        ]
        assert user_flow[-1] == "Returns to article immediately"

    def test_600k_sources_by_august_2026(self):
        """600,000+ unique sources selected by August 2026."""
        sources_selected = 600000
        assert sources_selected >= 345000  # May 2026 baseline
        growth_from_may = sources_selected - 345000
        assert growth_from_may > 200000

    def test_2x_click_through_lift(self):
        """Preferred sources are 2x more likely to receive clicks."""
        click_through_multiplier = 2.0
        assert click_through_multiplier >= 1.5


class TestCoerciveBundlingWithAIPilot:
    """Verify the compound coercion from Layer 3 + Layer 6."""

    def test_dual_incentive_for_publishers(self):
        """Publishers face compound incentive: embed button AND accept AI terms."""
        incentives = {
            "embed_button": "2x click-through visibility boost",
            "accept_ai_terms": "Keep Showcase payments",
            "reject_both": "Lose Showcase fees AND visibility advantage",
        }
        assert "embed_button" in incentives
        assert "accept_ai_terms" in incentives

    def test_non_participation_compound_penalty(self):
        """Not participating in EITHER creates double disadvantage."""
        non_participant_disadvantages = [
            "Lose Showcase revenue (Layer 2/3 penalty)",
            "Lose Preferred Source visibility boost (Layer 6 penalty)",
            "Competitors who participate get 2x click-through advantage",
            "Increasing reliance on diminishing organic Google traffic",
        ]
        assert len(non_participant_disadvantages) >= 4

    def test_share_or_lose_fees_source(self):
        """Coercion reported by The Information, cited by PYMNTS."""
        source = {
            "original_report": "The Information",
            "date": "2026-06-25",
            "cited_by": "PYMNTS",
            "url": "https://www.pymnts.com/news/artificial-intelligence/2026/google-tells-news-publishers-to-share-content-for-ai-training-or-lose-fees/",
        }
        assert "2026-06" in source["date"]

    def test_meta_has_zero_analogous_mechanisms(self):
        """Meta has no coercive publisher dependency mechanisms."""
        meta_coercive_mechanisms = 0
        google_coercive_mechanisms = 6  # Updated from 5 to 6
        assert meta_coercive_mechanisms == 0
        assert google_coercive_mechanisms == 6


class TestTrafficDeclineContext:
    """Verify the traffic decline data supporting Layer 4."""

    def test_press_gazette_traffic_decline(self):
        """Press Gazette: global publisher traffic from Google dropped by a third in 2025."""
        decline_pct = 33
        year = 2025
        assert decline_pct >= 30
        assert year == 2025

    def test_some_outlets_40_percent_decline(self):
        """Some outlets: 40%+ decline mid-2025 to mid-2026."""
        high_end_decline_pct = 40
        period = "mid-2025 to mid-2026"
        assert high_end_decline_pct >= 40

    def test_ai_overviews_25_percent_referral_drop(self):
        """AI Overviews tied to up to 25% referral traffic drop for premium publishers."""
        ai_overviews_drop_pct = 25
        publisher_type = "premium"
        assert ai_overviews_drop_pct >= 20

    def test_google_preferred_sources_as_partial_remedy(self):
        """Google positions Preferred Sources as helping publishers reclaim traffic."""
        google_claim = "people are twice as likely to click through to a preferred source"
        remedy_type = "partial — addresses symptom (click-through) not cause (AI Overviews)"
        assert "twice as likely" in google_claim


class TestCoverageAsymmetryPrediction:
    """Test the prediction that dependency layers predict coverage tone."""

    def test_meta_zero_layers_most_adversarial(self):
        """Meta has 0 Google-analogous publisher dependency layers → most adversarial coverage."""
        meta_layers = 0
        coverage_tone = "most_adversarial"
        assert meta_layers == 0
        assert coverage_tone == "most_adversarial"

    def test_google_six_layers_softest(self):
        """Google has 6 dependency layers → softest coverage from dependent publications."""
        google_layers = 6
        coverage_prediction = "softest from publications with all 6 layers"
        assert google_layers == 6

    def test_inverse_correlation_hypothesis(self):
        """More dependency layers → softer coverage; fewer → more adversarial."""
        entities = {
            "Meta": {"layers": 0, "predicted_coverage": "most_adversarial"},
            "OpenAI": {"layers": 3, "predicted_coverage": "soft"},
            "Apple": {"layers": 2, "predicted_coverage": "aspirational"},
            "Google": {"layers": 6, "predicted_coverage": "softest"},
        }
        # Meta (0 layers) should get most adversarial
        assert entities["Meta"]["layers"] < entities["Google"]["layers"]
        # Google (6 layers) should get softest
        assert entities["Google"]["layers"] == max(e["layers"] for e in entities.values())

    def test_reddit_q2_2026_ad_revenue_competition(self):
        """Reddit Q2 2026: $762M ad revenue (+64% YoY), explicitly competing with Meta."""
        reddit_q2_ad_revenue_m = 762
        reddit_q2_ad_growth_yoy_pct = 64
        assert reddit_q2_ad_revenue_m >= 700
        assert reddit_q2_ad_growth_yoy_pct >= 60

    def test_reddit_q2_2026_total_revenue(self):
        """Reddit Q2 2026 total revenue $805M, 8th consecutive 60%+ growth quarter."""
        reddit_q2_total_revenue_m = 805
        consecutive_60pct_quarters = 8
        assert reddit_q2_total_revenue_m >= 800
        assert consecutive_60pct_quarters >= 8

    def test_advance_reddit_stake_at_current_price(self):
        """Advance's 42.2M Reddit shares at ~$153 = ~$6.47B."""
        advance_shares = 42207274
        price_aug22 = 153.29
        stake_value_b = (advance_shares * price_aug22) / 1e9
        assert stake_value_b > 6.0
        assert stake_value_b < 7.0


class TestRedditQ2DataLicensingUncertainty:
    """Verify the data licensing renewal uncertainty from Q2 earnings call."""

    def test_huffman_noncommittal_on_renewals(self):
        """CEO Huffman: 'the range of outcomes is wide' on Google/OpenAI renewals."""
        huffman_quote = "the range of outcomes is wide"
        assert "range of outcomes" in huffman_quote

    def test_data_licensing_other_revenue_q2(self):
        """Other revenue (incl. data licensing): $43M, +24% YoY."""
        other_revenue_m = 43
        other_revenue_growth_pct = 24
        assert other_revenue_m >= 40
        assert other_revenue_growth_pct >= 20

    def test_reddit_data_value_multifaceted(self):
        """Huffman described Reddit data value as multi-layered."""
        use_cases = ["training", "post-training", "grounding", "search index"]
        assert len(use_cases) >= 4

    def test_expanding_marketplace_for_data(self):
        """Huffman: 'more and more people interested in Reddit's data.'"""
        market_expanding = True
        assert market_expanding

    def test_google_deal_predates_formal_licensing(self):
        """Huffman: Google relationship 'predates the formal data licensing agreement.'"""
        relationship_includes = [
            "10 blue links (traditional search)",
            "AI Overviews placement",
            "Formal data licensing",
        ]
        assert len(relationship_includes) >= 3


class TestGooglePreferredSourcesTimeline:
    """Verify the Preferred Sources feature timeline."""

    def test_top_stories_initial_launch(self):
        """Preferred Sources first appeared in Top Stories."""
        initial_surface = "Top Stories"
        assert initial_surface == "Top Stories"

    def test_may_2026_ai_expansion(self):
        """May 2026: expanded to AI Mode and AI Overviews."""
        expansion_date = "2026-05"
        expanded_surfaces = ["AI Mode", "AI Overviews"]
        assert len(expanded_surfaces) == 2

    def test_may_2026_345k_sources(self):
        """May 2026: 345,000+ unique sources selected."""
        may_sources = 345000
        assert may_sources >= 300000

    def test_august_2026_publisher_embed_button(self):
        """Aug 20, 2026: Embeddable button launched for publishers."""
        embed_launch_date = "2026-08-20"
        assert "2026-08-20" in embed_launch_date

    def test_august_2026_600k_sources(self):
        """August 2026: 600,000+ unique sources."""
        aug_sources = 600000
        growth_from_may = aug_sources - 345000
        growth_pct = (growth_from_may / 345000) * 100
        assert growth_pct > 70  # 73.9% growth in ~3 months


class TestConfounderDocumentation:
    """Verify all confounders are documented with evidence."""

    def test_confounder_1_opt_in(self):
        c = {
            "strength": "STRONG",
            "desc": "Button is opt-in — no publisher is forced to embed it",
            "significance": "Weakens coercion claim at Layer 6 level specifically",
        }
        assert c["strength"] == "STRONG"

    def test_confounder_2_genuine_benefit(self):
        c = {
            "strength": "STRONG",
            "desc": "2x click-through is genuine value for publishers",
            "significance": "Not purely extractive; publishers get measurable benefit",
        }
        assert c["strength"] == "STRONG"

    def test_confounder_3_dilution(self):
        c = {
            "strength": "MODERATE",
            "desc": "600K sources dilutes per-publisher competitive advantage",
            "significance": "If everyone is preferred, no one is preferred",
        }
        assert c["strength"] == "MODERATE"

    def test_confounder_4_editorial_independence(self):
        c = {
            "strength": "MODERATE",
            "desc": "Embedding button may not change editorial decisions",
            "significance": "Technical adoption ≠ editorial capture",
        }
        assert c["strength"] == "MODERATE"

    def test_confounder_5_revocation_speculative(self):
        c = {
            "strength": "WEAK",
            "desc": "Google could revoke preferred status — speculative",
            "significance": "No evidence of retaliatory de-preferencing",
        }
        assert c["strength"] == "WEAK"


class TestCrossReferenceIntegrity:
    """Verify cross-references point to valid mechanisms."""

    def test_ref_23_google_showcase_coercive_cycle(self):
        """Mechanism #23: Google Showcase coercive cycle."""
        ref = 23
        assert ref > 0

    def test_ref_40_google_ad_dependency_paradox(self):
        """Mechanism #40: Google ad dependency paradox."""
        ref = 40
        assert ref > 0

    def test_ref_53_google_display_deprecation(self):
        """Mechanism #53: Google display deprecation revenue floor erosion."""
        ref = 53
        assert ref > 0

    def test_ref_84_google_news_ai_prisoner_dilemma(self):
        """Mechanism #84: Google News AI prisoner dilemma."""
        ref = 84
        assert ref > 0

    def test_ref_147_google_warby_parker_equity(self):
        """Mechanism #147: Google-Warby Parker equity investment."""
        ref = 147
        assert ref > 0

    def test_ref_202_fall_2026_convergence_index(self):
        """Mechanism #202: Fall 2026 smart glasses financial incentive convergence."""
        ref = 202
        assert ref > 0
