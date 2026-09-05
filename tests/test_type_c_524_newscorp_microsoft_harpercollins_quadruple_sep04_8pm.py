"""
Type C #524: News Corp x Microsoft HarperCollins book licensing (Nov 2024) -
Quadruple-AI-Revenue Owner (OpenAI + Meta + Microsoft + Anthropic settlement)
- Iteration #524 Type C Financial Incentive Mapping Sep 4 2026 20:00 PDT
- Rotation 523 B -> 524 C.
- Novelty verified: no mechanism_name containing HarperCollins in
  profiles/competitor-entities.yaml or profiles/competitor-coverage-research.yaml
  (grep verified); no Type C commit with HarperCollins in the title
  (git log --grep verified); zero test_type_c_524 files on disk before this run
  (glob verified). The deal is referenced in prose only as an exclusion inside
  mechanism 519 (OpenAI deal explicitly excludes HarperCollins) - this is the
  first dedicated Type C deal mechanism for it.
- Findings (browser.search this run, 2 query sets, verbatim full-URL listings;
  all items via search-result excerpts, second-hand, marked bounded
  in-mechanism): 404 Media broke the story 2024-11-18 - HarperCollins confirmed
  a deal with an unnamed technology company for select nonfiction AI training
  with author opt-in. Bloomberg 2024-11-19 (anonymous sources): the company is
  Microsoft, training an undisclosed new AI model; Microsoft declined to
  comment. Terms: three-year license; $5,000 per title split 50/50 ($2,500
  author + $2,500 HarperCollins); author opt-in required; Microsoft selects
  titles; backlist nonfiction only; output capped at 200 consecutive words
  and/or 5% of book text; no new-book generation; pledge not to scrape piracy
  sites. First Big Five publisher to sign an AI licensing deal. Author
  reactions: Daniel Kibblesmith called it abominable (Bluesky); Alice Robb
  (Bloomberg Feb 2025) confirmed her 2018 book Why We Dream was offered.
  Attribution caveat: Microsoft identity never officially confirmed by either
  party.
- Quadruple frame: News Corp becomes the first and only tracked-publication
  owner receiving AI revenue from FOUR major AI companies through four
  distinct channels: OpenAI news licensing ($250M/5yr), Meta news licensing
  (up to $50M/yr), Microsoft book licensing (HarperCollins, per-title),
  Anthropic settlement share ($1.5B Bartz, approved Jul 20 2026).
- Statistical discipline: qualitative structural mapping only; correlation not
  causation; is_significant false; p_value NOT_CALCULATED; no tone scores.

Source URLs (all second-hand via search excerpts this run, Sep 4 2026):
- https://www.computerworld.com/article/3619928/has-microsoft-finally-agreed-to-pay-for-intellectual-property-to-train-its-genai-tools.html
- https://www.emarketer.com/content/microsoft-harpercollins-sign-ai-licensing-deal--author-opt-in-still-required
- https://www.eweek.com/news/harpercollins-books-train-microsoft-ai-models/
- https://www.medianama.com/2024/11/223-microsoft-inks-deal-harpercollins-train-ai-books/
- https://www.idaireland.fr/latest-news/insights/harpercollins-pens-deal-with-microsoft-to-train-ai-on-its-books
- https://www.wizcase.com/news/microsoft-partners-with-harpercollins-for-nonfiction-ai-training/
- https://sherwood.news/snacks/tech/harpercollins-will-let-microsoft-license-some-of-its-authors-books-for-ai/
- http://musically.com/2025/02/10/author-reveals-more-details-on-harpercollins-ai-deal-royalties/
- https://www.adweek.com/media/anthropic-content-licensing-lawsuits-publishers/
"""
import glob
import os
import pathlib

import yaml

PROFILES_DIR = pathlib.Path(__file__).parent.parent / 'profiles'
ENTITIES_PATH = PROFILES_DIR / 'competitor-entities.yaml'
NEWSCORP_PATH = PROFILES_DIR / 'news-corp.yaml'

MECH_KEY = 'mechanism_524_newscorp_microsoft_harpercollins_quadruple_ai_revenue'

EXPECTED_URLS = [
    'https://www.computerworld.com/article/3619928/has-microsoft-finally-agreed-to-pay-for-intellectual-property-to-train-its-genai-tools.html',
    'https://www.emarketer.com/content/microsoft-harpercollins-sign-ai-licensing-deal--author-opt-in-still-required',
    'https://www.eweek.com/news/harpercollins-books-train-microsoft-ai-models/',
    'https://www.medianama.com/2024/11/223-microsoft-inks-deal-harpercollins-train-ai-books/',
    'https://www.idaireland.fr/latest-news/insights/harpercollins-pens-deal-with-microsoft-to-train-ai-on-its-books',
    'https://www.wizcase.com/news/microsoft-partners-with-harpercollins-for-nonfiction-ai-training/',
    'https://sherwood.news/snacks/tech/harpercollins-will-let-microsoft-license-some-of-its-authors-books-for-ai/',
    'http://musically.com/2025/02/10/author-reveals-more-details-on-harpercollins-ai-deal-royalties/',
    'https://www.adweek.com/media/anthropic-content-licensing-lawsuits-publishers/',
]


def load_entities():
    with open(ENTITIES_PATH, encoding='utf-8') as f:
        return yaml.safe_load(f)


def get_raw():
    return ENTITIES_PATH.read_text(encoding='utf-8')


def get_mech():
    return load_entities()['entities']['openai'][MECH_KEY]


def test_competitor_entities_yaml_parses():
    d = load_entities()
    assert 'entities' in d and 'openai' in d['entities']


def test_mechanism_524_present():
    m = get_mech()
    assert m['mechanism_id'] == 524
    assert m['iteration'] == 524


def test_rotation_and_job_ids():
    m = get_mech()
    assert m['rotation'] == 'Type C'
    assert m['job_id'] == 'mediascope-daily-iteration'
    assert m['goal_id'] == 'goal_54093bda4145'
    assert m['date_analyzed'] == '2026-09-04'
    assert m['time_pdt'] == '20:00'


def test_harpercollins_deal_break_and_attribution():
    m = get_mech()
    d = m['microsoft_harpercollins_deal']
    assert d['break_date'] == '2024-11-18'
    assert '404 Media' in d['broken_by']
    assert 'Bloomberg' in d['identity_attribution']
    assert 'Microsoft' in d['identity_attribution']


def test_attribution_caveat_never_officially_confirmed():
    m = get_mech()
    caveat = m['microsoft_harpercollins_deal']['attribution_caveat']
    assert 'never officially confirmed' in caveat
    # the same caveat must also appear in the strong confounders
    strong = m['ranked_confounders']['strong']
    assert any('never officially confirmed' in c for c in strong)


def test_harpercollins_deal_terms():
    m = get_mech()
    d = m['microsoft_harpercollins_deal']
    assert d['term_years'] == 3
    assert '$5,000' in d['per_title_payment']
    assert '50/50' in d['per_title_payment']
    assert 'opt-in' in d['author_opt_in'] or 'opt in' in d['author_opt_in']
    assert '200 consecutive words' in d['output_guardrails']
    assert '5 percent' in d['output_guardrails']


def test_harpercollins_first_big_five():
    m = get_mech()
    assert 'first Big Five' in m['microsoft_harpercollins_deal']['first_big_five']


def test_author_reactions():
    m = get_mech()
    reactions = m['microsoft_harpercollins_deal']['author_reactions']
    assert len(reactions) == 2
    assert 'Kibblesmith' in reactions[0] and 'abominable' in reactions[0]
    assert 'Alice Robb' in reactions[1] and 'Why We Dream' in reactions[1]


def test_quadruple_revenue_frame():
    m = get_mech()
    q = m['quadruple_revenue_frame']
    assert 'FOUR' in q['status']
    assert '$250M' in q['leg_1_openai']
    assert 'EXCLUDES HarperCollins' in q['leg_1_openai']
    assert '$50M per year' in q['leg_2_meta']
    assert 'THIS mechanism' in q['leg_3_microsoft']
    assert '$1.5B' in q['leg_4_anthropic']
    assert 'Dow Jones' in q['division_separation']
    assert 'HarperCollins' in q['division_separation']


def test_voluntary_vs_involuntary_pricing():
    m = get_mech()
    p = m['voluntary_vs_involuntary_pricing']
    assert '$2,500' in p['microsoft_voluntary_rate']
    assert '$3,000' in p['anthropic_settlement_rate']
    assert 'illustrative' in p['illustrative_note']


def test_woo_and_sue_extension():
    m = get_mech()
    w = m['woo_and_sue_extension']
    assert 'woo and a sue' in w['thomson_doctrine']
    assert 'Microsoft' in w['woos']
    assert 'Perplexity' in w['sues']
    assert 'co-defendant' in w['irony']


def test_prediction_for_tracked_coverage():
    m = get_mech()
    p = m['prediction_for_tracked_coverage']
    assert 'symmetric' in p['text']
    assert 'Anthropic' in p['text']
    assert 'HarperCollins' in p['transmission_caveat']
    assert 'severity_framing_inversion' in p['control_note']


def test_extends_prior_mechanisms():
    m = get_mech()
    assert '519' in m['extends']
    assert '509' in m['extends']
    assert '489' in m['extends']


def test_ranked_confounders_present():
    m = get_mech()
    c = m['ranked_confounders']
    assert len(c['strong']) == 2
    assert len(c['moderate']) == 2
    assert len(c['weak']) == 2
    assert m['correlation_not_causation'] is True


def test_statistical_discipline_flags():
    m = get_mech()
    assert m['is_significant'] is False
    assert m['p_value'] == 'NOT_CALCULATED'
    assert m['statistical_scope'] == 'qualitative structural mapping only'
    assert m['tone_scores'] == 'NOT_SCORED'


def test_source_urls_in_raw_yaml():
    raw = get_raw()
    for url in EXPECTED_URLS:
        assert url in raw, 'missing URL in raw YAML: %s' % url


def test_mechanism_block_is_ascii():
    raw = get_raw()
    start = raw.index(MECH_KEY + ':')
    nxt = raw.index('\n  anthropic:', start)
    block = raw[start:nxt]
    block.encode('ascii')


def test_mechanism_id_unique_in_file():
    raw = get_raw()
    assert raw.count(MECH_KEY + ':') == 1


def test_no_silent_hash_truncation():
    # Regression guard for the #507 silent-mangle trap: hand-written scalars
    # must survive parse intact (per AGENTS.md rule, all are single-quoted).
    m = get_mech()
    assert '$5,000' in m['microsoft_harpercollins_deal']['per_title_payment']
    assert 'woo and a sue' in m['woo_and_sue_extension']['thomson_doctrine']
    assert 'FOUR' in m['quadruple_revenue_frame']['status']
    assert 'http://musically.com' in m['source_urls'][7]


def test_news_corp_profile_microsoft_leg():
    with open(NEWSCORP_PATH, encoding='utf-8') as f:
        d = yaml.safe_load(f)
    partners = [r['partner'] for r in d['revenue_relationships']]
    assert 'Microsoft' in partners
    ms_leg = [r for r in d['revenue_relationships'] if r['partner'] == 'Microsoft'][0]
    assert 'HarperCollins' in ms_leg['scope']
    assert 'never officially confirmed' in ms_leg['scope']
    assert ms_leg['verified'] is True
    anth_leg = [r for r in d['revenue_relationships'] if r['partner'] == 'Anthropic'][0]
    assert 'FOUR' in anth_leg['notes']
    ms_cr = d['competitor_relationships']['microsoft']
    assert ms_cr['financial_tie'] == 'licensing'
    assert '524' in ms_cr['description']


def test_novelty_no_other_524_files():
    here = os.path.dirname(os.path.abspath(__file__))
    matches = glob.glob(os.path.join(here, 'test_type_c_524*'))
    assert len(matches) == 1, matches
