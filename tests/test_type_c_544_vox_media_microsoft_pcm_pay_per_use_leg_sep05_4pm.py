"""
Type C #544: Vox Media x Microsoft Publisher Content Marketplace Pay-Per-Use Leg
(Feb 2026) - OpenAI-Plus-Microsoft Dual Payer, Meta $0, Co-Design Partner
- Iteration #544 Type C Financial Incentive Mapping Sep 5 2026 16:00 PDT
- Rotation 543 B -> 544 C.
- Novelty verified: zero Vox Media x Microsoft PCM mechanism in
  profiles/competitor-entities.yaml before insertion (repo grep verified);
  zero Vox Media x Meta mechanism before insertion (repo grep verified);
  zero test_type_c_544 files on disk before this run (glob verified); no
  Type C commit with 544 in the title (git log --grep verified). Distinct
  from mechanism 494 (OpenAI leg only) and mechanism 539 (DDM triple-payer,
  different publisher). The PCM co-design role existed only as profile notes
  in the-verge.yaml/wired.yaml; this is the first competitor-entities
  mechanism formalizing it for a tracked publication's parent.
- Findings (browser.search this run, verbatim full-URL listings; items via
  search-result excerpts, second-hand, marked bounded in-mechanism):
  - PCM leg: launched ~Feb 2026 by Microsoft Advertising; usage-based /
    pay-per-use pricing ("publishers will be paid on delivered value");
    Vox Media explicitly named a co-design partner ("codesigning PCM with
    companies including Verge parent Vox Media"); first-wave pilot partners:
    Business Insider Inc, Vox Media Inc, USA Today Co., People Inc, AP,
    Hearst Magazines, Conde Nast; Copilot first buyer, Yahoo onboarding;
    WSJ (~Jul 2026): eight-publisher pilot, Microsoft invested north of
    $10M including publisher payments, expects to rise.
  - Dual-payer matrix: OpenAI leg (May 29 2024, mechanism 494, undisclosed
    terms) + Microsoft PCM leg (pay-per-use) - Vox spans both pricing
    models, the flat-fee-plus-usage stack first documented at DDM (#539);
    both payers sit in the $13.75B OpenAI-Microsoft investment nexus
    (in-corpus datum, mechanism 82), so legs aggregate at nexus level.
  - RSL leverage leg: Vox Media joined the Really Simple Licensing
    Collective Nov 26 2025 (Digiday); 50+ partners; pay-per-crawl /
    pay-per-inference standard; Fastly enforcement; non-exclusive -
    leverage infrastructure, not a payer.
  - Meta contrast: zero known Vox Media x Meta AI deals as of Sep 5 2026;
    this run's searches returned none (bounded absence, iteration-492
    rule); cleanest owner-level Meta-$0 asymmetry among tracked pubs.
  - Directional predictions (predictions, not findings): Microsoft softer,
    OpenAI softer, Google mixed, Meta harder.
  - Structural contrasts: DDM #539 (Vox is the Meta-leg mirror - DDM
    collects from all three, Vox $0 from Meta); Conde Nast #504 (PCM
    co-design + $0 Meta companion); Hearst #489 (PCM first-wave, one leg
    short); mechanism 82 dependency spiral.
  - No coverage-tone claim (no The Verge post-PCM Microsoft tone analysis).
- Statistical discipline: qualitative structural mapping only; correlation
  not causation; is_significant false; p_value NOT_CALCULATED; tone scores
  NOT_SCORED.

Source URLs (all second-hand via search excerpts this run, Sep 5 2026):
- https://searchengineland.com/microsoft-launches-publisher-content-marketplace-for-ai-licensing-468191
- https://www.gadgets360.com/ai/news/microsoft-publisher-content-marketplace-licensing-platform-ai-usage-introduced-10946054?pfrom=home-ndtvworld_world_gadgets&technology
- https://digiday.com/media/qa-nikhil-kolar-vp-microsoft-ai-scales-its-click-to-sign-ai-content-marketplace/
- https://www.wsj.com/business/media/marketplaces-are-the-next-frontier-in-publisher-deals-with-ai-companies-11515b00
- https://technologymag.org/microsoft-says-its-building-an-app-store-for-ai-content-licensing/
- http://digiday.com/media/arena-group-buzzfeed-usa-today-co-vox-media-join-rsls-ai-content-licensing-efforts/
- https://www.voxmedia.com/2024/5/29/24166483/vox-media-openai-strategic-content-and-product-partnership/
"""
import pathlib

import yaml

PROFILES_DIR = pathlib.Path(__file__).parent.parent / 'profiles'
ENTITIES_PATH = PROFILES_DIR / 'competitor-entities.yaml'

MECH_KEY = 'mechanism_544_vox_media_microsoft_pcm_pay_per_use_leg'

EXPECTED_URLS = [
    'https://searchengineland.com/microsoft-launches-publisher-content-marketplace-for-ai-licensing-468191',
    'https://www.gadgets360.com/ai/news/microsoft-publisher-content-marketplace-licensing-platform-ai-usage-introduced-10946054?pfrom=home-ndtvworld_world_gadgets&technology',
    'https://digiday.com/media/qa-nikhil-kolar-vp-microsoft-ai-scales-its-click-to-sign-ai-content-marketplace/',
    'https://www.wsj.com/business/media/marketplaces-are-the-next-frontier-in-publisher-deals-with-ai-companies-11515b00',
    'https://technologymag.org/microsoft-says-its-building-an-app-store-for-ai-content-licensing/',
    'http://digiday.com/media/arena-group-buzzfeed-usa-today-co-vox-media-join-rsls-ai-content-licensing-efforts/',
    'https://www.voxmedia.com/2024/5/29/24166483/vox-media-openai-strategic-content-and-product-partnership/',
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

    def test_mechanism_544_present_under_openai(self):
        m = get_mech()
        assert m['mechanism_id'] == 544
        assert m['iteration'] == 544

    def test_rotation_and_job_ids(self):
        m = get_mech()
        assert m['rotation'] == 'Type C'
        assert m['job_id'] == 'mediascope-daily-iteration'
        assert m['goal_id'] == 'goal_54093bda4145'
        assert m['date_analyzed'] == '2026-09-05'
        assert m['time_pdt'] == '16:00'
        assert m['announcement_date'] == '2026-02'

    def test_mechanism_not_under_wrong_entity(self):
        d = load_entities()
        for entity in ('google', 'anthropic', 'meta', 'amazon', 'apple'):
            if entity in d['entities']:
                assert MECH_KEY not in d['entities'][entity]

    def test_type_financial_incentive_mapping(self):
        m = get_mech()
        assert m['type'] == 'financial_incentive_mapping'
        assert 'dual payer' in m['mechanism_name'].lower()
        assert 'dual-payer' in m['type_c_focus'].lower()


class TestPCMLegDealStructure:
    def test_pay_per_use_form(self):
        s = get_mech()['deal_structure']
        assert 'pay-per-use' in s['form']
        assert 'paid based on how that content is used' in s['form']

    def test_vox_named_codesign_partner(self):
        s = get_mech()['deal_structure']
        assert 'Verge parent Vox Media' in s['vox_role']

    def test_first_wave_partners_seven_named(self):
        s = get_mech()['deal_structure']
        partners = s['first_wave_partners']
        for name in ('Business Insider Inc', 'Vox Media Inc', 'USA Today Co.',
                     'People Inc', 'The Associated Press', 'Hearst Magazines',
                     'Conde Nast'):
            assert name in partners, name

    def test_pilot_scale_eight_publishers_and_ten_million(self):
        s = get_mech()['deal_structure']
        assert 'eight publishers' in s['pilot_scale']
        assert '$10M' in s['pilot_scale']
        assert 'Tim Frank' in s['pilot_scale']

    def test_first_buyer_copilot_yahoo_onboarding(self):
        s = get_mech()['deal_structure']
        assert 'Copilot' in s['first_buyer']
        assert 'Yahoo' in s['first_buyer']

    def test_pricing_model_delivered_value(self):
        s = get_mech()['deal_structure']
        assert 'paid on delivered value' in s['pricing_model']
        assert 'usage-based reporting' in s['pricing_model']

    def test_ownership_voluntary_and_editorial_independence(self):
        s = get_mech()['deal_structure']
        assert 'voluntary' in s['ownership']
        assert 'editorial independence' in s['ownership']


class TestDualPayerMatrix:
    def test_openai_leg_references_494_and_undisclosed(self):
        x = get_mech()['dual_payer_matrix']
        assert 'mechanism 494' in x['openai_leg']
        assert 'undisclosed' in x['openai_leg']
        assert 'Forte' in x['openai_leg']

    def test_pricing_distinction_flat_vs_usage(self):
        x = get_mech()['dual_payer_matrix']
        assert 'flat' in x['pricing_distinction']
        assert 'pay-per-use' in x['pricing_distinction']
        assert 'mechanism 539' in x['pricing_distinction']

    def test_payer_nexus_13_75b_aggregation(self):
        x = get_mech()['dual_payer_matrix']
        assert '$13.75B' in x['payer_nexus']
        assert 'mechanism 82' in x['payer_nexus']
        assert 'not fully independent' in x['payer_nexus']


class TestRSLLeverageLeg:
    def test_joined_nov_2025_with_named_peers(self):
        r = get_mech()['rsl_leverage_leg']
        assert 'Nov 26 2025' in r['joined']
        for name in ('Arena Group', 'BuzzFeed', 'USA Today Co.'):
            assert name in r['joined'], name

    def test_structure_fifty_partners_pay_per_crawl(self):
        r = get_mech()['rsl_leverage_leg']
        assert '50+ partners' in r['structure']
        assert 'pay-per-crawl' in r['structure']
        assert 'Fastly' in r['structure']
        assert 'Doug Leeds' in r['structure']

    def test_non_exclusive_and_not_a_payer(self):
        r = get_mech()['rsl_leverage_leg']
        assert 'non-exclusive' in r['exclusivity']
        assert 'not a payer' in r['role']
        assert 'mechanism 539' in r['role']


class TestMetaContrastAndPredictions:
    def test_meta_contrast_zero_deal_bounded(self):
        m = get_mech()
        assert '$0 from Meta' in m['meta_contrast']
        assert 'iteration-492' in m['meta_contrast']
        assert 'mechanism 494' in m['meta_contrast']

    def test_directional_predictions_four_entities(self):
        m = get_mech()
        preds = m['directional_predictions']
        assert isinstance(preds, list) and len(preds) == 4
        text = ' '.join(preds)
        assert 'Microsoft: softer' in text
        assert 'OpenAI: softer' in text
        assert 'Google: mixed' in text
        assert 'Meta: harder' in text
        assert m['predictions_not_findings'] is True

    def test_structural_contrasts_ddm_mirror(self):
        m = get_mech()
        text = '\n'.join(m['structural_contrasts'])
        assert '539' in text and 'mirror' in text
        assert '$0 from Meta' in text
        assert '504' in text
        assert '489' in text
        assert '82' in text


class TestConfoundersAndDiscipline:
    def test_five_ranked_confounders_strong_weak(self):
        m = get_mech()
        ranks = [c['rank'] for c in m['ranked_confounders']]
        assert ranks == [1, 2, 3, 4, 5]
        strengths = [c['strength'] for c in m['ranked_confounders']]
        assert strengths[0] == 'strong' and strengths[1] == 'strong'
        assert strengths[4] == 'weak'
        assert 'No The Verge post-PCM coverage-tone analysis' in m['ranked_confounders'][1]['confounder']

    def test_strongest_counterargument_null_predicts_no_effect(self):
        m = get_mech()
        assert 'null' in m['strongest_counterargument'].lower()
        assert 'no tone effect' in m['strongest_counterargument'].lower()

    def test_statistical_discipline_qualitative_only(self):
        m = get_mech()
        assert 'p_value NOT_CALCULATED' in m['statistical_discipline']
        assert 'is_significant False' in m['statistical_discipline']
        assert 'tone_scores NOT_SCORED' in m['statistical_discipline']
        assert 'correlation not causation' in m['statistical_discipline']

    def test_caution_no_tone_claim(self):
        m = get_mech()
        assert 'No coverage-tone claim is made' in m['caution']


class TestNoveltyAndSourceUrls:
    def test_novelty_distinguishes_494_and_539(self):
        m = get_mech()
        text = '\n'.join(m['novelty_verification'])
        assert 'mechanism 494' in text
        assert 'mechanism 539' in text
        assert 'test_type_c_544' in text
        assert 'the-verge.yaml' in text

    def test_all_seven_source_urls_present_verbatim(self):
        m = get_mech()
        for url in EXPECTED_URLS:
            assert url in m['source_urls'], url

    def test_no_constructed_urls_in_block(self):
        raw = get_raw_block()
        assert 'example.com' not in raw
        for line in raw.split('\n'):
            stripped = line.strip()
            if stripped.startswith('- http'):
                url = stripped[2:].strip()
                assert ' ' not in url, url


class TestYamlIntegrityAscii:
    def test_block_is_ascii_only(self):
        raw = get_raw_block()
        bad = [ch for ch in raw if ord(ch) > 127]
        assert not bad, bad[:10]

    def test_raw_block_boundaries(self):
        raw = get_raw_block()
        assert raw.strip().startswith('mechanism_544_vox_media_microsoft_pcm_pay_per_use_leg:')
        assert 'mechanism_539' not in raw.split('mechanism_544')[0][-200:]
