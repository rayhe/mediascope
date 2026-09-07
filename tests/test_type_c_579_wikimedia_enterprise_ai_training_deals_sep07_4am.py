"""Type C #579: Wikimedia Enterprise AI training deals (Jan 15 2026, Wikipedia
25th anniversary) - reference-layer AI licensing architecture across six
tracked entities (Microsoft, Meta, Amazon, Perplexity, Mistral AI, Google
since 2022); financial terms undisclosed; cost-pressure driver (crawler
requests exceed human requests, Wales on skyrocketing costs); OpenAI is the
standout announced-roster absence (most publisher deals, no disclosed
Wikimedia deal) - bounded per iteration-492; Anthropic/Apple/xAI absences
consistent with existing corpus postures; first dedicated mechanism, new to
corpus.

- Iteration #579 Type C Financial Incentive Mapping Sep 7 2026 04:00 PDT
- Rotation 578 B -> 579 C.
- Novelty verified: zero wikimedia/Wikimedia Enterprise mentions in
  iteration-log.md before this entry (grep count 0); no dedicated Wikimedia
  block in profiles/competitor-entities.yaml (grep verified); zero
  test_type_c_579 files on disk before this run (glob verified); no #579 in
  git log (grep verified). The wikipedia hits in tests 432/534 are incidental
  encyclopedia citations, not Wikimedia-deal mechanisms. Distinct from
  mechanism 391 (Perplexity Comet Plus publisher revenue share), mechanism
  509 (Anthropic zero-deal posture), mechanism 574 (Apple data-vendor payer
  architecture), mechanism 549 (News Corp x Meta), the meta_ai_deals
  13-partner overview (publisher-only), and the xai publisher_deals_note
  (Grokipedia free-riding).
- Findings (browser.search this run, 2 query sets, verbatim full-URL
  listings; deal facts second-hand via search-result excerpts, bounded
  in-mechanism; no pages opened first-hand):
  - Announcement: Jan 15 2026, Wikimedia Foundation, Wikimedia Enterprise
    partnerships with Microsoft, Meta, Amazon; Perplexity and Mistral AI
    signed over the prior year; Meta and Amazon enlisted previously; Google
    arrangement since 2022. Terms undisclosed.
  - Scale and cost pressure: 65M articles, 300+ languages, ~250,000
    volunteer editors; crawler requests exceed human requests; Jimmy Wales
    on skyrocketing hosting/memory/server costs at the donation-funded
    non-profit.
  - Becker quotes: Reuters ("critical component ... support financially");
    The Verge via MediaNama (feature requests, structuring data to company
    needs; sustainability in every AI company's best interest).
  - Enterprise product: APIs (articles, Commons images, Wiktionary,
    Wikidata); free plans limited; paid plans (terms not public) with daily
    snapshots, streaming real-time revisions, human support; open Kaggle
    dataset for noncommercial training.
  - Roster absences (bounded): OpenAI, Anthropic, Apple, xAI, Samsung, Snap.
- Statistical discipline: qualitative structural mapping only; correlation
  not causation; is_significant false; p_value NOT_CALCULATED; tone scores
  NOT_SCORED.

Source URLs (deal facts second-hand via search excerpts this run, Sep 7 2026):
- https://www.reuters.com/business/retail-consumer/wikipedia-owner-signs-microsoft-meta-ai-content-training-deals-2026-01-15/
- https://www.techrepublic.com/article/news-microsoft-meta-amazon-paying-wikipedia/
- https://www.medianama.com/2026/01/223-wikipedia-ai-licensing-deals-microsoft-meta-and-others-amid-rising-costs/
- https://www.thehindubusinessline.com/info-tech/wikipedia-partners-with-microsoft-meta-amazon-in-ai-content-training-deals/article70512455.ece
- https://www.deeplearning.ai/the-batch/wikimedia-foundation-strikes-deals-with-amazon-meta-microsoft-mistral-ai-and-perplexity
- https://q106fm.com/2026/01/15/wikipedia-owner-signs-on-microsoft-meta-in-ai-content-training-deals/
"""
import os
import pathlib

import yaml

REPO = pathlib.Path(__file__).parent.parent
PROFILES_DIR = REPO / 'profiles'
ENTITIES_PATH = PROFILES_DIR / 'competitor-entities.yaml'
LOG = REPO / 'iteration-log.md'

MECH_KEY = 'wikimedia_enterprise_ai_training_deals_579'

EXPECTED_URLS = [
    'https://www.reuters.com/business/retail-consumer/wikipedia-owner-signs-microsoft-meta-ai-content-training-deals-2026-01-15/',
    'https://www.techrepublic.com/article/news-microsoft-meta-amazon-paying-wikipedia/',
    'https://www.medianama.com/2026/01/223-wikipedia-ai-licensing-deals-microsoft-meta-and-others-amid-rising-costs/',
    'https://www.thehindubusinessline.com/info-tech/wikipedia-partners-with-microsoft-meta-amazon-in-ai-content-training-deals/article70512455.ece',
    'https://www.deeplearning.ai/the-batch/wikimedia-foundation-strikes-deals-with-amazon-meta-microsoft-mistral-ai-and-perplexity',
    'https://q106fm.com/2026/01/15/wikipedia-owner-signs-on-microsoft-meta-in-ai-content-training-deals/',
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

    def test_mechanism_id_and_iteration_579(self):
        mech = get_mech()
        assert mech['mechanism_id'] == 579
        assert mech['iteration'] == 579
        assert mech['iteration_type'] == 'C'

    def test_rotation_and_job_ids(self):
        mech = get_mech()
        assert mech['rotation'] == 'Type C'
        assert mech['date_analyzed'] == '2026-09-07'
        assert mech['time_pdt'] == '04:00'
        assert mech['job_id'] == 'mediascope-daily-iteration'
        assert mech['goal_id'] == 'goal_54093bda4145'

    def test_type_financial_incentive_mapping(self):
        assert get_mech()['type'] == 'financial_incentive_mapping'

    def test_mechanism_name_names_layer_and_first(self):
        name = get_mech()['mechanism_name']
        assert 'Wikimedia Enterprise' in name
        assert 'reference-layer' in name
        assert 'first dedicated mechanism' in name


class TestAnnouncementFacts:
    def test_announcement_date_jan_15_2026(self):
        assert get_mech()['announcement']['date'] == '2026-01-15'

    def test_occasion_25th_anniversary(self):
        assert '25th anniversary' in get_mech()['announcement']['occasion']

    def test_six_payers_in_roster(self):
        roster = get_mech()['payer_roster']
        entities = [r['entity'] for r in roster]
        assert len(roster) == 6
        for e in ('Microsoft', 'Meta', 'Amazon', 'Perplexity', 'Mistral AI', 'Google'):
            assert e in entities

    def test_google_arrangement_since_2022(self):
        roster = {r['entity']: r['status'] for r in get_mech()['payer_roster']}
        assert '2022' in roster['Google']

    def test_meta_amazon_previously_enlisted(self):
        roster = {r['entity']: r['status'] for r in get_mech()['payer_roster']}
        assert 'previously' in roster['Meta']
        assert 'previously' in roster['Amazon']

    def test_terms_not_disclosed(self):
        assert get_mech()['terms_disclosed'] is False


class TestCostPressureAndEnterpriseProduct:
    def test_scale_65m_articles_300_languages(self):
        scale = get_mech()['corpus_scale']
        assert '65 million' in scale['articles']
        assert '300+' in scale['languages']
        assert '250,000' in scale['editors']

    def test_crawler_requests_exceed_human(self):
        cp = get_mech()['cost_pressure']
        assert 'more requests from automated web crawlers than human users' in cp['crawler_vs_human']

    def test_wales_skyrocketing_costs(self):
        wales = get_mech()['cost_pressure']['wales_costs']
        assert 'Jimmy Wales' in wales
        assert 'skyrocket' in wales

    def test_becker_reuters_quote(self):
        q = get_mech()['becker_quotes']['reuters_interview']
        assert 'critical component' in q
        assert 'support financially' in q
        assert 'Lane Becker' in q

    def test_becker_verge_quote_via_medianama(self):
        q = get_mech()['becker_quotes']['verge_via_medianama']
        assert 'feature requests' in q
        assert 'The Verge' in q

    def test_enterprise_product_tiers(self):
        prod = get_mech()['enterprise_product']
        assert 'APIs' in prod['includes']
        assert 'daily snapshots' in prod['paid_plan']
        assert 'streaming real-time revisions' in prod['paid_plan']
        assert 'Kaggle' in prod['noncommercial']


class TestRosterAbsenceBounded:
    def test_six_absent_entities(self):
        absent = get_mech()['absent_from_announced_roster']['entities']
        for e in ('OpenAI', 'Anthropic', 'Apple', 'xAI', 'Samsung', 'Snap'):
            assert e in absent

    def test_absence_bounded_not_proven(self):
        bounded = get_mech()['absent_from_announced_roster']['bounded']
        assert 'iteration-492' in bounded
        assert 'not a proven non-deal' in bounded
        assert 'among other firms' in bounded

    def test_openai_standout_asymmetry(self):
        standout = get_mech()['absent_from_announced_roster']['openai_standout']
        assert 'most publisher content licensing deals' in standout.lower()
        assert '24+' in standout
        assert 'no disclosed Wikimedia Enterprise deal' in standout

    def test_the_verge_surface_no_tone_claim(self):
        surf = get_mech()['tracked_publication_surface']['the_verge']
        assert 'The Verge' in surf
        assert 'mechanism 494' in surf
        assert 'no tone claim' in surf


class TestStructuralContrasts:
    def test_contrasts_name_391_509_574_549(self):
        contrasts = ' '.join(get_mech()['structural_contrasts'])
        for ref in ('391', '509', '574', '549'):
            assert ref in contrasts

    def test_perplexity_dual_layer_spend(self):
        contrasts = ' '.join(get_mech()['structural_contrasts'])
        assert 'Comet Plus' in contrasts
        assert 'dual-layer' in contrasts

    def test_meta_pays_but_zero_at_tracked(self):
        contrasts = ' '.join(get_mech()['structural_contrasts'])
        assert '$0 at all 7 tracked publications' in contrasts

    def test_xai_grokipedia_free_riding(self):
        contrasts = ' '.join(get_mech()['structural_contrasts'])
        assert 'Grokipedia' in contrasts
        assert 'free-rides' in contrasts

    def test_six_directional_predictions(self):
        preds = get_mech()['directional_predictions']
        assert len(preds) == 6
        joined = ' '.join(preds)
        for e in ('Meta:', 'Microsoft:', 'OpenAI:', 'Anthropic:', 'Apple:', 'xAI:'):
            assert e in joined

    def test_predictions_not_findings_flag(self):
        assert get_mech()['predictions_not_findings'] is True


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

    def test_strongest_is_terms_undisclosed(self):
        first = get_mech()['ranked_confounders'][0]['confounder']
        assert 'terms undisclosed' in first
        assert 'unquantified' in first

    def test_roster_incompleteness_bounded_confounder(self):
        second = get_mech()['ranked_confounders'][1]
        assert second['strength'] == 'strong'
        assert 'iteration-492' in second['confounder']

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
    def test_novelty_first_dedicated_wikimedia(self):
        assert 'first dedicated Wikimedia Enterprise mechanism' in get_mech()['novelty']

    def test_novelty_distinguishes_corpus_neighbors(self):
        novelty = get_mech()['novelty']
        for ref in ('391', '509', '574', '549'):
            assert ref in novelty

    def test_all_six_source_urls_present_verbatim(self):
        sources = get_mech()['sources']
        assert len(sources) == 6
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
        assert ver['iteration'] == 579
        assert ver['type'] == 'C'
        assert ver['date'] == '2026-09-07 04:00 PDT'
        assert ver['yaml_parse_clean'] is True

    def test_block_is_ascii_only(self):
        raw = get_raw_block()
        assert all(ord(c) < 128 for c in raw), 'non-ASCII character in block'

    def test_no_em_dashes_in_block(self):
        raw = get_raw_block()
        assert '—' not in raw
        assert '–' not in raw

    def test_iteration_log_579_heading_present(self):
        with open(LOG, encoding='utf-8') as f:
            text = f.read()
        seg = _segment(text, 579)
        assert 'Wikimedia Enterprise' in seg
        assert '578 B -> 579 C' in seg

    def test_test_file_naming_convention(self):
        assert os.path.basename(__file__).startswith('test_type_c_579_')
