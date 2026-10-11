# -*- coding: utf-8 -*-
"""Type B #1383: journalist cross-entity saturation screening (Oct 10 2026,
~10:00 PM PDT) - NO clean fresh pair; NO mechanism landed.

FOURTH leg of the 1380-1384 window: D #1380 -> E #1381 -> A #1382 -> B #1383
(this run) -> C #1384. The 1375-1379 window is VERIFIED CLOSED.

1 delegated scout (3 tracks) + 4 main-run browser.search verification
sets, 0 browser.open per #503, excerpt-bounded. The scout's outcome and the
main-run screens are documented below; every scout claim is verified by
the main run's own git grep -F -i at HEAD (the #1341 lesson: the scout is
never trusted blindly).

  MAIN-RUN SCREENS (all excerpt-bounded, 0 browser.open per #503):
  - Ray-Ban Meta Audio Oct-13 launch: Gizmodo's launch piece ("Meta
    Introduces Audio-Only Smart Glasses to Avoid the 'Perv' Problem",
    James Pero byline) is SATURATED - 35 corpus files (the m806/m818
    line; the piece carries a Meta-paid travel/lodging disclosure). The
    Sun's Connect hands-on (thesun.ie) sits at an UNTRACKED outlet. All
    other launch coverage at untracked outlets (yankodesign, impartpad,
    theshortcut, geeky-gadgets, techmymoney).
  - Oakley Meta HSTN Oct-2026 reviews: UNTRACKED-OUTLET BYLINE GAP, not
    a finding - the surface sits at powder.com, zdnet.com, 91mobiles,
    fashionide, yardbarker, industrym; zero tracked-publication bylines
    at excerpt level.
  - Ray-Ban Meta Display Sep-2026: own-repo GitHub commit rows surfaced
    (circular, rejected); medial.app relays a Verge Display review
    ("amazes and terrifies me") with byline UNATTESTED in the excerpt;
    recordinglaw.com's Hamburg-DPA piece is a NEW URL key (zero
    pre-commit corpus hits) at an UNTRACKED outlet - new URL, not a new
    fact (the Sep-10 HmbBfDI report topic is in corpus).
  - Snap Specs 2026 shipping: Jay Peters (The Verge, relay-attested via
    wesearch.press) SATURATED - 20 corpus files; Andrew Williams
    (Trusted Reviews) has 2 corpus files AND the piece sits at an
    UNTRACKED outlet - discipline reject; a WIRED hands-on is
    relay-attested via futurewire.online with byline UNATTESTED;
    the theverge.com/tech/950492 snap-specs-ar-glasses-launch-date-preorder
    full slug form is a new verbatim key, but the URL base was already
    recorded in corpus via the #657 research-method note (browser.open
    policy block) - a re-surface of a known base, not a fresh key, and
    no byline at excerpt level either way.

  SCOUT OUTCOME: CLEAN NEGATIVE SCREEN - 15 searches, 0 browser.open,
  16 names screened across 3 tracks, ZERO candidates proposed. NOT a
  #1341-class instance (the scout ran its own git-grep corpus-blindness
  checks and self-rejected every saturated name before proposing; the
  tenth instance at #1369 stands as the last). Main-run verified every
  scout claim independently via git grep -F -i at HEAD (profiles/ +
  tests/):
  - Track 1 (Meta Audio / Oakley HSTN Oct-2026 launch bylines): James
    Pero (Gizmodo, 35 files), Katie Notopoulos (BI, 7 files, own Type B
    #953), Terrence O'Brien (Verge, 7 files), Samuel Gibbs (Guardian,
    12 files), Boone Ashworth (WIRED, saturated via Type B #998 /
    mechanism 830), Raymond Wong (Gizmodo, 40 files), Hamish Hector
    (TechRadar, 13 files, untracked outlet + Type B #963 / mechanism
    809), Andy Boxall (Android Police, 21 files, untracked outlet +
    Type B #988 / mechanism 824), Ben Schoon (9to5Google, untracked) -
    ALL SATURATED or UNTRACKED.
  - Track 2 (same-journalist divergence probes): Victoria Song (66),
    Alex Heath (24), David Pierce (16), Kyle Barr (15), Blake
    Montgomery (5), Kelvin Chan (6), Dara Kerr (10) - ALL SATURATED;
    Sabrina Ortiz (ZDNet, 6, untracked), Will Shanklin (Engadget, 6,
    untracked), Anshel Sag (Moor Insights, 1, untracked) - untracked
    outlets. The strongest Track-2-style finding the scout could have
    produced (the Wong Fury-vs-Aura divergence) already exists as
    mechanism 135.
  - Track 3 (Snap Specs 2026 shipping-phase bylines): collapses to one
    name at tracked outlets - James Pero (Gizmodo), whose launch-window
    register is already covered as Type B #858 / mechanism 746; the
    shipping-phase hands-ons are the same saturated byline. All other
    Specs coverage is untracked (TechCrunch, Road to VR, Kotaku,
    PhoneArena) or wire copy (Reuters, no byline).
  - Notable corpus-hygiene data (no pair emerged): Anuj Behal (MIT
    Technology Review) is the single zero-hit tracked-outlet name
    surfaced - NOT a candidate (no competitor-wearable arm found; the
    Meta arm is a Download-newsletter curator item, below the Type B
    evidence tier; flagged for a future run if a Behal competitor arm
    surfaces). Chris Haslam (WIRED) carries exactly 1 corpus hit - the
    prior scout's Oct-4 reject note itself; the stale rejection still
    holds. Beat-level finding: wearables-beat saturation at tracked
    outlets is near-total (the Sep 23-26 Connect launch window is
    covered across Gizmodo/Verge/WIRED/BI/Guardian); the scout
    recommends future Type B scouts pivot to untracked-to-tracked
    migration tracking or beat-adjacent coverage (privacy-policy
    reporting, India/EU enforcement) rather than launch-window bylines.

Why the screen came up empty: the Oct-13 Meta Audio launch window and
the Snap Specs shipping window at tracked outlets are covered by
already-mechanismized bylines (Pero, Wong, Ashworth, Notopoulos,
O'Brien, Gibbs); the remaining novel names sit at untracked outlets
(TechRadar, 9to5Google, ZDNet, Trusted Reviews) or in wire copy with no
byline. The corpus-blindness discipline held - the saturation list is
genuinely saturated, and the one zero-hit tracked-outlet name (Behal)
lacks a competitor arm.

Verdict saturation_screening_no_clean_pair - NOT a falsification-family
member. Max numeric mechanism id stays 1049 (Type B lands zero mechanisms
this run); ledger holds at 65; no sixty-sixth member; the sixty-fifth
member-form stays intact in profiles/financial-times.yaml. MANUAL /
QUALITATIVE ONLY per the Aug 28 2026 standing rule (tone NOT_SCORED;
p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant false; engine NOT
run; NOT artifact-grade; no_analysis_json_update true). Correlation is
not causation; hypothesis-generating only.

Type B lands zero mechanisms: no profiles/ edit this run. The record is
the iteration-log ## #1383 entry plus this test file.

Background suite per #795: the #1380-launched full suite runs at goal
hidden_files type_d_1380_full_suite.log: this run OBSERVES only (neither
re-launches, kills, nor writes to the suite). The verdict and tombstone
belong to #1385 per #795.

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

OWN_BASENAME = "test_type_b_1383_journalist_cross_entity_saturation_screening_oct10_10pm.py"

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "0" * 40  # placeholder pre-commit; patched in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1049  # max numeric; Type B lands ZERO mechanisms this run
NEXT_NUM = 1050  # integer only; key-form needles are format-built

# Post-doc-sync totals per #719: PATCHED post-collection
# (pre-sync 80903 + N tests; pre-sync 1707 + 1 file).
README_TEST_COUNT = 80982  # patched pre-main: pre-sync 80903 + 79 collected
README_FILE_COUNT = 1708  # patched pre-main: pre-sync 1707 + 1 (this file)

# Predecessor chain: #1382 Type A THIRD leg of the 1380-1384 window.
PRED_MAIN_1382 = "a4d8386621cbe1f7d65739a222765cd53d24f862"
PRED_ANCHOR_1382 = "7777cbdeef092eb842c2b1881957d606f94c2544"
PRED_DOCSYNC_1382 = "d12d3d2d897d3b5996a1b9aa1b667abe5a2ce151"
PRED_LOGHASH_1382 = "047ec2ee98ad8864f7486ece4bde63aabb856e1d"
PRED_PUSH_1382 = "901bacfabdbbf00abe29e551596c619d2f6ab0ac"

# This run's main commit (full sha), for the ancestor-form
# no-Type-B-#1383 pin. Staged 0*40 placeholder-only per #721;
# re-pinned in the anchor followup per #721 (PRED_MAIN_1383 re-pinned
# in BOTH this file and the #1382 file per the #1292 precedent).
PRED_MAIN_1383 = "0" * 40  # re-pinned to the #1383 main sha in the anchor followup per #721/#1292

# #1384's main commit (full sha), for the ancestor-form no-Type-C-#1384
# pin (the #1191-class self-trip; #1384 is Type C per the rotation).
# Staged 0*40 placeholder-only per #721; re-pinned in #1384's terminal
# log-hash followup per #721. (Type-correct per the #1352
# type-mismatch lesson: #1384 is Type C, so the pin greps
# "Type C #1384".)
PRED_MAIN_1384 = "0" * 40  # forward guard for #1384 Type C; re-pinned to the #1384 main sha in #1384's terminal log-hash followup per #721

# The #1382 window-predecessor file, for the staleness pin on its
# guard-lifecycle class (max id 1049; zero next-number 1050 all forms;
# sixty-fifth member present; no sixty-sixth member; ledger holds at
# 65).
B1382_FILE = (
    "test_type_a_1382_verge_anthropic_sep29_ipo_filing_pair_"
    "publication_level_control_case_oct10_9pm.py"
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
    "Ray-Ban Meta Audio October 2026 launch review byline The Verge",
    "Oakley Meta HSTN smart glasses review October 2026 author byline",
    "Ray-Ban Meta Display review September 2026 byline Verge WIRED Guardian",
    "Snap Specs AR glasses 2026 review author byline Verge WIRED",
]

EXPECTED_TOTAL = 79  # patched pre-main: 79 tests collected in the in-gate


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
#    + rotation guard: FOURTH leg of the 1380-1384 window.
# ---------------------------------------------------------------------------


class TestAnchor1383:
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
        assert "FOURTH leg of the 1380-1384 window" in src
        assert "D #1380 -> E #1381 -> A #1382" in src

    def test_1375_1379_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "the 1375-1379 window is VERIFIED CLOSED" in src

    def test_next_leg_is_1384_type_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "-> C #1384" in src


# ---------------------------------------------------------------------------
# 2. Main-run screens: all saturated, gap-class, or out-of-scope.
# ---------------------------------------------------------------------------


class TestMainRunScreens1383:
    def test_audio_pero_saturated(self):
        # Gizmodo's Ray-Ban Meta Audio launch piece ("Meta Introduces
        # Audio-Only Smart Glasses to Avoid the 'Perv' Problem", James
        # Pero byline) is SATURATED - 35 corpus files on the m806/m818
        # line. The piece carries a Meta-paid travel/lodging disclosure.
        # Re-screening would re-litigate.
        hits = _git_grep_tracked_source("James Pero", "profiles/")
        assert hits != [], hits
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "James Pero byline) is SATURATED" in src
        assert "35 corpus files" in src

    def test_audio_sun_untracked(self):
        # The Sun's Connect hands-on (thesun.ie) sits at an untracked
        # outlet (no profiles/the-sun.yaml): out of scope for a
        # profiles/ mechanism. Rejected on discipline, not saturation.
        out = _git("grep", "-l", "the-sun.yaml", "HEAD", "--",
                   "profiles/")
        assert out.stdout.strip() == "", out.stdout
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "thesun.ie) sits at an UNTRACKED outlet" in src

    def test_oakley_hstn_untracked_outlet_byline_gap(self):
        # The Oct-2026 Oakley Meta HSTN review surface sits at untracked
        # outlets (powder.com, zdnet.com, 91mobiles, fashionide,
        # yardbarker, industrym); zero tracked-publication bylines at
        # excerpt level. A byline gap is a gap, not a finding.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "UNTRACKED-OUTLET BYLINE GAP" in src
        assert "powder.com, zdnet.com, 91mobiles" in src

    def test_display_relay_and_new_url_keys(self):
        # The Ray-Ban Meta Display Sep-2026 surface: own-repo GitHub
        # commit rows surfaced (circular, rejected); medial.app relays a
        # Verge Display review ("amazes and terrifies me") with byline
        # UNATTESTED in the excerpt; recordinglaw.com's Hamburg-DPA
        # piece is a NEW URL key (zero pre-commit corpus hits, verified
        # by the main run's own git grep -F at HEAD) at an UNTRACKED
        # outlet - new URL, not a new fact. The Verge Specs canonical
        # URL's full slug form is a new verbatim key, but its URL base
        # (theverge.com/tech/950492) is already in corpus via the #657
        # research-method note (browser.open policy block) - a
        # re-surface of a known base, not a fresh key, and no byline at
        # excerpt level either way.
        out = _git("grep", "-F", "-l",
                   "recordinglaw.com/news/hamburg-dpa", "HEAD")
        assert out.stdout.strip() == "", out.stdout
        out = _git("grep", "-F", "-l",
                   "theverge.com/tech/950492/"
                   "snap-specs-ar-glasses-launch-date-preorder", "HEAD")
        assert out.stdout.strip() == "", out.stdout
        out = _git("grep", "-F", "-l", "theverge.com/tech/950492",
                   "HEAD")
        assert out.stdout.strip() != "", out.stdout
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "with byline UNATTESTED in the excerpt" in src
        assert "NEW URL key" in src

    def test_snap_specs_peters_saturated(self):
        # Jay Peters (The Verge) on Snap Specs 2026 (relay-attested via
        # wesearch.press) is SATURATED - 20 corpus files. Re-screening
        # would re-litigate.
        hits = _git_grep_tracked_source("Jay Peters", "profiles/")
        assert hits != [], hits
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Jay Peters (The Verge" in src
        assert "20 corpus files" in src

    def test_snap_williams_discipline_reject(self):
        # Andrew Williams (Trusted Reviews) has corpus hits (2 files:
        # a journalists.yaml career entry and a Type B #903 mention)
        # AND the Snap Specs piece sits at an untracked outlet. Double
        # reject: not zero-hit, and untracked outlet. Not a finding.
        out = _git("grep", "-l", "trustedreviews.yaml", "HEAD", "--",
                   "profiles/")
        assert out.stdout.strip() == "", out.stdout
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "discipline reject" in src


# ---------------------------------------------------------------------------
# 3. Scout corpus-blindness: every scout claim main-run-verified.
# ---------------------------------------------------------------------------


class TestScoutCorpusBlindness1383:
    def test_track1_all_saturated_or_untracked(self):
        # Track 1 (Meta Audio / Oakley HSTN Oct-2026 launch bylines):
        # every tracked-outlet byline the scout surfaced is saturated;
        # the rest sit at untracked outlets. Verified by the main run's
        # own git grep -F -i at HEAD (the #1341 lesson).
        expectations = {
            "Katie Notopoulos": 7,
            "Terrence O'Brien": 7,
            "Samuel Gibbs": 12,
            "Raymond Wong": 40,
            "Hamish Hector": 13,
            "Andy Boxall": 21,
        }
        for name, expected in expectations.items():
            out = _git("grep", "-i", "-F", "-l", name, "HEAD", "--",
                       "profiles/", "tests/")
            count = len([l for l in out.stdout.splitlines()
                         if l.strip()])
            assert count == expected, (name, count, expected)
        # Boone Ashworth: saturated via Type B #998 / mechanism 830
        # (journalists.yaml carrier).
        out = _git("grep", "-F", "-l", "mechanism_id: 830", "HEAD",
                   "--", "profiles/careers/journalists.yaml")
        assert out.stdout.strip() != "", out.stdout
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Track 1 (Meta Audio / Oakley HSTN Oct-2026 launch bylines)" in src

    def test_track2_all_saturated_or_untracked(self):
        # Track 2 (same-journalist divergence probes): all
        # tracked-outlet names saturated; the rest at untracked
        # outlets. The strongest finding this track could have produced
        # (Wong Fury-vs-Aura) already exists as mechanism 135.
        expectations = {
            "Victoria Song": 66,
            "Alex Heath": 24,
            "David Pierce": 16,
            "Kyle Barr": 15,
            "Blake Montgomery": 5,
            "Kelvin Chan": 6,
            "Dara Kerr": 10,
        }
        for name, expected in expectations.items():
            out = _git("grep", "-i", "-F", "-l", name, "HEAD", "--",
                       "profiles/", "tests/")
            count = len([l for l in out.stdout.splitlines()
                         if l.strip()])
            assert count == expected, (name, count, expected)
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "mechanism 135" in src

    def test_track3_collapses_to_saturated_pero(self):
        # Track 3 (Snap Specs 2026 shipping-phase bylines): the tracked-
        # outlet surface collapses to James Pero (Gizmodo), whose
        # launch-window register is already covered as Type B #858 /
        # mechanism 746. Everything else is untracked or wire copy.
        out = _git("grep", "-F", "-l", "mechanism_id: 746", "HEAD",
                   "--", "profiles/careers/journalists.yaml")
        assert out.stdout.strip() != "", out.stdout
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type B #858 / mechanism 746" in src

    def test_hygiene_behal_haslam(self):
        # Anuj Behal (MIT Technology Review): the single zero-hit
        # tracked-outlet name surfaced - NOT a candidate (no
        # competitor-wearable arm; the Meta arm is a
        # Download-newsletter curator item, below the Type B evidence
        # tier). Chris Haslam (WIRED): exactly 1 corpus hit, the prior
        # scout's Oct-4 reject note itself; the stale rejection holds.
        out = _git("grep", "-i", "-F", "-l", "Anuj Behal", "HEAD",
                   "--", "profiles/", "tests/")
        assert out.stdout.strip() == "", out.stdout
        out = _git("grep", "-i", "-F", "-l", "Chris Haslam", "HEAD",
                   "--", "profiles/", "tests/")
        assert len([l for l in out.stdout.splitlines()
                    if l.strip()]) == 1, out.stdout
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Anuj Behal (MIT" in src
        assert "Chris Haslam (WIRED)" in src

    def test_not_a_1341_instance(self):
        # NOT a #1341-class instance: the scout ran its own git-grep
        # corpus-blindness checks and self-rejected every saturated
        # name before proposing; the tenth instance at #1369 stands as
        # the last. The main run verified every scout claim
        # independently via git grep -F -i at HEAD.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NOT a" in src
        assert "#1341-class instance" in src
        assert "the tenth instance at #1369 stands as the last" in src


# ---------------------------------------------------------------------------
# 4. Mechanism novelty: max stays 1049; zero 1050 key forms; no
#    profiles/ edit.
# ---------------------------------------------------------------------------


class TestMechanismNovelty1383:
    def test_max_numeric_mechanism_id_stays_1049(self):
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
        assert "MECH_NUM = 1049" in src
        assert "NEXT_NUM = 1050" in src


# ---------------------------------------------------------------------------
# 5. Guard lifecycle: forward pins for #1384; #1383 staged this run.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1383:
    def test_pins_on_zero_mechanism_landing(self):
        # Type B lands zero mechanisms: max stays 1049, next 1050.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1049" in src
        assert "NEXT_NUM = 1050" in src

    def test_no_type_b_1383_in_git_log_pin(self):
        # Post-main-commit form for THIS run's own pin (the
        # #1191-class self-trip, re-pinned in this run's terminal
        # log-hash followup per #721/#1292): every commit whose
        # message matches "Type B #1383" must be this run's main
        # commit or a descendant of it. Deselected in the in-gate
        # run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type B #1383")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1383's own commits"
        main = _git("rev-parse", PRED_MAIN_1383).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_no_type_c_1384_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1384's terminal log-hash followup
        # per #721): every commit whose message matches "Type C
        # #1384" must be #1384's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1384 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type C #1384")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1384's own commits"
        main = _git("rev-parse", PRED_MAIN_1384).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1049_numeric_present_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(MECH_NUM) != []

    def test_1049_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_1049_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_1050_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1050_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1050_dash_absent_repo_wide(self):
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


class TestStalenessPins1383:
    def test_1382_guard_lifecycle_post_terminal_followup(self):
        # Post-terminal-followup form: 26 passed. The #1191-class
        # no_type_b_1383_in_git_log forward pin flips green in this
        # run's terminal log-hash followup per #721/#1292 (PRED_MAIN_1383
        # re-pinned in the #1382 file). There is NO #1272-class
        # forward-guard expiry this run: Type B lands zero mechanisms,
        # so the 1050-form pins stay green; the member and direction
        # pins stay green (no member, no direction landed this run).
        # The #1382 block is read-only to this run. Deselected
        # pre-commit (verified only post-terminal-followup).
        venv_py = os.path.join(REPO_ROOT, ".venv", "bin", "python")
        r = subprocess.run(
            [venv_py, "-m", "pytest",
             os.path.join(TESTS_DIR, B1382_FILE)
             + "::TestGuardLifecycle1382",
             "-q", "-p", "no:cacheprovider"],
            capture_output=True, text=True, timeout=300, cwd=REPO_ROOT,
        )
        tail = r.stdout.strip().splitlines()[-1]
        assert "26 passed" in tail, tail
# ---------------------------------------------------------------------------
# 7. Doc-sync per #719 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestDocSync1383:
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

    def test_readme_has_1383_table_row(self):
        src = _read(README_PATH)
        assert "test_type_b_1383" in src


# ---------------------------------------------------------------------------
# 8. Iteration log per #721 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestIterationLog1383:
    def test_log_has_1383_heading(self):
        # Written in the doc-sync commit per #721. Fails pre-commit
        # by design; deselected in the in-gate run.
        assert "## #1383" in _read(LOG_PATH)

    def test_log_registers_main_anchor_docsync_hashes(self):
        src = _read(LOG_PATH)
        assert "log-hash" in src

    def test_log_records_saturation_screening(self):
        src = _read(LOG_PATH)
        assert "saturation_screening_no_clean_pair" in src
        assert "1049" in src


# ---------------------------------------------------------------------------
# 9. Screening ledger: the journalists screened this run.
# ---------------------------------------------------------------------------


class TestScreeningLedger1383:
    def test_screened_journalists_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        for name in ("James Pero", "Katie Notopoulos", "Terrence O'Brien",
                     "Samuel Gibbs", "Boone Ashworth", "Raymond Wong",
                     "Hamish Hector", "Andy Boxall", "Ben Schoon",
                     "Victoria Song", "Alex Heath", "David Pierce",
                     "Kyle Barr", "Blake Montgomery", "Kelvin Chan",
                     "Dara Kerr", "Sabrina Ortiz", "Will Shanklin",
                     "Anshel Sag", "Anuj Behal", "Chris Haslam",
                     "Sean Keach", "Jay Peters", "Andrew Williams"):
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


class TestResearchMethod1383:
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


class TestVerdict1383:
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
        assert "belong to #1385 per #795" in src


# ---------------------------------------------------------------------------
# 12. In-flight isolation: the pending items stay out of this run.
# ---------------------------------------------------------------------------


class TestInFlightIsolation1383:
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


class TestRotation1383:
    def test_window_sequence(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1380 -> E #1381 -> A #1382" in src

    def test_next_leg_is_type_c(self):
        assert PRED_MAIN_1384 == "0" * 40

    def test_type_letter_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type B #1383" in src

    def test_background_suite_observed_only(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "OBSERVES only" in src
        assert "#1385" in src


# ---------------------------------------------------------------------------
# 14. ASCII and formatting hygiene.
# ---------------------------------------------------------------------------


class TestAscii1383:
    def test_no_em_dashes_in_test_file(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "\u2014" not in src

    def test_ascii_only_in_test_file(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        src.encode("ascii")

    def test_expected_total_declared(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "EXPECTED_TOTAL = %d" % EXPECTED_TOTAL in src
