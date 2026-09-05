"""
Type C #529: Canada Online News Act (C-18) - Google C$100M/yr Publisher
Dependency vs Meta Zero-Payment News Block - A Same-Market Natural Experiment
- Iteration #529 Type C Financial Incentive Mapping Sep 5 2026 01:00 PDT
- Rotation 528 B -> 529 C.
- Novelty verified: no mechanism_name containing C-18 / Canadian Journalism
  Collective / Online News Act dedicated mechanism in
  profiles/competitor-entities.yaml (grep verified: only prose mention is
  inside mechanism showcase_coercive_cycle->australia_termination as the
  Showcase-Canada termination anecdote, plus google entity prose); no Type C
  commit with C-18/Canada/Journalism Collective in the title
  (git log --grep verified); zero test_type_c_529 files on disk before this
  run (glob verified). This is the first dedicated Type C deal mechanism for
  the Canada experiment.
- Findings (browser.search this run, 3 query sets, verbatim full-URL listings;
  items via search-result excerpts and crawled article text, second-hand,
  marked bounded in-mechanism): Bill C-18 (Online News Act, royal assent Jun
  2023) designated exactly two companies (C$1B annual revenue + 20M monthly
  user threshold - only Google and Meta). Google: announced Nov 29 2023 a
  C$100M/yr deal (indexed to inflation, 5-year term) with the Canadian
  Journalism Collective (CJC, federally incorporated non-profit founded May
  2024), CRTC exemption granted Oct 2024; payments disbursed from Mar 2025 -
  C$22,193,608.09 to 108 news businesses by Apr 23 2025 (60% partial), C$55.2M
  to 338 news businesses by Jul 21 2025; ~450 of ~600 applicants eligible;
  ~C$13,798 per publisher FTE/yr (~C$6,806 for broadcasters); max single
  payment C$4.27M; CBC and Postmedia among the largest recipients (Unifor,
  Aug 2026). News Media Canada to UK CMA (Feb 13 2026): publishers hiring
  journalists after years of job losses. Meta: announced Jun 22 2023 it would
  end news on Facebook/Instagram in Canada, block effective Aug 2023, pays
  C$0; CRTC VP Broadcasting Scott Shortliffe wrote Meta counsel (Osler,
  Hoskin and Harcourt) Dec 3 2025 confirming no punishment, monitoring only;
  Canadian government in preliminary talks with Meta (Globe and Mail via
  Social Media Today, early 2026) about restoring news under a revised Act;
  US government seeking Act changes in trade negotiations.
- Natural experiment: same law, same threshold, same market; diametrically
  opposed financial postures (Google = quantified recurring dependency;
  Meta = zero-payment + two-year block that hurt independents reliant on
  Facebook referral traffic per Geist Oct 2024). NOT a coverage-tone claim:
  no tracked Canadian outlet sits in the MediaScope 7-publication corpus, so
  the predicted framing gradient is flagged for Type A follow-up, not
  asserted here.
- Statistical discipline: qualitative structural mapping only; correlation
  not causation; is_significant false; p_value NOT_CALCULATED; no tone
  scores.

Source URLs (all second-hand via search excerpts/crawls this run, Sep 5 2026):
- https://assets.publishing.service.gov.uk/media/69b970dc635612b767a46666/News_Media_Canada.pdf
- https://www.michaelgeist.ca/2024/10/crtc-approves-googles-100-million-online-news-act-exemption-deal/
- http://mediapost.com/publications/article/405544/google-makes-initial-payments-to-canadian-publishe.html
- https://www.editorandpublisher.com/stories/canadian-journalism-payments-show-proof-of-concept,255578
- https://www.thewirereport.ca/2024/12/16/canadian-journalism-collective-announces-estimated-amounts-it-expects-to-pay-out/
- https://unifor2000.ca/how-googles-funding-for-canadian-news-publishers-is-split-and-who-benefits-the-most/
- https://publications.gc.ca/collections/collection_2025/crtc/BC9-44-2025-eng.pdf
- https://jdi.queensu.ca/wp-content/uploads/2026/01/Kushniryk-Making-Platforms-Pay-%20JDI-Policy-Insight.pdf
- https://www.reuters.com/technology/meta-end-access-news-facebook-instagram-canada-2023-06-22/
- https://www.iphoneincanada.ca/2025/12/04/ottawa-wont-punish-facebook-for-blocking-news-links-regulator-says/
- https://Www.socialmediatoday.com/news/canadian-government-looks-to-bring-news-content-back-to-facebook/810763/
"""
import glob
import os
import pathlib

import yaml

PROFILES_DIR = pathlib.Path(__file__).parent.parent / 'profiles'
ENTITIES_PATH = PROFILES_DIR / 'competitor-entities.yaml'

MECH_KEY = 'mechanism_529_canada_c18_google_100m_meta_zero_natural_experiment'

EXPECTED_URLS = [
    'https://assets.publishing.service.gov.uk/media/69b970dc635612b767a46666/News_Media_Canada.pdf',
    'https://www.michaelgeist.ca/2024/10/crtc-approves-googles-100-million-online-news-act-exemption-deal/',
    'http://mediapost.com/publications/article/405544/google-makes-initial-payments-to-canadian-publishe.html',
    'https://www.editorandpublisher.com/stories/canadian-journalism-payments-show-proof-of-concept,255578',
    'https://www.thewirereport.ca/2024/12/16/canadian-journalism-collective-announces-estimated-amounts-it-expects-to-pay-out/',
    'https://unifor2000.ca/how-googles-funding-for-canadian-news-publishers-is-split-and-who-benefits-the-most/',
    'https://publications.gc.ca/collections/collection_2025/crtc/BC9-44-2025-eng.pdf',
    'https://jdi.queensu.ca/wp-content/uploads/2026/01/Kushniryk-Making-Platforms-Pay-%20JDI-Policy-Insight.pdf',
    'https://www.reuters.com/technology/meta-end-access-news-facebook-instagram-canada-2023-06-22/',
    'https://www.iphoneincanada.ca/2025/12/04/ottawa-wont-punish-facebook-for-blocking-news-links-regulator-says/',
    'https://Www.socialmediatoday.com/news/canadian-government-looks-to-bring-news-content-back-to-facebook/810763/',
]


def load_entities():
    with open(ENTITIES_PATH, encoding='utf-8') as f:
        return yaml.safe_load(f)


def get_raw():
    return ENTITIES_PATH.read_text(encoding='utf-8')


def get_mech():
    return load_entities()['entities']['google'][MECH_KEY]


def test_competitor_entities_yaml_parses():
    d = load_entities()
    assert 'entities' in d and 'google' in d['entities']


def test_mechanism_529_present():
    m = get_mech()
    assert m['mechanism_id'] == 529
    assert m['iteration'] == 529


def test_rotation_and_job_ids():
    m = get_mech()
    assert m['rotation'] == 'Type C'
    assert m['job_id'] == 'mediascope-daily-iteration'
    assert m['goal_id'] == 'goal_54093bda4145'
    assert m['date_analyzed'] == '2026-09-05'
    assert m['time_pdt'] == '01:00'


def test_google_leg_core_terms():
    m = get_mech()
    g = m['google_leg']
    assert g['annual_contribution_cad_m'] == 100
    assert g['inflation_indexed'] is True
    assert g['term_years'] == 5
    assert 'Canadian Journalism Collective' in g['distributor']
    assert 'CRTC' in g['exemption_granted_by']
    assert 'full-time equivalent' in g['distribution_basis']


def test_google_leg_disbursement_math():
    m = get_mech()
    g = m['google_leg']
    assert 'C$13,798' in g['estimated_per_fte_publisher']
    assert 'C$6,806' in g['estimated_per_fte_broadcaster']
    assert 'C$22,193,608.09' in g['disbursement_as_of_2025_04_23']
    assert '108' in g['disbursement_as_of_2025_04_23']
    assert 'C$55.2M' in g['disbursement_as_of_2025_07_21']
    assert '338' in g['disbursement_as_of_2025_07_21']
    assert '450' in g['eligible_applicants']
    assert 'C$4.27M' in g['max_single_payment_observed']
    assert 'CBC' in g['largest_recipients_reported']
    assert 'Postmedia' in g['largest_recipients_reported']


def test_google_leg_news_media_canada_quote():
    m = get_mech()
    q = m['google_leg']['news_media_canada_feb_2026']
    assert 'hire journalists' in q
    assert 'UK CMA' in q


def test_meta_leg_block_and_zero_payment():
    m = get_mech()
    d = m['meta_leg']
    assert d['payments_to_canadian_publishers'] == 0
    assert d['news_block_announcement'] == '2023-06-22'
    assert d['news_block_effective'] == '2023-08'


def test_meta_leg_crtc_no_punishment():
    m = get_mech()
    d = m['meta_leg']['crtc_dec_2025']
    assert 'Shortliffe' in d
    assert 'Dec 3, 2025' in d
    assert 'no enforcement action' in d


def test_meta_leg_2026_talks():
    m = get_mech()
    d = m['meta_leg']['govt_talks_2026']
    assert 'Globe and Mail' in d
    assert 'trade negotiations' in d


def test_natural_experiment_two_company_threshold():
    m = get_mech()
    n = m['natural_experiment_structure']
    assert 'Only Google and Meta' in n['same_threshold']
    assert 'C$1B' in n['same_threshold']
    assert 'C$100M/yr' in n['google_response']
    assert 'total exit from news' in n['meta_response']


def test_prediction_explicitly_not_verified():
    m = get_mech()
    p = m['natural_experiment_structure']['prediction']
    assert 'NOT VERIFIED' in p
    assert 'Type A follow-up' in p
    assert 'Android XR' in p


def test_geist_assessment_present():
    m = get_mech()
    g = m['natural_experiment_structure']['geist_assessment']
    assert 'Michael Geist' in g
    assert 'lost Facebook referral traffic' in g
    assert 'major miscalculation' in g


def test_us_contagion_jcpa_context():
    m = get_mech()
    u = m['us_contagion']
    assert 'JCPA' in u
    assert 'Oregon' in u


def test_extends_prior_mechanisms():
    m = get_mech()
    assert '519' in m['extends']
    assert '524' in m['extends']


def test_ranked_confounders_present():
    m = get_mech()
    c = m['ranked_confounders']
    assert len(c['strong']) == 2
    assert len(c['moderate']) == 2
    assert len(c['weak']) == 2
    assert any('Compelled' in s for s in c['strong'])
    assert any('modest' in s for s in c['strong'])
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
    nxt = raw.index('    cma_regulatory_neutralization:', start)
    block = raw[start:nxt]
    block.encode('ascii')


def test_mechanism_id_unique_in_file():
    raw = get_raw()
    assert raw.count(MECH_KEY + ':') == 1


def test_no_silent_hash_truncation():
    # Regression guard for the #507 silent-mangle trap: hand-written scalars
    # must survive parse intact (per AGENTS.md rule, all are single-quoted).
    m = get_mech()
    assert 'C$13,798' in m['google_leg']['estimated_per_fte_publisher']
    assert 'NOT VERIFIED' in m['natural_experiment_structure']['prediction']
    assert 'https://Www.socialmediatoday.com' in m['source_urls'][10]


def test_novelty_no_other_529_files():
    here = os.path.dirname(os.path.abspath(__file__))
    matches = glob.glob(os.path.join(here, 'test_type_c_529*'))
    assert len(matches) == 1, matches
