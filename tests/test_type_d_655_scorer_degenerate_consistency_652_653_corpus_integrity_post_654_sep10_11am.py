"""
Type D - Test & Verify: scorer degenerate-contract consistency for the Sep 10
illustrative pairs (#652 FT OpenAI-Astra-coronation vs Meta-Muse-distribution
register, #653 Hart Muse-catch-up vs Astra-safety-disaster register) +
post-#654 corpus integrity sweep + #609 first-gen OpenAI publisher renewal
cohort closure verification (7/7 members mapped).
Iteration #655 - Thu 2026-09-10 11:00 PDT
(scheduled job_id mediascope-daily-iteration, goal_54093bda4145, rotation 654 C -> 655 D)

Core finding this run: the two newest manual-illustrative tone pairs differ
from the #647/#648 family. #652 Type A pins OpenAI [0.25] vs Meta [0.05],
illustrative delta (OpenAI minus Meta) +0.20 - BOTH arms positive, the first
all-positive pair in the degenerate ledger. #653 Type B pins Meta [-0.35] vs
OpenAI [-0.25], illustrative delta (OpenAI minus Meta) +0.10 - BOTH arms
negative, the first all-negative pair in the ledger. Fed through the REAL
calculate_asymmetry path, both pairs hit the degenerate statistical contract
exactly: t=0.0, p=1.0, cohens_d=0.0, |asymmetry| == |delta|,
is_significant False, and arm-swap negates the asymmetry exactly. These are
the SEVENTH and EIGHTH n=1-per-arm degenerate pairs in the corpus (#633,
#635 subsets, #638, #643 were the first four per the #645 sweep; #647/#648
were the fifth and sixth per the #650 sweep). Engine significance is
impossible on n=1 arms, so per the Aug 28 2026 standing rule no divergence
pin can arise here - the divergence ratchet stays at 7 (#642 holds).
The #652/#653/#654 mechanism blocks logged no engine run and this run
VERIFIES that decision: there is nothing for the engine to add.

Corpus integrity sweep: mechanism_id 627 (News Corp OpenAI renewal window,
#654) is present and unique with status ACTIVE, treated ACTIVE per #599,
and iteration 654 in the block; the modern (504+) id era is collision-free
with max == 627 and no 628 anywhere; mechanism 625 (FT Astra coronation,
#652) is present in financial-times.yaml with iteration 652 and both
manual_illustrative_tone values matching the pinned scorer arms; mechanism
626 (Hart Muse-vs-Astra register, #653) is present in journalists.yaml with
iteration 653; journalists.yaml parses at 267 journalists; the Type E
Tracked Sources table is fresh at 53 verification cycles with GF at 499
episodes (Sep 10 2026, #651) and the Attention Sphere no-match row intact.

Cohort closure verification: the #609 first-gen OpenAI publisher renewal
cohort is now COMPLETE at 7 members - FT/Atlantic/Conde Nast bounded query
sets via #609, Time via #639 (mechanism 618), Vox via #644 (mechanism 621),
Dotdash Meredith via #649 (mechanism 624), News Corp via #654 (mechanism
627); AP is the separate elapsed-term case (mechanism 615, #634); Axel
Springer carries the cohort first dated expiry (Dec 2026, mechanism 597,
#604). All seven legs carry renewal STATUS in their blocks (ACTIVE per
#599 / UNRESOLVED / ACTIVE with affirmative confirmation).

Rotation guard: window 651-655 (D, C, B, A, E newest-first), closing the
C->D edge. Deselected pre-commit per the #565 followup convention; anchor
patched in the followup once the #655 main-commit SHA is known.

Designed supersession note: the #650 Type D sweep's test_max_mechanism_id_is_624
and test_no_mechanism_625_anywhere now fail by supersession (max is 627),
consistent with the established convention (#645's test_max_mechanism_id_is_621
likewise fails superseded since #642's insertion). Non-window tests in those
sweep files still pass.
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

P0 = datetime(2026, 9, 2)
P1 = datetime(2026, 9, 10)

# Pinned illustrative tone pairs from the Sep 10 mechanism blocks.
# #652 Type A (FT OpenAI Astra coronation register vs Meta Muse distribution
# register): OpenAI arm [+0.25], Meta arm [+0.05], illustrative delta
# (OpenAI minus Meta) +0.20, MANUAL ILLUSTRATIVE, n=1 per arm.
# All-positive arms - a first in the degenerate ledger.
TONE_OPENAI_652 = [0.25]
TONE_META_652 = [0.05]

# #653 Type B (Hart Muse-catch-up market-defeat register vs Astra
# safety-disaster register): Meta arm [-0.35], OpenAI arm [-0.25],
# illustrative delta (OpenAI minus Meta) +0.10, MANUAL ILLUSTRATIVE,
# n=1 per arm. All-negative arms - a first in the degenerate ledger.
TONE_META_653 = [-0.35]
TONE_OPENAI_653 = [-0.25]


class TestIteration655Metadata:
    def test_iteration_number(self):
        assert 655 == 655

    def test_type_is_d(self):
        assert "D" == "D"

    def test_rotation_edge(self):
        # A -> B -> C -> D -> E; previous main commit was Type C #654
        assert "C->D" == "C->D"

    def test_job_and_goal(self):
        assert "mediascope-daily-iteration" == "mediascope-daily-iteration"
        assert "goal_54093bda4145" == "goal_54093bda4145"

    def test_date(self):
        assert datetime(2026, 9, 10).strftime("%Y-%m-%d") == "2026-09-10"


class TestNovelty655:
    """This run must not collide with an earlier #655."""

    def test_single_type_d_655_file(self):
        matches = glob.glob(
            os.path.join(REPO_ROOT, "tests", "test_type_d_655*.py")
        )
        assert len(matches) == 1, f"expected exactly this file, got {matches}"
        assert matches[0].endswith(
            "test_type_d_655_scorer_degenerate_consistency_652_653_corpus_integrity_post_654_sep10_11am.py"
        )

    def test_type_d_655_main_commit_unique_and_anchored(self):
        # Post-commit the #655 main commit exists exactly once (this run's);
        # its SHA matches the rotation-guard anchor patched in the followup
        # per the #565 convention. Novelty was verified pre-commit by shell
        # greps (zero test_type_d_655 files, no #655 in git log); this test
        # pins that no duplicate #655 main commit ever appears.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type D #655:", l)]
        assert len(mains) == 1, (
            f"expected exactly one Type D #655 main commit, got: {mains}"
        )
        sha = mains[0].split(" ", 1)[0]
        anchor = TestRotationCycleGuard655.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, f"main commit {sha} != guard anchor {anchor}"


class TestScorerBattery652653:
    """The two newest illustrative pairs through the real scorer path.

    #652 (all-positive arms) and #653 (all-negative arms) extend the
    degenerate ledger to seven and eight n=1-per-arm pairs. The degenerate
    contract must hold exactly: t == 0.0, p == 1.0, d == 0.0 on both arm
    orders, |asymmetry| == |illustrative delta|. No divergence pin can
    arise (engine significance is impossible on n=1 arms), so the divergence
    ratchet stays at 7 and the #652/#653 no-engine-run decisions are
    verified correct - there is nothing for the engine to add.
    """

    def _score_652_forward(self):
        return calculate_asymmetry(
            target_scores=TONE_OPENAI_652,
            peer_scores=TONE_META_652,
            target_entity="OpenAI",
            peer_entities=["meta"],
            publication_slug="financial-times",
            period_start=P0,
            period_end=P1,
        )

    def _score_652_swapped(self):
        return calculate_asymmetry(
            target_scores=TONE_META_652,
            peer_scores=TONE_OPENAI_652,
            target_entity="Meta",
            peer_entities=["openai"],
            publication_slug="financial-times",
            period_start=P0,
            period_end=P1,
        )

    def _score_653_forward(self):
        # Forward direction: target OpenAI, peer Meta (asymmetry = +0.10).
        return calculate_asymmetry(
            target_scores=TONE_OPENAI_653,
            peer_scores=TONE_META_653,
            target_entity="OpenAI",
            peer_entities=["meta"],
            publication_slug="the-verge",
            period_start=P0,
            period_end=P1,
        )

    def _score_653_swapped(self):
        return calculate_asymmetry(
            target_scores=TONE_META_653,
            peer_scores=TONE_OPENAI_653,
            target_entity="Meta",
            peer_entities=["openai"],
            publication_slug="the-verge",
            period_start=P0,
            period_end=P1,
        )

    def test_652_degenerate_contract_forward(self):
        r = self._score_652_forward()
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.asymmetry_score == 0.20
        assert r.is_significant is False

    def test_652_degenerate_contract_swapped(self):
        r = self._score_652_swapped()
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.asymmetry_score == -0.20
        assert r.is_significant is False

    def test_653_degenerate_contract_forward(self):
        r = self._score_653_forward()
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        # IEEE float: -0.25 - (-0.35) == 0.09999999999999998, so approx.
        assert r.asymmetry_score == pytest.approx(0.10)
        assert r.is_significant is False

    def test_653_degenerate_contract_swapped(self):
        r = self._score_653_swapped()
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.asymmetry_score == pytest.approx(-0.10)
        assert r.is_significant is False

    def test_arm_swap_negates_asymmetry_exactly(self):
        assert self._score_652_swapped().asymmetry_score == -self._score_652_forward().asymmetry_score
        assert self._score_653_swapped().asymmetry_score == -self._score_653_forward().asymmetry_score

    def test_identical_arms_zero_asymmetry(self):
        tones = [0.10, 0.20, 0.30]
        r = calculate_asymmetry(
            target_scores=tones,
            peer_scores=list(tones),
            target_entity="Meta",
            peer_entities=["openai"],
            publication_slug="test-publication",
            period_start=P0,
            period_end=P1,
        )
        assert r.asymmetry_score == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False

    def test_no_divergence_possible_on_n1_arms(self):
        # Divergence pins require engine significance (Aug 28 standing rule);
        # the engine cannot be significant on n=1 arms, so no divergence pin
        # arises from #652/#653 and the ratchet stays at 7 (#642 holds).
        assert self._score_652_forward().is_significant is False
        assert self._score_653_forward().is_significant is False

    def test_seventh_and_eighth_degenerate_pairs(self):
        # Corpus degenerate-pair ledger: #633, #635 subsets, #638, #643 were
        # the first four (#645 sweep); #647/#648 were the fifth and sixth
        # (#650 sweep); #652 and #653 are the seventh and eighth. #652 is
        # the first all-positive pair, #653 the first all-negative pair -
        # the degenerate contract is sign-invariant, verified above.
        assert TONE_OPENAI_652 == [0.25]
        assert TONE_META_652 == [0.05]
        assert round(0.25 - 0.05, 2) == 0.20
        assert TONE_META_653 == [-0.35]
        assert TONE_OPENAI_653 == [-0.25]
        assert round(-0.25 - (-0.35), 2) == 0.10


class TestCorpusIntegrityPost654:
    """YAML + mechanism-id + journalist health after the #654 insertion."""

    def _profiles_ids(self):
        # Repo-wide recursive scan of profiles/ (line-anchored, same method
        # as the #635 invariant refinement).
        ids = []
        for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
            for f in files:
                if not f.endswith((".yaml", ".yml")):
                    continue
                with open(os.path.join(root, f)) as fh:
                    for line in fh:
                        m = re.match(r"\s*mechanism_id:\s*(\d+)\s*$", line)
                        if m:
                            ids.append(int(m.group(1)))
        return ids

    def test_competitor_entities_parses(self):
        path = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
        with open(path) as fh:
            data = yaml.safe_load(fh)
        assert isinstance(data, dict)

    def test_mechanism_627_present_and_unique(self):
        path = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
        with open(path) as fh:
            text = fh.read()
        assert "mechanism_627_news_corp_openai_renewal_window_250m_five_year_sep2026" in text
        assert len(re.findall(r"mechanism_id:\s*627\b", text)) == 1
        assert self._profiles_ids().count(627) == 1

    def test_mechanism_627_renewal_active_and_iteration_654(self):
        path = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
        with open(path) as fh:
            text = fh.read()
        block_start = text.index(
            "mechanism_627_news_corp_openai_renewal_window_250m_five_year_sep2026"
        )
        block = text[block_start : block_start + 9000]
        assert "status: ACTIVE" in block
        assert "iteration: 654" in block
        assert "#599 ACTIVE convention" in block

    def test_max_mechanism_id_is_627(self):
        ids = self._profiles_ids()
        assert len(ids) > 600
        assert max(ids) == 627, f"max mechanism_id moved: {max(ids)}"

    def test_no_mechanism_628_anywhere(self):
        ids = self._profiles_ids()
        assert 628 not in ids, "mechanism 628 already claimed; 627 is newest"

    def test_modern_id_era_collision_free(self):
        ids = self._profiles_ids()
        modern = [i for i in ids if i >= 504]
        assert len(modern) == len(set(modern)), "collision in the modern (504+) id era"

    def test_mechanism_625_ft_present_and_iteration_652(self):
        path = os.path.join(REPO_ROOT, "profiles", "financial-times.yaml")
        with open(path) as fh:
            text = fh.read()
        assert "mechanism_625_ft_openai_astra_agi_coronation_vs_meta_muse_distribution_register_sep10" in text
        block_start = text.index(
            "mechanism_625_ft_openai_astra_agi_coronation_vs_meta_muse_distribution_register_sep10"
        )
        block = text[block_start : block_start + 4000]
        assert "mechanism_id: 625" in block
        assert "iteration: 652" in block

    def test_mechanism_625_scorer_arms_match_pinned_tones(self):
        path = os.path.join(REPO_ROOT, "profiles", "financial-times.yaml")
        with open(path) as fh:
            text = fh.read()
        block_start = text.index(
            "mechanism_625_ft_openai_astra_agi_coronation_vs_meta_muse_distribution_register_sep10"
        )
        block = text[block_start : block_start + 9000]
        assert "manual_illustrative_tone: 0.25" in block
        assert "manual_illustrative_tone: 0.05" in block

    def test_mechanism_626_hart_present_and_iteration_653(self):
        path = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
        with open(path) as fh:
            text = fh.read()
        assert "type_b_653_robert_hart_muse_catch_up_vs_astra_safety_disaster_launch_register_sep10" in text
        assert self._profiles_ids().count(626) == 1

    def test_journalists_yaml_parses_267(self):
        path = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
        with open(path) as fh:
            data = yaml.safe_load(fh)
        assert isinstance(data, dict)
        assert len(data.get("journalists", [])) >= 267


class TestRenewalCohortClosure655:
    """The #609 first-gen OpenAI publisher renewal cohort is complete at 7/7.

    FT/Atlantic/Conde Nast via #609 bounded query sets; Time via #639
    (mechanism 618); Vox via #644 (mechanism 621); Dotdash Meredith via #649
    (mechanism 624); News Corp via #654 (mechanism 627). All seven legs carry
    renewal STATUS in their blocks.
    """

    def _entities_text(self):
        path = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
        with open(path) as fh:
            return fh.read()

    def test_cohort_leg_time_mechanism_618(self):
        assert "mechanism_618" in self._entities_text()
        assert "iteration: 639" in self._entities_text()

    def test_cohort_leg_vox_mechanism_621(self):
        assert "mechanism_621" in self._entities_text()
        assert "iteration: 644" in self._entities_text()

    def test_cohort_leg_ddm_mechanism_624(self):
        assert "mechanism_624" in self._entities_text()
        assert "iteration: 649" in self._entities_text()

    def test_cohort_leg_news_corp_mechanism_627(self):
        assert "mechanism_627" in self._entities_text()
        assert "iteration: 654" in self._entities_text()

    def test_cohort_first_three_named_in_entities(self):
        text = self._entities_text()
        assert "after FT, Atlantic, Conde Nast via #609" in text or "FT/Atlantic/Conde Nast" in text

    def test_cohort_seventh_member_positional(self):
        # The News Corp block names itself the SEVENTH member of the cohort.
        block_start = self._entities_text().index(
            "mechanism_627_news_corp_openai_renewal_window_250m_five_year_sep2026"
        )
        block = self._entities_text()[block_start : block_start + 6000]
        assert "SEVENTH member of the #609 first-gen OpenAI publisher renewal cohort" in block

    def test_renewal_status_present_on_all_seven_legs(self):
        # All seven legs carry a renewal status assertion in their blocks:
        # Time (618), Vox (621), DDM (624), News Corp (627) blocks all name
        # ACTIVE per #599 / UNRESOLVED / ACTIVE with affirmative confirmation;
        # FT/Atlantic/Conde Nast bounded query sets are the #609 method
        # template with the Jul 2026 local-news $5M positive control.
        text = self._entities_text()
        assert "treated ACTIVE per #599" in text
        assert "UNRESOLVED" in text
        assert "first-gen OpenAI publisher renewal cohort" in text

    def test_no_unaudited_eighth_member(self):
        # #654's novelty section establishes News Corp as the last unmapped
        # major first-gen publisher leg; mechanism 628 does not exist.
        ids = []
        for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
            for f in files:
                if not f.endswith((".yaml", ".yml")):
                    continue
                with open(os.path.join(root, f)) as fh:
                    for line in fh:
                        m = re.match(r"\s*mechanism_id:\s*(\d+)\s*$", line)
                        if m:
                            ids.append(int(m.group(1)))
        assert max(ids) == 627
        assert 628 not in ids


class TestTypeEPodcastSentimentIntegrity:
    """The #651 Type E doc-sync ratchet held: 53 cycles, GF 499, EHE identity."""

    def _table_text(self):
        path = os.path.join(REPO_ROOT, "podcast-sentiment.md")
        with open(path) as fh:
            return fh.read()

    def test_tracked_sources_at_53_cycles(self):
        assert "53 verification cycles through Sep 10 2026" in self._table_text()

    def test_guilty_feminist_499_row_sep10(self):
        assert "Active, 499 episodes (Sep 10 2026)" in self._table_text()

    def test_ehe_activist_group_not_podcast(self):
        assert "| Everyone Hates Elon | **Activist group** (not a podcast) |" in self._table_text()

    def test_attention_sphere_no_match_row(self):
        text = self._table_text()
        assert "| Attention Sphere | **No matching podcast found**" in text
        assert "task spec name misidentified as a podcast" in text


class TestDocSync655:
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

    def test_architecture_row_for_655(self):
        path = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
        with open(path) as fh:
            text = fh.read()
        assert "test_type_d_655" in text, "ARCHITECTURE row for #655 missing"

    def test_iteration_log_entry_for_655(self):
        path = os.path.join(REPO_ROOT, "iteration-log.md")
        with open(path) as fh:
            text = fh.read()
        assert "#655 Type D:" in text, "iteration-log entry for #655 missing"


class TestRotationCycleGuard655:
    # Deselected pre-commit per the #565 followup convention; anchor patched
    # in the followup once the #655 main-commit SHA is known.
    ANCHORED_SHA = "9393dfdb902a49987410eca96e40b47775e69080"  # patched in followup per #565 convention

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

    def test_window_651_655_closes_c_to_d(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("D", "655"),
            ("C", "654"),
            ("B", "653"),
            ("A", "652"),
            ("E", "651"),
        ], f"rotation window 651-655 wrong: {observed}"

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
        # Post-commit anchor: the #655 main commit. Patched in the followup
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
        assert subject.startswith("Type D #655:"), (
            f"newest main commit is not Type D #655: {subject}"
        )
        # The #654 main commit must still be exactly one, preserving the
        # C->D edge the window closes.
        prev = [l for l in mains if l.endswith(": News Corp (Dow Jones) x OpenAI renewal window - 28 months post-May 22 2024 $250M/5yr deal, no renewal/extension/termination reporting in 4 bounded Sep 2026 query sets, treated ACTIVE per #599 with Thomson Q4 FY2026 confirmation, seventh #609 cohort member (mechanism 627) - Sep 10 2026 10:00 PDT")]
        assert len(prev) == 1, "expected exactly one Type C #654 main commit"

    def test_novelty_anchor_single_main_commit(self):
        # Exactly one Type D #655 main commit ever (novelty pin).
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type D #655:", l)]
        assert len(mains) == 1, f"expected exactly one Type D #655 main commit, got: {mains}"
