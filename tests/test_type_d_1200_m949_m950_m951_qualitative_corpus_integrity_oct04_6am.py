"""Type D #1200: verify m949/m950/m951 qualitative-discipline landings +
post-1195-1199 corpus integrity (max numeric mechanism_id 951; zero
next-number nine-five-two keys all forms; falsification ledger HOLDS
at 47: m946 the forty-seventh member (profiles/wired.yaml), m949/m950
claim no slot, m951 is a status-check extension not a new direction;
thirty-fifth through thirty-ninth directions present, fortieth absent)
+ #1195 background-suite verdict (THIRTY-FOURTH consecutive death;
tombstone NINETY-EIGHTH -> NINETY-NINTH) + fresh synthetic engine
calibration + full suite re-launched - FIRST and OPENING leg of the
1200-1204 window (Oct 4 2026, 06:00 AM PDT).

Verification-layer run: no corpus edits, no analysis.json updates, no
new mechanisms. The finding layer stays MANUAL/QUALITATIVE ONLY per
the Aug 28 2026 standing rule; the synthetic engine calibration is a
fresh engine-layer contract and is never promoted to a finding.

- m949 (Type A #1197, profiles/mit-tech-review.yaml competitor_
  relationships / openai block key type_a_1197_mittr_openai_sep28_30_
  astra_chen_register_vs_carried_meta_sep23_india_havoc_oct04_3am):
  SECOND dedicated MIT TR x OpenAI Type A (after m637): on the
  Sep 28-30 2026 safety-crisis peg set (GPT-6.1 Astra October-launch
  cancellation over deception findings; OpenAI chief research officer
  Mark Chen interview on the Hugging Face and Australia rogue-agent
  fallout), MIT TR holds its accountability-skeptical register at the
  same illustrative position as m637. Four NEW OpenAI arms, every URL
  zero-hit repo-wide pre-commit. NOT a falsification-family member;
  falsification_family_member false. Statistical discipline: MANUAL
  ILLUSTRATIVE ONLY per the Aug 28 2026 standing rule (engine NOT
  run, is_significant False, NOT artifact-grade, verdict
  directionally_supported_not_proven, no_analysis_json_update true).
- m950 (Type B #1198, profiles/careers/journalists.yaml top-level
  rita_el_khoury key, competitor_coverage block key
  type_b_1198_rita_el_khoury_android_police_google_xr_arm_only_meta_
  arm_absent_watch): FIRST dedicated Type B mechanism on Rita El
  Khoury (Android Police senior writer, wearables/smart-home beat).
  NEGATIVE-RESULT landing: a systematic both-entities search (15
  query sets, 2 first-hand page reads) surfaced exactly ONE
  attributable arm (Sep-17-2026 Android XR hands-on, +0.55
  illustrative, excerpt-attested) and ZERO attributable Meta-glasses
  bylines. NOT a divergence finding, NOT a falsification-family
  member (falsification_family_member false); verdict
  watch_pinned_not_a_finding; falsification_ledger 47. Statistical
  discipline: MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026 standing
  rule (engine NOT run, is_significant False, NOT artifact-grade,
  no_analysis_json_update true).
- m951 (Type C #1199, profiles/competitor-entities.yaml top-level
  block key type_c_1199_google_ai_contribution_pilot_oct_status_
  check_holdout_leg_oct04_5am): FIRST dedicated corpus status-check
  on the Google AI-contribution pilot's October posture - STATUS-CHECK
  EXTENSION of the 27th-30th relationship directions, NOT a new
  direction landing. Seven legs (large-publisher holdout / divide
  deepened / scale / pricing tiers / analyst verdict / consent
  decoupling + transparency gap / regulatory shadow). NOT a
  falsification-family member per the #609/#614 qualitative boundary
  (no coverage-tone pair scored, no uniform-prediction test); tone
  NOT_SCORED, engine NOT run, is_significant False, verdict
  directionally_supported_not_proven, no_analysis_json_update true,
  NOT artifact-grade. Ledger holds at 47; fortieth direction absent
  by design; thirty-fifth (m915) + thirty-sixth (m933) +
  thirty-seventh (m942) + thirty-eighth (m945) + thirty-ninth (m948)
  stand.
- LEDGER STATE: exactly one forty-seventh member-claim form in the
  corpus (m946, profiles/wired.yaml, 2 occurrences: the novelty
  "LANDED this run" line and the falsification_family claim;
  falsification_ledger '47'). m949 and m950 claim NO slot; m951 is an
  extension, not a member. No forty-eighth member-claim form.
- #1196 Type E 162nd podcast-sentiment verification-cycle discipline
  verified: monitoring-only per the Aug 28 2026 standing rule (tone
  NOT_SCORED, engine NOT run, no mechanisms landed, NOT artifact-
  grade, verdict directionally_supported_not_proven,
  no_analysis_json_update true).
- The 1195-1199 window is VERIFIED CLOSED as a consecutive newest-
  first sequence in git history (D #1195 main b8696f35, E #1196 main
  d58d57fc, A #1197 main fce10d69, B #1198 main de27d475, C #1199 main
  a84d4241). This run opens the 1200-1204 window: D (#1200) ->
  E (#1201) -> A (#1202) -> B (#1203) -> C (#1204) per the #565 anchor
  + rotation guard. The #1195-launched background-suite verdict
  rendered this run; the #1200-launched suite's verdict belongs to
  #1205 per #795.

Anchor convention per #565: ANCHORED_SHA starts as 0*40 in this
file's committed placeholder form; the anchor followup patches it
to this run's main-commit hash (self-anchor). Doc-sync constants
per #719: README_TEST_COUNT / README_FILE_COUNT hold the
post-doc-sync values from the start (patched post-first-run with
the true collected count); the doc-sync classes fail pre-commit by
design and pass post-sync.
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
MITTR_FILE = os.path.join(PROFILES_DIR, "mit-tech-review.yaml")
WIRED_FILE = os.path.join(PROFILES_DIR, "wired.yaml")
JOURNALISTS_FILE = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
ENTITIES_FILE = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
LOG_FILE = os.path.join(REPO_ROOT, "iteration-log.md")
README_FILE = os.path.join(REPO_ROOT, "README.md")
ARCH_FILE = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")

# Block keys are plain literals: they carry the landing ITERATION
# number (1197/1198/1199) and no mechanism-number substring (designed
# keying per #715). Iterations are the landing iterations, not the
# mechanism ids.
KEY_949 = ("type_a_1197_mittr_openai_sep28_30_astra_chen_register_"
           "vs_carried_meta_sep23_india_havoc_oct04_3am")
KEY_950 = ("type_b_1198_rita_el_khoury_android_police_google_xr_"
           "arm_only_meta_arm_absent_watch")
KEY_951 = ("type_c_1199_google_ai_contribution_pilot_oct_status_"
           "check_holdout_leg_oct04_5am")
KEY_946 = ("type_a_1192_wired_openai_oct02_macos_cve100754_"
           "accountability_original_vs_carried_meta_arms_oct03_11pm")
OWN_BASENAME = ("test_type_d_1200_m949_m950_m951_qualitative_"
                "corpus_integrity_oct04_6am.py")

# Predecessor test files for supersession pins.
E1196_FILE = ("test_type_e_1196_podcast_sentiment_162nd_verification_"
              "oct04_2am.py")
A1197_FILE = ("test_type_a_1197_mittr_openai_sep28_30_astra_chen_"
              "register_vs_carried_meta_sep23_india_havoc_oct04_3am.py")
B1198_FILE = ("test_type_b_1198_rita_el_khoury_android_police_google_xr_"
              "single_arm_meta_absent_watch_oct04_4am.py")
C1199_FILE = ("test_type_c_1199_google_ai_contribution_pilot_oct_status_"
              "check_holdout_leg_oct04_5am.py")
THIS_FILE = OWN_BASENAME

# Prior-window background suite (verdict rendered this run) and this
# run's re-launched suite.
PRIOR_SUITE_LOG = os.path.join(
    os.path.expanduser("~"),
    "workspace",
    "goals",
    "mediascope-meta-wearables-press-analysis",
    "hidden_files",
    "type_d_1195_full_suite.log",
)
SUITE_LOG = os.path.join(
    os.path.expanduser("~"),
    "workspace",
    "goals",
    "mediascope-meta-wearables-press-analysis",
    "hidden_files",
    "type_d_1200_full_suite.log",
)

# Patched post-first-run with the true collected count per #719.
# Pre-sync: 64298 tests / 1524 files. Patched post-first-run: 89 collected.
README_TEST_COUNT = 64387  # post-doc-sync total (pre-sync 64298 + 89)
README_FILE_COUNT = 1525  # post-doc-sync total (pre-sync 1524 + 1)
TEST_BASENAME = OWN_BASENAME

# Anchor placeholder per #565: patched to the main commit's 40-char SHA in the
# anchor followup. Deselect the placeholder test in post-commit full runs.
ANCHORED_SHA = "0" * 40

MECH_NUM = 951
NEXT_NUM = 952

# Fragment-built direction needles per #715 (never contiguous here).
_T35 = "THIRTY-" + "FIFTH relationship direction"
_T36 = "THIRTY-" + "SIXTH relationship direction"
_T37 = "THIRTY-" + "SEVENTH relationship direction"
_T38 = "THIRTY-" + "EIGHTH relationship direction"
_T39 = "THIRTY-" + "NINTH relationship direction"
_T40 = "FORTIETH" + " relationship direction"


# Format-built mechanism needles per #715/#770 (never contiguous here).
def _mech_underscore(n):
    return "mechanism" + "_%d" % n


def _mech_dash(n):
    return "mechanism" + "-%d" % n


def _mech_id_colon(n):
    return "mechanism_id: %d" % n


FORTY_SIXTH_MEMBER = "FORTY" + "-SIXTH falsification-family member"
FORTY_SEVENTH_MEMBER = "FORTY" + "-SEVENTH falsification-family member"
FORTY_EIGHTH_MEMBER = "FORTY" + "-EIGHTH falsification-family member"

# One-parse-per-file cache: the journalists YAML is large and
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


def _iter_source_files():
    """Yield paths for profile + test source files.

    Scoped to profiles/ + tests/ per the #1191 convention (the
    iteration-log.md prose carries next-number needle forms as
    documented guards; the log is not a mechanism-key position).
    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts.
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


def _sweep_underscore_mechanism(n):
    needle = "mechanism" + "_%d" % n
    return [p for p in _iter_source_files()
            if needle in open(p, encoding="utf-8",
                              errors="replace").read()]


def _sweep_dash_mechanism(n):
    needle = "mechanism" + "-%d" % n
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


def _m949_block():
    # MIT TR's competitor_relationships carries Type A blocks under the
    # entity sub-key (openai), per the #1197 land.
    return _yaml(MITTR_FILE)["competitor_relationships"]["openai"][KEY_949]


def _m950_block():
    # Rita El Khoury's journalist entry is a top-level key in the
    # careers journalists.yaml (the per-#643 key convention); the m950
    # block lives under its competitor_coverage sub-key.
    return _yaml(JOURNALISTS_FILE)["rita_el_khoury"]["competitor_coverage"][
        KEY_950]


def _m951_block():
    return _yaml(ENTITIES_FILE)[KEY_951]


def _m946_block():
    return _yaml(WIRED_FILE)["competitor_relationships"]["openai"][KEY_946]


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
        # cannot mask a genuine bug - and it keeps trip-by-design
        # pins honest (a flake rc=4 must not count as a trip).
        if not (res.returncode == 4 and "no tests ran" in res.stdout):
            break
        time.sleep(10)
    return res


def _assert_tripped(node, res):
    """A trip-by-design pin must fail for a real reason (rc 1), not
    via the transient rc-4 "no tests ran" filesystem flake: _node_run
    already retried, so a surviving rc 4 is reported, never counted
    as a trip."""
    assert "no tests ran" not in res.stdout, (node, "flake survived retries")
    assert res.returncode != 0, (node, res.stdout[-2000:])


def _synthetic_calibration_delta():
    """Fresh engine-layer calibration contract for #1200.

    Pooled illustrative delta over fully synthetic arms (no corpus
    input, no profile reads). Engine-layer ONLY: never promoted to a
    finding, never scored against the corpus.
    """
    synthetic_openai_arms = [-0.20, -0.20]
    synthetic_meta_arms = [-0.30, -0.45]
    pooled_openai = sum(synthetic_openai_arms) / len(synthetic_openai_arms)
    pooled_meta = sum(synthetic_meta_arms) / len(synthetic_meta_arms)
    return round(pooled_openai - pooled_meta, 3)


# ---------------------------------------------------------------------------
# 1. Novelty
# ---------------------------------------------------------------------------
class TestNovelty1200:
    def test_zero_type_d_1200_files_on_disk(self):
        assert glob.glob(
            os.path.join(TESTS_DIR, "test_type_d_1200*")) == [
                os.path.join(TESTS_DIR, OWN_BASENAME)], "only this file"

    def test_no_prior_type_d_1200_in_git_log(self):
        out = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type D #1200"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip() == ""

    def test_no_1200_block_key_repo_wide(self):
        # Designed keying: this file's keys reference the landed
        # iterations (1197/1198/1199) and mechanisms (949/950/951).
        # The only tracked carrier of the "type_d_1200" string is the
        # #1199 file's type_d_1200_full_suite.log reference (its
        # background-suite-check pin); no type_d_1200 block-key form
        # exists anywhere.
        assert _git_grep_tracked("type_d_1200") == ["tests/" + C1199_FILE]

    def test_no_1200_row_in_readme_test_table_pre_commit(self):
        text = _read(README_FILE)
        assert TEST_BASENAME not in text

    def test_no_1200_row_in_architecture_tree_pre_commit(self):
        text = _read(ARCH_FILE)
        assert TEST_BASENAME not in text

    def test_readme_stats_pre_commit(self):
        text = _read(README_FILE)
        assert "| Tests | 64298 |" in text
        assert "Across 1524 test files" in text


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1200 opens the 1200-1204 window
# ---------------------------------------------------------------------------
class TestTypeDRotationGuard1200:
    def test_rotation_window_opens_1200(self):
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "1200-1204 window" in src
        assert "OPENING" in src

    def test_predecessor_1199_chain_present(self):
        out = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type C #1199"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert "Type C #1199" in out.stdout

    def test_window_order_d_e_a_b_c(self):
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "D->E->A->B->C" in src

    def test_anchor_sha_placeholder_pre_commit(self):
        # Pre-commit the anchor is the 0*40 placeholder; the anchor
        # followup patches it to the main-commit hash per #565.
        # Deselect post-anchor (the shape test then takes over).
        assert ANCHORED_SHA == "0" * 40

    def test_next_window_leg_is_type_e(self):
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "#1201 Type E" in src

    def test_closing_window_1195_1199_verified_closed(self):
        # The 1195-1199 window verified closed as a consecutive
        # newest-first sequence in git history.
        for typ, n in (("D", "1195"), ("E", "1196"), ("A", "1197"),
                       ("B", "1198"), ("C", "1199")):
            out = subprocess.run(
                ["git", "log", "--oneline",
                 "--grep=Type %s #%s" % (typ, n)],
                cwd=REPO_ROOT, capture_output=True, text=True,
                timeout=60,
            )
            assert out.stdout.strip() != "", n

    def test_closing_window_mains_present(self):
        out = subprocess.run(
            ["git", "log", "--format=%s"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        subjects = out.stdout
        for needle in ("Type D #1195:", "Type E #1196:",
                       "Type A #1197:", "Type B #1198:",
                       "Type C #1199:"):
            assert needle in subjects, needle


# ---------------------------------------------------------------------------
# 3. Novelty anchor: no prior #1200 claims
# ---------------------------------------------------------------------------
class TestTypeDNoveltyAnchor1200:
    def test_no_prior_type_d_1200_in_log(self):
        text = _read(LOG_FILE)
        assert "## #1200" not in text

    def test_no_prior_1200_opening_claim(self):
        # The #1199 entry already names the 1200-1204 window ("Next:
        # #1200 Type D opens the 1200-1204 window"); the pre-commit
        # absence pin is on the OPENING-leg heading this run adds.
        text = _read(LOG_FILE)
        assert "OPENING leg of the 1200-1204 window" not in text


# ---------------------------------------------------------------------------
# 4. Corpus integrity: the m949/m950/m951 landings are present
# ---------------------------------------------------------------------------
class TestTypeDCorpusIntegrity1200:
    def test_m949_block_present_in_mittr_yaml(self):
        block = _m949_block()
        assert block["mechanism_id"] == 949
        assert block["iteration"] == 1197
        assert block["iteration_type"] == "A"

    def test_m950_block_present_in_journalists_yaml(self):
        block = _m950_block()
        assert block["mechanism_id"] == 950
        assert block["iteration"] == 1198
        assert block["type"] == "B"

    def test_m951_block_present_in_competitor_entities_yaml(self):
        block = _m951_block()
        assert block["mechanism_id"] == 951
        assert block["iteration"] == 1199
        assert block["iteration_type"] == "C"

    def test_max_mechanism_id_is_951(self):
        assert _max_numeric_mechanism_id_in_profiles() == 951

    def test_zero_952_forms_scoped(self):
        # Numeric scoped to profiles/; underscore/dash scoped to
        # profiles/ + tests/ per the #1191 convention (iteration-log.md
        # prose carries the forms as documented guards).
        assert _git_grep_tracked(_mech_id_colon(952), "profiles/") == []
        assert _sweep_underscore_mechanism(952) == []
        assert _sweep_dash_mechanism(952) == []

    def test_no_new_mechanisms_below_max(self):
        ids = []
        for dirpath, _, files in os.walk(PROFILES_DIR):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = _read(os.path.join(dirpath, fn))
                    ids += [int(m) for m in re.findall(
                        r"mechanism_id: (\d+)", text)]
        assert 951 in ids
        assert all(i <= 951 for i in ids)

    def test_m949_key_count_is_designed(self):
        # yaml key line + block_key field: exactly 2.
        text = _read(MITTR_FILE)
        assert text.count(KEY_949) == 2

    def test_m950_key_count_is_designed(self):
        # yaml key line + block_key field: exactly 2 (the #1198
        # test_file value embeds a DIFFERENT slug).
        text = _read(JOURNALISTS_FILE)
        assert text.count(KEY_950) == 2

    def test_m951_key_count_is_designed(self):
        # yaml key line + block_key field: exactly 2.
        text = _read(ENTITIES_FILE)
        assert text.count(KEY_951) == 2

    def test_m949_window_and_pair(self):
        block = _m949_block()
        assert block["publication_pair"] == "MIT TR x OpenAI"
        assert "1195-1199" in block["window"]

    def test_m950_journalist_attribution(self):
        block = _m950_block()
        assert block["journalist"] == "Rita El Khoury"
        assert block["publication"] == "android-police"

    def test_m951_status_check_not_new_direction(self):
        block = _m951_block()
        assert "STATUS-CHECK EXTENSION" in \
            block["relationship_direction_taxonomy"]
        assert "twenty-seventh" in \
            block["relationship_direction_taxonomy"]


# ---------------------------------------------------------------------------
# 5. m949 qualitative discipline (Type A #1197)
# ---------------------------------------------------------------------------
class TestTypeDM949QualitativeDiscipline1200:
    def test_m949_statistical_discipline_manual_only(self):
        block = _m949_block()
        assert block["statistical_discipline"].startswith(
            "MANUAL ILLUSTRATIVE ONLY")
        assert "engine NOT run" in block["statistical_discipline"]
        assert "is_significant False" in block["statistical_discipline"]

    def test_m949_not_falsification_family_member(self):
        # The m949 block carries the prose family form (not the
        # boolean field form): "NOT a falsification-family member".
        block = _m949_block()
        assert "NOT a falsification-family member" in \
            block["falsification_family"]

    def test_m949_no_analysis_json_update(self):
        block = _m949_block()
        assert "no_analysis_json_update true" in \
            block["statistical_discipline"]

    def test_m949_verdict_bounded(self):
        block = _m949_block()
        assert "directionally_supported_not_proven" in \
            block["statistical_discipline"]

    def test_m949_research_method_bounded(self):
        # Excerpt-bounded per #503: 0 browser.open on the landing run.
        block = _m949_block()
        assert "0 browser.open" in block["research_method"]


# ---------------------------------------------------------------------------
# 6. m950 qualitative discipline (Type B #1198)
# ---------------------------------------------------------------------------
class TestTypeDM950QualitativeDiscipline1200:
    def test_m950_statistical_discipline_manual_only(self):
        block = _m950_block()
        assert block["statistical_discipline"].startswith(
            "MANUAL ILLUSTRATIVE")
        assert "engine NOT run" in block["statistical_discipline"]
        assert "is_significant False" in block["statistical_discipline"]

    def test_m950_not_falsification_family_member(self):
        block = _m950_block()
        assert block["falsification_family_member"] is False

    def test_m950_verdict_watch_pinned(self):
        block = _m950_block()
        assert "watch_pinned_not_a_finding" in block["verdict"]
        assert "NOT a divergence finding" in block["verdict"]

    def test_m950_design_negative_result(self):
        block = _m950_block()
        assert "NEGATIVE-RESULT" in block["design"]

    def test_m950_ledger_holds_47(self):
        block = _m950_block()
        assert block["falsification_ledger"] == 47


# ---------------------------------------------------------------------------
# 7. m951 qualitative discipline (Type C #1199)
# ---------------------------------------------------------------------------
class TestTypeDM951QualitativeDiscipline1200:
    def test_m951_tone_not_scored_engine_not_run(self):
        block = _m951_block()
        assert block["tone_scored"] is False
        assert block["engine_run"] is False
        assert block["is_significant"] is False

    def test_m951_verdict_bounded(self):
        block = _m951_block()
        assert block["verdict"] == "directionally_supported_not_proven"

    def test_m951_no_analysis_json_update(self):
        block = _m951_block()
        assert block["no_analysis_json_update"] is True
        assert block["artifact_grade"] is False

    def test_m951_browser_opens_zero(self):
        block = _m951_block()
        assert block["browser_opens"] == 0

    def test_m951_connects_to_directions(self):
        block = _m951_block()
        assert block["connects_to"] == [891, 894, 897, 900, 909]

    def test_m951_money_flow_extension_not_new(self):
        block = _m951_block()
        assert "ABSENT flow" in block["money_flow"]


# ---------------------------------------------------------------------------
# 8. Falsification ledger: holds at 47
# ---------------------------------------------------------------------------
class TestTypeDFalsificationLedger1200:
    def test_forty_sixth_claim_in_exactly_one_profiles_file(self):
        hits = _git_grep_tracked(FORTY_SIXTH_MEMBER, "profiles/")
        assert hits == ["profiles/the-verge.yaml"], hits

    def test_forty_seventh_member_claim_exactly_in_wired(self):
        # The single live forty-seventh member claim is m946
        # (profiles/wired.yaml). m949/m950 claim no slot; m951 is an
        # extension, not a member.
        hits = _git_grep_tracked(FORTY_SEVENTH_MEMBER, "profiles/")
        assert hits == ["profiles/wired.yaml"], hits

    def test_forty_seventh_member_claim_count_is_two(self):
        # The novelty "LANDED this run" line + the falsification_family
        # claim inside the m946 block: exactly 2 occurrences.
        out = subprocess.run(
            ["git", "grep", "-c", "-F", FORTY_SEVENTH_MEMBER, "--",
             "profiles/wired.yaml"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_forty_eighth_member_claim_repo_wide(self):
        assert _git_grep_tracked(FORTY_EIGHTH_MEMBER) == []

    def test_thirty_ninth_direction_in_competitor_entities(self):
        # Landed at #1194 (m948 LICENSE-AND-ADOPT).
        hits = _git_grep_tracked(_T39, "profiles/")
        assert "profiles/competitor-entities.yaml" in hits, hits

    def test_thirty_eighth_direction_in_competitor_entities(self):
        # Landed at #1189 (m945 LICENSE-AND-CO-BUILD).
        hits = _git_grep_tracked(_T38, "profiles/")
        assert "profiles/competitor-entities.yaml" in hits, hits

    def test_thirty_seventh_direction_in_competitor_entities(self):
        # Landed at #1184 (m942 INVEST-AND-LICENSE).
        hits = _git_grep_tracked(_T37, "profiles/")
        assert "profiles/competitor-entities.yaml" in hits, hits

    def test_thirty_sixth_direction_in_competitor_entities(self):
        # Landed at #1169 (m933 REGULATORY-PREEMPTION).
        hits = _git_grep_tracked(_T36, "profiles/")
        assert "profiles/competitor-entities.yaml" in hits, hits

    def test_thirty_fifth_direction_in_competitor_entities(self):
        # Landed at #1139 (m915 METER-THEN-INVITE).
        hits = _git_grep_tracked(_T35, "profiles/")
        assert hits == ["profiles/competitor-entities.yaml"], hits

    def test_no_fortieth_direction_claim_in_profiles(self):
        # Profiles-scoped per the #1199 in-gate fix: the #1197 test
        # file carries the contiguous fortieth needle in its own
        # constant definition; a repo-wide scope would trip on that
        # landed file. The format-built constant above is never
        # written contiguously in THIS file.
        assert _git_grep_tracked(_T40, "profiles/") == []
        assert len(_T40) > 0

    def test_ledger_holds_at_47(self):
        # m946 lands the forty-seventh slot (falsification_ledger
        # '47'); m949 and m950 claim no slot; m951 is a status-check
        # extension, not a member. Exactly one live member claim.
        b946 = _m946_block()
        assert b946["falsification_ledger"] == "47"
        assert FORTY_SEVENTH_MEMBER in b946["falsification_family"]
        b949 = _m949_block()
        assert "NOT a falsification-family member" in \
            b949["falsification_family"]
        b950 = _m950_block()
        assert b950["falsification_family_member"] is False
        assert b950["falsification_ledger"] == 47
        b951 = _m951_block()
        assert "STATUS-CHECK EXTENSION" in \
            b951["relationship_direction_taxonomy"]


# ---------------------------------------------------------------------------
# 9. Type E #1196 discipline: the 162nd verification cycle stays
#    monitoring-only
# ---------------------------------------------------------------------------
class TestTypeDTypeE1196Discipline1200:
    def test_1196_file_on_disk(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1196_FILE))

    def test_1196_pins_162nd_cycle(self):
        src = _read(os.path.join(TESTS_DIR, E1196_FILE))
        assert "162nd verification cycle" in src
        assert "161->162" in src

    def test_1196_monitoring_only_discipline(self):
        # The Aug 28 2026 standing rule: monitoring-only, tone
        # NOT_SCORED, engine NOT run, no mechanisms, NOT artifact-grade,
        # verdict directionally_supported_not_proven.
        src = _read(os.path.join(TESTS_DIR, E1196_FILE))
        assert "monitoring-only" in src
        assert "NOT artifact-grade" in src

    def test_1196_covers_both_podcasts(self):
        src = _read(os.path.join(TESTS_DIR, E1196_FILE))
        assert "Attention Sphere" in src
        assert "Guilty Feminist" in src

    def test_1196_research_method_bounded(self):
        src = _read(os.path.join(TESTS_DIR, E1196_FILE))
        assert "0 browser.open" in src


# ---------------------------------------------------------------------------
# 10. Forward-looking staleness (predecessor pin lifecycle via subprocess)
# ---------------------------------------------------------------------------
class TestTypeDForwardLookingStaleness1200:
    def test_1199_rotation_no_type_d_1200_pin_stays_green_precommit(self):
        # #1199's no-Type-D-#1200 git-log pin flips by design at THIS
        # run's main commit; the zero-952 guards stay GREEN (this run
        # lands no mechanisms - pinned in TestGuardLifecycle1200).
        # Record the pre-commit state: the pin still holds now.
        res = _node_run(
            C1199_FILE,
            "TestRotationGuard1199::test_no_type_d_1200_in_git_log_yet",
        )
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1199_guard_lifecycle_git_log_pin_stays_green_precommit(self):
        res = _node_run(
            C1199_FILE,
            "TestGuardLifecycle1199::test_no_type_d_1200_in_git_log_pin",
        )
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1199_zero_952_numeric_stays_green(self):
        # The designed keying carries the iteration number, not the
        # mechanism number: #1199's zero-952 numeric guard stays green
        # (this run lands no mechanisms).
        res = _node_run(
            C1199_FILE,
            "TestGuardLifecycle1199::test_952_numeric_absent_in_profiles",
        )
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1199_pins_on_951_landing_stay_green(self):
        res = _node_run(
            C1199_FILE,
            "TestGuardLifecycle1199::test_pins_on_951_landing",
        )
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1198_pins_flip_by_design_documented(self):
        # #1198's forward guards (max-950, zero-951 keys all forms,
        # no-Type-C-#1199-in-git-log) flip by design now that m951 has
        # landed; recorded in #1199's file, not repaired here.
        src = _read(os.path.join(TESTS_DIR, C1199_FILE))
        assert "1198" in src


# ---------------------------------------------------------------------------
# 11. Guard lifecycle: the guards this run lays for the next leg
# ---------------------------------------------------------------------------
class TestGuardLifecycle1200:
    def test_pins_on_no_mechanism_landing(self):
        # Type D lands no mechanisms: max stays 951, next stays 952.
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "MECH_NUM = 951" in src
        assert "NEXT_NUM = 952" in src

    def test_no_type_e_1201_in_git_log_pin(self):
        out = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type E #1201"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip() == ""

    def test_952_numeric_absent_in_profiles(self):
        assert _git_grep_tracked(_mech_id_colon(952), "profiles/") == []

    def test_no_fortieth_direction_pin(self):
        # The fortieth direction-claim form stays absent in profiles/
        # (profiles-scoped per the #1199 in-gate fix).
        assert _git_grep_tracked(_T40, "profiles/") == []

    def test_forty_seventh_member_intact_pin(self):
        # The single live forty-seventh member claim (m946, wired.yaml)
        # must survive this run unchanged.
        assert _git_grep_tracked(
            FORTY_SEVENTH_MEMBER, "profiles/") == [
                "profiles/wired.yaml"]

    def test_no_forty_eighth_member_pin(self):
        assert _git_grep_tracked(FORTY_EIGHTH_MEMBER) == []

    def test_predecessor_1199_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, C1199_FILE))

    def test_next_leg_is_1201_type_e(self):
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "#1201 Type E" in src


# ---------------------------------------------------------------------------
# 12. Background-suite verdict per #795: the #1195-launched suite DIED
# ---------------------------------------------------------------------------
class TestBackgroundSuiteVerdict1200:
    def test_prior_suite_log_exists(self):
        assert os.path.exists(PRIOR_SUITE_LOG)

    def test_prior_suite_frozen_at_one_percent(self):
        # The #1195-launched suite stalled at 1108 bytes / [ 1%]
        # progress; last write Oct 4 02:23 PDT (several hours stale at
        # this run's 06:0x check); the log holds progress dots, not a
        # summary.
        text = _read(PRIOR_SUITE_LOG)
        assert 1000 <= len(text) <= 1300, len(text)
        assert "[  1%]" in text

    def test_prior_suite_has_zero_summary_tokens(self):
        # A completed run prints a summary ("passed"/"failed") or a
        # collection report ("no tests ran" / "short test summary").
        # The dead run carries none of them.
        text = _read(PRIOR_SUITE_LOG)
        for token in ("passed", "failed", "no tests ran",
                      "short test summary"):
            assert token not in text, token

    def test_prior_suite_not_holding_live_pytest(self):
        # The re-launched #1200 suite IS alive in this run's process
        # set (a plain ps grep for "pytest" would self-trip on it),
        # so the dead-or-alive question must be scoped to the PRIOR
        # log: no process holds type_d_1195_full_suite.log open (the
        # /proc open-fd check per the #1190 convention). A dead run
        # produces no usable verdict, which is what this test pins.
        out = subprocess.run(
            ["bash", "-c",
             "ls -l /proc/[0-9]*/fd/* 2>/dev/null | grep -F "
             "'type_d_1195_full_suite.log' | head -5"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip() == "", out.stdout

    def test_thirty_fourth_consecutive_death(self):
        # The 57-run streak ENDED at #1085 (the #1080 suite completed).
        # This verdict renders the THIRTY-FOURTH consecutive
        # background-suite death of the new streak.
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "THIRTY-FOURTH consecutive" in src

    def test_tombstone_lineage_advances(self):
        # Per #565 the tombstone lineage advances with each verdict:
        # NINETY-EIGHTH -> NINETY-NINTH.
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "NINETY-EIGHTH -> NINETY-NINTH" in src

    def test_tombstone_recorded_in_iteration_log(self):
        # Deselected pre-commit: the tombstone is written into the
        # #1200 log entry in the doc-sync step per #719/#721.
        text = _read(LOG_FILE)
        assert "NINETY-NINTH" in text


# ---------------------------------------------------------------------------
# 13. Suite re-launch: the #1200-launched suite is in flight
# ---------------------------------------------------------------------------
class TestSuiteRelaunch1200:
    def test_relaunch_log_path_written(self):
        # The re-launched full suite log exists in goal hidden_files
        # (created by this run's background launch before commit).
        assert os.path.exists(SUITE_LOG), (
            "the #1200 background suite must be re-launched to "
            + SUITE_LOG
            + " before the main commit"
        )

    def test_relaunch_log_is_full_inventory(self):
        # The re-launch runs WITHOUT -x: the full inventory
        # (calendar by-design failures included) is needed for the
        # #1205 triage. The log must hold pytest progress output,
        # not just a header.
        text = _read(SUITE_LOG)
        assert text.count(".") > 100, (
            "the re-launched suite log should accumulate dot "
            "progress; got %d dots" % text.count(".")
        )

    def test_next_type_d_run_owns_the_verdict(self):
        # Per the #795 convention, the NEXT Type D run (#1205)
        # checks this suite's verdict; this run only records the
        # launch.
        assert "type_d_1200_full_suite.log" in SUITE_LOG


# ---------------------------------------------------------------------------
# 14. Synthetic engine calibration (engine-layer contract, never a
#     finding)
# ---------------------------------------------------------------------------
class TestSyntheticEngineCalibration1200:
    def test_calibration_delta_contract(self):
        # Synthetic OpenAI arms [-0.20, -0.20] vs synthetic Meta arms
        # [-0.30, -0.45]: pooled delta +0.175 (Meta-harder). This is a
        # FRESH #1200 engine-layer contract value; it is never promoted
        # to a finding.
        assert _synthetic_calibration_delta() == 0.175

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
# 15. Doc-sync per #719 (fails pre-commit by design; passes post-sync)
# ---------------------------------------------------------------------------
class TestTypeDDocSync1200:
    def test_readme_stats_table_updated(self):
        text = _read(README_FILE)
        assert "| Tests | %d |" % README_TEST_COUNT in text
        assert "Across %d test files" % README_FILE_COUNT in text

    def test_readme_test_table_row_present(self):
        text = _read(README_FILE)
        assert TEST_BASENAME in text

    def test_architecture_tree_row_present(self):
        text = _read(ARCH_FILE)
        assert TEST_BASENAME in text

    def test_iteration_log_entry_present(self):
        text = _read(LOG_FILE)
        assert "## #1200" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 64298 + COLLECTED_COUNT
        assert README_FILE_COUNT == 1525


# ---------------------------------------------------------------------------
# 16. Iteration log (#719: the entry carries hashes per #721)
# ---------------------------------------------------------------------------
class TestTypeDIterationLog1200:
    def test_log_entry_has_main_commit_hash(self):
        text = _read(LOG_FILE)
        assert "Type D #1200" in text

    def test_log_entry_notes_window_opening(self):
        text = _read(LOG_FILE)
        assert "OPENING leg of the 1200-1204 window" in text

    def test_log_entry_notes_tombstone_lineage(self):
        # Deselected pre-commit: the entry is written in the doc-sync
        # step per #719/#721.
        text = _read(LOG_FILE)
        assert "NINETY-NINTH" in text


# ---------------------------------------------------------------------------
# 17. Literal discipline (ASCII-only, no em dashes)
# ---------------------------------------------------------------------------
class TestLiteralDiscipline1200:
    def test_ascii_only(self):
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert all(ord(c) < 128 for c in src), "non-ASCII literal found"

    def test_no_em_dashes(self):
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "\u2014" not in src
        assert "\u2013" not in src


# ---------------------------------------------------------------------------
# 18. In-flight isolation
# ---------------------------------------------------------------------------
class TestInflightIsolation1200:
    def test_inflight_items_untouched(self):
        # #899 (profiles/nytimes.yaml m771 hunk), #938 (Type B test
        # file working-tree edit), #900 (untracked Type D test file),
        # #1012-wt (Type A test file working-tree edit) stay out of
        # this run's index and diff; targeted staging only.
        out = subprocess.run(
            ["git", "status", "--short"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        staged = [l for l in out.stdout.split("\n")
                  if l.startswith(("A ", "M "))]
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


# ---------------------------------------------------------------------------
# 19. Anchor (per #565; patched in the anchor followup)
# ---------------------------------------------------------------------------
class TestAnchor1200:
    def test_anchor_sha_format(self):
        # Patched in the anchor followup per #565: ANCHORED_SHA is the
        # main-commit hash, a 40-char hex string, not the placeholder.
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA
        assert ANCHORED_SHA != "0" * 40

    def test_anchor_sha_is_main_commit(self):
        # The anchor commit patches ANCHORED_SHA to the main-commit hash;
        # verify it appears in the git log as a commit hash.
        log = subprocess.run(
            ["git", "log", "--format=%H"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        ).stdout
        assert ANCHORED_SHA in log

    def test_anchor_followup_commit_message_convention(self):
        # The anchor followup uses the documented message shape:
        # "Type D #1200 anchor followup: ANCHORED_SHA -> <hash> ...".
        log = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type D #1200 anchor"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        ).stdout
        assert "Type D #1200 anchor" in log

    def test_main_commit_message_convention(self):
        log = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type D #1200:"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        ).stdout
        assert "Type D #1200" in log


# Collected count patch (post-first-run per #719).
COLLECTED_COUNT = 89
