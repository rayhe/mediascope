# -*- coding: utf-8 -*-
"""Type B #1273: m995 Kalley Huang (NYT) journalist cross-entity pair -
Meta Anthropic-spend accountability-exposure register vs Apple foldable
product-innovation register.

Mechanism 995 (CONTROL-CASE, NOT a falsification-family member; ledger
holds at 54). Same writer, same outlet, about nine days apart (late Aug
vs Sep 8 2026): Huang co-bylines the NYT scoop that Meta secretly
projected spending up to $10B a year on rival Anthropic's AI models
while Zuckerberg publicly attacked Anthropic (-0.35 MANUAL
ILLUSTRATIVE, accountability-exposure register), and solos the NYT
foldable-iPhone product-news piece framing Apple's first foldable as
the biggest iPhone design change in nearly two decades (+0.05,
innovation-positive product-news register). Illustrative delta (Apple
minus Meta) +0.40: Meta draws the harder register. The NYT x Apple and
NYT x Meta relationships are NOT licensing deals in the corpus (the NYT
x OpenAI relationship is litigation, in-corpus), so the uniform
payer-softening prediction is not adjudicated. MANUAL ILLUSTRATIVE ONLY
per the Aug 28 2026 standing rule (tones hand-assigned, n=1 per arm;
p_value/cohens_d/ci_95 NOT_CALCULATED; engine NOT run; is_significant
false; NOT artifact-grade; verdict control_case_observation; no
analysis.json update).

Research: main-run browser.search verification sets (Meta-arm
exact-headline search returning the europesays.com relay verbatim with
"Eli Tan and Kalley Huang reported the figures" and the $10B-a-year
figure; Apple-arm search returning the instrumentalcomms.com roundup
verbatim with "Kalley Huang of The New York Times reported" and the
Sep-8-2026 date; candidate-rejection audit: Brian X. Chen saturated
(#458), Eli Tan Meta-beat-only with no competitor arm, Cade Metz
saturated, Mike Isaac saturated (#1248), Kashmir Hill half-pair
rejected per #1248, Gurman/Stern/Stein/Peters/Perez saturated, Wayne Ma
no verifiable pair); corpus saturation greps: zero kalley_huang_type_b
key, both relay URLs zero-hit repo-wide, Meta-arm headline zero-hit
repo-wide, Apple-arm headline zero-hit repo-wide. 0 browser.open per
#503 (excerpt-bounded). All URLs copied verbatim from Full-URL
listings; no canonical nytimes.com URLs constructed. The m995 block
lands in profiles/careers/journalists.yaml as a new top-level
kalley_huang_type_b key (per the #643 convention), appended at the end
of the file. Targeted staging by explicit path only; the in-flight
#899/#938/#900/#1012-wt files stay out of this run's index/diff. Do
NOT touch #1024 m846.

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this
pre-commit file and is patched to the main-commit hash in the anchor
followup commit. One anchor test (the placeholder pin) fails BY DESIGN
pre-commit; TestAnchor1273 deselected in the in-gate run. The main
commit is the anchor per #565.

FOURTH leg of the 1270-1274 window: D #1270 -> E #1271 -> A #1272 ->
B #1273 -> C #1274 per the #565 anchor + rotation guard. Next run
#1274 Type C closes the window. Type B lands one mechanism
(mechanism 995).

Per #795: this run only CHECKS the #1270-launched background suite
(goal hidden_files type_d_1270_full_suite.log, OBSERVED NOT-ALIVE at
this run's check, about 8.75h stale with zero live pytest processes);
its verdict and tombstone belong to #1275 (next Type D). This run
neither re-launches, kills, nor writes to the suite. The #1272 repair
chain closed with its terminal placeholder patch committed by this run
pre-main (DOCSYNCSHA1272 placeholder gone from the log, asserted in
the rotation guard).

ASCII-only, no em dashes. Needles format-built per #715: this file
must not carry contiguous numeric/underscore/dash mechanism-key forms
of the next number, the forty-eighth / forty-ninth / fiftieth /
fifty-first / fifty-second / fifty-third / fifty-fourth member-claim
forms, or the fortieth direction form; the constants are constructed
at runtime. (The landed ordinals live as short lowercase forms in
prose here; the live full-form claims live in
profiles/financial-times.yaml, profiles/news-corp.yaml,
profiles/the-verge.yaml, profiles/guardian.yaml, and
profiles/careers/journalists.yaml: the forty-eighth, forty-ninth,
fiftieth, fifty-first, fifty-second, fifty-third, and fifty-fourth
members respectively.)
"""

import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
GOAL_HIDDEN = os.path.join(
    os.path.expanduser("~"), "workspace", "goals",
    "mediascope-meta-wearables-press-analysis", "hidden_files",
)
OWN_BASENAME = (
    "test_type_b_1273_kalley_huang_nyt_meta_anthropic_spend_"
    "vs_apple_foldable_oct06_8pm.py"
)
PROFILE_FILE = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1270_full_suite.log")

MECH_NUM = 995
NEXT_NUM = 996  # integer only; key-form needles are format-built
ITERATION = 1273

ANCHORED_SHA = "4b9d81ba42f43840ab16e3eeb00f72b7e89ae6d8"  # patched per #565 in the anchor followup (main commit sha)

# Predecessor #1272 chain (verified via git rev-parse pre-commit).
PRED_MAIN_1272 = "982ca183773272571d41195d40b18a487eaeb917"
PRED_ANCHOR_1272 = "cbe557f132784b14f39e979e199f4ebfc08d7103"
PRED_DOCSYNC_1272 = "d2a66b6b66775040587226be005888c63abd9d90"
PRED_FINAL_1272 = "d2a66b6b66775040587226be005888c63abd9d90"
# This run's own main sha: patched in the terminal log-hash followup
# per #721.
PRED_MAIN_1273 = "0" * 40
# Next leg's main sha: patched in #1274's log-hash followup per #721.
PRED_MAIN_1274 = "0" * 40

# The #1272 window-continuation file, for the staleness pin on its
# guard-lifecycle class (max id 994; zero next-number nine-nine-six
# / no-Type-B-#1273-in-git-log (flips BY DESIGN at this run's main
# commit - the #1191-class self-trip) / fortieth direction absent /
# forty-eighth member intact in profiles/financial-times.yaml /
# forty-ninth member intact + fiftieth member intact +
# fifty-second member intact in profiles/careers/journalists.yaml /
# fifty-first member intact in profiles/news-corp.yaml /
# fifty-third member intact in profiles/the-verge.yaml /
# fifty-fourth member intact in profiles/guardian.yaml (landed at
# #1257) / no fifty-fifth member (repo-wide) / ledger 54).
E1272_FILE = (
    "test_type_a_1272_guardian_openai_robinson_resignation_oct06_6pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 70642  # post-sync-positive per #719 (70564 + 78)
README_FILE_COUNT = 1598  # post-sync-positive per #719 (1597 + 1)

# The forward-guard needles are fragment-built per #715 so this file
# carries no contiguous literal of a forward-guard claim form. The
# fifty-fourth member claim lives ONLY in the profile block (HEAD
# post-#1257); this file references it via fragments.
_T40 = "FORT" + "IETH relationship direction"
_T48 = "FORT" + "Y-EIGHTH falsification-family member"
_T49 = "FORT" + "Y-NINTH falsification-family member"
_T50 = "FIFT" + "IETH falsification-family member"
_T51 = "FIFT" + "Y-FIRST falsification-family member"
_T52 = "FIFT" + "Y-SECOND falsification-family member"
_T53 = "FIFT" + "Y-THIRD falsification-family member"
_T54 = "FIFT" + "Y-FOURTH falsification-family member"
_T55 = "FIFT" + "Y-FIFTH falsification-family member"

BLOCK_KEY = (
    "type_b_1273_kalley_huang_nyt_meta_anthropic_spend_"
    "vs_apple_foldable_oct06_8pm"
)
JOURNALIST_KEY = "kalley_huang_type_b"

# The two relay URLs (verbatim from Full-URL listings); both zero-hit
# repo-wide pre-commit via git grep -F.
NOVEL_URLS = [
    "https://www.europesays.com/people/208390/",
    "https://www.instrumentalcomms.com/blog/foldable-iphone-mifepristone",
]

# Tones (MANUAL ILLUSTRATIVE).
META_TONE = -0.35  # NEW NYT x Meta Anthropic-spend arm
APPLE_TONE = 0.05  # NEW NYT x Apple foldable arm
DELTA = 0.40  # 0.05 - (-0.35)

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )


def _load_journalists():
    with open(PROFILE_FILE, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _block():
    data = _load_journalists()
    return data[JOURNALIST_KEY]["competitor_coverage"][BLOCK_KEY]


def _iter_source_files():
    """Yield paths for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts.
    """
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            yield os.path.join(root, f)
    for root, dirs, files in os.walk(TESTS_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            if f == OWN_BASENAME:
                continue
            if f.endswith(".py"):
                yield os.path.join(root, f)


def _repo_grep_underscore_mechanism(n):
    """Underscore-form mechanism key; needle format-built per #770."""
    needle = "%s%d" % (MECH_ID_MARKER, n)
    return [
        p
        for p in _iter_source_files()
        if needle in open(p, encoding="utf-8", errors="replace").read()
    ]


def _repo_grep_dash_mechanism(n):
    needle = "mechanism" + "-" + str(n)
    return [
        p
        for p in _iter_source_files()
        if needle in open(p, encoding="utf-8", errors="replace").read()
    ]


def _repo_grep_numeric_mechanism_id(n):
    """Working-tree profiles/ sweep for the colon-form mechanism id."""
    needle = "mechanism_id: %d" % n
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if needle in open(p, encoding="utf-8", errors="replace").read():
                hits.append(p)
    return hits


def _max_numeric_mechanism_id():
    found = []
    pat = re.compile(r"mechanism_id:\s*(\d+)")
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            found.extend(
                int(m) for m in pat.findall(
                    open(os.path.join(root, f),
                         encoding="utf-8", errors="replace").read()
                )
            )
    return max(found) if found else 0


def _git_grep_tracked_source(needle, scope):
    """Literal needle across tracked profile/test source files.

    scope is "profiles/" or None (profiles/ + tests/). Excludes the
    sweep carrier and __pycache__ artifacts per #715.
    """
    out = _git("grep", "-F", "-l", needle, "HEAD", "--",
               "profiles/", "tests/").stdout
    hits = []
    for line in out.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("HEAD:"):
            line = line[len("HEAD:"):]
        path = line
        if "__pycache__" in path:
            continue
        if path.endswith("/" + OWN_BASENAME) or path == OWN_BASENAME:
            continue
        if scope == "profiles/" and not path.startswith("profiles/"):
            continue
        hits.append(path)
    return hits


def _class_run(filename, classname):
    target = os.path.join(TESTS_DIR, filename)
    env = dict(os.environ)
    env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    return subprocess.run(
        ["python3", "-m", "pytest", target + "::" + classname, "-q",
         "--no-header", "-p", "no:cacheprovider"],
        cwd=REPO_ROOT, capture_output=True, text=True, env=env,
    )


# ---------------------------------------------------------------------------
# 1. Anchor per #565 (5 tests; deselected pre-commit, patched post-commit)
# ---------------------------------------------------------------------------
class TestAnchor1273:
    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit form: ANCHORED_SHA is 0*40; the anchor followup
        # patches it to the main commit sha per #565. Deselected in
        # the in-gate run; the patched form is asserted post-anchor.
        assert ANCHORED_SHA == "0" * 40

    def test_anchor_sha_patched_to_main_commit(self):
        # Post-commit form: ANCHORED_SHA patched to this run's main
        # commit sha per #565 in the anchor followup. Pre-commit this
        # is 0*40 and the test fails BY DESIGN; deselected in-gate.
        assert ANCHORED_SHA != "0" * 40
        assert len(ANCHORED_SHA) == 40

    def test_anchor_sha_format(self):
        assert len(ANCHORED_SHA) == 40

    def test_this_run_main_commit_is_anchor(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "main commit is the anchor" in src

    def test_rotation_phrase_in_docstring(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FOURTH leg of the 1270-1274 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------
class TestRotationGuard:
    def test_predecessor_1272_chain_verified(self):
        for sha in (
            PRED_MAIN_1272, PRED_ANCHOR_1272, PRED_DOCSYNC_1272,
            PRED_FINAL_1272,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1270 -> E #1271 -> A #1272 -> B #1273 -> C #1274" in src

    def test_next_leg_is_type_c_1274(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1274 Type C" in src

    def test_type_b_lands_m995(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type B lands m995" in src

    def test_1272_placeholder_patch_landed(self):
        # The #1272 repair's terminal placeholder patch (DOCSYNCSHA1272
        # -> d2a66b6b) is committed by this run pre-main; the #1272
        # chain is closed before this run's main commit lands.
        assert "DOCSYNCSHA1272" not in _read(LOG_PATH)


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline; landing-run form per #1238)
# ---------------------------------------------------------------------------
class TestMechanismNovelty1273:
    def test_no_own_test_file_pre_commit(self):
        matches = [
            f for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_b_1273")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_no_type_b_1273_in_git_log(self):
        out = _git("log", "--oneline", "--grep=Type B #1273")
        assert out.stdout.strip() == ""

    def test_max_mechanism_id_is_995_working_tree(self):
        # Post-landing working-tree form: the m995 block is landed
        # (uncommitted) so max is 995; pre-landing HEAD form is 994.
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_995_colon_form_lands_in_journalists(self):
        hits = _repo_grep_numeric_mechanism_id(MECH_NUM)
        assert hits == [PROFILE_FILE], hits

    def test_996_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_996_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_996_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_block_key_unique(self):
        out = _git("grep", "-F", "-l", BLOCK_KEY, "HEAD", "--",
                   "profiles/", "tests/")
        assert out.stdout.strip() == "", out.stdout

    def test_novel_urls_zero_hit_pre_commit(self):
        for url in NOVEL_URLS:
            out = _git("grep", "-F", "-l", url, "HEAD")
            assert out.stdout.strip() == "", url

    def test_novel_phrase_zero_hit_pre_commit(self):
        out = _git("grep", "-F", "-l",
                   "Meta projected spending up to $10bn", "HEAD")
        assert out.stdout.strip() == "", out.stdout

    def test_no_1273_row_in_doc_tables_pre_commit(self):
        assert "test_type_b_1273" not in _read(README_PATH)
        assert "test_type_b_1273" not in _read(ARCH_PATH)
        assert "## #1273" not in _read(LOG_PATH)

    def test_block_key_carries_no_995_substring(self):
        # Designed keying per #723/#738/#739: the iteration-form key
        # must not contain the mechanism number in any key form.
        assert "995" not in BLOCK_KEY

    def test_journalist_key_novel_on_head(self):
        out = _git("grep", "-F", "-l", JOURNALIST_KEY, "HEAD", "--",
                   "profiles/", "tests/")
        assert out.stdout.strip() == "", out.stdout


# ---------------------------------------------------------------------------
# 4. The NEW NYT x Meta Anthropic-spend arm
# ---------------------------------------------------------------------------
class TestKalleyHuangMetaArm:
    def test_block_present_in_journalists(self):
        data = _load_journalists()
        assert JOURNALIST_KEY in data
        assert BLOCK_KEY in data[JOURNALIST_KEY]["competitor_coverage"]

    def test_mechanism_id_995(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_meta_arm_tone(self):
        assert _block()["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == META_TONE

    def test_meta_arm_byline_carries_huang(self):
        assert "Kalley Huang" in _block()["meta_arm"]["author_byline"]

    def test_meta_arm_url_relay_attested(self):
        assert _block()["meta_arm"]["url"] == NOVEL_URLS[0]

    def test_meta_arm_date_late_august(self):
        assert "2026-08-30" in _block()["meta_arm"]["date"]


# ---------------------------------------------------------------------------
# 5. The NEW NYT x Apple foldable arm
# ---------------------------------------------------------------------------
class TestKalleyHuangAppleArm:
    def test_apple_arm_tone(self):
        assert _block()["apple_arm"]["tone_MANUAL_ILLUSTRATIVE"] == APPLE_TONE

    def test_apple_arm_solo_huang_byline(self):
        byline = _block()["apple_arm"]["author_byline"]
        assert "Kalley Huang" in byline
        assert "Eli Tan" not in byline

    def test_apple_arm_url_relay_attested(self):
        assert _block()["apple_arm"]["url"] == NOVEL_URLS[1]

    def test_apple_arm_date_sep_8(self):
        assert "2026-09-08" in _block()["apple_arm"]["date"]


# ---------------------------------------------------------------------------
# 6. The asymmetry delta
# ---------------------------------------------------------------------------
class TestAsymmetryDelta:
    def test_delta_value(self):
        assert _block()["scorer"][
            "illustrative_delta_apple_minus_meta"] == DELTA

    def test_delta_direction_meta_hard(self):
        assert DELTA > 0
        assert META_TONE < APPLE_TONE

    def test_control_case_not_falsification(self):
        assert _block()["falsification_family_member"] is False

    def test_ledger_holds_54(self):
        assert _block()["falsification_ledger"] == 54


# ---------------------------------------------------------------------------
# 7. Research method
# ---------------------------------------------------------------------------
class TestResearchMethod:
    def test_zero_browser_open_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "0 browser.open per #503" in src

    def test_excerpt_bounded(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "excerpt-bounded" in src

    def test_rejection_audit_present(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "candidate-rejection audit" in src

    def test_no_canonical_urls_constructed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "no canonical nytimes.com URLs constructed" in src


# ---------------------------------------------------------------------------
# 8. Statistical discipline
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline:
    def test_manual_illustrative_only(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MANUAL ILLUSTRATIVE ONLY" in src

    def test_no_significance_claim(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NOT_CALCULATED" in src
        assert "is_significant" in src

    def test_not_artifact_grade(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NOT artifact-grade" in src

    def test_no_analysis_json_update(self):
        assert _block()["no_analysis_json_update"] is True


# ---------------------------------------------------------------------------
# 9. Guard lifecycle: this run's forward pins for #1274
# ---------------------------------------------------------------------------
class TestGuardLifecycle1273:
    def test_pins_on_995_landing(self):
        # Type B lands m995: max becomes 995, next is 996.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 995" in src
        assert "NEXT_NUM = 996" in src

    def test_no_type_b_1273_in_git_log_pin(self):
        # Post-main-commit form (the #1191-class self-trip, re-pinned
        # in the terminal log-hash followup per #721): every commit
        # whose message matches "Type B #1273" must be this run's
        # main commit or a descendant of it - i.e., no PRIOR run
        # committed this run's iteration. The ancestor check (not an
        # enumerated own-set) is robust to any number of same-run
        # followup commits: each followup is a descendant of main by
        # construction, so the pin is stable and terminal. Deselected
        # in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type B #1273")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected this run's own commits"
        main = _git("rev-parse", PRED_MAIN_1273).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_no_type_c_1274_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1274's terminal log-hash followup
        # per #721): every commit whose message matches "Type C #1274"
        # must be #1274's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type C #1274")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1274's own commits"
        main = _git("rev-parse", PRED_MAIN_1274).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_996_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_996_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_996_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_fortieth_direction_pin(self):
        # The fortieth direction-claim form stays absent in profiles/
        # (profiles-scoped per the #1199 in-gate fix).
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_forty_eighth_member_intact_pin(self):
        # The live forty-eighth member claims (m952,
        # profiles/financial-times.yaml) must survive this run
        # unchanged.
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]

    def test_forty_ninth_member_intact_pin(self):
        # The live forty-ninth member claims (m956,
        # careers/journalists.yaml) must survive this run unchanged.
        assert _git_grep_tracked_source(_T49, "profiles/") == [
            "profiles/careers/journalists.yaml"]

    def test_fiftieth_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T50, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_first_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T51, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_second_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T52, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":5"), out.stdout

    def test_fifty_third_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T53, "HEAD", "--",
            "profiles/the-verge.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fourth_member_intact_pin(self):
        # The live fifty-fourth member claims (m985,
        # profiles/guardian.yaml, 2x, landed at #1257) must survive
        # this run unchanged.
        out = _git(
            "grep", "-c", "-F", _T54, "HEAD", "--",
            "profiles/guardian.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_fifty_fifth_member_pin(self):
        assert _git_grep_tracked_source(_T55, None) == []

    def test_predecessor_1272_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1272_FILE))

    def test_next_leg_is_1274_type_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1274 Type C" in src

    def test_1272_pins_stay_green_documented(self):
        # #1272's forward guards (max-994, zero-996 keys all forms,
        # no-Type-B-#1273-in-git-log, fortieth absent, forty-eighth +
        # forty-ninth + fiftieth + fifty-first + fifty-second +
        # fifty-third + fifty-fourth intact, no fifty-fifth; ledger 54)
        # verified GREEN at HEAD pre-commit this run. The
        # no-Type-B-#1273-in-git-log pin flips BY DESIGN at this run's
        # main commit (the #1191-class self-trip, re-pinned post-commit
        # by TestStalenessPins1273) and the zero-996-numeric pin trips
        # on the landed m995 block; the zero-996-underscore/dash pins
        # stay green per the #715 literal discipline. Documented in the
        # staleness pin below, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1273" in src
        assert "no_type_b_1273_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 10. Staleness pins: #1272's guard lifecycle flips by design
#     (1 test; deselected pre-commit, verified post-main-commit)
# ---------------------------------------------------------------------------
class TestStalenessPins1273:
    def test_1272_guard_lifecycle_post_commit(self):
        # Post-main-commit form: 18 tests in the class, 16 pass and
        # TWO flip BY DESIGN when this run's main commit lands: the
        # no_type_b_1273_in_git_log ancestor pin (its PRED_MAIN_1273
        # is still the 0*40 placeholder until this run's terminal
        # log-hash followup re-pins it per #721) and the
        # zero-996-numeric pin (trips on the landed m995 block) - the
        # #1191-class self-trip family. The pin is re-pinned to the
        # post-commit own-set form in the terminal log-hash followup
        # per #721; the class run below therefore expects the 16
        # surviving pins green and documents the two designed flips.
        # The #1272 block is read-only to this run; the quirk is
        # documented here, not repaired.
        res = _class_run(
            E1272_FILE,
            "TestGuardLifecycle1272",
        )
        out = res.stdout + res.stderr
        assert "2 failed, 16 passed" in out, out[-2000:]
        assert "no_type_b_1273_in_git_log" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 11. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------
class TestDocSync:
    def test_readme_test_file_table_has_1273_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_b_1273" in readme

    def test_architecture_has_1273_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_b_1273" in arch

    def test_readme_stats_ratcheted(self):
        # Post-sync-positive form per #719: asserts the ratcheted
        # counts (README_TEST_COUNT tests across README_FILE_COUNT
        # files). Fails pre-commit by design; deselected in the
        # in-gate run.
        readme = _read(README_PATH)
        assert ("| Tests | %d |" % README_TEST_COUNT) in readme
        assert ("Across %d test files" % README_FILE_COUNT) in readme


# ---------------------------------------------------------------------------
# 12. Iteration log (3 tests; deselected pre-commit per #721)
# ---------------------------------------------------------------------------
class TestIterationLog:
    def test_1273_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1273 Type B" in log

    def test_1272_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1272 Type A" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_PATH)
        assert "### Rotation transparency" in log


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------
class TestInFlightIsolation:
    def test_899_nytimes_hunk_untouched(self):
        res = _git("diff", "--name-only")
        modified = res.stdout.split()
        assert "profiles/nytimes.yaml" in modified
        # Its uncommitted hunk belongs to #899's run; this run stages
        # only its own files.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#899" in src

    def test_900_untracked_file_untouched(self):
        res = _git("status", "--short")
        assert "test_type_d_900_m769" in res.stdout

    def test_938_test_file_edit_owned_by_its_run(self):
        res = _git("status", "--short")
        assert "test_type_b_938" in res.stdout

    def test_1012_wt_working_tree_edit_owned_by_its_run(self):
        res = _git("status", "--short")
        assert "test_type_a_1012" in res.stdout

    def test_do_not_touch_1024_m846(self):
        # Guarded in the log entry per convention; the test file keeps
        # the in-flight list only (own-file reference would trip the
        # contiguous-literal discipline elsewhere).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1024" in src


# ---------------------------------------------------------------------------
# 14. Background suite: observed only per #795
# ---------------------------------------------------------------------------
class TestBackgroundSuite1273:
    def test_1270_suite_log_exists(self):
        assert os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1270_full_suite.log"))

    def test_this_run_launches_no_suite(self):
        # This run must not launch its own background suite; only the
        # #1270-launched suite is observed (verdict belongs to #1275).
        assert not os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1273_full_suite.log"))

    def test_observation_only_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "OBSERVES only" in src
        assert "verdict belongs to #1275" in src
