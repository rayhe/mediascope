"""
Type C #569: Washington Post x OpenAI Strategic Partnership (Apr 22 2025) Plus
Google News AI Pilot (Dec 11 2025) - Second OpenAI-Plus-Google Dual-Payer
Publisher After FT, Terms Undisclosed on Both Legs, Bezos-Owned Paper With
Zero Meta/Amazon/Apple/Anthropic AI Money
- Iteration #569 Type C Financial Incentive Mapping Sep 6 2026 17:00 PDT
- Rotation 568 B -> 569 C.
- Novelty verified: zero dedicated washington_post / Washington Post mechanism
  blocks in profiles/competitor-entities.yaml before insertion (grep verified;
  WaPo previously appeared only as a coverage-stat line and in portfolio
  lists); zero test files with 569 on disk before this run (glob verified);
  no commit with 569 in the title (git log --grep verified).
  Distinct from mechanism 437 (FT dual payer - the SAME OpenAI-plus-Google
  payer pair at a tracked publication), mechanism 489 (Hearst dual payer -
  OpenAI plus Amazon, different second payer), mechanism 514 (Guardian x
  OpenAI - single leg), mechanism 331 (Meta AI licensing network - WaPo
  absent from Meta's Dec 2025 bundle), mechanism 559 (Amazon x NYT - Amazon's
  flagship publisher deal; Bezos-owned WaPo gets $0 from Amazon).
- Findings (browser.search this run, 3 query sets, verbatim full-URL
  listings; deal facts via search-result excerpts, second-hand, marked
  bounded in-mechanism):
  - OpenAI leg: strategic partnership announced Apr 22 2025 - ChatGPT shows
    summaries, quotes, links to WaPo journalism with clear attribution and
    direct links. Financial terms undisclosed (WaPo declined to share when
    asked, TechCrunch). Peter Elkins-Williams (WaPo head of global
    partnerships) quote on meeting audiences where they are. Varun Shetty
    (OpenAI media partnerships) - 500M+ weekly ChatGPT users. WaPo remains
    LLM-agnostic while building own AI tools (Ask The Post AI, Climate
    Answers, Haystacker). One of 20+ OpenAI publisher deals spanning 160+
    publications in 20+ languages.
  - Google leg: News AI pilot announced Dec 11 2025 - Google's first
    AI-focused publisher deals; believed to involve cash payments with
    extended display rights and APIs, but explicitly NOT licensing deals
    (Press Gazette). Nine publishers incl. WaPo, Guardian, Der Spiegel,
    El Pais, Folha, Infobae, Kompas, Times of India, Washington Examiner.
    FT joined Feb 2026. NY Post Jun 26 2026 (via The Information): Google
    wants broad rights incl. AI training; Showcase ending as leverage;
    Jason Kint: "This is Google's game. They're gonna dominate here."
  - Dual-payer significance: WaPo is the second OpenAI-plus-Google dual-payer
    publisher in the corpus after FT (mechanism 437). Bezos owns WaPo
    personally (2013); Amazon the company pays WaPo $0. Meta $0 (WaPo absent
    from the Dec 5 2025 seven-publisher bundle, mechanism 331). Amazon $0.
    Apple $0. Anthropic $0 (mechanism 509).
  - Directional predictions (predictions, not findings): OpenAI softer
    (direct payer, ChatGPT display); Google softer-to-neutral (pilot, not a
    licensing deal, cash unconfirmed); Meta/Amazon/Apple neutral to no-deal;
    Anthropic zero-deal slot.
  - No coverage-tone claim (WaPo is not a tracked publication; Type A
    follow-up would need a WaPo corpus that does not exist here).
- Statistical discipline: qualitative structural mapping only; correlation
  not causation; is_significant false; p_value NOT_CALCULATED; tone scores
  NOT_SCORED.

Source URLs (deal facts second-hand via search excerpts this run, Sep 6 2026):
- https://techcrunch.com/2025/04/22/chatgpts-responses-will-now-include-washington-post-articles
- https://www.thewrap.com/openai-washington-post-chatgpt-search-results-deal/
- http://www.neowin.net/news/the-washington-post-strikes-a-deal-with-openai-to-share-content-with-chatgpt/
- https://www.maginative.com/article/the-washington-post-joins-openais-expanding-roster-of-media-partners/
- https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/
- http://www.loeb.com/en/newsevents/news/2025/05/media-briefing-what-the-washington-posts-deal-with-openai-says-about-the-future
- https://nypost.com/2026/06/26/business/google-looks-to-bleed-publishers-with-new-ai-partnerships-that-would-cull-their-content/
- https://www.webpronews.com/google-pilots-gemini-ai-in-news-with-washington-post-guardian/
"""
import pathlib

import yaml

PROFILES_DIR = pathlib.Path(__file__).parent.parent / 'profiles'
ENTITIES_PATH = PROFILES_DIR / 'competitor-entities.yaml'

MECH_KEY = 'mechanism_569_washington_post_openai_google_dual_ai_payer_partnership'

EXPECTED_URLS = [
    'https://techcrunch.com/2025/04/22/chatgpts-responses-will-now-include-washington-post-articles',
    'https://www.thewrap.com/openai-washington-post-chatgpt-search-results-deal/',
    'http://www.neowin.net/news/the-washington-post-strikes-a-deal-with-openai-to-share-content-with-chatgpt/',
    'https://www.maginative.com/article/the-washington-post-joins-openais-expanding-roster-of-media-partners/',
    'https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/',
    'http://www.loeb.com/en/newsevents/news/2025/05/media-briefing-what-the-washington-posts-deal-with-openai-says-about-the-future',
    'https://nypost.com/2026/06/26/business/google-looks-to-bleed-publishers-with-new-ai-partnerships-that-would-cull-their-content/',
    'https://www.webpronews.com/google-pilots-gemini-ai-in-news-with-washington-post-guardian/',
]


def load_entities():
    with open(ENTITIES_PATH, encoding='utf-8') as f:
        return yaml.safe_load(f)


def get_entity():
    return load_entities()['entities']['openai']


def get_mech():
    return get_entity()[MECH_KEY]


def get_raw_block():
    raw = ENTITIES_PATH.read_text(encoding='utf-8')
    start = raw.index('    ' + MECH_KEY + ':')
    end = raw.index('  anthropic:', start)
    return raw[start:end]


class TestMechanismPresenceAndIdentity:
    def test_yaml_parses_and_openai_entity_present(self):
        entities = load_entities()['entities']
        assert 'openai' in entities

    def test_mechanism_569_present_under_openai(self):
        assert MECH_KEY in get_entity()

    def test_rotation_and_job_ids(self):
        mech = get_mech()
        assert mech['mechanism_id'] == 569
        assert mech['iteration'] == 569
        assert mech['rotation'] == 'Type C'
        assert mech['date_analyzed'] == '2026-09-06'
        assert mech['time_pdt'] == '17:00'
        assert mech['job_id'] == 'mediascope-daily-iteration'
        assert mech['goal_id'] == 'goal_54093bda4145'

    def test_mechanism_not_under_wrong_entity(self):
        entities = load_entities()['entities']
        for name in ('google', 'amazon', 'meta', 'anthropic', 'apple'):
            assert MECH_KEY not in entities[name]

    def test_type_financial_incentive_mapping(self):
        assert get_mech()['type'] == 'financial_incentive_mapping'

    def test_mechanism_name_names_both_legs(self):
        name = get_mech()['mechanism_name']
        assert 'OpenAI' in name
        assert 'Google' in name
        assert 'Washington Post' in name


class TestOpenAILegFacts:
    def test_announcement_date_apr_22_2025(self):
        assert get_mech()['openai_leg']['announcement_date'] == '2025-04-22'

    def test_display_partnership_form(self):
        form = get_mech()['openai_leg']['form']
        assert 'summaries' in form and 'quotes' in form and 'links' in form
        assert 'attribution' in form

    def test_terms_undisclosed(self):
        terms = get_mech()['openai_leg']['payment_terms']
        assert 'undisclosed' in terms.lower()
        assert 'declined to share' in terms

    def test_elkins_williams_quote_present(self):
        quote = get_mech()['openai_leg']['elkins_williams_quote']
        assert 'meeting our audiences where they are' in quote

    def test_shetty_500m_weekly_users(self):
        counterparty = get_mech()['openai_leg']['openai_counterparty']
        assert 'Varun Shetty' in counterparty
        assert '500 million' in counterparty

    def test_llm_agnostic_posture_and_own_tools(self):
        posture = get_mech()['openai_leg']['llm_agnostic_posture']
        assert 'LLM-agnostic' in posture
        assert 'Ask The Post AI' in posture
        assert 'Haystacker' in posture

    def test_openai_portfolio_context_20_plus(self):
        ctx = get_mech()['openai_leg']['openai_portfolio_context']
        assert '20+' in ctx and '160+' in ctx

    def test_sue_one_deal_another_bifurcation(self):
        note = get_mech()['openai_leg']['sue_one_deal_another']
        assert 'NYT' in note and 'suing' in note


class TestGoogleLegFacts:
    def test_announcement_date_dec_11_2025(self):
        assert get_mech()['google_leg']['announcement_date'] == '2025-12-11'

    def test_pilot_form_news_ai_overviews(self):
        form = get_mech()['google_leg']['form']
        assert 'pilot' in form.lower()
        assert 'overviews' in form

    def test_not_licensing_deals_nuance(self):
        terms = get_mech()['google_leg']['payment_terms']
        assert 'NOT licensing deals' in terms
        assert 'believed' in terms

    def test_nine_publishers_include_wapo_and_guardian(self):
        pubs = get_mech()['google_leg']['publishers_in_pilot']
        assert len(pubs) == 9
        assert 'The Washington Post' in pubs
        assert 'The Guardian' in pubs

    def test_ft_joined_feb_2026(self):
        assert 'February 2026' in get_mech()['google_leg']['ft_joined']

    def test_kint_leverage_quote(self):
        leverage = get_mech()['google_leg']['leverage_reporting']
        assert 'Jason Kint' in leverage
        assert "dominate here" in leverage
        assert 'Showcase' in leverage


class TestDualPayerSignificance:
    def test_payer_pair_openai_plus_google(self):
        pair = get_mech()['dual_payer_significance']['payer_pair']
        assert 'OpenAI' in pair and 'Google' in pair

    def test_second_after_ft_437(self):
        sig = get_mech()['dual_payer_significance']
        assert 'second' in sig['second_after_ft'].lower()
        assert '437' in sig['second_after_ft'] or 'Financial Times' in sig['second_after_ft']

    def test_bezos_ownership_no_amazon_transfer(self):
        note = get_mech()['dual_payer_significance']['bezos_ownership']
        assert 'Jeff Bezos' in note
        assert 'personally' in note
        assert '$0' in note

    def test_meta_zero_wapo_absent_from_bundle(self):
        note = get_mech()['dual_payer_significance']['meta_zero']
        assert '$0' in note
        assert 'Washington Examiner' in note

    def test_amazon_apple_anthropic_zero_legs(self):
        sig = get_mech()['dual_payer_significance']
        assert '$0' in sig['amazon_zero']
        assert '$0' in sig['apple_zero']
        assert '$0' in sig['anthropic_zero']

    def test_llm_agnostic_tension_noted(self):
        assert 'LLM-agnostic' in get_mech()['dual_payer_significance']['llm_agnostic_tension']


class TestDirectionalPredictions:
    def test_six_predictions_present(self):
        assert len(get_mech()['directional_predictions']) == 6

    def test_openai_softer_google_tempered(self):
        preds = get_mech()['directional_predictions']
        openai_pred = [p for p in preds if p.startswith('OpenAI:')][0]
        google_pred = [p for p in preds if p.startswith('Google:')][0]
        assert 'softer' in openai_pred
        assert 'softer-to-neutral' in google_pred
        assert 'not a licensing deal' in google_pred

    def test_meta_amazon_apple_neutral_no_deal(self):
        preds = get_mech()['directional_predictions']
        for entity in ('Meta:', 'Amazon:', 'Apple:'):
            pred = [p for p in preds if p.startswith(entity)][0]
            assert 'no-deal' in pred

    def test_anthropic_zero_deal_slot(self):
        preds = get_mech()['directional_predictions']
        anthropic_pred = [p for p in preds if p.startswith('Anthropic:')][0]
        assert 'zero-deal' in anthropic_pred

    def test_predictions_not_findings_flag(self):
        assert get_mech()['predictions_not_findings'] is True

    def test_structural_contrasts_cover_437_489_519_331(self):
        contrasts = ' '.join(get_mech()['structural_contrasts'])
        for ref in ('437', '489', '519', '331'):
            assert ref in contrasts


class TestConfoundersAndDiscipline:
    def test_six_ranked_confounders(self):
        confs = get_mech()['ranked_confounders']
        assert len(confs) == 6
        assert [c['rank'] for c in confs] == [1, 2, 3, 4, 5, 6]

    def test_confounder_strengths_labeled(self):
        strengths = [c['strength'] for c in get_mech()['ranked_confounders']]
        assert strengths.count('strong') == 3
        assert strengths.count('moderate') == 2
        assert strengths.count('weak') == 1

    def test_strongest_is_google_pilot_not_licensing(self):
        first = get_mech()['ranked_confounders'][0]['confounder']
        assert 'NOT licensing deals' in first

    def test_bezos_ownership_confounder_ranked_strong(self):
        third = get_mech()['ranked_confounders'][2]
        assert third['strength'] == 'strong'
        assert 'Bezos' in third['confounder']

    def test_statistical_discipline_qualitative_only(self):
        disc = get_mech()['statistical_discipline']
        assert disc['scope'] == 'qualitative structural mapping only'
        assert disc['correlation_not_causation'] is True
        assert disc['p_value'] == 'NOT_CALCULATED'
        assert disc['is_significant'] is False
        assert disc['tone_scores'] == 'NOT_SCORED'

    def test_caution_no_tone_claim(self):
        mech = get_mech()
        assert mech['cautious_language_required'] is True
        assert mech['no_coverage_tone_claim'] is True
        assert 'No causal claim' in mech['correlational_note']


class TestNoveltyAndSourceUrls:
    def test_novelty_first_dedicated_washington_post(self):
        focus = get_mech()['type_c_focus']
        assert 'First dedicated Washington Post' in focus

    def test_all_eight_source_urls_present_verbatim(self):
        sources = get_mech()['sources']
        assert len(sources) == 8
        for url in EXPECTED_URLS:
            assert url in sources

    def test_no_constructed_urls_in_block(self):
        raw = get_raw_block()
        for url in EXPECTED_URLS:
            assert url in raw

    def test_research_method_names_three_query_sets(self):
        method = get_mech()['research_method']
        assert '3 query sets' in method
        assert 'iteration-492' in method

    def test_verification_block(self):
        ver = get_mech()['verification']
        assert ver['iteration'] == 569
        assert ver['type'] == 'C'
        assert ver['date'] == '2026-09-06 17:00 PDT'
        assert ver['yaml_parse_clean'] is True


class TestYamlIntegrityAscii:
    def test_block_is_ascii_only(self):
        raw = get_raw_block()
        assert all(ord(c) < 128 for c in raw), 'non-ASCII character in block'

    def test_raw_block_boundaries(self):
        raw = get_raw_block()
        assert raw.startswith('    ' + MECH_KEY + ':')
        assert raw.count('mechanism_569') == 1

    def test_no_em_dashes_in_block(self):
        raw = get_raw_block()
        assert '\u2014' not in raw
        assert '\u2013' not in raw
