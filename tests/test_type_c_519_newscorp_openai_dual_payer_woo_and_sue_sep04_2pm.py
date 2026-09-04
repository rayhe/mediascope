"""
Type C #519: News Corp x OpenAI content licensing deal (May 2024) - largest OpenAI
publisher deal, dual-AI-payer owner with Meta second leg and woo-and-sue posture
- Iteration #519 Type C Financial Incentive Mapping Sep 4 2026 14:00 PDT
- Rotation 518 B -> 519 C.
- Novelty verified: no mechanism_ key for a News Corp deal anywhere in
  profiles/competitor-entities.yaml before this run (grep verified); no Type C
  commit with "News Corp" in the title (git log --grep verified); zero
  test_type_c_519 files on disk before this run (glob verified). The deal is
  referenced only in prose/data rows (marketplace_intermediary_landscape tier-1
  bilateral listing, opacity index balanced-control notes) - this is the first
  dedicated Type C deal mechanism for it.
- Findings (browser.search this run, 3 query sets, verbatim full-URL listings;
  all items via search-result excerpts, second-hand, marked bounded
  in-mechanism): News Corp x OpenAI deal announced 2024-05-22 - OpenAI gets
  current and archived content from WSJ, Barron's, MarketWatch, IBD, FN, NY Post
  (US); Times, Sunday Times, Sun (UK); Australian, news.com.au, Daily Telegraph,
  Courier Mail, Advertiser, Herald Sun (AU) for BOTH training and ChatGPT
  answers; excludes HarperCollins and Realtor.com. Reported >$250M over five
  years (~$50M/yr, cash plus OpenAI tech credits, WSJ self-reporting; official
  terms undisclosed). Counterparties: Robert Thomson (News Corp CEO) and Sam
  Altman (OpenAI CEO). Largest documented OpenAI publisher payment in the repo
  value lists. Meta second leg: 2026-03-04, Alexandra Bruell (WSJ), up to
  $50M/yr for at least three years, US+UK content for Meta AI training and
  retrieval - News Corp is the only tracked-publication owner with deals from
  BOTH Meta and OpenAI. Sue-one-sign-the-other: Dow Jones + NY Post sued
  Perplexity AI in SDNY 2024-10-21 ("massive amount of illegal copying" into a
  RAG database, false attribution, up to $150k/violation, RAG-database
  destruction sought; July 2024 licensing letter unanswered; Thomson: "abuse of
  intellectual property") - five months after signing OpenAI, the #514 pattern
  stretched over months. Woo-and-sue: Thomson at the Morgan Stanley TMT
  conference (Mar 2026): "We have what you might call a woo and a sue
  strategy... there'll be a discount for those who hand themselves in, and
  there'll be a penalty for those that resist." Prediction: symmetric softening
  incentive toward both Meta and OpenAI for WSJ vs no-deal entities, conditional
  on owner-level transmission; control validation via the existing repo row that
  WSJ's Christopher Mims systematically discloses both deals - the repo's only
  publication-level disclosure practice.
- Statistical discipline: qualitative structural mapping only; correlation not
  causation; is_significant false; p_value NOT_CALCULATED; no tone scores.

Source URLs (all second-hand via search excerpts this run, Sep 4 2026):
- https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/
- http://firstamendment.mtsu.edu/post/openai-to-start-using-news-content-from-news-corp-in-multiyear-deal/
- https://www.theregister.com/2024/05/23/openai_news_corp/?td=rt-9cs
- https://venturebeat.com/ai/openai-partners-with-wall-street-journal-publisher-news-corp
- https://www.adweek.com/morning-media-newsfeed/news-corp-strikes-content-licensing-deal-with-openai/
- https://www.reuters.com/legal/murdoch-firms-dow-jones-new-york-post-sue-perplexity-ai-2024-10-21/
- https://www.editorandpublisher.com/stories/news-corp-meta-in-ai-content-licensing-deal-worth-up-to-50-million-a-year,260471
- https://www.wsj.com/business/media/news-corp-meta-in-ai-content-licensing-deal-worth-up-to-50-million-a-year-d4fbf244
- https://www.engadget.com/ai/meta-signs-a-multimillion-dollar-ai-licensing-deal-with-news-corp-234157902.html
- https://www.medianama.com/2024/10/223-news-corp-sues-perplexity-ai-copyright-infringement-seeks-150k-per-violation/?trk=article-ssr-frontend-pulse_little-text-block
"""
import pathlib

import yaml

PROFILES_DIR = pathlib.Path(__file__).parent.parent / 'profiles'
ENTITIES_PATH = PROFILES_DIR / 'competitor-entities.yaml'

MECH_KEY = 'mechanism_519_newscorp_openai_dual_payer_woo_and_sue'

EXPECTED_URLS = [
    'https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/',
    'http://firstamendment.mtsu.edu/post/openai-to-start-using-news-content-from-news-corp-in-multiyear-deal/',
    'https://www.theregister.com/2024/05/23/openai_news_corp/?td=rt-9cs',
    'https://venturebeat.com/ai/openai-partners-with-wall-street-journal-publisher-news-corp',
    'https://www.adweek.com/morning-media-newsfeed/news-corp-strikes-content-licensing-deal-with-openai/',
    'https://www.reuters.com/legal/murdoch-firms-dow-jones-new-york-post-sue-perplexity-ai-2024-10-21/',
    'https://www.editorandpublisher.com/stories/news-corp-meta-in-ai-content-licensing-deal-worth-up-to-50-million-a-year,260471',
    'https://www.wsj.com/business/media/news-corp-meta-in-ai-content-licensing-deal-worth-up-to-50-million-a-year-d4fbf244',
    'https://www.engadget.com/ai/meta-signs-a-multimillion-dollar-ai-licensing-deal-with-news-corp-234157902.html',
    'https://www.medianama.com/2024/10/223-news-corp-sues-perplexity-ai-copyright-infringement-seeks-150k-per-violation/?trk=article-ssr-frontend-pulse_little-text-block',
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


def test_mechanism_519_present():
    m = get_mech()
    assert m['mechanism_id'] == 519
    assert m['iteration'] == 519


def test_rotation_and_job_ids():
    m = get_mech()
    assert m['rotation'] == 'Type C'
    assert m['job_id'] == 'mediascope-daily-iteration'
    assert m['goal_id'] == 'goal_54093bda4145'
    assert m['date_analyzed'] == '2026-09-04'
    assert m['time_pdt'] == '14:00'


def test_openai_deal_structure_announcement_date():
    m = get_mech()
    assert m['announcement_date'] == '2024-05-22'
    ds = m['deal_structure']
    assert '250' in ds['reported_value']
    assert 'answer' in ds['form'].lower() or 'answers' in ds['form'].lower()


def test_openai_deal_mastheads():
    m = get_mech()
    ds = m['deal_structure']
    assert 'Wall Street Journal' in ds['us_mastheads']
    assert 'New York Post' in ds['us_mastheads']
    assert 'The Sun' in ds['uk_mastheads']
    assert 'news.com.au' in ds['au_mastheads']


def test_openai_deal_exclusions():
    m = get_mech()
    assert 'HarperCollins' in m['deal_structure']['exclusions']
    assert 'Realtor.com' in m['deal_structure']['exclusions']


def test_largest_openai_publisher_deal_flag():
    m = get_mech()
    assert m['deal_structure']['largest_openai_publisher_deal'].startswith('largest documented')


def test_meta_second_leg():
    m = get_mech()
    leg = m['meta_second_leg']
    assert leg['announcement_date'] == '2026-03-04'
    assert 'Alexandra Bruell' in leg['reported_by']
    assert '50 million' in leg['terms']
    assert 'three years' in leg['terms']
    assert 'BOTH' in leg['dual_payer_status']


def test_sue_one_sign_other_sequence():
    m = get_mech()
    s = m['sue_one_sign_other_sequence']
    assert s['event'].startswith('Dow Jones and NY Post sued Perplexity AI')
    assert '2024-10-21' in s['event']
    assert 'RAG' in s['claims']
    assert '150,000' in s['relief_sought']
    assert '514' in s['sequencing_note']


def test_thomson_suit_quote():
    m = get_mech()
    assert 'abuse of intellectual property' in m['sue_one_sign_other_sequence']['thomson_quote']


def test_woo_and_sue_strategy():
    m = get_mech()
    w = m['woo_and_sue_strategy']
    assert 'woo and a sue' in w['thomson_quote']
    assert 'discount' in w['thomson_quote'] and 'penalty' in w['thomson_quote']
    assert 'Morgan Stanley' in w['venue']


def test_prediction_and_control_validation():
    m = get_mech()
    p = m['prediction_for_tracked_coverage']
    assert 'symmetric' in p['text']
    assert 'Christopher Mims' in p['control_validation']
    assert '2026' in p['timing_bound']


def test_meta_contrast_dual_vs_single_deal():
    m = get_mech()
    assert 'Conde Nast' in m['meta_contrast']
    assert 'neutralizing' in m['meta_contrast']


def test_extends_prior_mechanisms():
    m = get_mech()
    assert '514' in m['extends']
    assert 'tier-1' in m['extends']


def test_ranked_confounders_present():
    m = get_mech()
    c = m['ranked_confounders']
    assert len(c['strong']) >= 2
    assert 'owner-newsroom separation' in c['strong'][0]
    assert len(c['moderate']) >= 2
    assert len(c['weak']) >= 1
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
    # block ends at the next 2-space entity key after the mechanism block
    nxt = raw.index('\n  anthropic:', start)
    block = raw[start:nxt]
    block.encode('ascii')


def test_mechanism_id_unique_in_file():
    raw = get_raw()
    assert raw.count(MECH_KEY + ':') == 1


def test_no_silent_hash_truncation():
    # Regression guard for the #507 silent-mangle trap: every hand-written
    # scalar containing ' #' must survive parse intact.
    m = get_mech()
    raw = get_raw()
    assert 'woo and a sue' in m['woo_and_sue_strategy']['thomson_quote']
    assert 'Perplexity perpetrates' in m['sue_one_sign_other_sequence']['thomson_quote']
    assert '250 million' in m['deal_structure']['reported_value']
