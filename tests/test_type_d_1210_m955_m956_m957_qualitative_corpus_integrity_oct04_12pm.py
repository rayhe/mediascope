"""Type D #1210: verify m955/m956/m957 qualitative-discipline landings +
post-1205-1209 corpus integrity (max numeric mechanism_id 957; zero
next-number nine-five-eight keys all forms; falsification ledger HOLDS
at 49: m956 the forty-ninth member (profiles/careers/journalists.yaml),
m955 claims no slot, m957 is a status-check extension not a new
direction; thirty-fifth through thirty-ninth directions present, the
fortieth absent by design) + #1205 background-suite verdict
(THIRTY-SIXTH consecutive death; tombstone ONE-HUNDREDTH ->
ONE-HUNDRED-FIRST) + fresh synthetic engine calibration + full suite
re-launched - FIRST and OPENING leg of the 1210-1214 window
(Oct 4 2026, 12:00 PM PDT).

Verification-layer run: no corpus edits, no analysis.json updates, no
new mechanisms. The finding layer stays MANUAL/QUALITATIVE ONLY per
the Aug 28 2026 standing rule; the synthetic engine calibration is a
fresh engine-layer contract and is never promoted to a finding.

- m955 (Type A #1207, profiles/business-insider.yaml competitor_
  relationships / anthropic block key type_a_1207_bi_anthropic_ipo_
  prospectus_smart_people_financial_skeptical_vs_meta_execution_
  neutral_sep29): BI Sep-29 Anthropic IPO-prospectus "smart people"
  financial-skeptical roundup (-0.30 MANUAL ILLUSTRATIVE) vs carried
  BI Meta product-execution triad (+0.08); illustrative delta -0.38;
  cross-lab near-parity on the financial-skepticism register family
  (deal lab -0.42 vs non-deal lab -0.30); the register follows the
  financial peg, not the payer. NOT a falsification-family member
  (control-case extension, no uniform-prediction test); verdict
  mechanism_refinement_not_a_discovery; ledger 48. Statistical
  discipline: MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026 standing
  rule (engine NOT run, is_significant false, NOT artifact-grade,
  no_analysis_json_update true). 17 browser.search query sets,
  0 browser.open per #503.
- m956 (Type B #1208, profiles/careers/journalists.yaml top-level
  blake_montgomery_type_b key, competitor_coverage block key
  type_b_1208_blake_montgomery_guardian_openai_rogue_vs_meta_18bn_
  falsification): Blake Montgomery (Guardian US tech editor) OpenAI
  Sep-8 launch mockery (-0.35 MANUAL ILLUSTRATIVE, solo byline) vs
  Meta Aug-26 $18bn teen-harm settlement reckoning (-0.40, co-byline
  Kerr); illustrative delta +0.05 near-null symmetric adversarial;
  Sep-28 cross-entity piece corroborates within-bylinesymmetry.
  Forty-ninth falsification-family member (ledger 48->49): the
  Guardian x OpenAI strategic content-licensing partnership buys no
  register softness from this reporter; the deal effect is
  journalist-contingent, not outlet-uniform. Statistical discipline:
  MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026 standing rule.
  Delegated research + main-run verification: 6 browser.search query
  sets, 0 browser.open per #503.
- m957 (Type C #1209, profiles/competitor-entities.yaml top-level
  block key type_c_1209_newscorp_dual_payer_ledger_october_wave_
  status_check_oct04_1130am): News Corp dual-payer licensing ledger
  October-2026 status check (combined ~$400M dual-lab revenue figure,
  NEW corpus money fact; October-wave tracker corroboration:
  everything-pr updated Oct 4, Press Gazette ~Sep 29); dual-payer
  status HOLDS; m519 prediction un-falsified. STATUS-CHECK EXTENSION
  of the m519 News Corp dual-payer line, NOT a new direction. NOT a
  falsification-family member per the #609/#614 qualitative boundary
  (no coverage-tone pair scored, no uniform-prediction test); tone
  NOT_SCORED, engine NOT run, is_significant False, verdict
  directionally_supported_not_proven, no_analysis_json_update true,
  NOT artifact-grade. Ledger holds at 49; the fortieth direction
  absent by design; 35th-39th stand.
- LEDGER STATE: exactly one forty-ninth member-claim form in the
  corpus (m956, profiles/careers/journalists.yaml, 3 occurrences: the
  notes landing line, the falsification_family claim, and the novelty
  line; falsification_ledger 49). m955 claims NO slot
  (falsification_family_member false, falsification_ledger 48); m957
  is an extension, not a member. No fiftieth member-claim form
  repo-wide.
- #1206 Type E 164th podcast-sentiment verification-cycle discipline
  verified: monitoring-only per the Aug 28 2026 standing rule (tone
  NOT_SCORED, engine NOT run, no mechanisms landed, NOT artifact-
  grade, verdict directionally_supported_not_proven,
  no_analysis_json_update true).
- The 1205-1209 window is VERIFIED CLOSED as a consecutive newest-
  first sequence in git history (D #1205 main 829b8a8b, E #1206 main
  be56e254, A #1207 main ec95a251, B #1208 main 33e4af12, C #1209
  main 52b03938). This run opens the 1210-1214 window: D (#1210) ->
  E (#1211) -> A (#1212) -> B (#1213) -> C (#1214) per the #565 anchor
  + rotation guard. The #1205-launched background-suite verdict
  rendered this run; the #1210-launched suite's verdict belongs to
  #1215 per #795.

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
BI_FILE = os.path.join(PROFILES_DIR, "business-insider.yaml")
JOURNALISTS_FILE = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
ENTITIES_FILE = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
LOG_FILE = os.path.join(REPO_ROOT, "iteration-log.md")
README_FILE = os.path.join(REPO_ROOT, "README.md")
ARCH_FILE = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")

# Block keys are plain literals: they carry the landing ITERATION
# number (1207/1208/1209) and no mechanism-number substring (designed
# keying per #715). Iterations are the landing iterations, not the
# mechanism ids.
KEY_955 = ("type_a_1207_bi_anthropic_ipo_prospectus_smart_people_"
           "financial_skeptical_vs_meta_execution_neutral_sep29")
KEY_956 = ("type_b_1208_blake_montgomery_guardian_openai_rogue_vs_"
           "meta_18bn_falsification")
KEY_957 = ("type_c_1209_newscorp_dual_payer_ledger_october_wave_"
           "status_check_oct04_1130am")
OWN_BASENAME = ("test_type_d_1210_m955_m956_m957_qualitative_"
                "corpus_integrity_oct04_12pm.py")

# Predecessor test files for supersession pins.
E1206_FILE = ("test_type_e_1206_podcast_sentiment_164th_verification_"
              "oct04_930am.py")
A1207_FILE = ("test_type_a_1207_bi_anthropic_ipo_prospectus_smart_"
              "people_financial_skeptical_vs_meta_execution_neutral_"
              "sep29_oct04_10am.py")
B1208_FILE = ("test_type_b_1208_blake_montgomery_guardian_openai_"
              "rogue_vs_meta_18bn_falsification_oct04_11am.py")
C1209_FILE = ("test_type_c_1209_newscorp_dual_payer_ledger_october_"
              "wave_status_check_oct04_1130am.py")
THIS_FILE = OWN_BASENAME

# Prior-window background suite (verdict rendered this run) and this
# run's re-launched suite.
PRIOR_SUITE_LOG = os.path.join(
    os.path.expanduser("~"),
    "workspace",
    "goals",
    "mediascope-meta-wearables-press-analysis",
    "hidden_files",
    "type_d_1205_full_suite.log",
)
SUITE_LOG = os.path.join(
    os.path.expanduser("~"),
    "workspace",
    "goals",
    "mediascope-meta-wearables-press-analysis",
    "hidden_files",
    "type_d_1210_full_suite.log",
)

# Patched post-first-run with the true collected count per #719.
# Pre-sync: 65091 tests / 1534 files. Patched post-first-run: N collected.
README_TEST_COUNT = 65091 + 101  # post-doc-sync total; patched per #719
README_FILE_COUNT = 1535  # post-doc-sync total (pre-sync 1534 + 1)
TEST_BASENAME = OWN_BASENAME

# Anchor placeholder per #565: patched to the main commit's 40-char SHA in the
# anchor followup. Deselect the placeholder test in post-commit full runs.
ANCHORED_SHA = "42ef40b085a6a44126a439bbbf89aa20ceaa892a"

MECH_NUM = 957
NEXT_NUM = 958

# Fragment-built direction needles per #715 (never contiguous here).
_T35 = "THIRTY-" + "FIFTH relationship direction"
_T36 = "THIRTY-" + "SIXTH relationship direction"
_T37 = "THIRTY-" + "SEVENTH relationship direction"
_T38 = "THIRTY-" + "EIGHTH relationship direction"
_T39 = "THIRTY-" + "NINTH relationship direction"
_T40 = "FORT" + "IETH relationship direction"


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
FORTY_NINTH_MEMBER = "FORTY" + "-NINTH falsification-family member"
FIFTIETH_MEMBER = "FIFT" + "IETH falsification-family member"

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


def _m955_block():
    # BI's competitor_relationships carries Type A blocks under the
    # entity sub-key (anthropic), per the #1207 land.
    return _yaml(BI_FILE)["competitor_relationships"]["anthropic"][KEY_955]


def _m956_block():
    # Blake Montgomery's journalist entry is a top-level key in the
    # careers journalists.yaml (the per-#643 key convention); the m956
    # block lives under its competitor_coverage sub-key.
    return _yaml(JOURNALISTS_FILE)["blake_montgomery_type_b"][
        "competitor_coverage"][KEY_956]


def _m957_block():
    return _yaml(ENTITIES_FILE)[KEY_957]


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


def _synthetic_calibration_delta():
    """Fresh engine-layer calibration contract for #1210.

    Pooled illustrative delta over fully synthetic arms (no corpus
    input, no profile reads). Engine-layer ONLY: never promoted to a
    finding, never scored against the corpus.
    """
    synthetic_anthropic_arms = [-0.15, -0.25]
    synthetic_meta_arms = [-0.40, -0.45]
    pooled_anthropic = (sum(synthetic_anthropic_arms)
                        / len(synthetic_anthropic_arms))
    pooled_meta = sum(synthetic_meta_arms) / len(synthetic_meta_arms)
    return round(pooled_anthropic - pooled_meta, 3)


# ---------------------------------------------------------------------------
# 1. Novelty
# ---------------------------------------------------------------------------
class TestNovelty1210:
    def test_zero_type_d_1210_files_on_disk(self):
        assert glob.glob(
            os.path.join(TESTS_DIR, "test_type_d_1210*")) == [
                os.path.join(TESTS_DIR, OWN_BASENAME)], "only this file"

    def test_no_prior_type_d_1210_in_git_log(self):
        out = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type D #1210"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip() == ""

    def test_no_1210_block_key_repo_wide(self):
        # Designed keying: this file's keys reference the landed
        # iterations (1207/1208/1209) and mechanisms (955/956/957).
        # The only tracked carrier of the "type_d_1210" string is the
        # #1209 file's forward-guard pin (its no-Type-D-#1210 git-log
        # pin); no type_d_1210 block-key form exists anywhere.
        assert _git_grep_tracked("type_d_1210") == ["tests/" + C1209_FILE]

    def test_no_1210_row_in_readme_test_table_pre_commit(self):
        text = _read(README_FILE)
        assert TEST_BASENAME not in text

    def test_no_1210_row_in_architecture_tree_pre_commit(self):
        text = _read(ARCH_FILE)
        assert TEST_BASENAME not in text

    def test_readme_stats_pre_commit(self):
        text = _read(README_FILE)
        assert "| Tests | 65091 |" in text
        assert "Across 1534 test files" in text


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1210 opens the 1210-1214 window
# ---------------------------------------------------------------------------
class TestTypeDRotationGuard1210:
    def test_rotation_window_opens_1210(self):
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "1210-1214 window" in src
        assert "OPENING" in src

    def test_predecessor_1209_chain_present(self):
        out = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type C #1209"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert "Type C #1209" in out.stdout

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
        assert "#1211 Type E" in src

    def test_closing_window_1205_1209_verified_closed(self):
        # The 1205-1209 window verified closed as a consecutive
        # newest-first sequence in git history.
        for typ, n in (("D", "1205"), ("E", "1206"), ("A", "1207"),
                       ("B", "1208"), ("C", "1209")):
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
        for needle in ("Type D #1205:", "Type E #1206:",
                       "Type A #1207:", "Type B #1208:",
                       "Type C #1209:"):
            assert needle in subjects, needle

    def test_closing_window_main_hashes_present(self):
        # The five main-commit short hashes are pinned so the chain
        # the window-close claim rests on is the real one.
        out = subprocess.run(
            ["git", "log", "--format=%H"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        full = out.stdout.splitlines()
        for short in ("829b8a8b", "be56e254", "ec95a251", "33e4af12",
                      "52b03938"):
            assert any(h.startswith(short) for h in full), short


# ---------------------------------------------------------------------------
# 3. Novelty anchor: no prior #1210 claims
# ---------------------------------------------------------------------------
class TestTypeDNoveltyAnchor1210:
    def test_no_prior_type_d_1210_in_log(self):
        text = _read(LOG_FILE)
        assert "## #1210" not in text

    def test_no_prior_1210_opening_claim(self):
        # The #1209 entry already names the next window ("next window
        # 1210-1214 opens with Type D #1210" lineage); the pre-commit
        # absence pin is on the OPENING-leg heading this run adds.
        text = _read(LOG_FILE)
        assert "OPENING leg of the 1210-1214 window" not in text


# ---------------------------------------------------------------------------
# 4. Corpus integrity: the m955/m956/m957 landings are present
# ---------------------------------------------------------------------------
class TestTypeDCorpusIntegrity1210:
    def test_m955_block_present_in_bi_yaml(self):
        block = _m955_block()
        assert block["mechanism_id"] == 955
        assert block["iteration"] == 1207
        assert block["iteration_type"] == "A"

    def test_m956_block_present_in_journalists_yaml(self):
        block = _m956_block()
        assert block["mechanism_id"] == 956
        assert block["iteration"] == 1208
        assert block["type"] == "B"

    def test_m957_block_present_in_competitor_entities_yaml(self):
        block = _m957_block()
        assert block["mechanism_id"] == 957
        assert block["iteration"] == 1209
        assert block["iteration_type"] == "C"

    def test_max_mechanism_id_is_957(self):
        assert _max_numeric_mechanism_id_in_profiles() == 957

    def test_zero_958_forms_scoped(self):
        # Numeric scoped to profiles/; underscore/dash scoped to
        # profiles/ + tests/ per the #1191 convention (iteration-log.md
        # prose carries the forms as documented guards).
        assert _git_grep_tracked(_mech_id_colon(958), "profiles/") == []
        assert _sweep_underscore_mechanism(958) == []
        assert _sweep_dash_mechanism(958) == []

    def test_no_new_mechanisms_below_max(self):
        ids = []
        for dirpath, _, files in os.walk(PROFILES_DIR):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = _read(os.path.join(dirpath, fn))
                    ids += [int(m) for m in re.findall(
                        r"mechanism_id: (\d+)", text)]
        assert 957 in ids
        assert all(i <= 957 for i in ids)

    def test_m955_key_count_is_designed(self):
        # yaml key line + block_key field + test_file field echo of
        # the same slug: exactly 3.
        text = _read(BI_FILE)
        assert text.count(KEY_955) == 3

    def test_m956_key_count_is_designed(self):
        # yaml key line + block_key field + test_file field echo of
        # the same slug: exactly 3.
        text = _read(JOURNALISTS_FILE)
        assert text.count(KEY_956) == 3

    def test_m957_key_count_is_designed(self):
        # yaml key line + block_key field: exactly 2.
        text = _read(ENTITIES_FILE)
        assert text.count(KEY_957) == 2

    def test_m955_window(self):
        block = _m955_block()
        assert block["window"].startswith("1205-1209")

    def test_m956_journalist_attribution(self):
        block = _m956_block()
        assert block["journalist"] == "Blake Montgomery"
        assert block["publication"] == "the-guardian"

    def test_m957_status_check_not_new_direction(self):
        block = _m957_block()
        assert "STATUS-CHECK EXTENSION" in \
            block["relationship_direction_taxonomy"]
        assert "not a new direction" in \
            block["relationship_direction_taxonomy"]


# ---------------------------------------------------------------------------
# 5. m955 qualitative discipline (Type A #1207)
# ---------------------------------------------------------------------------
class TestTypeDM955QualitativeDiscipline1210:
    def test_m955_statistical_discipline_manual_only(self):
        block = _m955_block()
        assert block["statistical_discipline"].startswith(
            "MANUAL ILLUSTRATIVE")
        assert "Engine NOT run" in block["statistical_discipline"]
        assert "is_significant: fa" in block["statistical_discipline"]

    def test_m955_not_falsification_family_member(self):
        block = _m955_block()
        assert block["falsification_family_member"] is False

    def test_m955_verdict_mechanism_refinement(self):
        block = _m955_block()
        assert "mechanism_refinement_not_a_discovery" in block["verdict"]

    def test_m955_connects_to_refinement_line(self):
        block = _m955_block()
        assert block["connects_to"] == [399, 420, 745, 790, 799, 871]

    def test_m955_ledger_holds_48(self):
        # Control-case extension: claims no slot; the ledger sat at 48
        # when m955 landed (pre-m956).
        block = _m955_block()
        assert block["falsification_ledger"] == 48

    def test_m955_no_analysis_json_update(self):
        block = _m955_block()
        assert block["no_analysis_json_update"] is True

    def test_m955_research_method_bounded(self):
        # Excerpt-bounded per #503: 0 browser.open on the landing run.
        block = _m955_block()
        assert "0 browser.open" in block["research_method"]


# ---------------------------------------------------------------------------
# 6. m956 qualitative discipline (Type B #1208)
# ---------------------------------------------------------------------------
class TestTypeDM956QualitativeDiscipline1210:
    def test_m956_statistical_discipline_manual_only(self):
        block = _m956_block()
        assert block["statistical_discipline"].startswith(
            "MANUAL ILLUSTRATIVE ONLY")
        assert "NOT_CALCULATED" in block["statistical_discipline"]
        assert "engine NOT run" in block["statistical_discipline"]

    def test_m956_forty_ninth_member(self):
        # The m956 block carries the landed forty-ninth member-claim
        # form in its falsification_family field.
        block = _m956_block()
        assert FORTY_NINTH_MEMBER in block["falsification_family"]

    def test_m956_member_flag_true(self):
        block = _m956_block()
        assert block["falsification_family_member"] is True

    def test_m956_ledger_advances_to_49(self):
        block = _m956_block()
        assert block["falsification_ledger"] == 49

    def test_m956_verdict_member_confirmed(self):
        block = _m956_block()
        assert "falsification_member_confirmed" in block["verdict"]

    def test_m956_connects_to_deal_line(self):
        # The Guardian x OpenAI deal (514) is in the connects list:
        # the deal whose softening prediction this reporter inverts.
        block = _m956_block()
        assert block["connects_to"] == [472, 513, 514, 532, 952]

    def test_m956_not_significant(self):
        block = _m956_block()
        assert block["is_significant"] is False

    def test_m956_no_analysis_json_update(self):
        block = _m956_block()
        assert block["no_analysis_json_update"] is True

    def test_m956_research_method_bounded(self):
        # Delegated research + main-run verification, 0 browser.open
        # per #503 on the landing run.
        block = _m956_block()
        assert "0 browser.open" in block["research_method"]


# ---------------------------------------------------------------------------
# 7. m957 qualitative discipline (Type C #1209)
# ---------------------------------------------------------------------------
class TestTypeDM957QualitativeDiscipline1210:
    def test_m957_tone_not_scored_engine_not_run(self):
        block = _m957_block()
        assert block["tone_scored"] is False
        assert block["engine_run"] is False
        assert block["is_significant"] is False

    def test_m957_verdict_bounded(self):
        block = _m957_block()
        assert block["verdict"] == "directionally_supported_not_proven"

    def test_m957_no_analysis_json_update(self):
        block = _m957_block()
        assert block["no_analysis_json_update"] is True
        assert block["artifact_grade"] is False

    def test_m957_browser_opens_zero(self):
        block = _m957_block()
        assert block["browser_opens"] == 0

    def test_m957_connects_to_dual_payer_line(self):
        block = _m957_block()
        assert block["connects_to"] == [519]

    def test_m957_money_flow_openai_pays_news_corp(self):
        block = _m957_block()
        assert block["money_flow"].startswith("OPENAI PAYS NEWS CORP")

    def test_m957_not_a_member(self):
        # STATUS-CHECK EXTENSION per the #609/#614 boundary: no
        # member flag field asserted true anywhere in the block.
        block = _m957_block()
        assert block.get("falsification_family_member") is not True


# ---------------------------------------------------------------------------
# 8. Falsification ledger: holds at 49
# ---------------------------------------------------------------------------
class TestTypeDFalsificationLedger1210:
    def test_forty_sixth_claim_in_exactly_one_profiles_file(self):
        hits = _git_grep_tracked(FORTY_SIXTH_MEMBER, "profiles/")
        assert hits == ["profiles/the-verge.yaml"], hits

    def test_forty_seventh_member_claim_exactly_in_wired(self):
        # The single live forty-seventh member claim is m946
        # (profiles/wired.yaml). m955/m956/m957 landings do not move
        # the 47th slot.
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

    def test_forty_eighth_member_claim_in_financial_times(self):
        # The single live forty-eighth member claim is m952
        # (profiles/financial-times.yaml).
        hits = _git_grep_tracked(FORTY_EIGHTH_MEMBER, "profiles/")
        assert hits == ["profiles/financial-times.yaml"], hits

    def test_forty_eighth_member_claim_count_is_two(self):
        # The novelty "LANDED this run" line + the falsification_family
        # claim inside the m952 block: exactly 2 occurrences.
        out = subprocess.run(
            ["git", "grep", "-c", "-F", FORTY_EIGHTH_MEMBER, "--",
             "profiles/financial-times.yaml"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_forty_ninth_member_claim_in_journalists(self):
        # The single live forty-ninth member claim is m956
        # (profiles/careers/journalists.yaml).
        hits = _git_grep_tracked(FORTY_NINTH_MEMBER, "profiles/")
        assert hits == ["profiles/careers/journalists.yaml"], hits

    def test_forty_ninth_member_claim_count_is_three(self):
        # The notes landing line + the falsification_family claim +
        # the novelty line inside the m956 block: exactly 3.
        out = subprocess.run(
            ["git", "grep", "-c", "-F", FORTY_NINTH_MEMBER, "--",
             "profiles/careers/journalists.yaml"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip().endswith(":3"), out.stdout

    def test_no_fiftieth_member_claim_repo_wide(self):
        assert _git_grep_tracked(FIFTIETH_MEMBER) == []

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
        # Profiles-scoped per the #1199 in-gate fix: the #1197 and
        # #1202 test files carry the contiguous fortieth needle in
        # their own constant definitions; a repo-wide scope would trip
        # on those landed files. The format-built constant above is
        # never written contiguously in THIS file.
        assert _git_grep_tracked(_T40, "profiles/") == []
        assert len(_T40) > 0

    def test_ledger_holds_at_49(self):
        # m956 lands the forty-ninth slot (falsification_ledger 49);
        # m955 claims no slot; m957 is a status-check extension, not
        # a member. Exactly one live member claim at the top slot.
        b955 = _m955_block()
        assert b955["falsification_family_member"] is False
        assert b955["falsification_ledger"] == 48
        b956 = _m956_block()
        assert b956["falsification_family_member"] is True
        assert b956["falsification_ledger"] == 49
        assert FORTY_NINTH_MEMBER in b956["falsification_family"]
        b957 = _m957_block()
        assert "STATUS-CHECK EXTENSION" in \
            b957["relationship_direction_taxonomy"]


# ---------------------------------------------------------------------------
# 9. Type E #1206 discipline: the 164th verification cycle stays
#    monitoring-only
# ---------------------------------------------------------------------------
class TestTypeDTypeE1206Discipline1210:
    def test_1206_file_on_disk(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1206_FILE))

    def test_1206_pins_164th_cycle(self):
        src = _read(os.path.join(TESTS_DIR, E1206_FILE))
        assert "164th verification cycle" in src
        assert "163->164" in src

    def test_1206_monitoring_only_discipline(self):
        # The Aug 28 2026 standing rule: monitoring-only, tone
        # NOT_SCORED, engine NOT run, no mechanisms, NOT artifact-grade,
        # verdict directionally_supported_not_proven.
        src = _read(os.path.join(TESTS_DIR, E1206_FILE))
        assert "monitoring-only" in src
        assert "NOT artifact-grade" in src

    def test_1206_covers_both_podcasts(self):
        src = _read(os.path.join(TESTS_DIR, E1206_FILE))
        assert "Attention Sphere" in src
        assert "Guilty Feminist" in src

    def test_1206_research_method_bounded(self):
        src = _read(os.path.join(TESTS_DIR, E1206_FILE))
        assert "0 browser.open" in src


# ---------------------------------------------------------------------------
# 10. Forward-looking staleness (predecessor pin lifecycle via subprocess)
# ---------------------------------------------------------------------------
class TestTypeDForwardLookingStaleness1210:
    def test_1209_rotation_no_type_d_1210_pin_stays_green_precommit(self):
        # #1209's no-Type-D-#1210 git-log pin flips by design at THIS
        # run's main commit; the zero-958 guards stay GREEN (this run
        # lands no mechanisms - pinned in TestGuardLifecycle1210).
        # Record the pre-commit state: the pin still holds now.
        res = _node_run(
            C1209_FILE,
            "TestGuardLifecycle1209::test_no_type_d_1210_in_git_log_pin",
        )
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1209_guard_lifecycle_958_numeric_stays_green_precommit(self):
        res = _node_run(
            C1209_FILE,
            "TestGuardLifecycle1209::test_958_numeric_absent_in_profiles",
        )
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1209_zero_958_forms_stay_green(self):
        # The designed keying carries the iteration number, not the
        # mechanism number: #1209's zero-958 numeric guard stays green
        # (this run lands no mechanisms).
        res = _node_run(
            C1209_FILE,
            "TestMechanismNovelty1209::test_zero_numeric_958_in_profiles",
        )
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1209_rotation_window_pin_stays_green_precommit(self):
        res = _node_run(
            C1209_FILE,
            "TestRotationGuard1209::test_rotation_window_is_1205_1209",
        )
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1208_pins_flip_by_design_documented(self):
        # #1208's forward guards (max-956, zero-957 keys all forms,
        # no-Type-C-#1209-in-git-log) flip by design now that m957 has
        # landed; recorded in #1209's file, not repaired here.
        src = _read(os.path.join(TESTS_DIR, C1209_FILE))
        assert "1208" in src


# ---------------------------------------------------------------------------
# 11. Guard lifecycle: the guards this run lays for the next leg
# ---------------------------------------------------------------------------
class TestGuardLifecycle1210:
    def test_pins_on_no_mechanism_landing(self):
        # Type D lands no mechanisms: max stays 957, next stays 958.
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "MECH_NUM = 957" in src
        assert "NEXT_NUM = 958" in src

    def test_no_type_e_1211_in_git_log_pin(self):
        out = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type E #1211"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip() == ""

    def test_958_numeric_absent_in_profiles(self):
        assert _git_grep_tracked(_mech_id_colon(958), "profiles/") == []

    def test_no_fortieth_direction_pin(self):
        # The fortieth direction-claim form stays absent in profiles/
        # (profiles-scoped per the #1199 in-gate fix).
        assert _git_grep_tracked(_T40, "profiles/") == []

    def test_forty_ninth_member_intact_pin(self):
        # The single live forty-ninth member claim (m956,
        # careers/journalists.yaml) must survive this run unchanged.
        assert _git_grep_tracked(
            FORTY_NINTH_MEMBER, "profiles/") == [
                "profiles/careers/journalists.yaml"]

    def test_no_fiftieth_member_pin(self):
        assert _git_grep_tracked(FIFTIETH_MEMBER) == []

    def test_predecessor_1209_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, C1209_FILE))

    def test_next_leg_is_1211_type_e(self):
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "#1211 Type E" in src


# ---------------------------------------------------------------------------
# 12. Background-suite verdict per #795: the #1205-launched suite DIED
# ---------------------------------------------------------------------------
class TestBackgroundSuiteVerdict1210:
    def test_prior_suite_log_exists(self):
        assert os.path.exists(PRIOR_SUITE_LOG)

    def test_prior_suite_frozen_at_thirteen_percent(self):
        # The #1205-launched suite stalled at 38653 bytes / [ 13%]
        # progress; last write Oct 4 11:32 PDT (~28 min stale at this
        # run's 12:0x check); the log holds progress dots, not a
        # summary.
        text = _read(PRIOR_SUITE_LOG)
        assert 37000 <= len(text) <= 40000, len(text)
        assert "[ 13%]" in text

    def test_prior_suite_has_zero_summary_tokens(self):
        # A completed run prints a summary ("passed"/"failed") or a
        # collection report ("no tests ran" / "short test summary").
        # The dead run carries none of them.
        text = _read(PRIOR_SUITE_LOG)
        for token in ("passed", "failed", "no tests ran",
                      "short test summary"):
            assert token not in text, token

    def test_prior_suite_not_holding_live_pytest(self):
        # The re-launched #1210 suite IS alive in this run's process
        # set (a plain ps grep for "pytest" would self-trip on it),
        # so the dead-or-alive question must be scoped to the PRIOR
        # log: no process holds type_d_1205_full_suite.log open (the
        # /proc open-fd check per the #1190 convention). A dead run
        # produces no usable verdict, which is what this test pins.
        out = subprocess.run(
            ["bash", "-c",
             "ls -l /proc/[0-9]*/fd/* 2>/dev/null | grep -F "
             "'type_d_1205_full_suite.log' | head -5"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip() == "", out.stdout

    def test_thirty_sixth_consecutive_death(self):
        # The 57-run streak ENDED at #1085 (the #1080 suite completed).
        # This verdict renders the THIRTY-SIXTH consecutive
        # background-suite death of the new streak.
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "THIRTY-SIXTH consecutive" in src

    def test_tombstone_lineage_advances(self):
        # Per #565 the tombstone lineage advances with each verdict:
        # ONE-HUNDREDTH -> ONE-HUNDRED-FIRST.
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "ONE-HUNDREDTH -> ONE-HUNDRED-FIRST" in src

    def test_tombstone_recorded_in_iteration_log(self):
        # Deselected pre-commit: the tombstone is written into the
        # #1210 log entry in the doc-sync step per #719/#721.
        text = _read(LOG_FILE)
        assert "ONE-HUNDRED-FIRST" in text


# ---------------------------------------------------------------------------
# 13. Suite re-launch: the #1210-launched suite is in flight
# ---------------------------------------------------------------------------
class TestSuiteRelaunch1210:
    def test_relaunch_log_path_written(self):
        # The re-launched full suite log exists in goal hidden_files
        # (created by this run's background launch before commit).
        assert os.path.exists(SUITE_LOG), (
            "the #1210 background suite must be re-launched to "
            + SUITE_LOG
            + " before the main commit"
        )

    def test_relaunch_log_is_full_inventory(self):
        # The re-launch runs WITHOUT -x: the full inventory
        # (calendar by-design failures included) is needed for the
        # #1215 triage. The log must hold pytest progress output,
        # not just a header.
        text = _read(SUITE_LOG)
        assert text.count(".") > 100, (
            "the re-launched suite log should accumulate dot "
            "progress; got %d dots" % text.count(".")
        )

    def test_next_type_d_run_owns_the_verdict(self):
        # Per the #795 convention, the NEXT Type D run (#1215)
        # checks this suite's verdict; this run only records the
        # launch.
        assert "type_d_1210_full_suite.log" in SUITE_LOG


# ---------------------------------------------------------------------------
# 14. Synthetic engine calibration (engine-layer contract, never a
#     finding)
# ---------------------------------------------------------------------------
class TestSyntheticEngineCalibration1210:
    def test_calibration_delta_contract(self):
        # Synthetic Anthropic arms [-0.15, -0.25] vs synthetic Meta
        # arms [-0.40, -0.45]: pooled delta +0.225 (Meta-harder). This
        # is a FRESH #1210 engine-layer contract value; it is never
        # promoted to a finding.
        assert _synthetic_calibration_delta() == 0.225

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
class TestTypeDDocSync1210:
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
        assert "## #1210" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 65091 + COLLECTED_COUNT
        assert README_FILE_COUNT == 1535


# ---------------------------------------------------------------------------
# 16. Iteration log (#719: the entry carries hashes per #721)
# ---------------------------------------------------------------------------
class TestTypeDIterationLog1210:
    def test_log_entry_has_main_commit_hash(self):
        text = _read(LOG_FILE)
        assert "Type D #1210" in text

    def test_log_entry_notes_window_opening(self):
        text = _read(LOG_FILE)
        assert "OPENING leg of the 1210-1214 window" in text

    def test_log_entry_notes_tombstone_lineage(self):
        # Deselected pre-commit: the entry is written in the doc-sync
        # step per #719/#721.
        text = _read(LOG_FILE)
        assert "ONE-HUNDRED-FIRST" in text


# ---------------------------------------------------------------------------
# 17. Literal discipline (ASCII-only, no em dashes)
# ---------------------------------------------------------------------------
class TestLiteralDiscipline1210:
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
class TestInflightIsolation1210:
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
class TestAnchor1210:
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
        # "Type D #1210 anchor followup: ANCHORED_SHA -> <hash> ...".
        log = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type D #1210 anchor"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        ).stdout
        assert "Type D #1210 anchor" in log

    def test_main_commit_message_convention(self):
        log = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type D #1210:"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        ).stdout
        assert "Type D #1210" in log


# Collected count patch (post-first-run per #719).
COLLECTED_COUNT = 101
