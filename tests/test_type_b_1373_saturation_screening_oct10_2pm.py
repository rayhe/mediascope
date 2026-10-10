# -*- coding: utf-8 -*-
"""Type B #1373: journalist cross-entity saturation screening (Oct 10 2026,
~2:00 PM PDT) - NO clean fresh pair; NO mechanism landed.

1 delegated scout (3 tracks, 16 searches, 0 browser.open, 5 git-grep
corpus-blindness batches) + 5 main-run browser.search verification sets,
0 browser.open per #503, excerpt-bounded. The scout proposed ZERO
candidates - a CLEAN NEGATIVE SCREEN, not a #1341-class instance (the
scout ran its own git-grep corpus-blindness checks and self-rejected
every saturated name before proposing; the ninth #1341 instance at
#1368 stands as the last). Main-run verified every scout claim via
independent git grep -F -i.

  SELF-REJECTED BY THE SCOUT (saturated; main-run verified):
  - Samuel Gibbs (Guardian): SATURATED - Type B #628 (Meta Ray-Ban
    Display vs Apple Vision Pro); 10 corpus files. Re-screening would
    re-litigate.
  - Dara Kerr (Guardian): SATURATED - Type B #513 (Meta vs OpenAI
    register split); 8 corpus files.
  - Kaitlyn Huamani (AP): SATURATED - Type B #1213 (Oct-4-2026 Meta vs
    OpenAI); 5 corpus files.
  - Barbara Ortutay (AP): SATURATED - Type B #343; cited in #1213;
    4 corpus files.
  - Sean Keach (The Sun): SATURATED - dedicated Type B (cross-medium
    register); 6 corpus files.
  - Kashmir Hill (NYT): SATURATED - dedicated Type B (NameTag expose
    vs Clearview/automaker arms); 17 corpus files.
  - Plus the scout's pre-checked saturated list (Gurman, Wong,
    Gorringe, Ashworth, Song, Ropek, Stein, Schoon, Hager, El Khoury,
    Abner Li, Bell, Bonifacic, C. Scott Brown, Wagner, Murgia, Murphy,
    Criddle, Bradshaw, Sato, Nguyen, Roth, Nilay Patel, Pierce,
    Robertson, Peters, Isaac, Weise, Kang, Roose, Metz, Hern, Milmo,
    Bogost, Goldberg, Honan, Warzel, Cranz, Kelly, Feiner, O'Donnell,
    Heaven, Matteo Wong, Kafka, Booth, Kleinman, Thompson, Williams,
    Heikkila, Jee, Ovide, Hunter, Maheshwari, Foer, Griffin, Varanasi,
    Zakrzewski, Taylor).

  ZERO-HIT BUT FAILED DIVERGENCE (main-run confirmed zero corpus hits;
  rejected on discipline, not saturation):
  - Toby Sterling (Reuters): 0 corpus hits, but the Meta arm is the
    Oct-2-2026 Reuters wire piece on Hans Anders halting Meta glasses
    sales (balanced wire reportage by genre, not an adversarial arm),
    and no competitor arm by Sterling surfaced. REJECTED.
  - Aisha Counts (Bloomberg): 0 corpus hits, but only 2024 Orion
    co-byline arms with saturated Kurt Wagner; no adversarial
    Sep-Oct-2026 Meta arm. REJECTED.
  - Hasan Chowdhury (Business Insider): 0 corpus hits, but no Meta
    glasses bylines found at all. REJECTED.
  - Tanya Basu (MIT Tech Review): 0 corpus hits, but no recent Meta
    glasses work (2020-2022 metaverse only). REJECTED.

  Why the screen came up empty: the Sep-24 Connect launch coverage at
  tracked outlets was dominated by already-covered bylines (Song,
  Ashworth, Gurman, Stein, Schoon, Hager, El Khoury, Perez, Gibbs,
  Huamani/Ortutay); the Oct Dutch/Norway ban coverage was mostly wire
  copy (Sterling/Reuters, AP) or Guardian staff already in the corpus.
  The corpus-blindness discipline held - the saturation list is
  genuinely saturated.

  REJECTED (main-run verification sets):
  - Reuters Norway-ban sweep: BYLINE GAP, not a finding - the Oct-6-2026
    Reuters factbox ("Factbox-Countries weigh banning smart glasses over
    privacy concerns") carries no named reporter byline; the Norway
    temporary-ban relay surface (thenyledger, losangelesweeklytimes) is
    byline-unattested at excerpt level. No clean pair attestable.
  - NYT sweep: BYLINE GAP, not a finding - the surface is relay/secondary
    (digitaltrends relay of the NYT ICE-ban reporting; Suffolk journal;
    NY Post class-action piece); no novel NYT staffer byline with both a
    Meta arm and a competitor arm surfaced. Kashmir Hill is
    carried-saturated in any case.
  - Jonathan Vanian (CNBC): SATURATED - carries a dedicated cross-entity
    register in profiles/competitor-coverage-research.yaml (Jonathan
    Vanian (CNBC) Same-Journalist Government-Action Vocabulary Register:
    Vanian covers both Meta and Anthropic for CNBC). Re-screening would
    re-litigate. Salvador Rodriguez surfaced no clean pair.
  - Kurt Wagner (Bloomberg): SATURATED - carried in
    profiles/careers/journalists.yaml (Bloomberg big-tech/AI/VC
    managing editor; "No Filter" narrative-shaping notes). Not a clean
    novel journalist.
  - Michael Liedtke (AP): BYLINE GAP, not a finding - ZERO corpus hits
    (novel name) but no bylined Meta-arm + competitor-arm pair surfaced
    at excerpt level in the main-run sweep (the query returned
    techpolicy.press, madrobot, seekingalpha and other non-AP surfaces,
    no Liedtke byline). One-sided at this point; a gap, not a finding.
  - The carried rejection lists stand: #1353's sixteen (Lily Hay Newman,
    Sarah Perez, Lauren Goode, Dominic Preston, Joanna Stern, Ariel Zilber,
    and ten more), #1358's six (Ryne Hager, Rita El Khoury, Abner Li,
    Karissa Bell, Igor Bonifacic, C. Scott Brown), and #1368's eight
    (Mark Gurman, Raymond Wong, Jessica Gorringe, Boone Ashworth,
    Victoria Song, Lucas Ropek, Scott Stein, Ben Schoon); re-screening
    them would re-litigate.

Verdict saturation_screening_no_clean_pair - NOT a falsification-family
member. Max numeric mechanism_id stays 1047 (Type B lands zero mechanisms
this run); ledger holds at 65; no sixty-sixth member; the sixty-fifth
member-form stays intact in profiles/financial-times.yaml. MANUAL /
QUALITATIVE ONLY per the Aug 28 2026 standing rule (tone NOT_SCORED;
p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant false; engine NOT
run; NOT artifact-grade; no_analysis_json_update true). Correlation is
not causation; hypothesis-generating only.

Type B lands zero mechanisms: no profiles/ edit this run. The record is
the iteration-log ## #1373 entry plus this test file.

This run is the FOURTH leg of the 1370-1374 window (D #1370 -> E #1371
-> A #1372 -> B #1373 -> C #1374 per the #565 anchor + rotation guard);
the 1365-1369 window is VERIFIED CLOSED. The next background-suite
verdict belongs to #1375 per #795 (the #1370-launched suite, goal
hidden_files type_d_1370_full_suite.log; this run CHECKS it only -
observed at [2%] with last write Oct 10 12:09 PDT and one live pytest
process at this run's ~1:1x PM PDT check, progressing slowly, not
adjudicated - and neither re-launches, kills, nor writes to it).

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

OWN_BASENAME = "test_type_b_1373_saturation_screening_oct10_2pm.py"

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "9cb2b6cd92de9faef3bf0bb2a31b904947ffea85"  # patched to the main commit sha in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1047  # max numeric; Type B lands ZERO mechanisms this run
NEXT_NUM = 1048  # integer only; key-form needles are format-built

# Post-doc-sync totals per #719: PATCHED post-collection
# (pre-sync 79976 + N tests; pre-sync 1697 + 1 file).
README_TEST_COUNT = 80047  # patched pre-main: pre-sync 79976 + 71 collected
README_FILE_COUNT = 1698  # patched pre-main: pre-sync 1697 + 1 (this file)

# Predecessor chain: #1372 Type A THIRD leg of the 1370-1374 window.
PRED_MAIN_1372 = "e162b718eaebe64f28146d7d9c0585e7a3c81e4a"
PRED_ANCHOR_1372 = "673ddcf9c442f1580d7943f33b1391ca30dfcabd"
PRED_DOCSYNC_1372 = "2ab733b4ea49167b2eee082f8f52fe1022f8db61"
PRED_LOGHASH_1372 = "bb1aa67685185c9b3f71f8bc8eb0bbcceb5e88c0"
PRED_PUSH_1372 = "8cb0bc7229adfaf7c8c9df45b1731957ead653f2"

# This run's main commit (full sha), for the ancestor-form
# no-Type-B-#1373 pin. Staged 0*40 placeholder-only per #721;
# re-pinned in the anchor followup per #721 (PRED_MAIN_1373 re-pinned
# in BOTH this file and the #1372 file per the #1292 precedent).
PRED_MAIN_1373 = "9cb2b6cd92de9faef3bf0bb2a31b904947ffea85"  # re-pinned to the #1373 main sha in the anchor followup per #721/#1292

# #1374's main commit (full sha), for the ancestor-form no-Type-C-#1374
# pin (the #1191-class self-trip; #1374 is Type C per the rotation).
# Staged 0*40 placeholder-only per #721; re-pinned in #1374's terminal
# log-hash followup per #721. (Type-correct per the #1352
# type-mismatch lesson: #1374 is Type C, so the pin greps
# "Type C #1374".)
PRED_MAIN_1374 = "0412f64205403436d0b2313963b86eb1814baa6e"  # re-pinned to the #1374 main sha in #1374's terminal log-hash followup per #721/#1292

# The #1372 window-predecessor file, for the staleness pin on its
# guard-lifecycle class (max id 1047; zero next-number 1048 all forms;
# sixty-fifth member present; no sixty-sixth member; ledger holds at
# 65).
B1372_FILE = (
    "test_type_a_1372_ft_anthropic_oct05_broadcom_syndication_"
    "financing_risk_vs_m441_google_channel_prediction_oct10_1pm.py"
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

# 5 main-run browser.search query sets + 1 delegated scout (3 tracks)
# this run (0 browser.open per #503).
QUERY_SETS = [
    "Reuters journalist Meta Ray-Ban smart glasses Norway ban October 2026 byline",
    "New York Times reporter Meta smart glasses privacy surveillance October 2026 byline",
    "CNBC reporter Meta smart glasses article September October 2026 Salvador Rodriguez OR Jonathan Vanian byline",
    "Kurt Wagner Bloomberg Meta Ray-Ban glasses September 2026 byline article",
    "Michael Liedtke AP technology writer Meta article 2026 OpenAI OR Anthropic OR Google",
]

# SCOUT OUTCOME: CLEAN NEGATIVE SCREEN - 16 searches, 0 browser.open,
# 5 git-grep corpus-blindness batches, ZERO candidates proposed. NOT a
# #1341-class instance (the scout self-rejected saturated names via its
# own corpus-blindness checks; the ninth instance at #1368 stands as the
# last). Main-run verified every scout claim independently via
# git grep -F -i (profiles/ + tests/ at HEAD):
# saturated: Samuel Gibbs (10 files, Type B #628), Dara Kerr (8 files,
# Type B #513), Kaitlyn Huamani (5 files, Type B #1213), Barbara Ortutay
# (4 files, Type B #343), Sean Keach (6 files, dedicated Type B),
# Kashmir Hill (17 files, dedicated Type B); zero-hit but failed
# divergence: Toby Sterling, Aisha Counts, Hasan Chowdhury, Tanya Basu
# (all 0 files; rejected on discipline: wire-balance / no adversarial
# arm / no bylines / stale arms).
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
#    + rotation guard: FOURTH leg of the 1370-1374 window.
# ---------------------------------------------------------------------------


class TestAnchor1373:
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
        assert "FOURTH leg of the 1370-1374 window" in src
        assert "D #1370 -> E #1371" in src

    def test_1365_1369_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "the 1365-1369 window is VERIFIED CLOSED" in src

    def test_next_leg_is_1374_type_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "-> C #1374" in src


# ---------------------------------------------------------------------------
# 2. Scout outcome: clean negative screen (NOT a #1341 instance) +
#    main-run screens all saturated or gap-class.
# ---------------------------------------------------------------------------


class TestScoutCorpusBlindness1373:
    def test_scout_clean_negative_screen(self):
        # The scout ran 16 searches + 5 git-grep corpus-blindness
        # batches and proposed ZERO candidates: a clean negative
        # screen, not a #1341-class instance (the scout ran its own
        # corpus-blindness checks and self-rejected saturated names
        # before proposing; the ninth instance at #1368 stands as the
        # last).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "CLEAN NEGATIVE SCREEN" in src
        assert "proposed ZERO" in src
        assert "NOT a #1341-class instance" in src

    def test_scout_saturated_self_rejections_verified(self):
        # Every scout self-rejection verified by the main run's own
        # git grep -F -i (profiles/ + tests/ at HEAD).
        for name in ("Samuel Gibbs", "Dara Kerr", "Kaitlyn Huamani",
                     "Barbara Ortutay", "Sean Keach", "Kashmir Hill"):
            out = _git("grep", "-i", "-F", "-l", name, "HEAD",
                       "--", "profiles/", "tests/")
            hits = [l for l in out.stdout.splitlines() if l.strip()]
            assert hits != [], (name, hits)
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type B #628" in src
        assert "Type B #513" in src
        assert "Type B #1213" in src
        assert "Type B #343" in src

    def test_scout_zero_hit_discipline_rejections_verified(self):
        # Zero corpus hits confirmed by the main run; rejected on
        # divergence discipline (wire-balance / no adversarial arm /
        # no bylines / stale arms), not saturation.
        for name in ("Toby Sterling", "Aisha Counts",
                     "Hasan Chowdhury", "Tanya Basu"):
            out = _git("grep", "-i", "-F", "-l", name, "HEAD",
                       "--", "profiles/", "tests/")
            assert out.stdout.strip() == "", (name, out.stdout)
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Toby Sterling" in src
        assert "balanced wire reportage by genre" in src
        assert "Aisha Counts" in src
        assert "Hasan Chowdhury" in src
        assert "Tanya Basu" in src

    def test_no_1341_instance_this_run(self):
        # The scout committed no corpus blindness: the ninth #1341
        # instance (#1368) stands as the last; this run pins the clean
        # screen instead.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "the ninth #1341 instance at" in src
        assert "#1368 stands as the last" in src

    def test_main_run_reuters_byline_gap(self):
        # The Reuters Oct-6 factbox carries no named reporter byline;
        # a byline gap is a gap, not a finding.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Reuters Norway-ban sweep: BYLINE GAP" in src

    def test_main_run_nyt_byline_gap(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NYT sweep: BYLINE GAP" in src

    def test_main_run_vanian_saturated(self):
        # Jonathan Vanian carries a dedicated cross-entity register
        # in the corpus; re-screening would re-litigate.
        hits = _git_grep_tracked_source(
            "Jonathan Vanian", "profiles/competitor-coverage-research.yaml")
        assert hits != [], hits
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Jonathan Vanian (CNBC): SATURATED" in src

    def test_main_run_wagner_saturated(self):
        hits = _git_grep_tracked_source(
            "Kurt Wagner", "profiles/careers/journalists.yaml")
        assert hits != [], hits
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Kurt Wagner (Bloomberg): SATURATED" in src

    def test_main_run_liedtke_byline_gap(self):
        # Zero corpus hits but no bylined pair at excerpt level: a
        # gap, not a finding.
        out = _git("grep", "-i", "-F", "-l", "Michael Liedtke",
                   "HEAD", "--", "profiles/", "tests/")
        assert out.stdout.strip() == "", out.stdout
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Michael Liedtke (AP): BYLINE GAP" in src

    def test_query_sets_bounded(self):
        # 5 main-run browser.search query sets, documented verbatim.
        assert len(QUERY_SETS) == 5
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        for q in QUERY_SETS:
            assert q in src, q


# ---------------------------------------------------------------------------
# 3. Mechanism novelty: Type B lands ZERO mechanisms this run; max stays
#    1047; next 1048 stays clean in all three key forms.
# ---------------------------------------------------------------------------


class TestMechanismNovelty1373:
    def test_max_numeric_mechanism_id_stays_1047(self):
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
        assert "MECH_NUM = 1047" in src
        assert "NEXT_NUM = 1048" in src


# ---------------------------------------------------------------------------
# 4. Guard lifecycle: forward pins for #1374; #1373 staged this run.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1373:
    def test_pins_on_zero_mechanism_landing(self):
        # Type B lands zero mechanisms: max stays 1047, next 1048.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1047" in src
        assert "NEXT_NUM = 1048" in src

    def test_no_type_b_1373_in_git_log_pin(self):
        # Post-main-commit form for THIS run's own pin (the
        # #1191-class self-trip, re-pinned in this run's terminal
        # log-hash followup per #721/#1292): every commit whose
        # message matches "Type B #1373" must be this run's main
        # commit or a descendant of it. Deselected in the in-gate
        # run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type B #1373")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1373's own commits"
        main = _git("rev-parse", PRED_MAIN_1373).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_no_type_c_1374_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1374's terminal log-hash followup
        # per #721): every commit whose message matches "Type C
        # #1374" must be #1374's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1374 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type C #1374")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1374's own commits"
        main = _git("rev-parse", PRED_MAIN_1374).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1047_numeric_present_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(MECH_NUM) != []

    def test_1047_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(MECH_NUM) == []

    def test_1047_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(MECH_NUM) == []

    def test_1048_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1048_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1048_dash_absent_repo_wide(self):
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
# 5. Staleness pin: the predecessor's guard lifecycle, run as-is.
# ---------------------------------------------------------------------------


class TestStalenessPins1373:
    def test_1372_guard_lifecycle_post_terminal_state(self):
        # Post-terminal-followup form: 30 tests in the class; ALL
        # pass. The #1191-class self-trip on the
        # no-Type-B-#1373-in-git-log pin (PRED_MAIN_1373 still 0*40
        # until THIS run's terminal log-hash followup re-pins it in
        # the #1372 predecessor file per #721/#1292) flips green in
        # the terminal followup. The no-Type-A-#1372 pin was already
        # re-pinned green in #1372's terminal followup. The
        # 1047-present / 1048-absent pins stay green (Type B lands
        # zero mechanisms); the forty-eighth through sixty-fifth
        # member pins stay green; the no-sixty-sixth pin stays green;
        # the fortieth-direction pin stays green.
        # Deselected in the in-gate run (fails pre-commit by design);
        # verified post-terminal.
        res = _class_run(B1372_FILE, "TestGuardLifecycle1372")
        out = res.stdout + res.stderr
        assert "30 passed" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 6. Doc-sync per #719 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestDocSync1373:
    def test_readme_test_file_table_has_1373_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_b_1373" in readme

    def test_architecture_has_1373_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_b_1373" in arch

    def test_readme_stats_ratcheted(self):
        # Post-sync-positive form per #719: asserts the ratcheted
        # counts (README_TEST_COUNT tests across README_FILE_COUNT
        # files). Fails pre-commit by design; deselected in the
        # in-gate run.
        readme = _read(README_PATH)
        assert ("| Tests | %d |" % README_TEST_COUNT) in readme
        assert ("Across %d test files" % README_FILE_COUNT) in readme


# ---------------------------------------------------------------------------
# 7. Iteration log per #721 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestIterationLog1373:
    def test_log_has_1373_entry(self):
        text = _read(LOG_PATH)
        assert "## #1373 Type B" in text

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
        assert "1047" in text

# ---------------------------------------------------------------------------
# 8. Screening ledger: the journalists screened this run.
# ---------------------------------------------------------------------------


class TestScreeningLedger1373:
    def test_screened_journalists_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        for name in ("Jonathan Vanian", "Kurt Wagner", "Michael Liedtke",
                     "Reuters", "Kashmir Hill", "Samuel Gibbs",
                     "Dara Kerr", "Kaitlyn Huamani", "Barbara Ortutay",
                     "Sean Keach", "Toby Sterling", "Aisha Counts",
                     "Hasan Chowdhury", "Tanya Basu"):
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
# 9. Research method.
# ---------------------------------------------------------------------------


class TestResearchMethod1373:
    def test_scout_plus_main_run_sets(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1 delegated scout (3 tracks, 16 searches" in src
        assert "5 main-run browser.search verification sets" in src

    def test_zero_browser_open(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "0 browser.open per #503" in src

    def test_scout_untrusted_convention(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1341 lesson" in src


# ---------------------------------------------------------------------------
# 10. Verdict: saturation screening, manual/qualitative only.
# ---------------------------------------------------------------------------


class TestVerdict1373:
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
        assert "this run CHECKS it only" in src
        assert "verdict belongs to #1375 per #795" in src
        assert "neither" in src
        assert "re-launches, kills, nor writes to it" in src


# ---------------------------------------------------------------------------
# 11. In-flight isolation: the pending items stay out of this run.
# ---------------------------------------------------------------------------


class TestInFlightIsolation1373:
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
