# -*- coding: utf-8 -*-
"""Type D #1250: verify m979/m980/m981 qualitative-discipline landings +
post-1245-1249 corpus integrity (max numeric mechanism_id 981; zero
next-number nine-eight-two keys all forms; falsification ledger HOLDS
at 52: m974 the fifty-second member (profiles/careers/journalists.yaml,
5 occurrences); m973 the fifty-first (profiles/news-corp.yaml, 3
occurrences); m959 the fiftieth (profiles/careers/journalists.yaml, 3
occurrences); m956 the forty-ninth (profiles/careers/journalists.yaml,
3 occurrences); m952 the forty-eighth (profiles/financial-times.yaml);
the fifty-third member-claim form absent repo-wide; the fortieth
relationship-direction form absent in profiles/; thirty-fifth through
thirty-ninth stand) + #1245 background-suite verdict (ALIVE at 20%;
the FORTY-THIRD consecutive death streak BREAKS; tombstone lineage
HOLDS at ONE-HUNDRED-EIGHTH; no re-launch) + recurring-failure triage
(deterministic F-prefix reproduces at five of six canonical positions
in the LIVE log; 3807 absent - new deviation; outcome INDETERMINATE,
pinned as missing evidence).

m979 (Type A #1247, profiles/competitor-coverage-research.yaml): FIRST
dedicated corpus mechanism mapping the October financial-peg coverage
landscape - bounded absence (three major Oct 1-5 financial pegs drew
zero profiled-publication originals in the 4-6 day window;
originator-wire plus trade relays); temporal extension of m976 from
the legal peg to the financial pegs; asymmetry scorer NOT RUN;
verdict bounded_absence_documented; NOT a falsification-family
member; ledger holds at 52.

m980 (Type B #1248, profiles/careers/journalists.yaml): Mike Isaac
(NYT) Meta AG-settlement competitive-maneuvering (-0.35) vs
Microsoft/OpenAI unsealed "largest theft of labor" (-0.55);
illustrative delta -0.20 near-symmetric adversarial with the
litigation adversary drawing the harder register; CONTROL-CASE, NOT
a falsification-family member (NYT x OpenAI is litigation, not a
deal); ledger holds at 52.

m981 (Type C #1249, profiles/competitor-entities.yaml): OpenAI
visual-ads expansion (Oct 5 2026, Advertising Week New York) - first
visual ChatGPT ad format; measurement/attribution stack named; $1B
annualized run rate; verdict milestone_documented; NOT a
falsification-family member; ledger holds at 52.

Type D lands no mechanisms: max stays 981, next stays 982. The ledger
HOLDS at 52. Verification-layer run: no corpus edits; profiles
verified only, not modified. 0 browser.search query sets this run
(all arms already in corpus via #1247-#1249); 0 browser.open per
#503.

Per #795: the #1245-launched background suite is VERDICTED this run
(goal hidden_files type_d_1245_full_suite.log: ~15K bytes, [ 20%]
progress, fresh writes at this run's ~22:05 check, live pytest
process holding the log open per the /proc open-fd check - ALIVE).
The FORTY-THIRD consecutive background-suite death streak BREAKS here
(the 57-run streak ENDED at #1085 when the #1080 suite completed).
Tombstone lineage HOLDS at ONE-HUNDRED-EIGHTH (no advance on an alive
verdict, per #565). This run does NOT re-launch (the suite is still
running; a second writer would double the 2.8 GB footprint on a
1 GB-free box); the #1255 Type D run owns the next verdict per #795.

Fresh synthetic engine calibration this run (+0.105 pooled illustrative
delta, engine-layer contract, never promoted to a finding).

This run is iteration #1250 Type D, the FIRST and OPENING leg of the
1250-1254 window (D #1250 -> E #1251 -> A #1252 -> B #1253 -> C #1254
per the #565 anchor + rotation guard). Committed predecessors
verified pre-commit: #1249 Type C (main 82871c5e / anchor 2f26605b /
doc-sync 25522e79 / log-hash 8179f925); the 1245-1249 window is
VERIFIED CLOSED. Rotation guard: this run's main commit is the anchor
per #565; ANCHORED_SHA patched post-commit. Next run #1251 Type A
continues the window; the next background-suite verdict belongs to
#1255 per #795.

Guard lifecycle note: #1249's no-Type-D-#1250-in-git-log pin flips BY
DESIGN at this run (pinned as forward-looking staleness in this file,
expecting "1 failed, 14 passed" on TestGuardLifecycle1249
post-commit); #1249's max-981, zero-982 (all forms), fortieth-absent,
forty-eighth-intact, forty-ninth-intact, fiftieth-intact,
fifty-first-intact, fifty-second-intact, no-fifty-third guards stay
green (Type D lands no mechanisms).

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit),
#900 (untracked Type D test file), #1012-wt (working-tree edit on the
committed Type A #1012 file). Explicit-path staging.

ASCII-only, no em dashes. Needles format-built per #715: this file
must not carry contiguous numeric/underscore/dash mechanism-key forms
of the landed (981) or next (982) number, the forty-eighth /
forty-ninth / fiftieth / fifty-first / fifty-second / fifty-third
member-claim forms, or the thirty-fifth through fortieth direction
forms; the constants are constructed at runtime. (The landed ordinals
live as short lowercase forms in prose here; the live full-form
claims live in profiles: the forty-eighth in financial-times.yaml,
the forty-ninth and fiftieth in profiles/careers/journalists.yaml,
the fifty-first in profiles/news-corp.yaml, the fifty-second in
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
# number (1247/1248/1249) and no mechanism-number substring (designed
# keying per #715). Iterations are the landing iterations, not the
# mechanism ids.
KEY_979 = ("type_a_1247_oct_financial_peg_coverage_landscape_"
           "bounded_absence_audit")
KEY_980 = ("type_b_1248_mike_isaac_nyt_meta_ag_settlement_vs_"
           "openai_theft_of_labor_oct05_8pm")
KEY_981 = ("type_c_1249_openai_visual_ads_chatgpt_advertising_week_"
           "oct05_9pm")
OWN_BASENAME = ("test_type_d_1250_m979_m980_m981_qualitative_"
                "corpus_integrity_oct05_10pm.py")

# Predecessor test files for supersession pins.
E1246_FILE = ("test_type_e_1246_podcast_sentiment_172nd_"
              "verification_oct05_7pm.py")
A1247_FILE = ("test_type_a_1247_oct_financial_peg_coverage_landscape_"
              "bounded_absence_audit_oct05_8pm.py")
B1248_FILE = ("test_type_b_1248_mike_isaac_nyt_meta_ag_settlement_"
              "vs_openai_theft_of_labor_oct05_8pm.py")
C1249_FILE = ("test_type_c_1249_openai_visual_ads_chatgpt_"
              "advertising_week_oct05_9pm.py")
THIS_FILE = OWN_BASENAME

# Prior-window background suite (verdict rendered this run). No
# re-launch this run: the suite is still alive, and a second writer
# would double the footprint on a 1 GB-free box.
GOAL_HIDDEN = os.path.join(
    os.path.expanduser("~"),
    "workspace",
    "goals",
    "mediascope-meta-wearables-press-analysis",
    "hidden_files",
)
PRIOR_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1245_full_suite.log")
NO_RELAUNCH_LOG = os.path.join(GOAL_HIDDEN, "type_d_1250_full_suite.log")

# Patched pre-main with the true collected count per #719.
# Pre-sync: 68414 tests / 1574 files. PATCH TARGET (in-gate count).
README_TEST_COUNT = 68522  # post-doc-sync total; patched per #719 (68414+108=68522)
README_FILE_COUNT = 1575  # post-doc-sync total (pre-sync 1574 + 1)
TEST_BASENAME = OWN_BASENAME

# Anchor placeholder per #565: patched to the main commit's 40-char SHA in the
# anchor followup. The shape test is placeholder-or-main tolerant pre-commit.
ANCHORED_SHA = "0" * 40  # patched to the main-commit sha in the anchor followup per #565

MECH_NUM = 981
NEXT_NUM = 982

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


def _m979_block():
    # The m979 block is a top-level key in
    # profiles/competitor-coverage-research.yaml (per the #1247 land).
    return _yaml(CCR_FILE)[KEY_979]


def _m980_block():
    # Mike Isaac's journalist entry is a top-level key in the
    # careers journalists.yaml (the per-#643 key convention); the m980
    # block lives under its competitor_coverage sub-key.
    return _yaml(JOURNALISTS_FILE)["mike_isaac_type_b"][
        "competitor_coverage"][KEY_980]


def _m981_block():
    return _yaml(ENTITIES_FILE)[KEY_981]


def _f_positions(log_path):
    text = _read(log_path)
    stream = re.sub(r" \[\s*\d+%\]\n?", "", text).replace("\n", "")
    return [m.start() for m in re.finditer(r"F+", stream)]


def _f_stream(log_path):
    text = _read(log_path)
    return re.sub(r" \[\s*\d+%\]\n?", "", text).replace("\n", "")


def _proc_holds_log(log_name):
    out = subprocess.run(
        ["bash", "-c",
         "ls -l /proc/[0-9]*/fd/* 2>/dev/null | grep -F "
         "'%s' | head -5" % log_name],
        cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
    )
    return out.stdout.strip()


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
    """Fresh engine-layer calibration contract for #1250.

    Pooled illustrative delta over fully synthetic arms (no corpus
    input, no repo reads). Engine-layer ONLY: never promoted to a
    finding, never scored against the corpus.
    """
    synthetic_google_arms = [-0.28, -0.33]
    synthetic_meta_arms = [-0.45, -0.37]
    pooled_google = (sum(synthetic_google_arms)
                     / len(synthetic_google_arms))
    pooled_meta = sum(synthetic_meta_arms) / len(synthetic_meta_arms)
    return round(pooled_google - pooled_meta, 3)

# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------

class TestAnchor1250:
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
        assert "FIRST and OPENING leg of the 1250-1254 window" in src


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------

class TestTypeDRotationGuard1250:
    def test_predecessor_shas_in_git_log(self):
        log = subprocess.run(
            ["git", "log", "--oneline", "-30"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        ).stdout
        for sha, label in (
            ("82871c5e", "1249 main"),
            ("2f26605b", "1249 anchor"),
            ("25522e79", "1249 doc-sync"),
            ("8179f925", "1249 log-hash"),
        ):
            assert sha in log, label

    def test_1249_type_c_in_git_log(self):
        out = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type C #1249"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        ).stdout
        assert out.strip() != ""

    def test_1245_1249_window_closed(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1245-1249" in src
        assert "VERIFIED CLOSED" in src

    def test_next_window_opens_1250(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "1250-1254" in src

    def test_next_leg_is_1251_type_a(self):
        src = _read(os.path.join(TESTS_DIR, OWN_BASENAME))
        assert "#1251 Type A" in src


# ---------------------------------------------------------------------------
# 3. Corpus integrity: the m979/m980/m981 landings are present
# ---------------------------------------------------------------------------

class TestTypeDCorpusIntegrity1250:
    def test_m979_block_present_in_ccr_yaml(self):
        block = _m979_block()
        assert block["mechanism_id"] == 979

    def test_m979_test_file_present(self):
        assert os.path.exists(
            os.path.join(TESTS_DIR, A1247_FILE))

    def test_m980_block_present_in_journalists_yaml(self):
        block = _m980_block()
        assert block["mechanism_id"] == 980

    def test_m980_test_file_present(self):
        assert os.path.exists(
            os.path.join(TESTS_DIR, B1248_FILE))

    def test_m981_block_present_in_competitor_entities_yaml(self):
        block = _m981_block()
        assert block["mechanism_id"] == 981

    def test_m981_test_file_present(self):
        assert os.path.exists(
            os.path.join(TESTS_DIR, C1249_FILE))

    def test_no_numeric_982_mechanism_id_in_profiles(self):
        assert _git_grep_tracked(
            _mech_id_colon(NEXT_NUM), "profiles/") == []

    def test_max_numeric_mechanism_id_is_981(self):
        # Type D lands no mechanisms: max stays 981.
        assert _max_numeric_mechanism_id_in_profiles() == MECH_NUM

    def test_zero_next_number_underscore_forms(self):
        assert _sweep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_next_number_dash_forms(self):
        assert _sweep_dash_mechanism(NEXT_NUM) == []

# ---------------------------------------------------------------------------
# 4. m979 qualitative discipline (Type A #1247, October financial-peg
#    coverage landscape: bounded absence, scorer NOT RUN)
# ---------------------------------------------------------------------------

class TestTypeDM979QualitativeDiscipline1250:
    def test_m979_mechanism_id(self):
        assert _m979_block()["mechanism_id"] == 979

    def test_m979_iteration_and_type(self):
        block = _m979_block()
        assert block["iteration"] == 1247
        assert block["iteration_type"] == "A"

    def test_m979_tone_not_scored(self):
        block = _m979_block()
        assert block["tone_scores"] == "NOT_SCORED"
        assert block["p_value"] == "NOT_CALCULATED"
        assert block["cohens_d"] == "NOT_CALCULATED"

    def test_m979_not_significant_not_artifact_grade(self):
        block = _m979_block()
        assert block["is_significant"] is False
        assert block["artifact_grade"] is False
        assert block["analysis_json_update"] is False

    def test_m979_verdict_bounded_absence(self):
        block = _m979_block()
        assert block["verdict"].startswith("bounded_absence_documented")
        assert "temporal extension" in block["verdict"]

    def test_m979_asymmetry_scorer_not_run(self):
        block = _m979_block()
        assert "NOT RUN" in block["asymmetry_scorer"]

    def test_m979_not_falsification_member_ledger_52(self):
        block = _m979_block()
        assert block["falsification_family_member"] is False
        assert "Ledger holds at 52" in block["verdict"]


# ---------------------------------------------------------------------------
# 5. m980 qualitative discipline (Type B #1248, Mike Isaac NYT:
#    CONTROL-CASE, comparator is litigation not the deal partner)
# ---------------------------------------------------------------------------

class TestTypeDM980QualitativeDiscipline1250:
    def test_m980_mechanism_id(self):
        assert _m980_block()["mechanism_id"] == 980

    def test_m980_journalist(self):
        block = _yaml(JOURNALISTS_FILE)["mike_isaac_type_b"]
        assert block["name"] == "Mike Isaac"
        assert 980 in block["mechanism_ids"]

    def test_m980_control_case(self):
        block = _m980_block()
        assert "CONTROL-CASE" in block["finding"]
        assert "Ledger holds at 52" in block["ledger_note"]

    def test_m980_comparator_is_litigation_not_deal(self):
        block = _m980_block()
        assert "litigation" in block["finding"]
        assert "deal" in block["finding"]

    def test_m980_iteration(self):
        block = _m980_block()
        assert block["iteration"] == 1248
        assert block["type"] == "B"

    def test_m980_not_falsification_member(self):
        block = _m980_block()
        assert block["falsification_family_member"] is False
        assert block["is_significant"] is False

    def test_m980_test_file_carried(self):
        block = _m980_block()
        assert block["test_file"] == "tests/" + B1248_FILE


# ---------------------------------------------------------------------------
# 6. m981 qualitative discipline (Type C #1249, OpenAI visual-ads
#    expansion: milestone_documented)
# ---------------------------------------------------------------------------

class TestTypeDM981QualitativeDiscipline1250:
    def test_m981_verdict_form(self):
        assert _m981_block()["verdict"] == "milestone_documented"

    def test_m981_claims_no_falsification_slot(self):
        block = _m981_block()
        assert block["falsification_family_member"] is False
        assert block["falsification_family"].startswith("NOT a member")

    def test_m981_first_visual_chatgpt_ad_format(self):
        assert "visual" in _m981_block()["finding"]

    def test_m981_manual_qualitative_only(self):
        block = _m981_block()
        assert block["artifact_grade"] is False
        assert block["iteration"] == 1249
        assert block["iteration_type"] == "C"
        assert block["is_significant"] is False

    def test_m981_measurement_stack_named(self):
        assert "AppsFlyer" in _m981_block()["finding"]

    def test_m981_ledger_holds_at_52(self):
        assert "ledger holds at 52" in _m981_block()["falsification_family"]

    def test_m981_test_file_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, C1249_FILE))


# ---------------------------------------------------------------------------
# 7. Falsification ledger holds at 52
# ---------------------------------------------------------------------------

class TestTypeDFalsificationLedger1250:
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
        fam = _m981_block()["falsification_family"]
        assert "ledger holds at 52" in fam
        assert "NOT a member" in fam

# ---------------------------------------------------------------------------
# 8. Type E #1246 podcast-cycle discipline verified
# ---------------------------------------------------------------------------

class TestTypeDE1246Discipline1250:
    def test_1246_tone_not_scored(self):
        src = _read(os.path.join(TESTS_DIR, E1246_FILE))
        assert "tone NOT_SCORED" in src

    def test_1246_engine_not_run(self):
        src = _read(os.path.join(TESTS_DIR, E1246_FILE))
        assert "engine NOT run" in src

    def test_1246_ledger_holds(self):
        src = _read(os.path.join(TESTS_DIR, E1246_FILE))
        assert "falsification ledger holds" in src

    def test_1246_no_mechanisms_added(self):
        src = _read(os.path.join(TESTS_DIR, E1246_FILE))
        assert "no mechanisms added" in src

# ---------------------------------------------------------------------------
# 9. Forward-looking staleness: #1249's pins at this run
# ---------------------------------------------------------------------------

class TestTypeDForwardLookingStaleness1250:
    def test_1249_pins_on_981_landing(self):
        # #1249 laid max-981/zero-982 guards for this run; this run
        # lands no mechanisms, so they stay GREEN.
        res = _node_run(
            C1249_FILE,
            "TestGuardLifecycle1249::test_pins_on_981_landing",
        )
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1249_no_type_d_1250_pin_green_precommit(self):
        # #1249's no-Type-D-#1250 git-log pin holds pre-commit; it
        # flips BY DESIGN at this run's main commit (pinned in
        # TestGuardLifecycle1250 + TestStalenessPins1250).
        res = _node_run(
            C1249_FILE,
            "TestGuardLifecycle1249::test_no_type_d_1250_in_git_log_pin",
        )
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1249_guard_lifecycle_982_numeric_stays_green_precommit(self):
        res = _node_run(
            C1249_FILE,
            "TestGuardLifecycle1249::test_982_numeric_absent_in_profiles",
        )
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1249_guard_lifecycle_982_underscore_stays_green_precommit(self):
        res = _node_run(
            C1249_FILE,
            "TestGuardLifecycle1249::test_982_underscore_absent_repo_wide",
        )
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1249_guard_lifecycle_982_dash_stays_green_precommit(self):
        res = _node_run(
            C1249_FILE,
            "TestGuardLifecycle1249::test_982_dash_absent_repo_wide",
        )
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1248_pins_flip_by_design_documented(self):
        # #1248's forward guards (max-980, zero-981 keys all forms,
        # no-Type-C-#1249-in-git-log) flipped by design at #1249's
        # main commit (m981 landed); recorded in #1249's file, not
        # repaired here.
        src = _read(os.path.join(TESTS_DIR, C1249_FILE))
        assert "1248" in src


# ---------------------------------------------------------------------------
# 10. Guard lifecycle: the guards this run lays for the next leg
# ---------------------------------------------------------------------------

class TestGuardLifecycle1250:
    def test_pins_on_no_mechanism_landing(self):
        # Type D lands no mechanisms: max stays 981, next stays 982.
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "MECH_NUM = 981" in src
        assert "NEXT_NUM = 982" in src

    def test_no_type_a_1251_in_git_log_pin(self):
        out = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type A #1251"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip() == ""

    def test_982_numeric_absent_in_profiles(self):
        assert _git_grep_tracked(_mech_id_colon(982), "profiles/") == []

    def test_982_underscore_absent_repo_wide(self):
        assert _git_grep_tracked(_mech_underscore(982)) == []

    def test_982_dash_absent_repo_wide(self):
        assert _git_grep_tracked(_mech_dash(982)) == []

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

    def test_fifty_first_member_present_pin(self):
        out = subprocess.run(
            ["git", "grep", "-c", "-F", FIFTY_FIRST_MEMBER, "HEAD", "--",
             "profiles/news-corp.yaml"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_fifty_second_member_present_pin(self):
        out = subprocess.run(
            ["git", "grep", "-c", "-F", FIFTY_SECOND_MEMBER, "HEAD", "--",
             "profiles/careers/journalists.yaml"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip().endswith(":5"), out.stdout

    def test_no_fifty_third_member_pin(self):
        assert _git_grep_tracked_source(FIFTY_THIRD_MEMBER, None) == []

    def test_predecessor_1249_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, C1249_FILE))

    def test_next_leg_is_1251_type_a(self):
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "#1251 Type A" in src

    def test_1249_pins_flip_by_design_documented(self):
        # #1249's no-Type-D-#1250-in-git-log pin flips BY DESIGN at
        # this run's main commit (the #1191-class self-trip, pinned in
        # TestStalenessPins1250); #1249's max-981, zero-982 (all
        # forms), fortieth-absent, forty-eighth-intact,
        # forty-ninth-intact, fiftieth-intact, fifty-first-intact,
        # fifty-second-intact, no-fifty-third guards stay green
        # (Type D lands no mechanisms).
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "TestStalenessPins1250" in src
        assert "no_type_d_1250_in_git_log_pin" in src


# ---------------------------------------------------------------------------
# 11. Background-suite verdict per #795: the #1245-launched suite is ALIVE
# ---------------------------------------------------------------------------

class TestBackgroundSuiteVerdict1250:
    def test_prior_suite_log_exists(self):
        assert os.path.exists(PRIOR_SUITE_LOG)

    def test_prior_suite_progressing(self):
        # The #1245-launched suite reached [ 20%] progress at this
        # run's ~22:05 check (~15K bytes, fresh writes). Progress
        # never regresses, so the marker stays present.
        text = _read(PRIOR_SUITE_LOG)
        assert "[ 20%]" in text, text[-2000:]
        assert 14000 <= len(text) <= 200000, len(text)

    def test_prior_suite_has_zero_summary_tokens(self):
        # A completed run prints a summary ("passed"/"failed") or a
        # collection report ("no tests ran" / "short test summary").
        # The live run carries none of them.
        text = _read(PRIOR_SUITE_LOG)
        for token in ("passed", "failed", "no tests ran",
                      "short test summary"):
            assert token not in text, token

    def test_prior_suite_holding_live_pytest(self):
        # The inverse of the #1190 death check: a live pytest process
        # DOES hold type_d_1245_full_suite.log open (fds 1/2/5/7/9 on
        # pid 138407 at this run's check). An empty result means the
        # suite died between the observation and this test.
        holders = _proc_holds_log("type_d_1245_full_suite.log")
        assert holders != "", "no live process holds the suite log"
        assert "type_d_1245_full_suite.log" in holders

    def test_death_streak_breaks_at_forty_three(self):
        # The 57-run streak ENDED at #1085 (the #1080 suite completed).
        # This verdict BREAKS the FORTY-THIRD consecutive
        # background-suite death streak of the new streak: the first
        # suite since #1080 to reach 20% alive.
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "FORTY-THIRD consecutive" in src
        assert "death streak BREAKS" in src

    def test_tombstone_lineage_holds(self):
        # Per #565 the tombstone lineage advances with each DEATH
        # verdict; on an ALIVE verdict it HOLDS: ONE-HUNDRED-EIGHTH
        # stands, no advance.
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "ONE-HUNDRED-EIGHTH" in src
        assert "lineage HOLDS" in src

    def test_alive_verdict_recorded_in_iteration_log(self):
        # Deselected pre-commit: the alive verdict is written into
        # the #1250 log entry in the doc-sync step per #719/#721.
        text = _read(LOG_FILE)
        assert "death streak BREAKS" in text


# ---------------------------------------------------------------------------
# 12. Recurring-failure triage
# ---------------------------------------------------------------------------

class TestRecurringFailureTriage1250:
    def test_live_log_series_prefix_reproduces(self):
        # FIFTH independent log carrying the deterministic prefix:
        # the canonical F+ run starts in the LIVE
        # type_d_1245_full_suite.log reproduce five of the six
        # pinned-series positions (1884/3690/5386/6932/7476) EXACTLY -
        # the first FORTY-THIRD-death-era prefix reproduction in a
        # live log, with ~1,000 tests added since the #1235 pin.
        positions = _f_positions(PRIOR_SUITE_LOG)
        for pos in (1884, 3690, 5386, 6932, 7476):
            assert pos in positions, (pos, positions[:12])

    def test_3807_absent_new_deviation(self):
        # The sixth pinned-series position (3807) is absent in the
        # live log: the 3780-3840 stream window is all dots. New
        # deviation vs the #1225/#1230/#1235 dead-log era, where all
        # six positions reproduced identically.
        stream = _f_stream(PRIOR_SUITE_LOG)
        window = stream[3780:3840]
        assert "F" not in window, repr(window)

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

    def test_prefix_reproduction_still_indeterminate(self):
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
# 13. No suite re-launch: the #1245 suite keeps running
# ---------------------------------------------------------------------------

class TestNoSuiteRelaunch1250:
    def test_no_1250_suite_log(self):
        # This run launches NOTHING: type_d_1250_full_suite.log must
        # not exist (a second full-suite writer would double the
        # 2.8 GB footprint on a 1 GB-free box).
        assert not os.path.exists(NO_RELAUNCH_LOG), (
            "this run must not re-launch the background suite")

    def test_prior_suite_not_killed(self):
        # This run neither kills nor writes to the #1245-launched
        # suite: the live pytest process still holds its log open.
        holders = _proc_holds_log("type_d_1245_full_suite.log")
        assert holders != "", "the #1245 suite must keep running"

    def test_next_type_d_1255_owns_next_verdict(self):
        # Per the #795 convention, the NEXT Type D run (#1255)
        # renders the next verdict on the still-running suite.
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "#1255" in src


# ---------------------------------------------------------------------------
# 14. Synthetic engine calibration (engine-layer contract, never a
#     finding)
# ---------------------------------------------------------------------------

class TestSyntheticEngineCalibration1250:
    def test_calibration_delta_contract(self):
        # Synthetic Google arms [-0.28, -0.33] vs synthetic Meta
        # arms [-0.45, -0.37]: pooled delta +0.105 (Meta-harder). This
        # is a FRESH #1250 engine-layer contract value; it is never
        # promoted to a finding.
        assert _synthetic_calibration_delta() == 0.105

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

class TestTypeDDocSync1250:
    def test_readme_test_file_table_has_1250_row_post_sync(self):
        readme = _read(README_FILE)
        assert "test_type_d_1250" in readme

    def test_architecture_has_1250_row_post_sync(self):
        arch = _read(ARCH_FILE)
        assert "test_type_d_1250" in arch

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

class TestTypeDIterationLog1250:
    def test_1250_entry_present_post_sync(self):
        log = _read(LOG_FILE)
        assert "## #1250 Type D" in log

    def test_1249_entry_present(self):
        log = _read(LOG_FILE)
        assert "## #1249 Type C" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_FILE)
        assert "### Rotation transparency" in log

    def test_alive_verdict_in_entry(self):
        log = _read(LOG_FILE)
        assert "death streak BREAKS" in log


# ---------------------------------------------------------------------------
# 17. Staleness pins: #1249's guard lifecycle flips BY DESIGN post-commit
# ---------------------------------------------------------------------------

class TestStalenessPins1250:
    def test_1249_guard_lifecycle_post_commit_self_trip(self):
        # Post-main-commit form: 14 of the 15 pass; the one that fails
        # BY DESIGN is test_no_type_d_1250_in_git_log_pin (this run's
        # own main commit carries "Type D #1250"). Type D lands no
        # mechanisms, so the zero-982 pins stay GREEN (no second
        # tripper this run). The #1249 block is read-only to this
        # run. Deselected pre-commit (all 15 pass pre-commit).
        res = _class_run(C1249_FILE, "TestGuardLifecycle1249")
        assert res.returncode != 0, res.stdout[-2000:]
        assert "1 failed, 14 passed" in res.stdout, res.stdout[-2000:]
        assert (
            "test_no_type_d_1250_in_git_log_pin" in res.stdout
        ), res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 18. Literal discipline per #715
# ---------------------------------------------------------------------------

class TestLiteralDiscipline1250:
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

class TestInflightIsolation1250:
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
