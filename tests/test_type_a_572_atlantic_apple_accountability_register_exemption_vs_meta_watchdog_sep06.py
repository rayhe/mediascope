"""Type A #572 (2026-09-06 20:00 PDT): The Atlantic x Apple accountability-register
exemption vs Meta AI Watchdog targeting - first dedicated mechanism under
competitor_relationships.apple.

The Atlantic (financial tie: DUAL investment + platform revenue - Laurene Powell
Jobs Trust holds ~$17B in Apple stock, owner via Emerson Collective; Apple News+
is "by far the most valuable syndication partner" per chief growth officer
Megha Garibaldi, Digiday; direction mutual; coverage_prediction softer; neither
link ever disclosed in Apple coverage) applies a philosophical design-criticism
and melancholy-review register to Apple, Meta's direct XR-hardware competitor,
while reserving its AI Watchdog accountability-investigation register for Meta.

Apple items: Warzel's Jun 2023 "The Vision Pro Is the Perfect Gadget for the
Apocalypse" (-0.35, dystopian-philosophical essay, "expensive gadget and a
gimmick," "an invitation to narrow our collective aperture"); the Feb 3 2024
"The Apple Vision Pro Is Spectacular and Sad" (-0.25, melancholy first-person
review, zero conduct scrutiny). Historical context: Bogost's Feb 2017 "The Myth
of Apple's Great Design" shows the design-criticism register is a longstanding
Atlantic Apple mode.

Meta comparators (in-corpus): Jul 24 2026 AI Watchdog "Why Would Meta Download
So Much Porn?" (-0.75, Meta named in headline, Strike 3 lawsuit, Celebgate and
GirlsDoPorn file lists, mechanism 481); Mar 25 2025 "The Unbelievable Scale of
AI's Pirated-Books Problem" (-0.65, unsealed Meta internal comms, "MZ"
permission to download LibGen).

Bounded absences (per iteration-492 rule, no zero-coverage claims): no Atlantic
AI Watchdog or equivalent accountability investigation of Apple's AI
training-data practices surfaced in bounded searches; no Atlantic
accountability-register coverage of the May 5 2026 $250M Siri false-advertising
settlement (Landsheft v. Apple, N.D. Cal.) surfaced either.

Scorer (MANUAL ILLUSTRATIVE, standing rule Aug 28 2026; arithmetic only):
Apple target [-0.35, -0.25] avg -0.30 vs Meta peer [-0.75, -0.65] avg -0.70.
Engine target-minus-peer +0.40, delta_manual_illustrative 0.40. THIRD
engine/finding-layer DIVERGENCE (#552 first in #555, #557 second in #560):
the engine claims significance on the synthetic illustrative inputs (Welch
p ~ 0.0299, d = 5.66, is_significant True) while the finding layer refuses
(significant False, p_value NOT_CALCULATED, empirical_required True) -
arithmetic layer vs finding layer separation, pinned deliberately per the
standing rule, not an oversight. p_value NOT_CALCULATED, cohens_d
NOT_CALCULATED, ci_95 NOT_CALCULATED at the finding layer. NOT
artifact-grade: n=2 vs n=2, genre mismatch, secondary verification.

Honesty note (directional support, strongest available setting): the standing
coverage_prediction for Atlantic x Apple was SOFTER, set on the dual financial
tie. Observed is an accountability-register exemption for Apple vs
watchdog-register targeting of Meta, directionally consistent with softer -
the first directional confirmation in the recent control run, against the
falsification family (#552, #557, #562, #567) which stands as the contrasting
pole. The claim is register SELECTION, not tone magnitude: the Apple items are
genuinely adversarial at product level, which is why the genre-mismatch
confounder is STRONG and the verdict is directionally_supported_not_proven.
Strongest confounders: (1) genre mismatch - investigative vs essay/review, the
comparison is about which entity gets the accountability register; (2) genuine
conduct differences - Meta items rest on unsealed court records and filed
lawsuits; (3) timing mismatch - Apple items 2023-2024 vs Meta items 2025-2026;
(4) secondary-source limitation - theatlantic.com direct fetch policy-blocked.

Novelty: first mechanism ever under competitor_relationships.apple in
atlantic.yaml (key previously held only the financial stub). Distinct from
#481 (Atlantic x OpenAI watchdog entity selection) and #404 (Atlantic x
Anthropic mitigation credit). Joins the register-asymmetry strand of #492
(Verge x Google dek-level privacy equivalence vs multi-article escalation).

Evidence hygiene: all URLs carried verbatim from tool output this run or from
in-repo corpus pointers; Warzel URL via artnet secondary quotation, Spectacular
and Sad URL verbatim from GitHub awesome-vision-pro list; Meta URLs from
in-corpus mechanism 481 and the fclawlib mirror; no zero-coverage claims per
iteration-492 rule. No em dashes in any new prose.

Recovery note: the 21:00 run completed the work but its commit never landed;
the mechanism, log entry, and this file were committed in the 22:00 recovery
run, and the rotation guard above was re-anchored to the run's immutable
commit per the #565/#570 followup-anchor convention.
"""

import os
import subprocess
from datetime import datetime

import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = os.path.join(REPO, 'profiles', 'atlantic.yaml')
LOG = os.path.join(REPO, 'iteration-log.md')

MECH_KEY = 'mechanism_572_atlantic_apple_accountability_register_exemption_vs_meta_watchdog'


def _load_profile():
    with open(PROFILE) as f:
        return yaml.safe_load(f)


def _mechanism():
    profile = _load_profile()
    return profile['competitor_relationships']['apple'][MECH_KEY]


class TestMechanismExistsAndShape:
    def test_mechanism_key_present_under_apple(self):
        profile = _load_profile()
        assert MECH_KEY in profile['competitor_relationships']['apple']

    def test_identity_fields(self):
        m = _mechanism()
        assert m['mechanism_id'] == 572
        assert m['iteration'] == 572
        assert m['iteration_type'] == 'A'
        assert m['date_analyzed'] == '2026-09-06'
        assert m['iteration_time'] == '2026-09-06 20:00 PDT'

    def test_publication_pair(self):
        m = _mechanism()
        assert m['publication'] == 'The Atlantic'
        assert m['competitor_pair'] == 'Apple vs Meta'

    def test_type_label(self):
        m = _mechanism()
        assert 'Type A' in m['type']

    def test_goal_and_job_ids(self):
        m = _mechanism()
        assert m['scheduled_job_id'] == 'mediascope-daily-iteration'
        assert m['goal_id'] == 'goal_54093bda4145'

    def test_financial_stub_still_present(self):
        profile = _load_profile()
        apple = profile['competitor_relationships']['apple']
        assert apple['financial_tie'] == 'investment'
        assert apple['coverage_prediction'] == 'softer'
        assert '17B' in apple['estimated_value']
        assert apple['direction'] == 'mutual'


class TestAppleSources:
    def test_two_apple_articles(self):
        m = _mechanism()
        assert len(m['apple_articles']) == 2

    def test_warzel_apocalypse_essay(self):
        m = _mechanism()
        warzel = m['apple_articles'][0]
        assert warzel['author'] == 'Charlie Warzel'
        assert warzel['date'] == '2023-06'
        assert warzel['url'] == ('https://www.theatlantic.com/technology/archive/2023/06/'
                                 'apple-vision-pro-screen-concession-gadget/674375/')
        assert warzel['register'] == 'dystopian_philosophical_essay'
        assert warzel['tone_score'] == -0.35
        assert 'collective aperture' in warzel['key_quote']

    def test_spectacular_and_sad_review(self):
        m = _mechanism()
        review = m['apple_articles'][1]
        assert review['date'] == '2024-02-03'
        assert review['url'] == ('https://www.theatlantic.com/technology/archive/2024/02/'
                                 'apple-vision-pro-headset-review/677347/')
        assert review['register'] == 'melancholy_first_person_review'
        assert review['tone_score'] == -0.25

    def test_apple_items_predate_meta_items(self):
        m = _mechanism()
        apple_dates = [a['date'] for a in m['apple_articles']]
        meta_dates = [a['date'] for a in m['meta_articles']]
        assert max(apple_dates) < min(meta_dates)

    def test_historical_context_bogost(self):
        m = _mechanism()
        ctx = m['historical_context'][0]
        assert ctx['author'] == 'Ian Bogost'
        assert ctx['register'] == 'adversarial_design_criticism'
        assert ctx['secondary_url'] == 'https://kottke.org/17/02/the-myth-of-apples-great-design'


class TestMetaComparators:
    def test_two_meta_articles(self):
        m = _mechanism()
        assert len(m['meta_articles']) == 2

    def test_strike3_watchdog_investigation(self):
        m = _mechanism()
        strike3 = m['meta_articles'][0]
        assert strike3['series'] == 'AI Watchdog'
        assert strike3['date'] == '2026-07-24'
        assert strike3['url'] == ('https://web.archive.org/web/20260724235323/'
                                  'https://www.theatlantic.com/technology/2026/07/'
                                  'meta-strike-3-porn-lawsuit/688023/')
        assert strike3['register'] == 'accountability_investigation_headline_named'
        assert strike3['tone_score'] == -0.75

    def test_libgen_court_records_investigation(self):
        m = _mechanism()
        libgen = m['meta_articles'][1]
        assert libgen['date'] == '2025-03-25'
        assert libgen['url'] == ('https://www.theatlantic.com/technology/archive/2025/03/'
                                 'libgenmetaopenai/682093/')
        assert libgen['register'] == 'accountability_investigation_court_records'
        assert libgen['tone_score'] == -0.65

    def test_meta_registers_are_accountability(self):
        m = _mechanism()
        for a in m['meta_articles']:
            assert a['register'].startswith('accountability_investigation')

    def test_apple_registers_are_not_accountability(self):
        m = _mechanism()
        for a in m['apple_articles']:
            assert not a['register'].startswith('accountability_investigation')


class TestScorerManualIllustrative:
    def test_scores_and_delta_arithmetic(self):
        m = _mechanism()
        sc = m['asymmetry_scoring_manual_illustrative']
        assert sc['target_scores_manual_illustrative'] == [-0.35, -0.25]
        assert sc['peer_scores_manual_illustrative'] == [-0.75, -0.65]
        assert abs(sum(sc['target_scores_manual_illustrative']) / 2
                   - sc['target_avg_manual_illustrative']) < 1e-9
        assert abs(sum(sc['peer_scores_manual_illustrative']) / 2
                   - sc['peer_avg_manual_illustrative']) < 1e-9
        assert abs(sc['delta_manual_illustrative']
                   - (sc['target_avg_manual_illustrative']
                      - sc['peer_avg_manual_illustrative'])) < 1e-9
        assert sc['delta_manual_illustrative'] == 0.40

    def test_delta_direction_target_softer(self):
        m = _mechanism()
        sc = m['asymmetry_scoring_manual_illustrative']
        assert sc['delta_direction'] == 'target softer than peer by 0.40'
        assert sc['delta_manual_illustrative'] > 0

    def test_engine_arithmetic_matches_logged_delta(self):
        from mediascope.score.asymmetry import calculate_asymmetry
        m = _mechanism()
        sc = m['asymmetry_scoring_manual_illustrative']
        r = calculate_asymmetry(
            sc['target_scores_manual_illustrative'],
            sc['peer_scores_manual_illustrative'],
            'Apple', ['Meta'], 'atlantic',
            datetime(2023, 6, 1), datetime(2026, 9, 6))
        assert abs(r.asymmetry_score - sc['delta_manual_illustrative']) < 1e-4
        assert abs(r.target_avg_tone
                   - sc['target_avg_manual_illustrative']) < 1e-4
        assert abs(r.peer_avg_tone
                   - sc['peer_avg_manual_illustrative']) < 1e-4

    def test_third_divergence_engine_claims_significance(self):
        # Divergence ratchet: engine claims significance on the synthetic
        # illustrative inputs while the finding layer refuses. #552 was the
        # first (p ~ 0.00023), #557 the second (p ~ 0.0047); this is the
        # third. Engine-implementation coupling caveat: if the engine's test
        # statistic changes, the magic p-value pin needs review.
        from mediascope.score.asymmetry import calculate_asymmetry
        m = _mechanism()
        sc = m['asymmetry_scoring_manual_illustrative']
        r = calculate_asymmetry(
            sc['target_scores_manual_illustrative'],
            sc['peer_scores_manual_illustrative'],
            'Apple', ['Meta'], 'atlantic',
            datetime(2023, 6, 1), datetime(2026, 9, 6))
        assert r.is_significant is True
        assert abs(r.p_value - 0.0298574998546681) < 1e-6
        assert sc['engine_divergence'] is True
        assert sc['engine_is_significant'] is True
        assert sc['empirical_required'] is True

    def test_no_empirical_significance_claim(self):
        m = _mechanism()
        sc = m['asymmetry_scoring_manual_illustrative']
        assert sc['p_value'] == 'NOT CALCULATED no observed corpus'
        assert sc['cohens_d'] == 'NOT CALCULATED'
        assert sc['ci_95'] == 'NOT CALCULATED'
        assert sc['significant'] is False
        assert 'MANUAL ILLUSTRATIVE' in sc['note']
        assert sc['engine_divergence'] is True
        assert sc['empirical_required'] is True
        assert 'divergence' in sc['divergence_note'].lower()
        assert sc['artifact_grade'] is False


class TestHonestyDirectionalSupport:
    def test_standing_prediction_softer(self):
        m = _mechanism()
        assert m['prediction_test']['standing_prediction'] == 'softer'

    def test_verdict_directional_not_proven(self):
        m = _mechanism()
        assert m['prediction_test']['verdict'] == 'directionally_supported_not_proven'

    def test_genre_mismatch_is_strong_confounder(self):
        m = _mechanism()
        strong = ' '.join(m['confounders_ranked']['strong'])
        assert 'genre mismatch' in strong

    def test_register_selection_framed_not_tone_magnitude(self):
        m = _mechanism()
        strong = ' '.join(m['confounders_ranked']['strong'])
        assert 'register SELECTION' in strong

    def test_bounded_absence_no_zero_claims(self):
        m = _mechanism()
        summary = m['discovery_summary']
        assert 'bounded by search-index visibility' in summary
        assert 'ZERO' not in summary

    def test_correlation_not_causation(self):
        m = _mechanism()
        assert m['correlation_not_causation'] is True
        assert 'Correlation only' in m['cautious_language']


class TestReferences:
    def test_source_urls_all_https_and_nonempty(self):
        m = _mechanism()
        urls = [a['url'] for a in m['apple_articles'] + m['meta_articles']]
        urls += [a['secondary_url'] for a in m['apple_articles']
                 if 'secondary_url' in a]
        urls += [a['secondary_url'] for a in m['meta_articles']
                 if 'secondary_url' in a]
        urls.append(m['historical_context'][0]['secondary_url'])
        assert len(urls) >= 7
        for u in urls:
            assert u.startswith('https://'), u
            assert len(u) > 20

    def test_no_em_dashes_in_prose_fields(self):
        import json
        m = _mechanism()
        blob = json.dumps(m)
        assert '\u2014' not in blob

    def test_cross_references_include_key_mechanisms(self):
        m = _mechanism()
        for ref in (481, 404, 16, 193):
            assert ref in m['cross_references']

    def test_cautious_language_flags(self):
        m = _mechanism()
        assert m['no_em_dash_verified'] is True
        assert m['research_date'] == '2026-09-06 UTC'


class TestIterationLogAndNovelty:
    def test_iteration_log_entry_present(self):
        with open(LOG) as f:
            text = f.read()
        assert '#572 Type A' in text

    def test_no_duplicate_572_mechanism_keys(self):
        profile = _load_profile()
        count = sum(1 for k in
                    profile['competitor_relationships']['apple']
                    if '572' in k)
        assert count == 1

    def test_rotation_guard_anchored_at_572_commit(self):
        # Anchored-commit convention (established by Type D #565's repair
        # of #560's guard, followed by #570's followup anchored at 382abc3):
        # the guard pins the rotation window as of THIS run's commit
        # (immutable), not HEAD - a HEAD-relative assertion decays every
        # hour as new runs land. The ANCHORED hash is a placeholder until
        # the main commit exists; it is patched to the real hash in the
        # followup commit, and this guard is excluded from the pre-commit
        # run, verified green post-commit.
        anchored = "e10400d"
        subjects = subprocess.run(
            ['git', 'log', '--format=%H %s', anchored],
            capture_output=True, text=True, cwd=REPO,
            check=True).stdout.splitlines()
        assert subjects, 'anchored commit not found in history'
        head_hash, head_subject = subjects[0].split(' ', 1)
        assert head_hash.startswith(anchored), \
            'anchor does not resolve to this run commit'
        assert 'Type A #572' in head_subject
        parent_subject = subprocess.run(
            ['git', 'log', '-1', '--format=%s', anchored + '^'],
            capture_output=True, text=True, cwd=REPO,
            check=True).stdout
        assert 'Type E #571' in parent_subject
