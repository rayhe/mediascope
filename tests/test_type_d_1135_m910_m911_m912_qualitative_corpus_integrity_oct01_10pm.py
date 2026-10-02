"""Type D -- Iteration #1135 (Thu 2026-10-01 22:00 PDT): m910/m911/m912
qualitative-discipline verification + post-1130-1134 corpus integrity
(max numeric mechanism_id 912; zero next-number 913 keys in
numeric/underscore/dash mechanism forms - the 913 needles are
format-built per #715 so no guard-literal carrier file exists; the
m910/m911/m912 block keys carry no mechanism-number substring
(designed keying), so they are plain literals; the #1131/#1132/#1133/
#1134 window files are NOT edited by this run - their now-stale
forward-looking pins are recorded as fail-by-design via subprocess in
the staleness class (#1130's max-909 + zero-910-numeric + no-thirty-
fourth-direction + no-forty-seventh-member guards trip on the landed
910/911/912 and THIRTY-FOURTH; #1131's staleness pin on #1130's
guard lifecycle flips on the 910/911/912 landings; #1132/#1133/#1134
supersession + forward-guard pins STAY GREEN - Type D lands no
mechanism); ledger holds at 46 with the FORTY-SIXTH member-claim form
present in exactly one profiles file (profiles/the-verge.yaml, m907
block, 2 occurrences - the #1127 designed pattern) and the
forty-seventh member-claim form absent repo-wide (needle format-built
per #715); the THIRTY-FOURTH relationship direction is present in
competitor-entities.yaml (m912 NEGOTIATE-WHILE-COVERING); the
thirty-fifth relationship-direction claim form is absent repo-wide
(needle format-built per #715)) + the #1130 background-suite verdict
(DIED at 3874 bytes / 3479 dots ~5% with last write Oct 1 19:10 PDT
and zero summary tokens, no live pytest process - TENTH consecutive
background-suite death of the new streak; the 57-run streak ENDED at
#1085 when the #1080 suite completed; tombstone lineage advances
EIGHTY-FIFTH -> EIGHTY-SIXTH) + fresh synthetic engine calibration
(new values, not #1130's) + re-launch of the full suite as a background
process writing to goal hidden_files type_d_1135_full_suite.log WITHOUT
-x (the full inventory, calendar by-design failures included, is needed
for the #1140 triage; the next Type D run checks its verdict per the
#795 convention).

Type D FIRST leg of the 1135-1139 window, OPENING it
(D->E->A->B->C). Committed predecessor #1134 Type C (9:00 PM PDT Oct 1)
CLOSED the 1130-1134 window (D #1130, E #1131, A #1132, B #1133,
C #1134). Rotation per the #565 anchor + rotation guard.
Concurrency note: the in-flight runs at this run's checks are the
#899 Type C block (m771, uncommitted hunk in profiles/nytimes.yaml),
the #938 Type B test file (uncommitted working-tree edit), the #900
Type D test file (untracked, on disk) and the #1012 working-tree
edit of the committed Type A #1012 test file - all UNCOMMITTED, no
Type C #899 / Type B #938 / Type D #900 main commits in git
history, and no ## #899 / ## #938 / ## #900 Type X entries in
iteration-log.md. This run does NOT touch the in-flight files;
the in-flight blocks are owned by their runs. Targeted staging only
per the repo-wide traversal lesson. Iteration numbers follow the
rotation schedule, not commit order. Do NOT touch #1024's m846
(FOURTEENTH, exclusionary-diversion): self-flagged
sourcing-constraint violation; Ray's revert/leave/rebuild-from-primary
decision still pending.

Verifies:
- m910 (Type A #1132, competitor-coverage-research.yaml 2-space block
  key, `mechanism_id: 910` field form; block key count 2 -
  colon-form line + test_file field, designed: no block_key field in
  the m910 block): NYT Sep-28-Oct-1 2026 OpenAI crisis-accountability
  triple (Sep-3 Hugging Face piece -0.45 + Sep-29 dismissed-warnings
  piece -0.50 + Sep-30 FTC probe -0.40, arm mean -0.45) vs carried
  NYT x Meta arms (Jun-23 holdout -0.65 + Jun-26 Arena scoop 0.0,
  un-rescored per #807). OpenAI mean sits INSIDE the Meta register
  range [-0.65, 0.0]; the Sep-16 valuation arm (+0.15, m771) inverts
  by -0.60 within 15 days. PLAINTIFF-CONTROL peg-following mechanism:
  register follows the NEWS PEG, not the entity. Sep-30 FTC arm
  (-0.40) pairs with FT (m901), WSJ (m904), Verge (m907 A2) into a
  uniform cross-publication enforcement register. NOT a
  falsification-family member; ledger holds at 46.
- m911 (Type B #1133, journalists.yaml 4-space block key under
  cherlynn_low competitor_coverage, `mechanism_id: 911` field form;
  block key count 3 - colon-form line + block_key field + test_file
  field, designed): Cherlynn Low (Engadget) Sep-18/19 Apple Watch
  Series 12 scored review (+0.30, 9.1/10, always-on ambient
  listening) vs Sep-23 Meta Connect 2026 liveblog (0.0,
  neutral-wry, surveillance joke) - genre-bound within-writer
  register contrast (delta +0.30) EXTENDING m872's constancy finding
  (+0.05 null same-genre). No financial gradient tested; NOT a
  falsification-family member; ledger holds at 46.
- m912 (Type C #1134, competitor-entities.yaml zero-indent block
  key, `mechanism_id: 912` field form; block key count 2 -
  colon-form line + block_key field, designed - no test_file field
  in the m912 block): Louisiana publisher John Georges pursues a
  Meta AI-content licensing deal while his outlets' newsroom covers
  Meta's Louisiana investments - NEGOTIATE-WHILE-COVERING as the
  THIRTY-FOURTH relationship direction: the independence risk
  crystallizes in the negotiation window, before any money flows.
  connects_to [519, 732]. Tone NOT_SCORED; NOT a falsification-family
  member; ledger holds at 46.

All three: MANUAL/QUALITATIVE ONLY, engine NOT run,
no analysis.json update, NOT artifact-grade, verdict
directionally_supported_not_proven. Correlation is not causation;
hypothesis-generating only.
"""

import glob
import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
RESEARCH_FILE = os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml")
JOURNALISTS_FILE = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
ENTITIES_FILE = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
VERGE_FILE = os.path.join(PROFILES_DIR, "the-verge.yaml")
LOG_FILE = os.path.join(REPO_ROOT, "iteration-log.md")
README_FILE = os.path.join(REPO_ROOT, "README.md")
ARCH_FILE = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")

# Block keys are plain literals: none carries a mechanism-number
# substring (designed keying per #715).
KEY_910 = ("type_a_1132_nyt_openai_sep28_oct01_crisis_accountability_"
           "register_vs_carried_meta_arms_oct01_7pm")
KEY_911 = ("type_b_1133_cherlynn_low_engadget_meta_connect_liveblog_"
           "vs_apple_watch_series_12_review_sep2026")
KEY_912 = ("type_c_1134_john_georges_meta_licensing_pursuit_"
           "negotiate_while_covering_thirty_fourth_direction_oct01_9pm")
OWN_BASENAME = ("test_type_d_1135_m910_m911_m912_qualitative_"
                "corpus_integrity_oct01_10pm.py")

# Predecessor test files for supersession pins.
D1130_FILE = ("test_type_d_1130_m907_m908_m909_qualitative_"
              "corpus_integrity_oct01_6pm.py")
E1131_FILE = "test_type_e_1131_podcast_sentiment_149th_verification_oct01_7pm.py"
A1132_FILE = ("test_type_a_1132_nyt_openai_sep28_oct01_crisis_"
              "accountability_register_vs_carried_meta_arms_oct01_7pm.py")
B1133_FILE = ("test_type_b_1133_cherlynn_low_engadget_meta_connect_"
              "liveblog_vs_apple_watch_series_12_review_sep2026_8pm.py")
C1134_FILE = ("test_type_c_1134_john_georges_meta_licensing_pursuit_"
              "negotiate_while_covering_oct01_9pm.py")

# Prior-window background suite (verdict rendered this run) and this
# run's re-launched suite.
PRIOR_SUITE_LOG = os.path.join(
    os.path.expanduser("~"),
    "workspace",
    "goals",
    "mediascope-meta-wearables-press-analysis",
    "hidden_files",
    "type_d_1130_full_suite.log",
)
SUITE_LOG = os.path.join(
    os.path.expanduser("~"),
    "workspace",
    "goals",
    "mediascope-meta-wearables-press-analysis",
    "hidden_files",
    "type_d_1135_full_suite.log",
)

# Patched post-commit once README/ARCHITECTURE doc-sync lands.
README_TEST_COUNT = 59520  # post-doc-sync total (59438 + 82)
README_FILE_COUNT = 1460  # post-doc-sync total
TEST_BASENAME = OWN_BASENAME

# Anchor placeholder per #565: patched to the main commit's 40-char SHA in the
# anchor followup. Deselect the placeholder test in post-commit full runs.
ANCHORED_SHA = "0" * 40

MECH_NUM = 912
NEXT_NUM = 913
PREV_NUM = 911

# Fragment-built direction needles per #715 (never contiguous here).
_T33 = "THIRTY-" + "THIRD relationship direction"
_T34 = "THIRTY-" + "FOURTH relationship direction"
_T35 = "THIRTY-" + "FIFTH relationship direction"


# Format-built mechanism needles per #715/#770 (never contiguous here).
def _mech_underscore(n):
    return "mechanism" + "_%d" % n


def _mech_dash(n):
    return "mechanism" + "-%d" % n


def _mech_id_colon(n):
    return "mechanism_id: %d" % n


FORTY_SIXTH_MEMBER = "FORTY" + "-SIXTH falsification-family member"
FORTY_SEVENTH_MEMBER = "FORTY" + "-SEVENTH falsification-family member"


def _read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _key_count_in_file(key, path):
    return _read(path).count(key)


def _git(*args):
    result = subprocess.run(
        ["git"] + list(args),
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=60,
    )
    return result.stdout


def _git_grep_tracked(needle, *paths):
    cmd = ["git", "grep", "-l", "-F", needle]
    if paths:
        cmd += ["--"] + list(paths)
    out = subprocess.run(
        cmd, cwd=REPO_ROOT, capture_output=True, text=True, timeout=90,
    )
    return [line for line in out.stdout.split("\n") if line.strip()]


def _max_numeric_mechanism_id_in_profiles():
    ids = []
    for dirpath, _, files in os.walk(PROFILES_DIR):
        for fn in files:
            if fn.endswith(".yaml"):
                text = _read(os.path.join(dirpath, fn))
                for m in re.findall(r"mechanism_id: (\d+)", text):
                    ids.append(int(m))
    return max(ids)


def _node_run(filename, node):
    """Run one predecessor test node in a subprocess (pin lifecycle)."""
    target = os.path.join(TESTS_DIR, filename) + "::" + node
    env = dict(os.environ)
    env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    venv_py = os.path.join(REPO_ROOT, ".venv", "bin", "python")
    return subprocess.run(
        [venv_py, "-m", "pytest", target, "-q", "--no-header",
         "-o", "addopts="],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        env=env,
        timeout=120,
    )


def _class_run(filename, classname):
    """Run one predecessor test class in a subprocess."""
    target = os.path.join(TESTS_DIR, filename) + "::" + classname
    env = dict(os.environ)
    env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    venv_py = os.path.join(REPO_ROOT, ".venv", "bin", "python")
    return subprocess.run(
        [venv_py, "-m", "pytest", target, "-q", "--no-header",
         "-o", "addopts="],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        env=env,
        timeout=120,
    )


# ---------------------------------------------------------------------------
# 1. Novelty
# ---------------------------------------------------------------------------
class TestNovelty1135:
    def test_no_type_d_1135_test_file_preexisting(self):
        hits = glob.glob(
            os.path.join(TESTS_DIR, "test_type_d_1135*.py"))
        assert hits == [os.path.join(TESTS_DIR, OWN_BASENAME)], hits

    def test_no_type_d_1135_in_git_log(self):
        # Deselected pre-commit per #565: the main commit does not
        # exist yet.
        log = _git("log", "--oneline", "--grep=Type D #1135")
        assert "Type D #1135" in log, log

    def test_max_id_is_912(self):
        needle = _mech_id_colon(MECH_NUM)
        hits = _git_grep_tracked(needle, "profiles/")
        assert hits == ["profiles/competitor-entities.yaml"], hits

    def test_zero_913_numeric_forms_in_profiles(self):
        needle = _mech_id_colon(NEXT_NUM)
        assert _git_grep_tracked(needle, "profiles/") == []

    def test_block_keys_unique_in_home_yamls(self):
        assert _key_count_in_file(KEY_910, RESEARCH_FILE) == 2
        assert _key_count_in_file(KEY_911, JOURNALISTS_FILE) == 3
        assert _key_count_in_file(KEY_912, ENTITIES_FILE) == 2
        # Designed keying: no mechanism-number substring in any
        # block key, so they are plain literals here.
        for key in (KEY_910, KEY_911, KEY_912):
            assert "910" not in key and "911" not in key and "912" not in key

    def test_no_type_e_1136_in_git_log(self):
        # The next leg must not exist yet.
        log = _git("log", "--oneline", "--grep=Type E #1136")
        assert "Type E #1136" not in log, log


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------
class TestTypeDRotationGuard1135:
    def test_rotation_window_opens_1135(self):
        # 1135-1139 window: D opens, then E -> A -> B -> C.
        log = _git("log", "--oneline", "--grep=Type C #1134")
        assert "Type C #1134" in log, log
        entry = _read(LOG_FILE)
        assert "1130-1134 window CLOSED" in entry

    def test_predecessor_1134_chain_present(self):
        log = _git("log", "--format=%H %s")
        assert "Type C #1134" in log, log
        for sha8 in ("afa0e480", "30577b04", "0390c85e", "a50bbdb2"):
            assert sha8 in log, sha8

    def test_anchor_sha_is_real(self):
        # Deselected pre-commit: patched in the anchor followup.
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA
        assert ANCHORED_SHA != "0" * 40


# ---------------------------------------------------------------------------
# 3. Novelty anchor
# ---------------------------------------------------------------------------
class TestTypeDNoveltyAnchor1135:
    def test_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per #565: the main commit does not
        # exist yet. Post-commit this asserts the single #1135
        # commit is the anchor and carries the test-file changes.
        log = _git("log", "--format=%H %s", "--grep=Type D #1135")
        assert "Type D #1135" in log
        assert ANCHORED_SHA in log


# ---------------------------------------------------------------------------
# 4. Corpus integrity
# ---------------------------------------------------------------------------
class TestTypeDCorpusIntegrity1135:
    def test_m910_block_present_in_research_yaml(self):
        with open(RESEARCH_FILE) as f:
            data = yaml.safe_load(f)
        block = data[KEY_910]
        assert block["mechanism_id"] == 910
        assert block["rotation_type"] == "A"

    def test_m911_block_present_in_journalists_yaml(self):
        with open(JOURNALISTS_FILE) as f:
            data = yaml.safe_load(f)
        block = data["cherlynn_low"]["competitor_coverage"][KEY_911]
        assert block["mechanism_id"] == 911
        assert block["type"] == "B"

    def test_m912_block_present_in_competitor_entities_yaml(self):
        with open(ENTITIES_FILE) as f:
            data = yaml.safe_load(f)
        block = data[KEY_912]
        assert block["mechanism_id"] == 912
        assert block["iteration_type"] == "C"

    def test_max_mechanism_id_is_912(self):
        assert _max_numeric_mechanism_id_in_profiles() == 912

    def test_zero_913_forms_repo_wide(self):
        assert _git_grep_tracked(_mech_id_colon(913)) == []
        assert _git_grep_tracked(_mech_underscore(913)) == []
        assert _git_grep_tracked(_mech_dash(913)) == []

    def test_m910_key_count_is_designed(self):
        # Colon-form line + test_file field; no block_key field in
        # the m910 block.
        assert _key_count_in_file(KEY_910, RESEARCH_FILE) == 2

    def test_m911_key_count_is_designed(self):
        # Colon-form line + block_key field + test_file field.
        assert _key_count_in_file(KEY_911, JOURNALISTS_FILE) == 3

    def test_m912_key_count_is_designed(self):
        # Colon-form line + block_key field; no test_file field in
        # the m912 block.
        assert _key_count_in_file(KEY_912, ENTITIES_FILE) == 2


# ---------------------------------------------------------------------------
# 5. m910 qualitative discipline
# ---------------------------------------------------------------------------
class TestTypeDM910QualitativeDiscipline:
    def _block(self):
        with open(RESEARCH_FILE) as f:
            data = yaml.safe_load(f)
        return data[KEY_910]

    def test_m910_run_metadata(self):
        b = self._block()
        assert b["iteration"] == 1132
        assert b["rotation_type"] == "A"
        assert b["publication"] == "The New York Times"
        assert b["competitor"] == "OpenAI"
        assert b["comparator_entity"] == "Meta"
        assert b["verdict"].startswith("PLAINTIFF-CONTROL")

    def test_m910_openai_arms(self):
        b = self._block()
        arms = b["openai_arms"]
        assert len(arms) == 3
        assert arms[0]["tone"] == -0.45
        assert arms[1]["tone"] == -0.50
        assert arms[2]["tone"] == -0.40
        assert "Rogue A.I. Agents" in arms[0]["piece"]
        assert "Dismissed Employee Security Warnings" in arms[1]["piece"]
        assert "F.T.C. Investigates" in arms[2]["piece"]
        assert arms[2]["register"] == "regulatory_enforcement"

    def test_m910_carried_meta_arms(self):
        b = self._block()
        meta = b["meta_arms_carried"]
        tones = [a["tone"] for a in meta]
        assert tones == [-0.65, 0.0]
        assert b["illustrative_delta"]["openai_arm_mean"] == -0.45
        assert b["illustrative_delta"]["meta_register_range"] == [-0.65, 0.0]
        assert "INSIDE" in b["illustrative_delta"]["placement"]

    def test_m910_valuation_arm_contrast(self):
        b = self._block()
        contrast = b["illustrative_delta"]["valuation_arm_contrast"]
        assert "-0.60" in contrast
        assert "+0.15" in contrast
        assert "register follows the peg, not the entity" in contrast

    def test_m910_enforcement_cross_publication_uniformity(self):
        b = self._block()
        pair = b["illustrative_delta"]["enforcement_cross_publication"]
        assert "m901" in pair and "m904" in pair and "m907" in pair
        assert "uniform enforcement register" in pair
        assert "-0.40" in pair

    def test_m910_statistical_discipline(self):
        b = self._block()
        assert "MANUAL ILLUSTRATIVE scores only" in b["statistical_discipline"]
        assert "p_value/cohens_d/ci_95 NOT_CALCULATED" in b["statistical_discipline"]
        assert "is_significant: false" in b["statistical_discipline"]
        assert "Engine NOT run" in b["statistical_discipline"]
        assert "directionally_supported_not_proven" in b["statistical_discipline"]
        assert b["no_analysis_json_update"] is True

    def test_m910_not_falsification_member(self):
        b = self._block()
        assert "NOT a falsification-family member" in b["falsification_family"]
        assert "Ledger holds at 46" in b["falsification_family"]
        assert FORTY_SEVENTH_MEMBER not in b["falsification_family"]

    def test_m910_confounder_and_counterevidence_disclosure(self):
        b = self._block()
        conf = b["confounders_ranked"]
        assert len(conf["strong"]) == 3
        assert any("excerpt-bounded" in c for c in conf["strong"])
        counter = b["counterevidence"]
        assert len(counter) == 3
        assert any("+0.15 valuation" in c for c in counter)
        assert any("-0.65" in c for c in counter)

    def test_m910_research_method_and_sources(self):
        b = self._block()
        assert "7 browser.search query sets" in b["research_method"]
        assert "0 browser.open per #503" in b["research_method"]
        assert b["test_file"] == (
            "tests/test_type_a_1132_nyt_openai_sep28_oct01_crisis_"
            "accountability_register_vs_carried_meta_arms_oct01_7pm.py")
        assert len(b["source_urls"]) == 5


# ---------------------------------------------------------------------------
# 6. m911 qualitative discipline
# ---------------------------------------------------------------------------
class TestTypeDM911QualitativeDiscipline:
    def _block(self):
        with open(JOURNALISTS_FILE) as f:
            data = yaml.safe_load(f)
        return data["cherlynn_low"]["competitor_coverage"][KEY_911]

    def test_m911_run_metadata(self):
        b = self._block()
        assert b["iteration"] == 1133
        assert b["type"] == "B"
        assert b["journalist"] == "Cherlynn Low"
        assert b["publication"] == "engadget"
        assert b["block_key"] == KEY_911
        assert b["test_file"] == (
            "tests/test_type_b_1133_cherlynn_low_engadget_meta_connect_"
            "liveblog_vs_apple_watch_series_12_review_sep2026_8pm.py")

    def test_m911_meta_arm(self):
        b = self._block()
        arm = b["new_meta_arm"]
        assert "Meta Connect 2026 live" in arm["title"]
        assert arm["date"] == "Sep 23 2026"
        assert arm["tone_score"] == 0.0
        assert "MANUAL ILLUSTRATIVE" in arm["tone_basis"]
        assert "0 browser.open per #503" in arm["tone_basis"]

    def test_m911_apple_arm(self):
        b = self._block()
        arms = b["new_apple_arms"]
        review = [a for a in arms
                  if "Apple Watch Series 12 scored review" in a["arm"]][0]
        assert review["tone_score"] == 0.3
        assert "WWW.Engadget.com" in review["url"]
        assert "9.1/10" in " ".join(review["key_quotes"])
        assert "MANUAL ILLUSTRATIVE" in review["tone_basis"]

    def test_m911_register_contrast_arithmetic(self):
        b = self._block()
        contrast = b["register_contrast"]
        assert contrast["meta_arm_tone"] == 0.0
        assert contrast["illustrative_delta_apple_minus_meta"] == 0.3
        assert "0.30 - 0.0 = +0.30" in contrast["delta_calc"]
        assert "degenerate contract" in contrast["reading"]

    def test_m911_extends_m872_genre_bound(self):
        b = self._block()
        assert "m872" in b["mechanism_name"]
        assert "m872" in b["register_contrast"]["reading"]
        assert "genre-bound" in b["mechanism_name"] or \
            "GENRE-BOUND" in b["register_contrast"]["reading"]
        assert "+0.05 null" in b["register_contrast"]["reading"]

    def test_m911_not_falsification_member(self):
        b = self._block()
        assert b["falsification_family_member"] is False
        assert "NOT a falsification-family member" in b["falsification_family"]
        assert "ledger holds at 46" in b["falsification_family"]

    def test_m911_financial_relationship_no_gradient(self):
        b = self._block()
        fin = b["financial_relationship"]
        assert "no gradient" in fin["result"].lower() or \
            "No Engadget x Meta financial relationship" in fin["engadget_meta"]
        assert "Static Media" in fin["ownership_change"]

    def test_m911_statistical_discipline(self):
        b = self._block()
        disc = b["statistical_discipline"]
        assert "MANUAL" in disc
        assert "p_value NOT_CALCULATED" in disc
        assert "is_significant false" in disc
        assert "engine NOT run" in disc
        assert b["no_analysis_json_update"] is True


# ---------------------------------------------------------------------------
# 7. m912 qualitative discipline
# ---------------------------------------------------------------------------
class TestTypeDM912QualitativeDiscipline:
    def _block(self):
        with open(ENTITIES_FILE) as f:
            data = yaml.safe_load(f)
        return data[KEY_912]

    def test_m912_run_metadata(self):
        b = self._block()
        assert b["iteration"] == 1134
        assert b["iteration_type"] == "C"
        assert "NEGOTIATE-WHILE-COVERING" in b["mechanism_name"]
        assert b["verdict"] == "directionally_supported_not_proven"
        assert b["block_key"] == KEY_912
        assert b["connects_to"] == [519, 732, 882, 112]

    def test_m912_thirty_fourth_direction_taxonomy(self):
        b = self._block()
        tax = b["relationship_direction_taxonomy"]
        assert _T34 in tax
        assert "NEGOTIATE-WHILE-COVERING" in tax
        assert "m624" in tax and "m636" in tax  # distinct from #1 and #2
        assert "m909" in tax  # distinct from #33
        assert "m807 enumeration" in tax

    def test_m912_finding(self):
        b = self._block()
        finding = b["finding"]
        assert "John Georges" in finding
        assert "potential source of financial support for journalism" in finding
        assert "NOT a signed contract" in finding
        assert "$50M/yr" in finding or "$50M" in finding
        assert "m519" in finding

    def test_m912_negotiation_window_geometry(self):
        b = self._block()
        finding = b["finding"]
        assert "negotiation window" in finding
        assert "independence risk" in finding.lower() or \
            "independence" in finding.lower()
        assert "Kevin Hall" in finding

    def test_m912_coverage_stakes(self):
        b = self._block()
        finding = b["finding"]
        assert "Hyperion" in finding or "Louisiana" in finding
        assert "$180M" in finding or "settlement" in finding.lower()

    def test_m912_not_falsification_member(self):
        b = self._block()
        assert b["falsification_family_member"] is False
        assert b["tone_scored"] is False
        assert b["engine_run"] is False
        assert b["is_significant"] is False
        assert b["artifact_grade"] is False
        assert b["no_analysis_json_update"] is True
        assert "ledger holds at 46" in b["falsification_family"]

    def test_m912_direction_qualitative_boundary(self):
        b = self._block()
        # Type C financial-architecture mapping, not a coverage-tone
        # pair: no uniform-prediction test per the #754 convention.
        assert "no coverage-tone pair" in b["falsification_family"]
        assert FORTY_SEVENTH_MEMBER not in b["falsification_family"]

    def test_m912_sources(self):
        b = self._block()
        urls = [s["url"] for s in b["sources"]]
        assert len(urls) == 5
        assert all(s.get("novel") for s in b["sources"])


# ---------------------------------------------------------------------------
# 8. Falsification ledger
# ---------------------------------------------------------------------------
class TestTypeDFalsificationLedger1135:
    def test_forty_sixth_claim_in_exactly_one_profiles_file(self):
        hits = _git_grep_tracked(FORTY_SIXTH_MEMBER, "profiles/")
        assert hits == ["profiles/the-verge.yaml"], hits

    def test_forty_sixth_claim_count_is_designed(self):
        # The #1127 designed pattern: falsification_family prose +
        # falsification_family field in the m907 block.
        text = _read(VERGE_FILE)
        assert text.count(FORTY_SIXTH_MEMBER) == 2

    def test_no_forty_seventh_member_claim_profiles_wide(self):
        hits = _git_grep_tracked(FORTY_SEVENTH_MEMBER, "profiles/")
        assert hits == [], hits

    def test_thirty_fourth_direction_in_competitor_entities(self):
        hits = _git_grep_tracked(_T34, "profiles/competitor-entities.yaml")
        assert hits == ["profiles/competitor-entities.yaml"], hits

    def test_no_thirty_fifth_direction_claim_repo_wide(self):
        assert _git_grep_tracked(_T35) == []

    def test_m910_m911_m912_not_members_ledger_holds(self):
        # m910 (plaintiff prediction), m911 (genre-bound contrast,
        # no gradient), m912 (financial-architecture mapping) are
        # not uniform-prediction tests: the ledger holds at 46.
        with open(RESEARCH_FILE) as f:
            b910 = yaml.safe_load(f)[KEY_910]
        assert "Ledger holds at 46" in b910["falsification_family"]
        with open(JOURNALISTS_FILE) as f:
            b911 = yaml.safe_load(f)["cherlynn_low"]["competitor_coverage"][KEY_911]
        assert b911["falsification_family_member"] is False
        with open(ENTITIES_FILE) as f:
            b912 = yaml.safe_load(f)[KEY_912]
        assert b912["falsification_family_member"] is False


# ---------------------------------------------------------------------------
# 9. Forward-looking staleness (pin lifecycle, subprocess)
# ---------------------------------------------------------------------------
class TestTypeDForwardLookingStaleness1135:
    def test_1130_guard_lifecycle_stale_by_design(self):
        # #1130's TestGuardLifecycle1130 pinned max 909, zero-910
        # numeric/underscore/dash, no-new-below-max,
        # no-thirty-fourth-direction and no-forty-seventh-member.
        # The 910 (#1132), 911 (#1133) and 912 (#1134) landings plus
        # the THIRTY-FOURTH direction trip every pin. Designed
        # lifecycle; recorded, not repaired.
        res = _class_run(D1130_FILE, "TestGuardLifecycle1130")
        assert res.returncode != 0, res.stdout[-2000:]

    def test_1130_novelty_max_pin_stays_green_by_design(self):
        # #1130's TestNovelty1130::test_max_id_is_909 asserts the
        # git-grep hit LIST for "mechanism_id: 909" equals exactly
        # [profiles/competitor-entities.yaml]. The 910/911/912
        # landings do not remove 909 from competitor-entities.yaml,
        # so this pin STAYS GREEN by design of its weak formulation
        # (unlike #1125's _max_numeric_mechanism_id() == 906 pin,
        # which tripped on the 907 landing). Recorded, not repaired.
        res = _node_run(
            D1130_FILE, "TestNovelty1130::test_max_id_is_909")
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1131_staleness_pin_on_1130_lifecycle_flips_by_design(self):
        # #1131 pinned #1130's guard lifecycle still green at 7 PM
        # Oct 1; the m910 (#1132), m911 (#1133) and m912 (#1134)
        # landings trip it.
        res = _class_run(E1131_FILE, "TestStalenessPins")
        assert res.returncode != 0, res.stdout[-2000:]

    def test_1132_staleness_pins_still_correct(self):
        # #1132 recorded the designed end-states of #1130's
        # max-909/zero-910-numeric/zero-910-underscore-dash/
        # no-new-below-max pins. Type D lands nothing, so every
        # recorded state holds.
        res = _class_run(A1132_FILE, "TestTypeAForwardLookingStaleness1132")
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1133_supersession_pins_stale_by_design(self):
        # #1133's TestSupersessionPins1133 contains
        # test_1132_no_type_b_1133_in_git_log_passes_pre_commit,
        # which fails BY DESIGN post-#1133-commit ("Type B #1133"
        # now in git log). The remaining supersession pins (max-910
        # fail, zero-911-numeric fail, underscore/dash 911 stays
        # green, no-new-below-max fail, forty-seventh stays green,
        # thirty-fourth stays green) still hold their designed
        # states - only the pre-commit-only git-log pin trips. Type
        # D lands nothing; recorded, not repaired.
        res = _class_run(B1133_FILE, "TestSupersessionPins1133")
        assert res.returncode != 0, res.stdout[-2000:]

    def test_1134_supersession_pins_still_green(self):
        # #1134 recorded the designed end-states of #1133's
        # max-911/zero-912-numeric/thirty-fourth-absent pins and
        # the stays-green states of the 912 underscore/dash,
        # forty-seventh-absent, forty-sixth-intact and
        # thirty-third-intact pins. Type D lands nothing, so every
        # recorded state holds.
        res = _class_run(C1134_FILE, "TestSupersessionPins1134")
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1134_forward_guards_still_green(self):
        # #1134's forward guards (zero-913 numeric/underscore/dash,
        # no-thirty-fifth, format-built-only, iteration-log
        # absence discipline) stay green: this run adds no
        # mechanism.
        res = _class_run(C1134_FILE, "TestForwardGuards1134")
        assert res.returncode == 0, res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 10. Guard lifecycle (forward guards for #1136)
# ---------------------------------------------------------------------------
class TestGuardLifecycle1135:
    def test_1135_file_pins_max_id_912_and_next_913(self):
        assert _max_numeric_mechanism_id_in_profiles() == 912

    def test_zero_next_numeric_913_in_profiles(self):
        assert _git_grep_tracked(_mech_id_colon(NEXT_NUM), "profiles/") == []

    def test_zero_next_underscore_913_repo_wide(self):
        assert _git_grep_tracked(_mech_underscore(NEXT_NUM)) == []

    def test_zero_next_dash_913_repo_wide(self):
        assert _git_grep_tracked(_mech_dash(NEXT_NUM)) == []

    def test_no_new_mechanisms_below_max(self):
        ids = []
        for dirpath, _, files in os.walk(PROFILES_DIR):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = _read(os.path.join(dirpath, fn))
                    ids += [int(m) for m in re.findall(
                        r"mechanism_id: (\d+)", text)]
        assert 912 in ids
        assert all(i <= 912 for i in ids)

    def test_no_thirty_fifth_direction_claim(self):
        hits = [p for p in _git_grep_tracked(_T35)]
        assert hits == [], hits

    def test_no_forty_seventh_member_claim(self):
        hits = [p for p in _git_grep_tracked(FORTY_SEVENTH_MEMBER)]
        assert hits == [], hits


# ---------------------------------------------------------------------------
# 11. Background-suite verdict (#1130 suite)
# ---------------------------------------------------------------------------
class TestBackgroundSuiteVerdict1135:
    def _log_stats(self):
        text = _read(PRIOR_SUITE_LOG)
        return (os.path.getsize(PRIOR_SUITE_LOG), text.count("."),
                text.count("F"), text.count("E"), text)

    def test_prior_suite_died_tenth_consecutive(self):
        # The #1130-launched background full suite DIED: 3874
        # bytes (3479 dots, ~5% progress), last write Oct 1
        # 19:10 PDT, zero summary tokens (no "passed"/"failed"
        # summary, no collected-count token), no live pytest
        # process. Per the #795 convention this is recorded as
        # DIED, not "interrupted": the run produces no usable
        # verdict.
        size, dots, fails, errors, text = self._log_stats()
        assert size == 3874, size
        assert dots == 3479, dots
        assert fails == 0, fails
        assert errors == 0, errors
        assert "passed" not in text
        assert "failed" not in text
        assert " collected " not in text
        assert "no tests ran" not in text

    def test_no_live_pytest_process(self):
        # The bracket pattern avoids self-matching the pgrep
        # command line (phantom-pid class per AGENTS.md).
        result = subprocess.run(
            ["pgrep", "-f", "[p]ytest.*type_d_1130"],
            capture_output=True,
            text=True,
        )
        assert result.returncode != 0, (
            "a pytest process for the #1130 suite must not still be "
            "alive when its verdict is recorded")

    def test_tombstone_lineage_advances_to_86th(self):
        # TENTH consecutive background-suite death of the new streak
        # (the 57-run streak ENDED at #1085 when the #1080 suite
        # completed). Tombstone lineage advances EIGHTY-FIFTH ->
        # EIGHTY-SIXTH; recorded in the #1135 iteration-log entry.
        # Deselected pre-commit (log entry is written in the
        # log-hash step per #721).
        text = _read(LOG_FILE)
        assert "EIGHTY-SIXTH" in text


# ---------------------------------------------------------------------------
# 12. Fresh synthetic engine calibration (new values, not #1130's)
# ---------------------------------------------------------------------------
class TestSyntheticEngineCalibration1135:
    # Scratch-run values produced at this run (Thu 2026-10-01 ~22:05
    # PDT) via mediascope.score.asymmetry.calculate_asymmetry with
    # its real signature (target_scores, peer_scores,
    # target_entity, peer_entities, publication_slug,
    # period_start, period_end). The finding layer stays MANUAL
    # ILLUSTRATIVE ONLY: the engine is never promoted to findings,
    # and these numbers are NOT a corpus claim.

    def _calculate(self):
        from datetime import datetime

        from mediascope.score.asymmetry import calculate_asymmetry

        def calc(target_scores, peer_scores):
            return calculate_asymmetry(
                target_scores,
                peer_scores,
                "Meta",
                ["Anthropic", "OpenAI"],
                "synthetic-calibration",
                datetime(2026, 10, 1),
                datetime(2026, 10, 1),
            )

        return calc

    def test_strong_effect_is_significant(self):
        calc = self._calculate()
        meta = [-0.61, -0.54, -0.67, -0.59, -0.63, -0.57, -0.66]
        comp = [0.15, -0.08, 0.21, 0.05, -0.02, 0.11, -0.06]
        result = calc(meta, comp)
        assert result.asymmetry_score == pytest.approx(-0.6614285714285714)
        assert result.t_statistic == pytest.approx(-14.575900932975928)
        assert result.p_value < 1e-6
        assert result.cohens_d == pytest.approx(-7.791146770679224)
        assert result.is_significant is True
        assert result.confidence_interval_lower == pytest.approx(-0.74)
        assert result.confidence_interval_upper == pytest.approx(-0.5842142857142858)
        # The strong arm-swap negates the asymmetry exactly.
        swapped = calc(comp, meta)
        assert swapped.asymmetry_score == pytest.approx(0.6614285714285714)

    def test_near_null_pair_stays_silent(self):
        calc = self._calculate()
        meta = [0.04, -0.03, 0.02, -0.05, 0.06, -0.01, 0.03]
        comp = [-0.02, 0.05, -0.06, 0.01, -0.04, 0.03, -0.05]
        result = calc(meta, comp)
        assert result.asymmetry_score == pytest.approx(0.019999999999999997)
        assert result.p_value > 0.05
        assert result.is_significant is False

    def test_degenerate_n1_contract(self):
        # The classic degenerate guard: n=1 per arm yields t=0.0,
        # p=1.0, d=0.0 and is_significant False regardless of the
        # illustrative pair mean.
        calc = self._calculate()
        result = calc([-0.45], [-0.40])
        assert result.asymmetry_score == pytest.approx(-0.05)
        assert result.t_statistic == 0.0
        assert result.p_value == 1.0
        assert result.cohens_d == 0.0
        assert result.is_significant is False

    def test_engine_layer_not_finding_layer(self):
        # The m910/m911/m912 mechanisms never promote engine
        # significance to a finding: all three carry finding-layer
        # is_significant False (or tone NOT_SCORED for the Type C).
        with open(RESEARCH_FILE) as f:
            b910 = yaml.safe_load(f)[KEY_910]
        assert "is_significant: false" in b910["statistical_discipline"]
        with open(JOURNALISTS_FILE) as f:
            b911 = yaml.safe_load(f)["cherlynn_low"]["competitor_coverage"][KEY_911]
        assert "is_significant false" in b911["statistical_discipline"]
        with open(ENTITIES_FILE) as f:
            b912 = yaml.safe_load(f)[KEY_912]
        assert b912["is_significant"] is False
        assert b912["engine_run"] is False


# ---------------------------------------------------------------------------
# 13. Suite re-launch
# ---------------------------------------------------------------------------
class TestSuiteRelaunch1135:
    def test_relaunch_log_path_written(self):
        # The re-launched full suite log exists in goal hidden_files
        # (created by this run's background launch before commit).
        assert os.path.exists(SUITE_LOG), (
            "the #1135 background suite must be re-launched to "
            + SUITE_LOG
            + " before the main commit"
        )

    def test_relaunch_log_is_full_inventory(self):
        # The re-launch runs WITHOUT -x: the full inventory
        # (calendar by-design failures included) is needed for the
        # #1140 triage. The log must hold pytest progress output,
        # not just a header.
        text = _read(SUITE_LOG)
        assert text.count(".") > 100, (
            "the re-launched suite log should accumulate dot "
            "progress; got %d dots" % text.count(".")
        )

    def test_next_type_d_run_owns_the_verdict(self):
        # Per the #795 convention, the NEXT Type D run (#1140)
        # checks this suite's verdict; this run only records the
        # launch.
        assert "type_d_1135_full_suite.log" in SUITE_LOG


# ---------------------------------------------------------------------------
# 14. Doc-sync per #719 (fails pre-commit by design; passes post-sync)
# ---------------------------------------------------------------------------
class TestTypeDDocSync1135:
    def _readme(self):
        return _read(README_FILE)

    def test_readme_stats_ratchet(self):
        text = self._readme()
        assert "| Tests | %d |" % README_TEST_COUNT in text
        assert "| %d | Across %d test files |" % (
            README_TEST_COUNT, README_FILE_COUNT) in text

    def test_readme_test_table_row(self):
        assert TEST_BASENAME in self._readme()

    def test_architecture_tree_row(self):
        assert TEST_BASENAME in _read(ARCH_FILE)

    def test_constants_patched(self):
        own = _read(__file__)
        assert "README_TEST_COUNT = 59520" in own
        assert "README_FILE_COUNT = 1460" in own


# ---------------------------------------------------------------------------
# 15. Iteration log per #721 (fails pre-commit by design)
# ---------------------------------------------------------------------------
class TestTypeDIterationLog1135:
    def _entry(self):
        return _read(LOG_FILE)

    def test_iteration_log_entry_present(self):
        assert "## #1135 Type D" in self._entry()

    def test_iteration_log_hashes_registered(self):
        text = self._entry()
        assert ANCHORED_SHA in text
        assert "1135-1139 window" in text

    def test_iteration_log_rotation_guard(self):
        text = self._entry()
        assert "FIRST leg" in text
        assert "D->E->A->B->C" in text


# ---------------------------------------------------------------------------
# 16. In-flight isolation
# ---------------------------------------------------------------------------
class TestInflightIsolation1135:
    def test_no_concurrent_inflight_iteration_commits_staged(self):
        # The in-flight #899/#938/#900/#1012-wt working-tree edits
        # are owned by their runs; this run stages only its own
        # files. (Pre-staging this passes vacuously; it guards the
        # post-staging state before commit. Naive "no ## #899
        # entries" substring checks are unsound: the historical
        # log prose from Sep 21 cites those numbers.)
        status = _git("status", "--short")
        staged = [line for line in status.splitlines()
                  if line.startswith(("M ", "A "))]
        for f in (
            "nytimes.yaml",
            "test_type_b_938_",
            "test_type_d_900_",
            "test_type_a_1012_",
        ):
            assert not any(f in line for line in staged), (f, staged)

    def test_this_run_touches_no_corpus_files(self):
        # Type D verification touches no corpus files; the staged
        # set for this run is the new test file + docs only. The
        # pre-existing uncommitted hunks (#899 nytimes.yaml, #938,
        # #1012-wt) are owned by their runs and stay unstaged.
        out = _git("diff", "--cached", "--name-only")
        staged = [line for line in out.split("\n") if line.strip()]
        for path in staged:
            assert path.startswith(("tests/", "README.md",
                                    "docs/ARCHITECTURE.md",
                                    "iteration-log.md")), path
