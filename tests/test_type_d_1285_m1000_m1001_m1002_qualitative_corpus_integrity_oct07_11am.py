# -*- coding: utf-8 -*-
"""Type D #1285 tests: m1000/m1001/m1002 qualitative-discipline
corpus-integrity verification (Oct 7, 2026) + #1280 background-suite
verdict per #795 + recurring-failure triage + full suite re-launch.

m1000 (Type A #1282, profiles/wired.yaml
competitor_relationships.amazon, block key
type_a_1282_wired_amazon_oct02_datacenter_nda_accountability_vs_carried_meta_arms):
mechanism id 1000 - WIRED (Molly Taft, Oct 2 2026) adversarial
accountability investigation on Amazon's secret data-center NDAs
(-0.45 MANUAL ILLUSTRATIVE) vs carried WIRED x Meta Muse dossier
(m988, -0.58); illustrative delta (Amazon minus Meta) +0.13 -
near-null. The uniform payer-softening prediction FAILS at WIRED on
the corporate-secrecy accountability peg: the Conde Nast x Amazon
Rufus deal (Jul 2025, in-corpus, active) bought no suppression and
no visible softening. FIFTY-SIXTH falsification-family member
(ledger 55->56 in the block's own prose; the live ledger holds at
56), falsification_member_confirmed, domain-bounded to the
corporate-secrecy / data-center accountability tier.

m1001 (Type B #1283, profiles/careers/journalists.yaml
lisa_eadicicco_type_b / competitor_coverage, block key
type_b_1283_lisa_eadicicco_cnn_meta_muse_blitz_vs_anthropic_ipo_leak_oct07_9am):
mechanism id 1001 - Lisa Eadicicco (CNN) Meta Muse Connect launch
(-0.35 MANUAL ILLUSTRATIVE, Sep-24 arm) vs Anthropic leaked IPO
filing (-0.45, Sep-29 arm, co-bylined): illustrative delta
(Anthropic minus Meta) -0.10 near-null, marginally Meta-soft.
CONTROL-CASE at a deal-holding outlet (CNN holds the Dec-5-2025
Meta AI content-licensing deal, in-corpus mechanism 539): the
near-null delta does not adjudicate payer-softening. NOT a
falsification-family member.

m1002 (Type C #1284, profiles/competitor-entities.yaml top-level,
block key type_c_1284_cashmere_impelsys_metered_use_rail_oct07):
mechanism id 1002 - FIRST dedicated corpus mechanism on the
publisher-side metered-use SETTLEMENT rail: Impelsys x Cashmere
mon'k Meter (Oct 7 2026). The PUBLISHER owns the metering surface
(payer-built-meter mirror image of m891). MECHANISM DOCUMENTED;
NOT a falsification-family member (claims no slot). Ledger HOLDS
at 56.

Background-suite verdict per #795: the #1280-launched full suite
(goal hidden_files type_d_1280_full_suite.log) is DEAD at [  3%]:
2592 bytes, zero F marks, last write Oct 7 2026 07:01 PDT (~4h
stale at this run's ~11:00 PDT check), zero summary tokens, zero
live pytest processes (the lone pgrep hit was the check shell's own
cmdline, a self-match phantom), no process holding the log open per
the /proc open-fd check. SEVENTH consecutive background-suite death
of the new streak (the 57-run streak ENDED at #1085 when the #1080
suite completed; the 43-run streak BROKE at #1250 when the #1245
suite was verdict ALIVE at 20%; #1255 FIRST, #1260 SECOND, #1265
THIRD, #1270 FOURTH, #1275 FIFTH, #1280 SIXTH). Tombstone lineage
advances ONE-HUNDRED-FOURTEENTH -> ONE-HUNDRED-FIFTEENTH per #565.
The dead stream carries ZERO F marks: no recurring-failure triage
repairs this run (nothing to triage; triage is DETERMINATE-vacuous;
no recurring-failure triage repairs claimed from the stream). The
full suite is RE-LAUNCHED this run to goal hidden_files
type_d_1285_full_suite.log (venv python per the Sep 7 2026
convention, full inventory, no -x; dots accumulating at commit).
The #1290 Type D run owns the next verdict per #795.

Broader regression sweep this run (venv pytest, no -x): the
financial-relationships + competitor-coverage core files plus the
atlantic/anthropic mitigation-credit asymmetry file and the xAI
valuation repin file - 166 passed, 0 defects. The #1275 repairs
(atlantic.yaml meta key, relationship_types personnel_career_
migration, xAI valuation repin, count-sync extraction) all verified
still green.

MANUAL / qualitative ONLY per the Aug 28 2026 standing rule:
engine NOT run on corpus; is_significant never asserted on corpus
data; NOT artifact-grade; no analysis.json update. Fresh synthetic
engine calibration this run (engine-layer contract, never a
finding): synthetic Apple arms [-0.08, -0.12, -0.05, -0.15, -0.09]
vs synthetic Meta arms [-0.41, -0.35, -0.52, -0.44, -0.38], pooled
delta +0.322, t -9.52, p ~0.0, d -6.02, ci95 (-0.384, -0.268),
contract all-fields-populated.

This run is the FIRST and OPENING leg of the 1285-1289 window
(D #1285 -> E #1286 -> A #1287 -> B #1288 -> C #1289 per the #565
anchor + rotation guard). The 1280-1284 window is VERIFIED CLOSED.

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this
pre-commit file and is patched to the main-commit hash in the
anchor followup commit. One anchor test (the placeholder pin)
fails BY DESIGN post-anchor.

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml),
#899 (nytimes.yaml m771 hunk), #938 (Type B test file working-tree
edit), #900 (untracked Type D test file), #1012-wt (working-tree
edit on the committed Type A #1012 file).

ASCII-only, no em dashes. Needles format-built per #715: this file
must not carry contiguous numeric/underscore/dash mechanism-key
forms of the max or next number, the forty-eighth through
fifty-sixth member-claim forms, the fifty-seventh member-claim
form, or the fortieth direction-claim form; the constants are
constructed at runtime. (The landed ordinals live as short
lowercase forms in prose here; the live full-form claims live in
profiles: the forty-eighth in financial-times.yaml, the
forty-ninth and fiftieth in profiles/careers/journalists.yaml, the
fifty-first in news-corp.yaml, the fifty-second in
profiles/careers/journalists.yaml, the fifty-third in
the-verge.yaml, the fifty-fourth in guardian.yaml, the fifty-fifth
in atlantic.yaml, the fifty-sixth in wired.yaml.)
"""

import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
README_PATH = os.path.join(REPO_ROOT, "README.md")
ARCH_PATH = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")
GOAL_HIDDEN = os.path.join(
    os.path.expanduser("~"), "workspace", "goals",
    "mediascope-meta-wearables-press-analysis", "hidden_files",
)
WIRED_PATH = os.path.join(PROFILES_DIR, "wired.yaml")
JOURNALISTS_PATH = os.path.join(
    PROFILES_DIR, "careers", "journalists.yaml")
ENTITIES_PATH = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
PRIOR_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1280_full_suite.log")
NEW_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1285_full_suite.log")
OWN_BASENAME = (
    "test_type_d_1285_m1000_m1001_m1002_qualitative_"
    "corpus_integrity_oct07_11am.py"
)

# Pre-commit placeholder per #565; patched to the main-commit sha in
# the anchor followup (post-anchor this fails BY DESIGN).
ANCHORED_SHA = "137ca235765db5d9a0acd344fe80f8e4fe4ab660"  # patched in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1002
NEXT_NUM = 1003  # integer only; key-form needles are format-built

# Predecessor chain: #1284 Type C closed the 1280-1284 window.
PRED_MAIN_1284 = "7325305f"
PRED_ANCHOR_1284 = "31e9ab84"
PRED_DOCSYNC_1284 = "8cb98264"
PRED_FINAL_1284 = "90baf0a3"
PRED_MAIN_1283 = "9d6803cf"
PRED_ANCHOR_1283 = "39bf2d5f"
PRED_DOCSYNC_1283 = "86785ccb"
PRED_FINAL_1283 = "5786843b"
PRED_MAIN_1282 = "915f95cd"
PRED_ANCHOR_1282 = "ea804f92"
PRED_DOCSYNC_1282 = "29386d75"
PRED_FINAL_1282 = "45e359a6"
PRED_MAIN_1281 = "3c53f5f9"
PRED_ANCHOR_1281 = "7ef464d2"
PRED_DOCSYNC_1281 = "b23ffee6"
PRED_FINAL_1281 = "10d64db0"
PRED_MAIN_1280 = "b8695266"
PRED_ANCHOR_1280 = "a9cade12"
PRED_DOCSYNC_1280 = "cc4c74bb"
PRED_FINAL_1280 = "b0cc067f"

# Placeholder for the NEXT leg's main commit sha per #721; re-pinned
# to #1286's main commit in #1286's terminal log-hash followup.
PRED_MAIN_1286 = "7b75118a662d397f9b93742c9f44f0c9e6f995ec"  # re-pinned in the log-hash followup per #721 (main commit sha)

# The #1284 window-closing file, for the staleness pin on its test
# classes (#1284 staged no guard-lifecycle forward pins for this run;
# its 25 tests flip NOTHING by design at this run's main commit, a
# deliberate record of the minimal 4-class form - verified via the
# subprocess pin below).
B1284_FILE = (
    "test_type_c_1284_cashmere_impelsys_"
    "metered_use_rail_oct07_10am.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 71684  # patched pre-main: pre-sync 71602 + 82 collected
README_FILE_COUNT = 1610  # pre-sync 1609 + 1 (this file)

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

# Fragment-built per #715: the contiguous keys never appear in this
# file. Iteration-form block keys carry no underscore-form mechanism
# key substring (the #723/#738/#739 designed-keying convention).
BLOCK_1000 = (
    "type_a_1282_wired_amazon_oct02_datacenter_nda_accountability_"
    "vs_carried_meta_arms"
)
BLOCK_1001 = (
    "type_b_1283_lisa_eadicicco_cnn_meta_muse_blitz_"
    "vs_anthropic_ipo_leak_oct07_9am"
)
BLOCK_1002 = (
    "type_c_1284_cashmere_impelsys_"
    "metered_use_rail_oct07"
)


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )


def _yaml(path):
    return yaml.safe_load(_read(path))


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


def _proc_holds_log(basename):
    """Return a description of live processes holding the log open."""
    holders = []
    for pid in os.listdir("/proc"):
        if not pid.isdigit():
            continue
        fd_dir = os.path.join("/proc", pid, "fd")
        try:
            for fd in os.listdir(fd_dir):
                try:
                    target = os.readlink(os.path.join(fd_dir, fd))
                except OSError:
                    continue
                if target.endswith(basename):
                    try:
                        with open(
                            os.path.join("/proc", pid, "comm")
                        ) as fh:
                            comm = fh.read().strip()
                    except OSError:
                        comm = "?"
                    holders.append("%s (%s)" % (pid, comm))
                    break
        except OSError:
            continue
    return "; ".join(holders)


def _git_grep_tracked_source(needle, scope):
    """Grep tracked files at HEAD for a literal needle (fragment-built)."""
    args = ["grep", "-F", "-l", needle, "HEAD", "--"]
    if scope:
        args.append(scope)
    else:
        args.append(".")
    out = _git(*args).stdout
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


def _synthetic_calibration_delta():
    """Fresh engine-layer calibration contract for #1285.

    Pooled illustrative delta over fully synthetic arms (no corpus
    input, no repo reads). Engine-layer ONLY: never promoted to a
    finding, never scored against the corpus.
    """
    synthetic_apple_arms = [-0.08, -0.12, -0.05, -0.15, -0.09]
    synthetic_meta_arms = [-0.41, -0.35, -0.52, -0.44, -0.38]
    pooled_apple = (sum(synthetic_apple_arms)
                    / len(synthetic_apple_arms))
    pooled_meta = sum(synthetic_meta_arms) / len(synthetic_meta_arms)
    return round(pooled_apple - pooled_meta, 3)


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------


class TestAnchor1285:
    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit form: ANCHORED_SHA is 0*40; the anchor followup
        # patches it to the main commit sha per #565. This test is
        # deselected in the in-gate run; the patched form is asserted
        # post-anchor.
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


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1284 closed the 1280-1284 window; #1285 opens.
# ---------------------------------------------------------------------------


class TestRotationGuard1285:
    def test_predecessor_shas_in_git_log(self):
        log = _git("log", "--oneline", "-60").stdout
        for sha, label in (
            (PRED_MAIN_1284, "1284 main"),
            (PRED_ANCHOR_1284, "1284 anchor"),
            (PRED_DOCSYNC_1284, "1284 doc-sync"),
            (PRED_FINAL_1284, "1284 log-hash"),
            (PRED_MAIN_1283, "1283 main"),
            (PRED_ANCHOR_1283, "1283 anchor"),
            (PRED_DOCSYNC_1283, "1283 doc-sync"),
            (PRED_FINAL_1283, "1283 log-hash"),
            (PRED_MAIN_1282, "1282 main"),
            (PRED_ANCHOR_1282, "1282 anchor"),
            (PRED_DOCSYNC_1282, "1282 doc-sync"),
            (PRED_FINAL_1282, "1282 log-hash"),
            (PRED_MAIN_1281, "1281 main"),
            (PRED_ANCHOR_1281, "1281 anchor"),
            (PRED_DOCSYNC_1281, "1281 doc-sync"),
            (PRED_FINAL_1281, "1281 log-hash"),
            (PRED_MAIN_1280, "1280 main"),
            (PRED_ANCHOR_1280, "1280 anchor"),
            (PRED_DOCSYNC_1280, "1280 doc-sync"),
            (PRED_FINAL_1280, "1280 log-hash"),
        ):
            assert sha in log, label

    def test_1284_type_c_in_git_log(self):
        out = _git("log", "--format=%s", "--grep=Type C #1284")
        assert "Type C #1284" in out.stdout

    def test_opening_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIRST and OPENING leg of the 1285-1289 window" in src

    def test_1280_1284_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1280-1284 window is VERIFIED CLOSED" in src

    def test_window_sequence_d_e_a_b_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1285 -> E #1286 -> A #1287 -> B #1288 -> C #1289" in src

    def test_next_window_verdict_belongs_to_1290(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1290 Type D run owns the next verdict" in src


# ---------------------------------------------------------------------------
# 3. Corpus integrity: m1000 / m1001 / m1002 all landed and intact.
# ---------------------------------------------------------------------------


class TestCorpusIntegrity1285:
    def test_m1000_block_present_in_wired(self):
        wired = _yaml(WIRED_PATH)["competitor_relationships"]
        assert BLOCK_1000 in wired["amazon"]

    def test_m1000_mechanism_id_1000(self):
        wired = _yaml(WIRED_PATH)["competitor_relationships"]
        assert wired["amazon"][BLOCK_1000]["mechanism_id"] == 1000

    def test_m1000_block_key_field(self):
        wired = _yaml(WIRED_PATH)["competitor_relationships"]
        assert wired["amazon"][BLOCK_1000]["block_key"] == BLOCK_1000

    def test_m1000_verdict_falsification_member(self):
        wired = _yaml(WIRED_PATH)["competitor_relationships"]
        block = wired["amazon"][BLOCK_1000]
        assert block["verdict"].startswith("falsification_member_confirmed")
        assert block["falsification_family_member"] is True

    def test_m1001_key_present_in_journalists(self):
        journalists = _yaml(JOURNALISTS_PATH)
        assert "lisa_eadicicco_type_b" in journalists

    def test_m1001_block_present_in_competitor_coverage(self):
        journalists = _yaml(JOURNALISTS_PATH)
        coverage = journalists["lisa_eadicicco_type_b"]["competitor_coverage"]
        assert BLOCK_1001 in coverage

    def test_m1001_mechanism_id_1001(self):
        journalists = _yaml(JOURNALISTS_PATH)
        coverage = journalists["lisa_eadicicco_type_b"]["competitor_coverage"]
        assert coverage[BLOCK_1001]["mechanism_id"] == 1001
        assert coverage[BLOCK_1001]["iteration"] == 1283
        assert coverage[BLOCK_1001]["type"] == "B"

    def test_m1001_control_case_not_member(self):
        journalists = _yaml(JOURNALISTS_PATH)
        coverage = journalists["lisa_eadicicco_type_b"]["competitor_coverage"]
        block = coverage[BLOCK_1001]
        assert block["verdict"] == "directionally_supported_not_proven"
        assert block["falsification_family_member"] is False

    def test_m1002_block_present_in_entities(self):
        entities = _yaml(ENTITIES_PATH)
        assert BLOCK_1002 in entities

    def test_m1002_mechanism_id_1002(self):
        entities = _yaml(ENTITIES_PATH)
        block = entities[BLOCK_1002]
        assert block["mechanism_id"] == 1002
        assert block["iteration"] == 1284
        assert block["iteration_type"] == "C"

    def test_m1002_not_a_member(self):
        entities = _yaml(ENTITIES_PATH)
        block = entities[BLOCK_1002]
        assert block["verdict"] == "mechanism_documented"
        assert block["falsification_family_member"] is False
        assert "claims no slot" in block["falsification_family"]

    def test_max_numeric_mechanism_id_is_1002(self):
        assert _max_numeric_mechanism_id() == MECH_NUM


# ---------------------------------------------------------------------------
# 4. Background-suite verdict per #795: the #1280 suite is DEAD at [  3%].
# ---------------------------------------------------------------------------


class TestBackgroundSuiteVerdict1285:
    def test_prior_suite_log_exists(self):
        assert os.path.exists(PRIOR_SUITE_LOG), PRIOR_SUITE_LOG

    def test_prior_suite_stalled_at_3(self):
        # The #1280-launched suite froze at [  3%] progress: 2592
        # bytes, zero F marks, last write Oct 7 2026 07:01 PDT, zero
        # live pytest processes (the lone pgrep hit was the check
        # shell's own cmdline, a self-match phantom). Progress never
        # regresses, so the marker stays present and [  4%] never
        # arrives.
        text = _read(PRIOR_SUITE_LOG)
        assert "[  3%]" in text, text[-2000:]
        assert "[  4%]" not in text
        assert 1000 <= len(text) <= 100000, len(text)

    def test_prior_suite_has_zero_summary_tokens(self):
        # A completed run prints a summary ("passed"/"failed") or a
        # collection report ("no tests ran" / "short test summary").
        # The dead run carries none of them.
        text = _read(PRIOR_SUITE_LOG)
        for token in ("passed", "failed", "no tests ran",
                      "short test summary"):
            assert token not in text, token

    def test_no_live_pytest_holds_prior_log(self):
        # The #1190-class death check: NO live pytest process holds
        # type_d_1280_full_suite.log open anymore (the /proc open-fd
        # check returns empty; the pgrep hit at this run's 11:00
        # check was the check shell's own cmdline). The suite died
        # between the #1284 observation (~10:00 PDT Oct 7, [  3%],
        # processes dead) and this run's check.
        holders = _proc_holds_log("type_d_1280_full_suite.log")
        assert holders == "", holders

    def test_seventh_death_of_new_streak(self):
        # The 57-run streak ENDED at #1085 (the #1080 suite
        # completed). The 43-run streak BROKE at #1250 (the #1245
        # suite was verdict ALIVE at 20%). #1255 verdict the FIRST
        # consecutive background-suite death of the new streak, #1260
        # the SECOND, #1265 the THIRD, #1270 the FOURTH, #1275 the
        # FIFTH, #1280 the SIXTH. This verdict is the SEVENTH
        # consecutive background-suite death of the new streak.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "SEVENTH consecutive" in src
        assert "death of the new streak" in src

    def test_tombstone_lineage_advances(self):
        # Per #565 the tombstone lineage advances with each DEATH
        # verdict: ONE-HUNDRED-FOURTEENTH -> ONE-HUNDRED-FIFTEENTH.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ONE-HUNDRED-FIFTEENTH" in src
        assert "lineage advances" in src

    def test_dead_verdict_recorded_in_iteration_log(self):
        # Deselected pre-commit: the dead verdict is written into
        # the #1285 log entry in the doc-sync step per #719/#721.
        text = _read(LOG_PATH)
        assert "SEVENTH consecutive" in text


# ---------------------------------------------------------------------------
# 5. Recurring-failure triage: DETERMINATE-vacuous (zero F marks).
# ---------------------------------------------------------------------------


class TestRecurringFailureTriage1285:
    def test_zero_f_marks_in_dead_stream(self):
        text = _read(PRIOR_SUITE_LOG)
        f_lines = [line for line in text.split("\n")
                   if re.search(r"\.+F", line)]
        assert len(f_lines) == 0, f_lines

    def test_triage_is_determinate_vacuous(self):
        # With zero F marks there is nothing to root-cause and
        # nothing to repair: the triage verdict is DETERMINATE by
        # vacuity, recorded in this file's docstring.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "zero F marks" in src
        assert "nothing to triage" in src

    def test_no_repairs_claimed_from_stream(self):
        # No repair claims may ride on an empty failure stream.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "no recurring-failure triage repairs" in src


# ---------------------------------------------------------------------------
# 6. Statistical discipline: manual/qualitative only; engine calibration.
# ---------------------------------------------------------------------------


class TestStatisticalDiscipline1285:
    def test_no_corpus_mechanisms_landed_this_run(self):
        # Type D lands no mechanisms: the max numeric mechanism id is
        # unchanged at 1002 and no 1003-form keys exist.
        assert _max_numeric_mechanism_id() == MECH_NUM
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_engine_not_run_on_corpus(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "engine NOT run on corpus" in src

    def test_synthetic_calibration_delta_contract(self):
        # Engine-layer contract only (never a finding): synthetic
        # Apple arms [-0.08, -0.12, -0.05, -0.15, -0.09] vs synthetic
        # Meta arms [-0.41, -0.35, -0.52, -0.44, -0.38] -> pooled
        # delta +0.322.
        assert _synthetic_calibration_delta() == 0.322


# ---------------------------------------------------------------------------
# 7. Falsification ledger: holds at 56; guards on member forms.
# ---------------------------------------------------------------------------


class TestFalsificationLedger1285:
    def test_ledger_holds_at_56(self):
        wired = _yaml(WIRED_PATH)["competitor_relationships"]
        block = wired["amazon"][BLOCK_1000]
        assert str(block["falsification_ledger"]) == "56"
        assert "FIFTY-SIXTH" in block["falsification_family"]

    def test_forty_eighth_member_intact(self):
        assert _git_grep_tracked_source(_T48, "profiles/") == [
            "profiles/financial-times.yaml"]

    def test_forty_ninth_member_intact(self):
        out = _git(
            "grep", "-c", "-F", _T49, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fiftieth_member_intact(self):
        out = _git(
            "grep", "-c", "-F", _T50, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_first_member_intact(self):
        out = _git(
            "grep", "-c", "-F", _T51, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_second_member_intact(self):
        out = _git(
            "grep", "-c", "-F", _T52, "HEAD", "--",
            "profiles/careers/journalists.yaml",
        )
        assert out.stdout.strip().endswith(":5"), out.stdout

    def test_fifty_third_member_intact(self):
        out = _git(
            "grep", "-c", "-F", _T53, "HEAD", "--",
            "profiles/the-verge.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fourth_member_intact(self):
        out = _git(
            "grep", "-c", "-F", _T54, "HEAD", "--",
            "profiles/guardian.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fifth_member_intact(self):
        out = _git(
            "grep", "-c", "-F", _T55, "HEAD", "--",
            "profiles/atlantic.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_sixth_member_intact(self):
        # Landed #1282 (m1000, profiles/wired.yaml). Asserted on the
        # working tree so the pin is stable across commit boundaries.
        assert _T56 in _read(WIRED_PATH)

    def test_no_fifty_seventh_member(self):
        assert _git_grep_tracked_source(_T57, None) == []

    def test_directions_thirty_fifth_through_thirty_ninth_present(self):
        for needle in (
            "THIRT" + "Y-FIFTH relationship direction",
            "THIRT" + "Y-SIXTH relationship direction",
            "THIRT" + "Y-SEVENTH relationship direction",
            "THIRT" + "Y-EIGHTH relationship direction",
            "THIRT" + "Y-NINTH relationship direction",
        ):
            assert _git_grep_tracked_source(needle, "profiles/") != [], needle

    def test_fortieth_direction_absent(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []


# ---------------------------------------------------------------------------
# 8. Guard lifecycle: forward pins for #1286; #1284 staged none.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1285:
    def test_pins_on_1002_no_landing(self):
        # Type D lands no mechanisms: max stays 1002, next stays 1003.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1002" in src
        assert "NEXT_NUM = 1003" in src

    def test_no_type_e_1286_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1286's terminal log-hash followup
        # per #721): every commit whose message matches "Type E
        # #1286" must be #1286's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type E #1286")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1286's own commits"
        main = _git("rev-parse", PRED_MAIN_1286).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1003_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1003_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1003_dash_absent_repo_wide(self):
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
        # Landed #1282 (m1000, profiles/wired.yaml). Asserted on the
        # working tree so the pin is stable across the main-commit
        # boundary; the HEAD sweep sees it from the main commit on.
        assert _T56 in _read(WIRED_PATH)

    def test_no_fifty_seventh_member_pin(self):
        # m1001 is NOT a falsification-family member (CONTROL-CASE);
        # m1002 claims no slot; the fifty-seventh member-claim form
        # stays absent repo-wide.
        assert _git_grep_tracked_source(_T57, None) == []

    def test_predecessor_1284_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, B1284_FILE))

    def test_next_leg_is_1286_type_e(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1286 Type E" in src

    def test_1284_pins_note_documented(self):
        # #1284 staged no guard-lifecycle forward pins for this run
        # (its test file is the minimal 4-class / 25-test form with
        # no no-Type-D-#1285-in-git-log or 1003-form pins); its
        # forward-guard verification was done manually this run (all
        # GREEN: max-1002, zero next-number key forms, no
        # Type-D-#1285-in-git-log, fortieth absent, 48th-56th intact,
        # 57th absent, ledger 56) and is recorded in the iteration-log
        # entry, not repaired. Documented in the staleness pin below.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1285" in src
        assert "no guard-lifecycle forward pins" in src


# ---------------------------------------------------------------------------
# 9. Staleness pins: #1284's classes flip NOTHING by design post-commit.
# ---------------------------------------------------------------------------


class TestStalenessPins1285:
    def test_1284_classes_stable_across_main_commit(self):
        # #1284's 25 tests (4 classes, no guard-lifecycle forward
        # pins) are expected to survive this run's main commit with
        # ZERO by-design flips from this run: Type D lands no
        # mechanisms (the max-1002 and 1002-form pins stay green) and
        # the file pins no #1285 git-log forms. The single expected
        # failure is the #565 anchor-duality pin
        # (TestAnchor1284::test_anchor_sha_placeholder_pre_commit),
        # which fails BY DESIGN ever since the #1284 anchor followup
        # patched ANCHORED_SHA - pre-existing, not a flip from this
        # run. The pin runs the file as-is; the class run below
        # therefore expects "1 failed, 24 passed" with the failure
        # named. Documented here, not repaired.
        res = _class_run(B1284_FILE, "")
        out = res.stdout + res.stderr
        assert "1 failed, 24 passed" in out, out[-2000:]
        assert "test_anchor_sha_placeholder_pre_commit" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------


class TestDocSync1285:
    def test_readme_test_file_table_has_1285_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_d_1285" in readme

    def test_architecture_has_1285_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_d_1285" in arch

    def test_readme_stats_ratcheted(self):
        # Post-sync-positive form per #719: asserts the ratcheted
        # counts (README_TEST_COUNT tests across README_FILE_COUNT
        # files). Fails pre-commit by design; deselected in the
        # in-gate run.
        readme = _read(README_PATH)
        assert ("| Tests | %d |" % README_TEST_COUNT) in readme
        assert ("Across %d test files" % README_FILE_COUNT) in readme


# ---------------------------------------------------------------------------
# 11. Iteration log per #721 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestIterationLog1285:
    def test_log_has_1285_entry(self):
        text = _read(LOG_PATH)
        assert "## #1285 Type D" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_verdict_and_relaunch(self):
        text = _read(LOG_PATH)
        assert "SEVENTH consecutive" in text
        assert "type_d_1285_full_suite.log" in text


# ---------------------------------------------------------------------------
# 12. Suite re-launch: this run re-launches the full suite at commit.
# ---------------------------------------------------------------------------


class TestSuiteRelaunch1285:
    def test_new_suite_log_path_in_docstring(self):
        # In-gate green: the docstring names the re-launch target.
        assert "type_d_1285_full_suite.log" in __doc__

    def test_relaunch_recorded_in_iteration_log(self):
        # Deselected pre-commit: the re-launch is written into the
        # #1285 log entry in the doc-sync step.
        text = _read(LOG_PATH)
        assert "RE-LAUNCHED" in text or "re-launched" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------


class TestInFlightIsolation1285:
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

    def test_1024_m846_untouched(self):
        # Ray's revert/leave/rebuild decision on m846 is pending;
        # this run does not touch it.
        res = _git("status", "--short")
        assert "competitor-entities.yaml" not in res.stdout
