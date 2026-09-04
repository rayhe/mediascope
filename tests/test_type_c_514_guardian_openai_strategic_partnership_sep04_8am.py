"""
Type C #514: Guardian x OpenAI strategic partnership (Feb 2025) - sue-one-sign-the-other
- Iteration #514 Type C Financial Incentive Mapping Sep 4 2026 08:00 PDT
- Rotation 513 B -> 514 C.
- Novelty verified: zero mechanism keys matching 'guardian' in
  profiles/competitor-entities.yaml before this run (grep verified); zero
  test_type_c files mentioning guardian-openai partnership (glob verified);
  the guardian.yaml profile carries a licensing_deals list entry but no
  mechanism_id-bearing mechanism. Extends (not duplicates) the existing
  publisher_content_deal_portfolio Guardian Feb 2025 listing with the first
  dedicated Type C deal mechanism for it.
- Findings (browser.search this run, 4 query sets, verbatim full-URL listings;
  no pages opened first-hand - all items via search-result excerpts, marked
  second-hand in-mechanism): Guardian-OpenAI strategic partnership announced
  Feb 14 2025 (GMG press release; trades Feb 17-20) - Guardian reporting and
  archive as ChatGPT news source, attributed short summaries and extracts,
  ChatGPT Enterprise internal rollout, terms undisclosed (spokesperson
  declined, Digiday), no explicit training-rights mention. Counterparties:
  Keith Underwood (CFO/COO, GMG - business-side signatory) and Brad Lightcap
  (COO, OpenAI) - the FIFTH Lightcap-signed publisher deal in the repo after
  #489 Hearst, #494 Vox, #499 Atlantic, #504 Conde Nast. Sue-one-sign-the-other:
  Feb 13 2025 the Guardian joined the News/Media Alliance suit vs Cohere
  (4,000+ works, SDNY, up to $150k/work, destruction sought) over unauthorized
  AI training - Bateson: 'egregious pattern of scraping... brazen theft and
  distortion of original journalism'; Feb 14 2025 the OpenAI deal was announced.
  Same conduct class litigated against the $5B Canadian lab and licensed to
  OpenAI within 24 hours. SPUR tension: Bateson co-founded the Standards for
  Publisher Usage Rights coalition (Feb 2026, with BBC/FT/Sky/Telegraph)
  demanding permission-or-payment standards one year after signing the bilateral
  OpenAI license. QuitGPT tension: Guardian ran a Bregman comment piece calling
  for a ChatGPT consumer boycott (~Mar 2026, bounded), flagged by Cadwalladr.
  Meta contrast: zero known Guardian-Meta AI licensing deals (per #513).
- Statistical discipline: qualitative structural mapping only; correlation not
  causation; is_significant false; no tone scores; no p_value.

Source URLs (all second-hand via search excerpts this run, Sep 4 2026):
- http://openai.com/index/openai-and-guardian-media-group-launch-content-partnership/
- http://EditorAndPublisher.com/stories/guardian-media-group-announces-strategic-partnership-with-openai,254405
- https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/
- https://www.engadget.com/ai/major-publishers-sue-ai-startup-cohere-over-copyright-infringement-165352238.html
- https://www.thenewworld.co.uk/rats-in-a-sack-the-guardians-hypocrisy-over-openai/
"""
import pathlib

import yaml

PROFILES_DIR = pathlib.Path(__file__).parent.parent / 'profiles'
ENTITIES_PATH = PROFILES_DIR / 'competitor-entities.yaml'

MECH_KEY = 'mechanism_514_guardian_openai_strategic_partnership'

EXPECTED_URLS = [
    'http://openai.com/index/openai-and-guardian-media-group-launch-content-partnership/',
    'http://EditorAndPublisher.com/stories/guardian-media-group-announces-strategic-partnership-with-openai,254405',
    'https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/',
    'https://www.thenewworld.co.uk/rats-in-a-sack-the-guardians-hypocrisy-over-openai/',
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


def test_mechanism_514_present():
    mech = get_mech()
    assert mech['mechanism_id'] == 514
    assert mech['iteration'] == 514


def test_rotation_and_job_ids():
    mech = get_mech()
    assert mech['rotation'] == 'Type C'
    assert mech['date_analyzed'] == '2026-09-04'
    assert mech['time_pdt'] == '08:00'
    assert mech['job_id'] == 'mediascope-daily-iteration'
    assert mech['goal_id'] == 'goal_54093bda4145'


def test_extends_existing_deal_portfolio():
    mech = get_mech()
    assert 'publisher_content_deal_portfolio' in mech['extends']
    data = load_entities()
    portfolio = data['entities']['openai']['publisher_content_deal_portfolio']
    partners = ' '.join(portfolio['notable_partners'])
    assert 'Guardian' in partners


def test_deal_structure_lightcap_fifth():
    ds = get_mech()['deal_structure']
    assert 'Lightcap' in ds['counterparties'][1]
    assert 'Underwood' in ds['counterparties'][0]
    assert 'fifth' in ds['lightcap_fifth']
    for tag in ('#489', '#494', '#499', '#504'):
        assert tag in ds['lightcap_fifth']


def test_deal_terms_opacity_and_training_rights():
    ds = get_mech()['deal_structure']
    assert ds['training_rights_explicit'] is False
    assert 'training' in ds['training_rights_note'].lower()
    assert ds['deal_terms_opacity']['exact_amount_undisclosed'] is True
    assert 'Digiday' in ds['deal_terms_opacity']['evidence']


def test_sue_one_sign_other_sequence():
    sq = get_mech()['sue_one_sign_other_sequence']
    assert sq['suit_date'] == '2025-02-13'
    assert '2025-02-14' in sq['deal_date']
    assert 'Cohere' in sq['suit'] and 'Guardian' in sq['suit']
    assert '4,000' in sq['suit']
    assert 'one day' in sq['sequence_gap']
    assert '$5B' in sq['sequence_gap']


def test_bateson_suit_quote():
    sq = get_mech()['sue_one_sign_other_sequence']
    assert 'brazen theft' in sq['bateson_suit_quote']
    assert 'egregious pattern' in sq['bateson_suit_quote']
    assert 'numerous partners' in sq['bateson_suit_quote']


def test_spur_tension():
    sp = get_mech()['spur_tension']
    assert 'Bateson' in sp['launch']
    assert '2026' in sp['launch']
    assert 'permission or payment' in sp['spur_complaint']
    assert 'BBC' in sp['launch'] and 'Financial Times' in sp['launch']


def test_quitgpt_editorial_tension():
    qg = get_mech()['quitgpt_editorial_tension']
    assert 'Bregman' in qg['event']
    assert 'Quit ChatGPT: right now!' in qg['event']
    assert 'Cadwalladr' in qg['flag']
    assert 'editorial-independence' in qg['bounded_note']
    assert 'bounded' in qg['event']


def test_meta_contrast_zero_deals():
    mech = get_mech()
    assert 'zero' in mech['meta_contrast'].lower()
    assert '#513' in mech['meta_contrast']
    assert 'CORRELATION NOT CAUSATION' in mech['meta_contrast']


def test_ranked_confounders_present():
    confs = get_mech()['ranked_confounders']
    assert len(confs) == 5
    assert confs[0]['strength'] == 'strong'
    assert 'coincidence' in confs[0]['confounder']
    assert confs[1]['strength'] == 'strong'
    assert 'second-hand' in confs[1]['confounder']


def test_statistical_discipline_flags():
    mech = get_mech()
    assert mech['correlation_not_causation'] is True
    assert mech['is_significant'] is False
    assert mech['statistical_scope'] == 'qualitative structural mapping only'
    assert mech['p_value'] == 'NOT_CALCULATED'


def test_source_urls_in_raw_yaml():
    raw = get_raw()
    for url in EXPECTED_URLS:
        assert url in raw, url


def test_mechanism_block_is_ascii():
    raw = get_raw()
    start = raw.index(MECH_KEY)
    end = raw.index('  anthropic:', start)
    block = raw[start:end]
    non_ascii = [c for c in block if ord(c) > 127]
    assert not non_ascii, non_ascii[:5]


def test_mechanism_id_unique_in_file():
    raw = get_raw()
    assert raw.count('mechanism_id: 514') == 1


def test_no_silent_hash_truncation():
    # Regression guard for the YAML plain-scalar '#' trap: values that must
    # contain '#' references survive parsing intact.
    mech = get_mech()
    assert '#513' in mech['meta_contrast']
    assert '#513' in mech['mediascope_relevance']
    assert '#504' in mech['deal_structure']['proactive_pre_deal_posture']
