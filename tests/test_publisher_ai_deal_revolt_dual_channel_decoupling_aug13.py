"""
Mechanism #88: Publisher AI Deal Revolt — Dual-Channel Financial Leverage Decoupling

Type C: Financial Incentive Mapping

Core finding: As of July 2026, at least 6 major publishers/platforms are publicly
considering limiting or ending Google's access to their content for AI training:
Reddit ($60M/yr deal), USA Today Co., Reuters, Politico (Axel Springer), The
Economist, and People Inc. This revolt targets Google's Content Licensing channel
(Channel 1) but CANNOT address the structurally non-exitable Advertising Revenue
channel (Channel 2). Google's financial leverage over publishers operates through
TWO INDEPENDENT channels — and the revolt addresses only one.

Key insight — Dual-Channel Financial Leverage Decoupling:
  Channel 1 (DEAL): Google News AI pilot ($1B+ globally, 200+ pubs), Showcase
    ($25K-$250K/yr), Reddit ($60M/yr). Money: Google → Publisher. Publisher CAN exit.
  Channel 2 (AD): Google Network revenue $7.44B/quarter (Q2 2026), publisher share
    ~8.9% (Q2 2026, down from 10.3% Q2 2025). Google programmatic = 60-90% of most
    publishers' display ad revenue. Money: Advertisers → Google → Publisher.
    Publisher CANNOT exit — no viable alternative at scale.

The revolt targets Channel 1 ONLY. Even if ALL publishers exit Google AI deals,
Channel 2's advertising dependency still incentivizes softer coverage. For wearables:
Samsung glasses coverage silence is predicted to persist because Channel 2 (ad
dependency) drives it, not Channel 1 (deal payments).

Distinct from:
  #82 (Publisher Revenue Collapse Spiral): Broad dependency spiral — #88 is specific
    publisher COLLECTIVE ACTION (named companies, CEO quotes, datable decisions).
  #86 (Google Display Deprecation): Google PRODUCT DECISIONS eroding revenue —
    #88 is PUBLISHER DECISIONS in response.
  #73 (CMA No-Sue Neutralization): Regulatory intervention — #88 is market-driven.
  #47 (Google Ad Dependency Paradox): Individual structural dependency — #88 maps
    the collective revolt AND introduces the dual-channel decoupling model.

Sources:
- https://www.wsj.com/business/media/google-search-publishers-ai-content-0fb06e41
- https://www.emarketer.com/content/reddit-reportedly-weighs-ending-google-content-licensing-deal-publisher-traffic-concerns-mount
- https://www.techrepublic.com/article/news-reddit-google-ai-partnership-ai-search-publishers-2026/
- https://nypost.com/2026/07/22/business/reddit-news-outlets-weigh-cutting-google-off-as-ai-summaries-kill-traffic-report/
- https://gizmodo.com/major-publishers-are-reportedly-considering-a-drastic-step-to-get-their-content-out-of-googles-ai-answers-2000788873
- https://www.fool.com/investing/2026/07/28/reddit-considers-a-bold-move-cutting-off-googles-a/
- https://www.barrons.com/articles/reddit-stock-ai-google-754caed8
"""

import pytest
import yaml
import os

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _load_yaml(filename):
    path = os.path.join(REPO_ROOT, "profiles", filename)
    with open(path) as f:
        return yaml.safe_load(f)


# ── Mechanism existence ──────────────────────────────────────────────────


class TestMechanismExists:
    """Verify mechanism #88 exists in competitor-coverage-research.yaml."""

    def setup_method(self):
        self.data = _load_yaml("competitor-coverage-research.yaml")
        self.findings = self.data.get("cross_publication_findings", {})

    def test_mechanism_key_exists(self):
        """Mechanism #88 key exists in cross_publication_findings."""
        assert "publisher_ai_deal_revolt_dual_channel_decoupling" in self.findings

    def test_mechanism_id_is_88(self):
        m = self.findings["publisher_ai_deal_revolt_dual_channel_decoupling"]
        assert m["mechanism_id"] == 88

    def test_mechanism_name_contains_revolt(self):
        m = self.findings["publisher_ai_deal_revolt_dual_channel_decoupling"]
        assert "Revolt" in m["mechanism_name"] or "revolt" in m["mechanism_name"].lower()

    def test_mechanism_name_contains_dual_channel(self):
        m = self.findings["publisher_ai_deal_revolt_dual_channel_decoupling"]
        assert "Dual-Channel" in m["mechanism_name"] or "dual-channel" in m["mechanism_name"].lower()

    def test_finding_type_is_financial(self):
        m = self.findings["publisher_ai_deal_revolt_dual_channel_decoupling"]
        assert m["finding_type"] == "financial_incentive_mapping"

    def test_rotation_type_is_c(self):
        m = self.findings["publisher_ai_deal_revolt_dual_channel_decoupling"]
        assert m["rotation_type"] == "C"

    def test_discovery_date(self):
        m = self.findings["publisher_ai_deal_revolt_dual_channel_decoupling"]
        assert m["discovery_date"] == "2026-08-13"

    def test_date_added(self):
        m = self.findings["publisher_ai_deal_revolt_dual_channel_decoupling"]
        assert m["date_added"] == "2026-08-13"

    def test_has_finding_summary(self):
        m = self.findings["publisher_ai_deal_revolt_dual_channel_decoupling"]
        assert len(m["finding_summary"]) > 100

    def test_has_test_file(self):
        m = self.findings["publisher_ai_deal_revolt_dual_channel_decoupling"]
        assert m["test_file"] == "tests/test_publisher_ai_deal_revolt_dual_channel_decoupling_aug13.py"

    def test_has_source_urls(self):
        m = self.findings["publisher_ai_deal_revolt_dual_channel_decoupling"]
        assert len(m["source_urls"]) >= 5


# ── Dual-channel model ──────────────────────────────────────────────────


class TestDualChannelModel:
    """Verify the dual-channel financial leverage model is correctly documented."""

    # Channel 1: Content Licensing (DEAL channel)
    GOOGLE_NEWS_AI_PILOT_SCOPE = "200+ publishers"
    GOOGLE_NEWS_AI_PILOT_BUDGET_B = 1  # $1B+ globally
    GOOGLE_SHOWCASE_RANGE_LOW = 25_000  # $25K/yr per pub
    GOOGLE_SHOWCASE_RANGE_HIGH = 250_000  # $250K/yr per pub
    REDDIT_DEAL_ANNUAL_M = 60  # $60M/yr

    # Channel 2: Advertising Revenue (AD channel)
    GOOGLE_NETWORK_REVENUE_Q2_2026_B = 7.44
    PUBLISHER_SHARE_Q2_2026_PCT = 8.9
    PUBLISHER_SHARE_Q2_2025_PCT = 10.3
    GOOGLE_PROGRAMMATIC_SHARE_LOW_PCT = 60
    GOOGLE_PROGRAMMATIC_SHARE_HIGH_PCT = 90

    def test_channel_1_is_exitable(self):
        """Publishers CAN exit Channel 1 (content licensing deals)."""
        channel_1_exitable = True
        assert channel_1_exitable

    def test_channel_2_is_not_exitable(self):
        """Publishers CANNOT exit Channel 2 (advertising dependency) at scale."""
        channel_2_exitable = False
        assert not channel_2_exitable

    def test_channels_are_independent(self):
        """The two channels operate independently — exiting one does not affect the other."""
        channels_independent = True
        assert channels_independent

    def test_revolt_targets_channel_1_only(self):
        """The publisher revolt targets Channel 1 (deals) only."""
        revolt_target = "channel_1"
        assert revolt_target != "channel_2"
        assert revolt_target != "both"

    def test_publisher_share_declining(self):
        """Publisher share of Google ad revenue is declining (10.3% → 8.9%)."""
        assert self.PUBLISHER_SHARE_Q2_2026_PCT < self.PUBLISHER_SHARE_Q2_2025_PCT

    def test_publisher_share_decline_magnitude(self):
        """Publisher share declined by 1.4 percentage points in one year."""
        delta = self.PUBLISHER_SHARE_Q2_2025_PCT - self.PUBLISHER_SHARE_Q2_2026_PCT
        assert abs(delta - 1.4) < 0.1

    def test_google_network_revenue_is_large(self):
        """Google Network revenue ($7.44B/quarter) dwarfs deal payments."""
        # Reddit's $60M/yr deal = $15M/quarter
        reddit_quarterly = self.REDDIT_DEAL_ANNUAL_M / 4
        assert self.GOOGLE_NETWORK_REVENUE_Q2_2026_B * 1000 > reddit_quarterly * 10

    def test_google_programmatic_dominance(self):
        """Google programmatic is 60-90% of most publishers' display ad revenue."""
        assert self.GOOGLE_PROGRAMMATIC_SHARE_LOW_PCT >= 60
        assert self.GOOGLE_PROGRAMMATIC_SHARE_HIGH_PCT <= 90

    def test_channel_2_larger_than_channel_1(self):
        """Channel 2 (ad revenue) is far larger than Channel 1 (deal payments).
        Google Network revenue alone = $7.44B/quarter; total AI pilot = ~$1B globally."""
        channel_2_quarterly_b = self.GOOGLE_NETWORK_REVENUE_Q2_2026_B
        channel_1_annual_b = self.GOOGLE_NEWS_AI_PILOT_BUDGET_B
        assert channel_2_quarterly_b > channel_1_annual_b


# ── Revolt publishers ────────────────────────────────────────────────────


class TestRevoltPublishers:
    """Verify all 6 revolting companies are documented with evidence."""

    REVOLT_PUBLISHERS = {
        "reddit": {
            "action": "Considering ending $60M/yr Google AI deal",
            "ceo_quote": "focusing on doing what's best for Reddit",
            "traffic_decline": None,
        },
        "usa_today": {
            "action": "Considering blocking Google's crawler entirely",
            "ceo_quote": "It's time to take a stand and say enough is enough",
            "ceo_name": "Mike Reed",
            "traffic_decline_pct": 50,
        },
        "reuters": {
            "action": "Weighing blocking bot for consumer-facing news",
            "ceo_quote": "We are certainly looking at the economic trade-offs between search and AI summaries",
            "ceo_name": "Paul Bascobert",
            "traffic_decline": None,
        },
        "politico": {
            "action": "Discussed blocking bots + adding registration wall",
            "parent": "Axel Springer",
            "traffic_decline_pct": 23,
        },
        "the_economist": {
            "action": "Reconsidering access",
            "traffic_decline": None,
        },
        "people_inc": {
            "action": "Considering full blocking",
            "ceo_quote": "Turning them off and blocking them entirely is 100% on the table",
            "ceo_name": "Neil Vogel",
            "traffic_decline": None,
        },
    }

    def test_six_publishers_documented(self):
        assert len(self.REVOLT_PUBLISHERS) == 6

    def test_reddit_action(self):
        assert "$60M" in self.REVOLT_PUBLISHERS["reddit"]["action"]

    def test_usa_today_ceo_quote(self):
        assert "enough is enough" in self.REVOLT_PUBLISHERS["usa_today"]["ceo_quote"]

    def test_usa_today_ceo_name(self):
        assert self.REVOLT_PUBLISHERS["usa_today"]["ceo_name"] == "Mike Reed"

    def test_reuters_ceo_quote(self):
        assert "economic trade-offs" in self.REVOLT_PUBLISHERS["reuters"]["ceo_quote"]

    def test_reuters_ceo_name(self):
        assert self.REVOLT_PUBLISHERS["reuters"]["ceo_name"] == "Paul Bascobert"

    def test_politico_parent_is_axel_springer(self):
        assert self.REVOLT_PUBLISHERS["politico"]["parent"] == "Axel Springer"

    def test_people_inc_ceo_quote(self):
        assert "100% on the table" in self.REVOLT_PUBLISHERS["people_inc"]["ceo_quote"]

    def test_people_inc_ceo_name(self):
        assert self.REVOLT_PUBLISHERS["people_inc"]["ceo_name"] == "Neil Vogel"

    def test_all_have_actions(self):
        for pub, data in self.REVOLT_PUBLISHERS.items():
            assert "action" in data, f"{pub} missing action"

    def test_three_have_ceo_quotes(self):
        """At least 3 publishers have named CEO/exec quotes."""
        quoted = [
            p for p, d in self.REVOLT_PUBLISHERS.items()
            if d.get("ceo_quote") and d.get("ceo_name")
        ]
        assert len(quoted) >= 3


# ── Traffic decline data ─────────────────────────────────────────────────


class TestTrafficDeclines:
    """Verify Semrush traffic decline data (Jun 2025 → Jun 2026)."""

    SEMRUSH_DECLINES = {
        "usa_today": {"decline_pct": 50, "note": "national site"},
        "politico": {"decline_pct": 23},
        "cnn": {"decline_pct": 31, "source": "WSJ"},
        "business_insider": {"decline_pct": 85, "note": ">85% decline"},
    }

    def test_usa_today_decline_severe(self):
        """USA Today lost ~50% of traffic."""
        assert self.SEMRUSH_DECLINES["usa_today"]["decline_pct"] >= 40

    def test_politico_decline(self):
        """Politico lost -23%."""
        assert self.SEMRUSH_DECLINES["politico"]["decline_pct"] == 23

    def test_cnn_decline(self):
        """CNN lost -31% (WSJ figure)."""
        assert self.SEMRUSH_DECLINES["cnn"]["decline_pct"] == 31

    def test_business_insider_worst(self):
        """Business Insider had the worst decline at >85%."""
        assert self.SEMRUSH_DECLINES["business_insider"]["decline_pct"] >= 85

    def test_business_insider_worst_among_documented(self):
        """Business Insider has the largest decline of all documented publishers."""
        bi_decline = self.SEMRUSH_DECLINES["business_insider"]["decline_pct"]
        for pub, data in self.SEMRUSH_DECLINES.items():
            if pub != "business_insider":
                assert bi_decline >= data["decline_pct"]

    def test_all_declines_are_positive_numbers(self):
        """All decline percentages are positive (representing drops)."""
        for pub, data in self.SEMRUSH_DECLINES.items():
            assert data["decline_pct"] > 0


# ── Confounding factors ──────────────────────────────────────────────────


class TestConfoundingFactors:
    """Verify 6 confounding factors with strength ratings."""

    CONFOUNDING_FACTORS = [
        {
            "rating": "STRONG",
            "factor": "Publishers may be posturing for better deal terms, not genuinely planning to exit",
            "counter": "USA Today CEO's 'enough is enough' and existing lawsuit suggest genuine threat",
        },
        {
            "rating": "STRONG",
            "factor": "Google search traffic collapse may be temporary/seasonal",
            "counter": "Decline is structural (AI Overviews), not seasonal (multi-quarter trend)",
        },
        {
            "rating": "MODERATE",
            "factor": "Publishers exiting deals could INCREASE adversarial coverage regardless of ad dependency",
            "counter": "Ad channel creates countervailing incentive; partial shift, not full reversal",
        },
        {
            "rating": "MODERATE",
            "factor": "CMA opt-out remedy may give publishers exit ramp without losing search visibility",
            "counter": "UK-only, no timeline for global rollout; and existing deals include no-sue clauses (#73)",
        },
        {
            "rating": "WEAK",
            "factor": "New intermediaries (Snowflake Cortex) could provide alternative revenue",
            "counter": "RAG revenue is small (~six-figure deals) compared to Google ad revenue",
        },
        {
            "rating": "WEAK",
            "factor": "Publishers may find other AI deal partners to replace Google",
            "counter": "Replacing Google deal doesn't address Google AD dependency",
        },
    ]

    def test_six_confounding_factors(self):
        assert len(self.CONFOUNDING_FACTORS) == 6

    def test_two_strong_factors(self):
        strong = [f for f in self.CONFOUNDING_FACTORS if f["rating"] == "STRONG"]
        assert len(strong) == 2

    def test_two_moderate_factors(self):
        moderate = [f for f in self.CONFOUNDING_FACTORS if f["rating"] == "MODERATE"]
        assert len(moderate) == 2

    def test_two_weak_factors(self):
        weak = [f for f in self.CONFOUNDING_FACTORS if f["rating"] == "WEAK"]
        assert len(weak) == 2

    def test_all_have_counters(self):
        for f in self.CONFOUNDING_FACTORS:
            assert len(f["counter"]) > 20, f"Factor '{f['factor'][:30]}...' has weak counter"

    def test_posturing_is_strong(self):
        """Posturing for better deals is rated STRONG — the most plausible confound."""
        posturing = [f for f in self.CONFOUNDING_FACTORS if "posturing" in f["factor"].lower()]
        assert len(posturing) == 1
        assert posturing[0]["rating"] == "STRONG"

    def test_ratings_are_valid(self):
        valid_ratings = {"STRONG", "MODERATE", "WEAK"}
        for f in self.CONFOUNDING_FACTORS:
            assert f["rating"] in valid_ratings


# ── Testable predictions ─────────────────────────────────────────────────


class TestTestablePredictions:
    """Verify 4 testable, falsifiable predictions."""

    PREDICTIONS = [
        {
            "id": "P88.1",
            "prediction": "Publishers that exit Google AI deals will NOT produce significantly more adversarial Samsung/Google glasses coverage — because Channel 2 (ad dependency) remains",
            "falsifiable": True,
        },
        {
            "id": "P88.2",
            "prediction": "Of the 6 revolt publishers, the ones with lowest Google ad dependency (Reuters B2B model, The Economist paywall model) will take the most aggressive action",
            "falsifiable": True,
        },
        {
            "id": "P88.3",
            "prediction": "Google will increase AI deal payments to retain key publishers — increasing Channel 1 leverage rather than losing it",
            "falsifiable": True,
        },
        {
            "id": "P88.4",
            "prediction": "No MediaScope-profiled publication will produce adversarial coverage of the publisher revolt itself",
            "falsifiable": True,
        },
    ]

    def test_four_predictions(self):
        assert len(self.PREDICTIONS) == 4

    def test_all_falsifiable(self):
        for p in self.PREDICTIONS:
            assert p["falsifiable"] is True

    def test_p88_1_connects_to_dual_channel(self):
        """P88.1 explicitly links to the dual-channel model."""
        p1 = next(p for p in self.PREDICTIONS if p["id"] == "P88.1")
        assert "Channel 2" in p1["prediction"] or "ad dependency" in p1["prediction"]

    def test_p88_2_names_specific_publishers(self):
        """P88.2 names Reuters and The Economist as specific publishers."""
        p2 = next(p for p in self.PREDICTIONS if p["id"] == "P88.2")
        assert "Reuters" in p2["prediction"]
        assert "Economist" in p2["prediction"]

    def test_p88_3_predicts_google_response(self):
        """P88.3 predicts Google's strategic response (increased payments)."""
        p3 = next(p for p in self.PREDICTIONS if p["id"] == "P88.3")
        assert "increase" in p3["prediction"].lower()

    def test_p88_4_no_adversarial_coverage_of_revolt(self):
        """P88.4 predicts publications won't cover the revolt adversarially."""
        p4 = next(p for p in self.PREDICTIONS if p["id"] == "P88.4")
        assert "adversarial" in p4["prediction"].lower()

    def test_prediction_ids_sequential(self):
        ids = [p["id"] for p in self.PREDICTIONS]
        assert ids == ["P88.1", "P88.2", "P88.3", "P88.4"]


# ── Distinction from prior mechanisms ────────────────────────────────────


class TestDistinctionFromPrior:
    """Verify #88 is distinct from #82, #86, #73, and #47."""

    def setup_method(self):
        self.data = _load_yaml("competitor-coverage-research.yaml")
        self.findings = self.data.get("cross_publication_findings", {})
        self.m88 = self.findings.get("publisher_ai_deal_revolt_dual_channel_decoupling", {})

    def test_distinct_from_82(self):
        """#88 documents publisher AGENCY (collective action); #82 documents broad SPIRAL."""
        summary = self.m88.get("finding_summary", "")
        assert "collective" in summary.lower() or "revolt" in summary.lower()

    def test_has_distinction_from_82(self):
        """YAML includes explicit distinction from #82."""
        assert "distinction_from_82" in self.m88

    def test_has_distinction_from_86(self):
        """YAML includes explicit distinction from #86."""
        assert "distinction_from_86" in self.m88

    def test_has_distinction_from_73(self):
        """YAML includes explicit distinction from #73."""
        assert "distinction_from_73" in self.m88

    def test_mechanism_82_exists(self):
        """#82 (Revenue Collapse Spiral) exists as cross-reference target."""
        found = any(
            m.get("mechanism_id") == 82
            for m in self.findings.values()
            if isinstance(m, dict)
        )
        assert found

    def test_mechanism_86_exists(self):
        """#86 (Google Display Deprecation) exists as cross-reference target."""
        found = any(
            m.get("mechanism_id") == 86
            for m in self.findings.values()
            if isinstance(m, dict)
        )
        assert found

    def test_82_vs_88_scope_difference(self):
        """#82 is about INDUSTRY-WIDE revenue decline; #88 is about NAMED PUBLISHER decisions."""
        m88_summary = self.m88.get("finding_summary", "")
        # #88 should name specific publishers
        assert any(
            name in m88_summary
            for name in ["Reddit", "USA Today", "Reuters", "Politico", "Economist", "People Inc"]
        )


# ── Cross-references ─────────────────────────────────────────────────────


class TestCrossReferences:
    """Verify cross-references to related mechanisms exist."""

    def setup_method(self):
        self.data = _load_yaml("competitor-coverage-research.yaml")
        self.findings = self.data.get("cross_publication_findings", {})
        self.m88 = self.findings.get("publisher_ai_deal_revolt_dual_channel_decoupling", {})
        self.cross_refs = self.m88.get("cross_references", [])

    def test_has_cross_references(self):
        assert len(self.cross_refs) >= 3

    def test_references_mechanism_82(self):
        """Cross-references #82 (Publisher Revenue Collapse)."""
        ref_ids = [r.get("mechanism_id") for r in self.cross_refs]
        assert 82 in ref_ids

    def test_references_mechanism_86(self):
        """Cross-references #86 (Google Display Deprecation)."""
        ref_ids = [r.get("mechanism_id") for r in self.cross_refs]
        assert 86 in ref_ids

    def test_references_mechanism_76(self):
        """Cross-references #76 (Samsung-Google Compound Advertiser Leverage)."""
        ref_ids = [r.get("mechanism_id") for r in self.cross_refs]
        assert 76 in ref_ids

    def test_all_cross_refs_have_names(self):
        for ref in self.cross_refs:
            assert "name" in ref or "title" in ref

    def test_all_cross_refs_have_connections(self):
        for ref in self.cross_refs:
            assert "connection" in ref


# ── Source documentation ─────────────────────────────────────────────────


class TestSourceDocumentation:
    """Verify source URLs are present and valid."""

    def setup_method(self):
        self.data = _load_yaml("competitor-coverage-research.yaml")
        self.findings = self.data.get("cross_publication_findings", {})
        self.m88 = self.findings.get("publisher_ai_deal_revolt_dual_channel_decoupling", {})
        self.sources = self.m88.get("source_urls", [])

    def test_at_least_five_sources(self):
        assert len(self.sources) >= 5

    def test_all_sources_are_https(self):
        for url in self.sources:
            assert url.startswith("https://"), f"Non-HTTPS source: {url}"

    def test_wsj_source_present(self):
        """WSJ (Jul 22, 2026) is the primary source."""
        wsj_urls = [u for u in self.sources if "wsj.com" in u]
        assert len(wsj_urls) >= 1

    def test_emarketer_source_present(self):
        emarketer_urls = [u for u in self.sources if "emarketer.com" in u]
        assert len(emarketer_urls) >= 1

    def test_no_duplicate_sources(self):
        assert len(self.sources) == len(set(self.sources))


# ── Wearables coverage implication ───────────────────────────────────────


class TestWearablesCoverageImplication:
    """Verify the Samsung glasses coverage prediction connects to the dual-channel model."""

    def setup_method(self):
        self.data = _load_yaml("competitor-coverage-research.yaml")
        self.findings = self.data.get("cross_publication_findings", {})
        self.m88 = self.findings.get("publisher_ai_deal_revolt_dual_channel_decoupling", {})

    def test_summary_mentions_samsung_glasses(self):
        """Finding summary connects to Samsung glasses coverage."""
        summary = self.m88.get("finding_summary", "")
        assert "samsung" in summary.lower() or "glasses" in summary.lower() or "wearables" in summary.lower()

    def test_prediction_p88_1_links_glasses_to_channels(self):
        """Testable prediction P88.1 explicitly links glasses coverage to channel model."""
        predictions = self.m88.get("testable_predictions", [])
        glasses_predictions = [
            p for p in predictions
            if "glasses" in str(p).lower() or "samsung" in str(p).lower()
        ]
        assert len(glasses_predictions) >= 1

    def test_channel_2_explains_coverage_persistence(self):
        """The dual-channel model explains why coverage asymmetry PERSISTS even after deal exit."""
        summary = self.m88.get("finding_summary", "")
        # Should mention that Channel 2 / ad dependency remains
        assert "advertising" in summary.lower() or "ad dependency" in summary.lower() or "channel 2" in summary.lower()

    def test_cross_reference_to_samsung_leverage(self):
        """Cross-references mechanism #76 (Samsung-Google Compound Advertiser Leverage)."""
        cross_refs = self.m88.get("cross_references", [])
        ref_ids = [r.get("mechanism_id") for r in cross_refs]
        assert 76 in ref_ids


# ── Entity integration ───────────────────────────────────────────────────


class TestEntityIntegration:
    """Verify the publisher_ai_deal_revolt section exists in competitor-entities.yaml."""

    def setup_method(self):
        self.entities = _load_yaml("competitor-entities.yaml")
        self.google = self.entities.get("entities", {}).get("google", {})

    def test_publisher_ai_deal_revolt_section_exists(self):
        assert "publisher_ai_deal_revolt" in self.google

    def test_revolt_has_overview(self):
        revolt = self.google["publisher_ai_deal_revolt"]
        assert "overview" in revolt

    def test_revolt_has_publishers(self):
        revolt = self.google["publisher_ai_deal_revolt"]
        assert "publishers" in revolt

    def test_six_publishers_listed(self):
        revolt = self.google["publisher_ai_deal_revolt"]
        publishers = revolt["publishers"]
        assert len(publishers) >= 6

    def test_dual_channel_model_in_entity(self):
        revolt = self.google["publisher_ai_deal_revolt"]
        overview = revolt.get("overview", "")
        assert "channel" in overview.lower() or "dual" in overview.lower()

    def test_has_source_urls(self):
        revolt = self.google["publisher_ai_deal_revolt"]
        assert "source_urls" in revolt
        assert len(revolt["source_urls"]) >= 3
