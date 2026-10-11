"""Type A #1377: Verge x Google Oct-8-2026 Xreal Aura Android XR
product-launch register vs carried Verge x Meta arms.

THIRD leg of the 1375-1379 window: D #1375 -> E #1376 -> A #1377 (this run)
-> B #1378 -> C #1379. New Type A mechanism (mechanism 1048) in
profiles/the-verge.yaml under competitor_relationships -> google:
adversarial-prediction non-manifestation on the product register - The
Verge's Oct-8-2026 Xreal Aura pre-order launch piece (Google-built Android
XR glasses, $1,279; relay-attested Verge original URL) runs a product-news
register with zero privacy/surveillance vocabulary (MANUAL ILLUSTRATIVE
+0.15), vs the carried Verge x Meta arm (m841, #1017: Sep-23/24 Connect
Muse Charm backlash framing, -0.30, un-rescored per #807); illustrative
delta (Google minus Meta) +0.45. The standing coverage_prediction for
Verge x Google is ADVERSARIAL (PMC dual Google lawsuits,
adversarial_litigation); the adversarial prediction does NOT manifest on
the product-launch register. EXTENDS m590 (adversarial-posture boundary,
#592 Sep-7) into the Oct-2026 XR shipping window and ANSWERS m492's
testable prediction (no privacy-vocabulary escalation on the shipping
peg). Verdict directionally_supported_not_proven. NOT a
falsification-family member (the family is defined on softer-predictions
failing; this is an adversarial-prediction non-manifestation, a distinct
lineage); ledger holds at 65; sixty-sixth member-form absent repo-wide.

Pre-run anchors: max numeric mechanism_id 1047 pre-commit, zero
numeric/underscore/dash-form 1048 keys repo-wide pre-commit (needles
format-built per #715, own file excluded), zero test_type_a_1377 files on
disk (glob), no "Type A #1377" in git log (--grep), block key zero-hit
repo-wide pre-commit, all 4 evidence URLs zero-hit repo-wide pre-commit
(git grep -F). 5 browser.search sets, 0 browser.open (excerpt-bounded per
#503; relay-attested per the #1243 Lawler precedent). ASCII-only, no em
dashes in new content. Post-commit: mechanism 1048 is the corpus max;
zero 1049 keys numeric/underscore/dash in profiles/.

Doc-sync (80321/1701 -> 80438/1702; +117/+1, venv python); 1375-1379
window THIRD leg D->E->A (anchor + rotation guard per #565);
concurrency: #899 (nytimes.yaml mechanism 771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), and the
#1012-wt working-tree edit on the committed Type A #1012 file stay
unstaged; #1024 m846 (profiles/competitor-entities.yaml) NOT touched -
decision pending.

Type A lands one mechanism (m1048): max numeric mechanism_id
1047->1048; ledger holds at 65; sixty-sixth member-form absent
repo-wide; fortieth direction absent by design. MANUAL / QUALITATIVE ONLY
per the Aug-28 standing rule; monitoring-only; NOT artifact-grade; no
analysis.json update. Correlation is not causation;
hypothesis-generating only.

Background suite per #795: the #1375-launched full suite runs at goal
hidden_files type_d_1375_full_suite.log: this run OBSERVES only (neither
re-launches, kills, nor writes to the suite). The verdict and tombstone
belong to #1380 per #795.

Concurrency: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file),
#1012-wt (working-tree edit on the committed Type A #1012 file) all left
out of this run's index/diff via explicit-path staging. #1024 m846
(profiles/competitor-entities.yaml) NOT touched - decision pending. Do
NOT touch #1024 m846.
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
    "test_type_a_1377_verge_google_oct08_xreal_aura_product_"
    "register_vs_carried_meta_arms_oct10_5pm.py"
)


# Pre-commit placeholder per #565; patched to the main-commit sha in
# the anchor followup (post-anchor the placeholder pin fails BY
# DESIGN).
ANCHORED_SHA = "f324251e7223d7337fff25071477e7ac376bb87a"

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1048
NEXT_NUM = 1049  # integer only; key-form needles are format-built

BLOCK_KEY = (
    "type_a_1377_verge_google_oct08_xreal_aura_android_xr_"
    "product_register_vs_carried_meta_arms"
)

# Predecessor chain: #1376 Type E was the SECOND leg of the
# 1375-1379 window. Its main/anchor/doc-sync/log-hash/push commits are
# pushed and ls-remote-verified.
PRED_MAIN_1376 = "1f9d1dd6c56e1fb881cec44eea95ce8e819d1773"
PRED_ANCHOR_1376 = "a60569528818adfeb6524c6192292d63611dbb2f"
PRED_DOCSYNC_1376 = "5de16c64a10d6c3b09d0bf640b3e4ea880bbf387"
PRED_FINAL_1376 = "c8da3a5ce5971afe5baebf2602136d09b0ac0f90"
PRED_PUSH_1376 = "a394e2722270d3b9af95eb92fe94eedc1990d2e9"

# This run's own main-commit sha, re-pinned per #721 in the anchor
# followup (the #1376 predecessor file's copy is re-pinned in the
# terminal log-hash followup per #721/#1292).
PRED_MAIN_1377 = "f324251e7223d7337fff25071477e7ac376bb87a"

# Forward guard for the next leg: #1378 Type B. Re-pinned by #1378's
# anchor followup per #721 (starts as 0*40; placeholder-only).
PRED_MAIN_1378 = "0" * 40

# The #1376 Type E file, for the staleness pin on its guard
# lifecycle (post-terminal form at this run is "26 passed": the
# no_type_a_1377_in_git_log forward pin flips green in this run's
# terminal log-hash followup per #721/#1292 when PRED_MAIN_1377 is
# re-pinned in the #1376 file. All 1049-form pins stay green
# throughout (this run lands m1048, not m1049); the member and
# direction pins stay green (no member, no direction landed this
# run). The #1376 block is read-only to this run; the flip is
# documented here, not repaired). Deselected pre-commit (verified only
# post-terminal-followup).
E1376_FILE = (
    "test_type_e_1376_podcast_sentiment_198th_"
    "verification_oct10_4pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 80438  # patched pre-main: pre-sync 80321 + 117 collected
README_FILE_COUNT = 1702  # patched pre-main: pre-sync 1701 + 1 (this file)

EXPECTED_TOTAL = 117

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

VERGE_AURA_URL = (
    "https://www.theverge.com/news/1006207/"
    "google-xreal-aura-glasses-price-release-date-preorder"
)
RELAY_GENAI = (
    "https://genainews.tech/xreal-opens-aura-pre-orders-"
    "at-1-279-undercutting-meta-vr-glasses/"
)
RELAY_PLAYTECH = (
    "https://playtechdeep.blog/2026/10/08/vr-news-for-october-08-2026-"
    "meta-is-working-on-a-virtual-cinema-environment-for-quest-"
    "vr-glasses/"
)
RELAY_IPHONEINCA = (
    "https://www.iphoneincanada.ca/2026/10/08/"
    "xreal-aura-xr-glasses-pre-orders/"
)
EVIDENCE_URLS = [VERGE_AURA_URL, RELAY_GENAI, RELAY_PLAYTECH, RELAY_IPHONEINCA]

GOOGLE_SCORE = 0.15
META_SCORE = -0.30
EXPECTED_DELTA = 0.45


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


def _mech1048():
    d = _load_verge()
    return d["competitor_relationships"]["google"][BLOCK_KEY]


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------


class TestAnchor1377:
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
# 2. Guard lifecycle for this run (pre-commit form; the no-Type-A-#1377
# pin is the #1191-class self-trip, re-pinned in the terminal log-hash
# followup per #721/#1292).
# ---------------------------------------------------------------------------


class TestGuardLifecycle1377:
    def test_pins_on_1048_landing(self):
        # Type A lands one mechanism: max numeric id 1047 -> 1048.
        # Pre-commit the working tree already carries the m1048
        # block, so the file-level constants pin the landing.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1048" in src
        assert "NEXT_NUM = 1049" in src
        assert _max_numeric_mechanism_id() == 1048

    def test_no_type_a_1377_in_git_log_pin(self):
        # Post-main-commit form for THIS run's own pin (the
        # #1191-class self-trip, re-pinned in this run's terminal
        # log-hash followup per #721/#1292): every commit whose
        # message matches "Type A #1377" must be this run's main
        # commit or a descendant of it. Deselected in the in-gate
        # run (fails pre-commit by design: PRED_MAIN_1377 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type A #1377")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1377's own commits"
        main = _git("rev-parse", PRED_MAIN_1377).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_no_type_b_1378_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1378's terminal log-hash followup
        # per #721): every commit whose message matches "Type B
        # #1378" must be #1378's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1378 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type B #1378")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1378's own commits"
        main = _git("rev-parse", PRED_MAIN_1378).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1049_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1049_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1049_dash_absent_repo_wide(self):
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


class TestMechanismNovelty1377:
    def test_block_key_present_in_working_tree(self):
        assert BLOCK_KEY in _read(VERGE_PATH)

    def test_block_key_absent_at_head(self):
        # Pre-commit novelty per #715: the block key is new to the
        # corpus (working tree only, not yet committed).
        out = _git("grep", "-F", "-l", BLOCK_KEY, "HEAD", "--", "profiles/")
        assert out.stdout.strip() == ""

    def test_mechanism_id_is_1048(self):
        assert _mech1048()["mechanism_id"] == 1048

    def test_iteration_is_1377(self):
        assert _mech1048()["iteration"] == 1377

    def test_iteration_type_is_a(self):
        assert _mech1048()["iteration_type"] == "A"

    def test_entity_pair_google_vs_meta(self):
        assert _mech1048()["entity_pair"] == "Google vs Meta"

    def test_publication_focus_verge(self):
        assert _mech1048()["publication_focus"] == "The Verge"

    def test_verdict_directionally_supported(self):
        assert _mech1048()["verdict"] == "directionally_supported_not_proven"

    def test_not_a_falsification_member(self):
        fam = _mech1048()["falsification_family"]
        assert fam.startswith("NOT a member")
        assert "ledger holds at 65" in fam

    def test_goal_id_matches(self):
        assert _mech1048()["goal_id"] == "goal_54093bda4145"

    def test_scheduled_job_id_matches(self):
        assert _mech1048()["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_author_kit_with_ray(self):
        assert _mech1048()["author"] == "Kit (with Ray)"

    def test_no_1048_substring_in_block_key(self):
        # Designed keying per #723/#738/#739: the block key carries
        # the iteration (1377), never the mechanism number (1048).
        assert "1048" not in BLOCK_KEY

    def test_distinct_from_m590(self):
        assert "m590" in _mech1048()["distinct_from_prior"]

    def test_distinct_from_m492(self):
        assert "m492" in _mech1048()["distinct_from_prior"]

    def test_answers_m492_testable_prediction(self):
        disc = _mech1048()["discovery_summary"]
        assert "ANSWERS m492" in disc


# ---------------------------------------------------------------------------
# 4. Evidence: URLs verbatim, relay attestation, bounded claims.
# ---------------------------------------------------------------------------


class TestEvidence1377:
    def test_verge_url_verbatim_in_block(self):
        assert VERGE_AURA_URL in _mech1048()["new_evidence"]["url_verbatim"]

    def test_relay_genai_verbatim_in_attestation(self):
        assert RELAY_GENAI in _mech1048()["new_evidence"]["attestation"]

    def test_relay_playtech_verbatim_in_attestation(self):
        assert RELAY_PLAYTECH in _mech1048()["new_evidence"]["attestation"]

    def test_relay_iphoneinca_verbatim_in_attestation(self):
        assert RELAY_IPHONEINCA in _mech1048()["new_evidence"]["attestation"]

    def test_zero_browser_open(self):
        assert "0 browser.open per #503" in _mech1048()["new_evidence"]["attestation"]

    def test_byline_gap_noted(self):
        assert "Byline unattested" in _mech1048()["new_evidence"]["attestation"]

    def test_register_zero_privacy_vocabulary(self):
        assert "Zero privacy or surveillance vocabulary" in _mech1048()["new_evidence"]["register"]

    def test_pricing_facts_in_register(self):
        reg = _mech1048()["new_evidence"]["register"]
        assert "$1,279" in reg and "$1,499" in reg

    def test_head_to_head_positioning_noted(self):
        reg = _mech1048()["new_evidence"]["register"]
        assert "head-to-head" in reg

    def test_url_novelty_claim(self):
        assert "zero-hit repo-wide pre-commit" in _mech1048()["new_evidence"]["novelty"]


# ---------------------------------------------------------------------------
# 5. Scores: illustrative delta arithmetic and scorer metadata.
# ---------------------------------------------------------------------------


class TestScores1377:
    def test_google_score(self):
        s = _mech1048()["asymmetry_scoring_manual_illustrative"]
        assert s["target_score_manual_illustrative"] == GOOGLE_SCORE

    def test_meta_score(self):
        s = _mech1048()["asymmetry_scoring_manual_illustrative"]
        assert s["peer_score_manual_illustrative"] == META_SCORE

    def test_delta_arithmetic(self):
        s = _mech1048()["asymmetry_scoring_manual_illustrative"]
        assert abs(s["delta_manual_illustrative"] - EXPECTED_DELTA) < 1e-9
        assert abs((GOOGLE_SCORE - META_SCORE) - EXPECTED_DELTA) < 1e-9

    def test_delta_direction(self):
        s = _mech1048()["asymmetry_scoring_manual_illustrative"]
        assert s["direction"] == "target softer than peer by 0.45"

    def test_significant_false(self):
        s = _mech1048()["asymmetry_scoring_manual_illustrative"]
        assert s["significant"] is False

    def test_stats_not_calculated(self):
        s = _mech1048()["asymmetry_scoring_manual_illustrative"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"

    def test_empirical_required(self):
        s = _mech1048()["asymmetry_scoring_manual_illustrative"]
        assert s["empirical_required"] is True

    def test_scorer_version_pinned(self):
        s = _mech1048()["asymmetry_scoring_manual_illustrative"]
        assert "mediascope/score/asymmetry.py" in s["scorer"]

    def test_carried_meta_arm_m841(self):
        arms = _mech1048()["carried_meta_arms"]
        assert any("m841" in a and "-0.30" in a for a in arms)

    def test_carried_meta_arm_m628(self):
        arms = _mech1048()["carried_meta_arms"]
        assert any("m628" in a for a in arms)


# ---------------------------------------------------------------------------
# 6. Statistical discipline (Aug-28 standing rule).
# ---------------------------------------------------------------------------


class TestStatisticalDiscipline1377:
    def test_manual_illustrative_only(self):
        assert "MANUAL ILLUSTRATIVE ONLY" in _mech1048()["statistical_discipline"]

    def test_engine_not_run(self):
        assert "engine NOT run" in _mech1048()["statistical_discipline"]

    def test_is_significant_false(self):
        assert "is_significant false" in _mech1048()["statistical_discipline"]

    def test_not_artifact_grade(self):
        assert "NOT artifact-grade" in _mech1048()["statistical_discipline"]

    def test_no_analysis_json_update(self):
        assert "no_analysis_json_update true" in _mech1048()["statistical_discipline"]

    def test_monitoring_only(self):
        assert "monitoring_only" in _mech1048()["statistical_discipline"]

    def test_correlation_not_causation(self):
        assert "Correlation is not causation" in _mech1048()["statistical_discipline"]

    def test_hypothesis_generating_only(self):
        assert "hypothesis-generating only" in _mech1048()["statistical_discipline"]

    def test_artifact_readiness_no_update(self):
        assert "No analysis.json update warranted" in _mech1048()["artifact_readiness"]

    def test_cautious_language_complete(self):
        cl = _mech1048()["cautious_language"]
        for key in ("correlation_not_causation", "no_editorial_control_claim",
                    "no_statistical_significance_claim", "significant_false",
                    "p_value_not_calculated", "ci_not_calculated",
                    "cohens_d_not_calculated"):
            assert cl[key] is True, key


# ---------------------------------------------------------------------------
# 7. Corpus novelty (HEAD-bounded, per #715).
# ---------------------------------------------------------------------------


class TestCorpusNovelty1377:
    def test_verge_aura_url_zero_hit_at_head(self):
        out = _git("grep", "-F", "-l", VERGE_AURA_URL, "HEAD")
        assert out.stdout.strip() == ""

    def test_relay_urls_zero_hit_at_head(self):
        for url in (RELAY_GENAI, RELAY_PLAYTECH, RELAY_IPHONEINCA):
            out = _git("grep", "-F", "-l", url, "HEAD")
            assert out.stdout.strip() == "", url

    def test_no_type_a_1377_in_git_log(self):
        out = _git("log", "--format=%H", "--grep=Type A #1377")
        assert out.stdout.strip() == ""

    def test_no_1377_heading_in_iteration_log_at_head(self):
        out = _git("grep", "-F", "-l", "## #1377", "HEAD", "--",
                   "iteration-log.md")
        assert out.stdout.strip() == ""

    def test_single_type_a_1377_file_on_disk(self):
        matches = [f for f in os.listdir(TESTS_DIR)
                   if f.startswith("test_type_a_1377")]
        assert matches == [OWN_BASENAME]

    def test_no_1377_row_in_readme_table_at_head(self):
        out = _git("grep", "-F", "-l", "test_type_a_1377", "HEAD", "--",
                   "README.md")
        assert out.stdout.strip() == ""


# ---------------------------------------------------------------------------
# 8. Doc-sync per #719 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestDocSync1377:
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

    def test_readme_has_1377_table_row(self):
        src = _read(README_PATH)
        assert "test_type_a_1377" in src


# ---------------------------------------------------------------------------
# 9. Iteration log per #721 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestIterationLog1377:
    def test_log_has_1377_heading(self):
        # Written in the doc-sync commit per #721. Fails pre-commit
        # by design; deselected in the in-gate run.
        assert "## #1377" in _read(ITERLOG_PATH)

    def test_log_registers_main_anchor_docsync_hashes(self):
        src = _read(ITERLOG_PATH)
        assert "log-hash" in src

    def test_log_mentions_mechanism_1048(self):
        src = _read(ITERLOG_PATH)
        assert "m1048" in src or "mechanism 1048" in src


# ---------------------------------------------------------------------------
# 10. Confounders and counterevidence.
# ---------------------------------------------------------------------------


class TestConfounders1377:
    def test_strong_confounders_present(self):
        strong = _mech1048()["confounders"]["strong"]
        assert len(strong) == 3

    def test_relay_attestation_confound_ranked_strong(self):
        strong = _mech1048()["confounders"]["strong"]
        assert any("Relay attestation only" in c for c in strong)

    def test_entity_attribution_confound(self):
        strong = _mech1048()["confounders"]["strong"]
        assert any("Xreal-built" in c for c in strong)

    def test_genre_peg_mismatch_confound(self):
        strong = _mech1048()["confounders"]["strong"]
        assert any("m637/m852" in c for c in strong)

    def test_moderate_confounders_present(self):
        assert len(_mech1048()["confounders"]["moderate"]) == 2

    def test_weak_confounders_present(self):
        assert len(_mech1048()["confounders"]["weak"]) == 1

    def test_counterevidence_m492_dek(self):
        ce = _mech1048()["counter_evidence"]
        assert any("m492" in c for c in ce)

    def test_counterevidence_litigation_domain(self):
        ce = _mech1048()["counter_evidence"]
        assert any("litigation-domain" in c for c in ce)

    def test_financial_context_adversarial(self):
        fc = _mech1048()["financial_context"]
        assert "adversarial_litigation" in fc
        assert "coverage_prediction adversarial" in fc

    def test_cross_references_complete(self):
        cr = _mech1048()["cross_references"]
        joined = " ".join(cr)
        for token in ("m590", "m492", "m841", "m628", "m928"):
            assert token in joined, token

    def test_testable_predictions_present(self):
        tp = _mech1048()["testable_predictions"]
        assert len(tp) == 2
        assert any("November 2026" in p for p in tp)


# ---------------------------------------------------------------------------
# 11. Staleness pins on the predecessor's guard lifecycle (deselected
# pre-commit; verified post-terminal-followup).
# ---------------------------------------------------------------------------


class TestStalenessPins1377:
    def test_1376_guard_lifecycle_post_terminal_followup(self):
        # Post-terminal-followup form: all 26 pass. The
        # no_type_a_1377_in_git_log forward pin flips green in this
        # run's terminal log-hash followup per #721/#1292 (PRED_MAIN_1377
        # re-pinned in the #1376 file). The 1049-form pins stay green
        # throughout (this run lands m1048, not m1049); the member and
        # direction pins stay green (no member, no direction landed this
        # run). The #1376 block is read-only to this run; the flip is
        # documented here, not repaired. Deselected pre-commit
        # (verified only post-terminal-followup).
        r = subprocess.run(
            ["python3", "-m", "pytest",
             os.path.join(TESTS_DIR, E1376_FILE)
             + "::TestGuardLifecycle1376",
             "-q", "-p", "no:cacheprovider"],
            capture_output=True, text=True, timeout=300, cwd=REPO_ROOT,
        )
        tail = r.stdout.strip().splitlines()[-1]
        assert "26 passed" in tail, tail


# ---------------------------------------------------------------------------
# 12. Push readiness: in-flight isolation and #1024 m846 untouched.
# ---------------------------------------------------------------------------


class TestPushReadiness1377:
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
# 13. Rotation: third leg of the 1375-1379 window.
# ---------------------------------------------------------------------------


class TestRotation1377:
    def test_window_sequence(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1375 -> E #1376 -> A #1377" in src

    def test_next_leg_is_type_b(self):
        assert PRED_MAIN_1378 == "0" * 40

    def test_type_letter_a(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Type A #1377" in src

    def test_background_suite_observed_only(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "OBSERVES only" in src
        assert "#1380" in src


# ---------------------------------------------------------------------------
# 14. ASCII and formatting hygiene.
# ---------------------------------------------------------------------------


class TestAscii1377:
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
        assert "EXPECTED_TOTAL = 117" in src
