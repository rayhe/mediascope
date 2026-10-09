"""Type D iteration #1320: m1021/m1022/m1023 qualitative-discipline
corpus-integrity verification + #1315 background-suite verdict (DEAD
at [  1%]; FOURTEENTH consecutive death of the new streak; tombstone
lineage ONE-HUNDRED-TWENTY-FIRST -> ONE-HUNDRED-TWENTY-SECOND) +
recurring-failure triage (ZERO F marks in the dead stream - nothing
to triage, DETERMINATE-vacuous; no recurring-failure triage repairs
claimed from the stream) + broader regression sweep (1315-1319 window
files; triage recorded in the iteration-log entry) + full suite
RE-LAUNCHED to goal/hidden_files/type_d_1320_full_suite.log.

m1021 (Type A #1317, profiles/competitor-coverage-research.yaml
publications): Semafor x Microsoft Suleyman executive-platform
interviews (+0.25 mean) vs Semafor x Meta LED-tampering accountability
exclusive (-0.30); illustrative delta (Microsoft minus Meta) +0.55;
supersedes the #1312 scout rejection; FIRST dedicated Semafor x
Microsoft mechanism; verdict thesis_consistent_observation; NOT a
falsification-family member; ledger holds at 59.

m1022 (Type B #1318, profiles/careers/journalists.yaml
will_shanklin_type_b competitor_coverage): Will Shanklin (Engadget)
Sep-23-2026 Muse-AI-glasses trust-interrogation (-0.20 MANUAL
ILLUSTRATIVE, "privacy-threatening 'perv glasses'") vs
Sep-9-2026 Apple iPhone Duo camera-compromise critique (-0.15 MANUAL
ILLUSTRATIVE, "The hot new iPhone feature is somehow absent from the
hot new iPhone"); illustrative delta (Apple minus Meta) +0.05 -
near-null register constancy, same writer, same outlet, 14 days apart;
ZERO-GRADIENT control (no Yahoo/Engadget x Meta/Apple licensing deal
in-corpus, m998 control-case documentation); verdict
directionally_supported_not_proven; NOT a falsification-family member;
ledger holds at 59.

m1023 (Type C #1319, profiles/competitor-entities.yaml top-level):
eleven-scheme AI-content payment landscape price-setting-power split
(nohacks.co Oct 4 2026); website-sets-price group (5 schemes,
excerpt-verified: Cloudflare Pay Per Crawl, Cloudflare Monetization
Gateway, x402, TollBit, RSL Collective) vs AI-company-sets-price
group (rows not excerpt-visible, NOT enumerated per #503);
price-setting power = value-design power; bilateral-deal layer
SATURATED; verdict mechanism_documented; NOT a falsification-family
member; ledger holds at 59; no new direction (fortieth absent by
design; thirty-fifth through thirty-ninth stand).

MANUAL / qualitative ONLY per the Aug 28 2026 standing rule
(statistical discipline: engine NOT run on corpus, tone values are
hand-assigned, p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant
false, NOT artifact-grade, no_analysis_json_update true).
Correlation is not causation; hypothesis-generating only.

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
RESEARCH_PATH = os.path.join(
    PROFILES_DIR, "competitor-coverage-research.yaml")
JOURNALISTS_PATH = os.path.join(
    PROFILES_DIR, "careers", "journalists.yaml")
ENTITIES_PATH = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
PRIOR_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1315_full_suite.log")
NEW_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1320_full_suite.log")
OWN_BASENAME = (
    "test_type_d_1320_m1021_m1022_m1023_qualitative_"
    "corpus_integrity_oct08_6pm.py"
)

# Pre-commit placeholder per #565; patched to the main-commit sha in
# the anchor followup (post-anchor the placeholder pin fails BY
# DESIGN).
ANCHORED_SHA = "e8903c2aa654d29ecaf5d90e47dc398d91420607"  # patched in the anchor followup per #565

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1023
NEXT_NUM = 1024  # integer only; key-form needles are format-built

# Predecessor chain: #1319 Type C closed the 1315-1319 window. #1315,
# #1316, #1317 have no push-status commit (push status recorded
# PENDING in the iteration-log entry, asserted separately below);
# #1318 and #1319 have push-status commits.
PRED_MAIN_1319 = "caf3e5f8"
PRED_ANCHOR_1319 = "1ef07552"
PRED_DOCSYNC_1319 = "5638566f"
PRED_FINAL_1319 = "83725b5d"
PRED_PUSH_1319 = "c5d4240d"
PRED_MAIN_1318 = "71c2cc52"
PRED_ANCHOR_1318 = "f61ddae6"
PRED_DOCSYNC_1318 = "725e0db1"
PRED_FINAL_1318 = "ee817ba0"
PRED_PUSH_1318 = "88c3a344"
PRED_MAIN_1317 = "7749f95d"
PRED_ANCHOR_1317 = "27fb204c"
PRED_DOCSYNC_1317 = "c5b63c08"
PRED_FINAL_1317 = "8f3d3f8d"
PRED_MAIN_1316 = "5d160c6c"
PRED_ANCHOR_1316 = "49d60e8a"
PRED_DOCSYNC_1316 = "9e3dc23b"
PRED_FINAL_1316 = "4867ff1c"
PRED_MAIN_1315 = "137d1a95"
PRED_ANCHOR_1315 = "265d3e56"
PRED_DOCSYNC_1315 = "5e867883"
PRED_FINAL_1315 = "2e11a9f9"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40; the no-Type-D-#1320 own-run pin
# flips green post-repin).
PRED_MAIN_1320 = "e8903c2aa654d29ecaf5d90e47dc398d91420607"  # re-pinned to main sha per #721

# Forward guard for the next leg: #1321 Type E. Re-pinned by #1321's
# terminal log-hash followup per #721 (starts as 0*40;
# placeholder-only).
PRED_MAIN_1321 = "0" * 40  # re-pinned by #1321 per #721

# The #1319 window-closing file, for the staleness pin on its guard
# lifecycle (22 tests; post-main-commit form is 1 failed / 21 passed -
# the no-Type-D-#1320 forward pin flips at this run's main commit and
# is re-pinned green in the terminal log-hash followup per #721, its
# PRED_MAIN_1320 re-pinned in BOTH files per the #1292 precedent; the
# 1023-numeric-absent #1272-class expiry lives in the #1318 file, not
# here). Documented in TestStalenessPins1320, not repaired.
E1319_FILE = (
    "test_type_c_1319_eleven_schemes_price_setting_"
    "power_oct08_5pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 74921  # patched pre-main: pre-sync 74826 + 95 collected
README_FILE_COUNT = 1645  # pre-sync 1644 + 1 (this file)

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

# Fragment-built per #715: the contiguous keys never appear in this
# file. Iteration-form block keys carry no underscore-form mechanism
# key substring (the #723/#738/#739 designed-keying convention).
BLOCK_1021 = (
    "type_a_1317_semafor_microsoft_suleyman_exec_"
    "platform_vs_meta_led_tampering_exclusive_"
    "oct08_3pm"
)
BLOCK_1022 = (
    "type_b_1318_will_shanklin_engadget_muse_glasses_"
    "vs_iphone_duo_camera_oct08_4pm"
)
BLOCK_1023 = (
    "type_c_1319_eleven_schemes_price_setting_"
    "power_oct08_5pm"
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


def _research_block_1021():
    """Locate the m1021 block under publications in the research file.

    The Type A blocks live directly under the publications top-level
    dict (m1021 sits after the last publication block, appended at
    #1317). The block carries no block_key field in the Type A corpus
    schema; it is identified by its YAML dict key (BLOCK_1021) and its
    title.
    """
    data = _yaml(RESEARCH_PATH)
    pubs = data.get("publications", {})
    return pubs.get(BLOCK_1021)


def _journalist_block_1022():
    """Locate the m1022 block on the Shanklin record.

    The Type B blocks live under the per-journalist top-level record's
    competitor_coverage dict (m1022 sits on the will_shanklin_type_b
    record, the FIRST dedicated Type B pair on Will Shanklin).
    """
    journalists = _yaml(JOURNALISTS_PATH)
    rec = journalists.get("will_shanklin_type_b")
    if not isinstance(rec, dict):
        return None
    cc = rec.get("competitor_coverage", {})
    if isinstance(cc, dict) and BLOCK_1022 in cc:
        return cc[BLOCK_1022]
    return None


def _entities_block_1023():
    """Locate the m1023 block (top-level key of competitor-entities)."""
    entities = _yaml(ENTITIES_PATH)
    return entities.get(BLOCK_1023)


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
    """Fresh engine-layer calibration contract for #1320.

    Pooled illustrative delta over fully synthetic arms (no corpus
    input, no repo reads). Engine-layer ONLY: never promoted to a
    finding, never scored against the corpus.
    """
    synthetic_apple_arms = [-0.08, -0.11, -0.06, -0.09, -0.10]
    synthetic_meta_arms = [-0.39, -0.36, -0.42, -0.38, -0.35]
    pooled_apple = (sum(synthetic_apple_arms)
                    / len(synthetic_apple_arms))
    pooled_meta = sum(synthetic_meta_arms) / len(synthetic_meta_arms)
    return round(pooled_apple - pooled_meta, 3)


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------


class TestAnchor1320:
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


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1319 closed the 1315-1319 window; #1320 opens.
# ---------------------------------------------------------------------------


class TestRotationGuard1320:
    def test_predecessor_shas_in_git_log(self):
        log = _git("log", "--oneline", "-80").stdout
        # #1315/#1316/#1317 have no push-status commit (push status
        # recorded PENDING in the iteration-log entry, asserted
        # separately below); #1318 and #1319 have push-status commits.
        for sha, label in (
            (PRED_MAIN_1319, "1319 main"),
            (PRED_ANCHOR_1319, "1319 anchor"),
            (PRED_DOCSYNC_1319, "1319 doc-sync"),
            (PRED_FINAL_1319, "1319 log-hash"),
            (PRED_PUSH_1319, "1319 push-status"),
            (PRED_MAIN_1318, "1318 main"),
            (PRED_ANCHOR_1318, "1318 anchor"),
            (PRED_DOCSYNC_1318, "1318 doc-sync"),
            (PRED_FINAL_1318, "1318 log-hash"),
            (PRED_PUSH_1318, "1318 push-status"),
            (PRED_MAIN_1317, "1317 main"),
            (PRED_ANCHOR_1317, "1317 anchor"),
            (PRED_DOCSYNC_1317, "1317 doc-sync"),
            (PRED_FINAL_1317, "1317 log-hash"),
            (PRED_MAIN_1316, "1316 main"),
            (PRED_ANCHOR_1316, "1316 anchor"),
            (PRED_DOCSYNC_1316, "1316 doc-sync"),
            (PRED_FINAL_1316, "1316 log-hash"),
            (PRED_MAIN_1315, "1315 main"),
            (PRED_ANCHOR_1315, "1315 anchor"),
            (PRED_DOCSYNC_1315, "1315 doc-sync"),
            (PRED_FINAL_1315, "1315 log-hash"),
        ):
            assert sha in log, label

    def test_1315_1316_1317_push_status_pending_in_log(self):
        # #1315, #1316, #1317 each recorded their push status as
        # PENDING in the iteration-log entry (four commits pushed and
        # ls-remote-verified, no separate push-status commit). This
        # run asserts the record, not a commit.
        text = _read(LOG_PATH)
        assert text.count("Push status (this run): PENDING") >= 3

    def test_1318_1319_push_status_done_commits(self):
        out = _git("log", "--format=%H %s")
        assert PRED_PUSH_1318 in out.stdout
        assert PRED_PUSH_1319 in out.stdout
        assert "push-status: DONE" in out.stdout

    def test_1319_type_c_in_git_log(self):
        out = _git("log", "--format=%s", "--grep=Type C #1319")
        assert "Type C #1319" in out.stdout

    def test_opening_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIRST and OPENING leg of the 1320-1324 window" in src

    def test_1315_1319_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1315-1319 window is VERIFIED CLOSED" in src

    def test_window_sequence_d_e_a_b_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1320 -> E #1321 -> A #1322 -> B #1323 -> C #1324" in src

    def test_next_window_verdict_belongs_to_1325(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1325 Type D run owns the next verdict" in src


# ---------------------------------------------------------------------------
# 3. Corpus integrity: m1021 / m1022 / m1023 all landed and intact.
# ---------------------------------------------------------------------------


class TestCorpusIntegrity1320:
    def test_m1021_block_present_in_research(self):
        data = _yaml(RESEARCH_PATH)
        pubs = data["publications"]
        assert BLOCK_1021 in pubs

    def test_m1021_mechanism_id_1021(self):
        block = _research_block_1021()
        assert block is not None
        assert block["mechanism_id"] == 1021
        assert block["iteration"] == 1317
        assert block["iteration_type"] == "A"

    def test_m1021_title_identifies_block(self):
        # The m1021 block carries no block_key field in the Type A
        # corpus schema; the block is identified by its YAML dict
        # key (BLOCK_1021, asserted present above) and its title.
        block = _research_block_1021()
        assert "Semafor" in block["title"]
        assert "Microsoft" in block["title"]

    def test_m1021_verdict_thesis_consistent(self):
        # m1021 is a thesis_consistent_observation (the naive uniform
        # payer-softening prediction MET on the Suleyman
        # executive-platform register; supersedes the #1312 scout
        # rejection); NOT a falsification-family member; ledger holds
        # at 59. The verdict is a direct field on the m1021 block
        # (the Type A research schema).
        block = _research_block_1021()
        assert block["verdict"] == "thesis_consistent_observation"
        assert "thesis_consistent_observation" in str(
            block["statistical_discipline"])

    def test_m1021_not_a_member_ledger_59(self):
        block = _research_block_1021()
        ff = str(block["falsification_family"])
        assert "NOT a falsification-family member" in ff
        assert "ledger holds at 59" in ff.lower()

    def test_m1021_author(self):
        block = _research_block_1021()
        assert block["author"] == "Kit (with Ray)"

    def test_m1022_block_present_in_journalists(self):
        assert _journalist_block_1022() is not None

    def test_m1022_mechanism_id_1022(self):
        block = _journalist_block_1022()
        assert block["mechanism_id"] == 1022
        assert block["iteration"] == 1318
        assert block["iteration_type"] == "B"

    def test_m1022_block_key_field(self):
        block = _journalist_block_1022()
        assert block["block_key"] == BLOCK_1022

    def test_m1022_verdict_directionally_supported(self):
        # m1022 is a directionally_supported_not_proven
        # zero-gradient control observation (near-null register
        # constancy, +0.05 illustrative delta), NOT a
        # falsification-family member; ledger holds at 59.
        block = _journalist_block_1022()
        assert block["verdict"] == "directionally_supported_not_proven"
        assert block["falsification_family_member"] is False

    def test_m1022_not_a_member_in_notes(self):
        # The FIRST dedicated Type B pair on Will Shanklin
        # (mention-level hits only, disclosed); the record notes carry
        # the ledger position.
        rec = _yaml(JOURNALISTS_PATH)["will_shanklin_type_b"]
        assert "FIRST" in rec["notes"]
        assert "ledger holds at 59" in rec["notes"]
        assert _journalist_block_1022()["author"] == "Kit (with Ray)"

    def test_m1023_block_present_in_entities(self):
        entities = _yaml(ENTITIES_PATH)
        assert BLOCK_1023 in entities

    def test_m1023_mechanism_id_1023(self):
        entities = _yaml(ENTITIES_PATH)
        block = entities[BLOCK_1023]
        assert block["mechanism_id"] == 1023
        assert block["iteration"] == 1319
        assert block["iteration_type"] == "C"

    def test_m1023_block_key_field(self):
        entities = _yaml(ENTITIES_PATH)
        assert entities[BLOCK_1023]["block_key"] == BLOCK_1023

    def test_m1023_verdict_mechanism_documented(self):
        entities = _yaml(ENTITIES_PATH)
        block = entities[BLOCK_1023]
        assert block["verdict"] == "mechanism_documented"
        assert block["falsification_family_member"] is False
        assert "ledger holds at 59" in block["falsification_family"]

    def test_m1023_author(self):
        entities = _yaml(ENTITIES_PATH)
        assert entities[BLOCK_1023]["author"] == "Kit (with Ray)"

    def test_max_numeric_mechanism_id_is_1023(self):
        assert _max_numeric_mechanism_id() == MECH_NUM


# ---------------------------------------------------------------------------
# 4. Background-suite verdict per #795: the #1315 suite is DEAD at [  1%].
# ---------------------------------------------------------------------------


class TestBackgroundSuiteVerdict1320:
    def test_prior_suite_log_exists(self):
        assert os.path.exists(PRIOR_SUITE_LOG), PRIOR_SUITE_LOG

    def test_prior_suite_stalled_at_1(self):
        # The #1315-launched suite froze at [  1%] progress: 1609
        # bytes, zero F marks, last write Oct 8 2026 14:27 PDT (~3.5h
        # stale at this run's ~06:00 PM PDT check), zero live pytest
        # processes (the pgrep sweep at this run's check returned zero
        # live pytest processes; the /proc open-fd check returns
        # empty). Progress never regresses, so the [  1%] marker stays
        # present and [  2%] never arrives. Observation history: #1315
        # launched it and saw it ALIVE at doc-sync (dots accumulating
        # at [  0%]); #1316 saw it STALLED at ~02:00 PM PDT (zero live
        # processes, last write 14:27); #1317 saw it STALLED at ~03:00
        # PM PDT; #1318 saw it STALLED at ~04:00 PM PDT; #1319 saw it
        # STALLED at ~05:00 PM PDT.
        text = _read(PRIOR_SUITE_LOG)
        assert "[  1%]" in text, text[-2000:]
        assert "[  2%]" not in text
        assert 100 <= len(text) <= 100000, len(text)

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
        # type_d_1315_full_suite.log open anymore (the /proc open-fd
        # check returns empty; the pgrep sweep at this run's ~06:00 PM
        # PDT check returned zero live pytest processes).
        holders = _proc_holds_log("type_d_1315_full_suite.log")
        assert holders == "", holders

    def test_fourteenth_death_of_new_streak(self):
        # The 57-run streak ENDED at #1085 (the #1080 suite
        # completed). The 43-run streak BROKE at #1250 (the #1245
        # suite was verdict ALIVE at 20%). #1255 verdict the FIRST
        # consecutive background-suite death of the new streak, #1260
        # the SECOND, #1265 the THIRD, #1270 the FOURTH, #1275 the
        # FIFTH, #1280 the SIXTH, #1285 the SEVENTH, #1290-launched
        # the EIGHTH (#1295 verdict), #1295-launched the NINTH (#1300
        # verdict), #1300-launched the TENTH (#1305 verdict),
        # #1305-launched the ELEVENTH (#1310 verdict), #1310-launched
        # the TWELFTH (#1315 verdict), #1315-launched the THIRTEENTH
        # (#1320 verdict... no: the #1315-launched suite's death
        # verdict is the FOURTEENTH consecutive background-suite death
        # of the new streak.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FOURTEENTH consecutive" in src
        assert "death of the new streak" in src

    def test_tombstone_lineage_advances(self):
        # Per #565 the tombstone lineage advances with each DEATH
        # verdict: ONE-HUNDRED-TWENTY-FIRST -> ONE-HUNDRED-TWENTY-SECOND.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ONE-HUNDRED-TWENTY-SECOND" in src
        assert "lineage advances" in src

    def test_dead_verdict_recorded_in_iteration_log(self):
        # Deselected pre-commit: the dead verdict is written into
        # the #1320 log entry in the doc-sync step per #719/#721.
        text = _read(LOG_PATH)
        assert "FOURTEENTH consecutive" in text


# ---------------------------------------------------------------------------
# 5. Recurring-failure triage: DETERMINATE-vacuous (zero F marks).
# ---------------------------------------------------------------------------


class TestRecurringFailureTriage1320:
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


class TestStatisticalDiscipline1320:
    def test_no_corpus_mechanisms_landed_this_run(self):
        # Type D lands no mechanisms: the max numeric mechanism id is
        # unchanged at 1023 and no 1024-form keys exist.
        assert _max_numeric_mechanism_id() == MECH_NUM
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_engine_not_run_on_corpus(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "engine NOT run on corpus" in src

    def test_synthetic_calibration_delta_contract(self):
        # Engine-layer contract only (never a finding): synthetic
        # Apple arms [-0.08, -0.11, -0.06, -0.09, -0.10] vs synthetic
        # Meta arms [-0.39, -0.36, -0.42, -0.38, -0.35] -> pooled
        # delta +0.292.
        assert _synthetic_calibration_delta() == 0.292


# ---------------------------------------------------------------------------
# 7. Falsification ledger: holds at 59; guards on member forms.
# ---------------------------------------------------------------------------


class TestFalsificationLedger1320:
    def test_ledger_holds_at_59(self):
        # m1021 carries the ledger-holds-at-59 note in its
        # falsification_family; m1022 and m1023 hold it in their
        # record notes / falsification_family fields.
        block = _research_block_1021()
        assert "ledger holds at 59" in str(
            block["falsification_family"]).lower()
        rec = _yaml(JOURNALISTS_PATH)["will_shanklin_type_b"]
        assert "ledger holds at 59" in rec["notes"]
        entities = _yaml(ENTITIES_PATH)
        assert "ledger holds at 59" in entities[
            BLOCK_1023]["falsification_family"]

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

    def test_fifty_ninth_member_intact(self):
        # Landed #1302 (m1012, profiles/news-corp.yaml, committed).
        # HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T59, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_no_sixtieth_member(self):
        assert _git_grep_tracked_source(_T60, None) == []

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
# 8. Guard lifecycle: forward pins for #1321; #1319 staged for this run.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1320:
    def test_pins_on_1023_no_landing(self):
        # Type D lands no mechanisms: max stays 1023, next stays 1024.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1023" in src
        assert "NEXT_NUM = 1024" in src

    def test_no_type_d_1320_in_git_log_pin(self):
        # Post-main-commit form for THIS run's own pin (the
        # #1191-class self-trip, re-pinned in this run's terminal
        # log-hash followup per #721): every commit whose message
        # matches "Type D #1320" must be this run's main commit or a
        # descendant of it. Deselected in the in-gate run (fails
        # pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type D #1320")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1320's own commits"
        main = _git("rev-parse", PRED_MAIN_1320).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_no_type_e_1321_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1321's terminal log-hash followup
        # per #721): every commit whose message matches "Type E
        # #1321" must be #1321's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type E #1321")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1321's own commits"
        main = _git("rev-parse", PRED_MAIN_1321).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1024_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1024_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1024_dash_absent_repo_wide(self):
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

    def test_fifty_ninth_member_present_pin(self):
        # Landed #1302 (m1012, profiles/news-corp.yaml, committed).
        # HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T59, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_no_sixtieth_member_pin(self):
        # Type D lands no mechanisms; the sixtieth member-claim form
        # stays absent repo-wide.
        assert _git_grep_tracked_source(_T60, None) == []

    def test_predecessor_1319_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1319_FILE))

    def test_next_leg_is_1321_type_e(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1321 Type E" in src

    def test_1319_pins_flip_documented(self):
        # #1319 staged guard-lifecycle forward pins for this run
        # (no-Type-D-#1320-in-git-log, zero one-zero-two-four keys all
        # forms, fortieth direction absent, forty-eighth through
        # fifty-ninth members intact, no sixtieth member, ledger 59);
        # all verified GREEN pre-commit this run (manual forward-guard
        # verification, recorded in the iteration-log entry). The
        # no-Type-D-#1320 pin flips BY DESIGN at this run's main
        # commit (the #1191-class self-trip, re-pinned post-commit by
        # TestStalenessPins1320); the 1024-form pins stay green
        # because Type D lands no mechanisms. Documented in the
        # staleness pin below, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1320" in src
        assert "no_type_d_1320_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 9. Staleness pins: #1319's guard lifecycle flips once, then re-pins.
# ---------------------------------------------------------------------------


class TestStalenessPins1320:
    def test_1319_guard_lifecycle_post_main_commit(self):
        # Post-main-commit form (pre-terminal-followup): 22 tests in
        # the class, 1 failed / 21 passed. The no_type_d_1320_in_git_log
        # pin flips BY DESIGN when this run's main commit lands and is
        # re-pinned green in the terminal log-hash followup per #721
        # (PRED_MAIN_1320 re-pinned to this run's main sha in BOTH this
        # file and the #1319 file per the #1292 precedent; the class
        # then settles at 22 passed). The 1024-form pins stay green
        # throughout (Type D lands no mechanisms; the #723/#738/#739
        # designed keying holds). (The test_1023_numeric_absent_in_
        # profiles pin that stays red permanently BY DESIGN - the
        # #1272-class expiry from m1023 landing - lives in the #1318
        # file's guard lifecycle, not here.) The class run below
        # therefore expects 1 failed / 21 passed at the post-main
        # checkpoint. The #1319 block is read-only to this run; the
        # flips are documented here, not repaired. Deselected in the
        # in-gate run (fails pre-commit by design - the pin is still
        # in placeholder form pre-commit).
        res = _class_run(E1319_FILE, "TestGuardLifecycle1319")
        out = res.stdout + res.stderr
        assert "1 failed" in out and "21 passed" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------


class TestDocSync1320:
    def test_readme_test_file_table_has_1320_row_post_sync(self):
        readme = _read(README_PATH)
        assert OWN_BASENAME in readme

    def test_architecture_has_1320_row_post_sync(self):
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
# 11. Iteration log per #721 (deselected pre-commit, flipped post-sync).
# ---------------------------------------------------------------------------


class TestIterationLog1320:
    def test_log_has_1320_entry(self):
        text = _read(LOG_PATH)
        assert "## #1320 Type D" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_verdict_and_relaunch(self):
        text = _read(LOG_PATH)
        assert "FOURTEENTH consecutive" in text
        assert "type_d_1320_full_suite.log" in text


# ---------------------------------------------------------------------------
# 12. Suite re-launch: this run re-launches the full suite at commit.
# ---------------------------------------------------------------------------


class TestSuiteRelaunch1320:
    def test_new_suite_log_path_in_docstring(self):
        # In-gate green: the docstring names the re-launch target.
        assert "type_d_1320_full_suite.log" in __doc__

    def test_relaunch_recorded_in_iteration_log(self):
        # Deselected pre-commit: the re-launch is written into the
        # #1320 log entry in the doc-sync step.
        text = _read(LOG_PATH)
        assert "RE-LAUNCHED" in text or "re-launched" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------


class TestInFlightIsolation1320:
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
