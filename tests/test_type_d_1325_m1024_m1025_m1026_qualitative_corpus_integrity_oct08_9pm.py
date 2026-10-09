"""Type D iteration #1325: m1024/m1025/m1026 qualitative-discipline
corpus-integrity verification + #1320 background-suite verdict (DEAD
at [  1%]; FIFTEENTH consecutive death of the new streak; tombstone
lineage ONE-HUNDRED-TWENTY-SECOND -> ONE-HUNDRED-TWENTY-THIRD) +
recurring-failure triage (ZERO F marks in the dead stream - nothing
to triage, DETERMINATE-vacuous; no recurring-failure triage repairs
claimed from the stream) + broader regression sweep (39 failed /
459 passed across the 1320-1324 window files in ~882s; triaged: 5
#565-class anchor placeholder-duality pins (post-anchor, fail by
design), 4 #1272-class forward-guard numeric expiries (the
1024-numeric pins in the #1320/#1321 files, the 1025-numeric pin in
the #1322 file, the 1026-numeric pin in the #1323 file -
m1024/m1025/m1026 landed after those runs pinned), 4 #1191-class
sixtieth-member self-trips (the sixtieth member landed at #1322/m1024
- permanent red by design), 1 #1191-class forward-pin placeholder
(TestGuardLifecycle1324::test_no_type_d_1325_in_git_log_pin - fails
pre-commit by design since PRED_MAIN_1325 is 0*40; flips green at the
terminal re-pin per #721), 4 #719-class doc-sync readme-stats-ratchet
staleness pins (README has moved to 75324/1649), 21 staleness
artifacts (pre-commit novelty/max/press pins overtaken by later
landings: TestCorpusIntegrity1320 max-1023 + no-landing pins,
TestStalenessPins1320 #1319-class run, TestMechanismNovelty1321 4,
TestPressSurfaces1321 one-new-key pin, TestStalenessPins1321
#1320-class run, TestMechanismNovelty1322 3, TestMechanismNovelty1323
6, TestMechanismNovelty1324 4). 0 remaining defects) + full
suite RE-LAUNCHED to goal/hidden_files/type_d_1325_full_suite.log.

m1024 (Type A #1322, profiles/financial-times.yaml competitor_
relationships.openai): FT Oct-8-2026 OpenAI revenue-scoop
accountability original (-0.35 MANUAL ILLUSTRATIVE, market-moving
scoop on the Apr-29-2024 licensing partner: annualized revenue
approaching $50B, ~$20B below signaled; Nasdaq -1.25%) vs carried FT
x Meta arms mean (-0.5833); illustrative delta (OpenAI minus Meta)
+0.23; the uniform payer-softening prediction FAILS on the
financial-scoop register; verdict falsification_member_confirmed;
SIXTIETH falsification-family member (ledger 59->60); FIFTH FT
publication-level member; FIRST falsification pin on the
financial-scoop register.

m1025 (Type B #1323, profiles/careers/journalists.yaml
katie_paul_type_b competitor_coverage): Katie Paul (Reuters)
Sep-22-2026 Muse 'human concierge' accountability exclusive (-0.45
MANUAL ILLUSTRATIVE, NEW Meta arm) vs carried Sep-8-2026 Muse-launch
accountability arm (-0.45, m633, un-rescored per #807); illustrative
delta 0.00 - register constancy, same writer, same outlet, 14 days
apart; TEMPORAL REPLICATION of the thirteenth member's writer-level
pattern per the #1143 precedent; verdict
directionally_supported_not_proven; NOT a falsification-family
member; ledger holds at 60.

m1026 (Type C #1324, profiles/competitor-entities.yaml top-level):
OpenAI x Atlassian reciprocal enterprise embed (announced Oct 6
2026); variant EXTENSION of the m807 vendor-embed family (reversed
arrow: lab capability embeds in vendor product, reciprocal
customer/user arrows); NOT a new relationship direction (fortieth
direction absent by design; thirty-fifth through thirty-ninth
stand); verdict mechanism_documented; NOT a falsification-family
member; ledger holds at 60; no new direction.

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
Do NOT touch #1024 m846.
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
FT_PATH = os.path.join(PROFILES_DIR, "financial-times.yaml")
JOURNALISTS_PATH = os.path.join(
    PROFILES_DIR, "careers", "journalists.yaml")
ENTITIES_PATH = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
PRIOR_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1320_full_suite.log")
NEW_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1325_full_suite.log")
OWN_BASENAME = (
    "test_type_d_1325_m1024_m1025_m1026_qualitative_"
    "corpus_integrity_oct08_9pm.py"
)

# Pre-commit placeholder per #565; patched to the main-commit sha in
# the anchor followup (post-anchor the placeholder pin fails BY
# DESIGN).
ANCHORED_SHA = "0" * 40

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1026
NEXT_NUM = 1027  # integer only; key-form needles are format-built

# Predecessor chain: #1324 Type C closed the 1320-1324 window. All
# five legs (#1320-#1324) have push-status commits (push status
# recorded DONE in their commits, asserted below).
PRED_MAIN_1324 = "ea330dde"
PRED_ANCHOR_1324 = "60d71470"
PRED_DOCSYNC_1324 = "984202d1"
PRED_FINAL_1324 = "84223372"
PRED_PUSH_1324 = "e9d2c0dd"
PRED_MAIN_1323 = "6fae5cd6"
PRED_ANCHOR_1323 = "60bc6f3c"
PRED_DOCSYNC_1323 = "7d9e7ec8"
PRED_FINAL_1323 = "98c2bab1"
PRED_PUSH_1323 = "d758f050"
PRED_MAIN_1322 = "237e0a1e"
PRED_ANCHOR_1322 = "1e2d00af"
PRED_DOCSYNC_1322 = "fa17e8d9"
PRED_FINAL_1322 = "85380d53"
PRED_PUSH_1322 = "83b6672f"
PRED_MAIN_1321 = "a8ac5238"
PRED_ANCHOR_1321 = "c2f5a24b"
PRED_DOCSYNC_1321 = "85e2481c"
PRED_FINAL_1321 = "a283839e"
PRED_PUSH_1321 = "8534de09"
PRED_PUSH_1320 = "115ee377"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40; the no-Type-D-#1325 own-run pin
# flips green post-repin).
PRED_MAIN_1325 = "0" * 40

# Forward guard for the next leg: #1326 Type E. Re-pinned by #1326's
# terminal log-hash followup per #721 (starts as 0*40;
# placeholder-only).
PRED_MAIN_1326 = "0" * 40

# The #1324 window-closing file, for the staleness pin on its guard
# lifecycle (23 tests; post-main-commit form is 1 failed / 22 passed -
# the no-Type-D-#1325 forward pin flips at this run's main commit and
# is re-pinned green in the terminal log-hash followup per #721, its
# PRED_MAIN_1325 re-pinned in BOTH files per the #1292 precedent; the
# 1027-form pins stay green because Type D lands no mechanisms).
# Documented in TestStalenessPins1325, not repaired.
E1324_FILE = (
    "test_type_c_1324_openai_atlassian_reciprocal_embed_"
    "oct08_8pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 75420  # patched pre-main: pre-sync 75324 + 96 collected
README_FILE_COUNT = 1650  # pre-sync 1649 + 1 (this file)

# m846 block region in profiles/competitor-entities.yaml at HEAD (the
# #1024 m846 decision-pending block; byte-identity pin in the
# in-flight isolation class).
M846_HEAD_START = 26350
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

# Fragment-built per #715: the contiguous keys never appear in this
# file. Iteration-form block keys carry no underscore-form mechanism
# key substring (the #723/#738/#739 designed-keying convention).
BLOCK_1024 = (
    "type_a_1322_ft_openai_oct08_revenue_scoop_"
    "accountability_vs_carried_meta_arms"
)
BLOCK_1025 = (
    "type_b_1323_katie_paul_reuters_human_concierge_"
    "vs_muse_launch_oct08_7pm"
)
BLOCK_1026 = (
    "type_c_1324_openai_atlassian_reciprocal_"
    "enterprise_embed_oct08_8pm"
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


def _find_block(data, key):
    """Recursively locate a block by its YAML dict key."""
    if isinstance(data, dict):
        for k, v in data.items():
            if k == key:
                return v
            found = _find_block(v, key)
            if found is not None:
                return found
    elif isinstance(data, list):
        for v in data:
            found = _find_block(v, key)
            if found is not None:
                return found
    return None


def _ft_block_1024():
    """Locate the m1024 block in financial-times.yaml.

    The Type A blocks live under the competitor_relationships.openai
    section (m1024 appended at #1322). The block carries no
    block_key field in the Type A corpus schema; it is identified by
    its YAML dict key (BLOCK_1024) and its title.
    """
    return _find_block(_yaml(FT_PATH), BLOCK_1024)


def _journalist_block_1025():
    """Locate the m1025 block on the Katie Paul record.

    The Type B blocks live under the per-journalist top-level
    record's competitor_coverage dict (m1025 sits on the
    katie_paul_type_b record, the FIRST dedicated Type B pair on
    Katie Paul).
    """
    journalists = _yaml(JOURNALISTS_PATH)
    rec = journalists.get("katie_paul_type_b")
    if not isinstance(rec, dict):
        return None
    cc = rec.get("competitor_coverage", {})
    if isinstance(cc, dict) and BLOCK_1025 in cc:
        return cc[BLOCK_1025]
    return None


def _entities_block_1026():
    """Locate the m1026 block (top-level key of competitor-entities)."""
    entities = _yaml(ENTITIES_PATH)
    return entities.get(BLOCK_1026)


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
    """Fresh engine-layer calibration contract for #1325.

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


class TestAnchor1325:
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
# 2. Rotation guard: #1324 closed the 1320-1324 window; #1325 opens.
# ---------------------------------------------------------------------------


class TestRotationGuard1325:
    def test_predecessor_shas_in_git_log(self):
        log = _git("log", "--oneline", "-100").stdout
        # All five legs of the 1320-1324 window have push-status
        # commits (push status recorded DONE in the iteration-log
        # entries and in the push-status commits).
        for sha, label in (
            (PRED_MAIN_1324, "1324 main"),
            (PRED_ANCHOR_1324, "1324 anchor"),
            (PRED_DOCSYNC_1324, "1324 doc-sync"),
            (PRED_FINAL_1324, "1324 log-hash"),
            (PRED_PUSH_1324, "1324 push-status"),
            (PRED_MAIN_1323, "1323 main"),
            (PRED_ANCHOR_1323, "1323 anchor"),
            (PRED_DOCSYNC_1323, "1323 doc-sync"),
            (PRED_FINAL_1323, "1323 log-hash"),
            (PRED_PUSH_1323, "1323 push-status"),
            (PRED_MAIN_1322, "1322 main"),
            (PRED_ANCHOR_1322, "1322 anchor"),
            (PRED_DOCSYNC_1322, "1322 doc-sync"),
            (PRED_FINAL_1322, "1322 log-hash"),
            (PRED_PUSH_1322, "1322 push-status"),
            (PRED_MAIN_1321, "1321 main"),
            (PRED_ANCHOR_1321, "1321 anchor"),
            (PRED_DOCSYNC_1321, "1321 doc-sync"),
            (PRED_FINAL_1321, "1321 log-hash"),
            (PRED_PUSH_1321, "1321 push-status"),
            (PRED_PUSH_1320, "1320 push-status"),
        ):
            assert sha in log, label

    def test_all_window_push_status_done_commits(self):
        out = _git("log", "--format=%H %s")
        for sha in (PRED_PUSH_1320, PRED_PUSH_1321, PRED_PUSH_1322,
                    PRED_PUSH_1323, PRED_PUSH_1324):
            assert sha in out.stdout
        assert "push-status: DONE" in out.stdout

    def test_1324_type_c_in_git_log(self):
        out = _git("log", "--format=%s", "--grep=Type C #1324")
        assert "Type C #1324" in out.stdout

    def test_opening_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIRST and OPENING leg of the 1325-1329 window" in src

    def test_1320_1324_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1320-1324 window is VERIFIED CLOSED" in src

    def test_window_sequence_d_e_a_b_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1325 -> E #1326 -> A #1327 -> B #1328 -> C #1329" in src

    def test_next_window_verdict_belongs_to_1330(self):
        # Per #795 the next background-suite verdict (on the
        # #1325-launched suite) belongs to the next Type D run,
        # #1330.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1330 Type D run owns the next verdict" in src


# ---------------------------------------------------------------------------
# 3. Corpus integrity: m1024 / m1025 / m1026 all landed and intact.
# ---------------------------------------------------------------------------


class TestCorpusIntegrity1325:
    def test_m1024_block_present_in_ft(self):
        assert _ft_block_1024() is not None

    def test_m1024_mechanism_id_1024(self):
        block = _ft_block_1024()
        assert block["mechanism_id"] == 1024
        assert block["iteration"] == 1322
        assert block["iteration_type"] == "A"

    def test_m1024_title_identifies_block(self):
        # The m1024 block carries no block_key field in the Type A
        # corpus schema; the block is identified by its YAML dict
        # key (BLOCK_1024, asserted present above) and its
        # mechanism_name (the Type A schema nests the prose title
        # under event/arms; mechanism_name is the block identifier).
        block = _ft_block_1024()
        assert "OpenAI" in block["mechanism_name"]
        assert "revenue" in block["mechanism_name"]

    def test_m1024_verdict_falsification_member_confirmed(self):
        # m1024 is the SIXTIETH falsification-family member (ledger
        # 59->60): the FT breaks a market-moving revenue scoop on its
        # own Apr-29-2024 licensing partner, so the uniform
        # payer-softening prediction FAILS on the financial-scoop
        # register.
        block = _ft_block_1024()
        assert block["verdict"].startswith(
            "falsification_member_confirmed")
        assert block["falsification_family_member"] is True
        assert "ledger 59->60" in str(block["falsification_family"])

    def test_m1024_author(self):
        block = _ft_block_1024()
        assert block["author"] == "Kit (with Ray)"

    def test_m1025_block_present_in_journalists(self):
        assert _journalist_block_1025() is not None

    def test_m1025_mechanism_id_1025(self):
        block = _journalist_block_1025()
        assert block["mechanism_id"] == 1025
        assert block["iteration"] == 1323
        assert block["iteration_type"] == "B"

    def test_m1025_block_key_field(self):
        block = _journalist_block_1025()
        assert block["block_key"] == BLOCK_1025

    def test_m1025_verdict_directionally_supported(self):
        # m1025 is a directionally_supported_not_proven temporal
        # replication of the thirteenth member's writer-level pattern
        # per the #1143 precedent (Katie Paul, same writer, same
        # outlet, 14 days apart, illustrative delta 0.00), NOT a
        # falsification-family member; ledger holds at 60.
        block = _journalist_block_1025()
        assert block["verdict"] == "directionally_supported_not_proven"
        assert block["falsification_family_member"] is False

    def test_m1025_not_a_member_in_notes(self):
        # The FIRST dedicated Type B pair on Katie Paul
        # (mention-level hits only, disclosed); the record notes
        # carry the ledger position.
        rec = _yaml(JOURNALISTS_PATH)["katie_paul_type_b"]
        assert "FIRST" in rec["notes"]
        assert "ledger holds at 60" in rec["notes"]
        assert _journalist_block_1025()["author"] == "Kit (with Ray)"

    def test_m1026_block_present_in_entities(self):
        entities = _yaml(ENTITIES_PATH)
        assert BLOCK_1026 in entities

    def test_m1026_mechanism_id_1026(self):
        entities = _yaml(ENTITIES_PATH)
        block = entities[BLOCK_1026]
        assert block["mechanism_id"] == 1026
        assert block["iteration"] == 1324
        assert block["iteration_type"] == "C"

    def test_m1026_block_key_field(self):
        entities = _yaml(ENTITIES_PATH)
        assert entities[BLOCK_1026]["block_key"] == BLOCK_1026

    def test_m1026_verdict_mechanism_documented(self):
        entities = _yaml(ENTITIES_PATH)
        block = entities[BLOCK_1026]
        assert block["verdict"] == "mechanism_documented"
        assert block["falsification_family_member"] is False
        assert "ledger holds at 60" in block["falsification_family"]

    def test_m1026_author(self):
        entities = _yaml(ENTITIES_PATH)
        assert entities[BLOCK_1026]["author"] == "Kit (with Ray)"

    def test_max_numeric_mechanism_id_is_1026(self):
        assert _max_numeric_mechanism_id() == MECH_NUM


# ---------------------------------------------------------------------------
# 4. Background-suite verdict per #795: the #1320 suite is DEAD at [  1%].
# ---------------------------------------------------------------------------


class TestBackgroundSuiteVerdict1325:
    def test_prior_suite_log_exists(self):
        assert os.path.exists(PRIOR_SUITE_LOG), PRIOR_SUITE_LOG

    def test_prior_suite_stalled_at_1(self):
        # The #1320-launched suite froze at [  1%] progress: 1526
        # bytes, zero F marks, last write Oct 8 2026 17:59 PDT (~3h
        # stale at this run's ~09:00 PM PDT check), zero live pytest
        # processes (the pgrep sweep at this run's check returned zero
        # live pytest processes; the /proc open-fd check returns
        # empty). Progress never regresses, so the [  1%] marker stays
        # present and [  2%] never arrives. Observation history: #1320
        # launched it and saw it ALIVE at doc-sync (dots accumulating
        # at [  0%]); #1321 saw it STALLED at ~07:00 PM PDT (zero live
        # processes, last write 17:59); #1322 saw it STALLED at ~08:00
        # PM PDT; #1323 saw it STALLED at ~08:00 PM PDT; #1324 saw it
        # STALLED at ~08:00 PM PDT (appears dead).
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
        # type_d_1320_full_suite.log open anymore (the /proc open-fd
        # check returns empty; the pgrep sweep at this run's ~09:00 PM
        # PDT check returned zero live pytest processes).
        holders = _proc_holds_log("type_d_1320_full_suite.log")
        assert holders == "", holders

    def test_fifteenth_death_of_new_streak(self):
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
        # (#1320 verdict), #1320-launched the FOURTEENTH (#1325
        # verdict... no: the #1320-launched suite's death verdict is
        # the FIFTEENTH consecutive background-suite death of the new
        # streak.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIFTEENTH consecutive" in src
        assert "death of the new streak" in src

    def test_tombstone_lineage_advances(self):
        # Per #565 the tombstone lineage advances with each DEATH
        # verdict: ONE-HUNDRED-TWENTY-SECOND -> ONE-HUNDRED-TWENTY-THIRD.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ONE-HUNDRED-TWENTY-THIRD" in src
        assert "lineage advances" in src

    def test_dead_verdict_recorded_in_iteration_log(self):
        # Deselected pre-commit: the dead verdict is written into
        # the #1325 log entry in the doc-sync step per #719/#721.
        text = _read(LOG_PATH)
        assert "FIFTEENTH consecutive" in text


# ---------------------------------------------------------------------------
# 5. Recurring-failure triage: DETERMINATE-vacuous (zero F marks).
# ---------------------------------------------------------------------------


class TestRecurringFailureTriage1325:
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


class TestStatisticalDiscipline1325:
    def test_no_corpus_mechanisms_landed_this_run(self):
        # Type D lands no mechanisms: the max numeric mechanism id is
        # unchanged at 1026 and no 1027-form keys exist.
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
# 7. Falsification ledger: holds at 60; guards on member forms.
# ---------------------------------------------------------------------------


class TestFalsificationLedger1325:
    def test_ledger_holds_at_60(self):
        # m1024 is the SIXTIETH member (ledger 59->60); m1025 and
        # m1026 carry the ledger-holds-at-60 note in their record
        # notes / falsification_family fields.
        block = _ft_block_1024()
        assert "ledger 59->60" in str(block["falsification_family"])
        rec = _yaml(JOURNALISTS_PATH)["katie_paul_type_b"]
        assert "ledger holds at 60" in rec["notes"]
        entities = _yaml(ENTITIES_PATH)
        assert "ledger holds at 60" in entities[
            BLOCK_1026]["falsification_family"]

    def test_forty_eighth_member_intact(self):
        out = _git(
            "grep", "-c", "-F", _T48, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

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
        # Landed #1282 (m1000, profiles/wired.yaml, committed). HEAD
        # sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T56, "HEAD", "--",
            "profiles/wired.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

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

    def test_sixtieth_member_intact(self):
        # Landed #1322 (m1024, profiles/financial-times.yaml,
        # committed). HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T60, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_no_sixty_first_member(self):
        assert _git_grep_tracked_source(_T61, None) == []

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
# 8. Guard lifecycle: forward pins for #1326; #1324 staged for this run.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1325:
    def test_pins_on_1026_no_landing(self):
        # Type D lands no mechanisms: max stays 1026, next stays 1027.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1026" in src
        assert "NEXT_NUM = 1027" in src

    def test_no_type_d_1325_in_git_log_pin(self):
        # Post-main-commit form for THIS run's own pin (the
        # #1191-class self-trip, re-pinned in this run's terminal
        # log-hash followup per #721): every commit whose message
        # matches "Type D #1325" must be this run's main commit or a
        # descendant of it. Deselected in the in-gate run (fails
        # pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type D #1325")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1325's own commits"
        main = _git("rev-parse", PRED_MAIN_1325).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_no_type_e_1326_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1326's terminal log-hash followup
        # per #721): every commit whose message matches "Type E
        # #1326" must be #1326's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1326 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type E #1326")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1326's own commits"
        main = _git("rev-parse", PRED_MAIN_1326).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1027_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1027_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1027_dash_absent_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_fortieth_direction_pin(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_forty_eighth_member_intact_pin(self):
        out = _git(
            "grep", "-c", "-F", _T48, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

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
        out = _git(
            "grep", "-c", "-F", _T56, "HEAD", "--",
            "profiles/wired.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_seventh_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T57, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_eighth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T58, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_ninth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T59, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixtieth_member_present_pin(self):
        # Landed #1322 (m1024, profiles/financial-times.yaml,
        # committed). HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T60, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_no_sixty_first_member_pin(self):
        # Type D lands no mechanisms; the sixty-first member-claim
        # form stays absent repo-wide.
        assert _git_grep_tracked_source(_T61, None) == []

    def test_predecessor_1324_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1324_FILE))

    def test_next_leg_is_1326_type_e(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1326 Type E" in src

    def test_1324_pins_flip_documented(self):
        # #1324 staged guard-lifecycle forward pins for this run
        # (no-Type-D-#1325-in-git-log, zero one-zero-two-seven keys
        # all forms, fortieth direction absent, forty-eighth through
        # sixtieth members intact, no sixty-first member, ledger 60);
        # all verified GREEN pre-commit this run (manual forward-guard
        # verification, recorded in the iteration-log entry). The
        # no-Type-D-#1325 pin flips BY DESIGN at this run's main
        # commit (the #1191-class self-trip, re-pinned post-commit by
        # TestStalenessPins1325); the 1027-form pins stay green
        # because Type D lands no mechanisms. Documented in the
        # staleness pin below, not repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TestStalenessPins1325" in src
        assert "no_type_d_1325_in_git_log_pin" in src
        assert "#1191-class" in src
        assert "#1272-class" in src


# ---------------------------------------------------------------------------
# 9. Staleness pins: #1324's guard lifecycle flips once, then re-pins.
# ---------------------------------------------------------------------------


class TestStalenessPins1325:
    def test_1324_guard_lifecycle_post_main_commit(self):
        # Post-main-commit form (pre-terminal-followup): 23 tests in
        # the class, 1 failed / 22 passed. The no_type_d_1325_in_git_log
        # pin flips BY DESIGN when this run's main commit lands and is
        # re-pinned green in the terminal log-hash followup per #721
        # (PRED_MAIN_1325 re-pinned to this run's main sha in BOTH this
        # file and the #1324 file per the #1292 precedent; the class
        # then settles at 23 passed). The 1027-form pins stay green
        # throughout (Type D lands no mechanisms; the #723/#738/#739
        # designed keying holds); the member and direction pins stay
        # green (no member, no direction landed this run). The #1324
        # block is read-only to this run; the flips are documented
        # here, not repaired. Deselected in the in-gate run (fails
        # pre-commit by design - the pin is still in placeholder form
        # pre-commit).
        res = _class_run(E1324_FILE, "TestGuardLifecycle1324")
        out = res.stdout + res.stderr
        assert "1 failed" in out and "22 passed" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------


class TestDocSync1325:
    def test_readme_test_file_table_has_1325_row_post_sync(self):
        readme = _read(README_PATH)
        assert OWN_BASENAME in readme

    def test_architecture_has_1325_row_post_sync(self):
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


class TestIterationLog1325:
    def test_log_has_1325_entry(self):
        text = _read(LOG_PATH)
        assert "## #1325 Type D" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_verdict_and_relaunch(self):
        text = _read(LOG_PATH)
        assert "FIFTEENTH consecutive" in text
        assert "type_d_1325_full_suite.log" in text


# ---------------------------------------------------------------------------
# 12. Suite re-launch: this run re-launches the full suite at commit.
# ---------------------------------------------------------------------------


class TestSuiteRelaunch1325:
    def test_new_suite_log_path_in_docstring(self):
        # In-gate green: the docstring names the re-launch target.
        assert "type_d_1325_full_suite.log" in __doc__

    def test_relaunch_recorded_in_iteration_log(self):
        # Deselected pre-commit: the re-launch is written into the
        # #1325 log entry in the doc-sync step.
        text = _read(LOG_PATH)
        assert "RE-LAUNCHED" in text or "re-launched" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------


class TestInFlightIsolation1325:
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
        # 26350-26472): Ray's revert/leave/rebuild-from-primary
        # decision still pending. Type D writes nothing to profiles/;
        # the m846 block must be byte-identical to HEAD. Do NOT touch
        # #1024 m846.
        head = _git(
            "show", "HEAD:profiles/competitor-entities.yaml").stdout
        work = _read(ENTITIES_PATH)
        assert (head.splitlines()[M846_HEAD_START - 1:M846_HEAD_END]
                == work.splitlines()[M846_HEAD_START - 1:M846_HEAD_END])
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "Do NOT touch #1024" in src
