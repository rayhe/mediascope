"""Type B #683: Hayden Field (The Verge) journalist-level byline-isolated register
pair - Meta Muse Spark launch (Apr 8, 2026, Field SOLE byline, competitive-deficit
re-entry register) vs OpenAI GPT-5.6 launch (Jun 26, 2026, Field SOLE byline,
product-unveiling under regulatory-friction register).

FIRST dedicated Type B mechanism on Hayden Field (mechanism_id 644, next free
pre-commit; max numeric mechanism_id was 643). The GPT-5.6 and Muse Spark
comparators are in-corpus (mechanism #425 already cites them); tones are
hand-scored this run (#683), illustrative only per the Aug 28 standing rule.
The new analytical work is byline attribution: the re-entry-deficit and
regulatory-friction registers are Field's own, full attribution, zero
co-byline dilution (stronger isolation than #678's co-byline Google arm).

Meta arm: The Verge Apr 8, 2026 "Meta is reentering the AI race with a new
model called Muse Spark" -
https://technewstube.com/theverge/1821587/meta-reentering-ai-race-new-model-called-muse-spark/
- Field SOLE byline (mirror-verified "By Hayden Field Apr 8, 2026, 12:12 pm").
Register = competitive-deficit re-entry ("first model since Mark Zuckerberg
spent billions overhauling the company's AI efforts"). Tone -0.15
(MANUAL ILLUSTRATIVE).

OpenAI arm: The Verge Jun 26, 2026 "OpenAI unveils GPT-5.6 amid US AI
regulatory drama" -
https://technewstube.com/theverge/1844887/openai-unveils-gpt-5-6-us-ai-regulatory-drama/
- Field SOLE byline (mirror-verified "By Hayden Field Jun 26, 2026, 1:00 pm").
Register = product-unveiling under regulatory friction ("Less than 24 hours
after news broke that OpenAI would stagger its next model release at the
request of the Trump administration"; "limited preview" of Sol flagship and
Terra medium-tier). Tone -0.10 (MANUAL ILLUSTRATIVE).

Finding: register differentiation within constancy. The same writer applies
adversarial-adjacent frames to both entities but differentiates the criticism
type: competitive-legitimacy deficit for Meta vs government-regulatory
friction for OpenAI. The Vox Media May 29, 2024 OpenAI content-licensing and
product partnership (OpenAI trains on The Verge archive; $0 Meta relationship;
no termination announced as of Aug 31, 2026, mechanism #425) does NOT predict
a softer OpenAI register at this journalist - the deal-predicts-softness
hypothesis fails for Field. Three-entity beat-lens constancy check: Field runs
the same "AI race loser" deficit lens on Google (Decoder Aug 13, 2026) and
Apple (Jun 9, 2025), so the deficit register is beat-lens, not Meta-targeted.
Constancy family: mechanism #626/#653 (Robert Hart) analytic shape.

Illustrative delta (OpenAI minus Meta) = -0.10 - (-0.15) = +0.05; p_value,
cohens_d, ci NOT_CALCULATED; is_significant False (Aug 28 standing rule);
statistical_contract degenerate_n1_per_arm per #638/#643. No engine run.
NOT artifact-grade.

Financial context (correlation, not causation): Vox-OpenAI deal predicts
softer OpenAI framing at The Verge; Field's GPT-5.6 arm runs
adversarial-adjacent (regulatory friction), opposite to the prediction. The
finding constrains the deal theory to publication-level aggregates, not this
journalist.

Verdict: constancy pin, NOT a falsification-family member, NOT a pure
asymmetry pin (near-null +0.05 delta, STRONG news-peg/time-order confounds).
No analysis.json update warranted.

Novelty vs prior work: distinct from mechanism #56 (Hayden Field AI-beat
concentration, Aug 11 - volume analysis, no byline-isolated pair scoring);
distinct from #425 (Type A publication-level Verge OpenAI aspiration vs Meta
deficit; #683 reuses those comparators under the #672/#678 reuse precedent -
new work is byline attribution, not new sourcing); distinct from #626/#653
(Robert Hart, different journalist); distinct from #371 (Kylie Robison,
different Verge AI reporter).

Rotation: Type B follows Type A (#682) per A,B,C,D,E. Rotation guard,
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

MECH_KEY = "mechanism_644_hayden_field_meta_muse_spark_reentry_deficit_vs_openai_gpt56_regulatory_launch_byline_register_sep11"
TEST_BASENAME = "test_type_b_683_hayden_field_meta_muse_spark_reentry_deficit_vs_openai_gpt56_regulatory_launch_byline_register_sep11_5pm.py"

META_TONE = -0.15
OPENAI_TONE = -0.10
EXPECTED_DELTA = 0.05

META_URL = "https://technewstube.com/theverge/1821587/meta-reentering-ai-race-new-model-called-muse-spark/"
OPENAI_URL = "https://technewstube.com/theverge/1844887/openai-unveils-gpt-5-6-us-ai-regulatory-drama/"

# Patched in the followup commit per the #565 convention once the main
# commit SHA is known. The rotation-guard class is deselected pre-commit.
ANCHORED_SHA = "9206d0a0af23816450cf7dfcc2eb711d7871ae75"


def _careers():
    with open(CAREERS_PATH) as f:
        return yaml.safe_load(f)


def _field():
    matches = []
    for j in _careers()["journalists"]:
        if isinstance(j, dict) and j.get("name") == "Hayden Field":
            matches.append(j)
    assert len(matches) == 1, "expected exactly one Hayden Field entry, got %d" % len(matches)
    return matches[0]


def _mechanism():
    field = _field()
    assert MECH_KEY in field, "%s missing from Hayden Field entry" % MECH_KEY
    return field[MECH_KEY]


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


class TestIterationMetadata683:
    def test_iteration_number(self):
        assert _mechanism()["iteration"] == 683

    def test_mechanism_id_next_free(self):
        assert _mechanism()["mechanism_id"] == 644

    def test_mechanism_id_unique_repo_wide(self):
        seen = {}
        for path in glob.glob(os.path.join(REPO_ROOT, "profiles", "**", "*.yaml"), recursive=True):
            text = open(path, encoding="utf-8", errors="replace").read()
            for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                if int(m.group(1)) == 644:
                    seen.setdefault(644, []).append(path)
        assert len(seen.get(644, [])) == 1, "mechanism_id 644 not unique: %r" % (seen.get(644),)

    def test_type_is_b(self):
        assert _mechanism()["type"] == "B"

    def test_goal_and_job_ids(self):
        m = _mechanism()
        assert m["goal_id"] == "goal_54093bda4145"
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_block_key_matches(self):
        assert _mechanism()["block_key"] == "type_b_683_hayden_field_meta_muse_spark_reentry_deficit_vs_openai_gpt56_regulatory_launch_byline_register_sep11"

    def test_first_byline_isolated_pair_on_field(self):
        field = _field()
        assert MECH_KEY in field
        other_pairs = [
            k for k in field
            if k.startswith("mechanism_") and k != MECH_KEY
        ]
        assert not other_pairs, "unexpected second mechanism on Hayden Field: %r" % (other_pairs,)

    def test_no_duplicate_683_file(self):
        others = [
            p for p in glob.glob(os.path.join(TESTS_DIR, "test_type_b_683_*.py"))
            if os.path.basename(p) != TEST_BASENAME
        ]
        assert not others, "duplicate #683 test files: %r" % (others,)


class TestNovelty683:
    """Iteration 683 is new; nothing with this number existed pre-commit."""

    def test_single_type_b_683_file(self):
        matches = glob.glob(os.path.join(REPO_ROOT, "tests", "test_type_b_683*.py"))
        assert len(matches) == 1, "expected exactly this file, got %r" % (matches,)
        assert matches[0].endswith(TEST_BASENAME)

    def test_type_b_683_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; the main
        # commit exists exactly once post-commit and its SHA matches the
        # rotation-guard anchor patched in the followup. Novelty was
        # verified pre-commit by shell greps (zero test_type_b_683 files,
        # no #683 in git log, no mechanism_id 644 in profiles); this test
        # pins that no duplicate #683 main commit ever appears.
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
            if re.match(r"^Type B #683:", line.split(" ", 1)[-1])
        ]
        assert len(mains) == 1, "expected exactly one Type B #683 main commit, got %r" % (mains,)
        sha = mains[0].split()[0]
        assert sha == TestRotationCycleGuard683.ANCHORED_SHA, (
            "anchor patched in followup per #565 convention"
        )


class TestFieldArms683:
    def test_meta_arm_date_and_sole_byline(self):
        meta = _mechanism()["meta_arm"]
        assert meta["date"] == "2026-04-08"
        assert meta["byline"] == "Hayden Field (sole)"
        assert "full" in meta["byline_attribution"]

    def test_meta_arm_url_verbatim(self):
        assert _mechanism()["meta_arm"]["url"] == META_URL

    def test_meta_arm_register_and_tone(self):
        meta = _mechanism()["meta_arm"]
        assert "competitive-deficit re-entry" in meta["register"]
        assert "reentering the AI race" in meta["register_detail"]
        assert meta["tone_illustrative"] == META_TONE

    def test_meta_arm_byline_mirror_verified(self):
        assert "By Hayden Field Apr 8, 2026, 12:12 pm" in _mechanism()["meta_arm"]["evidence_grade"]

    def test_openai_arm_date_and_sole_byline(self):
        openai = _mechanism()["openai_arm"]
        assert openai["date"] == "2026-06-26"
        assert openai["byline"] == "Hayden Field (sole)"
        assert "full" in openai["byline_attribution"]

    def test_openai_arm_url_verbatim(self):
        assert _mechanism()["openai_arm"]["url"] == OPENAI_URL

    def test_openai_arm_register_and_tone(self):
        openai = _mechanism()["openai_arm"]
        assert "regulatory friction" in openai["register"]
        assert "Trump administration" in openai["register_detail"]
        assert "limited preview" in openai["register_detail"]
        assert openai["tone_illustrative"] == OPENAI_TONE

    def test_openai_arm_byline_mirror_verified(self):
        assert "By Hayden Field Jun 26, 2026, 1:00 pm" in _mechanism()["openai_arm"]["evidence_grade"]

    def test_both_arms_same_publication(self):
        assert _mechanism()["meta_arm"]["publication"] == "The Verge"
        assert _mechanism()["openai_arm"]["publication"] == "The Verge"

    def test_lane_constancy_three_entity_beat_lens(self):
        lc = _mechanism()["lane_constancy"]
        assert "Google" in lc
        assert "Apple" in lc
        assert "Beat-lens" in lc
        assert "not Meta-selective" in lc


class TestScorerDelta683:
    def test_arrays(self):
        s = _mechanism()["asymmetry_scorer_result"]
        assert s["target_tones_manual_illustrative"] == [OPENAI_TONE]
        assert s["reference_tones_manual_illustrative"] == [META_TONE]

    def test_arithmetic(self):
        s = _mechanism()["asymmetry_scorer_result"]
        delta = s["target_avg"] - s["reference_avg"]
        assert abs(delta - EXPECTED_DELTA) < 1e-9, "delta %r != %r" % (delta, EXPECTED_DELTA)
        assert abs(s["delta_openai_minus_meta"] - EXPECTED_DELTA) < 1e-9

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

    def test_tones_hand_scored_this_run(self):
        s = _mechanism()["asymmetry_scorer_result"]
        assert "hand-assigned" in s["method"]

    def test_limitations_stated(self):
        lim = _mechanism()["asymmetry_scorer_result"]["limitations"]
        assert "no co-byline confound" in lim
        assert "#638/#643" in lim


class TestFinancialContext683:
    def test_correlation_not_causation(self):
        fc = _mechanism()["financial_context"]
        assert "Correlation, not causation" in fc

    def test_vox_openai_deal_does_not_predict_field_register(self):
        fc = _mechanism()["financial_context"]
        assert "May 29 2024" in fc
        assert "$0 Meta relationship" in fc
        assert "opposite direction" in fc

    def test_verdict_bounds(self):
        v = _mechanism()["verdict"]
        assert "NOT a falsification-family member" in v
        assert "NOT a pure asymmetry pin" in v
        assert "No analysis.json update warranted" in v


class TestConfounders683:
    def test_confounders_present_and_ranked(self):
        confs = _mechanism()["confounders"]
        assert len(confs) >= 5
        assert sum(c.startswith("[STRONG]") for c in confs) >= 3

    def test_strong_news_peg_mismatch(self):
        confs = _mechanism()["confounders"]
        strong = [c for c in confs if c.startswith("[STRONG]")]
        assert any("News peg" in c and "Trump administration" in c for c in strong)

    def test_strong_time_order(self):
        confs = _mechanism()["confounders"]
        strong = [c for c in confs if c.startswith("[STRONG]")]
        assert any("Time order" in c for c in strong)

    def test_strong_genuine_meta_turmoil(self):
        confs = _mechanism()["confounders"]
        strong = [c for c in confs if c.startswith("[STRONG]")]
        assert any("Genuine Meta turmoil" in c for c in strong)

    def test_cross_references_distinct_layers(self):
        refs = " ".join(_mechanism()["cross_references"])
        assert "#56" in refs
        assert "#425" in refs
        assert "#626/#653" in refs
        assert "#672/#678" in refs

    def test_novelty_language(self):
        nov = _mechanism()["novelty"]
        assert "FIRST dedicated Type B on Hayden Field" in nov
        assert "mechanism #56" in nov
        assert "#425" in nov


class TestRotationCycleGuard683:
    # Deselected pre-commit per the #565 followup convention; the rotation
    # window only closes once the #683 main commit exists.
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

    def test_window_679_683_closes_a_to_b(self):
        subjects = self._mains()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+):", s)
            assert m, "unparseable rotation subject: %r" % (s,)
            observed.append((m.group(1), m.group(2)))
        assert observed == [
            ("B", "683"),
            ("A", "682"),
            ("E", "681"),
            ("D", "680"),
            ("C", "679"),
        ], "rotation window 679-683 wrong: %r" % (observed,)

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
        # Post-commit anchor: the #683 main commit. Patched in the followup
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
        assert subject.startswith("Type B #683:"), (
            "post-commit anchor broken: newest main is not #683: %r" % (subject,)
        )

    def test_rotation_guard_regex_actually_matches(self):
        # #632 process note: a rotation guard whose regex never matches is a
        # silent no-op. Verify the guard regexes match a real main-commit
        # subject (the double-backslash r"...#(\d+)..." form silently matches
        # nothing). Written as a semantic check rather than a literal-pattern
        # check so the test cannot defeat itself by containing the pattern.
        src = open(os.path.join(TESTS_DIR, TEST_BASENAME)).read()
        patterns = re.findall(r're\.search\(r"([^"]+)"', src)
        guard_patterns = [p for p in patterns if p.startswith("Type (")]
        assert guard_patterns, "no rotation-guard regex found in this file"
        sample = "Type B #683: Hayden Field Meta Muse Spark vs OpenAI GPT-5.6 byline register"
        for p in guard_patterns:
            m = re.search(p, sample)
            assert m and m.group(1) == "B" and m.group(2) == "683", (
                "rotation regex %r fails to match a real subject "
                "(double-backslash bug?)" % (p,)
            )


class TestDocSyncRatchet683:
    # Fails pre-commit by design per the #565 followup convention; the README
    # test-file table row and ARCHITECTURE tree row land in the doc-sync commit.
    def test_readme_has_683_row(self):
        assert "test_type_b_683" in read_readme()

    def test_arch_has_683_row(self):
        assert "test_type_b_683" in read_arch()

    def test_readme_row_mentions_field(self):
        assert "Hayden Field" in read_readme()

    def test_log_starts_with_683(self):
        assert read_log_start().startswith("#683 Type B:")

    def test_def_test_count_matches(self):
        # The README row for #683 must carry this file's own def-test count.
        n = _count_def_tests()
        assert str(n) in read_readme(), (
            "README #683 row should mention this file's def-test count %d" % n
        )


class TestNoBrittlePatterns683:
    def test_yaml_reparses_clean(self):
        field = _field()
        m = field[MECH_KEY]
        assert isinstance(m["mechanism_id"], int)
        assert isinstance(m["meta_arm"]["tone_illustrative"], float)
        assert isinstance(m["openai_arm"]["tone_illustrative"], float)
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
            _mechanism()["openai_arm"]["url"],
        ]
        assert urls, "no URLs recorded"
        for u in urls:
            assert u.startswith(("http://", "https://")), "bad URL: %r" % (u,)
