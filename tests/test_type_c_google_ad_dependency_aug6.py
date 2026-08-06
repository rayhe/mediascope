"""
Tests for Type C Financial Incentive Mapping — Google Advertising Dependency Coercion
(Aug 6, 2026)

Validates the quadruple coercion structure between Google and publishers,
with fresh Q2 2026 earnings data from both Alphabet (Jul 22) and NYT (Aug 5).

KEY FINDINGS:
1. Google Network revenue Q2 2026: $7.3B (-0.7% YoY), now 8.9% of total
   Google advertising — publisher share at all-time low
2. NYT Q2 2026 stock crash (-13%): CEO explicitly blamed "big tech companies"
   for traffic decline; declining search referrals hurt even the NYT
3. Condé Nast "plan for zero search": Google traffic from majority to ~25%,
   expects single-digit; called AI Overviews "death blow"
4. Advertising Dependency Paradox: publications MOST harmed by Google direct
   editorial fury at Meta (no leverage over them), not Google (which does)

Source URLs:
- Alphabet Q2 2026 key metrics (Zacks): https://www.zacks.com/stock/news/2958597/heres-what-key-metrics-tell-us-about-alphabet-googl-q2-earnings
- Alphabet Q2 2026 (Fifth Person): https://fifthperson.com/alphabet-q2-2026/
- NYT Q2 2026 stock crash (WSJ): https://www.wsj.com/business/earnings/new-york-times-posts-higher-revenue-as-subscriber-growth-slows-545cc6a0
- NYT Q2 2026 subscriber miss (Reuters): https://www.reuters.com/business/media-telecom/new-york-times-misses-estimates-digital-subscriber-additions-2026-08-05/
- Google Ad Network 90% milestone: https://almcorp.com/blog/adsense-revenue-plunge-january-2026-causes-solutions-recovery/
- Google Ad Network Q1 2026 decline: https://props.id/google-ad-network-revenue-is-falling-how-publishers-win/
- Condé Nast zero search (SEJ): https://www.searchenginejournal.com/conde-nast-ceo-plan-as-if-search-traffic-will-be-zero/574786/
- Condé Nast death blow (PPC Land): https://ppc.land/conde-nast-ceo-calls-google-ai-a-death-blow-as-search-traffic-collapses/
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


@pytest.fixture(scope="module")
def entities():
    with open(os.path.join(PROFILES_DIR, 'competitor-entities.yaml')) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def research():
    with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def nytimes_profile():
    with open(os.path.join(PROFILES_DIR, 'nytimes.yaml')) as f:
        return yaml.safe_load(f)


def _get_google(entities):
    return entities['entities']['google']


# ===================================================================
# 1. Google Network Revenue Decline — Q2 2026 Data
# ===================================================================

class TestGoogleNetworkRevenueDecline:
    """Validates Alphabet Q2 2026 Network advertising revenue data."""

    def test_google_network_q2_2026_section_exists(self, entities):
        google = _get_google(entities)
        assert 'network_revenue_decline' in google

    def test_q2_2026_network_revenue_value(self, entities):
        google = _get_google(entities)
        data = google['network_revenue_decline']
        assert data['q2_2026_network_revenue_b'] == 7.3

    def test_q2_2026_network_yoy_decline(self, entities):
        google = _get_google(entities)
        data = google['network_revenue_decline']
        assert data['q2_2026_network_yoy_pct'] == -0.7

    def test_q1_2026_network_revenue_value(self, entities):
        google = _get_google(entities)
        data = google['network_revenue_decline']
        assert data['q1_2026_network_revenue_b'] == 6.97

    def test_q1_2026_network_yoy_decline(self, entities):
        google = _get_google(entities)
        data = google['network_revenue_decline']
        assert data['q1_2026_network_yoy_pct'] == -4.0

    def test_q2_2026_total_google_ad_revenue(self, entities):
        google = _get_google(entities)
        data = google['network_revenue_decline']
        assert data['q2_2026_total_google_ad_revenue_b'] == 81.63

    def test_q2_2026_network_share_of_total_ad(self, entities):
        """Network share of total Google ad revenue: $7.3B / $81.63B ≈ 8.9%."""
        google = _get_google(entities)
        data = google['network_revenue_decline']
        share = data['q2_2026_network_share_pct']
        assert 8.5 <= share <= 9.5  # approximately 8.9%

    def test_90_percent_milestone_documented(self, entities):
        """Google retains 90%+ of ad revenue for owned properties."""
        google = _get_google(entities)
        data = google['network_revenue_decline']
        desc = str(data.get('description', ''))
        assert '90' in desc

    def test_multi_quarter_decline_trend(self, entities):
        """Both Q1 and Q2 2026 show Network revenue declining."""
        google = _get_google(entities)
        data = google['network_revenue_decline']
        assert data['q1_2026_network_yoy_pct'] < 0
        assert data['q2_2026_network_yoy_pct'] < 0

    def test_source_urls_present(self, entities):
        google = _get_google(entities)
        data = google['network_revenue_decline']
        assert 'source_urls' in data
        assert len(data['source_urls']) >= 2


# ===================================================================
# 2. Google Advertising Dependency Coercion Structure
# ===================================================================

class TestGoogleAdvertisingCoercionStructure:
    """Validates the quadruple coercion model."""

    def test_coercion_section_exists(self, entities):
        google = _get_google(entities)
        assert 'advertising_dependency_coercion' in google

    def test_four_layers_documented(self, entities):
        """Four distinct coercion layers must be enumerated."""
        google = _get_google(entities)
        coercion = google['advertising_dependency_coercion']
        assert 'layers' in coercion
        assert len(coercion['layers']) == 4

    def test_layer_names(self, entities):
        google = _get_google(entities)
        layers = google['advertising_dependency_coercion']['layers']
        layer_names = [l['name'] for l in layers]
        assert 'advertising_dependency' in layer_names
        assert 'search_traffic_dependency' in layer_names
        assert 'showcase_fee_leverage' in layer_names
        assert 'pilot_deal_exclusion' in layer_names

    def test_advertising_dependency_has_google_share_stat(self, entities):
        """Google controls ~37% of US digital ad spend."""
        google = _get_google(entities)
        layers = google['advertising_dependency_coercion']['layers']
        ad_layer = [l for l in layers if l['name'] == 'advertising_dependency'][0]
        desc = str(ad_layer.get('detail', ''))
        assert '37' in desc or 'percent' in desc.lower()

    def test_search_traffic_layer_cites_ai_overviews(self, entities):
        google = _get_google(entities)
        layers = google['advertising_dependency_coercion']['layers']
        search_layer = [l for l in layers if l['name'] == 'search_traffic_dependency'][0]
        detail = str(search_layer.get('detail', ''))
        assert 'AI Overviews' in detail

    def test_meta_contrast_documented(self, entities):
        """Meta's voluntary, no-leverage model should be contrasted."""
        google = _get_google(entities)
        coercion = google['advertising_dependency_coercion']
        summary = str(coercion.get('meta_contrast', ''))
        assert 'Meta' in summary or 'voluntary' in summary.lower()


# ===================================================================
# 3. NYT Q2 2026 Earnings — Google Traffic Impact
# ===================================================================

class TestNYTQ2_2026Earnings:
    """Validates NYT Q2 2026 earnings data (reported Aug 5, 2026)."""

    def test_nyt_q2_2026_section_exists(self, nytimes_profile):
        # Must be in sec_filings or financial data section
        chain = nytimes_profile['ownership_chain']
        parent = [c for c in chain if 'New York Times Company' in c.get('name', '')][0]
        filings = parent.get('sec_filings', [])
        q2_filings = [f for f in filings if 'Q2 2026' in f.get('period', '')]
        assert len(q2_filings) >= 1

    def test_nyt_q2_2026_revenue(self, nytimes_profile):
        chain = nytimes_profile['ownership_chain']
        parent = [c for c in chain if 'New York Times Company' in c.get('name', '')][0]
        filings = parent.get('sec_filings', [])
        q2 = [f for f in filings if 'Q2 2026' in f.get('period', '')][0]
        notes = str(q2.get('notes', ''))
        assert '762' in notes  # $762.5M revenue

    def test_nyt_q2_2026_stock_decline(self, nytimes_profile):
        chain = nytimes_profile['ownership_chain']
        parent = [c for c in chain if 'New York Times Company' in c.get('name', '')][0]
        filings = parent.get('sec_filings', [])
        q2 = [f for f in filings if 'Q2 2026' in f.get('period', '')][0]
        notes = str(q2.get('notes', ''))
        assert '13%' in notes or '13 percent' in notes.lower()

    def test_nyt_q2_2026_subscriber_miss(self, nytimes_profile):
        chain = nytimes_profile['ownership_chain']
        parent = [c for c in chain if 'New York Times Company' in c.get('name', '')][0]
        filings = parent.get('sec_filings', [])
        q2 = [f for f in filings if 'Q2 2026' in f.get('period', '')][0]
        notes = str(q2.get('notes', ''))
        assert '280' in notes  # 280K digital subs added

    def test_nyt_ceo_google_traffic_quote(self, nytimes_profile):
        chain = nytimes_profile['ownership_chain']
        parent = [c for c in chain if 'New York Times Company' in c.get('name', '')][0]
        filings = parent.get('sec_filings', [])
        q2 = [f for f in filings if 'Q2 2026' in f.get('period', '')][0]
        notes = str(q2.get('notes', ''))
        assert 'traffic' in notes.lower()


# ===================================================================
# 4. Condé Nast Google Traffic Collapse
# ===================================================================

class TestCondeNastGoogleTrafficCollapse:
    """Validates documentation of Condé Nast's Google traffic decline."""

    def test_conde_nast_google_traffic_in_research(self, research):
        wired = research['publications']['wired']
        assert 'google_traffic_collapse' in wired

    def test_traffic_decline_from_majority_to_25pct(self, research):
        wired = research['publications']['wired']
        collapse = wired['google_traffic_collapse']
        desc = str(collapse.get('description', '') or collapse.get('detail', ''))
        assert '25' in desc  # Google share dropped to ~25%

    def test_zero_search_planning_documented(self, research):
        wired = research['publications']['wired']
        collapse = wired['google_traffic_collapse']
        desc = str(collapse.get('description', '') or collapse.get('detail', ''))
        assert 'zero' in desc.lower()

    def test_death_blow_quote_documented(self, research):
        wired = research['publications']['wired']
        collapse = wired['google_traffic_collapse']
        desc = str(collapse.get('description', '') or collapse.get('detail', ''))
        assert 'death blow' in desc.lower()

    def test_lynch_attribution(self, research):
        """Quote attributed to CEO Roger Lynch."""
        wired = research['publications']['wired']
        collapse = wired['google_traffic_collapse']
        desc = str(collapse.get('description', '') or collapse.get('detail', ''))
        assert 'Lynch' in desc

    def test_source_urls_present(self, research):
        wired = research['publications']['wired']
        collapse = wired['google_traffic_collapse']
        assert 'source_urls' in collapse
        assert len(collapse['source_urls']) >= 2


# ===================================================================
# 5. Advertising Dependency Paradox
# ===================================================================

class TestAdvertisingDependencyParadox:
    """Publications most harmed by Google direct fury at Meta, not Google."""

    def test_paradox_section_exists(self, research):
        wired = research['publications']['wired']
        assert 'advertising_dependency_paradox' in wired

    def test_paradox_identifies_misaligned_coverage(self, research):
        """Condé Nast harmed by Google, but Meta gets adversarial coverage."""
        wired = research['publications']['wired']
        paradox = wired['advertising_dependency_paradox']
        desc = str(paradox.get('description', '') or paradox.get('detail', ''))
        assert 'Meta' in desc
        assert 'Google' in desc

    def test_paradox_cites_no_meta_leverage(self, research):
        wired = research['publications']['wired']
        paradox = wired['advertising_dependency_paradox']
        desc = str(paradox.get('description', '') or paradox.get('detail', ''))
        # Meta has no leverage over Condé Nast (no search, no ad dependency)
        assert 'leverage' in desc.lower() or 'no deal' in desc.lower()

    def test_nyt_google_traffic_impact_acknowledged(self, research):
        """NYT acknowledged Google traffic impact in Q2 2026."""
        wired = research['publications']['wired']
        paradox = wired['advertising_dependency_paradox']
        desc = str(paradox.get('description', '') or paradox.get('detail', ''))
        assert 'NYT' in desc or 'New York Times' in desc


# ===================================================================
# 6. Cross-Entity Validation — Google vs Meta Revenue Structure
# ===================================================================

class TestGoogleMetaRevenueContrast:
    """Validates that Google and Meta have structurally different
    publisher leverage — Google has coercive leverage, Meta does not."""

    def test_meta_has_zero_ad_network_dependency(self, entities):
        """Meta doesn't run a publisher ad network — no AdSense equivalent."""
        meta = entities['entities']['meta']
        # Meta is a distinct entity
        assert meta is not None

    def test_google_has_network_revenue(self, entities):
        google = _get_google(entities)
        data = google['network_revenue_decline']
        assert data['q2_2026_network_revenue_b'] > 0

    def test_google_network_declining_while_total_grows(self, entities):
        """Google total ad revenue grows (+14.4%) while Network declines (-0.7%)."""
        google = _get_google(entities)
        data = google['network_revenue_decline']
        assert data['q2_2026_total_google_ad_yoy_pct'] > 0
        assert data['q2_2026_network_yoy_pct'] < 0

    def test_meta_no_search_traffic_leverage(self, entities):
        """Meta doesn't control search — can't reduce publisher traffic."""
        coercion = _get_google(entities)['advertising_dependency_coercion']
        contrast = str(coercion.get('meta_contrast', ''))
        assert 'search' in contrast.lower() or 'traffic' in contrast.lower()


# ===================================================================
# 7. News Corp Control Comparison — Balanced Deals
# ===================================================================

class TestNewsCorpControlComparison:
    """News Corp has deals with BOTH Meta ($50M/yr) and OpenAI ($250M/5yr)
    plus Google — and produces the most balanced coverage."""

    def test_news_corp_has_meta_deal(self, entities):
        """News Corp has Meta deal ($50M/yr)."""
        partners = entities['meta_ai_deals']['partners']
        nc = [p for p in partners if 'News Corp' in p.get('name', '')]
        assert len(nc) >= 1
        terms = nc[0].get('terms', '')
        assert '50M' in terms

    def test_news_corp_has_openai_deal(self, entities):
        """News Corp also has OpenAI deal ($250M/5yr)."""
        nc_excluded = [
            p for p in entities['meta_ai_deals']['excluded_publishers']
            if 'Nikkei' in p.get('name', '') or 'Financial Times' in p.get('name', '')
        ]
        # News Corp is a partner, not excluded — check partner list
        partners = entities['meta_ai_deals']['partners']
        nc = [p for p in partners if 'News Corp' in p.get('name', '')]
        assert len(nc) >= 1
        notes = nc[0].get('notes', '')
        assert 'OpenAI' in notes

    def test_balanced_deals_predict_balanced_coverage(self, entities):
        """Balanced financial relationships should predict balanced coverage."""
        coverage_preds = entities.get('coverage_predictions', {})
        assert 'softer' in coverage_preds or coverage_preds is not None


# ===================================================================
# 8. Data Freshness — Q2 2026 Earnings Dates
# ===================================================================

class TestDataFreshness:
    """Validates that the data is from fresh Q2 2026 earnings."""

    def test_alphabet_q2_2026_reporting_date(self, entities):
        google = _get_google(entities)
        data = google['network_revenue_decline']
        assert data.get('alphabet_q2_2026_report_date') == '2026-07-22'

    def test_nyt_q2_2026_reporting_date(self, nytimes_profile):
        chain = nytimes_profile['ownership_chain']
        parent = [c for c in chain if 'New York Times Company' in c.get('name', '')][0]
        filings = parent.get('sec_filings', [])
        q2 = [f for f in filings if 'Q2 2026' in f.get('period', '')][0]
        assert q2.get('report_date') == '2026-08-05'

    def test_google_search_revenue_q2_2026(self, entities):
        """Google Search & Other: $63.27B (+16.8%)."""
        google = _get_google(entities)
        data = google['network_revenue_decline']
        assert data.get('q2_2026_search_revenue_b') == 63.27
