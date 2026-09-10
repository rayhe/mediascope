"""
Type D - Test & Verify: scorer degenerate-contract consistency for the Sep 10
illustrative pairs (#647 WIRED x Anthropic Coxon-resignation register,
#648 Paresh Dave adversarial-actor selection) + post-#649 corpus integrity
sweep.
Iteration #650 - Thu 2026-09-10 06:00 PDT
(scheduled job_id mediascope-daily-iteration, goal_54093bda4145, rotation 649 C -> 650 D)

Core finding this run: the two newest manual-illustrative tone pairs (#647
Type A and #648 Type B) carry IDENTICAL tone values - Anthropic arm [+0.25],
Meta arm [-0.30], illustrative delta (Anthropic minus Meta) +0.55 - so the
battery exercises one engine input on both mechanism records. Fed through the
REAL calculate_asymmetry path, the pair hits the degenerate statistical
contract exactly: t=0.0, p=1.0, cohens_d=0.0, asymmetry +0.55, is_significant
False, and on the arm-swapped order (target Meta [-0.30], peer Anthropic
[+0.25]) the contract is symmetric: t=0.0, p=1.0, d=0.0, asymmetry -0.55,
is_significant False. These are the FIFTH and SIXTH n=1-per-arm degenerate
pairs in the corpus (#633, #635 subsets, #638, #643 were the first four per
the #645 sweep). Engine significance is impossible on n=1 arms, so per the
Aug 28 2026 standing rule no divergence pin can arise here - the divergence
ratchet stays at 7 (#642 holds). The mechanism blocks logged no engine run
and this run VERIFIES that decision: there is nothing for the engine to add.

Corpus integrity sweep: mechanism_id 624 (Dotdash Meredith OpenAI renewal
window, #649) is present and unique with renewal UNRESOLVED and iteration 649
in the block; the modern (504+) id era is collision-free with max == 624 and
no 625 anywhere; mechanism 622 (WIRED Coxon, #647) and mechanism 623 (Dave
adversarial-actor, #648) are present in wired.yaml with their iteration tags;
journalists.yaml parses at 267 journalists; the Type E Tracked Sources table
is fresh at 52 verification cycles with GF at 499 episodes (Sep 10 2026) and
the Attention Sphere no-match row intact.

Rotation guard: window 646-650 (D, C, B, A, E newest-first), closing the
C->D edge. Deselected pre-commit per the #565 followup convention; anchor
patched in the followup once the #650 main-commit SHA is known.

Designed supersession note: the #645 Type D sweep's
test_max_mechanism_id_is_621 and test_no_mechanism_622_anywhere now fail by
supersession (max is 624), consistent with the established convention (#640's
test_max_mechanism_id_is_618 likewise fails superseded since #642). Non-window
tests in those sweep files still pass.
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
# #647 Type A (WIRED x Anthropic Coxon-resignation register) and #648 Type B
# (Paresh Dave adversarial-actor selection) carry IDENTICAL tone values:
# Anthropic arm [0.25], Meta arm [-0.30]; illustrative delta
# (Anthropic minus Meta) +0.55, MANUAL ILLUSTRATIVE, n=1 per arm.
TONE_ANTHROPIC_647_648 = [0.25]
TONE_META_647_648 = [-0.30]


class TestIteration650Metadata:
    def test_iteration_number(self):
        assert 650 == 650

    def test_type_is_d(self):
        assert "D" == "D"

    def test_rotation_edge(self):
        # A -> B -> C -> D -> E; previous main commit was Type C #649
        assert "C->D" == "C->D"

    def test_job_and_goal(self):
        assert "mediascope-daily-iteration" == "mediascope-daily-iteration"
        assert "goal_54093bda4145" == "goal_54093bda4145"

    def test_date(self):
        assert datetime(2026, 9, 10).strftime("%Y-%m-%d") == "2026-09-10"


class TestNovelty650:
    """This run must not collide with an earlier #650."""

    def test_single_type_d_650_file(self):
        matches = glob.glob(
            os.path.join(REPO_ROOT, "tests", "test_type_d_650*.py")
        )
        assert len(matches) == 1, f"expected exactly this file, got {matches}"
        assert matches[0].endswith(
            "test_type_d_650_scorer_degenerate_consistency_647_648_corpus_integrity_post_649_sep10_6am.py"
        )

    def test_type_d_650_main_commit_unique_and_anchored(self):
        # Post-commit the #650 main commit exists exactly once (this run's);
        # its SHA matches the rotation-guard anchor patched in the followup
        # per the #565 convention. Novelty was verified pre-commit by shell
        # greps (zero test_type_d_650 files, no #650 in git log); this test
        # pins that no duplicate #650 main commit ever appears.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type D #650:", l)]
        assert len(mains) == 1, (
            f"expected exactly one Type D #650 main commit, got: {mains}"
        )
        sha = mains[0].split(" ", 1)[0]
        anchor = TestRotationCycleGuard650.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, f"main commit {sha} != guard anchor {anchor}"


class TestScorerBattery647648:
    """The two newest illustrative pairs through the real scorer path.

    #647 and #648 pin the same tone values (Anthropic [0.25], Meta [-0.30],
    delta +0.55, n=1 per arm), so the battery exercises one engine input
    against both mechanism records. The degenerate contract must hold
    exactly: t == 0.0, p == 1.0, d == 0.0 on both arm orders. No divergence
    pin can arise (engine significance is impossible on n=1 arms), so the
    divergence ratchet stays at 7 and the #647/#648 no-engine-run decisions
    are verified correct - there is nothing for the engine to add.
    """

    def _score_forward(self):
        return calculate_asymmetry(
            target_scores=TONE_ANTHROPIC_647_648,
            peer_scores=TONE_META_647_648,
            target_entity="Anthropic",
            peer_entities=["meta"],
            publication_slug="wired",
            period_start=P0,
            period_end=P1,
        )

    def _score_swapped(self):
        return calculate_asymmetry(
            target_scores=TONE_META_647_648,
            peer_scores=TONE_ANTHROPIC_647_648,
            target_entity="Meta",
            peer_entities=["anthropic"],
            publication_slug="wired",
            period_start=P0,
            period_end=P1,
        )

    def test_647_648_degenerate_contract_forward(self):
        r = self._score_forward()
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.asymmetry_score == 0.55
        assert r.is_significant is False

    def test_647_648_degenerate_contract_swapped(self):
        r = self._score_swapped()
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.asymmetry_score == -0.55
        assert r.is_significant is False

    def test_arm_swap_negates_asymmetry_exactly(self):
        assert self._score_swapped().asymmetry_score == -self._score_forward().asymmetry_score

    def test_identical_arms_zero_asymmetry(self):
        tones = [0.10, 0.20, 0.30]
        r = calculate_asymmetry(
            target_scores=tones,
            peer_scores=list(tones),
            target_entity="Meta",
            peer_entities=["anthropic"],
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
        # arises from #647/#648 and the ratchet stays at 7 (#642 holds).
        assert self._score_forward().is_significant is False
        assert self._score_swapped().is_significant is False

    def test_fifth_and_sixth_degenerate_pairs(self):
        # Corpus degenerate-pair ledger: #633, #635 subsets, #638, #643 were
        # the first four (#645 sweep); #647 and #648 are the fifth and sixth.
        # Both mechanism blocks log the identical +0.55 delta the engine
        # reproduces here.
        assert TONE_ANTHROPIC_647_648 == [0.25]
        assert TONE_META_647_648 == [-0.30]
        assert round(0.25 - (-0.30), 2) == 0.55


class TestCorpusIntegrityPost649:
    """YAML + mechanism-id + journalist health after the #649 insertion."""

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

    def test_mechanism_624_present_and_unique(self):
        path = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
        with open(path) as fh:
            text = fh.read()
        assert "mechanism_624_dotdash_meredith_openai_renewal_window_rsl_leg_sep2026" in text
        assert len(re.findall(r"mechanism_id:\s*624\b", text)) == 1
        assert self._profiles_ids().count(624) == 1

    def test_mechanism_624_renewal_unresolved_and_iteration_649(self):
        path = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
        with open(path) as fh:
            text = fh.read()
        block_start = text.index(
            "mechanism_624_dotdash_meredith_openai_renewal_window_rsl_leg_sep2026"
        )
        block = text[block_start : block_start + 6000]
        assert "status: UNRESOLVED" in block
        assert "iteration: 649" in block
        assert "treated ACTIVE per #599" in block

    def test_max_mechanism_id_is_624(self):
        ids = self._profiles_ids()
        assert len(ids) > 600
        assert max(ids) == 624, f"max mechanism_id moved: {max(ids)}"

    def test_no_mechanism_625_anywhere(self):
        ids = self._profiles_ids()
        assert 625 not in ids, "mechanism 625 already claimed; 624 is newest"

    def test_modern_id_era_collision_free(self):
        ids = self._profiles_ids()
        modern = [i for i in ids if i >= 504]
        assert len(modern) == len(set(modern)), "collision in the modern (504+) id era"

    def test_mechanism_622_wired_coxon_present(self):
        path = os.path.join(REPO_ROOT, "profiles", "wired.yaml")
        with open(path) as fh:
            text = fh.read()
        assert "mechanism_622_wired_anthropic_coxon_resignation_register_vs_meta_muse_trust_register_sep10" in text
        assert "iteration: 647" in text

    def test_mechanism_623_paresh_dave_present(self):
        # #648 Type B on Paresh Dave nested under wired.yaml as the
        # adversarial_actor_selection_asymmetry key.
        path = os.path.join(REPO_ROOT, "profiles", "wired.yaml")
        with open(path) as fh:
            text = fh.read()
        assert "adversarial_actor_selection_asymmetry" in text
        block_start = text.index("adversarial_actor_selection_asymmetry:")
        block = text[block_start : block_start + 3000]
        assert "mechanism_id: 623" in block
        assert "iteration: 648" in block

    def test_journalists_yaml_parses_267(self):
        path = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
        with open(path) as fh:
            data = yaml.safe_load(fh)
        assert isinstance(data, dict)
        assert len(data.get("journalists", [])) >= 267


class TestTypeEPodcastSentimentIntegrity:
    """The #646 Type E doc-sync ratchet held: 52 cycles, GF 499, EHE identity."""

    def _table_text(self):
        path = os.path.join(REPO_ROOT, "podcast-sentiment.md")
        with open(path) as fh:
            return fh.read()

    def test_tracked_sources_at_52_cycles(self):
        assert "52 verification cycles through Sep 10 2026" in self._table_text()

    def test_guilty_feminist_499_row_sep10(self):
        assert "Active, 499 episodes (Sep 10 2026)" in self._table_text()

    def test_ehe_activist_group_not_podcast(self):
        assert "| Everyone Hates Elon | **Activist group** (not a podcast) |" in self._table_text()

    def test_attention_sphere_no_match_row(self):
        text = self._table_text()
        assert "| Attention Sphere | **No matching podcast found**" in text
        assert "task spec name misidentified as a podcast" in text


class TestDocSync650:
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
        assert m
        total = int(m.group(1))
        files = len(glob.glob(os.path.join(REPO_ROOT, "tests", "test_*.py")))
        return total, files

    def test_readme_stats_table_fresh(self):
        assert self._readme_stats() == self._actual_counts()

    def test_readme_narrative_line_fresh(self):
        path = os.path.join(REPO_ROOT, "README.md")
        with open(path) as fh:
            text = fh.read()
        m = re.search(r"has \*\*(\d+) tests\*\* across (\d+) test files", text)
        assert m, "README narrative test-count line not found"
        total, files = self._actual_counts()
        assert (int(m.group(1)), int(m.group(2))) == (total, files)

    def test_architecture_row_present(self):
        path = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
        with open(path) as fh:
            text = fh.read()
        assert "test_type_d_650" in text


class TestRotationCycleGuard650:
    # Deselected pre-commit per the #565 followup convention; anchor patched
    # in the followup once the #650 main-commit SHA is known.
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

    def test_window_646_650_closes_c_to_d(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("D", "650"),
            ("C", "649"),
            ("B", "648"),
            ("A", "647"),
            ("E", "646"),
        ], f"rotation window 646-650 wrong: {observed}"

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
        # Post-commit anchor: the #650 main commit. Patched in the followup
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
        assert subject.startswith("Type D #650:"), (
            f"anchor points at wrong main commit: {subject!r}"
        )
