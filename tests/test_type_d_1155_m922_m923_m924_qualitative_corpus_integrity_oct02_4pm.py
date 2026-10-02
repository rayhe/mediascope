"""Type D -- Iteration #1155 (Fri 2026-10-02 16:00 PDT): m922/m923/m924
qualitative-discipline verification + post-1150-1154 corpus integrity
(max numeric mechanism_id 924; zero next-number nine-two-five keys in
numeric/underscore/dash mechanism forms - the 925 needles are
format-built per #715 so no guard-literal carrier file exists; the
m922/m923/m924 block keys carry no mechanism-number substring
(designed keying), so they are plain literals; the #1150/#1151/#1152/
#1153/#1154 window files are NOT edited by this run - their now-stale
forward-looking pins are recorded as fail-by-design via subprocess in
the staleness class (#1150's max-921 + zero-922-numeric pins trip on
the 922/923/924 landings while its zero-922 underscore/dash halves
stay green; #1151's #1150-class-green staleness pin flips now that the
#1150 guard class no longer passes; #1152's max-922 + zero-923-numeric
pins trip on the 923/924 landings; #1153's max-923-committed +
zero-924-numeric pins trip on the 924 landing; #1154's forward guards
stay GREEN - Type D lands no mechanism; #1154's supersession greens
hold except the post-commit Type-C-#1154 pin which flipped by design
and is deselected); ledger holds at 46 with the FORTY-SIXTH
member-claim form present in exactly one profiles file
(profiles/the-verge.yaml, m907 block, 2 occurrences - the #1127
designed pattern) and the forty-seventh member-claim form absent
repo-wide (needle format-built per #715); the THIRTY-FIFTH
relationship direction is present in competitor-entities.yaml (m915
METER-THEN-INVITE, landed at #1139); the thirty-sixth AND
thirty-seventh relationship-direction claim forms are both absent
repo-wide (needles format-built per #715)) + the #1150 background-suite
verdict (DIED at 7821 bytes / 7028 dots, ~11% progress, 6 F marks, with
last write Oct 2 14:00 PDT and zero summary tokens, no live pytest
process - NINETEENTH consecutive background-suite death of the new
streak; the 57-run streak ENDED at #1085 when the #1080 suite
completed; tombstone lineage advances EIGHTY-NINTH -> NINETIETH) +
fresh synthetic engine calibration (new values, not #1150's) +
re-launch of the full suite as a background process writing to goal
hidden_files type_d_1155_full_suite.log WITHOUT -x (the full inventory,
calendar by-design failures included, is needed for the #1160 triage;
the next Type D run checks its verdict per the #795 convention).

Type D FIRST leg of the 1155-1159 window, OPENING it
(D->E->A->B->C). Committed predecessor #1154 Type C (03:00 PM PDT Oct 2)
CLOSED the 1150-1154 window (D #1150, E #1151, A #1152, B #1153,
C #1154). Rotation per the #565 anchor + rotation guard.
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
- m922 (Type A #1152, profiles/guardian.yaml competitor_relationships/
  google/ 4-space block key, numeric colon-form field; block key count 1 -
  colon-form line only, designed): Sep-26 Guardian original "Broken
  promises, confiscated land" names Google's hyperscale AI datacentre in
  Tarluvada, Andhra Pradesh in investigative environmental-exploitation
  register (village-head quote "now Google is bringing them here"); Oct-2
  Guardian Weekly cover (Porter) "NOT IN MY BACKYARD" elevates the frame;
  bounded-absence arm: zero Guardian originals on the Oct-1 SDNY Castel
  $3.2B AdX-monopoly damages ruling; scorer Google arms [-0.45, -0.40] mean
  -0.425 vs carried Meta arms [-0.45, -0.50] (m487/m537) mean -0.475,
  illustrative delta +0.05 near-null NOT significant; counter-evidence m487
  Aug-2026 renewal register (-0.15, -0.05) - register SELECTION dominates,
  not entity targeting. NOT a falsification-family member (standing
  coverage_prediction "neutral" - the ledger carries the #754 count-only
  convention); ledger holds at 46.
- m923 (Type B #1153, profiles/careers/journalists.yaml jessica_conditt
  competitor_coverage 4-space block key, numeric colon-form field; block key
  count 3 - colon-form line + block_key field + test_file field echo,
  designed): two weeks after the Sep-9 Apple Audio Intelligence adversarial
  arm (-0.55 carried per #807: 'spy equipment' / 'spyware feature' dek
  variant), the Meta arm REMAINS a bounded absence: zero written Meta
  wearables coverage by Conditt across her Muck Rack list, Engadget author
  page, and the smart-glasses tag page during the Sep-23/24 Connect 2026
  launch window (bylines routed to Bell/Low/Moon/Holt - beat assignment in
  action); her Meta-tagged bylines are the Instagram logo roast ('corporate
  ragebait' snark), ruling out the entity-softness reading; absence NOT
  scored. NOT a falsification-family member (no boolean; ledger count 46
  per the #754 convention); ledger holds at 46.
- m924 (Type C #1154, profiles/competitor-entities.yaml zero-indent
  top-level block key, numeric colon-form field; block key count 2 -
  colon-form line + block_key field, designed): FIRST corpus documentation
  of the control-of-the-meter contest - Google's black-box Search Console
  "AI earnings" widget (#27 unilateral pricing, m891) vs SPUR's open
  content-telemetry standard with invitation-only AI Licensing Advisory
  Board (m915 METER-THEN-INVITE, the thirty-fifth direction); publisher
  walk-away framing (large publishers sitting out to pressure Google);
  Spur founder David Buttle's "more hedge than true market"
  characterization ("Google builds infrastructure in case courts or
  regulators mandate compensation for journalistic content in AI
  systems"); temporal extension of the m891 family, no new direction. NOT
  a falsification-family member (financial-incentive mapping per #609/
  #614); ledger holds at 46.

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
GUARDIAN_FILE = os.path.join(PROFILES_DIR, "guardian.yaml")
JOURNALISTS_FILE = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
ENTITIES_FILE = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
VERGE_FILE = os.path.join(PROFILES_DIR, "the-verge.yaml")
LOG_FILE = os.path.join(REPO_ROOT, "iteration-log.md")
README_FILE = os.path.join(REPO_ROOT, "README.md")
ARCH_FILE = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")

# Block keys are plain literals: none carries a mechanism-number
# substring (designed keying per #715). Iterations 1152/1153/1154 are
# the landing iterations, not the mechanism ids.
KEY_922 = ("type_a_1152_guardian_google_sep26_oct02_datacenter_"
           "adversarial_register_vs_carried_meta_arms")
KEY_923 = ("type_b_1153_jessica_conditt_engadget_meta_wearables_"
           "bounded_absence_temporal_extension_m674_oct02_2pm")
KEY_924 = ("type_c_1154_google_pay_per_value_post_rate_reception_"
           "walk_away_hedge_not_market_oct02_3pm")
OWN_BASENAME = ("test_type_d_1155_m922_m923_m924_qualitative_"
                "corpus_integrity_oct02_4pm.py")

# Predecessor test files for supersession pins.
D1150_FILE = ("test_type_d_1150_m919_m920_m921_qualitative_"
              "corpus_integrity_oct02_12pm.py")
E1151_FILE = ("test_type_e_1151_podcast_sentiment_"
              "153rd_verification_oct02_12pm.py")
A1152_FILE = ("test_type_a_1152_guardian_google_sep26_oct02_datacenter_"
              "adversarial_register_vs_carried_meta_arms_oct02_1pm.py")
B1153_FILE = ("test_type_b_1153_jessica_conditt_engadget_meta_wearables_"
              "bounded_absence_temporal_extension_m674_oct02_2pm.py")
C1154_FILE = ("test_type_c_1154_google_pay_per_value_post_rate_reception_"
              "hedge_not_market_oct02_3pm.py")

# Prior-window background suite (verdict rendered this run) and this
# run's re-launched suite.
PRIOR_SUITE_LOG = os.path.join(
    os.path.expanduser("~"),
    "workspace",
    "goals",
    "mediascope-meta-wearables-press-analysis",
    "hidden_files",
    "type_d_1150_full_suite.log",
)
SUITE_LOG = os.path.join(
    os.path.expanduser("~"),
    "workspace",
    "goals",
    "mediascope-meta-wearables-press-analysis",
    "hidden_files",
    "type_d_1155_full_suite.log",
)

# Patched post-commit once README/ARCHITECTURE doc-sync lands (per #719).
README_TEST_COUNT = 60877  # post-doc-sync total (60877 + N; patched)
README_FILE_COUNT = 1479  # post-doc-sync total (patched)
TEST_BASENAME = OWN_BASENAME

# Anchor placeholder per #565: patched to the main commit's 40-char SHA in the
# anchor followup. Deselect the placeholder test in post-commit full runs.
ANCHORED_SHA = "0" * 40

MECH_NUM = 924
NEXT_NUM = 925
PREV_NUM = 923

# Fragment-built direction needles per #715 (never contiguous here).
_T35 = "THIRTY-" + "FIFTH relationship direction"
_T36 = "THIRTY-" + "SIXTH relationship direction"
_T37 = "THIRTY-" + "SEVENTH relationship direction"
_T38 = "THIRTY-" + "EIGHTH relationship direction"


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

# One-parse-per-file cache: the journalists/guardian YAMLs are large
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
class TestNovelty1155:
    def test_no_type_d_1155_test_file_preexisting(self):
        hits = glob.glob(
            os.path.join(TESTS_DIR, "test_type_d_1155*.py"))
        assert hits == [os.path.join(TESTS_DIR, OWN_BASENAME)], hits

    def test_no_type_d_1155_in_git_log(self):
        # Deselected post-main-commit per #565: the main commit does
        # not exist yet pre-commit.
        log = _git("log", "--oneline", "--grep=Type D #1155")
        assert "Type D #1155" not in log, log

    def test_max_id_is_924(self):
        needle = _mech_id_colon(MECH_NUM)
        hits = _git_grep_tracked(needle, "profiles/")
        assert hits == ["profiles/competitor-entities.yaml"], hits

    def test_zero_925_numeric_forms_in_profiles(self):
        needle = _mech_id_colon(NEXT_NUM)
        assert _git_grep_tracked(needle, "profiles/") == []

    def test_block_keys_unique_in_home_yamls(self):
        assert _key_count_in_file(KEY_922, GUARDIAN_FILE) == 1
        assert _key_count_in_file(KEY_923, JOURNALISTS_FILE) == 3
        assert _key_count_in_file(KEY_924, ENTITIES_FILE) == 2
        # Designed keying: no mechanism-number substring in any
        # block key, so they are plain literals here.
        for key, num in ((KEY_922, "922"), (KEY_923, "923"),
                         (KEY_924, "924")):
            assert num not in key, key

    def test_no_type_e_1156_in_git_log(self):
        # The next leg must not exist yet.
        log = _git("log", "--oneline", "--grep=Type E #1156")
        assert "Type E #1156" not in log, log


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------
class TestTypeDRotationGuard1155:
    def test_rotation_window_opens_1155(self):
        # 1155-1159 window: D opens, then E -> A -> B -> C.
        log = _git("log", "--oneline", "--grep=Type C #1154")
        assert "Type C #1154" in log, log
        entry = _read(LOG_FILE)
        assert "1150-1154 window" in entry
        # The "CLOSED the 1150-1154 window" predecessor line is
        # written by this run's doc-sync (TestTypeDIterationLog1155).

    def test_predecessor_1154_chain_present(self):
        log = _git("log", "--format=%H %s")
        assert "Type C #1154" in log, log
        for sha8 in ("a032e49d", "3571d5f1", "31bbe553", "4b8b93a6",
                     "38d74753"):
            assert sha8 in log, sha8

    def test_window_order_d_e_a_b_c(self):
        log = _git("log", "--oneline")
        i1150 = log.index("Type D #1150")
        i1151 = log.index("Type E #1151")
        i1152 = log.index("Type A #1152")
        i1153 = log.index("Type B #1153")
        i1154 = log.index("Type C #1154")
        # Reverse-chronological log: later commits appear first.
        assert i1154 < i1153 < i1152 < i1151 < i1150

    def test_anchor_sha_placeholder_pre_commit(self):
        # Deselect this test in post-commit full runs: the anchor
        # followup patches ANCHORED_SHA to the main commit's 40-char
        # SHA per #565.
        assert ANCHORED_SHA == "0" * 40

    def test_anchor_sha_shape_40_hex(self):
        # Holds pre-commit (zero placeholder) and post-patch (commit
        # SHA).
        assert len(ANCHORED_SHA) == 40
        assert all(c in "0123456789abcdef" for c in ANCHORED_SHA)

    def test_next_window_leg_is_type_e(self):
        # The 1155-1159 window continues with Type E #1156 after
        # this run.
        assert "1155-1159" in (__doc__ or "")


# ---------------------------------------------------------------------------
# 3. Novelty anchor
# ---------------------------------------------------------------------------
class TestTypeDNoveltyAnchor1155:
    def _non_1155_lines(self, grep_pat):
        log = _git("log", "--oneline", "--grep=" + grep_pat)
        lines = [line for line in log.split("\n") if line.strip()]
        return [line for line in lines if "1155" not in line]

    def test_no_prior_type_d_1155_in_log(self):
        assert self._non_1155_lines("Type D #1155") == []

    def test_no_prior_1155_1159_window_claim(self):
        assert self._non_1155_lines("1155-1159") == []


# ---------------------------------------------------------------------------
# 4. Corpus integrity
# ---------------------------------------------------------------------------
class TestTypeDCorpusIntegrity1155:
    def test_m922_block_present_in_guardian_yaml(self):
        data = _yaml(GUARDIAN_FILE)
        block = data["competitor_relationships"]["google"][KEY_922]
        assert block["mechanism_id"] == 922
        assert block["iteration"] == 1152
        assert block["iteration_type"] == "A"

    def test_m923_block_present_in_journalists_yaml(self):
        data = _yaml(JOURNALISTS_FILE)
        block = data["jessica_conditt"]["competitor_coverage"][KEY_923]
        assert block["mechanism_id"] == 923
        assert block["iteration"] == 1153
        assert block["iteration_type"] == "B"

    def test_m924_block_present_in_competitor_entities_yaml(self):
        data = _yaml(ENTITIES_FILE)
        block = data[KEY_924]
        assert block["mechanism_id"] == 924
        assert block["iteration"] == 1154
        assert block["iteration_type"] == "C"

    def test_max_mechanism_id_is_924(self):
        assert _max_numeric_mechanism_id_in_profiles() == 924

    def test_zero_925_forms_repo_wide(self):
        assert _git_grep_tracked(_mech_id_colon(925)) == []
        assert _git_grep_tracked(_mech_underscore(925)) == []
        assert _git_grep_tracked(_mech_dash(925)) == []

    def test_no_new_mechanisms_below_max(self):
        ids = []
        for dirpath, _, files in os.walk(PROFILES_DIR):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = _read(os.path.join(dirpath, fn))
                    ids += [int(m) for m in re.findall(
                        r"mechanism_id: (\d+)", text)]
        assert 924 in ids
        assert all(i <= 924 for i in ids)

    def test_m922_key_count_is_designed(self):
        # Colon-form line only: the guardian.yaml blocks carry no
        # block_key/test_file echo fields.
        assert _key_count_in_file(KEY_922, GUARDIAN_FILE) == 1

    def test_m923_key_count_is_designed(self):
        # Colon-form line + block_key field + test_file field echo
        # of the same string in the filename.
        assert _key_count_in_file(KEY_923, JOURNALISTS_FILE) == 3

    def test_m924_key_count_is_designed(self):
        # Colon-form line + block_key field.
        assert _key_count_in_file(KEY_924, ENTITIES_FILE) == 2


# ---------------------------------------------------------------------------
# 5. m922 (Type A #1152) qualitative discipline
# ---------------------------------------------------------------------------
class TestTypeDM922QualitativeDiscipline1155:
    def _block(self):
        return _yaml(GUARDIAN_FILE)["competitor_relationships"][
            "google"][KEY_922]

    def test_m922_run_metadata(self):
        b = self._block()
        assert b["mechanism_id"] == 922
        assert b["iteration"] == 1152
        assert b["iteration_type"] == "A"
        assert b["iteration_time"] == "2026-10-02 13:00 PDT"
        assert "The Guardian" in b["publication_focus"]
        assert "Google" in b["entity_pair"]
        assert "Meta" in b["entity_pair"]

    def test_m922_discovery_summary(self):
        # Sep-26 Guardian original names Google's hyperscale AI
        # datacentre in Tarluvada; Oct-2 Weekly cover elevates the
        # frame; bounded-absence arm on the SDNY Castel ruling.
        b = self._block()
        disc = b["discovery_summary"]
        assert "Broken promises, confiscated land" in disc
        assert "Tarluvada" in disc
        assert "$3.2B" in disc or "3.2B" in disc

    def test_m922_scorer_manual_illustrative(self):
        # Google arms [-0.45, -0.40] mean -0.425 vs carried Meta arms
        # [-0.45, -0.50] mean -0.475: illustrative delta +0.05
        # near-null, NOT significant. Register SELECTION (not entity
        # targeting) is the counter-evidence.
        scorer = self._block()["scorer"]
        assert scorer["google_new_arms"] == [-0.45, -0.4]
        assert scorer["meta_carried_arms"] == [-0.45, -0.5]
        assert scorer["google_new_mean"] == pytest.approx(-0.425)
        assert scorer["meta_carried_mean"] == pytest.approx(-0.475)
        assert scorer["asymmetry_delta"] == pytest.approx(0.05)
        assert scorer["is_significant"] is False
        assert "MANUAL ILLUSTRATIVE ONLY" in scorer["note"]
        assert "No engine run." in scorer["note"]

    def test_m922_counter_evidence_register_selection(self):
        b = self._block()
        ce = b["counter_evidence"]
        assert "m487" in str(ce) or "-0.15" in str(ce)

    def test_m922_confounders_strong_first(self):
        confounders = self._block()["confounders"]
        assert len(confounders) == 5
        assert confounders[0]["strength"] == "STRONG"

    def test_m922_research_method(self):
        b = self._block()
        method = b["research_method"]
        assert "4 browser.search query sets" in method
        assert "0 browser.open" in method
        assert "verbatim" in method

    def test_m922_statistical_discipline(self):
        discipline = self._block()["statistical_discipline"]
        assert "MANUAL/QUALITATIVE ONLY" in discipline
        assert "NOT_CALCULATED" in discipline
        assert "is_significant False" in discipline
        assert "engine NOT run" in discipline

    def test_m922_artifact_discipline(self):
        b = self._block()
        assert b["artifact_grade"] is False
        assert b["no_analysis_json_update"] is True
        assert "Correlation is not causation" in str(
            b["correlation_not_causation"])

    def test_m922_not_falsification_member(self):
        # m922 carries no falsification_family_member boolean and no
        # falsification_family prose field: the not-a-member status is
        # carried by the ledger count field (which per the #754
        # convention records the count only, never the next-member
        # literal). Standing coverage_prediction is "neutral".
        b = self._block()
        assert "NOT a falsification-family member" in b["ledger"]
        assert "Ledger holds at 46" in b["ledger"]
        assert "falsification_family_member" not in b
        blob = yaml.safe_dump(b, allow_unicode=True)
        assert FORTY_SEVENTH_MEMBER not in blob


# ---------------------------------------------------------------------------
# 6. m923 (Type B #1153) qualitative discipline
# ---------------------------------------------------------------------------
class TestTypeDM923QualitativeDiscipline1155:
    def _block(self):
        return _yaml(JOURNALISTS_FILE)["jessica_conditt"][
            "competitor_coverage"][KEY_923]

    def test_m923_run_metadata(self):
        b = self._block()
        assert b["mechanism_id"] == 923
        assert b["iteration"] == 1153
        assert b["iteration_type"] == "B"
        assert "Jessica Conditt" in b["journalist"]
        assert b["publication_focus"] == "engadget"

    def test_m923_pattern_bounded_absence(self):
        # Two weeks after the Sep-9 Apple Audio Intelligence
        # adversarial arm, the Meta arm remains a bounded absence;
        # absence is not a register and is NOT scored.
        b = self._block()
        assert "bounded-absence" in b["pattern"]
        assert "NOT scored" in b["statistical_discipline"] or \
            "NOT_SCORED" in b["statistical_discipline"]

    def test_m923_meta_arm(self):
        arm = str(self._block()["meta_arm"])
        assert "Connect" in arm or "Meta" in arm

    def test_m923_apple_arm_carried(self):
        arm = str(self._block()["apple_arm"])
        assert "-0.55" in arm or "Audio Intelligence" in arm

    def test_m923_statistical_discipline(self):
        discipline = self._block()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE ONLY" in discipline
        assert "is_significant False" in discipline
        assert "Engine NOT run" in discipline
        assert "NOT_CALCULATED" in discipline

    def test_m923_confounders_strong_first(self):
        confounders = self._block()["confounders"]
        assert len(confounders) == 7
        assert confounders[0]["level"] == "STRONG"

    def test_m923_novelty(self):
        nov = self._block()["novelty"]
        assert "FIRST" in nov
        assert "Jessica Conditt" in nov

    def test_m923_not_falsification_member(self):
        # m923 carries no falsification_family_member boolean: the
        # not-a-member status is carried by the ledger count field
        # per the #754 convention.
        b = self._block()
        assert "falsification_family_member" not in b
        assert b["falsification_ledger"] == 46
        assert "ledger holds at 46" in b["falsification_family"]
        assert FORTY_SEVENTH_MEMBER not in b["falsification_family"]


# ---------------------------------------------------------------------------
# 7. m924 (Type C #1154) qualitative discipline
# ---------------------------------------------------------------------------
class TestTypeDM924QualitativeDiscipline1155:
    def _block(self):
        return _yaml(ENTITIES_FILE)[KEY_924]

    def test_m924_run_metadata(self):
        b = self._block()
        assert b["mechanism_id"] == 924
        assert b["iteration"] == 1154
        assert b["iteration_type"] == "C"
        assert b["iteration_time"] == "2026-10-02 15:00 PDT"
        assert b["connects_to"] == [891, 915, 921, 702, 666]

    def test_m924_finding_hedge_core(self):
        # Publisher walk-away framing plus Buttle's hedge
        # characterization: the payer-built meter as anticipatory
        # compliance infrastructure.
        f = self._block()["finding"]
        assert "hedge than true market" in f
        assert "Walking Away" in f
        assert "courts or regulators mandate compensation" in f

    def test_m924_finding_meter_contest(self):
        f = self._block()["finding"]
        assert "walk-away frame" in f
        assert "hedge characterization" in f

    def test_m924_money_flow_three_channels(self):
        mf = self._block()["money_flow"]
        assert "OBSERVED" in mf
        assert "DOCUMENTED" in mf
        assert "PREDICTIVE" in mf

    def test_m924_confounders_strong_first(self):
        confounders = self._block()["confounders"]
        assert len(confounders) == 5
        assert confounders[0]["strength"] == "STRONG"
        assert confounders[1]["strength"] == "STRONG"

    def test_m924_sources_novel(self):
        srcs = self._block()["sources"]
        assert len(srcs) == 4
        assert all(s["novel"] is True for s in srcs)
        assert all(s["accessed"] == "2026-10-02" for s in srcs)

    def test_m924_statistical_discipline(self):
        # Financial-incentive mapping per the #609/#614 qualitative
        # boundary: no coverage-tone pair scored, so no
        # uniform-prediction test; tone NOT_SCORED, engine NOT run.
        b = self._block()
        assert b["tone_scored"] is False
        assert b["engine_run"] is False
        assert b["is_significant"] is False
        assert b["verdict"] == "directionally_supported_not_proven"
        assert b["no_analysis_json_update"] is True
        assert b["artifact_grade"] is False

    def test_m924_not_falsification_member(self):
        b = self._block()
        assert b["falsification_family_member"] is False
        assert "ledger holds at 46" in b["falsification_family"]
        assert "no uniform-prediction test" in b["falsification_family"]
        assert FORTY_SEVENTH_MEMBER not in b["falsification_family"]


# ---------------------------------------------------------------------------
# 8. Falsification ledger
# ---------------------------------------------------------------------------
class TestTypeDFalsificationLedger1155:
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

    def test_m922_m923_m924_not_members_ledger_holds(self):
        # m922 (standing "neutral" coverage_prediction), m923
        # (bounded-absence temporal extension, no uniform prediction
        # test), m924 (financial-incentive mapping per #609/#614) are
        # not uniform-prediction tests: the ledger holds at 46.
        b922 = _yaml(GUARDIAN_FILE)["competitor_relationships"][
            "google"][KEY_922]
        assert "Ledger holds at 46" in b922["ledger"]
        assert "falsification_family_member" not in b922
        b923 = _yaml(JOURNALISTS_FILE)["jessica_conditt"][
            "competitor_coverage"][KEY_923]
        assert b923["falsification_ledger"] == 46
        assert "falsification_family_member" not in b923
        b924 = _yaml(ENTITIES_FILE)[KEY_924]
        assert b924["falsification_family_member"] is False
        assert "ledger holds at 46" in b924["falsification_family"]

# ---------------------------------------------------------------------------
# 9. Forward-looking staleness (subprocess pin lifecycle)
# ---------------------------------------------------------------------------
class TestTypeDForwardLookingStaleness1155:
    def test_1150_guard_lifecycle_max_921_trips_by_design(self):
        # #1150's TestGuardLifecycle1150 pinned max 921 and the
        # zero-922 numeric guard. The 922 (#1152), 923 (#1153) and 924
        # (#1154) landings trip them. Designed lifecycle; recorded,
        # not repaired.
        res = _class_run(D1150_FILE, "TestGuardLifecycle1150")
        assert res.returncode != 0, res.stdout[-2000:]

    def test_1150_zero_922_underscore_half_stays_green(self):
        # No underscore-form 922 ever landed as a contiguous literal:
        # the underscore half of #1150's lifecycle pins survives.
        res = _node_run(
            D1150_FILE,
            "TestGuardLifecycle1150::"
            "test_zero_next_underscore_922_repo_wide")
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1150_zero_922_dash_half_stays_green(self):
        res = _node_run(
            D1150_FILE,
            "TestGuardLifecycle1150::"
            "test_zero_next_dash_922_repo_wide")
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1151_1150_class_green_pin_flips_by_design(self):
        # #1151's staleness pin asserted #1150's whole guard-lifecycle
        # class stays green. It can no longer pass: two of the class's
        # pins (max-921, zero-922-numeric) tripped on the 922/923/924
        # landings. Designed lifecycle; recorded, not repaired.
        res = _class_run(E1151_FILE, "TestStalenessPins")
        assert res.returncode != 0, res.stdout[-2000:]

    def test_1152_max_922_pin_trips_by_design(self):
        # #1152's TestGuardLifecycle1152 pinned max 922 and the
        # zero-923 numeric guard. The m923 (#1153) and m924 (#1154)
        # landings trip them. Designed lifecycle; recorded, not
        # repaired.
        res = _node_run(
            A1152_FILE,
            "TestGuardLifecycle1152::"
            "test_1152_file_pins_max_id_922_and_next_923")
        assert res.returncode != 0, res.stdout[-2000:]

    def test_1152_zero_923_numeric_pin_trips_by_design(self):
        res = _node_run(
            A1152_FILE,
            "TestGuardLifecycle1152::"
            "test_zero_next_numeric_923_in_profiles")
        assert res.returncode != 0, res.stdout[-2000:]

    def test_1152_underscore_dash_923_halves_stay_green(self):
        for node in (
                "TestGuardLifecycle1152::"
                "test_zero_next_underscore_923_repo_wide",
                "TestGuardLifecycle1152::"
                "test_zero_next_dash_923_repo_wide"):
            res = _node_run(A1152_FILE, node)
            assert res.returncode == 0, (node, res.stdout[-2000:])

    def test_1153_max_923_committed_pin_scoped_stays_green(self):
        # #1153's max-923-committed pin scopes to the COMMITTED
        # journalists.yaml (git show HEAD), which still maxes at 923 -
        # m924 landed in competitor-entities.yaml, a different file. So
        # this pin stays green; the design-failing pin for the 924
        # landing is the zero-924-numeric pin (covered below).
        res = _node_run(
            B1153_FILE,
            "TestMechanismNovelty1153::"
            "test_max_numeric_mechanism_id_is_923_committed")
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1153_zero_924_numeric_pin_trips_by_design(self):
        res = _node_run(
            B1153_FILE,
            "TestMechanismNovelty1153::"
            "test_zero_numeric_924_in_profiles")
        assert res.returncode != 0, res.stdout[-2000:]

    def test_1153_underscore_dash_923_halves_stay_green(self):
        for node in (
                "TestMechanismNovelty1153::"
                "test_zero_underscore_923_repo_wide",
                "TestMechanismNovelty1153::"
                "test_zero_dash_923_repo_wide"):
            res = _node_run(B1153_FILE, node)
            assert res.returncode == 0, (node, res.stdout[-2000:])

    def test_1154_forward_guards_stay_green(self):
        # #1154's forward guards (zero-925 numeric/underscore/dash,
        # no-thirty-seventh, no-thirty-eighth, format-built-only,
        # iteration-log absence discipline) stay green: this run adds
        # no mechanism and the doc-sync prose uses hyphenated/
        # lowercase forms for the forward guards.
        res = _class_run(C1154_FILE, "TestForwardGuards1154")
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1154_max_924_pin_stays_green(self):
        res = _node_run(
            C1154_FILE,
            "TestMechanismNovelty1154::"
            "test_max_numeric_mechanism_id_is_924")
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1154_forty_seventh_ledger_pin_stays_green(self):
        res = _node_run(
            C1154_FILE,
            "TestLedger46Holds1154::"
            "test_forty_seventh_absent_repo_wide")
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1154_supersession_greens_hold(self):
        # #1154's supersession pins recorded #1153's end-states;
        # Type D lands nothing, so the recorded states hold. The
        # post-commit-flipped no-Type-C-#1154 pin is deselected by
        # design (it flipped red when #1154's main commit landed).
        for node in (
            "TestSupersessionPins1154::"
            "test_1153_max_923_pin_stays_green_own_block_scope",
            "TestSupersessionPins1154::"
            "test_1153_zero_924_numeric_pin_fails_by_design",
            "TestSupersessionPins1154::"
            "test_1153_zero_924_forward_guards_fail_by_design",
            "TestSupersessionPins1154::"
            "test_1153_underscore_923_stays_green",
            "TestSupersessionPins1154::"
            "test_1153_dash_923_stays_green",
            "TestSupersessionPins1154::"
            "test_1153_forty_seventh_absent_stays_green",
            "TestSupersessionPins1154::"
            "test_1153_forty_sixth_intact_stays_green",
            "TestSupersessionPins1154::"
            "test_1153_thirty_fifth_intact_stays_green",
            "TestSupersessionPins1154::"
            "test_1153_no_thirty_sixth_stays_green",
        ):
            res = _node_run(C1154_FILE, node)
            assert res.returncode == 0, (node, res.stdout[-2000:])


# ---------------------------------------------------------------------------
# 10. Guard lifecycle (forward guards for #1156)
# ---------------------------------------------------------------------------
class TestGuardLifecycle1155:
    def test_1155_file_pins_max_id_924_and_next_925(self):
        assert _max_numeric_mechanism_id_in_profiles() == 924

    def test_zero_next_numeric_925_in_profiles(self):
        assert _git_grep_tracked(_mech_id_colon(NEXT_NUM), "profiles/") == []

    def test_zero_next_underscore_925_repo_wide(self):
        assert _git_grep_tracked(_mech_underscore(NEXT_NUM)) == []

    def test_zero_next_dash_925_repo_wide(self):
        assert _git_grep_tracked(_mech_dash(NEXT_NUM)) == []

    def test_no_new_mechanisms_below_max(self):
        ids = []
        for dirpath, _, files in os.walk(PROFILES_DIR):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = _read(os.path.join(dirpath, fn))
                    ids += [int(m) for m in re.findall(
                        r"mechanism_id: (\d+)", text)]
        assert 924 in ids
        assert all(i <= 924 for i in ids)

    def test_no_thirty_sixth_direction_claim(self):
        hits = [p for p in _git_grep_tracked(_T36)]
        assert hits == [], hits

    def test_no_thirty_seventh_direction_claim(self):
        hits = [p for p in _git_grep_tracked(_T37)]
        assert hits == [], hits

    def test_no_thirty_eighth_direction_claim(self):
        hits = [p for p in _git_grep_tracked(_T38)]
        assert hits == [], hits

    def test_no_forty_seventh_member_claim(self):
        hits = [p for p in _git_grep_tracked(FORTY_SEVENTH_MEMBER)]
        assert hits == [], hits

    def test_no_forty_eighth_member_claim(self):
        hits = [p for p in _git_grep_tracked(FORTY_EIGHTH_MEMBER)]
        assert hits == [], hits


# ---------------------------------------------------------------------------
# 11. Background-suite verdict (#1150 suite)
# ---------------------------------------------------------------------------
class TestBackgroundSuiteVerdict1155:
    def _log_stats(self):
        text = _read(PRIOR_SUITE_LOG)
        return (os.path.getsize(PRIOR_SUITE_LOG), text.count("."),
                text.count("F"), text)

    def test_prior_suite_died_nineteenth_consecutive(self):
        # The #1150-launched background full suite DIED: 7821
        # bytes (7028 dots, 6 F marks, ~11% progress), last write
        # Oct 2 14:00 PDT, zero summary tokens (no "passed"/"failed"
        # summary, no collected-count token, no "no tests ran"), no
        # live pytest process. Per the #795 convention this is
        # recorded as DIED, not "interrupted": the run produces no
        # usable verdict.
        size, dots, fs, text = self._log_stats()
        assert size == 7821, size
        assert dots == 7028, dots
        assert fs == 6, fs
        assert "passed" not in text
        assert "failed" not in text
        assert " collected " not in text
        assert "no tests ran" not in text

    def test_no_live_pytest_process(self):
        # The bracket pattern avoids self-matching the pgrep
        # command line (phantom-pid class per AGENTS.md).
        result = subprocess.run(
            ["pgrep", "-f", "[p]ytest.*type_d_1150"],
            capture_output=True,
            text=True,
        )
        assert result.returncode != 0, (
            "a pytest process for the #1150 suite must not still be "
            "alive when its verdict is recorded")

    def test_last_write_stale(self):
        # The prior suite's last write predates this run by hours,
        # far beyond any healthy inter-write bound.
        import time
        mtime = os.path.getmtime(PRIOR_SUITE_LOG)
        assert mtime < time.time() - 7200, mtime

    def test_tombstone_lineage_advances_to_90th(self):
        # NINETEENTH consecutive background-suite death of the new
        # streak (the 57-run streak ENDED at #1085 when the #1080
        # suite completed). Tombstone lineage advances
        # EIGHTY-NINTH -> NINETIETH; recorded in the #1155
        # iteration-log entry. Deselected pre-commit (log entry is
        # written in the doc-sync step per #719/#721).
        text = _read(LOG_FILE)
        assert "NINETIETH" in text

# ---------------------------------------------------------------------------
# 12. Fresh synthetic engine calibration (new values, not #1150's)
# ---------------------------------------------------------------------------
class TestSyntheticEngineCalibration1155:
    # Scratch-run values produced at this run (Fri 2026-10-02 ~16:05
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
        meta = [-0.68, -0.59, -0.77, -0.51, -0.74, -0.63, -0.66]
        comp = [0.18, 0.05, 0.27, -0.04, 0.14, 0.08, -0.09]
        result = calc(meta, comp)
        assert result.asymmetry_score == pytest.approx(-0.7385714285714285)
        assert result.t_statistic == pytest.approx(-12.758627756024891)
        assert result.p_value < 1e-6
        assert result.cohens_d == pytest.approx(-6.819773398347081)
        assert result.is_significant is True
        assert result.confidence_interval_lower == pytest.approx(
            -0.8385714285714285)
        assert result.confidence_interval_upper == pytest.approx(
            -0.6300000000000001)
        # The strong arm-swap negates the asymmetry exactly.
        swapped = calc(comp, meta)
        assert swapped.asymmetry_score == pytest.approx(0.7385714285714285)

    def test_near_null_pair_stays_silent(self):
        calc = self._calculate()
        meta = [0.04, -0.05, 0.06, -0.03, 0.02, -0.02, 0.05]
        comp = [-0.03, 0.04, -0.02, 0.05, -0.06, 0.01, -0.04]
        result = calc(meta, comp)
        assert result.asymmetry_score == pytest.approx(0.01714285714285714)
        assert result.p_value > 0.05
        assert result.is_significant is False

    def test_degenerate_n1_contract(self):
        # The classic degenerate guard: n=1 per arm yields t=0.0,
        # p=1.0, d=0.0 and is_significant False regardless of the
        # illustrative pair mean (here the m922 Google-vs-Meta
        # illustrative arm pair -0.425 vs -0.475, delta +0.05).
        calc = self._calculate()
        result = calc([-0.425], [-0.475])
        assert result.asymmetry_score == pytest.approx(0.04999999999999999)
        assert result.t_statistic == 0.0
        assert result.p_value == 1.0
        assert result.cohens_d == 0.0
        assert result.is_significant is False

    def test_engine_layer_not_finding_layer(self):
        # The m922/m923/m924 mechanisms never promote engine
        # significance to a finding: all three carry manual-only
        # discipline (m922 MANUAL ILLUSTRATIVE, m923 MANUAL
        # ILLUSTRATIVE, m924 tone NOT_SCORED / engine NOT run).
        b922 = _yaml(GUARDIAN_FILE)["competitor_relationships"][
            "google"][KEY_922]
        assert "MANUAL ILLUSTRATIVE ONLY" in b922["scorer"]["note"]
        assert "is_significant False" in b922["statistical_discipline"]
        b923 = _yaml(JOURNALISTS_FILE)["jessica_conditt"][
            "competitor_coverage"][KEY_923]
        assert "MANUAL ILLUSTRATIVE ONLY" in b923["statistical_discipline"]
        assert "is_significant False" in b923["statistical_discipline"]
        b924 = _yaml(ENTITIES_FILE)[KEY_924]
        assert b924["is_significant"] is False
        assert b924["engine_run"] is False


# ---------------------------------------------------------------------------
# 13. Suite re-launch
# ---------------------------------------------------------------------------
class TestSuiteRelaunch1155:
    def test_relaunch_log_path_written(self):
        # The re-launched full suite log exists in goal hidden_files
        # (created by this run's background launch before commit).
        assert os.path.exists(SUITE_LOG), (
            "the #1155 background suite must be re-launched to "
            + SUITE_LOG
            + " before the main commit"
        )

    def test_relaunch_log_is_full_inventory(self):
        # The re-launch runs WITHOUT -x: the full inventory
        # (calendar by-design failures included) is needed for the
        # #1160 triage. The log must hold pytest progress output,
        # not just a header.
        text = _read(SUITE_LOG)
        assert text.count(".") > 100, (
            "the re-launched suite log should accumulate dot "
            "progress; got %d dots" % text.count(".")
        )

    def test_next_type_d_run_owns_the_verdict(self):
        # Per the #795 convention, the NEXT Type D run (#1160)
        # checks this suite's verdict; this run only records the
        # launch.
        assert "type_d_1155_full_suite.log" in SUITE_LOG


# ---------------------------------------------------------------------------
# 14. Doc-sync per #719 (fails pre-commit by design; passes post-sync)
# ---------------------------------------------------------------------------
class TestTypeDDocSync1155:
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
        assert "README_TEST_COUNT = %d" % README_TEST_COUNT in own
        assert "README_FILE_COUNT = %d" % README_FILE_COUNT in own


# ---------------------------------------------------------------------------
# 15. Iteration log per #721 (fails pre-commit by design)
# ---------------------------------------------------------------------------
class TestTypeDIterationLog1155:
    def _entry(self):
        return _read(LOG_FILE)

    def test_iteration_log_entry_present(self):
        assert "## #1155 Type D" in self._entry()

    def test_iteration_log_hashes_registered(self):
        text = self._entry()
        assert ANCHORED_SHA in text
        assert "1155-1159 window" in text

    def test_iteration_log_rotation_guard(self):
        text = self._entry()
        assert "FIRST leg" in text
        assert "D->E->A->B->C" in text
        assert "CLOSED the 1150-1154 window" in text

    def test_iteration_log_suite_verdict_recorded(self):
        text = self._entry()
        assert "NINETIETH" in text


# ---------------------------------------------------------------------------
# 16. Literal discipline per #715/#1116 (guarded forms format-built only)
# ---------------------------------------------------------------------------
class TestLiteralDiscipline1155:
    def test_format_built_only_in_this_file(self):
        # The #1116 lesson: guarded forms must never appear
        # contiguously in test-file prose. Every guarded needle is
        # format-built at runtime.
        own = _read(__file__)
        assert "mechanism" + "_924" not in own
        assert "mechanism" + "-924" not in own
        assert "mechanism_id: " + "924" not in own
        assert "mechanism" + "_925" not in own
        assert "mechanism" + "-925" not in own
        assert "mechanism_id: " + "925" not in own
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
class TestInflightIsolation1155:
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
