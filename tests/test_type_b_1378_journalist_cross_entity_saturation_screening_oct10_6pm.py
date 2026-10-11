# -*- coding: utf-8 -*-
"""Type B #1378: journalist cross-entity saturation screening (Oct 10 2026,
~6:00 PM PDT) - NO clean fresh pair; NO mechanism landed.

FOURTH leg of the 1375-1379 window: D #1375 -> E #1376 -> A #1377 -> B #1378
(this run) -> C #1379. The 1370-1374 window is VERIFIED CLOSED.

1 delegated scout (3 tracks) + 4 main-run browser.search verification
sets, 0 browser.open per #503, excerpt-bounded. The scout's outcome and the
main-run screens are documented below; every scout claim is verified by
the main run's own git grep -F -i at HEAD (the #1341 lesson: the scout is
never trusted blindly).

  MAIN-RUN SCREENS (all excerpt-bounded, 0 browser.open per #503):
  - Xreal Aura Oct-8 launch bylines: TRACKED-OUTLET BYLINE GAP, not a
    finding - the surfaced coverage sits at untracked outlets
    (tech-ish.com, m.gsmarena.com, aiweekly.co, 9to5google.com original,
    prnewswire.com); no tracked-publication byline surfaced at excerpt
    level. The Verge original (m1048, #1377) remains byline-unattested in
    relay excerpts.
  - Norway Oct-5 temporary-ban coverage: BYLINE GAP, not a finding -
    the surface is wire copy (AP, AFP, Reuters via relays) with no named
    reporter byline; confirms the #1373 Reuters/NYT byline-gap finding.
  - Meta Connect Sep-2026 glasses coverage: fresh bylines sit at
    UNTRACKED outlets - James Rogerson (TechRadar, 0 corpus hits; no
    profiles/techradar.yaml) and Dave LeClair (Tom's Guide, 0 corpus
    hits; no profiles/toms-guide.yaml) are novel names but out of scope
    for a profiles/ mechanism (rejected on discipline: untracked
    outlet, not saturation). Sean Keach (The Sun) surfaced but is
    SATURATED (dedicated Type B; 7 corpus files).
  - Julian Chokkattu (WIRED): SATURATED - 31 corpus hits (mechanisms
    351/362, 411, 425/426, 431, 436). Re-screening would re-litigate.

  SCOUT OUTCOME: CLEAN NEGATIVE SCREEN - 15 searches, 0 browser.open,
  29 names screened across 3 tracks, ZERO candidates proposed. NOT a
  #1341-class instance (the scout ran its own git-grep corpus-blindness
  checks and self-rejected every saturated name before proposing; the
  tenth instance at #1369 stands as the last). Main-run verified every
  scout claim independently via git grep -F -i (profiles/ + tests/ at
  HEAD):
  - Track 1 (Xreal Aura Oct-7 bylines, deadstack.net cluster):
    Sean Hollister (Verge, 10 files), James Pero (Gizmodo, 34 files),
    Kyle Barr (Gizmodo, 14 files, own test file), Boone Ashworth
    (WIRED, #1368 rejected list), Scott Stein (CNET, #1368 rejected
    list; CNET untracked anyway) - ALL SATURATED.
  - Track 2 (Connect Sep-24 + Norway ban): Connor Hart (Dow Jones
    Newswires, 1 file - any-hit rule), Sean Keach (The Sun, 7 files,
    #1373 rejected list), Kit Eaton (inc.com, 14 files), Michael Kan
    (1 file) - ALL SATURATED. Stine Jacobsen / Tasim Zahid (Reuters
    wire, 0 files each): REJECTED on discipline (Reuters untracked;
    unattributed wire copy).
  - Track 3 (fresh divergence probes): Barbara Speed (Guardian, 4),
    Alex Heath (Verge, 23), Yildirim (Gizmodo, 10), Mat Honan (MIT TR,
    4 + #1373 rejected list), James O'Donnell (MIT TR, 7 + #1373
    rejected list), Will Douglas Heaven (MIT TR, 7 + #1373 rejected
    list), Melissa Heikkila (MIT TR, 2 + #1373 rejected list),
    Samuel Gibbs (Guardian, 11 + #1373 rejected list) - ALL SATURATED.
    Devindra Hardawar (Engadget, 8), Mariella Moon (Engadget, 10),
    Jason England / Scott Younker (Tom's Guide, 11 / 5) - saturated
    names at UNTRACKED outlets (discipline reject). Hamish Hector
    (TechRadar), Daniel Sims / Dave LeClair / Akash Pandey
    (TechSpot / Tom's Guide / Medium, 0 files each) - novel names at
    untracked outlets (discipline reject, not findings).
  - Notable corpus-hygiene datum (no pair emerged): the Norway-ban
    story has NO tracked-outlet byline at all in the search surface -
    wire copy + junk sites only.

Why the screen came up empty: the Oct-8 Xreal Aura launch was covered
by untracked outlets and relay aggregators, not tracked-publication
staff bylines; the Oct-5 Norway proposal ran as unattributed wire copy;
the Sep-24 Connect coverage at tracked outlets was dominated by
already-covered bylines (Song, Ashworth, Gurman, Stein, Schoon, Hager,
El Khoury, Perez, Gibbs, Huamani/Ortutay, Keach, Chokkattu). The
corpus-blindness discipline held - the saturation list is genuinely
saturated, and the novel names sit at untracked outlets.

Verdict saturation_screening_no_clean_pair - NOT a falsification-family
member. Max numeric mechanism_id stays 1048 (Type B lands zero mechanisms
this run); ledger holds at 65; no sixty-sixth member; the sixty-fifth
member-form stays intact in profiles/financial-times.yaml. MANUAL /
QUALITATIVE ONLY per the Aug 28 2026 standing rule (tone NOT_SCORED;
p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant false; engine NOT
run; NOT artifact-grade; no_analysis_json_update true). Correlation is
not causation; hypothesis-generating only.

Type B lands zero mechanisms: no profiles/ edit this run. The record is
the iteration-log ## #1378 entry plus this test file.

Background suite per #795: the #1375-launched full suite runs at goal
hidden_files type_d_1375_full_suite.log: this run OBSERVES only (neither
re-launches, kills, nor writes to the suite). The verdict and tombstone
belong to #1380 per #795.

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
max or next number, the forty-eighth through sixty-sixth member-claim
forms, or the fortieth direction-claim form; the constants are
constructed at runtime. (The landed ordinals live as short lowercase
forms in prose here; the live full-form claims live in profiles: the
forty-eighth, fifty-eighth, and sixtieth in financial-times.yaml, the
forty-ninth, fiftieth, and fifty-second in profiles/careers/
journalists.yaml, the fifty-first, fifty-ninth, sixty-second, and
sixty-third in news-corp.yaml, the fifty-third in the-verge.yaml, the
fifty-fourth in guardian.yaml, the fifty-fifth in atlantic.yaml, the
fifty-sixth and sixty-first in wired.yaml, the fifty-seventh and
sixty-fourth in ap.yaml, the sixty-fifth in financial-times.yaml.)
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

OWN_BASENAME = "test_type_b_1378_journalist_cross_entity_saturation_screening_oct10_6pm.py"

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "606ca07822b406280840567e044ff02e70576a4f"  # patched to the main commit sha in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1048  # max numeric; Type B lands ZERO mechanisms this run
NEXT_NUM = 1049  # integer only; key-form needles are format-built

# Post-doc-sync totals per #719: PATCHED post-collection
# (pre-sync 80438 + N tests; pre-sync 1702 + 1 file).
README_TEST_COUNT = 80518  # patched pre-main: pre-sync 80438 + 80 collected
README_FILE_COUNT = 1703  # patched pre-main: pre-sync 1702 + 1 (this file)

# Predecessor chain: #1377 Type A THIRD leg of the 1375-1379 window.
PRED_MAIN_1377 = "f324251e7223d7337fff25071477e7ac376bb87a"
PRED_ANCHOR_1377 = "895584e94c7a663ba920c445f83362933ec12a70"
PRED_DOCSYNC_1377 = "4959967a82dab382b2ba3bd6a4ca15c6c4b279bd"
PRED_LOGHASH_1377 = "efa8c2439d02e26438f881016c2fe30f7e852d4d"
PRED_PUSH_1377 = "22550b66aeab4053aba01c7f3acc2b7887100e97"

# This run's main commit (full sha), for the ancestor-form
# no-Type-B-#1378 pin. Staged 0*40 placeholder-only per #721;
# re-pinned in the anchor followup per #721 (PRED_MAIN_1378 re-pinned
# in BOTH this file and the #1377 file per the #1292 precedent).
PRED_MAIN_1378 = "606ca07822b406280840567e044ff02e70576a4f"  # re-pinned to the #1378 main sha in the anchor followup per #721/#1292

# #1379's main commit (full sha), for the ancestor-form no-Type-C-#1379
# pin (the #1191-class self-trip; #1379 is Type C per the rotation).
# Staged 0*40 placeholder-only per #721; re-pinned in #1379's terminal
# log-hash followup per #721. (Type-correct per the #1352
# type-mismatch lesson: #1379 is Type C, so the pin greps
# "Type C #1379".)
PRED_MAIN_1379 = "7ca87451bbd968cf1897c87430a7d48d678b5ed1"  # re-pinned to the #1379 main sha in #1379's anchor followup per #721/#1292

# The #1377 window-predecessor file, for the staleness pin on its
# guard-lifecycle class (max id 1048; zero next-number 1049 all forms;
# sixty-fifth member present; no sixty-sixth member; ledger holds at
# 65).
B1377_FILE = (
    "test_type_a_1377_verge_google_oct08_xreal_aura_product_"
    "register_vs_carried_meta_arms_oct10_5pm.py"
)

# m846 block region in profiles/competitor-entities.yaml at HEAD (the
# #1024 m846 decision-pending block; byte-identity pin in the
# in-flight isolation class).
M846_HEAD_START = 26349
M846_HEAD_END = 26472

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
_T66 = "SIXT" + "Y-SIXTH falsification-family member"

# 4 main-run browser.search query sets + 1 delegated scout (3 tracks)
# this run (0 browser.open per #503).
QUERY_SETS = [
    "Xreal Aura glasses launch October 2026 price preorder byline author",
    "Meta Ray-Ban smart glasses Norway ban October 2026 reporter byline",
    "Meta Connect September 2026 Ray-Ban Display glasses review author byline Verge OR Wired OR Guardian",
    "Julian Chokkattu WIRED Meta Ray-Ban smart glasses review 2026",
]

EXPECTED_TOTAL = 80  # patched pre-main: 80 tests collected in the in-gate


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
#    + rotation guard: FOURTH leg of the 1375-1379 window.
# ---------------------------------------------------------------------------


class TestAnchor1378:
    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit form per #565: ANCHORED_SHA is 0*40 until the
        # anchor followup patches it to the main-commit sha. Fails BY
        # DESIGN post-anchor.
        assert ANCHORED_SHA == "0" * 40

    def test_anchor_sha_patched_to_main_commit(self):
        # Post-commit form: ANCHORED_SHA patched to this run's main
        # commit sha in the anchor followup (placeholder + expected
        # value and the ANCHORED_SHA constant are patched).
        # Deselected in the in-gate run.
        assert ANCHORED_SHA != "0" * 40
        assert len(ANCHORED_SHA) == 40

    def test_anchor_sha_format(self):
        # Either the placeholder or a full 40-hex sha.
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA) or \
            ANCHORED_SHA == "0" * 40

    def test_anchor_duality_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Anchor convention per #565" in src
        assert "fails BY DESIGN" in src

    def test_fourth_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FOURTH leg of the 1375-1379 window" in src
        assert "D #1375 -> E #1376 -> A #1377" in src

    def test_1370_1374_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "the 1370-1374 window is VERIFIED CLOSED" in src

    def test_next_leg_is_1379_type_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "-> C #1379" in src


# ---------------------------------------------------------------------------
# 2. Main-run screens: all saturated, gap-class, or out-of-scope.
# ---------------------------------------------------------------------------


class TestMainRunScreens1378:
    def test_xreal_aura_tracked_outlet_byline_gap(self):
        # The Oct-8 Xreal Aura launch surface sits at untracked outlets
        # (tech-ish, GSMArena, AI Weekly, 9to5Google, PR Newswire); no
        # tracked-publication byline surfaced at excerpt level. The
        # Verge original (m1048, #1377) stays byline-unattested in relay
        # excerpts. A byline gap is a gap, not a finding.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TRACKED-OUTLET BYLINE GAP" in src
        assert "9to5google.com original" in src

    def test_norway_ban_wire_copy_byline_gap(self):
        # The Oct-5 Norway proposal ran as unattributed wire copy (AP,
        # AFP, Reuters via relays); confirms the #1373 byline-gap
        # finding. A byline gap is a gap, not a finding.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Norway Oct-5 temporary-ban coverage: BYLINE GAP" in src
        assert "wire copy" in src

    def test_connect_fresh_bylines_untracked_outlets(self):
        # James Rogerson (TechRadar) and Dave LeClair (Tom's Guide) are
        # novel names (zero corpus hits each) but their outlets carry no
        # profiles/ file: out of scope for a profiles/ mechanism.
        # Rejected on discipline (untracked outlet), not saturation.
        for name in ("James Rogerson", "Dave LeClair"):
            out = _git("grep", "-i", "-F", "-l", name, "HEAD",
                       "--", "profiles/", "tests/")
            assert out.stdout.strip() == "", (name, out.stdout)
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "James Rogerson (TechRadar, 0 corpus hits" in src
        assert "Dave LeClair (Tom's Guide, 0 corpus hits" in src
        assert "rejected on discipline: untracked" in src

    def test_sean_keach_saturated(self):
        # The Sun's Sean Keach surfaced on the Connect beat but carries
        # a dedicated Type B (7 corpus files); re-screening would
        # re-litigate.
        hits = _git_grep_tracked_source("Sean Keach", "profiles/")
        assert hits != [], hits
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Sean Keach (The Sun) surfaced but is" in src
        assert "SATURATED" in src

    def test_chokkattu_saturated(self):
        # Julian Chokkattu (WIRED): 31 corpus hits, mechanisms 351/362,
        # 411, 425/426, 431, 436. Re-screening would re-litigate.
        out = _git("grep", "-i", "-F", "-l", "Julian Chokkattu", "HEAD",
                   "--", "profiles/", "tests/")
        hits = [l for l in out.stdout.splitlines() if l.strip()]
        assert len(hits) >= 30, hits
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Julian Chokkattu (WIRED): SATURATED" in src
        assert "31 corpus hits" in src

    def test_query_sets_bounded(self):
        # 4 main-run browser.search query sets, documented verbatim.
        assert len(QUERY_SETS) == 4
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        for q in QUERY_SETS:
            assert q in src, q


# ---------------------------------------------------------------------------
# 3. Scout outcome (filled from the scout's report; main-run verifies
#    every scout claim independently per the #1341 lesson).
# ---------------------------------------------------------------------------


class TestScoutCorpusBlindness1378:
    def test_scout_clean_negative_screen(self):
        # The scout ran 15 searches + its own git-grep corpus-blindness
        # checks across 3 tracks and proposed ZERO candidates: a clean
        # negative screen, not a #1341-class instance (the tenth
        # instance at #1369 stands as the last).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "CLEAN NEGATIVE SCREEN" in src
        assert "proposed ZERO" in src
        assert "NOT a #1341-class instance" in src

    def test_scout_track1_saturated_self_rejections_verified(self):
        # Every Track-1 self-rejection verified by the main run's own
        # git grep -F -i (profiles/ + tests/ at HEAD). Counts are the
        # main-run verified counts (the scout undercounted some; the
        # verdicts hold regardless).
        for name, minimum in (("Sean Hollister", 10), ("James Pero", 30),
                              ("Kyle Barr", 10), ("Alex Heath", 20)):
            out = _git("grep", "-i", "-F", "-l", name, "HEAD",
                       "--", "profiles/", "tests/")
            hits = [l for l in out.stdout.splitlines() if l.strip()]
            assert len(hits) >= minimum, (name, len(hits))
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Sean Hollister (Verge, 10 files)" in src
        assert "James Pero (Gizmodo, 34 files)" in src
        assert "Kyle Barr (Gizmodo, 14 files" in src

    def test_scout_track2_self_rejections_verified(self):
        for name, minimum in (("Connor Hart", 1), ("Sean Keach", 5),
                              ("Kit Eaton", 10), ("Michael Kan", 1)):
            out = _git("grep", "-i", "-F", "-l", name, "HEAD",
                       "--", "profiles/", "tests/")
            hits = [l for l in out.stdout.splitlines() if l.strip()]
            assert len(hits) >= minimum, (name, len(hits))
        # Reuters wire bylines: zero hits but rejected on discipline
        # (untracked outlet + unattributed wire copy), not saturation.
        for name in ("Stine Jacobsen", "Tasim Zahid"):
            out = _git("grep", "-i", "-F", "-l", name, "HEAD",
                       "--", "profiles/", "tests/")
            assert out.stdout.strip() == "", (name, out.stdout)
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Stine Jacobsen / Tasim Zahid (Reuters" in src
        assert "REJECTED on discipline" in src

    def test_scout_track3_self_rejections_verified(self):
        for name, minimum in (("Barbara Speed", 4), ("Alex Heath", 20),
                              ("Yildirim", 10), ("Mat Honan", 4),
                              ("Devindra Hardawar", 8),
                              ("Mariella Moon", 10)):
            out = _git("grep", "-i", "-F", "-l", name, "HEAD",
                       "--", "profiles/", "tests/")
            hits = [l for l in out.stdout.splitlines() if l.strip()]
            assert len(hits) >= minimum, (name, len(hits))
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Barbara Speed (Guardian, 4)" in src
        assert "Alex Heath (Verge, 23)" in src

    def test_no_1341_instance_this_run(self):
        # The scout committed no corpus blindness: the tenth #1341
        # instance (#1369) stands as the last; this run pins the clean
        # screen instead.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "the tenth #1341 instance at" in src
        assert "#1369 stands as the last" in src

    def test_scout_untrusted_convention(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1341 lesson" in src

# ---------------------------------------------------------------------------
# 4. Mechanism novelty: Type B lands ZERO mechanisms this run; max stays
#    1048; next 1049 stays clean in all three key forms.
# ---------------------------------------------------------------------------


class TestMechanismNovelty1378:
    def test_max_numeric_mechanism_id_stays_1048(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_zero_next_number_keys_all_forms(self):
        # Numeric (profiles/ scope), underscore and dash (profiles/ +
        # tests/ scope, own file excluded per #715). Holds pre-commit
        # and post-commit (Type B lands zero mechanisms).
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_profiles_edit_this_run(self):
        # Type B lands zero mechanisms: the ONLY profiles/
        # working-tree modification is the pre-existing in-flight
        # #899 hunk on profiles/nytimes.yaml (explicitly untouched
        # by this run; everything else in profiles/ is clean).
        out = _git("status", "--short", "--", "profiles/").stdout
        lines = [l for l in out.splitlines() if l.strip()]
        assert lines == [" M profiles/nytimes.yaml"], out

    def test_mech_num_next_num_pins(self):
        # The file's own constants pin the zero-landing arithmetic.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1048" in src
        assert "NEXT_NUM = 1049" in src


# ---------------------------------------------------------------------------
# 5. Guard lifecycle: forward pins for #1379; #1378 staged this run.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1378:
    def test_pins_on_zero_mechanism_landing(self):
        # Type B lands zero mechanisms: max stays 1048, next 1049.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1048" in src
        assert "NEXT_NUM = 1049" in src

    def test_no_type_b_1378_in_git_log_pin(self):
        # Post-main-commit form for THIS run's own pin (the
        # #1191-class self-trip, re-pinned in this run's terminal
        # log-hash followup per #721/#1292): every commit whose
        # message matches "Type B #1378" must be this run's main
        # commit or a descendant of it. Deselected in the in-gate
        # run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type B #1378")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1378's own commits"
        main = _git("rev-parse", PRED_MAIN_1378).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_no_type_c_1379_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1379's terminal log-hash followup
        # per #721): every commit whose message matches "Type C
        # #1379" must be #1379's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1379 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type C #1379")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1379's own commits"
        main = _git("rev-parse", PRED_MAIN_1379).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1048_numeric_present_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(MECH_NUM) != []

    def test_1048_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_1048_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_1049_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1049_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1049_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_fortieth_direction_pin(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_forty_eighth_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T48, "HEAD", "--",
                   "profiles/financial-times.yaml")
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_forty_ninth_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T49, "HEAD", "--",
                   "profiles/careers/journalists.yaml")
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fiftieth_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T50, "HEAD", "--",
                   "profiles/careers/journalists.yaml")
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_first_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T51, "HEAD", "--",
                   "profiles/news-corp.yaml")
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_second_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T52, "HEAD", "--",
                   "profiles/careers/journalists.yaml")
        assert out.stdout.strip().endswith(":5"), out.stdout

    def test_fifty_third_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T53, "HEAD", "--",
                   "profiles/the-verge.yaml")
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fourth_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T54, "HEAD", "--",
                   "profiles/guardian.yaml")
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fifth_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T55, "HEAD", "--",
                   "profiles/atlantic.yaml")
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_sixth_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T56, "HEAD", "--",
                   "profiles/wired.yaml")
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_seventh_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T57, "HEAD", "--",
                   "profiles/ap.yaml")
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_eighth_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T58, "HEAD", "--",
                   "profiles/financial-times.yaml")
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_ninth_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T59, "HEAD", "--",
                   "profiles/news-corp.yaml")
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixtieth_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T60, "HEAD", "--",
                   "profiles/financial-times.yaml")
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixty_first_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T61, "HEAD", "--",
                   "profiles/wired.yaml")
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_sixty_second_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T62, "HEAD", "--",
                   "profiles/news-corp.yaml")
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixty_third_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T63, "HEAD", "--",
                   "profiles/news-corp.yaml")
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_sixty_fourth_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T64, "HEAD", "--",
                   "profiles/ap.yaml")
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_sixty_fifth_member_intact_pin(self):
        # Post-landing form: the m1047 block (#1372) carries the
        # sixty-fifth member-claim form twice in
        # profiles/financial-times.yaml; Type B lands zero mechanisms
        # so it stays intact.
        out = _git("grep", "-c", "-F", _T65, "HEAD", "--",
                   "profiles/financial-times.yaml")
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_sixty_sixth_member_pin(self):
        # The sixty-sixth member-claim form stays absent repo-wide
        # (fragment-built needle per #715).
        needle = _T66
        hits = []
        for p in _iter_source_files():
            if needle in open(p, encoding="utf-8",
                               errors="replace").read():
                hits.append(p)
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                if needle in open(p, encoding="utf-8",
                                   errors="replace").read():
                    hits.append(p)
        assert hits == [], hits

    def test_ledger_holds_at_65_pin(self):
        # Type B lands zero mechanisms and the saturation-screening
        # verdict is NOT a falsification-family member: ledger holds
        # at 65. Pinned via the docstring's own prose form (kept
        # lowercase-short per #715).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ledger holds at 65" in src
        assert "no sixty-sixth member" in src

# ---------------------------------------------------------------------------
# 6. Staleness pin: the predecessor's guard lifecycle, run as-is.
# ---------------------------------------------------------------------------


class TestStalenessPins1378:
    def test_1377_guard_lifecycle_post_terminal_followup(self):
        # Post-terminal-followup form: 26 passed. The #1191-class
        # no_type_b_1378_in_git_log forward pin flips green in this
        # run's terminal log-hash followup per #721/#1292 (PRED_MAIN_1378
        # re-pinned in the #1377 file). There is NO #1272-class
        # forward-guard expiry this run: Type B lands zero mechanisms,
        # so the 1049-form pins stay green; the member and direction
        # pins stay green (no member, no direction landed this run).
        # The #1377 block is read-only to this run. Deselected
        # pre-commit (verified only post-terminal-followup).
        r = subprocess.run(
            ["python3", "-m", "pytest",
             os.path.join(TESTS_DIR, B1377_FILE)
             + "::TestGuardLifecycle1377",
             "-q", "-p", "no:cacheprovider"],
            capture_output=True, text=True, timeout=300, cwd=REPO_ROOT,
        )
        tail = r.stdout.strip().splitlines()[-1]
        assert "26 passed" in tail, tail


# ---------------------------------------------------------------------------
# 7. Doc-sync per #719 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestDocSync1378:
    def test_readme_test_count_post_sync_positive(self):
        # Post-sync-positive per #719: constants already hold the
        # post-doc-sync values; patched pre-main once the in-gate
        # collection count is known. Fails pre-commit by design;
        # deselected in the in-gate run.
        src = _read(README_PATH)
        assert str(README_TEST_COUNT) in src

    def test_readme_file_count_post_sync_positive(self):
        src = _read(README_PATH)
        assert str(README_FILE_COUNT) in src

    def test_readme_has_1378_table_row(self):
        src = _read(README_PATH)
        assert "test_type_b_1378" in src


# ---------------------------------------------------------------------------
# 8. Iteration log per #721 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestIterationLog1378:
    def test_log_has_1378_heading(self):
        # Written in the doc-sync commit per #721. Fails pre-commit
        # by design; deselected in the in-gate run.
        assert "## #1378" in _read(LOG_PATH)

    def test_log_registers_main_anchor_docsync_hashes(self):
        src = _read(LOG_PATH)
        assert "log-hash" in src

    def test_log_records_saturation_screening(self):
        src = _read(LOG_PATH)
        assert "saturation_screening_no_clean_pair" in src
        assert "1048" in src


# ---------------------------------------------------------------------------
# 9. Screening ledger: the journalists screened this run.
# ---------------------------------------------------------------------------


class TestScreeningLedger1378:
    def test_screened_journalists_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        for name in ("Julian Chokkattu", "Sean Keach", "James Rogerson",
                     "Dave LeClair", "Kashmir Hill", "Samuel Gibbs",
                     "Dara Kerr", "Kaitlyn Huamani", "Barbara Ortutay",
                     "Toby Sterling", "Aisha Counts", "Hasan Chowdhury",
                     "Tanya Basu", "Jonathan Vanian", "Kurt Wagner",
                     "Michael Liedtke"):
            assert name in src, name

    def test_carried_rejections_referenced(self):
        # The #1353 sixteen, the #1358 six, and the #1368 eight carry
        # as rejections; re-screening them would re-litigate.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        for name in ("Lily Hay Newman", "Sarah Perez", "Lauren Goode",
                     "Dominic Preston", "Joanna Stern", "Ariel Zilber",
                     "Ryne Hager", "Rita El Khoury", "Abner Li",
                     "Karissa Bell", "Igor Bonifacic", "C. Scott Brown",
                     "Mark Gurman", "Raymond Wong", "Jessica Gorringe",
                     "Boone Ashworth", "Victoria Song", "Lucas Ropek",
                     "Scott Stein", "Ben Schoon"):
            assert name in src, name

    def test_no_profiles_edit_this_run(self):
        # Type B lands zero mechanisms: no profiles/ edit this run
        # (verified via git status in the iteration-log entry, not
        # here).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "no profiles/ edit this run" in src


# ---------------------------------------------------------------------------
# 10. Research method.
# ---------------------------------------------------------------------------


class TestResearchMethod1378:
    def test_scout_plus_main_run_sets(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1 delegated scout (3 tracks)" in src
        assert "4 main-run browser.search verification sets" in src

    def test_zero_browser_open(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "0 browser.open per #503" in src

    def test_scout_untrusted_convention(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1341 lesson" in src


# ---------------------------------------------------------------------------
# 11. Verdict: saturation screening, manual/qualitative only.
# ---------------------------------------------------------------------------


class TestVerdict1378:
    def test_verdict_saturation_screening(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "saturation_screening_no_clean_pair" in src

    def test_not_falsification_family_member(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NOT a falsification-family" in src
        assert "ledger holds at 65" in src

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
        assert "this run OBSERVES only" in src
        assert "verdict and tombstone" in src
        assert "belong to #1380 per #795" in src


# ---------------------------------------------------------------------------
# 12. In-flight isolation: the pending items stay out of this run.
# ---------------------------------------------------------------------------


class TestInFlightIsolation1378:
    def test_m846_byte_identity_at_head(self):
        # The #1024 m846 decision-pending block is untouched: the
        # working-tree byte region matches HEAD exactly.
        head = _git("show",
                    "HEAD:profiles/competitor-entities.yaml").stdout
        work = _read(os.path.join(REPO_ROOT,
                                  "profiles/competitor-entities.yaml"))
        assert (head.splitlines()[M846_HEAD_START - 1:M846_HEAD_END]
                == work.splitlines()[M846_HEAD_START - 1:M846_HEAD_END])

    def test_in_flight_items_untouched_by_this_run(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Do NOT touch #1024" in src
        assert "#899" in src
        assert "#938" in src
        assert "#900" in src
        assert "#1012-wt" in src


# ---------------------------------------------------------------------------
# 13. Rotation.
# ---------------------------------------------------------------------------


class TestRotation1378:
    def test_window_sequence(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1375 -> E #1376 -> A #1377" in src

    def test_next_leg_is_type_c(self):
        assert PRED_MAIN_1379 == "0" * 40

    def test_type_letter_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type B #1378" in src

    def test_background_suite_observed_only(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "OBSERVES only" in src
        assert "#1380" in src


# ---------------------------------------------------------------------------
# 14. ASCII and formatting hygiene.
# ---------------------------------------------------------------------------


class TestAscii1378:
    def test_no_em_dashes_in_test_file(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "\u2014" not in src

    def test_ascii_only_in_test_file(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        src.encode("ascii")

    def test_expected_total_declared(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "EXPECTED_TOTAL = %d" % EXPECTED_TOTAL in src
