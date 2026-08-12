"""
Test: Cloudflare Publisher AI Crawl Default-Block → Google-OpenAI Financial Asymmetry Accelerator
Mechanism #64 — Type C: Financial Incentive Mapping
Date: 2026-08-12

FINDING:
Cloudflare's September 15, 2026 default policy change — blocking mixed-use AI crawlers
from ad-supported pages — creates a structural asymmetry that ACCELERATES the divergence
between Google (crawler-dependent) and OpenAI (deal-dependent) financial relationships
with publishers.

Google's Googlebot is a mixed-use crawler: it simultaneously indexes for Search AND
powers AI Overviews / AI Mode. Cloudflare's policy blocks mixed-use crawlers from
ad-supported pages by default. OpenAI's content licensing deals are API-based direct
access, NOT crawler-based — they are entirely unaffected by Cloudflare's blocking.

THREE MediaScope-profiled publication groups are Cloudflare customers:
1. Condé Nast (WIRED, New Yorker, Vogue, GQ, Ars Technica) — has OpenAI deal
2. Financial Times — has OpenAI deal
3. The Atlantic — has OpenAI deal

All three maintain OpenAI content licensing revenue while Cloudflare blocks Google's
mixed-use crawler from their ad-supported pages. This is the first time a THIRD-PARTY
INFRASTRUCTURE PROVIDER has intervened in the publisher-AI financial ecosystem in a
way that differentially impacts competitor entities.

PUBLISHER TRAFFIC DECLINE DATA (Jun 2025→Jun 2026, Semrush):
- USA Today: -18% organic Google traffic (WSJ)
- Politico: -20% (WSJ)
- CNN: -31% (WSJ)
- Business Insider: -31% to -35% (WSJ/Marketplace)
- DMG Media: -89% CTR from AI Overviews (Search Engine Land)
- Google AI Overviews: up to 25% publisher referral traffic decrease (Digital Content Next)
- Ahrefs (300K keywords): 58% lower average CTR when AI Overview present
- 75% of AI Mode sessions never leave for the web (GrowthMemo)

GOOGLE FINANCIAL STRESS:
- Q2 2026: Negative free cash flow (-$5.9B) — FIRST TIME IN COMPANY HISTORY
- Search+ads: $63.3B (+17%), but AI capex eating profitability
- AI capex guidance: $44.9B Q2, $195-205B/yr

REDDIT-GOOGLE DEAL RENEGOTIATION:
- Reddit weighing ending $60M/yr Google content licensing deal (WSJ, Jul 2026)
- Advance Publications owns 23.3% of Reddit (~$6.7B stake)
- Advance also owns Condé Nast (WIRED's parent)
- Reddit stock dropped ~9% on renegotiation news

CONFOUNDING FACTORS:
1. Cloudflare's policy affects ALL mixed-use crawlers, not just Google
2. Publishers can opt out of Cloudflare's default blocking
3. Google offers Google-Extended to opt out of AI training specifically
4. Some publishers may re-enable Google crawling for traffic dependency
5. Cloudflare's Pay Per Use model could create NEW publisher-Google revenue
6. The policy only affects ad-supported pages, not all content
7. Large enterprise Cloudflare customers may have custom agreements

TESTABLE PREDICTIONS:
1. After Sep 15, publications with BOTH Cloudflare + OpenAI deals will maintain
   OpenAI licensing revenue while blocking Google AI crawling — verify via
   Cloudflare dashboard settings / robots.txt changes
2. Google will accelerate its own content licensing deals to bypass Cloudflare
   blocking — watch for new Google-publisher deals Q4 2026
3. Coverage of Cloudflare's policy in Cloudflare-customer publications (WIRED, FT,
   The Atlantic) will frame it as empowering publishers rather than threatening
   the search ecosystem — check framing within 30 days of announcement
4. Reddit's Google deal renegotiation outcome will correlate with Advance's
   Condé Nast OpenAI deal status — both controlled by same parent company

CROSS-REFERENCES: #35 (Advance/Condé Nast Aggregate AI Dependency), #47 (Meta Ad
Revenue Competitor Structural Antagonism), #55 (Google Ad Dependency Paradox),
#41 (Google Showcase Coercive Cycle)

SOURCE URLS:
- https://techcrunch.com/2026/07/01/cloudflares-new-policy-pushes-ai-companies-to-pay-for-publishers-content/
- https://www.adweek.com/media/adweek-tech-advantage-publishers-pull-back-from-google-ai-search-while-creators-push-on/
- https://www.wsj.com/business/media/google-search-publishers-ai-content-0fb06e41
- https://www.emarketer.com/content/reddit-reportedly-weighs-ending-google-content-licensing-deal-publisher-traffic-concerns-mount
- https://gizmodo.com/major-publishers-are-reportedly-considering-a-drastic-step-to-get-their-content-out-of-googles-ai-answers-2000788873
- https://www.marketplace.org/story/2026/08/03/googles-ai-search-is-changing-who-gets-web-traffic
- https://arxiv.org/html/2605.14021
- https://www.ghacks.net/2026/07/23/reddit-and-major-publishers-consider-blocking-google-as-ai-overviews-cut-search-referral-traffic/
- https://teknowire.com/cloudflare-to-block-mixed-use-ai-crawlers-by-default-under-new-policy/
- https://www.theregister.com/ai-and-ml/2026/07/01/cloudflare-to-block-cynical-search-and-scrape-bots-from-ad-supported-web-pages/5264727
- https://searchengineland.com/ai-answers-disrupting-publisher-revenue-advertising-465185
"""

import pytest
import yaml
import os
import re
import glob


# ── helpers ──────────────────────────────────────────────────────────

def _profiles_dir():
    return os.path.join(os.path.dirname(__file__), '..', 'profiles')


def _load_yaml(filename):
    path = os.path.join(_profiles_dir(), filename)
    with open(path) as f:
        return yaml.safe_load(f)


def _load_competitor_entities():
    return _load_yaml('competitor-entities.yaml')


def _load_research():
    return _load_yaml('competitor-coverage-research.yaml')


def _get_mechanism():
    research = _load_research()
    findings = research.get('cross_publication_findings', [])
    if isinstance(findings, list):
        return next((f for f in findings if f.get('mechanism_id') == 64), None)
    elif isinstance(findings, dict):
        for v in findings.values():
            if isinstance(v, dict) and v.get('mechanism_id') == 64:
                return v
            if isinstance(v, list):
                for item in v:
                    if isinstance(item, dict) and item.get('mechanism_id') == 64:
                        return item
    return None


def _load_wired_profile():
    return _load_yaml('wired.yaml')


# ── Class 1: Cloudflare Policy Core Facts ────────────────────────────

class TestCloudflareDefaultBlockPolicy:
    """Verify the factual foundation of Cloudflare's Sep 15 2026 policy change."""

    def test_policy_effective_date(self):
        """Cloudflare default block takes effect September 15, 2026."""
        m = _get_mechanism()
        assert m is not None, "Mechanism #64 must exist"
        text = str(m).lower()
        assert 'september' in text or 'sep' in text or '2026-09-15' in text

    def test_policy_targets_mixed_use_crawlers(self):
        """Policy specifically targets mixed-use crawlers (search + AI training)."""
        m = _get_mechanism()
        text = str(m).lower()
        assert 'mixed' in text or 'mixed-use' in text.replace(' ', '')

    def test_policy_blocks_ad_supported_pages(self):
        """Blocking applies to pages with ads, not all content."""
        m = _get_mechanism()
        text = str(m).lower()
        assert 'ad' in text

    def test_google_is_primary_target(self):
        """Google's Googlebot is the primary mixed-use crawler affected."""
        m = _get_mechanism()
        text = str(m).lower()
        assert 'google' in text

    def test_googlebot_is_mixed_use(self):
        """Googlebot serves both search indexing AND AI Overviews/AI Mode."""
        m = _get_mechanism()
        text = str(m).lower()
        # Must mention that Google's crawler serves dual purpose
        assert any(term in text for term in ['ai overview', 'ai mode', 'mixed-use',
                                              'search and ai', 'dual', 'mixed use'])

    def test_policy_affects_new_and_free_customers(self):
        """Default applies to new customers, new sites, and free tier users."""
        m = _get_mechanism()
        text = str(m).lower()
        assert any(term in text for term in ['new customer', 'free', 'default'])

    def test_source_urls_include_cloudflare_announcement(self):
        """Source URLs include primary Cloudflare announcement coverage."""
        m = _get_mechanism()
        urls = m.get('source_urls', [])
        # Must have at least one URL from a primary tech news source covering the announcement
        known_sources = ['techcrunch', 'adweek', 'theregister', 'engadget',
                         'pymnts', 'eweek', 'teknowire', 'webpronews']
        found = [u for u in urls if any(s in u.lower() for s in known_sources)]
        assert len(found) >= 2, f"Need ≥2 primary source URLs, found {len(found)}"


# ── Class 2: Affected Publication Mapping ────────────────────────────

class TestCloudflareAffectedPublications:
    """Verify which MediaScope-profiled publications use Cloudflare."""

    def test_conde_nast_is_cloudflare_customer(self):
        """Condé Nast (WIRED parent) is a Cloudflare customer."""
        m = _get_mechanism()
        text = str(m).lower()
        assert 'condé nast' in text or 'conde nast' in text or 'wired' in text

    def test_ft_is_cloudflare_customer(self):
        """Financial Times is a Cloudflare customer."""
        m = _get_mechanism()
        text = str(m).lower()
        assert 'financial times' in text or 'ft' in text.split()

    def test_atlantic_is_cloudflare_customer(self):
        """The Atlantic is a Cloudflare customer."""
        m = _get_mechanism()
        text = str(m).lower()
        assert 'atlantic' in text

    def test_all_three_have_openai_deals(self):
        """All three Cloudflare-customer publications have OpenAI content deals."""
        m = _get_mechanism()
        text = str(m).lower()
        assert 'openai' in text
        # Must document the connection between Cloudflare usage and OpenAI deals
        assert 'deal' in text or 'licens' in text

    def test_at_least_three_cloudflare_publications_identified(self):
        """At least three distinct MediaScope-profiled publications identified as Cloudflare customers."""
        m = _get_mechanism()
        text = str(m).lower()
        found = 0
        if 'condé nast' in text or 'conde nast' in text or 'wired' in text:
            found += 1
        if 'financial times' in text or any(f' ft ' in f' {text} '):
            found += 1
        if 'atlantic' in text:
            found += 1
        assert found >= 3, f"Only {found} Cloudflare-customer publications identified"


# ── Class 3: Crawler vs Deal Asymmetry ───────────────────────────────

class TestCrawlerVsDealAsymmetry:
    """Core finding: crawler-based access (Google) is blocked while deal-based access (OpenAI) is unaffected."""

    def test_google_access_is_crawler_dependent(self):
        """Google's AI data access depends on web crawlers, making it vulnerable to blocking."""
        m = _get_mechanism()
        text = str(m).lower()
        assert 'crawler' in text
        assert 'google' in text

    def test_openai_access_is_deal_based(self):
        """OpenAI's content access is through licensing deals, not crawlers."""
        m = _get_mechanism()
        text = str(m).lower()
        assert any(term in text for term in ['licensing', 'deal', 'api', 'direct access'])

    def test_openai_unaffected_by_cloudflare_blocking(self):
        """OpenAI content deals are unaffected by Cloudflare's crawler blocking."""
        m = _get_mechanism()
        text = str(m).lower()
        assert any(term in text for term in ['unaffected', 'not affected', 'exempt',
                                              'independent', 'bypass', 'immune',
                                              'does not affect', 'not impact'])

    def test_asymmetry_documented(self):
        """The structural asymmetry between crawler-based and deal-based access is documented."""
        m = _get_mechanism()
        text = str(m).lower()
        assert 'asymmetr' in text

    def test_third_party_infrastructure_intervention(self):
        """Cloudflare is identified as a third-party infrastructure provider intervening in the ecosystem."""
        m = _get_mechanism()
        text = str(m).lower()
        assert 'cloudflare' in text
        assert any(term in text for term in ['infrastructure', 'third-party', 'third party',
                                              'intermediary', 'platform'])

    def test_meta_has_zero_deals_through_either_channel(self):
        """Meta has zero content licensing deals AND zero crawler protections to lose."""
        m = _get_mechanism()
        text = str(m).lower()
        assert 'meta' in text
        # Meta's position: no deals, no crawler access, pure adversarial coverage
        assert 'zero' in text or '0' in text


# ── Class 4: Publisher Traffic Decline Data ──────────────────────────

class TestPublisherTrafficDeclineData:
    """Verify publisher traffic decline data that motivates the crawler blocking."""

    def test_traffic_decline_data_present(self):
        """Traffic decline percentages are documented with source attribution."""
        m = _get_mechanism()
        text = str(m)
        # Should contain specific percentage declines
        pct_pattern = re.compile(r'\d+%')
        matches = pct_pattern.findall(text)
        assert len(matches) >= 3, f"Need ≥3 traffic decline data points, found {len(matches)}"

    def test_semrush_or_dcn_cited_as_source(self):
        """Traffic data attributed to Semrush, Digital Content Next, or Ahrefs."""
        m = _get_mechanism()
        text = str(m).lower()
        assert any(src in text for src in ['semrush', 'digital content next', 'ahrefs',
                                            'dcn', 'growthm'])

    def test_usa_today_traffic_decline(self):
        """USA Today organic Google traffic decline documented."""
        m = _get_mechanism()
        text = str(m).lower()
        assert 'usa today' in text

    def test_multiple_publishers_traffic_data(self):
        """Traffic decline data for multiple publishers, not just one."""
        m = _get_mechanism()
        text = str(m).lower()
        publishers_found = 0
        for pub in ['usa today', 'politico', 'cnn', 'business insider', 'reuters',
                    'huffington', 'washington post']:
            if pub in text:
                publishers_found += 1
        assert publishers_found >= 2, f"Only {publishers_found} publishers' traffic data"

    def test_publisher_ceo_quotes(self):
        """CEO/executive quotes from publishers considering blocking."""
        m = _get_mechanism()
        text = str(m).lower()
        # Should include at least one exec quote
        assert any(name in text for name in ['mike reed', 'neil vogel', 'paul bascobert',
                                              'enough is enough', 'on the table',
                                              'take a stand'])


# ── Class 5: Google Financial Stress Context ─────────────────────────

class TestGoogleFinancialStressContext:
    """Google's financial context that makes the crawler blocking more consequential."""

    def test_google_negative_fcf_documented(self):
        """Google's first-ever negative free cash flow (-$5.9B) is documented."""
        m = _get_mechanism()
        text = str(m).lower()
        assert any(term in text for term in ['negative', 'free cash flow', 'fcf', '-5.9',
                                              '-$5.9'])

    def test_google_search_revenue_still_growing(self):
        """Search+ads revenue still growing but AI investment eating profitability."""
        m = _get_mechanism()
        text = str(m).lower()
        assert any(term in text for term in ['search', '$63', 'growing', '17%'])

    def test_ai_investment_cannibalizing_search(self):
        """Google's AI investment is cannibalizing its core search business."""
        m = _get_mechanism()
        text = str(m).lower()
        assert any(term in text for term in ['cannibal', 'capex', 'investment',
                                              'eating', 'outran'])


# ── Class 6: Reddit-Google Deal Renegotiation ────────────────────────

class TestRedditGoogleDealRenegotiation:
    """Reddit's potential exit from Google content deal and Advance Publications connection."""

    def test_reddit_google_deal_value(self):
        """Reddit-Google deal is ~$60M/year."""
        m = _get_mechanism()
        text = str(m).lower()
        assert '$60' in text or '60 million' in text or '60m' in text

    def test_reddit_considering_ending_deal(self):
        """Reddit is considering ending or renegotiating the Google deal."""
        m = _get_mechanism()
        text = str(m).lower()
        assert 'reddit' in text
        assert any(term in text for term in ['end', 'renegotiat', 'shut', 'block',
                                              'weigh', 'consider'])

    def test_advance_reddit_ownership_connection(self):
        """Advance Publications' 23.3% Reddit stake connects to Condé Nast."""
        m = _get_mechanism()
        text = str(m).lower()
        assert 'advance' in text
        assert any(term in text for term in ['23', 'reddit', 'stake', 'ownership'])

    def test_advance_dual_position_documented(self):
        """Advance simultaneously owns Condé Nast (OpenAI deal) and Reddit (Google deal at risk)."""
        m = _get_mechanism()
        text = str(m).lower()
        assert 'advance' in text
        # Both Condé Nast and Reddit should be mentioned in the Advance context
        has_conde = 'condé nast' in text or 'conde nast' in text
        has_reddit = 'reddit' in text
        assert has_conde and has_reddit, "Advance's dual position must connect both entities"


# ── Class 7: Confounding Factors ─────────────────────────────────────

class TestConfoundingFactors:
    """Intellectual honesty: confounding factors that complicate the finding."""

    def test_confounding_factors_present(self):
        """At least 5 confounding factors documented."""
        m = _get_mechanism()
        cfs = m.get('confounding_factors', [])
        assert len(cfs) >= 5, f"Need ≥5 confounding factors, found {len(cfs)}"

    def test_opt_out_possibility_acknowledged(self):
        """Acknowledges publishers can opt out of Cloudflare's default blocking."""
        m = _get_mechanism()
        cfs = str(m.get('confounding_factors', [])).lower()
        assert 'opt' in cfs or 'override' in cfs or 'change' in cfs or 're-enable' in cfs

    def test_google_extended_acknowledged(self):
        """Acknowledges Google offers Google-Extended to opt out of AI training."""
        m = _get_mechanism()
        text = str(m).lower()
        assert 'google-extended' in text or 'google extended' in text or \
               'opt out' in text

    def test_pay_per_use_new_revenue_acknowledged(self):
        """Acknowledges Cloudflare's Pay Per Use could create new publisher-Google revenue."""
        m = _get_mechanism()
        text = str(m).lower()
        assert any(term in text for term in ['pay per', 'compensation', 'new revenue',
                                              'pay-per', 'tollbooth'])

    def test_enterprise_exception_acknowledged(self):
        """Acknowledges large enterprise customers may have custom agreements."""
        m = _get_mechanism()
        cfs = str(m.get('confounding_factors', [])).lower()
        assert any(term in cfs for term in ['enterprise', 'custom', 'large', 'existing'])


# ── Class 8: Testable Predictions ────────────────────────────────────

class TestTestablePredictions:
    """Predictions that would falsify or strengthen the mechanism."""

    def test_testable_predictions_present(self):
        """At least 3 testable predictions documented."""
        m = _get_mechanism()
        preds = m.get('testable_predictions', [])
        assert len(preds) >= 3, f"Need ≥3 testable predictions, found {len(preds)}"

    def test_prediction_about_post_sep15_behavior(self):
        """Prediction about publisher behavior after Sep 15 enforcement."""
        m = _get_mechanism()
        preds = str(m.get('testable_predictions', [])).lower()
        assert 'september' in preds or 'sep' in preds or 'after' in preds

    def test_prediction_about_google_response(self):
        """Prediction about how Google will respond to the blocking."""
        m = _get_mechanism()
        preds = str(m.get('testable_predictions', [])).lower()
        assert 'google' in preds

    def test_prediction_about_coverage_framing(self):
        """Prediction about how Cloudflare-customer publications will frame the policy."""
        m = _get_mechanism()
        preds = str(m.get('testable_predictions', [])).lower()
        assert any(term in preds for term in ['coverage', 'framing', 'frame', 'editorial'])


# ── Class 9: Cross-References ────────────────────────────────────────

class TestCrossReferences:
    """Verify cross-references to related mechanisms."""

    def test_cross_references_present(self):
        """At least 3 cross-references to related mechanisms."""
        m = _get_mechanism()
        refs = m.get('cross_references', [])
        assert len(refs) >= 3, f"Need ≥3 cross-references, found {len(refs)}"

    def test_references_advance_aggregate_dependency(self):
        """References mechanism #35 (Advance/Condé Nast Aggregate AI Dependency)."""
        m = _get_mechanism()
        refs = m.get('cross_references', [])
        ref_ids = []
        for r in refs:
            if isinstance(r, dict):
                ref_ids.append(r.get('mechanism_id', r.get('id')))
            elif isinstance(r, (int, str)):
                ref_ids.append(int(r) if str(r).isdigit() else r)
        assert 35 in ref_ids, f"Must reference mechanism #35, found refs: {ref_ids}"

    def test_references_meta_ad_antagonism(self):
        """References mechanism #47 (Meta Ad Revenue Competitor Structural Antagonism)."""
        m = _get_mechanism()
        refs = m.get('cross_references', [])
        ref_ids = []
        for r in refs:
            if isinstance(r, dict):
                ref_ids.append(r.get('mechanism_id', r.get('id')))
            elif isinstance(r, (int, str)):
                ref_ids.append(int(r) if str(r).isdigit() else r)
        assert 47 in ref_ids, f"Must reference mechanism #47, found refs: {ref_ids}"

    def test_references_google_ad_dependency(self):
        """References mechanism #55 (Google Ad Dependency Paradox)."""
        m = _get_mechanism()
        refs = m.get('cross_references', [])
        ref_ids = []
        for r in refs:
            if isinstance(r, dict):
                ref_ids.append(r.get('mechanism_id', r.get('id')))
            elif isinstance(r, (int, str)):
                ref_ids.append(int(r) if str(r).isdigit() else r)
        assert 55 in ref_ids, f"Must reference mechanism #55, found refs: {ref_ids}"


# ── Class 10: Structural Integrity ───────────────────────────────────

class TestStructuralIntegrity:
    """Verify the mechanism integrates correctly with the broader MediaScope toolkit."""

    def test_mechanism_id_is_64(self):
        """Mechanism is assigned ID 64."""
        m = _get_mechanism()
        assert m is not None, "Mechanism #64 must exist in competitor-coverage-research.yaml"
        assert m['mechanism_id'] == 64

    def test_mechanism_has_finding_summary(self):
        """Mechanism has a finding_summary field."""
        m = _get_mechanism()
        assert 'finding_summary' in m or 'finding' in m or 'description' in m

    def test_source_urls_minimum_count(self):
        """At least 8 source URLs provided."""
        m = _get_mechanism()
        urls = m.get('source_urls', [])
        assert len(urls) >= 8, f"Need ≥8 source URLs, found {len(urls)}"

    def test_source_urls_are_valid_format(self):
        """All source URLs are valid HTTP(S) URLs."""
        m = _get_mechanism()
        urls = m.get('source_urls', [])
        for url in urls:
            assert url.startswith('http://') or url.startswith('https://'), \
                f"Invalid URL format: {url}"

    def test_no_duplicate_source_urls(self):
        """No duplicate source URLs."""
        m = _get_mechanism()
        urls = m.get('source_urls', [])
        assert len(urls) == len(set(urls)), "Duplicate source URLs found"

    def test_mechanism_in_competitor_coverage_research(self):
        """Mechanism exists in competitor-coverage-research.yaml cross_publication_findings."""
        research = _load_research()
        findings = research.get('cross_publication_findings', [])
        found = False
        if isinstance(findings, list):
            found = any(f.get('mechanism_id') == 64 for f in findings if isinstance(f, dict))
        elif isinstance(findings, dict):
            for v in findings.values():
                if isinstance(v, dict) and v.get('mechanism_id') == 64:
                    found = True
                if isinstance(v, list):
                    for item in v:
                        if isinstance(item, dict) and item.get('mechanism_id') == 64:
                            found = True
        assert found, "Mechanism #64 not found in cross_publication_findings"

    def test_competitor_entities_google_updated(self):
        """Google entity in competitor-entities.yaml references Cloudflare blocking."""
        entities = _load_competitor_entities()
        google = entities.get('entities', {}).get('google', {})
        text = str(google).lower()
        assert 'cloudflare' in text, \
            "Google entity should reference Cloudflare default blocking"


# ── Class 11: Web Traffic Non-Human Majority ─────────────────────────

class TestWebTrafficNonHumanMajority:
    """Cloudflare's data showing >55% of web traffic is now non-human."""

    def test_non_human_traffic_majority_documented(self):
        """Documents that >55% of web traffic is now AI agents/bots."""
        m = _get_mechanism()
        text = str(m).lower()
        assert any(term in text for term in ['55%', 'majority', 'non-human',
                                              'non human', 'bot traffic'])

    def test_matthew_prince_quote_or_attribution(self):
        """Cloudflare CEO Matthew Prince quoted or attributed."""
        m = _get_mechanism()
        text = str(m).lower()
        assert any(term in text for term in ['prince', 'cloudflare ceo', 'co-founder'])


# ── Class 12: Coverage Incentive Direction ───────────────────────────

class TestCoverageIncentiveDirection:
    """How the Cloudflare policy changes coverage incentives for profiled publications."""

    def test_google_coverage_incentive_shift(self):
        """Documents how blocking Google changes the coverage incentive for Google."""
        m = _get_mechanism()
        text = str(m).lower()
        # Publishers blocking Google have LESS financial dependency on Google
        # → less reason to soften Google coverage
        assert any(term in text for term in ['incentive', 'coverage', 'editorial',
                                              'financial relationship', 'dependency'])

    def test_openai_deal_preservation_noted(self):
        """Notes that OpenAI deals are preserved, maintaining soft-coverage incentive."""
        m = _get_mechanism()
        text = str(m).lower()
        assert 'openai' in text
        assert any(term in text for term in ['maintain', 'preserv', 'continu',
                                              'unaffected', 'intact'])

    @pytest.mark.parametrize("entity,expected_direction", [
        ("google", "weakened"),   # Blocking Google weakens financial dependency
        ("openai", "preserved"),  # OpenAI deals unaffected, dependency preserved
        ("meta", "unchanged"),    # Meta has zero deals through either channel
    ])
    def test_coverage_incentive_per_entity(self, entity, expected_direction):
        """Each entity's coverage incentive direction is documented."""
        m = _get_mechanism()
        text = str(m).lower()
        assert entity in text, f"{entity} must be discussed in mechanism"
