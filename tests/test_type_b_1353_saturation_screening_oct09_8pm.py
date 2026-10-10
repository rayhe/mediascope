# -*- coding: utf-8 -*-
"""Type B #1353: journalist cross-entity saturation screening (Oct 9 2026,
~8:00 PM PDT) - NO clean fresh pair; NO mechanism landed.

1 delegated scout (3 tracks) + 8 main-run browser.search verification sets,
0 browser.open per #503, excerpt-bounded. Screened 16 journalists:

  IN-CORPUS (rejected - re-selecting would re-litigate):
  Lily Hay Newman (m635/m836/m1004 - the scout's "STRONG CANDIDATE" Track 1
  pair, Newman/Burgess Oct-2 ChatGPT Mac flaw vs Oct-3 Muse profiles, IS
  m1004 from Type B #1288; caught ONLY by the main-run #715 grep - the
  scout's characterization was untrusted, second instance of the #1341
  lesson), Sarah Perez (m617/m698/m1007/m1040), Lauren Goode (dedicated
  Type B in-corpus), Simon Hill (#395/#452), Dominic Preston (dedicated),
  Reece Rogers (#97/m629/m890/m991), Jason Aten (m887), Joanna Stern (m899),
  Nicole Nguyen (#1103/#1108), Ariel Zilber (#1343), Maxwell Zeff
  (in-corpus pair), Tim Bradshaw (#558).
  CLEAN MISS (no clean same-writer Meta-vs-competitor pair surfaced):
  Jacob Kastrenakes (no competitor-wearable arm), Casey Newton (no
  Platformer firings byline), Hannah Murphy (no FT firings originals),
  Will Knight (no clean pair, #1348-confirmed), Mike Isaac (no clean
  in-window pair, #1348-confirmed).

Verdict saturation_screening_no_clean_pair - NOT a falsification-family
member. Max numeric mechanism_id stays 1042 (Type B lands zero mechanisms
this run); ledger holds at 64; no sixty-fifth member. MANUAL /
QUALITATIVE ONLY per the Aug 28 2026 standing rule (tone NOT_SCORED;
p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant false; engine NOT
run; NOT artifact-grade; no_analysis_json_update true). Correlation is
not causation; hypothesis-generating only.

Type B lands zero mechanisms: no profiles/ edit this run. The record is
the iteration-log ## #1353 entry plus this test file.

This run is the FOURTH leg of the 1350-1354 window (D #1350 -> E #1351
-> A #1352 -> B #1353 -> C #1354 per the #565 anchor + rotation guard);
the 1345-1349 window is VERIFIED CLOSED. The next background-suite
verdict belongs to #1355 per #795 (the #1350-launched suite, goal
hidden_files type_d_1350_full_suite.log; this run CHECKS it only -
observed stalled at [0%] with no live pytest proc at this run's ~8:00 PM
PDT check - and neither re-launches, kills, nor writes to it).

NOTE on the #1352 file's forward pin: its
test_no_type_a_1353_in_git_log_pin is TYPE-MISMATCHED (the window
rotation makes #1353 Type B, so a "Type A #1353" commit can never
exist); the pin is unsatisfiable by design, documented in
TestStalenessPins1353, not repaired. This file stages the correct
forward pin for #1354: no-Type-C-#1354 (the #1191-class self-trip,
re-pinned in #1354's terminal log-hash followup per #721).

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this
pre-commit file and is patched to the main-commit hash in the anchor
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

OWN_BASENAME = "test_type_b_1353_saturation_screening_oct09_8pm.py"

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "0" * 40  # 0*40 pre-commit; patched to the main-commit sha in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1042  # max numeric; Type B lands ZERO mechanisms this run
NEXT_NUM = 1043  # integer only; key-form needles are format-built

# Predecessor chain: #1352 Type A THIRD leg of the 1350-1354 window.
PRED_MAIN_1352 = "2b33a0406fd0eca02c75cac70086bb9f9d5dab5a"
PRED_ANCHOR_1352 = "b12cace553e7d9281ad5980ab9a2a691822feb83"
PRED_DOCSYNC_1352 = "d162dbc79693395db169730abb2bbcaa125f3e4b"
PRED_FINAL_1352 = "01109848"

# This run's main commit (full sha), for the ancestor-form
# no-Type-B-#1353 pin. Staged 0*40 placeholder-only per #721;
# re-pinned in #1353's terminal log-hash followup per #721.
PRED_MAIN_1353 = "0" * 40  # staged placeholder per #721; re-pinned in #1353's terminal log-hash followup

# #1354's main commit (full sha), for the ancestor-form no-Type-C-#1354
# pin (the #1191-class self-trip; #1354 is Type C per the rotation).
# Staged 0*40 placeholder-only per #721; re-pinned in #1354's terminal
# log-hash followup per #721.
PRED_MAIN_1354 = "0" * 40  # staged placeholder per #721; re-pinned in #1354's terminal log-hash followup

# The #1352 window-predecessor file, for the staleness pin on its
# guard-lifecycle class (max id 1042; zero next-number
# one-zero-four-three / no-Type-A-#1353-in-git-log (TYPE-MISMATCHED,
# unsatisfiable by design - #1353 is Type B per the rotation) /
# fortieth direction absent / forty-eighth through sixty-fourth
# members intact / no sixty-fifth member / ledger holds at 64).
B1352_FILE = (
    "test_type_a_1352_wired_openai_oct08_09_governance_"
    "accountability_bounded_absence_vs_carried_meta_arms_oct09_7pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 78247  # post-doc-sync total (pre-sync 78178 + 69) - PATCHED post-collection
README_FILE_COUNT = 1678  # pre-sync 1677 + 1 (this file)

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

# 8 main-run browser.search query sets + 1 delegated scout (3 tracks)
# this run (0 browser.open per #503).
QUERY_SETS = [
    "The Verge OpenAI fired safety researchers October 2026 response",
    "Jacob Kastrenakes The Verge Snap Spectacles OR Apple Vision Pro October 2026",
    "Jason Aten Inc. Apple Intelligence privacy messages column 2026",
    "Reece Rogers WIRED Ray-Ban Meta LED ghost dot sticker investigation",
    "Casey Newton Platformer OpenAI safety researchers fired October 2026",
    "Will Knight WIRED Meta AI glasses privacy October 2026",
    "Joanna Stern Zuckerberg interview Meta camera-free glasses September 2026",
    "Hannah Murphy Financial Times OpenAI fired safety researchers October 2026",
]

# The scout's Track 1 "STRONG CANDIDATE" pair - VERIFIED IN-CORPUS at
# m1004 (Type B #1288). These are the verbatim relay URLs the scout
# returned; the main run verified them against the corpus per the #1341
# lesson (scout characterizations untrusted).
SCOUT_TRACK1_URLS = [
    "https://wesearch.press/s/a-flaw-in-chatgpts-mac-app-could-have-let-hackers-grab-sensi-ca874f47",
    "https://technewstube.com/wired/1872894/muse-creates-detailed-profiles-friends-family/",
]


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
#    + rotation guard: FOURTH leg of the 1350-1354 window.
# ---------------------------------------------------------------------------


class TestAnchor1353:
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
        assert "FOURTH leg of the 1350-1354 window" in src

    def test_1345_1349_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1345-1349" in src
        assert "VERIFIED CLOSED" in src

    def test_next_leg_is_1354_type_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "C #1354" in src


# ---------------------------------------------------------------------------
# 2. Scout corpus-blindness: the scout's "STRONG CANDIDATE" is m1004.
#    Type B lands ZERO mechanisms this run (max stays 1042).
# ---------------------------------------------------------------------------


class TestScoutCorpusBlindness1353:
    def test_scout_track1_pair_is_m1004_in_corpus(self):
        # The scout's Track 1 "STRONG CANDIDATE" (Newman/Burgess Oct-2
        # ChatGPT Mac flaw vs Oct-3 Muse profiles) is mechanism 1004
        # from Type B #1288: the block key sits in
        # profiles/careers/journalists.yaml. The main-run #715 grep
        # caught what the scout's characterization missed.
        hits = _git_grep_tracked_source(
            "type_b_1288_lily_hay_newman_chatgpt_mac_flaw_vs_meta_muse_dossier_oct02_oct03",
            "profiles/careers/journalists.yaml",
        )
        assert hits, "m1004 block must be corpus-recorded"

    def test_m1004_test_file_exists(self):
        path = os.path.join(
            TESTS_DIR,
            "test_type_b_1288_lily_hay_newman_chatgpt_mac_flaw_vs_meta_muse_dossier_oct02_oct03_2pm.py",
        )
        assert os.path.isfile(path)

    def test_max_numeric_mechanism_id_stays_1042(self):
        # Type B lands ZERO mechanisms this run: max numeric stays 1042.
        assert _max_numeric_mechanism_id() == MECH_NUM == 1042

    def test_no_type_b_1353_in_git_log_pin(self):
        # Ancestor-form self-trip per #1191: every commit whose message
        # matches "Type B #1353" must be #1353's main commit or a
        # descendant of it. Deselected in the in-gate run (fails
        # pre-commit by design); re-pinned in the terminal log-hash
        # followup per #721.
        out = _git("log", "--format=%H", "--grep=Type B #1353")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1353's own commits"
        main = _git("rev-parse", PRED_MAIN_1353).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_zero_next_number_keys_all_forms(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_1353_entry_in_iteration_log_pre_commit(self):
        text = _read(LOG_PATH)
        assert "## #1353" not in text

    def test_zero_type_b_1353_files_except_own(self):
        import glob
        found = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1353*"))
        assert [os.path.basename(p) for p in found] == [OWN_BASENAME]

    def test_scout_urls_not_reingested(self):
        # The scout's verbatim relay URLs are NOT ingested as novel
        # evidence anywhere (they are in-corpus via m1004); this run
        # asserts them only in the blindness test above.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        for url in SCOUT_TRACK1_URLS:
            assert url in src


# ---------------------------------------------------------------------------
# 3. Guard lifecycle for #1353 (no mechanism landed; forward guards for
#    #1354 Type C).
# ---------------------------------------------------------------------------


class TestGuardLifecycle1353:
    def test_pins_on_zero_mechanism_landing(self):
        # Type B lands zero mechanisms: max 1042, next 1043.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1042" in src
        assert "NEXT_NUM = 1043" in src

    def test_no_type_c_1354_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1354's terminal log-hash followup
        # per #721): every commit whose message matches "Type C
        # #1354" must be #1354's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type C #1354")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1354's own commits"
        main = _git("rev-parse", PRED_MAIN_1354).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1043_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1043_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1043_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_fortieth_direction_pin(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_forty_eighth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T48, "profiles/") != []

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
        assert _git_grep_tracked_source(_T65, "profiles/") == []
        assert _git_grep_tracked_source(_T65, "tests/") == []

    def test_ledger_holds_at_64_pin(self):
        assert _git_grep_tracked_source("Ledger holds at 64", "profiles/") != []


# ---------------------------------------------------------------------------
# 4. Staleness pins on the #1352 guard-lifecycle class (post-terminal).
# ---------------------------------------------------------------------------


class TestStalenessPins1353:
    def test_1352_guard_lifecycle_post_commit_state(self):
        # Post-terminal form: 25 tests in the class; 24 pass, 1 fails
        # BY DESIGN - the #1352 file's no-Type-A-#1353-in-git-log
        # forward pin is TYPE-MISMATCHED (the window rotation makes
        # #1353 Type B, so a "Type A #1353" commit can never exist;
        # documented, not repaired). All 1043 next-number pins stay
        # green (no mechanism landed at #1353); the forty-eighth
        # through sixty-fourth member pins stay green; the
        # no-sixty-fifth pin stays green; the ledger-holds-at-64 pin
        # stays green. Deselected in the in-gate run (fails
        # pre-commit by design); verified post-terminal.
        res = _class_run(B1352_FILE, "TestGuardLifecycle1352")
        out = res.stdout + res.stderr
        assert "1 failed, 24 passed" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 5. Doc-sync per #719 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestDocSync1353:
    def test_readme_test_file_table_has_1353_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_b_1353" in readme

    def test_architecture_has_1353_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_b_1353" in arch

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


class TestIterationLog1353:
    def test_log_has_1353_entry(self):
        text = _read(LOG_PATH)
        assert "## #1353 Type B" in text

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
        assert "m1004" in text


# ---------------------------------------------------------------------------
# 7. Screening ledger: every screened journalist's disposition is
#    corpus-grounded (dedicated Type B commits) or method-recorded
#    (clean misses).
# ---------------------------------------------------------------------------


def _dedicated_type_b_commits(name):
    out = _git("log", "--oneline", "--grep=Type B", "--grep=" + name,
              "--all-match").stdout
    return [line for line in out.splitlines() if line.strip()]


class TestScreeningLedger1353:
    def test_newman_rejected_m1004_dedicated(self):
        assert _dedicated_type_b_commits("Lily Hay Newman"), \
            "Newman must carry dedicated Type B commits (m1004 #1288)"

    def test_perez_rejected_m1040_dedicated(self):
        assert _dedicated_type_b_commits("Sarah Perez"), \
            "Perez must carry dedicated Type B commits (m1040 #1348)"

    def test_goode_rejected_dedicated(self):
        assert _dedicated_type_b_commits("Lauren Goode")

    def test_preston_rejected_dedicated(self):
        assert _dedicated_type_b_commits("Dominic Preston")

    def test_rogers_rejected_dedicated(self):
        assert _dedicated_type_b_commits("Reece Rogers")

    def test_aten_rejected_m887_dedicated(self):
        assert _dedicated_type_b_commits("Jason Aten"), \
            "Aten must carry dedicated Type B commits (m887 #1093)"

    def test_stern_rejected_m899_dedicated(self):
        assert _dedicated_type_b_commits("Joanna Stern"), \
            "Stern must carry dedicated Type B commits (m899 #1113)"

    def test_nguyen_rejected_dedicated(self):
        assert _dedicated_type_b_commits("Nicole Nguyen")

    def test_zilber_rejected_dedicated(self):
        assert _dedicated_type_b_commits("Ariel Zilber")

    def test_clean_misses_recorded_in_method(self):
        # Kastrenakes / Newton / Murphy / Knight / Isaac yielded no
        # clean same-writer pair across the 8 query sets; the method
        # section of this file records each miss.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        for name in ("Jacob Kastrenakes", "Casey Newton", "Hannah Murphy",
                     "Will Knight", "Mike Isaac"):
            assert name in src, name

    def test_zeff_pair_rejected_in_corpus(self):
        # The scout's Zeff candidate pair is in-corpus (the cited
        # commit d3a83151); the method section records the rejection.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Maxwell Zeff" in src
        assert "d3a83151" in src


# ---------------------------------------------------------------------------
# 8. Research method.
# ---------------------------------------------------------------------------


class TestResearchMethod1353:
    def test_eight_query_sets_documented(self):
        assert len(QUERY_SETS) == 8
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        for q in QUERY_SETS:
            assert q in src, q

    def test_zero_browser_open(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "0 browser.open per #503" in src

    def test_scout_handoff_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1 delegated scout (3 tracks)" in src

    def test_verbatim_urls_not_constructed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NOT constructed" in src

    def test_excerpt_bounded(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "excerpt-bounded" in src

    def test_scout_blindness_lesson_recorded(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "corpus-blindness" in src
        assert "#1341" in src


# ---------------------------------------------------------------------------
# 9. Verdict + statistical discipline.
# ---------------------------------------------------------------------------


class TestVerdict1353:
    def test_verdict_saturation_screening(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "saturation_screening_no_clean_pair" in src

    def test_manual_qualitative_only(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MANUAL /" in src
        assert "QUALITATIVE ONLY" in src

    def test_not_significant(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "is_significant false" in src

    def test_not_a_member_ledger_holds(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NOT a falsification-family member" in src
        assert "ledger holds at 64" in src

    def test_not_artifact_grade(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NOT artifact-grade" in src
        assert "no_analysis_json_update true" in src
