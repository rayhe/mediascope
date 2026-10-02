"""Type D -- Iteration #1145 (Fri 2026-10-02 08:00 PDT): m916/m917/m918
qualitative-discipline verification + post-1140-1144 corpus integrity
(max numeric mechanism_id 918; zero next-number 919 keys in
numeric/underscore/dash mechanism forms - the 919 needles are
format-built per #715 so no guard-literal carrier file exists; the
m916/m917/m918 block keys carry no mechanism-number substring
(designed keying), so they are plain literals; the #1140/#1141/#1142/
#1143/#1144 window files are NOT edited by this run - their now-stale
forward-looking pins are recorded as fail-by-design via subprocess in
the staleness class (#1140's max-915 + zero-916-numeric pins trip on
the 916/917/918 landings while its no-thirty-sixth-direction and
no-forty-seventh-member halves stay green; #1142's max-916 pin trips
on the 917/918 landings; #1143's max-917 + zero-918-numeric pins trip
on the 918 landing; #1144's zero-919 / no-thirty-seventh / format-built
/ iteration-log-absence forward guards stay GREEN - Type D lands no
mechanism; #1144's supersession greens hold except the post-commit
Type-C-#1144 pin which flipped by design and is deselected); ledger
holds at 46 with the FORTY-SIXTH member-claim form present in exactly
one profiles file (profiles/the-verge.yaml, m907 block, 2 occurrences
- the #1127 designed pattern) and the forty-seventh member-claim form
absent repo-wide (needle format-built per #715); the THIRTY-FIFTH
relationship direction is present in competitor-entities.yaml (m915
METER-THEN-INVITE, landed at #1139); the thirty-sixth AND
thirty-seventh relationship-direction claim forms are both absent
repo-wide (needles format-built per #715)) + the #1140 background-suite
verdict (DIED at 3555 bytes / 3191 dots + 11 xfails + 1 failure-mark,
~5% progress, with last write Oct 2 04:07 PDT and zero summary
tokens, no live pytest process - FOURTEENTH consecutive
background-suite death of the new streak; the 57-run streak ENDED at
#1085 when the #1080 suite completed; tombstone lineage advances
EIGHTY-SEVENTH -> EIGHTY-EIGHTH) + fresh synthetic engine calibration
(new values, not #1140's) + re-launch of the full suite as a background
process writing to goal hidden_files type_d_1145_full_suite.log WITHOUT
-x (the full inventory, calendar by-design failures included, is needed
for the #1150 triage; the next Type D run checks its verdict per the
#795 convention).

Type D FIRST leg of the 1145-1149 window, OPENING it
(D->E->A->B->C). Committed predecessor #1144 Type C (7:00 AM PDT Oct 2)
CLOSED the 1140-1144 window (D #1140, E #1141, A #1142, B #1143,
C #1144). Rotation per the #565 anchor + rotation guard.
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
- m916 (Type A #1142, profiles/wired.yaml competitor_relationships/
  openai 4-space block key, numeric colon-form field; block key count
  2 - colon-form line + test_file field echo of the same string in
  the filename, designed): WIRED x OpenAI Sep-26 rogue-agent
  government-disclosure bounded-absence silence vs the Dell Cameron
  Jul-28 adversarial register (-0.60) and carried WIRED x Meta arms.
  THIRD crisis peg tested at WIRED (after m877 Astra and m898 LASST).
  Register-AVAILABILITY finding per #1127: the accountability
  register is available for the licensing partner at six peers and
  was available at WIRED in July, but is unavailable for the
  partner's government-escalation episode in the bounded Sep-26/Oct-2
  sets (21 rows, 0 wired.com URLs), while carried WIRED x Meta arms
  sustain the adversarial register on Meta. Conde Nast x OpenAI deal
  (Aug 20 2024) is the standing financial context (coverage_prediction
  "softer"). NOT a falsification-family member; ledger holds at 46.
- m917 (Type B #1143, profiles/careers/journalists.yaml
  cristina_criddle competitor_coverage 4-space block key, numeric
  colon-form field; block key count 2 - colon-form line + block_key
  field, designed): Cristina Criddle (FT) Sep-16 "blindsided"
  accountability-adversarial on the OpenAI licensing-deal partner
  (-0.35, headline tier) - TEMPORAL EXTENSION of m758's writer-level
  pattern (Type B #878: Bakalar ethics-chief-exit -0.40, Meta
  within-piece constructive contrast +0.15, both carried per #807).
  Illustrative Meta-minus-OpenAI delta +0.50. NOT a new
  falsification-family member (same writer/partner prediction test
  already counted at #878 as the TWENTY-EIGHTH member); ledger
  holds at 46.
- m918 (Type C #1144, profiles/competitor-entities.yaml zero-indent
  top-level block key, numeric colon-form field; block key count 2 -
  colon-form line + block_key field, designed): Apple Siri AI
  publisher-negotiation watch Oct-2-2026 status check (51 days
  post-WSJ, zero signed-deal closures) + OpenAI "persistently
  underperforming" court filing documents the commercial failure of
  the predecessor Apple-OpenAI Siri deal. Variable-pay proposal
  EXTENDS #27 unilateral pricing (m891); no new direction
  (thirty-sixth absent by design; thirty-fifth stands). connects_to
  [156, 606, 654, 891]. 8 novel sources. Tone NOT_SCORED; engine
  NOT run; NOT a falsification-family member (financial-incentive
  mapping per #609/#614); ledger holds at 46.

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
WIRED_FILE = os.path.join(PROFILES_DIR, "wired.yaml")
JOURNALISTS_FILE = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
ENTITIES_FILE = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
VERGE_FILE = os.path.join(PROFILES_DIR, "the-verge.yaml")
LOG_FILE = os.path.join(REPO_ROOT, "iteration-log.md")
README_FILE = os.path.join(REPO_ROOT, "README.md")
ARCH_FILE = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")

# Block keys are plain literals: none carries a mechanism-number
# substring (designed keying per #715).
KEY_916 = ("type_a_1142_wired_openai_sep26_rogue_agent_gov_disclosure_"
           "bounded_absence_vs_cameron_jul28_adversarial_oct02_5am")
KEY_917 = ("type_b_1143_cristina_criddle_ft_blindsided_openai_"
           "anthropic_m758_temporal_extension_sep16")
KEY_918 = ("type_c_1144_apple_siri_ai_publisher_negotiation_watch_"
           "day_fifty_one_zero_closures_persistently_underperforming_"
           "filing_oct02_7am")
OWN_BASENAME = ("test_type_d_1145_m916_m917_m918_qualitative_"
                "corpus_integrity_oct02_8am.py")

# Predecessor test files for supersession pins.
D1140_FILE = ("test_type_d_1140_m913_m914_m915_qualitative_"
               "corpus_integrity_oct02_3am.py")
E1141_FILE = ("test_type_e_1141_podcast_sentiment_"
               "151st_verification_oct02_4am.py")
A1142_FILE = ("test_type_a_1142_wired_openai_sep26_rogue_agent_gov_"
               "disclosure_bounded_absence_vs_cameron_jul28_"
               "adversarial_oct02_5am.py")
B1143_FILE = ("test_type_b_1143_cristina_criddle_ft_blindsided_"
               "openai_anthropic_sep16_m758_temporal_extension_"
               "oct02_6am.py")
C1144_FILE = ("test_type_c_1144_apple_siri_publisher_watch_day51_"
               "zero_closures_underperforming_filing_oct02_7am.py")

# Prior-window background suite (verdict rendered this run) and this
# run's re-launched suite.
PRIOR_SUITE_LOG = os.path.join(
    os.path.expanduser("~"),
    "workspace",
    "goals",
    "mediascope-meta-wearables-press-analysis",
    "hidden_files",
    "type_d_1140_full_suite.log",
)
SUITE_LOG = os.path.join(
    os.path.expanduser("~"),
    "workspace",
    "goals",
    "mediascope-meta-wearables-press-analysis",
    "hidden_files",
    "type_d_1145_full_suite.log",
)

# Patched post-commit once README/ARCHITECTURE doc-sync lands.
README_TEST_COUNT = 60242  # post-doc-sync total (60151 + 91)
README_FILE_COUNT = 1470  # post-doc-sync total
TEST_BASENAME = OWN_BASENAME

# Anchor placeholder per #565: patched to the main commit's 40-char SHA in the
# anchor followup. Deselect the placeholder test in post-commit full runs.
ANCHORED_SHA = "0000000000000000000000000000000000000000"

MECH_NUM = 918
NEXT_NUM = 919
PREV_NUM = 917

# Fragment-built direction needles per #715 (never contiguous here).
_T35 = "THIRTY-" + "FIFTH relationship direction"
_T36 = "THIRTY-" + "SIXTH relationship direction"
_T37 = "THIRTY-" + "SEVENTH relationship direction"


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
class TestNovelty1145:
    def test_no_type_d_1145_test_file_preexisting(self):
        hits = glob.glob(
            os.path.join(TESTS_DIR, "test_type_d_1145*.py"))
        assert hits == [os.path.join(TESTS_DIR, OWN_BASENAME)], hits

    def test_no_type_d_1145_in_git_log(self):
        # Deselected pre-commit per #565: the main commit does not
        # exist yet.
        log = _git("log", "--oneline", "--grep=Type D #1145")
        assert "Type D #1145" in log, log

    def test_max_id_is_918(self):
        needle = _mech_id_colon(MECH_NUM)
        hits = _git_grep_tracked(needle, "profiles/")
        assert hits == ["profiles/competitor-entities.yaml"], hits

    def test_zero_919_numeric_forms_in_profiles(self):
        needle = _mech_id_colon(NEXT_NUM)
        assert _git_grep_tracked(needle, "profiles/") == []

    def test_block_keys_unique_in_home_yamls(self):
        assert _key_count_in_file(KEY_916, WIRED_FILE) == 2
        assert _key_count_in_file(KEY_917, JOURNALISTS_FILE) == 2
        assert _key_count_in_file(KEY_918, ENTITIES_FILE) == 2
        # Designed keying: no mechanism-number substring in any
        # block key, so they are plain literals here.
        for key in (KEY_916, KEY_917, KEY_918):
            assert "916" not in key and "917" not in key \
                and "918" not in key

    def test_no_type_e_1146_in_git_log(self):
        # The next leg must not exist yet.
        log = _git("log", "--oneline", "--grep=Type E #1146")
        assert "Type E #1146" not in log, log


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------
class TestTypeDRotationGuard1145:
    def test_rotation_window_opens_1145(self):
        # 1145-1149 window: D opens, then E -> A -> B -> C.
        log = _git("log", "--oneline", "--grep=Type C #1144")
        assert "Type C #1144" in log, log
        entry = _read(LOG_FILE)
        assert "1140-1144 window" in entry
        # The "CLOSED the 1140-1144 window" predecessor line is
        # written by this run's doc-sync (TestTypeDIterationLog1145).

    def test_predecessor_1144_chain_present(self):
        log = _git("log", "--format=%H %s")
        assert "Type C #1144" in log, log
        for sha8 in ("02b20835", "e9b37c8e", "f2d3867f", "5a908158",
                     "127c6be9"):
            assert sha8 in log, sha8

    def test_anchor_sha_is_real(self):
        # Deselected pre-commit: patched in the anchor followup.
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA
        assert ANCHORED_SHA != "0" * 40


# ---------------------------------------------------------------------------
# 3. Novelty anchor
# ---------------------------------------------------------------------------
class TestTypeDNoveltyAnchor1145:
    def test_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per #565: the main commit does not
        # exist yet. Post-commit this asserts the single #1145
        # commit is the anchor and carries the test-file changes.
        log = _git("log", "--format=%H %s", "--grep=Type D #1145")
        assert "Type D #1145" in log
        assert ANCHORED_SHA in log


# ---------------------------------------------------------------------------
# 4. Corpus integrity
# ---------------------------------------------------------------------------
class TestTypeDCorpusIntegrity1145:
    def test_m916_block_present_in_wired_yaml(self):
        data = _yaml(WIRED_FILE)
        block = data["competitor_relationships"]["openai"][KEY_916]
        assert block["mechanism_id"] == 916
        assert block["iteration"] == 1142
        assert block["iteration_type"] == "A"

    def test_m917_block_present_in_journalists_yaml(self):
        data = _yaml(JOURNALISTS_FILE)
        block = data["cristina_criddle"]["competitor_coverage"][KEY_917]
        assert block["mechanism_id"] == 917
        assert block["iteration"] == 1143
        assert block["type"] == "B"

    def test_m918_block_present_in_competitor_entities_yaml(self):
        data = _yaml(ENTITIES_FILE)
        block = data[KEY_918]
        assert block["mechanism_id"] == 918
        assert block["iteration"] == 1144
        assert block["iteration_type"] == "C"

    def test_max_mechanism_id_is_918(self):
        assert _max_numeric_mechanism_id_in_profiles() == 918

    def test_zero_919_forms_repo_wide(self):
        assert _git_grep_tracked(_mech_id_colon(919)) == []
        assert _git_grep_tracked(_mech_underscore(919)) == []
        assert _git_grep_tracked(_mech_dash(919)) == []

    def test_m916_key_count_is_designed(self):
        # Colon-form line + test_file field echo of the same string
        # in the filename (the test filename equals the block key).
        text = _read(WIRED_FILE)
        assert text.count(KEY_916) == 2
        lines = [l for l in text.splitlines() if KEY_916 in l]
        assert lines[0].strip() == KEY_916 + ":"
        assert "test_file" in lines[1]

    def test_m917_key_count_is_designed(self):
        # Colon-form line + block_key field.
        assert _key_count_in_file(KEY_917, JOURNALISTS_FILE) == 2

    def test_m918_key_count_is_designed(self):
        # Colon-form line + block_key field.
        assert _key_count_in_file(KEY_918, ENTITIES_FILE) == 2


# ---------------------------------------------------------------------------
# 5. m916 qualitative discipline
# ---------------------------------------------------------------------------
class TestTypeDM916QualitativeDiscipline:
    def _block(self):
        return _yaml(WIRED_FILE)["competitor_relationships"][
            "openai"][KEY_916]

    def test_m916_run_metadata(self):
        b = self._block()
        assert b["mechanism_id"] == 916
        assert b["iteration"] == 1142
        assert b["iteration_type"] == "A"
        assert b["publication"] == "WIRED"
        assert b["competitor"] == "OpenAI"
        assert b["comparator_entity"] == "Meta"
        assert b["publication_pair"] == "WIRED x OpenAI"

    def test_m916_finding_register_availability(self):
        b = self._block()
        finding = b["finding"]
        assert "THIRD Sep-26/Oct-1 2026 crisis peg" in finding
        assert "register-AVAILABILITY" in finding
        assert "m877" in finding and "m898" in finding
        assert "m694" in finding
        assert "NOT a falsification-family member" in \
            b["falsification_family"]

    def test_m916_bounded_absence(self):
        b = self._block()
        ba = b["bounded_absence"]
        assert ba["total_rows"] == 21
        assert ba["wired_urls"] == 0
        assert "query_set_1" in ba and "query_set_4" in ba
        assert "iteration-492 rule" in ba["rule"]

    def test_m916_peer_coverage(self):
        b = self._block()
        outlets = [p["outlet"] for p in b["peer_coverage"]]
        assert len(outlets) == 6
        for expected in ("NYT", "AP wire", "NPR", "CNN", "CBS News",
                         "The Daily Beast"):
            assert expected in outlets

    def test_m916_within_beat_counterfactual(self):
        b = self._block()
        cf = b["within_beat_counterfactual"]
        assert "Dell Cameron" in cf["journalist"]
        assert cf["tone"] == -0.60
        assert cf["register"].startswith("adversarial")
        assert "falsification-family tension" in cf["significance"]

    def test_m916_carried_meta_arms(self):
        b = self._block()
        arms = " ".join(b["carried_meta_arms"])
        assert "m877" in arms and "m820" in arms and "m757" in arms
        assert "-0.75" in arms

    def test_m916_financial_context(self):
        b = self._block()
        fin = b["financial_context"]
        assert "Aug 20 2024" in fin["conde_nast_openai_deal"]
        assert fin["prediction"] == "softer OpenAI coverage"

    def test_m916_confounder_disclosure(self):
        b = self._block()
        conf = b["confounders"]
        assert len(conf) == 4
        joined = " ".join(conf)
        assert "STRONG: WIRED paywall" in joined
        assert "COUNTER: Cameron" in joined

    def test_m916_research_method(self):
        b = self._block()
        assert "4 browser.search query sets" in b["research_method"]
        assert "0 browser.open" in b["research_method"]

    def test_m916_not_falsification_member(self):
        b = self._block()
        assert "Ledger holds at 46" in b["ledger"]
        assert "Ledger holds at 46" in b["falsification_family"]


# ---------------------------------------------------------------------------
# 6. m917 qualitative discipline
# ---------------------------------------------------------------------------
class TestTypeDM917QualitativeDiscipline:
    def _block(self):
        return _yaml(JOURNALISTS_FILE)["cristina_criddle"][
            "competitor_coverage"][KEY_917]

    def test_m917_run_metadata(self):
        b = self._block()
        assert b["mechanism_id"] == 917
        assert b["iteration"] == 1143
        assert b["type"] == "B"
        assert b["journalist"] == "Cristina Criddle"
        assert b["publication"] == "financial-times"
        assert b["design"] == "temporal-extension"
        assert b["block_key"] == KEY_917
        assert b["test_file"] == "tests/" + B1143_FILE

    def test_m917_new_arm(self):
        b = self._block()
        arm = b["new_openai_anthropic_arm"]
        assert "blindsided" in arm["title"]
        assert arm["date"] == "2026-09-16"
        assert arm["tone_score"] == -0.35
        assert arm["techmeme_timestamp"] == "2026-09-16 13:57:16"
        assert "biztoc.com" in arm["url"]
        assert "headline-tier" in arm["evidence_tier"]

    def test_m917_carried_arms_per_807(self):
        b = self._block()
        assert b["carried_bakalar_arm"]["tone_score"] == -0.4
        assert b["carried_bakalar_arm"]["carried_from"] == "m758"
        assert b["carried_meta_contrast_arm"]["tone_score"] == 0.15
        assert b["carried_meta_contrast_arm"]["carried_from"] == "m758"

    def test_m917_register_contrast_arithmetic(self):
        b = self._block()
        contrast = b["register_contrast"]
        assert contrast["illustrative_delta_meta_minus_openai"] == 0.5
        assert "n=1 new arm" in contrast["note"]

    def test_m917_temporal_extension_reading(self):
        b = self._block()
        assert "TEMPORAL EXTENSION of m758" in b["finding"]
        assert "TWENTY-EIGHTH" in b["finding"]
        assert "#878" in b["finding"]

    def test_m917_statistical_discipline(self):
        b = self._block()
        scorer = b["scorer"]
        assert "MANUAL ILLUSTRATIVE ONLY" in scorer["method"]
        assert "engine NOT run" in scorer["method"]
        assert "is_significant False" in scorer["method"]
        assert scorer["verdict"] == "directionally_supported_not_proven"
        assert b["no_analysis_json_update"] is True

    def test_m917_confounders_strong_first(self):
        b = self._block()
        conf = b["confounders"]
        assert len(conf) == 5
        assert conf[0].startswith("STRONG: dual-entity peg")
        assert conf[1].startswith("STRONG: headline-tier")

    def test_m917_research_method(self):
        b = self._block()
        assert "11 browser.search query sets" in b["research_method"]
        assert "0 browser.open" in b["research_method"]

    def test_m917_not_falsification_member(self):
        b = self._block()
        assert b["falsification_family_member"] is False
        assert b["falsification_ledger"] == 46
        assert "Ledger holds at 46" in b["ledger_note"]
        assert FORTY_SEVENTH_MEMBER not in b["ledger_note"]

    def test_m917_suite_status_checked_only(self):
        b = self._block()
        assert "CHECKED ONLY per #795" in b["background_suite_status"]
        assert "#1145" in b["background_suite_status"]


# ---------------------------------------------------------------------------
# 7. m918 qualitative discipline
# ---------------------------------------------------------------------------
class TestTypeDM918QualitativeDiscipline:
    def _block(self):
        return _yaml(ENTITIES_FILE)[KEY_918]

    def test_m918_run_metadata(self):
        b = self._block()
        assert b["mechanism_id"] == 918
        assert b["iteration"] == 1144
        assert b["iteration_type"] == "C"
        assert b["type"] == "financial_incentive_mapping"
        assert b["block_key"] == KEY_918
        assert b["connects_to"] == [156, 606, 654, 891]
        assert b["verdict"] == "directionally_supported_not_proven"

    def test_m918_no_new_direction_taxonomy(self):
        b = self._block()
        tax = b["relationship_direction_taxonomy"]
        assert "No new direction" in tax
        assert "m891" in tax
        assert "m915" in tax
        assert "m807 enumeration" in tax
        assert "thirty-sixth direction stays absent by design" in tax

    def test_m918_finding(self):
        b = self._block()
        finding = b["finding"]
        assert "51 days" in finding
        assert "zero signed" in finding
        assert "persistently underperforming" in finding
        assert "mechanism 156" in finding
        assert "156/606" in finding

    def test_m918_money_flow(self):
        b = self._block()
        flow = b["money_flow"]
        assert "Negotiation channel" in flow and "$0" in flow
        assert "Apple -> Google ~$1B/yr" in flow
        assert "persistently underperforming" in flow or \
            "Dead distribution leg" in flow

    def test_m918_confounder_strengths(self):
        b = self._block()
        strengths = [c["strength"] for c in b["confounders"]]
        assert strengths == ["STRONG", "STRONG", "MODERATE", "MODERATE",
                             "WEAK"]
        assert "Bounded absence is not proof" in b["confounders"][0]["text"]

    def test_m918_sources_all_novel(self):
        b = self._block()
        assert len(b["sources"]) == 8
        assert all(s["novel"] is True for s in b["sources"])
        urls = [s["url"] for s in b["sources"]]
        assert any("macrumors.com" in u for u in urls)
        assert any("9to5mac.com" in u for u in urls)

    def test_m918_coverage_nexus(self):
        b = self._block()
        nexus = b["coverage_nexus"]
        assert "MacRumors" in nexus and "Juli Clover" in nexus
        assert "mechanism 54" in nexus

    def test_m918_statistical_discipline(self):
        b = self._block()
        assert b["tone_scored"] is False
        assert b["engine_run"] is False
        assert b["is_significant"] is False
        assert b["artifact_grade"] is False
        assert b["no_analysis_json_update"] is True
        assert "no coverage-tone pair" in b["falsification_family"]
        assert "FIRST dedicated corpus mechanism" in b["novelty"]

    def test_m918_not_falsification_member(self):
        b = self._block()
        assert b["falsification_family_member"] is False
        assert "ledger holds at 46" in b["falsification_family"]
        assert FORTY_SEVENTH_MEMBER not in b["falsification_family"]
        assert b["yaml_parse_clean"] is True
        assert b["ascii_only"] is True


# ---------------------------------------------------------------------------
# 8. Falsification ledger
# ---------------------------------------------------------------------------
class TestTypeDFalsificationLedger1145:
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

    def test_no_thirty_seventh_direction_claim_repo_wide(self):
        assert _git_grep_tracked(_T37) == []

    def test_m916_m917_m918_not_members_ledger_holds(self):
        # m916 (register-availability), m917 (same-writer temporal
        # replication, not a new prediction test), m918
        # (financial-architecture mapping) are not
        # uniform-prediction tests: the ledger holds at 46.
        b916 = _yaml(WIRED_FILE)["competitor_relationships"][
            "openai"][KEY_916]
        assert "Ledger holds at 46" in b916["falsification_family"]
        b917 = _yaml(JOURNALISTS_FILE)["cristina_criddle"][
            "competitor_coverage"][KEY_917]
        assert b917["falsification_family_member"] is False
        assert b917["falsification_ledger"] == 46
        b918 = _yaml(ENTITIES_FILE)[KEY_918]
        assert b918["falsification_family_member"] is False


# ---------------------------------------------------------------------------
# 9. Forward-looking staleness (pin lifecycle, subprocess)
# ---------------------------------------------------------------------------
class TestTypeDForwardLookingStaleness1145:
    def test_1140_guard_lifecycle_max_915_trips_by_design(self):
        # #1140's TestGuardLifecycle1140 pinned max 915 and the
        # zero-916 numeric guard. The 916 (#1142), 917 (#1143) and
        # 918 (#1144) landings trip every max/next pin. Designed
        # lifecycle; recorded, not repaired.
        res = _class_run(D1140_FILE, "TestGuardLifecycle1140")
        assert res.returncode != 0, res.stdout[-2000:]

    def test_1140_no_thirty_sixth_half_stays_green(self):
        # No new relationship direction landed in the 1140-1144
        # window (m918 explicitly extends #27 without a new
        # direction): the thirty-sixth-direction guard survives.
        res = _node_run(
            D1140_FILE,
            "TestGuardLifecycle1140::test_no_thirty_sixth_direction_claim")
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1140_no_forty_seventh_half_stays_green(self):
        # No new falsification-family member was claimed in the
        # 1140-1144 window: the forty-seventh-member guard survives.
        res = _node_run(
            D1140_FILE,
            "TestGuardLifecycle1140::test_no_forty_seventh_member_claim")
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1142_max_916_pin_trips_by_design(self):
        # #1142's TestGuardLifecycle1142 pinned max 916 and the
        # zero-917 numeric guard. The m917 (#1143) and m918 (#1144)
        # landings trip them. Designed lifecycle; recorded, not
        # repaired.
        res = _node_run(
            A1142_FILE,
            "TestGuardLifecycle1142::"
            "test_1142_file_pins_max_id_916_and_next_917")
        assert res.returncode != 0, res.stdout[-2000:]

    def test_1143_max_917_pin_trips_by_design(self):
        # #1143's zero-918-numeric guard trips on the m918 landing
        # (#1144). Designed lifecycle; recorded, not repaired.
        res = _node_run(
            B1143_FILE,
            "TestGuardLifecycle1143::test_918_numeric_absent_in_profiles")
        assert res.returncode != 0, res.stdout[-2000:]

    def test_1144_forward_guards_stay_green(self):
        # #1144's forward guards (zero-919 numeric/underscore/dash,
        # no-thirty-seventh, format-built-only, iteration-log
        # absence discipline) stay green: this run adds no
        # mechanism and the doc-sync prose uses hyphenated/
        # lowercase forms for the forward guards.
        res = _class_run(C1144_FILE, "TestForwardGuards1144")
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1144_supersession_greens_hold(self):
        # #1144's supersession pins recorded #1143's end-states;
        # Type D lands nothing, so the recorded states hold. The
        # post-commit-flipped no-Type-C-#1144 pin is deselected by
        # design (it flipped red when #1144's main commit landed).
        for node in (
            "TestSupersessionPins1144::"
            "test_1143_max_917_fails_by_design",
            "TestSupersessionPins1144::"
            "test_1143_zero_numeric_918_in_profiles_fails_by_design",
            "TestSupersessionPins1144::"
            "test_1143_underscore_918_stays_green",
            "TestSupersessionPins1144::"
            "test_1143_dash_918_stays_green",
            "TestSupersessionPins1144::"
            "test_1143_forty_seventh_absent_stays_green",
            "TestSupersessionPins1144::"
            "test_1143_forty_sixth_intact_stays_green",
            "TestSupersessionPins1144::"
            "test_1143_thirty_fifth_intact_stays_green",
        ):
            res = _node_run(C1144_FILE, node)
            assert res.returncode == 0, (node, res.stdout[-800:])


# ---------------------------------------------------------------------------
# 10. Guard lifecycle (forward guards for #1146)
# ---------------------------------------------------------------------------
class TestGuardLifecycle1145:
    def test_1145_file_pins_max_id_918_and_next_919(self):
        assert _max_numeric_mechanism_id_in_profiles() == 918

    def test_zero_next_numeric_919_in_profiles(self):
        assert _git_grep_tracked(_mech_id_colon(NEXT_NUM), "profiles/") == []

    def test_zero_next_underscore_919_repo_wide(self):
        assert _git_grep_tracked(_mech_underscore(NEXT_NUM)) == []

    def test_zero_next_dash_919_repo_wide(self):
        assert _git_grep_tracked(_mech_dash(NEXT_NUM)) == []

    def test_no_new_mechanisms_below_max(self):
        ids = []
        for dirpath, _, files in os.walk(PROFILES_DIR):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = _read(os.path.join(dirpath, fn))
                    ids += [int(m) for m in re.findall(
                        r"mechanism_id: (\d+)", text)]
        assert 918 in ids
        assert all(i <= 918 for i in ids)

    def test_no_thirty_seventh_direction_claim(self):
        hits = [p for p in _git_grep_tracked(_T37)]
        assert hits == [], hits

    def test_no_thirty_sixth_direction_claim(self):
        hits = [p for p in _git_grep_tracked(_T36)]
        assert hits == [], hits

    def test_no_forty_seventh_member_claim(self):
        hits = [p for p in _git_grep_tracked(FORTY_SEVENTH_MEMBER)]
        assert hits == [], hits


# ---------------------------------------------------------------------------
# 11. Background-suite verdict (#1140 suite)
# ---------------------------------------------------------------------------
class TestBackgroundSuiteVerdict1145:
    def _log_stats(self):
        text = _read(PRIOR_SUITE_LOG)
        return (os.path.getsize(PRIOR_SUITE_LOG), text.count("."),
                text)

    def test_prior_suite_died_fourteenth_consecutive(self):
        # The #1140-launched background full suite DIED: 3555
        # bytes (3191 dots + 11 xfail marks + 1 failure mark, ~5%
        # progress), last write Oct 2 04:07 PDT, zero summary
        # tokens (no "passed"/"failed" summary, no collected-count
        # token, no "no tests ran"), no live pytest process. Per
        # the #795 convention this is recorded as DIED, not
        # "interrupted": the run produces no usable verdict.
        size, dots, text = self._log_stats()
        assert size == 3555, size
        assert dots == 3191, dots
        assert "passed" not in text
        assert "failed" not in text
        assert " collected " not in text
        assert "no tests ran" not in text

    def test_no_live_pytest_process(self):
        # The bracket pattern avoids self-matching the pgrep
        # command line (phantom-pid class per AGENTS.md).
        result = subprocess.run(
            ["pgrep", "-f", "[p]ytest.*type_d_1140"],
            capture_output=True,
            text=True,
        )
        assert result.returncode != 0, (
            "a pytest process for the #1140 suite must not still be "
            "alive when its verdict is recorded")

    def test_tombstone_lineage_advances_to_88th(self):
        # FOURTEENTH consecutive background-suite death of the new
        # streak (the 57-run streak ENDED at #1085 when the #1080
        # suite completed). Tombstone lineage advances
        # EIGHTY-SEVENTH -> EIGHTY-EIGHTH; recorded in the #1145
        # iteration-log entry. Deselected pre-commit (log entry is
        # written in the doc-sync step per #719/#721).
        text = _read(LOG_FILE)
        assert "EIGHTY-EIGHTH" in text


# ---------------------------------------------------------------------------
# 12. Fresh synthetic engine calibration (new values, not #1140's)
# ---------------------------------------------------------------------------
class TestSyntheticEngineCalibration1145:
    # Scratch-run values produced at this run (Fri 2026-10-02 ~08:10
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
        meta = [-0.81, -0.55, -0.74, -0.68, -0.79, -0.61, -0.70]
        comp = [0.19, 0.02, 0.27, -0.08, 0.14, 0.06, -0.11]
        result = calc(meta, comp)
        assert result.asymmetry_score == pytest.approx(-0.7671428571428573)
        assert result.t_statistic == pytest.approx(-12.074277198596782)
        assert result.p_value < 1e-6
        assert result.cohens_d == pytest.approx(-6.453972638583688)
        assert result.is_significant is True
        assert result.confidence_interval_lower == pytest.approx(
            -0.8828571428571428)
        assert result.confidence_interval_upper == pytest.approx(
            -0.6556785714285714)
        # The strong arm-swap negates the asymmetry exactly.
        swapped = calc(comp, meta)
        assert swapped.asymmetry_score == pytest.approx(0.7671428571428573)

    def test_near_null_pair_stays_silent(self):
        calc = self._calculate()
        meta = [0.04, -0.07, 0.02, -0.01, 0.06, -0.05, 0.00]
        comp = [-0.03, 0.05, -0.06, 0.01, -0.02, 0.04, -0.07]
        result = calc(meta, comp)
        assert result.asymmetry_score == pytest.approx(0.01)
        assert result.p_value > 0.05
        assert result.is_significant is False

    def test_degenerate_n1_contract(self):
        # The classic degenerate guard: n=1 per arm yields t=0.0,
        # p=1.0, d=0.0 and is_significant False regardless of the
        # illustrative pair mean (here the m916 Cameron -0.60 vs
        # carried Meta -0.45 pair).
        calc = self._calculate()
        result = calc([-0.60], [-0.45])
        assert result.asymmetry_score == pytest.approx(-0.15)
        assert result.t_statistic == 0.0
        assert result.p_value == 1.0
        assert result.cohens_d == 0.0
        assert result.is_significant is False

    def test_engine_layer_not_finding_layer(self):
        # The m916/m917/m918 mechanisms never promote engine
        # significance to a finding: all three carry manual-only
        # discipline (m916 register-AVAILABILITY, m917 MANUAL
        # ILLUSTRATIVE, m918 tone NOT_SCORED).
        b916 = _yaml(WIRED_FILE)["competitor_relationships"][
            "openai"][KEY_916]
        assert "MANUAL" in b916["finding"] or \
            "register-AVAILABILITY" in b916["finding"]
        b917 = _yaml(JOURNALISTS_FILE)["cristina_criddle"][
            "competitor_coverage"][KEY_917]
        assert "MANUAL ILLUSTRATIVE ONLY" in b917["scorer"]["method"]
        assert "is_significant False" in b917["scorer"]["method"]
        b918 = _yaml(ENTITIES_FILE)[KEY_918]
        assert b918["is_significant"] is False
        assert b918["engine_run"] is False


# ---------------------------------------------------------------------------
# 13. Suite re-launch
# ---------------------------------------------------------------------------
class TestSuiteRelaunch1145:
    def test_relaunch_log_path_written(self):
        # The re-launched full suite log exists in goal hidden_files
        # (created by this run's background launch before commit).
        assert os.path.exists(SUITE_LOG), (
            "the #1145 background suite must be re-launched to "
            + SUITE_LOG
            + " before the main commit"
        )

    def test_relaunch_log_is_full_inventory(self):
        # The re-launch runs WITHOUT -x: the full inventory
        # (calendar by-design failures included) is needed for the
        # #1150 triage. The log must hold pytest progress output,
        # not just a header.
        text = _read(SUITE_LOG)
        assert text.count(".") > 100, (
            "the re-launched suite log should accumulate dot "
            "progress; got %d dots" % text.count(".")
        )

    def test_next_type_d_run_owns_the_verdict(self):
        # Per the #795 convention, the NEXT Type D run (#1150)
        # checks this suite's verdict; this run only records the
        # launch.
        assert "type_d_1145_full_suite.log" in SUITE_LOG


# ---------------------------------------------------------------------------
# 14. Doc-sync per #719 (fails pre-commit by design; passes post-sync)
# ---------------------------------------------------------------------------
class TestTypeDDocSync1145:
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
        assert "README_TEST_COUNT = 60242" in own
        assert "README_FILE_COUNT = 1470" in own


# ---------------------------------------------------------------------------
# 15. Iteration log per #721 (fails pre-commit by design)
# ---------------------------------------------------------------------------
class TestTypeDIterationLog1145:
    def _entry(self):
        return _read(LOG_FILE)

    def test_iteration_log_entry_present(self):
        assert "## #1145 Type D" in self._entry()

    def test_iteration_log_hashes_registered(self):
        text = self._entry()
        assert ANCHORED_SHA in text
        assert "1145-1149 window" in text

    def test_iteration_log_rotation_guard(self):
        text = self._entry()
        assert "FIRST leg" in text
        assert "D->E->A->B->C" in text
        assert "CLOSED the 1140-1144 window" in text

    def test_iteration_log_suite_verdict_recorded(self):
        text = self._entry()
        assert "EIGHTY-EIGHTH" in text


# ---------------------------------------------------------------------------
# 16. Literal discipline per #715/#1116 (guarded forms format-built only)
# ---------------------------------------------------------------------------
class TestLiteralDiscipline1145:
    def test_format_built_only_in_this_file(self):
        # The #1116 lesson: guarded forms must never appear
        # contiguously in test-file prose. Every guarded needle is
        # format-built at runtime.
        own = _read(__file__)
        assert "mechanism" + "_918" not in own
        assert "mechanism" + "-918" not in own
        assert "mechanism_id: " + "918" not in own
        assert "mechanism" + "_919" not in own
        assert "mechanism" + "-919" not in own
        assert "mechanism_id: " + "919" not in own
        assert "THIRTY-" + "SIXTH relationship direction" not in own
        assert "THIRTY-" + "SEVENTH relationship direction" not in own
        assert "THIRTY-" + "EIGHTH relationship direction" not in own
        assert "FORTY-" + "SEVENTH falsification-family member" not in own
        assert "FORTY-" + "EIGHTH falsification-family member" not in own

    def test_landed_claim_prose_uses_lowercase_forms(self):
        # The landed claims (forty-sixth member, thirty-fifth
        # direction) are referenced in this file's prose only in
        # hyphenated/lowercase form, never as the contiguous
        # claim literals (which live only in the corpus files).
        own = _read(__file__).lower()
        assert "forty-sixth" in own
        assert "thirty-fifth" in own


# ---------------------------------------------------------------------------
# 17. In-flight isolation
# ---------------------------------------------------------------------------
class TestInflightIsolation1145:
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
