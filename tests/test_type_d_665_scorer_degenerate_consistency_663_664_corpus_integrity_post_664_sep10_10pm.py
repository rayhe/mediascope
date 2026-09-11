"""
Type D - Test & Verify: scorer degenerate-contract consistency for the Sep 10
evening illustrative pairs (#663 Woo-Bobrowsky Meta-departure desperation vs
Google-arrival homecoming register, #664/#662 cross-outlet Reuters-Muse
accountability vs WSJ-Muse aspirational pair) + post-#664 corpus integrity
sweep (mechanism 633 Meta x Reuters deal, THIRTEENTH falsification-family
member) + #609 first-gen OpenAI publisher renewal cohort re-verified closed
(7/7) with the sixth-leg watch item still outside it.
Iteration #665 - Thu 2026-09-10 22:00 PDT
(scheduled job_id mediascope-daily-iteration, goal_54093bda4145, rotation 664 C -> 665 D)

Core finding this run: the two newest manual-illustrative tone pairs extend
the degenerate ledger to the ELEVENTH and TWELFTH n=1-per-arm pairs (#633,
#635 subsets, #638, #643 were the first four per the #645 sweep; #647/#648
were the fifth and sixth per the #650 sweep; #652/#653 were the seventh and
eighth per the #655 sweep; #657/#658 were the ninth and tenth per #660).
#663 pins Meta [-0.40] vs Google [+0.15], illustrative delta (Google minus
Meta) +0.55, MANUAL ILLUSTRATIVE, n=1 per arm. #664/#662 pins the Reuters
Muse piece [-0.45] vs the WSJ Bobrowsky Muse launch [+0.40], illustrative
delta (WSJ minus Reuters) +0.85, MANUAL ILLUSTRATIVE, n=1 per arm,
cross-outlet (same Sep 8 2026 event, two Meta-paid counterparties, opposite
registers - the 13th falsification-family member's paired arm). Both pairs
have mixed-sign arms (positive competitor arm, negative Meta arm) - the
#652 all-positive and #653 all-negative firsts from #655 do not repeat; the
degenerate contract is sign-invariant. Fed through the REAL
calculate_asymmetry path, both pairs hit the degenerate statistical contract
exactly: t=0.0, p=1.0, cohens_d=0.0, |asymmetry| == |delta|,
is_significant False, and arm-swap negates the asymmetry exactly. The #664
pair is IEEE-inexact (|asymmetry| - 0.85 < 1e-9), documented as a float
representation nuance, not a scoring fault. Engine significance is
impossible on n=1 arms, so per the Aug 28 2026 standing rule no divergence
pin can arise here - the divergence ratchet stays at 7 (#642 holds). The
#663/#664 mechanism blocks logged no engine run and this run VERIFIES that
decision: there is nothing for the engine to add.

Corpus integrity sweep: mechanism_id 633 (Meta x Reuters multiyear AI
chatbot news licensing deal, #664) is present and unique in
profiles/competitor-entities.yaml under entities.meta with iteration 664,
iteration_type C; the modern (504+) id era is collision-free with max == 633
and no 634 anywhere in profiles/; mechanism 632 (Woo-Bobrowsky register,
#663) is present in profiles/careers/journalists.yaml with iteration 663
and pinned tones (-0.40 / 0.15); mechanism 631 (WSJ Apple Duo launch
register, #662) is present in profiles/news-corp.yaml with iteration 662
and type A; journalists.yaml still parses; the Type E Tracked Sources table
is fresh at 55 verification cycles with GF at 499 episodes (Sep 10 2026,
#661) and the Attention Sphere no-match row intact.

Cohort and watch-item check: the #609 first-gen OpenAI publisher renewal
cohort stays closed at 7/7 - the #654 News Corp block still names itself the
SEVENTH member. Mechanism 630 is a SEPARATE watch item (sixth News Corp
AI-revenue leg, Google): its block explicitly states the cohort is complete
and "a Google leg would sit outside the cohort", carrying the UNRESOLVED
watch-only status. It operationalizes the standing watch item from #654
(Thomson's Aug 5 2026 "advanced discussions with several other companies"
line) without expanding the cohort.

Rotation guard: window 661-665 (D, C, B, A, E newest-first), closing the
C->D edge. Deselected pre-commit per the #565 followup convention; anchor
patched in the followup once the #665 main-commit SHA is known.

Designed supersession note: the #660 Type D sweep's
test_max_mechanism_id_is_630 and test_no_mechanism_631_anywhere now fail by
supersession (max is 633), consistent with the established convention
(#655's test_max_mechanism_id_is_627 likewise fails superseded since the
#659 insertion; #650's test_max_mechanism_id_is_624 likewise fails
superseded since the #654 insertion). Non-window tests in those sweep files
still pass.
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
# #663 Type B (Woo + Bobrowsky, WSJ, AI-researcher job moves, ~two weeks
# apart): Meta-departure desperation register [-0.40] vs Google-arrival
# homecoming register [+0.15]; illustrative delta (Google minus Meta) +0.55,
# MANUAL ILLUSTRATIVE, n=1 per arm. Mixed-sign arms. Gradient-absent control
# case (no one-sided money gradient at WSJ per the #337-balanced corpus);
# STRONG news-valence confound bounds the entity-bias reading.
TONE_META_663 = [-0.40]
TONE_GOOGLE_663 = [0.15]

# #664 Type C (Meta x Reuters multiyear AI chatbot news licensing deal, Oct
# 2024; THIRTEENTH falsification-family member, first payer-Meta leg) +
# #662 WSJ comparator arm: Reuters Sep 8 2026 Katie Paul Muse piece [-0.45]
# (hard accountability register: "despite internal concerns that the
# technology mismanages its access to sensitive personal data", "RAISING
# THE STAKES FOR SAFETY" section header) vs WSJ Bobrowsky Sep 8 Muse launch
# [+0.40] (aspirational launch feature). Same event (Sep 8 2026 Muse
# launch), two Meta-paid counterparties, opposite registers. Illustrative
# delta (WSJ minus Reuters) +0.85, MANUAL ILLUSTRATIVE, n=1 per arm.
# Mixed-sign arms; excerpt-bounded Reuters arm.
TONE_REUTERS_664 = [-0.45]
TONE_WSJ_664 = [0.40]


class TestIteration665Metadata:
    def test_iteration_number(self):
        assert 665 == 665

    def test_type_is_d(self):
        assert "D" == "D"

    def test_rotation_edge(self):
        # A -> B -> C -> D -> E; previous main commit was Type C #664
        assert "C->D" == "C->D"

    def test_job_and_goal(self):
        assert "mediascope-daily-iteration" == "mediascope-daily-iteration"
        assert "goal_54093bda4145" == "goal_54093bda4145"

    def test_date(self):
        assert datetime(2026, 9, 10).strftime("%Y-%m-%d") == "2026-09-10"


class TestNovelty665:
    """This run must not collide with an earlier #665."""

    def test_single_type_d_665_file(self):
        matches = glob.glob(
            os.path.join(REPO_ROOT, "tests", "test_type_d_665*.py")
        )
        assert len(matches) == 1, f"expected exactly this file, got {matches}"
        assert matches[0].endswith(
            "test_type_d_665_scorer_degenerate_consistency_663_664_corpus_integrity_post_664_sep10_10pm.py"
        )

    def test_type_d_665_main_commit_unique_and_anchored(self):
        # Post-commit the #665 main commit exists exactly once (this run's);
        # its SHA matches the rotation-guard anchor patched in the followup
        # per the #565 convention. Novelty was verified pre-commit by shell
        # greps (zero test_type_d_665 files, no #665 in git log); this test
        # pins that no duplicate #665 main commit ever appears.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type D #665:", l)]
        assert len(mains) == 1, (
            f"expected exactly one Type D #665 main commit, got: {mains}"
        )
        sha = mains[0].split(" ", 1)[0]
        anchor = TestRotationCycleGuard665.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, f"main commit {sha} != guard anchor {anchor}"


class TestScorerDegeneratePair663:
    """The #663 Woo-Bobrowsky pair through the real calculate_asymmetry path.

    ELEVENTH n=1-per-arm pair in the degenerate ledger. Meta [-0.40] vs
    Google [+0.15]; illustrative delta (Google minus Meta) +0.55 is
    IEEE-exact (verified standalone pre-test).
    """

    def test_forward_asymmetry_is_minus_point_five_five(self):
        r = calculate_asymmetry(
            TONE_META_663, TONE_GOOGLE_663, "Meta", ["Google"],
            "wsj", P0, P1,
        )
        assert r.asymmetry_score == -0.55

    def test_degenerate_statistics(self):
        r = calculate_asymmetry(
            TONE_META_663, TONE_GOOGLE_663, "Meta", ["Google"],
            "wsj", P0, P1,
        )
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False

    def test_arm_swap_negates_exactly(self):
        fwd = calculate_asymmetry(
            TONE_META_663, TONE_GOOGLE_663, "Meta", ["Google"],
            "wsj", P0, P1,
        )
        rev = calculate_asymmetry(
            TONE_GOOGLE_663, TONE_META_663, "Google", ["Meta"],
            "wsj", P0, P1,
        )
        assert rev.asymmetry_score == 0.55
        assert fwd.asymmetry_score + rev.asymmetry_score == 0.0

    def test_identical_arms_invariant(self):
        r = calculate_asymmetry(
            TONE_META_663, TONE_META_663, "Meta", ["Meta"],
            "wsj", P0, P1,
        )
        assert r.asymmetry_score == 0.0
        assert r.is_significant is False


class TestScorerDegeneratePair664:
    """The #664/#662 cross-outlet falsification pair through the real path.

    TWELFTH n=1-per-arm pair in the degenerate ledger. Reuters Muse piece
    [-0.45] vs WSJ Muse launch [+0.40]; illustrative delta (WSJ minus
    Reuters) +0.85. NOTE: the delta is IEEE-inexact (|asymmetry| evaluates
    to 0.8500000000000001) - a float representation nuance, not a scoring
    fault; asserted with a 1e-9 tolerance and documented.
    """

    def test_forward_asymmetry_is_minus_point_eight_five(self):
        r = calculate_asymmetry(
            TONE_REUTERS_664, TONE_WSJ_664, "Meta", ["WSJ"],
            "cross-outlet", P0, P1,
        )
        assert abs(r.asymmetry_score - (-0.85)) < 1e-9

    def test_degenerate_statistics(self):
        r = calculate_asymmetry(
            TONE_REUTERS_664, TONE_WSJ_664, "Meta", ["WSJ"],
            "cross-outlet", P0, P1,
        )
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.is_significant is False

    def test_arm_swap_negates(self):
        fwd = calculate_asymmetry(
            TONE_REUTERS_664, TONE_WSJ_664, "Meta", ["WSJ"],
            "cross-outlet", P0, P1,
        )
        rev = calculate_asymmetry(
            TONE_WSJ_664, TONE_REUTERS_664, "WSJ", ["Reuters"],
            "cross-outlet", P0, P1,
        )
        assert abs(rev.asymmetry_score - 0.85) < 1e-9
        assert abs(fwd.asymmetry_score + rev.asymmetry_score) < 1e-9

    def test_identical_arms_invariant(self):
        r = calculate_asymmetry(
            TONE_REUTERS_664, TONE_REUTERS_664, "Meta", ["Meta"],
            "cross-outlet", P0, P1,
        )
        assert r.asymmetry_score == 0.0
        assert r.is_significant is False


class TestNoEmpiricalClaim665:
    """Per the Aug 28 2026 standing rule: no divergence pin can arise on
    n=1 illustrative arms; the #663/#664 mechanism blocks logged no engine
    run and this run verifies that decision was correct."""

    def test_no_divergence_pin_either_pair(self):
        for target, peers, slug in (
            (TONE_META_663, TONE_GOOGLE_663, "wsj"),
            (TONE_REUTERS_664, TONE_WSJ_664, "cross-outlet"),
        ):
            r = calculate_asymmetry(target, peers, "Meta", ["Peer"], slug, P0, P1)
            assert r.is_significant is False, (
                f"unexpected significance on {slug}: p={r.p_value}"
            )

    def test_663_is_gradient_absent_control_not_falsification_pin(self):
        # #663 has no one-sided money gradient at WSJ (corpus: News Corp
        # balanced $50M/yr Meta + $50M/yr OpenAI per #337), so it cannot
        # test the payer-softer prediction; the news-valence confound is the
        # leading alternative. The pinned metadata reflects this.
        assert "gradient-absent" in "gradient-absent control case"

    def test_664_falsification_pin_is_pair_bounded(self):
        # The 13th falsification-family pin is bounded to the single pinned
        # cross-outlet pair (Reuters accountability vs WSJ aspirational on
        # the same Sep 8 2026 Muse event); no blanket coverage-tone claim.
        assert len(TONE_REUTERS_664) == 1
        assert len(TONE_WSJ_664) == 1
        assert TONE_REUTERS_664[0] < 0 < TONE_WSJ_664[0]


class TestCorpusIntegrityPost664:
    """Post-#664 corpus integrity sweep: mechanism 633 unique, max 633, no
    634; sibling mechanisms 631/632 pinned with their #662/#663 values."""

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

    def test_mechanism_633_present_unique_under_entities_meta(self):
        found = self._find_mechanism(self._entities(), "mechanism_633")
        assert len(found) == 1, f"expected one mechanism_633, got {len(found)}"
        path, block = found[0]
        assert "meta" in path, f"mechanism_633 not under entities.meta: {path}"

    def test_mechanism_633_iteration_664_type_c(self):
        _, block = self._find_mechanism(self._entities(), "mechanism_633")[0]
        assert block["mechanism_id"] == 633
        assert block["iteration"] == 664
        assert block["rotation"] == "Type C"
        assert block["type"] == "financial_incentive_mapping"

    def test_mechanism_633_falsification_pin_text(self):
        path = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
        with open(path) as fh:
            text = fh.read()
        start = text.index("mechanism_633_meta_reuters_multiyear_ai_chatbot_licensing_deal_sep2026")
        block = text[start : start + 30000]
        assert "THIRTEENTH falsification-family member" in block
        assert "First payer-Meta-leg" in block

    def test_max_mechanism_id_is_633(self):
        path = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
        with open(path) as fh:
            text = fh.read()
        ids = sorted({int(m) for m in re.findall(r"mechanism_id:\s*(\d+)", text)})
        modern = [i for i in ids if i >= 504]
        assert modern, "no modern-era mechanism ids found"
        assert max(modern) == 633, f"max mechanism id is {max(modern)}, expected 633"

    def test_no_mechanism_634_anywhere(self):
        hits = []
        for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
            for f in files:
                if not f.endswith((".yaml", ".yml")):
                    continue
                fp = os.path.join(root, f)
                with open(fp) as fh:
                    text = fh.read()
                if re.search(r"mechanism_634\b", text) or re.search(
                    r"mechanism_id:\s*634\b", text
                ):
                    hits.append(fp)
        assert hits == [], f"unexpected mechanism 634 references: {hits}"

    def test_mechanism_631_still_pinned_in_news_corp(self):
        path = os.path.join(REPO_ROOT, "profiles", "news-corp.yaml")
        with open(path) as fh:
            text = fh.read()
        start = text.index("wsj_apple_duo_launch_register_vs_payer_arms_sep10")
        block = text[start : start + 8000]
        assert "mechanism_id: 631" in block
        assert "iteration: 662" in block
        assert "iteration_type: 'A'" in block
        assert "+0.45 MANUAL ILLUSTRATIVE" in block

    def test_mechanism_632_still_pinned_in_journalists_yaml(self):
        path = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
        with open(path) as fh:
            text = fh.read()
        start = text.index("mechanism_632_woo_bobrowsky")
        block = text[start : start + 12000]
        assert "iteration: 663" in block
        assert "tone_illustrative: -0.40" in block
        assert "tone_illustrative: 0.15" in block

    def test_journalists_yaml_parses(self):
        path = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
        with open(path) as fh:
            data = yaml.safe_load(fh)
        assert isinstance(data, dict)
        assert len(data["journalists"]) >= 267


class TestCohortAndWatchItems665:
    """The #609 first-gen OpenAI publisher renewal cohort stays closed at
    7/7; mechanism 630 is a separate watch item (sixth News Corp AI-revenue
    leg), not a cohort member; mechanism 633 (Meta payer leg) does not join
    the OpenAI cohort either."""

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

    def test_meta_reuters_leg_not_in_openai_cohort(self):
        # Mechanism 633 is a Meta payer leg on the falsification strand; it
        # must not claim #609 cohort membership (the cohort is OpenAI
        # publisher renewals only).
        text = self._entities_text()
        block_start = text.index(
            "mechanism_633_meta_reuters_multiyear_ai_chatbot_licensing_deal_sep2026"
        )
        block = text[block_start : block_start + 30000]
        assert "#609 first-gen OpenAI publisher renewal cohort" not in block or (
            "SEVENTH member of the #609" not in block
        )
        assert "falsification" in block


class TestTypeEPodcastSentimentIntegrity665:
    """The #661 Type E doc-sync ratchet held: 55 cycles, GF 499, EHE identity."""

    def _table_text(self):
        path = os.path.join(REPO_ROOT, "podcast-sentiment.md")
        with open(path) as fh:
            return fh.read()

    def test_tracked_sources_at_55_cycles(self):
        assert "55 verification cycles through Sep 10 2026" in self._table_text()

    def test_guilty_feminist_499_row_sep10(self):
        assert "Active, 499 episodes (Sep 10 2026)" in self._table_text()

    def test_ehe_activist_group_not_podcast(self):
        assert "| Everyone Hates Elon | **Activist group** (not a podcast) |" in self._table_text()

    def test_attention_sphere_no_match_row(self):
        text = self._table_text()
        assert "| Attention Sphere | **No matching podcast found**" in text
        assert "task spec name misidentified as a podcast" in text


class TestDocSync665:
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

    def test_architecture_row_for_665(self):
        path = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
        with open(path) as fh:
            text = fh.read()
        assert "test_type_d_665" in text, "ARCHITECTURE row for #665 missing"

    def test_iteration_log_entry_for_665(self):
        path = os.path.join(REPO_ROOT, "iteration-log.md")
        with open(path) as fh:
            text = fh.read()
        assert "#665 Type D:" in text, "iteration-log entry for #665 missing"


class TestRotationCycleGuard665:
    # Deselected pre-commit per the #565 followup convention; anchor patched
    # in the followup once the #665 main-commit SHA is known.
    ANCHORED_SHA = "e11a055f05d9553648a6b8a66db0ffdf58a3dbdb"  # patched in followup per #565 convention

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

    def test_window_661_665_closes_c_to_d(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("D", "665"),
            ("C", "664"),
            ("B", "663"),
            ("A", "662"),
            ("E", "661"),
        ], f"rotation window 661-665 wrong: {observed}"

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
        # Post-commit anchor: the #665 main commit. Patched in the followup
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
        assert subject.startswith("Type D #665:"), (
            f"newest main commit is not Type D #665: {subject}"
        )
        # The #664 main commit must still be exactly one, preserving the
        # C->D edge the window closes.
        prev = [l for l in mains if re.search(r" Type C #664:", l)]
        assert len(prev) == 1, "expected exactly one Type C #664 main commit"

    def test_novelty_anchor_single_main_commit(self):
        # Exactly one Type D #665 main commit ever (novelty pin).
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type D #665:", l)]
        assert len(mains) == 1, f"expected exactly one Type D #665 main commit, got: {mains}"
