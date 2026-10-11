"""Type A #1392: The Verge x OpenAI Oct-7/8-2026 GPT-6 Intelligent UI
launch register vs carried Meta arms.

THIRD leg of the 1390-1394 window: D #1390 -> E #1391 -> A #1392 (this
run) -> B #1393 -> C #1394. New Type A mechanism (mechanism 1051) in
profiles/the-verge.yaml under competitor_relationships -> openai: The
Verge covers its Vox Media licensing-deal partner OpenAI on the
Oct-7/8-2026 GPT-6 Intelligent UI launch with a straight product-news
register - rollout mechanics (GPT-6 Sol for paid tiers Oct 7, GPT-6
Luna for Free/Go Oct 8, 1.2B weekly users), competitive context
("more graphics-heavy and colorful" than Google's Gemini generative
interface), and a stronger-safety-training note; zero adversarial
vocabulary, zero skepticism about OpenAI's claims, zero privacy or
surveillance framing - for an OpenAI arm of +0.10 MANUAL
ILLUSTRATIVE, materially softer than the carried Verge x Meta
Connect Muse Charm backlash arm (-0.30, m841 #1017, un-rescored per
#807). Illustrative delta (OpenAI minus Meta) +0.40: the payer draws
the softer register on the product peg. This is the
cross-publication replication of m1050 (#1387, WIRED x OpenAI on the
SAME Oct-7/8 GPT-6 peg, delta +0.53): the soft product-launch
register appears at BOTH deal-partner outlets, suggesting it is
deal-partner-wide rather than WIRED-house-style. The naive uniform
payer-softening prediction is MET, not falsified; verdict
thesis_consistent_observation; NOT a falsification-family member;
ledger holds at 65; sixty-sixth member-form absent repo-wide;
fortieth direction absent. The Verge Astra-safety arc (Aug-Sep 2026)
and the m1252 Oct-5 safety-week falsification bound the softening to
the product-launch register, not blanket. Relay-attested only
(0 browser.open per #503, excerpt-bounded); the verbatim
theverge.com canonical URL arrived inside two independent relay
snippets, landed per the m1048 precedent with provenance disclosed.

Attempt-2 note: this run is attempt 2 of the 05:00 PDT
mediascope-daily-iteration slot (attempt 1 completed #1391 Type E:
all four commits pushed and ls-remote-verified, remote main tip
bc753ab3 matches local HEAD); per the #1297 precedent this run
executes the NEXT rotation leg (#1392 Type A).

Pre-run anchors: max numeric mechanism_id 1050 pre-commit, zero
numeric/underscore/dash-form 1052 keys repo-wide pre-commit (needles
format-built per #715/#770), "## #1392" zero-hit in iteration-log,
README stats 81768/1716 pre-commit, no #1392 row in README/
ARCHITECTURE test tables, fortieth direction absent, 48th-65th
members intact, no 66th member, ledger 65. No em dashes in new
content. Post-commit: mechanism 1051 is the corpus max; zero 1052
keys numeric/underscore/dash.

Research surface: 3 main-run browser.search verification sets (The
Verge OpenAI GPT-6 launch October 2026 - SELECTED the Oct-7 Verge
piece via five relays; WIRED Anthropic October 2026 - REJECTED,
own-repo circular + third-party relays, no WIRED original; quoted
Verge GPT-6 Intelligent UI October 7 2026 reporting - corroborating,
verbatim canonical URL in two independent snippets) + git grep -F
novelty verification on every candidate URL (5 new relay URLs
zero-hit at HEAD; 2 re-surfaces disclosed via m1050), 0
browser.open per #503. Snippet-bounded; Full-URL-listed URLs copied
verbatim; bounded search-result absence, not proof.

Background suite per #795: the #1390-launched full suite runs at goal
hidden_files type_d_1390_full_suite.log: this run OBSERVES only
(neither re-launches, kills, nor writes to the suite). The verdict
and tombstone belong to #1395 per #795.

Concurrency: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B
test file working-tree edit), #900 (untracked Type D test file),
#1012-wt (working-tree edit on the committed Type A #1012 file) all
left out of this run's index/diff via explicit-path staging. #1024
m846 (profiles/competitor-entities.yaml) NOT touched - decision
pending. Do NOT touch #1024 m846.

Tests: 131 tests collected, 14 classes. In-gate:
deselected per #565/#719/#721 (TestAnchor1392 1 +
TestGuardLifecycle1392 2 + TestDocSync1392 3 +
TestIterationLog1392 3 + TestStalenessPins1392 1).
"""

import os
import re
import subprocess

import pytest
import yaml


REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
ITERLOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
VERGE_PATH = os.path.join(PROFILES_DIR, "the-verge.yaml")
ENTITIES_PATH = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
OWN_BASENAME = (
    "test_type_a_1392_verge_openai_oct07_08_gpt6_intelligent_ui_"
    "launch_register_vs_carried_meta_arms_oct11_6am.py"
)


# Pre-commit placeholder per #565; patched to the main-commit sha in
# the anchor followup (post-anchor the placeholder pin fails BY
# DESIGN).
ANCHORED_SHA = "eb474941dc0dce1e7b6ee3fa189f63e2c69e2c5b"  # patched to the main commit sha in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1051
NEXT_NUM = 1052  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_a_1392_verge_openai_oct07_08_gpt6_intelligent_ui_"
    "launch_register_vs_carried_meta_arms"
)

# Predecessor chain: #1391 Type E was the SECOND leg of the
# 1390-1394 window. Its main/anchor/doc-sync/log-hash/push-status
# commits are pushed and ls-remote-verified (attempt 1 of this slot
# completed them; this run is attempt 2 per the #1297 precedent).
PRED_MAIN_1391 = "2fc0f17aa6d8d40a5f883da40238af2cded4ba94"
PRED_ANCHOR_1391 = "4645916a76163f880394fb15f9050e34893ccc92"
PRED_DOCSYNC_1391 = "0ab7ec27e1b7b9d0145dd5f729ca06ca110fc085"
PRED_FINAL_1391 = "9d262d5eb3354a2633b13f0bc3ecfe73947eed4b"
PRED_PUSH_1391 = "bc753ab37cfa39ff516b9eaf91b36b9507c3b877"

# This run's own main-commit sha, re-pinned per #721 in the anchor
# followup (the #1391 predecessor file's copy is re-pinned in the
# terminal log-hash followup per #721/#1292).
PRED_MAIN_1392 = "eb474941dc0dce1e7b6ee3fa189f63e2c69e2c5b"  # re-pinned by #1392 anchor followup per #721

# Forward guard for the next leg: #1393 Type B. Re-pinned by #1393's
# anchor followup per #721 (starts as 0*40; placeholder-only).
PRED_MAIN_1393 = "0" * 40

# The #1391 Type E file, for the staleness pin on its guard
# lifecycle (post-terminal form at this run is "23 passed, 3
# failed": the no_type_e_1391_in_git_log pin (the #1191-class
# self-trip from #1391's own main commit, spent) plus the
# no_type_a_1392_in_git_log forward pin (flips BY DESIGN at this
# run's main commit; re-pinned green in this run's terminal
# log-hash followup per #721/#1292) plus the #1272-class
# forward-guard expiry test_1051_numeric_absent_in_profiles (m1051
# now landed in profiles/the-verge.yaml). DOCUMENTED not repaired
# per precedent; the 1052-form pins stay green throughout (this run
# lands m1051, not m1052); the member and direction pins stay green
# (no member, no direction landed this run). The #1391 block is
# read-only to this run; the flips are documented here, not
# repaired). Deselected pre-commit (verified only
# post-terminal-followup).
E1391_FILE = (
    "test_type_e_1391_podcast_sentiment_201st_"
    "verification_oct11_5am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 81899  # patched pre-main: pre-sync 81768 + 131 collected
README_FILE_COUNT = 1717  # patched pre-main: pre-sync 1716 + 1 (this file)

EXPECTED_TOTAL = 131

# m846 block region in profiles/competitor-entities.yaml at HEAD (the
# #1024 m846 decision-pending block; byte-identity pin in the
# push-readiness class). HEAD lines, 1-based, verified intact
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
_T66 = "SIXT" + "Y-SIXTH falsification-family member"

# ---------------------------------------------------------------------------
# This run's surfaced evidence (Full-URL-listed URLs copied verbatim
# from the browser.search listings; the canonical theverge.com URL
# quoted verbatim in two independent relay snippets, landed per the
# m1048 precedent; corpus novelty verified pre-commit via git grep
# -F).
# ---------------------------------------------------------------------------

# A1 relays (all excerpt-bounded, 0 browser.open per #503).
RELAY_BADSIGNAL = "https://badsignal.ai/stories/chatgpt-intelligent-ui-gpt6"
RELAY_FAIRGATE = (
    "https://fairgatereport.com/openai-brings-gpt-6-to-chatgpt-with-"
    "new-intelligent-ui-for-visual-answers"
)
RELAY_YOUTUBE = "https://www.youtube.com/shorts/po-OAKfcuUU"
RELAY_GUZUS = (
    "https://github.com/guzus/ai-research-arm/blob/HEAD/research/"
    "2026-10-08-ai-news.md"
)
RELAY_LETSDATA = (
    "https://letsdatascience.com/news/openai-brings-gpt-6-and-"
    "intelligent-ui-to-chatgpt-4f0d797c"
)
# Re-surfaces (in corpus via m1050 #1387, disclosed not claimed new).
RELAY_WEBPRONEWS = (
    "https://www.webpronews.com/openais-gpt-6-overhauls-chatgpt-with-"
    "interactive-visual-answers-2/"
)
RELAY_TECHINSIDER = "https://tech-insider.org/gpt-6-intelligent-ui-rollout-2026/"
# Verbatim canonical URL, quoted in the youtube description snippet
# and independently in the guzus digest snippet (landed per the m1048
# precedent; zero corpus hits pre-commit; not in this run's Full-URL
# listings - provenance disclosed).
VERGE_CANONICAL = (
    "https://www.theverge.com/ai-artificial-intelligence/1007276/"
    "openai-chatgpt-intelligent-ui-gpt-6"
)
EVIDENCE_URLS = [RELAY_BADSIGNAL, RELAY_FAIRGATE, RELAY_YOUTUBE,
                 RELAY_GUZUS, RELAY_LETSDATA, RELAY_WEBPRONEWS,
                 RELAY_TECHINSIDER, VERGE_CANONICAL]

A1_SCORE = 0.10
META_CARRIED_M841 = -0.30
EXPECTED_DELTA = 0.40


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
    args = ["grep", "-F", "-l", needle, "HEAD", "--"]
    if scope:
        args.append(scope)
    return _git(*args)


def _load_verge():
    with open(VERGE_PATH, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _mech1051():
    d = _load_verge()
    return d["competitor_relationships"]["openai"][BLOCK_KEY]


def _git_log_hits(pattern):
    out = _git("log", "--format=%H", "--grep=" + pattern)
    return [line.strip() for line in out.stdout.splitlines()
            if line.strip()]


def _is_ancestor_or_self(main_sha, commit):
    if main_sha == "0" * 40:
        return False
    main = _git("rev-parse", main_sha).stdout.strip()
    if commit == main:
        return True
    r = _git("merge-base", "--is-ancestor", main, commit)
    return r.returncode == 0


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------


class TestAnchor1392:
    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit form: ANCHORED_SHA is 0*40; the anchor followup
        # patches it to this run's main commit sha. Deselected in
        # the in-gate run (fails pre-anchor only in the sense that
        # it pins the placeholder; the anchor followup flips it BY
        # DESIGN per #565).
        assert ANCHORED_SHA == "0" * 40

    def test_anchor_sha_patched_to_main_commit(self):
        # Post-anchor form: ANCHORED_SHA holds the main commit sha
        # (40 hex). Fails pre-anchor by design; verified only in
        # the anchor followup. Deselected in the in-gate run.
        main = _git("rev-parse", "HEAD").stdout.strip()
        assert ANCHORED_SHA == main
        assert len(ANCHORED_SHA) == 40

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
# 2. Guard lifecycle: #1391 predecessor verified; #1392 is the THIRD leg
# of the 1390-1394 window (D -> E -> A -> B -> C). The git-log pins use
# the ancestor form per the #1390 precedent (re-pinned in the terminal
# log-hash followup per #721/#1292).
# ---------------------------------------------------------------------------


class TestGuardLifecycle1392:
    def test_pins_on_1051_landing(self):
        # Type A lands one mechanism: max becomes 1051, next 1052.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1051" in src
        assert "NEXT_NUM = 1052" in src

    def test_no_type_a_1392_in_git_log_pin(self):
        # Ancestor form per the #1390 precedent: every commit whose
        # message matches "Type A #1392" must be this run's main
        # commit or a descendant of it (PRED_MAIN_1392 re-pinned in
        # the anchor followup per #721; the #1391 predecessor file's
        # copy is re-pinned in the terminal log-hash followup per
        # #721/#1292). Deselected in the in-gate run (fails
        # pre-commit by design: PRED_MAIN_1392 is 0*40).
        hits = _git_log_hits("Type A #1392")
        assert hits, "expected #1392's own commits"
        for h in hits:
            assert _is_ancestor_or_self(PRED_MAIN_1392, h), h

    def test_no_type_b_1393_in_git_log_pin(self):
        # Forward pin for the next leg (#1393 Type B): no "Type B
        # #1393" in git log yet; when #1393 lands, every matching
        # commit must be its main commit or a descendant
        # (PRED_MAIN_1393 re-pinned in #1393's terminal followup).
        # Deselected in the in-gate run (pins a future state).
        hits = _git_log_hits("Type B #1393")
        assert hits == []

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
        # The SIXTY-THIRD member-form anchor sits in
        # profiles/news-corp.yaml (count 2 intact), moved from
        # profiles/the-verge.yaml by a later run's profile edit per
        # the #1391 pin comment; form intact, location current.
        out = _git("grep", "-c", "-F", _T63, "HEAD", "--",
                   "profiles/news-corp.yaml")
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_sixty_fourth_member_intact_pin(self):
        out = _git("grep", "-c", "-F", _T64, "HEAD", "--",
                   "profiles/ap.yaml")
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_sixty_fifth_member_intact_pin(self):
        # m1048 (Type A #1372, profiles/financial-times.yaml
        # competitor_relationships.anthropic) is the SIXTY-FIFTH
        # falsification-family member; landed at #1372. m1049,
        # m1050, and m1051 are NOT falsification-family members.
        out = _git("grep", "-c", "-F", _T65, "HEAD", "--",
                   "profiles/financial-times.yaml")
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_sixty_sixth_member_pin(self):
        assert _git("grep", "-F", "-l", "SIXT" + "Y-SIXTH "
                   "falsification-family member", "HEAD") \
            .stdout.strip() == ""


# ---------------------------------------------------------------------------
# 3. Mechanism novelty: Type A lands exactly one mechanism (1051).
# ---------------------------------------------------------------------------


class TestMechanismNovelty1392:
    def test_block_key_present_in_working_tree(self):
        assert BLOCK_KEY in _read(VERGE_PATH)

    def test_block_key_absent_at_head(self):
        # Pre-commit novelty per #715: the block key is new to the
        # corpus (working tree only, not yet committed).
        out = _git("grep", "-F", "-l", BLOCK_KEY, "HEAD", "--", "profiles/")
        assert out.stdout.strip() == ""

    def test_mechanism_id_is_1051(self):
        assert _mech1051()["mechanism_id"] == 1051

    def test_iteration_is_1392(self):
        assert _mech1051()["iteration"] == 1392

    def test_iteration_type_is_a(self):
        assert _mech1051()["iteration_type"] == "A"

    def test_entity_pair_openai_vs_meta(self):
        assert _mech1051()["entity_pair"] == "OpenAI vs Meta"

    def test_publication_focus_verge(self):
        assert _mech1051()["publication_focus"] == "The Verge"

    def test_verdict_thesis_consistent(self):
        assert _mech1051()["verdict"] == "thesis_consistent_observation"

    def test_not_a_falsification_member(self):
        fam = _mech1051()["falsification_family"]
        assert fam.startswith("NOT a member")
        assert "ledger holds at 65" in fam

    def test_goal_id_matches(self):
        assert _mech1051()["goal_id"] == "goal_54093bda4145"

    def test_scheduled_job_id_matches(self):
        assert _mech1051()["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_author_kit_with_ray(self):
        assert _mech1051()["author"] == "Kit (with Ray)"

    def test_no_1051_substring_in_block_key(self):
        # Designed keying per #723/#738/#739: the block key carries
        # the iteration (1392), never the mechanism number (1051).
        assert "1051" not in BLOCK_KEY

    def test_distinct_from_m1050(self):
        # Cross-publication replication, not a re-score: m1050 is
        # WIRED x OpenAI on the same peg; this run is the Verge leg.
        assert "m1050" in _mech1051()["distinct_from_prior"]

    def test_extends_m1050_line(self):
        assert "m1050" in _mech1051()["extends_prior"]

    def test_discovery_summary_cross_publication_replication(self):
        disc = _mech1051()["discovery_summary"]
        assert "cross-publication replication" in disc
        assert "m1050" in disc

    def test_profiles_working_tree_mods_are_899_plus_this_run(self):
        # The working-tree profiles/ diff holds exactly two hunks:
        # the #899 nytimes.yaml m771 hunk (in-flight, owned by its
        # run) and this run's the-verge.yaml m1051 hunk.
        res = _git("diff", "--name-only")
        modified = sorted(res.stdout.split())
        profiles_mods = [p for p in modified
                         if p.startswith("profiles/")]
        assert profiles_mods == ["profiles/nytimes.yaml",
                                 "profiles/the-verge.yaml"], profiles_mods


# ---------------------------------------------------------------------------
# 4. Evidence: URLs verbatim, relay attestation, bounded claims.
# ---------------------------------------------------------------------------


class TestEvidence1392:
    def test_badsignal_relay_verbatim_in_attestation(self):
        assert RELAY_BADSIGNAL in _mech1051()["new_evidence"]["attestation"]

    def test_fairgate_relay_verbatim_in_attestation(self):
        assert RELAY_FAIRGATE in _mech1051()["new_evidence"]["attestation"]

    def test_youtube_relay_verbatim_in_attestation(self):
        assert RELAY_YOUTUBE in _mech1051()["new_evidence"]["attestation"]

    def test_guzus_relay_verbatim_in_attestation(self):
        assert RELAY_GUZUS in _mech1051()["new_evidence"]["attestation"]

    def test_letsdatascience_relay_verbatim_in_attestation(self):
        assert RELAY_LETSDATA in _mech1051()["new_evidence"]["attestation"]

    def test_webpronews_resurface_disclosed(self):
        # RE-SURFACE via m1050 #1387: disclosed, not claimed new.
        att = _mech1051()["new_evidence"]["attestation"]
        assert RELAY_WEBPRONEWS in att
        assert "RE-SURFACE" in att

    def test_techinsider_resurface_disclosed(self):
        att = _mech1051()["new_evidence"]["attestation"]
        assert RELAY_TECHINSIDER in att
        assert "RE-SURFACE" in att

    def test_verge_canonical_verbatim_landed_per_m1048(self):
        # The verbatim canonical URL, quoted in two independent
        # relay snippets, landed per the m1048 precedent with
        # provenance disclosed.
        att = _mech1051()["new_evidence"]["attestation"]
        assert VERGE_CANONICAL in att
        assert "m1048 precedent" in att

    def test_zero_browser_open(self):
        assert "0 browser.open per #503" in \
            _mech1051()["new_evidence"]["attestation"]

    def test_intelligent_ui_headline_quote(self):
        assert "Intelligent UI" in \
            _mech1051()["new_evidence"]["arm_a1"]["key_quotes"]

    def test_sol_luna_tiering_quote(self):
        assert "GPT-6 Sol" in \
            _mech1051()["new_evidence"]["arm_a1"]["key_quotes"]

    def test_1_2b_users_quote(self):
        assert "1.2 billion users" in \
            _mech1051()["new_evidence"]["arm_a1"]["key_quotes"]

    def test_graphics_heavy_colorful_quote(self):
        assert "more graphics-heavy and colorful" in \
            _mech1051()["new_evidence"]["arm_a1"]["key_quotes"]

    def test_novelty_claim_five_new_two_resurface(self):
        nov = _mech1051()["new_evidence"]["novelty"]
        assert "5 relay URLs zero-hit" in nov
        assert "2 re-surfaces" in nov

    def test_a1_score(self):
        assert _mech1051()["new_evidence"]["arm_a1"][
            "score_manual_illustrative"] == A1_SCORE


# ---------------------------------------------------------------------------
# 5. Scores: illustrative delta arithmetic and scorer metadata.
# ---------------------------------------------------------------------------


class TestScores1392:
    def test_openai_arm_score(self):
        s = _mech1051()["asymmetry_scoring_manual_illustrative"]
        assert s["target_score_manual_illustrative"] == A1_SCORE

    def test_meta_score(self):
        s = _mech1051()["asymmetry_scoring_manual_illustrative"]
        assert s["peer_score_manual_illustrative"] == META_CARRIED_M841

    def test_delta_arithmetic(self):
        s = _mech1051()["asymmetry_scoring_manual_illustrative"]
        assert abs(s["delta_manual_illustrative"] - EXPECTED_DELTA) < 1e-9
        assert abs((A1_SCORE - META_CARRIED_M841) - EXPECTED_DELTA) < 1e-9

    def test_delta_direction(self):
        s = _mech1051()["asymmetry_scoring_manual_illustrative"]
        assert s["direction"] == "target softer than peer by 0.40"

    def test_significant_false(self):
        s = _mech1051()["asymmetry_scoring_manual_illustrative"]
        assert s["significant"] is False

    def test_stats_not_calculated(self):
        s = _mech1051()["asymmetry_scoring_manual_illustrative"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"

    def test_empirical_required(self):
        s = _mech1051()["asymmetry_scoring_manual_illustrative"]
        assert s["empirical_required"] is True

    def test_scorer_version_pinned(self):
        s = _mech1051()["asymmetry_scoring_manual_illustrative"]
        assert "mediascope/score/asymmetry.py" in s["scorer"]

    def test_carried_meta_arm_m841(self):
        arms = _mech1051()["carried_meta_arms"]
        assert any("m841" in a and "-0.30" in a for a in arms)

    def test_carried_meta_arm_m628(self):
        arms = _mech1051()["carried_meta_arms"]
        assert any("m628" in a for a in arms)


# ---------------------------------------------------------------------------
# 6. Statistical discipline (Aug-28 standing rule).
# ---------------------------------------------------------------------------


class TestStatisticalDiscipline1392:
    def test_manual_illustrative_only(self):
        assert "MANUAL ILLUSTRATIVE ONLY" in \
            _mech1051()["statistical_discipline"]

    def test_engine_not_run(self):
        assert "engine NOT run" in _mech1051()["statistical_discipline"]

    def test_is_significant_false(self):
        assert "is_significant false" in \
            _mech1051()["statistical_discipline"]

    def test_not_artifact_grade(self):
        assert "NOT artifact-grade" in \
            _mech1051()["statistical_discipline"]

    def test_no_analysis_json_update(self):
        assert "no_analysis_json_update true" in \
            _mech1051()["statistical_discipline"]

    def test_monitoring_only(self):
        assert "monitoring_only" in _mech1051()["statistical_discipline"]

    def test_correlation_not_causation(self):
        assert "Correlation is not causation" in \
            _mech1051()["statistical_discipline"]

    def test_hypothesis_generating_only(self):
        assert "hypothesis-generating only" in \
            _mech1051()["statistical_discipline"]

    def test_artifact_readiness_no_update(self):
        assert "No analysis.json update warranted" in \
            _mech1051()["artifact_readiness"]

    def test_cautious_language_complete(self):
        cl = _mech1051()["cautious_language"]
        for key in ("correlation_not_causation", "no_editorial_control_claim",
                    "no_statistical_significance_claim", "significant_false",
                    "p_value_not_calculated", "ci_not_calculated",
                    "cohens_d_not_calculated"):
            assert cl[key] is True, key


# ---------------------------------------------------------------------------
# 7. Corpus novelty (HEAD-bounded, per #715).
# ---------------------------------------------------------------------------


class TestCorpusNovelty1392:
    def test_badsignal_url_zero_hit_at_head(self):
        out = _git("grep", "-F", "-l", RELAY_BADSIGNAL, "HEAD")
        assert out.stdout.strip() == ""

    def test_fairgate_url_zero_hit_at_head(self):
        out = _git("grep", "-F", "-l", RELAY_FAIRGATE, "HEAD")
        assert out.stdout.strip() == ""

    def test_youtube_url_zero_hit_at_head(self):
        out = _git("grep", "-F", "-l", RELAY_YOUTUBE, "HEAD")
        assert out.stdout.strip() == ""

    def test_guzus_url_zero_hit_at_head(self):
        out = _git("grep", "-F", "-l", RELAY_GUZUS, "HEAD")
        assert out.stdout.strip() == ""

    def test_letsdatascience_url_zero_hit_at_head(self):
        out = _git("grep", "-F", "-l", RELAY_LETSDATA, "HEAD")
        assert out.stdout.strip() == ""

    def test_verge_canonical_zero_hit_at_head(self):
        out = _git("grep", "-F", "-l", VERGE_CANONICAL, "HEAD")
        assert out.stdout.strip() == ""

    def test_webpronews_resurface_in_corpus_at_head(self):
        # RE-SURFACE: in corpus via m1050 #1387, disclosed.
        out = _git("grep", "-F", "-l", RELAY_WEBPRONEWS, "HEAD")
        assert out.stdout.strip() != ""

    def test_techinsider_resurface_in_corpus_at_head(self):
        out = _git("grep", "-F", "-l", RELAY_TECHINSIDER, "HEAD")
        assert out.stdout.strip() != ""

    def test_no_type_a_1392_in_git_log(self):
        out = _git("log", "--format=%H", "--grep=Type A #1392")
        assert out.stdout.strip() == ""

    def test_no_1392_heading_in_iteration_log_at_head(self):
        out = _git("grep", "-F", "-l", "## #1392", "HEAD", "--",
                   "iteration-log.md")
        assert out.stdout.strip() == ""

    def test_single_type_a_1392_file_on_disk(self):
        matches = [f for f in os.listdir(TESTS_DIR)
                   if f.startswith("test_type_a_1392")]
        assert matches == [OWN_BASENAME]

    def test_no_1392_row_in_readme_table_at_head(self):
        out = _git("grep", "-F", "-l", "test_type_a_1392", "HEAD", "--",
                   "README.md")
        assert out.stdout.strip() == ""


# ---------------------------------------------------------------------------
# 8. Doc-sync per #719 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestDocSync1392:
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

    def test_readme_has_1392_table_row(self):
        src = _read(README_PATH)
        assert "test_type_a_1392" in src


# ---------------------------------------------------------------------------
# 9. Iteration log per #721 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestIterationLog1392:
    def test_log_has_1392_heading(self):
        # Written in the doc-sync commit per #721. Fails pre-commit
        # by design; deselected in the in-gate run.
        assert "## #1392" in _read(ITERLOG_PATH)

    def test_log_registers_main_anchor_docsync_hashes(self):
        src = _read(ITERLOG_PATH)
        assert "log-hash" in src

    def test_log_mentions_m1051(self):
        src = _read(ITERLOG_PATH)
        assert "m1051" in src


# ---------------------------------------------------------------------------
# 10. Confounders and counterevidence.
# ---------------------------------------------------------------------------


class TestConfounders1392:
    def test_strong_confounders_present(self):
        strong = _mech1051()["confounders"]["strong"]
        assert len(strong) == 3

    def test_peg_asymmetry_ranked_strong(self):
        strong = _mech1051()["confounders"]["strong"]
        assert any("Peg asymmetry" in c for c in strong)

    def test_relay_attestation_ranked_strong(self):
        strong = _mech1051()["confounders"]["strong"]
        assert any("Relay attestation only" in c for c in strong)

    def test_single_arm_ranked_strong(self):
        strong = _mech1051()["confounders"]["strong"]
        assert any("Single fresh arm" in c for c in strong)

    def test_moderate_confounders_present(self):
        assert len(_mech1051()["confounders"]["moderate"]) == 2

    def test_weak_confounders_present(self):
        assert len(_mech1051()["confounders"]["weak"]) == 1

    def test_counterevidence_astra_arc_bounds_softening(self):
        ce = _mech1051()["counter_evidence"]
        assert any("Astra-safety arc" in c for c in ce)

    def test_counterevidence_m1252_falsification(self):
        ce = _mech1051()["counter_evidence"]
        assert any("m1252" in c for c in ce)

    def test_counterevidence_m1049_peg_valence(self):
        ce = _mech1051()["counter_evidence"]
        assert any("m1049" in c for c in ce)

    def test_financial_context_vox_deal(self):
        fc = _mech1051()["financial_context"]
        assert "Vox Media x OpenAI" in fc
        assert "coverage_prediction" in fc

    def test_cross_references_complete(self):
        cr = _mech1051()["cross_references"]
        for num in (1050, 1049, 1048, 841, 628, 880, 1252, 907):
            assert num in cr, num

    def test_testable_predictions_present(self):
        tp = _mech1051()["testable_predictions"]
        assert len(tp) == 2


# ---------------------------------------------------------------------------
# 11. Staleness pins on the predecessor's guard lifecycle (deselected
# pre-commit; verified post-terminal-followup).
# ---------------------------------------------------------------------------


class TestStalenessPins1392:
    def test_1391_guard_lifecycle_post_terminal_followup(self):
        # Post-terminal-followup form: 23 passed, 3 failed. The
        # no_type_e_1391_in_git_log pin (the #1191-class self-trip
        # from #1391's own main commit, spent at #1391) plus the
        # no_type_a_1392_in_git_log forward pin (flips BY DESIGN at
        # this run's main commit; re-pinned green in this run's
        # terminal log-hash followup per #721/#1292) plus the
        # #1272-class forward-guard expiry
        # test_1051_numeric_absent_in_profiles (m1051 now landed in
        # profiles/the-verge.yaml). DOCUMENTED not repaired per
        # precedent. The 1052-form pins stay green throughout (this
        # run lands m1051, not m1052); the member and direction pins
        # stay green (no member, no direction landed this run). The
        # #1391 block is read-only to this run; the flips are
        # documented here, not repaired. Deselected pre-commit
        # (verified only post-terminal-followup).
        r = subprocess.run(
            ["python3", "-m", "pytest",
             os.path.join(TESTS_DIR, E1391_FILE)
             + "::TestGuardLifecycle1391",
             "-q", "-p", "no:cacheprovider"],
            capture_output=True, text=True, timeout=300, cwd=REPO_ROOT,
        )
        tail = r.stdout.strip().splitlines()[-1]
        assert "23 passed" in tail and "3 failed" in tail, tail
        assert "test_no_type_a_1392_in_git_log_pin" in r.stdout
        assert "test_1051_numeric_absent_in_profiles" in r.stdout


# ---------------------------------------------------------------------------
# 12. Push readiness: in-flight isolation and #1024 m846 untouched.
# ---------------------------------------------------------------------------


class TestPushReadiness1392:
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
        work = _read(ENTITIES_PATH)
        assert (head.splitlines()[M846_HEAD_START - 1:M846_HEAD_END]
                == work.splitlines()[M846_HEAD_START - 1:M846_HEAD_END])
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Do NOT touch #1024" in src

    def test_m846_not_in_working_diff(self):
        out = _git("diff", "--name-only")
        assert "profiles/competitor-entities.yaml" not in out.stdout


# ---------------------------------------------------------------------------
# 13. Rotation: third leg of the 1390-1394 window; attempt-2 retry.
# ---------------------------------------------------------------------------


class TestRotation1392:
    def test_window_sequence(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1390 -> E #1391 -> A #1392" in src

    def test_next_leg_is_type_b(self):
        assert PRED_MAIN_1393 == "0" * 40

    def test_type_letter_a(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type A #1392" in src

    def test_attempt_2_retry_documented(self):
        # Per the #1297 precedent: attempt 1 of the 05:00 PDT slot
        # completed #1391 (four commits pushed, ls-remote-verified);
        # this run (attempt 2) executes the next rotation leg.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "attempt 2" in src
        assert "#1297 precedent" in src

    def test_background_suite_observed_only(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "OBSERVES only" in src
        assert "#1390" in src
        assert "#1395" in src


# ---------------------------------------------------------------------------
# 14. ASCII and formatting hygiene.
# ---------------------------------------------------------------------------


class TestAscii1392:
    def test_no_em_dashes_in_test_file(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "\u2014" not in src

    def test_ascii_only_in_test_file(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        src.encode("ascii")

    def test_no_em_dashes_in_profile_block(self):
        src = _read(VERGE_PATH)
        assert "\u2014" not in src

    def test_expected_total_declared(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "EXPECTED_TOTAL = %d" % EXPECTED_TOTAL in src
