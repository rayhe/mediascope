"""Type D -- Iteration #1150 (Fri 2026-10-02 12:00 PDT): m919/m920/m921
qualitative-discipline verification + post-1145-1149 corpus integrity
(max numeric mechanism_id 921; zero next-number 922 keys in
numeric/underscore/dash mechanism forms - the 922 needles are
format-built per #715 so no guard-literal carrier file exists; the
m919/m920/m921 block keys carry no mechanism-number substring
(designed keying), so they are plain literals; the #1145/#1146/#1147/
#1148/#1149 window files are NOT edited by this run - their now-stale
forward-looking pins are recorded as fail-by-design via subprocess in
the staleness class (#1145's max-918 + zero-919-numeric pins trip on
the 919/920/921 landings while its zero-919 underscore/dash halves
stay green; #1147's max-919 + zero-920-numeric pins trip on the 920/921
landings; #1148's zero-921 numeric pin trips on the 921 landing; #1149's
forward guards stay GREEN - Type D lands no mechanism; #1149's supersession
greens hold except the post-commit Type-C-#1149 pin which flipped by
design and is deselected); ledger holds at 46 with the FORTY-SIXTH
member-claim form present in exactly one profiles file
(profiles/the-verge.yaml, m907 block, 2 occurrences - the #1127
designed pattern) and the forty-seventh member-claim form absent
repo-wide (needle format-built per #715); the THIRTY-FIFTH
relationship direction is present in competitor-entities.yaml (m915
METER-THEN-INVITE, landed at #1139); the thirty-sixth AND
thirty-seventh relationship-direction claim forms are both absent
repo-wide (needles format-built per #715)) + the #1145 background-suite
verdict (DIED at 385 bytes / 353 dots, ~0.6% progress, with last write
Oct 2 08:14 PDT and zero summary tokens, no live pytest process -
EIGHTEENTH consecutive background-suite death of the new streak; the
57-run streak ENDED at #1085 when the #1080 suite completed; tombstone
lineage advances EIGHTY-EIGHTH -> EIGHTY-NINTH) + fresh synthetic
engine calibration (new values, not #1145's) + re-launch of the full
suite as a background process writing to goal hidden_files
type_d_1150_full_suite.log WITHOUT -x (the full inventory, calendar
by-design failures included, is needed for the #1155 triage; the next
Type D run checks its verdict per the #795 convention).

Type D FIRST leg of the 1150-1154 window, OPENING it
(D->E->A->B->C). Committed predecessor #1149 Type C (11:00 AM PDT Oct 2)
CLOSED the 1145-1149 window (D #1145, E #1146, A #1147, B #1148,
C #1149). Rotation per the #565 anchor + rotation guard.
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
- m919 (Type A #1147, profiles/news-corp.yaml competitor_relationships/
  2-space block key, numeric colon-form field; block key count 1 -
  colon-form line only, designed): WSJ Oct-1 FTC agent-safety-probe
  original names Anthropic ALONGSIDE OpenAI in the enforcement register
  yet discloses ONLY the OpenAI licensing partnership (the
  HarperCollins/Bartz v. Anthropic $1.5B settlement-revenue vector
  undisclosed); Aug-25 WSJ $30T TAM-pitch arm (+0.10); illustrative
  Anthropic-minus-Meta delta +0.15 near-null. NOT a
  falsification-family member; ledger holds at 46.
- m920 (Type B #1148, profiles/careers/journalists.yaml dan_howley
  competitor_coverage 4-space block key, numeric colon-form field;
  block key count 3 - colon-form line + block_key field + test_file
  field echo, designed): Dan Howley (Yahoo Finance) Sep-26 "same
  consent problem" thesis-level parity between Meta glasses and Apple
  Watch ambient-audio features (thesis-level delta 0.0;
  fact-intensity residual Meta-harder ~0.10); journalist-level parity
  BOUND on the m75 privacy-vocabulary-bifurcation family. NOT a
  falsification-family member; ledger holds at 46.
- m921 (Type C #1149, profiles/competitor-entities.yaml zero-indent
  top-level block key, numeric colon-form field; block key count 2 -
  colon-form line + block_key field, designed): Reach plc H1 2026
  RNS disclosure - "we know AI firms are using our content in their
  products many millions of times a day" (first regulated-earnings
  quantification of unlicensed AI usage in the corpus); AI licensing
  deals a near-term strategic priority; publisher-side P&L leg
  extending m468; publisher-side mirror of #27 unilateral pricing
  (m891/m918). NOT a falsification-family member (financial-incentive
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
NEWS_CORP_FILE = os.path.join(PROFILES_DIR, "news-corp.yaml")
JOURNALISTS_FILE = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
ENTITIES_FILE = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
VERGE_FILE = os.path.join(PROFILES_DIR, "the-verge.yaml")
LOG_FILE = os.path.join(REPO_ROOT, "iteration-log.md")
README_FILE = os.path.join(REPO_ROOT, "README.md")
ARCH_FILE = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")

# Block keys are plain literals: none carries a mechanism-number
# substring (designed keying per #715). Iterations 1147/1148/1149 are
# the landing iterations, not the mechanism ids.
KEY_919 = ("type_a_1147_wsj_anthropic_oct01_ftc_probe_disclosure_"
           "asymmetry_plus_aug25_tam_pitch_vs_carried_meta_arms_oct02_9am")
KEY_920 = ("type_b_1148_dan_howley_yahoo_finance_meta_glasses_apple_watch_"
           "same_consent_problem_parity_bound_sep26")
KEY_921 = ("type_c_1149_reach_plc_h1_2026_earnings_ai_usage_disclosure_"
           "many_millions_oct02_11am")
OWN_BASENAME = ("test_type_d_1150_m919_m920_m921_qualitative_"
                "corpus_integrity_oct02_12pm.py")

# Predecessor test files for supersession pins.
D1145_FILE = ("test_type_d_1145_m916_m917_m918_qualitative_"
              "corpus_integrity_oct02_8am.py")
E1146_FILE = ("test_type_e_1146_podcast_sentiment_"
              "152nd_verification_oct02_8am.py")
A1147_FILE = ("test_type_a_1147_wsj_anthropic_oct01_ftc_probe_disclosure_"
              "asymmetry_aug25_tam_pitch_vs_carried_meta_arms_oct02_9am.py")
B1148_FILE = ("test_type_b_1148_dan_howley_yahoo_finance_meta_glasses_"
              "apple_watch_same_consent_problem_parity_bound_sep26_10am.py")
C1149_FILE = ("test_type_c_1149_reach_plc_h1_2026_earnings_"
              "ai_usage_disclosure_oct02_11am.py")

# Prior-window background suite (verdict rendered this run) and this
# run's re-launched suite.
PRIOR_SUITE_LOG = os.path.join(
    os.path.expanduser("~"),
    "workspace",
    "goals",
    "mediascope-meta-wearables-press-analysis",
    "hidden_files",
    "type_d_1145_full_suite.log",
)
SUITE_LOG = os.path.join(
    os.path.expanduser("~"),
    "workspace",
    "goals",
    "mediascope-meta-wearables-press-analysis",
    "hidden_files",
    "type_d_1150_full_suite.log",
)

# Patched post-commit once README/ARCHITECTURE doc-sync lands.
README_TEST_COUNT = 60600  # post-doc-sync total (60512 + 88)
README_FILE_COUNT = 1475  # post-doc-sync total
TEST_BASENAME = OWN_BASENAME

# Anchor placeholder per #565: patched to the main commit's 40-char SHA in the
# anchor followup. Deselect the placeholder test in post-commit full runs.
ANCHORED_SHA = "0" * 40

MECH_NUM = 921
NEXT_NUM = 922
PREV_NUM = 920

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
class TestNovelty1150:
    def test_no_type_d_1150_test_file_preexisting(self):
        hits = glob.glob(
            os.path.join(TESTS_DIR, "test_type_d_1150*.py"))
        assert hits == [os.path.join(TESTS_DIR, OWN_BASENAME)], hits

    def test_no_type_d_1150_in_git_log(self):
        # Deselected pre-commit per #565: the main commit does not
        # exist yet.
        log = _git("log", "--oneline", "--grep=Type D #1150")
        assert "Type D #1150" in log, log

    def test_max_id_is_921(self):
        needle = _mech_id_colon(MECH_NUM)
        hits = _git_grep_tracked(needle, "profiles/")
        assert hits == ["profiles/competitor-entities.yaml"], hits

    def test_zero_922_numeric_forms_in_profiles(self):
        needle = _mech_id_colon(NEXT_NUM)
        assert _git_grep_tracked(needle, "profiles/") == []

    def test_block_keys_unique_in_home_yamls(self):
        assert _key_count_in_file(KEY_919, NEWS_CORP_FILE) == 1
        assert _key_count_in_file(KEY_920, JOURNALISTS_FILE) == 3
        assert _key_count_in_file(KEY_921, ENTITIES_FILE) == 2
        # Designed keying: no mechanism-number substring in any
        # block key, so they are plain literals here.
        for key, num in ((KEY_919, "919"), (KEY_920, "920"),
                         (KEY_921, "921")):
            assert num not in key, key

    def test_no_type_e_1151_in_git_log(self):
        # The next leg must not exist yet.
        log = _git("log", "--oneline", "--grep=Type E #1151")
        assert "Type E #1151" not in log, log


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------
class TestTypeDRotationGuard1150:
    def test_rotation_window_opens_1150(self):
        # 1150-1154 window: D opens, then E -> A -> B -> C.
        log = _git("log", "--oneline", "--grep=Type C #1149")
        assert "Type C #1149" in log, log
        entry = _read(LOG_FILE)
        assert "1145-1149 window" in entry
        # The "CLOSED the 1145-1149 window" predecessor line is
        # written by this run's doc-sync (TestTypeDIterationLog1150).

    def test_predecessor_1149_chain_present(self):
        log = _git("log", "--format=%H %s")
        assert "Type C #1149" in log, log
        for sha8 in ("04645a0b", "52af28a6", "9b87f43a", "c795f343"):
            assert sha8 in log, sha8

    def test_anchor_sha_is_real(self):
        # Deselected pre-commit: patched in the anchor followup.
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA
        assert ANCHORED_SHA != "0" * 40


# ---------------------------------------------------------------------------
# 3. Novelty anchor
# ---------------------------------------------------------------------------
class TestTypeDNoveltyAnchor1150:
    def test_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per #565: the main commit does not
        # exist yet. Post-commit this asserts the single #1150
        # commit is the anchor and carries the test-file changes.
        log = _git("log", "--format=%H %s", "--grep=Type D #1150")
        assert "Type D #1150" in log
        assert ANCHORED_SHA in log


# ---------------------------------------------------------------------------
# 4. Corpus integrity
# ---------------------------------------------------------------------------
class TestTypeDCorpusIntegrity1150:
    def test_m919_block_present_in_news_corp_yaml(self):
        data = _yaml(NEWS_CORP_FILE)
        block = data["competitor_relationships"][KEY_919]
        assert block["mechanism_id"] == 919
        assert block["iteration"] == 1147
        assert block["iteration_type"] == "A"

    def test_m920_block_present_in_journalists_yaml(self):
        data = _yaml(JOURNALISTS_FILE)
        block = data["dan_howley"]["competitor_coverage"][KEY_920]
        assert block["mechanism_id"] == 920
        assert block["iteration"] == 1148
        assert block["type"] == "B"

    def test_m921_block_present_in_competitor_entities_yaml(self):
        data = _yaml(ENTITIES_FILE)
        block = data[KEY_921]
        assert block["mechanism_id"] == 921
        assert block["iteration"] == 1149
        assert block["iteration_type"] == "C"

    def test_max_mechanism_id_is_921(self):
        assert _max_numeric_mechanism_id_in_profiles() == 921

    def test_zero_922_forms_repo_wide(self):
        assert _git_grep_tracked(_mech_id_colon(922)) == []
        assert _git_grep_tracked(_mech_underscore(922)) == []
        assert _git_grep_tracked(_mech_dash(922)) == []

    def test_m919_key_count_is_designed(self):
        # Colon-form line only: the news-corp.yaml blocks carry no
        # block_key/test_file echo fields.
        assert _key_count_in_file(KEY_919, NEWS_CORP_FILE) == 1

    def test_m920_key_count_is_designed(self):
        # Colon-form line + block_key field + test_file field echo
        # of the same string in the filename.
        assert _key_count_in_file(KEY_920, JOURNALISTS_FILE) == 3

    def test_m921_key_count_is_designed(self):
        # Colon-form line + block_key field.
        assert _key_count_in_file(KEY_921, ENTITIES_FILE) == 2


# ---------------------------------------------------------------------------
# 5. m919 (Type A #1147) qualitative discipline
# ---------------------------------------------------------------------------
class TestTypeDM919QualitativeDiscipline1150:
    def _block(self):
        return _yaml(NEWS_CORP_FILE)["competitor_relationships"][KEY_919]

    def test_m919_run_metadata(self):
        b = self._block()
        assert b["mechanism_id"] == 919
        assert b["iteration"] == 1147
        assert b["iteration_type"] == "A"
        assert "Anthropic" in b["entity_pair"]
        assert "Meta" in b["entity_pair"]

    def test_m919_disclosure_asymmetry_finding(self):
        # Two receiving financial relationships (OpenAI licensing
        # partnership; HarperCollins/Bartz v. Anthropic $1.5B
        # settlement-revenue vector), one disclosed, in a single piece
        # naming both entities. Disclosure geometry, not tone softness.
        b = self._block()
        finding = b["finding"]
        assert "DOES disclose the OpenAI licensing tie" in finding
        assert "no disclosure of that receiving tie" in finding
        assert "disclosure_asymmetry" in \
            b["relation_to_disclosure_asymmetry"]

    def test_m919_tam_pitch_arm(self):
        # The Aug-25 WSJ $30T TAM-pitch arm widens the documented WSJ x
        # Anthropic register range; illustrative delta +0.15 near-null.
        b = self._block()
        scorer = b["scorer"]
        assert scorer["anthropic_arm_tones"] == [-0.35, 0.10]
        assert scorer["meta_arm_tones"] == [-0.30, -0.25]
        assert scorer["illustrative_delta_anthropic_minus_meta"] == \
            pytest.approx(0.15)
        assert "MANUAL ILLUSTRATIVE ONLY" in scorer["method"]
        assert "engine NOT run" in scorer["method"]

    def test_m919_confounders_strong_first(self):
        # Disclosure-policy confound leads (boilerplate may cover only
        # direct licensing deals); carried-arm dependency follows.
        b = self._block()
        strong = b["confounders"]["strong"]
        assert len(strong) >= 1
        assert strong[0].startswith("Disclosure-policy confound")

    def test_m919_research_method(self):
        b = self._block()
        method = b["research_method"]
        assert "4 browser.search query sets" in method
        assert "0 browser.open" in method
        assert "All URLs copied verbatim from Full-URL listings" in method

    def test_m919_statistical_discipline(self):
        b = self._block()
        discipline = b["statistical_discipline"]
        assert "MANUAL/QUALITATIVE ONLY" in discipline
        assert "is_significant False" in discipline
        assert "engine NOT run" in discipline

    def test_m919_artifact_discipline(self):
        b = self._block()
        assert b["artifact_grade"] == "NOT artifact-grade"
        assert b["no_analysis_json_update"] is True
        assert b["correlation_not_causation"] is True

    def test_m919_not_falsification_member(self):
        # m919 carries no falsification_family_member boolean and no
        # falsification_family prose field: the not-a-member status is
        # carried by the ledger count field (which per the #754
        # convention records the count only, never the next-member
        # literal).
        b = self._block()
        assert "Ledger holds at 46" in b["ledger"]
        assert "falsification_family_member" not in b
        blob = yaml.safe_dump(b, allow_unicode=True)
        assert FORTY_SEVENTH_MEMBER not in blob


# ---------------------------------------------------------------------------
# 6. m920 (Type B #1148) qualitative discipline
# ---------------------------------------------------------------------------
class TestTypeDM920QualitativeDiscipline1150:
    def _block(self):
        return _yaml(JOURNALISTS_FILE)["dan_howley"][
            "competitor_coverage"][KEY_920]

    def test_m920_run_metadata(self):
        b = self._block()
        assert b["mechanism_id"] == 920
        assert b["iteration"] == 1148
        assert b["type"] == "B"
        assert b["journalist"] == "Dan Howley"
        assert b["publication"] == "yahoo-finance"

    def test_m920_segment_identified(self):
        seg = self._block()["segment"]
        assert "same consent problem" in seg["title"]
        assert seg["date"] == "2026-09-26"

    def test_m920_apple_arm(self):
        arm = str(self._block()["apple_arm"])
        assert "Live Rewind" in arm
        assert "Siri Recap" in arm

    def test_m920_meta_arm(self):
        arm = str(self._block()["meta_arm"])
        assert "LED" in arm
        assert "Stern" in arm

    def test_m920_parity_bound_finding(self):
        # Thesis-level delta 0.0; fact-intensity residual Meta-harder
        # ~0.10. Journalist-level parity BOUND on the m75
        # privacy-vocabulary-bifurcation family, not an overturning of
        # the aggregate 152-cycle pattern.
        parity = self._block()["register_parity"]
        assert parity["thesis_level_delta"] == 0.0
        assert "~0.10" in parity["fact_intensity_residual"]
        assert "m75" in parity["reading"]

    def test_m920_scorer_manual_illustrative(self):
        scorer = self._block()["scorer"]
        assert "MANUAL ILLUSTRATIVE ONLY" in scorer["method"]
        assert "is_significant False" in scorer["method"]

    def test_m920_statistical_discipline(self):
        discipline = self._block()["statistical_discipline"]
        assert "MANUAL" in discipline
        assert "is_significant false" in discipline
        assert "NOT_CALCULATED" in discipline

    def test_m920_confounders_strong_first(self):
        confounders = self._block()["confounders"]
        assert len(confounders) == 6
        assert confounders[0].startswith("STRONG:")

    def test_m920_not_falsification_member(self):
        b = self._block()
        assert b["falsification_family_member"] is False
        assert b["falsification_ledger"] == 46
        assert b["no_analysis_json_update"] is True


# ---------------------------------------------------------------------------
# 7. m921 (Type C #1149) qualitative discipline
# ---------------------------------------------------------------------------
class TestTypeDM921QualitativeDiscipline1150:
    def _block(self):
        return _yaml(ENTITIES_FILE)[KEY_921]

    def test_m921_run_metadata(self):
        b = self._block()
        assert b["mechanism_id"] == 921
        assert b["iteration"] == 1149
        assert b["iteration_type"] == "C"
        assert "Reach plc H1 2026" in b["mechanism_name"]

    def test_m921_finding(self):
        # First regulated-earnings quantification of unlicensed AI usage
        # in the corpus; AI licensing deals named a near-term strategic
        # priority in the RNS review.
        b = self._block()
        assert "many millions of times a day" in b["finding"]
        assert "H1 2026" in b["finding"] or "half-year" in b["finding"]

    def test_m921_money_flow(self):
        # The pipeline is a stated intention, not a money flow: the
        # usage-based preference restates the publisher-side mirror of
        # the #27 unilateral-pricing geometry.
        b = self._block()
        assert "PREDICTIVE" in b["money_flow"]
        assert "no counterparties named" in b["money_flow"]
        assert 468 in b["connects_to"]

    def test_m921_confounder_strengths(self):
        confounders = self._block()["confounders"]
        assert len(confounders) >= 3
        assert confounders[0]["strength"] == "STRONG"

    def test_m921_research_method(self):
        # m921 carries no research_method field: the method is
        # documented in the iteration-log entry (5 browser.search
        # query sets, 0 browser.open per #503). The block's sources
        # carry the novel-URL discipline markers instead.
        b = self._block()
        sources = b["sources"]
        assert len(sources) == 7
        for s in sources:
            assert s["novel"] is True
            assert s["accessed"] == "2026-10-02"

    def test_m921_sources_novel(self):
        b = self._block()
        assert len(b["sources"]) == 7

    def test_m921_statistical_discipline(self):
        # Financial-incentive mapping per the #609/#614 qualitative
        # boundary: no coverage-tone pair scored, so no
        # uniform-prediction test; tone NOT_SCORED, engine NOT run.
        b = self._block()
        assert b["tone_scored"] is False
        assert b["engine_run"] is False
        assert b["is_significant"] is False
        assert b["verdict"] == "directionally_supported_not_proven"

    def test_m921_not_falsification_member(self):
        b = self._block()
        assert b["falsification_family_member"] is False
        assert "#609" in b["falsification_family"] or \
            "#614" in b["falsification_family"]
        assert FORTY_SEVENTH_MEMBER not in b["falsification_family"]


# ---------------------------------------------------------------------------
# 8. Falsification ledger
# ---------------------------------------------------------------------------
class TestTypeDFalsificationLedger1150:
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

    def test_m919_m920_m921_not_members_ledger_holds(self):
        # m919 (disclosure-geometry), m920 (journalist-level parity
        # bound, not a new prediction test), m921
        # (financial-incentive mapping per #609/#614) are not
        # uniform-prediction tests: the ledger holds at 46.
        b919 = _yaml(NEWS_CORP_FILE)["competitor_relationships"][KEY_919]
        assert "Ledger holds at 46" in b919["ledger"]
        assert "falsification_family_member" not in b919
        b920 = _yaml(JOURNALISTS_FILE)["dan_howley"][
            "competitor_coverage"][KEY_920]
        assert b920["falsification_family_member"] is False
        assert b920["falsification_ledger"] == 46
        b921 = _yaml(ENTITIES_FILE)[KEY_921]
        assert b921["falsification_family_member"] is False


# ---------------------------------------------------------------------------
# 9. Forward-looking staleness (pin lifecycle, subprocess)
# ---------------------------------------------------------------------------
class TestTypeDForwardLookingStaleness1150:
    def test_1145_guard_lifecycle_max_918_trips_by_design(self):
        # #1145's TestGuardLifecycle1145 pinned max 918 and the
        # zero-919 numeric guard. The 919 (#1147), 920 (#1148) and
        # 921 (#1149) landings trip every max/next pin. Designed
        # lifecycle; recorded, not repaired.
        res = _class_run(D1145_FILE, "TestGuardLifecycle1145")
        assert res.returncode != 0, res.stdout[-2000:]

    def test_1145_zero_919_underscore_half_stays_green(self):
        # No underscore-form 919 ever landed as a contiguous literal:
        # the underscore halves of #1145's lifecycle pins survive.
        res = _node_run(
            D1145_FILE,
            "TestGuardLifecycle1145::"
            "test_zero_next_underscore_919_repo_wide")
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1147_max_919_pin_trips_by_design(self):
        # #1147's TestGuardLifecycle1147 pinned max 919 and the
        # zero-920 numeric guard. The m920 (#1148) and m921 (#1149)
        # landings trip them. Designed lifecycle; recorded, not
        # repaired.
        res = _node_run(
            A1147_FILE,
            "TestGuardLifecycle1147::"
            "test_1147_file_pins_max_id_919_and_next_920")
        assert res.returncode != 0, res.stdout[-2000:]

    def test_1147_zero_920_numeric_pin_trips_by_design(self):
        res = _node_run(
            A1147_FILE,
            "TestGuardLifecycle1147::test_zero_next_numeric_920_in_profiles")
        assert res.returncode != 0, res.stdout[-2000:]

    def test_1148_921_numeric_pin_trips_by_design(self):
        # #1148's zero-921 numeric guard trips on the m921 landing
        # (#1149). Designed lifecycle; recorded, not repaired.
        res = _node_run(
            B1148_FILE,
            "TestGuardLifecycle1148::"
            "test_921_numeric_absent_in_profiles")
        assert res.returncode != 0, res.stdout[-2000:]

    def test_1149_forward_guards_stay_green(self):
        # #1149's forward guards (zero-922 numeric/underscore/dash,
        # no-thirty-seventh, format-built-only, iteration-log
        # absence discipline) stay green: this run adds no
        # mechanism and the doc-sync prose uses hyphenated/
        # lowercase forms for the forward guards.
        res = _class_run(C1149_FILE, "TestForwardGuards1149")
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1149_supersession_greens_hold(self):
        # #1149's supersession pins recorded #1148's end-states;
        # Type D lands nothing, so the recorded states hold. The
        # post-commit-flipped no-Type-C-#1149 pin is deselected by
        # design (it flipped red when #1149's main commit landed).
        for node in (
            "TestSupersessionPins1149::"
            "test_1148_921_numeric_guard_lifecycle_fails_by_design",
            "TestSupersessionPins1149::"
            "test_1148_zero_numeric_921_in_profiles_fails_by_design",
            "TestSupersessionPins1149::"
            "test_1148_underscore_920_stays_green",
            "TestSupersessionPins1149::"
            "test_1148_dash_920_stays_green",
            "TestSupersessionPins1149::"
            "test_1148_forty_seventh_absent_stays_green",
            "TestSupersessionPins1149::"
            "test_1148_forty_sixth_intact_stays_green",
            "TestSupersessionPins1149::"
            "test_1148_thirty_fifth_intact_stays_green",
        ):
            res = _node_run(C1149_FILE, node)
            assert res.returncode == 0, (node, res.stdout[-800:])


# ---------------------------------------------------------------------------
# 10. Guard lifecycle (forward guards for #1151)
# ---------------------------------------------------------------------------
class TestGuardLifecycle1150:
    def test_1150_file_pins_max_id_921_and_next_922(self):
        assert _max_numeric_mechanism_id_in_profiles() == 921

    def test_zero_next_numeric_922_in_profiles(self):
        assert _git_grep_tracked(_mech_id_colon(NEXT_NUM), "profiles/") == []

    def test_zero_next_underscore_922_repo_wide(self):
        assert _git_grep_tracked(_mech_underscore(NEXT_NUM)) == []

    def test_zero_next_dash_922_repo_wide(self):
        assert _git_grep_tracked(_mech_dash(NEXT_NUM)) == []

    def test_no_new_mechanisms_below_max(self):
        ids = []
        for dirpath, _, files in os.walk(PROFILES_DIR):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = _read(os.path.join(dirpath, fn))
                    ids += [int(m) for m in re.findall(
                        r"mechanism_id: (\d+)", text)]
        assert 921 in ids
        assert all(i <= 921 for i in ids)

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
# 11. Background-suite verdict (#1145 suite)
# ---------------------------------------------------------------------------
class TestBackgroundSuiteVerdict1150:
    def _log_stats(self):
        text = _read(PRIOR_SUITE_LOG)
        return (os.path.getsize(PRIOR_SUITE_LOG), text.count("."),
                text)

    def test_prior_suite_died_eighteenth_consecutive(self):
        # The #1145-launched background full suite DIED: 385
        # bytes (353 dots, ~0.6% progress), last write Oct 2 08:14
        # PDT, zero summary tokens (no "passed"/"failed" summary,
        # no collected-count token, no "no tests ran"), no live
        # pytest process. Per the #795 convention this is recorded
        # as DIED, not "interrupted": the run produces no usable
        # verdict.
        size, dots, text = self._log_stats()
        assert size == 385, size
        assert dots == 353, dots
        assert "passed" not in text
        assert "failed" not in text
        assert " collected " not in text
        assert "no tests ran" not in text

    def test_no_live_pytest_process(self):
        # The bracket pattern avoids self-matching the pgrep
        # command line (phantom-pid class per AGENTS.md).
        result = subprocess.run(
            ["pgrep", "-f", "[p]ytest.*type_d_1145"],
            capture_output=True,
            text=True,
        )
        assert result.returncode != 0, (
            "a pytest process for the #1145 suite must not still be "
            "alive when its verdict is recorded")

    def test_last_write_stale(self):
        # The prior suite's last write predates this run by hours,
        # far beyond any healthy inter-write bound.
        import time
        mtime = os.path.getmtime(PRIOR_SUITE_LOG)
        assert mtime < time.time() - 7200, mtime

    def test_tombstone_lineage_advances_to_89th(self):
        # EIGHTEENTH consecutive background-suite death of the new
        # streak (the 57-run streak ENDED at #1085 when the #1080
        # suite completed). Tombstone lineage advances
        # EIGHTY-EIGHTH -> EIGHTY-NINTH; recorded in the #1150
        # iteration-log entry. Deselected pre-commit (log entry is
        # written in the doc-sync step per #719/#721).
        text = _read(LOG_FILE)
        assert "EIGHTY-NINTH" in text


# ---------------------------------------------------------------------------
# 12. Fresh synthetic engine calibration (new values, not #1145's)
# ---------------------------------------------------------------------------
class TestSyntheticEngineCalibration1150:
    # Scratch-run values produced at this run (Fri 2026-10-02 ~12:05
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
        meta = [-0.72, -0.61, -0.83, -0.55, -0.77, -0.66, -0.70]
        comp = [0.21, 0.09, 0.30, -0.02, 0.17, 0.11, -0.06]
        result = calc(meta, comp)
        assert result.asymmetry_score == pytest.approx(-0.8057142857142857)
        assert result.t_statistic == pytest.approx(-13.497613382013478)
        assert result.p_value < 1e-6
        assert result.cohens_d == pytest.approx(-7.214777830661362)
        assert result.is_significant is True
        assert result.confidence_interval_lower == pytest.approx(
            -0.9085714285714286)
        assert result.confidence_interval_upper == pytest.approx(
            -0.6956785714285715)
        # The strong arm-swap negates the asymmetry exactly.
        swapped = calc(comp, meta)
        assert swapped.asymmetry_score == pytest.approx(0.8057142857142857)

    def test_near_null_pair_stays_silent(self):
        calc = self._calculate()
        meta = [0.03, -0.06, 0.05, -0.02, 0.01, -0.04, 0.02]
        comp = [-0.04, 0.02, -0.01, 0.06, -0.05, 0.03, -0.02]
        result = calc(meta, comp)
        assert result.asymmetry_score == pytest.approx(1.08e-18)
        assert result.p_value > 0.05
        assert result.is_significant is False

    def test_degenerate_n1_contract(self):
        # The classic degenerate guard: n=1 per arm yields t=0.0,
        # p=1.0, d=0.0 and is_significant False regardless of the
        # illustrative pair mean (here the m919 Anthropic-vs-Meta
        # illustrative arm pair -0.35 vs -0.125).
        calc = self._calculate()
        result = calc([-0.35], [-0.125])
        assert result.asymmetry_score == pytest.approx(-0.225)
        assert result.t_statistic == 0.0
        assert result.p_value == 1.0
        assert result.cohens_d == 0.0
        assert result.is_significant is False

    def test_engine_layer_not_finding_layer(self):
        # The m919/m920/m921 mechanisms never promote engine
        # significance to a finding: all three carry manual-only
        # discipline (m919 MANUAL ILLUSTRATIVE, m920 MANUAL
        # ILLUSTRATIVE, m921 tone NOT_SCORED).
        b919 = _yaml(NEWS_CORP_FILE)["competitor_relationships"][KEY_919]
        assert "MANUAL ILLUSTRATIVE ONLY" in b919["scorer"]["method"]
        assert "is_significant False" in b919["statistical_discipline"]
        b920 = _yaml(JOURNALISTS_FILE)["dan_howley"][
            "competitor_coverage"][KEY_920]
        assert "MANUAL ILLUSTRATIVE ONLY" in b920["scorer"]["method"]
        assert "is_significant false" in b920["statistical_discipline"]
        b921 = _yaml(ENTITIES_FILE)[KEY_921]
        assert b921["is_significant"] is False
        assert b921["engine_run"] is False


# ---------------------------------------------------------------------------
# 13. Suite re-launch
# ---------------------------------------------------------------------------
class TestSuiteRelaunch1150:
    def test_relaunch_log_path_written(self):
        # The re-launched full suite log exists in goal hidden_files
        # (created by this run's background launch before commit).
        assert os.path.exists(SUITE_LOG), (
            "the #1150 background suite must be re-launched to "
            + SUITE_LOG
            + " before the main commit"
        )

    def test_relaunch_log_is_full_inventory(self):
        # The re-launch runs WITHOUT -x: the full inventory
        # (calendar by-design failures included) is needed for the
        # #1155 triage. The log must hold pytest progress output,
        # not just a header.
        text = _read(SUITE_LOG)
        assert text.count(".") > 100, (
            "the re-launched suite log should accumulate dot "
            "progress; got %d dots" % text.count(".")
        )

    def test_next_type_d_run_owns_the_verdict(self):
        # Per the #795 convention, the NEXT Type D run (#1155)
        # checks this suite's verdict; this run only records the
        # launch.
        assert "type_d_1150_full_suite.log" in SUITE_LOG


# ---------------------------------------------------------------------------
# 14. Doc-sync per #719 (fails pre-commit by design; passes post-sync)
# ---------------------------------------------------------------------------
class TestTypeDDocSync1150:
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
        assert "README_TEST_COUNT = 60600" in own
        assert "README_FILE_COUNT = 1475" in own


# ---------------------------------------------------------------------------
# 15. Iteration log per #721 (fails pre-commit by design)
# ---------------------------------------------------------------------------
class TestTypeDIterationLog1150:
    def _entry(self):
        return _read(LOG_FILE)

    def test_iteration_log_entry_present(self):
        assert "## #1150 Type D" in self._entry()

    def test_iteration_log_hashes_registered(self):
        text = self._entry()
        assert ANCHORED_SHA in text
        assert "1150-1154 window" in text

    def test_iteration_log_rotation_guard(self):
        text = self._entry()
        assert "FIRST leg" in text
        assert "D->E->A->B->C" in text
        assert "CLOSED the 1145-1149 window" in text

    def test_iteration_log_suite_verdict_recorded(self):
        text = self._entry()
        assert "EIGHTY-NINTH" in text


# ---------------------------------------------------------------------------
# 16. Literal discipline per #715/#1116 (guarded forms format-built only)
# ---------------------------------------------------------------------------
class TestLiteralDiscipline1150:
    def test_format_built_only_in_this_file(self):
        # The #1116 lesson: guarded forms must never appear
        # contiguously in test-file prose. Every guarded needle is
        # format-built at runtime.
        own = _read(__file__)
        assert "mechanism" + "_921" not in own
        assert "mechanism" + "-921" not in own
        assert "mechanism_id: " + "921" not in own
        assert "mechanism" + "_922" not in own
        assert "mechanism" + "-922" not in own
        assert "mechanism_id: " + "922" not in own
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
class TestInflightIsolation1150:
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
