"""Type C #584: Disney x OpenAI $1B Sora deal arc (Dec 11 2025 - Mar 24 2026) -
largest entertainment licensing relationship OpenAI signed, equity-plus-licensing-plus-API-customer
structure, terminated with zero dollars transferred; first dedicated Disney mechanism in the corpus,
new to corpus.

- Iteration #584 Type C Financial Incentive Mapping Sep 7 2026 09:00 PDT
- Rotation 583 B -> 584 C.
- Novelty verified: zero disney mentions in profiles/competitor-entities.yaml before
  insertion (grep count 0); no Disney x OpenAI deal arc in iteration-log.md (grep
  verified); zero test_type_c_584 files on disk before this run (glob verified);
  no #584 in git log (grep verified). The the-verge.yaml annotations (Mar 31 2026
  $122B round piece noting "ending $1B Disney deal"; Apr 8 2026 "The vibes are off
  at OpenAI" noting "Sora discontinuation 30 mins after Disney collab") carry no
  Type C financial-incentive mechanism - coverage annotation only.
- Findings (browser.search this run, 2 query sets, verbatim full-URL
  listings; deal facts second-hand via search-result excerpts, bounded
  in-mechanism; no pages opened first-hand):
  - Announcement Dec 11 2025 (Reuters primary): $1B Disney equity investment in
    OpenAI plus warrants for additional equity; 3-year licensing agreement for
    200+ Disney/Marvel/Pixar/Star Wars characters on Sora and ChatGPT Images
    (excludes talent likenesses/voices); Disney becomes major OpenAI API customer
    (Disney+ products, ChatGPT for employees); curated fan videos streamable on
    Disney+; Iger/Altman talks began years earlier; Disney shares +2%.
  - Termination Mar 24 2026: OpenAI discontinued Sora outright (X announcement,
    no reason given); iOS app, API, Sora.com shut; WSJ reports full plug-pull
    including no video inside ChatGPT; Altman told staff to shut generative-video
    products; refocus on business/coding ahead of potential Q4 IPO.
  - Disney exit: deal dead; NO MONEY CHANGED HANDS (TheStreet); Disney execs
    learned 30 min after meeting OpenAI teams ("big rug-pull", Reuters source via
    TechSpot); Disney spokesperson respects OpenAI's decision; Josh D'Amaro took
    over as Disney CEO days earlier (TheWrap).
  - Sora metrics: 5M worldwide downloads Oct 2025 (+4,400% from 107K Sep, #1 App
    Store, Sensor Tower via Barron's); collapse to -32% MoM Dec 2025 and -45%
    Jan 2026, 1.2M cumulative US installs (Appfigures via Campaign).
- Statistical discipline: qualitative structural mapping only; correlation
  not causation; is_significant false; p_value NOT_CALCULATED; tone scores
  NOT_SCORED; no coverage-tone claim.

Source URLs (deal facts second-hand via search excerpts this run, Sep 7 2026):
- https://www.reuters.com/business/media-telecom/disney-makes-1-billion-investment-openai-brings-characters-sora-2025-12-11/
- https://www.marketplace.org/story/2025/12/23/why-disney-is-partnering-with-openais-sora
- https://www.barrons.com/articles/disney-openai-sora-deal-collapse-ai-strategy-6ed5f56c
- https://www.morningstar.com/news/marketwatch/20251211200/walt-disney-invests-1-billion-in-openai-and-licenses-characters-for-use-on-sora
- https://www.thestreet.com/technology/openai-is-shutting-down-sora-and-the-disney-deal-is-off
- https://www.techspot.com/news/111812-openai-pulls-plug-sora-ending-1-billion-disney.html
- https://www.campaignlive.com/article/openai-shuts-down-sora-billion-dollar-disney-deal-comes-end/1952808?utm_source=website&utm_medium=social
- https://petapixel.com/2026/03/24/openai-kills-sora-and-loses-disneys-1b-investment/
- https://www.thewrap.com/industry-news/business/sora-disney-openai-dead-why/
- https://gizmodo.com/disney-openai-sora-deal-dead-2000737676
"""
import pathlib

import yaml

REPO = pathlib.Path(__file__).parent.parent
PROFILES_DIR = REPO / 'profiles'
ENTITIES_PATH = PROFILES_DIR / 'competitor-entities.yaml'
LOG = REPO / 'iteration-log.md'

MECH_KEY = 'disney_openai_1b_sora_deal_arc_584'

EXPECTED_URLS = [
    'https://www.reuters.com/business/media-telecom/disney-makes-1-billion-investment-openai-brings-characters-sora-2025-12-11/',
    'https://www.marketplace.org/story/2025/12/23/why-disney-is-partnering-with-openais-sora',
    'https://www.barrons.com/articles/disney-openai-sora-deal-collapse-ai-strategy-6ed5f56c',
    'https://www.morningstar.com/news/marketwatch/20251211200/walt-disney-invests-1-billion-in-openai-and-licenses-characters-for-use-on-sora',
    'https://www.thestreet.com/technology/openai-is-shutting-down-sora-and-the-disney-deal-is-off',
    'https://www.techspot.com/news/111812-openai-pulls-plug-sora-ending-1-billion-disney.html',
    'https://www.campaignlive.com/article/openai-shuts-down-sora-billion-dollar-disney-deal-comes-end/1952808?utm_source=website&utm_medium=social',
    'https://petapixel.com/2026/03/24/openai-kills-sora-and-loses-disneys-1b-investment/',
    'https://www.thewrap.com/industry-news/business/sora-disney-openai-dead-why/',
    'https://gizmodo.com/disney-openai-sora-deal-dead-2000737676',
]


def load_doc():
    with open(ENTITIES_PATH, encoding='utf-8') as f:
        return yaml.safe_load(f)


def get_mech():
    return load_doc()[MECH_KEY]


def get_raw_block():
    raw = ENTITIES_PATH.read_text(encoding='utf-8')
    start = raw.index('\n' + MECH_KEY + ':')
    return raw[start:]


def _segment(text, n):
    head = '#%d ' % n
    start = text.index(head)
    nxt = '#%d ' % (n + 1)
    end = text.find('\n' + nxt, start)
    return text[start:end if end != -1 else len(text)]


class TestMechanismPresenceAndIdentity:
    def test_yaml_parses_and_top_level_key_present(self):
        doc = load_doc()
        assert MECH_KEY in doc

    def test_mechanism_id_and_iteration_584(self):
        mech = get_mech()
        assert mech['mechanism_id'] == 584
        assert mech['iteration'] == 584
        assert mech['iteration_type'] == 'C'

    def test_rotation_and_job_ids(self):
        mech = get_mech()
        assert mech['rotation'] == 'Type C'
        assert mech['date_analyzed'] == '2026-09-07'
        assert mech['time_pdt'] == '09:00'
        assert mech['job_id'] == 'mediascope-daily-iteration'
        assert mech['goal_id'] == 'goal_54093bda4145'

    def test_type_financial_incentive_mapping(self):
        assert get_mech()['type'] == 'financial_incentive_mapping'

    def test_mechanism_name_names_disney_openai_sora(self):
        name = get_mech()['mechanism_name']
        assert 'Disney' in name
        assert 'OpenAI' in name
        assert 'Sora' in name
        assert 'first dedicated mechanism' in name


class TestAnnouncementFacts:
    def test_announcement_date_dec_11_2025(self):
        assert get_mech()['announcement']['date'] == '2025-12-11'

    def test_primary_report_reuters(self):
        assert get_mech()['announcement']['primary_report'] == 'Reuters'

    def test_equity_leg_1b_plus_warrants(self):
        leg = get_mech()['equity_leg']
        assert '$1B equity investment' in leg['investment']
        assert 'warrants' in leg['warrants']

    def test_licensing_leg_three_year_200_characters(self):
        leg = get_mech()['licensing_leg']
        assert '3-year' in leg['term']
        assert '200+' in leg['characters']
        assert 'Marvel' in leg['characters']
        assert 'Pixar' in leg['characters']

    def test_licensing_excludes_talent_likenesses(self):
        leg = get_mech()['licensing_leg']
        assert 'no talent likenesses or voices' in leg['exclusions']

    def test_customer_leg_api_and_employees(self):
        leg = get_mech()['customer_leg']
        assert 'major customer of OpenAI' in leg['api_customer']
        assert 'ChatGPT for Disney employees' in leg['employee_deployment']

    def test_iger_altman_talks_began_years_earlier(self):
        assert 'years earlier' in get_mech()['announcement']['talks_origin']


class TestTerminationFacts:
    def test_termination_date_mar_24_2026(self):
        assert get_mech()['termination']['date'] == '2026-03-24'

    def test_sora_discontinued_via_x(self):
        term = get_mech()['termination']
        assert 'saying goodbye to Sora' in term['announcement_channel']

    def test_full_plug_pull_scope(self):
        term = get_mech()['termination']
        assert 'Sora.com' in term['scope']
        assert 'no video functionality inside ChatGPT' in term['scope']

    def test_no_money_changed_hands(self):
        dx = get_mech()['disney_exit']
        assert 'zero' in dx['money_transferred']
        assert 'no money changed hands' in dx['money_transferred']

    def test_rug_pull_30_minutes(self):
        dx = get_mech()['disney_exit']
        assert '30 minutes' in dx['rug_pull']
        assert 'big rug-pull' in dx['rug_pull']

    def test_disney_spokesperson_quote(self):
        dx = get_mech()['disney_exit']
        assert 'respect OpenAI' in dx['disney_statement']
        assert 'exit the video generation business' in dx['disney_statement']

    def test_sora_download_collapse_stats(self):
        met = get_mech()['sora_metrics']
        assert '5M worldwide downloads' in met['peak']
        assert '4,400%' in met['peak']
        assert '32%' in met['collapse']
        assert '45%' in met['collapse']
        assert '1.2M cumulative' in met['collapse']


class TestFinancialStructure:
    def test_four_legs_present(self):
        mech = get_mech()
        for leg in ('equity_leg', 'licensing_leg', 'customer_leg'):
            assert leg in mech
        assert 'warrants' in mech['equity_leg']

    def test_largest_entertainment_licensing_claim(self):
        sig = get_mech()['mediascope_significance']
        assert 'largest single entertainment licensing relationship' in sig['largest_entertainment_licensing']

    def test_equity_leg_distinctive_in_corpus(self):
        sig = get_mech()['mediascope_significance']
        assert 'AI-lab equity leg' in sig['equity_distinctiveness']

    def test_abc_news_ownership_noted(self):
        sig = get_mech()['mediascope_significance']
        assert 'ABC News' in sig['abc_news_ownership']

    def test_natural_experiment_framing(self):
        sig = get_mech()['mediascope_significance']
        assert 'natural_experiment' in sig
        assert '$0 transferred' in sig['natural_experiment']
        assert 'announced-but-unfunded' in sig['natural_experiment']

    def test_meta_zero_disney_relationship(self):
        sig = get_mech()['mediascope_significance']
        assert '$0 Disney financial relationship' in sig['meta_contrast']


class TestCorpusContrasts:
    def test_contrasts_name_504_549_519_391(self):
        contrasts = ' '.join(get_mech()['structural_contrasts'])
        for ref in ('504', '549', '519', '391'):
            assert ref in contrasts

    def test_549_funded_vs_unfunded_boundary(self):
        contrasts = ' '.join(get_mech()['structural_contrasts'])
        assert 'never funded' in contrasts
        assert 'unfunded-announcement boundary case' in contrasts

    def test_391_inverse_headline_vs_realized(self):
        contrasts = ' '.join(get_mech()['structural_contrasts'])
        assert 'headline $1B, realized $0' in contrasts

    def test_three_directional_predictions(self):
        preds = get_mech()['directional_predictions']
        assert len(preds) == 3
        joined = ' '.join(preds)
        assert 'OpenAI:' in joined
        assert 'ABC News' in joined
        assert 'Meta:' in joined

    def test_predictions_not_findings_flag(self):
        assert get_mech()['predictions_not_findings'] is True

    def test_tracked_surface_no_tone_claim(self):
        sig = get_mech()['mediascope_significance']
        assert 'The Verge' in sig['tracked_surface']
        assert 'no tone claim' in sig['tracked_surface']


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

    def test_strongest_is_no_money_transferred(self):
        first = get_mech()['ranked_confounders'][0]['confounder']
        assert 'no money changed hands' in first
        assert 'prospective, never realized' in first

    def test_entertainment_ip_leverage_class_confounder(self):
        entry = get_mech()['ranked_confounders'][2]
        assert entry['strength'] == 'strong'
        assert 'entertainment IP, not news content' in entry['confounder']

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


class TestNoveltyAndSources:
    def test_novelty_first_dedicated_disney(self):
        assert 'first dedicated Disney mechanism' in get_mech()['novelty']

    def test_novelty_distinguishes_corpus_neighbors(self):
        novelty = get_mech()['novelty']
        for ref in ('504', '549', '519', '391'):
            assert ref in novelty

    def test_all_ten_source_urls_present_verbatim(self):
        sources = get_mech()['sources']
        assert len(sources) == 10
        for url in EXPECTED_URLS:
            assert url in sources

    def test_no_constructed_urls_in_block(self):
        raw = get_raw_block()
        for url in EXPECTED_URLS:
            assert url in raw

    def test_research_method_names_two_query_sets(self):
        method = get_mech()['research_method']
        assert '2 browser.search query sets' in method
        assert 'iteration-492' in method

    def test_verification_block(self):
        ver = get_mech()['verification']
        assert ver['iteration'] == 584
        assert ver['type'] == 'C'
        assert ver['date'] == '2026-09-07 09:00 PDT'
        assert ver['yaml_parse_clean'] is True

    def test_block_is_ascii_only(self):
        raw = get_raw_block()
        assert all(ord(c) < 128 for c in raw), 'non-ASCII character in block'

    def test_no_em_dashes_in_block(self):
        raw = get_raw_block()
        assert '—' not in raw
        assert '–' not in raw

    def test_iteration_log_584_heading_present(self):
        with open(LOG, encoding='utf-8') as f:
            text = f.read()
        seg = _segment(text, 584)
        assert 'Disney' in seg
        assert '583 B -> 584 C' in seg
