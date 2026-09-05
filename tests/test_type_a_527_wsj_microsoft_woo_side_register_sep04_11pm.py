"""Type A #527 (2026-09-04 23:00 PDT): WSJ x Microsoft woo-side register.

Direct follow-up to #524 Type C (News Corp x Microsoft HarperCollins book
licensing, Nov 2024 - the fourth AI revenue leg) and woo-side complement to
#522 Type A (WSJ x Perplexity sue-side register, delta -0.125 n.s.).
#524 predicted symmetric softening incentives toward OpenAI, Meta, AND
Microsoft for WSJ coverage vs no-deal entities.

Three first-hand WSJ Microsoft articles opened via browser.open this run:
1. "Microsoft Needs Copilot to Get Back in the Air" (~2026-04-23, Dan
   Gallagher + Asa Fitch) - skeptical financial scrutiny WITH cushioning
   ("AI winner" to "AI loser", $800B market cap loss, 3.5% Copilot
   conversion "isn't tremendous", "competitors are eating its lunch" - but
   "patient investors should be rewarded"). tone -0.15. Same Gallagher who
   wrote #522's Perplexity quixotic-dismissal (-0.30, zero rebuttal):
   within-journalist gradient favors the deal partner.
2. "Microsoft's Satya Nadella: We Can't Let AI Giants Eat the Economy"
   (~2026-06-21, Bradley Olson + Tina Li) - elder-statesman access
   interview; Microsoft as reformer taking on "AI giants" OpenAI and
   Anthropic (its own deal partners). tone +0.10.
3. "Microsoft Profit Jumps 31% as Azure Cloud Sales Surpass $100 Billion"
   (~2026-07-29, Anissa Gardizy) - celebratory earnings; comparative praise
   ("stayed cash-flow positive, unlike... Alphabet, which recently reported
   negative cash flows"); $3.2B Anthropic investment gain; 3,200 Xbox
   layoffs buried mid-piece. tone +0.25.

Scorer: Microsoft avg +0.0667 vs Meta rogue-AI comparator -0.45 (#522):
delta -0.5167 directionally consistent with #524, n=3 vs n=1, p_value
NOT_CALCULATED (standing rule Aug 28), is_significant False, adjusted
-0.167 (small). NOT artifact-grade.

Financial context: News Corp receives Microsoft AI revenue through the
HarperCollins book-licensing leg (Nov 2024, $5K/title 50/50 split, 3-year
term, Bloomberg-reported via anonymous sources, NEVER officially
confirmed). Direction of money predicts direction of editorial sympathy
(correlation, not causation). Book-division deal attenuates
owner-to-WSJ-newsroom transmission vs the Dow Jones news legs.

Strongest counterargument: the Copilot piece proves WSJ does hard
financial scrutiny of Microsoft with only standard analyst cushioning;
earnings positivity tracks real results; Meta's -0.45 is incident-driven,
not entity-driven. The woo-and-sue incentive is not needed to explain the
register gap.

Evidence hygiene: all three 2026 WSJ articles opened first-hand via
browser.open this run (verbatim quotes in the YAML entry); all URLs carried
verbatim from search-result full-URL listings - no canonical URLs
constructed. No zero-coverage claims (iteration-492 rule).

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

MECH_KEY = 'mechanism_527_wsj_microsoft_woo_side_register_sep04'


def _load_profile():
    with open(NEWS_CORP) as f:
        return yaml.safe_load(f)


def _mechanism():
    profile = _load_profile()
    return profile['competitor_relationships']['microsoft'][MECH_KEY]


def _mechanism_block_text():
    with open(NEWS_CORP) as f:
        text = f.read()
    start = text.index(MECH_KEY)
    end = text.index('\n  anthropic:', start)
    return text[start:end]


class TestMechanismExistsAndShape:
    def test_mechanism_key_present_under_microsoft(self):
        profile = _load_profile()
        assert MECH_KEY in profile['competitor_relationships']['microsoft']

    def test_identity_fields(self):
        m = _mechanism()
        assert m['mechanism_id'] == 527
        assert m['iteration'] == 527
        assert m['iteration_type'] == 'A'
        assert m['date'] == '2026-09-04'

    def test_three_articles_present(self):
        m = _mechanism()
        assert len(m['articles']) == 3

    def test_financial_context_names_harpercollins(self):
        m = _mechanism()
        assert 'HarperCollins' in m['financial_context']
        assert 'correlation, not causation' in m['financial_context']


class TestProvenance:
    EXPECTED_URLS = [
        'https://www.wsj.com/tech/ai/microsoft-needs-copilot-to-get-back-in-the-air-6a9746d5',
        'https://www.wsj.com/tech/ai/microsofts-satya-nadella-we-cant-let-ai-giants-eat-the-economy-b9d33b9f',
        'https://www.wsj.com/articles/microsoft-earnings-q4-fy26-msft-stock-dfd3843e',
    ]

    def test_urls_are_verbatim_wsj_https(self):
        urls = [a['url'] for a in _mechanism()['articles']]
        assert urls == self.EXPECTED_URLS
        for u in urls:
            assert u.startswith('https://www.wsj.com/')

    def test_all_first_hand_this_run(self):
        for a in _mechanism()['articles']:
            assert a['research_method'] == 'first_hand_browser_open_sep04'

    def test_bylines_match_first_hand_reads(self):
        bylines = [a['byline'] for a in _mechanism()['articles']]
        assert bylines == [
            'Dan Gallagher and Asa Fitch',
            'Bradley Olson and Tina Li',
            'Anissa Gardizy',
        ]

    def test_dates_present_and_2026(self):
        for a in _mechanism()['articles']:
            assert a['date'].startswith('2026-')

    def test_key_quotes_nonempty_and_verbatim(self):
        for a in _mechanism()['articles']:
            assert len(a['key_quotes']) >= 3
        copilot = _mechanism()['articles'][0]
        assert any('800 billion' in q for q in copilot['key_quotes'])
        earnings = _mechanism()['articles'][2]
        assert any('cash-flow positive' in q for q in earnings['key_quotes'])

    def test_registers_distinct(self):
        regs = [a['register'] for a in _mechanism()['articles']]
        assert len(set(regs)) == 3


class TestScorerDiscipline:
    def _scorer(self):
        return _mechanism()['asymmetry_scorer_MANUAL_ILLUSTRATIVE']

    def test_delta_value(self):
        assert self._scorer()['delta'] == pytest.approx(-0.5167)

    def test_target_peer_scores(self):
        s = self._scorer()
        assert s['target_scores_MANUAL_ILLUSTRATIVE'] == [-0.45]
        assert s['peer_scores_MANUAL_ILLUSTRATIVE'] == [-0.15, 0.10, 0.25]

    def test_p_value_not_calculated(self):
        assert 'NOT_CALCULATED' in self._scorer()['p_value']

    def test_not_significant(self):
        s = self._scorer()
        assert s['significant'] is False
        assert s['significant_empirical'] is False

    def test_correlation_not_causation(self):
        assert _mechanism()['correlation_not_causation'] is True

    def test_adjusted_delta_documented(self):
        s = self._scorer()
        assert s['adjusted_delta'] == pytest.approx(-0.167)
        assert 'beat_assignment' in s['adjustments']


class TestCautiousLanguage:
    def test_no_em_dashes_in_block(self):
        block = _mechanism_block_text()
        assert '\u2014' not in block
        assert '\u2013' not in block

    def test_no_curly_quotes_in_block(self):
        block = _mechanism_block_text()
        for ch in ('\u2018', '\u2019', '\u201c', '\u201d'):
            assert ch not in block

    def test_strongest_counterargument_present(self):
        m = _mechanism()
        ca = m['strongest_counterargument']
        assert 'Copilot' in ca
        assert 'incident-driven' in ca

    def test_confounder_levels_ranked(self):
        levels = [c['level'] for c in _mechanism()['confounders']]
        assert levels.count('STRONG') == 3
        assert levels.count('MODERATE') == 3
        assert levels.count('WEAK') == 1

    def test_artifact_readiness_not_warranted(self):
        assert 'No analysis.json update warranted' in _mechanism()['artifact_readiness']


class TestNoveltyAndLog:
    def test_mechanism_id_527_unique_in_profile(self):
        with open(NEWS_CORP) as f:
            text = f.read()
        assert text.count('mechanism_527') == 1

    def test_cross_references_519_522_524(self):
        refs = ' '.join(_mechanism()['cross_references'])
        assert '#519' in refs
        assert '#522' in refs
        assert '#524' in refs

    def test_log_has_527_heading_line_anchored(self):
        with open(LOG) as f:
            text = f.read()
        assert re.search(r'^#527 Type A:', text, re.MULTILINE)

    def test_log_newest_first_527_before_526(self):
        with open(LOG) as f:
            text = f.read()
        assert text.index('#527 Type A:') < text.index('#526 Type E:')

    def test_log_entry_names_author_kit_with_ray(self):
        m = _mechanism()
        assert m['author'] == 'Kit (with Ray)'
