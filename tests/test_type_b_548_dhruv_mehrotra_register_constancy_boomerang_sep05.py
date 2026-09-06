"""Type B #548 (2026-09-05 20:00 PDT): Dhruv Mehrotra Bloomberg-boomerang
register-constancy test - WIRED investigative data reporter.

Career arc: WIRED first stint (JD Vance Venmo, Epstein island phone tracking,
ShotSpotter, Neuralink monkeys) -> Bloomberg (Epstein's Inbox data work,
Sep 2025, 18,000 emails) -> returned to WIRED May 18, 2026 (Editor and
Publisher announcement: https://www.editorandpublisher.com/stories/dhruv-mehrotra-is-welcomed-back-to-wired,261589;
verified Monday via date -d).

WIRED-return Meta pieces (4, all data-forensics adversarial):
1. NameTag exposé Jun 4 2026 (Cameron + Mehrotra)
   https://www.wired.com/story/meta-smart-glasses-face-recognition-nametag-connections/
   tone -0.75
2. NameTag removal follow-up Jun 5 2026 (Mehrotra + Cameron), -0.70
   (secondary-attested via repo sample_output wearables_advocacy_coalition_analysis_2026_jul.md)
3. Rank One Pentagon-contractor face-recognition follow-up, Jun 2026
   (Cameron + Mehrotra), -0.75
   (secondary-attested: https://thetechstreetnow.com/meta-face-recognition-for-its-glasses-came-from-a-pentagon-contractor-wired-reports/)
4. Project Cannes Jun 29 2026 (Khalili + Mehrotra): Meta contractors posed
   as minors to test rival AI chatbots (ChatGPT, Gemini, Character.AI),
   -0.80 (repo commit f4c52c7400f8a297fc90d21f4a9ca3e229904034)

Non-Meta adversarial-forensics baseline (3):
1. Epstein's Island Visitors Exposed by Data Broker (WIRED, first stint), -0.80
2. They're Not Breathing: ICE Detention Center 911 Calls (WIRED), -0.80
3. Epstein's Inbox: 18,000 emails (Bloomberg, Sep 2025), -0.75
   (all attested via https://www.404media.co/the-journalist-who-tracked-epstein-island-visitors-phones-with-dhruv-mehrotra/)

Scorer (MANUAL ILLUSTRATIVE, standing rule Aug 28 2026; arithmetic only):
Meta [-0.75, -0.70, -0.75, -0.80] avg -0.75 vs non-Meta [-0.80, -0.80, -0.75]
avg -0.783. Delta (Meta minus non-Meta) +0.033. p_value NOT_CALCULATED,
is_significant False, artifact-grade False.

Interpretation (falsification family, extends #66 rather than duplicates;
distinct from #366 which covered Cameron): Mehrotra's adversarial
data-forensics register is constant across targets and employers. The Meta
concentration at WIRED is beat-assignment (investigations desk routes Meta
probes to him), not individual entity-targeting. Falsifies the reporter-level
bias hypothesis for Mehrotra, consistent with the #457 Adrienne So and
#493 Fowler company-agnostic precedents.

Strongest counterargument: the Meta concentration could still reflect
institutional targeting filtered through a beat - WIRED assigns Mehrotra Meta
investigations because Meta is the standing surveillance-beat target, and his
uniform register is compatible with both company-agnostic forensics AND
assignment-driven Meta focus. The constancy finding rules out personal entity
animus only, not institutional selection. MANUAL ILLUSTRATIVE, correlation-only.

Evidence hygiene: URLs carried verbatim from tool output this run; no
wired.com URLs constructed for the 404-Media-attested baseline pieces (none
returned verbatim); truncated wired.com URLs from search snippets were NOT
used. No em dashes in any new prose.

Novelty (per durable rule): zero dhruv_mehrotra keys in journalist_cross_entity_coverage
before this run (grep verified); no #548 in git log --grep; mechanism 66 is
team-level (Cameron/Mehrotra pair) and 366 is Cameron-only, so an individual
Mehrotra register-constancy mechanism is distinct; stated explicitly in the
YAML distinguishes_from field.
"""

import os
import re

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = os.path.join(REPO, 'profiles', 'wired.yaml')
LOG = os.path.join(REPO, 'iteration-log.md')


def _load_profile():
    with open(PROFILE) as f:
        return yaml.safe_load(f)


def _mechanism():
    profile = _load_profile()
    return profile['journalist_cross_entity_coverage']['dhruv_mehrotra']


def _mechanism_block_text():
    with open(PROFILE) as f:
        text = f.read()
    start = text.index('  dhruv_mehrotra:')
    end = text.index('\n  wired_openai_rogue_swarm_aug26_followup_silence:', start)
    return text[start:end]


class TestMechanismExistsAndShape:
    def test_mechanism_key_present(self):
        profile = _load_profile()
        assert 'dhruv_mehrotra' in profile['journalist_cross_entity_coverage']

    def test_identity_fields(self):
        m = _mechanism()
        assert m['mechanism_id'] == 548
        assert m['iteration'] == 548
        assert m['type'].startswith('Type B')
        assert m['journalist'] == 'Dhruv Mehrotra'
        assert m['date_analyzed'] == '2026-09-05'

    def test_finding_type_and_extension(self):
        m = _mechanism()
        assert m['finding_type'] == 'journalist_cross_entity_register_constancy_falsification'
        assert m['extends_mechanism'] == 66

    def test_distinguishes_from_prior(self):
        m = _mechanism()
        blob = ' '.join(m['distinguishes_from'])
        assert 'mechanism 66' in blob
        assert 'mechanism 366' in blob
        assert 'individual-level' in blob

    def test_author_kit_with_ray(self):
        assert _mechanism()['author'] == 'Kit (with Ray)'


class TestCareerTimeline:
    def test_wired_return_date_and_source(self):
        m = _mechanism()
        assert m['career_timeline']['wired_return'] == '2026-05-18'
        src = m['career_timeline']['return_source']
        assert src.startswith('https://www.editorandpublisher.com/stories/dhruv-mehrotra-is-welcomed-back-to-wired')

    def test_bloomberg_stint_recorded(self):
        m = _mechanism()
        stint = m['career_timeline']['bloomberg_stint']
        assert 'Epstein' in stint
        assert '18,000' in stint


class TestCorpusComparators:
    def test_four_meta_pieces(self):
        m = _mechanism()
        assert len(m['meta_pieces_wired_return']) == 4

    def test_nametag_piece_direct_url(self):
        m = _mechanism()
        nt = [p for p in m['meta_pieces_wired_return'] if 'NameTag' in p['title']]
        assert len(nt) == 1
        assert nt[0]['url'] == 'https://www.wired.com/story/meta-smart-glasses-face-recognition-nametag-connections/'
        assert 'Dhruv Mehrotra' in nt[0]['authors']
        assert nt[0]['register'] == 'data_forensics_adversarial'

    def test_project_cannes_piece(self):
        m = _mechanism()
        pc = [p for p in m['meta_pieces_wired_return'] if 'Project Cannes' in p['title']]
        assert len(pc) == 1
        assert 'Joel Khalili' in pc[0]['authors']
        assert 'Dhruv Mehrotra' in pc[0]['authors']

    def test_three_non_meta_baseline(self):
        m = _mechanism()
        assert len(m['non_meta_adversarial_forensics_baseline']) == 3
        pubs = {b['publication'] for b in m['non_meta_adversarial_forensics_baseline']}
        assert pubs == {'wired', 'bloomberg'}

    def test_baseline_sources_verbatim(self):
        m = _mechanism()
        for b in m['non_meta_adversarial_forensics_baseline']:
            assert b['source_url'] == 'https://www.404media.co/the-journalist-who-tracked-epstein-island-visitors-phones-with-dhruv-mehrotra/'

    def test_all_registers_identical(self):
        m = _mechanism()
        regs = [p['register'] for p in m['meta_pieces_wired_return']]
        regs += [b['register'] for b in m['non_meta_adversarial_forensics_baseline']]
        assert set(regs) == {'data_forensics_adversarial'}


class TestScorer:
    def test_arrays(self):
        r = _mechanism()['asymmetry_scorer_result']
        assert r['target_entity'] == 'meta'
        assert r['target_tones_manual_illustrative'] == [-0.75, -0.70, -0.75, -0.80]
        assert r['reference_tones_manual_illustrative'] == [-0.80, -0.80, -0.75]

    def test_arithmetic(self):
        r = _mechanism()['asymmetry_scorer_result']
        assert abs(r['target_avg'] - (-0.75)) < 1e-9
        assert abs(r['reference_avg'] - (-0.783)) < 0.001
        assert abs(r['delta_meta_minus_non_meta'] - 0.033) < 0.001
        assert r['interpretation'] == 'near_zero_constancy_not_asymmetry'

    def test_manual_illustrative_guards(self):
        r = _mechanism()['asymmetry_scorer_result']
        assert r['p_value'] == 'NOT_CALCULATED'
        assert r['cohens_d'] == 'NOT_CALCULATED'
        assert r['ci'] == 'NOT_CALCULATED'
        assert r['is_significant'] is False
        assert r['artifact_grade'] is False

    def test_limitations_stated(self):
        r = _mechanism()['asymmetry_scorer_result']
        assert 'n=4 vs n=3' in r['limitations']


class TestConfoundersAndCounterargument:
    def test_confounders_present_and_ranked(self):
        m = _mechanism()
        confs = m['confounders']
        assert len(confs) >= 5
        assert confs[0]['strength'] == 'STRONG'
        blob = ' '.join(c['text'] for c in confs)
        assert 'Co-byline dilution' in blob
        assert 'Beat assignment' in blob

    def test_strongest_counterargument_beat_filtering(self):
        ca = _mechanism()['strongest_counterargument']
        assert 'institutional' in ca
        assert 'MANUAL ILLUSTRATIVE' in ca
        assert 'correlation-only' in ca

    def test_financial_context_correlation_only(self):
        fc = _mechanism()['financial_context']
        assert '$5-10M' in fc
        assert '$0 from Meta' in fc
        assert 'does not imply causation' in fc


class TestNoEmDashes:
    def test_no_em_dashes_in_block(self):
        assert '—' not in _mechanism_block_text()


class TestIterationLog:
    def test_log_entry_present(self):
        with open(LOG) as f:
            text = f.read()
        assert '#548' in text
        assert 'Type B' in text

    def test_log_entry_relative_order(self):
        with open(LOG) as f:
            text = f.read()
        m547 = re.search(r'^#547\b', text, re.MULTILINE)
        m548 = re.search(r'^#548\b', text, re.MULTILINE)
        assert m548 is not None and m547 is not None
        assert m548.start() < m547.start()

    def test_log_entry_content(self):
        with open(LOG) as f:
            text = f.read()
        start = text.index('#548 Type B')
        end = text.index('#547 Type A')
        block = text[start:end]
        assert 'Mehrotra' in block
        assert '+0.033' in block
        assert 'NOT artifact-grade' in block
