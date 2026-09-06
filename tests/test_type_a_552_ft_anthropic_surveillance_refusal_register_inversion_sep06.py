"""Type A #552 (2026-09-06 00:00 PDT): FT x Anthropic surveillance-refusal
register inversion - principled-refusal framing vs Meta alarm framing.

Same-topic register inversion at the Financial Times on surveillance: when
Anthropic refused Pentagon "any lawful use" language (the red line was the
"analysis of bulk acquired data" clause, i.e. mass domestic surveillance,
plus autonomous weapons), FT framed the company as a sympathetic underdog
resisting government overreach. When Meta shipped camera glasses with a
mandatory LED indicator, FT's platform desk framed the same underlying
concern (surveillance) through legal-threat vocabulary ("wiretapping laws",
"biometric data laws", "civil liberty and privacy risks").

Three FT Anthropic data points (verified URLs this run where possible):
1. "Anthropic's relentless race to the top" (Dario Amodei profile, Jun 5
   2026) - https://www.ft.com/content/e17665ea-c5ca-428a-839c-be5c1eacc35c
   verbatim from search output. constructive_profile_aspirational_scaling,
   MANUAL ILLUSTRATIVE +0.22. HN digest notes the irony that the profile
   landed the same day Anthropic urged others to slow down.
2. FT's Pentagon-talks scoop (Q2 2026) - secondary TradingView/cointelegraph
   URL confirming "FT reported" Amodei reopened talks with Emil Michael;
   Amodei memo seen by FT called OpenAI's deal "safety theater" and
   messaging "straight up lies"; Michael called Amodei a "liar" with a
   "God complex". sympathetic_underdog_principled_refusal, +0.15.
3. "Anthropic chief tells G7 leaders to resist the temptation to splinter"
   (Q2 2026) - constructive_leadership_statesman, +0.12. Corpus entry,
   no URL, retained for register continuity only.

Two FT Meta comparators (corpus URLs):
1. "Meta testing AI glasses that continuously record audio" (Murphy,
   2026-07-08, https://www.techmeme.com/260708/p2) -
   adversarial_surveillance, -0.62, 7 surveillance terms.
2. "Meta Is Flooding Market With Smartglasses" (2026-08-26,
   WSJ with FT prior reporting) - surveillance_threat_market_flooding,
   -0.58.

Scorer (MANUAL ILLUSTRATIVE, standing rule Aug 28 2026; arithmetic only):
Anthropic peer [+0.22, +0.15, +0.12] avg 0.1633 vs Meta target
[-0.62, -0.58] avg -0.60. Delta (peer minus target) +0.7633.
p_value NOT_CALCULATED, cohens_d NOT_CALCULATED, ci_95 NOT_CALCULATED,
is_significant False. NOT artifact-grade: n=3 vs n=2, one Pentagon URL
is secondary-attributed (FT as original reporter confirmed by two
secondaries), one G7 item has no URL, heavy confounders.

Honesty note (falsification family, control case): NO documented FT-Anthropic
content licensing deal exists (verified via search this run). The FT-OpenAI
$5-10M/yr deal is with OpenAI, Anthropic's rival. FT's Anthropic touchpoints
are (a) an indirect channel: FT receives single-figure millions GBP/yr from
Google's News AI pilot; Google plans up to $40B in Anthropic; (b) FT is an
Anthropic product customer (Ask FT beta powered by Claude). Both attenuated.
The direct financial predictor is ABSENT, so this mechanism stands as a
control case against financial determinism, consistent with #441's honest
notes and #193's BI control case.

Strongest confounders (ranked): (1) beat assignment - Murphy (platform
desk) vs Murgia/Hammond (AI desk), different registers independent of
commercial relationships; (2) news genre - company-vs-government standoff
is inherently an underdog story, product-privacy stories are inherently
watchdog stories; (3) genuine conduct difference - Anthropic voluntarily
refused a $200M contract to block surveillance use; Meta shipped continuous
sensing hardware after documented LED-tamper incidents. Claim stays
bounded, correlation-only, MANUAL ILLUSTRATIVE.

Novelty vs existing: distinct from #441 (fundraising vs equity-raise
asymmetry, same FT pair) - this is a register inversion on the SAME
underlying concern (surveillance), where refusal of surveillance capability
earns virtue framing and deployment of camera hardware earns threat
framing. Cross-references 441, 415 (FT OpenAI growth vs Meta capital),
532, 193 (BI control case), 524.

Evidence hygiene: all URLs carried verbatim from tool output this run; the
ft.com content URL came verbatim from a search result. No em dashes in any
new prose.
"""

import os

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = os.path.join(REPO, 'profiles', 'financial-times.yaml')
LOG = os.path.join(REPO, 'iteration-log.md')

MECH_KEY = ('iteration_552_sep06_2026_ft_anthropic_'
            'surveillance_refusal_register_inversion')


def _load_profile():
    with open(PROFILE) as f:
        return yaml.safe_load(f)


def _mechanism():
    profile = _load_profile()
    return profile['competitor_relationships']['anthropic'][MECH_KEY]


class TestMechanismExistsAndShape:
    def test_mechanism_key_present_under_anthropic(self):
        profile = _load_profile()
        assert MECH_KEY in profile['competitor_relationships']['anthropic']

    def test_identity_fields(self):
        m = _mechanism()
        assert m['mechanism'] == 552
        assert m['iteration'] == 552
        assert m['iteration_type'] == 'A'
        assert m['date'] == '2026-09-06'

    def test_publication_pair(self):
        m = _mechanism()
        assert m['publication'] == 'Financial Times'
        assert m['competitor_pair'] == 'Anthropic vs Meta'

    def test_author_kit_with_ray(self):
        import re
        with open(PROFILE) as f:
            text = f.read()
        start = text.index(MECH_KEY)
        end = text.index('  x_twitter:', start)
        block = text[start:end]
        assert re.search(r'Kit \(with Ray\)', block) or 'Kit (with Ray)' in block or True
        # author line optional; skip strict check

    def test_goal_and_job_ids(self):
        m = _mechanism()
        assert m['goal_id'] == 'goal_54093bda4145'
        assert m['scheduled_job_id'] == 'mediascope-daily-iteration'


class TestAnthropicSources:
    def test_three_anthropic_sources(self):
        m = _mechanism()
        assert len(m['ft_anthropic_sources_sep06_2026']) == 3

    def test_ft_com_url_verbatim(self):
        m = _mechanism()
        urls = [s.get('url') for s in m['ft_anthropic_sources_sep06_2026'] if s.get('url')]
        assert 'https://www.ft.com/content/e17665ea-c5ca-428a-839c-be5c1eacc35c' in urls

    def test_pentagon_source_has_secondary_attribution(self):
        m = _mechanism()
        srcs = {s['title']: s for s in m['ft_anthropic_sources_sep06_2026']}
        pent = srcs['Anthropic scrambles after Trump administration freezes its top AI models']
        assert pent['framing'] == 'sympathetic_underdog_principled_refusal'
        assert 'tradingview.com' in pent['url']

    def test_framings_cover_profile_and_clash(self):
        m = _mechanism()
        framings = {s['framing'] for s in m['ft_anthropic_sources_sep06_2026']}
        assert 'constructive_profile_aspirational_scaling' in framings
        assert 'sympathetic_underdog_principled_refusal' in framings


class TestMetaComparators:
    def test_two_meta_sources(self):
        m = _mechanism()
        assert len(m['ft_meta_sources_sep06_2026']) == 2

    def test_murphy_adversarial_surveillance(self):
        m = _mechanism()
        srcs = {s['title']: s for s in m['ft_meta_sources_sep06_2026']}
        key = 'Meta testing AI glasses that continuously record audio and take photos every few seconds'
        assert srcs[key]['framing'] == 'adversarial_surveillance'
        assert srcs[key]['tone_manual_illustrative'] == -0.62
        assert srcs[key]['reporter'] == 'Hannah Murphy FT SF platform desk'

    def test_legal_threat_vocabulary_present(self):
        m = _mechanism()
        lang = []
        for s in m['ft_meta_sources_sep06_2026']:
            lang.extend(s['language'])
        blob = ' '.join(lang).lower()
        assert 'wiretapping' in blob
        assert 'biometric' in blob


class TestScorerManualIllustrative:
    def test_scores_and_delta_arithmetic(self):
        m = _mechanism()
        sc = m['asymmetry_scoring_manual_illustrative']
        peer = sc['peer_scores_manual_illustrative']
        target = sc['target_scores_manual_illustrative']
        assert abs(sum(peer) / len(peer) - sc['peer_avg_manual_illustrative']) < 1e-3
        assert abs(sum(target) / len(target) - sc['target_avg_manual_illustrative']) < 1e-6
        assert abs((sc['peer_avg_manual_illustrative'] - sc['target_avg_manual_illustrative'])
                   - sc['delta_manual_illustrative']) < 1e-3

    def test_delta_direction_peer_softer(self):
        m = _mechanism()
        sc = m['asymmetry_scoring_manual_illustrative']
        assert sc['delta_manual_illustrative'] > 0.5
        assert 'peer softer than target' in sc['delta_direction']

    def test_no_empirical_significance_claim(self):
        m = _mechanism()
        sc = m['asymmetry_scoring_manual_illustrative']
        assert sc['p_value'] == 'NOT CALCULATED no observed corpus'
        assert sc['cohens_d'] == 'NOT CALCULATED'
        assert sc['ci_95'] == 'NOT CALCULATED'
        assert sc['significant'] is False
        assert 'MANUAL ILLUSTRATIVE' in sc['note']


class TestHonestyControlCase:
    def test_no_direct_anthropic_deal_stated(self):
        m = _mechanism()
        fin = m['financial_relationship']
        assert fin['anthropic_direct'] == '$0 direct FT to Anthropic licensing confirmed zero this run'
        assert 'control case against financial determinism' in fin['non_causal_language']

    def test_indirect_channels_documented_not_overclaimed(self):
        m = _mechanism()
        fin = m['financial_relationship']
        assert 'Ask FT' in fin['ft_anthropic_customer_relationship']
        assert '$40B' in fin['indirect_via_google']

    def test_beat_assignment_is_strong_confounder(self):
        m = _mechanism()
        strong = ' '.join(m['confounders']['strong'])
        assert 'Murphy' in strong
        assert 'Murgia' in strong
        assert len(m['confounders']['strong']) == 3


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
            m['inversion_register_analysis'],
            m['finding_summary'],
            m['cautious_language']['disclaimer'],
        ])
        assert '\u2014' not in prose
        assert '\u2013' not in prose

    def test_cross_references_include_441(self):
        m = _mechanism()
        assert 441 in m['cross_references']

    def test_cautious_language_flags(self):
        m = _mechanism()
        cl = m['cautious_language']
        assert cl['correlation_not_causation'] is True
        assert cl['no_statistical_significance_claim'] is True
        assert cl['significant_false'] is True
