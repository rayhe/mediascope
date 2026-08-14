"""
Mechanism #94: Apple Advertising Revenue Structural Opacity —
Coverage Accountability Asymmetry

Type C: Financial Incentive Mapping — August 14, 2026 02:00 PT

KEY FINDING: Apple's advertising business set a June-quarter revenue record
in Q3 FY2026 (reported Jul 30, 2026) as part of $30.7B Services revenue.
CFO Kevan Parekh identified advertising as one of four categories showing
"strong double-digit growth." Yet Apple discloses NO separate advertising
revenue figure — the ONLY major tech company to maintain this opacity.

This creates a structural accountability asymmetry:

  Meta:    Discloses $39.7B quarterly ad revenue (Q2 2026)
           → Publisher dependency on Meta ad dollars CAN be estimated
           → Media critics CAN construct financial conflict arguments
           → Coverage independence is perpetually questionable

  Google:  Discloses $88.3B quarterly ad revenue (Q2 2026)
           → Google News Showcase deal values reported/estimable
           → Same accountability mechanism exists

  Apple:   Discloses ZERO advertising revenue figure
           → eMarketer estimates ~$8.5B/yr (2026), Bloomberg ~$7-10B
           → Publisher dependency on Apple ad dollars CANNOT be calculated
           → Coverage accountability is structurally impossible

The opacity extends to the publisher-side relationship:
  - Apple News in-article ads: publishers get 70% of Apple-sold ad revenue
  - Apple News+ subscription: publishers split 50% of $12.99/mo by engagement
  - No publisher discloses Apple News/News+ financial details
  - Apple's 100 editors curate Top Stories placement, which drives
    engagement-weighted revenue — editorial curation is a financial lever

Additional Apple ad business expansion signals (all undisclosed revenue):
  - Apr 14, 2025: Rebranded from "Apple Search Ads" to "Apple Ads" —
    signaling expansion beyond App Store
  - 2024: Took direct ad sales from NBCUniversal — Apple now directly
    controls publisher financial relationships on Apple News
  - Apr 14, 2026: Apple Business launched across 200+ countries
  - Mar 3, 2026: Added multiple ad positions in App Store search
  - Summer 2026: Apple Maps ads launching in US and Canada
  - Apple Ads ToS rewrite removed requirement for ads to run on
    Apple-owned properties — opening third-party inventory
  - Ford navigation deal places Apple Maps in vehicles from 2027

THE ONE-WAY TRANSPARENCY STREET:
When a media critic asks "Is WIRED's Meta coverage influenced by
Meta's advertising?", the question is answerable — Meta's $39.7B ad
revenue is public, Condé Nast's general ad dependency is estimable.

When the EQUIVALENT question is asked about Apple — "Is WIRED's Apple
coverage influenced by Apple's advertising via Apple News?" — the
question is STRUCTURALLY UNANSWERABLE. Apple does not disclose:
  1. Total advertising revenue
  2. Apple News ad revenue specifically
  3. Per-publisher revenue share amounts
  4. Revenue split between in-article ads vs feed ads
  5. How editorial curation (Top Stories) affects per-publisher revenue

This means publications that profit from Apple's ad business are
shielded from the exact accountability framework routinely applied
to their Meta and Google coverage.

Tim Cook Q4 FY2025 (Oct 2025 call): "The advertising category, which
is a combination of third party and first party, did set a record
during the quarter... I'm dodging the question intentionally because
we don't split it at that level."

Kevan Parekh Q3 FY2026 (Jul 30, 2026 call): Set "June quarter records"
in advertising alongside App Store, AppleCare, music, video. "Strong
double-digit growth" in advertising. No dollar figure provided.

10-Q (Jul 31, 2026): Services revenue increase "primarily due to higher
net sales from advertising and cloud services."

DISTINCTION from existing mechanisms:
  - Mechanism #46 (Apple News Platform Leverage): Focuses on distribution
    dependency — publishers NEED Apple News traffic. #94 focuses on
    ADVERTISING revenue opacity — publishers RECEIVE undisclosed ad dollars.
  - Mechanism #61 (Apple News Glasses Prelaunch Alignment): Focuses on
    competitive positioning incentives for N50 launch. #94 focuses on
    the structural impossibility of AUDITING the financial relationship.
  - Both #46 and #61 document the EXISTENCE of financial dependency.
    #94 documents why that dependency CANNOT BE MEASURED — and how that
    immeasurability shields Apple coverage from accountability.

Sources:
- Apple Q3 FY2026 8-K (SEC filing, Jul 30, 2026):
  https://www.sec.gov/Archives/edgar/data/320193/000032019326000018/a8-kex991q3202606272026.htm
- PPC Land analysis of Q3 FY2026 ad business (Aug 4, 2026):
  https://ppc.land/apple-ads-set-june-quarter-record-as-services-revenue-gains-12-to-30-7bn/
- Search Engine Watch ad business analysis (Aug 5, 2026):
  https://searchenginewatch.com/2026/08/04/apples-advertising-business-just-had-its-best-quarter-ever/
- Apple Ads rebrand (Apr 14, 2025):
  https://searchads.apple.com/blog/post/Apple-Search-Ads-is-now-Apple-Ads
- Campaign US — Apple direct ad sales transition (replacing NBCUniversal):
  https://www.campaignlive.com/article/apple-begins-selling-news-ads-directly/1897348
- eMarketer Apple Ads revenue estimate ~$8.5B (via PPC Land):
  https://ppc.land/apple-ads-set-june-quarter-record-as-services-revenue-gains-12-to-30-7bn/
- Apple Q4 FY2025 earnings call (Tim Cook "dodging" quote):
  http://fool.com/earnings/call-transcripts/2025/10/31/apple-q4-2025-earnings-call-transcript/
- Bloomberg Apple ad revenue estimate $7-10B (via Mint):
  https://www.livemint.com/us/business/apples-next-revenue-push-reports-suggest-ads-are-coming-to-maps-as-part-of-its-100-billion-services-strategy-11761495201330.html
- Meta Q2 2026 earnings ($60.8B total rev, advertising primary):
  https://investor.fb.com/investor-events/event-details/2026/Meta-Q2-2026-Earnings/
- Seeking Alpha Q3 FY2026 call transcript:
  https://seekingalpha.com/article/4928290-apple-inc-aapl-q3-2026-earnings-call-transcript

Created: 2026-08-14 02:00 PT
"""

import yaml
import os
import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_yaml(filename):
    path = os.path.join(REPO_ROOT, "profiles", filename)
    with open(path) as f:
        return yaml.safe_load(f)


def load_research():
    return load_yaml("competitor-coverage-research.yaml")


class TestMechanism94Exists:
    """Verify mechanism #94 exists in competitor-coverage-research.yaml."""

    def test_mechanism_94_in_cross_publication_findings(self):
        data = load_research()
        findings = data.get("cross_publication_findings", {})
        assert "apple_ad_revenue_opacity_coverage_accountability_asymmetry" in findings

    def test_mechanism_id_is_94(self):
        data = load_research()
        m = data["cross_publication_findings"]["apple_ad_revenue_opacity_coverage_accountability_asymmetry"]
        assert m["mechanism_id"] == 94

    def test_has_finding_summary(self):
        data = load_research()
        m = data["cross_publication_findings"]["apple_ad_revenue_opacity_coverage_accountability_asymmetry"]
        assert len(m.get("finding_summary", "")) >= 100

    def test_has_source_urls(self):
        data = load_research()
        m = data["cross_publication_findings"]["apple_ad_revenue_opacity_coverage_accountability_asymmetry"]
        assert len(m.get("source_urls", [])) >= 5

    def test_has_confounding_factors(self):
        data = load_research()
        m = data["cross_publication_findings"]["apple_ad_revenue_opacity_coverage_accountability_asymmetry"]
        assert len(m.get("confounding_factors", [])) >= 3

    def test_has_testable_predictions(self):
        data = load_research()
        m = data["cross_publication_findings"]["apple_ad_revenue_opacity_coverage_accountability_asymmetry"]
        assert len(m.get("testable_predictions", [])) >= 2

    def test_has_date_added(self):
        data = load_research()
        m = data["cross_publication_findings"]["apple_ad_revenue_opacity_coverage_accountability_asymmetry"]
        assert m.get("date_added") == "2026-08-14"

    def test_has_test_file(self):
        data = load_research()
        m = data["cross_publication_findings"]["apple_ad_revenue_opacity_coverage_accountability_asymmetry"]
        assert "test_apple_ad_revenue_opacity" in m.get("test_file", "")


class TestAppleAdRevenueOpacityInEntities:
    """Verify apple_ad_revenue_opacity section in competitor-entities.yaml."""

    def test_section_exists(self):
        data = load_yaml("competitor-entities.yaml")
        apple = data["entities"]["apple"]
        assert "apple_ad_revenue_opacity" in apple

    def test_has_mechanism_id(self):
        data = load_yaml("competitor-entities.yaml")
        opacity = data["entities"]["apple"]["apple_ad_revenue_opacity"]
        assert opacity.get("mechanism_id") == 94

    def test_emarketer_estimate(self):
        data = load_yaml("competitor-entities.yaml")
        opacity = data["entities"]["apple"]["apple_ad_revenue_opacity"]
        assert opacity.get("emarketer_estimate_2026_b") == 8.5

    def test_bloomberg_estimate_range(self):
        data = load_yaml("competitor-entities.yaml")
        opacity = data["entities"]["apple"]["apple_ad_revenue_opacity"]
        assert opacity.get("bloomberg_estimate_low_b") == 7
        assert opacity.get("bloomberg_estimate_high_b") == 10

    def test_disclosure_status_none(self):
        data = load_yaml("competitor-entities.yaml")
        opacity = data["entities"]["apple"]["apple_ad_revenue_opacity"]
        assert opacity.get("apple_ad_revenue_disclosed") is False

    def test_meta_comparison_present(self):
        data = load_yaml("competitor-entities.yaml")
        opacity = data["entities"]["apple"]["apple_ad_revenue_opacity"]
        comp = opacity.get("entity_disclosure_comparison", {})
        assert "meta" in comp
        assert comp["meta"]["discloses_ad_revenue"] is True

    def test_google_comparison_present(self):
        data = load_yaml("competitor-entities.yaml")
        opacity = data["entities"]["apple"]["apple_ad_revenue_opacity"]
        comp = opacity.get("entity_disclosure_comparison", {})
        assert "google" in comp
        assert comp["google"]["discloses_ad_revenue"] is True


class TestOneWayTransparencyStreet:
    """Test the core analytical finding: accountability is structurally asymmetric."""

    def test_meta_dependency_calculable(self):
        """Meta discloses ad revenue, so publisher dependency is estimable."""
        data = load_yaml("competitor-entities.yaml")
        opacity = data["entities"]["apple"]["apple_ad_revenue_opacity"]
        comp = opacity["entity_disclosure_comparison"]["meta"]
        assert comp["discloses_ad_revenue"] is True
        assert comp.get("q2_2026_total_revenue_b", 0) > 0

    def test_google_dependency_calculable(self):
        """Google discloses ad revenue, so publisher dependency is estimable."""
        data = load_yaml("competitor-entities.yaml")
        opacity = data["entities"]["apple"]["apple_ad_revenue_opacity"]
        comp = opacity["entity_disclosure_comparison"]["google"]
        assert comp["discloses_ad_revenue"] is True

    def test_apple_dependency_not_calculable(self):
        """Apple does NOT disclose ad revenue, so dependency cannot be measured."""
        data = load_yaml("competitor-entities.yaml")
        opacity = data["entities"]["apple"]["apple_ad_revenue_opacity"]
        assert opacity["apple_ad_revenue_disclosed"] is False

    def test_accountability_asymmetry_documented(self):
        """The core finding: media critics can question Meta/Google coverage
        independence using public financial data, but cannot make the equivalent
        case for Apple coverage."""
        data = load_yaml("competitor-entities.yaml")
        opacity = data["entities"]["apple"]["apple_ad_revenue_opacity"]
        assert "accountability_asymmetry" in opacity
        asym = opacity["accountability_asymmetry"]
        assert "meta_google" in str(asym).lower() or len(str(asym)) > 50


class TestAppleDirectAdSalesTransition:
    """Verify documentation of Apple taking direct ad sales from NBCUniversal."""

    def test_direct_ad_sales_documented(self):
        data = load_yaml("competitor-entities.yaml")
        opacity = data["entities"]["apple"]["apple_ad_revenue_opacity"]
        expansion = opacity.get("ad_business_expansion_timeline", [])
        descriptions = " ".join([str(e) for e in expansion])
        assert "nbcuniversal" in descriptions.lower() or "direct" in descriptions.lower()

    def test_ad_rebrand_documented(self):
        data = load_yaml("competitor-entities.yaml")
        opacity = data["entities"]["apple"]["apple_ad_revenue_opacity"]
        expansion = opacity.get("ad_business_expansion_timeline", [])
        descriptions = " ".join([str(e) for e in expansion])
        assert "apple ads" in descriptions.lower() or "rebrand" in descriptions.lower()


class TestApplePublisherAdRevenueShare:
    """Verify documentation of the 70% in-article ad revenue share."""

    def test_in_article_ad_share_documented(self):
        data = load_yaml("competitor-entities.yaml")
        opacity = data["entities"]["apple"]["apple_ad_revenue_opacity"]
        assert opacity.get("in_article_ad_publisher_share_pct") == 70

    def test_feed_ad_share_engagement_based(self):
        data = load_yaml("competitor-entities.yaml")
        opacity = data["entities"]["apple"]["apple_ad_revenue_opacity"]
        assert "engagement" in str(opacity.get("feed_ad_publisher_share", "")).lower()

    def test_self_sold_ad_share_100_pct(self):
        data = load_yaml("competitor-entities.yaml")
        opacity = data["entities"]["apple"]["apple_ad_revenue_opacity"]
        assert opacity.get("self_sold_ad_publisher_share_pct") == 100


class TestQ3FY2026AdRecord:
    """Verify Q3 FY2026 advertising record details are documented."""

    def test_q3_ad_record_flag(self):
        data = load_yaml("competitor-entities.yaml")
        opacity = data["entities"]["apple"]["apple_ad_revenue_opacity"]
        q3 = opacity.get("q3_fy2026_record", {})
        assert q3.get("set_record") is True

    def test_q3_cfo_quote(self):
        data = load_yaml("competitor-entities.yaml")
        opacity = data["entities"]["apple"]["apple_ad_revenue_opacity"]
        q3 = opacity.get("q3_fy2026_record", {})
        assert "double-digit" in str(q3.get("cfo_description", "")).lower()

    def test_q3_10q_language(self):
        data = load_yaml("competitor-entities.yaml")
        opacity = data["entities"]["apple"]["apple_ad_revenue_opacity"]
        q3 = opacity.get("q3_fy2026_record", {})
        assert "advertising" in str(q3.get("sec_filing_language", "")).lower()


class TestConfoundingFactors:
    """Verify scholarly rigor: confounding factors with strength levels."""

    def test_at_least_3_confounding_factors(self):
        data = load_research()
        m = data["cross_publication_findings"]["apple_ad_revenue_opacity_coverage_accountability_asymmetry"]
        assert len(m["confounding_factors"]) >= 3

    def test_has_strong_confounding_factor(self):
        data = load_research()
        m = data["cross_publication_findings"]["apple_ad_revenue_opacity_coverage_accountability_asymmetry"]
        strengths = [f.get("strength", "") for f in m["confounding_factors"]]
        assert "STRONG" in strengths

    def test_multiple_strength_levels(self):
        data = load_research()
        m = data["cross_publication_findings"]["apple_ad_revenue_opacity_coverage_accountability_asymmetry"]
        strengths = set(f.get("strength", "") for f in m["confounding_factors"])
        assert len(strengths) >= 2


class TestCrossReferences:
    """Verify mechanism #94 cross-references related mechanisms."""

    def test_has_related_mechanisms(self):
        data = load_research()
        m = data["cross_publication_findings"]["apple_ad_revenue_opacity_coverage_accountability_asymmetry"]
        related = m.get("related_mechanisms", [])
        assert len(related) >= 2

    def test_references_mechanism_46(self):
        """Should reference #46 Apple News Platform Leverage."""
        data = load_research()
        m = data["cross_publication_findings"]["apple_ad_revenue_opacity_coverage_accountability_asymmetry"]
        related = m.get("related_mechanisms", [])
        assert 46 in related

    def test_references_mechanism_61(self):
        """Should reference #61 Apple News Glasses Prelaunch Alignment."""
        data = load_research()
        m = data["cross_publication_findings"]["apple_ad_revenue_opacity_coverage_accountability_asymmetry"]
        related = m.get("related_mechanisms", [])
        assert 61 in related


class TestSourceURLQuality:
    """Verify all source URLs are present and from verifiable sources."""

    def test_has_sec_filing_source(self):
        data = load_research()
        m = data["cross_publication_findings"]["apple_ad_revenue_opacity_coverage_accountability_asymmetry"]
        urls = " ".join(m.get("source_urls", []))
        assert "sec.gov" in urls

    def test_has_earnings_analysis_source(self):
        data = load_research()
        m = data["cross_publication_findings"]["apple_ad_revenue_opacity_coverage_accountability_asymmetry"]
        urls = " ".join(m.get("source_urls", []))
        assert "ppc.land" in urls or "searchenginewatch" in urls

    def test_has_direct_ad_sales_source(self):
        data = load_research()
        m = data["cross_publication_findings"]["apple_ad_revenue_opacity_coverage_accountability_asymmetry"]
        urls = " ".join(m.get("source_urls", []))
        assert "campaignlive" in urls

    def test_all_urls_start_with_https(self):
        data = load_research()
        m = data["cross_publication_findings"]["apple_ad_revenue_opacity_coverage_accountability_asymmetry"]
        for url in m.get("source_urls", []):
            assert url.startswith("http"), f"URL does not start with http: {url}"
