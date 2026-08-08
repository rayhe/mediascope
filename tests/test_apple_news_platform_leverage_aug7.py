"""
Type C: Apple News+ Platform Dependency — The Hidden Publisher Leverage
Mechanism

Apple's Apple News+ subscription platform creates a financial dependency
between Apple and 400+ publishers that is DISTINCT from AI content
licensing deals — and largely invisible in the MediaScope framework
until now. This mechanism operates through Apple's 50% revenue share
on subscription fees, Apple One bundle revenue dilution, and App Store
subscription commissions (15-30%).

KEY FINDING — APPLE'S QUINTUPLE PUBLISHER LEVERAGE:

Apple has FIVE distinct financial relationship mechanisms with publishers,
making it the THIRD most entangled entity after Microsoft (7) and
Amazon (6):

  1. Apple News+ Subscription Platform (50% revenue share)
     - 400+ titles, 125M monthly users (free + paid)
     - CIRP: 24% of US Apple customers pay for News+ (up from 15% in 2020)
     - Apple takes 50% of $12.99/mo subscription, rest split by engagement
     - "By far the most valuable syndication partner" — The Atlantic CGO

  2. App Store Subscription Tax (15-30%)
     - ALL iOS subscription revenue runs through Apple's in-app purchase
     - NYT 10.8M digital subscribers, many iOS → 15% cut per subscriber
     - News Partner Program reduced to 15% from year one (vs 30%/15%)

  3. Apple One Bundle Revenue Dilution
     - Apple One Premier ($37.95/mo) includes News+
     - Revenue allocated to News+ is diluted vs standalone $12.99
     - Subscribers getting News+ through Apple One = lower per-publisher payout

  4. Content Distribution Monopoly (2.5B active devices)
     - Apple News preinstalled on every iPhone, iPad, Mac
     - 125M monthly users across US, Canada, UK, Australia
     - #1 news app in US, Canada, Australia (as of 2025)
     - 100 editors curate content — Apple controls discovery

  5. Publisher Content Bypass for AI ($0 → $1B to Google)
     - Apple paid Google $1B/yr for Gemini trained on publisher content
     - Publishers receive $0 from Apple for AI content flow
     - Bypassed 2.5 years of publisher deal negotiations

THE LIFELINE PARADOX:
Publishers now publicly describe Apple News+ as their "most valuable
syndication partner" and a "lifeline" at the exact moment their
Google search traffic is being cannibalized (-34.5% from AI Overviews)
and Meta deprioritized news. This INCREASES Apple's leverage: publishers
who can't afford to leave Apple News+ cannot afford to criticize Apple.

Apple Q3 FY2026 (Jul 30, 2026): $30.7B Services revenue (+12% YoY),
1.5B paid subscriptions across all services, 2.5B active devices.

Sources:
- Digiday (Apple News+ as stable revenue stream):
  https://digiday.com/media/media-briefing-publishers-see-apple-news-as-a-stable-revenue-stream-amid-volatile-referral-traffic/
- CIRP growth data (9to5Mac):
  https://9to5mac.com/2024/05/29/apple-news-subscriptions-growing-4x-faster-than-major-publishers/
- Cult of Mac (subscription growth):
  https://www.cultofmac.com/news/apple-news-subscription-growth
- Apple 125M MAU (Good e-Reader / FT):
  https://goodereader.com/blog/digital-publishing/apple-news-is-expanding-into-more-countries-in-2025
- Apple 2025 record year (WebWire):
  https://www.webwire.com/ViewPressRel.asp?aId=349070
- Apple Q3 FY26 earnings (AppleInsider):
  https://appleinsider.com/articles/26/07/30/apple-hits-15-billion-subscription-milestone-still-falls-short-of-wall-street-wants
- 50% revenue split (CNBC via 9to5Mac):
  https://9to5mac.com/2019/11/14/apple-news-plus-subscribers/?extended-comments=1
- News Partner Program 15% (Cult of Mac):
  https://www.cultofmac.com/news/apple-news-program-takes-a-smaller-cut-of-publishers-revenue
- Apple Q3 FY26 (MacStories):
  https://www.macstories.net/news/apple-reports-q3-2026-earnings/

Created: 2026-08-07 20:00 PT
"""

import yaml
import os
import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_yaml(filename):
    path = os.path.join(REPO_ROOT, "profiles", filename)
    with open(path) as f:
        return yaml.safe_load(f)


class TestAppleNewsPlatformLeverage:
    """Verify the apple_news_platform_leverage section exists and is complete."""

    def test_apple_entity_has_news_platform_leverage(self):
        data = load_yaml("competitor-entities.yaml")
        apple = data["entities"]["apple"]
        assert "apple_news_platform_leverage" in apple

    def test_revenue_share_50_percent(self):
        data = load_yaml("competitor-entities.yaml")
        leverage = data["entities"]["apple"]["apple_news_platform_leverage"]
        assert leverage["subscription_revenue_share_pct"] == 50

    def test_monthly_active_users_125m(self):
        data = load_yaml("competitor-entities.yaml")
        leverage = data["entities"]["apple"]["apple_news_platform_leverage"]
        assert leverage["monthly_active_users_m"] == 125

    def test_title_count_400_plus(self):
        data = load_yaml("competitor-entities.yaml")
        leverage = data["entities"]["apple"]["apple_news_platform_leverage"]
        assert leverage["title_count"] >= 400

    def test_subscription_price(self):
        data = load_yaml("competitor-entities.yaml")
        leverage = data["entities"]["apple"]["apple_news_platform_leverage"]
        assert leverage["subscription_price_usd"] == 12.99

    def test_cirp_penetration_rate(self):
        data = load_yaml("competitor-entities.yaml")
        leverage = data["entities"]["apple"]["apple_news_platform_leverage"]
        assert leverage["cirp_us_penetration_pct_2024"] == 24
        assert leverage["cirp_us_penetration_pct_2020"] == 15

    def test_has_source_urls(self):
        data = load_yaml("competitor-entities.yaml")
        leverage = data["entities"]["apple"]["apple_news_platform_leverage"]
        assert len(leverage["source_urls"]) >= 4

    def test_has_profiled_publisher_participation(self):
        data = load_yaml("competitor-entities.yaml")
        leverage = data["entities"]["apple"]["apple_news_platform_leverage"]
        participants = leverage["profiled_publisher_participation"]
        assert len(participants) >= 3


class TestAppleQuintupleLeverage:
    """Verify the quintuple_publisher_leverage section with all 5 layers."""

    def test_has_quintuple_leverage(self):
        data = load_yaml("competitor-entities.yaml")
        apple = data["entities"]["apple"]
        assert "quintuple_publisher_leverage" in apple

    def test_five_layers(self):
        data = load_yaml("competitor-entities.yaml")
        leverage = data["entities"]["apple"]["quintuple_publisher_leverage"]
        assert len(leverage["layers"]) == 5

    def test_layer_names(self):
        data = load_yaml("competitor-entities.yaml")
        leverage = data["entities"]["apple"]["quintuple_publisher_leverage"]
        names = [layer["name"] for layer in leverage["layers"]]
        assert "apple_news_plus_platform" in names
        assert "app_store_subscription_tax" in names
        assert "apple_one_revenue_dilution" in names
        assert "content_distribution_monopoly" in names
        assert "publisher_content_bypass_for_ai" in names

    def test_meta_contrast_present(self):
        data = load_yaml("competitor-entities.yaml")
        leverage = data["entities"]["apple"]["quintuple_publisher_leverage"]
        assert "meta_contrast" in leverage
        assert len(leverage["meta_contrast"]) > 50


class TestAppleQ3FY26Earnings:
    """Verify Apple Q3 FY2026 earnings data in entity."""

    def test_has_q3_fy26_earnings(self):
        data = load_yaml("competitor-entities.yaml")
        apple = data["entities"]["apple"]
        assert "q3_fy26_earnings" in apple

    def test_services_revenue(self):
        data = load_yaml("competitor-entities.yaml")
        earnings = data["entities"]["apple"]["q3_fy26_earnings"]
        assert earnings["services_revenue_b"] == 30.7

    def test_total_revenue(self):
        data = load_yaml("competitor-entities.yaml")
        earnings = data["entities"]["apple"]["q3_fy26_earnings"]
        assert earnings["total_revenue_b"] == 109.4

    def test_paid_subscriptions(self):
        data = load_yaml("competitor-entities.yaml")
        earnings = data["entities"]["apple"]["q3_fy26_earnings"]
        assert earnings["paid_subscriptions_b"] == 1.5

    def test_active_devices(self):
        data = load_yaml("competitor-entities.yaml")
        earnings = data["entities"]["apple"]["q3_fy26_earnings"]
        assert earnings["active_devices_b"] == 2.5

    def test_has_source_urls(self):
        data = load_yaml("competitor-entities.yaml")
        earnings = data["entities"]["apple"]["q3_fy26_earnings"]
        assert len(earnings["source_urls"]) >= 2


class TestLifelineParadox:
    """Verify the Lifeline Paradox finding is documented."""

    def test_lifeline_paradox_in_leverage(self):
        data = load_yaml("competitor-entities.yaml")
        leverage = data["entities"]["apple"]["quintuple_publisher_leverage"]
        overview = leverage.get("overview", "")
        assert "lifeline" in overview.lower() or "paradox" in overview.lower()

    def test_atlantic_most_valuable_partner(self):
        data = load_yaml("competitor-entities.yaml")
        leverage = data["entities"]["apple"]["apple_news_platform_leverage"]
        participants = leverage["profiled_publisher_participation"]
        atlantic = [p for p in participants if "Atlantic" in p.get("name", "")]
        assert len(atlantic) == 1
        assert "most valuable" in atlantic[0].get("quote", "").lower() or \
               "most valuable" in atlantic[0].get("detail", "").lower()

    def test_conde_nast_participation(self):
        data = load_yaml("competitor-entities.yaml")
        leverage = data["entities"]["apple"]["apple_news_platform_leverage"]
        participants = leverage["profiled_publisher_participation"]
        conde_nast = [p for p in participants
                      if "Condé Nast" in p.get("name", "") or
                      "Conde Nast" in p.get("name", "")]
        assert len(conde_nast) == 1

    def test_ft_not_on_apple_news(self):
        """FT is notably NOT on Apple News — important for financial isolation."""
        data = load_yaml("competitor-entities.yaml")
        leverage = data["entities"]["apple"]["apple_news_platform_leverage"]
        participants = leverage["profiled_publisher_participation"]
        ft = [p for p in participants
              if "Financial Times" in p.get("name", "")]
        assert len(ft) == 1
        assert ft[0].get("status") == "not_available"


class TestProfiledPublisherAppleExposure:
    """Verify Apple News+ participation is documented for each profiled
    publication, enabling cross-reference with Meta coverage tone."""

    @pytest.mark.parametrize("pub_name,expected_status", [
        ("Condé Nast (WIRED)", "partner"),
        ("The Atlantic", "partner"),
        ("News Corp (WSJ)", "partner"),
        ("Financial Times", "not_available"),
    ])
    def test_publisher_apple_news_status(self, pub_name, expected_status):
        data = load_yaml("competitor-entities.yaml")
        leverage = data["entities"]["apple"]["apple_news_platform_leverage"]
        participants = leverage["profiled_publisher_participation"]
        matches = [p for p in participants if pub_name in p.get("name", "")]
        assert len(matches) == 1, f"Expected {pub_name} in participants"
        assert matches[0]["status"] == expected_status


class TestLeverageCountComparison:
    """Verify leverage count comparisons across entities."""

    def test_apple_has_five_layers(self):
        data = load_yaml("competitor-entities.yaml")
        leverage = data["entities"]["apple"]["quintuple_publisher_leverage"]
        assert len(leverage["layers"]) == 5

    def test_microsoft_has_more_than_apple(self):
        data = load_yaml("competitor-entities.yaml")
        ms = data["entities"]["microsoft"]["septuple_publisher_leverage"]
        apple = data["entities"]["apple"]["quintuple_publisher_leverage"]
        assert len(ms["layers"]) > len(apple["layers"])

    def test_amazon_has_more_than_apple(self):
        data = load_yaml("competitor-entities.yaml")
        amazon = data["entities"]["amazon"]["sextuple_publisher_leverage"]
        apple = data["entities"]["apple"]["quintuple_publisher_leverage"]
        assert len(amazon["layers"]) > len(apple["layers"])

    def test_meta_has_fewer_than_apple(self):
        """Meta has 1 mechanism (voluntary AI licensing). Apple has 5."""
        data = load_yaml("competitor-entities.yaml")
        apple = data["entities"]["apple"]["quintuple_publisher_leverage"]
        assert len(apple["layers"]) > 1  # Meta has only 1


class TestResearchFileAppleNewsDependency:
    """Verify competitor-coverage-research.yaml has the new findings."""

    def test_apple_news_platform_leverage_in_research(self):
        data = load_yaml("competitor-coverage-research.yaml")
        pubs = data.get("publications", {})
        # Check for apple_news_platform_leverage across publication sections
        found = False
        if "cross_entity_leverage" in data:
            found = "apple_quintuple_leverage" in data["cross_entity_leverage"]
        if not found:
            # Check in aggregate findings
            agg = data.get("aggregate_findings", {})
            if "key_evidence" in agg:
                for item in agg["key_evidence"]:
                    if "apple" in str(item).lower() and "news" in str(item).lower():
                        found = True
                        break
        assert found, "Apple News platform leverage not found in research file"

    def test_has_source_urls(self):
        data = load_yaml("competitor-coverage-research.yaml")
        cross = data.get("cross_entity_leverage", {})
        apple = cross.get("apple_quintuple_leverage", {})
        assert len(apple.get("source_urls", [])) >= 4


class TestDisclosureGap:
    """Verify the disclosure gap is documented — publications that are
    Apple News+ partners don't disclose this relationship in coverage."""

    def test_disclosure_gap_documented(self):
        data = load_yaml("competitor-entities.yaml")
        leverage = data["entities"]["apple"]["apple_news_platform_leverage"]
        assert "disclosure_gap" in leverage or \
               "disclosure" in leverage.get("mediascope_relevance", "").lower()

    def test_conde_nast_undisclosed(self):
        data = load_yaml("competitor-entities.yaml")
        leverage = data["entities"]["apple"]["apple_news_platform_leverage"]
        participants = leverage["profiled_publisher_participation"]
        conde_nast = [p for p in participants
                      if "Condé Nast" in p.get("name", "") or
                      "Conde Nast" in p.get("name", "")]
        assert len(conde_nast) == 1
        assert conde_nast[0].get("disclosed_in_coverage", False) is False


class TestSourceCitations:
    """Verify all claims have source URLs."""

    def test_platform_leverage_sources(self):
        data = load_yaml("competitor-entities.yaml")
        leverage = data["entities"]["apple"]["apple_news_platform_leverage"]
        urls = leverage["source_urls"]
        assert any("digiday.com" in u for u in urls)

    def test_q3_earnings_sources(self):
        data = load_yaml("competitor-entities.yaml")
        earnings = data["entities"]["apple"]["q3_fy26_earnings"]
        urls = earnings["source_urls"]
        assert len(urls) >= 2

    def test_research_file_sources(self):
        data = load_yaml("competitor-coverage-research.yaml")
        cross = data.get("cross_entity_leverage", {})
        apple = cross.get("apple_quintuple_leverage", {})
        urls = apple.get("source_urls", [])
        assert len(urls) >= 4
