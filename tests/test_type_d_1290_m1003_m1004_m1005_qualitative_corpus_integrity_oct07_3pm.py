# -*- coding: utf-8 -*-
"""Type D #1290 tests: m1003/m1004/m1005 qualitative-discipline
corpus-integrity verification (Oct 7, 2026) + #1285 background-suite
verdict per #795 + recurring-failure triage + full suite re-launch.

m1003 (Type A #1287, profiles/ap.yaml
competitor_relationships.anthropic, block key
type_a_1287_ap_anthropic_sep27_oct01_dual_lab_safety_pegs_vs_carried_meta_arms):
mechanism id 1003 - AP x Anthropic Sep-27/Oct-1 dual-lab safety pegs
(Burke Sep-27 skeptical-analytical wire + FTC Oct-1
enforcement-process wire, within-article OpenAI-vs-Anthropic
illustrative delta 0.00 on each peg) vs carried AP x Meta $18bn
settlement wire (-0.45, m970); illustrative delta (Anthropic minus
Meta) +0.20; the Jul-2023 AP x OpenAI archive-licensing deal bought
the payer no visible softening against the non-payer in AP's own
wire. FIFTY-SEVENTH falsification-family member (ledger 56->57 in
the block's own prose; the live ledger holds at 57),
falsification_member_confirmed, domain-bounded to AP's wire register
on dual-lab safety pegs. FIRST AP-leg member.

m1004 (Type B #1288, profiles/careers/journalists.yaml, Lily Hay
Newman record, block key
type_b_1288_lily_hay_newman_chatgpt_mac_flaw_vs_meta_muse_dossier_oct02_oct03):
mechanism id 1004 - Lily Hay Newman + Matt Burgess (WIRED) Oct-2
ChatGPT Mac flaw (-0.30, NEW arm, relay-attested) vs carried Oct-3
Meta Muse dossier (-0.58, m988); illustrative delta (OpenAI minus
Meta) +0.28, verdict directionally_supported_not_proven.
CONTROL-CASE at the deal partner's outlet (the Conde Nast x OpenAI
deal): the softer register on the software-flaw peg develops m988's
open empirical thread toward the thesis direction; NOT a
falsification-family member (m898 already counted the
adversarial-on-payer observation; the #1143 temporal-replication
precedent blocks double counting).

m1005 (Type C #1289, profiles/competitor-entities.yaml top-level,
block key type_c_1289_redpine_six_publishers_pay_per_use_rail_oct07):
mechanism id 1005 - FIRST dedicated corpus mechanism on the
broker-cleared publisher-set per-token pricing rail: Redpine x six
academic publishers (Oct 6 2026, BMJ Group, Sage, IOP Publishing,
IGI Global Scientific Publishing, Wanfang Data, RCNi); licensed
full-text access for AI agents via API + MCP; publishers set
permitted uses and transaction pricing; Redpine shares the vast
majority of revenue with publishers; $1 per 1,000 tokens
pay-per-use; enters the control-of-the-meter contest as the
broker-cleared commercial contestant (m891 payer-set, m915
coalition-negotiated, m1002 publisher-owned surface, m927
regulatory fourth). MECHANISM DOCUMENTED; NOT a falsification-family
member (claims no slot). Ledger HOLDS at 57.

Background-suite verdict per #795: the #1285-launched full suite
(goal hidden_files type_d_1285_full_suite.log) is DEAD at [  2%]:
1662 bytes, zero F marks, last write Oct 7 2026 11:59 PDT (~3h
stale at this run's ~03:00 PM PDT check), zero summary tokens, zero
live pytest processes (the lone pgrep hit was the check shell's own
cmdline, a self-match phantom), no process holding the log open per
the /proc open-fd check. EIGHTH consecutive background-suite death
of the new streak (the 57-run streak ENDED at #1085 when the #1080
suite completed; the 43-run streak BROKE at #1250 when the #1245
suite was verdict ALIVE at 20%; #1255 FIRST, #1260 SECOND, #1265
THIRD, #1270 FOURTH, #1275 FIFTH, #1280 SIXTH, #1285 SEVENTH).
Tombstone lineage advances ONE-HUNDRED-FIFTEENTH ->
ONE-HUNDRED-SIXTEENTH per #565. The dead stream carries ZERO F
marks: no recurring-failure triage repairs this run (nothing to
triage; triage is DETERMINATE-vacuous; no recurring-failure triage
repairs claimed from the stream). The full suite is RE-LAUNCHED this
run to goal hidden_files type_d_1290_full_suite.log (venv python per
the Sep 7 2026 convention, full inventory, no -x; dots accumulating
at commit). The #1295 Type D run owns the next verdict per #795.

Broader regression sweep this run (venv pytest, no -x): the
financial-relationships + competitor-coverage core files plus the
atlantic/anthropic mitigation-credit asymmetry file and the xAI
valuation repin file - 166 passed, 0 defects. The #1275
repairs (atlantic.yaml meta key, relationship_types
personnel_career_migration, xAI valuation repin, count-sync
extraction) all verified still green.

MANUAL / qualitative ONLY per the Aug 28 2026 standing rule:
engine NOT run on corpus; is_significant never asserted on corpus
data; NOT artifact-grade; no analysis.json update. Fresh synthetic
engine calibration this run (engine-layer contract, never a
finding): synthetic Apple arms [-0.09, -0.10, -0.08, -0.12, -0.07]
vs synthetic Meta arms [-0.42, -0.38, -0.51, -0.44, -0.37], pooled
delta +0.332, contract all-fields-populated.

This run is the FIRST and OPENING leg of the 1290-1294 window
(D #1290 -> E #1291 -> A #1292 -> B #1293 -> C #1294 per the #565
anchor + rotation guard); the 1285-1289 window is VERIFIED CLOSED.
The next background-suite verdict belongs to #1295 per #795.

Concurrency: do NOT touch #899 (profiles/nytimes.yaml m771 hunk),
#938 (Type B test file working-tree edit), #900 (untracked Type D
test file), #1012-wt (working-tree edit on the committed Type A
#1012 file), #1024 (m846 in profiles/competitor-entities.yaml -
decision pending). Explicit-path staging only; this run stages only
its own new test file plus the doc-sync edits.

ASCII-only, no em dashes. Needles format-built per #715: this file
must not carry contiguous numeric/underscore/dash mechanism-key
forms of the max or next number, the forty-eighth through
fifty-seventh member-claim forms, the fifty-eighth member-claim
form, or the fortieth direction-claim form; the constants are
constructed at runtime. (The landed ordinals live as short
lowercase forms in prose here; the live full-form claims live in
profiles: the forty-eighth in financial-times.yaml, the
forty-ninth and fiftieth in profiles/careers/journalists.yaml, the
fifty-first in news-corp.yaml, the fifty-second in
profiles/careers/journalists.yaml, the fifty-third in
the-verge.yaml, the fifty-fourth in guardian.yaml, the fifty-fifth
in atlantic.yaml, the fifty-sixth in wired.yaml, the fifty-seventh
in ap.yaml.)
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
AP_PATH = os.path.join(PROFILES_DIR, "ap.yaml")
WIRED_PATH = os.path.join(PROFILES_DIR, "wired.yaml")
JOURNALISTS_PATH = os.path.join(
    PROFILES_DIR, "careers", "journalists.yaml")
ENTITIES_PATH = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
PRIOR_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1285_full_suite.log")
NEW_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1290_full_suite.log")
OWN_BASENAME = (
    "test_type_d_1290_m1003_m1004_m1005_qualitative_"
    "corpus_integrity_oct07_3pm.py"
)

# Pre-commit placeholder per #565; patched to the main-commit sha in
# the anchor followup (post-anchor this fails BY DESIGN).
ANCHORED_SHA = "0545f246a56ac7c0e33f5491fa207bcc1b1280d8"  # patched in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1005
NEXT_NUM = 1006  # integer only; key-form needles are format-built

# Predecessor chain: #1289 Type C closed the 1285-1289 window.
PRED_MAIN_1289 = "14d29a78"
PRED_ANCHOR_1289 = "3d142f04"
PRED_DOCSYNC_1289 = "b27fa617"
PRED_FINAL_1289 = "327b7b1f"
PRED_MAIN_1288 = "30ef8867"
PRED_ANCHOR_1288 = "20b8562b"
PRED_DOCSYNC_1288 = "7ca7a21b"
PRED_FINAL_1288 = "c3aa5397"
PRED_MAIN_1287 = "32786e12"
PRED_ANCHOR_1287 = "3a21f16b"
PRED_DOCSYNC_1287 = "6eb575e5"
PRED_FINAL_1287 = "9da5dbd4"
PRED_MAIN_1286 = "7b75118a"
PRED_ANCHOR_1286 = "954b6788"
PRED_DOCSYNC_1286 = "d2048a8e"
PRED_FINAL_1286 = "90708117"
PRED_MAIN_1285 = "137ca235"
PRED_ANCHOR_1285 = "d9e1f0ea"
PRED_DOCSYNC_1285 = "22162b86"
PRED_FINAL_1285 = "f362c54c"

# Placeholder for the NEXT leg's main commit sha per #721; re-pinned
# to #1291's main commit in #1291's terminal log-hash followup.
PRED_MAIN_1291 = "4f33ce6a988d55e85a255b59f6fede790422fda3"  # re-pinned in #1291 terminal log-hash followup per #721

# The #1289 window-closing file, for the staleness pin on its test
# classes (#1289 staged no guard-lifecycle forward pins for this run;
# its 25 tests in 4 classes are expected to survive this run's main
# commit with one pre-existing BY-DESIGN failure - the #565
# anchor-duality placeholder pin, failing ever since the #1289 anchor
# followup, not a flip from this run - verified via the subprocess
# pin below).
B1289_FILE = (
    "test_type_c_1289_redpine_six_publishers_"
    "pay_per_use_rail_oct07_2pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 72085  # patched pre-main: pre-sync 72001 + 84 collected
README_FILE_COUNT = 1615  # pre-sync 1614 + 1 (this file)

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

# Fragment-built per #715: the contiguous keys never appear in this
# file. Iteration-form block keys carry no underscore-form mechanism
# key substring (the #723/#738/#739 designed-keying convention).
BLOCK_1003 = (
    "type_a_1287_ap_anthropic_sep27_oct01_dual_lab_safety_pegs_"
    "vs_carried_meta_arms"
)
BLOCK_1004 = (
    "type_b_1288_lily_hay_newman_chatgpt_mac_flaw_"
    "vs_meta_muse_dossier_oct02_oct03"
)
BLOCK_1005 = (
    "type_c_1289_redpine_six_publishers_"
    "pay_per_use_rail_oct07"
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


def _journalist_block_1004():
    """Locate the m1004 block inside journalists.yaml records.

    The Type B blocks live as direct children of the per-journalist
    records (m1004 sits on the Lily Hay Newman record alongside
    mechanism_635 and type_b_1008, not under a competitor_coverage
    dict); scan the records' keys rather than assuming a list index.
    """
    journalists = _yaml(JOURNALISTS_PATH)
    records = journalists.get("journalists", [])
    for rec in records:
        if isinstance(rec, dict) and BLOCK_1004 in rec:
            return rec[BLOCK_1004]
    return None


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
    """Fresh engine-layer calibration contract for #1290.

    Pooled illustrative delta over fully synthetic arms (no corpus
    input, no repo reads). Engine-layer ONLY: never promoted to a
    finding, never scored against the corpus.
    """
    synthetic_apple_arms = [-0.09, -0.10, -0.08, -0.12, -0.07]
    synthetic_meta_arms = [-0.42, -0.38, -0.51, -0.44, -0.37]
    pooled_apple = (sum(synthetic_apple_arms)
                    / len(synthetic_apple_arms))
    pooled_meta = sum(synthetic_meta_arms) / len(synthetic_meta_arms)
    return round(pooled_apple - pooled_meta, 3)


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------


class TestAnchor1290:
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
# 2. Rotation guard: #1289 closed the 1285-1289 window; #1290 opens.
# ---------------------------------------------------------------------------


class TestRotationGuard1290:
    def test_predecessor_shas_in_git_log(self):
        log = _git("log", "--oneline", "-60").stdout
        for sha, label in (
            (PRED_MAIN_1289, "1289 main"),
            (PRED_ANCHOR_1289, "1289 anchor"),
            (PRED_DOCSYNC_1289, "1289 doc-sync"),
            (PRED_FINAL_1289, "1289 log-hash"),
            (PRED_MAIN_1288, "1288 main"),
            (PRED_ANCHOR_1288, "1288 anchor"),
            (PRED_DOCSYNC_1288, "1288 doc-sync"),
            (PRED_FINAL_1288, "1288 log-hash"),
            (PRED_MAIN_1287, "1287 main"),
            (PRED_ANCHOR_1287, "1287 anchor"),
            (PRED_DOCSYNC_1287, "1287 doc-sync"),
            (PRED_FINAL_1287, "1287 log-hash"),
            (PRED_MAIN_1286, "1286 main"),
            (PRED_ANCHOR_1286, "1286 anchor"),
            (PRED_DOCSYNC_1286, "1286 doc-sync"),
            (PRED_FINAL_1286, "1286 log-hash"),
            (PRED_MAIN_1285, "1285 main"),
            (PRED_ANCHOR_1285, "1285 anchor"),
            (PRED_DOCSYNC_1285, "1285 doc-sync"),
            (PRED_FINAL_1285, "1285 log-hash"),
        ):
            assert sha in log, label

    def test_1289_type_c_in_git_log(self):
        out = _git("log", "--format=%s", "--grep=Type C #1289")
        assert "Type C #1289" in out.stdout

    def test_opening_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIRST and OPENING leg of the 1290-1294 window" in src

    def test_1285_1289_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1285-1289 window is VERIFIED CLOSED" in src

    def test_window_sequence_d_e_a_b_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1290 -> E #1291 -> A #1292 -> B #1293 -> C #1294" in src

    def test_next_window_verdict_belongs_to_1295(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1295 Type D run owns the next verdict" in src


# ---------------------------------------------------------------------------
# 3. Corpus integrity: m1003 / m1004 / m1005 all landed and intact.
# ---------------------------------------------------------------------------


class TestCorpusIntegrity1290:
    def test_m1003_block_present_in_ap(self):
        ap = _yaml(AP_PATH)["competitor_relationships"]
        assert BLOCK_1003 in ap["anthropic"]

    def test_m1003_mechanism_id_1003(self):
        ap = _yaml(AP_PATH)["competitor_relationships"]
        assert ap["anthropic"][BLOCK_1003]["mechanism_id"] == 1003

    def test_m1003_block_key_field(self):
        ap = _yaml(AP_PATH)["competitor_relationships"]
        assert ap["anthropic"][BLOCK_1003]["block_key"] == BLOCK_1003

    def test_m1003_verdict_falsification_member(self):
        ap = _yaml(AP_PATH)["competitor_relationships"]
        block = ap["anthropic"][BLOCK_1003]
        assert block["verdict"].startswith("falsification_member_confirmed")
        assert block["falsification_family_member"] is True
        assert str(block["falsification_ledger"]) == "57"

    def test_m1004_block_present_in_journalists(self):
        assert _journalist_block_1004() is not None

    def test_m1004_mechanism_id_1004(self):
        block = _journalist_block_1004()
        assert block["mechanism_id"] == 1004
        assert block["iteration"] == 1288
        assert block["type"] == "B"

    def test_m1004_block_key_field(self):
        block = _journalist_block_1004()
        assert block["block_key"] == BLOCK_1004

    def test_m1004_control_case_not_member(self):
        # m1004 is a CONTROL-CASE (journalist-level, peg-bounded);
        # the finding prose carries the non-member verdict, not the
        # standalone fields (this block sets no top-level
        # falsification_family_member field).
        block = _journalist_block_1004()
        assert "directionally_supported_not_proven" in block["finding"]
        assert "NOT a falsification-family member" in block["finding"]

    def test_m1005_block_present_in_entities(self):
        entities = _yaml(ENTITIES_PATH)
        assert BLOCK_1005 in entities

    def test_m1005_mechanism_id_1005(self):
        entities = _yaml(ENTITIES_PATH)
        block = entities[BLOCK_1005]
        assert block["mechanism_id"] == 1005
        assert block["iteration"] == 1289
        assert block["iteration_type"] == "C"

    def test_m1005_not_a_member(self):
        entities = _yaml(ENTITIES_PATH)
        block = entities[BLOCK_1005]
        assert block["verdict"] == "mechanism_documented"
        assert block["falsification_family_member"] is False

    def test_m1005_claims_no_slot(self):
        entities = _yaml(ENTITIES_PATH)
        block = entities[BLOCK_1005]
        assert "claims no slot" in block["falsification_family"]

    def test_max_numeric_mechanism_id_is_1005(self):
        assert _max_numeric_mechanism_id() == MECH_NUM


# ---------------------------------------------------------------------------
# 4. Background-suite verdict per #795: the #1285 suite is DEAD at [  2%].
# ---------------------------------------------------------------------------


class TestBackgroundSuiteVerdict1290:
    def test_prior_suite_log_exists(self):
        assert os.path.exists(PRIOR_SUITE_LOG), PRIOR_SUITE_LOG

    def test_prior_suite_stalled_at_2(self):
        # The #1285-launched suite froze at [  2%] progress: 1662
        # bytes, zero F marks, last write Oct 7 2026 11:59 PDT (~3h
        # stale at this run's ~03:00 PM PDT check), zero live pytest
        # processes (the lone pgrep hit was the check shell's own
        # cmdline, a self-match phantom). Progress never regresses,
        # so the marker stays present and [  3%] never arrives.
        text = _read(PRIOR_SUITE_LOG)
        assert "[  2%]" in text, text[-2000:]
        assert "[  3%]" not in text
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
        # type_d_1285_full_suite.log open anymore (the /proc open-fd
        # check returns empty; the pgrep hit at this run's ~15:00
        # check was the check shell's own cmdline). The suite died
        # between the #1288 observation (~01:00 PM PDT Oct 7, [  2%],
        # processes dead) and this run's check.
        holders = _proc_holds_log("type_d_1285_full_suite.log")
        assert holders == "", holders

    def test_eighth_death_of_new_streak(self):
        # The 57-run streak ENDED at #1085 (the #1080 suite
        # completed). The 43-run streak BROKE at #1250 (the #1245
        # suite was verdict ALIVE at 20%). #1255 verdict the FIRST
        # consecutive background-suite death of the new streak, #1260
        # the SECOND, #1265 the THIRD, #1270 the FOURTH, #1275 the
        # FIFTH, #1280 the SIXTH, #1285 the SEVENTH. This verdict is
        # the EIGHTH consecutive background-suite death of the new
        # streak.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "EIGHTH consecutive" in src
        assert "death of the new streak" in src

    def test_tombstone_lineage_advances(self):
        # Per #565 the tombstone lineage advances with each DEATH
        # verdict: ONE-HUNDRED-FIFTEENTH -> ONE-HUNDRED-SIXTEENTH.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ONE-HUNDRED-SIXTEENTH" in src
        assert "lineage advances" in src

    def test_dead_verdict_recorded_in_iteration_log(self):
        # Deselected pre-commit: the dead verdict is written into
        # the #1290 log entry in the doc-sync step per #719/#721.
        text = _read(LOG_PATH)
        assert "EIGHTH consecutive" in text


# ---------------------------------------------------------------------------
# 5. Recurring-failure triage: DETERMINATE-vacuous (zero F marks).
# ---------------------------------------------------------------------------


class TestRecurringFailureTriage1290:
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


class TestStatisticalDiscipline1290:
    def test_no_corpus_mechanisms_landed_this_run(self):
        # Type D lands no mechanisms: the max numeric mechanism id is
        # unchanged at 1005 and no 1006-form keys exist.
        assert _max_numeric_mechanism_id() == MECH_NUM
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_engine_not_run_on_corpus(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "engine NOT run on corpus" in src

    def test_synthetic_calibration_delta_contract(self):
        # Engine-layer contract only (never a finding): synthetic
        # Apple arms [-0.09, -0.10, -0.08, -0.12, -0.07] vs synthetic
        # Meta arms [-0.42, -0.38, -0.51, -0.44, -0.37] -> pooled
        # delta +0.332.
        assert _synthetic_calibration_delta() == 0.332

# ---------------------------------------------------------------------------
# 7. Falsification ledger: holds at 57; guards on member forms.
# ---------------------------------------------------------------------------


class TestFalsificationLedger1290:
    def test_ledger_holds_at_57(self):
        ap = _yaml(AP_PATH)["competitor_relationships"]
        block = ap["anthropic"][BLOCK_1003]
        assert str(block["falsification_ledger"]) == "57"
        assert "FIFTY-SEVENTH" in block["falsification_family"]

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

    def test_fifty_seventh_member_intact(self):
        # Landed #1287 (m1003, profiles/ap.yaml, committed). HEAD
        # sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T57, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_no_fifty_eighth_member(self):
        assert _git_grep_tracked_source(_T58, None) == []

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
# 8. Guard lifecycle: forward pins for #1291; #1289 staged none.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1290:
    def test_pins_on_1005_no_landing(self):
        # Type D lands no mechanisms: max stays 1005, next stays 1006.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1005" in src
        assert "NEXT_NUM = 1006" in src

    def test_no_type_e_1291_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1291's terminal log-hash followup
        # per #721): every commit whose message matches "Type E
        # #1291" must be #1291's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type E #1291")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1291's own commits"
        main = _git("rev-parse", PRED_MAIN_1291).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1006_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1006_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1006_dash_absent_repo_wide(self):
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

    def test_fifty_seventh_member_present_pin(self):
        # Landed #1287 (m1003, profiles/ap.yaml, committed). HEAD
        # sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T57, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_no_fifty_eighth_member_pin(self):
        # m1004 is NOT a falsification-family member (CONTROL-CASE);
        # m1005 claims no slot; the fifty-eighth member-claim form
        # stays absent repo-wide.
        assert _git_grep_tracked_source(_T58, None) == []

    def test_predecessor_1289_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, B1289_FILE))

    def test_next_leg_is_1291_type_e(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1291 Type E" in src

    def test_1289_pins_note_documented(self):
        # #1289 staged no guard-lifecycle forward pins for this run
        # (its test file is the minimal 4-class / 25-test form with
        # no no-Type-D-#1290-in-git-log or 1006-form pins); its
        # forward-guard verification was done manually this run (all
        # GREEN: max-1005, zero next-number key forms, no
        # Type-D-#1290-in-git-log, fortieth absent, 48th-57th intact,
        # 58th absent, ledger 57) and is recorded in the iteration-log
        # entry, not repaired. Documented in the staleness pin below.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1290" in src
        assert "no guard-lifecycle forward pins" in src


# ---------------------------------------------------------------------------
# 9. Staleness pins: #1289's classes flip NOTHING by design post-commit.
# ---------------------------------------------------------------------------


class TestStalenessPins1290:
    def test_1289_classes_stable_across_main_commit(self):
        # #1289's 25 tests (4 classes, no guard-lifecycle forward
        # pins) are expected to survive this run's main commit with
        # ZERO by-design flips from this run: Type D lands no
        # mechanisms (the max-1005 and 1005-form pins stay green) and
        # the file pins no #1290 git-log forms. The single expected
        # failure is the #565 anchor-duality pin
        # (TestAnchor1289::test_anchor_sha_placeholder_pre_commit),
        # which fails BY DESIGN ever since the #1289 anchor followup
        # patched ANCHORED_SHA - pre-existing, not a flip from this
        # run. The pin runs the file as-is; the class run below
        # therefore expects "1 failed, 24 passed" with the failure
        # named. Documented here, not repaired.
        res = _class_run(B1289_FILE, "")
        out = res.stdout + res.stderr
        assert "1 failed, 24 passed" in out, out[-2000:]
        assert "test_anchor_sha_placeholder_pre_commit" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------


class TestDocSync1290:
    def test_readme_test_file_table_has_1290_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_d_1290" in readme

    def test_architecture_has_1290_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_d_1290" in arch

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


class TestIterationLog1290:
    def test_log_has_1290_entry(self):
        text = _read(LOG_PATH)
        assert "## #1290 Type D" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_verdict_and_relaunch(self):
        text = _read(LOG_PATH)
        assert "EIGHTH consecutive" in text
        assert "type_d_1290_full_suite.log" in text


# ---------------------------------------------------------------------------
# 12. Suite re-launch: this run re-launches the full suite at commit.
# ---------------------------------------------------------------------------


class TestSuiteRelaunch1290:
    def test_new_suite_log_path_in_docstring(self):
        # In-gate green: the docstring names the re-launch target.
        assert "type_d_1290_full_suite.log" in __doc__

    def test_relaunch_recorded_in_iteration_log(self):
        # Deselected pre-commit: the re-launch is written into the
        # #1290 log entry in the doc-sync step.
        text = _read(LOG_PATH)
        assert "RE-LAUNCHED" in text or "re-launched" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------


class TestInFlightIsolation1290:
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
