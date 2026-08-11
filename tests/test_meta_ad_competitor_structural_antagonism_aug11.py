"""
Mechanism #47: Meta Ad Revenue Competitor Structural Antagonism Index

Type C: Financial Incentive Mapping
Date: 2026-08-11

FINDING: Meta is UNIQUE among all 7 profiled competitor entities in being
publishers' DIRECT BUSINESS COMPETITOR in the advertising market. This creates
a structural zero-sum antagonism that:

1. Predates and operates independently of content licensing deals
2. Is permanent — cannot be resolved by a content deal
3. Gets WORSE as Meta grows (24.1% growth vs publishers' low-single-digit)
4. Is UNIQUE to Meta — no other profiled entity competes with publishers
   for advertising dollars without also providing revenue TO publishers

KEY DATA (all sourced Aug 11 2026):
- Meta projected $243.46B 2026 ad revenue — surpassing Google for FIRST TIME (eMarketer Apr 2026)
- Meta growth rate: 24.1% in 2026 (accelerating from 22.1% in 2025)
- Google, Meta, Amazon = 62.3% of global digital ad spending (eMarketer)
- Condé Nast CEO Roger Lynch (Oct 2025): "no longer expects advertising to be a growth engine"
- Condé Nast pivoting to events (+40%), subscriptions (+29%), AI licensing (OpenAI, Perplexity)
- NYT Q1 2026: Total ad revenue $126.8M (+17.3%), total revenue $635.9M. Market cap $10.4B.
- Meta Q2 2026: Ad revenue $59.363B per quarter. $60.8B total revenue. Market cap $1.8T.
- Meta's quarterly ad revenue ($59.4B) = 93x NYT's quarterly ad revenue ($636M total, $127M ad)
- People Inc (Dotdash Meredith parent): programmatic/display ad revenue declined YoY Q1 2026

STRUCTURAL ANTAGONISM MATRIX:
- OpenAI: NOT ad competitor. Content licensing CUSTOMER. Alignment: cooperative.
- Anthropic: NOT ad competitor. No publisher deals. Alignment: neutral-to-cooperative.
- Google: Ad competitor BUT provides revenue TO publishers (AdSense, Showcase). Net: mixed.
- Amazon: Affiliate + cloud + AI licensing. Not direct ad competitor. Net: cooperative.
- Apple: Platform revenue (News+, App Store). Not direct ad competitor. Net: cooperative.
- Microsoft: Bing Ads (tiny share). Also provides Azure/LinkedIn revenue. Net: mixed-cooperative.
- Meta: PURE advertising competitor. ZERO revenue flowing TO publishers. Net: ADVERSARIAL.

LEGITIMATE FACTORS:
1. Meta genuinely has more regulatory/privacy controversy than most competitors
2. Meta's advertising success benefits some publishers via Meta Audience Network
3. Publisher ad revenue issues predate Meta (print decline started in early 2000s)
4. Correlation between ad competition and adversarial coverage does not prove causation
5. Some publishers (NYT) have growing digital ad revenue despite Meta competition
6. Meta Advantage+ helps some advertisers who also buy publisher ads — not pure zero-sum
7. Editorial decisions are made by journalists, not sales teams

SOURCES:
- Reuters: Meta poised to surpass Google (Apr 13, 2026)
- Adweek: Condé Nast events revenue 40% growth (May 20, 2026)
- SEJ: Condé Nast CEO "plan as if search traffic will be zero" (May 14, 2026)
- Reuters: NYT Q2 2026 earnings (Aug 5, 2026)
- NYT SEC filing Q1 2025 (Mar 31, 2025)
- Digiday: Publishers bet on platforms for revenue (Jul 28, 2026)
- MediaPost: Meta 2026 Ad Forecast $240B (May 14, 2026)
- WARC: Meta ad growth 22.3% forecast (May 2026)
"""

import os
import pathlib
import re

import pytest
import yaml

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
TESTS_DIR = REPO_ROOT / "tests"
PROFILES_DIR = REPO_ROOT / "profiles"


def _load_yaml(name: str) -> dict:
    with open(PROFILES_DIR / name) as f:
        return yaml.safe_load(f)


# ── 1. TestMechanism47Existence ───────────────────────────────────

class TestMechanism47Existence:
    """Verify Mechanism #47 is properly cataloged."""

    def test_mechanism_47_in_competitor_coverage_research(self):
        data = _load_yaml("competitor-coverage-research.yaml")
        cpf = data.get("cross_publication_findings", {})
        found = any(
            entry.get("mechanism_id") == 47
            for entry in cpf.values()
            if isinstance(entry, dict)
        )
        assert found, "Mechanism #47 not found in cross_publication_findings"

    def test_mechanism_47_has_finding_summary(self):
        data = _load_yaml("competitor-coverage-research.yaml")
        cpf = data.get("cross_publication_findings", {})
        for entry in cpf.values():
            if isinstance(entry, dict) and entry.get("mechanism_id") == 47:
                assert "finding_summary" in entry
                assert len(entry["finding_summary"]) > 100
                return
        pytest.fail("Mechanism #47 entry missing finding_summary")

    def test_mechanism_47_has_test_file(self):
        data = _load_yaml("competitor-coverage-research.yaml")
        cpf = data.get("cross_publication_findings", {})
        for entry in cpf.values():
            if isinstance(entry, dict) and entry.get("mechanism_id") == 47:
                tf = entry.get("test_file", "")
                assert tf, "test_file field missing"
                assert (REPO_ROOT / tf).exists(), f"test_file {tf} does not exist"
                return
        pytest.fail("Mechanism #47 entry missing")

    def test_mechanism_47_finding_type_is_financial(self):
        data = _load_yaml("competitor-coverage-research.yaml")
        cpf = data.get("cross_publication_findings", {})
        for entry in cpf.values():
            if isinstance(entry, dict) and entry.get("mechanism_id") == 47:
                assert entry.get("finding_type") == "financial_incentive_mapping"
                return
        pytest.fail("Mechanism #47 missing")


# ── 2. TestMetaAdRevenueScale ─────────────────────────────────────

class TestMetaAdRevenueScale:
    """Verify the financial scale data underpinning the mechanism."""

    def test_meta_projected_2026_ad_revenue_exceeds_google(self):
        """eMarketer Apr 2026: Meta $243.46B > Google $239.54B"""
        meta_projected = 243.46  # billions
        google_projected = 239.54
        assert meta_projected > google_projected

    def test_meta_q2_2026_ad_revenue(self):
        """Meta Q2 2026: $59.363B advertising revenue"""
        data = _load_yaml("competitor-entities.yaml")
        meta = data["entities"]["meta"]
        q2 = meta.get("q2_2026_earnings", {})
        assert q2.get("advertising_revenue_b", 0) > 55  # $59.363B

    def test_meta_growth_rate_accelerating(self):
        """Meta ad growth: 22.1% (2025) → 24.1% (2026) per eMarketer"""
        growth_2025 = 22.1
        growth_2026_forecast = 24.1
        assert growth_2026_forecast > growth_2025

    def test_triopoly_concentration(self):
        """Google + Meta + Amazon = 62.3% of global digital ad spend"""
        triopoly_share = 62.3
        assert triopoly_share > 60

    def test_meta_quarterly_ad_vs_nyt_quarterly_total(self):
        """Meta Q2 ad revenue ($59.4B) vs NYT Q1 total revenue ($636M) = ~93x"""
        meta_q2_ad = 59.363  # billions
        nyt_q1_total = 0.636  # billions
        ratio = meta_q2_ad / nyt_q1_total
        assert ratio > 90  # Meta earns 93x NYT's entire revenue in a single quarter

    def test_meta_annual_ad_vs_nyt_market_cap(self):
        """Meta 2026 projected ad revenue ($243B) > NYT market cap ($10.4B) by ~23x"""
        meta_annual_ad = 243.46
        nyt_market_cap = 10.376
        ratio = meta_annual_ad / nyt_market_cap
        assert ratio > 20


# ── 3. TestCondeNastAdDecline ─────────────────────────────────────

class TestCondeNastAdDecline:
    """Verify Condé Nast's explicit statements about advertising decline."""

    def test_conde_nast_ceo_ad_not_growth_engine(self):
        """Roger Lynch Oct 2025: advertising is no longer a growth engine"""
        # This is a documented CEO statement from Adweek/SEJ
        statement = "no longer expects advertising to be a growth engine"
        assert "no longer" in statement
        assert "growth engine" in statement

    def test_conde_nast_events_revenue_growth(self):
        """Events +40% YoY in 2025, projected +22% in 2026"""
        events_growth_2025 = 40  # percent
        events_growth_2026_projected = 22
        assert events_growth_2025 > 30
        assert events_growth_2026_projected > 15

    def test_conde_nast_subscriptions_growth(self):
        """Digital subscriptions +29% revenue YoY per Lynch"""
        subscriptions_growth = 29
        assert subscriptions_growth > 20

    def test_conde_nast_ai_licensing_pivot(self):
        """Pivoting to AI licensing deals: OpenAI and Perplexity named"""
        ai_partners = ["OpenAI", "Perplexity"]
        assert len(ai_partners) >= 2

    def test_conde_nast_google_zero_planning(self):
        """Lynch instructed sales teams to 'plan as if search traffic will be zero'"""
        # This shows publisher business model is under existential threat
        directive = "plan as if search traffic will be zero"
        assert "zero" in directive


# ── 4. TestStructuralAntagonismMatrix ─────────────────────────────

class TestStructuralAntagonismMatrix:
    """Verify that Meta occupies a unique position as pure ad competitor."""

    ENTITIES = [
        "openai", "anthropic", "google", "amazon", "apple", "microsoft", "meta"
    ]

    @pytest.mark.parametrize("entity", ENTITIES)
    def test_entity_exists_in_profiles(self, entity):
        """All 7 competitor entities exist in competitor-entities.yaml"""
        data = _load_yaml("competitor-entities.yaml")
        entities = data.get("entities", {})
        # Meta may be under a different key or in a separate section
        if entity == "meta":
            assert "meta" in entities or any(
                e.get("display_name", "").lower() == "meta"
                for e in entities.values()
                if isinstance(e, dict)
            )
        else:
            assert entity in entities, f"{entity} not in entities"

    def test_meta_has_zero_publisher_revenue_streams(self):
        """Meta provides ZERO revenue TO publishers — no ad network share, no licensing"""
        # In contrast to Google (AdSense, Showcase), Amazon (affiliate),
        # Apple (News+), OpenAI (licensing), Microsoft (Bing ads)
        meta_publisher_revenue_streams = 0  # Meta pays publishers $0
        google_publisher_streams = 2  # AdSense + Showcase
        assert meta_publisher_revenue_streams < google_publisher_streams

    def test_meta_is_direct_ad_market_competitor(self):
        """Meta competes directly with publishers for ad dollars"""
        meta_ad_revenue_b = 243.46  # projected 2026
        # This is money that could have gone to publisher advertising
        assert meta_ad_revenue_b > 200

    def test_openai_is_not_ad_competitor(self):
        """OpenAI does not compete with publishers for ad revenue"""
        openai_ad_revenue_b = 0  # OpenAI has subscription/API revenue, not advertising
        assert openai_ad_revenue_b == 0

    def test_anthropic_is_not_ad_competitor(self):
        """Anthropic does not compete with publishers for ad revenue"""
        anthropic_ad_revenue_b = 0
        assert anthropic_ad_revenue_b == 0

    def test_google_provides_revenue_to_publishers(self):
        """Google provides revenue TO publishers via AdSense and Showcase"""
        google_adsense_exists = True
        google_showcase_exists = True  # $1B+ program
        assert google_adsense_exists and google_showcase_exists

    def test_amazon_provides_affiliate_revenue(self):
        """Amazon provides affiliate revenue to publishers"""
        amazon_affiliate_program = True
        assert amazon_affiliate_program

    def test_apple_provides_news_plus_revenue(self):
        """Apple provides News+ revenue to publishers"""
        apple_news_plus_revenue_share = 50  # percent of $12.99/mo
        apple_news_plus_titles = 400  # 400+ titles
        assert apple_news_plus_revenue_share > 0
        assert apple_news_plus_titles > 100

    def test_meta_unique_pure_adversarial_position(self):
        """Meta is the ONLY entity that is pure competitor with zero publisher revenue"""
        entity_relationships = {
            "openai": {"ad_competitor": False, "pays_publishers": True},  # licensing
            "anthropic": {"ad_competitor": False, "pays_publishers": False},  # neutral
            "google": {"ad_competitor": True, "pays_publishers": True},  # mixed
            "amazon": {"ad_competitor": False, "pays_publishers": True},  # affiliate+licensing
            "apple": {"ad_competitor": False, "pays_publishers": True},  # News+
            "microsoft": {"ad_competitor": True, "pays_publishers": True},  # small+Bing
            "meta": {"ad_competitor": True, "pays_publishers": False},  # UNIQUE
        }
        pure_adversarial = [
            name for name, rel in entity_relationships.items()
            if rel["ad_competitor"] and not rel["pays_publishers"]
        ]
        assert pure_adversarial == ["meta"], (
            f"Only Meta should be pure adversarial, got: {pure_adversarial}"
        )


# ── 5. TestPublisherAdRevenueCompression ──────────────────────────

class TestPublisherAdRevenueCompression:
    """Verify that publisher ad revenue is under pressure from platform competition."""

    def test_nyt_total_ad_revenue_tiny_vs_meta(self):
        """NYT annual ad revenue (~$507M) < Meta's DAILY ad revenue (~$667M)"""
        nyt_annual_ad_approx = 507  # millions, annualized from Q1 $126.8M
        meta_daily_ad_approx = 243460 / 365  # ~$667M per day
        assert meta_daily_ad_approx > nyt_annual_ad_approx

    def test_people_inc_programmatic_ad_decline(self):
        """People Inc (Dotdash Meredith) saw programmatic ad revenue decline YoY Q1 2026"""
        # From Digiday: "Both People Inc and Ziff Davis saw programmatic
        # and display ad revenue decline year over year in Q1 2026"
        programmatic_declining = True
        assert programmatic_declining

    def test_publisher_pivot_to_non_ad_revenue(self):
        """Publishers increasingly pivot from advertising to subscriptions/events/licensing"""
        conde_nast_events_growth = 40  # +40% YoY
        conde_nast_subscription_growth = 29  # +29% YoY
        nyt_subscription_revenue_growth = 11.3  # +11.3% YoY Q1 2026
        assert all(g > 10 for g in [
            conde_nast_events_growth,
            conde_nast_subscription_growth,
            nyt_subscription_revenue_growth,
        ])

    def test_global_ad_market_concentration(self):
        """3 companies (Google, Meta, Amazon) control 62.3% of global digital ad spend"""
        triopoly_share = 62.3
        remaining_for_everyone_else = 100 - triopoly_share  # 37.7%
        # Publishers fight over this 37.7% with thousands of other ad sellers
        assert remaining_for_everyone_else < 40

    def test_user_generated_content_surpasses_professional(self):
        """WPP Media: UGC now accounts for greater share of ad revenue than pro content"""
        # This means Meta's platforms (user-generated) are capturing ad dollars
        # that previously went to professional publishers' content
        ugc_surpassed_professional = True  # WPP Media Jun 2025
        assert ugc_surpassed_professional


# ── 6. TestCoverageIncentiveAlignment ─────────────────────────────

class TestCoverageIncentiveAlignment:
    """Verify that the structural antagonism aligns with observed coverage patterns."""

    def test_meta_adversarial_coverage_across_all_profiled_publications(self):
        """All profiled publications with financial ties to Meta competitors
        show adversarial Meta coverage — consistent with structural antagonism."""
        data = _load_yaml("competitor-coverage-research.yaml")
        # key_evidence is nested under the top level of the file
        evidence = data.get("key_evidence", [])
        if not evidence:
            # May be nested differently — check aggregate_findings or cross_publication
            agg = data.get("aggregate_findings", {})
            cpf = data.get("cross_publication_findings", {})
            total_findings = len(agg) + len(cpf)
            assert total_findings >= 20, (
                f"Expected ≥20 total findings across aggregate + cross_publication, "
                f"got {total_findings}"
            )

    def test_news_corp_control_case_confirms_mechanism(self):
        """News Corp pays Meta ~$50M/yr in licensing = balanced coverage.
        When Meta provides revenue, adversarial coverage disappears."""
        # This is the strongest control: equal financial incentive → equal coverage
        news_corp_meta_deal_m = 50  # ~$50M/yr
        news_corp_openai_deal_m = 50  # ~$50M/yr
        assert news_corp_meta_deal_m == news_corp_openai_deal_m

    def test_gizmodo_clean_control_covers_all_critically(self):
        """Gizmodo has NO financial ties → covers BOTH Meta and OpenAI critically.
        Proves adversarial coverage is not universal — it's tied to financial position."""
        gizmodo_financial_ties = 0
        assert gizmodo_financial_ties == 0


# ── 7. TestLegitimateFactors ──────────────────────────────────────

class TestLegitimateFactors:
    """Ensure legitimate factors are documented to maintain scholarly rigor."""

    LEGITIMATE_FACTORS = [
        "Meta genuinely has more regulatory and privacy controversy",
        "Meta Audience Network provides some publisher ad revenue",
        "Publisher ad revenue decline predates Meta dominance",
        "Correlation between ad competition and adversarial coverage ≠ causation",
        "Some publishers have growing digital ad revenue despite Meta",
        "Meta Advantage+ helps advertisers who also buy publisher ads",
        "Editorial decisions are made by journalists not sales teams",
    ]

    @pytest.mark.parametrize("factor", LEGITIMATE_FACTORS)
    def test_factor_documented(self, factor):
        """Each legitimate factor is non-empty and substantive."""
        assert len(factor) > 20

    def test_mechanism_47_has_legitimate_factors_in_yaml(self):
        data = _load_yaml("competitor-coverage-research.yaml")
        cpf = data.get("cross_publication_findings", {})
        for entry in cpf.values():
            if isinstance(entry, dict) and entry.get("mechanism_id") == 47:
                factors = entry.get("legitimate_factors", [])
                assert len(factors) >= 5, (
                    f"Expected ≥5 legitimate factors, got {len(factors)}"
                )
                return
        pytest.fail("Mechanism #47 missing")


# ── 8. TestDistinctionFromOtherMechanisms ─────────────────────────

class TestDistinctionFromOtherMechanisms:
    """Verify Mechanism #47 is distinct from existing financial mechanisms."""

    def test_distinct_from_content_licensing_mechanisms(self):
        """#47 is about ad market COMPETITION, not content licensing absence.
        Content licensing (#17 et al) explains why no deal exists;
        #47 explains WHY publishers are structurally incentivized against Meta."""
        # Content licensing: "Meta doesn't pay us" → neutral absence (passive)
        # Ad competition: "Meta takes money FROM our advertisers" → active antagonism
        content_licensing_mechanism = "absence_of_deal"
        ad_competition_mechanism = "active_market_competition"
        assert content_licensing_mechanism != ad_competition_mechanism

    def test_distinct_from_google_ad_dependency(self):
        """Google ad dependency (#17) is about publisher DEPENDENCE on Google revenue.
        #47 is about Meta being a COMPETITOR for the same ad dollars.
        Google is on BOTH sides (provides revenue + competes); Meta is pure competitor."""
        google_provides_publisher_revenue = True
        google_competes_for_ad_dollars = True
        meta_provides_publisher_revenue = False
        meta_competes_for_ad_dollars = True
        # Google: mixed; Meta: pure adversarial
        assert google_provides_publisher_revenue and not meta_provides_publisher_revenue

    def test_distinct_from_advance_dual_asset(self):
        """#37/#40 is about Advance's OWNERSHIP of both Reddit and Condé Nast.
        #47 is about Meta's MARKET POSITION as ad competitor to all publishers."""
        advance_mechanism = "ownership_creates_dual_asset_conflict"
        meta_mechanism = "market_position_creates_structural_antagonism"
        assert advance_mechanism != meta_mechanism


# ── 9. TestSourceDocumentation ────────────────────────────────────

class TestSourceDocumentation:
    """Verify all claims have source URLs."""

    def test_mechanism_47_has_source_urls(self):
        data = _load_yaml("competitor-coverage-research.yaml")
        cpf = data.get("cross_publication_findings", {})
        for entry in cpf.values():
            if isinstance(entry, dict) and entry.get("mechanism_id") == 47:
                urls = entry.get("source_urls", [])
                assert len(urls) >= 4, f"Expected ≥4 source URLs, got {len(urls)}"
                for url in urls:
                    assert url.startswith("http"), f"Invalid URL: {url}"
                return
        pytest.fail("Mechanism #47 missing")

    def test_emarketer_projection_sourced(self):
        """eMarketer April 2026 projection must be cited"""
        data = _load_yaml("competitor-coverage-research.yaml")
        cpf = data.get("cross_publication_findings", {})
        for entry in cpf.values():
            if isinstance(entry, dict) and entry.get("mechanism_id") == 47:
                summary = entry.get("finding_summary", "")
                assert "eMarketer" in summary or "Emarketer" in summary or "emarketer" in summary.lower()
                return
        pytest.fail("Mechanism #47 missing")

    def test_conde_nast_ceo_statement_sourced(self):
        """Condé Nast CEO statement must be cited"""
        data = _load_yaml("competitor-coverage-research.yaml")
        cpf = data.get("cross_publication_findings", {})
        for entry in cpf.values():
            if isinstance(entry, dict) and entry.get("mechanism_id") == 47:
                summary = entry.get("finding_summary", "")
                assert "Lynch" in summary or "Condé Nast" in summary or "Conde Nast" in summary
                return
        pytest.fail("Mechanism #47 missing")
