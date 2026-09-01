"""
Test mechanism #448 Type C: Reddit Q2 2026 earnings Meta competitor Google AI headwind Advance margin loan
- Iteration 448 Type C Financial Incentive Mapping Sep 1 2026 14:00 PDT
- Corrects stale 30%/34% figures in #417/#427 via 2026 proxy primary source
- Adds Q2 2026 10-Q SEC filing $805M +61% YoY, EPS $1.25 beat $0.95, Q3 guidance $860-870M above $829M
- DAUq 130.3M +18% YoY but US DAUq declined 53.2M from 53.5M first QoQ decline
- choppy search-engine traffic + SEO headwinds Google AI Overviews
- Meta explicitly identified as competitor via Threads/Forum Reuters Jul 31 2026
- Advance total public equity ~$11.51B down from ~$13.47B $1.96B decline 15 days Reddit concentration 51.6%
- Margin loan danger zone 7.8M shares pledged $145.38-$148.54 below floor $140.67 potential margin call risk VPF/collar
- MANUAL ILLUSTRATIVE only, p_value NOT_CALCULATED, cohens_d NOT_CALCULATED, is_significant false
"""
import yaml, pathlib, re

def load_mech():
    path = pathlib.Path('profiles/competitor-entities.yaml')
    data = yaml.safe_load(path.read_text())
    mech = data['entities']['reddit']['reddit_q2_2026_earnings_meta_competitor_google_ai_headwind_advance_margin_loan_448']
    return mech

def test_mechanism_exists():
    mech = load_mech()
    assert mech is not None, "mechanism 448 not found"

def test_mechanism_id_448():
    mech = load_mech()
    assert mech['mechanism_id'] == 448

def test_type_c():
    mech = load_mech()
    assert 'Type C' in mech['type']

def test_iteration_448():
    mech = load_mech()
    assert mech['iteration'] == 448

def test_iteration_type_c():
    mech = load_mech()
    assert mech['iteration_type'] == 'C'

def test_date_analyzed_2026_09_01():
    mech = load_mech()
    assert mech['date_analyzed'] == '2026-09-01'

def test_iteration_time():
    mech = load_mech()
    assert '2026-09-01 14:00 PDT' in mech['iteration_time']

def test_goal_id():
    mech = load_mech()
    assert mech['goal_id'] == 'goal_54093bda4145'

def test_scheduled_job_id():
    mech = load_mech()
    assert mech['scheduled_job_id'] == 'mediascope-daily-iteration'

def test_publication_focus_wired():
    mech = load_mech()
    assert 'WIRED' in mech['publication_focus']

def test_competitor_pair_meta():
    mech = load_mech()
    assert 'Meta' in mech['competitor_pair']

def test_financial_channel_q2_2026():
    mech = load_mech()
    assert 'Q2 2026' in mech['financial_channel'] or 'q2_2026' in mech['financial_channel'].lower()

def test_payment_direction_google_openai_meta():
    mech = load_mech()
    pd = mech['payment_direction']
    assert 'Google' in pd and 'OpenAI' in pd and 'Advance' in pd

def test_overview_contains_805M():
    mech = load_mech()
    ov = mech['overview']
    assert '$805M' in ov and '+61%' in ov

def test_overview_contains_731M_consensus():
    mech = load_mech()
    ov = mech['overview']
    assert '$731M' in ov and 'consensus' in ov.lower()

def test_overview_contains_eps_beat():
    mech = load_mech()
    ov = mech['overview']
    assert '$1.25' in ov and '$0.95' in ov

def test_overview_contains_q3_guidance():
    mech = load_mech()
    ov = mech['overview']
    assert '$860-870M' in ov or '860-870' in ov

def test_overview_contains_dauq_130():
    mech = load_mech()
    ov = mech['overview']
    assert '130.3M' in ov and '18%' in ov

def test_overview_contains_us_dauq_decline():
    mech = load_mech()
    ov = mech['overview']
    assert '53.2M' in ov and '53.5M' in ov

def test_overview_contains_choppy_search():
    mech = load_mech()
    ov = mech['overview'].lower()
    assert 'choppy' in ov and 'search' in ov

def test_overview_contains_seo_headwinds():
    mech = load_mech()
    ov = mech['overview'].lower()
    assert 'seo headwind' in ov

def test_overview_contains_meta_competitor_threads_forum():
    mech = load_mech()
    ov = mech['overview']
    assert 'Meta' in ov and 'Threads' in ov and 'Forum' in ov

def test_overview_contains_21_percent_crash():
    mech = load_mech()
    ov = mech['overview']
    assert '21%' in ov and 'Jul 31' in ov

def test_overview_contains_5_94B_stake():
    mech = load_mech()
    ov = mech['overview']
    assert '$5.94B' in ov and '$140.67' in ov

def test_overview_contains_11_51B_total():
    mech = load_mech()
    ov = mech['overview']
    assert '$11.51B' in ov and '$13.47B' in ov

def test_overview_contains_1_96B_decline():
    mech = load_mech()
    ov = mech['overview']
    assert '$1.96B' in ov

def test_overview_contains_51_6_percent_concentration():
    mech = load_mech()
    ov = mech['overview']
    assert '51.6%' in ov

def test_overview_contains_margin_loan_danger_zone():
    mech = load_mech()
    ov = mech['overview'].lower()
    assert 'margin' in ov and '7.8m' in ov

def test_overview_contains_pledged_floor():
    mech = load_mech()
    ov = mech['overview']
    assert '$145.38' in ov or '$148.54' in ov or '145' in ov

def test_overview_contains_proxy_correction():
    mech = load_mech()
    ov = mech['overview']
    assert '21.9%' in ov or '65.2%' in ov or '42,191,092' in ov or '2026 proxy' in ov

def test_overview_contains_rpo_143():
    mech = load_mech()
    ov = mech['overview']
    assert '$143.7M' in ov or '143.7' in ov

def test_overview_contains_correlation_not_causation():
    mech = load_mech()
    ov = mech['overview'].lower()
    assert 'correlation does not imply causation' in ov or 'correlational' in ov

def test_overview_contains_structural_incentive_not_proof():
    mech = load_mech()
    ov = mech['overview'].lower()
    assert 'structural incentive' in ov and 'not proof' in ov

def test_no_em_dashes():
    mech = load_mech()
    # ensure no em dash character in overview
    assert '—' not in mech['overview'], "em dash found in overview - banned"
    assert '—' not in mech.get('cautious_language',''), "em dash in cautious_language"

def test_asymmetry_scorer_manual_illustrative():
    mech = load_mech()
    scorer = mech['asymmetry_scorer_result']
    assert scorer['methodology'].startswith('MANUAL ILLUSTRATIVE') or 'MANUAL ILLUSTRATIVE' in scorer['methodology']
    assert scorer['p_value'] == 'NOT_CALCULATED'
    assert scorer['cohens_d'] == 'NOT_CALCULATED'
    assert scorer['is_significant'] is False

def test_asymmetry_scorer_delta():
    mech = load_mech()
    scorer = mech['asymmetry_scorer_result']
    assert 'delta' in scorer
    assert scorer['delta'] < 0  # Meta more negative than Google/OpenAI

def test_asymmetry_requires_empirical_validation():
    mech = load_mech()
    scorer = mech['asymmetry_scorer_result']
    assert 'requires' in scorer['methodology'].lower() or 'requires' in scorer.get('requires_empirical_validation','').lower()
    assert 'Welch' in scorer['methodology'] or 'Welch' in scorer.get('requires_empirical_validation','')

def test_confounder_count_6plus():
    mech = load_mech()
    assert len(mech['confounders']) >= 6

def test_confounder_strengths():
    mech = load_mech()
    strengths = [c['strength'] for c in mech['confounders']]
    assert 'STRONG' in strengths and 'MODERATE' in strengths and 'WEAK' in strengths

def test_confounder_adjustment_not_calculated():
    mech = load_mech()
    for c in mech['confounders']:
        assert c['adjustment'] == 'NOT_CALCULATED'

def test_cautious_language_contains_manual_illustrative():
    mech = load_mech()
    cl = mech['cautious_language']
    assert 'MANUAL ILLUSTRATIVE' in cl
    assert 'p_value' in cl.lower() or 'p_value NOT_CALCULATED' in cl or 'NOT_CALCULATED' in cl

def test_cautious_language_contains_no_claim_significance():
    mech = load_mech()
    cl = mech['cautious_language'].lower()
    assert 'do not claim' in cl or 'no claim' in cl or 'is_significant false' in cl

def test_source_urls_https_6plus():
    mech = load_mech()
    urls = mech['source_urls']
    assert len(urls) >= 6
    for u in urls:
        assert u.startswith('https://'), f"url not https: {u}"

def test_primary_sources_sec_proxy():
    mech = load_mech()
    urls = [ps['url'] for ps in mech['primary_sources']]
    assert any('sec.gov' in u and 'rddt-20260423' in u for u in urls)

def test_primary_sources_sec_10k():
    mech = load_mech()
    urls = [ps['url'] for ps in mech['primary_sources']]
    assert any('sec.gov' in u and '000062' in u for u in urls)

def test_primary_sources_reuters_conde_nast():
    mech = load_mech()
    urls = [ps['url'] for ps in mech['primary_sources']]
    assert any('reuters.com' in u and 'conde-nast' in u for u in urls)

def test_cross_references_417_427():
    mech = load_mech()
    refs = mech.get('cross_references', [])
    assert '417' in refs and '427' in refs

def test_verification_browser():
    mech = load_mech()
    ver = mech.get('verification', {})
    assert '2026-09-01' in ver.get('browser_verified','') or 'QA audit' in ver.get('browser_verified','')

def test_yaml_parse_clean():
    path = pathlib.Path('profiles/competitor-entities.yaml')
    data = yaml.safe_load(path.read_text())
    assert data is not None
    # also wired.yaml
    wpath = pathlib.Path('profiles/wired.yaml')
    wdata = yaml.safe_load(wpath.read_text())
    assert wdata is not None
