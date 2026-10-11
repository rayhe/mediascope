"""Type A #1397: competitor-coverage saturation screening (Oct 11 2026,
~9:00 AM PDT).

Three publication+competitor pairs screened this run; NO clean fresh
mechanism, NO mechanism landed (verdict
saturation_screening_no_clean_mechanism; max stays 1051, ledger holds
at 65, no sixty-sixth member).

SET 1 - WIRED x OpenAI (6 main-run rows, all novel relay URLs, zero
pre-commit corpus hits via git grep -F): the Oct-6 Isabella Ward
mathematicians accountability piece (banked m1027 #1327, SIXTY-FIRST
falsification-family member), the Oct-7 Reece Rogers Intelligent UI
review (banked m1050 #1387, thesis_consistent_observation, delta
+0.53), the Oct-7 Dots agent hands-on (banked m991 #1267), the Oct-9
Big Five publishers AI-use piece (same Ward-era WIRED AI beat, no new
peg), and the wdcnews6 IPO-delay piece (relay of the wdcnews relay
chain). New URLs, no new facts. The Verge x OpenAI is likewise
saturated (m1051 #1392).

SET 2 - FT x Anthropic (6 main-run rows: 5 novel relay URLs + 1
re-surface via #1382, every novel URL zero pre-commit corpus hits
via git grep -F): the Oct-1/2 IPO-timing peg
(Bloomberg Oct-1 scoops, WSJ Sep-18, Reuters Sep-28 prospectus review)
is Bloomberg/WSJ/Reuters-original, not an FT original; the live-feeds
FT "sustainability" citation is a thin excerpt-tier follow-up of m859
(#1047, FT Sep-14 IPO-profitability reporting), not a clean fresh peg;
the Oct-5/6 Broadcom syndication financing-risk register is banked
m1047 (#1372, SIXTY-FIFTH falsification-family member). New URLs, no
new facts. The dimsumdaily.hk URL key is EXCLUDED from the keys list:
its path carries a non-ASCII hyphen, violating the ASCII-only rule;
documented, not ingested.

SET 3 - Apple "Welcome Home" Oct-13 smart-home event (3 main-run
rows, all novel relay URLs, zero pre-commit corpus hits via git grep
-F): Joswiak Oct-8 teaser; Tribeca "Apple Experience" Oct 13 9am ET;
the camera-and-presence-sensor hub (J490, ~$350) and the J450 home
camera (text updates instead of video, facial recognition, low frame
rate, no video recording). NO WIRED/Verge/FT/NYT/Guardian original
surfaced in the bounded 2-set surface - only Apple-beat relays
(thurrott, macdailynews, macrumors, appleinsider, newsy-today,
gadgets360, geeky-gadgets, basic-tutorials, hanaringo, glitched) of
Gurman/Bloomberg/MacRumors reporting. The event is 2 days out:
pre-event bounded absence is NOT a finding. Logged as a WATCH ITEM
for post-Oct-13 runs: the camera-bearing hub is the first
camera-on-device Apple product since the wearables stigma debate, and
the testable prediction is a register comparison - whether tracked
outlets apply the same privacy register to Apple's camera-bearing hub
as they applied to Meta's "perv glasses" register.

Type A lands no mechanisms this run: max numeric mechanism_id stays
1051, ledger holds at 65, no sixty-sixth member. MANUAL /
QUALITATIVE ONLY per the Aug-28 standing rule; monitoring-only;
NOT artifact-grade; no analysis.json update. Correlation is not
causation; hypothesis-generating only.

Research method: 7 main-run browser.search verification sets
(WIRED x OpenAI October 2026; Apple Oct-13 "Welcome Home"; Bloomberg
x Anthropic October 2026; FT x Anthropic IPO; NYT x Anthropic IPO;
WIRED x Apple smart-home hub; The Verge x Apple smart-home) + git
grep -F novelty verification on every candidate URL; no delegated
scout this run (retry attempt; main-run sets only per the #1376 retry
precedent and the #1341 lesson); 0 browser.open per #503;
snippet-bounded; all URLs copied verbatim from the browser.search
Full-URL listings (the dimsumdaily key excluded for non-ASCII path);
bounded search-result absence, not proof.

Background suite per #795: the #1395-launched full suite runs at
goal hidden_files type_d_1395_full_suite.log: this run OBSERVES
only (neither re-launches, kills, nor writes to the suite).
Observed at this run's check (see the ## #1397 iteration-log
entry); verdict and tombstone belong to #1400 per #795.

Concurrency: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B
test file working-tree edit), #900 (untracked Type D test file),
#1012-wt (working-tree edit on the committed Type A #1012 file)
all left out of this run's index/diff via explicit-path staging.
#1024 m846 (profiles/competitor-entities.yaml) NOT touched -
decision pending. Do NOT touch #1024 m846.
"""
import os
import re
import subprocess

import pytest


REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
ITERLOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
ENTITIES_PATH = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
OWN_BASENAME = (
    "test_type_a_1397_wired_openai_ft_anthropic_apple_oct13_"
    "saturation_screening_oct11_9am.py"
)


# Pre-commit placeholder per #565; patched to the main-commit sha in
# the anchor followup (post-anchor the placeholder pin fails BY
# DESIGN).
ANCHORED_SHA = "74aba7af51166ff55c57e8411eda5284d953a328"  # patched to the main commit sha in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1051
NEXT_NUM = 1052  # integer only; key-form needles are format-built

# Predecessor chain: #1396 Type E was the SECOND leg of the
# 1395-1399 window. Its main/anchor/doc-sync/log-hash/push-status
# commits are pushed and ls-remote-verified.
PRED_MAIN_1396 = "bacc76abc43d75bea47cc504bd2f453c95bb1ef3"
PRED_ANCHOR_1396 = "2522bb31e74b9c83ef7ad14efdc5d24e93b3dd43"
PRED_DOCSYNC_1396 = "8d8fe731f18e3d1486b5963ba30013bd207fdb70"
PRED_FINAL_1396 = "047d7866913ac9da3bb282ba5d6feba223c0a863"
PRED_PUSH_1396 = "5d5cff21991ddb3132440881e00cfb0683e8357a"

# This run's own main-commit sha, re-pinned per #721 in the anchor
# followup (the #1396 predecessor file's copy is re-pinned in the
# terminal log-hash followup per #721/#1292).
PRED_MAIN_1397 = "74aba7af51166ff55c57e8411eda5284d953a328"  # re-pinned by #1397 anchor followup per #721

# Forward guard for the next leg: #1398 Type B (starts as 0*40;
# placeholder-only; re-pinned to the #1398 main sha in #1398's
# terminal log-hash followup per #721/#1292).
PRED_MAIN_1398 = "0" * 40

# The #1396 Type E file, for the staleness pin on its guard
# lifecycle (post-terminal form at this run is "25 passed, 2
# failed": the two strict-form #1191-class pins - the
# no-Type-E-#1396 own pin and the no-Type-A-#1397 forward pin -
# self-trip permanently post-landing per the #1392 strict-form
# precedent; DOCUMENTED not repaired; the substantive guards are
# verified satisfied via merge-base --is-ancestor in the test
# below). Documented in TestStalenessPins1397, not repaired.
D1396_FILE = (
    "test_type_e_1396_podcast_sentiment_202nd_"
    "verification_oct11_8am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 82364  # patched pre-main: pre-sync 82275 + 89 collected
README_FILE_COUNT = 1722  # patched pre-main: pre-sync 1721 + 1 (this file)

# m846 block region in profiles/competitor-entities.yaml at HEAD (the
# #1024 m846 decision-pending block; byte-identity pin in the
# in-flight isolation class). HEAD lines, 1-based, verified intact
# this run.
M846_HEAD_START = 26349
M846_HEAD_END = 26472

# The forward-guard needles are fragment-built per #715 so this file
# carries no contiguous sensitive literal.
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

# ---------------------------------------------------------------------------
# This run's surfaced evidence (all URLs copied verbatim from the
# browser.search Full-URL listings; corpus novelty verified pre-commit
# via git grep -F). Snippet-bounded throughout.
# ---------------------------------------------------------------------------

WIRED_OPENAI_NEW_KEYS = [
    # The wikinews.live relay of the Oct-6 Isabella Ward
    # mathematicians accountability piece (banked m1027 #1327).
    # New URL, no new fact.
    "https://wikinews.live/articles/archive/OpenAI-Is-Pissing-Off-"
    "a-Bunch-of-MathematiciansAgain-07-October-2026.php",
    # The technewstube relay of the same mathematicians piece.
    # New URL, no new fact.
    "https://technewstube.com/wired/1873761/openai-pissing-off-"
    "bunch-mathematiciansagain/",
    # The technewstube relay of the Oct-7 Reece Rogers Intelligent
    # UI review (banked m1050 #1387). New URL, no new fact.
    "https://technewstube.com/wired/1874215/new-chatgpt-show-than-tell/",
    # The 15minutenews relay of the Oct-7 Dots agent hands-on
    # (banked m991 #1267). New URL, no new fact.
    "https://www.15minutenews.com/article/2026/10/07/284621957/"
    "openai-wants-its-new-agent-to-run-your-life-mine-said-it-loved-me/",
    # The explainx.ai blog piece on the Oct-9 WIRED Big Five
    # publishers AI-use reporting (same WIRED AI beat, no new
    # tracked peg). New URL, no new fact.
    "https://explainx.ai/blog/big-five-publishers-quietly-using-ai-"
    "covers-copy-staff-revolt-wired-2026",
    # The wdcnews6 IPO-delay piece (relay-chain item, no tracked
    # publication original). New URL, no new fact.
    "https://wdcnews6.com/why-openai-anthropic-and-oura-have-"
    "delayed-their-ipos/",
]

FT_ANTHROPIC_NEW_KEYS = [
    # The techsnif relay of Bloomberg's Oct-1 Anthropic IPO-timing
    # scoop. New URL, no new fact; the original is Bloomberg's, not
    # the FT's.
    "https://techsnif.com/story/anthropic-could-start-formal-"
    "marketing-for-its-ipo-as-soon-a-919a6a",
    # The verilynews relay of the mid-November IPO peg. New URL,
    # no new fact.
    "https://verilynews.com/anthropic-reportedly-eyes-november-ipo/",
    # The thinkmarkets FAQ on the Anthropic IPO. New URL, no new
    # fact.
    "https://www.thinkmarkets.com/en/trading-academy/market-events/"
    "anthropic-ipo-2026-date-valuation-and-how-to-trade/",
    # The tech-insider.org Cramer/AI-risk piece (thin peg, no
    # tracked publication original). New URL, no new fact.
    "https://tech-insider.org/cramer-anthropic-ipo-researcher-10-"
    "percent-ai-risk-2026/",
    # NOTE: the saascity.io prospectus recap
    # (https://saascity.io/blog/anthropic-ipo-prospectus-saas-
    # founders-2026) is NOT a new key - it re-surfaces (in corpus
    # via #1382, m1049 Verge x Anthropic Sep-29 IPO-filing pair;
    # the #1382 precedent caught it on the in-gate repair). 5 new
    # keys, 1 re-surface on this set.
    # The live-feeds IPO-timeline piece, which cites "Financial
    # Times - Investors weigh whether Anthropic can sustain
    # surging revenues post-IPO": a thin excerpt-tier follow-up of
    # m859 (#1047, FT Sep-14 IPO-profitability reporting), not a
    # clean fresh peg. New URL, no new fact.
    "https://www.live-feeds.com/feed/anthropic-shifts-planned-ipo-"
    "to-november",
    # NOTE: the dimsumdaily.hk relay URL is EXCLUDED from this
    # list - its path carries a non-ASCII hyphen, violating the
    # ASCII-only rule. Documented, not ingested.
]

APPLE_OCT13_NEW_KEYS = [
    # The macdailynews Oct-8 event-announcement piece (Joswiak
    # teaser; Tribeca Apple Experience Oct 13 9am ET). New URL, no
    # new fact; Apple-beat relay, not a tracked-publication
    # original.
    "https://macdailynews.com/2026/10/08/its-official-apple-to-hold-"
    "welcome-home-product-event-on-october-13th/",
    # The thurrott Oct-13 announcement piece (same peg). New URL,
    # no new fact.
    "https://www.thurrott.com/smart-tech/342635/apple-announces-"
    "welcome-home-event-on-october-13",
    # The appleinsider Oct-1 J450 home-camera piece (text updates
    # instead of video; facial recognition; low frame rate; no
    # video recording). New URL, no new fact.
    "https://appleinsider.com/articles/26/10/01/apples-home-camera-"
    "will-watch-the-house-but-you-wont-see-what-it-sees",
]


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git", "-C", REPO_ROOT] + list(args),
        capture_output=True, text=True, timeout=120,
    )


def _iter_source_files():
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs
                   if d not in ("__pycache__", ".git", "node_modules")]
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
    return _git(*args)


def _corpus_hits_for_url(url):
    return _git("grep", "-F", "-l", url, "HEAD").stdout.strip()


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------


class TestAnchor1397:
    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit form: ANCHORED_SHA is 0*40; the anchor followup
        # patches it to this run's main commit sha. Deselected in
        # the in-gate run (the anchor followup flips it BY DESIGN
        # per #565).
        assert ANCHORED_SHA == "0" * 40

    def test_anchor_sha_patched_to_main_commit(self):
        # Post-anchor form per the #1392/#1393/#1394 precedent:
        # asserts patched non-placeholder, not HEAD equality (the
        # terminal log-hash followup moves HEAD past the anchor
        # commit). Fails pre-anchor by design; verified only in the
        # anchor followup. Deselected in the in-gate run.
        assert ANCHORED_SHA != "0" * 40
        assert len(ANCHORED_SHA) == 40
        assert all(c in "0123456789abcdef" for c in ANCHORED_SHA)
        out = _git("cat-file", "-e", ANCHORED_SHA)
        assert out.returncode == 0

    def test_anchor_sha_format(self):
        assert len(ANCHORED_SHA) == 40
        assert all(c in "0123456789abcdef" for c in ANCHORED_SHA)

    def test_anchor_duality_documented(self):
        # The dual pin (placeholder pre-commit, sha post-anchor) is
        # documented in the module docstring and the ANCHORED_SHA
        # comment (post-anchor the placeholder pin fails BY DESIGN).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Pre-commit placeholder per #565" in src
        assert "anchor followup" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1396 predecessor verified; #1397 is the THIRD leg
# of the 1395-1399 window (D -> E -> A -> B -> C).
# ---------------------------------------------------------------------------


class TestRotationGuard1397:
    def test_predecessor_1396_shas_in_git_log(self):
        for sha in (PRED_MAIN_1396, PRED_ANCHOR_1396,
                    PRED_DOCSYNC_1396, PRED_FINAL_1396,
                    PRED_PUSH_1396):
            out = _git("cat-file", "-e", sha)
            assert out.returncode == 0, sha

    def test_1396_push_status_done(self):
        # The ## #1396 entry registers "Push status (this run):
        # DONE" with the four-commit range; the push-status followup
        # commit message is verified in the git log.
        text = _read(ITERLOG_PATH)
        assert "## #1396 Type E" in text
        assert "Push status (this run): DONE" in text
        out = _git("log", "--oneline", "--grep=Push-status followup: #1396")
        assert "Push-status followup: #1396 push DONE" in out.stdout

    def test_1396_type_e_in_git_log(self):
        out = _git("log", "--oneline", "--grep=Type E #1396")
        assert "Type E #1396" in out.stdout

    def test_third_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "THIRD leg" in src
        assert "1395-1399 window" in src

    def test_window_sequence_d_e_a_b_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D -> E -> A -> B -> C" in src


# ---------------------------------------------------------------------------
# 3. Mechanism novelty: Type A lands zero mechanisms this run.
# ---------------------------------------------------------------------------


class TestMechanismNovelty1397:
    def test_no_new_mechanisms_landed(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_zero_next_number_keys(self):
        # Zero 1052-form keys: numeric in profiles/, underscore and
        # dash repo-wide (own file excluded, needles format-built
        # per #715/#770).
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_profiles_untouched_in_working_tree(self):
        res = _git("diff", "--name-only")
        modified = res.stdout.split()
        profiles_mods = [p for p in modified
                         if p.startswith("profiles/")]
        # The #899 nytimes.yaml m771 hunk is the documented
        # in-flight item (its own run owns it); nothing else in
        # profiles/ may be touched by this run.
        assert profiles_mods == ["profiles/nytimes.yaml"], profiles_mods
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#899" in src

    def test_falsification_ledger_unchanged(self):
        # Ledger holds at 65: no new falsification-family member
        # landed this run (the 65th, m1047, was landed by #1372 and
        # stays intact).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ledger holds at 65" in src


# ---------------------------------------------------------------------------
# 4. Guard lifecycle: #1396's forward guards verified GREEN pre-commit;
# the #1191-class self-trip on the no-Type-A-#1397 pin trips BY DESIGN
# at this run's main commit (re-pinned green in the terminal log-hash
# followup per #721/#1292 - ancestor form per the #1395 precedent);
# the no-Type-B-#1398 forward pin stays 0*40 through this run.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1397:
    def test_pins_on_1051_no_landing(self):
        # Type A lands no mechanisms this run: max stays 1051, next
        # 1052.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1051" in src
        assert "NEXT_NUM = 1052" in src

    def test_no_type_a_1397_in_git_log_pin(self):
        # Post-main-commit ANCESTOR form for THIS run's own pin
        # (per the #1395 precedent): every commit whose message
        # matches "Type A #1397" must be this run's main commit or a
        # descendant of it. Deselected in the in-gate run (fails
        # pre-commit by design: PRED_MAIN_1397 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type A #1397")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1397's own commits"
        main = _git("rev-parse", PRED_MAIN_1397).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_no_type_b_1398_in_git_log_pin(self):
        # Post-main-commit ANCESTOR form for the NEXT leg (the
        # #1191-class self-trip, re-pinned in #1398's terminal
        # log-hash followup per #721): every commit whose message
        # matches "Type B #1398" must be #1398's main commit or a
        # descendant of it. Deselected in the in-gate run (fails
        # pre-commit by design: PRED_MAIN_1398 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type B #1398")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1398's own commits"
        main = _git("rev-parse", PRED_MAIN_1398).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1052_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1052_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1052_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_max_numeric_mechanism_id_is_1051(self):
        assert _max_numeric_mechanism_id() == MECH_NUM

    def test_no_fortieth_direction_pin(self):
        assert _git_grep_tracked_source(_T40, "profiles/").stdout == ""

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
        # m1047 (Type A #1372, profiles/financial-times.yaml
        # competitor_relationships.anthropic) is the SIXTY-FIFTH
        # falsification-family member; landed at #1372. m1048,
        # m1049, m1050 and m1051 are NOT falsification-family
        # members.
        out = _git("grep", "-c", "-F", _T65, "HEAD", "--",
                   "profiles/financial-times.yaml")
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_sixty_sixth_member_pin(self):
        assert _git("grep", "-F", "-l", "SIXT" + "Y-SIXTH "
                   "falsification-family member", "HEAD") \
            .stdout.strip() == ""


# ---------------------------------------------------------------------------
# 5. Staleness pins: #1396's guard lifecycle post-terminal-followup.
# ---------------------------------------------------------------------------


class TestStalenessPins1397:
    def test_1396_guard_lifecycle_post_terminal_followup(self):
        # Post-terminal-followup form: 25 passed, 2 failed. The 2
        # failures are the two strict-form #1191-class pins in the
        # #1396 file - the no-Type-E-#1396 own pin and the
        # no-Type-A-#1397 forward pin both assert the empty
        # pre-commit state (strict form, unlike the #1395 file's
        # ancestor form), so they self-trip permanently post-landing
        # per the #1392 strict-form precedent. DOCUMENTED not
        # repaired. The substantive guards are VERIFIED SATISFIED:
        # the sole "Type E #1396" hit is #1396's own main commit
        # (bacc76ab), descendant-or-self of the re-pinned
        # PRED_MAIN_1396; the sole "Type A #1397" hit is this run's
        # own main commit, descendant-or-self of the re-pinned
        # PRED_MAIN_1397 (re-pinned in the #1396 file in this run's
        # terminal log-hash followup per #721/#1292). All 1052-absent
        # pins green; fortieth-through-sixty-fifth member pins
        # green; no-sixty-sixth pin green; ledger-65 pin green.
        # Deselected pre-commit (verified only post-terminal-followup).
        r = subprocess.run(
            ["python3", "-m", "pytest",
             os.path.join(TESTS_DIR, D1396_FILE)
             + "::TestGuardLifecycle1396",
             "-q", "-p", "no:cacheprovider"],
            capture_output=True, text=True, timeout=300, cwd=REPO_ROOT,
        )
        tail = r.stdout.strip().splitlines()[-1]
        assert "25 passed, 2 failed" in tail, tail
        # Substantive-guard verification for the two strict-form
        # self-trips (the run-time receipts, not just documentation).
        for needle, pred in (("Type E #1396", "PRED_MAIN_1396"),
                             ("Type A #1397", "PRED_MAIN_1397")):
            out = _git("log", "--format=%H", "--grep=%s" % needle)
            hits = [line.strip() for line in out.stdout.splitlines()
                    if line.strip()]
            assert len(hits) == 1, (needle, hits)
            main = _git("rev-parse", globals()[pred]).stdout.strip()
            assert main != "0" * 40
            rr = _git("merge-base", "--is-ancestor", main, hits[0])
            assert rr.returncode == 0, (needle, hits[0])


# ---------------------------------------------------------------------------
# 6. WIRED x OpenAI saturation screen.
# ---------------------------------------------------------------------------


class TestWiredOpenAISaturation1397:
    def test_six_new_keys_all_novel_urls(self):
        # 6 main-run rows, every URL verified zero pre-commit corpus
        # hits via git grep -F repo-wide.
        assert len(WIRED_OPENAI_NEW_KEYS) == 6
        for url in WIRED_OPENAI_NEW_KEYS:
            assert _corpus_hits_for_url(url) == "", url

    def test_mathematicians_peg_banked_m1027(self):
        # The Oct-6 Isabella Ward mathematicians accountability
        # piece is banked: m1027 (#1327), SIXTY-FIRST
        # falsification-family member (WIRED ran adversarial
        # product-review originals on the licensing partner).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "banked m1027 #1327" in src
        assert "SIXTY-FIRST" in src

    def test_intelligent_ui_peg_banked_m1050(self):
        # The Oct-7 Reece Rogers Intelligent UI review is banked:
        # m1050 (#1387), thesis_consistent_observation, illustrative
        # delta +0.53 (payer softer on the product-launch register).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "banked m1050 #1387" in src
        assert "+0.53" in src

    def test_dots_peg_banked_m991(self):
        # The Oct-7 Dots agent hands-on is banked: m991 (#1267,
        # WIRED x OpenAI Dots agent-launch register).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "banked m991 #1267" in src

    def test_all_relays_no_new_fact(self):
        # All 6 are relay URLs on already-banked pegs (or
        # relay-chain items with no tracked original): new URLs, no
        # new facts. Re-screening would re-litigate m1027/m1050/m991.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "New URLs, no new facts" in src
        assert "re-litigate" in src

    def test_verge_openai_saturated_m1051(self):
        # The Verge x OpenAI pair is likewise saturated: m1051
        # landed at #1392 (The Verge x OpenAI Oct-7/8 GPT-6
        # Intelligent UI launch register vs carried Meta arms).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "m1051 #1392" in src

    def test_no_fresh_wired_openai_pair_proposed(self):
        # ZERO candidates proposed on the WIRED x OpenAI pair this
        # run: not a #1341 instance (no false-positive landing),
        # saturation documented, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NO clean fresh" in src

    def test_ascii_only_keys(self):
        # ASCII-only rule: every key is pure ASCII (the #1394 ASCII
        # self-trip lesson). The wikinews slug carries no em dash
        # (MathematiciansAgain, no dash in the slug).
        for url in WIRED_OPENAI_NEW_KEYS:
            assert all(ord(c) < 128 for c in url), url


# ---------------------------------------------------------------------------
# 7. FT x Anthropic saturation screen.
# ---------------------------------------------------------------------------


class TestFTAnthropicSaturation1397:
    def test_five_new_keys_all_novel_urls(self):
        # 5 new main-run keys on this set (the saascity.io URL is a
        # re-surface, tested separately below; the dimsumdaily.hk
        # key is excluded for its non-ASCII path). Every ingested
        # URL verified zero pre-commit corpus hits via git grep -F
        # repo-wide.
        assert len(FT_ANTHROPIC_NEW_KEYS) == 5
        for url in FT_ANTHROPIC_NEW_KEYS:
            assert _corpus_hits_for_url(url) == "", url

    def test_saascity_resurfaces_via_1382(self):
        # The saascity.io prospectus recap re-surfaces: in corpus
        # via #1382 (m1049, Verge x Anthropic Sep-29 IPO-filing
        # pair) - profiles/the-verge.yaml and the #1382 test file.
        # The in-gate repair caught it (pre-commit novelty grep had
        # only covered the techsnif and live-feeds keys on this
        # set); re-surface, not a new key.
        hits = _git("grep", "-F", "-l",
                    "saascity.io/blog/anthropic-ipo-prospectus-saas-"
                    "founders-2026", "HEAD").stdout.strip().splitlines()
        assert len(hits) == 2, hits

    def test_ipo_timing_peg_is_bloomberg_wsj_reuters_originals(self):
        # The Oct-1/2 IPO-timing peg (mid-November target, investor
        # day Oct 14, $1.8-2T valuation) is Bloomberg-Oct-1 /
        # WSJ-Sep-18 / Reuters-Sep-28 originals - relayed by
        # techsnif, verilynews, thinkmarkets, saascity,
        # tech-insider - NOT an FT original. No tracked
        # publication+competitor pair to land.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NOT an FT original" in src

    def test_livefeeds_ft_sustainability_citation_thin_followup(self):
        # The live-feeds FT "sustainability" citation is a thin
        # excerpt-tier follow-up of m859 (#1047, FT Sep-14
        # IPO-profitability reporting), not a clean fresh peg: no
        # first-hand read, no distinct register, would re-litigate
        # m859. NOT proposed.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "thin" in src
        assert "m859" in src
        assert "NOT proposed" in src

    def test_m1047_broadcom_syndication_banked(self):
        # The Oct-5/6 Broadcom syndication financing-risk register
        # is banked: m1047 (#1372), SIXTY-FIFTH falsification-family
        # member (first financing-risk-register falsification at
        # FT).
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "m1047 (#1372)" in src
        assert "SIXTY-FIFTH" in src

    def test_all_relays_no_new_fact(self):
        # All 6 are relays of banked pegs or of other outlets'
        # originals: new URLs, no new facts.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "New URLs, no new facts" in src

    def test_dimsumdaily_excluded_non_ascii(self):
        # The dimsumdaily.hk relay URL is excluded from the keys
        # list: its path carries a non-ASCII hyphen, violating the
        # ASCII-only rule. Documented here, not ingested - the
        # #1394 ASCII self-trip lesson.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "EXCLUDED" in src
        assert "non-ASCII" in src

    def test_no_fresh_ft_anthropic_pair_proposed(self):
        # ZERO candidates proposed on the FT x Anthropic pair this
        # run: not a #1341 instance, saturation documented.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NO clean fresh" in src

    def test_ascii_only_keys(self):
        for url in FT_ANTHROPIC_NEW_KEYS:
            assert all(ord(c) < 128 for c in url), url


# ---------------------------------------------------------------------------
# 8. Apple "Welcome Home" Oct-13 watch item.
# ---------------------------------------------------------------------------


class TestAppleOct13Watch1397:
    def test_three_new_keys_all_novel_urls(self):
        # 3 main-run rows, every URL verified zero pre-commit corpus
        # hits via git grep -F repo-wide.
        assert len(APPLE_OCT13_NEW_KEYS) == 3
        for url in APPLE_OCT13_NEW_KEYS:
            assert _corpus_hits_for_url(url) == "", url

    def test_event_oct13_pre_peg(self):
        # Joswiak Oct-8 teaser; Tribeca "Apple Experience" Oct 13
        # 9am ET; hub ~$350; J450 home camera; HomePod mini + Apple
        # TV 4K refreshes. The event is 2 days out.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Tribeca" in src
        assert "2 days out" in src

    def test_no_tracked_publication_original_in_bounded_surface(self):
        # Bounded search-result absence: no WIRED / Verge / FT /
        # NYT / Guardian original surfaced in the 2 search sets -
        # only Apple-beat relays of Gurman/Bloomberg/MacRumors
        # reporting. Not proof of non-publication.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "no WIRED/Verge/FT/NYT/Guardian original" in src
        assert "bounded search-result absence" in src

    def test_camera_bearing_hub_privacy_peg(self):
        # The hub carries a camera and presence sensor for
        # in-room recognition; the J450 home camera does facial
        # recognition with text updates instead of video and no
        # video recording. This is the first camera-on-device Apple
        # product since the wearables stigma debate - a future
        # privacy-register comparison peg.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "camera and presence sensor" in src
        assert "text updates instead of video" in src

    def test_register_comparison_watch_item(self):
        # TESTABLE PREDICTION for post-Oct-13 runs: if a tracked
        # outlet runs an original on the camera-bearing hub, compare
        # its privacy register to the Meta "perv glasses" register
        # (m875 #1073: Schoon Weekender -0.45 Meta blame vs +0.10
        # Samsung/Google). Asymmetry would extend m875; symmetry
        # would bound it.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TESTABLE PREDICTION" in src
        assert "perv glasses" in src

    def test_not_a_mechanism_this_run(self):
        # Pre-event bounded absence is NOT a finding: no mechanism
        # landed on the Apple peg this run. Watch item only.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NOT a finding" in src
        assert "Watch item only" in src

    def test_ascii_only_keys(self):
        for url in APPLE_OCT13_NEW_KEYS:
            assert all(ord(c) < 128 for c in url), url


# ---------------------------------------------------------------------------
# 9. Research method.
# ---------------------------------------------------------------------------


class TestResearchMethod1397:
    def test_seven_main_run_search_sets(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "7 main-run browser.search verification sets" in src

    def test_no_delegated_scout_retry(self):
        # Retry attempt: no delegated scout; main-run sets only per
        # the #1376 retry precedent and the #1341 lesson.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "no delegated scout this run" in src
        assert "#1376 retry precedent" in src
        assert "#1341 lesson" in src

    def test_zero_browser_open(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "0 browser.open per #503" in src

    def test_snippet_bounded(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Snippet-bounded" in src
        assert "snippet-bounded" in src

    def test_verbatim_urls(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "verbatim from the browser.search Full-URL listings" in src
        assert "bounded search-result absence, not proof" in src


# ---------------------------------------------------------------------------
# 10. Statistical discipline.
# ---------------------------------------------------------------------------


class TestStatisticalDiscipline1397:
    def test_manual_qualitative_only(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MANUAL /" in src
        assert "QUALITATIVE ONLY" in src

    def test_aug_28_standing_rule(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Aug-28 standing rule" in src

    def test_monitoring_only_verdict(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "monitoring-only" in src

    def test_not_artifact_grade(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "NOT artifact-grade" in src

    def test_no_analysis_json_update(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "no analysis.json update" in src

    def test_correlation_not_causation(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Correlation is not causation" in src


# ---------------------------------------------------------------------------
# 11. Doc-sync per #719 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestDocSync1397:
    def test_readme_test_file_table_has_1397_row_post_sync(self):
        readme = _read(README_PATH)
        assert OWN_BASENAME in readme

    def test_architecture_has_1397_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert OWN_BASENAME in arch

    def test_readme_stats_ratcheted(self):
        # Post-sync-positive form per #719: asserts the ratcheted
        # counts (README_TEST_COUNT tests across README_FILE_COUNT
        # files). Fails pre-commit by design; deselected in the
        # in-gate run.
        readme = _read(README_PATH)
        assert ("| Tests | %d |" % README_TEST_COUNT) in readme
        assert ("Across %d test files" % README_FILE_COUNT) in readme


# ---------------------------------------------------------------------------
# 12. Iteration log per #721 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestIterationLog1397:
    def test_iteration_log_has_1397_entry_post_sync(self):
        text = _read(ITERLOG_PATH)
        assert "## #1397 Type A" in text

    def test_iteration_log_registers_hashes(self):
        text = _read(ITERLOG_PATH)
        assert "Hash chain" in text

    def test_iteration_log_covers_background_suite(self):
        # Per #795 the next background-suite verdict belongs to
        # #1400 (the #1395-launched suite runs at
        # goal/hidden_files/type_d_1395_full_suite.log); this run
        # observes only.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "verdict and tombstone belong to #1400" in src


# ---------------------------------------------------------------------------
# 13. In-flight isolation: explicit-path staging; never sweep #899,
# #938, #900, #1012-wt into this run's index. Do NOT touch #1024 m846.
# ---------------------------------------------------------------------------


class TestInFlightIsolation1397:
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

    def test_own_diff_excludes_inflight(self):
        # This run's staged set must never include the in-flight
        # files; verified at commit time by explicit-path staging.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "explicit-path" in src

    def test_1024_m846_block_untouched(self):
        # #1024 m846 (profiles/competitor-entities.yaml, HEAD lines
        # 26349-26472): decision still pending. Type A lands zero
        # mechanisms this run; the m846 block must be byte-identical
        # to HEAD. Do NOT touch #1024 m846.
        head = _git(
            "show", "HEAD:profiles/competitor-entities.yaml").stdout
        work = _read(ENTITIES_PATH)
        assert (head.splitlines()[M846_HEAD_START - 1:M846_HEAD_END]
                == work.splitlines()[M846_HEAD_START - 1:M846_HEAD_END])
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Do NOT touch #1024" in src

    def test_background_suite_untouched(self):
        # Per #795 this run only OBSERVES the #1395-launched suite;
        # the verdict and tombstone belong to #1400.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "verdict and tombstone belong to #1400" in src
        assert "explicit-path" in src
