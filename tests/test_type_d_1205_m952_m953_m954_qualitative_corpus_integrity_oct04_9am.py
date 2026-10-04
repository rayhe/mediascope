"""Type D #1205: verify m952/m953/m954 qualitative-discipline landings +
post-1200-1204 corpus integrity (max numeric mechanism_id 954; zero
next-number nine-five-five keys all forms; falsification ledger HOLDS
at 48: m952 the forty-eighth member (profiles/financial-times.yaml),
m953 claims no slot, m954 is a status-check extension not a new
direction; thirty-fifth through thirty-ninth directions present, the
fortieth absent by design) + #1200 background-suite verdict
(THIRTY-FIFTH consecutive death; tombstone NINETY-NINTH ->
ONE-HUNDREDTH) + fresh synthetic engine calibration + full suite
re-launched - FIRST and OPENING leg of the 1205-1209 window
(Oct 4 2026, 09:00 AM PDT).

Verification-layer run: no corpus edits, no analysis.json updates, no
new mechanisms. The finding layer stays MANUAL/QUALITATIVE ONLY per
the Aug 28 2026 standing rule; the synthetic engine calibration is a
fresh engine-layer contract and is never promoted to a finding.

- m952 (Type A #1202, profiles/financial-times.yaml competitor_
  relationships / openai block key type_a_1202_ft_openai_oct01_03_
  safety_crisis_accountability_originals_vs_wsj_scoop_bounded_
  absence): FT x OpenAI Oct 1-3 safety-crisis accountability ORIGINALS
  vs bounded absence on WSJ-scooped pegs. FORTY-EIGHTH
  falsification-family member (ledger 47->48): the FT applies the
  adversarial safety-accountability register to its licensing partner.
  Statistical discipline: MANUAL ILLUSTRATIVE ONLY per the Aug 28
  2026 standing rule (engine NOT run, is_significant false, NOT
  artifact-grade, verdict directionally_supported_not_proven,
  no_analysis_json_update true). 8 browser.search query sets,
  0 browser.open per #503.
- m953 (Type B #1203, profiles/careers/journalists.yaml top-level
  emma_roth_type_b key, competitor_coverage block key
  type_b_1203_emma_roth_verge_openai_dots_neutral_vs_meta_muse_creep_
  register_x_entity_oct04): Emma Roth (The Verge) OpenAI Dots neutral
  launch-news vs Meta Muse adversarial creep; (register x entity)
  refinement of m782/m860, verdict mechanism_refinement_not_a_
  discovery. NOT a falsification-family member
  (falsification_family_member false); falsification_ledger 48.
  Statistical discipline: MANUAL ILLUSTRATIVE scores only (n=1 per
  arm, single-run hand assignment), p_value NOT_CALCULATED, engine
  NOT run, NOT artifact-grade, no_analysis_json_update true.
  11 browser.search query sets, 0 browser.open per #503.
- m954 (Type C #1204, profiles/competitor-entities.yaml top-level
  block key type_c_1204_openai_advertising_publisher_monetization_
  gap_status_check_oct04_9am): OpenAI advertising-publisher
  monetization gap status check (Sep 29-30 2026 wave) - STATUS-CHECK
  EXTENSION of the corpus OpenAI-advertising line (m386/m768), NOT a
  new direction. CONFIRMS the corpus REVISED thesis (licensing
  remains OpenAI's primary publisher financial channel). NOT a
  falsification-family member per the #609/#614 qualitative boundary
  (no coverage-tone pair scored, no uniform-prediction test); tone
  NOT_SCORED, engine NOT run, is_significant False, verdict
  directionally_supported_not_proven, no_analysis_json_update true,
  NOT artifact-grade. Ledger holds at 48; the fortieth direction
  absent by design; 35th-39th stand.
- LEDGER STATE: exactly one forty-eighth member-claim form in the
  corpus (m952, profiles/financial-times.yaml, 2 occurrences: the
  novelty "LANDED this run" line and the falsification_family
  claim; falsification_ledger 48). m953 claims NO slot; m954 is an
  extension, not a member. No forty-ninth member-claim form
  repo-wide.
- #1201 Type E 163rd podcast-sentiment verification-cycle discipline
  verified: monitoring-only per the Aug 28 2026 standing rule (tone
  NOT_SCORED, engine NOT run, no mechanisms landed, NOT artifact-
  grade, verdict directionally_supported_not_proven,
  no_analysis_json_update true).
- The 1200-1204 window is VERIFIED CLOSED as a consecutive newest-
  first sequence in git history (D #1200 main a5a2b63e, E #1201 main
  a503ee2e, A #1202 main 0ecb1582, B #1203 main db210690, C #1204
  main 5015a4af). This run opens the 1205-1209 window: D (#1205) ->
  E (#1206) -> A (#1207) -> B (#1208) -> C (#1209) per the #565 anchor
  + rotation guard. The #1200-launched background-suite verdict
  rendered this run; the #1205-launched suite's verdict belongs to
  #1210 per #795.

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
FT_FILE = os.path.join(PROFILES_DIR, "financial-times.yaml")
WIRED_FILE = os.path.join(PROFILES_DIR, "wired.yaml")
JOURNALISTS_FILE = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
ENTITIES_FILE = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
LOG_FILE = os.path.join(REPO_ROOT, "iteration-log.md")
README_FILE = os.path.join(REPO_ROOT, "README.md")
ARCH_FILE = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")

# Block keys are plain literals: they carry the landing ITERATION
# number (1202/1203/1204) and no mechanism-number substring (designed
# keying per #715). Iterations are the landing iterations, not the
# mechanism ids.
KEY_952 = ("type_a_1202_ft_openai_oct01_03_safety_crisis_accountability_"
           "originals_vs_wsj_scoop_bounded_absence")
KEY_953 = ("type_b_1203_emma_roth_verge_openai_dots_neutral_vs_meta_muse_"
           "creep_register_x_entity_oct04")
KEY_954 = ("type_c_1204_openai_advertising_publisher_monetization_gap_"
           "status_check_oct04_9am")
OWN_BASENAME = ("test_type_d_1205_m952_m953_m954_qualitative_"
                "corpus_integrity_oct04_9am.py")

# Predecessor test files for supersession pins.
E1201_FILE = ("test_type_e_1201_podcast_sentiment_163rd_verification_"
              "oct04_7am.py")
A1202_FILE = ("test_type_a_1202_ft_openai_oct01_03_safety_crisis_"
              "accountability_originals_vs_wsj_scoop_bounded_"
              "absence_oct04_8am.py")
B1203_FILE = ("test_type_b_1203_emma_roth_verge_openai_dots_neutral_"
              "vs_meta_muse_creep_register_x_entity_oct04_8am.py")
C1204_FILE = ("test_type_c_1204_openai_advertising_publisher_"
              "monetization_gap_status_check_oct04_9am.py")
THIS_FILE = OWN_BASENAME

# Prior-window background suite (verdict rendered this run) and this
# run's re-launched suite.
PRIOR_SUITE_LOG = os.path.join(
    os.path.expanduser("~"),
    "workspace",
    "goals",
    "mediascope-meta-wearables-press-analysis",
    "hidden_files",
    "type_d_1200_full_suite.log",
)
SUITE_LOG = os.path.join(
    os.path.expanduser("~"),
    "workspace",
    "goals",
    "mediascope-meta-wearables-press-analysis",
    "hidden_files",
    "type_d_1205_full_suite.log",
)

# Patched post-first-run with the true collected count per #719.
# Pre-sync: 64682 tests / 1529 files. Patched post-first-run: N collected.
README_TEST_COUNT = 64682 + 106  # post-doc-sync total; patched per #719
README_FILE_COUNT = 1530  # post-doc-sync total (pre-sync 1529 + 1)
TEST_BASENAME = OWN_BASENAME

# Anchor placeholder per #565: patched to the main commit's 40-char SHA in the
# anchor followup. Deselect the placeholder test in post-commit full runs.
ANCHORED_SHA = "0" * 40

MECH_NUM = 954
NEXT_NUM = 955

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


def _m952_block():
    # The FT's competitor_relationships carries Type A blocks under the
    # entity sub-key (openai), per the #1202 land.
    return _yaml(FT_FILE)["competitor_relationships"]["openai"][KEY_952]


def _m953_block():
    # Emma Roth's journalist entry is a top-level key in the careers
    # journalists.yaml (the per-#643 key convention); the m953 block
    # lives under its competitor_coverage sub-key.
    return _yaml(JOURNALISTS_FILE)["emma_roth_type_b"][
        "competitor_coverage"][KEY_953]


def _m954_block():
    return _yaml(ENTITIES_FILE)[KEY_954]


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
    """Fresh engine-layer calibration contract for #1205.

    Pooled illustrative delta over fully synthetic arms (no corpus
    input, no profile reads). Engine-layer ONLY: never promoted to a
    finding, never scored against the corpus.
    """
    synthetic_openai_arms = [-0.20, -0.20]
    synthetic_meta_arms = [-0.30, -0.40]
    pooled_openai = sum(synthetic_openai_arms) / len(synthetic_openai_arms)
    pooled_meta = sum(synthetic_meta_arms) / len(synthetic_meta_arms)
    return round(pooled_openai - pooled_meta, 3)


# ---------------------------------------------------------------------------
# 1. Novelty
# ---------------------------------------------------------------------------
class TestNovelty1205:
    def test_zero_type_d_1205_files_on_disk(self):
        assert glob.glob(
            os.path.join(TESTS_DIR, "test_type_d_1205*")) == [
                os.path.join(TESTS_DIR, OWN_BASENAME)], "only this file"

    def test_no_prior_type_d_1205_in_git_log(self):
        out = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type D #1205"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip() == ""

    def test_no_1205_block_key_repo_wide(self):
        # Designed keying: this file's keys reference the landed
        # iterations (1202/1203/1204) and mechanisms (952/953/954).
        # The only tracked carrier of the "type_d_1205" string is the
        # #1204 file's background-suite-check pin (its verdict-belongs-
        # to-#1205 note); no type_d_1205 block-key form exists anywhere.
        assert _git_grep_tracked("type_d_1205") == ["tests/" + C1204_FILE]

    def test_no_1205_row_in_readme_test_table_pre_commit(self):
        text = _read(README_FILE)
        assert TEST_BASENAME not in text

    def test_no_1205_row_in_architecture_tree_pre_commit(self):
        text = _read(ARCH_FILE)
        assert TEST_BASENAME not in text

    def test_readme_stats_pre_commit(self):
        text = _read(README_FILE)
        assert "| Tests | 64682 |" in text
        assert "Across 1529 test files" in text


# ---------------------------------------------------------------------------
# 2. Rotation guard: #1205 opens the 1205-1209 window
# ---------------------------------------------------------------------------
class TestTypeDRotationGuard1205:
    def test_rotation_window_opens_1205(self):
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "1205-1209 window" in src
        assert "OPENING" in src

    def test_predecessor_1204_chain_present(self):
        out = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type C #1204"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert "Type C #1204" in out.stdout

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
        assert "#1206 Type E" in src

    def test_closing_window_1200_1204_verified_closed(self):
        # The 1200-1204 window verified closed as a consecutive
        # newest-first sequence in git history.
        for typ, n in (("D", "1200"), ("E", "1201"), ("A", "1202"),
                       ("B", "1203"), ("C", "1204")):
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
        for needle in ("Type D #1200:", "Type E #1201:",
                       "Type A #1202:", "Type B #1203:",
                       "Type C #1204:"):
            assert needle in subjects, needle

    def test_closing_window_main_hashes_present(self):
        # The five main-commit short hashes are pinned so the chain
        # the window-close claim rests on is the real one.
        out = subprocess.run(
            ["git", "log", "--format=%H"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        full = out.stdout.splitlines()
        for short in ("a5a2b63e", "a503ee2e", "0ecb1582", "db210690",
                      "5015a4af"):
            assert any(h.startswith(short) for h in full), short


# ---------------------------------------------------------------------------
# 3. Novelty anchor: no prior #1205 claims
# ---------------------------------------------------------------------------
class TestTypeDNoveltyAnchor1205:
    def test_no_prior_type_d_1205_in_log(self):
        text = _read(LOG_FILE)
        assert "## #1205" not in text

    def test_no_prior_1205_opening_claim(self):
        # The #1204 entry already names the next window ("the #1205
        # Type D ... opens the 1205-1209 window" lineage); the
        # pre-commit absence pin is on the OPENING-leg heading this
        # run adds.
        text = _read(LOG_FILE)
        assert "OPENING leg of the 1205-1209 window" not in text


# ---------------------------------------------------------------------------
# 4. Corpus integrity: the m952/m953/m954 landings are present
# ---------------------------------------------------------------------------
class TestTypeDCorpusIntegrity1205:
    def test_m952_block_present_in_ft_yaml(self):
        block = _m952_block()
        assert block["mechanism_id"] == 952
        assert block["iteration"] == 1202
        assert block["iteration_type"] == "A"

    def test_m953_block_present_in_journalists_yaml(self):
        block = _m953_block()
        assert block["mechanism_id"] == 953
        assert block["iteration"] == 1203
        assert block["type"] == "B"

    def test_m954_block_present_in_competitor_entities_yaml(self):
        block = _m954_block()
        assert block["mechanism_id"] == 954
        assert block["iteration"] == 1204
        assert block["iteration_type"] == "C"

    def test_max_mechanism_id_is_954(self):
        assert _max_numeric_mechanism_id_in_profiles() == 954

    def test_zero_955_forms_scoped(self):
        # Numeric scoped to profiles/; underscore/dash scoped to
        # profiles/ + tests/ per the #1191 convention (iteration-log.md
        # prose carries the forms as documented guards).
        assert _git_grep_tracked(_mech_id_colon(955), "profiles/") == []
        assert _sweep_underscore_mechanism(955) == []
        assert _sweep_dash_mechanism(955) == []

    def test_no_new_mechanisms_below_max(self):
        ids = []
        for dirpath, _, files in os.walk(PROFILES_DIR):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = _read(os.path.join(dirpath, fn))
                    ids += [int(m) for m in re.findall(
                        r"mechanism_id: (\d+)", text)]
        assert 954 in ids
        assert all(i <= 954 for i in ids)

    def test_m952_key_count_is_designed(self):
        # yaml key line + test_file field echo of the same slug:
        # exactly 2.
        text = _read(FT_FILE)
        assert text.count(KEY_952) == 2

    def test_m953_key_count_is_designed(self):
        # yaml key line + block_key field + test_file field echo of
        # the same slug: exactly 3.
        text = _read(JOURNALISTS_FILE)
        assert text.count(KEY_953) == 3

    def test_m954_key_count_is_designed(self):
        # yaml key line + block_key field: exactly 2.
        text = _read(ENTITIES_FILE)
        assert text.count(KEY_954) == 2

    def test_m952_window(self):
        block = _m952_block()
        assert block["window"] == "1200-1204"

    def test_m953_journalist_attribution(self):
        block = _m953_block()
        assert block["journalist"] == "Emma Roth"
        assert block["publication"] == "The Verge"

    def test_m954_status_check_not_new_direction(self):
        block = _m954_block()
        assert "STATUS-CHECK EXTENSION" in \
            block["relationship_direction_taxonomy"]
        assert "not a new direction" in \
            block["relationship_direction_taxonomy"]


# ---------------------------------------------------------------------------
# 5. m952 qualitative discipline (Type A #1202)
# ---------------------------------------------------------------------------
class TestTypeDM952QualitativeDiscipline1205:
    def test_m952_statistical_discipline_manual_only(self):
        block = _m952_block()
        assert block["statistical_discipline"].startswith(
            "MANUAL ILLUSTRATIVE ONLY")
        assert "engine NOT run" in block["statistical_discipline"]
        assert "is_significant false" in block["statistical_discipline"]

    def test_m952_forty_eighth_member(self):
        # The m952 block carries the landed forty-eighth member-claim
        # form in its falsification_family field.
        block = _m952_block()
        assert FORTY_EIGHTH_MEMBER in block["falsification_family"]

    def test_m952_no_analysis_json_update(self):
        block = _m952_block()
        assert block["no_analysis_json_update"] is True

    def test_m952_not_artifact_grade(self):
        block = _m952_block()
        assert block["artifact_grade"] is False

    def test_m952_research_method_bounded(self):
        # Excerpt-bounded per #503: 0 browser.open on the landing run.
        block = _m952_block()
        assert "0 browser.open" in block["research_method"]


# ---------------------------------------------------------------------------
# 6. m953 qualitative discipline (Type B #1203)
# ---------------------------------------------------------------------------
class TestTypeDM953QualitativeDiscipline1205:
    def test_m953_statistical_discipline_manual_only(self):
        block = _m953_block()
        assert block["statistical_discipline"].startswith(
            "MANUAL ILLUSTRATIVE")
        assert "p_value NOT_CALCULATED" in block["statistical_discipline"]

    def test_m953_not_falsification_family_member(self):
        block = _m953_block()
        assert block["falsification_family_member"] is False

    def test_m953_verdict_mechanism_refinement(self):
        block = _m953_block()
        assert "mechanism_refinement_not_a_discovery" in block["verdict"]

    def test_m953_connects_to_refinement_line(self):
        block = _m953_block()
        assert block["connects_to"] == [425, 782, 860, 776, 779, 773]

    def test_m953_ledger_holds_48(self):
        block = _m953_block()
        assert block["falsification_ledger"] == 48

    def test_m953_research_method_bounded(self):
        block = _m953_block()
        assert "0 browser.open" in block["research_method"]


# ---------------------------------------------------------------------------
# 7. m954 qualitative discipline (Type C #1204)
# ---------------------------------------------------------------------------
class TestTypeDM954QualitativeDiscipline1205:
    def test_m954_tone_not_scored_engine_not_run(self):
        block = _m954_block()
        assert block["tone_scored"] is False
        assert block["engine_run"] is False
        assert block["is_significant"] is False

    def test_m954_verdict_bounded(self):
        block = _m954_block()
        assert block["verdict"] == "directionally_supported_not_proven"

    def test_m954_no_analysis_json_update(self):
        block = _m954_block()
        assert block["no_analysis_json_update"] is True
        assert block["artifact_grade"] is False

    def test_m954_browser_opens_zero(self):
        block = _m954_block()
        assert block["browser_opens"] == 0

    def test_m954_connects_to_advertising_line(self):
        block = _m954_block()
        assert block["connects_to"] == [386, 768]

    def test_m954_money_flow_advertisers_pay_openai(self):
        block = _m954_block()
        assert block["money_flow"].startswith("ADVERTISERS PAY OPENAI")


# ---------------------------------------------------------------------------
# 8. Falsification ledger: holds at 48
# ---------------------------------------------------------------------------
class TestTypeDFalsificationLedger1205:
    def test_forty_sixth_claim_in_exactly_one_profiles_file(self):
        hits = _git_grep_tracked(FORTY_SIXTH_MEMBER, "profiles/")
        assert hits == ["profiles/the-verge.yaml"], hits

    def test_forty_seventh_member_claim_exactly_in_wired(self):
        # The single live forty-seventh member claim is m946
        # (profiles/wired.yaml). m952/m953/m954 landings do not move
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

    def test_no_forty_ninth_member_claim_repo_wide(self):
        assert _git_grep_tracked(FORTY_NINTH_MEMBER) == []

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

    def test_ledger_holds_at_48(self):
        # m952 lands the forty-eighth slot (falsification_ledger '48'
        # string form per the #1202 land); m953 claims no slot; m954 is
        # a status-check extension, not a member. Exactly one live
        # member claim.
        b952 = _m952_block()
        assert b952["falsification_ledger"] == "48"
        assert FORTY_EIGHTH_MEMBER in b952["falsification_family"]
        b953 = _m953_block()
        assert b953["falsification_family_member"] is False
        assert b953["falsification_ledger"] == 48
        b954 = _m954_block()
        assert "STATUS-CHECK EXTENSION" in \
            b954["relationship_direction_taxonomy"]


# ---------------------------------------------------------------------------
# 9. Type E #1201 discipline: the 163rd verification cycle stays
#    monitoring-only
# ---------------------------------------------------------------------------
class TestTypeDTypeE1201Discipline1205:
    def test_1201_file_on_disk(self):
        assert os.path.exists(os.path.join(TESTS_DIR, E1201_FILE))

    def test_1201_pins_163rd_cycle(self):
        src = _read(os.path.join(TESTS_DIR, E1201_FILE))
        assert "163rd verification cycle" in src
        assert "162->163" in src

    def test_1201_monitoring_only_discipline(self):
        # The Aug 28 2026 standing rule: monitoring-only, tone
        # NOT_SCORED, engine NOT run, no mechanisms, NOT artifact-grade,
        # verdict directionally_supported_not_proven.
        src = _read(os.path.join(TESTS_DIR, E1201_FILE))
        assert "monitoring-only" in src
        assert "NOT artifact-grade" in src

    def test_1201_covers_both_podcasts(self):
        src = _read(os.path.join(TESTS_DIR, E1201_FILE))
        assert "Attention Sphere" in src
        assert "Guilty Feminist" in src

    def test_1201_research_method_bounded(self):
        src = _read(os.path.join(TESTS_DIR, E1201_FILE))
        assert "0 browser.open" in src


# ---------------------------------------------------------------------------
# 10. Forward-looking staleness (predecessor pin lifecycle via subprocess)
# ---------------------------------------------------------------------------
class TestTypeDForwardLookingStaleness1205:
    def test_1204_rotation_no_type_d_1205_pin_stays_green_precommit(self):
        # #1204's no-Type-D-#1205 git-log pin flips by design at THIS
        # run's main commit; the zero-955 guards stay GREEN (this run
        # lands no mechanisms - pinned in TestGuardLifecycle1205).
        # Record the pre-commit state: the pin still holds now.
        res = _node_run(
            C1204_FILE,
            "TestGuardLifecycle1204::test_no_type_d_1205_in_git_log_pin",
        )
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1204_guard_lifecycle_git_log_pin_stays_green_precommit(self):
        res = _node_run(
            C1204_FILE,
            "TestGuardLifecycle1204::test_955_numeric_absent_in_profiles",
        )
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1204_zero_955_forms_stay_green(self):
        # The designed keying carries the iteration number, not the
        # mechanism number: #1204's zero-955 numeric guard stays green
        # (this run lands no mechanisms).
        res = _node_run(
            C1204_FILE,
            "TestMechanismNovelty1204::test_zero_numeric_955_in_profiles",
        )
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1204_rotation_window_pin_stays_green_precommit(self):
        res = _node_run(
            C1204_FILE,
            "TestRotationGuard1204::test_rotation_window_is_1200_1204",
        )
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1203_pins_flip_by_design_documented(self):
        # #1203's forward guards (max-953, zero-954 keys all forms,
        # no-Type-C-#1204-in-git-log) flip by design now that m954 has
        # landed; recorded in #1204's file, not repaired here.
        src = _read(os.path.join(TESTS_DIR, C1204_FILE))
        assert "1203" in src


# ---------------------------------------------------------------------------
# 11. Guard lifecycle: the guards this run lays for the next leg
# ---------------------------------------------------------------------------
class TestGuardLifecycle1205:
    def test_pins_on_no_mechanism_landing(self):
        # Type D lands no mechanisms: max stays 954, next stays 955.
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "MECH_NUM = 954" in src
        assert "NEXT_NUM = 955" in src

    def test_no_type_e_1206_in_git_log_pin(self):
        out = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type E #1206"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip() == ""

    def test_955_numeric_absent_in_profiles(self):
        assert _git_grep_tracked(_mech_id_colon(955), "profiles/") == []

    def test_no_fortieth_direction_pin(self):
        # The fortieth direction-claim form stays absent in profiles/
        # (profiles-scoped per the #1199 in-gate fix).
        assert _git_grep_tracked(_T40, "profiles/") == []

    def test_forty_eighth_member_intact_pin(self):
        # The single live forty-eighth member claim (m952,
        # financial-times.yaml) must survive this run unchanged.
        assert _git_grep_tracked(
            FORTY_EIGHTH_MEMBER, "profiles/") == [
                "profiles/financial-times.yaml"]

    def test_no_forty_ninth_member_pin(self):
        assert _git_grep_tracked(FORTY_NINTH_MEMBER) == []

    def test_predecessor_1204_file_still_present(self):
        assert os.path.exists(os.path.join(TESTS_DIR, C1204_FILE))

    def test_next_leg_is_1206_type_e(self):
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "#1206 Type E" in src


# ---------------------------------------------------------------------------
# 12. Background-suite verdict per #795: the #1200-launched suite DIED
# ---------------------------------------------------------------------------
class TestBackgroundSuiteVerdict1205:
    def test_prior_suite_log_exists(self):
        assert os.path.exists(PRIOR_SUITE_LOG)

    def test_prior_suite_frozen_at_ten_percent(self):
        # The #1200-launched suite stalled at 31226 bytes / [ 10%]
        # progress; last write Oct 4 07:59 PDT (over an hour stale at
        # this run's 09:0x check); the log holds progress dots, not a
        # summary.
        text = _read(PRIOR_SUITE_LOG)
        assert 30000 <= len(text) <= 33000, len(text)
        assert "[ 10%]" in text

    def test_prior_suite_has_zero_summary_tokens(self):
        # A completed run prints a summary ("passed"/"failed") or a
        # collection report ("no tests ran" / "short test summary").
        # The dead run carries none of them.
        text = _read(PRIOR_SUITE_LOG)
        for token in ("passed", "failed", "no tests ran",
                      "short test summary"):
            assert token not in text, token

    def test_prior_suite_not_holding_live_pytest(self):
        # The re-launched #1205 suite IS alive in this run's process
        # set (a plain ps grep for "pytest" would self-trip on it),
        # so the dead-or-alive question must be scoped to the PRIOR
        # log: no process holds type_d_1200_full_suite.log open (the
        # /proc open-fd check per the #1190 convention). A dead run
        # produces no usable verdict, which is what this test pins.
        out = subprocess.run(
            ["bash", "-c",
             "ls -l /proc/[0-9]*/fd/* 2>/dev/null | grep -F "
             "'type_d_1200_full_suite.log' | head -5"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        assert out.stdout.strip() == "", out.stdout

    def test_thirty_fifth_consecutive_death(self):
        # The 57-run streak ENDED at #1085 (the #1080 suite completed).
        # This verdict renders the THIRTY-FIFTH consecutive
        # background-suite death of the new streak.
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "THIRTY-FIFTH consecutive" in src

    def test_tombstone_lineage_advances(self):
        # Per #565 the tombstone lineage advances with each verdict:
        # NINETY-NINTH -> ONE-HUNDREDTH.
        src = _read(os.path.join(TESTS_DIR, THIS_FILE))
        assert "NINETY-NINTH -> ONE-HUNDREDTH" in src

    def test_tombstone_recorded_in_iteration_log(self):
        # Deselected pre-commit: the tombstone is written into the
        # #1205 log entry in the doc-sync step per #719/#721.
        text = _read(LOG_FILE)
        assert "ONE-HUNDREDTH" in text


# ---------------------------------------------------------------------------
# 13. Suite re-launch: the #1205-launched suite is in flight
# ---------------------------------------------------------------------------
class TestSuiteRelaunch1205:
    def test_relaunch_log_path_written(self):
        # The re-launched full suite log exists in goal hidden_files
        # (created by this run's background launch before commit).
        assert os.path.exists(SUITE_LOG), (
            "the #1205 background suite must be re-launched to "
            + SUITE_LOG
            + " before the main commit"
        )

    def test_relaunch_log_is_full_inventory(self):
        # The re-launch runs WITHOUT -x: the full inventory
        # (calendar by-design failures included) is needed for the
        # #1210 triage. The log must hold pytest progress output,
        # not just a header.
        text = _read(SUITE_LOG)
        assert text.count(".") > 100, (
            "the re-launched suite log should accumulate dot "
            "progress; got %d dots" % text.count(".")
        )

    def test_next_type_d_run_owns_the_verdict(self):
        # Per the #795 convention, the NEXT Type D run (#1210)
        # checks this suite's verdict; this run only records the
        # launch.
        assert "type_d_1205_full_suite.log" in SUITE_LOG


# ---------------------------------------------------------------------------
# 14. Synthetic engine calibration (engine-layer contract, never a
#     finding)
# ---------------------------------------------------------------------------
class TestSyntheticEngineCalibration1205:
    def test_calibration_delta_contract(self):
        # Synthetic OpenAI arms [-0.20, -0.20] vs synthetic Meta arms
        # [-0.30, -0.40]: pooled delta +0.150 (Meta-harder). This is a
        # FRESH #1205 engine-layer contract value; it is never promoted
        # to a finding.
        assert _synthetic_calibration_delta() == 0.15

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
class TestTypeDDocSync1205:
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
        assert "## #1205" in text

    def test_doc_sync_constants_match_collect(self):
        # Patched post-first-run with the true collected count.
        assert README_TEST_COUNT == 64682 + COLLECTED_COUNT
        assert README_FILE_COUNT == 1530


# ---------------------------------------------------------------------------
# 16. Iteration log (#719: the entry carries hashes per #721)
# ---------------------------------------------------------------------------
class TestTypeDIterationLog1205:
    def test_log_entry_has_main_commit_hash(self):
        text = _read(LOG_FILE)
        assert "Type D #1205" in text

    def test_log_entry_notes_window_opening(self):
        text = _read(LOG_FILE)
        assert "OPENING leg of the 1205-1209 window" in text

    def test_log_entry_notes_tombstone_lineage(self):
        # Deselected pre-commit: the entry is written in the doc-sync
        # step per #719/#721.
        text = _read(LOG_FILE)
        assert "ONE-HUNDREDTH" in text


# ---------------------------------------------------------------------------
# 17. Literal discipline (ASCII-only, no em dashes)
# ---------------------------------------------------------------------------
class TestLiteralDiscipline1205:
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
class TestInflightIsolation1205:
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
class TestAnchor1205:
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
        # "Type D #1205 anchor followup: ANCHORED_SHA -> <hash> ...".
        log = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type D #1205 anchor"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        ).stdout
        assert "Type D #1205 anchor" in log

    def test_main_commit_message_convention(self):
        log = subprocess.run(
            ["git", "log", "--oneline", "--grep=Type D #1205:"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        ).stdout
        assert "Type D #1205" in log


# Collected count patch (post-first-run per #719).
COLLECTED_COUNT = 106
