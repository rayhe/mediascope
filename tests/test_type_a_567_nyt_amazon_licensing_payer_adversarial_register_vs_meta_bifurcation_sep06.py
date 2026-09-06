"""Type A #567 (2026-09-06 15:00 PDT): The New York Times x Amazon licensing-payer
adversarial register vs Meta bifurcation - falsification control extending
#562 to the actual payer.

NYT (financial tie: licensing, Amazon pays the Times an estimated $20-25M
per year, direction receiving, coverage_prediction softer set in #559)
applies an ADVERSARIAL register to Amazon anyway: Karen Weise's Oct 2025
internal-documents investigation on Amazon robotics plans to avoid adding
more than 500,000 jobs by 2033 and automate 75 percent of operations
(-0.50, framed as aggressive corporate culture of labor displacement), and
the Jul 30 2026 NYT piece on Amazon and Google AI data-center spending
framing the capital outlay as investor jitters about whether it will pay
off (-0.30). The same paper covers Meta with a BIFURCATED register per
mechanism #69: positive on open-source AI philosophy (+0.40, serving the
anti-OpenAI litigation narrative), adversarial on AI execution (-0.65,
2026-06-23 voluntary-review holdout), neutral on business scoops (0.0,
2026-06-26 Arena prediction markets).

Scorer (MANUAL ILLUSTRATIVE, standing rule Aug 28 2026; arithmetic only):
Amazon target [-0.50, -0.30] avg -0.40 vs Meta peer
[+0.40, -0.65, 0.0] avg -0.0833. Engine target-minus-peer -0.3167,
delta_manual_illustrative -0.3167 (target harsher than peer by 0.32).
Engine p not significant, is_significant False: both layers agree not
significant (agreement pole, same class as #558 and #562). p_value
NOT_CALCULATED, cohens_d NOT_CALCULATED, ci_95 NOT_CALCULATED,
is_significant False. NOT artifact-grade: n=2 vs n=3, secondary
attributions, heavy confounders.

Honesty note (falsification, strongest available setting): the standing
coverage_prediction for NYT x Amazon was SOFTER (#559). Observed is
adversarial toward the actual payer, FALSIFYING that prediction. The
money-sympathy direction is INVERTED: the entity writing the check absorbs
the harder coverage. Strongest confounders: (1) item selection - two
adversarial items selected from search results, no exhaustive corpus scan,
disclosed not zero-claimed; (2) genre mismatch - labor-investigative plus
business-skeptical Amazon items vs mixed Meta comparators, and the hardest
Meta comparator (-0.65) already exceeds the hardest Amazon item (-0.50) at
item level; (3) genuine conduct - robotics job-displacement and $200B-plus
capex are genuinely adversarial facts; (4) secondary-source limitation -
neither NYT article read first-hand this run.

Novelty: first mechanism ever under competitor_relationships.amazon in
nytimes.yaml (key previously held only the financial stub). Distinct from
#562 (NYT x Google control, $0 tie) - this run extends the falsification
to the PAYING counterparty. Joins the falsification family (#552, #557,
#562, #193) and the publisher-posture instrumentality strand of #471.

Open empirical test (not asserted): the next major Amazon AI product
launch (Alexa+ expansion or next Rufus upgrade) vs the next major Meta AI
release at the NYT tests whether the adversarial register persists
(falsification strengthens) or softens (selection confounder dominates).

Evidence hygiene: all URLs carried verbatim from tool output this run or
from in-repo corpus pointers; the Jul 30 2026 NYT URL is cited with its
third-party GitHub attribution provenance disclosed; no zero-coverage
claims per iteration-492 rule. No em dashes in any new prose.
"""

import os
from datetime import datetime

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = os.path.join(REPO, 'profiles', 'nytimes.yaml')
LOG = os.path.join(REPO, 'iteration-log.md')

MECH_KEY = ('mechanism_567_nyt_amazon_licensing_payer_adversarial_'
            'register_vs_meta_bifurcation_sep06')


def _load_profile():
    with open(PROFILE) as f:
        return yaml.safe_load(f)


def _mechanism():
    profile = _load_profile()
    return profile['competitor_relationships']['amazon'][MECH_KEY]


class TestMechanismExistsAndShape:
    def test_mechanism_key_present_under_amazon(self):
        profile = _load_profile()
        assert MECH_KEY in profile['competitor_relationships']['amazon']

    def test_identity_fields(self):
        m = _mechanism()
        assert m['mechanism_id'] == 567
        assert m['iteration'] == 567
        assert m['iteration_type'] == 'A'
        assert m['date_analyzed'] == '2026-09-06'
        assert m['iteration_time'] == '2026-09-06 15:00 PDT'

    def test_publication_pair(self):
        m = _mechanism()
        assert m['publication'] == 'The New York Times'
        assert m['competitor_pair'] == 'Amazon vs Meta'

    def test_type_label(self):
        m = _mechanism()
        assert 'Type A' in m['type']

    def test_goal_and_job_ids(self):
        m = _mechanism()
        assert m['scheduled_job_id'] == 'mediascope-daily-iteration'
        assert m['goal_id'] == 'goal_54093bda4145'

    def test_financial_stub_still_present(self):
        profile = _load_profile()
        amazon = profile['competitor_relationships']['amazon']
        assert amazon['financial_tie'] == 'licensing'
        assert amazon['coverage_prediction'] == 'softer'


class TestAmazonSources:
    def test_two_amazon_sources(self):
        m = _mechanism()
        srcs = m['nyt_amazon_sources_sep06_2026']
        assert len(srcs) == 2

    def test_weise_robotics_investigation(self):
        m = _mechanism()
        srcs = m['nyt_amazon_sources_sep06_2026']
        rob = srcs[0]
        assert 'Weise' in rob['reporter']
        assert rob['date'] == '2025-10-22'
        assert rob['tone_manual_illustrative'] == -0.50
        assert '500,000 jobs' in rob['language'][0]
        assert 'iheart.com' in rob['notes']

    def test_ai_capex_jitters_item(self):
        m = _mechanism()
        srcs = m['nyt_amazon_sources_sep06_2026']
        capex = srcs[1]
        assert capex['date'] == '2026-07-30'
        assert capex['tone_manual_illustrative'] == -0.30
        assert 'jitters are growing' in capex['language']
        assert 'third-party GitHub' in capex['url_source']

    def test_post_deal_timing(self):
        m = _mechanism()
        srcs = m['nyt_amazon_sources_sep06_2026']
        for s in srcs:
            assert s['date'] >= '2025-05-29', s['date']


class TestMetaComparators:
    def test_three_meta_sources(self):
        m = _mechanism()
        srcs = m['nyt_meta_sources_sep06_2026']
        assert len(srcs) == 3

    def test_open_source_positive_strand(self):
        m = _mechanism()
        srcs = m['nyt_meta_sources_sep06_2026']
        assert srcs[0]['tone_manual_illustrative'] == 0.40
        assert 'litigation' in srcs[0]['notes']

    def test_voluntary_review_adversarial(self):
        m = _mechanism()
        srcs = m['nyt_meta_sources_sep06_2026']
        assert srcs[1]['date'] == '2026-06-23'
        assert srcs[1]['tone_manual_illustrative'] == -0.65
        assert 'nytimes.com' in srcs[1]['url']

    def test_arena_neutral_scoop(self):
        m = _mechanism()
        srcs = m['nyt_meta_sources_sep06_2026']
        assert srcs[2]['date'] == '2026-06-26'
        assert srcs[2]['tone_manual_illustrative'] == 0.0


class TestScorerManualIllustrative:
    def test_scores_and_delta_arithmetic(self):
        m = _mechanism()
        sc = m['asymmetry_scoring_manual_illustrative']
        peer = sc['peer_scores_manual_illustrative']
        target = sc['target_scores_manual_illustrative']
        assert abs(sum(peer) / len(peer)
                   - sc['peer_avg_manual_illustrative']) < 1e-3
        assert abs(sum(target) / len(target)
                   - sc['target_avg_manual_illustrative']) < 1e-3
        assert abs((sc['target_avg_manual_illustrative']
                    - sc['peer_avg_manual_illustrative'])
                   - sc['delta_manual_illustrative']) < 1e-3

    def test_delta_direction_target_harsher(self):
        m = _mechanism()
        sc = m['asymmetry_scoring_manual_illustrative']
        assert sc['delta_manual_illustrative'] == -0.3167
        assert 'target harsher than peer' in sc['delta_direction']

    def test_engine_arithmetic_matches_logged_delta(self):
        from mediascope.score.asymmetry import calculate_asymmetry
        m = _mechanism()
        sc = m['asymmetry_scoring_manual_illustrative']
        r = calculate_asymmetry(
            sc['target_scores_manual_illustrative'],
            sc['peer_scores_manual_illustrative'],
            'Amazon', ['Meta'], 'nytimes',
            datetime(2025, 10, 1), datetime(2026, 9, 6))
        assert abs(r.asymmetry_score - sc['delta_manual_illustrative']) < 1e-4
        assert abs(r.target_avg_tone
                   - sc['target_avg_manual_illustrative']) < 1e-4
        assert abs(r.peer_avg_tone
                   - sc['peer_avg_manual_illustrative']) < 1e-4
        assert r.is_significant is False

    def test_no_empirical_significance_claim(self):
        m = _mechanism()
        sc = m['asymmetry_scoring_manual_illustrative']
        assert sc['p_value'] == 'NOT CALCULATED no observed corpus'
        assert sc['cohens_d'] == 'NOT CALCULATED'
        assert sc['ci_95'] == 'NOT CALCULATED'
        assert sc['significant'] is False
        assert 'MANUAL ILLUSTRATIVE' in sc['note']


class TestHonestyFalsification:
    def test_paying_counterparty_stated(self):
        m = _mechanism()
        fin = m['financial_relationship']
        assert fin['amazon_direct'].startswith('Estimated $20-25M')
        assert 'INVERTED' in fin['non_causal_language']

    def test_softer_prediction_falsified(self):
        m = _mechanism()
        assert 'FALSIFIES' in m['finding_summary']
        assert 'coverage_prediction' in m['finding']

    def test_item_selection_is_strong_confounder(self):
        m = _mechanism()
        strong = ' '.join(m['confounders']['strong'])
        assert 'item selection' in strong
        assert 'genre mismatch' in strong
        assert 'genuine conduct' in strong
        assert len(m['confounders']['strong']) == 3

    def test_genre_mismatch_item_level_counterpoint(self):
        m = _mechanism()
        strong = ' '.join(m['confounders']['strong'])
        assert '-0.65' in strong and '-0.50' in strong

    def test_open_empirical_test_named(self):
        m = _mechanism()
        assert 'Amazon' in m['open_empirical_test']
        assert 'Rufus' in m['open_empirical_test'] or \
            'Alexa+' in m['open_empirical_test']


class TestReferences:
    def test_source_urls_all_https_and_nonempty(self):
        m = _mechanism()
        urls = m['source_urls']
        assert len(urls) >= 8
        for u in urls:
            assert u.startswith('https://'), u

    def test_no_em_dashes_in_prose_fields(self):
        m = _mechanism()
        prose = ' '.join([
            m['finding'],
            m['finding_summary'],
            m['register_analysis'],
            m['cautious_language']['disclaimer'],
        ])
        assert ' ' not in prose
        assert '–' not in prose

    def test_cross_references_include_key_mechanisms(self):
        m = _mechanism()
        assert 69 in m['cross_references']
        assert 471 in m['cross_references']
        assert 552 in m['cross_references']
        assert 557 in m['cross_references']
        assert 559 in m['cross_references']
        assert 562 in m['cross_references']

    def test_cautious_language_flags(self):
        m = _mechanism()
        cl = m['cautious_language']
        assert cl['correlation_not_causation'] is True
        assert cl['no_statistical_significance_claim'] is True
        assert cl['significant_false'] is True


class TestIterationLogAndNovelty:
    def test_iteration_log_entry_present(self):
        with open(LOG) as f:
            text = f.read()
        assert '#567 Type A' in text

    def test_no_duplicate_567_mechanism_keys(self):
        profile = _load_profile()
        count = sum(1 for k in
                    profile['competitor_relationships']['amazon']
                    if '567' in k)
        assert count == 1

    def test_rotation_guard_previous_is_566_type_e(self):
        import subprocess
        out = subprocess.run(
            ['git', 'log', '--oneline', '-1'], capture_output=True,
            text=True, cwd=REPO).stdout
        assert '566' in out and 'Type E' in out
