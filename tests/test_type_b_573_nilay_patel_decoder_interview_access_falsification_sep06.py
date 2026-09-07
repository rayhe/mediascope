"""Type B #573 (2026-09-06 22:00 PDT): Nilay Patel (The Verge) Decoder
CEO-interview entity selection - deal-partner OpenAI gets no sit-down plus
adversarial third-party register, while non-partner Meta gets recurring
product-forward CEO sit-downs. Vox-OpenAI deal falsification at the
interview-access layer.

Mechanism: on Decoder, The Verge's flagship interview show, Meta CEO Mark
Zuckerberg gets recurring product-forward sit-downs (Oct 2022 Quest Pro,
Sep 2023 Quest 3/Threads, Sep 2024 Orion/"end the smartphone era"), always
guest-hosted by Meta-beat deputy editor Alex Heath. Deal-partner OpenAI's
CEO has no Decoder sit-down in the bounded window (bounded absence per the
iteration-492 rule: no surfaced sit-down, no claim about invitation or
refusal); OpenAI is instead covered through adversarial third-party
episodes, all POST-dating the May 29 2024 Vox Media x OpenAI strategic
content and product partnership (in-corpus mechanism #494): Apr 2026 Ronan
Farrow on "Sam Altman's strained relationship with the truth" (thesis "Sam
unconstrained by truth"), Jul 27 2026 "What Apple's OpenAI lawsuit is
really about" ("already-damaged reputation"), Aug 27 2026 "OpenAI's
executive exodus has one big winner" (Brockman power consolidation).
Anthropic, with no Vox deal, got an aspirational executive sit-down (CPO
Mike Krieger, 2024, "wants to build AI products that are worth the hype").

The naive prediction from the Vox-OpenAI deal is softer OpenAI treatment on
the owner's flagship interview show. Observed is the reverse: the deal
partner absorbs the adversarial register while the $0-deal Meta CEO gets
the recurring sit-down. The softer prediction is FALSIFIED, joining the
falsification family (#552, #557, #562, #567 recent Type A; #457, #471,
#472, #492, #493, #498 older). Distinct from #498 (Swisher's personal
adversarial register, uniform across entities) and from mechanism #6 (the
EIC Delegation Paradox: Patel personally interviews Google/Microsoft CEOs
constructively while delegating Zuck to Heath) - this is interview-ACCESS
entity selection, a different layer of the same show.

Scorer (MANUAL ILLUSTRATIVE, standing rule Aug 28 2026; arithmetic only):
OpenAI target [-0.70, -0.60, -0.45] avg -0.5833 vs Meta peer [-0.20, -0.15,
-0.15] avg -0.1667. Engine target-minus-peer -0.4167,
delta_manual_illustrative -0.4167. FOURTH engine/finding-layer DIVERGENCE
(#552 first in #555, #557 second in #560, #572 third in #572): the engine
claims significance on the synthetic illustrative inputs (Welch p ~
0.0243, d = -4.56, is_significant True) while the finding layer refuses
(significant False, p_value NOT_CALCULATED, empirical_required True).
p_value NOT_CALCULATED, cohens_d NOT_CALCULATED, ci_95 NOT_CALCULATED at
the finding layer. NOT artifact-grade: n=3 vs n=3, host mismatch (Heath vs
Patel/Field), secondary-source descriptions, genre mismatch (sit-downs vs
third-party accountability episodes).

Novelty: first competitor_coverage block on the Nilay Patel journalists.yaml
entry (parsed-verified absent before this run). The Farrow-episode YouTube
URL was previously cited only as a source line in mechanism #6's docstring;
no scored OpenAI episode set, no deal-falsification verdict, and no
interview-access entity-selection mechanism existed for Patel/Decoder.

Evidence hygiene: all URLs carried verbatim from this run's browser.search
Full-URL listings; episode descriptions from podcast-listing pages (secondary
sources, flagged as a STRONG confounder); no zero-coverage claims per the
iteration-492 rule; no em dashes in any new prose.
"""

import os
import subprocess
from datetime import datetime

import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOURNALISTS = os.path.join(REPO, 'profiles', 'careers', 'journalists.yaml')
LOG = os.path.join(REPO, 'iteration-log.md')

OPENAI_SCORES = [-0.70, -0.60, -0.45]
META_SCORES = [-0.20, -0.15, -0.15]

OPENAI_URLS = [
    'https://www.youtube.com/watch?v=TfN5ket9L8Q',
    'https://www.goloudnow.com/podcasts/decoder-with-nilay-patel-385/ai-will-make-money-sooner-than-you-think-says-cohere-ceo-aidan-gomez-473167',
    'http://au.radio.net/podcast/recodedecode',
]
META_URLS = [
    'https://www.everand.com/podcast/773063094/Why-Mark-Zuckerberg-wants-to-end-the-smartphone-era-The-Meta-CEO-wants-to-get-into-AR-and-out-of-politics',
    'https://www.everand.com/podcast/674090997/Mark-Zuckerberg-on-Threads-the-future-of-AI-and-Quest-3-The-Meta-CEO-sits-down-with-Decoder-guest-host-Alex-Heath-to-discuss-the-future-of-AI-the',
    'https://www.podchaser.com/podcasts/decoder-with-nilay-patel-100800/episodes/mark-zuckerberg-on-the-quest-p-152263701',
]


def _patel():
    with open(JOURNALISTS) as f:
        data = yaml.safe_load(f)
    for j in data['journalists']:
        if j.get('name') == 'Nilay Patel':
            return j
    raise AssertionError('Nilay Patel entry missing')


def _mechanism():
    return _patel()['competitor_coverage']['cross_entity_analysis']


class TestMechanismExistsAndShape:
    def test_competitor_coverage_block_present(self):
        assert 'competitor_coverage' in _patel()

    def test_identity_fields(self):
        m = _mechanism()
        assert m['mechanism_id'] == 573
        assert m['iteration'] == 573
        assert m['journalist'] == 'Nilay Patel'
        assert m['publication'] == 'the-verge'
        assert m['date'] == '2026-09-06'

    def test_pattern_field(self):
        m = _mechanism()
        assert m['pattern'] == 'interview_access_entity_selection_deal_falsification'

    def test_first_block_on_patel_entry(self):
        cc = _patel()['competitor_coverage']
        assert 'cross_entity_analysis' in cc

    def test_role_at_window(self):
        m = _mechanism()
        assert m['role_at_window'] == 'editor_in_chief'


class TestEpisodeEvidence:
    def test_openai_item_count_and_scores(self):
        m = _mechanism()
        items = m['openai_items']
        assert len(items) == 3
        assert [i['tone_manual_illustrative'] for i in items] == OPENAI_SCORES

    def test_openai_urls_verbatim(self):
        m = _mechanism()
        urls = [i['source_url'] for i in m['openai_items']]
        assert urls == OPENAI_URLS

    def test_openai_farrow_episode_framing(self):
        m = _mechanism()
        farrow = m['openai_items'][0]
        assert 'Farrow' in farrow['title']
        assert 'strained relationship with the truth' in farrow['framing']

    def test_openai_episodes_postdate_vox_deal(self):
        m = _mechanism()
        for i in m['openai_items']:
            assert i['date'] > '2024-05-29', 'episode must post-date the Vox-OpenAI deal'

    def test_meta_item_count_and_scores(self):
        m = _mechanism()
        items = m['meta_items']
        assert len(items) == 3
        assert [i['tone_manual_illustrative'] for i in items] == META_SCORES

    def test_meta_urls_verbatim(self):
        m = _mechanism()
        urls = [i['source_url'] for i in m['meta_items']]
        assert urls == META_URLS

    def test_meta_sitdowns_guest_hosted_by_heath(self):
        m = _mechanism()
        for i in m['meta_items']:
            assert i['host'] == 'Alex Heath (guest host)', \
                'Zuckerberg Decoder sit-downs are Heath-hosted, not Patel-hosted'

    def test_anthropic_calibration_krieger_sitdown(self):
        m = _mechanism()
        cal = m['anthropic_calibration']
        assert 'Krieger' in cal['title']
        assert cal['framing'] == 'aspirational_executive_sitdown'
        assert 'zeno.fm' in cal['source_url']


class TestScorerArithmetic:
    def test_engine_reproduces_delta(self):
        from mediascope.score.asymmetry import calculate_asymmetry
        m = _mechanism()
        sc = m['scorer']
        r = calculate_asymmetry(
            sc['target_scores'], sc['peer_scores'],
            'OpenAI', ['Meta'], 'the-verge',
            datetime(2022, 10, 1), datetime(2026, 9, 6))
        assert abs(r.asymmetry_score - sc['delta_manual_illustrative']) < 1e-4
        assert abs(r.asymmetry_score - (-0.4167)) < 1e-4

    def test_engine_reproduces_avgs(self):
        from mediascope.score.asymmetry import calculate_asymmetry
        m = _mechanism()
        sc = m['scorer']
        r = calculate_asymmetry(
            sc['target_scores'], sc['peer_scores'],
            'OpenAI', ['Meta'], 'the-verge',
            datetime(2022, 10, 1), datetime(2026, 9, 6))
        assert abs(r.target_avg_tone - (-0.5833)) < 1e-4
        assert abs(r.peer_avg_tone - (-0.1667)) < 1e-4

    def test_yaml_arrays_byte_matched(self):
        m = _mechanism()
        sc = m['scorer']
        assert sc['target_scores'] == OPENAI_SCORES
        assert sc['peer_scores'] == META_SCORES

    def test_target_is_openai_deal_partner(self):
        m = _mechanism()
        assert m['scorer']['target_entity'] == 'openai'
        assert m['scorer']['peer_entities'] == ['meta']

    def test_delta_direction_target_harsher(self):
        m = _mechanism()
        assert m['scorer']['delta_direction'] == 'target harsher than peer by 0.42'


class TestFourthDivergence:
    def test_engine_claims_significance(self):
        from mediascope.score.asymmetry import calculate_asymmetry
        m = _mechanism()
        sc = m['scorer']
        r = calculate_asymmetry(
            sc['target_scores'], sc['peer_scores'],
            'OpenAI', ['Meta'], 'the-verge',
            datetime(2022, 10, 1), datetime(2026, 9, 6))
        assert r.is_significant is True
        assert abs(r.p_value - 0.0243) < 1e-3
        assert sc['engine_check']['is_significant'] is True

    def test_finding_layer_refuses(self):
        m = _mechanism()
        sc = m['scorer']
        assert sc['is_significant'] is False
        assert sc['p_value'] == 'NOT_CALCULATED'
        assert sc['cohens_d'] == 'NOT_CALCULATED'
        assert sc['ci_95'] == 'NOT_CALCULATED'

    def test_fourth_divergence_pinned(self):
        m = _mechanism()
        sc = m['scorer']
        assert sc['engine_check']['divergence'] == 'fourth engine/finding divergence'
        assert sc['artifact_grade'] is False

    def test_divergence_note_names_lineage(self):
        m = _mechanism()
        note = m['scorer']['divergence_note']
        assert '#552' in note and '#557' in note and '#572' in note


class TestFalsificationFamily:
    def test_softer_prediction_falsified(self):
        m = _mechanism()
        assert m['verdict'] == 'falsified_softer_prediction'

    def test_vox_deal_in_financial_context(self):
        m = _mechanism()
        fc = m['financial_context']
        assert '2024-05-29' in fc or 'May 29 2024' in fc
        assert 'mechanism #494' in fc

    def test_distinct_from_498_swisher(self):
        m = _mechanism()
        refs = m['cross_references']
        assert 498 in refs
        assert 'Swisher' in m['distinction_from_498']

    def test_distinct_from_mechanism_6(self):
        m = _mechanism()
        assert 'echanism #6' in m['distinction_from_mechanism_6']

    def test_falsification_family_refs(self):
        m = _mechanism()
        refs = m['cross_references']
        for n in (552, 557, 562, 567):
            assert n in refs


class TestIterationLogAndNovelty:
    def test_iteration_log_entry_present(self):
        with open(LOG) as f:
            text = f.read()
        assert '#573 Type B' in text

    def test_no_duplicate_573_mechanism_keys(self):
        count = sum(1 for k in
                    _patel()['competitor_coverage']['cross_entity_analysis']
                    if '573' in str(k))
        assert count <= 1

    def test_rotation_guard_anchored_at_573_commit(self):
        # Anchored-commit convention (#565 -> bd7f2fd, #570 -> 382abc3,
        # #572 -> e10400d): the guard pins the rotation window as of THIS
        # run's commit (immutable), not HEAD. The ANCHORED hash is a
        # placeholder until the main commit exists; patched to the real
        # hash in the followup commit; excluded from the pre-commit run,
        # verified green post-commit.
        anchored = "POST_COMMIT_ANCHOR"
        subjects = subprocess.run(
            ['git', 'log', '--format=%H %s', anchored],
            capture_output=True, text=True, cwd=REPO,
            check=True).stdout.splitlines()
        assert subjects, 'anchored commit not found in history'
        head_hash, head_subject = subjects[0].split(' ', 1)
        assert head_hash.startswith(anchored)
        assert 'Type B #573' in head_subject
        parent_subject = subprocess.run(
            ['git', 'log', '-1', '--format=%s', anchored + '^'],
            capture_output=True, text=True, cwd=REPO,
            check=True).stdout
        assert 'Type A #572' in parent_subject

    def test_ascii_clean(self):
        with open(os.path.join(REPO, 'profiles', 'careers',
                               'journalists.yaml'), encoding='utf-8') as f:
            blob = f.read()
        assert '\u2014' not in blob and '\u2013' not in blob
