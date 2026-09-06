"""
Type C #549: News Corp x Meta AI Content Licensing Deal (Mar 2026) - Up To $50M
Per Year, At-Least-Three-Year Term, Meta Leg of the Quadruple-Revenue
Architecture
- Iteration #549 Type C Financial Incentive Mapping Sep 5 2026 21:00 PDT
- Rotation 548 B -> 549 C.
- Novelty verified: zero News Corp x Meta mechanism in
  profiles/competitor-entities.yaml before insertion (repo grep verified - only
  quadruple-frame bullets in mechanisms 519/524 and the news-corp.yaml
  revenue_relationships bullet); zero test_type_c_549 files on disk before
  this run (glob verified); no Type C commit with 549 in the title
  (git log --grep verified). Distinct from mechanism 519 (OpenAI leg) and
  mechanism 524 (Microsoft HarperCollins leg) - first first-class
  formalization of the Meta leg, placed under the meta entity.
- Findings (browser.search this run, verbatim full-URL listings; items via
  search-result excerpts, second-hand, marked bounded in-mechanism):
  - Deal: announced Mar 4 2026, broken by WSJ self-report (Alexandra Bruell)
    - a tracked publication reporting its own parent's AI licensing deal;
    Thomson teased at the Morgan Stanley TMT conference the Monday before
    ('one very public horizontal deal' near, others at an 'advanced stage').
  - Terms: up to $50M per year (people familiar with the matter; neither
    company publicly detailed financial specifics); at least three years;
    News Corp US + UK content (WSJ, NY Post, Barron's, MarketWatch, Times of
    London, The Sun - Dow Jones news division); retrieval for Meta AI
    products + training on story archives; HarperCollins excluded (news-only
    leg; the book leg sits with Microsoft per mechanism 524).
  - Headline annual parity: OpenAI leg (May 2024) more than $250M over five
    years approx $50M/yr vs Meta leg up to $50M/yr - near-identical headline
    annual values, different structures (five-year reported aggregate vs
    at-least-three-year 'up to' ceiling); Meta implied aggregate $150M
    smaller than OpenAI $250M+.
  - Woo-and-sue Meta application: Thomson doctrine quote; Perplexity sued by
    two News Corp subsidiaries (Oct 2024); Meta is the second 'wooed'
    flagship AI lab after OpenAI.
  - Facebook News irony: Meta shut down the Facebook News tab in 2024 and
    stopped paying publishers for news ~2 years earlier (Piercom); now pays
    up to $50M/yr for News Corp news content for AI - the pendulum reversed
    once the buyer became Meta AI instead of Facebook distribution.
  - Meta other deals: People Inc., USA Today, CNN, Fox News (terms
    undisclosed) per the WSJ report itself.
  - Directional predictions (predictions, not findings): Meta softer, OpenAI
    softer, Microsoft softer, Anthropic adversarial slot, Google neutral to
    no-deal, Perplexity adversarial.
  - Structural contrasts: 519 (OpenAI leg, parity pair), 524 (quadruple
    frame formalized), 539/544 (Meta-$0 mirrors at DDM/Vox - News Corp is
    the ONLY tracked-publication owner WITH a Meta leg),
    news-corp.yaml revenue_relationships (verified bullet).
  - No coverage-tone claim (no WSJ post-deal Meta tone analysis in corpus).
- Statistical discipline: qualitative structural mapping only; correlation
  not causation; is_significant false; p_value NOT_CALCULATED; tone scores
  NOT_SCORED.

Source URLs (all second-hand via search excerpts this run, Sep 5 2026):
- https://www.wsj.com/business/media/news-corp-meta-in-ai-content-licensing-deal-worth-up-to-50-million-a-year-d4fbf244
- https://www.editorandpublisher.com/stories/news-corp-meta-in-ai-content-licensing-deal-worth-up-to-50-million-a-year,260471
- https://www.engadget.com/ai/meta-signs-a-multimillion-dollar-ai-licensing-deal-with-news-corp-234157902.html
- https://www.mediaweek.com.au/meta-to-pay-news-corp-up-to-us50m-a-year-for-ai-content
- https://www.thewrap.com/media-platforms/journalism/news-corp-meta-ai-content-deal/
- https://www.piercom.com/insight/meta-deal-news-corp-trusted-journalism-drives-ai-systems/
- https://www.afaqs.com/news/digital/meta-signs-multi-year-ai-content-licensing-deal-with-news-corp-11177406
- https://dataconomy.com/2026/03/04/meta-signs-150-million-ai-content-deal-with-news-corp/
- https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/
"""
import pathlib

import yaml

PROFILES_DIR = pathlib.Path(__file__).parent.parent / 'profiles'
ENTITIES_PATH = PROFILES_DIR / 'competitor-entities.yaml'

MECH_KEY = 'mechanism_549_newscorp_meta_50m_yr_deal'

EXPECTED_URLS = [
    'https://www.wsj.com/business/media/news-corp-meta-in-ai-content-licensing-deal-worth-up-to-50-million-a-year-d4fbf244',
    'https://www.editorandpublisher.com/stories/news-corp-meta-in-ai-content-licensing-deal-worth-up-to-50-million-a-year,260471',
    'https://www.engadget.com/ai/meta-signs-a-multimillion-dollar-ai-licensing-deal-with-news-corp-234157902.html',
    'https://www.mediaweek.com.au/meta-to-pay-news-corp-up-to-us50m-a-year-for-ai-content',
    'https://www.thewrap.com/media-platforms/journalism/news-corp-meta-ai-content-deal/',
    'https://www.piercom.com/insight/meta-deal-news-corp-trusted-journalism-drives-ai-systems/',
    'https://www.afaqs.com/news/digital/meta-signs-multi-year-ai-content-licensing-deal-with-news-corp-11177406',
    'https://dataconomy.com/2026/03/04/meta-signs-150-million-ai-content-deal-with-news-corp/',
    'https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/',
]


def load_entities():
    with open(ENTITIES_PATH, encoding='utf-8') as f:
        return yaml.safe_load(f)


def get_mech():
    return load_entities()['entities']['meta'][MECH_KEY]


def get_raw_block():
    raw = ENTITIES_PATH.read_text(encoding='utf-8')
    start = raw.index('    ' + MECH_KEY + ':')
    end = raw.index('  xai:', start)
    return raw[start:end]


class TestMechanismPresenceAndIdentity:
    def test_yaml_parses_and_meta_entity_present(self):
        d = load_entities()
        assert 'entities' in d and 'meta' in d['entities']

    def test_mechanism_549_present_under_meta(self):
        m = get_mech()
        assert m['mechanism_id'] == 549
        assert m['iteration'] == 549

    def test_rotation_and_job_ids(self):
        m = get_mech()
        assert m['rotation'] == 'Type C'
        assert m['job_id'] == 'mediascope-daily-iteration'
        assert m['goal_id'] == 'goal_54093bda4145'
        assert m['date_analyzed'] == '2026-09-05'
        assert m['time_pdt'] == '21:00'
        assert m['announcement_date'] == '2026-03-04'

    def test_mechanism_not_under_wrong_entity(self):
        d = load_entities()
        for entity in ('openai', 'anthropic', 'google', 'amazon', 'apple', 'microsoft', 'samsung'):
            if entity in d['entities']:
                assert MECH_KEY not in d['entities'][entity]

    def test_type_financial_incentive_mapping(self):
        m = get_mech()
        assert m['type'] == 'financial_incentive_mapping'


class TestDealTerms:
    def test_value_up_to_50m_per_year(self):
        m = get_mech()
        assert 'up to $50 million per year' in m['deal_terms']['value']
        assert 'people familiar with the matter' in m['deal_terms']['value']

    def test_companies_declined_specifics(self):
        m = get_mech()
        assert 'neither company publicly detailed financial specifics' in m['deal_terms']['value']

    def test_term_at_least_three_years(self):
        m = get_mech()
        assert 'at least three years' in m['deal_terms']['term']

    def test_scope_us_uk_brands(self):
        m = get_mech()
        scope = m['deal_terms']['scope']
        for brand in ('Wall Street Journal', 'New York Post', "Barron's", 'MarketWatch',
                      'Times of London', 'The Sun'):
            assert brand in scope, brand
        assert 'U.S.' in scope and 'U.K.' in scope

    def test_use_cases_retrieval_and_training(self):
        m = get_mech()
        assert 'retrieve new information' in m['deal_terms']['use_cases']
        assert 'archives' in m['deal_terms']['use_cases']

    def test_book_division_excluded(self):
        m = get_mech()
        assert 'HarperCollins not covered' in m['deal_terms']['book_division_excluded']
        assert 'mechanism 524' in m['deal_terms']['book_division_excluded']


class TestHeadlineValueParity:
    def test_openai_leg_terms(self):
        m = get_mech()
        assert 'more than $250 million over five years' in m['headline_value_parity']['openai_leg']
        assert 'May 2024' in m['headline_value_parity']['openai_leg']

    def test_meta_leg_terms(self):
        m = get_mech()
        assert 'up to $50 million per year' in m['headline_value_parity']['meta_leg']
        assert 'Mar 2026' in m['headline_value_parity']['meta_leg']

    def test_parity_note_not_strictly_comparable(self):
        m = get_mech()
        note = m['headline_value_parity']['parity_note']
        assert '$50M/yr' in note
        assert 'not strictly comparable' in note

    def test_aggregate_difference(self):
        m = get_mech()
        assert '$150M' in m['headline_value_parity']['aggregate_difference']
        assert '$250M+' in m['headline_value_parity']['aggregate_difference']


class TestWooAndSueAndSelfReport:
    def test_broke_by_wsj_self_report(self):
        m = get_mech()
        assert 'Wall Street Journal self-report' in m['broke_by']
        assert 'Alexandra Bruell' in m['broke_by']

    def test_thomson_tease_morgan_stanley(self):
        m = get_mech()
        assert 'Morgan Stanley' in m['thomson_tease']
        assert 'advanced stage' in m['thomson_tease']

    def test_doctrine_quote(self):
        m = get_mech()
        q = m['woo_and_sue_meta_application']['doctrine_quote']
        assert 'woo and a sue strategy' in q
        assert 'discount for those who hand themselves in' in q
        assert 'penalty for those that resist' in q

    def test_sue_counterpoint_perplexity(self):
        m = get_mech()
        assert 'Perplexity' in m['woo_and_sue_meta_application']['sue_counterpoint']

    def test_meta_second_wooed_lab(self):
        m = get_mech()
        assert "second 'wooed' flagship AI lab after OpenAI" in m['woo_and_sue_meta_application']['meta_as_wooed']

    def test_facebook_news_irony(self):
        m = get_mech()
        assert 'Facebook News tab in 2024' in m['facebook_news_irony']
        assert 'up to $50M per year' in m['facebook_news_irony']

    def test_meta_other_deals_undisclosed(self):
        m = get_mech()
        assert 'People Inc.' in m['meta_other_deals']
        assert 'not disclosed' in m['meta_other_deals']


class TestDirectionalPredictions:
    def test_six_predictions_present(self):
        m = get_mech()
        preds = m['directional_predictions']
        assert isinstance(preds, list) and len(preds) == 6

    def test_prediction_entities_and_directions(self):
        m = get_mech()
        text = ' '.join(m['directional_predictions'])
        assert 'Meta: softer' in text
        assert 'OpenAI: softer' in text
        assert 'Microsoft: softer' in text
        assert 'Anthropic: adversarial' in text
        assert 'Google: neutral' in text
        assert 'Perplexity: adversarial' in text
        assert m['predictions_not_findings'] is True

    def test_structural_contrasts(self):
        m = get_mech()
        text = '\n'.join(m['structural_contrasts'])
        assert '519' in text
        assert '524' in text
        assert '539' in text and '544' in text
        assert 'ONLY tracked-publication owner WITH a Meta leg' in text
        assert 'news-corp.yaml' in text


class TestConfoundersAndDiscipline:
    def test_six_ranked_confounders(self):
        m = get_mech()
        ranks = [c['rank'] for c in m['ranked_confounders']]
        assert ranks == [1, 2, 3, 4, 5, 6]
        strengths = [c['strength'] for c in m['ranked_confounders']]
        assert strengths[0] == 'strong' and strengths[1] == 'strong'
        assert strengths[4] == 'weak' and strengths[5] == 'weak'
        assert 'up to $50M' in m['ranked_confounders'][0]['confounder']
        assert 'no WSJ post-deal Meta coverage-tone analysis' in m['ranked_confounders'][1]['confounder']

    def test_strongest_counterargument_null(self):
        m = get_mech()
        ca = m['strongest_counterargument'].lower()
        assert 'null' in ca
        assert 'no directional shift' in ca

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
    def test_novelty_distinguishes_519_and_524(self):
        m = get_mech()
        text = '\n'.join(m['novelty_verification'])
        assert 'mechanisms 519/524' in text
        assert 'HarperCollins' in text
        assert 'test_type_c_549' in text
        assert 'news-corp.yaml' in text

    def test_all_nine_source_urls_present_verbatim(self):
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
        assert raw.strip().startswith('mechanism_549_newscorp_meta_50m_yr_deal:')
        assert '\t' not in raw
