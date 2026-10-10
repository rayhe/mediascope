# -*- coding: utf-8 -*-
"""Type B #1368: journalist cross-entity saturation screening (Oct 10 2026,
~10:00 AM PDT) - NO clean fresh pair; NO mechanism landed.

1 delegated scout (3 tracks) + 5 main-run browser.search verification sets,
0 browser.open per #503, excerpt-bounded. Scout picks ALL rejected; main-run
screens ALL saturated or gap-class. The scout's three headline picks are the
SIXTH #1341-class scout-corpus-blindness instance (the scout proposed as
"new" journalists already carrying dedicated Type B mechanisms or full
cross-entity mechanisms):

  REJECTED (scout picks, main-run verified):
  - Mark Gurman (Bloomberg, Power On): SATURATED - carries a dedicated Type B
    block (type_b_593_mark_gurman_access_journalism_register_asymmetry in
    profiles/careers/journalists.yaml). The scout's "NEW candidate, strongest
    find" (Sep 2026 Meta HUD-glasses reporting vs Sep-27 Power On Apple N50
    privacy-framed arm) re-surfaces a journalist the corpus already covers at
    the within-writer cross-entity unit - re-screening would re-litigate.
    SIXTH #1341 instance.
  - Raymond Wong (Gizmodo): SATURATED - carries a dedicated Type B test file
    (test_type_b_698_raymond_wong_duo_hands_on_vs_ray_ban_gen2_review_
    register_constancy_sep12_8am.py). The scout's "genuinely new name" claim
    fails git grep; his Meta-vs-Apple register comparison already landed.
    Sixth-instance sub-case.
  - Jessica Gorringe (Trusted Reviews): SATURATED - carries a full
    cross-entity constancy mechanism in profiles/competitor-coverage-
    research.yaml (entity-neutral adversarial privacy register on BOTH Meta
    and Apple; the entity-neutral control case). The scout's "partial lead"
    framing understates a fully documented mechanism. Sixth-instance
    sub-case.
  - TechCrunch Sep-23, 2026 pieces (camera-free AI glasses; Muse agent
    rundown): BYLINE GAP, not a finding - bylines did not surface at excerpt
    level; the corpus TC wearables trio (Lucas Ropek, Sarah Perez,
    Anthony Ha) is already saturated (Ropek dedicated tests Aug 24/26;
    #274). No clean pair attestable.
  - Fortune contractor/class-action reporting: BYLINE GAP, not a finding -
    the staffer byline did not surface in any search result. No clean pair
    attestable.
  - Ben Schoon (9to5Google): REJECTED - Meta arm ("Meta launches audio-only
    glasses and Gen 3 Ray-Ban with slimmer designs", Sep 24 2026) is
    neutral-to-positive, so no adversarial-Meta arm exists for a divergence
    pair; outlet is Google-focused by design (publication-level confound).

  REJECTED (main-run verification sets):
  - Boone Ashworth (WIRED): DEEPLY saturated - mechanisms #70, #431, #998,
    #678; his Oct-4-2026 Gen-3 review ("People might think you're a creep")
    re-surfaces the same register. Not a clean novel journalist.
  - Victoria Song (The Verge): SATURATED - carries a dedicated Type B
    mechanism (m827, #993). Confirmed live by the corpus itself (search
    surfaced the project's own commit).
  - Lucas Ropek (TechCrunch): SATURATED - dedicated tests Aug 24/26; the
    Sep-25 Connect-week Meta piece bylines to him via relay. Not clean.
  - Scott Stein (CNET): SATURATED - Type B #588 (register constancy,
    mechanism #106-adjacent). Not clean.
  - The carried rejection lists stand: #1353's sixteen (Lily Hay Newman,
    Sarah Perez, Lauren Goode, Dominic Preston, Joanna Stern, Ariel Zilber,
    and ten more) and #1358's six (Ryne Hager, Rita El Khoury, Abner Li,
    Karissa Bell, Igor Bonifacic, C. Scott Brown); re-screening them would
    re-litigate.

Verdict saturation_screening_no_clean_pair - NOT a falsification-family
member. Max numeric mechanism_id stays 1046 (Type B lands zero mechanisms
this run); ledger holds at 64; no sixty-fifth member. MANUAL /
QUALITATIVE ONLY per the Aug 28 2026 standing rule (tone NOT_SCORED;
p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant false; engine NOT
run; NOT artifact-grade; no_analysis_json_update true). Correlation is
not causation; hypothesis-generating only.

Type B lands zero mechanisms: no profiles/ edit this run. The record is
the iteration-log ## #1368 entry plus this test file.

This run is the FOURTH leg of the 1365-1369 window (D #1365 -> E #1366
-> A #1367 -> B #1368 -> C #1369 per the #565 anchor + rotation guard);
the 1360-1364 window is VERIFIED CLOSED. The next background-suite
verdict belongs to #1370 per #795 (the #1365-launched suite, goal
hidden_files type_d_1365_full_suite.log; this run CHECKS it only -
observed STALLED at [  1%] with last write Oct 10 07:59 PDT and zero live
pytest processes at this run's ~10:0x AM PDT check - and neither
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

OWN_BASENAME = "test_type_b_1368_saturation_screening_oct10_10am.py"

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "e994f9cbae3754e7564dbfff878d965e6dc945cf"  # patched to the main-commit sha in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1046  # max numeric; Type B lands ZERO mechanisms this run
NEXT_NUM = 1047  # integer only; key-form needles are format-built

# Post-doc-sync totals per #719: PATCHED post-collection
# (pre-sync 79521 + N tests; pre-sync 1692 + 1 file).
README_TEST_COUNT = 79590  # patched pre-main: pre-sync 79521 + 69 collected
README_FILE_COUNT = 1693  # patched pre-main: pre-sync 1692 + 1 (this file)

# Predecessor chain: #1367 Type A THIRD leg of the 1365-1369 window.
PRED_MAIN_1367 = "14901df4fb5297b912f752909e1180997635f5d0"
PRED_ANCHOR_1367 = "230bc8f9"
PRED_DOCSYNC_1367 = "9ba68e5a"
PRED_LOGHASH_1367 = "da849d6e"

# This run's main commit (full sha), for the ancestor-form
# no-Type-B-#1368 pin. Staged 0*40 placeholder-only per #721;
# re-pinned in the anchor followup per #721 (PRED_MAIN_1368 re-pinned
# in BOTH this file and the #1367 file per the #1292 precedent).
PRED_MAIN_1368 = "e994f9cbae3754e7564dbfff878d965e6dc945cf"  # re-pinned to the #1368 main sha in the anchor followup per #721/#1292

# #1369's main commit (full sha), for the ancestor-form no-Type-C-#1369
# pin (the #1191-class self-trip; #1369 is Type C per the rotation).
# Staged 0*40 placeholder-only per #721; re-pinned in #1369's terminal
# log-hash followup per #721. (Type-correct per the #1352
# type-mismatch lesson: #1369 is Type C, so the pin greps
# "Type C #1369".)
PRED_MAIN_1369 = "0" * 40  # re-pinned to the #1369 main sha in #1369's terminal log-hash followup per #721/#1292

# The #1367 window-predecessor file, for the staleness pin on its
# guard-lifecycle class (max id 1046; zero next-number 1047 all forms;
# no sixty-fifth member; ledger holds at 64).
B1367_FILE = (
    "test_type_a_1367_ft_openai_oct05_chatgpt_image_ads_"
    "ad_monetization_selection_vs_carried_meta_arms_oct10_9am.py"
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

# 5 main-run browser.search query sets + 1 delegated scout (3 tracks)
# this run (0 browser.open per #503).
QUERY_SETS = [
    "WIRED writer Ray-Ban Meta glasses privacy review September 2026 byline",
    "Victoria Song The Verge Meta Ray-Ban smart glasses article 2026",
    "Boone Ashworth WIRED smart glasses review 2026",
    "TechCrunch reporter Meta Connect 2026 smart glasses article September 2026",
    "Mark Gurman Power On Meta smart glasses Apple glasses 2026",
]

# SCOUT PICKS (titles only; scout-supplied claims untrusted per the
# #1341 lesson; every pick verified independently by the main run via its
# own searches and git grep -F - ALL REJECTED: the SIXTH #1341
# scout-corpus-blindness instance, after #1353's m1004 re-surfacing,
# #1354's test_type_c_1329 re-surfacing, #1358's triple misattribution,
# #1359's test_type_c_1329 re-surfacing, and #1363's FIFTH instance):
# Pick 1: Mark Gurman (Bloomberg, Power On) - Meta HUD-glasses/Audio
#   reporting (Sep 2026) vs Sep-27 Power On Apple N50 privacy-framed arm:
#   REJECTED - carries a DEDICATED Type B block
#   (type_b_593_mark_gurman_access_journalism_register_asymmetry in
#   profiles/careers/journalists.yaml). The scout's "NEW candidate,
#   strongest find" is a re-surfacing; re-screening would re-litigate.
# Pick 2: Raymond Wong (Gizmodo) - "Ray-Ban Meta (Gen 3) Review:
#   Technically an Upgrade" (Oct 2026) vs Jun-2025 Vision Pro "Spatial
#   Personas" arm: REJECTED - carries a DEDICATED Type B test file
#   (test_type_b_698_raymond_wong_duo_hands_on_vs_ray_ban_gen2_review_
#   register_constancy_sep12_8am.py). The scout's "genuinely new name"
#   claim fails git grep -F.
# Pick 3: Jessica Gorringe (Trusted Reviews) - Gen-3 review (Sep 2026,
#   Meta arm only, no competitor arm found): REJECTED - carries a FULL
#   cross-entity constancy mechanism in profiles/competitor-coverage-
#   research.yaml (entity-neutral adversarial privacy register on BOTH
#   Meta and Apple; the entity-neutral control case). One-sided arm
#   regardless.
# Pick 4: TechCrunch Sep-23, 2026 pieces (camera-free AI glasses; Muse
#   agent rundown): BYLINE GAP - bylines unattested at excerpt level;
#   the corpus TC wearables trio (Lucas Ropek, Sarah Perez, Anthony Ha)
#   is already saturated. Not a finding.
# Pick 5: Fortune contractor/class-action reporting: BYLINE GAP - staffer
#   byline did not surface in any search result. Not a finding.
# Pick 6: Ben Schoon (9to5Google) - REJECTED - Meta arm is
#   neutral-to-positive, so no adversarial-Meta arm exists for a
#   divergence pair; outlet is Google-focused by design
#   (publication-level confound).
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
#    + rotation guard: FOURTH leg of the 1365-1369 window.
# ---------------------------------------------------------------------------


class TestAnchor1368:
    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit form per #565: ANCHORED_SHA is 0*40 until the
        # anchor followup patches it to the main-commit sha. Fails BY
        # DESIGN post-anchor.
        assert ANCHORED_SHA == "0" * 40

    def test_anchor_sha_patched_to_main_commit(self):
        # Post-anchor form per #565: ANCHORED_SHA equals the main
        # commit sha. Deselected in the in-gate run (fails pre-commit
        # by design); flipped in the anchor followup.
        assert ANCHORED_SHA == _git("rev-parse", "HEAD").stdout.strip()
        assert ANCHORED_SHA != "0" * 40

    def test_anchor_sha_format(self):
        # Either the placeholder or a full 40-hex sha.
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA) or \
            ANCHORED_SHA == "0" * 40

    def test_anchor_duality_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Anchor convention per #565" in src

    def test_fourth_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FOURTH leg of the 1365-1369 window" in src
        assert "D #1365 -> E #1366" in src

    def test_1360_1364_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "the 1360-1364 window is VERIFIED CLOSED" in src

    def test_next_leg_is_1369_type_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "-> C #1369" in src


# ---------------------------------------------------------------------------
# 2. Scout-corpus blindness: every scout pick rejected on corpus grounds.
# ---------------------------------------------------------------------------


class TestScoutCorpusBlindness1368:
    def test_scout_pick1_mark_gurman_rejected_saturated(self):
        # The scout's "NEW candidate, strongest find" carries a DEDICATED
        # Type B block in the corpus; re-screening would re-litigate.
        hits = _git_grep_tracked_source(
            "type_b_593_mark_gurman", "profiles/careers/journalists.yaml")
        assert hits != [], hits
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "type_b_593_mark_gurman_access_journalism_register_asymmetry" \
            in src

    def test_scout_pick2_raymond_wong_rejected_saturated(self):
        # The scout's "genuinely new name" carries a DEDICATED Type B
        # test file in the corpus; the claim fails git grep -F.
        out = _git("grep", "-F", "-l", "test_type_b_698_raymond_wong",
                   "HEAD", "--", "tests/")
        assert out.stdout.strip() != "", out.stdout
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "test_type_b_698_raymond_wong" in src

    def test_scout_pick3_jessica_gorringe_rejected_saturated(self):
        # The scout's "partial lead" is a FULL cross-entity constancy
        # mechanism in the corpus (entity-neutral control case).
        out = _git("grep", "-F", "-l", "Jessica Gorringe",
                   "HEAD", "--", "profiles/competitor-coverage-research.yaml")
        assert out.stdout.strip() != "", out.stdout
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "entity-neutral control case" in src

    def test_scout_pick4_techcrunch_byline_gap_not_finding(self):
        # A byline gap is a gap, not a finding: no clean pair
        # attestable at excerpt level.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "BYLINE GAP - bylines unattested at excerpt level" in src
        assert "the corpus TC wearables trio" in src

    def test_scout_pick5_fortune_byline_gap_not_finding(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "BYLINE GAP - staffer" in src
        assert "did not surface in any search result" in src

    def test_scout_pick6_ben_schoon_rejected_weak(self):
        # No adversarial-Meta arm exists for a divergence pair; the
        # outlet confound is documented.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "no adversarial-Meta arm exists" in src
        assert "Google-focused by design" in src

    def test_sixth_1341_instance_pinned(self):
        # The scout's three headline picks are the SIXTH #1341-class
        # scout-corpus-blindness instance.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "SIXTH #1341-class" in src
        assert "#1363's FIFTH instance" in src

    def test_main_run_ashworth_saturated_in_corpus(self):
        # Boone Ashworth: deeply saturated (#70, #431, #998, #678);
        # his Oct-4 Gen-3 review re-surfaces the same register.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Boone Ashworth" in src
        assert "#70, #431, #998," in src
        assert "#678" in src

    def test_main_run_song_saturated_in_corpus(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Victoria Song" in src
        assert "m827, #993" in src

    def test_main_run_ropek_saturated_in_corpus(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Lucas Ropek" in src
        assert "dedicated tests Aug 24/26" in src

    def test_main_run_stein_saturated_in_corpus(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Scott Stein" in src
        assert "Type B #588" in src

    def test_query_sets_bounded(self):
        # 5 main-run browser.search query sets, documented verbatim.
        assert len(QUERY_SETS) == 5
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        for q in QUERY_SETS:
            assert q in src, q

# ---------------------------------------------------------------------------
# 3. Mechanism novelty: Type B lands ZERO mechanisms this run; max stays
#    1046; next 1047 stays clean in all three key forms.
# ---------------------------------------------------------------------------


class TestMechanismNovelty1368:
    def test_max_numeric_mechanism_id_stays_1046(self):
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
        assert "MECH_NUM = 1046" in src
        assert "NEXT_NUM = 1047" in src


# ---------------------------------------------------------------------------
# 4. Guard lifecycle: forward pins for #1369; #1368 staged this run.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1368:
    def test_pins_on_zero_mechanism_landing(self):
        # Type B lands zero mechanisms: max stays 1046, next 1047.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1046" in src
        assert "NEXT_NUM = 1047" in src

    def test_no_type_b_1368_in_git_log_pin(self):
        # Post-main-commit form for THIS run's own pin (the
        # #1191-class self-trip, re-pinned in this run's terminal
        # log-hash followup per #721/#1292): every commit whose
        # message matches "Type B #1368" must be this run's main
        # commit or a descendant of it. Deselected in the in-gate
        # run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type B #1368")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1368's own commits"
        main = _git("rev-parse", PRED_MAIN_1368).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_no_type_c_1369_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1369's terminal log-hash followup
        # per #721): every commit whose message matches "Type C
        # #1369" must be #1369's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1369 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type C #1369")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1369's own commits"
        main = _git("rev-parse", PRED_MAIN_1369).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1047_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1047_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1047_dash_absent_repo_wide(self):
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

    def test_no_sixty_fifth_member_pin(self):
        assert _git("grep", "-F", "-l", "SIXT" + "Y-FIFTH "
                   "falsification-family member", "HEAD") \
            .stdout.strip() == ""

    def test_ledger_holds_at_64_pin(self):
        # Type B lands zero mechanisms and the saturation-screening
        # verdict is NOT a falsification-family member: ledger holds
        # at 64. Pinned via the docstring's own prose form (kept
        # lowercase-short per #715).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ledger holds at 64" in src
        assert "no sixty-fifth member" in src

# ---------------------------------------------------------------------------
# 5. Staleness pin: the predecessor's guard lifecycle, run as-is.
# ---------------------------------------------------------------------------


class TestStalenessPins1368:
    def test_1367_guard_lifecycle_post_terminal_state(self):
        # Post-terminal-followup form: 25 tests in the class; 24
        # pass, 1 fails BY DESIGN - the #1191-class self-trip on the
        # no-Type-B-#1368-in-git-log pin (PRED_MAIN_1368 is still 0*40
        # until THIS run's terminal log-hash followup re-pins it in
        # BOTH copies per #721/#1292). The no-Type-A-#1367 pin flips
        # green in #1367's terminal followup (re-pinned in both
        # copies). The 1047-absent pins stay green (Type B lands zero
        # mechanisms); the forty-eighth through sixty-fourth member
        # pins stay green; the no-sixty-fifth pin stays green; the
        # fortieth-direction pin stays green.
        # Deselected in the in-gate run (fails pre-commit by design);
        # verified post-terminal.
        res = _class_run(B1367_FILE, "TestGuardLifecycle1367")
        out = res.stdout + res.stderr
        assert "1 failed, 24 passed" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 6. Doc-sync per #719 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestDocSync1368:
    def test_readme_test_file_table_has_1368_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_b_1368" in readme

    def test_architecture_has_1368_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_b_1368" in arch

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


class TestIterationLog1368:
    def test_log_has_1368_entry(self):
        text = _read(LOG_PATH)
        assert "## #1368 Type B" in text

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
        assert "1046" in text

# ---------------------------------------------------------------------------
# 8. Screening ledger: the journalists screened this run.
# ---------------------------------------------------------------------------


class TestScreeningLedger1368:
    def test_screened_journalists_documented(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        for name in ("Mark Gurman", "Raymond Wong", "Jessica Gorringe",
                     "Boone Ashworth", "Victoria Song", "Lucas Ropek",
                     "Scott Stein", "Ben Schoon"):
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
# 9. Research method.
# ---------------------------------------------------------------------------


class TestResearchMethod1368:
    def test_scout_plus_main_run_sets(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1 delegated scout (3 tracks)" in src
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


class TestVerdict1368:
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
        assert "verdict belongs to #1370 per #795" in src
        assert "neither" in src
        assert "re-launches, kills, nor writes to it" in src


# ---------------------------------------------------------------------------
# 11. In-flight isolation: the pending items stay out of this run.
# ---------------------------------------------------------------------------


class TestInFlightIsolation1368:
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
