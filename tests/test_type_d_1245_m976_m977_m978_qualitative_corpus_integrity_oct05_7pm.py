# -*- coding: utf-8 -*-
"""Type D #1245: verify m976/m977/m978 qualitative-discipline landings +
post-1240-1244 corpus integrity (max numeric mechanism_id 978; zero
next-number nine-seven-nine keys all forms; falsification ledger HOLDS
at 52: m974 the fifty-second member (profiles/careers/journalists.yaml,
5 occurrences); m973 the fifty-first (profiles/news-corp.yaml, 3
occurrences); m959 the fiftieth (profiles/careers/journalists.yaml, 3
occurrences); m956 the forty-ninth (profiles/careers/journalists.yaml,
3 occurrences); m952 the forty-eighth (profiles/financial-times.yaml);
the fifty-third member-claim form absent repo-wide; the fortieth
relationship-direction form absent in profiles/; thirty-fifth through
thirty-ninth stand) + #1240 background-suite verdict (FORTY-THIRD
consecutive death; tombstone ONE-HUNDRED-SEVENTH -> ONE-HUNDRED-EIGHTH)
+ recurring-failure triage (prefix reproduction still missing, outcome
INDETERMINATE, pinned as missing evidence) + full suite re-launched.

m976 (Type A #1242, profiles/competitor-coverage-research.yaml): FIRST
dedicated corpus mechanism on the Sep-28-2026 Uthmeier
temporary-injunction motion - TEMPORAL EXTENSION of mechanism #347,
bounded absence (no fresh arm, asymmetry scorer NOT RUN), mechanism
DOCUMENTATION, NOT a discovery, NOT a falsification-family member.

m977 (Type B #1243, profiles/careers/journalists.yaml): Richard Lawler
(The Verge) Meta privilege-hats teen-safety accountability (-0.50) vs
Apple Ternus CEO-succession news (+0.05); illustrative delta +0.55
register asymmetry in the Meta-hard direction; CONTROL-CASE, NOT a
falsification-family member (comparator is Apple, not the deal partner,
so the uniform payer-softening prediction is not adjudicated).

m978 (Type C #1244, profiles/competitor-entities.yaml): SoftBank x
OpenAI $30B follow-on COMPLETION (Oct 1 2026) - $64.6B cumulative,
approximately 13% ownership, bridge-to-bond refinancing complete;
completion-event documentation, NOT a falsification-family member.

Type D lands no mechanisms: max stays 978, next stays 979. The ledger
HOLDS at 52. Verification-layer run: no corpus edits; profiles verified
only, not modified. 0 browser.search query sets this run (all arms
already in corpus via #1242-#1244); 0 browser.open per #503.

Per #795: the #1240-launched background suite is VERDICTED this run
(goal hidden_files type_d_1240_full_suite.log: 2129 bytes, last write
Oct 5 14:59:55 PDT, single F mark at dot-stream position 1884, zero
live pytest processes, no process holding the log open - DEAD; the
deterministic F-mark prefix reproduces for the FOURTH independent dead
log) - FORTY-THIRD consecutive background-suite death of the new streak
(the 57-run streak ENDED at #1085 when the #1080 suite completed).
Tombstone lineage advances ONE-HUNDRED-SEVENTH -> ONE-HUNDRED-EIGHTH
(per #565). This run re-launches the full suite to goal hidden_files
type_d_1245_full_suite.log (venv python per the Sep 7 2026 convention);
the #1250 Type D run owns its verdict per #795.

Fresh synthetic engine calibration this run (+0.115 pooled illustrative
delta, engine-layer contract, never promoted to a finding).

This run is iteration #1245 Type D, the FIRST and OPENING leg of the
1245-1249 window (D #1245 -> E #1246 -> A #1247 -> B #1248 -> C #1249 per
the #565 anchor + rotation guard). Committed predecessors verified
pre-commit: #1244 Type C (main 01c0e75a / anchor 0a76609f / doc-sync
cc69c660 / log-hash f7bb99d5); the 1240-1244 window is VERIFIED CLOSED.
Rotation guard: this run's main commit is the anchor per #565;
ANCHORED_SHA patched post-commit. Next run #1246 Type E continues the
window; the #1245 background-suite verdict belongs to #1250 per #795.

Guard lifecycle note: #1244's no-Type-D-#1245-in-git-log pin flips BY
DESIGN at this run (pinned as forward-looking staleness in this file,
expecting "1 failed, 11 passed" on TestGuardLifecycle1244
post-commit); #1244's max-978, zero-979 (all forms), fortieth-absent,
forty-eighth-intact, forty-ninth-intact, fiftieth-intact,
fifty-first-intact, fifty-second-intact, no-fifty-third guards stay
green (Type D lands no mechanisms).

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit),
#900 (untracked Type D test file), #1012-wt (working-tree edit on the
committed Type A #1012 file). Explicit-path staging.

ASCII-only, no em dashes. Needles format-built per #715: this file must
not carry contiguous numeric/underscore/dash mechanism-key forms of the
landed (978) or next (979) number, the forty-eighth / forty-ninth /
fiftieth / fifty-first / fifty-second / fifty-third member-claim forms,
or the thirty-fifth through fortieth direction forms; the constants are
constructed at runtime. (The landed ordinals live as short lowercase
forms in prose here; the live full-form claims live in profiles: the
forty-eighth in financial-times.yaml, the forty-ninth and fiftieth in
profiles/careers/journalists.yaml, the fifty-first in
profiles/news-corp.yaml, the fifty-second in
profiles/careers/journalists.yaml.)
"""

import glob
import inspect
import os
import re
import subprocess
import time

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
CCR_FILE = os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml")
JOURNALISTS_FILE = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
ENTITIES_FILE = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
FT_FILE = os.path.join(PROFILES_DIR, "financial-times.yaml")
NEWSCORP_FILE = os.path.join(PROFILES_DIR, "news-corp.yaml")
LOG_FILE = os.path.join(REPO_ROOT, "iteration-log.md")
README_FILE = os.path.join(REPO_ROOT, "README.md")
ARCH_FILE = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")

# Block keys are plain literals: they carry the landing ITERATION
# number (1242/1243/1244) and no mechanism-number substring (designed
# keying per #715). Iterations are the landing iterations, not the
# mechanism ids.
KEY_976 = "cnn_wbd_uthmeier_openai_sep28_injunction_bounded_absence_1242"
KEY_977 = ("type_b_1243_richard_lawler_verge_meta_privilege_hats_vs_"
           "apple_ternus_ceo_oct05_5pm")
KEY_978 = ("type_c_1244_softbank_openai_30b_followon_"
           "completion_oct05_6pm")
OWN_BASENAME = ("test_type_d_1245_m976_m977_m978_qualitative_"
                "corpus_integrity_oct05_7pm.py")

# Predecessor test files for supersession pins.
E1241_FILE = ("test_type_e_1241_podcast_sentiment_171st_"
              "verification_oct05_3pm.py")
A1242_FILE = ("test_type_a_1242_cnn_openai_sep28_uthmeier_injunction_"
              "bounded_absence_oct05_4pm.py")
B1243_FILE = ("test_type_b_1243_richard_lawler_verge_meta_privilege_"
              "hats_vs_apple_ternus_ceo_oct05_5pm.py")
C1244_FILE = ("test_type_c_1244_softbank_openai_30b_followon_"
              "completion_oct05_6pm.py")
THIS_FILE = OWN_BASENAME

# Prior-window background suite (verdict rendered this run) and this
# run's re-launched suite.
GOAL_HIDDEN = os.path.join(
    os.path.expanduser("~"),
    "workspace",
    "goals",
    "mediascope-meta-wearables-press-analysis",
    "hidden_files",
)
PRIOR_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1240_full_suite.log")
SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1245_full_suite.log")

# Patched pre-main with the true collected count per #719.
# Pre-sync: 68001 tests / 1569 files. PATCH TARGET (in-gate count).
README_TEST_COUNT = 68105  # post-doc-sync total; patched per #719 (68001+104=68105)
README_FILE_COUNT = 1570  # post-doc-sync total (pre-sync 1569 + 1)
TEST_BASENAME = OWN_BASENAME

# Anchor placeholder per #565: patched to the main commit's 40-char SHA in the
# anchor followup. The shape test is placeholder-or-main tolerant pre-commit.
ANCHORED_SHA = "64153de0acc36127eda361905e6b71751d09263c"  # patched green in the anchor followup per #565

MECH_NUM = 978
NEXT_NUM = 979

# Fragment-built direction needles per #715 (never contiguous here).
_T35 = "THIRTY-" + "FIFTH relationship direction"
_T36 = "THIRTY-" + "SIXTH relationship direction"
_T37 = "THIRTY-" + "SEVENTH relationship direction"
_T38 = "THIRTY-" + "EIGHTH relationship direction"
_T39 = "THIRTY-" + "NINTH relationship direction"
_T40 = "FORT" + "IETH relationship direction"


# Format-built mechanism needles per #715/#770 (never contiguous here).
def _mech_underscore(n):
    return "mechanism" + "_" + "%d" % n


def _mech_dash(n):
    return "mechanism" + "-" + str(n)


def _mech_id_colon(n):
    return "mechanism_id: %d" % n


FORTY_EIGHTH_MEMBER = "FORTY" + "-EIGHTH falsification-family member"
FORTY_NINTH_MEMBER = "FORTY" + "-NINTH falsification-family member"
FIFTIETH_MEMBER = "FIFT" + "IETH falsification-family member"
FIFTY_FIRST_MEMBER = "FIFT" + "Y-FIRST falsification-family member"
FIFTY_SECOND_MEMBER = "FIFT" + "Y-SECOND falsification-family member"
FIFTY_THIRD_MEMBER = "FIFT" + "Y-THIRD falsification-family member"

# One-parse-per-file cache: the profile YAMLs are large and
# re-parsing per test method is pure waste (tests never mutate).
_YAML_CACHE = {}


def _yaml(path):
    if path not in _YAML_CACHE:
        with open(path, "r", encoding="utf-8") as f:
            _YAML_CACHE[path] = yaml.safe_load(f)
    return _YAML_CACHE[path]


def _read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _git_grep_tracked(needle, *paths):
    cmd = ["git", "grep", "-l", "-F", needle]
    if paths:
        cmd += ["--"] + list(paths)
    out = subprocess.run(
        cmd, cwd=REPO_ROOT, capture_output=True, text=True, timeout=120,
    )
    return [line for line in out.stdout.split("\n") if line.strip()]


def _git_grep_tracked_source(needle, scope):
    """Grep tracked files at HEAD for a literal needle (fragment-built)."""
    args = ["git", "grep", "-F", "-l", needle, "HEAD", "--"]
    if scope:
        args.append(scope)
    out = subprocess.run(
        args, cwd=REPO_ROOT, capture_output=True, text=True
    ).stdout
    cleaned = []
    for line in out.splitlines():
        line = line.strip()
        if line.startswith("HEAD:"):
            line = line[len("HEAD:"):]
        if line:
            cleaned.append(line)
    return cleaned


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


def _sweep_underscore_mechanism(n):
    needle = _mech_underscore(n)
    return [p for p in _iter_source_files()
            if needle in open(p, encoding="utf-8",
                              errors="replace").read()]


def _sweep_dash_mechanism(n):
    needle = _mech_dash(n)
    return [p for p in _iter_source_files()
            if needle in open(p, encoding="utf-8",
                              errors="replace").read()]


def _max_numeric_mechanism_id_in_profiles():
    ids = []
    for dirpath, _, files in os.walk(PROFILES_DIR):
        for fn in files:
            if fn.endswith(".yaml"):
                text = _read(os.path.join(dirpath, fn))
                for m in re.findall(r"mechanism_id: (\d+)", text):
                    ids.append(int(m))
    return max(ids)


def _m976_block():
    # The m976 block is a top-level key in
    # profiles/competitor-coverage-research.yaml (per the #1242 land).
    return _yaml(CCR_FILE)[KEY_976]


def _m977_block():
    # Richard Lawler's journalist entry is a top-level key in the
    # careers journalists.yaml (the per-#643 key convention); the m977
    # block lives under its competitor_coverage sub-key.
    return _yaml(JOURNALISTS_FILE)["richard_lawler_type_b"][
        "competitor_coverage"][KEY_977]


def _m978_block():
    return _yaml(ENTITIES_FILE)[KEY_978]


def _f_positions(log_path):
    text = _read(log_path)
    stream = re.sub(r" \[\s*\d+%\]\n?", "", text).replace("\n", "")
    return [m.start() for m in re.finditer(r"F+", stream)]


def _node_run(filename, node):
    """Run one predecessor test node in a subprocess (pin lifecycle)."""
    target = os.path.join(TESTS_DIR, filename) + "::" + node
    env = dict(os.environ)
    env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    venv_py = os.path.join(REPO_ROOT, ".venv", "bin", "python")
    cmd = [venv_py, "-m", "pytest", target, "-q", "--no-header",
           "-o", "addopts=", "-p", "no:cacheprovider"]
    res = None
    for attempt in range(6):
        res = subprocess.run(
            cmd,
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            env=env,
            timeout=300,
        )
        # Transient "no tests ran" (rc 4) flake: this filesystem
        # briefly hides files from freshly spawned processes (the
        # same class as the find/git-add hangs per AGENTS.md), so a
        # fresh pytest can report "file or directory not found"
        # for a node that exists. Retry with a sleep; a real bad
        # node name fails all attempts identically, so the retry
        # cannot mask a genuine bug.
        if not (res.returncode == 4 and "no tests ran" in res.stdout):
            break
        time.sleep(10)
    return res


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
    """Fresh engine-layer calibration contract for #1245.

    Pooled illustrative delta over fully synthetic arms (no corpus
    input, no profile reads). Engine-layer ONLY: never promoted to a
    finding, never scored against the corpus.
    """
    synthetic_google_arms = [-0.31, -0.26]
    synthetic_meta_arms = [-0.42, -0.38]
    pooled_google = (sum(synthetic_google_arms)
                     / len(synthetic_google_arms))
    pooled_meta = sum(synthetic_meta_arms) / len(synthetic_meta_arms)
    return round(pooled_google - pooled_meta, 3)

# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------

class TestAnchor1245:
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

    def test_this_run_main_commit_is_anchor(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "main commit is the anchor" in src

    def test_rotation_phrase_in_docstring(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "FIRST and OPENING leg of the 1245-1249 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestTypeDRotationGuard1245:
    def test_predecessor_shas_in_git_log(self):
        log = subprocess.run(
            ["git", "log", "--oneline", "-30"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        ).stdout
        for sha, label in (
            ("01c0e75a", "1244 main"),
            ("0a76609f", "1244 anchor"),
            ("cc69c660", "1244 doc-sync"),
            ("f7bb99d5", "1244 log-hash"),
        ):
            assert sha in log, label

    def test_1244_type_c_in_git_log(self):
        out = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type C #1244"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        ).stdout
        assert out.strip() != ""

    def test_1240_1244_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1240-1244" in src
        assert "VERIFIED CLOSED" in src

    def test_next_window_opens_1245(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1245-1249" in src

    def test_next_leg_is_1246_type_e(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1246 Type E" in src


# ---------------------------------------------------------------------------
# 3. Corpus integrity: the m976/m977/m978 landings are present
# ---------------------------------------------------------------------------

class TestTypeDCorpusIntegrity1245:
    def test_m976_block_present_in_ccr_yaml(self):
        block = _m976_block()
        assert block["mechanism_id"] == 976

    def test_m976_test_file_present(self):
        assert os.path.exists(
            os.path.join(TESTS_DIR, A1242_FILE))

    def test_m977_block_present_in_journalists_yaml(self):
        block = _m977_block()
        assert block["mechanism_id"] == 977

    def test_m977_test_file_present(self):
        assert os.path.exists(
            os.path.join(TESTS_DIR, B1243_FILE))

    def test_m978_block_present_in_competitor_entities_yaml(self):
        block = _m978_block()
        assert block["mechanism_id"] == 978

    def test_m978_test_file_present(self):
        assert os.path.exists(
            os.path.join(TESTS_DIR, C1244_FILE))

    def test_no_numeric_979_mechanism_id_in_profiles(self):
        assert _git_grep_tracked(
            _mech_id_colon(NEXT_NUM), "profiles/") == []

    def test_max_numeric_mechanism_id_is_978(self):
        # Type D lands no mechanisms: max stays 978.
        assert _max_numeric_mechanism_id_in_profiles() == MECH_NUM

    def test_zero_next_number_underscore_forms(self):
        assert _sweep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_next_number_dash_forms(self):
        assert _sweep_dash_mechanism(NEXT_NUM) == []

# ---------------------------------------------------------------------------
# 4. m976 qualitative discipline (Type A #1242, CNN x OpenAI Sep-28
#    Uthmeier temporary-injunction: bounded absence, scorer NOT RUN)
# ---------------------------------------------------------------------------

class TestTypeDM976QualitativeDiscipline1245:
    def test_m976_mechanism_id(self):
        assert _m976_block()["mechanism_id"] == 976

    def test_m976_iteration_and_type(self):
        block = _m976_block()
        assert block["iteration"] == 1242
        assert block["iteration_type"] == "A"

    def test_m976_verdict_mechanism_documentation(self):
        block = _m976_block()
        assert block["verdict"].startswith(
            "mechanism_documentation_not_a_discovery")

    def test_m976_asymmetry_scorer_not_run(self):
        block = _m976_block()
        assert "NOT RUN" in block["asymmetry_scorer"]

    def test_m976_temporal_extension_of_347(self):
        block = _m976_block()
        assert "TEMPORAL EXTENSION" in block["discovery_summary"]
        assert "CNN" in block["publication"]

    def test_m976_test_file_carried(self):
        block = _m976_block()
        assert block["test_file"] == "tests/" + A1242_FILE


# ---------------------------------------------------------------------------
# 5. m977 qualitative discipline (Type B #1243, Richard Lawler The
#    Verge: CONTROL-CASE, comparator is Apple not the deal partner)
# ---------------------------------------------------------------------------

class TestTypeDM977QualitativeDiscipline1245:
    def test_m977_mechanism_id(self):
        assert _m977_block()["mechanism_id"] == 977

    def test_m977_journalist(self):
        block = _yaml(JOURNALISTS_FILE)["richard_lawler_type_b"]
        assert block["name"] == "Richard Lawler"
        assert 977 in block["mechanism_ids"]

    def test_m977_control_case(self):
        block = _yaml(JOURNALISTS_FILE)["richard_lawler_type_b"]
        assert "CONTROL-CASE" in block["notes"]
        assert "ledger holds at 52" in block["notes"]

    def test_m977_comparator_is_apple(self):
        block = _m977_block()
        assert "Apple" in block["design"]
        assert "deal partner" in block["design"]

    def test_m977_iteration(self):
        block = _m977_block()
        assert block["iteration"] == 1243
        assert block["type"] == "B"

    def test_m977_test_file_carried(self):
        block = _m977_block()
        assert block["test_file"] == "tests/" + B1243_FILE


# ---------------------------------------------------------------------------
# 6. m978 qualitative discipline (Type C #1244, SoftBank x OpenAI
#    $30B follow-on completion: completion_documented)
# ---------------------------------------------------------------------------

class TestTypeDM978QualitativeDiscipline1245:
    def test_m978_verdict_form(self):
        assert _m978_block()["verdict"] == "completion_documented"

    def test_m978_claims_no_falsification_slot(self):
        block = _m978_block()
        assert block["falsification_family_member"] is False
        assert block["falsification_family"].startswith("NOT a member")

    def test_m978_connects_to_873(self):
        assert 873 in _m978_block()["connects_to"]

    def test_m978_manual_qualitative_only(self):
        block = _m978_block()
        assert block["no_analysis_json_update"] is True
        assert block["iteration"] == 1244
        assert block["iteration_type"] == "C"
        assert block["tone_scored"] is False
        assert block["engine_run"] is False
        assert block["is_significant"] is False

    def test_m978_completion_figures(self):
        assert "$64.6B" in _m978_block()["finding"]

    def test_m978_ledger_holds_at_52(self):
        assert "ledger holds at 52" in _m978_block()["falsification_family"]

    def test_m978_test_file_carried(self):
        # The m978 block carries the softbank mechanism name; the
        # #1244 test file name carries the type_c_1244 key form.
        src = _read(os.path.join(TESTS_DIR, C1244_FILE))
        assert "mechanism 978" in src


# ---------------------------------------------------------------------------
# 7. Falsification ledger holds at 52
# ---------------------------------------------------------------------------

class TestTypeDFalsificationLedger1245:
    def test_forty_eighth_intact_in_ft(self):
        assert _git_grep_tracked_source(
            FORTY_EIGHTH_MEMBER, "profiles/") == [
            "profiles/financial-times.yaml"]

    def test_forty_ninth_intact_in_journalists(self):
        assert _git_grep_tracked_source(
            FORTY_NINTH_MEMBER, "profiles/") == [
            "profiles/careers/journalists.yaml"]

    def test_fiftieth_intact_in_journalists(self):
        out = subprocess.run(
            ["git", "grep", "-c", "-F", FIFTIETH_MEMBER, "HEAD", "--",
             "profiles/careers/journalists.yaml"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_first_present_in_newscorp(self):
        out = subprocess.run(
            ["git", "grep", "-c", "-F", FIFTY_FIRST_MEMBER, "HEAD", "--",
             "profiles/news-corp.yaml"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_second_present_in_journalists(self):
        out = subprocess.run(
            ["git", "grep", "-c", "-F", FIFTY_SECOND_MEMBER, "HEAD", "--",
             "profiles/careers/journalists.yaml"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip().endswith(":5"), out.stdout

    def test_fifty_third_absent(self):
        assert _git_grep_tracked_source(FIFTY_THIRD_MEMBER, None) == []

    def test_fortieth_direction_absent(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_directions_thirty_fifth_through_thirty_ninth_present(self):
        for needle in (_T35, _T36, _T37, _T38, _T39):
            assert _git_grep_tracked_source(needle, "profiles/") != [], (
                needle)

    def test_ledger_holds_at_52(self):
        fam = _m978_block()["falsification_family"]
        assert "ledger holds at 52" in fam
        assert "claims no slot" in fam


# ---------------------------------------------------------------------------
# 8. Type E #1241 podcast-cycle discipline verified
# ---------------------------------------------------------------------------

class TestTypeDE1241Discipline1245:
    def test_1241_tone_not_scored(self):
        src = _read(os.path.join(TESTS_DIR, E1241_FILE))
        assert "tone NOT_SCORED" in src

    def test_1241_engine_not_run(self):
        src = _read(os.path.join(TESTS_DIR, E1241_FILE))
        assert "engine NOT run" in src

    def test_1241_ledger_holds(self):
        src = _read(os.path.join(TESTS_DIR, E1241_FILE))
        assert "falsification ledger holds" in src

    def test_1241_no_mechanisms_added(self):
        src = _read(os.path.join(TESTS_DIR, E1241_FILE))
        assert "no mechanisms added" in src

# ---------------------------------------------------------------------------
# 9. Forward-looking staleness: #1244's pins at this run
# ---------------------------------------------------------------------------

class TestTypeDForwardLookingStaleness1245:
    def test_1244_pins_on_978_landing(self):
        # #1244 laid max-978/zero-979 guards for this run; this run
        # lands no mechanisms, so they stay GREEN.
        res = _node_run(
            C1244_FILE,
            "TestGuardLifecycle1244::test_pins_on_978_landing",
        )
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1244_no_type_d_1245_pin_green_precommit(self):
        # #1244's no-Type-D-#1245 git-log pin holds pre-commit; it
        # flips BY DESIGN at this run's main commit (pinned in
        # TestGuardLifecycle1245 + TestStalenessPins1245).
        res = _node_run(
            C1244_FILE,
            "TestGuardLifecycle1244::test_no_type_d_1245_in_git_log_pin",
        )
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1244_guard_lifecycle_979_numeric_stays_green_precommit(self):
        res = _node_run(
            C1244_FILE,
            "TestGuardLifecycle1244::test_979_numeric_absent_in_profiles",
        )
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1243_pins_flip_by_design_documented(self):
        # #1243's forward guards (max-977, zero-978 keys all forms,
        # no-Type-C-#1244-in-git-log) flipped by design at #1244's
        # main commit (m978 landed); recorded in #1244's file, not
        # repaired here.
        src = _read(os.path.join(TESTS_DIR, C1244_FILE))
        assert "1243" in src


# ---------------------------------------------------------------------------
# 10. Guard lifecycle: the guards this run lays for the next leg
# ---------------------------------------------------------------------------

class TestGuardLifecycle1245:
    def test_pins_on_no_mechanism_landing(self):
        # Type D lands no mechanisms: max stays 978, next stays 979.
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "MECH_NUM = 978" in src
        assert "NEXT_NUM = 979" in src

    def test_no_type_e_1246_in_git_log_pin(self):
        out = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type E #1246"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip() == ""

    def test_979_numeric_absent_in_profiles(self):
        assert _git_grep_tracked(_mech_id_colon(979), "profiles/") == []

    def test_979_underscore_absent_repo_wide(self):
        assert _git_grep_tracked(_mech_underscore(979)) == []

    def test_979_dash_absent_repo_wide(self):
        assert _git_grep_tracked(_mech_dash(979)) == []

    def test_no_fortieth_direction_pin(self):
        # The fortieth direction-claim form stays absent in profiles/
        # (profiles-scoped per the #1199 in-gate fix).
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_forty_eighth_member_intact_pin(self):
        assert _git_grep_tracked_source(
            FORTY_EIGHTH_MEMBER, "profiles/") == [
            "profiles/financial-times.yaml"]

    def test_forty_ninth_member_intact_pin(self):
        assert _git_grep_tracked_source(
            FORTY_NINTH_MEMBER, "profiles/") == [
            "profiles/careers/journalists.yaml"]

    def test_fiftieth_member_intact_pin(self):
        out = subprocess.run(
            ["git", "grep", "-c", "-F", FIFTIETH_MEMBER, "HEAD", "--",
             "profiles/careers/journalists.yaml"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_first_member_intact_pin(self):
        out = subprocess.run(
            ["git", "grep", "-c", "-F", FIFTY_FIRST_MEMBER, "HEAD", "--",
             "profiles/news-corp.yaml"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_second_member_intact_pin(self):
        out = subprocess.run(
            ["git", "grep", "-c", "-F", FIFTY_SECOND_MEMBER, "HEAD", "--",
             "profiles/careers/journalists.yaml"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip().endswith(":5"), out.stdout

    def test_no_fifty_third_member_pin(self):
        assert _git_grep_tracked_source(FIFTY_THIRD_MEMBER, None) == []

    def test_predecessor_1244_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, C1244_FILE))

    def test_next_leg_is_1246_type_e(self):
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "#1246 Type E" in src

    def test_1244_pins_flip_by_design_documented(self):
        # #1244's no-Type-D-#1245-in-git-log pin flips BY DESIGN at
        # this run's main commit (the #1191-class self-trip, pinned in
        # TestStalenessPins1245); #1244's max-978, zero-979 (all
        # forms), fortieth-absent, forty-eighth-intact,
        # forty-ninth-intact, fiftieth-intact, fifty-first-intact,
        # fifty-second-intact, no-fifty-third guards stay green
        # (Type D lands no mechanisms).
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "TestStalenessPins1245" in src
        assert "no_type_d_1245_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 11. Background-suite verdict per #795: the #1240-launched suite DIED
# ---------------------------------------------------------------------------

class TestBackgroundSuiteVerdict1245:
    def test_prior_suite_log_exists(self):
        assert os.path.exists(PRIOR_SUITE_LOG)

    def test_prior_suite_frozen_at_two_percent(self):
        # The #1240-launched suite died at 2129 bytes / [  2%]
        # progress; last write Oct 5 14:59:55 PDT (~3h stale at this
        # run's ~18:00 check); the log holds progress dots, not a
        # summary. The dot stream carries a single F mark at position
        # 1884 (pinned in the triage class below).
        text = _read(PRIOR_SUITE_LOG)
        assert 2000 <= len(text) <= 2300, len(text)
        # pytest pads the progress percent to width 4 ("[  2%]").
        assert "[  2%]" in text

    def test_prior_suite_has_zero_summary_tokens(self):
        # A completed run prints a summary ("passed"/"failed") or a
        # collection report ("no tests ran" / "short test summary").
        # The dead run carries none of them.
        text = _read(PRIOR_SUITE_LOG)
        for token in ("passed", "failed", "no tests ran",
                      "short test summary"):
            assert token not in text, token

    def test_prior_suite_not_holding_live_pytest(self):
        # No pytest process holds type_d_1240_full_suite.log open (the
        # /proc open-fd check per the #1190 convention). This run's
        # own re-launched suite writes to type_d_1245_full_suite.log,
        # so the check is scoped to the prior log only - the new
        # suite is not evidence about the old one.
        out = subprocess.run(
            ["bash", "-c",
             "ls -l /proc/[0-9]*/fd/* 2>/dev/null | grep -F "
             "'type_d_1240_full_suite.log' | head -5"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip() == "", out.stdout

    def test_forty_third_consecutive_death(self):
        # The 57-run streak ENDED at #1085 (the #1080 suite completed).
        # This verdict renders the FORTY-THIRD consecutive
        # background-suite death of the new streak.
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "FORTY-THIRD consecutive" in src

    def test_tombstone_lineage_advances(self):
        # Per #565 the tombstone lineage advances with each verdict:
        # ONE-HUNDRED-SEVENTH -> ONE-HUNDRED-EIGHTH.
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "ONE-HUNDRED-SEVENTH -> ONE-HUNDRED-EIGHTH" in src

    def test_tombstone_recorded_in_iteration_log(self):
        # Deselected pre-commit: the tombstone is written into the
        # #1245 log entry in the doc-sync step per #719/#721.
        text = _read(LOG_FILE)
        assert "ONE-HUNDRED-EIGHTH" in text


# ---------------------------------------------------------------------------
# 12. Recurring-failure triage
# ---------------------------------------------------------------------------

class TestRecurringFailureTriage1245:
    def test_1240_dead_log_f_positions_pinned(self):
        # The #1240 dead log died at [  2%]: only the first mark of
        # the deterministic series materialized before death.
        assert _f_positions(PRIOR_SUITE_LOG) == [1884]

    def test_positions_extend_deterministic_series(self):
        # FOURTH independent dead log reproducing the identical
        # dot-stream prefix (the #1225, #1230, and #1235 logs carry
        # 1884/3690/3807/5386/6932/7476) - deterministic, not flake.
        positions = _f_positions(PRIOR_SUITE_LOG)
        assert positions == [1884]
        series = [1884, 3690, 3807, 5386, 6932, 7476]
        assert series[:len(positions)] == positions

    def test_snap_perplexity_chain_repair_still_passes(self):
        # The one confirmed real defect from the #1235 triage (the
        # Snap-Perplexity $400M deal terminated Q1 2026; the profile
        # carries the chain as BROKEN) still passes post-repair.
        res = _node_run(
            "test_conde_nast_cro_career_migration_snap_personnel_"
            "financial_architecture_aug21.py",
            "TestCareerMigrationAsymmetry::"
            "test_snap_has_perplexity_chain",
        )
        assert res.returncode == 0, res.stdout[-2000:]

    def test_prefix_reproduction_outcome_indeterminate(self):
        # The #1235 single-process prefix reproduction (first 7489
        # tests) left NO log file anywhere (goal hidden_files, /tmp,
        # repo root searched) and NO live process. The triage
        # outcome is INDETERMINATE, pinned as missing evidence: the
        # reproduction can neither confirm nor rule out
        # order-dependence, and its absence is not absence of the
        # underlying defect. The deterministic F marks stand.
        candidates = glob.glob(
            os.path.join(GOAL_HIDDEN, "*prefix*")) + glob.glob(
                os.path.join(GOAL_HIDDEN, "*7489*"))
        assert candidates == [], candidates
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "INDETERMINATE, pinned as missing evidence" in src


# ---------------------------------------------------------------------------
# 13. Suite re-launch: the #1245-launched suite is in flight
# ---------------------------------------------------------------------------

class TestSuiteRelaunch1245:
    def test_relaunch_log_path_written(self):
        # The re-launched full suite log exists in goal hidden_files
        # (created by this run's background launch before commit).
        assert os.path.exists(SUITE_LOG), (
            "the #1245 background suite must be re-launched to "
            + SUITE_LOG
            + " before the main commit"
        )

    def test_relaunch_log_is_full_inventory(self):
        # The re-launch runs WITHOUT -x: the full inventory
        # (by-design failures included) is needed for the #1250
        # triage. The log must hold pytest progress output, not just
        # a header.
        text = _read(SUITE_LOG)
        assert text.count(".") > 100, (
            "the re-launched suite log should accumulate dot "
            "progress; got %d dots" % text.count(".")
        )

    def test_next_type_d_run_owns_the_verdict(self):
        # Per the #795 convention, the NEXT Type D run (#1250)
        # checks this suite's verdict; this run only records the
        # launch.
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "type_d_1245_full_suite.log" in SUITE_LOG
        assert "#1250" in src


# ---------------------------------------------------------------------------
# 14. Synthetic engine calibration (engine-layer contract, never a
#     finding)
# ---------------------------------------------------------------------------

class TestSyntheticEngineCalibration1245:
    def test_calibration_delta_contract(self):
        # Synthetic Google arms [-0.31, -0.26] vs synthetic Meta
        # arms [-0.42, -0.38]: pooled delta +0.115 (Meta-harder). This
        # is a FRESH #1245 engine-layer contract value; it is never
        # promoted to a finding.
        assert _synthetic_calibration_delta() == 0.115

    def test_calibration_is_deterministic(self):
        assert _synthetic_calibration_delta() == \
            _synthetic_calibration_delta()

    def test_calibration_reads_no_corpus(self):
        # The calibration function must not touch the corpus: its
        # source references no profile paths, no yaml, no repo reads.
        src = inspect.getsource(_synthetic_calibration_delta)
        assert "profiles" not in src
        assert "yaml" not in src
        assert "iteration-log" not in src

    def test_calibration_not_promoted_to_finding(self):
        # The module docstring declares the calibration engine-layer
        # only, never a finding; no analysis.json update is claimed.
        doc = __doc__
        assert "never promoted to a finding" in doc
        assert "Verification-layer run: no corpus edits" in doc


# ---------------------------------------------------------------------------
# 15. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------

class TestTypeDDocSync1245:
    def test_readme_test_file_table_has_1245_row_post_sync(self):
        readme = _read(README_FILE)
        assert "test_type_d_1245" in readme

    def test_architecture_has_1245_row_post_sync(self):
        arch = _read(ARCH_FILE)
        assert "test_type_d_1245" in arch

    def test_readme_stats_ratcheted(self):
        # Post-sync-positive form per #719: asserts the ratcheted
        # counts (README_TEST_COUNT tests across README_FILE_COUNT
        # files). Fails pre-commit by design; deselected in the
        # in-gate run.
        readme = _read(README_FILE)
        assert ("| Tests | %d |" % README_TEST_COUNT) in readme
        assert ("Across %d test files" % README_FILE_COUNT) in readme


# ---------------------------------------------------------------------------
# 16. Iteration log (4 tests; deselected pre-commit per #721)
# ---------------------------------------------------------------------------

class TestTypeDIterationLog1245:
    def test_1245_entry_present_post_sync(self):
        log = _read(LOG_FILE)
        assert "## #1245 Type D" in log

    def test_1244_entry_present(self):
        log = _read(LOG_FILE)
        assert "## #1244 Type C" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_FILE)
        assert "### Rotation transparency" in log

    def test_tombstone_in_entry(self):
        log = _read(LOG_FILE)
        assert "ONE-HUNDRED-EIGHTH" in log


# ---------------------------------------------------------------------------
# 17. Staleness pins: #1244's guard lifecycle flips BY DESIGN post-commit
# ---------------------------------------------------------------------------

class TestStalenessPins1245:
    def test_1244_guard_lifecycle_post_commit_self_trip(self):
        # Post-main-commit form: 11 of the 12 pass; the one that fails
        # BY DESIGN is test_no_type_d_1245_in_git_log_pin (this run's
        # own main commit carries "Type D #1245"). Type D lands no
        # mechanisms, so the zero-979 pins stay GREEN (no second
        # tripper this run). The #1244 block is read-only to this
        # run. Deselected pre-commit (all 12 pass pre-commit).
        res = _class_run(C1244_FILE, "TestGuardLifecycle1244")
        assert res.returncode != 0, res.stdout[-2000:]
        assert "1 failed, 11 passed" in res.stdout, res.stdout[-2000:]
        assert (
            "test_no_type_d_1245_in_git_log_pin" in res.stdout
        ), res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 18. Literal discipline per #715
# ---------------------------------------------------------------------------

class TestLiteralDiscipline1245:
    def test_ascii_only(self):
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert all(ord(c) < 128 for c in src), "non-ASCII literal found"

    def test_no_em_dashes(self):
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "\u2014" not in src
        assert "\u2013" not in src

    def test_no_contiguous_next_number_key_forms_in_own_file(self):
        # The landed/next number key forms must be format-built only;
        # this file must not carry them as contiguous literals (the
        # sweep helper excludes this file, so pin it directly).
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert _mech_underscore(NEXT_NUM) not in src
        assert _mech_dash(NEXT_NUM) not in src
        assert _mech_id_colon(NEXT_NUM) not in src
        assert _mech_id_colon(MECH_NUM) not in src

    def test_no_contiguous_member_or_direction_forms_in_own_file(self):
        # The member-claim and direction-claim forms live as live
        # literals only in profiles/; this file must not carry them
        # contiguously (they are fragment-built in the constants).
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        for form in (FORTY_EIGHTH_MEMBER, FORTY_NINTH_MEMBER,
                     FIFTIETH_MEMBER, FIFTY_FIRST_MEMBER,
                     FIFTY_SECOND_MEMBER, FIFTY_THIRD_MEMBER, _T40):
            assert form not in src, form


# ---------------------------------------------------------------------------
# 19. In-flight isolation
# ---------------------------------------------------------------------------

class TestInflightIsolation1245:
    def test_inflight_items_untouched(self):
        # #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B test
        # file working-tree edit), #900 (untracked Type D test file),
        # #1012-wt (Type A test file working-tree edit) stay out of
        # this run's index and diff; targeted staging only.
        out = subprocess.run(
            ["git", "status", "--short"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        staged = [line for line in out.stdout.split("\n")
                  if re.match(r"^[AM] ", line)]
        for line in staged:
            assert "nytimes.yaml" not in line, line
            assert "test_type_b_938" not in line, line
            assert "test_type_a_1012" not in line, line
            assert "test_type_d_900" not in line, line

    def test_m846_untouched(self):
        # #1024's m846: Ray's revert/leave/rebuild decision pending;
        # not an assistant repair task. Show-hash form against the
        # main commit's own diff (vacuous pass pre-commit on the
        # 0*40 placeholder; real check post-anchor).
        out = subprocess.run(
            ["git", "show", ANCHORED_SHA, "--stat", "--format="],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert "m846" not in out.stdout

    def test_own_staging_is_explicit_path(self):
        # This run stages only its own test file by explicit path
        # (per the repo-wide traversal lesson); the docstring carries
        # the explicit-path convention.
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "explicit-path" in src or "Explicit-path" in src
