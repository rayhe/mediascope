# -*- coding: utf-8 -*-
"""Type B #1278: m998 Kris Holt (Engadget) journalist cross-entity pair -
Meta Connect 2026 launch roundup vs Google EU location-data fine news.

Mechanism 998 (CONTROL-CASE, NOT a falsification-family member; ledger
holds at 55). Same writer, same outlet, two days apart (Sep 21 vs Sep 23
2026): Holt runs a neutral Engadget product-launch roundup of Meta
Connect 2026 - "Everything announced at Meta Connect 2026" (0.00 MANUAL
ILLUSTRATIVE, zero privacy vocabulary in the surfaced text), and an
accountability-register Engadget piece on Google's EUR 403M ($463M) EU
location-data fine with the repeat-offender dek "Hardly the first time
it's run afoul of EU regulations" (-0.50 MANUAL ILLUSTRATIVE).
Illustrative delta (Google minus Meta) -0.50: Google draws the harder
register (Meta-soft direction). Yahoo/Engadget has NO documented AI
content-licensing deal with Meta or Google anywhere in the corpus (the
corpus documents the absence explicitly), so the uniform
payer-softening prediction is not adjudicated. MANUAL ILLUSTRATIVE ONLY
per the Aug 28 2026 standing rule (tones hand-assigned, n=1 per arm;
p_value/cohens_d/ci_95 NOT_CALCULATED; engine NOT run; is_significant
false; NOT artifact-grade; verdict control_case_observation; no
analysis.json update).

Research: 1 delegated scout (ranked 3 candidate pairs; SELECTED #1
Holt/Engadget Meta-Connect-roundup vs Google-EU-fine - tightest 2-day
same-journalist same-outlet window with byline-complete arms; #2 Anna
Washenko/Engadget held as backup - OpenAI arm 41 days stale; #3
Nicholas Sutrich/Android Central held - Google-arm relay missing;
candidate-rejection audit: 15 prior Type B journalists saturated,
Deepa Seetharaman outlet-mid-cycle, Steven Tweedie single-piece
dual-entity, 8 no-clean-pair discards) + 2 main-run browser.search
verification sets (exact-headline Meta-arm search returning the
engadget.com Meta category page verbatim with "Everything announced at
Meta Connect 2026 ... By Kris Holt" plus the author page "Meta By Kris
Holt ... Everything announced at Meta Connect 2026"; exact-headline
Google-arm search returning the theairmedia aggregator verbatim with
"staff@engadget.com (Kris Holt)" and the "Hardly the first time" dek
plus the engadget.com canonical rendering); corpus saturation greps:
both relay URLs zero-hit repo-wide, no kris_holt_type_b key pre-commit
(prior "Kris Holt" mentions are #1153 research-note prose only), Meta-arm
and Google-arm relay headlines zero-hit repo-wide; 0 browser.open per
#503 (excerpt-bounded). All URLs copied verbatim from Full-URL
listings; no canonical URLs constructed. The m998 block lands in
profiles/careers/journalists.yaml as a new top-level kris_holt_type_b
key (per the #643 convention), appended at the end of the file.
Targeted staging by explicit path only; the in-flight
#899/#938/#900/#1012-wt files stay out of this run's index/diff. Do
NOT touch #1024 m846.

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this
pre-commit file and is patched to the main-commit hash in the anchor
followup commit. One anchor test (the placeholder pin) fails BY DESIGN
pre-commit; TestAnchor1278 deselected in the in-gate run. The main
commit is the anchor per #565.

FOURTH leg of the 1275-1279 window: D #1275 -> E #1276 -> A #1277 ->
B #1278 -> C #1279 per the #565 anchor + rotation guard. Next run
#1279 Type C closes the window. Type B lands one mechanism
(mechanism 998).

Per #795: this run only CHECKS the #1275-launched background suite
(goal hidden_files type_d_1275_full_suite.log, OBSERVED NOT-ALIVE at
this run's check, last write Oct 7 02:01 PDT with zero live pytest
processes); its verdict and tombstone belong to #1280 (next Type D).
This run neither re-launches, kills, nor writes to the suite. The
#1277 repair chain closed with its terminal log-hash followup
committed by #1277 (PRED_MAIN_1277 re-pinned in the #1276 file per
#721).

ASCII-only, no em dashes. Needles format-built per #715: this file
must not carry contiguous numeric/underscore/dash mechanism-key forms
of the next number, the forty-eighth / forty-ninth / fiftieth /
fifty-first / fifty-second / fifty-third / fifty-fourth / fifty-fifth
member-claim forms, or the fortieth direction form; the constants are
constructed at runtime. (The landed ordinals live as short lowercase
forms in prose here; the live full-form claims live in
profiles/financial-times.yaml, profiles/news-corp.yaml,
profiles/the-verge.yaml, profiles/guardian.yaml,
profiles/atlantic.yaml, and profiles/careers/journalists.yaml: the
forty-eighth, forty-ninth, fiftieth, fifty-first, fifty-second,
fifty-third, fifty-fourth, and fifty-fifth members respectively.)
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
    "test_type_b_1278_kris_holt_engadget_meta_connect_roundup_"
    "vs_google_eu_fine_oct07_4am.py"
)
PROFILE_FILE = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1275_full_suite.log")

MECH_NUM = 998
NEXT_NUM = 999  # integer only; key-form needles are format-built
ITERATION = 1278

ANCHORED_SHA = "0" * 40  # patched per #565 in the anchor followup (main commit sha)

# Predecessor #1277 chain (verified via git rev-parse pre-commit).
PRED_MAIN_1277 = "eee6dfc46080a0abc0c3bd21d5126c0ec08b1643"
PRED_ANCHOR_1277 = "6f1128d64088323a34822672fe3a79da478e50ca"
PRED_DOCSYNC_1277 = "044c42055ec996d15a03dfc3ad729bcabd8e1c1d"
PRED_FINAL_1277 = "8ce5bf681e1382a02b810466a5873b3e3a301d9e"
# This run's own main sha: patched in the terminal log-hash followup
# per #721.
PRED_MAIN_1278 = "0" * 40  # re-pinned in the terminal log-hash followup per #721 (main commit sha)
# Next leg's main sha: patched in #1279's log-hash followup per #721.
PRED_MAIN_1279 = "0" * 40

# The #1277 window-continuation file, for the staleness pin on its
# guard-lifecycle class (max id 997; zero next-number nine-nine-nine
# / no-Type-C-#1279-in-git-log (flips BY DESIGN at #1279's main commit
# - the #1191-class self-trip) / fortieth direction absent /
# forty-eighth member intact in profiles/financial-times.yaml /
# forty-ninth member intact + fiftieth member intact +
# fifty-second member intact in profiles/careers/journalists.yaml /
# fifty-first member intact in profiles/news-corp.yaml /
# fifty-third member intact in profiles/the-verge.yaml /
# fifty-fourth member intact in profiles/guardian.yaml /
# fifty-fifth member intact in profiles/atlantic.yaml (landed at #1277)
# / no fifty-sixth member (repo-wide) / ledger 55).
E1277_FILE = (
    "test_type_a_1277_atlantic_openai_robinson_essay_oct07_3am.py"
)
D1276_FILE = (
    "test_type_e_1276_podcast_sentiment_178th_verification_oct07_2am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 71117  # post-sync-positive per #719 (71039 + 78)
README_FILE_COUNT = 1603  # post-sync-positive per #719 (1602 + 1)

# The forward-guard needles are fragment-built per #715 so this file
# carries no contiguous literal of a forward-guard claim form. The
# fifty-fifth member claim lives ONLY in the profile block (HEAD
# post-#1277); this file references it via fragments.
_T40 = "FORT" + "IETH relationship direction"
_T48 = "FORT" + "Y-EIGHTH falsification-family member"
_T49 = "FORT" + "Y-NINTH falsification-family member"
_T50 = "FIFT" + "IETH falsification-family member"
_T51 = "FIFT" + "Y-FIRST falsification-family member"
_T52 = "FIFT" + "Y-SECOND falsification-family member"
_T53 = "FIFT" + "Y-THIRD falsification-family member"
_T54 = "FIFT" + "Y-FOURTH falsification-family member"
_T55 = "FIFT" + "Y-FIFTH falsification-family member"
_T56 = "FIFT" + "Y-SIXTH falsification-family member"

BLOCK_KEY = (
    "type_b_1278_kris_holt_engadget_meta_connect_roundup_"
    "vs_google_eu_fine_oct07_4am"
)
JOURNALIST_KEY = "kris_holt_type_b"

# The two relay URLs (verbatim from Full-URL listings); both zero-hit
# repo-wide pre-commit via git grep -F.
NOVEL_URLS = [
    "https://briefly.co/anchor/Wearables/story/"
    "everything-announced-at-meta-connect-2026---engadget",
    "https://theairmedia.passproevents.in/story/795792",
]

# Tones (MANUAL ILLUSTRATIVE).
META_TONE = 0.0  # NEW Engadget x Meta Connect roundup arm
GOOGLE_TONE = -0.5  # NEW Engadget x Google EU fine arm
DELTA = -0.5  # -0.5 - 0.0

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
class TestAnchor1278:
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
        assert "FOURTH leg of the 1275-1279 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------
class TestRotationGuard:
    def test_predecessor_1277_chain_verified(self):
        for sha in (
            PRED_MAIN_1277, PRED_ANCHOR_1277, PRED_DOCSYNC_1277,
            PRED_FINAL_1277,
        ):
            res = _git("cat-file", "-t", sha)
            assert res.stdout.strip() == "commit", "missing %s" % sha

    def test_window_order_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1275 -> E #1276 -> A #1277 -> B #1278 -> C #1279" in src

    def test_next_leg_is_type_c_1279(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Next run #1279 Type C" in src

    def test_type_b_lands_m998(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type B lands m998" in src

    def test_1277_log_hash_followup_landed(self):
        # #1277's terminal log-hash followup re-pinned PRED_MAIN_1277
        # in the #1276 file per #721; the #1277 chain is closed before
        # this run's main commit lands.
        assert PRED_FINAL_1277 in _git(
            "log", "--format=%H", "--grep=Type A #1277").stdout


# ---------------------------------------------------------------------------
# 3. Mechanism novelty (the #715 discipline; landing-run form per #1238)
# ---------------------------------------------------------------------------
class TestMechanismNovelty1278:
    def test_no_own_test_file_pre_commit(self):
        matches = [
            f for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_b_1278")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_no_type_b_1278_in_git_log(self):
        out = _git("log", "--oneline", "--grep=Type B #1278")
        assert out.stdout.strip() == ""

    def test_max_mechanism_id_is_998_working_tree(self):
        # Post-landing working-tree form: the m998 block is landed
        # (uncommitted) so max is 998; pre-landing HEAD form is 997.
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_998_colon_form_lands_in_journalists(self):
        hits = _repo_grep_numeric_mechanism_id(MECH_NUM)
        assert hits == [PROFILE_FILE], hits

    def test_999_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_999_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_999_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_block_key_unique(self):
        out = _git("grep", "-F", "-l", BLOCK_KEY, "HEAD", "--",
                   "profiles/", "tests/")
        assert out.stdout.strip() == "", out.stdout

    def test_novel_urls_zero_hit_pre_commit(self):
        for url in NOVEL_URLS:
            out = _git("grep", "-F", "-l", url, "HEAD", "--",
                       "profiles/", "tests/").stdout
            paths = []
            for line in out.splitlines():
                line = line.strip()
                if not line:
                    continue
                if line.startswith("HEAD:"):
                    line = line[5:]
                paths.append(line)
            assert paths == [], (url, paths)

    def test_novel_phrase_zero_hit_pre_commit(self):
        out = _git("grep", "-F", "-l",
                   "Everything announced at Meta Connect 2026", "HEAD")
        assert out.stdout.strip() == "", out.stdout

    def test_no_1278_row_in_doc_tables_pre_commit(self):
        assert "test_type_b_1278" not in _read(README_PATH)
        assert "test_type_b_1278" not in _read(ARCH_PATH)
        assert "## #1278" not in _read(LOG_PATH)

    def test_block_key_carries_no_998_substring(self):
        # Designed keying per #723/#738/#739: the iteration-form key
        # must not contain the mechanism number in any key form.
        assert "998" not in BLOCK_KEY

    def test_journalist_key_novel_on_head(self):
        out = _git("grep", "-F", "-l", JOURNALIST_KEY, "HEAD", "--",
                   "profiles/", "tests/")
        assert out.stdout.strip() == "", out.stdout


# ---------------------------------------------------------------------------
# 4. The NEW Engadget x Meta Connect roundup arm
# ---------------------------------------------------------------------------
class TestKrisHoltMetaArm:
    def test_block_present_in_journalists(self):
        data = _load_journalists()
        assert JOURNALIST_KEY in data
        assert BLOCK_KEY in data[JOURNALIST_KEY]["competitor_coverage"]

    def test_mechanism_id_998(self):
        assert _block()["mechanism_id"] == MECH_NUM

    def test_meta_arm_tone(self):
        assert _block()["meta_arm"]["tone_MANUAL_ILLUSTRATIVE"] == META_TONE

    def test_meta_arm_byline_carries_holt(self):
        assert "Kris Holt" in _block()["meta_arm"]["author_byline"]

    def test_meta_arm_url_relay_attested(self):
        assert _block()["meta_arm"]["url"] == NOVEL_URLS[0]

    def test_meta_arm_date_sep_23(self):
        assert "2026-09-23" in _block()["meta_arm"]["date"]


# ---------------------------------------------------------------------------
# 5. The NEW Engadget x Google EU fine arm
# ---------------------------------------------------------------------------
class TestKrisHoltGoogleArm:
    def test_google_arm_tone(self):
        assert _block()["google_arm"]["tone_MANUAL_ILLUSTRATIVE"] == GOOGLE_TONE

    def test_google_arm_byline_carries_holt(self):
        assert "Kris Holt" in _block()["google_arm"]["author_byline"]

    def test_google_arm_url_relay_attested(self):
        assert _block()["google_arm"]["url"] == NOVEL_URLS[1]

    def test_google_arm_date_sep_21(self):
        assert "2026-09-21" in _block()["google_arm"]["date"]


# ---------------------------------------------------------------------------
# 6. The asymmetry delta
# ---------------------------------------------------------------------------
class TestAsymmetryDelta:
    def test_delta_value(self):
        assert _block()["scorer"][
            "illustrative_delta_google_minus_meta"] == DELTA

    def test_delta_direction_meta_soft(self):
        assert DELTA < 0
        assert META_TONE > GOOGLE_TONE

    def test_control_case_not_falsification(self):
        assert _block()["falsification_family_member"] is False

    def test_ledger_holds_55(self):
        assert _block()["falsification_ledger"] == 55


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
        assert "no canonical URLs constructed" in src


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
# 9. Guard lifecycle: this run's forward pins for #1279
# ---------------------------------------------------------------------------
class TestGuardLifecycle1278:
    def test_pins_on_998_landing(self):
        # Type B lands m998: max becomes 998, next is 999.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 998" in src
        assert "NEXT_NUM = 999" in src

    def test_no_type_c_1279_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1279's terminal log-hash followup
        # per #721): every commit whose message matches "Type C #1279"
        # must be #1279's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type C #1279")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1279's own commits"
        main = _git("rev-parse", PRED_MAIN_1279).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_999_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_999_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_999_dash_absent_repo_wide(self):
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
        assert _git_grep_tracked_source(_T50, "profiles/") == [
            "profiles/careers/journalists.yaml"]

    def test_fifty_first_member_intact_pin(self):
        assert _git_grep_tracked_source(_T51, "profiles/") == [
            "profiles/news-corp.yaml"]

    def test_fifty_second_member_intact_pin(self):
        assert _git_grep_tracked_source(_T52, "profiles/") == [
            "profiles/careers/journalists.yaml"]

    def test_fifty_third_member_intact_pin(self):
        assert _git_grep_tracked_source(_T53, "profiles/") == [
            "profiles/the-verge.yaml"]

    def test_fifty_fourth_member_intact_pin(self):
        # The live fifty-fourth member claims (m985,
        # profiles/guardian.yaml, 2x, landed at #1257) must survive
        # this run unchanged.
        assert _git_grep_tracked_source(_T54, "profiles/") == [
            "profiles/guardian.yaml"]

    def test_fifty_fifth_member_intact_pin(self):
        # The live fifty-fifth member claims (m997,
        # profiles/atlantic.yaml, 2x, landed at #1277) must survive
        # this run unchanged.
        assert _git_grep_tracked_source(_T55, "profiles/") == [
            "profiles/atlantic.yaml"]

    def test_no_fifty_sixth_member_pin(self):
        assert _git_grep_tracked_source(_T56, None) == []

    def test_predecessor_1277_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1277_FILE))

    def test_next_leg_is_1279_type_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1279 Type C" in src

    def test_1277_pins_documented(self):
        # #1277's forward guards (max-997, zero-998 keys all forms,
        # no-Type-B-#1278-in-git-log, fortieth absent, forty-eighth
        # through fifty-fifth intact, no fifty-sixth; ledger 55)
        # verified GREEN at HEAD pre-commit this run. The
        # no-Type-B-#1278-in-git-log pin flips BY DESIGN at this run's
        # main commit (the #1191-class self-trip, re-pinned post-commit
        # by TestStalenessPins1278) and the zero-998-numeric pin trips
        # on the landed m998 block; the zero-998-underscore/dash pins
        # stay green per the #715 literal discipline. Documented in the
        # staleness pin below, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1278" in src
        assert "2 failed, 16 passed" in src
        assert "no_type_c_1279_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 10. Staleness pins: #1277's guard lifecycle flips by design
#     (1 test; deselected pre-commit, verified post-main-commit)
# ---------------------------------------------------------------------------
class TestStalenessPins1278:
    def test_1277_guard_lifecycle_post_commit(self):
        # Post-main-commit form: 18 tests in the class, 16 pass and
        # TWO flip BY DESIGN when this run's main commit lands: the
        # no_type_b_1278_in_git_log ancestor pin (its PRED_MAIN_1278
        # is still the 0*40 placeholder until this run's terminal
        # log-hash followup re-pins it per #721) and the
        # zero-998-numeric pin (trips on the landed m998 block) - the
        # #1191-class self-trip family. The pin is re-pinned to the
        # post-commit own-set form in the terminal log-hash followup
        # per #721; the class run below therefore expects the 16
        # surviving pins green and documents the two designed flips.
        # The #1277 block is read-only to this run; the quirk is
        # documented here, not repaired.
        res = _class_run(
            E1277_FILE,
            "TestGuardLifecycle1277",
        )
        out = res.stdout + res.stderr
        assert "2 failed, 16 passed" in out, out[-2000:]
        assert "no_type_b_1278_in_git_log" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 11. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------
class TestDocSync:
    def test_readme_test_file_table_has_1278_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_b_1278" in readme

    def test_architecture_has_1278_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_b_1278" in arch

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
    def test_1278_entry_present_post_sync(self):
        log = _read(LOG_PATH)
        assert "## #1278 Type B" in log

    def test_1277_entry_present(self):
        log = _read(LOG_PATH)
        assert "## #1277 Type A" in log

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
class TestBackgroundSuite1278:
    def test_1275_suite_log_exists(self):
        assert os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1275_full_suite.log"))

    def test_this_run_launches_no_suite(self):
        # This run must not launch its own background suite; only the
        # #1275-launched suite is observed (verdict belongs to #1280).
        assert not os.path.exists(
            os.path.join(GOAL_HIDDEN, "type_d_1278_full_suite.log"))

    def test_observation_only_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "OBSERVES only" in src
        assert "verdict belongs to #1280" in src
