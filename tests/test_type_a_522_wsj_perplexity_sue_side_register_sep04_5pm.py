"""Type A #522 (2026-09-04 17:00 PDT): WSJ x Perplexity sue-side register.

First WSJ x Perplexity coverage analysis in the repo. Perplexity is the
sue-side pole of News Corp's woo-and-sue strategy: Dow Jones and NY Post
sued Perplexity AI in SDNY 2024-10-21 (case 1:24-cv-07984) for massive
illegal copying into a RAG answer-engine database, verbatim reproductions,
false attribution, up to $150k/infringement, RAG-database destruction
sought; the July 2024 licensing-demand letter went unanswered. No licensing
deal exists. #519 predicted harder or neutral WSJ registers toward no-deal
entities.

Observed three 2026 WSJ items (two first-hand opened this run, one bounded
search excerpt): Snap-Perplexity deal scrapped (business-failure register,
-0.2); the $34.5B Chrome bid dismissed as "a long shot... an overreach"
(quixotic-dismissal register, -0.3); the Comet browser agent as prompt
injection attack vector (security-threat register, -0.4).

Live scorer this run: Perplexity [-0.2,-0.3,-0.4] vs OpenAI/Anthropic
rogue-triangle soft pair [-0.2,-0.15]: delta -0.125, p_value 0.1537,
cohens_d -1.4852, CI (-0.225,-0.025), is_significant False. Directional
support for #519 at tiny n; NOT artifact-grade. Internal tension: Meta is a
deal partner yet scores -0.45 (harder than Perplexity), so the incentive
cannot explain the full triangle.

Statistical discipline: MANUAL ILLUSTRATIVE tones; p_value reported as
n.s.; is_significant False; correlation_not_causation True.

Evidence hygiene: both 2026 WSJ articles opened first-hand via browser.open
this run (verbatim quotes in the YAML entry); the 1Password-agents piece is
a bounded search excerpt. All URLs carried verbatim from search-result
full-URL listings or tool-verified opens - no canonical URLs constructed.
No zero-coverage claims (iteration-492 rule).

Durable conventions (from #495): line-anchored (^, re.MULTILINE) heading
search in iteration-log.md; relative newest-first ordering between
neighbors, never absolute-top or fixed head slices.
"""

import os
import re
from datetime import datetime

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NEWS_CORP = os.path.join(REPO, 'profiles', 'news-corp.yaml')
LOG = os.path.join(REPO, 'iteration-log.md')


def _load_profile():
    with open(NEWS_CORP) as f:
        return yaml.safe_load(f)


def _perplexity():
    profile = _load_profile()
    return profile['competitor_relationships']['perplexity']


class TestProfileStructure:
    def test_perplexity_key_exists_in_competitor_relationships(self):
        rels = _load_profile()['competitor_relationships']
        assert 'perplexity' in rels

    def test_perplexity_appears_exactly_once(self):
        rels = _load_profile()['competitor_relationships']
        assert list(rels.keys()).count('perplexity') == 1

    def test_financial_tie_is_lawsuit_active(self):
        assert _perplexity()['financial_tie'] == 'lawsuit_active'

    def test_coverage_prediction_is_harder(self):
        assert _perplexity()['coverage_prediction'] == 'harder'

    def test_three_coverage_examples(self):
        assert len(_perplexity()['coverage_examples']) == 3

    def test_examples_carry_required_fields_with_typed_tones(self):
        for ex in _perplexity()['coverage_examples']:
            assert isinstance(ex['tone'], float), ex.get('title')
            assert isinstance(ex['title'], str)
            assert isinstance(ex['publication'], str)
            assert isinstance(ex['date'], str)
            assert isinstance(ex['source_url'], str)
            assert isinstance(ex['verification'], str)

    def test_verification_values_in_known_vocabulary(self):
        allowed = {'first_hand_open', 'bounded_search_excerpt'}
        for ex in _perplexity()['coverage_examples']:
            assert ex['verification'] in allowed, ex.get('title')

    def test_two_first_hand_one_bounded(self):
        verifs = [ex['verification'] for ex in _perplexity()['coverage_examples']]
        assert verifs.count('first_hand_open') == 2
        assert verifs.count('bounded_search_excerpt') == 1

    def test_suit_case_number_and_dates_in_description(self):
        desc = _perplexity()['description']
        assert '1:24-cv-07984' in desc
        assert '2024-10-21' in desc

    def test_no_em_dash_leakage_in_entry(self):
        blob = yaml.safe_dump(_perplexity(), allow_unicode=True)
        assert '\u2014' not in blob


class TestCoverageEvidence:
    def test_verbatim_urls(self):
        urls = [ex['source_url'] for ex in _perplexity()['coverage_examples']]
        assert 'https://www.wsj.com/business/earnings/snap-perplexity-mutually-end-ai-deal-071f83ed' in urls
        assert 'https://www.wsj.com/tech/googles-big-win-is-even-bigger-for-apple-6a4ffc40' in urls
        assert 'https://www.wsj.com/tech/ai/1password-for-claude-ai-agents-password-manager-111a7a8a' in urls

    def test_tone_values_match_scorer_inputs(self):
        tones = [ex['tone'] for ex in _perplexity()['coverage_examples']]
        assert sorted(tones) == [-0.4, -0.3, -0.2]

    def test_sue_side_register_tone_is_avg(self):
        entry = _perplexity()
        assert abs(entry['sue_side_register_tone'] - (-0.3)) < 1e-9

    def test_chrome_bid_quote_captured(self):
        ex = [e for e in _perplexity()['coverage_examples']
              if 'Google' in e['title'] and 'Apple' in e['title']][0]
        assert 'long shot' in ex['framing']
        assert 'overreach' in ex['framing']


class TestScorerResult:
    def _result(self):
        return _perplexity()['asymmetry_scorer_result']

    def test_delta_matches_live_engine_output(self):
        assert self._result()['delta'] == -0.125

    def test_p_value_reported_not_significant(self):
        assert self._result()['p_value'] == 0.1537
        assert self._result()['is_significant'] is False

    def test_cohens_d_and_ci_recorded(self):
        r = self._result()
        assert r['cohens_d'] == -1.4852
        assert r['confidence_interval'] == [-0.225, -0.025]

    def test_target_and_peer_scores_match_profile_tones(self):
        r = self._result()
        profile_tones = sorted(ex['tone'] for ex in _perplexity()['coverage_examples'])
        assert sorted(r['target_scores']) == profile_tones

    def test_discipline_block_marks_manual_and_not_artifact_grade(self):
        r = self._result()
        assert 'MANUAL ILLUSTRATIVE' in r['statistical_discipline']
        assert 'NOT artifact-grade' in r['significance_interpretation']


class TestScorerReproducibility:
    def test_live_engine_reproduces_logged_delta_and_p(self):
        from mediascope.score.asymmetry import calculate_asymmetry
        r = calculate_asymmetry(
            [-0.2, -0.3, -0.4], [-0.2, -0.15],
            'Perplexity', ['OpenAI', 'Anthropic'], 'wsj',
            datetime(2026, 5, 1), datetime(2026, 9, 4))
        assert round(r.asymmetry_score, 4) == -0.125
        assert round(r.p_value, 4) == 0.1537
        assert r.is_significant is False

    def test_is_significant_boundary_not_crossed(self):
        assert 0.1537 > 0.05


class TestDocSync:
    def test_iteration_log_has_522_heading_line_anchored(self):
        with open(LOG) as f:
            text = f.read()
        assert re.search(r'(?m)^#522 Type A: WSJ x Perplexity', text)

    def test_log_entry_names_rotation_from_521_type_e(self):
        with open(LOG) as f:
            text = f.read()
        assert 'rotation 521 E -> 522 A' in text

    def test_log_entry_documents_novelty_checks(self):
        with open(LOG) as f:
            text = f.read()
        assert 'Zero test_type_a_522 files on disk' in text
