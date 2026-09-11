"""Type B #678: Boone Ashworth (WIRED) journalist-level byline-isolated register
pair - Meta second LED fix (sole byline, reactive) vs Google Android XR
hands-on (co-byline with Julian Chokkattu, enthusiastic).

FIRST journalist-level byline-isolated mechanism on Ashworth for this pair
(mechanism_id 641, next free pre-commit; max numeric mechanism_id was 640).
Both arms are in-corpus comparators reused per the #672 precedent; tones are
carried from mechanism 640 (#677), no new hand-scoring this run. The new
analytical work is byline attribution.

Meta arm: WIRED Aug 27, 2026 "Meta Ray-Ban Display Second LED Fix" -
https://www.wired.com/story/meta-ray-ban-display-second-led-fix/ - Boone
Ashworth SOLE byline. Register = reactive "closes loophole" on a fix that
blocks mid-recording LED covering; sits inside WIRED's broader Meta
surveillance-alarm register (corpus baseline -0.773). Tone -0.15
(MANUAL ILLUSTRATIVE, carried from #677). Full byline attribution: the
reactive register is Ashworth's own.

Google arm: WIRED May 19, 2026 "Hands-On With All of Google's New Upcoming
Android XR Smart Glasses" -
https://www.wired.com/story/hands-on-with-all-of-google-new-upcoming-android-xr-smart-glasses/
- byline Julian Chokkattu + Boone Ashworth (co-byline). Register =
enthusiastic/playful hands-on, zero surveillance vocabulary. Tone +0.15
(MANUAL ILLUSTRATIVE, carried from #677). Partial byline attribution: the
enthusiasm is shared with Chokkattu (STRONG co-byline-dilution confound).

Finding: same journalist, same Gear desk, same publication, same product
category (camera smart glasses) - opposite registers. The "beat assignment /
editorial lane" confound invoked in mechanism #431 is CONTROLLED at
journalist level here; what varies is entity plus product stage plus news
peg, not lane. Illustrative delta (Google minus Meta) = 0.15 - (-0.15) =
+0.30; p_value, cohens_d, ci NOT_CALCULATED; is_significant False (Aug 28
standing rule); statistical_contract degenerate_n1_per_arm. No engine run.
NOT artifact-grade.

Financial context (correlation, not causation): no financial gradient
predicts this gap. Conde Nast holds $0 AI licensing from Google; Advance
Publications SUED Google Jan 14, 2026 (SDNY adtech antitrust); CEO Roger
Lynch described Google AI Overviews as an existential "death blow" to
publisher revenue (mechanism #547 carried). The named financial ties predict
harder Google coverage, opposite to the observed direction.

Verdict: journalist-level byline-isolation pin. NOT a falsification-family
member. NOT a pure asymmetry pin (co-byline dilution plus product-stage
plus time-order confounds bound it). No analysis.json update warranted.

Novelty vs prior work: distinct from mechanism #431 (broad
tamper-enforcement family, Meta vs Samsung vs Google vs Apple, delta
-0.625); distinct from #677/mechanism 640 (publication-level scoring of the
same pair); distinct from iteration_385 (Ashworth OpenAI Dev Day +0.85 vs
Business Wars Meta podcast -0.7, different medium and different comparator).

Rotation: Type B follows Type A (#677) per A,B,C,D,E. Rotation guard,
doc-sync, and novelty-anchor classes are deselected pre-commit per the #565
followup convention; anchor patched in the followup commit once the main
commit SHA is known.
"""

import ast
import glob
import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAREERS_PATH = os.path.join(REPO_ROOT, "profiles", "careers", "journalists.yaml")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")

MECH_KEY = "mechanism_641_boone_ashworth_meta_led_fix_vs_google_xr_hands_on_byline_register_sep11"
TEST_BASENAME = "test_type_b_678_boone_ashworth_meta_led_fix_vs_google_xr_hands_on_byline_register_sep11_11am.py"

META_TONE = -0.15
GOOGLE_TONE = 0.15
EXPECTED_DELTA = 0.30

META_URL = "https://www.wired.com/story/meta-ray-ban-display-second-led-fix/"
GOOGLE_URL = "https://www.wired.com/story/hands-on-with-all-of-google-new-upcoming-android-xr-smart-glasses/"

# Patched in the followup commit per the #565 convention once the main
# commit SHA is known. The rotation-guard class is deselected pre-commit.
ANCHORED_SHA = "bac818b0aa3bbd91e0e2d2af60002bab127fc10f"


def _careers():
    with open(CAREERS_PATH) as f:
        return yaml.safe_load(f)


def _ashworth():
    matches = []
    for j in _careers()["journalists"]:
        if isinstance(j, dict) and j.get("name") == "Boone Ashworth":
            matches.append(j)
    assert len(matches) == 1, "expected exactly one Boone Ashworth entry, got %d" % len(matches)
    return matches[0]


def _mechanism():
    ash = _ashworth()
    assert MECH_KEY in ash, "%s missing from Boone Ashworth entry" % MECH_KEY
    return ash[MECH_KEY]


def _mechanism_text():
    return yaml.safe_dump(_mechanism(), allow_unicode=True)


def _count_def_tests():
    path = os.path.join(TESTS_DIR, TEST_BASENAME)
    tree = ast.parse(open(path).read())
    return sum(
        isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
        and n.name.startswith("test_")
        for n in ast.walk(tree)
    )


def read_readme():
    with open(README_PATH) as f:
        return f.read()


def read_arch():
    with open(ARCH_PATH) as f:
        return f.read()


def read_log_start():
    with open(LOG_PATH) as f:
        return f.read()


class TestIterationMetadata678:
    def test_iteration_number(self):
        assert _mechanism()["iteration"] == 678

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 641

    def test_mechanism_id_unique_repo_wide(self):
        seen = {}
        for path in glob.glob(os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True):
            text = open(path, encoding="utf-8", errors="replace").read()
            for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                if int(m.group(1)) == 641:
                    seen.setdefault(641, []).append(path)
        assert len(seen.get(641, [])) == 1, "mechanism_id 641 not unique: %r" % (seen.get(641),)

    def test_type_is_b(self):
        assert _mechanism()["type"] == "B"

    def test_goal_and_job_ids(self):
        m = _mechanism()
        assert m["goal_id"] == "goal_54093bda4145"
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_block_key_matches(self):
        assert _mechanism()["block_key"] == "type_b_678_boone_ashworth_meta_led_fix_vs_google_xr_hands_on_byline_register_sep11"

    def test_first_byline_isolated_pair_on_ashworth(self):
        ash = _ashworth()
        assert MECH_KEY in ash
        other_pairs = [
            k for k in ash
            if k.startswith("mechanism_") and "byline_register" in k and k != MECH_KEY
        ]
        assert not other_pairs, "unexpected second byline-isolated Ashworth pair: %r" % (other_pairs,)

    def test_no_duplicate_678_file(self):
        others = [
            p for p in glob.glob(os.path.join(TESTS_DIR, "test_type_b_678_*.py"))
            if os.path.basename(p) != TEST_BASENAME
        ]
        assert not others, "duplicate #678 test files: %r" % (others,)


class TestNovelty678:
    """Iteration 678 is new; nothing with this number existed pre-commit."""

    def test_single_type_b_678_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_b_678*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_b_678_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; the main
        # commit exists exactly once post-commit and its SHA matches the
        # rotation-guard anchor patched in the followup. Novelty was
        # verified pre-commit by shell greps (zero test_type_b_678 files,
        # no #678 in git log, no mechanism_id 641 in profiles); this test
        # pins that no duplicate #678 main commit ever appears.
        out = subprocess.run(
            ["git", "log", "--format=%H %s"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        mains = [
            line
            for line in out.stdout.splitlines()
            if re.match(r"^Type B #678:", line.split(" ", 1)[-1])
        ]
        assert len(mains) == 1, "expected exactly one Type B #678 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        assert sha == TestRotationCycleGuard678.ANCHORED_SHA, (
            "anchor patched in followup per #565 convention"
        )


class TestAshworthArms678:
    def test_meta_arm_date_and_sole_byline(self):
        meta = _mechanism()["meta_arm"]
        assert meta["date"] == "2026-08-27"
        assert meta["byline"] == "Boone Ashworth (sole)"
        assert "full" in meta["byline_attribution"]

    def test_meta_arm_url_verbatim(self):
        assert _mechanism()["meta_arm"]["url"] == META_URL

    def test_meta_arm_register_and_tone(self):
        meta = _mechanism()["meta_arm"]
        assert "closes loophole" in meta["register"]
        assert meta["tone_illustrative"] == META_TONE
        assert "carried from mechanism 640" in meta["tone_provenance"]

    def test_google_arm_date_and_co_byline(self):
        google = _mechanism()["google_arm"]
        assert google["date"] == "2026-05-19"
        assert "Julian Chokkattu" in google["byline"]
        assert "Boone Ashworth" in google["byline"]
        assert "partial" in google["byline_attribution"]

    def test_google_arm_url_verbatim(self):
        assert _mechanism()["google_arm"]["url"] == GOOGLE_URL

    def test_google_arm_register_and_tone(self):
        google = _mechanism()["google_arm"]
        assert "zero surveillance vocabulary" in google["register"]
        assert google["tone_illustrative"] == GOOGLE_TONE
        assert "carried from mechanism 640" in google["tone_provenance"]

    def test_both_arms_same_publication_and_desk(self):
        m = _mechanism()
        assert m["meta_arm"]["publication"] == "WIRED"
        assert m["google_arm"]["publication"] == "WIRED"
        assert "Gear" in m["lane_constancy"]

    def test_lane_constancy_controls_beat_assignment(self):
        lane = _mechanism()["lane_constancy"]
        assert "CONTROLLED" in lane
        assert "431" in lane


class TestScorerDelta678:
    def test_arrays(self):
        s = _mechanism()["asymmetry_scorer_result"]
        assert s["target_tones_manual_illustrative"] == [GOOGLE_TONE]
        assert s["reference_tones_manual_illustrative"] == [META_TONE]

    def test_arithmetic(self):
        s = _mechanism()["asymmetry_scorer_result"]
        delta = s["target_avg"] - s["reference_avg"]
        assert abs(delta - EXPECTED_DELTA) < 1e-9, "delta %r != %r" % (delta, EXPECTED_DELTA)
        assert abs(s["delta_google_minus_meta"] - EXPECTED_DELTA) < 1e-9

    def test_manual_illustrative_guards(self):
        s = _mechanism()["asymmetry_scorer_result"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci"] == "NOT_CALCULATED"
        assert s["is_significant"] is False
        assert s["statistical_contract"] == "degenerate_n1_per_arm"
        assert s["artifact_grade"] is False

    def test_no_engine_run(self):
        s = _mechanism()["asymmetry_scorer_result"]
        assert "no engine run" in s["method"]

    def test_tones_carried_not_rescored(self):
        s = _mechanism()["asymmetry_scorer_result"]
        assert "carried from mechanism 640" in s["method"]

    def test_limitations_stated(self):
        lim = _mechanism()["asymmetry_scorer_result"]["limitations"]
        assert "co-byline" in lim
        assert "#638/#643" in lim


class TestFinancialContext678:
    def test_correlation_not_causation(self):
        fc = _mechanism()["financial_context"]
        assert "Correlation, not causation" in fc

    def test_no_gradient_predicts_gap(self):
        fc = _mechanism()["financial_context"]
        assert "$0 AI licensing from Google" in fc
        assert "SUED Google" in fc
        assert "opposite to the observed direction" in fc

    def test_verdict_bounds(self):
        v = _mechanism()["verdict"]
        assert "NOT a falsification-family member" in v
        assert "NOT a pure asymmetry pin" in v
        assert "No analysis.json update warranted" in v


class TestConfounders678:
    def test_confounders_present_and_ranked(self):
        confs = _mechanism()["confounders"]
        assert len(confs) >= 5
        assert sum(c.startswith("[STRONG]") for c in confs) >= 3

    def test_strong_co_byline_dilution(self):
        confs = _mechanism()["confounders"]
        strong = [c for c in confs if c.startswith("[STRONG]")]
        assert any("Co-byline dilution" in c and "Chokkattu" in c for c in strong)

    def test_strong_product_stage(self):
        confs = _mechanism()["confounders"]
        strong = [c for c in confs if c.startswith("[STRONG]")]
        assert any("Product stage" in c for c in strong)

    def test_strong_time_order(self):
        confs = _mechanism()["confounders"]
        strong = [c for c in confs if c.startswith("[STRONG]")]
        assert any("Time order" in c for c in strong)

    def test_cross_references_distinct_layers(self):
        refs = " ".join(_mechanism()["cross_references"])
        assert "#677" in refs
        assert "#431" in refs
        assert "iteration_385" in refs


class TestRotationCycleGuard678:
    # Deselected pre-commit per the #565 followup convention; the rotation
    # window only closes once the #678 main commit exists.
    ANCHORED_SHA = ANCHORED_SHA

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

    def test_window_674_678_closes_a_to_b(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("B", "678"),
            ("A", "677"),
            ("E", "676"),
            ("D", "675"),
            ("C", "674"),
        ], "rotation window 674-678 wrong: %r" % (observed,)

    def test_rotation_adjacency_cycle_valid(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m
            observed.append(m.group(1))
        assert observed == ["B", "A", "E", "D", "C"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, (
                "rotation broken: %s -> %s is not a valid cycle edge" % (a, b)
            )

    def test_anchor_is_main_patch_in_followup(self):
        # Post-commit anchor: the #678 main commit. Patched in the followup
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
        assert sha.startswith(self.ANCHORED_SHA), "anchor not yet patched: %s" % sha
        assert subject.startswith("Type B #678:"), (
            "post-commit anchor broken: newest main is not #678: %r" % (subject,)
        )

    def test_rotation_guard_regex_actually_matches(self):
        # #632 process note: a rotation guard whose regex never matches is a
        # silent no-op. Verify the guard regexes match a real main-commit
        # subject (the double-backslash r"...#(\\d+)..." form silently matches
        # nothing). Written as a semantic check rather than a literal-pattern
        # check so the test cannot defeat itself by containing the pattern.
        src = open(os.path.join(TESTS_DIR, TEST_BASENAME)).read()
        patterns = re.findall(r're\.search\(r"([^"]+)"', src)
        guard_patterns = [p for p in patterns if p.startswith("Type (")]
        assert guard_patterns, "no rotation-guard regex found in this file"
        sample = "Type B #678: Boone Ashworth Meta LED-fix vs Google XR hands-on byline register"
        for p in guard_patterns:
            m = re.search(p, sample)
            assert m and m.group(1) == "B" and m.group(2) == "678", (
                "rotation regex %r fails to match a real subject "
                "(double-backslash bug?)" % (p,)
            )


class TestDocSyncRatchet678:
    # Fails pre-commit by design per the #565 followup convention; the README
    # test-file table row and ARCHITECTURE tree row land in the doc-sync commit.
    def test_readme_has_678_row(self):
        assert "test_type_b_678" in read_readme()

    def test_arch_has_678_row(self):
        assert "test_type_b_678" in read_arch()

    def test_readme_row_mentions_ashworth(self):
        assert "Ashworth" in read_readme()

    def test_log_starts_with_678(self):
        assert read_log_start().startswith("#678 Type B:")

    def test_def_test_count_matches(self):
        # The README row for #678 must carry this file's own def-test count.
        n = _count_def_tests()
        assert str(n) in read_readme(), (
            "README #678 row should mention this file's def-test count %d" % n
        )


class TestNoBrittlePatterns678:
    def test_yaml_reparses_clean(self):
        ash = _ashworth()
        m = ash[MECH_KEY]
        assert isinstance(m["mechanism_id"], int)
        assert isinstance(m["meta_arm"]["tone_illustrative"], float)
        assert isinstance(m["google_arm"]["tone_illustrative"], float)
        assert isinstance(m["asymmetry_scorer_result"]["is_significant"], bool)

    def test_no_em_dash_in_mechanism(self):
        assert "\u2014" not in _mechanism_text()
        assert "\u2028" not in _mechanism_text()
        src = open(os.path.join(TESTS_DIR, TEST_BASENAME)).read()
        assert "\u2014" not in src
        assert "\u2028" not in src

    def test_all_urls_http_or_https(self):
        urls = [
            _mechanism()["meta_arm"]["url"],
            _mechanism()["google_arm"]["url"],
        ]
        assert urls, "no URLs recorded"
        for u in urls:
            assert u.startswith(("http://", "https://")), "bad URL: %r" % (u,)
