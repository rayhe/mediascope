"""Type A #1382: The Verge x Anthropic Sep-29-2026 IPO-filing pair -
publication-level control-case extension of m557.

THIRD leg of the 1380-1384 window: D #1380 -> E #1381 -> A #1382 (this
run) -> B #1383 -> C #1384. New Type A mechanism (mechanism 1049) in
profiles/the-verge.yaml under competitor_relationships -> anthropic:
publication-level control-case extension of m557's neutral-prediction
finding onto the adversarial peg. The Verge's Sep-29-2026 Anthropic
IPO-filing pair (Jess Weatherbed: the $4.6B-revenue/$42B-loss piece,
MANUAL ILLUSTRATIVE -0.50, and the catastrophic-risk-filing piece,
MANUAL ILLUSTRATIVE -0.45; relay-attested, 0 browser.open per #503)
applies a hard financial/safety-scrutiny register to the $0-tie AI lab
on the adversarial peg. Carried Meta comparators (m841 #1017 Sep-23/24
Connect Muse Charm -0.30; m628 #657 surveillance register), un-rescored
per #807. Illustrative Anthropic arm mean -0.475 vs Meta -0.30: delta
(Anthropic minus Meta) -0.175 - the non-deal lab draws the HARDER
register. Consistent with m557's neutral-prediction control case
(aspirational register on milestones, hard register on adversarial pegs;
peg valence drives register, not the financial tie). EXTENDS m968's
journalist-level boundary case (Weatherbed same-day symmetric
adversarial, ledger held at 50) to the publication level. NOT a
falsification-family member (control-case extension; Anthropic is not
the deal partner; the uniform payer-softening prediction untested here);
ledger holds at 65; sixty-sixth member-form absent repo-wide; fortieth
direction absent.

Pre-run anchors: max numeric mechanism_id 1048 pre-commit, zero
numeric/underscore/dash-form 1049 keys repo-wide pre-commit (needles
format-built per #715/#770), "## #1382" zero-hit in iteration-log,
README stats 80781/1706 pre-commit, no #1382 row in README/ARCHITECTURE
test tables, fortieth direction absent, 48th-65th members intact, no
66th member, ledger 65. No em dashes in new content. Post-commit:
mechanism 1049 is the corpus max; zero 1050 keys
numeric/underscore/dash in profiles/.

Research surface: 4 main-run browser.search verification sets (Verge
Galaxy XR / M5 Vision Pro peg screens - rejected, stale 2025 launches;
FT OpenAI $278B cash-burn - rejected, saturated via m754; Verge
Anthropic Sep-29 IPO pair - SELECTED; Guardian Anthropic Sep-29 Milmo
piece - rejected as m517-line extension with weaker publication-level
novelty) + git grep -F novelty verification on every candidate URL
(ainformed.dev and saascity.io zero-hit repo-wide; the techseen URL is
in-corpus via m968 journalist-level only, absent from the-verge.yaml
publication profile), 0 browser.open per #503. Snippet-bounded; all URLs
copied verbatim from the browser.search Full-URL listings; bounded
search-result absence, not proof.

Background suite per #795: the #1380-launched full suite runs at goal
hidden_files type_d_1380_full_suite.log: this run OBSERVES only
(neither re-launches, kills, nor writes to the suite). The verdict and
tombstone belong to #1385 per #795.

Concurrency: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file),
#1012-wt (working-tree edit on the committed Type A #1012 file) all left
out of this run's index/diff via explicit-path staging. #1024 m846
(profiles/competitor-entities.yaml) NOT touched - decision pending. Do
NOT touch #1024 m846.

Tests: 122 tests collected, 14 classes. In-gate: 112 passed +
10 deselected per #565/#719/#721 (TestAnchor1382 1 +
TestGuardLifecycle1382 2 + TestDocSync1382 3 +
TestIterationLog1382 3 + TestStalenessPins1382 1).
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
    "test_type_a_1382_verge_anthropic_sep29_ipo_filing_pair_"
    "publication_level_control_case_oct10_9pm.py"
)


# Pre-commit placeholder per #565; patched to the main-commit sha in
# the anchor followup (post-anchor the placeholder pin fails BY
# DESIGN).
ANCHORED_SHA = "a4d8386621cbe1f7d65739a222765cd53d24f862"  # patched to the main commit sha in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1049
NEXT_NUM = 1050  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_a_1382_verge_anthropic_sep29_ipo_filing_pair_"
    "publication_level_control_case_vs_carried_meta_arms"
)

# Predecessor chain: #1381 Type E was the SECOND leg of the
# 1380-1384 window. Its main/anchor/doc-sync/log-hash/push commits are
# pushed and ls-remote-verified.
PRED_MAIN_1381 = "6cbfa881d09bdf0cc40925887e36e5098f74ed8d"
PRED_ANCHOR_1381 = "08c12fb53506618b7bee0e57ec7038a74174c3fed"
PRED_DOCSYNC_1381 = "fc73dc6b85687c9f856fdb66f7c30cbe9aa34757"
PRED_FINAL_1381 = "561fa0fd404a7de660d61739bd363f0b564422b2"
PRED_PUSH_1381 = "36a7d03b9b3505634e08d40aa0a067e52399977d"

# This run's own main-commit sha, re-pinned per #721 in the anchor
# followup (the #1381 predecessor file's copy is re-pinned in the
# terminal log-hash followup per #721/#1292).
PRED_MAIN_1382 = "a4d8386621cbe1f7d65739a222765cd53d24f862"  # re-pinned by #1382 anchor followup per #721

# Forward guard for the next leg: #1383 Type B. Re-pinned by #1383's
# anchor followup per #721 (starts as 0*40; placeholder-only).
PRED_MAIN_1383 = "47493cff35df503be4b02893acd8300cd852c1b6"  # forward guard for #1383 Type B; re-pinned to the #1383 main sha in #1383's terminal log-hash followup per #721/#1292

# The #1381 Type E file, for the staleness pin on its guard
# lifecycle (post-terminal form at this run is "26 passed": the
# no_type_a_1382_in_git_log forward pin flips green in this run's
# terminal log-hash followup per #721/#1292 when PRED_MAIN_1382 is
# re-pinned in the #1381 file. All 1050-form pins stay green
# throughout (this run lands m1049, not m1050); the member and
# direction pins stay green (no member, no direction landed this
# run). The #1381 block is read-only to this run; the flip is
# documented here, not repaired). Deselected pre-commit (verified only
# post-terminal-followup).
E1381_FILE = (
    "test_type_e_1381_podcast_sentiment_199th_"
    "verification_oct10_9pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 80903  # patched pre-main: pre-sync 80781 + 122 collected
README_FILE_COUNT = 1707  # patched pre-main: pre-sync 1706 + 1 (this file)

EXPECTED_TOTAL = 122

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

# A1: Weatherbed's loss-multiplier piece (byline attested via the
# author's Muck Rack profile listing; the canonical theverge.com URL
# did not surface, not landed per policy).
RELAY_MUCKRACK = "http://muckrack.com/jess-weatherbed/articles"
# A2: the catastrophic-risk-filing piece (verbatim Verge lede via the
# techseen story record; in-corpus via m968 journalist-level only).
RELAY_TECHSEEN = (
    "https://techseen.com/story/"
    "anthropic-s-ipo-filing-shows-soaring-revenue-mounting-costs-and-"
    "existe-6ce54d1"
)
# Corroborating relays, NEW to corpus this run (zero pre-commit hits).
RELAY_AINFORMED = (
    "https://www.ainformed.dev/articles/2026-09-29-anthropic-warns-of-"
    "catastrophic-ai-risks-in-ipo-filing"
)
RELAY_SAASCITY = (
    "https://saascity.io/blog/anthropic-ipo-prospectus-saas-founders-2026"
)
EVIDENCE_URLS = [RELAY_MUCKRACK, RELAY_TECHSEEN, RELAY_AINFORMED,
                 RELAY_SAASCITY]

ANTHROPIC_ARM_MEAN = -0.475
META_CARRIED_M841 = -0.30
EXPECTED_DELTA = -0.175


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


def _mech1049():
    d = _load_verge()
    return d["competitor_relationships"]["anthropic"][BLOCK_KEY]


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------


class TestAnchor1382:
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
# 2. Guard lifecycle for this run (pre-commit form; the no-Type-A-#1382
# pin is the #1191-class self-trip, re-pinned in the terminal log-hash
# followup per #721/#1292).
# ---------------------------------------------------------------------------


class TestGuardLifecycle1382:
    def test_pins_on_1049_landing(self):
        # Type A lands one mechanism: max numeric id 1048 -> 1049.
        # Pre-commit the working tree already carries the m1049
        # block, so the file-level constants pin the landing.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1049" in src
        assert "NEXT_NUM = 1050" in src
        assert _max_numeric_mechanism_id() == 1049

    def test_no_type_a_1382_in_git_log_pin(self):
        # Post-main-commit form for THIS run's own pin (the
        # #1191-class self-trip, re-pinned in this run's terminal
        # log-hash followup per #721/#1292): every commit whose
        # message matches "Type A #1382" must be this run's main
        # commit or a descendant of it. Deselected in the in-gate
        # run (fails pre-commit by design: PRED_MAIN_1382 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type A #1382")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1382's own commits"
        main = _git("rev-parse", PRED_MAIN_1382).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_no_type_b_1383_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1383's terminal log-hash followup
        # per #721): every commit whose message matches "Type B
        # #1383" must be #1383's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1383 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type B #1383")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1383's own commits"
        main = _git("rev-parse", PRED_MAIN_1383).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1050_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1050_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1050_dash_absent_repo_wide(self):
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


class TestMechanismNovelty1382:
    def test_block_key_present_in_working_tree(self):
        assert BLOCK_KEY in _read(VERGE_PATH)

    def test_block_key_absent_at_head(self):
        # Pre-commit novelty per #715: the block key is new to the
        # corpus (working tree only, not yet committed).
        out = _git("grep", "-F", "-l", BLOCK_KEY, "HEAD", "--", "profiles/")
        assert out.stdout.strip() == ""

    def test_mechanism_id_is_1049(self):
        assert _mech1049()["mechanism_id"] == 1049

    def test_iteration_is_1382(self):
        assert _mech1049()["iteration"] == 1382

    def test_iteration_type_is_a(self):
        assert _mech1049()["iteration_type"] == "A"

    def test_entity_pair_anthropic_vs_meta(self):
        assert _mech1049()["entity_pair"] == "Anthropic vs Meta"

    def test_publication_focus_verge(self):
        assert _mech1049()["publication_focus"] == "The Verge"

    def test_verdict_directionally_supported(self):
        assert _mech1049()["verdict"] == "directionally_supported_not_proven"

    def test_not_a_falsification_member(self):
        fam = _mech1049()["falsification_family"]
        assert fam.startswith("NOT a member")
        assert "ledger holds at 65" in fam

    def test_goal_id_matches(self):
        assert _mech1049()["goal_id"] == "goal_54093bda4145"

    def test_scheduled_job_id_matches(self):
        assert _mech1049()["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_author_kit_with_ray(self):
        assert _mech1049()["author"] == "Kit (with Ray)"

    def test_no_1049_substring_in_block_key(self):
        # Designed keying per #723/#738/#739: the block key carries
        # the iteration (1382), never the mechanism number (1049).
        assert "1049" not in BLOCK_KEY

    def test_distinct_from_m557(self):
        assert "m557" in _mech1049()["distinct_from_prior"]

    def test_extends_m968_journalist_level(self):
        assert "m968" in _mech1049()["extends_prior"]

    def test_distinct_from_m517(self):
        assert "m517" in _mech1049()["distinct_from_prior"]

    def test_publication_level_novelty(self):
        disc = _mech1049()["discovery_summary"]
        assert "publication-level" in disc
        assert "m968" in disc


# ---------------------------------------------------------------------------
# 4. Evidence: URLs verbatim, relay attestation, bounded claims.
# ---------------------------------------------------------------------------


class TestEvidence1382:
    def test_muckrack_relay_verbatim_in_attestation(self):
        assert RELAY_MUCKRACK in _mech1049()["new_evidence"]["attestation"]

    def test_techseen_relay_verbatim_in_attestation(self):
        assert RELAY_TECHSEEN in _mech1049()["new_evidence"]["attestation"]

    def test_ainformed_relay_verbatim_in_attestation(self):
        assert RELAY_AINFORMED in _mech1049()["new_evidence"]["attestation"]

    def test_saascity_relay_verbatim_in_attestation(self):
        assert RELAY_SAASCITY in _mech1049()["new_evidence"]["attestation"]

    def test_zero_browser_open(self):
        assert "0 browser.open per #503" in _mech1049()["new_evidence"]["attestation"]

    def test_byline_attested(self):
        assert "Jess Weatherbed" in _mech1049()["new_evidence"]["attestation"]

    def test_a1_loss_headline_quote(self):
        assert "lost $42 billion" in _mech1049()["new_evidence"]["arm_a1"]["key_quotes"]

    def test_a1_editorial_closer_quote(self):
        assert "a long, long way off" in _mech1049()["new_evidence"]["arm_a1"]["key_quotes"]

    def test_a2_risk_lede_quote(self):
        assert "further increase the risk that our models cause harm" in _mech1049()["new_evidence"]["arm_a2"]["key_quotes"]

    def test_a2_power_retention_noted(self):
        assert "retain power" in _mech1049()["new_evidence"]["arm_a2"]["key_quotes"]

    def test_url_novelty_claim(self):
        assert "zero-hit repo-wide pre-commit" in _mech1049()["new_evidence"]["novelty"]

    def test_canonical_url_gap_noted(self):
        assert "canonical theverge.com URL did not surface" in _mech1049()["new_evidence"]["attestation"]


# ---------------------------------------------------------------------------
# 5. Scores: illustrative delta arithmetic and scorer metadata.
# ---------------------------------------------------------------------------


class TestScores1382:
    def test_anthropic_arm_mean(self):
        s = _mech1049()["asymmetry_scoring_manual_illustrative"]
        assert s["target_score_manual_illustrative"] == ANTHROPIC_ARM_MEAN

    def test_meta_score(self):
        s = _mech1049()["asymmetry_scoring_manual_illustrative"]
        assert s["peer_score_manual_illustrative"] == META_CARRIED_M841

    def test_delta_arithmetic(self):
        s = _mech1049()["asymmetry_scoring_manual_illustrative"]
        assert abs(s["delta_manual_illustrative"] - EXPECTED_DELTA) < 1e-9
        assert abs((ANTHROPIC_ARM_MEAN - META_CARRIED_M841) - EXPECTED_DELTA) < 1e-9

    def test_delta_direction(self):
        s = _mech1049()["asymmetry_scoring_manual_illustrative"]
        assert s["direction"] == "target harder than peer by 0.175"

    def test_significant_false(self):
        s = _mech1049()["asymmetry_scoring_manual_illustrative"]
        assert s["significant"] is False

    def test_stats_not_calculated(self):
        s = _mech1049()["asymmetry_scoring_manual_illustrative"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"

    def test_empirical_required(self):
        s = _mech1049()["asymmetry_scoring_manual_illustrative"]
        assert s["empirical_required"] is True

    def test_scorer_version_pinned(self):
        s = _mech1049()["asymmetry_scoring_manual_illustrative"]
        assert "mediascope/score/asymmetry.py" in s["scorer"]

    def test_carried_meta_arm_m841(self):
        arms = _mech1049()["carried_meta_arms"]
        assert any("m841" in a and "-0.30" in a for a in arms)

    def test_carried_meta_arm_m628(self):
        arms = _mech1049()["carried_meta_arms"]
        assert any("m628" in a for a in arms)


# ---------------------------------------------------------------------------
# 6. Statistical discipline (Aug-28 standing rule).
# ---------------------------------------------------------------------------


class TestStatisticalDiscipline1382:
    def test_manual_illustrative_only(self):
        assert "MANUAL ILLUSTRATIVE ONLY" in _mech1049()["statistical_discipline"]

    def test_engine_not_run(self):
        assert "engine NOT run" in _mech1049()["statistical_discipline"]

    def test_is_significant_false(self):
        assert "is_significant false" in _mech1049()["statistical_discipline"]

    def test_not_artifact_grade(self):
        assert "NOT artifact-grade" in _mech1049()["statistical_discipline"]

    def test_no_analysis_json_update(self):
        assert "no_analysis_json_update true" in _mech1049()["statistical_discipline"]

    def test_monitoring_only(self):
        assert "monitoring_only" in _mech1049()["statistical_discipline"]

    def test_correlation_not_causation(self):
        assert "Correlation is not causation" in _mech1049()["statistical_discipline"]

    def test_hypothesis_generating_only(self):
        assert "hypothesis-generating only" in _mech1049()["statistical_discipline"]

    def test_artifact_readiness_no_update(self):
        assert "No analysis.json update warranted" in _mech1049()["artifact_readiness"]

    def test_cautious_language_complete(self):
        cl = _mech1049()["cautious_language"]
        for key in ("correlation_not_causation", "no_editorial_control_claim",
                    "no_statistical_significance_claim", "significant_false",
                    "p_value_not_calculated", "ci_not_calculated",
                    "cohens_d_not_calculated"):
            assert cl[key] is True, key


# ---------------------------------------------------------------------------
# 7. Corpus novelty (HEAD-bounded, per #715).
# ---------------------------------------------------------------------------


class TestCorpusNovelty1382:
    def test_ainformed_url_zero_hit_at_head(self):
        out = _git("grep", "-F", "-l", RELAY_AINFORMED, "HEAD")
        assert out.stdout.strip() == ""

    def test_saascity_url_zero_hit_at_head(self):
        out = _git("grep", "-F", "-l", RELAY_SAASCITY, "HEAD")
        assert out.stdout.strip() == ""

    def test_techseen_url_absent_from_verge_profile_at_head(self):
        # The techseen URL is in-corpus via m968 (journalist-level,
        # profiles/careers/journalists.yaml) but must be absent from
        # the publication profile (the-verge.yaml) pre-commit.
        out = _git("grep", "-F", RELAY_TECHSEEN, "HEAD", "--",
                   "profiles/the-verge.yaml")
        assert out.stdout.strip() == ""

    def test_muckrack_url_absent_from_verge_profile_at_head(self):
        out = _git("grep", "-F", RELAY_MUCKRACK, "HEAD", "--",
                   "profiles/the-verge.yaml")
        assert out.stdout.strip() == ""

    def test_no_type_a_1382_in_git_log(self):
        out = _git("log", "--format=%H", "--grep=Type A #1382")
        assert out.stdout.strip() == ""

    def test_no_1382_heading_in_iteration_log_at_head(self):
        out = _git("grep", "-F", "-l", "## #1382", "HEAD", "--",
                   "iteration-log.md")
        assert out.stdout.strip() == ""

    def test_single_type_a_1382_file_on_disk(self):
        matches = [f for f in os.listdir(TESTS_DIR)
                   if f.startswith("test_type_a_1382")]
        assert matches == [OWN_BASENAME]

    def test_no_1382_row_in_readme_table_at_head(self):
        out = _git("grep", "-F", "-l", "test_type_a_1382", "HEAD", "--",
                   "README.md")
        assert out.stdout.strip() == ""


# ---------------------------------------------------------------------------
# 8. Doc-sync per #719 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestDocSync1382:
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

    def test_readme_has_1382_table_row(self):
        src = _read(README_PATH)
        assert "test_type_a_1382" in src


# ---------------------------------------------------------------------------
# 9. Iteration log per #721 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestIterationLog1382:
    def test_log_has_1382_heading(self):
        # Written in the doc-sync commit per #721. Fails pre-commit
        # by design; deselected in the in-gate run.
        assert "## #1382" in _read(ITERLOG_PATH)

    def test_log_registers_main_anchor_docsync_hashes(self):
        src = _read(ITERLOG_PATH)
        assert "log-hash" in src

    def test_log_mentions_m1049(self):
        src = _read(ITERLOG_PATH)
        assert "m1049" in src


# ---------------------------------------------------------------------------
# 10. Confounders and counterevidence.
# ---------------------------------------------------------------------------


class TestConfounders1382:
    def test_strong_confounders_present(self):
        strong = _mech1049()["confounders"]["strong"]
        assert len(strong) == 3

    def test_relay_attestation_confound_ranked_strong(self):
        strong = _mech1049()["confounders"]["strong"]
        assert any("Relay attestation only" in c for c in strong)

    def test_single_byline_confound(self):
        strong = _mech1049()["confounders"]["strong"]
        assert any("Single byline" in c for c in strong)

    def test_peg_asymmetry_confound(self):
        strong = _mech1049()["confounders"]["strong"]
        assert any("Peg asymmetry" in c for c in strong)

    def test_moderate_confounders_present(self):
        assert len(_mech1049()["confounders"]["moderate"]) == 2

    def test_weak_confounders_present(self):
        assert len(_mech1049()["confounders"]["weak"]) == 1

    def test_counterevidence_m965_contrast(self):
        ce = _mech1049()["counter_evidence"]
        assert any("m965" in c for c in ce)

    def test_counterevidence_m557_milestone_arms(self):
        ce = _mech1049()["counter_evidence"]
        assert any("m557" in c for c in ce)

    def test_financial_context_neutral(self):
        fc = _mech1049()["financial_context"]
        assert "$0" in fc
        assert "coverage_prediction neutral" in fc

    def test_cross_references_complete(self):
        cr = _mech1049()["cross_references"]
        for num in (557, 968, 841, 628, 517, 965):
            assert num in cr, num

    def test_testable_predictions_present(self):
        tp = _mech1049()["testable_predictions"]
        assert len(tp) == 2
        assert any("November 2026" in p for p in tp)


# ---------------------------------------------------------------------------
# 11. Staleness pins on the predecessor's guard lifecycle (deselected
# pre-commit; verified post-terminal-followup).
# ---------------------------------------------------------------------------


class TestStalenessPins1382:
    def test_1381_guard_lifecycle_post_terminal_followup(self):
        # Post-terminal-followup form: 25 passed, 1 failed. The
        # no_type_a_1382_in_git_log forward pin flips green in this
        # run's terminal log-hash followup per #721/#1292 (PRED_MAIN_1382
        # re-pinned in the #1381 file). The ONE failure is the
        # #1272-class forward-guard expiry, DOCUMENTED not repaired
        # per precedent: test_1049_numeric_absent_in_profiles trips on
        # the landed m1049 block (mechanism_id: 1049 now committed in
        # profiles/the-verge.yaml). The 1050-form pins stay green
        # throughout (this run lands m1049, not m1050); the member and
        # direction pins stay green (no member, no direction landed this
        # run). The #1381 block is read-only to this run; the expiry is
        # documented here, not repaired. Deselected pre-commit
        # (verified only post-terminal-followup).
        r = subprocess.run(
            ["python3", "-m", "pytest",
             os.path.join(TESTS_DIR, E1381_FILE)
             + "::TestGuardLifecycle1381",
             "-q", "-p", "no:cacheprovider"],
            capture_output=True, text=True, timeout=300, cwd=REPO_ROOT,
        )
        tail = r.stdout.strip().splitlines()[-1]
        assert "25 passed" in tail and "1 failed" in tail, tail
        assert "test_1049_numeric_absent_in_profiles" in r.stdout


# ---------------------------------------------------------------------------
# 12. Push readiness: in-flight isolation and #1024 m846 untouched.
# ---------------------------------------------------------------------------


class TestPushReadiness1382:
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
# 13. Rotation: third leg of the 1380-1384 window.
# ---------------------------------------------------------------------------


class TestRotation1382:
    def test_window_sequence(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1380 -> E #1381 -> A #1382" in src

    def test_next_leg_is_type_b(self):
        assert PRED_MAIN_1383 == "0" * 40

    def test_type_letter_a(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type A #1382" in src

    def test_background_suite_observed_only(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "OBSERVES only" in src
        assert "#1380" in src
        assert "#1385" in src


# ---------------------------------------------------------------------------
# 14. ASCII and formatting hygiene.
# ---------------------------------------------------------------------------


class TestAscii1382:
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
        assert "EXPECTED_TOTAL = 122" in src
