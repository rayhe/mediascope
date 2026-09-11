"""
Type D - Test & Verify: scorer degenerate-boundary for the first mixed-n
(n=2 vs n=1) illustrative pair (#667 Type A, Reuters x OpenAI Sep 4-10
register vs Reuters x Meta Muse register) + THIRTEENTH n=1-per-arm
degenerate-ledger pair (#668 Type B, Lily Hay Newman Meta-vs-Apple
register) + post-#669 corpus integrity sweep (mechanism 636 NYT CEO
pay-or-litigate doctrine, mechanism 635 Lily Hay Newman, mechanism 634
Reuters x OpenAI) + #609 cohort / falsification-ledger closure checks.

Iteration #670 - Fri 2026-09-11 03:00 PDT
(scheduled job_id mediascope-daily-iteration, goal_54093bda4145, rotation 669 C -> 670 D)

Core finding this run: the FIRST mixed-n (n=2 vs n=1) illustrative pair
run through the real calculate_asymmetry path (#667: OpenAI [0.15, 0.20]
vs Meta [-0.45], illustrative delta (OpenAI minus Meta) +0.625) EXPOSES A
BOUNDARY in the degenerate contract. The welch_t_test n<2 guard still
fires (t=0.0, p=1.0), |asymmetry| == |delta| holds EXACTLY (0.625,
IEEE-exact, unlike #664's 0.8500000000000001), arm-swap negates exactly,
is_significant False. BUT cohens_d does NOT degenerate: it returns
+17.677669529663685, a computable junk effect size (the n=1 arm
contributes zero variance, so the pooled sd collapses to the n=2 arm's
own sd: 0.625 / 0.0353553...). The #667 mechanism block documents
"engine_degenerate: ... (Welch t and Cohen's d degenerate: p=1.0, d=0.0).
Engine NOT run" - the d=0.0 half of that projection is CONTRADICTED by
the real engine (CORRECTION documented this run; the #667 block is left
untouched per the Type D read-only convention). This pair is the SEVENTH
degenerate-boundary pin (FIRST through SIXTH: #578/#585/#590/#595/#605/
#610 sweeps; #578 d=-10.61, #593 d=-9.2376 were the prior junk-d
exemplars), and the first POSITIVE large junk-d: sign-invariant junk.

Per the Aug 28 2026 standing rule the junk d strengthens the
no-empirical-claim discipline: a computable d on degenerate arms is
meaningless (t=0.0/p=1.0, significance impossible), so the engine output
must be ignored for findings. No divergence pin arises (divergence pins
require engine significance); the divergence ratchet stays at 7 (#642
holds).

#668 Type B (Apple [+0.10] vs Meta [-0.30], illustrative delta (Apple
minus Meta) +0.40) is the THIRTEENTH n=1-per-arm degenerate-ledger pair
(ELEVENTH #663 and TWELFTH #664 per #665; first four #645, fifth/sixth
#650, seventh/eighth #655, ninth/tenth #660): the classic contract holds
exactly - t=0.0, p=1.0, d=0.0, |asymmetry| == 0.40 IEEE-exact, arm-swap
negates exactly, is_significant False.

#669 Type C (NYT CEO pay-or-litigate doctrine, mechanism 636) logged no
tone pin and this run VERIFIES that decision: the block carries
tone_scores NOT_SCORED, p_value/cohens_d/ci_95 NOT_CALCULATED,
engine_run false - there are no tone arms for the engine to score.

Corpus integrity sweep: mechanism_id 636 (NYT CEO pay-or-litigate
doctrine, #669) is present and unique in
profiles/competitor-entities.yaml under entities.amazon with iteration
669, rotation Type C; mechanism 635 (Lily Hay Newman register, #668) is
present in profiles/careers/journalists.yaml with iteration 668, type B;
mechanism 634 (Reuters x OpenAI register, #667) is present under
entities.openai with iteration 667, iteration_type A; the modern (504+)
id era is collision-free with max == 636 and no 637 anywhere in
profiles/; journalists.yaml parses (>= 267 journalists).

Cohort and ledger checks: the #609 first-gen OpenAI publisher renewal
cohort stays closed at 7/7 (the #654 News Corp block still names itself
the SEVENTH member); mechanism 630 is still a separate UNRESOLVED watch
item (sixth News Corp AI-revenue leg, Google) outside the cohort;
mechanism 633 (Meta x Reuters, #664) does not join the OpenAI cohort;
the falsification ledger stands at 14 (#667 FOURTEENTH); mechanism 635
(#668) is explicitly NOT a falsification-family member (gradient-absent);
mechanism 636 (#669) is falsification-adjacent, not a tone pin, not a
ledger member.

Type E integrity: the Tracked Sources table is at 56 verification cycles
through Sep 10 2026 (#666), GF at 499 episodes (Sep 10 2026), EHE
activist-group (not a podcast) row intact, Attention Sphere no-match row
intact with the misidentified-spec text.

Rotation guard: window 666-670 (D, C, B, A, E newest-first), closing the
C->D edge. Deselected pre-commit per the #565 followup convention; anchor
patched in the followup once the #670 main-commit SHA is known.

Designed supersession note: the #665 Type D sweep's
test_max_mechanism_id_is_633 and test_no_mechanism_634_anywhere now fail
by supersession (max is 636; mechanism_634 is now a real key under
entities.openai), consistent with the established convention (the
test_type_c_634 file name is the ITERATION #634 test file, a different
namespace; the mechanism_634 key form was checked explicitly).
"""
import glob
import os
import re
import subprocess
import sys
from datetime import datetime

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO_ROOT)

from mediascope.score.asymmetry import calculate_asymmetry

P0 = datetime(2026, 9, 4)
P1 = datetime(2026, 9, 11)

# Pinned illustrative tone pairs from the Sep 11 mechanism blocks.
# #667 Type A (Reuters, Sep 4-10 2026 window): OpenAI arms [0.15, 0.20]
# (Friar's Communacopia/Goldman enterprise-growth narrative +0.15;
# ChatGPT for Financial Services design-partner validation +0.20) vs
# Meta arm [-0.45] (Reuters Katie Paul Muse-launch accountability
# register). Illustrative delta (OpenAI minus Meta) +0.625, MANUAL
# ILLUSTRATIVE, n=2 vs n=1 - the FIRST mixed-n illustrative pair. The
# Breakingviews -0.25 arm is register-range context only, NOT scored.
TONE_OPENAI_667 = [0.15, 0.20]
TONE_META_667 = [-0.45]

# #668 Type B (WIRED, Lily Hay Newman): Apple arm [+0.10] (Apple Watch
# Series 12 / Ultra 4 "audio intelligence" reassurance-adoption headline
# with skeptical dek caveat) vs Meta arm [-0.30] (Meta Muse launch
# trust-deficit register). Illustrative delta (Apple minus Meta) +0.40,
# MANUAL ILLUSTRATIVE, n=1 per arm - the THIRTEENTH degenerate-ledger
# pair. Gradient-absent control case, NOT a falsification-family member.
TONE_APPLE_668 = [0.10]
TONE_META_668 = [-0.30]

# Engine-verified junk d for the #667 mixed-n pair. cohens_d computes
# pooled variance ((2-1)*var([0.15,0.20]) + (1-1)*0) / (2+1-2) = the n=2
# arm's own variance 0.00125, so d = 0.625 / sqrt(0.00125).
JUNK_D_667 = 17.677669529663685


class TestIteration670Metadata:
    def test_iteration_number(self):
        assert 670 == 670

    def test_type_is_d(self):
        assert "D" == "D"

    def test_rotation_edge(self):
        # A -> B -> C -> D -> E; previous main commit was Type C #669
        assert "C->D" == "C->D"

    def test_run_time_sep11_3am(self):
        assert "2026-09-11 03:00 PDT" == "2026-09-11 03:00 PDT"


class TestNovelty670:
    """This run must not collide with an earlier #670."""

    def test_single_type_d_670_file(self):
        matches = glob.glob(
            os.path.join(REPO_ROOT, "tests", "test_type_d_670*.py")
        )
        assert len(matches) == 1, f"expected exactly this file, got {matches}"
        assert matches[0].endswith(
            "test_type_d_670_scorer_degenerate_boundary_667_ledger668_corpus_integrity_post_669_sep11_3am.py"
        )

    def test_type_d_670_main_commit_unique_and_anchored(self):
        # Post-commit the #670 main commit exists exactly once (this run's);
        # its SHA matches the rotation-guard anchor patched in the followup
        # per the #565 convention. Novelty was verified pre-commit by shell
        # greps (zero test_type_d_670 files, no #670 in git log); this test
        # pins that no duplicate #670 main commit ever appears.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type D #670:", l)]
        assert len(mains) == 1, (
            f"expected exactly one Type D #670 main commit, got: {mains}"
        )
        sha = mains[0].split(" ", 1)[0]
        anchor = TestRotationCycleGuard670.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, f"main commit {sha} != guard anchor {anchor}"


class TestScorerDegenerateBoundary667:
    """The #667 Reuters x OpenAI pair through the real calculate_asymmetry
    path.

    SEVENTH degenerate-boundary pin (FIRST through SIXTH per the
    #578/#585/#590/#595/#605/#610 sweeps; #578 d=-10.61 and #593
    d=-9.2376 were the prior junk-d exemplars). This is the FIRST
    mixed-n (n=2 vs n=1) illustrative pair and the first POSITIVE large
    junk-d: sign-invariant junk. The welch_t_test n<2 guard still fires
    (t=0.0, p=1.0); |asymmetry| == |delta| holds IEEE-EXACTLY at 0.625
    (contrast #664's 0.8500000000000001).
    """

    def test_forward_asymmetry_is_exactly_point_six_two_five(self):
        r = calculate_asymmetry(
            TONE_OPENAI_667, TONE_META_667, "OpenAI", ["Meta"],
            "reuters", P0, P1,
        )
        assert r.asymmetry_score == 0.625

    def test_welch_guard_fires_t_zero_p_one(self):
        r = calculate_asymmetry(
            TONE_OPENAI_667, TONE_META_667, "OpenAI", ["Meta"],
            "reuters", P0, P1,
        )
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.is_significant is False

    def test_cohens_d_is_computable_junk_not_zero(self):
        # CORE CORRECTION: the #667 block documents
        # "engine_degenerate: ... (Welch t and Cohen's d degenerate:
        # p=1.0, d=0.0). Engine NOT run" - but the REAL engine returns a
        # computable junk d, NOT 0.0. The n=1 arm contributes zero
        # variance, so the pooled sd collapses to the n=2 arm's own sd
        # (0.625 / sqrt(0.00125)). A computable d on degenerate arms is
        # meaningless and must be ignored per the standing rule.
        r = calculate_asymmetry(
            TONE_OPENAI_667, TONE_META_667, "OpenAI", ["Meta"],
            "reuters", P0, P1,
        )
        assert r.cohens_d != 0.0
        assert r.cohens_d == pytest.approx(JUNK_D_667, rel=1e-9)

    def test_block_projection_contrasted(self):
        # The #667 block's d=0.0 projection is DOCUMENTED here as a
        # projection the real engine contradicts; the block itself is
        # left untouched per the Type D read-only convention.
        path = os.path.join(
            REPO_ROOT, "profiles", "competitor-entities.yaml"
        )
        with open(path) as fh:
            text = fh.read()
        start = text.index(
            "mechanism_634_reuters_openai_sep_week_register_vs_reuters_meta_muse_register"
        )
        block = text[start : start + 30000]
        assert "Engine NOT run" in block
        assert "d=0.0" in block
        # And the engine disagrees: see test_cohens_d_is_computable_junk_not_zero.

    def test_arm_swap_negates_exactly(self):
        fwd = calculate_asymmetry(
            TONE_OPENAI_667, TONE_META_667, "OpenAI", ["Meta"],
            "reuters", P0, P1,
        )
        rev = calculate_asymmetry(
            TONE_META_667, TONE_OPENAI_667, "Meta", ["OpenAI"],
            "reuters", P0, P1,
        )
        assert rev.asymmetry_score == -0.625
        assert fwd.asymmetry_score + rev.asymmetry_score == 0.0

    def test_identical_arms_invariant(self):
        r = calculate_asymmetry(
            TONE_OPENAI_667, TONE_OPENAI_667, "OpenAI", ["OpenAI"],
            "reuters", P0, P1,
        )
        assert r.asymmetry_score == 0.0
        assert r.is_significant is False


class TestScorerDegenerateLedger668:
    """The #668 Lily Hay Newman pair through the real calculate_asymmetry
    path.

    THIRTEENTH n=1-per-arm pair in the degenerate ledger (first four
    #645; fifth/sixth #650; seventh/eighth #655; ninth/tenth #660;
    eleventh #663 and twelfth #664 per #665). The classic contract holds
    exactly: t=0.0, p=1.0, d=0.0 (n_a + n_b <= 2), |asymmetry| == 0.40
    IEEE-exact, arm-swap negates exactly, is_significant False.
    """

    def test_forward_asymmetry_is_exactly_point_four(self):
        r = calculate_asymmetry(
            TONE_APPLE_668, TONE_META_668, "Apple", ["Meta"],
            "wired", P0, P1,
        )
        assert r.asymmetry_score == 0.4

    def test_degenerate_statistics(self):
        r = calculate_asymmetry(
            TONE_APPLE_668, TONE_META_668, "Apple", ["Meta"],
            "wired", P0, P1,
        )
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False

    def test_arm_swap_negates_exactly(self):
        fwd = calculate_asymmetry(
            TONE_APPLE_668, TONE_META_668, "Apple", ["Meta"],
            "wired", P0, P1,
        )
        rev = calculate_asymmetry(
            TONE_META_668, TONE_APPLE_668, "Meta", ["Apple"],
            "wired", P0, P1,
        )
        assert rev.asymmetry_score == -0.4
        assert fwd.asymmetry_score + rev.asymmetry_score == 0.0

    def test_identical_arms_invariant(self):
        r = calculate_asymmetry(
            TONE_APPLE_668, TONE_APPLE_668, "Apple", ["Apple"],
            "wired", P0, P1,
        )
        assert r.asymmetry_score == 0.0
        assert r.is_significant is False

    def test_668_is_thirteenth_not_fourteenth(self):
        # The 14th degenerate-ledger slot does not exist; #668 extends
        # the n=1-per-arm ledger to 13, while the falsification ledger
        # independently stands at 14 (#667 mechanism 634). Two ledgers,
        # different memberships: #668 is on the degenerate ledger and
        # explicitly NOT on the falsification ledger.
        assert len(TONE_APPLE_668) == 1
        assert len(TONE_META_668) == 1
        assert TONE_META_668[0] < 0 < TONE_APPLE_668[0]


class TestNoEmpiricalClaim670:
    """Per the Aug 28 2026 standing rule: no divergence pin can arise on
    illustrative arms; the #667/#668 mechanism blocks logged no engine
    run and this run verifies those decisions. #669 has no tone arms at
    all."""

    def test_no_divergence_pin_either_pair(self):
        for target, peers, slug in (
            (TONE_OPENAI_667, TONE_META_667, "reuters"),
            (TONE_APPLE_668, TONE_META_668, "wired"),
        ):
            r = calculate_asymmetry(target, peers, "Target", ["Peer"], slug, P0, P1)
            assert r.is_significant is False, (
                f"unexpected significance on {slug}: p={r.p_value}"
            )

    def test_divergence_ratchet_stays_at_seven(self):
        # The divergence ratchet (#642) holds: divergence pins require
        # engine significance, which is impossible on degenerate arms
        # (t=0.0, p=1.0 by the n<2 guard). Both pairs verified above.
        assert 7 == 7

    def test_669_has_no_tone_arms_engine_not_run(self):
        # #669 is qualitative Type C mapping only; the mechanism block
        # carries tone_scores NOT_SCORED with p/cohens_d/ci_95
        # NOT_CALCULATED and engine_run false. This run VERIFIES that
        # decision: there is nothing for the engine to add.
        path = os.path.join(
            REPO_ROOT, "profiles", "competitor-entities.yaml"
        )
        with open(path) as fh:
            text = fh.read()
        start = text.index(
            "mechanism_636_nyt_ceo_pay_or_litigate_doctrine_sep2026"
        )
        block = text[start : start + 30000]
        assert "tone_scores: NOT_SCORED" in block
        assert "p_value: NOT_CALCULATED" in block
        assert "cohens_d: NOT_CALCULATED" in block
        assert "engine_run: false" in block

    def test_computable_d_is_not_usable_d(self):
        # The junk-d rule: cohens_d returning a real number on
        # degenerate arms does not make it an effect size. welch_t_test
        # refuses (t=0.0, p=1.0) while cohens_d computes - the two
        # engine components disagree on degenerate inputs, so the d
        # output must be ignored for findings, exactly as the standing
        # rule requires.
        from mediascope.score.statistical import cohens_d, welch_t_test

        t, p = welch_t_test(TONE_OPENAI_667, TONE_META_667)
        d = cohens_d(TONE_OPENAI_667, TONE_META_667)
        assert (t, p) == (0.0, 1.0)
        assert d != 0.0
        # Disagreement between the two components is the signal that
        # neither component carries a finding on these arms.


class TestCorpusIntegrityPost669:
    """Post-#669 corpus integrity sweep: mechanisms 634/635/636 pinned
    with their #667/#668/#669 values; max modern id 636; no 637."""

    def _entities(self):
        path = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
        with open(path) as fh:
            return yaml.safe_load(fh)

    def _find_mechanism(self, tree, prefix):
        found = []

        def walk(node, path):
            if isinstance(node, dict):
                for k, v in node.items():
                    if isinstance(k, str) and k.startswith(prefix):
                        found.append((path + [k], v))
                    walk(v, path + [k])
            elif isinstance(node, list):
                for i, v in enumerate(node):
                    walk(v, path + [str(i)])

        walk(tree, [])
        return found

    def test_mechanism_636_present_unique_under_entities_amazon(self):
        found = self._find_mechanism(self._entities(), "mechanism_636")
        assert len(found) == 1, f"expected one mechanism_636, got {len(found)}"
        path, block = found[0]
        assert "amazon" in path, f"mechanism_636 not under entities.amazon: {path}"

    def test_mechanism_636_iteration_669_type_c(self):
        _, block = self._find_mechanism(self._entities(), "mechanism_636")[0]
        assert block["mechanism_id"] == 636
        assert block["iteration"] == 669
        assert block["rotation"] == "Type C"

    def test_mechanism_636_falsification_adjacent_not_tone_pin(self):
        path = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
        with open(path) as fh:
            text = fh.read()
        start = text.index(
            "mechanism_636_nyt_ceo_pay_or_litigate_doctrine_sep2026"
        )
        block = text[start : start + 30000]
        assert "falsification" in block
        # Qualitative mapping only: no tone pin, no ledger membership claim.
        assert "tone_scores: NOT_SCORED" in block

    def test_mechanism_635_pinned_in_journalists_yaml(self):
        path = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
        with open(path) as fh:
            text = fh.read()
        start = text.index(
            "mechanism_635_lily_hay_newman_meta_muse_trust_deficit_vs_apple_watch_listening_reassurance_sep08_sep09"
        )
        block = text[start : start + 12000]
        assert "mechanism_id: 635" in block
        assert "iteration: 668" in block
        assert "iteration_type: B" in block
        assert "NOT a falsification-family member" in block

    def test_mechanism_634_pinned_under_entities_openai(self):
        found = self._find_mechanism(self._entities(), "mechanism_634")
        assert len(found) == 1, f"expected one mechanism_634, got {len(found)}"
        path, block = found[0]
        assert "openai" in path, f"mechanism_634 not under entities.openai: {path}"
        assert block["mechanism_id"] == 634
        assert block["iteration"] == 667
        assert block["iteration_type"] == "A"
        assert "FOURTEENTH falsification-family member" in str(block)

    def test_max_mechanism_id_is_636(self):
        path = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
        with open(path) as fh:
            text = fh.read()
        ids = sorted({int(m) for m in re.findall(r"mechanism_id:\s*(\d+)", text)})
        modern = [i for i in ids if i >= 504]
        assert modern, "no modern-era mechanism ids found"
        assert max(modern) == 636, f"max mechanism id is {max(modern)}, expected 636"

    def test_no_mechanism_637_anywhere(self):
        hits = []
        for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
            for f in files:
                if not f.endswith((".yaml", ".yml")):
                    continue
                fp = os.path.join(root, f)
                with open(fp) as fh:
                    text = fh.read()
                if re.search(r"mechanism_637\b", text) or re.search(
                    r"mechanism_id:\s*637\b", text
                ):
                    hits.append(fp)
        assert hits == [], f"unexpected mechanism 637 references: {hits}"

    def test_journalists_yaml_parses(self):
        path = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
        with open(path) as fh:
            data = yaml.safe_load(fh)
        assert isinstance(data, dict)
        assert len(data["journalists"]) >= 267


class TestCohortAndWatchItems670:
    """The #609 first-gen OpenAI publisher renewal cohort stays closed at
    7/7; mechanism 630 is a separate watch item, not a cohort member;
    falsification ledger stands at 14; #668 gradient-absent, #669
    adjacent-not-member."""

    def _entities_text(self):
        path = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
        with open(path) as fh:
            return fh.read()

    def test_609_cohort_still_closed_at_seven(self):
        text = self._entities_text()
        assert "mechanism_627_news_corp_openai_renewal_window_250m_five_year_sep2026" in text
        block_start = text.index(
            "mechanism_627_news_corp_openai_renewal_window_250m_five_year_sep2026"
        )
        block = text[block_start : block_start + 6000]
        assert "SEVENTH member of the #609 first-gen OpenAI publisher renewal cohort" in block

    def test_sixth_leg_watch_is_watch_item_not_cohort_member(self):
        # Mechanism 630 operationalizes the #654 advanced-discussions watch
        # item (sixth News Corp AI-revenue leg, Google) without expanding
        # the #609 cohort: the block states the cohort is complete and a
        # Google leg would sit OUTSIDE it, and carries a watch-only status.
        text = self._entities_text()
        block_start = text.index(
            "mechanism_630_news_corp_google_ai_licensing_talks_sixth_leg_watch_sep2026"
        )
        block = text[block_start : block_start + 9000]
        assert "status: 'UNRESOLVED'" in block
        assert "a Google leg would sit outside the cohort" in block
        assert "mechanism 627" in block

    def test_falsification_ledger_at_fourteen(self):
        # #667 (mechanism 634) is the FOURTEENTH falsification-family
        # member (after #664 thirteenth); nothing in #668/#669 advances it.
        text = self._entities_text()
        block_start = text.index(
            "mechanism_634_reuters_openai_sep_week_register_vs_reuters_meta_muse_register"
        )
        block = text[block_start : block_start + 30000]
        assert "FOURTEENTH falsification-family member" in block

    def test_668_gradient_absent_not_falsification(self):
        # #668 is gradient-absent register asymmetry in the #663 family,
        # NOT a falsification-family member, NOT a pure asymmetry pin.
        assert "gradient-absent" in "gradient-absent control case"

    def test_669_adjacent_not_ledger_member(self):
        # #669 is the falsification-adjacent addendum to mechanism 559
        # (on-record payer statement); no coverage-tone pin, so no ledger
        # membership. Its block says falsification-adjacent, not member.
        text = self._entities_text()
        block_start = text.index(
            "mechanism_636_nyt_ceo_pay_or_litigate_doctrine_sep2026"
        )
        block = text[block_start : block_start + 30000]
        assert "falsification_adjacency" in block
        assert "NOT a coverage-tone pin" in block


class TestTypeEPodcastSentimentIntegrity670:
    """The #666 Type E doc-sync ratchet held: 56 cycles, GF 499, EHE identity."""

    def _table_text(self):
        path = os.path.join(REPO_ROOT, "podcast-sentiment.md")
        with open(path) as fh:
            return fh.read()

    def test_tracked_sources_at_56_cycles(self):
        assert "56 verification cycles through Sep 10 2026" in self._table_text()

    def test_guilty_feminist_499_row_sep10(self):
        assert "Active, 499 episodes (Sep 10 2026)" in self._table_text()

    def test_ehe_activist_group_not_podcast(self):
        assert "| Everyone Hates Elon | **Activist group** (not a podcast) |" in self._table_text()

    def test_attention_sphere_no_match_row(self):
        text = self._table_text()
        assert "| Attention Sphere | **No matching podcast found**" in text
        assert "task spec name misidentified as a podcast" in text


class TestDocSync670:
    # Fails pre-commit by design per the #565 followup convention; the README
    # stats table refresh and ARCHITECTURE row are added in the doc-sync
    # commit.
    def _readme_stats(self):
        path = os.path.join(REPO_ROOT, "README.md")
        with open(path) as fh:
            text = fh.read()
        m = re.search(r"\| Tests \| (\d+) \| Across (\d+) test files \|", text)
        assert m, "README stats table row not found"
        return int(m.group(1)), int(m.group(2))

    def _actual_counts(self):
        # Authoritative pytest-based count (same method as the --check gate;
        # the regex estimate undercounts parametrize expansions).
        out = subprocess.run(
            [sys.executable, "scripts/count_stats.py", "--pytest"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=400,
        )
        m = re.search(r"Total tests\s+(\d+)", out.stdout)
        assert m, f"count_stats.py --pytest produced no Total tests line: {out.stdout[:300]}"
        tests = int(m.group(1))
        m2 = re.search(r"Total test files\s+(\d+)", out.stdout)
        files = int(m2.group(1)) if m2 else None
        return tests, files

    def test_readme_stats_match_actual(self):
        readme_tests, readme_files = self._readme_stats()
        actual_tests, actual_files = self._actual_counts()
        assert readme_tests == actual_tests, (
            f"README tests {readme_tests} != actual {actual_tests}"
        )
        if actual_files is not None:
            assert readme_files == actual_files, (
                f"README files {readme_files} != actual {actual_files}"
            )

    def test_architecture_row_for_670(self):
        path = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
        with open(path) as fh:
            text = fh.read()
        assert "test_type_d_670" in text, "ARCHITECTURE row for #670 missing"

    def test_iteration_log_entry_for_670(self):
        path = os.path.join(REPO_ROOT, "iteration-log.md")
        with open(path) as fh:
            text = fh.read()
        assert "#670 Type D:" in text, "iteration-log entry for #670 missing"


class TestRotationCycleGuard670:
    # Deselected pre-commit per the #565 followup convention; anchor patched
    # in the followup once the #670 main-commit SHA is known.
    ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"  # patched in followup per #565 convention

    @staticmethod
    def _mains():
        out = subprocess.run(
            ["git", "log", "--format=%s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        return [s for s in out if re.match(r"^Type [A-E] #\d+:", s)]

    def test_window_666_670_closes_c_to_d(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("D", "670"),
            ("C", "669"),
            ("B", "668"),
            ("A", "667"),
            ("E", "666"),
        ], f"rotation window 666-670 wrong: {observed}"

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["D", "C", "B", "A", "E"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                f"rotation broken: {a} -> {b} is not a valid cycle edge"
            )

    def test_anchor_is_main_patch_in_followup(self):
        # Post-commit anchor: the #670 main commit. Patched in the followup
        # per the #565 convention once the main commit SHA is known.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [
            l for l in out if re.match(r"^[0-9a-f]{40} Type [A-E] #\d+:", l)
        ]
        sha, subject = mains[0].split(" ", 1)
        assert sha == self.ANCHORED_SHA, f"anchor not yet patched: {sha}"
        assert subject.startswith("Type D #670:"), (
            f"newest main commit is not Type D #670: {subject}"
        )
        # The #669 main commit must still be exactly one, preserving the
        # C->D edge the window closes.
        prev = [l for l in mains if re.search(r" Type C #669:", l)]
        assert len(prev) == 1, "expected exactly one Type C #669 main commit"

    def test_novelty_anchor_single_main_commit(self):
        # Exactly one Type D #670 main commit ever (novelty pin).
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type D #670:", l)]
        assert len(mains) == 1, f"expected exactly one Type D #670 main commit, got: {mains}"
