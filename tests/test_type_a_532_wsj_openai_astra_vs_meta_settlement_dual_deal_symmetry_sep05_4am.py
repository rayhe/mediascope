"""Type A #532 (2026-09-05 04:00 PDT): WSJ x OpenAI Astra-cycle vs Meta
settlement-cycle - dual-deal symmetry test.

First Type A empirical test of #519 Type C's dual-deal symmetric-softening
prediction. News Corp collects ~$50M/yr from BOTH OpenAI (May 2024,
$250M/5yr) and Meta (Mar 2026, up to $50M/yr); #519 predicted symmetric
softening toward both vs no-deal entities.

Aug-Sep 2026 gave both companies major negative news in the same window:
OpenAI's Astra "critical" cyber rating (Sep 2) plus Hugging Face hack
fallout (Aug 8); Meta's $18B teen-safety settlement (Aug 26, two pieces).
All four WSJ articles via search-result excerpts (wsj.com paywalled, none
opened first-hand this run) - bounded, honestly labeled.

Scorer (MANUAL ILLUSTRATIVE): OpenAI [-0.15, -0.25] avg -0.20; Meta
[-0.30, -0.25] avg -0.275; delta -0.075 (Meta trivially harder).
p_value NOT_CALCULATED (standing rule Aug 28), is_significant False.
Directionally consistent with #519 symmetry (gap far smaller than the
rogue-AI window's -0.25), but n=2 per side - does not confirm.
Correlation not causation. NOT artifact-grade.

Strongest counterargument: the rogue-AI window (Jul-Aug 2026) showed a
LARGER gap (OpenAI -0.2 vs Meta -0.45, delta -0.25) in the same
publication, so asymmetry persists in some windows; straight news
reporting of negative events is the null expectation for a quality
newsroom regardless of incentives.

Evidence hygiene: all four URLs carried verbatim from search-result
full-URL listings - no canonical URLs constructed. No zero-coverage
claims (iteration-492 rule). Bounded excerpts, not first-hand reads.

Durable conventions (from #495): line-anchored (^, re.MULTILINE) heading
search in iteration-log.md; relative newest-first ordering between
neighbors, never absolute-top or fixed head slices.
"""

import os
import re

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NEWS_CORP = os.path.join(REPO, 'profiles', 'news-corp.yaml')
LOG = os.path.join(REPO, 'iteration-log.md')

MECH_KEY = 'mechanism_532_wsj_openai_astra_vs_meta_settlement_dual_deal_symmetry_sep05'


def _load_profile():
    with open(NEWS_CORP) as f:
        return yaml.safe_load(f)


def _mechanism():
    profile = _load_profile()
    return profile['competitor_relationships']['openai'][MECH_KEY]


def _mechanism_block_text():
    with open(NEWS_CORP) as f:
        text = f.read()
    start = text.index(MECH_KEY)
    end = text.index('\n  meta:', start)
    return text[start:end]


class TestMechanismExistsAndShape:
    def test_mechanism_key_present_under_openai(self):
        profile = _load_profile()
        assert MECH_KEY in profile['competitor_relationships']['openai']

    def test_identity_fields(self):
        m = _mechanism()
        assert m['mechanism_id'] == 532
        assert m['iteration'] == 532
        assert m['iteration_type'] == 'A'
        assert m['date'] == '2026-09-05'

    def test_two_articles_per_side(self):
        m = _mechanism()
        assert len(m['articles_openai']) == 2
        assert len(m['articles_meta']) == 2

    def test_financial_context_names_dual_payer(self):
        m = _mechanism()
        assert 'OpenAI leg May 2024' in m['financial_context']
        assert 'Meta leg Mar 2026' in m['financial_context']

    def test_author_kit_with_ray(self):
        assert _mechanism()['author'] == 'Kit (with Ray)'


class TestProvenance:
    EXPECTED_OPENAI_URLS = [
        'https://www.wsj.com/tech/ai/openai-to-restrict-astra-model-after-rating-it-critical-cyber-risk-499b5a46',
        'https://www.wsj.com/tech/ai/openai-pauses-some-work-on-new-ai-model-over-cybersecurity-concerns-8473a86f',
    ]
    EXPECTED_META_URLS = [
        'https://www.wsj.com/tech/meta-reaches-18-billion-settlement-with-48-states-over-child-safety-claims-cf725a2b',
        'https://www.wsj.com/tech/personal-tech/meta-teen-safety-instagram-facebook-ae83287d',
    ]

    def test_urls_are_verbatim_wsj_https(self):
        m = _mechanism()
        openai_urls = [a['url'] for a in m['articles_openai']]
        meta_urls = [a['url'] for a in m['articles_meta']]
        assert openai_urls == self.EXPECTED_OPENAI_URLS
        assert meta_urls == self.EXPECTED_META_URLS
        for u in openai_urls + meta_urls:
            assert u.startswith('https://www.wsj.com/')

    def test_all_bounded_excerpts_not_first_hand(self):
        m = _mechanism()
        for a in m['articles_openai'] + m['articles_meta']:
            assert a['research_method'] == 'search_result_excerpt_bounded_sep05'

    def test_dates_present_and_2026(self):
        m = _mechanism()
        for a in m['articles_openai'] + m['articles_meta']:
            assert a['date'].startswith('2026-')

    def test_key_quotes_nonempty(self):
        m = _mechanism()
        for a in m['articles_openai'] + m['articles_meta']:
            assert len(a['key_quotes']) >= 2

    def test_openai_disclosure_quote_present(self):
        quotes = ' '.join(
            q for a in _mechanism()['articles_openai'] for q in a['key_quotes']
        )
        assert 'content-licensing partnership with OpenAI' in quotes

    def test_meta_facebook_files_quote_present(self):
        quotes = ' '.join(
            q for a in _mechanism()['articles_meta'] for q in a['key_quotes']
        )
        assert 'Facebook Files' in quotes

    def test_registers_distinct(self):
        m = _mechanism()
        regs = [a['register'] for a in m['articles_openai'] + m['articles_meta']]
        assert len(set(regs)) == 4


class TestScorerDiscipline:
    def _scorer(self):
        return _mechanism()['asymmetry_scorer_MANUAL_ILLUSTRATIVE']

    def test_delta_value(self):
        assert self._scorer()['delta'] == pytest.approx(-0.075)

    def test_target_peer_scores(self):
        s = self._scorer()
        assert s['target_scores_MANUAL_ILLUSTRATIVE'] == [-0.30, -0.25]
        assert s['peer_scores_MANUAL_ILLUSTRATIVE'] == [-0.15, -0.25]
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
        assert any('rogue-ai window' in x.lower() for x in ce)

    def test_relation_to_519_honest(self):
        rel = _mechanism()['relation_to_519']
        assert '#519' in rel
        assert 'does not confirm it' in rel
        assert 'Correlation not causation' in rel

    def test_distinct_from_prior(self):
        d = _mechanism()['distinct_from_prior']
        assert '#522' in d
        assert '#527' in d
        assert 'rogue_ai_framing_tone' in d


class TestNoveltyAndLog:
    def test_mechanism_id_532_unique_in_profile(self):
        with open(NEWS_CORP) as f:
            text = f.read()
        assert text.count('mechanism_532') == 1

    def test_log_has_532_heading_line_anchored(self):
        with open(LOG) as f:
            text = f.read()
        assert re.search(r'^#532 Type A:', text, re.MULTILINE)

    def test_log_newest_first_532_before_531(self):
        with open(LOG) as f:
            text = f.read()
        assert text.index('#532 Type A:') < text.index('#531 Type E:')
