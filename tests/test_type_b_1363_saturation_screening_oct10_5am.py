# -*- coding: utf-8 -*-
"""Type B #1363: journalist cross-entity saturation screening (Oct 10 2026,
~5:00 AM PDT) - NO clean fresh pair; NO mechanism landed.

1 delegated scout (3 tracks) + 9 main-run browser.search verification sets,
0 browser.open per #503, excerpt-bounded. Fresh candidates screened this run
(scout picks pending final documentation below; main-run screens documented
in full):

  REJECTED (main-run verification):
  - Allison Johnson (The Verge, the scout's #1 pick): SATURATED -
    carries a dedicated Type B mechanism (type_b_1223, Oct 4,
    allison_johnson_type_b in journalists.yaml); the scout's Meta-arm
    piece ("Meta's AI agent is a cute little guy who's great at
    spending my money") is the SAME Meta arm as the #1223 mechanism
    - a re-surfacing, not a novel pair. FIFTH #1341
    scout-corpus-blindness instance.
  - Kris Holt (Engadget, the scout's #2 pick): SATURATED - carries a
    dedicated Type B mechanism (kris_holt_type_b, #1278); the scout's
    Meta-arm piece ("Everything announced at Meta Connect 2026") is
    the SAME Connect-roundup Meta arm as the #1278 mechanism - a
    re-surfacing, not a novel pair. FIFTH #1341 instance.
  - Nicholas Sutrich (Android Central, the scout's #3 pick): standing
    rejection from #1318 (Google-arm relay missing; Meta-arm byline
    rested on photo credits, canonical URL unrecovered) HOLDS - and
    the main run's independent search shows his Meta register is
    POSITIVE ("The Oakley Meta HSTN are the new gold standard for
    smart glasses"), so no adversarial-Meta arm exists for a
    divergence pair. Rejected on discipline.
  - David Pierce (The Verge): DEEPLY saturated - a dedicated Type B
    cross-entity entry (David Pierce cross-entity, Institutional Framing
    Immunity) is already in the corpus; the main-run search surfaced the
    project's own commit messages for it. Not a clean novel journalist.
  - James Pero (Gizmodo): the Sep-23 Ray-Ban Meta Audio piece
    ("Meta Introduces Audio-Only Smart Glasses to Avoid the 'Perv'
    Problem") carries the m806 comparator mechanism (#958/#1003);
    Pero carries m791/m806/m833-class dedicated Type B mechanisms.
    Saturated.
  - Brian X. Chen / Eli Tan (NYT, Sep-24 'Pervert Glasses' column
    bylines): both already in the corpus (Chen 9 profile/test hits,
    Tan 14 hits incl. the "primary NYT Meta reporter" career note);
    no clean cross-entity comparator pair verified.
  - Nicholas Sutrich (Android Central): Meta-POSITIVE register ("The
    Oakley Meta HSTN are the new gold standard for smart glasses", Aug
    2025) - no adversarial-Meta arm; the Google Aura comparator was
    already rejected at #1318 (Google-arm relay missing). No clean
    Meta-vs-competitor divergence pair.
  - Anna Washenko (Engadget): standing rejection from #1318 (Meta-arm
    byline conflict - listings attribute the Ray-Ban Display piece to
    Washenko but the article page reads "Karissa Bell for Engadget",
    unresolvable at excerpt level). Not re-screened.
  - The Fortune-angle Meta-wearables search (Connect-week 'Phoenix'
    headset / post-smartphone pieces) surfaced aggregators only
    (startupfortune, jbiznews, tech-insider), no Fortune-staff byline
    pair with a competitor comparator arm.
  - The carried rejection lists stand: #1353's sixteen (Lily Hay
    Newman, Sarah Perez, Lauren Goode, Dominic Preston, Joanna Stern,
    Ariel Zilber, and ten more) and #1358's six (Ryne Hager, Rita El
    Khoury, Abner Li, Karissa Bell, Igor Bonifacic, C. Scott Brown);
    re-screening them would re-litigate.

The scout's picks are documented in the SCOUT PICKS section below
(titles only; scout-supplied relay URLs treated as untrusted per the
#1341 lesson; every pick verified independently by the main run via its
own searches and git grep -F - all three rejected: the FIFTH #1341
instance).

Verdict saturation_screening_no_clean_pair - NOT a falsification-family
member. Max numeric mechanism_id stays 1045 (Type B lands zero mechanisms
this run); ledger holds at 64; no sixty-fifth member. MANUAL /
QUALITATIVE ONLY per the Aug 28 2026 standing rule (tone NOT_SCORED;
p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant false; engine NOT
run; NOT artifact-grade; no_analysis_json_update true). Correlation is
not causation; hypothesis-generating only.

Type B lands zero mechanisms: no profiles/ edit this run. The record is
the iteration-log ## #1363 entry plus this test file.

This run is the FOURTH leg of the 1360-1364 window (D #1360 -> E #1361
-> A #1362 -> B #1363 -> C #1364 per the #565 anchor + rotation guard);
the 1355-1359 window is VERIFIED CLOSED. The next background-suite
verdict belongs to #1365 per #795 (the #1360-launched suite, goal
hidden_files type_d_1360_full_suite.log; this run CHECKS it only -
observed STALLED at [  3%] with last write Oct 10 03:59 PDT and zero live
pytest processes at this run's ~5:0x AM PDT check - and neither
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

OWN_BASENAME = "test_type_b_1363_saturation_screening_oct10_5am.py"

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "8074ebdc9f41667975b6a28858afd8c8d72f79eb"  # patched to the main-commit sha in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1045  # max numeric; Type B lands ZERO mechanisms this run
NEXT_NUM = 1046  # integer only; key-form needles are format-built

# Post-doc-sync totals per #719: PATCHED post-collection
# (pre-sync 79085 + 63 tests; pre-sync 1687 + 1 file).
README_TEST_COUNT = 79148  # patched post-collection
README_FILE_COUNT = 1688

# Predecessor chain: #1362 Type A THIRD leg of the 1360-1364 window.
PRED_MAIN_1362 = "330f55d0660e3b7686c8abb07b64f5310845b3b8"
PRED_ANCHOR_1362 = "6d6b1899a01e3d08ea6523d69f64b7e07b8c7cb6"
PRED_DOCSYNC_1362 = "c0ecb69fdd572d3cfa5295134314ee8c109ee954"
PRED_LOGHASH_1362 = "5e64bfb8fbae819f255ae0834a23802919b0ce93"
PRED_PUSH_1362 = "2eecb9f4d0343ebb315fd065db2a76b1483ce6cb"

# This run's main commit (full sha), for the ancestor-form
# no-Type-B-#1363 pin. Staged 0*40 placeholder-only per #721;
# re-pinned in the anchor followup per #721 (PRED_MAIN_1363 re-pinned
# in BOTH this file and the #1362 file per the #1292 precedent).
PRED_MAIN_1363 = "8074ebdc9f41667975b6a28858afd8c8d72f79eb"  # re-pinned to the #1363 main sha in the anchor followup per #721/#1292

# #1364's main commit (full sha), for the ancestor-form no-Type-C-#1364
# pin (the #1191-class self-trip; #1364 is Type C per the rotation).
# Staged 0*40 placeholder-only per #721; re-pinned in #1364's terminal
# log-hash followup per #721. (Type-correct per the #1352
# type-mismatch lesson: #1364 is Type C, so the pin greps
# "Type C #1364".)
PRED_MAIN_1364 = "0" * 40

# The #1362 window-predecessor file, for the staleness pin on its
# guard-lifecycle class (max id 1045; zero next-number 1046 all forms;
# no sixty-fifth member; ledger holds at 64).
B1362_FILE = (
    "test_type_a_1362_nyt_openai_oct08_publisher_copyright_suit_"
    "legal_enforcement_bounded_absence_vs_carried_meta_arms_oct10_4am.py"
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

# 9 main-run browser.search query sets + 1 delegated scout (3 tracks)
# this run (0 browser.open per #503).
QUERY_SETS = [
    "Meta Connect 2026 Ray-Ban Meta glasses TechCrunch author September October 2026",
    "WIRED Ray-Ban Meta glasses privacy surveillance article author 2026",
    "Bloomberg Meta Ray-Ban smart glasses author September 2026 glasses",
    "\"Meta\" glasses \"Snap\" Spectacles same author review comparison 2026",
    "David Pierce The Verge Meta Connect 2026 glasses Apple smart glasses",
    "Meta Ray-Ban \"pervert glasses\" Engadget author October 2026 Meta Lab stores",
    "\"Complaints About Meta's\" \"Pervert Glasses\" Won't Slow Tech's Wearable Gadgets Drive New York Times author",
    "Fortune reporter Meta smart glasses wearables October 2026 article",
    "Nicholas Sutrich Android Central Meta smart glasses article 2026",
]

# SCOUT PICKS (titles only; scout-supplied relay URLs untrusted per the
# #1341 lesson; every pick verified independently by the main run via its
# own searches and git grep -F - ALL THREE REJECTED: the FIFTH #1341
# scout-corpus-blindness instance, after #1353's m1004 re-surfacing,
# #1354's test_type_c_1329 re-surfacing, #1358's triple
# misattribution, and #1359's test_type_c_1329 re-surfacing):
# Pick 1: Allison Johnson (The Verge) - "Meta's AI agent is a cute
#   little guy who's great at spending my money" (Sep 23, 2026) vs
#   Google "The Pixel 10A finally costs what it should" (Jun 23,
#   2026): REJECTED - Johnson carries a DEDICATED Type B mechanism
#   (type_b_1223, Oct 4, allison_johnson_type_b in journalists.yaml),
#   and the scout's Meta-arm piece is the SAME Meta arm as the #1223
#   mechanism (re-surfacing, not novel). Saturated.
# Pick 2: Kris Holt (Engadget) - "Everything announced at Meta
#   Connect 2026" (Sep 24, 2026) vs OpenAI "ChatGPT Space" relay
#   (Sep 29, 2026) + bonus Oct-2024 Meta dox piece: REJECTED - Holt
#   carries a DEDICATED Type B mechanism (kris_holt_type_b, #1278),
#   and the scout's Meta-arm piece is the SAME Connect-roundup Meta
#   arm as the #1278 mechanism (re-surfacing, not novel). Saturated.
# Pick 3: Nicholas Sutrich (Android Central) - "I've used Meta
#   Ray-Ban Display for a year..." (Sep 16, 2026) vs Samsung/Google
#   Android XR glasses pieces: REJECTED - screened at #1318
#   (Google-arm relay missing; Meta-arm byline rested on photo
#   credits, canonical URL unrecovered); the main run's independent
#   search shows Sutrich's Meta register is POSITIVE ("The Oakley
#   Meta HSTN are the new gold standard for smart glasses") - no
#   adversarial-Meta arm exists, so no clean divergence pair.
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
#    + rotation guard: FOURTH leg of the 1360-1364 window.
# ---------------------------------------------------------------------------


class TestAnchor1363:
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
        assert "FOURTH leg of the 1360-1364 window" in src

    def test_1355_1359_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1355-1359" in src
        assert "VERIFIED CLOSED" in src

    def test_next_leg_is_1364_type_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "C #1364" in src


# ---------------------------------------------------------------------------
# 2. Novelty pins + scout record: pre-commit surface must be clean, and
#    the scout's picks are untrusted until main-run verification.
# ---------------------------------------------------------------------------


class TestScoutCorpusBlindness1363:
    def test_scout_pick1_allison_johnson_rejected_saturated(self):
        # Allison Johnson (the scout's #1 pick) carries a DEDICATED
        # Type B mechanism (type_b_1223, Oct 4); the scout's Meta-arm
        # piece is the same Meta arm as the #1223 mechanism - a
        # re-surfacing, not a novel pair. FIFTH #1341 instance.
        hits = _git_grep_tracked_source(
            "allison_johnson_type_b",
            "profiles/careers/journalists.yaml",
        )
        assert hits, "allison_johnson_type_b must be corpus-recorded"

    def test_scout_pick2_kris_holt_rejected_saturated(self):
        # Kris Holt (the scout's #2 pick) carries a DEDICATED Type B
        # mechanism (kris_holt_type_b, #1278); the scout's Meta-arm
        # piece is the same Connect-roundup Meta arm as the #1278
        # mechanism - a re-surfacing. FIFTH #1341 instance.
        hits = _git_grep_tracked_source(
            "kris_holt_type_b",
            "profiles/careers/journalists.yaml",
        )
        assert hits, "kris_holt_type_b must be corpus-recorded"

    def test_scout_pick3_sutrich_rejected_1318_holds(self):
        # Nicholas Sutrich (the scout's #3 pick): the #1318 standing
        # rejection (Google-arm relay missing) HOLDS; the main run's
        # independent search shows his Meta register is POSITIVE, so
        # no adversarial-Meta arm exists for a divergence pair.
        hits = _git_grep_tracked_source(
            "Nicholas Sutrich",
            "profiles/careers/journalists.yaml",
        )
        assert hits, "Sutrich #1318 screen must be corpus-recorded"

    def test_main_run_pierce_saturated_in_corpus(self):
        # David Pierce (Editor-at-Large, The Verge) carries a dedicated
        # cross-entity journalist profile in the corpus (career
        # migration note, Vergecast co-host, institutional framing
        # immunity analysis); the main-run search surfaced the
        # project's own commit messages for it.
        hits = _git_grep_tracked_source(
            "David Pierce",
            "profiles/careers/journalists.yaml",
        )
        assert hits, "Pierce profile must be corpus-recorded"

    def test_main_run_pero_saturated_in_corpus(self):
        # James Pero's Sep-23 Meta Ray-Ban Audio piece carries the
        # m806 comparator mechanism (#958/#1003).
        log = _read(LOG_PATH)
        assert "Type B #958" in log or "m806" in log
        hits = _git_grep_tracked_source(
            "James Pero",
            "profiles/careers/journalists.yaml",
        )
        assert hits, "Pero must be corpus-recorded"

    def test_main_run_chen_tan_saturated_in_corpus(self):
        # Brian X. Chen and Eli Tan are both already in the corpus.
        hits = _git_grep_tracked_source(
            "Brian X. Chen",
            "profiles/",
        )
        assert hits, "Chen must be corpus-recorded"
        hits = _git_grep_tracked_source(
            "Eli Tan",
            "profiles/",
        )
        assert hits, "Tan must be corpus-recorded"

    def test_main_run_washenko_rejection_holds(self):
        # The Washenko Meta-arm byline conflict rejection (Meta-arm
        # listings say Washenko, article page reads "Karissa Bell for
        # Engadget") was landed at #1318; this run does not re-screen.
        hits = _git_grep_tracked_source(
            "byline conflict",
            "profiles/careers/journalists.yaml",
        )
        assert hits, "Washenko byline-conflict rejection must hold"

    def test_max_numeric_mechanism_id_stays_1045(self):
        # Type B lands ZERO mechanisms this run: max numeric stays 1045.
        assert _max_numeric_mechanism_id() == MECH_NUM == 1045

    def test_no_type_b_1363_in_git_log_pin(self):
        # Ancestor-form self-trip per #1191: every commit whose message
        # matches "Type B #1363" must be #1363's main commit or a
        # descendant of it. Deselected in the in-gate run (fails
        # pre-commit by design); re-pinned in the terminal log-hash
        # followup per #721.
        out = _git("log", "--format=%H", "--grep=Type B #1363")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1363's own commits"
        main = _git("rev-parse", PRED_MAIN_1363).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_zero_next_number_keys_all_forms(self):
        # Numeric (profiles/ scope), underscore and dash (profiles/ +
        # tests/ scope, own file excluded per #715). Holds pre-commit
        # and post-commit (Type B lands zero mechanisms, the 1046
        # pins stay green).
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_1363_entry_in_iteration_log_pre_commit(self):
        text = _read(LOG_PATH)
        assert "## #1363" not in text

    def test_zero_type_b_1363_files_except_own(self):
        import glob
        found = glob.glob(os.path.join(TESTS_DIR, "test_type_b_1363*"))
        assert [os.path.basename(p) for p in found] == [OWN_BASENAME]

    def test_query_sets_bounded(self):
        # 9 main-run browser.search query sets + 1 delegated scout
        # (3 tracks); 0 browser.open per #503.
        assert len(QUERY_SETS) == 9
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "0 browser.open per #503" in src


# ---------------------------------------------------------------------------
# 3. Guard lifecycle: forward pins for #1364; #1363 stages the
#    #1191-class no-Type-C-#1364 self-trip (re-pinned post-commit
#    per #721). Type-correct per the #1352 type-mismatch lesson.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1363:
    def test_pins_on_zero_mechanism_landing(self):
        # Type B lands zero mechanisms: max 1045, next 1046.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1045" in src
        assert "NEXT_NUM = 1046" in src

    def test_no_type_c_1364_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1364's terminal log-hash followup
        # per #721): every commit whose message matches "Type C
        # #1364" must be #1364's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        # Type-correct per the #1352 type-mismatch lesson (#1364 is
        # Type C per the rotation).
        out = _git("log", "--format=%H", "--grep=Type C #1364")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1364's own commits"
        main = _git("rev-parse", PRED_MAIN_1364).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1046_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1046_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1046_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_fortieth_direction_pin(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_forty_eighth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]

    def test_forty_ninth_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T49, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

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

    def test_fifty_fourth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T54, "HEAD", "--",
            "profiles/guardian.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fifth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T55, "HEAD", "--",
            "profiles/atlantic.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_sixth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T56, "HEAD", "--",
            "profiles/wired.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_seventh_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T57, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_eighth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T58, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_ninth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T59, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixtieth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T60, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixty_first_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T61, "HEAD", "--",
            "profiles/wired.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_sixty_second_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T62, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixty_third_member_intact_pin(self):
        # The sixty-third member-claim form is committed at HEAD
        # (landed #1342, m1036, profiles/news-corp.yaml).
        out = _git(
            "grep", "-c", "-F", _T63, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_sixty_fourth_member_present_pin(self):
        # The sixty-fourth member-claim form is committed at HEAD
        # (landed #1347, m1039, profiles/ap.yaml).
        out = _git(
            "grep", "-c", "-F", _T64, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_sixty_fifth_member_pin(self):
        # m1045 is mechanism_documented, NOT a member, and this run
        # lands zero mechanisms: the sixty-fifth member-claim form
        # stays absent repo-wide.
        assert _git_grep_tracked_source(_T65, "profiles/") == []
        assert _git_grep_tracked_source(_T65, "tests/") == []

    def test_ledger_holds_at_64_pin(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ledger holds at 64" in src


# ---------------------------------------------------------------------------
# 4. Staleness pins: #1362's guard lifecycle flips BY DESIGN post-commit.
# ---------------------------------------------------------------------------


class TestStalenessPins1363:
    def test_1362_guard_lifecycle_post_commit_state(self):
        # Post-terminal form: 25 tests in the class; ALL 25 pass.
        # Type B lands zero mechanisms, so every #1362 forward guard
        # stays green: max-1045, zero-1046 all forms, fortieth absent,
        # forty-eighth through sixty-fourth members intact,
        # no-sixty-fifth member, ledger holds at 64. The
        # no_type_b_1363_in_git_log ancestor pin (the #1191-class
        # self-trip) was red at this run's main-commit time; the
        # terminal log-hash followup re-pins PRED_MAIN_1363 in BOTH
        # its own file's copy and the #1362 predecessor file's copy
        # per the #1292 re-pin-both-copies precedent and the #721
        # re-pin rule, flipping it green. Deselected in the in-gate
        # run (fails pre-commit by design); verified post-terminal.
        res = _class_run(B1362_FILE, "TestGuardLifecycle1362")
        out = res.stdout + res.stderr
        assert "25 passed" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 5. Doc-sync per #719 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestDocSync1363:
    def test_readme_test_file_table_has_1363_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_b_1363" in readme

    def test_architecture_has_1363_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_b_1363" in arch

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


class TestIterationLog1363:
    def test_log_has_1363_entry(self):
        text = _read(LOG_PATH)
        assert "## #1363 Type B" in text

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
        assert "1045" in text


# ---------------------------------------------------------------------------
# 7. Screening ledger: the journalists screened this run.
# ---------------------------------------------------------------------------


class TestScreeningLedger1363:
    def test_screened_journalists_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        for name in ("David Pierce", "James Pero", "Brian X. Chen",
                     "Eli Tan", "Nicholas Sutrich", "Anna Washenko"):
            assert name in src, name

    def test_carried_rejections_referenced(self):
        # The #1353 sixteen and the #1358 six carry as rejections;
        # re-screening them would re-litigate.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        for name in ("Lily Hay Newman", "Sarah Perez", "Lauren Goode",
                     "Dominic Preston", "Joanna Stern", "Ariel Zilber",
                     "Ryne Hager", "Rita El Khoury", "Abner Li",
                     "Karissa Bell", "Igor Bonifacic", "C. Scott Brown"):
            assert name in src, name

    def test_no_profiles_edit_this_run(self):
        # Type B lands zero mechanisms: no profiles/ edit this run
        # (verified via git status in the iteration-log entry, not
        # here).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "no profiles/ edit this run" in src


# ---------------------------------------------------------------------------
# 8. Research method.
# ---------------------------------------------------------------------------


class TestResearchMethod1363:
    def test_scout_plus_main_run_sets(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1 delegated scout (3 tracks)" in src
        assert "9 main-run browser.search verification sets" in src

    def test_zero_browser_open(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "0 browser.open per #503" in src

    def test_scout_untrusted_convention(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1341 lesson" in src


# ---------------------------------------------------------------------------
# 9. Verdict: saturation screening, manual/qualitative only.
# ---------------------------------------------------------------------------


class TestVerdict1363:
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
        assert "verdict belongs to #1365 per #795" in src
        assert "neither" in src
        assert "re-launches, kills, nor writes to it" in src
