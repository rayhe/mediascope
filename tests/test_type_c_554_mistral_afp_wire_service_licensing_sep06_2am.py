"""
Type C #554: Mistral AI x AFP Wire-Service Content Licensing Deal (Jan 2025) -
Multi-Year, Terms Undisclosed, First Non-US-Lab Mechanism, Completes the
Wire-Service AI-Licensing Triad
- Iteration #554 Type C Financial Incentive Mapping Sep 6 2026 02:00 PDT
- Rotation 553 B -> 554 C.
- Novelty verified: zero mistral entity in profiles/competitor-entities.yaml
  before insertion (grep verified - only investor-side mechanism 188 inside
  the samsung entity); zero test files with 554 on disk before this run (glob
  verified); no Type C commit with 554 in the title (git log --grep verified);
  zero 'mistral.*afp' hits in tests/ before this run (grep verified).
  Distinct from mechanism 188 (Mistral AI investment context, investor-side),
  mechanism 509 (Anthropic zero-deal posture, the small-lab counterexample
  that DID pay), and mechanisms 519/524/549 (newspaper-publisher deals) -
  first WIRE-SERVICE (wholesale, not branded) licensing mechanism and first
  non-US AI lab payer mechanism, placed under the new mistral entity (payer
  entity, mirroring the 544-under-openai and 549-under-meta conventions).
- Findings (browser.search this run, verbatim full-URL listings; deal facts
  via search-result excerpts, second-hand, marked bounded in-mechanism):
  - Deal: announced Jan 16, 2025, via Mistral press release + AFP announcement;
    simultaneous multi-outlet coverage (TechCrunch, Sifted, Neowin, ReadWrite).
  - Terms: multi-year agreement, length not disclosed; financial details not
    disclosed by either party.
  - Scope: full AFP text news archive dating back to 1983 plus daily feed of
    ~2,300 text stories/day in six languages (French, English, Spanish,
    Portuguese, German, Arabic); photos and videos excluded (text only).
  - Product: Le Chat, Mistral's conversational AI assistant; AFP stories
    consulted for current-information queries and cited inline; stated purpose
    is factuality grounding / hallucination reduction, especially for business
    users.
  - Mistral positioning: Sifted frames Mistral as a European alternative to
    Big Tech LLM builders 'such as OpenAI, Meta and Google' - Meta named
    explicitly as the competitive set; first content partnership of this kind
    for Mistral; founded 2023, raised over EUR 1bn, valued at EUR 5.8bn at
    signing.
  - Timing: announced one day after Google's similar deal with The Associated
    Press (Jan 15, 2025); OpenAI announced an Axios content partnership the
    same week and disclosed 20 media partnerships.
  - Wire-service AI-licensing triad: AP licensed to OpenAI (Jul 2023) and
    Google/Gemini (Jan 15, 2025); Reuters licensed to Meta for Meta AI
    real-time news answers (Oct 25, 2024; multi-year, terms confidential,
    Reuters compensated); AFP licensed to Mistral (Jan 16, 2025). All three
    global wire services now carry a flagship AI-lab payer, each from a
    different lab; AFP was the last of the three to license. Wire services
    are wholesale news suppliers feeding thousands of downstream outlets
    including tracked publications, so payer relationships at the wire layer
    propagate structurally through the news supply chain.
  - Executive quotes: Arthur Mensch (Mistral CEO/co-founder) on verified
    professional journalism; Fabrice Fries (AFP CEO) on diversifying revenue
    beyond the media sector and the 'European identity' framing.
  - Directional predictions (predictions, not findings): Mistral softer
    (direct payer); Meta neutral to no-deal on the AFP leg (wire leg sits
    with Reuters); OpenAI neutral (AP leg); Google neutral (AP leg, day
    before); Anthropic adversarial slot (zero-deal posture, #509).
  - Structural contrasts: 188 (investor-side complement), 509 (small-lab
    counterexample), 519/524/549 (newspaper-publisher deals), OpenAI x AP /
    Google x AP (other wire legs), Meta x Reuters (Meta's wire leg; AFP is
    the wire Meta did NOT pay).
  - No coverage-tone claim (no AFP post-deal Mistral-vs-Meta tone analysis
    in corpus).
- Statistical discipline: qualitative structural mapping only; correlation
  not causation; is_significant false; p_value NOT_CALCULATED; tone scores
  NOT_SCORED.

Source URLs (deal facts second-hand via search excerpts this run, Sep 6 2026):
- https://techcrunch.com/2025/01/16/mistral-signs-deal-with-afp-to-offer-up-to-date-answers-in-le-chat/
- https://sifted.eu/articles/mistral-afp-partnership-news
- https://www.neowin.net/news/mistral-ais-chatgpt-competitor-now-features-afp-news-items-thanks-to-partnership/
- https://readwrite.com/mistral-ai-announces-partnership-with-press-organization-afp/
- https://mediaconnect.com/afp-and-mistral-ai-announce-global-partnership-to-enhance-ai-responses-with-reliable-news-content
- https://dig.watch/updates/afp-partnership-strengthens-mistrals-global-reach
- https://www.reuters.com/technology/artificial-intelligence/meta-platforms-use-reuters-news-content-ai-chatbot-2024-10-25/?ref=aileap&utm_source=aileap&utm_medium=referral
"""
import pathlib
import re

import yaml

PROFILES_DIR = pathlib.Path(__file__).parent.parent / 'profiles'
ENTITIES_PATH = PROFILES_DIR / 'competitor-entities.yaml'

MECH_KEY = 'mechanism_554_mistral_afp_wire_service_licensing'

EXPECTED_URLS = [
    'https://techcrunch.com/2025/01/16/mistral-signs-deal-with-afp-to-offer-up-to-date-answers-in-le-chat/',
    'https://sifted.eu/articles/mistral-afp-partnership-news',
    'https://www.neowin.net/news/mistral-ais-chatgpt-competitor-now-features-afp-news-items-thanks-to-partnership/',
    'https://readwrite.com/mistral-ai-announces-partnership-with-press-organization-afp/',
    'https://mediaconnect.com/afp-and-mistral-ai-announce-global-partnership-to-enhance-ai-responses-with-reliable-news-content',
    'https://dig.watch/updates/afp-partnership-strengthens-mistrals-global-reach',
    'https://www.reuters.com/technology/artificial-intelligence/meta-platforms-use-reuters-news-content-ai-chatbot-2024-10-25/?ref=aileap&utm_source=aileap&utm_medium=referral',
]


def load_entities():
    with open(ENTITIES_PATH, encoding='utf-8') as f:
        return yaml.safe_load(f)


def get_entity():
    return load_entities()['entities']['mistral']


def get_mech():
    return get_entity()[MECH_KEY]


def get_raw_block():
    raw = ENTITIES_PATH.read_text(encoding='utf-8')
    start = raw.index('    ' + MECH_KEY + ':')
    end = raw.index('relationship_types:', start)
    return raw[start:end]


class TestMechanismPresenceAndIdentity:
    def test_yaml_parses_and_mistral_entity_present(self):
        e = load_entities()['entities']
        assert 'mistral' in e
        assert e['mistral']['display_name'] == 'Mistral AI'

    def test_mechanism_554_present_under_mistral(self):
        m = get_mech()
        assert m['mechanism_id'] == 554
        assert m['iteration'] == 554

    def test_rotation_and_job_ids(self):
        m = get_mech()
        assert m['rotation'] == 'Type C'
        assert m['job_id'] == 'mediascope-daily-iteration'
        assert m['goal_id'] == 'goal_54093bda4145'
        assert m['date_analyzed'] == '2026-09-06'
        assert m['time_pdt'] == '02:00'

    def test_mechanism_not_under_wrong_entity(self):
        entities = load_entities()['entities']
        for other in ('meta', 'openai', 'google', 'anthropic', 'samsung'):
            assert MECH_KEY not in entities[other], other

    def test_type_financial_incentive_mapping(self):
        assert get_mech()['type'] == 'financial_incentive_mapping'


class TestDealTerms:
    def test_multi_year_term_length_undisclosed(self):
        assert 'multi-year' in get_mech()['deal_terms']['structure']
        assert 'not disclosed' in get_mech()['deal_terms']['structure']

    def test_financial_terms_undisclosed(self):
        assert 'not disclosed' in get_mech()['deal_terms']['value']

    def test_archive_back_to_1983(self):
        assert '1983' in get_mech()['deal_terms']['scope']

    def test_daily_volume_and_six_languages(self):
        scope = get_mech()['deal_terms']['scope']
        assert '2,300' in scope
        for lang in ('French', 'English', 'Spanish', 'Portuguese', 'German', 'Arabic'):
            assert lang in scope, lang

    def test_photos_videos_excluded(self):
        assert 'not part of the agreement' in get_mech()['deal_terms']['exclusions']

    def test_le_chat_product_grounding(self):
        product = get_mech()['deal_terms']['product']
        assert 'Le Chat' in product
        assert get_mech()['deal_terms']['stated_purpose'].startswith('factuality grounding')


class TestWireServiceTriad:
    def test_ap_leg_openai_and_google(self):
        ap = get_mech()['wire_service_ai_licensing_triad']['ap_leg']
        assert 'OpenAI' in ap and 'Jul 2023' in ap
        assert 'Google' in ap and 'Jan 15, 2025' in ap

    def test_reuters_leg_meta(self):
        rw = get_mech()['wire_service_ai_licensing_triad']['reuters_leg']
        assert 'Meta' in rw and 'Oct 25, 2024' in rw
        assert 'Reuters compensated' in rw

    def test_afp_leg_this_mechanism(self):
        afp = get_mech()['wire_service_ai_licensing_triad']['afp_leg']
        assert 'Mistral' in afp and 'Jan 16, 2025' in afp

    def test_triad_all_three_wires_have_payers(self):
        sig = get_mech()['wire_service_ai_licensing_triad']['triad_significance']
        assert 'AFP was the last of the three to license' in sig
        assert 'wholesale news suppliers' in sig

    def test_one_day_after_google_ap_timing(self):
        assert 'one day after' in get_mech()['mistral_positioning']['deal_timing']


class TestMistralPositioning:
    def test_european_alternative_names_meta_competitor(self):
        alt = get_mech()['mistral_positioning']['european_alternative']
        assert 'Meta' in alt and 'OpenAI' in alt and 'Google' in alt

    def test_first_content_partnership_of_kind(self):
        assert 'first content partnership' in get_mech()['mistral_positioning']['first_of_kind']

    def test_scale_at_signing_figures(self):
        scale = get_mech()['mistral_positioning']['scale_at_signing']
        assert 'EUR 1 billion' in scale and 'EUR 5.8 billion' in scale


class TestDirectionalPredictions:
    def test_five_predictions_present(self):
        preds = get_mech()['directional_predictions']
        assert len(preds) == 5

    def test_predictions_not_findings_flag(self):
        assert get_mech()['predictions_not_findings'] is True

    def test_structural_contrasts_include_188_509_519(self):
        joined = ' '.join(get_mech()['structural_contrasts'])
        for token in ('188', '509', '519', 'Meta x Reuters'):
            assert token in joined, token


class TestConfoundersAndDiscipline:
    def test_five_ranked_confounders(self):
        confs = get_mech()['ranked_confounders']
        assert len(confs) == 5
        assert [c['rank'] for c in confs] == [1, 2, 3, 4, 5]

    def test_confounder_strengths_labeled(self):
        strengths = [c['strength'] for c in get_mech()['ranked_confounders']]
        assert strengths == ['strong', 'strong', 'moderate', 'moderate', 'weak']

    def test_strongest_is_terms_undisclosed(self):
        assert 'undisclosed' in get_mech()['ranked_confounders'][0]['confounder']

    def test_statistical_discipline_qualitative_only(self):
        sd = get_mech()['statistical_discipline']
        assert sd['p_value'] == 'NOT_CALCULATED'
        assert sd['is_significant'] is False
        assert sd['tone_scores'] == 'NOT_SCORED'
        assert sd['correlation_not_causation'] is True

    def test_caution_no_tone_claim(self):
        assert get_mech()['no_coverage_tone_claim'] is True
        assert get_mech()['cautious_language_required'] is True


class TestNoveltyAndSourceUrls:
    def test_novelty_first_wire_service_mechanism(self):
        focus = get_mech()['type_c_focus']
        assert 'first wire-service' in focus
        assert 'first mechanism for a non-US AI lab payer' in focus

    def test_all_seven_source_urls_present_verbatim(self):
        raw = get_raw_block()
        for url in EXPECTED_URLS:
            assert url in raw, url

    def test_no_constructed_urls_in_block(self):
        raw = get_raw_block()
        found = re.findall(r'https?://[^\s\'"]+', raw)
        for url in found:
            assert url in EXPECTED_URLS, url

    def test_reuters_meta_leg_url_verbatim_with_query_params(self):
        raw = get_raw_block()
        assert '?ref=aileap&utm_source=aileap&utm_medium=referral' in raw


class TestYamlIntegrityAscii:
    def test_block_is_ascii_only(self):
        raw = get_raw_block()
        assert all(ord(c) < 128 for c in raw), 'non-ASCII char in block'

    def test_raw_block_boundaries(self):
        raw = get_raw_block()
        assert raw.startswith('    ' + MECH_KEY + ':')
        assert 'mechanism_554' in raw
