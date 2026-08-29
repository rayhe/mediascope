"""
Test for Iteration #366 Type C Financial Incentive Mapping
Mechanism #368 — Google Zero 55%→25% + Amazon $70B Ads TTM + OpenAI $1-5M Licensing Marginal Replacement
"""
import yaml
import pathlib
import re

REPO = pathlib.Path.home() / "workspace/repos/mediascope"

def load_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def test_wired_mechanism_exists():
    wired = load_yaml(REPO / "profiles/wired.yaml")
    assert 'google_zero_amazon_ads_dependency_aug29' in wired, "Mechanism #368 missing in wired.yaml"
    mech = wired['google_zero_amazon_ads_dependency_aug29']
    assert mech['mechanism_id'] == 368
    assert mech['date_analyzed'] == '2026-08-29'
    assert 'Type C' in mech['type']
    assert 'Financial Incentive' in mech['type']

def test_wired_mechanism_traffic_collapse():
    wired = load_yaml(REPO / "profiles/wired.yaml")
    mech = wired['google_zero_amazon_ads_dependency_aug29']
    tc = mech['traffic_collapse']
    assert tc['google_search_share_2023'] == '55% (Lynch via FT, Mar 2026)' or '55%' in tc['google_search_share_2023']
    assert '25%' in tc['google_search_share_2025']
    assert tc['decline_pct_points'] == 30 or tc.get('decline_pct_points') == 30
    assert 'death blow' in tc['lynch_quote_death_blow'].lower()
    assert 'zero' in tc['lynch_quote_zero_traffic'].lower()

def test_wired_mechanism_amazon_ads():
    wired = load_yaml(REPO / "profiles/wired.yaml")
    mech = wired['google_zero_amazon_ads_dependency_aug29']
    ads = mech['amazon_ads_ttm']
    assert ads['q1_2026_revenue_b'] == 17.2
    assert ads['ttm_crossed_b'] == 70
    assert ads['q1_2026_yoy_growth_pct'] == 24
    # source URLs present
    assert 'bestmediainfo.com' in ads['source_bestmediainfo']
    assert 'ppc.land' in ads['source_ppcland']
    assert 'techcrunch.com' in ads['aws_marketplace']

def test_wired_mechanism_openai_licensing():
    wired = load_yaml(REPO / "profiles/wired.yaml")
    mech = wired['google_zero_amazon_ads_dependency_aug29']
    lic = mech['openai_licensing_range']
    assert '$1-5M' in lic['mid_tier_range']
    assert '$50M' in lic['news_corp'] or '50M' in lic['news_corp']
    assert 'tens of millions' in lic['axel_springer'].lower() or 'tens' in lic['axel_springer'].lower()
    assert 'Undisclosed' in lic['conde_nast_undisclosed'] or 'undisclosed' in lic['conde_nast_undisclosed'].lower()

def test_wired_mechanism_conde_nast_revenue():
    wired = load_yaml(REPO / "profiles/wired.yaml")
    mech = wired['google_zero_amazon_ads_dependency_aug29']
    rev = mech['conde_nast_revenue_context']
    assert '1.9-2.0' in rev['revenue_estimate_b']
    assert '28-90%' in rev['ad_decline_replacement'] or '28-90' in rev['ad_decline_replacement']
    assert 'profitable' in rev['profitability'].lower() or 'Profitable' in rev['profitability']

def test_wired_mechanism_financial_quadrupling():
    wired = load_yaml(REPO / "profiles/wired.yaml")
    mech = wired['google_zero_amazon_ads_dependency_aug29']
    quad = mech['financial_incentive_quadrupling']
    assert 'google' in quad
    assert 'amazon' in quad
    assert 'openai' in quad
    assert 'meta' in quad
    assert '$0' in quad['meta'] or '$0' in str(quad['meta'])
    assert 'Direction of money' in quad['prediction']
    assert 'causation' in quad['cautious_language'].lower()

def test_wired_mechanism_source_urls():
    wired = load_yaml(REPO / "profiles/wired.yaml")
    mech = wired['google_zero_amazon_ads_dependency_aug29']
    urls = mech['source_urls']
    assert len(urls) >= 10, f"Expected >=10 source URLs, got {len(urls)}"
    # Verify specific domains
    domains = ' '.join(urls)
    assert 'reuters.com' in domains
    assert 'adweek.com' in domains
    assert 'aicerts.ai' in domains
    assert 'ronntorossian.medium.com' in domains or 'medium.com' in domains
    assert 'searchenginejournal.com' in domains
    assert 'bestmediainfo.com' in domains
    assert 'ppc.land' in domains
    assert 'techcrunch.com' in domains
    assert 'bloomberglaw.com' in domains
    assert 'siliconangle.com' in domains

def test_wired_mechanism_no_em_dashes():
    wired = load_yaml(REPO / "profiles/wired.yaml")
    mech = wired['google_zero_amazon_ads_dependency_aug29']
    # Check no em dashes in critical text fields (Ray's standing preference)
    text_fields = [
        str(mech.get('finding', '')),
        str(mech.get('focus', '')),
        str(mech.get('financial_incentive_quadrupling', {}).get('prediction', '')),
    ]
    for txt in text_fields:
        assert '—' not in txt, f"Em dash found in mechanism text: {txt[:200]}"
        assert '–' not in txt, f"En dash found in mechanism text: {txt[:200]}"

def test_competitor_entities_mechanism_exists():
    comp = load_yaml(REPO / "profiles/competitor-entities.yaml")
    assert 'entities' in comp
    assert 'google' in comp['entities']
    google = comp['entities']['google']
    assert 'financial_dependency_aug29' in google, "Mechanism #368 missing under entities.google"
    mech = google['financial_dependency_aug29']
    assert mech['mechanism_id'] == 368
    assert mech['date_analyzed'] == '2026-08-29'
    assert 'Type C' in mech['type']
    assert 'Financial Incentive' in mech['type']

def test_competitor_entities_mechanism_structure():
    comp = load_yaml(REPO / "profiles/competitor-entities.yaml")
    mech = comp['entities']['google']['financial_dependency_aug29']
    # Required subsections
    assert 'traffic_collapse' in mech
    assert 'amazon_ads' in mech
    assert 'openai_licensing' in mech
    assert 'total_ai_licensing' in mech
    assert 'source_urls' in mech
    assert len(mech['source_urls']) >= 8
    # Verify financial numbers
    assert mech['traffic_collapse']['google_search_2023'] == '55%' or '55%' in str(mech['traffic_collapse']['google_search_2023'])
    assert mech['amazon_ads']['ttm_b'] == 70
    assert mech['openai_licensing']['mid_tier'] == '$1-5M/yr' or '$1-5M' in mech['openai_licensing']['mid_tier']
