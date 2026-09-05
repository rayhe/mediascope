"""
Type C #534: Dotdash Meredith x OpenAI Strategic Content Partnership (May 7 2024)
- Earliest Lightcap-Counterparty Publisher Deal, $16M Fixed Plus Variable
  Payment Structure, Ad-Tech (D/Cipher) Leg, Consumer-Tech Review Beat
  (Lifewire) Exposure
- Iteration #534 Type C Financial Incentive Mapping Sep 5 2026 06:00 PDT
- Rotation 533 B -> 534 C.
- Novelty verified: zero dedicated Dotdash Meredith mechanism in
  profiles/competitor-entities.yaml before insertion (repo grep verified -
  only comparison mentions: mechanism 386 deal-value band, line 2592 annual
  value list, and portfolio-list names); no Type C commit with Dotdash in
  the title (git log --grep verified); zero test_dotdash files in tests/
  before this run (glob verified); zero test_type_c_534 files on disk
  (glob verified). First dedicated DDM mechanism in the repo.
- Findings (browser.search this run, 3 query sets, verbatim full-URL
  listings; items via search-result excerpts, second-hand, marked bounded
  in-mechanism):
  - Announced May 7 2024 (IAC PRNewswire release; Reuters same-day): multiyear
    strategic partnership and licensing agreement, term length undisclosed.
  - Three legs: (1) content licensing - historical and ongoing DDM content for
    model training; (2) attribution surfacing - DDM content and links displayed
    in ChatGPT responses; (3) ad-tech collaboration - OpenAI models deployed to
    enhance D/Cipher, DDM's cookieless intent-based ad targeting (launched May
    2023).
  - Payment anatomy (Adweek, Nov 2024): approximately $16M/yr fixed, quarterly
    ~$4M installments booked in the licensing revenue line (which also includes
    Apple News+ payments); variable appearance-frequency payment (leaked
    Adweek pitch deck) not yet received/reported as of Nov 2024 - floor $16M,
    no verified ceiling. Formally undisclosed (Reuters: financial details not
    disclosed).
  - Earnings impact: Q2 2024 DDM revenue $425.2M (+3%), licensing+other +19%
    "led by partnerships with Apple News+ and OpenAI" (Reuters Aug 6 2024);
    pre-deal licensing avg $25.5M/qtr (7 quarters) vs $29.75M/qtr post-deal
    (2 quarters) per Adweek; $16M fixed is ~3.6% of DDM's $439M Q3 revenue
    (Adweek's annual-vs-quarter comparison, reproduced as reported).
  - Lightcap sequencing correction: DDM (May 7 2024) is the EARLIEST
    Lightcap-counterparty publisher deal in the corpus; the repo's Lightcap
    sequence (#489 Hearst, #494 Vox, #499 Atlantic, #504 Conde Nast,
    #514 Guardian-as-fifth) counts mechanism-order, not chronological order.
  - Tech-review beat exposure: release names "rigorous product reviews" as a
    licensed content category; Lifewire is the DDM consumer-tech vertical
    (bounded via Wikipedia/third-party portfolio sources). Boundary stated in
    mechanism: PCMag is Ziff Davis, NOT DDM - no PCMag claim made.
  - People Inc. rebrand (Jul 31 2025) included as bounded Wikipedia-sourced note.
  - No coverage-tone claim: no Lifewire OpenAI-vs-Meta tone analysis exists;
    flagged as Type A follow-up (Lifewire coverage) and Type B follow-up
    (disclosure practice) - NOT asserted here.
- Statistical discipline: qualitative structural mapping only; correlation
  not causation; is_significant false; p_value NOT_CALCULATED; tone scores
  NOT_SCORED.

Source URLs (all second-hand via search excerpts this run, Sep 5 2026):
- https://www.iac.com/press-releases/dotdash-meredith-announces-strategic-partnership-with-openai-bringing-iconic-brands-and-trusted-content-to-chatgpt?skip=0
- https://www.reuters.com/markets/deals/investopedia-owner-dotdash-meridith-signs-content-license-deal-with-openai-2024-05-07/?taid=663a4b5da3010f000118141a&utm_campaign=trueAnthem:+Trending+Content&utm_medium=trueAnthem&utm_source=twitter
- https://www.adweek.com/media/openai-dotdash-meredith-licensing-payment/
- https://www.engadget.com/openai-partners-with-people-publisher-dotdash-meredith-212832821.html
- https://www.mediapost.com/publications/article/395858/dotdash-meredith-forms-a-strategic-partnership-wit.html
- https://www.reuters.com/business/media-telecom/iacs-core-profit-rises-after-unit-dotdash-meredith-sees-uptick-advertising-2024-08-06/
- https://www.benton.org/headlines/openai-inks-licensing-deal-dotdash-meredith
- https://en.wikipedia.org/wiki/People_Inc.
- https://en.wikipedia.org/wiki/Dotdash_Meredith
"""
import re

import yaml

import pathlib

PROFILES_DIR = pathlib.Path(__file__).parent.parent / 'profiles'
ENTITIES_PATH = PROFILES_DIR / 'competitor-entities.yaml'
ITERATION_LOG = pathlib.Path(__file__).parent.parent / 'iteration-log.md'

MECH_KEY = 'mechanism_534_dotdash_meredith_openai_earliest_lightcap_consumer_review_beat'

EXPECTED_URLS = [
    'https://www.iac.com/press-releases/dotdash-meredith-announces-strategic-partnership-with-openai-bringing-iconic-brands-and-trusted-content-to-chatgpt?skip=0',
    'https://www.reuters.com/markets/deals/investopedia-owner-dotdash-meridith-signs-content-license-deal-with-openai-2024-05-07/?taid=663a4b5da3010f000118141a&utm_campaign=trueAnthem:+Trending+Content&utm_medium=trueAnthem&utm_source=twitter',
    'https://www.adweek.com/media/openai-dotdash-meredith-licensing-payment/',
    'https://www.engadget.com/openai-partners-with-people-publisher-dotdash-meredith-212832821.html',
    'https://www.mediapost.com/publications/article/395858/dotdash-meredith-forms-a-strategic-partnership-wit.html',
    'https://www.reuters.com/business/media-telecom/iacs-core-profit-rises-after-unit-dotdash-meredith-sees-uptick-advertising-2024-08-06/',
    'https://www.benton.org/headlines/openai-inks-licensing-deal-dotdash-meredith',
    'https://en.wikipedia.org/wiki/People_Inc.',
    'https://en.wikipedia.org/wiki/Dotdash_Meredith',
]


def load_entities():
    with open(ENTITIES_PATH, encoding='utf-8') as f:
        return yaml.safe_load(f)


def get_mech():
    return load_entities()['entities']['openai'][MECH_KEY]


def get_raw_block():
    raw = ENTITIES_PATH.read_text(encoding='utf-8')
    start = raw.index('    ' + MECH_KEY + ':')
    end = raw.index('  anthropic:', start)
    return raw[start:end]


class TestMechanismPresenceAndIdentity:
    def test_yaml_parses_and_openai_entity_present(self):
        d = load_entities()
        assert 'entities' in d and 'openai' in d['entities']

    def test_mechanism_534_present_under_openai(self):
        m = get_mech()
        assert m['mechanism_id'] == 534
        assert m['iteration'] == 534

    def test_rotation_and_job_ids(self):
        m = get_mech()
        assert m['rotation'] == 'Type C'
        assert m['job_id'] == 'mediascope-daily-iteration'
        assert m['goal_id'] == 'goal_54093bda4145'
        assert m['date_analyzed'] == '2026-09-05'
        assert m['time_pdt'] == '06:00'
        assert m['announcement_date'] == '2024-05-07'

    def test_mechanism_not_under_wrong_entity(self):
        d = load_entities()
        for entity in ('google', 'anthropic', 'meta', 'amazon', 'apple'):
            if entity in d['entities']:
                assert MECH_KEY not in d['entities'][entity]

    def test_type_c_focus_first_dedicated_ddm(self):
        m = get_mech()
        assert 'First dedicated Dotdash Meredith mechanism' in m['type_c_focus']


class TestDealStructure:
    def test_three_legs_present(self):
        m = get_mech()
        legs = m['deal_structure']['three_legs']
        keys = {list(leg.keys())[0] for leg in legs}
        assert keys == {'leg_1_content_licensing', 'leg_2_attribution_surfacing',
                        'leg_3_adtech_collaboration'}

    def test_adtech_leg_distinguishes_hearst(self):
        m = get_mech()
        leg3 = m['deal_structure']['three_legs'][2]['leg_3_adtech_collaboration']
        assert 'D/Cipher' in leg3
        assert 'cookieless' in leg3

    def test_counterparties_vogel_and_lightcap(self):
        m = get_mech()
        cp = m['deal_structure']['counterparties']
        assert 'Neil Vogel' in cp['dotdash_meredith']
        assert 'Brad Lightcap' in cp['openai']

    def test_content_categories_include_product_reviews(self):
        m = get_mech()
        cats = m['deal_structure']['content_categories_named_in_release']
        assert 'rigorous product reviews' in cats

    def test_release_brands_named(self):
        m = get_mech()
        brands = m['deal_structure']['brands_named_in_release']
        assert 'PEOPLE' in brands
        assert 'Investopedia' in brands
        assert len(brands) >= 6


class TestPaymentAnatomy:
    def test_fixed_payment_16m(self):
        m = get_mech()
        t = m['deal_terms']
        assert t['exact_amount_formally_undisclosed'] is True
        assert '16M' in t['fixed_payment_reported'] or '$16M' in t['fixed_payment_reported']

    def test_quarterly_installments(self):
        m = get_mech()
        assert '4M' in m['deal_terms']['fixed_payment_reported']

    def test_variable_payment_unreported_floor_not_ceiling(self):
        m = get_mech()
        v = m['deal_terms']['variable_payment']
        assert 'not yet received' in v
        assert 'at least $16M' in v
        assert 'unbounded above' in v

    def test_licensing_revenue_before_after(self):
        m = get_mech()
        t = m['deal_terms']
        assert '25.5M' in t['licensing_revenue_before']
        assert '29.75M' in t['licensing_revenue_after']

    def test_earnings_q2_2024(self):
        m = get_mech()
        q = m['earnings_impact']['q2_2024']
        assert '425.2M' in q
        assert '19%' in q
        assert 'Apple News+ and OpenAI' in q

    def test_dual_payer_apple_news_note(self):
        m = get_mech()
        assert 'Apple News+' in m['earnings_impact']['dual_payer_note']
        assert 'second financial dependency' in m['earnings_impact']['dual_payer_note']


class TestLightcapSequencingAndExposure:
    def test_earliest_lightcap_correction(self):
        m = get_mech()
        s = m['lightcap_sequencing_correction']
        assert 'EARLIEST' in s['correction']
        assert 'mechanism-order' in s['sequence_context']
        assert '514 Guardian (Feb 2025, framed as fifth)' in s['sequence_context']

    def test_lifewire_tech_review_beat(self):
        m = get_mech()
        b = m['tech_review_beat_exposure']
        assert 'Lifewire' in b['lifewire']
        assert 'bounded' in b['lifewire']
        assert 'rigorous product reviews' in b['licensed_product_reviews']

    def test_pcmag_boundary_explicitly_stated(self):
        m = get_mech()
        assert 'Ziff Davis' in m['tech_review_beat_exposure']['boundary_note']
        assert 'no PCMag claim' in m['tech_review_beat_exposure']['boundary_note']

    def test_type_a_followup_flagged_not_verified(self):
        m = get_mech()
        assert 'NOT verified' in m['tech_review_beat_exposure']['type_a_followup_flagged']

    def test_rebrand_note_bounded(self):
        m = get_mech()
        assert 'People Inc.' in m['rebrand_note']['detail']
        assert 'bounded' in m['rebrand_note']['detail']

    def test_disclosure_posture_unknown_bounded(self):
        m = get_mech()
        d = m['disclosure_posture']
        assert 'bounded unknown' in d['known']
        assert 'NOT verified' in d['type_b_followup_flagged']


class TestConfoundersDisciplineAndHygiene:
    def test_five_ranked_confounders(self):
        m = get_mech()
        confs = m['ranked_confounders']
        assert len(confs) == 5
        strengths = {c['strength'] for c in confs}
        assert 'strong' in strengths and 'moderate' in strengths

    def test_strongest_counterargument_present(self):
        m = get_mech()
        c = m['strongest_counterargument']
        assert '3.6%' in c
        assert 'the null (independent review standards)' in c

    def test_statistical_discipline(self):
        m = get_mech()
        s = m['statistical_discipline']
        assert 'p_value NOT_CALCULATED' in s
        assert 'is_significant False' in s
        assert 'NOT_SCORED' in s

    def test_caution_structural_mapping_only(self):
        m = get_mech()
        assert 'No coverage-tone claim is made' in m['caution']

    def test_source_urls_verbatim_and_https(self):
        m = get_mech()
        assert m['source_urls'] == EXPECTED_URLS
        assert all(u.startswith('https://') for u in m['source_urls'])

    def test_block_ascii_only_no_em_dashes(self):
        block = get_raw_block()
        non_ascii = [c for c in block if ord(c) > 127]
        assert non_ascii == [], non_ascii

    def test_cross_references_cover_lightcap_sequence(self):
        m = get_mech()
        refs = ' '.join(m['cross_references'])
        for rid in ('386', '489', '494', '478', '468', '504'):
            assert rid in refs, rid


class TestIterationLog:
    def test_iteration_534_entry_present(self):
        text = ITERATION_LOG.read_text(encoding='utf-8')
        assert '#534 Type C' in text

    def test_iteration_534_entry_near_top_and_descending(self):
        text = ITERATION_LOG.read_text(encoding='utf-8')
        ids = [int(x) for x in re.findall(r'^#(\d+) Type', text, re.M)]
        assert 534 in ids
        assert ids[0] == 534
        # leading run of recent entries must be strictly descending (#523 sits
        # deep in the log from a historical late append, per #530 repair note)
        run = []
        for i in ids:
            if run and i >= run[-1]:
                break
            run.append(i)
        assert run == sorted(run, reverse=True)
        assert run[:2] == [534, 533]
