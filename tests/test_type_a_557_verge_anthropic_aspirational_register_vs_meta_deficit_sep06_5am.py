"""Type A #557 (2026-09-06 05:00 PDT): The Verge x Anthropic aspirational-register
vs Meta deficit register - control case against financial determinism.

The Verge (Vox Media/PMC) has a documented OpenAI licensing deal (May 29 2024)
but $0 financial tie with Anthropic. Yet The Verge applies an aspirational
business-milestone register to Anthropic (IPO filing as maturation, Pentagon
solidarity hero framing, EU AI Act compliance register) while applying a
deficit/follower register to Meta ("reentering the AI race", researchers
rejecting offers over values, supply-constraint pause). The softness crosses
the deal boundary: the licensing deal cannot be the sole driver.

Three Verge Anthropic data points (verified URLs this run where possible):
1. "Anthropic has officially filed to go public" (2026-06-01) -
   business_milestone_maturation, MANUAL ILLUSTRATIVE +0.25, corpus pointer
   via #52 (theverge.com blocked per standing rule).
2. "Employees across OpenAI and Google support Anthropic's lawsuit against the
   Pentagon" (2026-03-09) - solidarity_hero_underdog, +0.30, verbatim
   theverge.com URL surfaced in this run's browser.search output.
3. "Anthropic plans Claude watermarks as EU AI Act duties start" (mid-Aug
   2026) - regulatory_compliance_responsible, +0.10, Verge-attributed via
   stechtimes.com secondary (verbatim Full-URL listing this run); no direct
   theverge.com URL surfaced verbatim, recorded as secondary-attributed.

Three Verge Meta comparators (corpus URLs):
1. "Meta is reentering the AI race with a new model called Muse Spark"
   (2026-04-08) - deficit_follower, -0.35, "reentering" implies Meta left.
2. "Sources: some AI researchers rejected Meta's offers to stay at jobs that
   align with their values" (2025-07-10) - values_deficit_rejection, -0.30.
3. "Meta pauses wider Ray-Ban Display expansion due to supply shortages"
   (2026-01-06) - supply_constraint_deficit, -0.15.

Scorer (MANUAL ILLUSTRATIVE, standing rule Aug 28 2026; arithmetic only):
Anthropic peer [+0.25, +0.30, +0.10] avg 0.2167 vs Meta target
[-0.35, -0.30, -0.15] avg -0.2667. Delta (peer minus target) +0.4833.
p_value NOT_CALCULATED, cohens_d NOT_CALCULATED, ci_95 NOT_CALCULATED,
is_significant False. NOT artifact-grade: n=3 vs n=3, one Verge item is
secondary-attributed (Verge as original reporter per SendTech Times), heavy
confounders.

Honesty note (control case, falsification family): NO documented
Verge/Vox/PMC-Anthropic content licensing deal exists (verified this run).
The Vox Media-OpenAI strategic partnership is with Anthropic's primary
rival. Strongest confounders: (1) beat concentration - Hayden Field's AI
beat is functionally an OpenAI/Anthropic beat per #52 (15+ vs 2-3 articles
in 14 months); (2) news genre - IPO filings and solidarity letters are
inherently upbeat, talent-war and supply-constraint stories inherently
deficit; (3) hype-cycle position - Anthropic pre-IPO ~$2T target Oct 2026
vs Meta as incumbent follower.

Novelty: first mechanism ever under competitor_relationships.anthropic in
the-verge.yaml (key previously held only financial metadata). Distinct from
#425 (Verge OpenAI aspiration vs Meta deficit, same AI-model domain, deal
partner peer) and #507 (Verge OpenAI ad-monetization boundary condition,
domain-bounded softening). Extends #52 from journalist to publication level.

Open empirical test (not asserted): The Verge confirmed the Aug 29 2026
Sony/Warner music copyright filing against Anthropic (per fathom.news); the
Verge headline framing of that suit tests whether the aspirational register
survives genuinely adversarial facts.

Evidence hygiene: all URLs carried verbatim from tool output this run or
from in-repo corpus pointers verified by prior runs; no zero-coverage claims
per iteration-492 rule. No em dashes in any new prose.
"""

import os

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = os.path.join(REPO, 'profiles', 'the-verge.yaml')
LOG = os.path.join(REPO, 'iteration-log.md')

MECH_KEY = ('mechanism_557_verge_anthropic_aspirational_register_vs_'
            'meta_deficit_sep06')


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
        assert m['mechanism_id'] == 557
        assert m['iteration'] == 557
        assert m['iteration_type'] == 'A'
        assert m['date_analyzed'] == '2026-09-06'

    def test_publication_pair(self):
        m = _mechanism()
        assert m['publication'] == 'The Verge'
        assert m['competitor_pair'] == 'Anthropic vs Meta'

    def test_type_label(self):
        m = _mechanism()
        assert 'Type A' in m['type']

    def test_goal_and_job_ids(self):
        m = _mechanism()
        assert m['goal_id'] == 'goal_54093bda4145'
        assert m['scheduled_job_id'] == 'mediascope-daily-iteration'


class TestAnthropicSources:
    def test_three_anthropic_sources(self):
        m = _mechanism()
        assert len(m['verge_anthropic_sources_sep06_2026']) == 3

    def test_verbatim_theverge_url_from_this_run(self):
        m = _mechanism()
        urls = [s.get('url') for s in m['verge_anthropic_sources_sep06_2026']
                if s.get('url')]
        assert ('https://www.theverge.com/ai-artificial-intelligence/891514/'
                'anthropic-pentagon-lawsuit-amicus-brief-openai-google') in urls

    def test_pentagon_source_solidarity_framing(self):
        m = _mechanism()
        srcs = {s['title']: s
                for s in m['verge_anthropic_sources_sep06_2026']}
        pent = srcs['Employees across OpenAI and Google support Anthropic\'s '
                    'lawsuit against the Pentagon']
        assert pent['framing'] == 'solidarity_hero_underdog'
        assert pent['tone_manual_illustrative'] == 0.30

    def test_watermark_source_secondary_attribution_disclosed(self):
        m = _mechanism()
        srcs = {s['title']: s
                for s in m['verge_anthropic_sources_sep06_2026']}
        wm = srcs['Anthropic plans Claude watermarks as EU AI Act duties '
                  'start']
        assert wm['framing'] == 'regulatory_compliance_responsible'
        assert 'stechtimes.com' in wm['url']
        assert 'secondary' in wm['url_source'].lower()

    def test_framings_cover_milestone_solidarity_compliance(self):
        m = _mechanism()
        framings = {s['framing']
                    for s in m['verge_anthropic_sources_sep06_2026']}
        assert 'business_milestone_maturation' in framings
        assert 'solidarity_hero_underdog' in framings
        assert 'regulatory_compliance_responsible' in framings


class TestMetaComparators:
    def test_three_meta_sources(self):
        m = _mechanism()
        assert len(m['verge_meta_sources_sep06_2026']) == 3

    def test_muse_spark_deficit_follower(self):
        m = _mechanism()
        srcs = {s['title']: s
                for s in m['verge_meta_sources_sep06_2026']}
        key = ('Meta is reentering the AI race with a new model called '
               'Muse Spark')
        assert srcs[key]['framing'] == 'deficit_follower'
        assert srcs[key]['tone_manual_illustrative'] == -0.35

    def test_deficit_vocabulary_present(self):
        m = _mechanism()
        lang = []
        for s in m['verge_meta_sources_sep06_2026']:
            lang.extend(s['language'])
        blob = ' '.join(lang).lower()
        assert 'reentering' in blob
        assert 'rejected' in blob

    def test_supply_pause_comparator(self):
        m = _mechanism()
        srcs = {s['title']: s
                for s in m['verge_meta_sources_sep06_2026']}
        key = ('Meta pauses wider Ray-Ban Display expansion due to supply '
               'shortages')
        assert srcs[key]['framing'] == 'supply_constraint_deficit'
        assert 'theverge.com' in srcs[key]['url']


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
        assert abs((sc['peer_avg_manual_illustrative']
                    - sc['target_avg_manual_illustrative'])
                   - sc['delta_manual_illustrative']) < 1e-3

    def test_delta_direction_peer_softer(self):
        m = _mechanism()
        sc = m['asymmetry_scoring_manual_illustrative']
        assert sc['delta_manual_illustrative'] > 0.4
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
        assert fin['anthropic_direct'] == ('$0 direct Verge to Anthropic '
                                          'licensing confirmed zero this run')
        assert 'control case against financial determinism' in fin[
            'non_causal_language']

    def test_openai_deal_is_with_rival_not_anthropic(self):
        m = _mechanism()
        fin = m['financial_relationship']
        assert 'May 29 2024' in fin['verge_openai_deal']
        assert 'rival' in fin['non_causal_language']

    def test_beat_concentration_is_strong_confounder(self):
        m = _mechanism()
        strong = ' '.join(m['confounders']['strong'])
        assert 'Field' in strong
        assert 'hype' in strong
        assert len(m['confounders']['strong']) == 3

    def test_open_empirical_test_named(self):
        m = _mechanism()
        assert 'Sony' in m['open_empirical_test']
        assert 'Warner' in m['open_empirical_test']


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

    def test_cross_references_include_52_and_425(self):
        m = _mechanism()
        assert 52 in m['cross_references']
        assert 425 in m['cross_references']
        assert 507 in m['cross_references']

    def test_cautious_language_flags(self):
        m = _mechanism()
        cl = m['cautious_language']
        assert cl['correlation_not_causation'] is True
        assert cl['no_statistical_significance_claim'] is True
        assert cl['significant_false'] is True

    def test_iteration_log_entry_present(self):
        with open(LOG) as f:
            text = f.read()
        assert '#557 Type A' in text
