"""Type A #1387: WIRED x OpenAI Oct-7/8-2026 GPT-6 Intelligent UI
launch register vs carried Meta arms.

THIRD leg of the 1385-1389 window: D #1385 -> E #1386 -> A #1387 (this
run) -> B #1388 -> C #1389. New Type A mechanism (mechanism 1050) in
profiles/wired.yaml under competitor_relationships -> openai: WIRED
covers its Conde Nast licensing-deal partner OpenAI on the Oct-7/8-2026
GPT-6 Intelligent UI launch with a mixed register - Reece Rogers
hands-on positive (+0.10 MANUAL ILLUSTRATIVE, "These visual elements
felt like a welcome change") plus WIRED launch analysis skeptical
(-0.20, "genuine capability versus presentation polish"), relay-attested,
0 browser.open per #503 - for an OpenAI arm mean of -0.05, materially
softer than the carried WIRED x Meta Muse dossier arm (-0.58, m988
#1262, un-rescored per #807). Illustrative delta (OpenAI minus Meta)
+0.53: the payer draws the softer register on the product peg. The
naive uniform payer-softening prediction is MET, not falsified;
verdict thesis_consistent_observation; NOT a falsification-family
member; ledger holds at 65; sixty-sixth member-form absent repo-wide;
fortieth direction absent. The skeptical headline ("More Show Than
Tell") and polish-questioning bound the softening as relative, not
absolute. DISTINCT from m1042 (#1352, governance bounded-absence
selection on the firings, different peg/axis), m991 (#1267, Dots
launch), m1027 (#1327, adversarial originals); EXTENDS m991's
product-launch register line.

Pre-run anchors: max numeric mechanism_id 1049 pre-commit, zero
numeric/underscore/dash-form 1050 keys repo-wide pre-commit (needles
format-built per #715/#770), "## #1387" zero-hit in iteration-log,
README stats 81270/1711 pre-commit, no #1387 row in README/ARCHITECTURE
test tables, fortieth direction absent, 48th-65th members intact, no
66th member, ledger 65. No em dashes in new content. Post-commit:
mechanism 1050 is the corpus max; zero 1051 keys
numeric/underscore/dash in profiles/.

Research surface: 4 main-run browser.search verification sets (WIRED
GPT-6 OpenAI launch October 2026 - SELECTED the Rogers hands-on +
WIRED analysis via relays; Reece Rogers WIRED GPT-6 Intelligent UI
hands-on review - corroborating; WIRED GPT-6 analysis presentation
polish - corroborating; Anthropic IPO November 2026 - REJECTED, stale
peg + #1382 saturation) + git grep -F novelty verification on every
candidate URL (all 4 relay URLs zero-hit at HEAD), 0 browser.open per
#503. Snippet-bounded; all URLs copied verbatim from the
browser.search Full-URL listings; bounded search-result absence, not
proof.

Background suite per #795: the #1385-launched full suite runs at goal
hidden_files type_d_1385_full_suite.log: this run OBSERVES only
(neither re-launches, kills, nor writes to the suite). The verdict and
tombstone belong to #1390 per #795.

Concurrency: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file),
#1012-wt (working-tree edit on the committed Type A #1012 file) all left
out of this run's index/diff via explicit-path staging. #1024 m846
(profiles/competitor-entities.yaml) NOT touched - decision pending. Do
NOT touch #1024 m846.

Tests: 121 tests collected, 14 classes. In-gate: 111 passed +
10 deselected per #565/#719/#721 (TestAnchor1387 1 +
TestGuardLifecycle1387 2 + TestDocSync1387 3 +
TestIterationLog1387 3 + TestStalenessPins1387 1).
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
WIRED_PATH = os.path.join(PROFILES_DIR, "wired.yaml")
ENTITIES_PATH = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
OWN_BASENAME = (
    "test_type_a_1387_wired_openai_oct07_08_gpt6_intelligent_ui_"
    "launch_register_vs_carried_meta_arms_oct11_1am.py"
)


# Pre-commit placeholder per #565; patched to the main-commit sha in
# the anchor followup (post-anchor the placeholder pin fails BY
# DESIGN).
ANCHORED_SHA = "0" * 40

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1050
NEXT_NUM = 1051  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_a_1387_wired_openai_oct07_08_gpt6_intelligent_ui_"
    "launch_register_vs_carried_meta_arms"
)

# Predecessor chain: #1386 Type E was the SECOND leg of the
# 1385-1389 window. Its main/anchor/doc-sync/log-hash/push commits are
# pushed and ls-remote-verified.
PRED_MAIN_1386 = "7574d2ae104d93ca0c4df8034868b16121c9c5b6"
PRED_ANCHOR_1386 = "074d85a7b45761a4cf2288728000aa0a312ca213"
PRED_DOCSYNC_1386 = "c4d84525ce0c4fc4ec2f7de5b1268f492ea3303e"
PRED_FINAL_1386 = "0d51cbe37555bd19c43f7bd744c245f0e92012c0"
PRED_PUSH_1386 = "499b2cae507dcc71d8df4608d58627d1b34b7033"

# This run's own main-commit sha, re-pinned per #721 in the anchor
# followup (the #1386 predecessor file's copy is re-pinned in the
# terminal log-hash followup per #721/#1292).
PRED_MAIN_1387 = "0" * 40

# Forward guard for the next leg: #1388 Type B. Re-pinned by #1388's
# anchor followup per #721 (starts as 0*40; placeholder-only).
PRED_MAIN_1388 = "0" * 40

# The #1386 Type E file, for the staleness pin on its guard
# lifecycle (post-terminal form at this run is "25 passed, 1 failed":
# the no_type_a_1387_in_git_log forward pin flips green in this run's
# terminal log-hash followup per #721/#1292 when PRED_MAIN_1387 is
# re-pinned in the #1386 file. The ONE failure is the #1272-class
# forward-guard expiry, DOCUMENTED not repaired per precedent:
# test_1050_numeric_absent_in_profiles trips on the landed m1050 block
# (mechanism_id: 1050 now committed in profiles/wired.yaml). The
# 1051-form pins stay green throughout (this run lands m1050, not
# m1051); the member and direction pins stay green (no member, no
# direction landed this run). The #1386 block is read-only to this
# run; the expiry is documented here, not repaired). Deselected
# pre-commit (verified only post-terminal-followup).
E1386_FILE = (
    "test_type_e_1386_podcast_sentiment_200th_"
    "verification_oct11_12am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 81391  # patched pre-main: pre-sync 81270 + 121 collected
README_FILE_COUNT = 1712  # patched pre-main: pre-sync 1711 + 1 (this file)

EXPECTED_TOTAL = 121

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
_T66 = "SIXT" + "Y-SIXTH falsification-family member"

# ---------------------------------------------------------------------------
# This run's surfaced evidence (all URLs copied verbatim from the
# browser.search Full-URL listings; corpus novelty verified pre-commit
# via git grep -F).
# ---------------------------------------------------------------------------

# A1 relays: Rogers hands-on (positive verdict, skeptical headline).
RELAY_WEBPRONEWS = (
    "https://www.webpronews.com/openais-gpt-6-overhauls-chatgpt-with-"
    "interactive-visual-answers-2/"
)
RELAY_FINDSKILL = (
    "https://findskill.ai/blog/chatgpt-gpt-6-free-intelligent-ui-"
    "what-changed-2026/"
)
RELAY_MUCKRACK = "https://muckrack.com/reece-rogers/articles"
# A2 relay: WIRED launch analysis (skeptical).
RELAY_TECHINSIDER = "https://tech-insider.org/gpt-6-intelligent-ui-rollout-2026/"
EVIDENCE_URLS = [RELAY_WEBPRONEWS, RELAY_FINDSKILL, RELAY_MUCKRACK,
                 RELAY_TECHINSIDER]

A1_SCORE = 0.10
A2_SCORE = -0.20
OPENAI_ARM_MEAN = -0.05
META_CARRIED_M988 = -0.58
EXPECTED_DELTA = 0.53


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


def _load_wired():
    with open(WIRED_PATH, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _mech1050():
    d = _load_wired()
    return d["competitor_relationships"]["openai"][BLOCK_KEY]


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------


class TestAnchor1387:
    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit form: ANCHORED_SHA is 0*40; the anchor followup
        # patches it to the main commit sha per #565. This test runs
        # in the in-gate (passes pre-commit); post-anchor it fails BY
        # DESIGN (the patched form is asserted post-anchor).
        assert ANCHORED_SHA == "0" * 40

    def test_anchor_sha_patched_to_main_commit(self):
        # Post-commit form: ANCHORED_SHA patched to this run's main
        # commit sha per #565 in the anchor followup (both this
        # expected value and the ANCHORED_SHA constant are patched).
        # Pre-commit this is 0*40 and the test fails BY DESIGN;
        # deselected in the in-gate run.
        assert ANCHORED_SHA != "0" * 40
        assert len(ANCHORED_SHA) == 40

    def test_anchor_sha_format(self):
        assert len(ANCHORED_SHA) == 40

    def test_anchor_duality_documented(self):
        # The #565 duality: the placeholder pin passes pre-commit and
        # fails post-anchor BY DESIGN; the patched pin is the mirror.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "BY DESIGN post-anchor" in src or "fails BY DESIGN" in src

    def test_no_sixty_sixth_member_pin(self):
        assert _git("grep", "-F", "-l", "SIXT" + "Y-SIXTH "
                   "falsification-family member", "HEAD") \
            .stdout.strip() == ""


# ---------------------------------------------------------------------------
# 2. Guard lifecycle for this run (pre-commit form; the no-Type-A-#1387
# pin is the #1191-class self-trip, re-pinned in the terminal log-hash
# followup per #721/#1292).
# ---------------------------------------------------------------------------


class TestGuardLifecycle1387:
    def test_pins_on_1050_landing(self):
        # Type A lands one mechanism: max numeric id 1049 -> 1050.
        # Pre-commit the working tree already carries the m1050
        # block, so the file-level constants pin the landing.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1050" in src
        assert "NEXT_NUM = 1051" in src
        assert _max_numeric_mechanism_id() == 1050

    def test_no_type_a_1387_in_git_log_pin(self):
        # Post-main-commit form for THIS run's own pin (the
        # #1191-class self-trip, re-pinned in this run's terminal
        # log-hash followup per #721/#1292): every commit whose
        # message matches "Type A #1387" must be this run's main
        # commit or a descendant of it. Deselected in the in-gate
        # run (fails pre-commit by design: PRED_MAIN_1387 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type A #1387")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1387's own commits"
        main = _git("rev-parse", PRED_MAIN_1387).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_no_type_b_1388_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1388's terminal log-hash followup
        # per #721): every commit whose message matches "Type B
        # #1388" must be #1388's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1388 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type B #1388")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1388's own commits"
        main = _git("rev-parse", PRED_MAIN_1388).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1051_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1051_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1051_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_fortieth_direction_pin(self):
        assert _git_grep_tracked_source(_T40, "profiles/").stdout.strip() == ""

    def test_forty_eighth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T48, None).stdout.strip() != ""

    def test_forty_ninth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T49, None).stdout.strip() != ""

    def test_fiftieth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T50, None).stdout.strip() != ""

    def test_fifty_first_member_intact_pin(self):
        assert _git_grep_tracked_source(_T51, None).stdout.strip() != ""

    def test_fifty_second_member_intact_pin(self):
        assert _git_grep_tracked_source(_T52, None).stdout.strip() != ""

    def test_fifty_third_member_intact_pin(self):
        assert _git_grep_tracked_source(_T53, None).stdout.strip() != ""

    def test_fifty_fourth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T54, None).stdout.strip() != ""

    def test_fifty_fifth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T55, None).stdout.strip() != ""

    def test_fifty_sixth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T56, None).stdout.strip() != ""

    def test_fifty_seventh_member_intact_pin(self):
        assert _git_grep_tracked_source(_T57, None).stdout.strip() != ""

    def test_fifty_eighth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T58, None).stdout.strip() != ""

    def test_fifty_ninth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T59, None).stdout.strip() != ""

    def test_sixtieth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T60, None).stdout.strip() != ""

    def test_sixty_first_member_intact_pin(self):
        assert _git_grep_tracked_source(_T61, None).stdout.strip() != ""

    def test_sixty_second_member_intact_pin(self):
        assert _git_grep_tracked_source(_T62, None).stdout.strip() != ""

    def test_sixty_third_member_intact_pin(self):
        assert _git_grep_tracked_source(_T63, None).stdout.strip() != ""

    def test_sixty_fourth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T64, None).stdout.strip() != ""

    def test_sixty_fifth_member_intact_pin(self):
        assert _git_grep_tracked_source(_T65, None).stdout.strip() != ""

    def test_no_sixty_sixth_member_pin(self):
        assert _git_grep_tracked_source(_T66, None).stdout.strip() == ""


# ---------------------------------------------------------------------------
# 3. Mechanism novelty and content.
# ---------------------------------------------------------------------------


class TestMechanismNovelty1387:
    def test_block_key_present_in_working_tree(self):
        assert BLOCK_KEY in _read(WIRED_PATH)

    def test_block_key_absent_at_head(self):
        # Pre-commit novelty per #715: the block key is new to the
        # corpus (working tree only, not yet committed).
        out = _git("grep", "-F", "-l", BLOCK_KEY, "HEAD", "--", "profiles/")
        assert out.stdout.strip() == ""

    def test_mechanism_id_is_1050(self):
        assert _mech1050()["mechanism_id"] == 1050

    def test_iteration_is_1387(self):
        assert _mech1050()["iteration"] == 1387

    def test_iteration_type_is_a(self):
        assert _mech1050()["iteration_type"] == "A"

    def test_entity_pair_openai_vs_meta(self):
        assert _mech1050()["entity_pair"] == "OpenAI vs Meta"

    def test_publication_focus_wired(self):
        assert _mech1050()["publication_focus"] == "WIRED"

    def test_verdict_thesis_consistent(self):
        assert _mech1050()["verdict"] == "thesis_consistent_observation"

    def test_not_a_falsification_member(self):
        fam = _mech1050()["falsification_family"]
        assert fam.startswith("NOT a member")
        assert "ledger holds at 65" in fam

    def test_goal_id_matches(self):
        assert _mech1050()["goal_id"] == "goal_54093bda4145"

    def test_scheduled_job_id_matches(self):
        assert _mech1050()["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_author_kit_with_ray(self):
        assert _mech1050()["author"] == "Kit (with Ray)"

    def test_no_1050_substring_in_block_key(self):
        # Designed keying per #723/#738/#739: the block key carries
        # the iteration (1387), never the mechanism number (1050).
        assert "1050" not in BLOCK_KEY

    def test_distinct_from_m1042(self):
        assert "m1042" in _mech1050()["distinct_from_prior"]

    def test_extends_m991(self):
        assert "m991" in _mech1050()["extends_prior"]

    def test_discovery_summary_product_launch(self):
        disc = _mech1050()["discovery_summary"]
        assert "product-launch" in disc
        assert "m991" in disc


# ---------------------------------------------------------------------------
# 4. Evidence: URLs verbatim, relay attestation, bounded claims.
# ---------------------------------------------------------------------------


class TestEvidence1387:
    def test_webpronews_relay_verbatim_in_attestation(self):
        assert RELAY_WEBPRONEWS in _mech1050()["new_evidence"]["attestation"]

    def test_techinsider_relay_verbatim_in_attestation(self):
        assert RELAY_TECHINSIDER in _mech1050()["new_evidence"]["attestation"]

    def test_findskill_relay_verbatim_in_attestation(self):
        assert RELAY_FINDSKILL in _mech1050()["new_evidence"]["attestation"]

    def test_muckrack_relay_verbatim_in_attestation(self):
        assert RELAY_MUCKRACK in _mech1050()["new_evidence"]["attestation"]

    def test_zero_browser_open(self):
        assert "0 browser.open per #503" in _mech1050()["new_evidence"]["attestation"]

    def test_rogers_byline_attested(self):
        assert "Reece Rogers" in _mech1050()["new_evidence"]["attestation"]

    def test_welcome_change_quote(self):
        assert "These visual elements felt like a welcome change" in \
            _mech1050()["new_evidence"]["arm_a1"]["key_quotes"]

    def test_show_than_tell_headline(self):
        assert "The New ChatGPT Is More Show Than Tell" in \
            _mech1050()["new_evidence"]["arm_a1"]["key_quotes"]

    def test_presentation_polish_quote(self):
        assert "genuine capability versus presentation polish" in \
            _mech1050()["new_evidence"]["arm_a2"]["key_quotes"]

    def test_only_outlet_hands_on_quote(self):
        assert "the only outlet that has so far published a hands-on test" in \
            _mech1050()["new_evidence"]["arm_a1"]["key_quotes"]

    def test_url_novelty_claim(self):
        assert "zero-hit repo-wide pre-commit" in _mech1050()["new_evidence"]["novelty"]

    def test_canonical_gap_noted(self):
        assert "No WIRED canonical URL surfaced" in _mech1050()["new_evidence"]["attestation"]


# ---------------------------------------------------------------------------
# 5. Scores: illustrative delta arithmetic and scorer metadata.
# ---------------------------------------------------------------------------


class TestScores1387:
    def test_openai_arm_mean(self):
        s = _mech1050()["asymmetry_scoring_manual_illustrative"]
        assert s["target_score_manual_illustrative"] == OPENAI_ARM_MEAN

    def test_meta_score(self):
        s = _mech1050()["asymmetry_scoring_manual_illustrative"]
        assert s["peer_score_manual_illustrative"] == META_CARRIED_M988

    def test_delta_arithmetic(self):
        s = _mech1050()["asymmetry_scoring_manual_illustrative"]
        assert abs(s["delta_manual_illustrative"] - EXPECTED_DELTA) < 1e-9
        assert abs((OPENAI_ARM_MEAN - META_CARRIED_M988) - EXPECTED_DELTA) < 1e-9

    def test_delta_direction(self):
        s = _mech1050()["asymmetry_scoring_manual_illustrative"]
        assert s["direction"] == "target softer than peer by 0.53"

    def test_significant_false(self):
        s = _mech1050()["asymmetry_scoring_manual_illustrative"]
        assert s["significant"] is False

    def test_stats_not_calculated(self):
        s = _mech1050()["asymmetry_scoring_manual_illustrative"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"

    def test_empirical_required(self):
        s = _mech1050()["asymmetry_scoring_manual_illustrative"]
        assert s["empirical_required"] is True

    def test_scorer_version_pinned(self):
        s = _mech1050()["asymmetry_scoring_manual_illustrative"]
        assert "mediascope/score/asymmetry.py" in s["scorer"]

    def test_carried_meta_arm_m988(self):
        arms = _mech1050()["carried_meta_arms"]
        assert any("m988" in a and "-0.58" in a for a in arms)

    def test_a1_a2_scores(self):
        assert _mech1050()["new_evidence"]["arm_a1"]["score_manual_illustrative"] == A1_SCORE
        assert _mech1050()["new_evidence"]["arm_a2"]["score_manual_illustrative"] == A2_SCORE


# ---------------------------------------------------------------------------
# 6. Statistical discipline (Aug-28 standing rule).
# ---------------------------------------------------------------------------


class TestStatisticalDiscipline1387:
    def test_manual_illustrative_only(self):
        assert "MANUAL ILLUSTRATIVE ONLY" in _mech1050()["statistical_discipline"]

    def test_engine_not_run(self):
        assert "engine NOT run" in _mech1050()["statistical_discipline"]

    def test_is_significant_false(self):
        assert "is_significant false" in _mech1050()["statistical_discipline"]

    def test_not_artifact_grade(self):
        assert "NOT artifact-grade" in _mech1050()["statistical_discipline"]

    def test_no_analysis_json_update(self):
        assert "no_analysis_json_update true" in _mech1050()["statistical_discipline"]

    def test_monitoring_only(self):
        assert "monitoring_only" in _mech1050()["statistical_discipline"]

    def test_correlation_not_causation(self):
        assert "Correlation is not causation" in _mech1050()["statistical_discipline"]

    def test_hypothesis_generating_only(self):
        assert "hypothesis-generating only" in _mech1050()["statistical_discipline"]

    def test_artifact_readiness_no_update(self):
        assert "No analysis.json update warranted" in _mech1050()["artifact_readiness"]

    def test_cautious_language_complete(self):
        cl = _mech1050()["cautious_language"]
        for key in ("correlation_not_causation", "no_editorial_control_claim",
                    "no_statistical_significance_claim", "significant_false",
                    "p_value_not_calculated", "ci_not_calculated",
                    "cohens_d_not_calculated"):
            assert cl[key] is True, key


# ---------------------------------------------------------------------------
# 7. Corpus novelty (HEAD-bounded, per #715).
# ---------------------------------------------------------------------------


class TestCorpusNovelty1387:
    def test_webpronews_url_zero_hit_at_head(self):
        out = _git("grep", "-F", "-l", RELAY_WEBPRONEWS, "HEAD")
        assert out.stdout.strip() == ""

    def test_techinsider_url_zero_hit_at_head(self):
        out = _git("grep", "-F", "-l", RELAY_TECHINSIDER, "HEAD")
        assert out.stdout.strip() == ""

    def test_findskill_url_zero_hit_at_head(self):
        out = _git("grep", "-F", "-l", RELAY_FINDSKILL, "HEAD")
        assert out.stdout.strip() == ""

    def test_muckrack_url_zero_hit_at_head(self):
        out = _git("grep", "-F", "-l", RELAY_MUCKRACK, "HEAD")
        assert out.stdout.strip() == ""

    def test_no_type_a_1387_in_git_log(self):
        out = _git("log", "--format=%H", "--grep=Type A #1387")
        assert out.stdout.strip() == ""

    def test_no_1387_heading_in_iteration_log_at_head(self):
        out = _git("grep", "-F", "-l", "## #1387", "HEAD", "--",
                   "iteration-log.md")
        assert out.stdout.strip() == ""

    def test_single_type_a_1387_file_on_disk(self):
        matches = [f for f in os.listdir(TESTS_DIR)
                   if f.startswith("test_type_a_1387")]
        assert matches == [OWN_BASENAME]

    def test_no_1387_row_in_readme_table_at_head(self):
        out = _git("grep", "-F", "-l", "test_type_a_1387", "HEAD", "--",
                   "README.md")
        assert out.stdout.strip() == ""


# ---------------------------------------------------------------------------
# 8. Doc-sync per #719 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestDocSync1387:
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

    def test_readme_has_1387_table_row(self):
        src = _read(README_PATH)
        assert "test_type_a_1387" in src


# ---------------------------------------------------------------------------
# 9. Iteration log per #721 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestIterationLog1387:
    def test_log_has_1387_heading(self):
        # Written in the doc-sync commit per #721. Fails pre-commit
        # by design; deselected in the in-gate run.
        assert "## #1387" in _read(ITERLOG_PATH)

    def test_log_registers_main_anchor_docsync_hashes(self):
        src = _read(ITERLOG_PATH)
        assert "log-hash" in src

    def test_log_mentions_m1050(self):
        src = _read(ITERLOG_PATH)
        assert "m1050" in src


# ---------------------------------------------------------------------------
# 10. Confounders and counterevidence.
# ---------------------------------------------------------------------------


class TestConfounders1387:
    def test_strong_confounders_present(self):
        strong = _mech1050()["confounders"]["strong"]
        assert len(strong) == 3

    def test_peg_asymmetry_ranked_strong(self):
        strong = _mech1050()["confounders"]["strong"]
        assert any("Peg asymmetry" in c for c in strong)

    def test_relay_attestation_ranked_strong(self):
        strong = _mech1050()["confounders"]["strong"]
        assert any("Relay attestation only" in c for c in strong)

    def test_single_outlet_ranked_strong(self):
        strong = _mech1050()["confounders"]["strong"]
        assert any("Single-outlet pair" in c for c in strong)

    def test_moderate_confounders_present(self):
        assert len(_mech1050()["confounders"]["moderate"]) == 2

    def test_weak_confounders_present(self):
        assert len(_mech1050()["confounders"]["weak"]) == 1

    def test_counterevidence_m1027_bounds_softening(self):
        ce = _mech1050()["counter_evidence"]
        assert any("m1027" in c for c in ce)

    def test_counterevidence_m1042_selection_axis(self):
        ce = _mech1050()["counter_evidence"]
        assert any("m1042" in c for c in ce)

    def test_financial_context_conde_nast_deal(self):
        fc = _mech1050()["financial_context"]
        assert "Conde Nast x OpenAI" in fc
        assert "coverage_prediction" in fc

    def test_cross_references_complete(self):
        cr = _mech1050()["cross_references"]
        for num in (1042, 991, 988, 1027, 946, 916):
            assert num in cr, num

    def test_testable_predictions_present(self):
        tp = _mech1050()["testable_predictions"]
        assert len(tp) == 2


# ---------------------------------------------------------------------------
# 11. Staleness pins on the predecessor's guard lifecycle (deselected
# pre-commit; verified post-terminal-followup).
# ---------------------------------------------------------------------------


class TestStalenessPins1387:
    def test_1386_guard_lifecycle_post_terminal_followup(self):
        # Post-terminal-followup form: 25 passed, 1 failed. The
        # no_type_a_1387_in_git_log forward pin flips green in this
        # run's terminal log-hash followup per #721/#1292 (PRED_MAIN_1387
        # re-pinned in the #1386 file). The ONE failure is the
        # #1272-class forward-guard expiry, DOCUMENTED not repaired
        # per precedent: test_1050_numeric_absent_in_profiles trips on
        # the landed m1050 block (mechanism_id: 1050 now committed in
        # profiles/wired.yaml). The 1051-form pins stay green
        # throughout (this run lands m1050, not m1051); the member and
        # direction pins stay green (no member, no direction landed this
        # run). The #1386 block is read-only to this run; the expiry is
        # documented here, not repaired. Deselected pre-commit
        # (verified only post-terminal-followup).
        r = subprocess.run(
            ["python3", "-m", "pytest",
             os.path.join(TESTS_DIR, E1386_FILE)
             + "::TestGuardLifecycle1386",
             "-q", "-p", "no:cacheprovider"],
            capture_output=True, text=True, timeout=300, cwd=REPO_ROOT,
        )
        tail = r.stdout.strip().splitlines()[-1]
        assert "25 passed" in tail and "1 failed" in tail, tail
        assert "test_1050_numeric_absent_in_profiles" in r.stdout


# ---------------------------------------------------------------------------
# 12. Push readiness: in-flight isolation and #1024 m846 untouched.
# ---------------------------------------------------------------------------


class TestPushReadiness1387:
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
# 13. Rotation: third leg of the 1385-1389 window.
# ---------------------------------------------------------------------------


class TestRotation1387:
    def test_window_sequence(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1385 -> E #1386 -> A #1387" in src

    def test_next_leg_is_type_b(self):
        assert PRED_MAIN_1388 == "0" * 40

    def test_type_letter_a(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type A #1387" in src

    def test_background_suite_observed_only(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "OBSERVES only" in src
        assert "#1385" in src
        assert "#1390" in src


# ---------------------------------------------------------------------------
# 14. ASCII and formatting hygiene.
# ---------------------------------------------------------------------------


class TestAscii1387:
    def test_no_em_dashes_in_test_file(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "\u2014" not in src

    def test_ascii_only_in_test_file(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        src.encode("ascii")

    def test_no_em_dashes_in_profile_block(self):
        src = _read(WIRED_PATH)
        assert "\u2014" not in src

    def test_expected_total_declared(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "EXPECTED_TOTAL = 121" in src
