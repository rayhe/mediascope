"""
Type C #483: Schibsted Media x OpenAI real-time content deal (Feb 12 2025) and
terms-opacity mapping.
- Iteration #483 Type C Financial Incentive Mapping Sep 3 2026 01:00 PDT
- Rotation 482 B -> 483 C.
- First dedicated Schibsted mechanism in the repo. Schibsted Media (Feb 2025)
  previously appeared only as a portfolio-list name in
  publisher_content_deal_portfolio.notable_partners; iteration #478's novelty
  note explicitly flagged Schibsted as the remaining Type C candidate.
- Findings (both party announcements opened first-hand via browser.open this
  run): real-time news-article integration into ChatGPT (up-to-date summaries
  with attribution) from VG, Aftenposten, Aftonbladet, Svenska Dagbladet;
  300M-user reach claim in both announcements; NO financial terms, term length,
  or exclusivity disclosed anywhere; Schibsted receives innovation resources,
  OpenAI tech access, and real-time engagement data; pre-existing entanglement
  (1000+ employee ChatGPT enterprise deal, mandatory AI training, Copilot since
  Jul 2023, CDTO photographed with Altman) means the content deal deepens an
  existing relationship rather than initiating one.
- Statistical discipline: qualitative structural mapping only; correlation not
  causation; is_significant false; no tone scores; no p_value.

Sources (opened via browser.open this run, Sep 3 2026):
- Schibsted announcement
  https://schibsted.com/news/schibsted-media-partners-with-openai/
- OpenAI announcement
  https://openai.com/index/openai-partners-with-schibsted-media-group
- Press Gazette AI deals tracker (deal listed 12 February 2025, no value)
  https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/
- Fast Company (The Information Jan 2024 benchmark band 1-5M USD/yr)
  https://www.FASTCOMPANY.COM/91116001/financial-times-openai-licensing-deal
- ENMNews (terms and exclusivity undisclosed)
  https://enmnews.com/2026/07/07/openai-taps-major-european-media-house-chatgpt-news-feed
- Schibsted AI-readiness article (enterprise entanglement)
  https://schibsted.com/news/how-schibsted-sets-up-its-employees-for-ai-success/
"""
import pathlib

import yaml

PROFILES_DIR = pathlib.Path(__file__).parent.parent / 'profiles'

SCHIBSTED_URL = 'https://schibsted.com/news/schibsted-media-partners-with-openai/'
OPENAI_URL = 'https://openai.com/index/openai-partners-with-schibsted-media-group'
PRESSGAZETTE_URL = 'https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/'
FASTCO_URL = 'https://www.FASTCOMPANY.COM/91116001/financial-times-openai-licensing-deal'
ENMNEWS_URL = 'https://enmnews.com/2026/07/07/openai-taps-major-european-media-house-chatgpt-news-feed'
SCHIBSTED_AI_URL = 'https://schibsted.com/news/how-schibsted-sets-up-its-employees-for-ai-success/'

MECH_KEY = 'mechanism_483_schibsted_openai_realtime_content_deal'

EXPECTED_BRANDS = ['VG (Norway)', 'Aftenposten (Norway)', 'Aftonbladet (Sweden)',
                   'Svenska Dagbladet (Sweden)']


def load_entities():
    path = PROFILES_DIR / 'competitor-entities.yaml'
    return yaml.safe_load(path.read_text())


def get_raw():
    return (PROFILES_DIR / 'competitor-entities.yaml').read_text()


def get_mech():
    data = load_entities()
    return data['entities']['openai'][MECH_KEY]


def test_competitor_entities_yaml_parses():
    assert load_entities() is not None


def test_mechanism_483_present():
    mech = get_mech()
    assert mech['mechanism_id'] == 483
    assert mech['iteration'] == 483


def test_rotation_and_job_ids():
    mech = get_mech()
    assert mech['rotation'] == 'Type C'
    assert mech['date_analyzed'] == '2026-09-03'
    assert mech['time_pdt'] == '01:00'
    assert mech['job_id'] == 'mediascope-daily-iteration'
    assert mech['goal_id'] == 'goal_54093bda4145'


def test_announcement_date():
    mech = get_mech()
    assert mech['announcement_date'] == '2025-02-12'


def test_deal_structure_brands():
    mech = get_mech()
    struct = mech['deal_structure']
    assert struct['brands_named'] == EXPECTED_BRANDS
    assert 'real-time' in struct['form'] or 'real-time' in struct['content_scope']
    assert 'attribution' in struct['content_scope']
    assert '300 million' in struct['reach_claim']
    assert 'Varun Shetty' in struct['openai_counterparty']
    assert 'Siv Juvik Tveitnes' in struct['schibsted_counterparty']


def test_deal_terms_opacity():
    mech = get_mech()
    op = mech['deal_terms_opacity']
    assert op['exact_amount_undisclosed'] is True
    assert op['term_length_undisclosed'] is True
    assert op['exclusivity_window_undisclosed'] is True
    assert 'Press Gazette' in op['evidence']
    assert '1 to 5 million' in op['benchmark_band']
    assert 'not an outlier' in op['opacity_pattern']


def test_what_schibsted_receives():
    mech = get_mech()
    rec = mech['what_schibsted_receives']
    assert len(rec) == 3
    joined = ' '.join(rec)
    assert 'innovation' in joined
    assert 'real-time data' in joined


def test_pre_existing_entanglement():
    mech = get_mech()
    ent = mech['pre_existing_entanglement']
    joined = ' '.join(ent)
    assert '1000+' in joined
    assert 'July 2023' in joined
    assert 'Altman' in joined
    assert '600,000+' in joined
    assert 'bounds sudden-capture' in joined


def test_nordic_significance():
    mech = get_mech()
    sig = mech['nordic_significance']
    joined = ' '.join(sig)
    assert 'Nordic' in joined
    assert 'Norwegian' in joined or 'Swedish' in joined


def test_statistical_discipline():
    mech = get_mech()
    sd = mech['statistical_discipline']
    assert sd['correlation_not_causation'] is True
    assert sd['is_significant'] is False
    assert sd['p_value'] == 'NOT_CALCULATED'
    assert sd['tone_scores'] == 'none'


def test_ranked_confounders():
    mech = get_mech()
    confs = mech['ranked_confounders']
    assert len(confs) == 4
    assert [c['rank'] for c in confs] == [1, 2, 3, 4]
    assert confs[0]['strength'] == 'strong'
    assert 'party-issued' in confs[0]['confounder']
    assert confs[2]['strength'] == 'moderate'
    assert 'coverage-tone' in confs[2]['confounder']


def test_cross_references():
    mech = get_mech()
    joined = ' '.join(mech['cross_references'])
    assert 'notable_partners' in joined
    assert '478' in joined
    assert '473' in joined
    assert '468' in joined


def test_novelty_verification():
    mech = get_mech()
    joined = ' '.join(mech['novelty_verification'])
    assert 'portfolio-list name' in joined
    assert '478' in joined
    assert 'Not Microsoft PCM related' in joined


def test_source_urls():
    mech = get_mech()
    urls = mech['source_urls']
    assert len(urls) == 6
    for u in (SCHIBSTED_URL, OPENAI_URL, PRESSGAZETTE_URL, FASTCO_URL,
              ENMNEWS_URL, SCHIBSTED_AI_URL):
        assert u in urls
    for u in urls:
        assert u.startswith('https://'), u


def test_caution_bounds_claim():
    mech = get_mech()
    assert 'No coverage-tone claim is made' in mech['caution']


def test_no_em_dash_or_nul_in_block():
    raw = get_raw()
    start = raw.index(MECH_KEY)
    end = raw.index('european_ad_expansion_dual_dependency_aug30:')
    block = raw[start:end]
    assert '\u2014' not in block
    assert '\u2013' not in block
    assert '\x00' not in block
    assert block.isascii()


def test_mechanism_uniqueness_repo_wide():
    raw = get_raw()
    assert raw.count(MECH_KEY + ':') == 1
    assert raw.count('mechanism_id: 483') == 1
