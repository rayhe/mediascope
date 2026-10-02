"""Type D -- Iteration #1140 (Fri 2026-10-02 03:00 PDT): m913/m914/m915
qualitative-discipline verification + post-1135-1139 corpus integrity
(max numeric mechanism_id 915; zero next-number 916 keys in
numeric/underscore/dash mechanism forms - the 916 needles are
format-built per #715 so no guard-literal carrier file exists; the
m913/m914/m915 block keys carry no mechanism-number substring
(designed keying), so they are plain literals; the #1136/#1137/#1138/
#1139 window files are NOT edited by this run - their now-stale
forward-looking pins are recorded as fail-by-design via subprocess in
the staleness class (#1135's max-912 + zero-913-numeric +
no-new-below-max + no-thirty-fifth-direction guards trip on the
landed 913/914/915 and the THIRTY-FIFTH direction; #1136's staleness
pin on #1135's guard lifecycle flips; #1137/#1138/#1139 supersession
+ forward-guard pins STAY GREEN - Type D lands no mechanism); ledger
holds at 46 with the FORTY-SIXTH member-claim form present in exactly
one profiles file (profiles/the-verge.yaml, m907 block, 2 occurrences
- the #1127 designed pattern) and the forty-seventh member-claim form
absent repo-wide (needle format-built per #715); the THIRTY-FIFTH
relationship direction is present in competitor-entities.yaml (m915
METER-THEN-INVITE, landed at #1139); the thirty-sixth relationship-
direction claim form is absent repo-wide (needle format-built per
#715)) + the #1135 background-suite verdict (DIED at 1843 bytes /
1659 dots ~2% with last write Oct 1 23:02 PDT and zero summary
tokens, no live pytest process - ELEVENTH consecutive
background-suite death of the new streak; the 57-run streak ENDED at
#1085 when the #1080 suite completed; tombstone lineage advances
EIGHTY-SIXTH -> EIGHTY-SEVENTH) + fresh synthetic engine calibration
(new values, not #1135's) + re-launch of the full suite as a background
process writing to goal hidden_files type_d_1140_full_suite.log WITHOUT
-x (the full inventory, calendar by-design failures included, is needed
for the #1145 triage; the next Type D run checks its verdict per the
#795 convention).

Type D FIRST leg of the 1140-1144 window, OPENING it
(D->E->A->B->C). Committed predecessor #1139 Type C (2:00 AM PDT Oct 2)
CLOSED the 1135-1139 window (D #1135, E #1136, A #1137, B #1138,
C #1139). Rotation per the #565 anchor + rotation guard.
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
(FOURTEENTH, exclusionary-diversion): Ray's revert/leave/rebuild
decision still pending - not an assistant repair task.

Verifies:
- m913 (Type A #1137, profiles/atlantic.yaml
  competitor_relationships/openai 4-space block key,
  `mechanism_id: 913` field form; block key count 1 - colon-form
  line only, designed: no block_key or test_file field echoing the
  block key in the m913 block): The Atlantic's Sep-26/Oct-1 2026
  OpenAI crisis-window posture - bounded-absence silence across four
  crisis pegs (Sep-26 rogue-agent disclosure, Sep-29 LASST Hugging
  Face lawsuit, Sep-28 Astra cancellation, Sep-30 FTC agent-safety
  probe) plus the Sep-29 Kevin Roose 2017-AGI-auction book excerpt
  (newslocker relay, historical register, tone NOT_SCORED) vs
  carried Meta AI Watchdog arms (m481: -0.75/-0.55). Register-
  AVAILABILITY finding, not mean-tone (per #1127): the
  accountability register is unavailable for the licensing partner
  on these pegs while available for Meta and for the same pegs at
  six peer publications. May 29 2024 Atlantic-OpenAI licensing deal
  is the standing financial context (coverage_prediction
  "softer"). NOT a falsification-family member; ledger holds at
  46.
- m914 (Type B #1138, profiles/careers/journalists.yaml
  stevie_bonifield competitor_coverage 4-space block key,
  `mechanism_id: 914` field form; block key count 2 - colon-form
  line + block_key field, designed): Stevie Bonifield (The Verge)
  Sep-24 Meta Connect 2026 product-positive recap (+0.10, "the star
  of the event", zero privacy interrogation) vs Apr-16 Google Gucci
  glasses fashion-partnership news (+0.15) - competitive
  quote-inclusion: Spiegel's anti-Meta brand diss ("the Meta brand
  ... not something people want anywhere near their face")
  platformed inside the Google arm. Illustrative delta +0.05
  near-null; STRONG 5-month temporal confound. EXTENDS m150's
  quote-inclusion observation to a second writer/outlet. No Vox
  x Google / Vox x Meta financial gradient found. NOT a
  falsification-family member; ledger holds at 46.
- m915 (Type C #1139, profiles/competitor-entities.yaml zero-indent
  top-level block key, `mechanism_id: 915` field form; block key
  count 2 - colon-form line + block_key field, designed): SPUR
  releases the content telemetry standard and invites OpenAI,
  Anthropic, Google, Meta, Microsoft onto an invitation-only AI
  Licensing Advisory Board (Oct 2 2026) - METER-THEN-INVITE as the
  THIRTY-FIFTH relationship direction per the m807 enumeration:
  the publishers collectively build the usage-measurement
  infrastructure, then invite the metered labs into its governance
  (meter-designer seats the metered at the rule-making table).
  connects_to [514, 891, 912]; distinct from #27 unilateral pricing
  m891 (opposite designer/invitation arrow), #21 metered-recycling
  m873 (different metered object), #15 ecosystem-grant m852
  (consideration-is-the-point). Metering channel OPEN at $0
  pre-monetization; governance channel OPEN as invitation (~20
  seats, none confirmed). 6 novel sources (Digiday/Guaglione
  primary). Tone NOT_SCORED; engine NOT run; NOT a
  falsification-family member; ledger holds at 46.

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
ATLANTIC_FILE = os.path.join(PROFILES_DIR, "atlantic.yaml")
JOURNALISTS_FILE = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
ENTITIES_FILE = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
VERGE_FILE = os.path.join(PROFILES_DIR, "the-verge.yaml")
LOG_FILE = os.path.join(REPO_ROOT, "iteration-log.md")
README_FILE = os.path.join(REPO_ROOT, "README.md")
ARCH_FILE = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")

# Block keys are plain literals: none carries a mechanism-number
# substring (designed keying per #715).
KEY_913 = ("type_a_1137_atlantic_openai_sep26_oct01_crisis_window_"
           "silence_historical_register_vs_meta_watchdog_oct02_12am")
KEY_914 = ("type_b_1138_stevie_bonifield_verge_meta_connect_recap_"
           "vs_google_gucci_glasses_sep2026")
KEY_915 = ("type_c_1139_spur_telemetry_standard_ai_licensing_"
           "advisory_board_meter_then_invite_thirty_fifth_direction_"
           "oct02_2am")
OWN_BASENAME = ("test_type_d_1140_m913_m914_m915_qualitative_"
                "corpus_integrity_oct02_3am.py")

# Predecessor test files for supersession pins.
D1135_FILE = ("test_type_d_1135_m910_m911_m912_qualitative_"
              "corpus_integrity_oct01_10pm.py")
E1136_FILE = ("test_type_e_1136_podcast_sentiment_"
              "150th_verification_oct01_11pm.py")
A1137_FILE = ("test_type_a_1137_atlantic_openai_sep26_oct01_crisis_"
              "window_silence_historical_register_vs_meta_watchdog_"
              "oct02_12am.py")
B1138_FILE = ("test_type_b_1138_stevie_bonifield_verge_meta_connect_"
              "recap_vs_google_gucci_glasses_oct02_1am.py")
C1139_FILE = ("test_type_c_1139_spur_telemetry_standard_"
              "advisory_board_meter_then_invite_oct02_2am.py")

# Prior-window background suite (verdict rendered this run) and this
# run's re-launched suite.
PRIOR_SUITE_LOG = os.path.join(
    os.path.expanduser("~"),
    "workspace",
    "goals",
    "mediascope-meta-wearables-press-analysis",
    "hidden_files",
    "type_d_1135_full_suite.log",
)
SUITE_LOG = os.path.join(
    os.path.expanduser("~"),
    "workspace",
    "goals",
    "mediascope-meta-wearables-press-analysis",
    "hidden_files",
    "type_d_1140_full_suite.log",
)

# Patched post-commit once README/ARCHITECTURE doc-sync lands.
README_TEST_COUNT = 59880  # post-doc-sync total (59796 + 84)
README_FILE_COUNT = 1465  # post-doc-sync total
TEST_BASENAME = OWN_BASENAME

# Anchor placeholder per #565: patched to the main commit's 40-char SHA in the
# anchor followup. Deselect the placeholder test in post-commit full runs.
ANCHORED_SHA = "48062ab54603fdfb7b5b1561007ca52891199cc8"

MECH_NUM = 915
NEXT_NUM = 916
PREV_NUM = 914

# Fragment-built direction needles per #715 (never contiguous here).
_T34 = "THIRTY-" + "FOURTH relationship direction"
_T35 = "THIRTY-" + "FIFTH relationship direction"
_T36 = "THIRTY-" + "SIXTH relationship direction"


# Format-built mechanism needles per #715/#770 (never contiguous here).
def _mech_underscore(n):
    return "mechanism" + "_%d" % n


def _mech_dash(n):
    return "mechanism" + "-%d" % n


def _mech_id_colon(n):
    return "mechanism_id: %d" % n


FORTY_SIXTH_MEMBER = "FORTY" + "-SIXTH falsification-family member"
FORTY_SEVENTH_MEMBER = "FORTY" + "-SEVENTH falsification-family member"

# One-parse-per-file cache: the journalists/entities YAMLs are large
# and re-parsing per test method is pure waste (tests never mutate).
_YAML_CACHE = {}


def _yaml(path):
    if path not in _YAML_CACHE:
        with open(path, "r", encoding="utf-8") as f:
            _YAML_CACHE[path] = yaml.safe_load(f)
    return _YAML_CACHE[path]


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
        cmd, cwd=REPO_ROOT, capture_output=True, text=True, timeout=120,
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
        timeout=300,
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
        timeout=300,
    )


# ---------------------------------------------------------------------------
# 1. Novelty
# ---------------------------------------------------------------------------
class TestNovelty1140:
    def test_no_type_d_1140_test_file_preexisting(self):
        hits = glob.glob(
            os.path.join(TESTS_DIR, "test_type_d_1140*.py"))
        assert hits == [os.path.join(TESTS_DIR, OWN_BASENAME)], hits

    def test_no_type_d_1140_in_git_log(self):
        # Deselected pre-commit per #565: the main commit does not
        # exist yet.
        log = _git("log", "--oneline", "--grep=Type D #1140")
        assert "Type D #1140" in log, log

    def test_max_id_is_915(self):
        needle = _mech_id_colon(MECH_NUM)
        hits = _git_grep_tracked(needle, "profiles/")
        assert hits == ["profiles/competitor-entities.yaml"], hits

    def test_zero_916_numeric_forms_in_profiles(self):
        needle = _mech_id_colon(NEXT_NUM)
        assert _git_grep_tracked(needle, "profiles/") == []

    def test_block_keys_unique_in_home_yamls(self):
        assert _key_count_in_file(KEY_913, ATLANTIC_FILE) == 1
        assert _key_count_in_file(KEY_914, JOURNALISTS_FILE) == 2
        assert _key_count_in_file(KEY_915, ENTITIES_FILE) == 2
        # Designed keying: no mechanism-number substring in any
        # block key, so they are plain literals here.
        for key in (KEY_913, KEY_914, KEY_915):
            assert "913" not in key and "914" not in key and "915" not in key

    def test_no_type_e_1141_in_git_log(self):
        # The next leg must not exist yet.
        log = _git("log", "--oneline", "--grep=Type E #1141")
        assert "Type E #1141" not in log, log


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------
class TestTypeDRotationGuard1140:
    def test_rotation_window_opens_1140(self):
        # 1140-1144 window: D opens, then E -> A -> B -> C.
        log = _git("log", "--oneline", "--grep=Type C #1139")
        assert "Type C #1139" in log, log
        entry = _read(LOG_FILE)
        assert "1135-1139 window CLOSED" in entry

    def test_predecessor_1139_chain_present(self):
        log = _git("log", "--format=%H %s")
        assert "Type C #1139" in log, log
        for sha8 in ("03622895", "1ae8073e", "c9b9c3e6", "1703bfbe"):
            assert sha8 in log, sha8

    def test_anchor_sha_is_real(self):
        # Deselected pre-commit: patched in the anchor followup.
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA
        assert ANCHORED_SHA != "0" * 40


# ---------------------------------------------------------------------------
# 3. Novelty anchor
# ---------------------------------------------------------------------------
class TestTypeDNoveltyAnchor1140:
    def test_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per #565: the main commit does not
        # exist yet. Post-commit this asserts the single #1140
        # commit is the anchor and carries the test-file changes.
        log = _git("log", "--format=%H %s", "--grep=Type D #1140")
        assert "Type D #1140" in log
        assert ANCHORED_SHA in log


# ---------------------------------------------------------------------------
# 4. Corpus integrity
# ---------------------------------------------------------------------------
class TestTypeDCorpusIntegrity1140:
    def test_m913_block_present_in_atlantic_yaml(self):
        data = _yaml(ATLANTIC_FILE)
        block = data["competitor_relationships"]["openai"][KEY_913]
        assert block["mechanism_id"] == 913
        assert block["iteration_type"] == "A"

    def test_m914_block_present_in_journalists_yaml(self):
        data = _yaml(JOURNALISTS_FILE)
        block = data["stevie_bonifield"]["competitor_coverage"][KEY_914]
        assert block["mechanism_id"] == 914
        assert block["type"] == "B"

    def test_m915_block_present_in_competitor_entities_yaml(self):
        data = _yaml(ENTITIES_FILE)
        block = data[KEY_915]
        assert block["mechanism_id"] == 915
        assert block["iteration_type"] == "C"

    def test_max_mechanism_id_is_915(self):
        assert _max_numeric_mechanism_id_in_profiles() == 915

    def test_zero_916_forms_repo_wide(self):
        assert _git_grep_tracked(_mech_id_colon(916)) == []
        assert _git_grep_tracked(_mech_underscore(916)) == []
        assert _git_grep_tracked(_mech_dash(916)) == []

    def test_m913_key_count_is_designed(self):
        # Colon-form line only; no block_key or test_file field
        # echoes the block key in the m913 block.
        assert _key_count_in_file(KEY_913, ATLANTIC_FILE) == 1

    def test_m914_key_count_is_designed(self):
        # Colon-form line + block_key field.
        assert _key_count_in_file(KEY_914, JOURNALISTS_FILE) == 2

    def test_m915_key_count_is_designed(self):
        # Colon-form line + block_key field.
        assert _key_count_in_file(KEY_915, ENTITIES_FILE) == 2


# ---------------------------------------------------------------------------
# 5. m913 qualitative discipline
# ---------------------------------------------------------------------------
class TestTypeDM913QualitativeDiscipline:
    def _block(self):
        return _yaml(ATLANTIC_FILE)["competitor_relationships"][
            "openai"][KEY_913]

    def test_m913_run_metadata(self):
        b = self._block()
        assert b["mechanism_id"] == 913
        assert b["iteration"] == 1137
        assert b["iteration_type"] == "A"
        assert b["publication"] == "The Atlantic"
        assert b["competitor"] == "OpenAI"
        assert b["comparator_entity"] == "Meta"

    def test_m913_finding_register_availability(self):
        b = self._block()
        finding = b["finding"]
        assert "bounded" in finding and "absence" in finding
        assert "register-AVAILABILITY" in finding
        assert "HISTORICAL register" in finding
        assert "m694" in finding
        assert "NOT a" in finding and "falsification-family member" in finding

    def test_m913_crisis_pegs(self):
        b = self._block()
        pegs = b["crisis_pegs_peer_registers"]
        assert len(pegs) == 4
        peg_text = " ".join(p["peg"] for p in pegs)
        assert "rogue-agent" in peg_text
        assert "LASST" in peg_text
        assert "Astra" in peg_text
        assert "FTC" in peg_text
        registers = " ".join(p["peer_register"] for p in pegs)
        assert "-0.35 to -0.50" in registers

    def test_m913_roose_excerpt_arm(self):
        b = self._block()
        surface = b["atlantic_surface_sep29_week"][0]
        assert "newslocker.com" in surface["relay_url"]
        assert "auction" in surface["title"].lower()
        assert surface["register"] == "historical_book_excerpt"
        assert "NOT_SCORED" in surface["manual_illustrative_tone"]

    def test_m913_carried_meta_arms(self):
        b = self._block()
        arms = b["meta_arms_carried_from_481"]
        tones = [a["manual_illustrative_tone"] for a in arms]
        assert tones == [-0.75, -0.55]
        assert all(a["register"] == "accountability_investigation"
                   for a in arms)
        assert b["scorer_manual_illustrative"]["peer_scores"] == [-0.75, -0.55]

    def test_m913_financial_context(self):
        b = self._block()
        fin = b["financial_context"]
        assert "May 29 2024" in fin["openai_deal"]
        assert fin["coverage_prediction"] == "softer"
        assert fin["meta_deal"] == "$0, no AI licensing relationship"

    def test_m913_statistical_discipline(self):
        b = self._block()
        assert "NOT_CALCULATED" in b["statistical_discipline"]
        assert "is_significant False" in b["statistical_discipline"]
        assert "engine NOT run" in b["statistical_discipline"]
        assert "directionally_supported_not_proven" in \
            b["statistical_discipline"]
        assert b["no_analysis_json_update"] is True

    def test_m913_not_falsification_member(self):
        b = self._block()
        assert "NOT a falsification-family member" in \
            b["falsification_family"]
        assert "Ledger holds at 46" in b["falsification_family"]
        assert FORTY_SEVENTH_MEMBER not in b["falsification_family"]
        assert b["ledger"] == "Ledger holds at 46"

    def test_m913_confounder_and_counterevidence_disclosure(self):
        b = self._block()
        conf = b["confounders_ranked"]
        assert len(conf["strong"]) == 2
        assert any("Search-index bounded absence" in c
                   for c in conf["strong"])
        counter = b["counter_evidence"]
        assert len(counter) == 3
        assert any("m694" in c for c in counter)
        assert "4 browser.search query sets" in b["research_method"]
        assert "0 browser.open" in b["research_method"]
        assert len(b["source_urls"]) == 2


# ---------------------------------------------------------------------------
# 6. m914 qualitative discipline
# ---------------------------------------------------------------------------
class TestTypeDM914QualitativeDiscipline:
    def _block(self):
        return _yaml(JOURNALISTS_FILE)["stevie_bonifield"][
            "competitor_coverage"][KEY_914]

    def test_m914_run_metadata(self):
        b = self._block()
        assert b["mechanism_id"] == 914
        assert b["iteration"] == 1138
        assert b["type"] == "B"
        assert b["journalist"] == "Stevie Bonifield"
        assert b["publication"] == "theverge"
        assert b["block_key"] == KEY_914
        assert b["test_file"] == (
            "tests/test_type_b_1138_stevie_bonifield_verge_meta_connect_"
            "recap_vs_google_gucci_glasses_oct02_1am.py")

    def test_m914_meta_arm(self):
        b = self._block()
        arm = b["new_meta_arm"]
        assert "Meta Connect 2026" in arm["title"]
        assert arm["date"] == "Sep 24 2026"
        assert arm["tone_score"] == 0.1
        assert "Zero privacy/surveillance vocabulary" in \
            arm["register_notes"]
        assert "MANUAL ILLUSTRATIVE" in arm["tone_basis"]

    def test_m914_google_arm(self):
        b = self._block()
        arm = b["new_google_arm"]
        assert "Gucci" in arm["title"]
        assert arm["date"] == "Apr 16 2026"
        assert arm["tone_score"] == 0.15
        quotes = " ".join(arm["key_quotes"])
        assert "not something people want anywhere near their face" in \
            quotes
        assert "MANUAL ILLUSTRATIVE" in arm["tone_basis"]

    def test_m914_register_contrast_arithmetic(self):
        b = self._block()
        contrast = b["register_contrast"]
        assert contrast["meta_arm_tone"] == 0.1
        assert contrast["google_arm_tone"] == 0.15
        assert contrast["illustrative_delta_google_minus_meta"] == 0.05
        assert "0.15 - 0.10 = +0.05" in contrast["delta_calc"]
        assert "m150" in contrast["reading"]
        assert "QUOTE-INCLUSION" in contrast["reading"]

    def test_m914_financial_relationship_no_gradient(self):
        b = self._block()
        fin = b["financial_relationship"]
        assert "No Vox Media x Google financial relationship" in \
            fin["verge_google"]
        assert "No Vox Media x Meta financial relationship" in \
            fin["verge_meta"]
        assert "no financial gradient" in fin["result"].lower() or \
            "No payer-softening prediction is testable" in fin["test"]

    def test_m914_statistical_discipline(self):
        b = self._block()
        disc = b["statistical_discipline"]
        assert "MANUAL" in disc
        assert "NOT_CALCULATED" in disc
        assert "is_significant false" in disc
        assert "engine NOT run" in disc
        assert b["no_analysis_json_update"] is True

    def test_m914_confounder_and_counterevidence(self):
        b = self._block()
        conf = b["confounders"]
        assert any("STRONG: temporal gap" in c for c in conf)
        assert any("~5 months" in c for c in conf)
        counter = b["counterevidence"]
        assert len(counter) == 3
        assert any("+0.10" in c for c in counter)

    def test_m914_not_falsification_member(self):
        b = self._block()
        assert b["falsification_family_member"] is False
        assert b["falsification_ledger"] == 46
        assert "NOT a falsification-family member" in \
            b["falsification_family"]
        assert "ledger holds at 46" in b["falsification_family"]
        assert FORTY_SEVENTH_MEMBER not in b["ledger_note"]


# ---------------------------------------------------------------------------
# 7. m915 qualitative discipline
# ---------------------------------------------------------------------------
class TestTypeDM915QualitativeDiscipline:
    def _block(self):
        return _yaml(ENTITIES_FILE)[KEY_915]

    def test_m915_run_metadata(self):
        b = self._block()
        assert b["mechanism_id"] == 915
        assert b["iteration"] == 1139
        assert b["iteration_type"] == "C"
        assert b["block_key"] == KEY_915
        assert b["connects_to"] == [514, 891, 912]
        assert b["verdict"] == "directionally_supported_not_proven"

    def test_m915_thirty_fifth_direction_taxonomy(self):
        b = self._block()
        tax = b["relationship_direction_taxonomy"]
        assert _T35 in tax
        assert "METER-THEN-INVITE" in tax
        assert "m807 enumeration" in tax
        assert "m891" in tax  # distinct from #27 unilateral pricing
        assert "m873" in tax  # distinct from #21 metered-recycling
        assert "m852" in tax  # distinct from #15 ecosystem-grant

    def test_m915_finding(self):
        b = self._block()
        finding = b["finding"]
        assert "SPUR" in finding
        assert "Digiday" in finding
        assert "Guaglione" in finding
        assert "telemetry" in finding
        assert "AI Licensing Advisory Board" in finding
        assert "m514" in finding

    def test_m915_money_flow(self):
        b = self._block()
        flow = b["money_flow"]
        assert "Metering channel" in flow
        assert "$0" in flow
        assert "pre-monetization" in flow
        assert "Governance channel" in flow
        assert "invitation" in flow

    def test_m915_not_falsification_member(self):
        b = self._block()
        assert b["falsification_family_member"] is False
        assert b["tone_scored"] is False
        assert b["engine_run"] is False
        assert b["is_significant"] is False
        assert b["artifact_grade"] is False
        assert b["no_analysis_json_update"] is True
        assert "ledger holds at 46" in b["falsification_family"]
        assert FORTY_SEVENTH_MEMBER not in b["falsification_family"]

    def test_m915_sources(self):
        b = self._block()
        urls = [s["url"] for s in b["sources"]]
        assert len(urls) == 6
        assert all(s.get("novel") for s in b["sources"])
        assert any("digiday" in u for u in urls)

    def test_m915_coverage_nexus(self):
        b = self._block()
        nexus = b["coverage_nexus"]
        assert "Guardian" in nexus
        assert "Slade" in nexus
        assert "m514" in nexus

    def test_m915_statistical_discipline(self):
        b = self._block()
        # Type C financial-architecture mapping, not a coverage-tone
        # pair: no uniform-prediction test per the #754 convention.
        assert "no coverage-tone pair" in b["falsification_family"]
        assert "FIRST dedicated corpus mechanism" in b["novelty"]
        assert b["yaml_parse_clean"] is True
        assert b["ascii_only"] is True
        assert b["verdict"] == "directionally_supported_not_proven"


# ---------------------------------------------------------------------------
# 8. Falsification ledger
# ---------------------------------------------------------------------------
class TestTypeDFalsificationLedger1140:
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

    def test_thirty_fifth_direction_in_competitor_entities(self):
        hits = _git_grep_tracked(_T35, "profiles/competitor-entities.yaml")
        assert hits == ["profiles/competitor-entities.yaml"], hits

    def test_no_thirty_sixth_direction_claim_repo_wide(self):
        assert _git_grep_tracked(_T36) == []

    def test_m913_m914_m915_not_members_ledger_holds(self):
        # m913 (register-availability), m914 (quote-inclusion, no
        # gradient), m915 (financial-architecture mapping) are not
        # uniform-prediction tests: the ledger holds at 46.
        b913 = _yaml(ATLANTIC_FILE)["competitor_relationships"][
            "openai"][KEY_913]
        assert "Ledger holds at 46" in b913["falsification_family"]
        b914 = _yaml(JOURNALISTS_FILE)["stevie_bonifield"][
            "competitor_coverage"][KEY_914]
        assert b914["falsification_family_member"] is False
        b915 = _yaml(ENTITIES_FILE)[KEY_915]
        assert b915["falsification_family_member"] is False


# ---------------------------------------------------------------------------
# 9. Forward-looking staleness (pin lifecycle, subprocess)
# ---------------------------------------------------------------------------
class TestTypeDForwardLookingStaleness1140:
    def test_1135_guard_lifecycle_stale_by_design(self):
        # #1135's TestGuardLifecycle1135 pinned max 912, zero-913
        # numeric/underscore/dash, no-new-below-max,
        # no-thirty-fifth-direction and no-forty-seventh-member.
        # The 913 (#1137), 914 (#1138) and 915 (#1139) landings plus
        # the THIRTY-FIFTH direction trip every pin except the
        # underscore/dash 913 guards. Designed lifecycle; recorded,
        # not repaired.
        res = _class_run(D1135_FILE, "TestGuardLifecycle1135")
        assert res.returncode != 0, res.stdout[-2000:]

    def test_1135_novelty_max_pin_stays_green_by_design(self):
        # #1135's TestNovelty1135::test_max_id_is_912 asserts the
        # git-grep hit LIST for "mechanism_id: 912" equals exactly
        # [profiles/competitor-entities.yaml]. The 913/914/915
        # landings do not remove 912 from competitor-entities.yaml,
        # so this pin STAYS GREEN by design of its weak formulation
        # (unlike #1130's _max_numeric_mechanism_id() == 906 pin,
        # which tripped on the 907 landing). Recorded, not repaired.
        res = _node_run(
            D1135_FILE, "TestNovelty1135::test_max_id_is_912")
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1136_staleness_pin_on_1135_lifecycle_flips_by_design(self):
        # #1136 pinned #1135's guard lifecycle still green at 11 PM
        # Oct 1; the m913 (#1137), m914 (#1138) and m915 (#1139)
        # landings plus the THIRTY-FIFTH direction trip it.
        res = _class_run(E1136_FILE, "TestStalenessPins")
        assert res.returncode != 0, res.stdout[-2000:]

    def test_1137_staleness_pins_still_correct(self):
        # #1137 recorded the designed end-states of #1135's
        # max-912/zero-913-numeric/zero-913-underscore-dash/
        # no-new-below-max pins. Type D lands nothing, so every
        # recorded state holds - EXCEPT the thirty-fifth half of
        # the no-thirty-fifth/no-forty-seventh pin: the #1139
        # THIRTY-FIFTH landing (m915 METER-THEN-INVITE) trips it.
        # The class therefore returns nonzero now; the flip is
        # recorded, not repaired. The forty-seventh half stays
        # green (verified by the direct node run below).
        res = _class_run(A1137_FILE, "TestTypeAForwardLookingStaleness1137")
        assert res.returncode != 0, res.stdout[-2000:]

    def test_1137_forty_seventh_half_stays_green(self):
        # The forty-seventh member-claim guard survives the
        # #1139 landing: no new falsification-family member was
        # claimed. Direct node run on #1135's guard.
        res = _node_run(
            D1135_FILE,
            "TestGuardLifecycle1135::test_no_forty_seventh_member_claim")
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1137_thirty_fifth_half_tripped_by_1139_landing(self):
        # The thirty-fifth direction guard trips on the landed
        # THIRTY-FIFTH direction (m915): the guard's expectation
        # was valid at #1137 time (pre-#1139) and its lifecycle
        # ends here by design.
        res = _node_run(
            D1135_FILE,
            "TestGuardLifecycle1135::test_no_thirty_fifth_direction_claim")
        assert res.returncode != 0, res.stdout[-2000:]

    def test_1138_forward_looking_staleness_still_green(self):
        # #1138 recorded the designed end-states of #1137's
        # max-913/zero-914-numeric/thirty-fifth-absent pins and the
        # stays-green states of the 914 underscore/dash,
        # forty-seventh-absent, forty-sixth-intact and
        # thirty-fourth-intact pins. Type D lands nothing, so every
        # recorded state holds.
        res = _class_run(B1138_FILE, "TestForwardLookingStaleness1138")
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1139_supersession_pins_still_green(self):
        # #1139 recorded the designed end-states of #1138's
        # max-914/zero-915-numeric pins (fail by design) and the
        # stays-green states of the 915 underscore/dash,
        # forty-seventh-absent, forty-sixth-intact and
        # thirty-fourth-intact pins. Type D lands nothing, so every
        # recorded state holds.
        res = _class_run(C1139_FILE, "TestSupersessionPins1139")
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1139_forward_guards_still_green(self):
        # #1139's forward guards (zero-916 numeric/underscore/dash,
        # no-thirty-sixth, format-built-only, iteration-log
        # absence discipline) stay green: this run adds no
        # mechanism.
        res = _class_run(C1139_FILE, "TestForwardGuards1139")
        assert res.returncode == 0, res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 10. Guard lifecycle (forward guards for #1141)
# ---------------------------------------------------------------------------
class TestGuardLifecycle1140:
    def test_1140_file_pins_max_id_915_and_next_916(self):
        assert _max_numeric_mechanism_id_in_profiles() == 915

    def test_zero_next_numeric_916_in_profiles(self):
        assert _git_grep_tracked(_mech_id_colon(NEXT_NUM), "profiles/") == []

    def test_zero_next_underscore_916_repo_wide(self):
        assert _git_grep_tracked(_mech_underscore(NEXT_NUM)) == []

    def test_zero_next_dash_916_repo_wide(self):
        assert _git_grep_tracked(_mech_dash(NEXT_NUM)) == []

    def test_no_new_mechanisms_below_max(self):
        ids = []
        for dirpath, _, files in os.walk(PROFILES_DIR):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = _read(os.path.join(dirpath, fn))
                    ids += [int(m) for m in re.findall(
                        r"mechanism_id: (\d+)", text)]
        assert 915 in ids
        assert all(i <= 915 for i in ids)

    def test_no_thirty_sixth_direction_claim(self):
        hits = [p for p in _git_grep_tracked(_T36)]
        assert hits == [], hits

    def test_no_forty_seventh_member_claim(self):
        hits = [p for p in _git_grep_tracked(FORTY_SEVENTH_MEMBER)]
        assert hits == [], hits


# ---------------------------------------------------------------------------
# 11. Background-suite verdict (#1135 suite)
# ---------------------------------------------------------------------------
class TestBackgroundSuiteVerdict1140:
    def _log_stats(self):
        text = _read(PRIOR_SUITE_LOG)
        return (os.path.getsize(PRIOR_SUITE_LOG), text.count("."),
                text.count("F"), text.count("E"), text)

    def test_prior_suite_died_eleventh_consecutive(self):
        # The #1135-launched background full suite DIED: 1843
        # bytes (1659 dots, ~2% progress), last write Oct 1
        # 23:02 PDT, zero summary tokens (no "passed"/"failed"
        # summary, no collected-count token), no live pytest
        # process. Per the #795 convention this is recorded as
        # DIED, not "interrupted": the run produces no usable
        # verdict.
        size, dots, fails, errors, text = self._log_stats()
        assert size == 1843, size
        assert dots == 1659, dots
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
            ["pgrep", "-f", "[p]ytest.*type_d_1135"],
            capture_output=True,
            text=True,
        )
        assert result.returncode != 0, (
            "a pytest process for the #1135 suite must not still be "
            "alive when its verdict is recorded")

    def test_tombstone_lineage_advances_to_87th(self):
        # ELEVENTH consecutive background-suite death of the new
        # streak (the 57-run streak ENDED at #1085 when the #1080
        # suite completed). Tombstone lineage advances EIGHTY-SIXTH
        # -> EIGHTY-SEVENTH; recorded in the #1140 iteration-log
        # entry. Deselected pre-commit (log entry is written in the
        # log-hash step per #721).
        text = _read(LOG_FILE)
        assert "EIGHTY-SEVENTH" in text


# ---------------------------------------------------------------------------
# 12. Fresh synthetic engine calibration (new values, not #1135's)
# ---------------------------------------------------------------------------
class TestSyntheticEngineCalibration1140:
    # Scratch-run values produced at this run (Fri 2026-10-02 ~03:05
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
                datetime(2026, 10, 2),
                datetime(2026, 10, 2),
            )

        return calc

    def test_strong_effect_is_significant(self):
        calc = self._calculate()
        meta = [-0.72, -0.58, -0.69, -0.63, -0.75, -0.60, -0.66]
        comp = [0.22, 0.05, 0.31, -0.02, 0.18, 0.09, -0.05]
        result = calc(meta, comp)
        assert result.asymmetry_score == pytest.approx(-0.7728571428571428)
        assert result.t_statistic == pytest.approx(-14.056295135749473)
        assert result.p_value < 1e-6
        assert result.cohens_d == pytest.approx(-7.513405789335949)
        assert result.is_significant is True
        assert result.confidence_interval_lower == pytest.approx(
            -0.8728928571428571)
        assert result.confidence_interval_upper == pytest.approx(
            -0.6742499999999999)
        # The strong arm-swap negates the asymmetry exactly.
        swapped = calc(comp, meta)
        assert swapped.asymmetry_score == pytest.approx(0.7728571428571428)

    def test_near_null_pair_stays_silent(self):
        calc = self._calculate()
        meta = [0.07, -0.02, 0.05, -0.04, 0.01, -0.06, 0.03]
        comp = [-0.05, 0.03, -0.01, 0.06, -0.03, 0.02, -0.04]
        result = calc(meta, comp)
        assert result.asymmetry_score == pytest.approx(0.008571428571428574)
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
        # The m913/m914/m915 mechanisms never promote engine
        # significance to a finding: all three carry finding-layer
        # is_significant False (or tone NOT_SCORED for the Type C).
        b913 = _yaml(ATLANTIC_FILE)["competitor_relationships"][
            "openai"][KEY_913]
        assert "is_significant False" in b913["statistical_discipline"]
        b914 = _yaml(JOURNALISTS_FILE)["stevie_bonifield"][
            "competitor_coverage"][KEY_914]
        assert "is_significant false" in b914["statistical_discipline"]
        b915 = _yaml(ENTITIES_FILE)[KEY_915]
        assert b915["is_significant"] is False
        assert b915["engine_run"] is False


# ---------------------------------------------------------------------------
# 13. Suite re-launch
# ---------------------------------------------------------------------------
class TestSuiteRelaunch1140:
    def test_relaunch_log_path_written(self):
        # The re-launched full suite log exists in goal hidden_files
        # (created by this run's background launch before commit).
        assert os.path.exists(SUITE_LOG), (
            "the #1140 background suite must be re-launched to "
            + SUITE_LOG
            + " before the main commit"
        )

    def test_relaunch_log_is_full_inventory(self):
        # The re-launch runs WITHOUT -x: the full inventory
        # (calendar by-design failures included) is needed for the
        # #1145 triage. The log must hold pytest progress output,
        # not just a header.
        text = _read(SUITE_LOG)
        assert text.count(".") > 100, (
            "the re-launched suite log should accumulate dot "
            "progress; got %d dots" % text.count(".")
        )

    def test_next_type_d_run_owns_the_verdict(self):
        # Per the #795 convention, the NEXT Type D run (#1145)
        # checks this suite's verdict; this run only records the
        # launch.
        assert "type_d_1140_full_suite.log" in SUITE_LOG


# ---------------------------------------------------------------------------
# 14. Doc-sync per #719 (fails pre-commit by design; passes post-sync)
# ---------------------------------------------------------------------------
class TestTypeDDocSync1140:
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
        assert "README_TEST_COUNT = 59880" in own
        assert "README_FILE_COUNT = 1465" in own


# ---------------------------------------------------------------------------
# 15. Iteration log per #721 (fails pre-commit by design)
# ---------------------------------------------------------------------------
class TestTypeDIterationLog1140:
    def _entry(self):
        return _read(LOG_FILE)

    def test_iteration_log_entry_present(self):
        assert "## #1140 Type D" in self._entry()

    def test_iteration_log_hashes_registered(self):
        text = self._entry()
        assert ANCHORED_SHA in text
        assert "1140-1144 window" in text

    def test_iteration_log_rotation_guard(self):
        text = self._entry()
        assert "FIRST leg" in text
        assert "D->E->A->B->C" in text


# ---------------------------------------------------------------------------
# 16. In-flight isolation
# ---------------------------------------------------------------------------
class TestInflightIsolation1140:
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
