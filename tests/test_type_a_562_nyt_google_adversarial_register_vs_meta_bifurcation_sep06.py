"""Type A #562 (2026-09-06 10:00 PDT): The New York Times x Google adversarial
register confirmed vs Meta bifurcation - control case against financial
determinism.

NYT (financial tie: adversarial, $0 licensing) applies an ADVERSARIAL
register to Google AI: it commissioned the Oumi AI Overviews accuracy study
and was first to report it (2026-04-09, tens of millions of incorrect
answers per hour, ungrounded responses, misinformation crisis), filed its
own court motion against Google and the DOJ in the search monopoly remedy
trial (2025-04-07), and reported the monopoly-ruling outcomes in a
straight-to-critical register (David McCabe). The same paper covers Meta
with a BIFURCATED register per mechanism #69: positive on open-source AI
philosophy (serves the anti-OpenAI litigation narrative), adversarial on AI
execution (2026-06-23 voluntary-review holdout), neutral on business scoops
(2026-06-26 Arena prediction markets). Google is harsher by MANUAL
ILLUSTRATIVE 0.45 despite being the commercial dependency (dominant traffic
referrer whose traffic reduction the NYT 10-Q flags as a business risk;
Canada C-18 has Google paying C$100M per year into the publisher fund while
Meta blocks news entirely, #529). Money does not buy softness in this lane.

Three NYT Google data points (verbatim URLs from this run):
1. NYT first to report Oumi AI Overviews study (2026-04-09) -
   commissioned_misinformation_investigation, -0.70, secondary-attributed
   via MobileSyrup and NY Post (both attribute NYT as first to report).
2. NYT court motion against Google and DOJ over public access in the
   search monopoly remedy trial (2025-04-07) - institutional_adversarial,
   -0.50, Editor and Publisher reporting on the NYT filing.
3. Google avoids harshest penalties in landmark search monopoly ruling
   (2025-09-02) - monopoly_adversarial_reportage, -0.40, David McCabe NYT
   byline via Editor and Publisher reprint.

Three NYT Meta comparators (in-corpus):
1. Meta open-source AI philosophy positive strand (mechanism #69) - +0.40,
   instrumental to the anti-OpenAI litigation narrative.
2. NYT Meta AI voluntary-review and government-review holdout
   (2026-06-23, in-corpus sample output) - ai_execution_adversarial, -0.65.
3. NYT Arena prediction-markets partnership scoop (2026-06-26, in-corpus
   reconstruction from Reuters) - neutral_business_scoop, 0.0.

Scorer (MANUAL ILLUSTRATIVE, standing rule Aug 28 2026; arithmetic only):
Google target [-0.70, -0.50, -0.40] avg -0.5333 vs Meta peer
[+0.40, -0.65, 0.0] avg -0.0833. Engine target-minus-peer -0.45,
delta_manual_illustrative -0.45 (target harsher than peer by 0.45).
Engine p ~ 0.28, is_significant False: both layers agree not significant
(agreement pole, same class as #558). p_value NOT_CALCULATED,
cohens_d NOT_CALCULATED, ci_95 NOT_CALCULATED, is_significant False.
NOT artifact-grade: n=3 vs n=3, secondary attributions, heavy confounders.

Honesty note (control case, falsification family): NO NYT-Google AI
licensing deal exists ($0, adversarial tie confirmed this run). The
money-sympathy direction is INVERTED: commercial dependency (traffic,
C-18 fund) coincides with the harsher register. Strongest confounders:
(1) litigation instrumentality - adversarial Google AI and positive Meta
open-source strands both serve legal postures (publisher coalition,
anti-OpenAI suit); (2) item selection - no verbatim nytimes.com URL
surfaced for a positive Google AI item this run, disclosed not
zero-claimed; (3) the Apr 2025 court motion is institutional action, not
coverage tone (exclusion-robust: Google avg moves -0.5333 to -0.55).

Novelty: first mechanism ever under competitor_relationships.google in
nytimes.yaml (key previously held only financial metadata). Distinct from
#537 (Guardian Meta-vs-OpenAI same-day register, different publication)
and #547 (WIRED x Google/Samsung camera glasses, different lane). Extends
the falsification family (#552, #557, #193) to the NYT and to the
inverted-money-sympathy boundary.

Open empirical test (not asserted): the next major Google AI launch vs the
next major Meta open-source release at NYT tests whether the registers
persist (instrumentality hypothesis) or soften (selection confounder).

Evidence hygiene: all URLs carried verbatim from tool output this run or
from in-repo corpus pointers; no zero-coverage claims per iteration-492
rule. No em dashes in any new prose.
"""

import os
from datetime import datetime

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = os.path.join(REPO, 'profiles', 'nytimes.yaml')
LOG = os.path.join(REPO, 'iteration-log.md')

MECH_KEY = ('mechanism_562_nyt_google_adversarial_register_confirmed_vs_'
            'meta_bifurcation_sep06')


def _load_profile():
    with open(PROFILE) as f:
        return yaml.safe_load(f)


def _mechanism():
    profile = _load_profile()
    return profile['competitor_relationships']['google'][MECH_KEY]


class TestMechanismExistsAndShape:
    def test_mechanism_key_present_under_google(self):
        profile = _load_profile()
        assert MECH_KEY in profile['competitor_relationships']['google']

    def test_identity_fields(self):
        m = _mechanism()
        assert m['mechanism_id'] == 562
        assert m['iteration'] == 562
        assert m['iteration_type'] == 'A'
        assert m['date_analyzed'] == '2026-09-06'

    def test_publication_pair(self):
        m = _mechanism()
        assert m['publication'] == 'The New York Times'
        assert m['competitor_pair'] == 'Google vs Meta'

    def test_type_label(self):
        m = _mechanism()
        assert 'Type A' in m['type']

    def test_goal_and_job_ids(self):
        m = _mechanism()
        assert m['scheduled_job_id'] == 'mediascope-daily-iteration'
        assert m['goal_id'] == 'goal_54093bda4145'


class TestGoogleSources:
    def test_three_google_sources(self):
        m = _mechanism()
        srcs = m['nyt_google_sources_sep06_2026']
        assert len(srcs) == 3

    def test_oumi_study_commissioned_adversarial(self):
        m = _mechanism()
        srcs = m['nyt_google_sources_sep06_2026']
        oumi = srcs[0]
        assert 'Oumi' in oumi['title']
        assert oumi['date'] == '2026-04-09'
        assert oumi['tone_manual_illustrative'] == -0.70
        assert 'first to report' in oumi['url_source']
        assert 'misinformation crisis' in oumi['language']

    def test_court_motion_institutional_action_disclosed(self):
        m = _mechanism()
        srcs = m['nyt_google_sources_sep06_2026']
        motion = srcs[1]
        assert motion['date'] == '2025-04-07'
        assert motion['tone_manual_illustrative'] == -0.50
        assert 'institutional' in motion['notes'].lower()

    def test_monopoly_ruling_critical_register(self):
        m = _mechanism()
        srcs = m['nyt_google_sources_sep06_2026']
        ruling = srcs[2]
        assert 'McCabe' in ruling['notes']
        assert ruling['tone_manual_illustrative'] == -0.40

    def test_urls_verbatim_and_https(self):
        m = _mechanism()
        srcs = m['nyt_google_sources_sep06_2026']
        for s in srcs:
            assert s['url'].startswith('https://'), s['url']


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
        assert sc['delta_manual_illustrative'] == -0.45
        assert 'target harsher than peer' in sc['delta_direction']

    def test_engine_arithmetic_matches_logged_delta(self):
        from mediascope.score.asymmetry import calculate_asymmetry
        m = _mechanism()
        sc = m['asymmetry_scoring_manual_illustrative']
        r = calculate_asymmetry(
            sc['target_scores_manual_illustrative'],
            sc['peer_scores_manual_illustrative'],
            'Google', ['Meta'], 'nytimes',
            datetime(2025, 4, 1), datetime(2026, 9, 6))
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


class TestHonestyControlCase:
    def test_zero_google_licensing_deal_stated(self):
        m = _mechanism()
        fin = m['financial_relationship']
        assert fin['google_direct'].startswith('$0')
        assert 'control case against financial determinism' in fin[
            'non_causal_language']

    def test_inverted_money_sympathy(self):
        m = _mechanism()
        fin = m['financial_relationship']
        assert 'INVERTED' in fin['non_causal_language']
        assert 'C$100M' in fin['canada_c18_context']

    def test_litigation_instrumentality_is_strong_confounder(self):
        m = _mechanism()
        strong = ' '.join(m['confounders']['strong'])
        assert 'instrumentality' in strong
        assert 'selection' in strong
        assert len(m['confounders']['strong']) == 3

    def test_open_empirical_test_named(self):
        m = _mechanism()
        assert 'Gemini' in m['open_empirical_test']
        assert 'open-source' in m['open_empirical_test']


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
        assert '\u2014' not in prose
        assert '\u2013' not in prose

    def test_cross_references_include_key_mechanisms(self):
        m = _mechanism()
        assert 69 in m['cross_references']
        assert 529 in m['cross_references']
        assert 552 in m['cross_references']
        assert 557 in m['cross_references']
        assert 559 in m['cross_references']

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
        assert '#562 Type A' in text

    def test_no_duplicate_562_mechanism_keys(self):
        profile = _load_profile()
        count = sum(1 for k in
                    profile['competitor_relationships']['google']
                    if '562' in k)
        assert count == 1
