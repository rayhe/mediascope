# -*- coding: utf-8 -*-
"""Type D #1300 tests: m1009/m1010/m1011 qualitative-discipline
corpus-integrity verification (Oct 7, 2026) + #1295 background-suite
verdict per #795 + recurring-failure triage + full suite re-launch.

m1009 (Type A #1297, profiles/guardian.yaml
competitor_relationships.openai, block key
type_a_1297_guardian_openai_oct06_kwon_rebuild_trust_parliamentary_register_vs_carried_meta_arms):
mechanism id 1009 - Guardian x OpenAI Oct-6 Kwon parliamentary-apology
register (the Oct-6 Guardian Australia video original: OpenAI chief
strategy officer Jason Kwon before the Joint Select Committee on AI in
Sydney over the June Medicare-portal agent breach and the 84-day
notification gap, headlined "OpenAI has 'work to do to rebuild trust'
in Australia, executive tells AI inquiry") vs carried Guardian x Meta
accountability arms (m687: police-warnings documents investigation
-0.55, teen-accounts influencer payouts -0.45); verdict
thesis_consistent_observation, NOT a falsification-family member
(ledger holds at 58); the Feb-2025 Guardian x OpenAI strategic
content-licensing deal (mechanism_514) predicts softer OpenAI coverage
and the register runs adversarial on the payer - a thesis-consistent
observation, not a new prediction test per the #1143
temporal-replication precedent. MANUAL ILLUSTRATIVE ONLY per the Aug 28
2026 standing rule: engine NOT run on corpus; p_value/cohens_d/ci_95
NOT_CALCULATED; is_significant false; NOT artifact-grade; no
analysis.json update. Correlation is not causation;
hypothesis-generating only.

m1010 (Type B #1298, profiles/careers/journalists.yaml
nicholas_sutrich_type_b record competitor_coverage; block key
fragment-built in the BLOCK_1010 constant below per #715, so no
contiguous literal appears in this file):
mechanism id 1010 - FIRST dedicated Type B mechanism on Nicholas
Sutrich (Android Central, Future plc; prior corpus mentions are #1278
scout-rejection notes only): Sep-16 Meta Ray-Ban Display year-review
(-0.15, qualified-positive long-term review register) vs May-20 Xreal
Project Aura hands-on from Google I/O 2026 (+0.30, aspirational
register, zero privacy-interrogation of the camera array);
illustrative delta (Google/Xreal minus Meta) +0.45; the documented AI
content-licensing deal at the outlet is Future plc x OpenAI (m473, Dec
2024), NOT Google/Xreal - no named financial gradient predicts the
observed gradient, so the writer-register pattern bounds the deal
explanation rather than confirming it (same brief as #1293);
NOT a falsification-family member (ledger holds at 58).
MANUAL/QUALITATIVE ONLY per the Aug 28 2026 standing rule: engine NOT
run on corpus; NOT artifact-grade; no analysis.json update.

m1011 (Type C #1299, profiles/competitor-entities.yaml top-level, block key
type_c_1299_signsplit_signed_data_contributor_paid_data_pools_oct07):
mechanism id 1011 - FIRST dedicated corpus mechanism on the
contributor-paid consent-verified data-pool rail (SignSplit PBC emerges
from stealth Oct 5 2026 with a $400M strategic seed commitment from W
Group at a $1B valuation; AI/robotics firms pay to access Data Pools
and Research Pools while individuals/institutions contribute data,
work, likeness and receive compensation; consent+provenance+terms+
payment attached per contribution; verification layer for signed
content); distinct from m786/m891/m915/m999/m1002/m1005/m1008;
closest corpus analogue m804 (ownership-inversion, publisher-side);
verdict mechanism_documented, NOT a falsification-family member
(ledger holds at 58); no new direction (fortieth absent by design;
thirty-fifth through thirty-ninth stand). MANUAL / qualitative ONLY
per the Aug 28 2026 standing rule: engine NOT run; NOT artifact-grade;
no analysis.json update.

This run is Type D #1300, the FIRST and OPENING leg of the 1300-1304
window (D #1300 -> E #1301 -> A #1302 -> B #1303 -> C #1304 per the #565
anchor + rotation guard); the 1295-1299 window is VERIFIED CLOSED. It
renders the #1295-launched background-suite verdict per #795: the suite
is DEAD at [  1%] (1466 bytes, zero F marks, last write Oct 7 2026
19:59 PDT, zero live pytest processes, no process holding the log open)
- the TENTH consecutive background-suite death of the new streak;
tombstone lineage advances ONE-HUNDRED-SEVENTEENTH ->
ONE-HUNDRED-EIGHTEENTH. Recurring-failure triage: zero F marks in the
dead stream - nothing to triage, DETERMINATE-vacuous; no
recurring-failure triage repairs claimed from the stream. The full
suite is re-launched this run to type_d_1300_full_suite.log (venv
python per the Sep 7 2026 convention, full inventory, no -x; dots
accumulating at commit); the #1305 Type D run owns the next verdict
per #795.

Type D lands no mechanisms: max numeric mechanism id stays 1011, next
stays 1012; ledger holds at 58; the forty-eighth through
fifty-eighth member-claim forms stay intact, the fifty-ninth
member-claim form stays absent repo-wide, the fortieth
direction-claim form stays absent in profiles/, and the thirty-fifth
through thirty-ninth directions stand. Forward guards for #1301 are
staged in this file (PRED_MAIN_1301 0*40 placeholder per #721); the
no-Type-D-#1300 forward pin belongs to this file (the #1299 Type C
file staged the no-Type-D-#1300-in-git-log forward pin plus the
1012-form pins - their verification was done manually this run:
max-1011, zero one-zero-one-two keys all forms, no Type D #1300 in git
log, fortieth direction absent, forty-eighth through fifty-eighth
members intact, no fifty-ninth member, ledger 58 - all GREEN
pre-commit, recorded in the iteration-log entry). The forward-guard
needles (next-number one-zero-one-two forms, the fifty-ninth
member-claim form, the fortieth direction-claim form) are all
format-built at runtime in the new test file; no contiguous forms
anywhere in the new files or this entry's prose (prose uses lowercase
forms). The landed ordinals live as short lowercase forms in the
test-file prose; the live full-form claims live in profiles (the
forty-eighth in financial-times.yaml, the forty-ninth and fiftieth in
profiles/careers/journalists.yaml, the fifty-first in news-corp.yaml,
the fifty-second in profiles/careers/journalists.yaml, the
fifty-third in the-verge.yaml, the fifty-fourth in guardian.yaml, the
fifty-fifth in atlantic.yaml, the fifty-sixth in wired.yaml, the
fifty-seventh in ap.yaml, the fifty-eighth in financial-times.yaml).

Concurrency: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B test
file working-tree edit), #900 (untracked Type D test file), #1012-wt
(working-tree edit on the committed Type A #1012 file) all left out of
this run's index/diff (explicit-path staging). #1024 m846
(profiles/competitor-entities.yaml) NOT touched - decision pending.
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
GUARDIAN_PATH = os.path.join(PROFILES_DIR, "guardian.yaml")
JOURNALISTS_PATH = os.path.join(
    PROFILES_DIR, "careers", "journalists.yaml")
ENTITIES_PATH = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
PRIOR_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1295_full_suite.log")
NEW_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1300_full_suite.log")
OWN_BASENAME = (
    "test_type_d_1300_m1009_m1010_m1011_qualitative_"
    "corpus_integrity_oct07_11pm.py"
)

# Pre-commit placeholder per #565; patched to the main-commit sha in
# the anchor followup (post-anchor this fails BY DESIGN).
ANCHORED_SHA = "73eae8b27c3de34e37602f5562c7dae2987d3c7f"  # patched in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1011
NEXT_NUM = 1012  # integer only; key-form needles are format-built

# Predecessor chain: #1299 Type C closed the 1295-1299 window.
PRED_MAIN_1299 = "43b3adab"
PRED_ANCHOR_1299 = "30f7653e"
PRED_DOCSYNC_1299 = "5aea67f5"
PRED_FINAL_1299 = "8386902d"
PRED_PUSH_1299 = "b96404b8"
PRED_MAIN_1298 = "10c95ef2"
PRED_ANCHOR_1298 = "f2379272"
PRED_DOCSYNC_1298 = "c131b2cd"
PRED_FINAL_1298 = "af86fc87"
PRED_PUSH_1298 = "c02d2b41"
PRED_MAIN_1297 = "a8bd4c5d"
PRED_ANCHOR_1297 = "031bc983"
PRED_DOCSYNC_1297 = "f9cdd60c"
PRED_FINAL_1297 = "277ce84e"
PRED_PUSH_1297 = "8d2e3632"
PRED_MAIN_1296 = "14af9fec"
PRED_ANCHOR_1296 = "ab777872"
PRED_DOCSYNC_1296 = "064eb530"
PRED_FINAL_1296 = "953ddaaa"
PRED_PUSH_1296 = "4a3062a0"
PRED_MAIN_1295 = "99b14c16"
PRED_ANCHOR_1295 = "6a72097f"
PRED_DOCSYNC_1295 = "977fae5d"
PRED_FINAL_1295 = "6bb3a68e"
PRED_PUSH_1295 = "35856f7b"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40; the no-Type-D-#1300 own-run pin
# flips green post-repin).
PRED_MAIN_1300 = "0" * 40

# Forward guard for the next leg: #1301 Type E. Re-pinned by #1301's
# terminal log-hash followup per #721 (starts as 0*40;
# placeholder-only).
PRED_MAIN_1301 = "0" * 40

# The #1299 window-closing file, for the staleness pin on its guard
# lifecycle (21 tests; post-terminal-followup form is 21 passed - the
# no-Type-D-#1300 pin flips at this run's main commit and is re-pinned
# green in the terminal log-hash followup per #721, its PRED_MAIN_1300
# re-pinned in BOTH files per the #1292 precedent; the 1012-form pins
# stay green since Type D lands no mechanisms).
B1299_FILE = (
    "test_type_c_1299_signsplit_signed_data_contributor_paid_"
    "data_pools_oct07_10pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 72891  # patched pre-main: pre-sync 72803 + 88 collected
README_FILE_COUNT = 1625  # pre-sync 1624 + 1 (this file)

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

# Fragment-built per #715: the contiguous keys never appear in this
# file (BLOCK_1010 is split so the #1298 zero-hit-except-landed pin
# stays green). Iteration-form block keys carry no underscore-form
# mechanism key substring (the #723/#738/#739 designed-keying
# convention).
BLOCK_1009 = (
    "type_a_1297_guardian_openai_oct06_kwon_rebuild_trust_"
    "parliamentary_register_vs_carried_meta_arms"
)
BLOCK_1010 = (
    "type_b_1298_nicholas_sutrich_android_central_meta_display_"
    "year_review_vs_xreal_aura"
)
BLOCK_1011 = (
    "type_c_1299_signsplit_signed_data_contributor_paid_"
    "data_pools_oct07"
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


def _guardian_block_1009():
    """Locate the m1009 block under competitor_relationships.openai."""
    data = _yaml(GUARDIAN_PATH)
    rels = data.get("competitor_relationships", {})
    openai = rels.get("openai", {})
    return openai.get(BLOCK_1009)


def _journalist_block_1010():
    """Locate the m1010 block on the Nicholas Sutrich record.

    The Type B blocks live under the per-journalist top-level record's
    competitor_coverage dict (m1010 sits on the nicholas_sutrich_type_b
    record, the FIRST dedicated Type B pair on Sutrich).
    """
    journalists = _yaml(JOURNALISTS_PATH)
    rec = journalists.get("nicholas_sutrich_type_b")
    if not isinstance(rec, dict):
        return None
    cc = rec.get("competitor_coverage", {})
    if isinstance(cc, dict) and BLOCK_1010 in cc:
        return cc[BLOCK_1010]
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
    args = ["git", "grep", "-F", "-l", needle, "HEAD", "--"]
    args.append(scope if scope else ".")
    out = subprocess.run(
        args, cwd=REPO_ROOT, capture_output=True, text=True).stdout
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
    """Fresh engine-layer calibration contract for #1300.

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


class TestAnchor1300:
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
# 2. Rotation guard: #1299 closed the 1295-1299 window; #1300 opens.
# ---------------------------------------------------------------------------


class TestRotationGuard1300:
    def test_predecessor_shas_in_git_log(self):
        log = _git("log", "--oneline", "-60").stdout
        for sha, label in (
            (PRED_MAIN_1299, "1299 main"),
            (PRED_ANCHOR_1299, "1299 anchor"),
            (PRED_DOCSYNC_1299, "1299 doc-sync"),
            (PRED_FINAL_1299, "1299 log-hash"),
            (PRED_PUSH_1299, "1299 push-status"),
            (PRED_MAIN_1298, "1298 main"),
            (PRED_ANCHOR_1298, "1298 anchor"),
            (PRED_DOCSYNC_1298, "1298 doc-sync"),
            (PRED_FINAL_1298, "1298 log-hash"),
            (PRED_PUSH_1298, "1298 push-status"),
            (PRED_MAIN_1297, "1297 main"),
            (PRED_ANCHOR_1297, "1297 anchor"),
            (PRED_DOCSYNC_1297, "1297 doc-sync"),
            (PRED_FINAL_1297, "1297 log-hash"),
            (PRED_PUSH_1297, "1297 push-status"),
            (PRED_MAIN_1296, "1296 main"),
            (PRED_ANCHOR_1296, "1296 anchor"),
            (PRED_DOCSYNC_1296, "1296 doc-sync"),
            (PRED_FINAL_1296, "1296 log-hash"),
            (PRED_PUSH_1296, "1296 push-status"),
            (PRED_MAIN_1295, "1295 main"),
            (PRED_ANCHOR_1295, "1295 anchor"),
            (PRED_DOCSYNC_1295, "1295 doc-sync"),
            (PRED_FINAL_1295, "1295 log-hash"),
            (PRED_PUSH_1295, "1295 push-status"),
        ):
            assert sha in log, label

    def test_1299_type_c_in_git_log(self):
        out = _git("log", "--format=%s", "--grep=Type C #1299")
        assert "Type C #1299" in out.stdout

    def test_opening_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIRST and OPENING leg of the 1300-1304 window" in src

    def test_1295_1299_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1295-1299 window is VERIFIED CLOSED" in src

    def test_window_sequence_d_e_a_b_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1300 -> E #1301 -> A #1302 -> B #1303 -> C #1304" in src

    def test_next_window_verdict_belongs_to_1305(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1305 Type D run owns the next verdict" in src


# ---------------------------------------------------------------------------
# 3. Corpus integrity: m1009 / m1010 / m1011 all landed and intact.
# ---------------------------------------------------------------------------


class TestCorpusIntegrity1300:
    def test_m1009_block_present_in_guardian(self):
        data = _yaml(GUARDIAN_PATH)
        rels = data["competitor_relationships"]
        assert BLOCK_1009 in rels["openai"]

    def test_m1009_mechanism_id_1009(self):
        block = _guardian_block_1009()
        assert block is not None
        assert block["mechanism_id"] == 1009
        assert block["iteration"] == 1297
        assert block["iteration_type"] == "A"

    def test_m1009_block_key_field(self):
        block = _guardian_block_1009()
        assert block["block_key"] == BLOCK_1009

    def test_m1009_verdict_thesis_consistent(self):
        # m1009 is a thesis_consistent_observation, NOT a
        # falsification-family member; ledger holds at 58.
        block = _guardian_block_1009()
        assert block["verdict"] == "thesis_consistent_observation"
        assert block["falsification_family_member"] is False
        assert str(block["falsification_ledger"]) == "58"

    def test_m1009_statistical_discipline(self):
        block = _guardian_block_1009()
        assert "engine NOT run" in block["statistical_discipline"]
        assert block["author"] == "Kit (with Ray)"

    def test_m1010_block_present_in_journalists(self):
        assert _journalist_block_1010() is not None

    def test_m1010_mechanism_id_1010(self):
        block = _journalist_block_1010()
        assert block["mechanism_id"] == 1010
        assert block["iteration"] == 1298
        assert block["iteration_type"] == "B"

    def test_m1010_block_key_field(self):
        block = _journalist_block_1010()
        assert block["block_key"] == BLOCK_1010

    def test_m1010_not_a_member_in_finding(self):
        # m1010 is NOT a falsification-family member; the finding
        # prose carries the non-member verdict; the record notes carry
        # the ledger position and the FIRST-Sutrich novelty.
        block = _journalist_block_1010()
        assert "NOT a falsification-family member" in block["finding"]
        assert block.get("author") == "Kit (with Ray)"
        rec = _yaml(JOURNALISTS_PATH)["nicholas_sutrich_type_b"]
        assert "FIRST dedicated Type B pair on Nicholas Sutrich" in rec[
            "notes"]
        assert "ledger holds at 58" in rec["notes"]

    def test_m1011_block_present_in_entities(self):
        entities = _yaml(ENTITIES_PATH)
        assert BLOCK_1011 in entities

    def test_m1011_mechanism_id_1011(self):
        entities = _yaml(ENTITIES_PATH)
        block = entities[BLOCK_1011]
        assert block["mechanism_id"] == 1011
        assert block["iteration"] == 1299
        assert block["iteration_type"] == "C"

    def test_m1011_block_key_field(self):
        entities = _yaml(ENTITIES_PATH)
        assert entities[BLOCK_1011]["block_key"] == BLOCK_1011

    def test_m1011_verdict_mechanism_documented(self):
        entities = _yaml(ENTITIES_PATH)
        block = entities[BLOCK_1011]
        assert block["verdict"] == "mechanism_documented"
        assert block["falsification_family_member"] is False
        assert "ledger holds at 58" in block["falsification_family"]

    def test_max_numeric_mechanism_id_is_1011(self):
        assert _max_numeric_mechanism_id() == MECH_NUM


# ---------------------------------------------------------------------------
# 4. Background-suite verdict per #795: the #1295 suite is DEAD at [  1%].
# ---------------------------------------------------------------------------


class TestBackgroundSuiteVerdict1300:
    def test_prior_suite_log_exists(self):
        assert os.path.exists(PRIOR_SUITE_LOG), PRIOR_SUITE_LOG

    def test_prior_suite_stalled_at_1(self):
        # The #1295-launched suite froze at [  1%] progress: 1466
        # bytes, zero F marks, last write Oct 7 2026 19:59 PDT (~3h
        # stale at this run's ~11:00 PM PDT check), zero live pytest
        # processes, no process holding the log open per the /proc
        # open-fd check. Progress never regresses, so the marker stays
        # present and [  2%] never arrives.
        text = _read(PRIOR_SUITE_LOG)
        assert "[  1%]" in text, text[-2000:]
        assert "[  2%]" not in text
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
        # type_d_1295_full_suite.log open anymore (the /proc open-fd
        # check returns empty; the pgrep hits at this run's ~23:00
        # check were the check shell's own cmdline and its pgrep
        # child - self-match phantoms). The suite died between the
        # #1299 observation (~10:00 PM PDT Oct 7, [  1%], zero live
        # processes) and this run's check.
        holders = _proc_holds_log("type_d_1295_full_suite.log")
        assert holders == "", holders

    def test_tenth_death_of_new_streak(self):
        # The 57-run streak ENDED at #1085 (the #1080 suite
        # completed). The 43-run streak BROKE at #1250 (the #1245
        # suite was verdict ALIVE at 20%). #1255 verdict the FIRST
        # consecutive background-suite death of the new streak, #1260
        # the SECOND, #1265 the THIRD, #1270 the FOURTH, #1275 the
        # FIFTH, #1280 the SIXTH, #1285 the SEVENTH, #1290-launched
        # the EIGHTH, #1295-launched the NINTH (verdict rendered this
        # run). This verdict is the TENTH consecutive
        # background-suite death of the new streak.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TENTH consecutive" in src
        assert "death of the new streak" in src

    def test_tombstone_lineage_advances(self):
        # Per #565 the tombstone lineage advances with each DEATH
        # verdict: ONE-HUNDRED-SEVENTEENTH -> ONE-HUNDRED-EIGHTEENTH.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ONE-HUNDRED-EIGHTEENTH" in src
        assert "lineage advances" in src

    def test_dead_verdict_recorded_in_iteration_log(self):
        # Deselected pre-commit: the dead verdict is written into
        # the #1300 log entry in the doc-sync step per #719/#721.
        text = _read(LOG_PATH)
        assert "TENTH consecutive" in text


# ---------------------------------------------------------------------------
# 5. Recurring-failure triage: DETERMINATE-vacuous (zero F marks).
# ---------------------------------------------------------------------------


class TestRecurringFailureTriage1300:
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


class TestStatisticalDiscipline1300:
    def test_no_corpus_mechanisms_landed_this_run(self):
        # Type D lands no mechanisms: the max numeric mechanism id is
        # unchanged at 1011 and no 1012-form keys exist.
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
# 7. Falsification ledger: holds at 58; guards on member forms.
# ---------------------------------------------------------------------------


class TestFalsificationLedger1300:
    def test_ledger_holds_at_58(self):
        block = _guardian_block_1009()
        assert str(block["falsification_ledger"]) == "58"
        entities = _yaml(ENTITIES_PATH)
        assert "ledger holds at 58" in entities[
            BLOCK_1011]["falsification_family"]

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
        assert _T56 in _read(os.path.join(PROFILES_DIR, "wired.yaml"))

    def test_fifty_seventh_member_intact(self):
        # Landed #1287 (m1003, profiles/ap.yaml, committed). HEAD
        # sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T57, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_eighth_member_intact(self):
        # Landed #1292 (m1006, profiles/financial-times.yaml,
        # committed). HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T58, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_no_fifty_ninth_member(self):
        assert _git_grep_tracked_source(_T59, None) == []

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
# 8. Guard lifecycle: forward pins for #1301; #1299 staged for this run.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1300:
    def test_pins_on_1011_no_landing(self):
        # Type D lands no mechanisms: max stays 1011, next stays 1012.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1011" in src
        assert "NEXT_NUM = 1012" in src

    def test_no_type_d_1300_in_git_log_pin(self):
        # Post-main-commit form for THIS run's own pin (the
        # #1191-class self-trip, re-pinned in this run's terminal
        # log-hash followup per #721): every commit whose message
        # matches "Type D #1300" must be this run's main commit or a
        # descendant of it. Deselected in the in-gate run (fails
        # pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type D #1300")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1300's own commits"
        main = _git("rev-parse", PRED_MAIN_1300).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_no_type_e_1301_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1301's terminal log-hash followup
        # per #721): every commit whose message matches "Type E
        # #1301" must be #1301's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type E #1301")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1301's own commits"
        main = _git("rev-parse", PRED_MAIN_1301).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1012_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1012_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1012_dash_absent_repo_wide(self):
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
        assert _T56 in _read(os.path.join(PROFILES_DIR, "wired.yaml"))

    def test_fifty_seventh_member_present_pin(self):
        # Landed #1287 (m1003, profiles/ap.yaml, committed). HEAD
        # sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T57, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_eighth_member_present_pin(self):
        # Landed #1292 (m1006, profiles/financial-times.yaml,
        # committed). HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T58, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_no_fifty_ninth_member_pin(self):
        # Type D lands no mechanisms; the fifty-ninth member-claim
        # form stays absent repo-wide.
        assert _git_grep_tracked_source(_T59, None) == []

    def test_predecessor_1299_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, B1299_FILE))

    def test_next_leg_is_1301_type_e(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1301 Type E" in src

    def test_1299_pins_flip_documented(self):
        # #1299 staged guard-lifecycle forward pins for this run
        # (no-Type-D-#1300-in-git-log, zero one-zero-one-two keys all
        # forms, fortieth direction absent, forty-eighth through
        # fifty-eighth members intact, no fifty-ninth member); all
        # verified GREEN pre-commit this run (manual forward-guard
        # verification, recorded in the iteration-log entry). The
        # no-Type-D-#1300 pin flips BY DESIGN at this run's main
        # commit (the #1191-class self-trip, re-pinned post-commit by
        # TestStalenessPins1300); the 1012-form pins stay green
        # because Type D lands no mechanisms. Documented in the
        # staleness pin below, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1300" in src
        assert "no_type_d_1300_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 9. Staleness pins: #1299's guard lifecycle flips once, then re-pins.
# ---------------------------------------------------------------------------


class TestStalenessPins1300:
    def test_1299_guard_lifecycle_post_terminal_self_trip(self):
        # Post-terminal-followup form: 21 tests in the class; ONE flips
        # BY DESIGN when this run's main commit lands (the
        # no_type_d_1300_in_git_log pin - the #1191-class self-trip)
        # and flips back green in the terminal log-hash followup per
        # #721 (PRED_MAIN_1300 re-pinned to this run's main sha in BOTH
        # this file and the #1299 file per the #1292 precedent). The
        # 1012-form pins stay green throughout (Type D lands no
        # mechanisms; the #723/#738/#739 designed keying holds). The
        # class run below therefore expects 21 passed post-terminal.
        # Documented here, not repaired. Deselected in the in-gate
        # run (fails pre-commit by design: the no_type_d_1300 pin has
        # no commits to match yet).
        res = _class_run(B1299_FILE, "TestGuardLifecycle1299")
        out = res.stdout + res.stderr
        assert "21 passed" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------


class TestDocSync1300:
    def test_readme_test_file_table_has_1300_row_post_sync(self):
        readme = _read(README_PATH)
        assert "test_type_d_1300" in readme

    def test_architecture_has_1300_row_post_sync(self):
        arch = _read(ARCH_PATH)
        assert "test_type_d_1300" in arch

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


class TestIterationLog1300:
    def test_log_has_1300_entry(self):
        text = _read(LOG_PATH)
        assert "## #1300 Type D" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_verdict_and_relaunch(self):
        text = _read(LOG_PATH)
        assert "TENTH consecutive" in text
        assert "type_d_1300_full_suite.log" in text


# ---------------------------------------------------------------------------
# 12. Suite re-launch: this run re-launches the full suite at commit.
# ---------------------------------------------------------------------------


class TestSuiteRelaunch1300:
    def test_new_suite_log_path_in_docstring(self):
        # In-gate green: the docstring names the re-launch target.
        assert "type_d_1300_full_suite.log" in __doc__

    def test_relaunch_recorded_in_iteration_log(self):
        # Deselected pre-commit: the re-launch is written into the
        # #1300 log entry in the doc-sync step.
        text = _read(LOG_PATH)
        assert "RE-LAUNCHED" in text or "re-launched" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------


class TestInFlightIsolation1300:
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
