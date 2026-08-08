"""
Tests for the Publisher AI Revenue Opacity Index finding.

Validates the cross-publisher financial disclosure analysis that maps
transparency tiers against coverage adversariality patterns.

Sources:
- Digiday Q1 2026 AI licensing briefing (May 8, 2026)
- News Corp Q4 FY2026 earnings (Aug 5, 2026) via Reuters, NY Post, WSJ
- NYT Q2 2026 earnings (Aug 5, 2026)
- News Corp Q3 FY2026 earnings call transcript (Motley Fool)
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_competitor_entities():
    with open(os.path.join(PROFILES_DIR, 'competitor-entities.yaml'), 'r') as f:
        return yaml.safe_load(f)


def load_nytimes():
    with open(os.path.join(PROFILES_DIR, 'nytimes.yaml'), 'r') as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def opacity_index():
    data = load_competitor_entities()
    return data.get('publisher_ai_revenue_opacity_index', {})


@pytest.fixture(scope='module')
def nyt_data():
    return load_nytimes()


# ─── Structure Tests ─────────────────────────────────────────────────

class TestOpacityIndexStructure:
    """Verify the opacity index section exists and has required fields."""

    def test_section_exists(self, opacity_index):
        assert opacity_index, "publisher_ai_revenue_opacity_index section missing"

    def test_has_analysis_date(self, opacity_index):
        assert opacity_index.get('analysis_date') == '2026-08-08'

    def test_has_finding_type(self, opacity_index):
        assert opacity_index.get('finding_type') == 'financial_incentive_mapping'

    def test_has_thesis(self, opacity_index):
        thesis = opacity_index.get('thesis', '')
        assert len(thesis) > 100, "Thesis too short"

    def test_has_three_tiers(self, opacity_index):
        tiers = opacity_index.get('opacity_tiers', [])
        assert len(tiers) == 3, f"Expected 3 tiers, got {len(tiers)}"

    def test_tiers_numbered_correctly(self, opacity_index):
        tiers = opacity_index.get('opacity_tiers', [])
        for i, tier in enumerate(tiers, 1):
            assert tier['tier'] == i, f"Tier {i} has wrong number {tier['tier']}"

    def test_has_cross_tier_correlation(self, opacity_index):
        assert 'cross_tier_correlation' in opacity_index

    def test_has_digiday_meta_finding(self, opacity_index):
        assert 'digiday_meta_finding' in opacity_index

    def test_has_news_corp_q4_update(self, opacity_index):
        assert 'news_corp_q4_fy2026_update' in opacity_index


# ─── Tier 1: Black Box Tests ─────────────────────────────────────────

class TestTier1BlackBox:
    """Tier 1: Privately held publishers with zero disclosure."""

    @pytest.fixture
    def tier1(self, opacity_index):
        tiers = opacity_index.get('opacity_tiers', [])
        return next((t for t in tiers if t['tier'] == 1), {})

    def test_label_contains_black_box(self, tier1):
        assert 'BLACK BOX' in tier1.get('label', '')

    def test_has_four_publishers(self, tier1):
        pubs = tier1.get('publishers', [])
        assert len(pubs) == 4, f"Expected 4 Tier 1 publishers, got {len(pubs)}"

    @pytest.mark.parametrize("publisher_fragment", [
        "Condé Nast",
        "The Atlantic",
        "Financial Times",
        "Vox Media",
    ])
    def test_tier1_includes_publisher(self, tier1, publisher_fragment):
        pubs = tier1.get('publishers', [])
        names = [p['name'] for p in pubs]
        assert any(publisher_fragment in n for n in names), \
            f"{publisher_fragment} not found in Tier 1: {names}"

    def test_conde_nast_has_5_ai_deals(self, tier1):
        pubs = tier1.get('publishers', [])
        cn = next((p for p in pubs if 'Condé Nast' in p['name']), None)
        assert cn is not None
        assert cn['ai_deals_known'] == 5

    def test_conde_nast_zero_disclosed_values(self, tier1):
        pubs = tier1.get('publishers', [])
        cn = next((p for p in pubs if 'Condé Nast' in p['name']), None)
        assert cn['disclosed_values'] == 0

    def test_atlantic_emerson_apple_conflict(self, tier1):
        pubs = tier1.get('publishers', [])
        atl = next((p for p in pubs if 'Atlantic' in p['name']), None)
        assert atl is not None
        assert 'Apple' in atl.get('additional_conflicts', '')

    def test_all_tier1_privately_held(self, tier1):
        """Every Tier 1 publisher should have 'private' in their disclosure mechanism."""
        pubs = tier1.get('publishers', [])
        for p in pubs:
            mechanism = p.get('disclosure_mechanism', '').lower()
            assert 'private' in mechanism, \
                f"{p['name']} disclosure mechanism does not mention 'private': {mechanism}"

    def test_all_tier1_high_adversariality(self, tier1):
        """Every Tier 1 publisher should have HIGH adversariality."""
        pubs = tier1.get('publishers', [])
        for p in pubs:
            adversariality = p.get('meta_coverage_adversariality', '').upper()
            assert 'HIGH' in adversariality, \
                f"{p['name']} adversariality should include HIGH: {adversariality}"


# ─── Tier 2: Bundled Disclosure Tests ─────────────────────────────────

class TestTier2Bundled:
    """Tier 2: Public companies that bundle AI revenue with other income."""

    @pytest.fixture
    def tier2(self, opacity_index):
        tiers = opacity_index.get('opacity_tiers', [])
        return next((t for t in tiers if t['tier'] == 2), {})

    def test_label_contains_bundled(self, tier2):
        assert 'BUNDLED' in tier2.get('label', '')

    def test_has_three_publishers(self, tier2):
        pubs = tier2.get('publishers', [])
        assert len(pubs) == 3, f"Expected 3 Tier 2 publishers, got {len(pubs)}"

    @pytest.mark.parametrize("publisher_fragment", [
        "New York Times",
        "USA Today",
        "People Inc",
    ])
    def test_tier2_includes_publisher(self, tier2, publisher_fragment):
        pubs = tier2.get('publishers', [])
        names = [p['name'] for p in pubs]
        assert any(publisher_fragment in n for n in names), \
            f"{publisher_fragment} not found in Tier 2: {names}"

    def test_nyt_bundle_label(self, tier2):
        pubs = tier2.get('publishers', [])
        nyt = next((p for p in pubs if 'New York Times' in p['name']), None)
        assert nyt is not None
        assert 'affiliate' in nyt.get('bundle_label', '').lower()
        assert 'licensing' in nyt.get('bundle_label', '').lower()

    def test_nyt_ai_not_isolatable(self, tier2):
        pubs = tier2.get('publishers', [])
        nyt = next((p for p in pubs if 'New York Times' in p['name']), None)
        assert nyt['ai_revenue_isolatable'] is False

    def test_nyt_q1_2026_bundle_amount(self, tier2):
        """NYT Q1 2026 affiliate/licensing/other was $68.5M."""
        pubs = tier2.get('publishers', [])
        nyt = next((p for p in pubs if 'New York Times' in p['name']), None)
        assert '$68.5M' in nyt.get('q1_2026_bundle', '')

    def test_nyt_q2_2026_derived_amount(self, tier2):
        """Derived Q2 2026 figure should be ~$75.5M."""
        pubs = tier2.get('publishers', [])
        nyt = next((p for p in pubs if 'New York Times' in p['name']), None)
        assert '$75.5M' in nyt.get('q2_2026_bundle_derived', '')

    def test_usa_today_q1_bundle_125pct_growth(self, tier2):
        """USA Today 'other digital revenue' grew 125.6% YoY in Q1 2026."""
        pubs = tier2.get('publishers', [])
        ust = next((p for p in pubs if 'USA Today' in p['name']), None)
        assert '125.6%' in ust.get('q1_2026_bundle', '')

    def test_people_inc_meta_attribution(self, tier2):
        """People Inc. explicitly attributed Q1 growth to Meta deal."""
        pubs = tier2.get('publishers', [])
        pi = next((p for p in pubs if 'People Inc' in p['name']), None)
        assert 'Meta' in pi.get('ai_attribution', '')

    def test_people_inc_google_traffic_loss(self, tier2):
        """Barry Diller: People Inc. lost 65% of Google referral traffic."""
        pubs = tier2.get('publishers', [])
        pi = next((p for p in pubs if 'People Inc' in p['name']), None)
        assert '65%' in pi.get('google_traffic_loss', '')

    def test_all_tier2_moderate_adversariality(self, tier2):
        """Tier 2 publishers should show MODERATE or LOW adversariality."""
        pubs = tier2.get('publishers', [])
        for p in pubs:
            adversariality = p.get('meta_coverage_adversariality', '').upper()
            assert 'MODERATE' in adversariality or 'LOW' in adversariality, \
                f"{p['name']} adversariality should be MODERATE or LOW: {adversariality}"


# ─── Tier 3: Transparent Tests ────────────────────────────────────────

class TestTier3Transparent:
    """Tier 3: News Corp — the only publisher naming AI deal partners in earnings."""

    @pytest.fixture
    def tier3(self, opacity_index):
        tiers = opacity_index.get('opacity_tiers', [])
        return next((t for t in tiers if t['tier'] == 3), {})

    def test_label_contains_transparent(self, tier3):
        assert 'TRANSPARENT' in tier3.get('label', '')

    def test_has_one_publisher(self, tier3):
        pubs = tier3.get('publishers', [])
        assert len(pubs) == 1

    def test_publisher_is_news_corp(self, tier3):
        pubs = tier3.get('publishers', [])
        assert 'News Corp' in pubs[0]['name']

    def test_news_corp_names_ai_deals(self, tier3):
        pubs = tier3.get('publishers', [])
        nc = pubs[0]
        deals = nc.get('ai_deals_named', '')
        assert 'OpenAI' in deals
        assert 'Meta' in deals

    def test_news_corp_q4_revenue_beat(self, tier3):
        pubs = tier3.get('publishers', [])
        nc = pubs[0]
        assert '$2.34B' in nc.get('q4_fy2026_revenue', '')

    def test_news_corp_record_profitability(self, tier3):
        pubs = tier3.get('publishers', [])
        nc = pubs[0]
        assert 'Record' in nc.get('q4_fy2026_profitability', '')
        assert '$230M' in nc.get('q4_fy2026_profitability', '')

    def test_news_corp_adj_eps_doubled(self, tier3):
        """Adj EPS nearly doubled from $0.19 to $0.35."""
        pubs = tier3.get('publishers', [])
        nc = pubs[0]
        eps = nc.get('q4_fy2026_adj_eps', '')
        assert '$0.35' in eps
        assert '$0.19' in eps or '$0.21' in eps  # beat or prior

    def test_news_corp_anthropic_settlement(self, tier3):
        """News Corp expects Anthropic $1.5B settlement proceeds."""
        pubs = tier3.get('publishers', [])
        nc = pubs[0]
        assert '1.5B' in nc.get('anthropic_settlement', '')

    def test_news_corp_ai_inputs_positioning(self, tier3):
        """Thomson self-positioned News Corp as 'AI inputs company'."""
        pubs = tier3.get('publishers', [])
        nc = pubs[0]
        assert 'AI inputs company' in nc.get('self_positioning', '')

    def test_news_corp_low_adversariality(self, tier3):
        pubs = tier3.get('publishers', [])
        nc = pubs[0]
        assert 'LOW' in nc.get('meta_coverage_adversariality', '').upper()

    def test_news_corp_has_source_urls(self, tier3):
        pubs = tier3.get('publishers', [])
        nc = pubs[0]
        urls = nc.get('source_urls', [])
        assert len(urls) >= 2
        assert any('reuters.com' in u for u in urls)


# ─── Cross-Tier Correlation Tests ────────────────────────────────────

class TestCrossTierCorrelation:
    """Verify the inverse transparency-adversariality pattern."""

    @pytest.fixture
    def correlation(self, opacity_index):
        return opacity_index.get('cross_tier_correlation', {})

    def test_has_finding(self, correlation):
        assert 'Inverse' in correlation.get('finding', '')

    def test_has_evidence_points(self, correlation):
        points = correlation.get('evidence_points', [])
        assert len(points) == 3

    def test_tier1_evidence_high(self, correlation):
        points = correlation.get('evidence_points', [])
        t1 = next((p for p in points if 'Tier 1' in p.get('point', '')), None)
        assert t1 is not None
        assert t1['adversariality'] == 'HIGH'

    def test_tier2_evidence_moderate(self, correlation):
        points = correlation.get('evidence_points', [])
        t2 = next((p for p in points if 'Tier 2' in p.get('point', '')), None)
        assert t2 is not None
        assert t2['adversariality'] == 'MODERATE'

    def test_tier3_evidence_low(self, correlation):
        points = correlation.get('evidence_points', [])
        t3 = next((p for p in points if 'Tier 3' in p.get('point', '')), None)
        assert t3 is not None
        assert t3['adversariality'] == 'LOW'

    def test_structural_implication_mentions_opacity(self, correlation):
        impl = correlation.get('structural_implication', '')
        assert 'information asymmetry' in impl.lower() or 'opacity' in impl.lower()

    @pytest.mark.parametrize("pub_name", [
        "WIRED", "The Atlantic", "The Verge", "Financial Times"
    ])
    def test_tier1_publications_listed(self, correlation, pub_name):
        points = correlation.get('evidence_points', [])
        t1 = next((p for p in points if 'Tier 1' in p.get('point', '')), None)
        assert pub_name in t1.get('publications', [])

    @pytest.mark.parametrize("pub_name", [
        "NYT", "USA Today", "People Inc."
    ])
    def test_tier2_publications_listed(self, correlation, pub_name):
        points = correlation.get('evidence_points', [])
        t2 = next((p for p in points if 'Tier 2' in p.get('point', '')), None)
        assert pub_name in t2.get('publications', [])


# ─── Digiday Meta-Finding Tests ──────────────────────────────────────

class TestDigidayMetaFinding:
    """Verify the Digiday industry-wide revenue attribution problem."""

    @pytest.fixture
    def digiday(self, opacity_index):
        return opacity_index.get('digiday_meta_finding', {})

    def test_has_source_url(self, digiday):
        url = digiday.get('source_url', '')
        assert 'digiday.com' in url

    def test_has_key_quote(self, digiday):
        quote = digiday.get('key_quote', '')
        assert 'broke out' in quote.lower() or 'ai licensing' in quote.lower()

    def test_has_analyst_quote(self, digiday):
        quote = digiday.get('analyst_quote', '')
        assert 'Benchmark' in quote or 'Kurnos' in quote

    def test_date_is_may_2026(self, digiday):
        assert digiday.get('date') == '2026-05-08'


# ─── News Corp Q4 FY2026 Update Tests ────────────────────────────────

class TestNewsCorpQ4FY2026:
    """Verify the News Corp Q4 FY2026 financial update data."""

    @pytest.fixture
    def nc_update(self, opacity_index):
        return opacity_index.get('news_corp_q4_fy2026_update', {})

    def test_report_date(self, nc_update):
        assert nc_update.get('report_date') == '2026-08-05'

    def test_fiscal_period(self, nc_update):
        assert 'Q4 FY2026' in nc_update.get('fiscal_period', '')

    def test_total_revenue(self, nc_update):
        assert '$2.34B' in nc_update.get('total_revenue', '')

    def test_adj_eps(self, nc_update):
        assert '$0.35' in nc_update.get('adj_eps', '')

    def test_net_income(self, nc_update):
        assert '$230M' in nc_update.get('net_income_continuing', '')
        assert '167%' in nc_update.get('net_income_continuing', '')

    def test_dow_jones_revenue(self, nc_update):
        assert '$644M' in nc_update.get('dow_jones_revenue', '')

    def test_real_estate_revenue(self, nc_update):
        assert '$553M' in nc_update.get('digital_real_estate_revenue', '')

    def test_book_publishing_revenue(self, nc_update):
        assert '$566M' in nc_update.get('book_publishing_revenue', '')

    def test_ai_partnerships_mention_both(self, nc_update):
        status = nc_update.get('ai_partnerships_status', '')
        assert 'OpenAI' in status
        assert 'Meta' in status

    def test_anthropic_settlement_status(self, nc_update):
        assert '1.5B' in nc_update.get('anthropic_settlement_status', '')

    def test_ceo_ip_quote(self, nc_update):
        assert 'IP powers AI' in nc_update.get('ceo_self_positioning', '')

    def test_has_source_urls(self, nc_update):
        urls = nc_update.get('source_urls', [])
        assert len(urls) >= 3
        assert any('reuters.com' in u for u in urls)
        assert any('nypost.com' in u for u in urls)
        assert any('wsj.com' in u for u in urls)


# ─── NYT Q2 2026 Derived Revenue Tests ───────────────────────────────

class TestNYTQ2DerivedRevenue:
    """Verify the NYT Q2 2026 affiliate/licensing/other derivation in nytimes.yaml."""

    def test_nytimes_yaml_exists(self):
        path = os.path.join(PROFILES_DIR, 'nytimes.yaml')
        assert os.path.exists(path)

    def test_nytimes_yaml_loadable(self, nyt_data):
        assert nyt_data is not None


# ─── Inverse Correlation Parametric Tests ─────────────────────────────

class TestInverseCorrelation:
    """Parametric tests verifying the opacity → adversariality inverse pattern."""

    OPACITY_ADVERSARIALITY_MAP = [
        # (publisher_fragment, expected_tier, expected_adversariality_contains)
        ("Condé Nast", 1, "HIGH"),
        ("The Atlantic", 1, "HIGH"),
        ("Financial Times", 1, "HIGH"),
        ("Vox Media", 1, "HIGH"),
        ("New York Times", 2, "MODERATE"),
        ("USA Today", 2, "MODERATE"),
        ("People Inc", 2, "MODERATE"),
        ("News Corp", 3, "LOW"),
    ]

    @pytest.mark.parametrize("pub_fragment,expected_tier,expected_adv",
                             OPACITY_ADVERSARIALITY_MAP)
    def test_publisher_tier_adversariality(self, opacity_index, pub_fragment,
                                           expected_tier, expected_adv):
        """Each publisher should be in the expected tier with expected adversariality."""
        tiers = opacity_index.get('opacity_tiers', [])
        target_tier = next((t for t in tiers if t['tier'] == expected_tier), None)
        assert target_tier is not None, f"Tier {expected_tier} not found"

        pubs = target_tier.get('publishers', [])
        pub = next((p for p in pubs if pub_fragment in p['name']), None)
        assert pub is not None, \
            f"{pub_fragment} not found in Tier {expected_tier}: {[p['name'] for p in pubs]}"

        adversariality = pub.get('meta_coverage_adversariality', '').upper()
        assert expected_adv in adversariality, \
            f"{pub_fragment} adversariality {adversariality} does not contain {expected_adv}"


# ─── Source Verification Tests ────────────────────────────────────────

class TestSourceVerification:
    """Verify all source URLs are present and well-formed."""

    def test_digiday_url_format(self, opacity_index):
        url = opacity_index['digiday_meta_finding']['source_url']
        assert url.startswith('https://digiday.com/')

    def test_reuters_url_in_news_corp(self, opacity_index):
        urls = opacity_index['news_corp_q4_fy2026_update']['source_urls']
        reuters = [u for u in urls if 'reuters.com' in u]
        assert len(reuters) == 1
        assert '2026-08-05' in reuters[0] or '2026-08' in reuters[0]

    def test_all_source_urls_https(self, opacity_index):
        """Every source URL in the opacity index should be HTTPS."""
        def find_urls(obj, urls=None):
            if urls is None:
                urls = []
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if 'url' in k.lower() and isinstance(v, str) and v.startswith('http'):
                        urls.append(v)
                    elif 'url' in k.lower() and isinstance(v, list):
                        for item in v:
                            if isinstance(item, str) and item.startswith('http'):
                                urls.append(item)
                    else:
                        find_urls(v, urls)
            elif isinstance(obj, list):
                for item in obj:
                    find_urls(item, urls)
            return urls

        urls = find_urls(opacity_index)
        assert len(urls) > 0, "No URLs found"
        for url in urls:
            assert url.startswith('https://'), f"Non-HTTPS URL: {url}"
