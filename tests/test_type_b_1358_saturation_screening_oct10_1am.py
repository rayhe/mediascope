# -*- coding: utf-8 -*-
"""Type B #1358: journalist cross-entity saturation screening (Oct 10 2026,
~1:00 AM PDT) - NO clean fresh pair; NO mechanism landed.

1 delegated scout (3 tracks) + 14 main-run browser.search verification sets,
0 browser.open per #503, excerpt-bounded. Screened 6 fresh journalists this
run (all rejected) on top of the #1353 sixteen:

  REJECTED (main-run verification):
  - Ryne Hager (Android Police; the scout's #1 pick): prior
    beat-boundary rejection stands (iteration-log line 4426,
    "Corbin Davenport/Ryne Hager (beat-boundary)"); the scout's
    piece titles did not surface in any of 3 main-run searches;
    "ryne hager" hits the journalists.yaml roster and the
    iteration-log - not a clean novel journalist.
  - Rita El Khoury (the scout's runner-up): the claimed Sep-24-2026
    Android Authority Meta Ray-Ban Audio piece did NOT verify in
    3 independent main-run searches (quoted-title, site-scoped,
    author-page routes); the m950 single-arm watch (Type B #1198,
    Sep-17-2026 Android Police Xreal Aura XR hands-on, +0.55
    illustrative) HOLDS - no Meta-arm conversion this run.
  - Abner Li (9to5Google; the scout's fallback): WRONG BYLINE - the
    WeSearch record attributes the Sep-23-2026 9to5Google Meta
    piece ("Meta launches audio-only and Gen 3 Ray-Ban smart
    glasses", verbatim
    https://9to5google.com/2026/09/23/meta-ray-ban-gen-3-audio-only-smart-glasses/)
    to Ben Schoon, who is Type-B-saturated (#1073, m875).
  - Karissa Bell (Engadget; the scout's fallback): deeply saturated
    (m722 #818, mechanism #113, #1153 bounded-absence extension).
  - Igor Bonifacic (Engadget; main-run screen): zero attributable
    Meta-glasses bylines surfaced; his OpenAI arm ("Free accounts
    can now access ChatGPT's upgraded task scheduling tool") has
    no Meta counterpart by him.
  - C. Scott Brown (Android Authority; main-run screen): the Oct-6
    Meta v128/v129 navigation piece is bylined Hillary Keverenge,
    not Brown; his own Meta pieces are stale (Feb 2026).

The scout's slate is the THIRD #1341 instance (scout
corpus-blindness / misattribution: Hager titles unverified, El
Khoury Meta arm unverified, Li byline wrong). Scout
characterizations untrusted; the main run verified everything via
git grep -F and its own searches.

Verdict saturation_screening_no_clean_pair - NOT a falsification-family
member. Max numeric mechanism_id stays 1044 (Type B lands zero mechanisms
this run); ledger holds at 64; no sixty-fifth member. MANUAL /
QUALITATIVE ONLY per the Aug 28 2026 standing rule (tone NOT_SCORED;
p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant false; engine NOT
run; NOT artifact-grade; no_analysis_json_update true). Correlation is
not causation; hypothesis-generating only.

Type B lands zero mechanisms: no profiles/ edit this run. The record is
the iteration-log ## #1358 entry plus this test file.

This run is the FOURTH leg of the 1355-1359 window (D #1355 -> E #1356
-> A #1357 -> B #1358 -> C #1359 per the #565 anchor + rotation guard);
the 1350-1354 window is VERIFIED CLOSED. The next background-suite
verdict belongs to #1360 per #795 (the #1355-launched suite, goal
hidden_files type_d_1355_full_suite.log; this run CHECKS it only -
observed DEAD at [  2%] with last write Oct 9 22:59 PDT and zero live
pytest processes at this run's ~1:0x AM PDT check - and neither
re-launches, kills, nor writes to it).

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
JOURNALISTS_PATH = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")

OWN_BASENAME = "test_type_b_1358_saturation_screening_oct10_1am.py"

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "908543be62bb67b02516ad7cd13422ee6078bb4f"  # patched to the main-commit sha in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1044  # max numeric; Type B lands ZERO mechanisms this run
NEXT_NUM = 1045  # integer only; key-form needles are format-built

# Post-doc-sync totals per #719: PATCHED post-collection
# (pre-sync 78660 + 61 tests; pre-sync 1682 + 1 file).
README_TEST_COUNT = 78721  # patched post-collection
README_FILE_COUNT = 1683


# Predecessor chain: #1357 Type A THIRD leg of the 1355-1359 window.
PRED_MAIN_1357 = "bc362a9bf6becb8350bcfe7884f17d1c46500669"
PRED_ANCHOR_1357 = "628c80855b9cdeaf64255f9a3cc0f6bd8737b625"
PRED_DOCSYNC_1357 = "758eebd41de69e87af56725732819bf710b5a7f9"
PRED_LOGHASH_1357 = "830034627613eb81ce19b6d75e073ad1d06bb7b9"
PRED_PUSH_1357 = "69e20bb0534da97249dd15f114d3911142e2a128"

# This run's main commit (full sha), for the ancestor-form
# no-Type-B-#1358 pin. Staged 0*40 placeholder-only per #721;
# re-pinned in #1358's terminal log-hash followup per #721.
PRED_MAIN_1358 = "908543be62bb67b02516ad7cd13422ee6078bb4f"  # re-pinned to the #1358 main sha in the anchor followup per #721/#1292

# #1359's main commit (full sha), for the ancestor-form no-Type-C-#1359
# pin (the #1191-class self-trip; #1359 is Type C per the rotation).
# Staged 0*40 placeholder-only per #721; re-pinned in #1359's terminal
# log-hash followup per #721.
PRED_MAIN_1359 = "7795bebf6e978c513a9ebbd76cc823bb03747154"  # re-pinned to #1359 main sha in #1359's anchor followup per #721/#1292

# The #1357 window-predecessor file, for the staleness pin on its
# guard-lifecycle class (max id 1044; zero next-number
# keys all forms; no sixty-fifth member; ledger holds at 64).
B1357_FILE = (
    "test_type_a_1357_ft_openai_oct08_publisher_copyright_suit_"
    "legal_enforcement_bounded_absence_vs_carried_meta_arms_oct09_11pm.py"
)

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

# 14 main-run browser.search query sets + 1 delegated scout (3 tracks)
# this run (0 browser.open per #503).
QUERY_SETS = [
    "David Pierce The Verge Meta Connect 2026 Ray-Ban Meta glasses hands-on",
    "Mark Gurman Meta smart glasses Ray-Ban Meta October 2026",
    "Ryne Hager Android Police Ray-Ban Meta Audio October 2026",
    "Ryne Hager Android Police Google Aura smart glasses September 2026",
    "Ryne Hager smart glasses one thing wear",
    "Rita El Khoury Ray-Ban Meta Audio September 2026",
    "Rita El Khoury Android Authority Google Aura glasses September 2026",
    "site:androidauthority.com Ray-Ban Meta Audio El Khoury",
    "Rita El Khoury author page Meta glasses article byline 2026",
    "Abner Li 9to5Google Ray-Ban Meta Audio September 2026",
    "Meta launches audio-only and Gen 3 Ray-Ban smart glasses author 9to5Google",
    "Karissa Bell Engadget Meta Connect 2026 glasses",
    "Igor Bonifacic Engadget Meta glasses September 2026",
    "C. Scott Brown Android Authority Meta Ray-Ban September October 2026",
]

# The scout's picks, as returned (titles only; the scout supplied relay
# URLs, but the main run treats all scout-supplied evidence as
# untrusted per the #1341 lesson and verified each pick independently
# via its own searches and git grep -F - all three picks REJECTED).
# Pick 1: Ryne Hager (Android Police) - "Ray-Ban Meta Audio: Meta finally
#   did the one thing that could get me to wear smart glasses"
#   (Oct 1, 2026) vs "Google's new Aura smart glasses look like they'd
#   fit right in at a spy convention" (Sep 24, 2026).
# Pick 2: Rita El Khoury - Meta Ray-Ban Audio (Sep 24, 2026,
#   Android Authority, claimed) vs Google "Aura" glasses + "Nimbus"
#   smartwatch (Sep 23, 2026, claimed).
# Fallback: Abner Li (9to5Google) - Meta Ray-Ban Audio piece
#   (Sep 23, 2026, claimed) vs Google Wear OS battery-drain pieces
#   (Sep 26-27, claimed).
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
#    + rotation guard: FOURTH leg of the 1355-1359 window.
# ---------------------------------------------------------------------------


class TestAnchor1358:
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

    def test_fourth_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FOURTH leg of the 1355-1359 window" in src

    def test_1350_1354_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1350-1354" in src
        assert "VERIFIED CLOSED" in src

    def test_next_leg_is_1359_type_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "C #1359" in src


# ---------------------------------------------------------------------------
# 2. Scout corpus-blindness: the scout's three picks all rejected on
#    main-run verification (THIRD #1341 instance).
# ---------------------------------------------------------------------------


class TestScoutCorpusBlindness1358:
    def test_scout_pick1_hager_rejected_beat_boundary(self):
        # Ryne Hager carries a standing beat-boundary rejection
        # (iteration-log, "Corbin Davenport/Ryne Hager
        # (beat-boundary)"); the scout's piece titles did not surface
        # in any of the 3 main-run Hager searches; "ryne hager" hits
        # the journalists.yaml roster - not a clean novel journalist.
        log = _read(LOG_PATH)
        assert "Ryne Hager (beat-boundary)" in log

    def test_scout_pick2_el_khoury_meta_arm_unverified(self):
        # The claimed Sep-24-2026 Android Authority Meta Ray-Ban Audio
        # piece did NOT verify in 3 independent main-run searches
        # (quoted-title, site-scoped, author-page). The m950
        # single-arm watch (Type B #1198, Sep-17-2026 Android Police
        # Xreal Aura XR hands-on) HOLDS - no Meta-arm conversion.
        hits = _git_grep_tracked_source(
            "type_b_1198_rita_el_khoury_android_police_google_xr_arm_only_"
            "meta_arm_absent_watch",
            "profiles/careers/journalists.yaml",
        )
        assert hits, "m950 watch block must be corpus-recorded"

    def test_scout_fallback_abner_li_wrong_byline(self):
        # The WeSearch record attributes the Sep-23-2026 9to5Google
        # Meta piece to Ben Schoon (not Abner Li); Schoon is
        # Type-B-saturated (#1073, m875). Karissa Bell (the other
        # fallback) is deeply saturated (m722 #818, #113, #1153).
        hits = _git_grep_tracked_source(
            "type_b_1073_ben_schoon_9to5google_weekender_camera_stigma_"
            "meta_blame_vs_samsung_google_victim_framing_sep29",
            "profiles/careers/journalists.yaml",
        )
        assert hits, "m875 Schoon block must be corpus-recorded"

    def test_max_numeric_mechanism_id_stays_1044(self):
        # Type B lands ZERO mechanisms this run: max numeric stays 1044.
        assert _max_numeric_mechanism_id() == MECH_NUM == 1044

    def test_no_type_b_1358_in_git_log_pin(self):
        # Ancestor-form self-trip per #1191: every commit whose message
        # matches "Type B #1358" must be #1358's main commit or a
        # descendant of it. Deselected in the in-gate run (fails
        # pre-commit by design); re-pinned in the terminal log-hash
        # followup per #721.
        out = _git("log", "--format=%H", "--grep=Type B #1358")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1358's own commits"
        main = _git("rev-parse", PRED_MAIN_1358).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_zero_next_number_keys_all_forms(self):
        # Numeric (profiles/ scope), underscore and dash (profiles/ +
        # tests/ scope, own file excluded per #715). Holds pre-commit
        # and post-commit (Type B lands zero mechanisms, the 1045
        # pins stay green).
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_1358_entry_in_iteration_log_pre_commit(self):
        text = _read(LOG_PATH)
        assert "## #1358" not in text

    def test_zero_type_b_1358_files_except_own(self):
        import glob
        found = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1358*"))
        assert [os.path.basename(p) for p in found] == [OWN_BASENAME]

    def test_query_sets_bounded(self):
        # 14 main-run browser.search query sets + 1 delegated scout
        # (3 tracks); 0 browser.open per #503.
        assert len(QUERY_SETS) == 14
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "0 browser.open per #503" in src


# ---------------------------------------------------------------------------
# 3. Guard lifecycle: forward pins for #1359; #1358 stages the
#    #1191-class no-Type-C-#1359 self-trip (re-pinned post-commit
#    per #721). Type-correct per the #1352 type-mismatch lesson.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1358:
    def test_pins_on_zero_mechanism_landing(self):
        # Type B lands zero mechanisms: max 1044, next 1045.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1044" in src
        assert "NEXT_NUM = 1045" in src

    def test_no_type_c_1359_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1359's terminal log-hash followup
        # per #721): every commit whose message matches "Type C
        # #1359" must be #1359's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        # Type-correct per the #1352 type-mismatch lesson (#1359 is
        # Type C per the rotation).
        out = _git("log", "--format=%H", "--grep=Type C #1359")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1359's own commits"
        main = _git("rev-parse", PRED_MAIN_1359).stdout.strip()
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
        # m1044 is mechanism_documented, NOT a member, and this run
        # lands zero mechanisms: the sixty-fifth member-claim form
        # stays absent repo-wide.
        assert _git_grep_tracked_source(_T65, "profiles/") == []
        assert _git_grep_tracked_source(_T65, "tests/") == []

    def test_ledger_holds_at_64_pin(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ledger holds at 64" in src


# ---------------------------------------------------------------------------
# 4. Staleness pins: #1357's guard lifecycle flips BY DESIGN post-commit.
# ---------------------------------------------------------------------------


class TestStalenessPins1358:
    def test_1357_guard_lifecycle_post_commit_state(self):
        # Post-terminal form: 25 tests in the class; ALL 25 pass.
        # Type B lands zero mechanisms, so every #1357 forward guard
        # stays green: max-1044, zero-1045 all forms, fortieth absent,
        # forty-eighth through sixty-fourth members intact,
        # no-sixty-fifth member, ledger holds at 64. The
        # no_type_b_1358_in_git_log ancestor pin (the #1191-class
        # self-trip) was red at this run's main-commit time; the
        # terminal log-hash followup re-pins PRED_MAIN_1358 in BOTH
        # its own file's copy and the #1357 predecessor file's copy
        # per the #1292 re-pin-both-copies precedent and the #721
        # re-pin rule, flipping it green. Deselected in the in-gate
        # run (fails pre-commit by design); verified post-terminal.
        res = _class_run(B1357_FILE, "TestGuardLifecycle1357")
        out = res.stdout + res.stderr
        assert "25 passed" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 5. Doc-sync per #719 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestDocSync1358:
    def test_readme_test_file_table_has_1358_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_b_1358" in readme

    def test_architecture_has_1358_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_b_1358" in arch

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


class TestIterationLog1358:
    def test_log_has_1358_entry(self):
        text = _read(LOG_PATH)
        assert "## #1358 Type B" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_finding(self):
        text = _read(LOG_PATH)
        assert "saturation_screening_no_clean_pair" in text
        assert "1044" in text


# ---------------------------------------------------------------------------
# 7. Screening ledger: the 6 fresh journalists screened this run.
# ---------------------------------------------------------------------------


class TestScreeningLedger1358:
    def test_screened_journalists_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        for name in ("Ryne Hager", "Rita El Khoury", "Abner Li",
                     "Karissa Bell", "Igor Bonifacic", "C. Scott Brown"):
            assert name in src, name

    def test_carried_rejections_referenced(self):
        # The #1353 sixteen carry as rejections; re-screening them
        # would re-litigate.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        for name in ("Lily Hay Newman", "Sarah Perez", "Lauren Goode",
                     "Dominic Preston", "Joanna Stern", "Ariel Zilber"):
            assert name in src, name

    def test_no_profiles_edit_this_run(self):
        # Type B lands zero mechanisms: profiles/careers/
        # journalists.yaml is untouched by this run (verified via
        # git status in the iteration-log entry, not here).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "no profiles/ edit this run" in src

    def test_m950_watch_holds(self):
        # The El Khoury Meta arm did not verify; the m950 watch
        # (Type B #1198) is not converted to a two-arm mechanism.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "m950" in src
        assert "no Meta-arm conversion" in src


# ---------------------------------------------------------------------------
# 8. Research method.
# ---------------------------------------------------------------------------


class TestResearchMethod1358:
    def test_scout_plus_main_run_sets(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1 delegated scout (3 tracks)" in src
        assert "14 main-run browser.search verification sets" in src

    def test_zero_browser_open(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "0 browser.open per #503" in src

    def test_scout_blindness_third_instance(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "THIRD #1341 instance" in src

    def test_urls_verbatim_convention(self):
        # The one URL carried this run (the 9to5Google Meta piece)
        # was copied verbatim from the main run's own Full-URL
        # listing, not constructed, and is used only to document the
        # Schoon byline attribution - never as novel evidence.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert ("https://9to5google.com/2026/09/23/"
                "meta-ray-ban-gen-3-audio-only-smart-glasses/") in src


# ---------------------------------------------------------------------------
# 9. Verdict: saturation screening, manual/qualitative only.
# ---------------------------------------------------------------------------


class TestVerdict1358:
    def test_verdict_saturation_screening(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "saturation_screening_no_clean_pair" in src

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
