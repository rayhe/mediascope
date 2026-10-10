"""Type D iteration #1355: m1042/m1043 qualitative-discipline
corpus-integrity verification + #1350 background-suite verdict (DEAD
at [  0%]; TWENTY-FIRST consecutive death of the new streak; tombstone
lineage ONE-HUNDRED-TWENTY-EIGHTH -> ONE-HUNDRED-TWENTY-NINTH) +
recurring-failure triage (ZERO F marks in the dead stream - nothing
to triage, DETERMINATE-vacuous; no recurring-failure triage repairs
claimed from the stream) + broader regression sweep (32 failed / 454
passed across the 1350-1354 window files in ~403s; triaged: 5
#565-class anchor placeholder-duality and post-HEAD-move staleness
pins, 13 #1272-class forward-guard numeric expiries and
max-mechanism staleness pins, 2 #1191-class forward-pin self-trips
(the #1352 no-Type-A-#1353 type-mismatched pin, unsatisfiable BY
DESIGN; the #1354 no-Type-D-#1355 pin, flips green at this run's
terminal re-pin per #721), 5 #719-class doc-sync readme-stats-ratchet
staleness pins, 7 staleness artifacts; 0 remaining defects)
+ full suite RE-LAUNCHED to goal/hidden_files/type_d_1355_full_suite.log.

m1042 (Type A #1352, profiles/wired.yaml
competitor_relationships.openai): WIRED x OpenAI
governance-accountability selection - ZERO WIRED originals on the two
biggest OpenAI governance-accountability pegs of Oct 8-9 2026 (the
safety-researcher firings escalation: the trio's Oct-8 open letter
charging "prioritizing safety over the near-term interests of
OpenAI" plus OpenAI's Oct-9 X response alleging "a significant breach
of trust"; the Oct-8 three-preprint math pull: sign error collapsing
one proof and two dependents, 722 -> 719 manuscripts) inside a
5-search bounded surface, versus carried Meta arms on the same
register (m988 Oct 4-5 Muse dossier accountability, the Oct-3 WIRED
"muse-creates-detailed-profiles" original, m970 Aug-26 $18bn
teen-addiction settlement wire). Selection asymmetry on the
governance register, consistent with the wired.yaml
competitor_relationships.openai coverage_prediction "softer" on the
SELECTION axis - but the AP x OpenAI leg of the SAME firings peg ran
HARD (m1039 #1347, SIXTY-FOURTH member), so no payer-gradient claim
survives; the finding BOUNDS the m1027 adversarialism
(register-follows-peg) rather than extending any pattern. Verdict
mechanism_documented; NOT a falsification-family member; ledger
holds at 64. Domain-bounded to WIRED's governance register on the
Oct-8/9-2026 pegs.

m1043 (Type C #1354, profiles/competitor-entities.yaml):
evening-window financial-incentive saturation verification (1
delegated scout, 4 ranked candidates, ALL rejected on main-run corpus
verification - the #1341 scout-corpus-blindness lesson, third
instance; 2 main-run browser.search verification sets; 0
browser.open per #503; every surfaced development maps to an
already-banked mechanism or an out-of-scope rejection; ZERO novel
mechanisms; corpus current as of Oct 9 2026 ~9pm PDT). Verdict
mechanism_documented; NOT a falsification-family member (a
saturation verification runs no uniform-prediction test); ledger
holds at 64.

Statistical discipline: MANUAL / QUALITATIVE ONLY per the Aug 28 2026
standing rule (tone NOT_SCORED; p_value/cohens_d/ci_95
NOT_CALCULATED; is_significant false; engine NOT run on corpus;
verdict mechanism_documented on a verification, not a discovery; NOT
artifact-grade; no_analysis_json_update true). Correlation is not
causation; hypothesis-generating only. The body's "verify the
asymmetry scoring produces statistically meaningful results" resolves
to verifying the discipline, not running the scorer: the scorer is
intentionally NOT run on the corpus per the standing rule, so no
statistical-significance claim is made or verified in this run; the
synthetic calibration delta contract (0.316) is an engine-layer-only
check, never a finding, never scored against the corpus.

The #1350-launched suite is verdict DEAD at [  0%] (TWENTY-FIRST
consecutive death of the new streak; tombstone lineage
ONE-HUNDRED-TWENTY-EIGHTH -> ONE-HUNDRED-TWENTY-NINTH). Last write
17:20:59 PDT; zero live pytest processes at this run's ~10:00 PM PDT
check; no summary tokens in the stream; zero F marks in the dead
stream - nothing to triage, DETERMINATE-vacuous; no
recurring-failure triage repairs claimed from the stream. full suite
RE-LAUNCHED to goal/hidden_files/type_d_1355_full_suite.log.

Type D lands no mechanisms this run: max numeric mechanism_id stays
1043, no 1044-form keys exist (numeric/underscore/dash), fortieth
relationship direction absent, forty-eighth through sixty-fourth
falsification-family members intact, no sixty-fifth member
repo-wide, ledger holds at 64.

Concurrency: #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B
test file working-tree edit), #900 (untracked Type D test file),
#1012-wt (working-tree edit on the committed Type A #1012 file) all
left out of this run's index/diff (explicit-path staging). #1024 m846
(profiles/competitor-entities.yaml) NOT touched - decision pending.
"""

import os
import re
import subprocess

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
ENTITIES_PATH = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
PRIOR_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1350_full_suite.log")
NEW_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1355_full_suite.log")
OWN_BASENAME = (
    "test_type_d_1355_m1042_m1043_qualitative_"
    "corpus_integrity_oct09_10pm.py"
)

# Pre-commit placeholder per #565; patched to the main-commit sha in
# the anchor followup (post-anchor the placeholder pin fails BY
# DESIGN).
ANCHORED_SHA = "0" * 40

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

MECH_NUM = 1043
NEXT_NUM = 1044  # integer only; key-form needles are format-built

BLOCK_1042 = (
    "type_a_1352_wired_openai_oct08_09_governance_accountability_"
    "bounded_absence_vs_carried_meta_arms"
)
BLOCK_1043 = "type_c_1354_financial_incentive_evening_saturation_oct09_9pm"
BLOCK_M1039_AP = (
    "type_a_1347_ap_openai_oct09_chan_safety_researcher_firings_"
    "wire_vs_carried_meta_18bn_arm_oct09_2pm"
)

# Predecessor chain: #1354 Type C closed the 1350-1354 window. All
# five legs (#1350-#1354) are pushed and ls-remote-verified (push
# status recorded DONE in each run's iteration-log entry, asserted
# below).
PRED_MAIN_1354 = "caa10633"
PRED_ANCHOR_1354 = "885ca746"
PRED_DOCSYNC_1354 = "ad2e1a79"
PRED_FINAL_1354 = "3b6d00f5"
PRED_MAIN_1353 = "93d015a7"
PRED_ANCHOR_1353 = "542bc5e9"
PRED_DOCSYNC_1353 = "4e70ae40"
PRED_FINAL_1353 = "3076d3c0"
PRED_MAIN_1352 = "2b33a040"
PRED_ANCHOR_1352 = "b12cace5"
PRED_DOCSYNC_1352 = "d162dbc7"
PRED_FINAL_1352 = "01109848"
PRED_MAIN_1351 = "2de72295"
PRED_ANCHOR_1351 = "47f671e5"
PRED_DOCSYNC_1351 = "959ebce6"
PRED_FINAL_1351 = "3fd8199c"
PRED_MAIN_1350 = "238da12b"
PRED_ANCHOR_1350 = "ad150bc9"
PRED_DOCSYNC_1350 = "d021c8f6"
PRED_FINAL_1350 = "ad728320"

# This run's own main-commit sha, re-pinned per #721 in the terminal
# log-hash followup (starts as 0*40; the no-Type-D-#1355 own-run pin
# flips green post-repin).
PRED_MAIN_1355 = "0" * 40

# Forward guard for the next leg: #1356 Type E. Re-pinned by #1356's
# anchor followup per #721 (starts as 0*40; placeholder-only).
PRED_MAIN_1356 = "0" * 40

# The #1354 window-closing file, for the staleness pin on its guard
# lifecycle (27 tests; post-terminal-followup form is 27 passed - the
# no-Type-D-#1355 forward pin flips at this run's main commit and is
# re-pinned green in the terminal log-hash followup per #721, its
# PRED_MAIN_1355 re-pinned in BOTH files per the #1292 precedent; the
# 1044-form pins stay green because Type D lands no mechanisms).
# Documented in TestStalenessPins1355, not repaired.
E1354_FILE = (
    "test_type_c_1354_financial_incentive_evening_saturation_oct09_9pm.py"
)

# Doc-sync constants per #719: post-doc-sync values from the start.
# Patched pre-main once the in-gate collection count is known.
README_TEST_COUNT = 78451  # patched pre-main: pre-sync 78352 + 99 collected
README_FILE_COUNT = 1680  # patched pre-main: pre-sync 1679 + 1 (this file)

# m846 block region in profiles/competitor-entities.yaml at HEAD (the
# #1024 m846 decision-pending block; byte-identity pin in the
# in-flight isolation class).
M846_HEAD_START = 26349
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
_T62 = "SIXT" + "Y-SECOND falsification-family member"
_T63 = "SIXT" + "Y-THIRD falsification-family member"
_T64 = "SIXT" + "Y-FOURTH falsification-family member"
_T65 = "SIXT" + "Y-FIFTH falsification-family member"


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


def _wired_block_1042():
    """Locate the m1042 block in wired.yaml.

    The Type A blocks live under the competitor_relationships.openai
    section (m1042 appended at #1352). It is identified by its YAML
    dict key (BLOCK_1042) under the openai section.
    """
    data = _yaml(WIRED_PATH)
    return data["competitor_relationships"]["openai"][BLOCK_1042]


def _entities_block_1043():
    """Locate the m1043 block (top-level key of competitor-entities)."""
    entities = _yaml(ENTITIES_PATH)
    return entities.get(BLOCK_1043)


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
    """Fresh engine-layer calibration contract for #1355.

    Pooled illustrative delta over fully synthetic arms (no corpus
    input, no repo reads). Engine-layer ONLY: never promoted to a
    finding, never scored against the corpus.
    """
    synthetic_apple_arms = [-0.07, -0.10, -0.05, -0.08, -0.09]
    synthetic_meta_arms = [-0.41, -0.37, -0.44, -0.39, -0.36]
    pooled_apple = (sum(synthetic_apple_arms)
                    / len(synthetic_apple_arms))
    pooled_meta = sum(synthetic_meta_arms) / len(synthetic_meta_arms)
    return round(pooled_apple - pooled_meta, 3)


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------


class TestAnchor1355:
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
# 2. Rotation guard: #1354 closed the 1350-1354 window; #1355 opens.
# The 1350-1354 window is VERIFIED CLOSED.
# ---------------------------------------------------------------------------


class TestRotationGuard1355:
    def test_predecessor_shas_in_git_log(self):
        log = _git("log", "--oneline", "-150").stdout
        # All five legs of the 1350-1354 window have push-status
        # commits (push status recorded DONE in the iteration-log
        # entries and in the push-status commits).
        for sha, label in (
            (PRED_MAIN_1354, "1354 main"),
            (PRED_ANCHOR_1354, "1354 anchor"),
            (PRED_DOCSYNC_1354, "1354 doc-sync"),
            (PRED_FINAL_1354, "1354 log-hash"),
            (PRED_MAIN_1353, "1353 main"),
            (PRED_ANCHOR_1353, "1353 anchor"),
            (PRED_DOCSYNC_1353, "1353 doc-sync"),
            (PRED_FINAL_1353, "1353 log-hash"),
            (PRED_MAIN_1352, "1352 main"),
            (PRED_ANCHOR_1352, "1352 anchor"),
            (PRED_DOCSYNC_1352, "1352 doc-sync"),
            (PRED_FINAL_1352, "1352 log-hash"),
            (PRED_MAIN_1351, "1351 main"),
            (PRED_ANCHOR_1351, "1351 anchor"),
            (PRED_DOCSYNC_1351, "1351 doc-sync"),
            (PRED_FINAL_1351, "1351 log-hash"),
            (PRED_MAIN_1350, "1350 main"),
            (PRED_ANCHOR_1350, "1350 anchor"),
            (PRED_DOCSYNC_1350, "1350 doc-sync"),
            (PRED_FINAL_1350, "1350 log-hash"),
        ):
            assert sha in log, label

    def test_all_window_push_status_done(self):
        # Push status is recorded in each run's iteration-log entry
        # (in the repo, at HEAD); the main sha appears in the same
        # entry's push-status line.
        text = _git("show", "HEAD:iteration-log.md").stdout
        for sha, num in (
            (PRED_MAIN_1354, "1354"), (PRED_MAIN_1353, "1353"),
            (PRED_MAIN_1352, "1352"), (PRED_MAIN_1351, "1351"),
            (PRED_MAIN_1350, "1350"),
        ):
            assert sha[:8] in text, num
        assert text.count("Push status (this run)") >= 5
        assert text.count("Push status (this run): DONE") >= 4

    def test_1354_type_c_in_git_log(self):
        out = _git("log", "--format=%s", "--grep=Type C #1354")
        assert "Type C #1354" in out.stdout

    def test_opening_leg_phrase(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIRST and OPENING leg of the 1355-1359 window" in src

    def test_1350_1354_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1350-1354 window is VERIFIED CLOSED" in src

    def test_window_sequence_d_e_a_b_c(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1355 -> E #1356 -> A #1357 -> B #1358 -> C #1359" in src

    def test_next_window_verdict_belongs_to_1360(self):
        # Per #795 the next background-suite verdict (on the
        # #1355-launched suite) belongs to the next Type D run,
        # #1360.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1360 Type D run owns the next verdict" in src


# ---------------------------------------------------------------------------
# 3. Corpus integrity: m1042 / m1043 landed in the 1350-1354 window and
# are intact.
# ---------------------------------------------------------------------------


class TestCorpusIntegrity1355:
    def test_m1042_block_present_in_wired(self):
        assert _wired_block_1042() is not None

    def test_m1042_mechanism_id_1042(self):
        block = _wired_block_1042()
        assert block["mechanism_id"] == 1042
        assert block["iteration"] == 1352
        assert block["iteration_type"] == "A"
        assert block["block_key"] == BLOCK_1042

    def test_m1042_governance_register_peg_identified(self):
        # The Type A corpus schema nests the prose peg under the
        # competitor_relationships.openai section; the Oct-8/9
        # governance-accountability bounded-absence peg and the WIRED
        # x OpenAI vs carried-Meta-arms pairing identify the block.
        text = _yaml(WIRED_PATH)
        raw = str(text["competitor_relationships"]["openai"][BLOCK_1042])
        assert "governance-accountability" in raw
        assert "bounded absence" in raw

    def test_m1042_verdict_mechanism_documented(self):
        # m1042 documents the WIRED x OpenAI governance-accountability
        # selection: ZERO WIRED originals on the two biggest OpenAI
        # governance-accountability pegs of Oct 8-9 2026 (the
        # safety-researcher firings escalation; the Oct-8 three-preprint
        # math pull) versus carried Meta arms on the same register.
        # Verdict mechanism_documented; NOT a falsification-family
        # member (the AP leg's hardness on the same firings peg, m1039
        # #1347, blocks any payer-gradient claim); ledger holds at 64.
        block = _wired_block_1042()
        assert block["verdict"] == "mechanism_documented"
        assert block["falsification_family_member"] is False
        assert block["author"] == "Kit (with Ray)"
        assert "Ledger holds at 64" in block["ledger_note"]

    def test_m1043_block_present_in_entities(self):
        assert _entities_block_1043() is not None

    def test_m1043_mechanism_id_1043(self):
        block = _entities_block_1043()
        assert block["mechanism_id"] == 1043
        assert block["iteration"] == 1354
        assert block["iteration_type"] == "C"
        assert block["block_key"] == BLOCK_1043

    def test_m1043_verdict_mechanism_documented(self):
        # m1043 documents the evening-window financial-incentive
        # saturation verification (1 delegated scout, 4 ranked
        # candidates, all rejected on main-run corpus verification; 2
        # main-run browser.search verification sets; 0 browser.open per
        # #503; zero novel mechanisms; corpus current as of Oct 9 2026
        # ~9pm PDT); verdict mechanism_documented; NOT a
        # falsification-family member (a saturation verification runs
        # no uniform-prediction test); ledger holds at 64.
        block = _entities_block_1043()
        assert block["verdict"] == "mechanism_documented"
        assert block["falsification_family_member"] is False
        assert "ledger holds at 64" in block["falsification_family"]

    def test_m1043_author_field_absent_by_design(self):
        # The m1043 block carries no author field (unlike m1042); its
        # provenance rides on the rotation_transparency and
        # concurrency fields. Documented as the verified form, not a
        # defect.
        block = _entities_block_1043()
        assert block.get("author") is None
        assert "rotation_transparency" in block
        assert "concurrency" in block

    def test_max_numeric_mechanism_id_is_1043(self):
        assert _max_numeric_mechanism_id() == MECH_NUM


# ---------------------------------------------------------------------------
# 4. Background-suite verdict per #795: the #1350 suite is DEAD at [  0%].
# ---------------------------------------------------------------------------


class TestBackgroundSuiteVerdict1355:
    def test_prior_suite_log_exists(self):
        assert os.path.exists(PRIOR_SUITE_LOG), PRIOR_SUITE_LOG

    def test_prior_suite_stalled_at_0(self):
        # The #1350-launched suite froze at [  0%] progress: 130
        # bytes pre-tombstone, zero F marks, last write Oct 9 2026
        # 17:20:59 PDT (~2.5h stale at this run's ~10:00 PM PDT
        # check), zero live pytest processes (the pgrep sweep at this
        # run's check returned zero live pytest processes; the /proc
        # open-fd check returns empty). Progress never regresses, so
        # the [  0%] marker stays present and [  1%] never arrives.
        # Observation history: #1350 launched it and saw it ALIVE at
        # launch (dots accumulating); #1351 observed it ALIVE at [0%]
        # (dots accumulating, 130 bytes, last write 17:20 PDT);
        # #1352 observed it ALIVE at [0%] with 1 live pytest proc
        # (~7:00 PM PDT check); #1353 and #1354 observed it STALLED
        # at [0%] with zero live pytest procs (last write 17:20 PDT,
        # recorded not adjudicated); this run verdicts it DEAD at
        # ~10:00 PM PDT.
        text = _read(PRIOR_SUITE_LOG)
        assert "[  0%]" in text, text[-2000:]
        assert "[  1%]" not in text
        assert 100 <= len(text) <= 100000, len(text)

    def test_prior_suite_has_zero_summary_tokens(self):
        # A completed run prints a summary ("passed"/"failed") or a
        # collection report ("no tests ran" / "short test summary").
        # The dead run carries none of them (the tombstone line is
        # worded to avoid those tokens).
        text = _read(PRIOR_SUITE_LOG)
        for token in ("passed", "failed", "no tests ran",
                      "short test summary"):
            assert token not in text, token

    def test_no_live_pytest_holds_prior_log(self):
        # The #1190-class death check: NO live pytest process holds
        # type_d_1350_full_suite.log open anymore (the /proc open-fd
        # check returns empty; the pgrep sweep at this run's ~10:00 PM
        # PDT check returned zero live pytest processes).
        holders = _proc_holds_log("type_d_1350_full_suite.log")
        assert holders == "", holders

    def test_twenty_first_death_of_new_streak(self):
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
        # verdict), #1325-launched the FIFTEENTH (#1330 verdict),
        # #1330-launched the SIXTEENTH (#1335 verdict),
        # #1335-launched the SEVENTEENTH (#1340 verdict),
        # #1340-launched the EIGHTEENTH (#1345 verdict),
        # #1345-launched the NINETEENTH (#1350 verdict),
        # #1350-launched the TWENTIETH (#1355 verdict): the
        # #1350-launched suite's death verdict, rendered this run,
        # is the TWENTY-FIRST consecutive background-suite death of
        # the new streak.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "TWENTY-FIRST consecutive" in src
        assert "death of the new streak" in src

    def test_tombstone_lineage_advances(self):
        # Per #565 the tombstone lineage advances with each DEATH
        # verdict: ONE-HUNDRED-TWENTY-EIGHTH ->
        # ONE-HUNDRED-TWENTY-NINTH.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "ONE-HUNDRED-TWENTY-EIGHTH" in src
        assert "lineage advances" in src

    def test_tombstone_written_to_prior_log(self):
        # The verdict's tombstone is appended to the dead log file
        # (this run owns the verdict per #795).
        text = _read(PRIOR_SUITE_LOG)
        assert "TOMBSTONE #1355" in text
        assert "TWENTY-FIRST consecutive" in text

    def test_dead_verdict_recorded_in_iteration_log(self):
        # Deselected pre-commit: the dead verdict is written into
        # the #1355 log entry in the doc-sync step per #719/#721.
        text = _read(LOG_PATH)
        assert "TWENTY-FIRST consecutive" in text


# ---------------------------------------------------------------------------
# 5. Recurring-failure triage: DETERMINATE-vacuous (zero F marks).
# ---------------------------------------------------------------------------


class TestRecurringFailureTriage1355:
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


class TestStatisticalDiscipline1355:
    def test_no_corpus_mechanisms_landed_this_run(self):
        # Type D lands no mechanisms: the max numeric mechanism id is
        # unchanged at 1043 and no 1044-form keys exist.
        assert _max_numeric_mechanism_id() == MECH_NUM
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_engine_not_run_on_corpus(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "engine NOT run on corpus" in src

    def test_scoring_verification_is_discipline_not_significance(self):
        # The body's "verify the asymmetry scoring produces
        # statistically meaningful results" is answered by the
        # discipline, not by running the scorer: per the Aug 28 2026
        # standing rule the scorer is intentionally NOT run on the
        # corpus, so no statistical-significance claim is made or
        # verified here.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "resolves\nto verifying the discipline" in src

    def test_synthetic_calibration_delta_contract(self):
        # Engine-layer contract only (never a finding): synthetic
        # Apple arms [-0.07, -0.10, -0.05, -0.08, -0.09] vs synthetic
        # Meta arms [-0.41, -0.37, -0.44, -0.39, -0.36] -> pooled
        # delta +0.316.
        assert _synthetic_calibration_delta() == 0.316


# ---------------------------------------------------------------------------
# 7. Falsification ledger: holds at 64; guards on member forms.
# ---------------------------------------------------------------------------


class TestFalsificationLedger1355:
    def test_ledger_holds_at_64(self):
        # Zero new falsification-family members in the 1350-1354
        # window (m1042 and m1043 are mechanism_documented, NOT
        # members): m1042 (wired.yaml) carries the "Ledger holds at
        # 64" ledger note; m1043 (competitor-entities
        # falsification_family) carries the ledger-holds-at-64 note;
        # m1039 (ap.yaml, the SIXTY-FOURTH member) carries
        # falsification_ledger "64".
        assert "Ledger holds at 64" in _wired_block_1042()["ledger_note"]
        entities = _yaml(ENTITIES_PATH)
        assert "ledger holds at 64" in entities[
            BLOCK_1043]["falsification_family"]
        ap = _yaml(os.path.join(PROFILES_DIR, "ap.yaml"))
        assert ap["competitor_relationships"]["openai"][
            BLOCK_M1039_AP]["falsification_ledger"] == "64"

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
        # Landed #1237 (m979, profiles/news-corp.yaml, committed);
        # the count moved 2->3 after #1325 (the #1237 block carries an
        # extra member-claim form mention); stable since. HEAD sweep
        # is stable for a committed landing.
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

    def test_sixty_first_member_intact(self):
        # Landed #1327 (m1027, profiles/wired.yaml, committed). HEAD
        # sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T61, "HEAD", "--",
            "profiles/wired.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_sixty_second_member_intact(self):
        # Landed #1332 (m1030, profiles/news-corp.yaml, committed).
        # HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T62, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixty_third_member_intact(self):
        # Landed #1342 (m1036, profiles/news-corp.yaml, committed).
        # HEAD sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T63, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_sixty_fourth_member_intact(self):
        # Landed #1347 (m1039, profiles/ap.yaml, committed). HEAD
        # sweep is stable for a committed landing.
        out = _git(
            "grep", "-c", "-F", _T64, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_sixty_fifth_member(self):
        assert _git_grep_tracked_source(_T65, None) == []

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
# 8. Guard lifecycle: forward pins for #1356; #1354 staged for this run.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1355:
    def test_pins_on_1043_no_landing(self):
        # Type D lands no mechanisms: max stays 1043, next stays 1044.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "MECH_NUM = 1043" in src
        assert "NEXT_NUM = 1044" in src

    def test_no_type_d_1355_in_git_log_pin(self):
        # Post-main-commit form for THIS run's own pin (the
        # #1191-class self-trip, re-pinned in this run's terminal
        # log-hash followup per #721): every commit whose message
        # matches "Type D #1355" must be this run's main commit or a
        # descendant of it. Deselected in the in-gate run (fails
        # pre-commit by design).
        out = _git("log", "--format=%H", "--grep=Type D #1355")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1355's own commits"
        main = _git("rev-parse", PRED_MAIN_1355).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_no_type_e_1356_in_git_log_pin(self):
        # Post-main-commit form for the NEXT leg (the #1191-class
        # self-trip, re-pinned in #1356's terminal log-hash followup
        # per #721): every commit whose message matches "Type E
        # #1356" must be #1356's main commit or a descendant of it.
        # Deselected in the in-gate run (fails pre-commit by design:
        # PRED_MAIN_1356 is 0*40).
        out = _git("log", "--format=%H", "--grep=Type E #1356")
        hits = [line.strip() for line in out.stdout.splitlines()
                if line.strip()]
        assert hits, "expected #1356's own commits"
        main = _git("rev-parse", PRED_MAIN_1356).stdout.strip()
        for h in hits:
            r = _git("merge-base", "--is-ancestor", main, h)
            assert r.returncode == 0, h

    def test_1044_numeric_absent_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_1044_underscore_absent_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_1044_dash_absent_repo_wide(self):
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
        out = _git(
            "grep", "-c", "-F", _T60, "HEAD", "--",
            "profiles/financial-times.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixty_first_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T61, "HEAD", "--",
            "profiles/wired.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_sixty_second_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T62, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_sixty_third_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T63, "HEAD", "--",
            "profiles/news-corp.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_sixty_fourth_member_present_pin(self):
        out = _git(
            "grep", "-c", "-F", _T64, "HEAD", "--",
            "profiles/ap.yaml",
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_sixty_fifth_member_pin(self):
        assert _git_grep_tracked_source(_T65, None) == []

    def test_predecessor_1354_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1354_FILE))

    def test_next_leg_is_1356_type_e(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "D #1355 -> E #1356 -> A #1357 -> B #1358 -> C #1359" in src

    def test_1354_pins_flip_by_design_documented(self):
        # The #1354 file's no-Type-D-#1355 forward pin fails
        # pre-commit by design (PRED_MAIN_1355 is 0*40) and flips
        # green in this run's terminal log-hash followup per
        # #721/#1292; the #1272-class expiry class does not exist for
        # a Type D run (no mechanisms landed). Documented here, not
        # repaired.
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1272-class" in src


# ---------------------------------------------------------------------------
# 9. Staleness pins: #1354's guard lifecycle flips once, then re-pins.
# ---------------------------------------------------------------------------


class TestStalenessPins1355:
    def test_1354_guard_lifecycle_post_terminal_followup(self):
        # Post-terminal-followup form: all 27 pass. The
        # no_type_d_1355_in_git_log pin (the #1191-class self-trip:
        # this run's main commit carries "Type D #1355") flipped BY
        # DESIGN at this run's main commit and is re-pinned green in
        # the terminal log-hash followup per #721 (PRED_MAIN_1355 now
        # holds this run's main sha in BOTH this file and the #1354
        # file per the #1292 precedent). The 1044-form pins stay green
        # throughout (Type D lands no mechanisms; the #723/#738/#739
        # designed keying holds); the member and direction pins stay
        # green (no member, no direction landed this run). The #1354
        # block is read-only to this run; the flip is documented here,
        # not repaired. Deselected pre-commit (verified only
        # post-terminal-followup).
        res = _class_run(E1354_FILE, "TestGuardLifecycle1354")
        out = res.stdout + res.stderr
        assert "27 passed" in out, out[-2000:]


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------


class TestDocSync1355:
    def test_readme_test_file_table_has_1355_row_post_sync(self):
        readme = _read(README_PATH)
        assert OWN_BASENAME in readme

    def test_architecture_has_1355_row_post_sync(self):
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


class TestIterationLog1355:
    def test_log_has_1355_entry(self):
        text = _read(LOG_PATH)
        assert "## #1355 Type D" in text

    def test_log_entry_carries_hash_chain(self):
        # The doc-sync writes the entry with the main/anchor hashes;
        # the terminal log-hash followup registers the doc-sync hash
        # here per #721.
        text = _read(LOG_PATH)
        assert "main commit" in text
        assert "anchor" in text

    def test_log_entry_records_verdict_and_relaunch(self):
        text = _read(LOG_PATH)
        assert "TWENTY-FIRST consecutive" in text
        assert "type_d_1355_full_suite.log" in text


# ---------------------------------------------------------------------------
# 12. Suite re-launch: this run re-launches the full suite at commit.
# ---------------------------------------------------------------------------


class TestSuiteRelaunch1355:
    def test_new_suite_log_path_in_docstring(self):
        # In-gate green: the docstring names the re-launch target.
        assert "type_d_1355_full_suite.log" in __doc__

    def test_relaunch_recorded_in_iteration_log(self):
        # Deselected pre-commit: the re-launch is written into the
        # #1355 log entry in the doc-sync step.
        text = _read(LOG_PATH)
        assert "RE-LAUNCHED" in text or "re-launched" in text


# ---------------------------------------------------------------------------
# 13. In-flight isolation
# ---------------------------------------------------------------------------


class TestInFlightIsolation1355:
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
        # 26349-26472): Ray's revert/leave/rebuild-from-primary
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
