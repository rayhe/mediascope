"""Type A #537 (2026-09-05 09:00 PDT): Guardian x Meta vs OpenAI same-day
register asymmetry - Aug 18 2026 natural experiment.

First Type A same-day, same-publication, severity-inverted natural experiment
in the corpus. On Aug 18 2026 The Guardian published (both attributed to the
Guardian US tech-reporting beat per buzzsumo journalist profile, crawl ~Sep 4
2026): "Reel-ing it in: Meta is paying influencers to promote teen accounts"
(adversarial accountability register) and "OpenAI announces slowing pace of
development after hack by rogue agent" (corporate-announcement stewardship
register). The OpenAI window's severity strictly dominates: rogue agent
hacking Hugging Face, a 1,000-employee slowdown petition, a Bernie Sanders
pause letter to Altman. The Meta Aug 18 item is teen-account influencer
marketing. Second pieces in the window: Bhuiyan Jul 29 Meta earnings
"diminishment" register vs Milmo Jul OpenAI rogue-agent self-disclosure
news register (carried from mechanism_517, adversarial capacity exists).

Scorer (MANUAL ILLUSTRATIVE): Meta [-0.45, -0.40] avg -0.425; OpenAI
[-0.15, -0.10] avg -0.125; delta -0.30 (Meta harder). p_value NOT_CALCULATED
(standing rule Aug 28), is_significant False. n=2 per side. The Guardian
prints the facts on both, so this is REGISTER asymmetry, not suppression;
mirror-verified no disclosure of the Feb 2025 Guardian-OpenAI licensing
deal in the OpenAI piece. Correlation not causation. NOT artifact-grade.

Strongest counterargument: the register difference may be entirely
news-genre driven (announcement peg vs accountability peg), and
mechanism_517 proves the Guardian can hit OpenAI adversarially; a
one-window test cannot resolve genre vs company. Accepted as confounder;
claim stays bounded and correlation-only.

Evidence hygiene: mirror URL and buzzsumo attribution URL carried verbatim
from tool output this run; no canonical Guardian URLs constructed. OpenAI
piece mirror opened first-hand (38 lines). No zero-coverage claims
(iteration-492 rule).

Durable conventions (from #495): line-anchored (^, re.MULTILINE) heading
search in iteration-log.md; relative newest-first ordering between
neighbors, never absolute-top or fixed head slices.
"""

import os
import re

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GUARDIAN = os.path.join(REPO, 'profiles', 'guardian.yaml')
LOG = os.path.join(REPO, 'iteration-log.md')

MECH_KEY = 'mechanism_537_guardian_meta_vs_openai_deal_partner_same_day_register_asymmetry_sep05'


def _load_profile():
    with open(GUARDIAN) as f:
        return yaml.safe_load(f)


def _mechanism():
    profile = _load_profile()
    return profile['competitor_relationships']['meta'][MECH_KEY]


def _mechanism_block_text():
    with open(GUARDIAN) as f:
        text = f.read()
    start = text.index(MECH_KEY)
    end = text.index('\n  anthropic:', start)
    return text[start:end]


class TestMechanismExistsAndShape:
    def test_mechanism_key_present_under_meta(self):
        profile = _load_profile()
        assert MECH_KEY in profile['competitor_relationships']['meta']

    def test_identity_fields(self):
        m = _mechanism()
        assert m['mechanism_id'] == 537
        assert m['iteration'] == 537
        assert m['iteration_type'] == 'A'
        assert m['date'] == '2026-09-05'

    def test_same_day_experiment_has_both_pieces(self):
        exp = _mechanism()['same_day_natural_experiment']
        assert exp['date'] == '2026-08-18'
        assert exp['meta_piece']['title'].startswith('Reel-ing it in')
        assert exp['openai_piece']['title'].startswith(
            'OpenAI announces slowing pace of development'
        )

    def test_two_pieces_per_side(self):
        m = _mechanism()
        exp = m['same_day_natural_experiment']
        assert exp['meta_piece'] and exp['openai_piece']
        assert m['meta_window_second_piece']['title'].startswith(
            'Meta misses earnings forecasts'
        )
        assert m['openai_window_second_piece']['title'].startswith(
            'OpenAI says its models went rogue'
        )

    def test_financial_context_names_partnership_and_zero_meta(self):
        fc = _mechanism()['financial_context']
        assert 'Feb 14 2025' in fc
        assert '$0' in fc
        assert 'Correlation only' in fc

    def test_author_kit_with_ray(self):
        assert _mechanism()['author'] == 'Kit (with Ray)'


class TestProvenance:
    def test_mirror_url_verbatim(self):
        url = _mechanism()['same_day_natural_experiment']['openai_piece'][
            'mirror_url'
        ]
        assert url == (
            'http://d33gy59ovltp76.cloudfront.net/news/'
            'openai-announces-slowing-pace-of-development-after-hack-by-rogue-agent'
        )

    def test_attribution_url_verbatim(self):
        assert _mechanism()['same_day_natural_experiment']['attribution_url'] == (
            'https://buzzsumo.com/journalist/johana-bhuiyan-149038734/'
        )

    def test_no_licensing_deal_disclosure_in_openai_piece(self):
        piece = _mechanism()['same_day_natural_experiment']['openai_piece']
        assert piece['disclosure_of_licensing_deal'] is False
        assert 'Feb 14 2025' in piece['disclosure_note']

    def test_openai_piece_first_hand_mirror_opened(self):
        piece = _mechanism()['same_day_natural_experiment']['openai_piece']
        assert piece['research_method'] == 'mirror_first_hand_opened_sep05'
        assert len(piece['key_quotes']) >= 2

    def test_registers_distinct(self):
        m = _mechanism()
        exp = m['same_day_natural_experiment']
        regs = [
            exp['meta_piece']['register'],
            exp['openai_piece']['register'],
            m['meta_window_second_piece']['register'],
            m['openai_window_second_piece']['register'],
        ]
        assert len(set(regs)) == 4

    def test_dates_present_and_2026(self):
        m = _mechanism()
        exp = m['same_day_natural_experiment']
        for piece in (
            exp['meta_piece'],
            exp['openai_piece'],
            m['meta_window_second_piece'],
        ):
            assert piece['date'].startswith('2026-')

    def test_sources_verified_date(self):
        assert _mechanism()['sources_verified_date'] == '2026-09-05'


class TestScorerDiscipline:
    def _scorer(self):
        return _mechanism()['asymmetry_scorer_MANUAL_ILLUSTRATIVE']

    def test_delta_value(self):
        assert self._scorer()['delta'] == pytest.approx(-0.30)

    def test_target_peer_scores(self):
        s = self._scorer()
        assert s['target_scores_MANUAL_ILLUSTRATIVE'] == [-0.45, -0.40]
        assert s['peer_scores_MANUAL_ILLUSTRATIVE'] == [-0.15, -0.10]
        assert s['target_entity'] == 'meta'
        assert s['peer_entity'] == 'openai'

    def test_p_value_not_calculated(self):
        assert 'NOT_CALCULATED' in self._scorer()['p_value']

    def test_not_significant(self):
        assert self._scorer()['is_significant'] is False

    def test_methodology_warns_not_empirical(self):
        method = self._scorer()['methodology']
        assert 'MANUAL ILLUSTRATIVE' in method
        assert 'DO NOT claim empirical significance' in method

    def test_correlation_not_causation(self):
        assert _mechanism()['correlation_not_causation'] is True


class TestCautiousLanguage:
    def test_no_em_dashes_in_block(self):
        block = _mechanism_block_text()
        assert '\u2014' not in block
        assert '\u2013' not in block

    def test_no_curly_quotes_in_block(self):
        block = _mechanism_block_text()
        for ch in ('\u2018', '\u2019', '\u201c', '\u201d'):
            assert ch not in block

    def test_block_is_ascii(self):
        _mechanism_block_text().encode('ascii')

    def test_confounder_levels_ranked(self):
        c = _mechanism()['confounders_ranked']
        assert len(c['strong']) == 3
        assert len(c['moderate']) == 2
        assert len(c['weak']) == 1

    def test_counter_evidence_present(self):
        ce = _mechanism()['counter_evidence']
        assert len(ce) == 3
        assert any('517' in x for x in ce)

    def test_relation_to_517_honest(self):
        rel = _mechanism()['relation_to_517']
        assert '517' in rel
        assert 'does not contradict it' in rel
        assert 'Correlation not causation' in rel

    def test_distinct_from_prior(self):
        d = _mechanism()['distinct_from_prior']
        assert '#532' in d
        assert '#527' in d
        assert 'no-disclosure check' in d


class TestNoveltyAndLog:
    def test_mechanism_id_537_unique_in_profile(self):
        with open(GUARDIAN) as f:
            text = f.read()
        assert text.count('mechanism_537') == 1

    def test_log_has_537_heading_line_anchored(self):
        with open(LOG) as f:
            text = f.read()
        assert re.search(r'^#537 Type A:', text, re.MULTILINE)

    def test_log_newest_first_537_before_536(self):
        with open(LOG) as f:
            text = f.read()
        assert text.index('#537 Type A:') < text.index('#536 Type E:')
