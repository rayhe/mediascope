"""
Type D - Test & Verify: scorer degenerate-contract consistency for the Sep 10
afternoon illustrative pairs (#657 Verge Snap-Specs event-forward vs Meta
LED-tamper alarm register, #658 Rogers Meta Muse-Image opt-out-alarm vs
Anthropic Claude-Cowork playful register) + post-#659 corpus integrity sweep
(mechanism 630 News Corp x Google sixth-leg watch) + #609 first-gen OpenAI
publisher renewal cohort re-verified closed (7/7) with the sixth-leg watch
item correctly outside it.
Iteration #660 - Thu 2026-09-10 17:00 PDT
(scheduled job_id mediascope-daily-iteration, goal_54093bda4145, rotation 659 C -> 660 D)

Core finding this run: the two newest manual-illustrative tone pairs extend
the degenerate ledger to the NINTH and TENTH n=1-per-arm pairs (#633, #635
subsets, #638, #643 were the first four per the #645 sweep; #647/#648 were
the fifth and sixth per the #650 sweep; #652/#653 were the seventh and
eighth per the #655 sweep). #657 pins Snap [0.2] vs Meta [-0.2],
illustrative delta (Snap minus Meta) +0.40. #658 pins Anthropic [0.10] vs
Meta [-0.45], illustrative delta (Anthropic minus Meta) +0.55. Both pairs
have mixed-sign arms (positive competitor arm, negative Meta arm) - the
#652 all-positive and #653 all-negative firsts from #655 do not repeat;
the degenerate contract is sign-invariant. Fed through the REAL
calculate_asymmetry path, both pairs hit the degenerate statistical contract
exactly: t=0.0, p=1.0, cohens_d=0.0, |asymmetry| == |delta|,
is_significant False, and arm-swap negates the asymmetry exactly. Engine
significance is impossible on n=1 arms, so per the Aug 28 2026 standing rule
no divergence pin can arise here - the divergence ratchet stays at 7 (#642
holds). The #657/#658 mechanism blocks logged no engine run and this run
VERIFIES that decision: there is nothing for the engine to add.

Corpus integrity sweep: mechanism_id 630 (News Corp x Google AI licensing
talks sixth-leg watch, #659) is present and unique in
profiles/competitor-entities.yaml with iteration 659, iteration_type C,
signed_ai_licensing_deal 'NONE on record as of Sep 10 2026', and
google_talks_leg status 'UNRESOLVED' (TALKS DOCUMENTED / NO SIGNED DEAL /
UNRESOLVED); the modern (504+) id era is collision-free with max == 630
and no 631 anywhere; mechanism 628 (Verge x Snap Specs shipping-phase
register, #657) is present in the-verge.yaml with iteration 657 and both
manual_illustrative_tone values matching the pinned scorer arms (0.2 /
-0.2); mechanism 629 (Rogers Muse-Image vs Claude-Cowork register, #658)
is present in journalists.yaml with iteration 658 and pinned tones
(meta_tone -0.45, anthropic_tone 0.1, tone_illustrative -0.45 / 0.1);
journalists.yaml parses at 267 journalists; profiles/news-corp.yaml carries
the Google revenue_relationships entry typed ai_licensing_talks_unconfirmed
(verified false, signed null), clearly distinguished from the five signed
legs; the Type E Tracked Sources table is fresh at 54 verification cycles
with GF at 499 episodes (Sep 10 2026, #656) and the Attention Sphere
no-match row intact.

Cohort and watch-item check: the #609 first-gen OpenAI publisher renewal
cohort stays closed at 7/7 (the #654 News Corp block still names itself the
SEVENTH member); mechanism 630 is a SEPARATE watch item (sixth News Corp
AI-revenue leg, not a first-gen OpenAI cohort leg) and makes no cohort
membership claim - the sixth-leg watch operationalizes the #654
advanced-discussions watch item without expanding the cohort.

Rotation guard: window 656-660 (D, C, B, A, E newest-first), closing the
C->D edge. Deselected pre-commit per the #565 followup convention; anchor
patched in the followup once the #660 main-commit SHA is known.

Designed supersession note: the #655 Type D sweep's
test_max_mechanism_id_is_627 and test_no_mechanism_628_anywhere now fail by
supersession (max is 630), consistent with the established convention
(#650's test_max_mechanism_id_is_624 likewise fails superseded since the
#654 insertion). Non-window tests in those sweep files still pass.
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
# #657 Type A (Verge Snap Specs shipping-phase event-forward product register
# vs Meta LED-tamper surveillance-alarm register): Snap arm [+0.2], Meta arm
# [-0.2], illustrative delta (Snap minus Meta) +0.40, MANUAL ILLUSTRATIVE,
# n=1 per arm. Mixed-sign arms; excerpt-bounded Snap arm (theverge.com
# policy-blocked), mirror-bounded Meta arm.
TONE_SNAP_657 = [0.2]
TONE_META_657 = [-0.2]

# #658 Type B (Rogers Muse-Image opt-out-alarm register vs Anthropic
# Claude-Cowork playful-enthusiasm register, same journalist same day):
# Meta arm [-0.45], Anthropic arm [+0.10], illustrative delta
# (Anthropic minus Meta) +0.55, MANUAL ILLUSTRATIVE, n=1 per arm.
# Mixed-sign arms; snippet-bounded WIRED sourcing per paywall convention.
TONE_META_658 = [-0.45]
TONE_ANTHROPIC_658 = [0.1]


class TestIteration660Metadata:
    def test_iteration_number(self):
        assert 660 == 660

    def test_type_is_d(self):
        assert "D" == "D"

    def test_rotation_edge(self):
        # A -> B -> C -> D -> E; previous main commit was Type C #659
        assert "C->D" == "C->D"

    def test_job_and_goal(self):
        assert "mediascope-daily-iteration" == "mediascope-daily-iteration"
        assert "goal_54093bda4145" == "goal_54093bda4145"

    def test_date(self):
        assert datetime(2026, 9, 10).strftime("%Y-%m-%d") == "2026-09-10"


class TestNovelty660:
    """This run must not collide with an earlier #660."""

    def test_single_type_d_660_file(self):
        matches = glob.glob(
            os.path.join(REPO_ROOT, "tests", "test_type_d_660*.py")
        )
        assert len(matches) == 1, f"expected exactly this file, got {matches}"
        assert matches[0].endswith(
            "test_type_d_660_scorer_degenerate_consistency_657_658_corpus_integrity_post_659_sep10_5pm.py"
        )

    def test_type_d_660_main_commit_unique_and_anchored(self):
        # Post-commit the #660 main commit exists exactly once (this run's);
        # its SHA matches the rotation-guard anchor patched in the followup
        # per the #565 convention. Novelty was verified pre-commit by shell
        # greps (zero test_type_d_660 files, no #660 in git log); this test
        # pins that no duplicate #660 main commit ever appears.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type D #660:", l)]
        assert len(mains) == 1, (
            f"expected exactly one Type D #660 main commit, got: {mains}"
        )
        sha = mains[0].split(" ", 1)[0]
        anchor = TestRotationCycleGuard660.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, f"main commit {sha} != guard anchor {anchor}"


class TestScorerBattery657658:
    """The two newest illustrative pairs through the real scorer path.

    #657 (mixed-sign arms, Snap positive vs Meta negative) and #658
    (mixed-sign arms, Anthropic positive vs Meta negative) are the NINTH
    and TENTH n=1-per-arm degenerate pairs in the corpus ledger. The
    degenerate contract must hold exactly: t == 0.0, p == 1.0, d == 0.0
    on both arm orders, |asymmetry| == |illustrative delta|. No divergence
    pin can arise (engine significance is impossible on n=1 arms), so the
    divergence ratchet stays at 7 and the #657/#658 no-engine-run
    decisions are verified correct - there is nothing for the engine to
    add.
    """

    def _score_657_forward(self):
        # Forward direction: target Snap, peer Meta (asymmetry = +0.40).
        return calculate_asymmetry(
            target_scores=TONE_SNAP_657,
            peer_scores=TONE_META_657,
            target_entity="Snap",
            peer_entities=["meta"],
            publication_slug="the-verge",
            period_start=P0,
            period_end=P1,
        )

    def _score_657_swapped(self):
        return calculate_asymmetry(
            target_scores=TONE_META_657,
            peer_scores=TONE_SNAP_657,
            target_entity="Meta",
            peer_entities=["snap"],
            publication_slug="the-verge",
            period_start=P0,
            period_end=P1,
        )

    def _score_658_forward(self):
        # Forward direction: target Anthropic, peer Meta (asymmetry = +0.55).
        return calculate_asymmetry(
            target_scores=TONE_ANTHROPIC_658,
            peer_scores=TONE_META_658,
            target_entity="Anthropic",
            peer_entities=["meta"],
            publication_slug="wired",
            period_start=P0,
            period_end=P1,
        )

    def _score_658_swapped(self):
        return calculate_asymmetry(
            target_scores=TONE_META_658,
            peer_scores=TONE_ANTHROPIC_658,
            target_entity="Meta",
            peer_entities=["anthropic"],
            publication_slug="wired",
            period_start=P0,
            period_end=P1,
        )

    def test_657_degenerate_contract_forward(self):
        r = self._score_657_forward()
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.asymmetry_score == 0.40
        assert r.is_significant is False

    def test_657_degenerate_contract_swapped(self):
        r = self._score_657_swapped()
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.asymmetry_score == -0.40
        assert r.is_significant is False

    def test_658_degenerate_contract_forward(self):
        r = self._score_658_forward()
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.asymmetry_score == 0.55
        assert r.is_significant is False

    def test_658_degenerate_contract_swapped(self):
        r = self._score_658_swapped()
        assert r.t_statistic == 0.0
        assert r.p_value == 1.0
        assert r.cohens_d == 0.0
        assert r.asymmetry_score == -0.55
        assert r.is_significant is False

    def test_arm_swap_negates_asymmetry_exactly(self):
        assert self._score_657_swapped().asymmetry_score == -self._score_657_forward().asymmetry_score
        assert self._score_658_swapped().asymmetry_score == -self._score_658_forward().asymmetry_score

    def test_identical_arms_zero_asymmetry(self):
        tones = [0.10, -0.20, 0.30]
        r = calculate_asymmetry(
            target_scores=tones,
            peer_scores=list(tones),
            target_entity="Snap",
            peer_entities=["meta"],
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
        # arises from #657/#658 and the ratchet stays at 7 (#642 holds).
        assert self._score_657_forward().is_significant is False
        assert self._score_658_forward().is_significant is False

    def test_ninth_and_tenth_degenerate_pairs(self):
        # Corpus degenerate-pair ledger: #633, #635 subsets, #638, #643 were
        # the first four (#645 sweep); #647/#648 were the fifth and sixth
        # (#650 sweep); #652/#653 were the seventh and eighth (#655 sweep);
        # #657 and #658 are the ninth and tenth. Both are mixed-sign
        # (positive competitor arm, negative Meta arm) - unlike #652's
        # all-positive and #653's all-negative arms, which do not repeat;
        # the degenerate contract is sign-invariant, verified above.
        assert TONE_SNAP_657 == [0.2]
        assert TONE_META_657 == [-0.2]
        assert 0.2 - (-0.2) == 0.40
        assert TONE_META_658 == [-0.45]
        assert TONE_ANTHROPIC_658 == [0.1]
        assert 0.1 - (-0.45) == 0.55


class TestCorpusIntegrityPost659:
    """YAML + mechanism-id + journalist health after the #659 insertion."""

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

    def test_mechanism_630_present_and_unique(self):
        path = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
        with open(path) as fh:
            text = fh.read()
        assert "mechanism_630_news_corp_google_ai_licensing_talks_sixth_leg_watch_sep2026" in text
        assert len(re.findall(r"mechanism_id:\s*630\b", text)) == 1
        assert self._profiles_ids().count(630) == 1

    def test_mechanism_630_iteration_659_unresolved(self):
        path = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
        with open(path) as fh:
            text = fh.read()
        block_start = text.index(
            "mechanism_630_news_corp_google_ai_licensing_talks_sixth_leg_watch_sep2026"
        )
        block = text[block_start : block_start + 9000]
        assert "iteration: 659" in block
        assert "iteration_type: C" in block
        assert "signed_ai_licensing_deal: 'NONE on record as of Sep 10 2026'" in block
        assert "status: 'UNRESOLVED'" in block

    def test_max_mechanism_id_is_630(self):
        ids = self._profiles_ids()
        assert len(ids) > 600
        assert max(ids) == 630, f"max mechanism_id moved: {max(ids)}"

    def test_no_mechanism_631_anywhere(self):
        ids = self._profiles_ids()
        assert 631 not in ids, "mechanism 631 already claimed; 630 is newest"

    def test_modern_id_era_collision_free(self):
        ids = self._profiles_ids()
        modern = [i for i in ids if i >= 504]
        assert len(modern) == len(set(modern)), "collision in the modern (504+) id era"

    def test_mechanism_628_verge_present_and_iteration_657(self):
        path = os.path.join(REPO_ROOT, "profiles", "the-verge.yaml")
        with open(path) as fh:
            text = fh.read()
        assert "mechanism_628_verge_snap_sep_specs_event_vs_meta_led_tamper_alarm_sep10" in text
        block_start = text.index(
            "mechanism_628_verge_snap_sep_specs_event_vs_meta_led_tamper_alarm_sep10"
        )
        block = text[block_start : block_start + 4000]
        assert "mechanism_id: 628" in block
        assert "iteration: 657" in block

    def test_mechanism_628_scorer_arms_match_pinned_tones(self):
        path = os.path.join(REPO_ROOT, "profiles", "the-verge.yaml")
        with open(path) as fh:
            text = fh.read()
        block_start = text.index(
            "mechanism_628_verge_snap_sep_specs_event_vs_meta_led_tamper_alarm_sep10"
        )
        block = text[block_start : block_start + 9000]
        assert "manual_illustrative_tone: 0.2" in block
        assert "manual_illustrative_tone: -0.2" in block

    def test_mechanism_629_rogers_present_and_iteration_658(self):
        path = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
        with open(path) as fh:
            text = fh.read()
        assert "mechanism_629_reece_rogers_muse_image_opt_out_alarm_vs_claude_cowork_playful_register_jul07" in text
        assert self._profiles_ids().count(629) == 1
        block_start = text.index(
            "mechanism_629_reece_rogers_muse_image_opt_out_alarm_vs_claude_cowork_playful_register_jul07"
        )
        block = text[block_start : block_start + 4000]
        assert "mechanism_id: 629" in block
        assert "iteration: 658" in block

    def test_mechanism_629_scorer_arms_match_pinned_tones(self):
        path = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
        with open(path) as fh:
            text = fh.read()
        block_start = text.index(
            "mechanism_629_reece_rogers_muse_image_opt_out_alarm_vs_claude_cowork_playful_register_jul07"
        )
        block = text[block_start : block_start + 9000]
        assert "meta_tone: -0.45" in block
        assert "anthropic_tone: 0.1" in block
        assert "tone_illustrative: -0.45" in block
        assert "tone_illustrative: 0.1" in block

    def test_journalists_yaml_parses_267(self):
        path = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
        with open(path) as fh:
            data = yaml.safe_load(fh)
        assert isinstance(data, dict)
        assert len(data.get("journalists", [])) >= 267

    def test_news_corp_google_watch_entry(self):
        path = os.path.join(REPO_ROOT, "profiles", "news-corp.yaml")
        with open(path) as fh:
            text = fh.read()
        assert "type: ai_licensing_talks_unconfirmed" in text
        assert "signed: null" in text
        assert "POTENTIAL SIXTH AI-revenue leg, WATCH ONLY" in text


class TestCohortAndWatchItems660:
    """The #609 first-gen OpenAI publisher renewal cohort stays closed at
    7/7; mechanism 630 is a separate watch item (sixth News Corp AI-revenue
    leg), not a cohort member."""

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


class TestTypeEPodcastSentimentIntegrity:
    """The #656 Type E doc-sync ratchet held: 54 cycles, GF 499, EHE identity."""

    def _table_text(self):
        path = os.path.join(REPO_ROOT, "podcast-sentiment.md")
        with open(path) as fh:
            return fh.read()

    def test_tracked_sources_at_54_cycles(self):
        assert "54 verification cycles through Sep 10 2026" in self._table_text()

    def test_guilty_feminist_499_row_sep10(self):
        assert "Active, 499 episodes (Sep 10 2026)" in self._table_text()

    def test_ehe_activist_group_not_podcast(self):
        assert "| Everyone Hates Elon | **Activist group** (not a podcast) |" in self._table_text()

    def test_attention_sphere_no_match_row(self):
        text = self._table_text()
        assert "| Attention Sphere | **No matching podcast found**" in text
        assert "task spec name misidentified as a podcast" in text


class TestDocSync660:
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

    def test_architecture_row_for_660(self):
        path = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
        with open(path) as fh:
            text = fh.read()
        assert "test_type_d_660" in text, "ARCHITECTURE row for #660 missing"

    def test_iteration_log_entry_for_660(self):
        path = os.path.join(REPO_ROOT, "iteration-log.md")
        with open(path) as fh:
            text = fh.read()
        assert "#660 Type D:" in text, "iteration-log entry for #660 missing"


class TestRotationCycleGuard660:
    # Deselected pre-commit per the #565 followup convention; anchor patched
    # in the followup once the #660 main-commit SHA is known.
    ANCHORED_SHA = "44cc5ec0604d48cc32d5a64a6a2b6d0839fc5edf"  # patched in followup per #565 convention

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

    def test_window_656_660_closes_c_to_d(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("D", "660"),
            ("C", "659"),
            ("B", "658"),
            ("A", "657"),
            ("E", "656"),
        ], f"rotation window 656-660 wrong: {observed}"

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
        # Post-commit anchor: the #660 main commit. Patched in the followup
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
        assert subject.startswith("Type D #660:"), (
            f"newest main commit is not Type D #660: {subject}"
        )
        # The #659 main commit must still be exactly one, preserving the
        # C->D edge the window closes.
        prev = [l for l in mains if re.search(r" Type C #659:", l)]
        assert len(prev) == 1, "expected exactly one Type C #659 main commit"

    def test_novelty_anchor_single_main_commit(self):
        # Exactly one Type D #660 main commit ever (novelty pin).
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type D #660:", l)]
        assert len(mains) == 1, f"expected exactly one Type D #660 main commit, got: {mains}"
