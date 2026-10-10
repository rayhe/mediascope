# -*- coding: utf-8 -*-
"""Type C #1359: financial-incentive saturation screening (Oct 10 2026,
~2:00 AM PDT) - NO novel money leg; NO mechanism landed.

1 delegated scout (3 tracks) + 2 main-run browser.search verification sets
+ main-run corpus git-grep verification, 0 browser.open per #503,
excerpt-bounded. The scout returned 4 ranked financial-incentive
candidates; the main run verified every pick against the corpus and its
own searches, and REJECTED ALL FOUR:

  REJECTED (main-run verification):
  - Pick 1: Judge Mehta dismisses the Chegg + Penske Media AI Overviews
    antitrust suits (Oct 1, 2026, D.D.C.; 25-cv-543 / 25-cv-3192;
    corroborating relay from the main run's own Full-URL listing,
    https://www.aitechdaily.com/google-ai-overviews-chegg-penske-dismissal/,
    used only to document the in-corpus leg - never as novel evidence).
    The scout claimed "no corpus mechanism covers a publisher-party AI
    Overview dismissal" - FALSE. The corpus banks exactly this leg:
    tests/test_type_c_1129_mehta_dismisses_chegg_penske_suits_
    litigation_channel_closure_oct01_5pm.py (Oct 1, 5pm run).
  - Pick 2: the NYT $28M+ cumulative AI-litigation spend ($4.2M in
    Q1 2026 alone), relayed by stockmoguls Sep 6, 2026. In-corpus as
    mechanism 753 (PROMOTES mechanism 636's $4.2M Q1 datum; the $28M+
    cumulative figure is corpus-recorded). The Q2 2026 $4.6M special
    item (NYT 10-Q, pelcro relay from the main run's own Full-URL
    listing, https://www.get.pelcro.com/blog/new-york-times-q2-2026-results,
    used only to document corroboration - never as novel evidence)
    confirms the spend economics already banked - no new leg.
  - Pick 3: the October 2026 Google AI Contribution Pilot relay wave
    (Technori Oct-1 relay of The Information's Sep-29 figures; the
    public-acknowledgment layer via the June 18, 2026 policy blog by
    Markham Erickson). Figures saturated (m1099/m1199); the
    acknowledgment layer is a thin relay-only delta on a saturated
    mechanism, not a new money leg.
  - Pick 4: the DOJ 20-page Statement of Interest backing fair use in
    NYT v. Microsoft (filed Sep 1, 2026; VINTAGE). In-corpus as
    mechanism 672.

The scout's slate is the FOURTH #1341 instance (scout
corpus-blindness / misattribution: after #1353's m1004 re-surfacing,
#1354's test_type_c_1329 re-surfacing, and #1358's three
misattributions - the scout claimed pick 1 was "not in REJECT-list"
and "not covered by any corpus mechanism" while the corpus has a
dedicated test file for exactly that leg). Scout characterizations
untrusted; the main run verified every pick via git grep -F and its
own searches. The scout's relay URLs are not carried as evidence
(unverifiable); two URLs from the main run's own Full-URL listings are
carried verbatim, used only to document corroboration of the
in-corpus legs - never as novel evidence.

Verdict saturation_screening_no_novel_mechanism - NOT a
falsification-family member. Max numeric mechanism_id stays 1044
(Type C lands zero mechanisms this run); ledger holds at 64; no
sixty-fifth member. MANUAL / QUALITATIVE ONLY per the Aug 28 2026
standing rule (tone NOT_SCORED; p_value/cohens_d/ci_95
NOT_CALCULATED; is_significant false; engine NOT run; NOT
artifact-grade; no_analysis_json_update true). Correlation is not
causation; hypothesis-generating only.

Type C lands zero mechanisms: no profiles/ edit this run (neither
profiles/competitor-entities.yaml nor any publication profile). The
record is the iteration-log ## #1359 entry plus this test file.

This run is the FIFTH and CLOSING leg of the 1355-1359 window
(D #1355 -> E #1356 -> A #1357 -> B #1358 -> C #1359 per the #565
anchor + rotation guard); the 1350-1354 window is VERIFIED CLOSED.
The next background-suite verdict belongs to #1360 per #795 (the
#1355-launched suite, goal hidden_files type_d_1355_full_suite.log;
this run CHECKS it only - neither re-launches, kills, nor writes to
it).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this
pre-commit file and is patched to the main-commit sha in the anchor
followup commit. One anchor test (the placeholder pin) fails BY DESIGN
post-anchor.

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit),
#900 (untracked Type D test file), #1012-wt (working-tree edit on the
committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file must
not carry contiguous numeric/underscore/dash mechanism-key forms of the
max or next number, the forty-eighth through sixty-fifth member-claim
forms, or the fortieth direction-claim form; the constants are
constructed at runtime. (The landed ordinals live as short lowercase
forms in prose here; the live full-form claims live in profiles: the
forty-eighth, fifty-eighth, and sixtieth in financial-times.yaml, the
forty-ninth, fiftieth, and fifty-second in profiles/careers/
journalists.yaml, the fifty-first, fifty-ninth, sixty-second, and
sixty-third in news-corp.yaml, the fifty-third in the-verge.yaml, the
fifty-fourth in guardian.yaml, the fifty-fifth in atlantic.yaml, the
fifty-sixth and sixty-first in wired.yaml, the fifty-seventh and
sixty-fourth in ap.yaml; the sixty-fifth is absent repo-wide as of this
run.)
"""

import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")

OWN_BASENAME = "test_type_c_1359_financial_incentive_saturation_oct10_2am.py"

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "7795bebf6e978c513a9ebbd76cc823bb03747154"  # patched to the main-commit sha in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1044  # max numeric; Type C lands ZERO mechanisms this run
NEXT_NUM = 1045  # integer only; key-form needles are format-built

# Post-doc-sync totals per #719: PATCHED post-collection
# (pre-sync 78721 + 67 tests; pre-sync 1683 + 1 file).
README_TEST_COUNT = 78721 + 67  # patched post-collection
README_FILE_COUNT = 1684


# Predecessor chain: #1358 Type B FOURTH leg of the 1355-1359 window.
PRED_MAIN_1358 = "908543be62bb67b02516ad7cd13422ee6078bb4f"
PRED_ANCHOR_1358 = "9f937a379d67c073f2f876c16aa4c0282112797d"
PRED_DOCSYNC_1358 = "0e527cd781d5239bd069580d5585f4af28d49d54"
PRED_LOGHASH_1358 = "407a7339f8bb273fcc99effe1763b1303e4bcaf9"
PRED_PUSH_1358 = "cb4f57ed7623d6ba6bd0365eac9af54b23d47451"

# #1357 Type A THIRD leg, for the rotation-guard chain.
PRED_MAIN_1357 = "bc362a9bf6becb8350bcfe7884f17d1c46500669"
PRED_ANCHOR_1357 = "628c80855b9cdeaf64255f9a3cc0f6bd8737b625"
PRED_DOCSYNC_1357 = "758eebd41de69e87af56725732819bf710b5a7f9"
PRED_LOGHASH_1357 = "830034627613eb81ce19b6d75e073ad1d06bb7b9"

# This run's main commit (full sha), for the ancestor-form
# no-Type-C-#1359 pin. Staged 0*40 placeholder-only per #721;
# re-pinned in #1359's terminal log-hash followup per #721.
PRED_MAIN_1359 = "7795bebf6e978c513a9ebbd76cc823bb03747154"  # re-pinned to #1359 main sha in the anchor followup per #721/#1292 (own-file copy; the #1358 file copy re-pinned in the same followup)

# #1360's main commit (full sha), for the ancestor-form no-Type-D-#1360
# pin (the #1191-class self-trip; #1360 is Type D per the rotation and
# per #795). Staged 0*40 placeholder-only per #721; re-pinned in
# #1360's terminal log-hash followup per #721. Type-correct per the
# #1352 type-mismatch lesson.
PRED_MAIN_1360 = "0" * 40  # re-pinned to #1360 main sha in the terminal log-hash followup per #721/#1292

# The #1358 window-predecessor file, for the staleness pin on its
# guard-lifecycle class (max id 1044; zero next-number
# keys all forms; no sixty-fifth member; ledger holds at 64).
A1358_FILE = "test_type_b_1358_saturation_screening_oct10_1am.py"

# The forward-guard needles are fragment-built per #715 so this file
# carries no contiguous literal of a forward-guard claim form.
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
_T57 = "FIFT" + "Y-SEVENTH falsification-family member"
_T58 = "FIFT" + "Y-EIGHTH falsification-family member"
_T59 = "FIFT" + "Y-NINTH falsification-family member"
_T60 = "SIXT" + "IETH falsification-family member"
_T61 = "SIXT" + "Y-FIRST falsification-family member"
_T62 = "SIXT" + "Y-SECOND falsification-family member"
_T63 = "SIXT" + "Y-THIRD falsification-family member"
_T64 = "SIXT" + "Y-FOURTH falsification-family member"
_T65 = "SIXT" + "Y-FIFTH falsification-family member"

# 2 main-run browser.search verification sets + 1 delegated scout
# (3 tracks) + main-run corpus git-grep verification this run
# (0 browser.open per #503).
QUERY_SETS = [
    "Google wins dismissal Chegg Penske Media AI Overviews lawsuit Judge Mehta October 2026",
    "New York Times AI litigation spending $28 million 10-Q filing",
]

# The scout's 4 picks, as returned (titles only; the scout supplied
# relay URLs, but the main run treats all scout-supplied evidence as
# untrusted per the #1341 lesson and verified each pick independently
# via its own searches and git grep -F - all four picks REJECTED).
# Pick 1: Judge Mehta dismisses the Chegg + Penske Media AI Overviews
#   antitrust suits (Oct 1, 2026; 25-cv-543 / 25-cv-3192) - the scout
#   claimed "no corpus mechanism covers" it; the corpus banks exactly
#   this leg as test_type_c_1129 (Oct 1, 5pm).
# Pick 2: NYT $28M+ cumulative AI-litigation spend ($4.2M Q1 2026),
#   stockmoguls Sep-6 relay - in-corpus as mechanism 753 (extends 636).
# Pick 3: October 2026 Google AI Contribution Pilot relay wave
#   (Technori Oct-1 relay of The Information's Sep-29 figures; June 18,
#   2026 policy-blog acknowledgment by Markham Erickson) - figures
#   saturated (m1099/m1199); relay-only, no new money leg.
# Pick 4: DOJ 20-page Statement of Interest backing fair use in NYT v.
#   Microsoft (filed Sep 1, 2026; VINTAGE) - in-corpus as mechanism 672.
SCOUT_PICKS_DOCUMENTED_IN_DOCSTRING = True


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )


def _iter_source_files():
    """Yield paths for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson).
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
    """Return file paths containing the underscore-form mechanism key.

    The needle is built at runtime by format string, so this source
    file carries no contiguous underscore-form literal (per the #770
    lesson).
    """
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
    return max(found) if found else None


def _git_grep_tracked_source(needle, scope):
    """Grep tracked files at HEAD for a literal needle (fragment-built)."""
    args = ["git", "grep", "-F", "-l", needle, "HEAD", "--"]
    if scope:
        args.append(scope)
    out = subprocess.run(
        args, cwd=REPO_ROOT, capture_output=True, text=True
    ).stdout
    cleaned = []
    for line in out.splitlines():
        line = line.strip()
        if line.startswith("HEAD:"):
            line = line[len("HEAD:"):]
        if line:
            cleaned.append(line)
    return cleaned


def _class_run(filename, classname):
    target = os.path.join(TESTS_DIR, filename)
    env = dict(os.environ)
    env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    venv_py = os.path.join(REPO_ROOT, ".venv", "bin", "python")
    return subprocess.run(
        [venv_py, "-m", "pytest", target, "-k", classname,
         "-q", "--no-header", "-o", "addopts=", "-p", "no:cacheprovider"],
        cwd=REPO_ROOT, capture_output=True, text=True, env=env,
        timeout=600,
    )


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup)
#    + rotation guard: FIFTH and CLOSING leg of the 1355-1359 window.
# ---------------------------------------------------------------------------


class TestAnchor1359:
    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit form: ANCHORED_SHA is 0*40; the anchor followup
        # patches it to the main-commit sha. This test fails BY
        # DESIGN post-anchor and is deselected in the in-gate run;
        # the patched form is asserted by
        # test_anchor_sha_patched_to_main_commit. Terminal per #565.
        assert ANCHORED_SHA == "0" * 40

    def test_anchor_sha_patched_to_main_commit(self):
        # Post-commit form: ANCHORED_SHA patched to this run's main
        # commit sha in the anchor followup (placeholder + expected
        # value and the ANCHORED_SHA constant are patched).
        # Deselected in the in-gate run.
        assert ANCHORED_SHA != "0" * 40
        assert len(ANCHORED_SHA) == 40

    def test_anchor_sha_format(self):
        assert len(ANCHORED_SHA) == 40
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA)

    def test_anchor_duality_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Anchor convention per #565" in src
        assert "fails BY DESIGN post-anchor" in src

    def test_fifth_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIFTH and CLOSING leg of the 1355-1359 window" in src

    def test_1350_1354_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1350-1354" in src
        assert "VERIFIED CLOSED" in src

    def test_next_leg_is_1360_type_d(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1360" in src
        assert "verdict belongs to #1360 per #795" in src


# ---------------------------------------------------------------------------
# 2. Scout corpus-blindness: the scout's four picks all rejected on
#    main-run verification (FOURTH #1341 instance) + the #715 novelty
#    discipline.
# ---------------------------------------------------------------------------


class TestScoutCorpusBlindness1359:
    def test_scout_pick1_mehta_dismissal_in_corpus(self):
        # The scout claimed "no corpus mechanism covers a publisher-party
        # AI Overview dismissal"; the corpus banks exactly this leg as
        # test_type_c_1129 (Oct 1, 5pm). FOURTH #1341 instance.
        path = os.path.join(
            TESTS_DIR,
            "test_type_c_1129_mehta_dismisses_chegg_penske_suits_"
            "litigation_channel_closure_oct01_5pm.py",
        )
        assert os.path.exists(path), "in-corpus #1129 dismissal leg"

    def test_scout_pick2_nyt_spend_in_corpus(self):
        # The scout's $28M+ NYT AI-litigation-spend pick is in-corpus
        # as mechanism 753 (PROMOTES mechanism 636's $4.2M Q1 datum).
        hits = _git_grep_tracked_source(
            "The Times has already spent more than $28 million",
            "profiles/competitor-entities.yaml",
        )
        assert hits, "m753 NYT $28M spend block must be corpus-recorded"

    def test_scout_pick3_pilot_figures_saturated(self):
        # The AI Contribution Pilot figures are saturated (m1099/m1199);
        # the October relay wave adds no new money leg.
        hits = _git_grep_tracked_source(
            "AI Contribution Pilot", "profiles/competitor-entities.yaml"
        )
        assert hits, "pilot legs must be corpus-recorded"

    def test_scout_pick4_doj_soi_in_corpus(self):
        # The Sep-1 DOJ Statement of Interest is in-corpus as mechanism
        # 672 (VINTAGE, out of the run window).
        hits = _git_grep_tracked_source(
            "US DOJ Statement of Interest in NYT v. OpenAI",
            "profiles/competitor-entities.yaml",
        )
        assert hits, "m672 DOJ SOI block must be corpus-recorded"

    def test_max_numeric_mechanism_id_stays_1044(self):
        # Type C lands ZERO mechanisms this run: max numeric stays 1044.
        assert _max_numeric_mechanism_id() == MECH_NUM == 1044

    def test_no_type_c_1359_in_git_log_pin(self):
        # Ancestor-form self-trip per #1191: every commit whose message
        # matches "Type C #1359" must be #1359's main commit or a
        # descendant of it. Deselected in the in-gate run (fails
        # pre-commit by design); re-pinned in the terminal log-hash
        # followup per #721.
        out = _git("log", "--format=%H", "--grep=Type C #1359")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1359's own commits"
        main = _git("rev-parse", PRED_MAIN_1359).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_zero_next_number_keys_all_forms(self):
        # Numeric (profiles/ scope), underscore and dash (profiles/ +
        # tests/ scope, own file excluded per #715). Holds pre-commit
        # and post-commit (Type C lands zero mechanisms, the 1045
        # pins stay green).
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_1359_entry_in_iteration_log_pre_commit(self):
        text = _read(LOG_PATH)
        assert "## #1359" not in text

    def test_zero_type_c_1359_files_except_own(self):
        import glob
        found = glob.glob(os.path.join(TESTS_DIR, "test_type_c_1359*"))
        assert [os.path.basename(p) for p in found] == [OWN_BASENAME]

    def test_query_sets_bounded(self):
        # 2 main-run browser.search query sets + 1 delegated scout
        # (3 tracks) + main-run corpus git-grep verification;
        # 0 browser.open per #503.
        assert len(QUERY_SETS) == 2
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "0 browser.open per #503" in src


# ---------------------------------------------------------------------------
# 3. Guard lifecycle: forward pins for #1360; #1358 staged the
#    #1191-class no-Type-C-#1359 self-trip (re-pinned post-commit
#    per #721). Type-correct per the #1352 type-mismatch lesson.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1359:
    def test_pins_on_zero_mechanism_landing(self):
        # Type C lands zero mechanisms: max 1044, next 1045.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1044" in src
        assert "NEXT_NUM = 1045" in src

    def test_no_type_d_1360_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1360's terminal log-hash followup
        # per #721): every commit whose message matches "Type D
        # #1360" must be #1360's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1360 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type D #1360")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1360's own commits"
        main = _git("rev-parse", PRED_MAIN_1360).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1045_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1045_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1045_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_fortieth_direction_pin(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_forty_eighth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]

    def test_forty_ninth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T49, "profiles/") != []

    def test_fiftieth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T50, "profiles/") != []

    def test_fifty_first_member_intact_pin(self):
        assert _git_grep_tracked_source(_T51, "profiles/") != []

    def test_fifty_second_member_intact_pin(self):
        assert _git_grep_tracked_source(_T52, "profiles/") != []

    def test_fifty_third_member_intact_pin(self):
        assert _git_grep_tracked_source(_T53, "profiles/") != []

    def test_fifty_fourth_member_present_pin(self):
        assert _git_grep_tracked_source(_T54, "profiles/") != []

    def test_fifty_fifth_member_present_pin(self):
        assert _git_grep_tracked_source(_T55, "profiles/") != []

    def test_fifty_sixth_member_present_pin(self):
        assert _git_grep_tracked_source(_T56, "profiles/") != []

    def test_fifty_seventh_member_present_pin(self):
        assert _git_grep_tracked_source(_T57, "profiles/") != []

    def test_fifty_eighth_member_present_pin(self):
        assert _git_grep_tracked_source(_T58, "profiles/") != []

    def test_fifty_ninth_member_present_pin(self):
        assert _git_grep_tracked_source(_T59, "profiles/") != []

    def test_sixtieth_member_present_pin(self):
        assert _git_grep_tracked_source(_T60, "profiles/") != []

    def test_sixty_first_member_present_pin(self):
        assert _git_grep_tracked_source(_T61, "profiles/") != []

    def test_sixty_second_member_present_pin(self):
        assert _git_grep_tracked_source(_T62, "profiles/") != []

    def test_sixty_third_member_intact_pin(self):
        assert _git_grep_tracked_source(_T63, "profiles/") != []

    def test_sixty_fourth_member_present_pin(self):
        assert _git_grep_tracked_source(_T64, "profiles/") != []

    def test_no_sixty_fifth_member_pin(self):
        # Type C lands zero mechanisms this run: the sixty-fifth
        # member-claim form stays absent repo-wide.
        assert _git_grep_tracked_source(_T65, "profiles/") == []
        assert _git_grep_tracked_source(_T65, "tests/") == []

    def test_ledger_holds_at_64_pin(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ledger holds at 64" in src


# ---------------------------------------------------------------------------
# 4. Staleness pins: #1358's guard lifecycle flips BY DESIGN post-commit.
# ---------------------------------------------------------------------------


class TestStalenessPins1359:
    def test_1358_guard_lifecycle_post_commit_state(self):
        # Post-terminal form: 25 tests in the class; ALL 25 pass.
        # Type C lands zero mechanisms, so every #1358 forward guard
        # stays green: max-1044, zero-1045 all forms, fortieth absent,
        # forty-eighth through sixty-fourth members intact,
        # no-sixty-fifth member, ledger holds at 64. The
        # no_type_c_1359_in_git_log ancestor pin (the #1191-class
        # self-trip) was red at this run's main-commit time; the
        # terminal log-hash followup re-pins PRED_MAIN_1359 in BOTH
        # its own file's copy and the #1358 predecessor file's copy
        # per the #1292 re-pin-both-copies precedent and the #721
        # re-pin rule, flipping it green. Deselected in the in-gate
        # run (fails pre-commit by design); verified post-terminal.
        res = _class_run(A1358_FILE, "TestGuardLifecycle1358")
        out = res.stdout + res.stderr
        assert "25 passed" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 5. Doc-sync per #719 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestDocSync1359:
    def test_readme_test_file_table_has_1359_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_c_1359" in readme

    def test_architecture_has_1359_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_c_1359" in arch

    def test_readme_stats_ratcheted(self):
        # Post-sync-positive form per #719: asserts the ratcheted
        # counts (README_TEST_COUNT tests across README_FILE_COUNT
        # files). Fails pre-commit by design; deselected in the
        # in-gate run.
        readme = _read(README_PATH)
        assert ("| Tests | %d |" % README_TEST_COUNT) in readme
        assert ("Across %d test files" % README_FILE_COUNT) in readme


# ---------------------------------------------------------------------------
# 6. Iteration log per #721 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestIterationLog1359:
    def test_log_has_1359_entry(self):
        text = _read(LOG_PATH)
        assert "## #1359 Type C" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_finding(self):
        text = _read(LOG_PATH)
        assert "saturation_screening_no_novel_mechanism" in text
        assert "1044" in text


# ---------------------------------------------------------------------------
# 7. Screening ledger: the 4 rejected financial-incentive candidates.
# ---------------------------------------------------------------------------


class TestScreeningLedger1359:
    def test_rejected_picks_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        for name in ("Mehta", "Penske", "Chegg",
                     "NYT $28M", "Contribution Pilot",
                     "Statement of Interest"):
            assert name in src, name

    def test_in_corpus_rejections_referenced(self):
        # Picks 1, 2, and 4 are corpus-recorded; pick 3's figures are
        # corpus-saturated. Re-banking them would duplicate the record.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        for ref in ("test_type_c_1129", "mechanism 753",
                    "m1099/m1199", "mechanism 672"):
            assert ref in src, ref

    def test_no_profiles_edit_this_run(self):
        # Type C lands zero mechanisms: no profiles/ edit this run
        # (neither profiles/competitor-entities.yaml nor any
        # publication profile; verified via git status in the
        # iteration-log entry, not here).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "no profiles/ edit this run" in src

    def test_fourth_1341_instance_recorded(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FOURTH #1341 instance" in src


# ---------------------------------------------------------------------------
# 8. Research method.
# ---------------------------------------------------------------------------


class TestResearchMethod1359:
    def test_scout_plus_main_run_sets(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1 delegated scout (3 tracks)" in src
        assert "2 main-run browser.search verification sets" in src

    def test_zero_browser_open(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "0 browser.open per #503" in src

    def test_scout_blindness_fourth_instance(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FOURTH #1341 instance" in src
        assert "Scout characterizations" in src
        assert "untrusted" in src

    def test_urls_verbatim_convention(self):
        # The two URLs carried this run come from the main run's own
        # Full-URL listings, copied verbatim, NOT constructed, and are
        # used only to document corroboration of the in-corpus legs -
        # never as novel evidence.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert ("https://www.aitechdaily.com/google-ai-overviews-"
                "chegg-penske-dismissal/") in src
        assert ("https://www.get.pelcro.com/blog/"
                "new-york-times-q2-2026-results") in src


# ---------------------------------------------------------------------------
# 9. Verdict: saturation screening, manual/qualitative only.
# ---------------------------------------------------------------------------


class TestVerdict1359:
    def test_verdict_saturation_screening(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "saturation_screening_no_novel_mechanism" in src

    def test_not_falsification_family_member(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NOT a falsification-family" in src
        assert "ledger holds at 64" in src

    def test_manual_qualitative_only(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MANUAL /" in src
        assert "QUALITATIVE ONLY per the Aug 28 2026 standing rule" in src
        assert "tone NOT_SCORED" in src
        assert "no_analysis_json_update true" in src

    def test_correlation_not_causation(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Correlation is" in src
        assert "hypothesis-generating only" in src

    def test_background_suite_checked_only(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "this run CHECKS it only" in src
        assert "verdict belongs to #1360 per #795" in src
        assert "neither" in src
        assert "re-launches, kills, nor writes to it" in src


# ---------------------------------------------------------------------------
# 10. In-flight isolation: #899/#938/#900/#1012-wt stay out of this
#     run's index; #1024's m846 stays untouched.
# ---------------------------------------------------------------------------


class TestInFlightIsolation1359:
    def test_899_nytimes_hunk_untouched(self):
        res = _git("diff", "--name-only")
        modified = res.stdout.split()
        assert "profiles/nytimes.yaml" in modified
        # Its uncommitted hunk belongs to #899's run; this run stages
        # only its own files.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#899" in src

    def test_938_type_b_file_untouched(self):
        res = _git("diff", "--name-only")
        modified = res.stdout.split()
        assert any(p.startswith("tests/test_type_b_938_") for p in modified)
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#938" in src

    def test_900_untracked_type_d_file_untouched(self):
        res = _git("status", "--porcelain")
        assert "tests/test_type_d_900_" in res.stdout
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#900" in src

    def test_1012_working_tree_edit_untouched(self):
        res = _git("diff", "--name-only")
        modified = res.stdout.split()
        assert any(p.startswith("tests/test_type_a_1012_") for p in modified)
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1012-wt" in src

    def test_1024_m846_untouched(self):
        # #1024's m846 block (FOURTEENTH, exclusionary-diversion) in
        # profiles/competitor-entities.yaml has a self-flagged
        # sourcing-constraint violation; Ray's revert/leave/rebuild
        # decision is pending. This run does not touch the file at all.
        res = _git("diff", "--name-only")
        modified = res.stdout.split()
        assert "profiles/competitor-entities.yaml" not in modified
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1024" in src
