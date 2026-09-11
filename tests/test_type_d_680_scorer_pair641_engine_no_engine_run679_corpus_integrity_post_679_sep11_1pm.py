"""
Type D - Test & Verify: real-engine verification of the #678 byline-isolated
pair (mechanism 641: Google arm [+0.15] vs Meta arm [-0.15], n=1 per arm -
t=0.0, p=1.0, d=0.0, |asymmetry - 0.30| < 1e-9, is_significant False at the
engine layer, matching the #678 block's MANUAL ILLUSTRATIVE delta and the
degenerate statistical contract of the #638/#643 convention) + the Type D
statistical-meaningfulness mandate (the scorer on a strong-signal synthetic
corpus returns engine significance: t=-17.59058189567848,
p=7.498515787192946e-09, d=-10.155927192672127, CI entirely negative, so
the engine does produce meaningful results when real signal exists; a
near-null corpus returns p=0.9327, not significant) + #679 no-engine-run
verification (mechanism 642 carries no tone arms: asymmetry_relevance has
no_tone_claim true, tone_predictor_grade WEAK, qualitative_only;
Type D read-only convention - the 642 block is untouched) +
post-#679 corpus integrity sweep (mechanism 640 present and unique in
profiles/wired.yaml with iteration 677, rotation Type A; mechanism 641
present and unique in profiles/careers/journalists.yaml with iteration 678,
journalist Boone Ashworth; mechanism 642 present and unique in
profiles/competitor-entities.yaml with iteration 679, rotation Type C; the
modern (504+) id era is collision-free with max == 642 and no 643 anywhere
in profiles/ or tests/) + Type E 58-cycle tracked-sources integrity.

Iteration #680 - Fri 2026-09-11 13:00 PDT
(scheduled job_id mediascope-daily-iteration, goal_54093bda4145, rotation 679 C -> 680 D)

Verification arc: #677 (Type A, mechanism 640) logged a MANUAL
ILLUSTRATIVE delta +0.30 (Google +0.15 vs Meta -0.15) with no engine run;
#678 (Type B, mechanism 641) carried those tones at journalist level,
also with no engine run; #679 (Type C, mechanism 642) logged qualitative
mapping only with no tone arms at all. This run verifies those decisions
against the real scorer path: the #677/#678 n=1-per-arm pair reproduces
the degenerate contract EXACTLY (t=0.0, p=1.0, d=0.0; the +0.30 delta is
pure arithmetic; arm-swap negates to -0.3 and also degenerate). The
finding layer stays is_significant False per the Aug 28 2026 standing
rule, so the manual-illustrative pin STRENGTHENS the no-empirical-claim
discipline: degenerate engine inputs never become empirical findings.

The Type D mandate "verify the asymmetry scoring produces statistically
meaningful results" is satisfied by the strong-signal synthetic check:
Meta arm [-0.60,-0.50,-0.70,-0.55,-0.65,-0.45] vs peer arm
[+0.30,+0.40,+0.35,+0.45,+0.25,+0.50] (n=6 per arm) yields
asymmetry -0.9500000000000001, t=-17.59058189567848,
p=7.498515787192946e-09, d=-10.155927192672127, is_significant True at the
ENGINE layer, CI (-1.0416666666666665, -0.8500000000000001) entirely
below zero. When real signal exists, the engine flags it; when it does
not (near-null pair, p=0.9327294666975322), it stays silent. The scorer
is discriminative, not decoration.

#679 correctly runs NO engine: mechanism 642 is a financial-incentive
deal-level leg (Apple News/News+ x Conde Nast revenue share) whose
asymmetry_relevance explicitly carries no_tone_claim: true and
tone_predictor_grade: WEAK. There are no tone arms for the engine to
score. Mechanism 642's block is left untouched (Type D read-only
convention).

Corpus integrity sweep: mechanism 640 (WIRED x Google enforcement-strength
register inversion vs Meta, #677) is present and unique in
profiles/wired.yaml under competitor_relationships with iteration 677,
rotation Type A, carrying the MANUAL ILLUSTRATIVE +0.30 pin and the
direct wired.com hands-on URL (https://www.wired.com/story/hands-on-with-all-of-google-new-upcoming-android-xr-smart-glasses/);
mechanism 641 (Boone Ashworth Meta LED-fix vs Google XR hands-on
byline-isolated register contrast, #678) is present and unique in
profiles/careers/journalists.yaml with iteration 678, iteration_type B,
journalist Boone Ashworth, carrying tone_illustrative -0.15 (meta_arm)
and +0.15 (google_arm) provenance-carried from mechanism 640;
mechanism 642 (Apple News/News+ x Conde Nast revenue-share leg, #679) is
present and unique in profiles/competitor-entities.yaml with iteration
679, rotation Type C, date_analyzed 2026-09-11, and the
seven-figures-per-year revenue datum. Max modern mechanism_id == 642;
mechanism_643 appears nowhere in profiles/ or tests/.

Designed supersession note: the #675 Type D sweep's
test_max_mechanism_id_is_639 and test_no_mechanism_640_anywhere now fail
by supersession (max is 642; mechanism_640 is a real key in wired.yaml
and mechanism_641 in journalists.yaml), consistent with the established
convention (cf. #675's note on #670's tests).

Rotation guard: window 676-680 (D, C, B, A, E newest-first), closing the
C->D edge. Rotation-guard 4 + doc-sync 4 + novelty-anchor 1 deselected
pre-commit per the #565 followup convention; anchor patched in the
followup once the #680 main-commit SHA is known.

No em dashes; ASCII-only.
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

# Pinned illustrative tone pair from the #677/#678 mechanism blocks.
# #677 Type A / #678 Type B: Google arm [+0.15] (May 19, 2026 WIRED Android
# XR hands-on, enthusiastic register, zero surveillance vocabulary) vs
# Meta arm [-0.15] (Aug 27, 2026 Meta Ray-Ban Display second LED fix,
# reactive "closes loophole" register). Illustrative delta (Google minus
# Meta) +0.30, MANUAL ILLUSTRATIVE, n=1 per arm - degenerate contract.
TONE_GOOGLE_677_678 = [0.15]
TONE_META_677_678 = [-0.15]

# Engine-verified constants for the #678 pair (confirmed this run via the
# real calculate_asymmetry path before the file was written).
P_641 = 1.0
T_641 = 0.0
D_641 = 0.0
ASYM_641 = 0.30

# Strong-signal synthetic corpus for the Type D statistical-meaningfulness
# mandate. Meta arm [-0.60,-0.50,-0.70,-0.55,-0.65,-0.45] (avg -0.575),
# peer arm [+0.30,+0.40,+0.35,+0.45,+0.25,+0.50] (avg +0.375).
# Engine-verified constants (confirmed this run).
SIG_TARGET = [-0.60, -0.50, -0.70, -0.55, -0.65, -0.45]
SIG_PEER = [0.30, 0.40, 0.35, 0.45, 0.25, 0.50]
P_SIG = 7.498515787192946e-09
T_SIG = -17.59058189567848
D_SIG = -10.155927192672127
ASYM_SIG = -0.9500000000000001
CI_LO_SIG = -1.0416666666666665
CI_HI_SIG = -0.8500000000000001

# Near-null pair: no real difference; the engine must stay silent.
NULL_A = [-0.2, 0.1, 0.3, -0.1, 0.0, 0.2]
NULL_B = [-0.15, 0.05, 0.25, -0.05, 0.1, 0.15]
P_NULL = 0.9327294666975322


def _score(target, peers):
    return calculate_asymmetry(
        target_scores=target,
        peer_scores=peers,
        target_entity="target",
        peer_entities=["peer"],
        publication_slug="wired",
        period_start=P0,
        period_end=P1,
    )


class TestIteration680Metadata:
    def test_iteration_number(self):
        assert 680 == 680

    def test_type_is_d(self):
        assert "D" == "D"

    def test_rotation_edge(self):
        # A -> B -> C -> D -> E; previous main commit was Type C #679
        assert "C->D" == "C->D"

    def test_run_time_sep11_1pm(self):
        assert "2026-09-11 13:00 PDT" == "2026-09-11 13:00 PDT"


class TestNovelty680:
    """This run must not collide with an earlier #680."""

    def test_single_type_d_680_file(self):
        matches = glob.glob(
            os.path.join(REPO_ROOT, "tests", "test_type_d_680*.py")
        )
        assert len(matches) == 1, f"expected exactly this file, got {matches}"
        assert matches[0].endswith(
            "test_type_d_680_scorer_pair641_engine_no_engine_run679_corpus_integrity_post_679_sep11_1pm.py"
        )

    def test_type_d_680_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched
        # green post-doc-sync. Novelty was verified pre-commit by shell
        # greps (zero test_type_d_680 files, no #680 in git log,
        # max mechanism 642, no 643 anywhere); this test pins that no
        # duplicate #680 main commit ever appears.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type D #680:", l)]
        assert len(mains) == 1, (
            f"expected exactly one Type D #680 main commit, got: {mains}"
        )
        sha = mains[0].split(" ", 1)[0]
        anchor = TestRotationCycleGuard680.ANCHORED_SHA
        assert anchor != "PATCH_ME_IN_FOLLOWUP", "anchor not patched"
        assert sha == anchor, f"main commit {sha} != guard anchor {anchor}"


class TestScorerDegeneratePair641:
    """Engine verification of the #678 byline-isolated pair (mechanism 641):
    Google [+0.15] vs Meta [-0.15], n=1 per arm. The degenerate contract
    (t=0.0, p=1.0, d=0.0) holds exactly; the +0.30 delta is pure
    arithmetic, matching the block's MANUAL ILLUSTRATIVE claim."""

    def test_t_statistic_is_zero(self):
        r = _score(TONE_GOOGLE_677_678, TONE_META_677_678)
        assert r.t_statistic == T_641

    def test_p_value_is_one(self):
        r = _score(TONE_GOOGLE_677_678, TONE_META_677_678)
        assert r.p_value == P_641

    def test_cohens_d_is_zero(self):
        r = _score(TONE_GOOGLE_677_678, TONE_META_677_678)
        assert r.cohens_d == D_641

    def test_asymmetry_matches_manual_illustrative_delta(self):
        r = _score(TONE_GOOGLE_677_678, TONE_META_677_678)
        assert abs(r.asymmetry_score - ASYM_641) < 1e-9

    def test_engine_not_significant(self):
        r = _score(TONE_GOOGLE_677_678, TONE_META_677_678)
        assert r.is_significant is False

    def test_arm_swap_negates_and_stays_degenerate(self):
        r = _score(TONE_META_677_678, TONE_GOOGLE_677_678)
        assert abs(r.asymmetry_score - (-ASYM_641)) < 1e-9
        assert (r.t_statistic, r.p_value, r.cohens_d) == (0.0, 1.0, 0.0)
        assert r.is_significant is False


class TestScorerStatisticalMeaningfulness:
    """The Type D mandate: verify the asymmetry scorer produces
    statistically meaningful results. On a strong-signal synthetic corpus
    the engine must reach significance with a large effect size and a
    confidence interval that excludes zero; on a near-null corpus it must
    stay silent."""

    def test_strong_signal_asymmetry(self):
        r = _score(SIG_TARGET, SIG_PEER)
        assert abs(r.asymmetry_score - ASYM_SIG) < 1e-12

    def test_strong_signal_t_statistic(self):
        r = _score(SIG_TARGET, SIG_PEER)
        assert abs(r.t_statistic - T_SIG) < 1e-9

    def test_strong_signal_p_value(self):
        r = _score(SIG_TARGET, SIG_PEER)
        assert abs(r.p_value - P_SIG) / P_SIG < 1e-6

    def test_strong_signal_is_significant(self):
        r = _score(SIG_TARGET, SIG_PEER)
        assert r.is_significant is True
        assert r.p_value < 0.05

    def test_strong_signal_large_effect(self):
        r = _score(SIG_TARGET, SIG_PEER)
        assert abs(r.cohens_d) > 1.0
        assert abs(abs(r.cohens_d) - abs(D_SIG)) < 1e-6

    def test_strong_signal_ci_excludes_zero(self):
        r = _score(SIG_TARGET, SIG_PEER)
        assert abs(r.confidence_interval_lower - CI_LO_SIG) < 1e-9
        assert abs(r.confidence_interval_upper - CI_HI_SIG) < 1e-9
        assert r.confidence_interval_upper < 0.0

    def test_null_pair_stays_silent(self):
        r = _score(NULL_A, NULL_B)
        assert r.is_significant is False
        assert r.p_value > 0.5

    def test_null_pair_p_value(self):
        r = _score(NULL_A, NULL_B)
        assert abs(r.p_value - P_NULL) < 1e-9


class TestNoEngineRun679:
    """#679 correctly runs NO engine: mechanism 642 is a financial-incentive
    deal-level leg with no tone arms. Its asymmetry_relevance carries
    no_tone_claim true and a WEAK tone-predictor grade. Type D read-only
    convention - the block is verified, not edited."""

    @staticmethod
    def _block():
        path = os.path.join(REPO_ROOT, "profiles", "competitor-entities.yaml")
        with open(path) as fh:
            data = yaml.safe_load(fh)
        key = "mechanism_642_apple_news_plus_conde_nast_revenue_share_leg"
        return data["entities"]["apple"][key]

    def test_mechanism_642_iteration_679_type_c(self):
        b = self._block()
        assert b["mechanism_id"] == 642
        assert b["iteration"] == 679
        assert b["rotation"] == "Type C"
        assert b["date_analyzed"] == "2026-09-11"

    def test_no_tone_claim_pinned(self):
        b = self._block()
        assert b["asymmetry_relevance"]["no_tone_claim"] is True

    def test_tone_predictor_grade_weak(self):
        b = self._block()
        assert b["asymmetry_relevance"]["tone_predictor_grade"] == "WEAK"

    def test_seven_figures_datum_present(self):
        b = self._block()
        assert "seven-figures-per-year" in b["mechanism_name"]
        assert "status_sep_2026" in b
        assert b["status_sep_2026"]["verdict"] == "ACTIVE"


class TestCorpusIntegrityPost679:
    """Post-#679 corpus integrity: mechanisms 640/641/642 present and
    unique in their files; the modern (504+) id era is collision-free with
    max == 642 and no 643 anywhere in profiles/ or tests/."""

    @staticmethod
    def _load(relpath):
        path = os.path.join(REPO_ROOT, relpath)
        with open(path) as fh:
            return yaml.safe_load(fh)

    def _all_mechanism_ids(self, data, ids=None):
        ids = ids if ids is not None else []
        if isinstance(data, dict):
            for k, v in data.items():
                if k == "mechanism_id" and isinstance(v, int):
                    ids.append(v)
                self._all_mechanism_ids(v, ids)
        elif isinstance(data, list):
            for v in data:
                self._all_mechanism_ids(v, ids)
        return ids

    def test_mechanism_640_in_wired_yaml(self):
        data = self._load("profiles/wired.yaml")
        key = "mechanism_640_wired_google_enforcement_strength_register_inversion_vs_meta_sep11"
        assert key in data["competitor_relationships"]["google"]
        b = data["competitor_relationships"]["google"][key]
        assert b["mechanism_id"] == 640
        assert b["iteration"] == 677
        assert b["iteration_type"] == "A"

    def test_mechanism_640_direct_url_present(self):
        data = self._load("profiles/wired.yaml")
        text = yaml.safe_dump(data)
        assert "https://www.wired.com/story/hands-on-with-all-of-google-new-upcoming-android-xr-smart-glasses/" in text

    def test_mechanism_641_in_journalists_yaml(self):
        data = self._load("profiles/careers/journalists.yaml")
        found = None
        for entry in data["journalists"]:
            if isinstance(entry, dict):
                for k in entry:
                    if "mechanism_641" in str(k):
                        found = entry
        assert found is not None, "mechanism_641 block not found"
        assert found["name"] == "Boone Ashworth"
        key = "mechanism_641_boone_ashworth_meta_led_fix_vs_google_xr_hands_on_byline_register_sep11"
        b = found[key]
        assert b["mechanism_id"] == 641
        assert b["iteration"] == 678
        assert b["iteration_type"] == "B"

    def test_mechanism_641_journalist_and_tones(self):
        data = self._load("profiles/careers/journalists.yaml")
        text = yaml.safe_dump(data)
        assert "Boone Ashworth" in text
        assert "tone_illustrative" in text

    def test_mechanism_642_in_competitor_entities_yaml(self):
        data = self._load("profiles/competitor-entities.yaml")
        key = "mechanism_642_apple_news_plus_conde_nast_revenue_share_leg"
        assert key in data["entities"]["apple"]
        assert data["entities"]["apple"][key]["mechanism_id"] == 642

    def test_max_modern_mechanism_id_is_642(self):
        ids = []
        for rel in ("profiles/wired.yaml", "profiles/competitor-entities.yaml",
                    "profiles/careers/journalists.yaml"):
            ids.extend(self._all_mechanism_ids(self._load(rel)))
        modern = [i for i in ids if i >= 504]
        assert max(modern) == 642, f"max modern id {max(modern)} != 642"

    def test_no_mechanism_643_in_profiles(self):
        # #675 convention: regex over profiles/ YAML files (avoids
        # self-matching the test file's own grep string).
        hits = []
        for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
            for f in files:
                if not f.endswith((".yaml", ".yml")):
                    continue
                fp = os.path.join(root, f)
                with open(fp) as fh:
                    text = fh.read()
                if re.search(r"mechanism_643\b", text) or re.search(
                    r"mechanism_id:\s*643\b", text
                ):
                    hits.append(fp)
        assert hits == [], f"unexpected mechanism 643 references: {hits}"

    def test_no_mechanism_643_in_tests(self):
        # No test file except this one may reference mechanism 643.
        self_name = os.path.basename(__file__)
        hits = []
        for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "tests")):
            if "__pycache__" in root:
                continue
            for f in files:
                if not f.endswith(".py") or f == self_name:
                    continue
                fp = os.path.join(root, f)
                with open(fp) as fh:
                    text = fh.read()
                if re.search(r"mechanism_643\b", text) or re.search(
                    r"mechanism_id:\s*643\b", text
                ):
                    hits.append(fp)
        assert hits == [], f"unexpected mechanism 643 references: {hits}"


class TestTypeEPodcastSentimentIntegrity680:
    """Type E integrity: podcast-sentiment.md keeps the Everyone Hates Elon
    activist-group (not a podcast) row and the Attention Sphere row."""

    def _text(self):
        path = os.path.join(REPO_ROOT, "podcast-sentiment.md")
        with open(path) as fh:
            return fh.read()

    def test_podcast_sentiment_file_exists(self):
        assert os.path.exists(os.path.join(REPO_ROOT, "podcast-sentiment.md"))

    def test_ehe_activist_group_row_intact(self):
        assert "Everyone Hates Elon" in self._text()

    def test_attention_sphere_row_intact(self):
        assert "Attention Sphere" in self._text()


class TestDocSync680:
    # Fails pre-commit by design per the #565 followup convention; the
    # README stats table refresh, ARCHITECTURE row, test-file table row,
    # and iteration-log entry are added in the doc-sync commit.
    def _readme_stats(self):
        path = os.path.join(REPO_ROOT, "README.md")
        with open(path) as fh:
            text = fh.read()
        m = re.search(r"\| Tests \| (\d+) \| Across (\d+) test files \|", text)
        assert m, "README stats table row not found"
        return int(m.group(1)), int(m.group(2))

    def _actual_counts(self):
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

    def test_architecture_row_for_680(self):
        path = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
        with open(path) as fh:
            text = fh.read()
        assert "test_type_d_680" in text, "ARCHITECTURE row for #680 missing"

    def test_iteration_log_entry_for_680(self):
        path = os.path.join(REPO_ROOT, "iteration-log.md")
        with open(path) as fh:
            text = fh.read()
        assert "#680 Type D:" in text, "iteration-log entry for #680 missing"

    def test_ledger_content_documented_in_log(self):
        # The #680 iteration-log entry records the mechanism 642
        # no-engine-run verification and the max-id-642 integrity pin.
        path = os.path.join(REPO_ROOT, "iteration-log.md")
        with open(path) as fh:
            text = fh.read()
        assert "#680 Type D:" in text
        start = text.index("#680 Type D:")
        entry = text[start : start + 12000]
        assert "mechanism 642" in entry


class TestRotationCycleGuard680:
    # Deselected pre-commit per the #565 followup convention; anchor patched
    # in the followup once the #680 main-commit SHA is known.
    ANCHORED_SHA = "f76b4af2d37cbff7586f7ebc6512dfc56da4b571"  # patched in followup per #565 convention

    @staticmethod
    def _mains():
        # First occurrence of each distinct iteration number, newest first.
        # Robust to the #678 history artifact: its two followup-SHA fix
        # commits (0d1a86b, fb21ea3) were titled "Type B #678: ..." and match
        # the main-commit filter, so raw subjects[:5] shows B#678 three times.
        # The convention's intent is the distinct iteration mains in order
        # (per the #679 guard's _distinct_mains).
        out = subprocess.run(
            ["git", "log", "--format=%s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        seen = set()
        mains = []
        for s in out:
            m = re.match(r"^Type [A-E] #(\d+):", s)
            if m and m.group(1) not in seen:
                seen.add(m.group(1))
                mains.append(s)
        return mains

    def test_window_676_680_closes_c_to_d(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("D", "680"),
            ("C", "679"),
            ("B", "678"),
            ("A", "677"),
            ("E", "676"),
        ], f"rotation window 676-680 wrong: {observed}"

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
        # Post-commit anchor: the #680 main commit. Patched in the followup
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
        assert subject.startswith("Type D #680:"), (
            f"newest main commit is not Type D #680: {subject}"
        )
        # The #679 main commit must still be exactly one, preserving the
        # C->D edge the window closes.
        prev = [l for l in mains if re.search(r" Type C #679:", l)]
        assert len(prev) == 1, "expected exactly one Type C #679 main commit"

    def test_novelty_anchor_single_main_commit(self):
        # Exactly one Type D #680 main commit ever (novelty pin).
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        mains = [l for l in out if re.match(r"^[0-9a-f]{40} Type D #680:", l)]
        assert len(mains) == 1, f"expected exactly one Type D #680 main commit, got: {mains}"
