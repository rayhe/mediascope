"""
Type C #539: Dotdash Meredith (People Inc) Triple-Payer AI Revenue Architecture -
OpenAI Flat-Fee (May 7 2024) + Microsoft PCM Pay-Per-Use (Nov 5 2025) +
Meta Dec 2025 Multi-Year
- Iteration #539 Type C Financial Incentive Mapping Sep 5 2026 11:00 PDT
- Rotation 538 B -> 539 C.
- Novelty verified: zero triple-payer mechanism in
  profiles/competitor-entities.yaml before insertion (repo grep verified);
  zero People Inc / Microsoft PCM DDM-leg mechanism before insertion (repo
  grep verified); zero DDM Meta-leg mechanism before insertion (only the
  meta_ai_deals bullet); zero test_type_c_539 files on disk before this run
  (glob verified); no Type C commit with 539 or triple-payer in the title
  (git log --grep verified). Distinct from mechanism 534 (OpenAI leg only)
  and mechanism 519 (dual-payer, different publisher). First triple-payer
  mechanism in the corpus.
- Findings (browser.search this run, 4 query sets, verbatim full-URL
  listings; items via search-result excerpts, second-hand, marked bounded
  in-mechanism):
  - Leg 2 (Microsoft PCM): announced Nov 5 2025 during IAC Q3 earnings -
    People Inc (formerly Dotdash Meredith, renamed Jul 31 2025) as launch
    partner in Microsoft Publisher Content Marketplace; pay-per-use
    ("a la carte") model with Copilot as first buyer; Vogel characterized
    the earlier OpenAI deal as "all-you-can-eat"; terms undisclosed;
    Vogel praised Microsoft commitment to paying for content; Cloudflare
    crawler-blocking "brought almost everyone to the table"; Google search
    referrals fell 54 percent to 24 percent of traffic over two years,
    attributed to AI Overviews; IAC Q3 2025: People Inc digital revenue
    +9 percent to $269M, performance marketing +38 percent, licensing
    +24 percent.
  - Leg 3 (Meta): Dec 5 2025, Reuters reporting Axios - People Inc among
    8 Dec 2025 Meta publishers, multi-year, undisclosed, entertainment
    and lifestyle content for Meta AI (corpus meta_ai_deals partners list).
  - Zero-deal entities: Anthropic (zero-deal posture re-confirmed Aug
    2026, Adweek, Turvey quote), Google (no AI licensing deal, adversarial
    traffic leg), Amazon (no deal known), Apple (no standalone AI deal;
    Apple News+ commingles in licensing line per mechanism 534).
  - Structural contrast: News Corp dual-payer (#519) -> DDM first
    triple-payer; Conde Nast ($0 from Meta) is the mirror image on the
    Meta leg (DDM has Meta, CN does not); Hearst dual (OpenAI + Amazon
    Rufus, #489) is one leg short of DDM.
  - No coverage-tone claim: Lifewire Meta-vs-OpenAI-vs-Microsoft tone
    comparison flagged as future Type A, NOT asserted here
    (iteration-492 rule).
- Statistical discipline: qualitative structural mapping only; correlation
  not causation; is_significant false; p_value NOT_CALCULATED; tone scores
  NOT_SCORED.

Source URLs (all second-hand via search excerpts this run, Sep 5 2026):
- https://www.indexbox.io/blog/people-inc-signs-ai-content-licensing-deal-with-microsoft/
- https://dig.watch/updates/microsoft-deal-signals-pay-per-use-path-for-ai-access-to-people-inc-content
- https://www.findarticles.com/people-inc-signs-microsoft-ai-licensing-deal/
- https://www.reuters.com/business/meta-strikes-multiple-ai-deals-with-news-publishers-axios-reports-2025-12-05/
- https://www.adweek.com/media/anthropic-content-licensing-lawsuits-publishers/
- https://www.adweek.com/media/openai-dotdash-meredith-licensing-payment/
"""
import pathlib

import yaml

PROFILES_DIR = pathlib.Path(__file__).parent.parent / 'profiles'
ENTITIES_PATH = PROFILES_DIR / 'competitor-entities.yaml'

MECH_KEY = 'mechanism_539_dotdash_meredith_triple_payer_openai_meta_microsoft_pcm'

EXPECTED_URLS = [
    'https://www.indexbox.io/blog/people-inc-signs-ai-content-licensing-deal-with-microsoft/',
    'https://dig.watch/updates/microsoft-deal-signals-pay-per-use-path-for-ai-access-to-people-inc-content',
    'https://www.findarticles.com/people-inc-signs-microsoft-ai-licensing-deal/',
    'https://www.reuters.com/business/meta-strikes-multiple-ai-deals-with-news-publishers-axios-reports-2025-12-05/',
    'https://www.adweek.com/media/anthropic-content-licensing-lawsuits-publishers/',
    'https://www.adweek.com/media/openai-dotdash-meredith-licensing-payment/',
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

    def test_mechanism_539_present_under_openai(self):
        m = get_mech()
        assert m['mechanism_id'] == 539
        assert m['iteration'] == 539

    def test_rotation_and_job_ids(self):
        m = get_mech()
        assert m['rotation'] == 'Type C'
        assert m['job_id'] == 'mediascope-daily-iteration'
        assert m['goal_id'] == 'goal_54093bda4145'
        assert m['date_analyzed'] == '2026-09-05'
        assert m['time_pdt'] == '11:00'

    def test_mechanism_not_under_wrong_entity(self):
        d = load_entities()
        for entity in ('google', 'anthropic', 'meta', 'amazon', 'apple'):
            if entity in d['entities']:
                assert MECH_KEY not in d['entities'][entity]

    def test_type_financial_incentive_mapping(self):
        m = get_mech()
        assert m['type'] == 'financial_incentive_mapping'


class TestTriplePayerLegs:
    def test_three_legs_present(self):
        m = get_mech()
        for leg in ('leg_1_openai', 'leg_2_microsoft_pcm', 'leg_3_meta'):
            assert leg in m, leg

    def test_leg_1_openai_flat_fee_references_534(self):
        leg = get_mech()['leg_1_openai']
        assert leg['announcement_date'] == '2024-05-07'
        assert 'mechanism 534' in leg['summary']
        assert '16M' in leg['payment']
        assert 'all-you-can-eat' in leg['model']

    def test_leg_2_microsoft_pcm_date_and_form(self):
        leg = get_mech()['leg_2_microsoft_pcm']
        assert leg['announcement_date'] == '2025-11-05'
        assert 'Publisher Content Marketplace' in leg['form']
        assert leg['first_buyer'] == 'Microsoft Copilot'
        assert leg['terms'] == 'undisclosed'

    def test_leg_2_pay_per_use_vogel_language(self):
        leg = get_mech()['leg_2_microsoft_pcm']
        assert 'pay-per-use' in leg['model']
        assert 'a la carte' in leg['model']

    def test_leg_2_announced_at_iac_q3_earnings(self):
        leg = get_mech()['leg_2_microsoft_pcm']
        assert 'IAC Q3 2025' in leg['announced_at']
        assert leg['sequence'] == 'second AI deal after OpenAI'

    def test_leg_3_meta_date_and_scope(self):
        leg = get_mech()['leg_3_meta']
        assert leg['announcement_date'] == '2025-12-05'
        assert leg['reported_by'] == 'Reuters reporting Axios'
        assert leg['scope'] == 'entertainment and lifestyle content for Meta AI'

    def test_leg_3_included_in_meta_round_of_8(self):
        leg = get_mech()['leg_3_meta']
        assert 'People Inc' in leg['included_in_meta_round']
        assert 'CNN' in leg['included_in_meta_round']


class TestZeroDealEntitiesAndGoogleAdversarialLeg:
    def test_zero_deal_set_has_four_entities(self):
        z = get_mech()['zero_deal_entities']
        assert [e['entity'] for e in z] == ['Anthropic', 'Google', 'Amazon', 'Apple']

    def test_anthropic_zero_deal_reconfirmed_aug_2026(self):
        a = get_mech()['zero_deal_entities'][0]
        assert a['entity'] == 'Anthropic'
        assert a['mechanism'] == 509
        assert 'Aug 2026' in a['status']
        assert 'twice a day' in a['status']

    def test_google_adversarial_traffic_collapse(self):
        g = get_mech()['google_adversarial_leg']
        assert g['search_referrals_two_years_ago'] == '54 percent of People Inc traffic'
        assert g['search_referrals_q3_2025'] == '24 percent of traffic'
        assert g['attributed_to'].startswith('Google AI Overviews')

    def test_google_adversarial_bot_blocking_leverage(self):
        g = get_mech()['google_adversarial_leg']
        assert 'Cloudflare' in g['leverage']
        assert 'almost everyone to the table' in g['leverage']

    def test_vogel_pricing_distinction_stack(self):
        v = get_mech()['vogel_pricing_distinction']
        assert 'all-you-can-eat' in v['openai_model']
        assert 'a la carte' in v['microsoft_pcm_model']
        assert '18 months' in v['significance']

    def test_earnings_signal_materializing(self):
        e = get_mech()['earnings_signal']
        assert '$269M' in e['iac_q3_2025']
        assert '24 percent' in e['iac_q3_2025']


class TestDirectionalPredictions:
    def _as_pairs(self):
        # YAML parses "- Key: value" list items as single-key dicts
        pairs = {}
        for item in get_mech()['directional_predictions']:
            pairs.update(item)
        return pairs

    def test_predictions_cover_all_seven_entities(self):
        p = self._as_pairs()
        for entity in ('OpenAI', 'Microsoft', 'Meta', 'Google', 'Anthropic', 'Amazon', 'Apple'):
            assert entity in p, entity

    def test_meta_leg_corrects_meta_zero_assumption(self):
        p = self._as_pairs()
        assert 'CORRECTS any assumption that DDM is Meta-zero' in p['Meta']

    def test_payers_predict_softer_zero_dealers_predict_no_softening(self):
        p = self._as_pairs()
        soft = [k for k, v in p.items() if 'predicts softer coverage' in v]
        assert sorted(soft) == ['Meta', 'Microsoft', 'OpenAI']
        zero = [k for k, v in p.items() if 'no softening pressure' in v]
        assert sorted(zero) == ['Amazon', 'Anthropic', 'Apple']

    def test_google_predicted_harder(self):
        p = self._as_pairs()
        assert 'adversarial' in p['Google'] and 'predicts harder coverage' in p['Google']


class TestStructuralContrastAndNovelty:
    def _as_pairs(self):
        pairs = {}
        for item in get_mech()['structural_contrast']:
            pairs.update(item)
        return pairs

    def test_newscorp_519_first_triple_payer_extension(self):
        c = self._as_pairs()
        assert 'first triple-payer in corpus' in c['news_corp_dual_payer_519']

    def test_conde_nast_meta_leg_mirror_image(self):
        c = self._as_pairs()
        assert '$0 from Meta' in c['conde_nast_504']
        assert 'mirror image' in c['conde_nast_504']

    def test_hearst_489_one_leg_short(self):
        c = self._as_pairs()
        assert 'Amazon Rufus' in c['hearst_489']

    def test_lifewire_beat_exposure_and_type_a_flag(self):
        t = get_mech()['tech_review_beat_exposure']
        assert 'lifewire' in t['lifewire'].lower()
        assert 'NOT verified this run' in t['type_a_followup']
        assert 'Ziff Davis' in t['boundary_note']

    def test_five_ranked_confounders_and_counterargument(self):
        m = get_mech()
        ranks = [c['rank'] for c in m['ranked_confounders']]
        assert ranks == [1, 2, 3, 4, 5]
        assert 'null' in m['strongest_counterargument'].lower()


class TestSourceUrlsVerbatim:
    def test_all_six_source_urls_present_verbatim(self):
        m = get_mech()
        for url in EXPECTED_URLS:
            assert url in m['source_urls'], url

    def test_no_constructed_urls_in_block(self):
        raw = get_raw_block()
        assert 'example.com' not in raw
        for line in raw.split('\n'):
            stripped = line.strip()
            if stripped.startswith('- https://'):
                url = stripped[2:].strip()
                assert ' ' not in url, url

    def test_meta_reuters_url_is_axios_sourced(self):
        m = get_mech()
        meta_url = 'https://www.reuters.com/business/meta-strikes-multiple-ai-deals-with-news-publishers-axios-reports-2025-12-05/'
        assert meta_url in m['source_urls']


class TestYamlIntegrityAscii:
    def test_block_is_ascii_only(self):
        raw = get_raw_block()
        bad = [ch for ch in raw if ord(ch) > 127]
        assert not bad, bad[:10]

    def test_statistical_discipline_qualitative_only(self):
        m = get_mech()
        assert 'p_value NOT_CALCULATED' in m['statistical_discipline']
        assert 'is_significant False' in m['statistical_discipline']
        assert 'tone_scores NOT_SCORED' in m['statistical_discipline']
