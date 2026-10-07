# -*- coding: utf-8 -*-
"""Type D #1275: verify m994/m995/m996 qualitative-discipline landings +
post-1270-1274 corpus integrity (max numeric mechanism id nine-nine-six;
zero next-number nine-nine-seven keys all forms; falsification ledger
HOLDS at 54: m985 the fifty-fourth member (profiles/guardian.yaml, 2
occurrences); m982 the fifty-third member (profiles/the-verge.yaml, 2
occurrences); m974 the fifty-second member
(profiles/careers/journalists.yaml, 5 occurrences); m973 the
fifty-first (profiles/news-corp.yaml, 3 occurrences); m959 the
fiftieth (profiles/careers/journalists.yaml, 3 occurrences); m956
the forty-ninth (profiles/careers/journalists.yaml); m952 the
forty-eighth (profiles/financial-times.yaml); the fifty-fifth
member-claim form absent repo-wide; the fortieth relationship
direction form absent in profiles/; thirty-fifth through thirty-ninth
stand) + #1270 background-suite verdict (DEAD at [ 7%]; the FIFTH
consecutive background-suite death of the new streak - the death
streak restarted at #1255 after the #1250 ALIVE verdict broke the
43-run death streak; tombstone lineage ONE-HUNDRED-TWELFTH ->
ONE-HUNDRED-THIRTEENTH; full suite re-launched to
type_d_1275_full_suite.log) + recurring-failure triage (THREE F marks
in the dead stream - all three root-caused and ALL THREE REPAIRED this
run: (1) test_openai_softer_still - Atlantic x OpenAI
coverage_prediction loaded adversarial against the pinned softer; root
cause: Type A #1137 (m913, Oct 2 2026) deleted the two-space meta
entity-key line when inserting its mechanism block, orphaning the meta
body at four-space indentation inside the openai mapping where its
keys shadowed the entity-level keys under duplicate-key-wins-last;
(2) test_all_entities_covered[atlantic] - the same deletion removed
the meta entity, failing the seven-entity coverage pin; (3)
test_relationship_types_valid - wired.snap
personnel_career_migration (m727, Type A #827) absent from
competitor-entities.yaml relationship_types (the #1085 fix extended
only test_competitor_coverage.py's own enum). Repairs landed this run:
atlantic.yaml meta key restored (openai licensing/softer unshadowed,
meta none/adversarial stub back, all seven entities present);
relationship_types gains personnel_career_migration with m727
provenance. Standalone re-run of the three files: 3 failed / 135
passed pre-repair, 11 passed post-repair across the three previously
failing nodes. Outcome DETERMINATE, pinned as repaired evidence) +
corpus repairs pinned (TestAtlanticMetaKeyRestoration1275,
TestRelationshipTypesEnumRepair1275).

m994 (Type A #1272, profiles/guardian.yaml
competitor_relationships.openai): Guardian Oct-3-2026 Dan Milmo
Robinson-resignation straight-news original (-0.30 MANUAL
ILLUSTRATIVE, NEW arm) vs carried Guardian x Meta accountability
register (m687 police-warnings -0.55 + teen-accounts -0.45, mean
-0.50). Illustrative delta (OpenAI minus Meta) +0.25 clean (n=1 vs
n=1), +0.20 pooled (n=1 vs n=2). Directionally softer for the Feb-2025
licensing partner, matching the softer-prediction; temporal
replication of m934's +0.167. NOT a falsification-family member.
Ledger HOLDS at 54. MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026
standing rule; NOT artifact-grade; no analysis.json update.
Correlation is not causation; hypothesis-generating only.

m995 (Type B #1273, profiles/careers/journalists.yaml
kalley_huang_type_b competitor_coverage): FIRST dedicated Type B
mechanism on Kalley Huang (NYT). Huang's Meta ~Aug-30 arm runs an
accountability-exposure register on the secret Anthropic-spend scoop
(co-byline Eli Tan, -0.35 MANUAL ILLUSTRATIVE) vs her Apple Sep-8 arm
running innovation-positive foldable-iPhone product news (solo byline,
+0.05 MANUAL ILLUSTRATIVE). Illustrative delta (Apple minus Meta)
+0.40 in the Meta-hard direction. CONTROL-CASE per the
#1243/#1248/#1268 precedent: no documented financial relationship
between NYT and Meta or Apple in the corpus, so the uniform
payer-softening prediction is NOT adjudicated. NOT a
falsification-family member. Ledger HOLDS at 54. MANUAL ILLUSTRATIVE
ONLY per the Aug 28 2026 standing rule; NOT artifact-grade; no
analysis.json update.

m996 (Type C #1274, profiles/competitor-entities.yaml top-level):
FIRST dedicated corpus mechanism on the AI-agent ad-buy rail: pubX
$5M Series A (Chicago Ventures lead) + Compliant acquisition; Oct 7
live agent-to-agent Mucinex media buy at Advertising Week New York
with Paradium.AI and USA TODAY Co. reviewing and accepting; prices the
agent-action traffic type m391 (Comet Plus 80/20) allocates revenue
across; Paradium.AI double-participation with m738 (RTB Digital
10-year $100M/yr 8-K); tollbooth-layer join with m786 (where m786
prices crawler ACCESS, pubX prices agent PLACEMENT). BOUNDARY: no
competitor lab is a counterparty (monetization rail, not a
lab-publisher deal). Verdict mechanism_documented; connects_to [738,
391, 750, 786, 463]; NOT a falsification-family member; ledger holds
at 54; no new direction (fortieth absent by design; thirty-fifth
through thirty-ninth stand). Tone NOT_SCORED. MANUAL / qualitative
ONLY per the Aug 28 2026 standing rule. NOT artifact-grade; no
analysis.json update.

Statistical discipline: the finding layer stays MANUAL/QUALITATIVE
ONLY per the Aug 28 2026 standing rule (no corpus mechanisms landed
this run; engine NOT run on corpus; is_significant never asserted on
corpus data; NOT artifact-grade; no analysis.json update). Fresh
synthetic engine calibration this run - engine-layer contract only,
never promoted to a finding.
Synthetic Apple arms [-0.10, -0.14] vs synthetic Meta arms [-0.38, -0.34],
pooled delta +0.240.

Rotation transparency: this run is iteration #1275 Type D, the FIRST
and OPENING leg of the 1275-1279 window (D #1275 -> E #1276 -> A #1277
-> B #1278 -> C #1279 per the #565 anchor + rotation guard).
Committed predecessors verified pre-commit: #1274 Type C (main
856e8b86 / anchor 27751674 / doc-sync d9d245d9 / log-hash e9661355);
#1273 Type B (main 4b9d81ba / anchor 9aa84bf5 / doc-sync 8e2e24c9 /
log-hash ccafb5ef); #1272 Type A (main 982ca183 / anchor cbe557f1 /
doc-sync d2a66b6b / log-hash 38176763); #1271 Type E (main 2a299281 /
anchor c4669ea2 / doc-sync 5c41406e / log-hash 33006eae); the
1270-1274 window is VERIFIED CLOSED. Rotation guard: this run's main
commit is the anchor per #565; ANCHORED_SHA patched post-commit. Next:
#1276 Type E continues the window; the next background-suite verdict
belongs to #1280 per #795.

Guard lifecycle note: #1274's forward guards (max-nine-nine-six,
zero-nine-nine-seven all forms, no-Type-D-#1275-in-git-log, fortieth
absent, forty-eighth through fifty-fourth intact, fifty-fifth absent,
ledger 54) hold GREEN pre-commit; the no-Type-D-#1275-in-git-log pin
flips BY DESIGN at this run's main commit (the #1191-class self-trip,
pinned post-commit in TestStalenessPins1275 expecting 16 passed / 1
failed).

In-gate: 116 passed + 14 deselected by design (TestAnchor1275 5 +
TestTypeDDocSync1275 3 + TestTypeDIterationLog1275 4 +
TestStalenessPins1275 1 + test_dead_verdict_recorded_in_iteration_log 1
per #565/#719/#721); 2 in-gate defects found and fixed (calibration
docstring phrase split across a line break; suite-log accumulation
threshold vs slow collection timing); 4 corpus/test repairs landed and
pinned (atlantic.yaml meta-key restoration reversing the #1137
shadowing defect; competitor-entities.yaml relationship_types
personnel_career_migration extension per the #1085 convention;
test_type_d_deal_count_cascade_aug6.py xAI valuation repin to $250B
post-SpaceX-merger; test_type_d_02am_cross_validation_aug9.py
count-sync extraction repaired from stale-prose max to
stats-table/tree-range); test-file constants post-sync-positive per
#719 (130 collected, 20 classes); 0 browser.search query sets this run
(all arms already in corpus via #1272-#1274); 0 browser.open per #503.

Do NOT touch #1024 (m846 in profiles/competitor-entities.yaml), #899
(nytimes.yaml m771 hunk), #938 (Type B test file working-tree edit),
#900 (untracked Type D test file), #1012-wt (working-tree edit on the
committed Type A #1012 file). Explicit-path staging (this run: the new
test file + the atlantic.yaml meta-key hunk + the
competitor-entities.yaml relationship_types hunk, each staged by
explicit path; the m846 hunk stays out).

ASCII-only, no em dashes. Needles format-built per #715: this file
must not carry contiguous numeric/underscore/dash mechanism-key forms
of the landed (nine-nine-six) or next (nine-nine-seven) number, the
forty-eighth / forty-ninth / fiftieth / fifty-first / fifty-second /
fifty-third / fifty-fourth / fifty-fifth member-claim forms, or the
thirty-fifth through fortieth direction forms; the constants are
constructed at runtime. (The landed ordinals live as short lowercase
forms in prose here; the live full-form claims live in profiles: the
forty-eighth in financial-times.yaml, the forty-ninth and fiftieth
and fifty-second in profiles/careers/journalists.yaml, the
fifty-first in profiles/news-corp.yaml, the fifty-third in
profiles/the-verge.yaml, the fifty-fourth in profiles/guardian.yaml.)
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
GUARDIAN_FILE = os.path.join(PROFILES_DIR, "guardian.yaml")
ATLANTIC_FILE = os.path.join(PROFILES_DIR, "atlantic.yaml")
JOURNALISTS_FILE = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
ENTITIES_FILE = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
LOG_FILE = os.path.join(REPO_ROOT, "iteration-log.md")
README_FILE = os.path.join(REPO_ROOT, "README.md")
ARCH_FILE = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")

# Block keys are plain literals: they carry the landing ITERATION
# number (1272/1273/1274) and no mechanism-number substring (designed
# keying per #715). Iterations are the landing iterations, not the
# mechanism ids.
KEY_994 = ("type_a_1272_guardian_openai_robinson_resignation_"
           "culture_broken_october")
KEY_995 = ("type_b_1273_kalley_huang_nyt_meta_anthropic_spend_"
           "vs_apple_foldable_oct06_8pm")
KEY_996 = ("type_c_1274_pubx_agent_to_agent_advertising_"
           "infrastructure_oct07")
JOURNALIST_KEY_995 = "kalley_huang_type_b"
OWN_BASENAME = ("test_type_d_1275_m994_m995_m996_qualitative_"
                "corpus_integrity_oct07_1am.py")

# Predecessor test files for supersession pins.
E1271_FILE = ("test_type_e_1271_podcast_sentiment_177th_"
              "verification_oct06_5pm.py")
A1272_FILE = ("test_type_a_1272_guardian_openai_robinson_resignation_"
              "oct06_6pm.py")
B1273_FILE = ("test_type_b_1273_kalley_huang_nyt_meta_anthropic_spend_"
              "vs_apple_foldable_oct06_8pm.py")
C1274_FILE = ("test_type_c_1274_pubx_agent_to_agent_advertising_"
              "infrastructure_oct07_12am.py")
THIS_FILE = OWN_BASENAME

# Prior-window background suite (verdict rendered this run: DEAD at
# [ 7%]). This run re-launches the full suite to NEW_SUITE_LOG; the
# #1280 Type D run owns the next verdict per #795.
GOAL_HIDDEN = os.path.join(
    os.path.expanduser("~"),
    "workspace",
    "goals",
    "mediascope-meta-wearables-press-analysis",
    "hidden_files",
)
PRIOR_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1270_full_suite.log")
NEW_SUITE_LOG = os.path.join(GOAL_HIDDEN, "type_d_1275_full_suite.log")
NON_D_SUITE_LOGS = [
    os.path.join(GOAL_HIDDEN, "type_d_1276_full_suite.log"),
    os.path.join(GOAL_HIDDEN, "type_d_1277_full_suite.log"),
    os.path.join(GOAL_HIDDEN, "type_d_1278_full_suite.log"),
    os.path.join(GOAL_HIDDEN, "type_d_1279_full_suite.log"),
]

# Patched pre-main with the true collected count per #719.
# Pre-sync: 70731 tests / 1599 files. PATCH TARGET (in-gate count).
README_TEST_COUNT = 70861  # post-doc-sync total; patched per #719 (70731+130=70861)
README_FILE_COUNT = 1600  # post-doc-sync total (pre-sync 1599 + 1)
TEST_BASENAME = OWN_BASENAME

# Anchor placeholder per #565: patched to the main commit's 40-char SHA in the
# anchor followup. The shape test is placeholder-or-main tolerant pre-commit.
ANCHORED_SHA = "0" * 40  # patched in the anchor followup per #565

MECH_NUM = 996
NEXT_NUM = 997

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
FORTY_NINTH_MEMBER = "FORT" + "Y-NINTH falsification-family member"
FIFTIETH_MEMBER = "FIFT" + "IETH falsification-family member"
FIFTY_FIRST_MEMBER = "FIFT" + "Y-FIRST falsification-family member"
FIFTY_SECOND_MEMBER = "FIFT" + "Y-SECOND falsification-family member"
FIFTY_THIRD_MEMBER = "FIFT" + "Y-THIRD falsification-family member"
FIFTY_FOURTH_MEMBER = "FIFT" + "Y-FOURTH falsification-family member"
FIFTY_FIFTH_MEMBER = "FIFT" + "Y-FIFTH falsification-family member"

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
            yield os.path.join(root, f)


def _proc_holds_log(log_name):
    out = subprocess.run(
        ["bash", "-c",
         "ls -l /proc/[0-9]*/fd/* 2>/dev/null | grep -F "
         "'%s' | head -5" % log_name],
        cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
    )
    return out.stdout.strip()


def _m994_block():
    # The m994 block lives under competitor_relationships -> openai
    # in profiles/guardian.yaml (per the #1272 land; spec-faithful
    # polarity: the NEW arm lands on the OpenAI target side).
    return _yaml(GUARDIAN_FILE)["competitor_relationships"]["openai"][KEY_994]


def _m995_block():
    # Kalley Huang's journalist entry is a top-level key in the
    # careers journalists.yaml (the per-#643 key convention); the
    # m995 block lives under its competitor_coverage sub-key.
    return _yaml(JOURNALISTS_FILE)[JOURNALIST_KEY_995][
        "competitor_coverage"][KEY_995]


def _m996_block():
    return _yaml(ENTITIES_FILE)[KEY_996]


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
    """Fresh engine-layer calibration contract for #1275.

    Pooled illustrative delta over fully synthetic arms (no corpus
    input, no repo reads). Engine-layer ONLY: never promoted to a
    finding, never scored against the corpus.
    """
    synthetic_apple_arms = [-0.10, -0.14]
    synthetic_meta_arms = [-0.38, -0.34]
    pooled_apple = (sum(synthetic_apple_arms)
                    / len(synthetic_apple_arms))
    pooled_meta = sum(synthetic_meta_arms) / len(synthetic_meta_arms)
    return round(pooled_apple - pooled_meta, 3)


# ---------------------------------------------------------------------------
# 1. Anchor (pre-commit placeholder per #565; patched in anchor followup).
# ---------------------------------------------------------------------------


class TestAnchor1275:
    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit form: ANCHORED_SHA is 0*40; the anchor followup
        # patches it to this run's main commit SHA per #565.
        assert ANCHORED_SHA == "0" * 40

    def test_anchor_sha_patched_to_main_commit(self):
        # Post-commit form: ANCHORED_SHA patched to this run's main
        # commit (40 hex chars). Deselected pre-commit with the class.
        assert ANCHORED_SHA != "0" * 40
        assert len(ANCHORED_SHA) == 40

    def test_anchor_sha_format(self):
        assert len(ANCHORED_SHA) == 40
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA)

    def test_this_run_main_commit_is_anchor(self):
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "anchor per #565" in src

    def test_rotation_phrase_in_docstring(self):
        assert "FIRST" in __doc__ and "OPENING leg" in __doc__


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1274 window closed, #1275 window opens.
# ---------------------------------------------------------------------------


class TestTypeDRotationGuard1275:
    def test_predecessor_shas_in_git_log(self):
        out = subprocess.run(
            ["git", "log", "--oneline", "-30"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        ).stdout
        for sha in ("856e8b86", "4b9d81ba", "982ca183", "2a299281"):
            assert sha in out, sha

    def test_1274_type_c_in_git_log(self):
        out = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type C #1274", "-3"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        ).stdout
        assert "1274" in out

    def test_1270_1274_window_closed(self):
        assert "1270-1274 window is VERIFIED CLOSED" in __doc__

    def test_next_window_opens_1275(self):
        assert "1275-1279 window" in __doc__

    def test_next_leg_is_1276_type_e(self):
        assert "E #1276" in __doc__


# ---------------------------------------------------------------------------
# 3. Corpus integrity: m994/m995/m996 landed; max 996; zero 997.
# ---------------------------------------------------------------------------


class TestTypeDCorpusIntegrity1275:
    def test_m994_block_present_in_guardian_yaml(self):
        block = _m994_block()
        assert block["mechanism_id"] == 994
        assert block["block_key"] == KEY_994

    def test_m994_test_file_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, A1272_FILE))

    def test_m995_block_present_in_journalists_yaml(self):
        block = _m995_block()
        assert block["mechanism_id"] == 995
        assert block["iteration"] == 1273
        assert block["type"] == "B"
        assert block["block_key"] == KEY_995

    def test_m995_test_file_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, B1273_FILE))

    def test_m996_block_present_in_competitor_entities_yaml(self):
        block = _m996_block()
        assert block["mechanism_id"] == 996
        assert block["iteration"] == 1274
        assert block["block_key"] == KEY_996

    def test_m996_test_file_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, C1274_FILE))

    def test_no_numeric_997_mechanism_id_in_profiles(self):
        needle = _mech_id_colon(NEXT_NUM)
        for path in _iter_source_files():
            if not path.startswith(PROFILES_DIR):
                continue
            text = _read(path)
            assert needle not in text, path

    def test_max_numeric_mechanism_id_is_996(self):
        found = set()
        for path in _iter_source_files():
            if not path.startswith(PROFILES_DIR):
                continue
            for m in re.finditer(r"mechanism_id:\s*(\d+)", _read(path)):
                found.add(int(m.group(1)))
        assert max(found) == MECH_NUM, max(found)

    def test_zero_next_number_underscore_forms(self):
        needle = _mech_underscore(NEXT_NUM)
        hits = [p for p in _iter_source_files() if needle in _read(p)]
        assert hits == [], hits

    def test_zero_next_number_dash_forms(self):
        needle = _mech_dash(NEXT_NUM)
        hits = [p for p in _iter_source_files() if needle in _read(p)]
        assert hits == [], hits


# ---------------------------------------------------------------------------
# 4. m994 qualitative discipline (Type A #1272, Guardian x OpenAI).
# ---------------------------------------------------------------------------


class TestTypeDM994QualitativeDiscipline1275:
    def test_m994_mechanism_id(self):
        assert _m994_block()["mechanism_id"] == 994

    def test_m994_block_key_matches(self):
        assert _m994_block()["block_key"] == KEY_994

    def test_m994_verdict_thesis_consistent_observation(self):
        assert _m994_block()["verdict"] == "thesis_consistent_observation"

    def test_m994_not_falsification_member(self):
        block = _m994_block()
        assert block["falsification_family_member"] is False
        assert block["falsification_ledger"] == "54"

    def test_m994_openai_minus_meta_clean_delta(self):
        scorer = _m994_block()["asymmetry_scorer_result"]
        assert scorer["illustrative_delta_openai_minus_meta_clean"] == 0.25

    def test_m994_pooled_delta(self):
        scorer = _m994_block()["asymmetry_scorer_result"]
        assert scorer["illustrative_delta_openai_minus_meta_pooled"] == 0.2

    def test_m994_engine_not_run(self):
        scorer = _m994_block()["asymmetry_scorer_result"]
        assert scorer["engine_run"] is False
        assert scorer["is_significant"] is False
        assert scorer["p_value"] == "NOT_CALCULATED"

    def test_m994_no_analysis_json_update(self):
        assert _m994_block()["no_analysis_json_update"] is True

    def test_m994_openai_arm_tone(self):
        scorer = _m994_block()["asymmetry_scorer_result"]
        assert scorer["target_scores_MANUAL_ILLUSTRATIVE"] == [-0.3]

    def test_m994_test_file_matches(self):
        assert A1272_FILE.startswith("test_type_a_1272")


# ---------------------------------------------------------------------------
# 5. m995 qualitative discipline (Type B #1273, Kalley Huang).
# ---------------------------------------------------------------------------


class TestTypeDM995QualitativeDiscipline1275:
    def test_m995_mechanism_id(self):
        assert _m995_block()["mechanism_id"] == 995

    def test_m995_iteration_and_type(self):
        block = _m995_block()
        assert block["iteration"] == 1273
        assert block["type"] == "B"

    def test_m995_journalist_huang(self):
        assert _m995_block()["journalist"] == "Kalley Huang"

    def test_m995_verdict_control_case_observation(self):
        assert _m995_block()["verdict"].startswith(
            "control_case_observation")

    def test_m995_not_falsification_member(self):
        assert _m995_block()["falsification_family_member"] is False

    def test_m995_ledger_holds_at_54_in_verdict(self):
        assert "Ledger holds at 54" in _m995_block()["verdict"]

    def test_m995_manual_illustrative(self):
        assert "MANUAL ILLUSTRATIVE ONLY" in _m995_block()["finding"]

    def test_m995_meta_arm_tone(self):
        assert _m995_block()["meta_arm"][
            "tone_MANUAL_ILLUSTRATIVE"] == -0.35

    def test_m995_apple_arm_tone(self):
        assert _m995_block()["apple_arm"][
            "tone_MANUAL_ILLUSTRATIVE"] == 0.05

    def test_m995_block_key_matches(self):
        assert _m995_block()["block_key"] == KEY_995

    def test_m995_test_file_matches(self):
        assert _m995_block()["test_file"].endswith(B1273_FILE)


# ---------------------------------------------------------------------------
# 6. m996 qualitative discipline (Type C #1274, pubX).
# ---------------------------------------------------------------------------


class TestTypeDM996QualitativeDiscipline1275:
    def test_m996_mechanism_id(self):
        assert _m996_block()["mechanism_id"] == 996

    def test_m996_iteration_and_type(self):
        block = _m996_block()
        assert block["iteration"] == 1274
        assert block["iteration_type"] == "C"

    def test_m996_verdict_mechanism_documented(self):
        assert _m996_block()["verdict"] == "mechanism_documented"

    def test_m996_not_falsification_member(self):
        block = _m996_block()
        assert block["falsification_family_member"] is False
        assert "ledger holds at 54" in block["falsification_family"]

    def test_m996_block_key_matches(self):
        assert _m996_block()["block_key"] == KEY_996

    def test_m996_connects_to(self):
        assert _m996_block()["connects_to"] == [738, 391, 750, 786, 463]

    def test_m996_tone_not_scored(self):
        assert _m996_block()["tone_scored"] is False

    def test_m996_no_analysis_json_update(self):
        assert _m996_block()["no_analysis_json_update"] is True

    def test_m996_no_new_direction(self):
        assert "no new direction" in _m996_block()["finding"].lower()

    def test_m996_manual_only(self):
        assert "MANUAL" in _m996_block()["finding"]


# ---------------------------------------------------------------------------
# 7. Falsification ledger holds at 54.
# ---------------------------------------------------------------------------


class TestTypeDFalsificationLedger1275:
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

    def test_fifty_third_present_in_verge(self):
        out = subprocess.run(
            ["git", "grep", "-c", "-F", FIFTY_THIRD_MEMBER, "HEAD", "--",
             "profiles/the-verge.yaml"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fourth_present_in_guardian(self):
        # m985 landed at #1257: the fifty-fourth member-claim form is
        # live in profiles/guardian.yaml (2 occurrences); no later
        # run has displaced it.
        out = subprocess.run(
            ["git", "grep", "-c", "-F", FIFTY_FOURTH_MEMBER, "HEAD", "--",
             "profiles/guardian.yaml"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fifth_absent(self):
        assert _git_grep_tracked_source(FIFTY_FIFTH_MEMBER, None) == []

    def test_fortieth_direction_absent(self):
        assert _git_grep_tracked_source(_T40, "profiles/") == []

    def test_directions_thirty_fifth_through_thirty_ninth_present(self):
        for needle in (_T35, _T36, _T37, _T38, _T39):
            assert _git_grep_tracked_source(needle, "profiles/") != [], (
                needle)

    def test_ledger_holds_at_54(self):
        fam = _m996_block()["falsification_family"]
        assert "ledger holds at 54" in fam
        assert "NOT a member" in fam


# ---------------------------------------------------------------------------
# 8. Corpus repair pins: the #1137 atlantic.yaml shadowing defect.
# ---------------------------------------------------------------------------


class TestAtlanticMetaKeyRestoration1275:
    """Pin the #1137 repair: the meta entity key is back at two-space
    indentation, so the orphaned body no longer shadows the openai
    entity-level keys under duplicate-key-wins-last."""

    def _cr(self):
        return _yaml(ATLANTIC_FILE)["competitor_relationships"]

    def test_meta_entity_present(self):
        assert "meta" in self._cr()

    def test_all_seven_entities_present(self):
        assert set(self._cr().keys()) == {
            "openai", "meta", "anthropic", "amazon", "apple", "google",
            "x_twitter"}

    def test_openai_unshadowed_licensing_softer(self):
        # Pre-repair the loader returned financial_tie none /
        # coverage_prediction adversarial for openai (the orphaned
        # meta body shadowing the entity keys).
        openai = self._cr()["openai"]
        assert openai["financial_tie"] == "licensing"
        assert openai["coverage_prediction"] == "softer"

    def test_meta_stub_restored(self):
        meta = self._cr()["meta"]
        assert meta["financial_tie"] == "none"
        assert meta["estimated_value"] == "$0"
        assert meta["coverage_prediction"] == "adversarial"

    def test_meta_key_at_entity_indentation(self):
        # The raw file must carry the meta key at two-space
        # indentation (entity level), not nested inside openai.
        text = _read(ATLANTIC_FILE)
        assert re.search(r"^  meta:$", text, re.M)


# ---------------------------------------------------------------------------
# 9. Corpus repair pins: relationship_types enum extension.
# ---------------------------------------------------------------------------


class TestRelationshipTypesEnumRepair1275:
    """Pin the #1085-class repair at the corpus-enum level:
    personnel_career_migration (m727) is a recognized
    relationship_types value, so test_financial_relationships.py's
    corpus-driven valid_types set accepts the wired.snap tie."""

    def _rel_types(self):
        return _yaml(ENTITIES_FILE)["relationship_types"]

    def test_personnel_career_migration_defined(self):
        assert "personnel_career_migration" in self._rel_types()

    def test_provenance_mentions_727(self):
        desc = self._rel_types()["personnel_career_migration"]
        assert "727" in desc

    def test_wired_snap_tie_now_valid(self):
        wired = _yaml(os.path.join(PROFILES_DIR, "wired.yaml"))
        tie = wired["competitor_relationships"]["snap"]["financial_tie"]
        assert tie == "personnel_career_migration"
        assert tie in self._rel_types()

    def test_no_duplicate_enum_keys(self):
        text = _read(ENTITIES_FILE)
        assert text.count("personnel_career_migration:") == 1


# ---------------------------------------------------------------------------
# 10. Forward-looking staleness: #1274's pins pre-commit.
# ---------------------------------------------------------------------------


class TestTypeDForwardLookingStaleness1275:
    def test_1274_pins_on_996_landing(self):
        # #1274 landed the max (nine-nine-six); its guard-lifecycle
        # pins on the 996 landing stay green pre-commit (Type D
        # lands no mechanisms).
        res = _class_run(C1274_FILE, "TestGuardLifecycle1274")
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1274_no_type_d_1275_pin_green_precommit(self):
        # The no-Type-D-#1275-in-git-log pin is green pre-commit and
        # flips BY DESIGN at this run's main commit (the #1191-class
        # self-trip); pinned post-commit in TestStalenessPins1275.
        out = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type D #1275"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        ).stdout
        assert "Type D #1275" not in out

    def test_1274_guard_lifecycle_997_numeric_stays_green_precommit(self):
        needle = _mech_id_colon(NEXT_NUM)
        hits = [p for p in _iter_source_files()
                if p.startswith(PROFILES_DIR) and needle in _read(p)]
        assert hits == [], hits

    def test_1274_guard_lifecycle_997_underscore_stays_green_precommit(self):
        needle = _mech_underscore(NEXT_NUM)
        hits = [p for p in _iter_source_files() if needle in _read(p)]
        assert hits == [], hits

    def test_1274_guard_lifecycle_997_dash_stays_green_precommit(self):
        needle = _mech_dash(NEXT_NUM)
        hits = [p for p in _iter_source_files() if needle in _read(p)]
        assert hits == [], hits

    def test_1273_pins_no_flip_documented(self):
        # #1273's guard lifecycle already flipped at its own main
        # commit; nothing in this run re-flips it (Type D lands no
        # mechanisms, repairs touch no member/direction forms).
        assert "1273" in __doc__


# ---------------------------------------------------------------------------
# 11. Guard lifecycle: forward pins for #1276.
# ---------------------------------------------------------------------------


class TestGuardLifecycle1275:
    def test_pins_on_996_landing(self):
        # m994/m995/m996 are landed; the max-numeric pin sits on the
        # landed number while the next-number pins stay green.
        assert _m994_block()["mechanism_id"] == MECH_NUM - 2
        assert _m995_block()["mechanism_id"] == MECH_NUM - 1
        assert _m996_block()["mechanism_id"] == MECH_NUM

    def test_no_type_d_1275_in_git_log_pin(self):
        out = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type D #1275"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        ).stdout
        assert "Type D #1275" not in out

    def test_997_numeric_absent_in_profiles(self):
        needle = _mech_id_colon(NEXT_NUM)
        for path in _iter_source_files():
            if not path.startswith(PROFILES_DIR):
                continue
            assert needle not in _read(path), path

    def test_997_underscore_absent_repo_wide(self):
        needle = _mech_underscore(NEXT_NUM)
        hits = [p for p in _iter_source_files() if needle in _read(p)]
        assert hits == [], hits

    def test_997_dash_absent_repo_wide(self):
        needle = _mech_dash(NEXT_NUM)
        hits = [p for p in _iter_source_files() if needle in _read(p)]
        assert hits == [], hits

    def test_no_fortieth_direction_pin(self):
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

    def test_fifty_third_member_intact_pin(self):
        out = subprocess.run(
            ["git", "grep", "-c", "-F", FIFTY_THIRD_MEMBER, "HEAD", "--",
             "profiles/the-verge.yaml"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_fifty_fourth_member_present_pin(self):
        out = subprocess.run(
            ["git", "grep", "-c", "-F", FIFTY_FOURTH_MEMBER, "HEAD", "--",
             "profiles/guardian.yaml"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_fifty_fifth_member_pin(self):
        assert _git_grep_tracked_source(FIFTY_FIFTH_MEMBER, None) == []

    def test_predecessor_1274_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, C1274_FILE))

    def test_next_leg_is_1276_type_e(self):
        assert "E #1276" in __doc__

    def test_1274_pins_flip_by_design_documented(self):
        assert "flips BY DESIGN" in __doc__


# ---------------------------------------------------------------------------
# 12. Background-suite verdict: the #1270-launched suite is DEAD at [ 7%].
# ---------------------------------------------------------------------------


class TestBackgroundSuiteVerdict1275:
    def test_prior_suite_log_exists(self):
        assert os.path.exists(PRIOR_SUITE_LOG)

    def test_prior_suite_stalled_at_7(self):
        # The #1270-launched suite froze at [  7%] progress: 26161
        # bytes, 314 lines, three F marks, last write Oct 6 2026
        # 18:12, zero live pytest processes. Progress never
        # regresses, so the marker stays present and [  8%] never
        # arrives.
        text = _read(PRIOR_SUITE_LOG)
        assert "[  7%]" in text, text[-2000:]
        assert "[  8%]" not in text
        assert 10000 <= len(text) <= 100000, len(text)

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
        # type_d_1270_full_suite.log open anymore (the /proc open-fd
        # check returns empty). The suite died between the #1274
        # observation (~00:10 PDT Oct 7, [  7%], processes dead) and
        # this run's check.
        holders = _proc_holds_log("type_d_1270_full_suite.log")
        assert holders == "", holders

    def test_fifth_death_of_new_streak(self):
        # The 57-run streak ENDED at #1085 (the #1080 suite
        # completed). The 43-run streak BROKE at #1250 (the #1245
        # suite was verdict ALIVE at 20%). #1255 verdict the FIRST
        # consecutive background-suite death of the new streak, #1260
        # the SECOND, #1265 the THIRD, #1270 the FOURTH. This verdict
        # is the FIFTH consecutive background-suite death of the new
        # streak.
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "FIFTH consecutive" in src
        assert "death of the new streak" in src

    def test_tombstone_lineage_advances(self):
        # Per #565 the tombstone lineage advances with each DEATH
        # verdict: ONE-HUNDRED-TWELFTH -> ONE-HUNDRED-THIRTEENTH.
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "ONE-HUNDRED-THIRTEENTH" in src
        assert "lineage advances" in src

    def test_dead_verdict_recorded_in_iteration_log(self):
        # Deselected pre-commit: the dead verdict is written into
        # the #1275 log entry in the doc-sync step per #719/#721.
        text = _read(LOG_FILE)
        assert "FIFTH consecutive" in text


# ---------------------------------------------------------------------------
# 13. Recurring-failure triage: three F marks, all repaired (DETERMINATE).
# ---------------------------------------------------------------------------


class TestRecurringFailureTriage1275:
    def test_three_f_marks_in_dead_stream(self):
        text = _read(PRIOR_SUITE_LOG)
        f_lines = [line for line in text.split("\n")
                   if re.search(r"\.+F", line)]
        assert len(f_lines) == 3, f_lines

    def test_f_files_are_the_triaged_three(self):
        text = _read(PRIOR_SUITE_LOG)
        assert "test_atlantic_anthropic_mitigation_credit_asymmetry" in text
        assert "test_competitor_coverage.py" in text
        assert "test_financial_relationships.py" in text

    def test_root_cause_1137_meta_key_deletion_documented(self):
        # The #1137 defect is pinned in this file's docstring: the
        # deleted two-space meta entity-key line orphaned the meta
        # body inside the openai mapping (duplicate-key shadowing).
        assert "duplicate-key-wins-last" in __doc__
        assert "orphaning the meta" in __doc__

    def test_repairs_landed_in_working_tree(self):
        # Both repairs are in the working tree pre-commit (staged by
        # explicit path in the main commit): the atlantic meta key
        # and the relationship_types enum extension.
        atlantic = _yaml(ATLANTIC_FILE)["competitor_relationships"]
        assert "meta" in atlantic
        assert atlantic["openai"]["coverage_prediction"] == "softer"
        rel_types = _yaml(ENTITIES_FILE)["relationship_types"]
        assert "personnel_career_migration" in rel_types

    def test_previously_failing_nodes_now_pass(self):
        # The three dead-stream F marks reproduced in isolation
        # pre-repair (3 failed / 135 passed across the three files);
        # post-repair the exact failing nodes pass.
        nodes = [
            ("test_atlantic_anthropic_mitigation_credit_asymmetry_aug30_404.py",
             "TestAtlanticFinancialRelationships404::test_openai_softer_still"),
            ("test_competitor_coverage.py",
             "TestPublicationRelationships::test_all_entities_covered[atlantic]"),
            ("test_financial_relationships.py",
             "TestCrossProfileConsistency::test_relationship_types_valid"),
        ]
        for filename, node in nodes:
            res = _node_run(filename, node)
            assert res.returncode == 0, (filename, node,
                                         res.stdout[-2000:])

    def test_triage_outcome_determinate(self):
        # Unlike #1270's INDETERMINATE (dead before the first pinned
        # position), this window's triage is DETERMINATE: three F
        # marks observed, root-caused, repaired, re-verified green.
        assert "Outcome DETERMINATE" in __doc__


# ---------------------------------------------------------------------------
# 14. Suite relaunch: the #1275-launched full suite.
# ---------------------------------------------------------------------------


class TestSuiteRelaunch1275:
    def test_1275_suite_log_exists(self):
        assert os.path.exists(NEW_SUITE_LOG), NEW_SUITE_LOG

    def test_1275_suite_log_accumulating(self):
        size = os.path.getsize(NEW_SUITE_LOG)
        assert size > 500, size

    def test_no_non_d_window_suite_logs(self):
        for path in NON_D_SUITE_LOGS:
            assert not os.path.exists(path), path

    def test_next_type_d_1280_owns_next_verdict(self):
        assert "#1280" in __doc__


# ---------------------------------------------------------------------------
# 15. Synthetic engine calibration (engine-layer contract, never a finding).
# ---------------------------------------------------------------------------


class TestSyntheticEngineCalibration1275:
    def test_calibration_delta_contract(self):
        # Synthetic Apple arms [-0.10, -0.14] vs synthetic Meta
        # arms [-0.38, -0.34]: pooled delta +0.240 (Meta-harder). This
        # is a FRESH #1275 engine-layer contract value; it is never
        # promoted to a finding.
        assert _synthetic_calibration_delta() == 0.24

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
        assert "no analysis.json update" in doc


# ---------------------------------------------------------------------------
# 16. Doc-sync per #719 (3 tests; deselected pre-commit, flipped post-sync)
# ---------------------------------------------------------------------------


class TestTypeDDocSync1275:
    def test_readme_test_file_table_has_1275_row_post_sync(self):
        readme = _read(README_FILE)
        assert "test_type_d_1275" in readme

    def test_architecture_has_1275_row_post_sync(self):
        arch = _read(ARCH_FILE)
        assert "test_type_d_1275" in arch

    def test_readme_stats_ratcheted(self):
        # Post-sync-positive form per #719: asserts the ratcheted
        # counts (README_TEST_COUNT tests across README_FILE_COUNT
        # files). Fails pre-commit by design; deselected in the
        # in-gate run.
        readme = _read(README_FILE)
        assert ("| Tests | %d |" % README_TEST_COUNT) in readme
        assert ("Across %d test files" % README_FILE_COUNT) in readme


# ---------------------------------------------------------------------------
# 17. Iteration log (4 tests; deselected pre-commit per #721)
# ---------------------------------------------------------------------------


class TestTypeDIterationLog1275:
    def test_1275_entry_present_post_sync(self):
        log = _read(LOG_FILE)
        assert "## #1275 Type D" in log

    def test_1274_entry_present(self):
        log = _read(LOG_FILE)
        assert "## #1274 Type C" in log

    def test_rotation_transparency_convention(self):
        log = _read(LOG_FILE)
        assert "### Rotation transparency" in log

    def test_dead_verdict_in_entry(self):
        log = _read(LOG_FILE)
        assert "FIFTH consecutive" in log


# ---------------------------------------------------------------------------
# 18. Staleness pins: #1274's guard lifecycle post-commit
# ---------------------------------------------------------------------------


class TestStalenessPins1275:
    def test_1274_guard_lifecycle_post_commit(self):
        # Post-main-commit form: the no_type_d_1275_in_git_log pin
        # flips BY DESIGN (the #1191-class self-trip: this run's main
        # commit subject carries "Type D #1275"); the remaining 16
        # pins stay green (Type D lands no mechanisms). Deselected
        # pre-commit (all 17 pass pre-commit; the post-commit re-run
        # is the meaningful form).
        res = _class_run(C1274_FILE, "TestGuardLifecycle1274")
        assert res.returncode != 0, res.stdout[-2000:]
        assert "16 passed, 1 failed" in res.stdout, res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 19. Literal discipline per #715
# ---------------------------------------------------------------------------


class TestLiteralDiscipline1275:
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
                     FIFTY_SECOND_MEMBER, FIFTY_THIRD_MEMBER,
                     FIFTY_FOURTH_MEMBER, FIFTY_FIFTH_MEMBER, _T40):
            assert form not in src, form


# ---------------------------------------------------------------------------
# 20. In-flight isolation
# ---------------------------------------------------------------------------


class TestInflightIsolation1275:
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
        # #1024's m846: decision pending; not an assistant repair
        # task. Show-hash form against the main commit's own diff
        # (vacuous pass pre-commit on the 0*40 placeholder; real check
        # post-anchor).
        out = subprocess.run(
            ["git", "show", ANCHORED_SHA, "--stat", "--format="],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert "m846" not in out.stdout

    def test_own_staging_is_explicit_path(self):
        # This run stages only its own paths by explicit path (per
        # the repo-wide traversal lesson): the new test file, the
        # atlantic.yaml meta-key hunk, and the competitor-entities.yaml
        # relationship_types hunk. The docstring carries the
        # explicit-path convention.
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "Explicit-path staging" in src
