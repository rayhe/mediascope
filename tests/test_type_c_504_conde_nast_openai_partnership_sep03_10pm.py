"""
Type C #504: Conde Nast x OpenAI strategic content partnership (Aug 20 2024) -
owner-level tie to tracked publication WIRED, with CEO Senate-testimony
reversal baseline.
- Iteration #504 Type C Financial Incentive Mapping Sep 3 2026 22:00 PDT
- Rotation 503 B -> 504 C.
- First dedicated Conde Nast-deal mechanism in the repo. Conde Nast is the
  corporate owner of WIRED, a tracked publication central to the goal, making
  this an owner-level financial tie between a tracked publication's parent and
  a competitor entity (OpenAI) - the same structural class as mechanism 494
  (Vox/Verge). Novelty verified: zero Conde Nast mechanism_name entries in
  competitor-entities.yaml and competitor-coverage-research.yaml, zero
  test_type_c Conde Nast files, no Type C commit mapping the deal.
- Findings (browser.search this run, 2 query sets, verbatim full-URL listings;
  no page opened first-hand, all items via search-result excerpts marked
  second-hand in-mechanism): Aug 20 2024 multi-year partnership; Conde Nast
  brand content (Vogue, The New Yorker, Conde Nast Traveler, GQ, Architectural
  Digest, Vanity Fair, WIRED, Bon Appetit) displayed in ChatGPT and the
  SearchGPT prototype (launched Jul 25 2024) with direct links; counterparties
  Roger Lynch (CEO, Conde Nast, internal memo: partnership "begins to make up
  for some of that revenue" lost to search) and Brad Lightcap (COO, OpenAI -
  fourth Lightcap-signed publisher deal in the repo after 489 Hearst, 494 Vox,
  499 Atlantic); financial terms undisclosed (Reuters); pre-deal adversarial
  baseline - Lynch's Jan 10 2024 Senate Judiciary testimony ("Fair use is not
  intended to simply enrich tech companies that prefer not to pay"; GenAI tools
  keep "100 percent of the value for themselves"; "many" media companies could
  go out of business), seven months before signing, the strongest CEO-level
  pre/post posture reversal in the portfolio; newsroom-reaction bounded absence
  (iteration-492 rule); Meta contrast $0 from Meta (mechanism 453).
- Statistical discipline: qualitative structural mapping only; correlation not
  causation; is_significant false; no tone scores; no p_value.

Sources (research provenance per mechanism research_method, Sep 3 2026):
- Reuters on the Aug 20 2024 announcement (search excerpt)
  https://www.reuters.com/technology/openai-signs-deal-with-cond-nast-2024-08-20/?outputType=chromeless
- Neowin on the partnership and Lynch/Lightcap quotes (search excerpt)
  https://www.neowin.net/news/cond-nast-joins-the-growing-list-of-openais-content-partners/
- Press Gazette deal tracker on Lynch's existential warning (search excerpt)
  https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/
- Editor and Publisher via Hollywood Reporter on brands in scope (search excerpt)
  http://EditorAndPublisher.com/stories/cond-nast-inks-multiyear-openai-deal-for-its-magazine-brands,251539
- TechTarget on the SearchGPT copyright framing (search excerpt)
  https://www.techtarget.com/ai/news/366608126/OpenAI-Conde-Nast-searchGPT-deal-addresses-copyright-concerns
- Adweek on the multiyear partnership (search excerpt)
  https://www.adweek.com/morning-media-newsfeed/conde-nast-openai-strike-multiyear-partnership-in-new-ai-deal/
- Verdict on the partnership extension into media (search excerpt)
  https://www.verdict.co.uk/newsletters/openai-partners-with-conde-nast-extending-its-reach-into-the-media-industry/
- The Register on Lynch's Jan 2024 Senate testimony (search excerpt)
  https://www.theregister.com/software/2024/01/12/congress-told-ai-firms-should-pay-for-copyrighted-content/1381839?td=keepreading
- Editor and Publisher on the Senate hearing announcement (search excerpt)
  https://www.editorandpublisher.com/stories/senate-judiciary-committee-to-hold-hearing-on-oversight-of-artificial-intelligence-ai-future-of,247546
- Editor and Publisher on the hearing report (search excerpt)
  https://www.EditorandPublisher.com/stories/senators-hear-testimony-that-ai-is-worsening-news-industrys-troubles,247579
- Digital Watch Observatory on the testimony (search excerpt)
  https://dig.watch/updates/us-media-executives-call-for-legislation-on-ai-content-compensation
"""
import pathlib

import yaml

PROFILES_DIR = pathlib.Path(__file__).parent.parent / 'profiles'
ENTITIES_PATH = PROFILES_DIR / 'competitor-entities.yaml'

MECH_KEY = 'mechanism_504_conde_nast_openai_strategic_partnership'
NEXT_MECH_KEY = 'mechanism_473_future_plc_openai_strategic_partnership:'

EXPECTED_URLS = [
    'https://www.reuters.com/technology/openai-signs-deal-with-cond-nast-2024-08-20/?outputType=chromeless',
    'https://www.neowin.net/news/cond-nast-joins-the-growing-list-of-openais-content-partners/',
    'https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/',
    'http://EditorAndPublisher.com/stories/cond-nast-inks-multiyear-openai-deal-for-its-magazine-brands,251539',
    'https://www.techtarget.com/ai/news/366608126/OpenAI-Conde-Nast-searchGPT-deal-addresses-copyright-concerns',
    'https://www.adweek.com/morning-media-newsfeed/conde-nast-openai-strike-multiyear-partnership-in-new-ai-deal/',
    'https://www.verdict.co.uk/newsletters/openai-partners-with-conde-nast-extending-its-reach-into-the-media-industry/',
    'https://www.theregister.com/software/2024/01/12/congress-told-ai-firms-should-pay-for-copyrighted-content/1381839?td=keepreading',
    'https://www.editorandpublisher.com/stories/senate-judiciary-committee-to-hold-hearing-on-oversight-of-artificial-intelligence-ai-future-of,247546',
    'https://www.EditorandPublisher.com/stories/senators-hear-testimony-that-ai-is-worsening-news-industrys-troubles,247579',
    'https://dig.watch/updates/us-media-executives-call-for-legislation-on-ai-content-compensation',
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


def test_mechanism_504_present():
    mech = get_mech()
    assert mech['mechanism_id'] == 504
    assert mech['iteration'] == 504


def test_rotation_and_job_ids():
    mech = get_mech()
    assert mech['rotation'] == 'Type C'
    assert mech['date_analyzed'] == '2026-09-03'
    assert mech['time_pdt'] == '22:00'
    assert mech['job_id'] == 'mediascope-daily-iteration'
    assert mech['goal_id'] == 'goal_54093bda4145'


def test_announcement_date():
    mech = get_mech()
    assert mech['announcement_date'] == '2024-08-20'


def test_deal_structure_brands_and_counterparties():
    mech = get_mech()
    struct = mech['deal_structure']
    assert 'WIRED' in struct['brands_in_scope']
    assert 'Vogue' in struct['brands_in_scope']
    assert 'The New Yorker' in struct['brands_in_scope']
    assert 'Roger Lynch' in struct['counterparties']
    assert 'Brad Lightcap' in struct['counterparties']
    assert 'fourth Lightcap-signed' in struct['counterparties']
    assert '489' in struct['counterparties']
    assert '494' in struct['counterparties']
    assert '499' in struct['counterparties']
    assert 'begins to make up for some of that revenue' in struct['lynch_memo_quote']
    assert 'accuracy, integrity, and respect for quality reporting' in struct['lightcap_quote']


def test_searchgpt_context():
    mech = get_mech()
    struct = mech['deal_structure']
    assert 'Jul 25 2024' in struct['searchgpt_context']
    assert 'SearchGPT' in struct['searchgpt_context']
    assert 'direct links' in struct['content_flow_to_openai']


def test_deal_terms_opacity():
    mech = get_mech()
    opacity = mech['deal_terms_opacity']
    assert opacity['exact_amount_undisclosed'] is True
    assert opacity['term_length_undisclosed'] is True
    assert 'not disclosed' in opacity['evidence']
    assert '478' in opacity['opacity_pattern']
    assert '494' in opacity['opacity_pattern']
    assert '499' in opacity['opacity_pattern']


def test_pre_deal_adversarial_baseline():
    mech = get_mech()
    base = mech['pre_deal_adversarial_baseline']
    assert 'Jan 10 2024' in base['senate_hearing']
    assert 'prefer not to pay' in base['lynch_fair_use_quote']
    assert '100 percent of the value' in base['lynch_value_extraction_quote']
    assert 'many' in base['lynch_existential_warning']
    assert 'go out of business' in base['lynch_existential_warning']
    assert 'seven months' in base['reversal_arc']
    assert '499' in base['reversal_arc']
    assert 'no tone claim is made in this mechanism' in base['analytical_note']


def test_newsroom_reaction_bounded():
    mech = get_mech()
    bounded = mech['newsroom_reaction_bounded']
    assert 'bounded absence' in bounded['status']
    assert 'iteration-492 rule' in bounded['status']
    assert 'not a zero claim' in bounded['status']
    assert '494' in bounded['contrast']
    assert '499' in bounded['contrast']


def test_meta_contrast():
    mech = get_mech()
    assert '$0 from Meta' in mech['meta_contrast']
    assert '453' in mech['meta_contrast']
    assert 'CORRELATION NOT CAUSATION' in mech['meta_contrast']


def test_mediascope_relevance_owner_level_wired():
    mech = get_mech()
    rel = mech['mediascope_relevance']
    assert 'First dedicated Conde Nast-deal mechanism' in rel
    assert 'WIRED' in rel
    assert 'owner-level' in rel
    assert '494' in rel
    assert 'Type A' in rel


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
    assert any('second-hand' in c['confounder'] for c in confs)


def test_research_method_marks_second_hand():
    mech = get_mech()
    assert 'browser.search' in mech['research_method']
    assert 'second-hand' in mech['research_method']
    assert 'no page opened first-hand' in mech['research_method']
    assert 'iteration-492' in mech['research_method']


def test_source_urls():
    mech = get_mech()
    assert mech['source_urls'] == EXPECTED_URLS


def test_no_em_dash_or_nul_in_block():
    raw = get_raw()
    start = raw.index(MECH_KEY)
    end = raw.index(NEXT_MECH_KEY)
    block = raw[start:end]
    assert '—' not in block
    assert '–' not in block
    assert '\x00' not in block
    assert block.isascii()


def test_mechanism_uniqueness_repo_wide():
    raw = get_raw()
    assert raw.count(MECH_KEY + ':') == 1
    assert raw.count('mechanism_id: 504') == 1
