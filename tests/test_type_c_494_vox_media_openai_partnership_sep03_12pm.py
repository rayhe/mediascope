"""
Type C #494: Vox Media x OpenAI strategic content and product partnership
(May 29 2024) - owner-level tie to tracked publication The Verge.
- Iteration #494 Type C Financial Incentive Mapping Sep 3 2026 12:00 PDT
- Rotation 493 B -> 494 C.
- First dedicated Vox Media mechanism in the repo. Vox Media owns The Verge,
  a tracked publication; previously Vox appeared only as a one-line
  portfolio-list entry (openai_deal: May 2024, undisclosed) with no dedicated
  mechanism (grep verified), no test_vox* Type C file, no Type C commit with
  Vox in the title.
- Findings (voxmedia.com announcement and TechCrunch Jun 2024 opened
  first-hand via browser.open this run; VentureBeat/Adweek/FastCompany/Slashdot
  via verbatim search-result URLs): May 29 2024 multi-faceted deal; brands Vox,
  The Verge, Eater, New York Magazine, The Cut, Vulture, SB Nation; OpenAI gets
  current content plus full archive for training; ChatGPT 100M weekly users
  with brand attribution and referrals; Vox builds audience/advertiser products
  on OpenAI tech; Forte first-party data platform ad-targeting extension (2x
  performance claim) = ad-tech collaboration like Dotdash Meredith, unlike
  Hearst #489; counterparties Bankoff, Wasserstein, Brad Lightcap (OpenAI COO,
  same as Hearst #489); Axios exclusive by Sara Fischer; terms undisclosed;
  newsroom blindsided (Wasserstein Slack+email moments before Axios);
  Vox Media Union "informed without warning" statement; Kelsey Piper (OpenAI
  NDA expose author) frustration plus EIC written non-interference assurances;
  Bryan Walsh "This article is OpenAI training data"; Amy McCarthy "protection
  racket" quote; Atlantic parallel "A Devil's Bargain With OpenAI"; pre-deal
  critical baseline (environmental impact, board upheavals, trustworthiness)
  enabling future Type A pre/post comparison; Meta contrast $0 from Meta.
- Statistical discipline: qualitative structural mapping only; correlation not
  causation; is_significant false; no tone scores; no p_value.

Sources (opened via browser.open first-hand this run, Sep 3 2026, unless noted):
- Vox Media announcement (May 29 2024)
  https://www.voxmedia.com/2024/5/29/24166483/vox-media-openai-strategic-content-and-product-partnership/
- TechCrunch on newsroom/union reaction (Jun 22 2024)
  https://techcrunch.com/2024/06/22/whats-in-it-for-us-journalists-ask-as-publications-sign-content-deals-with-openai/
- VentureBeat on the dual announcement (URL from search)
  https://venturebeat.com/ai/openai-partners-with-the-atlantic-and-the-verge-publisher-vox-media
- Adweek/Axios syndication (URL from search)
  https://www.adweek.com/morning-media-newsfeed/the-atlantic-vox-media-ink-licensing-product-deals-with-openai/
- Slashdot/Ars Technica on journalist reactions incl. Piper, Walsh, Beres
  (URL from search)
  https://news.slashdot.org/story/24/06/01/0245209/journalists-deeply-troubled-by-openais-content-deals-with-vox-the-atlantic
- Fast Company portfolio list (Vox ad-targeting product note, URL from search)
  https://www.FastCompany.com/91130785/companies-reddit-news-corp-deals-openai-train-chatgpt-partnerships
"""
import pathlib

import yaml

PROFILES_DIR = pathlib.Path(__file__).parent.parent / 'profiles'
ENTITIES_PATH = PROFILES_DIR / 'competitor-entities.yaml'

MECH_KEY = 'mechanism_494_vox_media_openai_strategic_partnership'
NEXT_MECH_KEY = 'mechanism_473_future_plc_openai_strategic_partnership:'

EXPECTED_BRANDS = [
    'Vox',
    'The Verge',
    'Eater',
    'New York Magazine',
    'The Cut',
    'Vulture',
    'SB Nation',
]

EXPECTED_URLS = [
    'https://www.voxmedia.com/2024/5/29/24166483/vox-media-openai-strategic-content-and-product-partnership/',
    'https://techcrunch.com/2024/06/22/whats-in-it-for-us-journalists-ask-as-publications-sign-content-deals-with-openai/',
    'https://venturebeat.com/ai/openai-partners-with-the-atlantic-and-the-verge-publisher-vox-media',
    'https://www.adweek.com/morning-media-newsfeed/the-atlantic-vox-media-ink-licensing-product-deals-with-openai/',
    'https://news.slashdot.org/story/24/06/01/0245209/journalists-deeply-troubled-by-openais-content-deals-with-vox-the-atlantic',
    'https://www.FastCompany.com/91130785/companies-reddit-news-corp-deals-openai-train-chatgpt-partnerships',
]


def load_entities():
    with open(ENTITIES_PATH, encoding='utf-8') as f:
        return yaml.safe_load(f)


def get_raw():
    with open(ENTITIES_PATH, encoding='utf-8') as f:
        return f.read()


def get_mech():
    data = load_entities()
    return data['entities']['openai'][MECH_KEY]


def test_competitor_entities_yaml_parses():
    assert load_entities() is not None


def test_mechanism_494_present():
    mech = get_mech()
    assert mech['mechanism_id'] == 494
    assert mech['iteration'] == 494


def test_rotation_and_job_ids():
    mech = get_mech()
    assert mech['rotation'] == 'Type C'
    assert mech['date_analyzed'] == '2026-09-03'
    assert mech['time_pdt'] == '12:00'
    assert mech['job_id'] == 'mediascope-daily-iteration'
    assert mech['goal_id'] == 'goal_54093bda4145'


def test_announcement_date():
    mech = get_mech()
    assert mech['announcement_date'] == '2024-05-29'


def test_deal_structure_brands():
    mech = get_mech()
    struct = mech['deal_structure']
    assert struct['brands_in_scope'] == EXPECTED_BRANDS
    assert 'The Verge' in struct['brands_in_scope']
    assert '100 million' in struct['reach_and_attribution']
    assert 'brand attribution' in struct['reach_and_attribution']
    assert 'entire archive' in struct['content_flow_to_openai']
    assert 'Jim Bankoff' in struct['counterparties']
    assert 'Pam Wasserstein' in struct['counterparties']
    assert 'Brad Lightcap' in struct['counterparties']
    assert 'Sara Fischer' in struct['scoop']


def test_deal_structure_ad_tech_collaboration():
    mech = get_mech()
    struct = mech['deal_structure']
    assert 'Forte' in struct['ad_tech_collaboration']
    assert 'Dotdash Meredith' in struct['ad_tech_collaboration']
    assert 'Hearst' in struct['ad_tech_collaboration']
    assert 'Strategist Gift Scout' in struct['product_flow_to_vox']


def test_deal_terms_opacity():
    mech = get_mech()
    opacity = mech['deal_terms_opacity']
    assert opacity['exact_amount_undisclosed'] is True
    assert opacity['term_length_undisclosed'] is True
    assert 'two-year' in opacity['evidence']
    assert '478' in opacity['opacity_pattern']
    assert '489' in opacity['opacity_pattern']


def test_newsroom_and_union_opposition():
    mech = get_mech()
    opp = mech['newsroom_and_union_opposition']
    assert 'moments before the Axios exclusive' in opp['blindsided_rollout']
    assert 'informed without warning' in opp['vox_media_union']
    assert 'Kelsey Piper' in opp['kelsey_piper']
    assert 'If that is false I will quit' in opp['kelsey_piper']
    assert 'paperclip' in opp['bryan_walsh']
    assert 'protection racket' in opp['union_bargaining']
    assert '489' in opp['analytical_note']


def test_pre_deal_critical_baseline():
    mech = get_mech()
    base = mech['pre_deal_critical_baseline']
    assert 'environmental impact' in base['finding']
    assert 'trustworthiness' in base['finding']
    assert 'Type A' in base['analytical_note']


def test_meta_contrast():
    mech = get_mech()
    assert '$0 from Meta' in mech['meta_contrast']
    assert 'CORRELATION NOT CAUSATION' in mech['meta_contrast']
    assert 'mechanism 127' in mech['meta_contrast']


def test_mediascope_relevance_owner_level():
    mech = get_mech()
    rel = mech['mediascope_relevance']
    assert 'First dedicated Vox Media mechanism' in rel
    assert 'The Verge' in rel
    assert 'owner-level' in rel


def test_statistical_discipline():
    mech = get_mech()
    disc = mech['statistical_discipline']
    assert disc['correlation_not_causation'] is True
    assert disc['is_significant'] is False
    assert disc['tone_scores'] == 'none'
    assert disc['p_value'] == 'NOT_CALCULATED'


def test_ranked_confounders():
    mech = get_mech()
    confs = mech['ranked_confounders']
    assert len(confs) == 4
    strengths = [c['strength'] for c in confs]
    assert strengths[0] == 'strong'
    assert strengths.count('moderate') == 2
    assert strengths[3] == 'weak'
    assert any('issuer communications' in c['confounder'] for c in confs)


def test_research_method_marks_first_hand():
    mech = get_mech()
    assert 'opened' in mech['research_method']
    assert 'first-hand' in mech['research_method']


def test_source_urls():
    mech = get_mech()
    assert mech['source_urls'] == EXPECTED_URLS


def test_no_em_dash_or_nul_in_block():
    raw = get_raw()
    start = raw.index(MECH_KEY)
    end = raw.index(NEXT_MECH_KEY)
    block = raw[start:end]
    assert '\u2014' not in block
    assert '\u2013' not in block
    assert '\x00' not in block
    assert block.isascii()


def test_mechanism_uniqueness_repo_wide():
    raw = get_raw()
    assert raw.count(MECH_KEY + ':') == 1
    assert raw.count('mechanism_id: 494') == 1
