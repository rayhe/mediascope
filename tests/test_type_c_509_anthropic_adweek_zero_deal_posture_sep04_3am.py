"""
Type C #509: Anthropic institutionalized zero-deal posture (Adweek, ~Aug 26 2026)
- Iteration #509 Type C Financial Incentive Mapping Sep 4 2026 03:00 PDT
- Rotation 508 B -> 509 C.
- Novelty verified: zero test_type_c files mentioning adweek/stenberg/turvey
  (glob verified before writing); zero 'stenberg' or 'On Background' mentions
  in profiles/competitor-entities.yaml (grep verified); mechanism_509 key
  absent before this run (grep count 0). Extends (not duplicates) the existing
  publisher_deals_note zero-deal mapping and the Press Gazette Aug 2026
  confirmation with a second independent trade-press source read first-hand.
- Findings (browser.open first-hand this run on the Adweek URL, full text read;
  date inferred ~Aug 26 2026 from the search-result relative timestamp 9 days
  before the Sep 4 read, marked weak-confounder in-mechanism): Adweek 'On
  Background with Mark Stenberg' newsletter piece on why Anthropic never signed
  a publisher licensing deal and never got sued by a digital publisher
  (headline corrected from 'never been sued'; $1.5B Bartz authors settlement
  stands). Named partnerships owner Tom Turvey (VP product partnerships, joined
  Feb 2024); 'pick up the phone twice a day and say no' institutionalized
  refusal; fair-use ideological line per all five sources; enterprise-only data
  strategy ('half a million medical journal articles in Dutch'); publisher-suit
  economics (NYT ~$30M OpenAI case spend as deterrence); brand-as-legal-shield
  ('good actors ... doing no harm'); xAI as zero-deal/zero-suit companion.
- Statistical discipline: qualitative structural mapping only; correlation not
  causation; is_significant false; no tone scores; no p_value.

Source (first-hand this run, Sep 4 2026):
- https://www.adweek.com/media/anthropic-content-licensing-lawsuits-publishers/
"""
import pathlib

import yaml

PROFILES_DIR = pathlib.Path(__file__).parent.parent / 'profiles'
ENTITIES_PATH = PROFILES_DIR / 'competitor-entities.yaml'

MECH_KEY = 'mechanism_509_anthropic_institutionalized_zero_deal_posture'

EXPECTED_URL = 'https://www.adweek.com/media/anthropic-content-licensing-lawsuits-publishers/'


def load_entities():
    with open(ENTITIES_PATH, encoding='utf-8') as f:
        return yaml.safe_load(f)


def get_raw():
    with open(ENTITIES_PATH, encoding='utf-8') as f:
        return f.read()


def get_mech():
    data = load_entities()
    return data['entities']['anthropic'][MECH_KEY]


def test_competitor_entities_yaml_parses():
    assert load_entities() is not None


def test_mechanism_509_present():
    mech = get_mech()
    assert mech['mechanism_id'] == 509
    assert mech['iteration'] == 509


def test_rotation_and_job_ids():
    mech = get_mech()
    assert mech['rotation'] == 'Type C'
    assert mech['date_analyzed'] == '2026-09-04'
    assert mech['time_pdt'] == '03:00'
    assert mech['job_id'] == 'mediascope-daily-iteration'
    assert mech['goal_id'] == 'goal_54093bda4145'


def test_extends_existing_zero_deal_note():
    mech = get_mech()
    assert 'publisher_deals_note' in mech['extends']
    data = load_entities()
    assert 'publisher_deals_note' in data['entities']['anthropic']


def test_source_block_first_hand():
    src = get_mech()['source']
    assert src['outlet'] == 'Adweek'
    assert src['read_first_hand'] is True
    assert src['read_date'] == '2026-09-04'
    assert src['url'] == EXPECTED_URL
    assert 'Stenberg' in src['column']
    assert 'never sued by a digital publisher' in src['correction_note']


def test_findings_turvey_and_refusal():
    findings = get_mech()['findings']
    assert 'Turvey' in findings['partnerships_owner']
    assert 'February 2024' in findings['partnerships_owner']
    assert 'twice a day and say no' in findings['institutionalized_refusal']
    assert 'fair use' in findings['fair_use_ideological_line']


def test_findings_suit_inventory_and_economics():
    findings = get_mech()['findings']
    inv = findings['publisher_suit_inventory']
    assert len(inv) == 4
    joined = ' '.join(inv)
    for name in ('Ziff Davis', 'Perplexity', 'Cohere', 'Penske Media'):
        assert name in joined
    assert '$30M' in findings['timing_defense'] or '30M' in findings['timing_defense']


def test_findings_brand_shield_and_xai():
    findings = get_mech()['findings']
    assert 'good actors' in findings['brand_as_legal_shield']
    assert 'xAI' in findings['xai_companion']
    assert '965B' in findings['valuation_crosscheck']


def test_meta_contrast_zero_vs_thirteen():
    mech = get_mech()
    assert '13' in mech['meta_contrast']
    assert 'zero' in mech['meta_contrast'].lower()


def test_ranked_confounders_present():
    confs = get_mech()['ranked_confounders']
    assert len(confs) == 3
    assert confs[0]['strength'] == 'strong'
    assert 'Troveo' in confs[0]['confounder'] or 'undisclosed' in confs[0]['confounder']


def test_statistical_discipline_flags():
    mech = get_mech()
    assert mech['correlation_not_causation'] is True
    assert mech['is_significant'] is False
    assert mech['statistical_scope'] == 'qualitative structural mapping only'


def test_source_url_in_raw_yaml():
    assert EXPECTED_URL in get_raw()


def test_mechanism_block_is_ascii():
    raw = get_raw()
    start = raw.index(MECH_KEY)
    end = raw.index('author_settlement_source: https://www.pymnts.com')
    block = raw[start:end]
    non_ascii = [c for c in block if ord(c) > 127]
    assert not non_ascii, non_ascii[:5]


def test_mechanism_id_unique_in_file():
    raw = get_raw()
    assert raw.count('mechanism_id: 509') == 1
