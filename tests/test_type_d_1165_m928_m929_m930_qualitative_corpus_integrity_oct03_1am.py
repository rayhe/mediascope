"""Type D -- Iteration #1165 (Sat 2026-10-03 01:00 PDT): m928/m929/m930
qualitative-discipline verification + post-1160-1164 corpus integrity
(max numeric mechanism_id 930; zero next-number nine-three-one keys in
numeric/underscore/dash mechanism forms - the 931 needles are
format-built per #715 so no guard-literal carrier file exists; the
m928/m929/m930 block keys carry no mechanism-number substring
(designed keying), so they are plain literals; the #1160/#1161/#1162/
#1163/#1164 window files are NOT edited by this run - their now-stale
forward-looking pins are recorded as fail-by-design via subprocess in
the staleness class (#1160's max-927 + zero-928-numeric pins trip on
the 928/929/930 landings while its zero-928 underscore/dash halves
stay green; #1161's max-927 + zero-928-numeric pins trip while its
underscore/dash halves stay green; #1162's max-928 + zero-929-numeric
pins trip on the 929/930 landings; #1163's zero-930 guard trips on
the numeric half landing while its underscore/dash halves stay green;
#1164's zero-931 forward guards stay GREEN - Type D lands no
mechanism; #1164's supersession greens hold); ledger holds at 46 with
the FORTY-SIXTH member-claim form present in exactly one profiles
file (profiles/the-verge.yaml, m907 block, 2 occurrences - the #1127
designed pattern) and the forty-seventh member-claim form absent
repo-wide (needle format-built per #715); the THIRTY-FIFTH
relationship direction is present in competitor-entities.yaml (m915
METER-THEN-INVITE, landed at #1139) and the THIRTY-FOURTH is present
as well; the thirty-sixth AND thirty-seventh relationship-direction
claim forms are both absent repo-wide (needles format-built per
#715)) + the #1160 background-suite verdict (DIED at 3863 bytes /
3467 dots / 1 F mark, last write Oct 2 22:03:58 PDT, zero summary
tokens, no live pytest process - TWENTY-FIFTH consecutive
background-suite death of the new streak; the 57-run streak ENDED at
#1085 when the #1080 suite completed; tombstone lineage advances
NINETY-FIRST -> NINETY-SECOND) + fresh synthetic engine calibration
(new values, not #1160's) + re-launch of the full suite as
a background process writing to goal hidden_files
type_d_1165_full_suite.log WITHOUT -x (the full inventory, calendar
by-design failures included, is needed for the #1170 triage; the next
Type D run checks its verdict per the #795 convention).

Type D FIRST leg of the 1165-1169 window, OPENING it
(D->E->A->B->C). Committed predecessor #1164 Type C (12:00 AM PDT Oct 3)
CLOSED the 1160-1164 window (D #1160, E #1161, A #1162, B #1163,
C #1164). Rotation per the #565 anchor + rotation guard.
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
- m928 (Type A #1162, profiles/gizmodo.yaml competitor_relationships/
  snap/ 4-space block key, numeric colon-form field; block key count
  1 - colon-form line only, designed): FIRST dedicated corpus
  mechanism on Gizmodo's Sep-23-2026 Snap-vs-Xreal comparison hands-on
  by Kyle Barr ("In the Race for the Dorkiest AR Glasses, Only One
  Seems Built for Today") at Qualcomm's Snapdragon Summit -
  comparative-sobriety register (Xreal arm +0.10 MANUAL ILLUSTRATIVE)
  vs carried m577 Gizmodo x Meta adversarial band (-0.617 mean):
  illustrative Xreal-minus-Meta delta +0.717, same magnitude as
  m748's Snap-minus-Meta +0.717; Xreal arm +0.10 vs carried m748 Snap
  arm +0.10: delta 0.00 near-null (symmetric non-Meta wearable band).
  Extends the m919 disclosure_asymmetry strand descriptively on the
  PRESENT-disclosure side (explicit Qualcomm vendor-paid-travel
  disclosure line in full). NOT a falsification-family member
  (same-publication temporal replication of the #862 m748 family
  per the #1143 precedent, not a new prediction test); ledger
  holds at 46.
- m929 (Type B #1163, journalists.yaml Mark Gurman mapping-form entry,
  competitor_coverage/ 4-space YAML key, numeric colon-form field;
  YAML key uses the mechanism_1163_... form while the block_key
  field carries the type_b_1163_... form - they differ by design;
  each string count 1): temporal reversal bound on the m593
  access-prediction - the same access-dependent Apple-beat reporter
  now applies the warmer register to Meta (Sep-27-2026 Power On Meta
  VR Glasses hands-on, product_praise_hands_on, +0.35 MANUAL
  ILLUSTRATIVE) and the execution-skeptical roadmap register to
  Apple (+0.10): illustrative Meta-minus-Apple delta +0.25,
  sign-reversed vs m593's -0.55. NOT a falsification-family member
  (no financial gradient under test; Bloomberg financial-null per
  #85/m593 makes the deal-softness prediction NULL, not failed).
  The reversal binds the ACCESS driver class; ledger holds at 46.
- m930 (Type C #1164, profiles/competitor-entities.yaml zero-indent
  top-level block key, numeric colon-form field; block key count 2 -
  colon-form line + block_key field, designed): FIRST dedicated corpus
  mechanism on the Sep 17-19 2026 Reddit v. Anthropic demurrer denial
  (Judge Harold Kahn, SF Superior Court) - three of five claims
  proceed on an implied-in-fact User Agreement contract (breach of
  contract, interference with contract, California UCL); two tossed
  (unjust enrichment, trespass to chattels) with Oct 16 refile leave.
  The court-validated enforcement leg of the m614 pay-or-sue
  bifurcation (connects_to [614, 636]); seven novel sources; five
  confounders strong-first. Money flow PROSPECTIVE, enforcement
  channel VALIDATED. NOT a falsification-family member (no
  coverage-tone pair scored, per the #609/#614 qualitative
  boundary); ledger holds at 46.

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
GIZMODO_FILE = os.path.join(PROFILES_DIR, "gizmodo.yaml")
JOURNALISTS_FILE = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
ENTITIES_FILE = os.path.join(PROFILES_DIR, "competitor-entities.yaml")
VERGE_FILE = os.path.join(PROFILES_DIR, "the-verge.yaml")
LOG_FILE = os.path.join(REPO_ROOT, "iteration-log.md")
README_FILE = os.path.join(REPO_ROOT, "README.md")
ARCH_FILE = os.path.join(REPO_ROOT, "docs", "ARCHITECTURE.md")

# Block keys are plain literals: none carries a mechanism-number
# substring (designed keying per #715). Iterations 1162/1163/1164 are
# the landing iterations, not the mechanism ids.
KEY_928 = ("gizmodo_snap_xreal_aura_sobriety_comparison_register_"
           "1162_sep23")
YAML_KEY_929 = ("mechanism_1163_mark_gurman_bloomberg_power_on_meta_vr_"
                "glasses_vs_apple_execution_skepticism_m593_reversal_"
                "sep27")
BLOCK_KEY_929 = ("type_b_1163_mark_gurman_bloomberg_power_on_meta_vr_"
                 "glasses_praise_vs_apple_vision_pro_execution_"
                 "skepticism_m593_reversal_sep27_oct02_11pm")
# The YAML key for the m929 block (mechanism_1163_... form) differs
# from the block_key field string (type_b_1163_... form) by design;
# each appears exactly once in journalists.yaml.
KEY_930 = ("type_c_1164_reddit_anthropic_demurrer_denial_kahn_"
           "pay_or_sue_enforcement_oct03_12am")
OWN_BASENAME = ("test_type_d_1165_m928_m929_m930_qualitative_"
                "corpus_integrity_oct03_1am.py")

# Predecessor test files for supersession pins.
D1160_FILE = ("test_type_d_1160_m925_m926_m927_qualitative_"
              "corpus_integrity_oct02_9pm.py")
E1161_FILE = ("test_type_e_1161_podcast_sentiment_"
              "155th_verification_oct02_9pm.py")
A1162_FILE = ("test_type_a_1162_gizmodo_snap_xreal_aura_sep23_"
              "comparison_vs_carried_meta_arms_oct02_10pm.py")
B1163_FILE = ("test_type_b_1163_mark_gurman_bloomberg_power_on_meta_vr_"
              "glasses_vs_apple_execution_skepticism_m593_reversal_"
              "sep27_oct02_11pm.py")
C1164_FILE = ("test_type_c_1164_reddit_anthropic_demurrer_denial_kahn_"
              "pay_or_sue_enforcement_oct03_12am.py")

# Prior-window background suite (verdict rendered this run) and this
# run's re-launched suite.
PRIOR_SUITE_LOG = os.path.join(
    os.path.expanduser("~"),
    "workspace",
    "goals",
    "mediascope-meta-wearables-press-analysis",
    "hidden_files",
    "type_d_1160_full_suite.log",
)
SUITE_LOG = os.path.join(
    os.path.expanduser("~"),
    "workspace",
    "goals",
    "mediascope-meta-wearables-press-analysis",
    "hidden_files",
    "type_d_1165_full_suite.log",
)

# Patched post-commit once README/ARCHITECTURE doc-sync lands (per #719).
README_TEST_COUNT = 61740  # post-doc-sync total (61638 + 102)
README_FILE_COUNT = 1490  # post-doc-sync total
TEST_BASENAME = OWN_BASENAME

# Anchor placeholder per #565: patched to the main commit's 40-char SHA in the
# anchor followup. Deselect the placeholder test in post-commit full runs.
ANCHORED_SHA = "0" * 40  # patched in the anchor followup per #565 (Type D self-anchor)

MECH_NUM = 930
NEXT_NUM = 931
PREV_NUM = 929

# Fragment-built direction needles per #715 (never contiguous here).
_T34 = "THIRTY-" + "FOURTH relationship direction"
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

# One-parse-per-file cache: the journalists/gizmodo YAMLs are large
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


def _mark_gurman_entry():
    # Mark Gurman's journalist entry lives in the journalists.yaml
    # top-level list as a mapping-form entry; his mechanism blocks
    # are keys of its competitor_coverage mapping.
    for entry in _yaml(JOURNALISTS_FILE)["journalists"]:
        if isinstance(entry, dict) and entry.get("name") == "Mark Gurman":
            return entry
    raise AssertionError("Mark Gurman entry not found in journalists.yaml")


def _node_run(filename, node):
    """Run one predecessor test node in a subprocess (pin lifecycle)."""
    target = os.path.join(TESTS_DIR, filename) + "::" + node
    env = dict(os.environ)
    env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    venv_py = os.path.join(REPO_ROOT, ".venv", "bin", "python")
    return subprocess.run(
        [venv_py, "-m", "pytest", target, "-q", "--no-header",
         "-o", "addopts=", "-p", "no:cacheprovider"],
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
         "-o", "addopts=", "-p", "no:cacheprovider"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        env=env,
        timeout=300,
    )

# ---------------------------------------------------------------------------
# 1. Novelty
# ---------------------------------------------------------------------------
class TestNovelty1165:
    def test_no_type_d_1165_test_file_preexisting(self):
        hits = glob.glob(
            os.path.join(TESTS_DIR, "test_type_d_1165*.py"))
        assert hits == [os.path.join(TESTS_DIR, OWN_BASENAME)], hits

    def test_no_type_d_1165_in_git_log(self):
        # Deselected post-main-commit per #565: the main commit does
        # not exist yet pre-commit.
        log = _git("log", "--oneline", "--grep=Type D #1165")
        assert "Type D #1165" not in log, log

    def test_max_id_is_930(self):
        needle = _mech_id_colon(MECH_NUM)
        hits = _git_grep_tracked(needle, "profiles/")
        assert hits == ["profiles/competitor-entities.yaml"], hits

    def test_zero_931_numeric_forms_in_profiles(self):
        needle = _mech_id_colon(NEXT_NUM)
        assert _git_grep_tracked(needle, "profiles/") == []

    def test_block_keys_unique_in_home_yamls(self):
        assert _key_count_in_file(KEY_928, GIZMODO_FILE) == 1
        assert _key_count_in_file(YAML_KEY_929, JOURNALISTS_FILE) == 1
        assert _key_count_in_file(BLOCK_KEY_929, JOURNALISTS_FILE) == 1
        assert _key_count_in_file(KEY_930, ENTITIES_FILE) == 2
        # Designed keying: no mechanism-number substring in any
        # block key, so they are plain literals here.
        for key, num in ((KEY_928, "928"), (YAML_KEY_929, "929"),
                         (BLOCK_KEY_929, "929"), (KEY_930, "930")):
            assert num not in key, key

    def test_no_type_e_1166_in_git_log(self):
        # The next leg must not exist yet.
        log = _git("log", "--oneline", "--grep=Type E #1166")
        assert "Type E #1166" not in log, log


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------
class TestTypeDRotationGuard1165:
    def test_rotation_window_opens_1165(self):
        # 1165-1169 window: D opens, then E -> A -> B -> C.
        log = _git("log", "--oneline", "--grep=Type C #1164")
        assert "Type C #1164" in log, log
        entry = _read(LOG_FILE)
        assert "1160-1164 window" in entry
        # The "CLOSED the 1160-1164 window" predecessor line is
        # written by this run's doc-sync (TestTypeDIterationLog1165).

    def test_predecessor_1164_chain_present(self):
        log = _git("log", "--format=%H %s")
        assert "Type C #1164" in log, log
        for sha8 in ("ff67d154", "76631e0a", "6b6919dc", "3070072f"):
            assert sha8 in log, sha8

    def test_window_order_d_e_a_b_c(self):
        log = _git("log", "--oneline")
        i1160 = log.index("Type D #1160")
        i1161 = log.index("Type E #1161")
        i1162 = log.index("Type A #1162")
        i1163 = log.index("Type B #1163")
        i1164 = log.index("Type C #1164")
        # Reverse-chronological log: later commits appear first.
        assert i1164 < i1163 < i1162 < i1161 < i1160

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
        # The 1165-1169 window continues with Type E #1166 after
        # this run.
        assert "1165-1169" in (__doc__ or "")


# ---------------------------------------------------------------------------
# 3. Novelty anchor
# ---------------------------------------------------------------------------
class TestTypeDNoveltyAnchor1165:
    def _non_1165_lines(self, grep_pat):
        # --grep matches commit BODIES too: the #1164 main commit
        # body forward-references "Type D #1165" / "1165-1169"
        # ("next window 1165-1169 opens with Type D #1165"), so a
        # bare --grep hit is not a novelty violation. Drop this
        # run's own commits (their subjects carry the bare
        # iteration number); what remains must not SUBJECT-claim
        # this run.
        log = _git("log", "--format=%H %s", "--grep=" + grep_pat)
        lines = [line for line in log.split("\n") if line.strip()]
        return [line for line in lines
                if "1165" not in line.split(" ", 1)[1]]

    def test_no_prior_type_d_1165_in_log(self):
        for line in self._non_1165_lines("Type D #1165"):
            subject = line.split(" ", 1)[1]
            assert "Type D #1165" not in subject, line

    def test_no_prior_1165_1169_window_claim(self):
        for line in self._non_1165_lines("1165-1169"):
            subject = line.split(" ", 1)[1]
            assert "1165-1169" not in subject, line

# ---------------------------------------------------------------------------
# 4. Corpus integrity
# ---------------------------------------------------------------------------
class TestTypeDCorpusIntegrity1165:
    def test_m928_block_present_in_gizmodo_yaml(self):
        data = _yaml(GIZMODO_FILE)
        block = data["competitor_relationships"]["snap"][KEY_928]
        assert block["mechanism_id"] == 928
        assert block["iteration"] == 1162
        assert block["iteration_type"] == "A"

    def test_m929_block_present_in_journalists_yaml(self):
        block = _mark_gurman_entry()["competitor_coverage"][YAML_KEY_929]
        assert block["mechanism_id"] == 929
        assert block["iteration"] == 1163
        assert block["iteration_type"] == "B"

    def test_m930_block_present_in_competitor_entities_yaml(self):
        data = _yaml(ENTITIES_FILE)
        block = data[KEY_930]
        assert block["mechanism_id"] == 930
        assert block["iteration"] == 1164
        assert block["iteration_type"] == "C"

    def test_max_mechanism_id_is_930(self):
        assert _max_numeric_mechanism_id_in_profiles() == 930

    def test_zero_931_forms_repo_wide(self):
        assert _git_grep_tracked(_mech_id_colon(931)) == []
        assert _git_grep_tracked(_mech_underscore(931)) == []
        assert _git_grep_tracked(_mech_dash(931)) == []

    def test_no_new_mechanisms_below_max(self):
        ids = []
        for dirpath, _, files in os.walk(PROFILES_DIR):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = _read(os.path.join(dirpath, fn))
                    ids += [int(m) for m in re.findall(
                        r"mechanism_id: (\d+)", text)]
        assert 930 in ids
        assert all(i <= 930 for i in ids)

    def test_m928_key_count_is_designed(self):
        # Colon-form line only: the gizmodo.yaml m928 block carries
        # no block_key/test_file echo fields.
        assert _key_count_in_file(KEY_928, GIZMODO_FILE) == 1

    def test_m929_key_counts_are_designed(self):
        # The YAML key (mechanism_1163_... form) and the block_key
        # field string (type_b_1163_... form) differ by design; each
        # appears exactly once.
        assert _key_count_in_file(YAML_KEY_929, JOURNALISTS_FILE) == 1
        assert _key_count_in_file(BLOCK_KEY_929, JOURNALISTS_FILE) == 1

    def test_m930_key_count_is_designed(self):
        # Colon-form line + block_key field.
        assert _key_count_in_file(KEY_930, ENTITIES_FILE) == 2


# ---------------------------------------------------------------------------
# 5. m928 (Type A #1162) qualitative discipline
# ---------------------------------------------------------------------------
class TestTypeDM928QualitativeDiscipline1165:
    def _block(self):
        return _yaml(GIZMODO_FILE)["competitor_relationships"][
            "snap"][KEY_928]

    def test_m928_run_metadata(self):
        b = self._block()
        assert b["mechanism_id"] == 928
        assert b["iteration"] == 1162
        assert b["iteration_type"] == "A"
        assert b["time_pdt"] == "22:00"
        assert "Gizmodo" in b["publication_focus"]
        assert "Snap/Xreal" in b["competitor_pair"]
        assert "Meta" in b["competitor_pair"]

    def test_m928_new_arm_register(self):
        b = self._block()
        arm = b["articles_new"][0]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == 0.10
        assert arm["register"] == "comparative_sobriety_hands_on"
        assert "Dorkiest AR Glasses" in arm["title"]

    def test_m928_carried_arms_per_807(self):
        b = self._block()
        carried = b["carried_arms_per_807"]
        assert any("m577" in c["mechanism"] for c in carried)
        assert any("m748" in c["mechanism"] for c in carried)
        assert "-0.617" in " ".join(c["arms"] for c in carried)

    def test_m928_scorer_manual_illustrative(self):
        b = self._block()
        scorer = b["scorer_MANUAL_ILLUSTRATIVE_ONLY"]
        assert "+0.717" in scorer
        assert "NOT_CALCULATED" in scorer
        assert "engine NOT run" in scorer
        assert "is_significant False" in scorer
        assert "delta 0.00 near-null" in scorer

    def test_m928_disclosure_observation(self):
        b = self._block()
        assert "disclosure_asymmetry" in b["disclosure_observation"]
        assert "m919" in b["disclosure_observation"]
        assert "PRESENT-disclosure" in b["disclosure_observation"]
        assert "Qualcomm" in b["disclosure_observation"]

    def test_m928_confounders_strong_first(self):
        b = self._block()
        confs = b["confounders_strong_first"]
        assert len(confs) == 5
        assert confs[0].startswith("STRONG")
        assert confs[1].startswith("STRONG")

    def test_m928_research_method(self):
        b = self._block()
        assert "9 browser.search query sets" in b["research_method"]
        assert "0 browser.open" in b["research_method"]

    def test_m928_statistical_discipline(self):
        b = self._block()
        sd = b["statistical_discipline"]
        assert "MANUAL/QUALITATIVE ONLY" in sd
        assert "is_significant False" in sd
        assert "engine NOT run" in sd
        assert "directionally_supported_not_proven" in sd
        assert "NOT artifact-grade" in sd


# ---------------------------------------------------------------------------
# 6. m929 (Type B #1163) qualitative discipline
# ---------------------------------------------------------------------------
class TestTypeDM929QualitativeDiscipline1165:
    def _block(self):
        return _mark_gurman_entry()["competitor_coverage"][YAML_KEY_929]

    def test_m929_run_metadata(self):
        b = self._block()
        assert b["mechanism_id"] == 929
        assert b["type"] == "B"
        assert b["journalist"] == "Mark Gurman"
        assert b["iteration"] == 1163
        assert b["iteration_type"] == "B"
        assert b["iteration_time"] == "2026-10-02 23:00 PDT"
        assert b["publication"] == "bloomberg"

    def test_m929_pattern_temporal_reversal(self):
        b = self._block()
        assert "m593" in b["pattern"]
        assert "reversal" in b["pattern"].lower()
        assert "access" in b["pattern"].lower()

    def test_m929_new_meta_vr_arm(self):
        b = self._block()
        arm = b["new_meta_vr_arm"]
        assert arm["tone_illustrative"] == 0.35
        assert arm["register"] == "product_praise_hands_on"
        assert "Meta VR Glasses" in arm["piece"]

    def test_m929_new_apple_arm(self):
        b = self._block()
        arm = b["new_apple_arm"]
        assert arm["tone_illustrative"] == 0.10
        assert arm["register"] == "execution_skepticism_roadmap"

    def test_m929_scorer_delta_reversal(self):
        b = self._block()
        scorer = b["asymmetry_scorer"]
        assert scorer["new_meta_tone"] == 0.35
        assert scorer["new_apple_tone"] == 0.10
        assert scorer["illustrative_delta_meta_minus_apple"] == 0.25
        assert scorer["m593_carried_delta"] == -0.55
        assert scorer["direction_reversal_vs_m593"] is True
        assert scorer["p_value"] == "NOT_CALCULATED"
        assert scorer["is_significant"] is False
        assert "MANUAL ILLUSTRATIVE" in scorer["tone_basis"]
        assert scorer["statistical_contract"] == "degenerate_n1_per_arm"
        assert scorer["artifact_grade"] is False

    def test_m929_block_key_field_differs_by_design(self):
        b = self._block()
        assert b["block_key"] == BLOCK_KEY_929
        assert b["block_key"] != YAML_KEY_929

    def test_m929_confounders_ranked_strong_first(self):
        b = self._block()
        strong = b["confounders_ranked"]["strong"]
        assert len(strong) == 2
        assert "Product merit" in strong[0]

    def test_m929_research_method(self):
        b = self._block()
        assert "22 browser.search query sets" in b["research_method"]
        assert "REJECTED candi" in b["research_method"]

    def test_m929_not_falsification_member(self):
        b = self._block()
        assert "NOT a falsification-family member" in b[
            "falsification_family"]
        assert "ledger holds at 46" in b["falsification_family"]


# ---------------------------------------------------------------------------
# 7. m930 (Type C #1164) qualitative discipline
# ---------------------------------------------------------------------------
class TestTypeDM930QualitativeDiscipline1165:
    def _block(self):
        return _yaml(ENTITIES_FILE)[KEY_930]

    def test_m930_run_metadata(self):
        b = self._block()
        assert b["mechanism_id"] == 930
        assert b["iteration"] == 1164
        assert b["iteration_type"] == "C"
        assert b["iteration_time"] == "2026-10-03 00:00 PDT"
        assert b["type"] == "financial_incentive_mapping"

    def test_m930_finding_seven_legs(self):
        b = self._block()
        assert "Seven legs" in b["finding"]
        assert "demurrer denial" in b["finding"]
        assert "Harold Kahn" in b["finding"]
        assert "implied-in-fact" in b["finding"]

    def test_m930_money_flow_validated_enforcement(self):
        b = self._block()
        assert "VALIDATED" in b["money_flow"]
        assert "Enforcement channel" in b["money_flow"]
        assert "m614" in b["money_flow"]

    def test_m930_connects_to(self):
        b = self._block()
        assert b["connects_to"] == [614, 636]

    def test_m930_sources_seven_novel(self):
        b = self._block()
        assert len(b["sources"]) == 7
        assert all(s["novel"] is True for s in b["sources"])
        assert any("ccstartup.com" in s["url"] for s in b["sources"])

    def test_m930_confounders_strong_first(self):
        b = self._block()
        confs = b["confounders"]
        assert len(confs) == 5
        assert confs[0]["strength"] == "STRONG"
        assert confs[1]["strength"] == "STRONG"
        assert "demurrer" in confs[0]["text"].lower()

    def test_m930_statistical_discipline(self):
        b = self._block()
        assert b["tone_scored"] is False
        assert b["engine_run"] is False
        assert b["is_significant"] is False
        assert b["verdict"] == "directionally_supported_not_proven"
        assert b["no_analysis_json_update"] is True
        assert b["artifact_grade"] is False

    def test_m930_novelty_research_method(self):
        b = self._block()
        assert "FIRST dedicated corpus mechanism" in b["novelty"]
        assert "Temporal extension of m614" in b["novelty"]

    def test_m930_not_falsification_member(self):
        b = self._block()
        assert b["falsification_family_member"] is False
        assert "ledger holds at 46" in b["falsification_family"].lower()
        assert "thirty-sixth" in b["falsification_family"]

# ---------------------------------------------------------------------------
# 8. Falsification ledger
# ---------------------------------------------------------------------------
class TestTypeDFalsificationLedger1165:
    def test_forty_sixth_claim_in_exactly_one_profiles_file(self):
        hits = _git_grep_tracked(FORTY_SIXTH_MEMBER, "profiles/")
        assert hits == ["profiles/the-verge.yaml"], hits

    def test_forty_sixth_claim_count_is_designed(self):
        out = subprocess.run(
            ["git", "grep", "-c", "-F", FORTY_SIXTH_MEMBER, "--",
             "profiles/the-verge.yaml"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
        )
        # The #1127 designed pattern: exactly 2 occurrences in the
        # m907 block.
        assert out.stdout.strip().endswith(":2"), out.stdout

    def test_no_forty_seventh_member_claim_repo_wide(self):
        assert _git_grep_tracked(FORTY_SEVENTH_MEMBER) == []

    def test_thirty_fifth_direction_in_competitor_entities(self):
        hits = _git_grep_tracked(_T35, "profiles/")
        assert hits == ["profiles/competitor-entities.yaml"], hits

    def test_thirty_fourth_direction_in_competitor_entities(self):
        hits = _git_grep_tracked(_T34, "profiles/")
        assert "profiles/competitor-entities.yaml" in hits, hits

    def test_no_thirty_sixth_direction_claim_repo_wide(self):
        assert _git_grep_tracked(_T36) == []

    def test_no_thirty_seventh_direction_claim_repo_wide(self):
        assert _git_grep_tracked(_T37) == []

    def test_m928_m929_m930_not_members_ledger_holds(self):
        b928 = _yaml(GIZMODO_FILE)["competitor_relationships"][
            "snap"][KEY_928]
        assert "NOT a member" in b928["falsification_family"]
        b929 = _mark_gurman_entry()["competitor_coverage"][YAML_KEY_929]
        assert "NOT a falsification-family member" in b929[
            "falsification_family"]
        b930 = _yaml(ENTITIES_FILE)[KEY_930]
        assert b930["falsification_family_member"] is False
        for text in (b928["falsification_family"],
                     b929["falsification_family"],
                     b930["falsification_family"]):
            assert "ledger holds at 46" in text.lower(), text


# ---------------------------------------------------------------------------
# 9. Forward-looking staleness (predecessor pin lifecycle via subprocess)
# ---------------------------------------------------------------------------
class TestTypeDForwardLookingStaleness1165:
    def test_1160_max_927_pin_trips_by_design(self):
        # #1160's guard-lifecycle max-927 pin trips on the
        # 928/929/930 landings: the trip IS the landing event.
        res = _node_run(
            D1160_FILE,
            "TestGuardLifecycle1160::"
            "test_1160_file_pins_max_id_927_and_next_928")
        assert res.returncode != 0, res.stdout[-2000:]

    def test_1160_zero_928_numeric_pin_trips_by_design(self):
        # m928 landed mechanism_id: 928 in gizmodo.yaml.
        res = _node_run(
            D1160_FILE,
            "TestGuardLifecycle1160::"
            "test_zero_next_numeric_928_in_profiles")
        assert res.returncode != 0, res.stdout[-2000:]

    def test_1160_zero_928_underscore_dash_halves_stay_green(self):
        # Designed keying: no mechanism-number substring in the
        # m928/m929/m930 block keys, so the underscore/dash halves
        # stay green.
        for node in ("test_zero_next_underscore_928_repo_wide",
                     "test_zero_next_dash_928_repo_wide",
                     "test_no_thirty_sixth_direction_claim",
                     "test_no_thirty_seventh_direction_claim",
                     "test_no_thirty_eighth_direction_claim",
                     "test_no_forty_seventh_member_claim",
                     "test_no_forty_eighth_member_claim"):
            res = _node_run(
                D1160_FILE, "TestGuardLifecycle1160::" + node)
            assert res.returncode == 0, (node, res.stdout[-2000:])

    def test_1161_type_e_pins_trip_by_design(self):
        # Type E lands no mechanisms, but the #1162/#1163/#1164 A/B/C
        # legs landed 928/929/930 after #1161: its max-927 and
        # zero-928-numeric pins trip by design.
        for node in ("test_type_e_adds_no_mechanisms",
                     "test_zero_928_numeric_mechanism_id_in_profiles"):
            res = _node_run(
                E1161_FILE, "TestMechanismNovelty::" + node)
            assert res.returncode != 0, (node, res.stdout[-2000:])

    def test_1161_underscore_dash_halves_stay_green(self):
        for node in ("test_zero_928_underscore_mechanism_repo_wide",
                     "test_zero_928_dash_mechanism_repo_wide"):
            res = _node_run(
                E1161_FILE, "TestMechanismNovelty::" + node)
            assert res.returncode == 0, (node, res.stdout[-2000:])

    def test_1162_max_928_and_zero_929_numeric_trip_by_design(self):
        # m929 (journalists.yaml) and m930 (competitor-entities.yaml)
        # landed after #1162.
        for node in ("test_1162_file_pins_max_id_928_and_next_929",
                     "test_zero_next_numeric_929_in_profiles"):
            res = _node_run(
                A1162_FILE, "TestGuardLifecycle1162::" + node)
            assert res.returncode != 0, (node, res.stdout[-2000:])

    def test_1162_underscore_dash_929_and_guards_stay_green(self):
        for node in ("test_zero_next_underscore_929_repo_wide",
                     "test_zero_next_dash_929_repo_wide",
                     "test_no_thirty_sixth_direction_claim",
                     "test_no_forty_seventh_member_claim"):
            res = _node_run(
                A1162_FILE, "TestGuardLifecycle1162::" + node)
            assert res.returncode == 0, (node, res.stdout[-2000:])

    def test_1163_zero_930_numeric_guard_trips_by_design(self):
        # #1163's combined zero-930 guard trips because the numeric
        # half landed (m930 carries the colon-form 930 field in
        # competitor-entities.yaml).
        res = _node_run(
            B1163_FILE,
            "TestForwardLookingStaleness1163::"
            "test_zero_930_guards_are_forward")
        assert res.returncode != 0, res.stdout[-2000:]

    def test_1163_underscore_dash_930_halves_stay_green(self):
        # The underscore/dash halves stay green: designed keying
        # (iteration 1164 in the m930 key, no 930 substring).
        assert _git_grep_tracked(_mech_underscore(930)) == []
        assert _git_grep_tracked(_mech_dash(930)) == []

    def test_1163_flipped_pin_and_thirty_fifth_stay_green(self):
        for node in ("test_1162_zero_929_numeric_pin_flipped_by_design",
                     "test_thirty_fifth_direction_still_present"):
            res = _node_run(
                B1163_FILE, "TestForwardLookingStaleness1163::" + node)
            assert res.returncode == 0, (node, res.stdout[-2000:])

    def test_1164_zero_931_guards_stay_green(self):
        # Type D lands no mechanism: #1164's forward guards (zero
        # 931 numeric/underscore/dash) stay green.
        res = _class_run(C1164_FILE, "TestForwardLookingStaleness1164")
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1164_guard_lifecycle_stays_green(self):
        # Thirty-sixth/seventh absent, thirty-fifth/fourth present,
        # m807 taxonomy named: all hold - Type D claims nothing new.
        res = _class_run(C1164_FILE, "TestGuardLifecycle1164")
        assert res.returncode == 0, res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 10. Guard lifecycle (forward guards for #1166)
# ---------------------------------------------------------------------------
class TestGuardLifecycle1165:
    def test_1165_file_pins_max_id_930_and_next_931(self):
        assert _max_numeric_mechanism_id_in_profiles() == 930

    def test_zero_next_numeric_931_in_profiles(self):
        assert _git_grep_tracked(_mech_id_colon(NEXT_NUM), "profiles/") == []

    def test_zero_next_underscore_931_repo_wide(self):
        assert _git_grep_tracked(_mech_underscore(NEXT_NUM)) == []

    def test_zero_next_dash_931_repo_wide(self):
        assert _git_grep_tracked(_mech_dash(NEXT_NUM)) == []

    def test_no_new_mechanisms_below_max(self):
        ids = []
        for dirpath, _, files in os.walk(PROFILES_DIR):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = _read(os.path.join(dirpath, fn))
                    ids += [int(m) for m in re.findall(
                        r"mechanism_id: (\d+)", text)]
        assert 930 in ids
        assert all(i <= 930 for i in ids)

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
# 11. Background-suite verdict (#1160 suite)
# ---------------------------------------------------------------------------
class TestBackgroundSuiteVerdict1165:
    def _log_stats(self):
        text = _read(PRIOR_SUITE_LOG)
        return (os.path.getsize(PRIOR_SUITE_LOG), text.count("."),
                text.count("F"), text)

    def test_prior_suite_died_twenty_fifth_consecutive(self):
        # The #1160-launched background full suite DIED: 3863
        # bytes (3467 dots, 1 F mark, ~5% progress), last write
        # Oct 2 22:03:58 PDT, zero summary tokens (no "passed"/
        # "failed" summary, no collected-count token, no "no tests
        # ran"), no live pytest process. Per the #795 convention
        # this is recorded as DIED, not "interrupted": the run
        # produces no usable verdict.
        size, dots, fs, text = self._log_stats()
        assert size == 3863, size
        assert dots == 3467, dots
        assert fs == 1, fs
        assert "passed" not in text
        assert "failed" not in text
        assert " collected " not in text
        assert "no tests ran" not in text

    def test_no_live_pytest_process(self):
        # The bracket pattern avoids self-matching the pgrep
        # command line (phantom-pid class per AGENTS.md); the
        # returned pid is re-checked with ps because pgrep can
        # match transient parallel workers.
        result = subprocess.run(
            ["pgrep", "-f", "[p]ytest.*type_d_1160"],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            for pid in result.stdout.split():
                check = subprocess.run(
                    ["ps", "-p", pid, "-o", "args="],
                    capture_output=True, text=True)
                assert check.returncode != 0 or "type_d_1160" not in \
                    check.stdout, (
                        "a pytest process for the #1160 suite must not "
                        "still be alive when its verdict is recorded")

    def test_last_write_stale(self):
        # The prior suite's last write predates this run by hours,
        # far beyond any healthy inter-write bound.
        import time
        mtime = os.path.getmtime(PRIOR_SUITE_LOG)
        assert mtime < time.time() - 7200, mtime

    def test_tombstone_lineage_advances_to_92nd(self):
        # TWENTY-FIFTH consecutive background-suite death of the new
        # streak (the 57-run streak ENDED at #1085 when the #1080
        # suite completed). Tombstone lineage advances
        # NINETY-FIRST -> NINETY-SECOND; recorded in the #1165
        # iteration-log entry. Deselected pre-commit (log entry is
        # written in the doc-sync step per #719/#721).
        text = _read(LOG_FILE)
        assert "NINETY-SECOND" in text


# ---------------------------------------------------------------------------
# 12. Fresh synthetic engine calibration (new values, not #1160's)
# ---------------------------------------------------------------------------
class TestSyntheticEngineCalibration1165:
    # Scratch-run values produced at this run (Sat 2026-10-03 ~01:05
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
                datetime(2026, 10, 3),
                datetime(2026, 10, 3),
            )

        return calc

    def test_strong_effect_is_significant(self):
        calc = self._calculate()
        meta = [-0.66, -0.73, -0.59, -0.81, -0.64, -0.70, -0.77]
        comp = [0.18, 0.27, 0.05, 0.33, 0.12, 0.21, -0.03]
        result = calc(meta, comp)
        assert result.asymmetry_score == pytest.approx(-0.8614285714285715)
        assert result.t_statistic == pytest.approx(-15.550398609638384)
        assert result.p_value < 1e-6
        assert result.cohens_d == pytest.approx(-8.312037689290383)
        assert result.is_significant is True
        assert result.confidence_interval_lower == pytest.approx(
            -0.9571428571428572)
        assert result.confidence_interval_upper == pytest.approx(
            -0.7599642857142858)
        # The strong arm-swap negates the asymmetry exactly.
        swapped = calc(comp, meta)
        assert swapped.asymmetry_score == pytest.approx(0.8614285714285715)

    def test_near_null_pair_stays_silent(self):
        calc = self._calculate()
        meta = [0.08, -0.06, 0.04, -0.09, 0.02, -0.05, 0.07]
        comp = [-0.04, 0.06, -0.08, 0.03, -0.06, 0.09, -0.02]
        result = calc(meta, comp)
        assert result.asymmetry_score == pytest.approx(0.004285714285714287)
        assert result.p_value > 0.05
        assert result.is_significant is False

    def test_degenerate_n1_contract(self):
        # The classic degenerate guard: n=1 per arm yields t=0.0,
        # p=1.0, d=0.0 and is_significant False regardless of the
        # illustrative pair mean (here the m929 Meta-vs-Apple
        # illustrative arm pair +0.35 vs +0.10, delta +0.25).
        calc = self._calculate()
        result = calc([0.35], [0.10])
        assert result.asymmetry_score == pytest.approx(0.25)
        assert result.t_statistic == 0.0
        assert result.p_value == 1.0
        assert result.cohens_d == 0.0
        assert result.is_significant is False

    def test_engine_layer_not_finding_layer(self):
        # The m928/m929/m930 mechanisms never promote engine
        # significance to a finding: all three carry manual-only
        # discipline (m928 MANUAL ILLUSTRATIVE, m929 MANUAL
        # ILLUSTRATIVE, m930 tone NOT_SCORED / engine NOT run).
        b928 = _yaml(GIZMODO_FILE)["competitor_relationships"][
            "snap"][KEY_928]
        assert "scorer_MANUAL_ILLUSTRATIVE_ONLY" in b928
        assert "is_significant False" in b928["statistical_discipline"]
        b929 = _mark_gurman_entry()["competitor_coverage"][YAML_KEY_929]
        assert "MANUAL ILLUSTRATIVE" in b929["asymmetry_scorer"][
            "tone_basis"]
        assert b929["asymmetry_scorer"]["is_significant"] is False
        b930 = _yaml(ENTITIES_FILE)[KEY_930]
        assert b930["is_significant"] is False
        assert b930["engine_run"] is False


# ---------------------------------------------------------------------------
# 13. Suite re-launch
# ---------------------------------------------------------------------------
class TestSuiteRelaunch1165:
    def test_relaunch_log_path_written(self):
        # The re-launched full suite log exists in goal hidden_files
        # (created by this run's background launch before commit).
        assert os.path.exists(SUITE_LOG), (
            "the #1165 background suite must be re-launched to "
            + SUITE_LOG
            + " before the main commit"
        )

    def test_relaunch_log_is_full_inventory(self):
        # The re-launch runs WITHOUT -x: the full inventory
        # (calendar by-design failures included) is needed for the
        # #1170 triage. The log must hold pytest progress output,
        # not just a header.
        text = _read(SUITE_LOG)
        assert text.count(".") > 100, (
            "the re-launched suite log should accumulate dot "
            "progress; got %d dots" % text.count(".")
        )

    def test_next_type_d_run_owns_the_verdict(self):
        # Per the #795 convention, the NEXT Type D run (#1170)
        # checks this suite's verdict; this run only records the
        # launch.
        assert "type_d_1165_full_suite.log" in SUITE_LOG

# ---------------------------------------------------------------------------
# 14. Doc-sync per #719 (fails pre-commit by design; passes post-sync)
# ---------------------------------------------------------------------------
class TestTypeDDocSync1165:
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
class TestTypeDIterationLog1165:
    def _entry(self):
        return _read(LOG_FILE)

    def test_iteration_log_entry_present(self):
        assert "## #1165 Type D" in self._entry()

    def test_iteration_log_hashes_registered(self):
        text = self._entry()
        assert ANCHORED_SHA in text
        assert "1160-1164 window" in text

    def test_iteration_log_rotation_guard(self):
        text = self._entry()
        assert "FIRST leg" in text
        assert "D->E->A->B->C" in text
        assert "CLOSED the 1160-1164 window" in text

    def test_iteration_log_suite_verdict_recorded(self):
        text = self._entry()
        assert "NINETY-SECOND" in text


# ---------------------------------------------------------------------------
# 16. Literal discipline per #715/#1116 (guarded forms format-built only)
# ---------------------------------------------------------------------------
class TestLiteralDiscipline1165:
    def test_format_built_only_in_this_file(self):
        # The #1116 lesson: guarded forms must never appear
        # contiguously in test-file prose. Every guarded needle is
        # format-built at runtime.
        own = _read(__file__)
        assert "mechanism" + "_930" not in own
        assert "mechanism" + "-930" not in own
        assert "mechanism_id: " + "930" not in own
        assert "mechanism" + "_931" not in own
        assert "mechanism" + "-931" not in own
        assert "mechanism_id: " + "931" not in own
        assert "THIRTY-" + "SIXTH relationship direction" not in own
        assert "THIRTY-" + "SEVENTH relationship direction" not in own
        assert "THIRTY-" + "EIGHTH relationship direction" not in own
        assert "FORTY-" + "SEVENTH falsification-family member" not in own
        assert "FORTY-" + "EIGHTH falsification-family member" not in own

    def test_landed_claim_prose_uses_lowercase_forms(self):
        # The landed claims (forty-sixth member, thirty-fifth
        # direction) are referenced in this file's prose in
        # hyphenated/lowercase form, never as the contiguous
        # claim literals (which live only in the corpus files).
        own = _read(__file__).lower()
        assert "forty-sixth" in own
        assert "thirty-fifth" in own


# ---------------------------------------------------------------------------
# 17. In-flight isolation
# ---------------------------------------------------------------------------
class TestInflightIsolation1165:
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
