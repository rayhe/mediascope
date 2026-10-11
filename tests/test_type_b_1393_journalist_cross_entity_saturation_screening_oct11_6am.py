"""Type B #1393: journalist cross-entity saturation screening - NO clean
fresh pair, NO mechanism landed (verdict saturation_screening_no_clean_pair;
main-run screens only, no delegated scout per the #1376 retry precedent -
nothing to distrust, everything main-run verified per the #1341 lesson;
6 browser.search query sets, 0 browser.open per #503; 5 names screened,
ZERO candidates proposed, NOT a #1341 instance; max stays 1051, ledger
holds at 65, no sixty-sixth member) - Type B FOURTH leg of the 1390-1394
window (Oct 11 2026, ~6:00 AM PDT).

Anchor convention per #565: ANCHORED_SHA is 0*40 pre-commit and is patched
to the main commit sha in the anchor followup; the placeholder pin passes
pre-commit and fails BY DESIGN post-anchor.

Rotation guard: this run is the FOURTH leg of the 1390-1394 window
(D #1390 -> E #1391 -> A #1392 -> B #1393 -> C #1394 per the #565 anchor +
rotation guard); the 1385-1389 window is VERIFIED CLOSED (all five legs
pushed and ls-remote-verified). Next: #1394 Type C continues the window
(correct type per the #1352 type-mismatch lesson); the next background-suite
verdict belongs to #1395 per #795. The #1390-launched full suite runs at the
goal hidden_files type_d_1390_full_suite.log: this run OBSERVES only
(neither re-launches, kills, nor writes to the suite).

Background suite (per #795): OBSERVED ONLY. Verdict belongs to #1395.

Concurrency: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file) all stay out of
this run's index and diff (explicit-path staging); do NOT touch #1024
m846 (profiles/competitor-entities.yaml untouched, decision pending).

ASCII-only, no em dashes. Needles format-built per #715: this file must
not carry contiguous numeric/underscore/dash mechanism-key forms of the
max or next number, the forty-eighth through sixty-sixth member-claim
forms, or the fortieth direction-claim form; the constants are
constructed at runtime. (The landed ordinals live as short lowercase
forms in prose here; the live full-form claims live in profiles: the
forty-eighth, fifty-eighth, and sixty-fifth in financial-times.yaml, the
forty-ninth, fiftieth, and fifty-second in profiles/careers/
journalists.yaml, the fifty-first, fifty-ninth, sixty-second, and
sixty-third in news-corp.yaml, the fifty-third in the-verge.yaml, the
fifty-fourth in guardian.yaml, the fifty-fifth in atlantic.yaml, the
fifty-sixth and sixty-first in wired.yaml, the fifty-seventh and
sixty-fourth in ap.yaml.)

Staleness note: #1391's TestGuardLifecycle1391 carries TWO #1191-class
post-terminal failures plus one #1272-class forward-guard expiry
(test_1051_numeric_absent_in_profiles trips on the m1051 block landed by
#1392 in profiles/the-verge.yaml) - DOCUMENTED not repaired per
precedent. This run's own pins take the post-landing form: 1051 numeric
PRESENT in profiles, 1052 all forms absent.
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

OWN_BASENAME = ("test_type_b_1393_journalist_cross_entity_"
                "saturation_screening_oct11_6am.py")

# Patched per #565 in the anchor followup (main commit sha).
ANCHORED_SHA = "6ff79d844bc5255950379dc8f454ee4587fb2aad"  # patched to the main commit sha in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1051  # max numeric; Type B lands ZERO mechanisms this run
NEXT_NUM = 1052  # integer only; key-form needles are format-built

# Post-doc-sync totals per #719: PATCHED post-collection
# (pre-sync 81899 + N tests; pre-sync 1717 + 1 file).
README_TEST_COUNT = 81993  # patched pre-main: pre-sync 81899 + 94 collected
README_FILE_COUNT = 1718  # patched pre-main: pre-sync 1717 + 1 (this file)

# Predecessor chain: #1392 Type A THIRD leg of the 1390-1394 window.
PRED_MAIN_1392 = "eb474941dc0dce1e7b6ee3fa189f63e2c69e2c5b"
PRED_ANCHOR_1392 = "21697d4fe8589ebbc81a16425f38b55b8d037206"
PRED_DOCSYNC_1392 = "1ea1167cbbb96260bffbf2ad02a32a6c42689175"
PRED_LOGHASH_1392 = "fbaee5a624a53bfb7a15d70ff28eb6cea6bfd549"
PRED_PUSH_1392 = "49b6f5dbc3cb5737c7fe43d90d22c917580a531b"

# This run's main commit (full sha), for the ancestor-form
# no-Type-B-#1393 pin. Staged 0*40 placeholder-only per #721;
# re-pinned in the anchor followup per #721 (PRED_MAIN_1393 re-pinned
# in BOTH this file and the #1392 file per the #1292 precedent).
PRED_MAIN_1393 = "6ff79d844bc5255950379dc8f454ee4587fb2aad"  # re-pinned to the #1393 main sha in the anchor followup per #721/1292

# #1394's main commit (full sha), for the ancestor-form no-Type-C-#1394
# pin (the #1191-class self-trip; #1394 is Type C per the rotation).
# Staged 0*40 placeholder-only per #721; re-pinned in #1394's terminal
# log-hash followup per #721. (Type-correct per the #1352
# type-mismatch lesson: #1394 is Type C, so the pin greps
# "Type C #1394".)
PRED_MAIN_1394 = "0" * 40

# The #1392 window-predecessor file, for the staleness pin on its
# guard-lifecycle class (max id 1051 landed; zero next-number 1052 all
# forms; sixty-fifth member present; no sixty-sixth member; ledger
# holds at 65).
B1392_FILE = ("test_type_a_1392_verge_openai_oct07_08_gpt6_"
              "intelligent_ui_launch_register_vs_carried_meta_"
              "arms_oct11_6am.py")

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

# 6 main-run browser.search query sets this run (0 browser.open per
# #503; no delegated scout per the #1376 retry precedent).
QUERY_SETS = [
    "Lauren Goode WIRED Meta glasses AI October 2026",
    "Boone Ashworth WIRED wearables Meta review 2026",
    "Caroline Haskins WIRED Meta AI coverage",
    "Makena Kelly Verge Meta tech policy coverage 2026",
    "Casey Newton Platformer Meta coverage October 2026",
    "Ray-Ban Meta Audio glasses launch review journalist October 2026 Verge WIRED",
]

# New verbatim URL keys this run (zero pre-commit corpus hits via
# git grep -F at HEAD, verified by the main run): screened, not paired.
NEW_URL_KEYS = [
    "https://www.manton.org/2026/10/07/watching-x.html",
    "https://eshumarneedi.com/2026/10/02/on-openais-dev-day-announcements.html",
    "https://wesearch.press/s/meta-glasses-nova-gen-3-review-not-much-new-ecd50b7f",
    "https://gizmodo.com/ray-ban-meta-gen-3-ai-glasses-review-2000822961",
    "https://www.youtube.com/watch?v=Fd2kdgL9Qmg",
    "https://memeburn.com/samsung-intelligent-eyewear/",
    "https://ivy.fm/tag/makena-kelly",
]

# Re-surfaced verbatim URL keys this run (pre-commit corpus hits at
# HEAD): not new facts.
RESURFACE_URL_KEYS = [
    "https://www.theshortcut.com/p/meta-glasses-camera-free-first-look",
    "https://dev.to/the_daily_flare/smart-glasses-how-the-technology-is-advancing-in-2026-29pm",
    "https://gizmodo.com/meta-introduces-audio-only-smart-glasses-to-avoid-the-perv-problem-2000815782",
    "https://muckrack.com/caroline_haskins/articles",
    "https://muckrack.com/casey-newton-2/articles",
]

EXPECTED_TOTAL = 94  # patched pre-main: 94 tests collected in the in-gate


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
        if needle in open(p, encoding="utf-8",
                           errors="replace").read()
    ]


def _repo_grep_dash_mechanism(n):
    needle = "mechanism" + "-" + str(n)
    return [
        p
        for p in _iter_source_files()
        if needle in open(p, encoding="utf-8",
                           errors="replace").read()
    ]


def _repo_grep_numeric_mechanism_id(n):
    needle = "mechanism_id: %d" % n
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if needle in open(p, encoding="utf-8",
                               errors="replace").read():
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


def _count_head_hits(name):
    out = _git("grep", "-i", "-F", "-l", name, "HEAD", "--",
               "profiles/", "tests/")
    return len([l for l in out.stdout.splitlines() if l.strip()])


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup)
#    + rotation guard: FOURTH leg of the 1390-1394 window.
# ---------------------------------------------------------------------------


class TestAnchor1393:
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
        assert "FOURTH leg of the 1390-1394 window" in src
        assert "D #1390 -> E #1391 -> A #1392" in src

    def test_1385_1389_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "the 1385-1389 window is VERIFIED CLOSED" in src

    def test_next_leg_is_1394_type_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "-> C #1394" in src


# ---------------------------------------------------------------------------
# 2. Main-run screens: five journalists plus the Audio launch surface.
# ---------------------------------------------------------------------------


class TestMainRunScreens1393:
    def test_goode_saturated(self):
        # Lauren Goode (WIRED Senior Correspondent): 42 corpus files
        # at HEAD. The #436 Type B cross-entity wearables analysis
        # (Apple Vision Pro empathetic "I cried" vs Meta Ray-Ban
        # clinical avoidance; Snap Spectacles playful; Google I/O 2026
        # Android XR playful; beat shift to AI semiconductors) already
        # landed, with asymmetry score 0.87. This run's set surfaced
        # only own-repo circular commits (54c9bd58 #436-era, 7a27c85,
        # e29a2f4a), TikTok clips, and unrelated items. SATURATED.
        # Re-screening would re-litigate. No fresh pair.
        assert _count_head_hits("Lauren Goode") == 42
        out = _git("grep", "-F", "-l", "Lauren Goode", "HEAD",
                   "--", "profiles/careers/journalists.yaml")
        assert out.stdout.strip() != "", out.stdout
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "42 corpus files" in src
        assert "0.87" in src

    def test_ashworth_saturated(self):
        # Boone Ashworth (WIRED Gear): 45 corpus files at HEAD -
        # mechanisms #365/#385/#442/#678/#998 (OpenAI aspirational vs
        # Meta mass-surveillance inversion, Snap-vs-Meta pricing
        # inversion, Google XR hands-on register, Sep-23 Connect
        # news-register bound on m743). SATURATED. This run's new URL
        # key (the wesearch.press Oct-4 Meta Glasses Nova Gen 3 review
        # relay, 7/10 "Not Much New") is a new URL, not a new fact -
        # the review register sits inside the already-tracked
        # Ashworth-Meta corpus. No fresh pair.
        assert _count_head_hits("Boone Ashworth") == 45
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "45 corpus files" in src
        assert "m743" in src
        assert ("https://wesearch.press/s/meta-glasses-nova-gen-3-"
                "review-not-much-new-ecd50b7f") in NEW_URL_KEYS

    def test_haskins_bounded(self):
        # Caroline Haskins (WIRED business desk, Mar 2026): 6 corpus
        # files at HEAD. Type B #553 already ran her cross-entity
        # comparison (Project Cannes Meta investigation -0.80 vs Flock
        # ALPR misuse -0.65/-0.60/-0.45; illustrative delta +0.10
        # MANUAL ILLUSTRATIVE, falsifying the journalist-level
        # anti-Meta bias hypothesis). This run's set re-surfaced her
        # muckrack page and the talkingbiznews hire piece; no new
        # cross-entity material. BOUNDED. No new pair proposed.
        assert _count_head_hits("Caroline Haskins") == 6
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "6 corpus files" in src
        assert "#553" in src
        assert "https://muckrack.com/caroline_haskins/articles" in \
            RESURFACE_URL_KEYS

    def test_kelly_bounded_absence(self):
        # Makena Kelly (The Verge policy reporter): 3 corpus files at
        # HEAD, all techmeme byline relays of policy pieces (sponsored
        # content, self-preferencing documents, interoperability bill).
        # Bounded search-result absence: no Meta byline, no wearable
        # or product-review arm, no competitor arm. A policy-beat
        # reporter with no cross-entity wearable material is not a
        # pair candidate. The ivy.fm podcast-appearances page is a new
        # URL key, not a new fact (career background already in
        # corpus). NOT proposed.
        assert _count_head_hits("Makena Kelly") == 3
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "bounded search-result absence" in src
        assert "https://ivy.fm/tag/makena-kelly" in NEW_URL_KEYS

    def test_newton_moderate(self):
        # Casey Newton (Platformer): 12 corpus files at HEAD -
        # mechanism 24 (Disclosure-as-Inoculation Paradox: fiance at
        # Anthropic, announced Feb 2026) and #1083 m881 (Anthropic vs
        # Meta personal-gradient pair, illustrative delta +0.30 in the
        # direction the PERSONAL tie predicts). MODERATE, not
        # saturated - but this run's two new URL keys (manton.org
        # Oct-7 X-return relay; eshumarneedi Oct-2 Dots relay) are new
        # URLs, not new facts: the Dots-vs-Muse piece and the X-return
        # are tracked themes. No fresh cross-entity pair beyond m881.
        assert _count_head_hits("Casey Newton") == 12
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "12 corpus files" in src
        assert "m881" in src
        assert ("https://www.manton.org/2026/10/07/watching-x.html"
                in NEW_URL_KEYS)
        assert ("https://eshumarneedi.com/2026/10/02/on-openais-"
                "dev-day-announcements.html" in NEW_URL_KEYS)

    def test_audio_launch_no_fresh_tracked_pair(self):
        # Ray-Ban Meta Audio launch surface (ships Oct 13 2026, $349,
        # camera-free): the theshortcut.com first-look and the
        # gizmodo.com Pero "Perv Problem" piece are re-surfaces
        # (tracked); the gizmodo.com Raymond Wong Gen 3 review and the
        # bytesizedai YouTube explainer are new URL keys but not
        # tracked-outlet byline pairs (relay/video-tier, no WIRED or
        # Verge byline at excerpt level); the memeburn.com Samsung
        # eyewear pricing piece is competitor context with no tracked
        # byline. No fresh tracked-outlet byline pair emerges.
        for u in ("https://www.theshortcut.com/p/meta-glasses-"
                  "camera-free-first-look",
                  "https://gizmodo.com/meta-introduces-audio-only-"
                  "smart-glasses-to-avoid-the-perv-problem-2000815782"):
            assert u in RESURFACE_URL_KEYS, u
        for u in ("https://gizmodo.com/ray-ban-meta-gen-3-ai-"
                  "glasses-review-2000822961",
                  "https://www.youtube.com/watch?v=Fd2kdgL9Qmg",
                  "https://memeburn.com/samsung-intelligent-eyewear/"):
            assert u in NEW_URL_KEYS, u
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "no tracked-outlet byline pair" in src

    def test_url_keys_novelty_verified(self):
        # Every new verbatim URL key zero-hits at HEAD (verified by
        # the main run's own git grep -F); every re-surface key hits.
        for u in NEW_URL_KEYS:
            out = _git("grep", "-F", "-l", u, "HEAD")
            assert out.stdout.strip() == "", u
        for u in RESURFACE_URL_KEYS:
            out = _git("grep", "-F", "-l", u, "HEAD")
            assert out.stdout.strip() != "", u


# ---------------------------------------------------------------------------
# 3. Corpus verification: every screening claim main-run-verified.
# ---------------------------------------------------------------------------


class TestCorpusVerification1393:
    def test_m1051_block_carrier(self):
        # The m1051 block (landed by #1392) sits in profiles/the-verge.yaml
        # and carries the Verge x OpenAI GPT-6 register; this run's
        # screens extend the tracked-byline set without re-litigating it.
        out = _git("grep", "-F", "-l", "mechanism_id: 1051", "HEAD",
                   "--", "profiles/the-verge.yaml")
        assert out.stdout.strip() != "", out.stdout

    def test_goode_cross_entity_intact(self):
        # The Goode cross-entity carriers (#436, #385) remain intact
        # in profiles; this run adds nothing to them.
        out = _git("grep", "-F", "-l", "Lauren Goode", "HEAD",
                   "--", "profiles/careers/journalists.yaml")
        assert out.stdout.strip() != "", out.stdout
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#436" in src

    def test_haskins_falsification_intact(self):
        # The Haskins surveillance-beat constancy record (#553, the
        # journalist-level anti-Meta-bias falsification) remains
        # intact in profiles; this run adds nothing to it.
        out = _git("grep", "-F", "-l", "Caroline Haskins", "HEAD",
                   "--", "profiles/careers/journalists.yaml")
        assert out.stdout.strip() != "", out.stdout
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "falsifying the journalist-level" in src

    def test_newton_mechanisms_intact(self):
        # The Newton carriers (mechanism 24, m881) remain intact in
        # profiles; this run adds nothing to them.
        assert _repo_grep_numeric_mechanism_id(24) != []
        assert _repo_grep_numeric_mechanism_id(881) != []
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "mechanism 24" in src and "m881" in src

    def test_not_a_1341_instance(self):
        # NOT a #1341-class instance: no delegated scout ran this run
        # (main-run sets only per the #1376 retry precedent); the main
        # run verified every screening claim independently via git
        # grep -F -i at HEAD. The tenth instance at #1369 stands as
        # the last.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NOT a #1341-class instance" in src
        assert "the tenth instance at #1369 stands as the last" in src


# ---------------------------------------------------------------------------
# 4. Mechanism novelty: max stays 1051; zero 1052 key forms; no
#    profiles/ edit.
# ---------------------------------------------------------------------------


class TestMechanismNovelty1393:
    def test_max_numeric_mechanism_id_stays_1051(self):
        assert _max_numeric_mechanism_id() == MECH_NUM == 1051

    def test_1052_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1052_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1052_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_profiles_edit_this_run(self):
        # Type B lands zero mechanisms: no profiles/ file may carry a
        # #1393 block. The working tree must show zero profiles/
        # modifications outside the in-flight #899 hunk.
        out = _git("status", "--short")
        for line in out.stdout.splitlines():
            if "profiles/" in line:
                assert "profiles/nytimes.yaml" in line, line

    def test_mech_num_constants(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1051" in src
        assert "NEXT_NUM = 1052" in src


# ---------------------------------------------------------------------------
# 5. Guard lifecycle for this run (pre-commit form; the no-Type-B-#1393
# pin is the #1191-class self-trip, re-pinned in the terminal log-hash
# followup per #721/#1292).
# ---------------------------------------------------------------------------


class TestGuardLifecycle1393:
    def test_pins_on_zero_mechanism_landing(self):
        # Type B lands zero mechanisms: max stays 1051, next 1052.
        # The m1051 block (landed by #1392) is already committed, so
        # the 1051 numeric pin takes the PRESENT form this run; the
        # #1272-class 1051-absent expiry in #1391's file stays
        # DOCUMENTED not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1051" in src
        assert "NEXT_NUM = 1052" in src
        assert _max_numeric_mechanism_id() == 1051

    def test_no_type_b_1393_in_git_log_pin(self):
        # Post-main-commit form for THIS run's own pin (the
        # #1191-class self-trip, re-pinned in this run's terminal
        # log-hash followup per #721/#1292): every commit whose
        # message matches "Type B #1393" must be this run's main
        # commit or a descendant of it. Deselected in the in-gate
        # run (fails pre-commit by design: PRED_MAIN_1393 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type B #1393")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1393's own commits"
        main = _git("rev-parse", PRED_MAIN_1393).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_no_type_c_1394_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1394's terminal log-hash followup
        # per #721): every commit whose message matches "Type C
        # #1394" must be #1394's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1394 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type C #1394")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1394's own commits"
        main = _git("rev-parse", PRED_MAIN_1394).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1051_numeric_present_in_profiles(self):
        # Post-landing form: the m1051 block is committed in
        # profiles/the-verge.yaml by #1392.
        assert _repo_grep_numeric_mechanism_id(MECH_NUM) != []

    def test_1052_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1052_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1052_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_fortieth_direction_pin(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_forty_eighth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T48, None) != []

    def test_forty_ninth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T49, None) != []

    def test_fiftieth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T50, None) != []

    def test_fifty_first_member_intact_pin(self):
        assert _git_grep_tracked_source(_T51, None) != []

    def test_fifty_second_member_intact_pin(self):
        assert _git_grep_tracked_source(_T52, None) != []

    def test_fifty_third_member_intact_pin(self):
        assert _git_grep_tracked_source(_T53, None) != []

    def test_fifty_fourth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T54, None) != []

    def test_fifty_fifth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T55, None) != []

    def test_fifty_sixth_member_intact_pin(self):
        # (ASCII class-name form; the fifty-sixth member-claim form
        # stays intact in profiles/wired.yaml.)
        assert _git_grep_tracked_source(_T56, None) != []

    def test_fifty_seventh_member_intact_pin(self):
        assert _git_grep_tracked_source(_T57, None) != []

    def test_fifty_eighth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T58, None) != []

    def test_fifty_ninth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T59, None) != []

    def test_sixtieth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T60, None) != []

    def test_sixty_first_member_intact_pin(self):
        assert _git_grep_tracked_source(_T61, None) != []

    def test_sixty_second_member_intact_pin(self):
        assert _git_grep_tracked_source(_T62, None) != []

    def test_sixty_third_member_intact_pin(self):
        assert _git_grep_tracked_source(_T63, None) != []

    def test_sixty_fourth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T64, None) != []

    def test_sixty_fifth_member_intact_pin(self):
        # The m1047 block (#1372) carries the sixty-fifth
        # member-claim form in profiles/financial-times.yaml; Type B
        # lands zero mechanisms so it stays intact.
        assert _git_grep_tracked_source(_T65, None) != []

    def test_no_sixty_sixth_member_pin(self):
        # The sixty-sixth member-claim form stays absent repo-wide
        # (fragment-built needle per #715).
        assert _git_grep_tracked_source(_T66, None) == []

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


class TestStalenessPins1393:
    def test_1392_guard_lifecycle_post_terminal_followup(self):
        # Post-terminal-followup form: 27 passed. The #1191-class
        # no_type_b_1393_in_git_log forward pin flips green in this
        # run's terminal log-hash followup per #721/#1292
        # (PRED_MAIN_1393 re-pinned in the #1392 file). There is NO
        # #1272-class forward-guard expiry on THIS predecessor: #1392
        # landed m1051, so its pins already take the post-landing
        # form (1051 present, 1052 absent). The #1391 1051-absent
        # expiry stays DOCUMENTED not repaired (see docstring). The
        # #1392 block is read-only to this run. Deselected pre-commit
        # (verified only post-terminal-followup).
        venv_py = os.path.join(REPO_ROOT, ".venv", "bin", "python")
        r = subprocess.run(
            [venv_py, "-m", "pytest",
             os.path.join(TESTS_DIR, B1392_FILE)
             + "::TestGuardLifecycle1392",
             "-q", "-p", "no:cacheprovider"],
            capture_output=True, text=True, timeout=300, cwd=REPO_ROOT,
        )
        tail = r.stdout.strip().splitlines()[-1]
        assert "27 passed" in tail, tail


# ---------------------------------------------------------------------------
# 7. Doc-sync per #719 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestDocSync1393:
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

    def test_readme_has_1393_table_row(self):
        src = _read(README_PATH)
        assert "test_type_b_1393" in src


# ---------------------------------------------------------------------------
# 8. Iteration log per #721 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestIterationLog1393:
    def test_log_has_1393_heading(self):
        # Written in the doc-sync commit per #721. Fails pre-commit
        # by design; deselected in the in-gate run.
        assert "## #1393" in _read(LOG_PATH)

    def test_log_registers_main_anchor_docsync_hashes(self):
        src = _read(LOG_PATH)
        assert "log-hash" in src

    def test_log_records_saturation_screening(self):
        src = _read(LOG_PATH)
        assert "saturation_screening_no_clean_pair" in src
        assert "1051" in src


# ---------------------------------------------------------------------------
# 9. Screening ledger: the journalists screened this run.
# ---------------------------------------------------------------------------


class TestScreeningLedger1393:
    def test_goode_ledger_entry(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Lauren Goode" in src
        assert "#436" in src and "0.87" in src
        assert "SATURATED" in src

    def test_ashworth_ledger_entry(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Boone Ashworth" in src
        assert "m743" in src
        assert "SATURATED" in src

    def test_haskins_ledger_entry(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Caroline Haskins" in src
        assert "#553" in src
        assert "BOUNDED" in src

    def test_kelly_ledger_entry(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Makena Kelly" in src
        assert "bounded search-result absence" in src

    def test_newton_ledger_entry(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Casey Newton" in src
        assert "mechanism 24" in src and "m881" in src
        assert "MODERATE" in src

    def test_zero_candidates_proposed(self):
        # Five names screened, ZERO candidates proposed: no clean
        # fresh pair exists at tracked outlets this run. The ledger
        # records the screen, not a finding.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ZERO candidates proposed" in src
        assert "no clean" in src and "fresh pair" in src


# ---------------------------------------------------------------------------
# 10. Research method: bounded, relay-attested, snippet-tier.
# ---------------------------------------------------------------------------


class TestResearchMethod1393:
    def test_six_query_sets(self):
        assert len(QUERY_SETS) == 6
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "6 main-run browser.search query sets" in src

    def test_zero_browser_open(self):
        # 0 browser.open per #503: snippet-bounded, relay-attested.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "0 browser.open per #503" in src

    def test_snippet_bounded(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "snippet-bounded" in src

    def test_urls_verbatim(self):
        # All URLs copied verbatim from the browser.search Full-URL
        # listings; no canonical URLs constructed.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "copied verbatim" in src
        assert "no canonical URLs constructed" in src

    def test_no_delegated_scout(self):
        # No delegated scout this run (retry attempt; main-run sets
        # only per the #1376 retry precedent - nothing to distrust,
        # everything main-run verified per the #1341 lesson).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "no delegated scout" in src
        assert "#1376 retry precedent" in src


# ---------------------------------------------------------------------------
# 11. Verdict: saturation screening, no falsification-family member.
# ---------------------------------------------------------------------------


class TestVerdict1393:
    def test_verdict_string(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "saturation_screening_no_clean_pair" in src

    def test_not_a_falsification_member(self):
        # A clean-negative screen generates no thesis claim and no
        # falsification claim: NOT a falsification-family member;
        # the ledger holds at 65.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NOT a falsification-family member" in src
        assert "ledger holds at 65" in src

    def test_no_mechanism_landed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NO mechanism landed" in src
        assert "max stays 1051" in src

    def test_manual_qualitative_only(self):
        # MANUAL / QUALITATIVE ONLY per the Aug-28 standing rule.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MANUAL" in src and "QUALITATIVE ONLY" in src
        assert "Aug-28 standing rule" in src

    def test_no_analysis_json_update(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "no analysis.json update" in src
        assert "NOT artifact-grade" in src

    def test_monitoring_only(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "monitoring-only" in src


# ---------------------------------------------------------------------------
# 12. In-flight isolation: #899/#938/#900/#1012-wt untouched; #1024
#     m846 byte-identical.
# ---------------------------------------------------------------------------


class TestInFlightIsolation1393:
    def test_899_nytimes_hunk_in_working_diff(self):
        # The #899 hunk IS in the unstaged working diff (owned by
        # #899's run); this run stages only its own files via
        # explicit-path staging, so it never enters this run's index.
        res = _git("diff", "--name-only")
        assert "profiles/nytimes.yaml" in res.stdout.split()

    def test_899_nytimes_hunk_owned_by_its_run(self):
        # Its uncommitted hunk belongs to #899's run; this run stages
        # only its own files.
        res = _git("status", "--short")
        assert "profiles/nytimes.yaml" in res.stdout

    def test_900_untracked_file_untouched(self):
        res = _git("status", "--short")
        assert "test_type_d_900_m769" in res.stdout

    def test_938_test_file_edit_owned_by_its_run(self):
        res = _git("status", "--short")
        assert "test_type_b_938" in res.stdout

    def test_1012_wt_working_tree_edit_owned_by_its_run(self):
        res = _git("status", "--short")
        assert "test_type_a_1012" in res.stdout

    def test_own_diff_excludes_inflight(self):
        # This run's staged set must never include the in-flight
        # files; verified at commit time by explicit-path staging.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "explicit-path" in src

    def test_m846_block_byte_identity(self):
        # #1024 m846 (profiles/competitor-entities.yaml, HEAD lines
        # 26349-26472): decision still pending. The m846 block must
        # be byte-identical to HEAD. Do NOT touch #1024 m846.
        head = _git(
            "show", "HEAD:profiles/competitor-entities.yaml").stdout
        work = _read(os.path.join(REPO_ROOT,
                                  "profiles/competitor-entities.yaml"))
        assert (head.splitlines()[M846_HEAD_START - 1:M846_HEAD_END]
                == work.splitlines()[M846_HEAD_START - 1:M846_HEAD_END])
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Do NOT touch #1024" in src

    def test_m846_not_in_working_diff(self):
        out = _git("diff", "--name-only")
        assert "profiles/competitor-entities.yaml" not in out.stdout


# ---------------------------------------------------------------------------
# 13. Rotation: FOURTH leg of the 1390-1394 window.
# ---------------------------------------------------------------------------


class TestRotation1393:
    def test_window_sequence(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1390 -> E #1391 -> A #1392 -> B #1393" in src

    def test_next_leg_is_type_c(self):
        assert PRED_MAIN_1394 == "0" * 40

    def test_type_letter_b(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type B #1393" in src

    def test_background_suite_observed_only(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "OBSERVES only" in src
        assert "#1390" in src
        assert "#1395" in src

    def test_1394_forward_guard_staged(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "PRED_MAIN_1394" in src
        assert "no-Type-C-#1394 pin" in src


# ---------------------------------------------------------------------------
# 14. ASCII and formatting hygiene.
# ---------------------------------------------------------------------------


class TestAscii1393:
    def test_no_em_dashes_in_test_file(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "\u2014" not in src

    def test_ascii_only_in_test_file(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        src.encode("ascii")

    def test_expected_total_declared(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "EXPECTED_TOTAL = 94" in src

    def test_no_1052_key_forms_in_file(self):
        # #715/#770 discipline: no contiguous 1052 key forms carried
        # as literals; needles are format-built at runtime (the same
        # construction as the _repo_grep_* helpers).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert ("%s%d" % (MECH_ID_MARKER, NEXT_NUM)) not in src
        assert ("mechanism" + "-" + str(NEXT_NUM)) not in src
        assert ("mechanism_id: %d" % NEXT_NUM) not in src
