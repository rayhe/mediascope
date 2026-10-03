"""Type D -- Iteration #1160 (Fri 2026-10-02 21:00 PDT): m925/m926/m927
qualitative-discipline verification + post-1155-1159 corpus integrity
(max numeric mechanism_id 927; zero next-number nine-two-eight keys in
numeric/underscore/dash mechanism forms - the 928 needles are
format-built per #715 so no guard-literal carrier file exists; the
m925/m926/m927 block keys carry no mechanism-number substring
(designed keying), so they are plain literals; the #1155/#1156/#1157/
#1158/#1159 window files are NOT edited by this run - their now-stale
forward-looking pins are recorded as fail-by-design via subprocess in
the staleness class (#1155's max-924 + zero-925-numeric pins trip on
the 925/926/927 landings while its zero-925 underscore/dash halves
stay green; #1156's max-924 + zero-925-numeric pins trip while its
underscore/dash halves stay green; #1157's max-925 + zero-926-numeric
pins trip on the 926/927 landings; #1158's zero-927-numeric pin trips
on the 927 landing while its underscore/dash halves stay green;
#1159's zero-928 forward guards stay GREEN - Type D lands no
mechanism; #1159's supersession greens hold); ledger holds at 46 with
the FORTY-SIXTH member-claim form present in exactly one profiles
file (profiles/the-verge.yaml, m907 block, 2 occurrences - the #1127
designed pattern) and the forty-seventh member-claim form absent
repo-wide (needle format-built per #715); the THIRTY-FIFTH
relationship direction is present in competitor-entities.yaml (m915
METER-THEN-INVITE, landed at #1139) and the THIRTY-FOURTH is present
as well; the thirty-sixth AND thirty-seventh relationship-direction
claim forms are both absent repo-wide (needles format-built per
#715)) + the #1155 background-suite verdict (DIED at 1804 bytes /
1628 dots / 0 F marks, ~2% progress, with last write Oct 2 16:51:36
PDT and zero summary tokens, no live pytest process - TWENTY-THIRD
consecutive background-suite death of the new streak; the 57-run
streak ENDED at #1085 when the #1080 suite completed; tombstone
lineage advances NINETIETH -> NINETY-FIRST) + fresh synthetic engine
calibration (new values, not #1155's) + re-launch of the full suite as
a background process writing to goal hidden_files
type_d_1160_full_suite.log WITHOUT -x (the full inventory, calendar
by-design failures included, is needed for the #1165 triage; the next
Type D run checks its verdict per the #795 convention).

Type D FIRST leg of the 1160-1164 window, OPENING it
(D->E->A->B->C). Committed predecessor #1159 Type C (08:00 PM PDT Oct 2)
CLOSED the 1155-1159 window (D #1155, E #1156, A #1157, B #1158,
C #1159). Rotation per the #565 anchor + rotation guard.
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
- m925 (Type A #1157, profiles/news-corp.yaml competitor_relationships/
  openai/ 6-space block key, numeric colon-form field; block key count
  1 - colon-form line only, designed): SECOND dedicated NY Post x
  OpenAI enforcement-register mechanism and FIRST on the Post as
  story originator - Sep-30-2026 FTC sweeping-probe original (Post
  first to report per Reuters relay), regulatory-enforcement
  accountability register applied to the ~$50M/yr May-2024 OpenAI
  licensing partner with no softening visible (tone -0.40 MANUAL
  ILLUSTRATIVE); extends the m763 Sep-9-19 adversarial triad (mean
  -0.483) by 11 days; illustrative delta vs triad mean +0.083, vs
  carried Meta arm -0.50: +0.10 near-null, dual-payer tabloid symmetry
  holds. Extends the m919 news-corp disclosure_asymmetry strand
  descriptively (WSJ Oct-1 disclosed the tie inline; Post Sep-30
  shows no disclosure line in the surfaced excerpt - not observed in
  excerpt, UNVERIFIED for the full page per #492). NOT a
  falsification-family member (same-publication temporal replication
  per the #1143 precedent, not a new prediction test); ledger
  holds at 46.
- m926 (Type B #1158, journalists.yaml Ina Fried list-entry
  mechanism block, 4-space key, numeric colon-form field; block_key
  field count 1 - the YAML key differs from the block_key string by
  design): SECOND dedicated Type B mechanism on Ina Fried (Axios) -
  Sep-25-2026 "Meta needs you to believe it cares about privacy"
  privacy-claim skepticism register (virtue DOUBTED, -0.25) vs the
  carried m638 Apple ambient-AI privacy-virtue headline register
  (virtue GRANTED, +0.30); illustrative delta Meta-minus-Apple -0.55,
  the gap WIDENS from m638's +0.20 Apple-minus-Meta when the peg
  moves from launch-access to privacy-claims; temporal extension of
  m638 with carried arms un-rescored per #807. NOT a
  falsification-family member (no Axios AI-lab deal in corpus,
  gradient-absent per the #663 family); ledger holds at 46.
- m927 (Type C #1159, profiles/competitor-entities.yaml zero-indent
  top-level block key, numeric colon-form field; block key count 2 -
  colon-form line + block_key field, designed): FIRST corpus
  documentation of the Stealth Bot Prohibition Act (H.R. 9915)
  Sep-29/30-2026 publisher fly-in as the STATE's entry into the
  control-of-the-meter contest (third meter-designer alongside
  Google's payer-built widget m891 and SPUR's coalition-built
  standard m915) - mandatory bot identification with FTC + state AG
  enforcement (up to $53K per violation) that prices nothing but
  meters everything; the bill establishes no licensing price and no
  automatic payment obligation (Search Engine Watch analytical
  datum); TollBit 22B AI bot scrapes H1-2026 scale quantum; Lynch
  selective theft-register vs deal-partner inventory juxtaposition
  in one text. Money flow PROSPECTIVE, not enacted. NOT a
  falsification-family member (no coverage-tone pair scored, per
  the #609/#614 qualitative boundary); ledger holds at 46.

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
# substring (designed keying per #715). Iterations 1157/1158/1159 are
# the landing iterations, not the mechanism ids.
KEY_925 = ("nypost_ftc_probe_sweeping_openai_anthropic_super_"
           "intelligence_original_sep30_1157")
KEY_926 = ("type_b_1158_ina_fried_axios_meta_privacy_virtue_doubt_"
           "vs_apple_privacy_virtue_grant_m638_extension_sep25_"
           "oct02_7pm")
# The YAML key for the m926 block (mechanism_1158_... form) differs
# from the block_key field string by design; the block_key field
# carries the type_b_1158_... form asserted below.
YAML_KEY_926 = ("mechanism_1158_ina_fried_axios_meta_privacy_virtue_"
                "doubt_vs_apple_privacy_virtue_grant_m638_extension_"
                "sep25")
KEY_927 = ("type_c_1159_stealth_bot_act_state_meter_third_"
           "contestant_oct02_8pm")
OWN_BASENAME = ("test_type_d_1160_m925_m926_m927_qualitative_"
                "corpus_integrity_oct02_9pm.py")

# Predecessor test files for supersession pins.
D1155_FILE = ("test_type_d_1155_m922_m923_m924_qualitative_"
              "corpus_integrity_oct02_4pm.py")
E1156_FILE = ("test_type_e_1156_podcast_sentiment_"
              "154th_verification_oct02_5pm.py")
A1157_FILE = ("test_type_a_1157_nypost_ftc_probe_sweeping_openai_"
              "anthropic_original_sep30_vs_carried_meta_arms_"
              "oct02_6pm.py")
B1158_FILE = ("test_type_b_1158_ina_fried_axios_meta_privacy_virtue_"
              "doubt_vs_apple_privacy_virtue_grant_m638_extension_"
              "sep25_oct02_7pm.py")
C1159_FILE = ("test_type_c_1159_stealth_bot_act_state_meter_third_"
              "contestant_m924_extension_oct02_8pm.py")

# Prior-window background suite (verdict rendered this run) and this
# run's re-launched suite.
PRIOR_SUITE_LOG = os.path.join(
    os.path.expanduser("~"),
    "workspace",
    "goals",
    "mediascope-meta-wearables-press-analysis",
    "hidden_files",
    "type_d_1155_full_suite.log",
)
SUITE_LOG = os.path.join(
    os.path.expanduser("~"),
    "workspace",
    "goals",
    "mediascope-meta-wearables-press-analysis",
    "hidden_files",
    "type_d_1160_full_suite.log",
)

# Patched post-commit once README/ARCHITECTURE doc-sync lands (per #719).
README_TEST_COUNT = 61355  # post-doc-sync total (61254 + 101)
README_FILE_COUNT = 1485  # post-doc-sync total
TEST_BASENAME = OWN_BASENAME

# Anchor placeholder per #565: patched to the main commit's 40-char SHA in the
# anchor followup. Deselect the placeholder test in post-commit full runs.
ANCHORED_SHA = "0000000000000000000000000000000000000000"  # placeholder per #565 (patched post-commit)

MECH_NUM = 927
NEXT_NUM = 928
PREV_NUM = 926

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

# One-parse-per-file cache: the journalists/news-corp YAMLs are large
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


def _ina_fried_entry():
    # The Ina Fried journalist entry lives in the journalists.yaml
    # top-level list (unlike jessica_conditt's mapping-form entry);
    # her mechanism blocks are direct keys of the list item.
    for entry in _yaml(JOURNALISTS_FILE)["journalists"]:
        if isinstance(entry, dict) and entry.get("name") == "Ina Fried":
            return entry
    raise AssertionError("Ina Fried entry not found in journalists.yaml")


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
class TestNovelty1160:
    def test_no_type_d_1160_test_file_preexisting(self):
        hits = glob.glob(
            os.path.join(TESTS_DIR, "test_type_d_1160*.py"))
        assert hits == [os.path.join(TESTS_DIR, OWN_BASENAME)], hits

    def test_no_type_d_1160_in_git_log(self):
        # Deselected post-main-commit per #565: the main commit does
        # not exist yet pre-commit.
        log = _git("log", "--oneline", "--grep=Type D #1160")
        assert "Type D #1160" not in log, log

    def test_max_id_is_927(self):
        needle = _mech_id_colon(MECH_NUM)
        hits = _git_grep_tracked(needle, "profiles/")
        assert hits == ["profiles/competitor-entities.yaml"], hits

    def test_zero_928_numeric_forms_in_profiles(self):
        needle = _mech_id_colon(NEXT_NUM)
        assert _git_grep_tracked(needle, "profiles/") == []

    def test_block_keys_unique_in_home_yamls(self):
        assert _key_count_in_file(KEY_925, NEWS_CORP_FILE) == 1
        assert _key_count_in_file(KEY_926, JOURNALISTS_FILE) == 1
        assert _key_count_in_file(KEY_927, ENTITIES_FILE) == 2
        # Designed keying: no mechanism-number substring in any
        # block key, so they are plain literals here.
        for key, num in ((KEY_925, "925"), (KEY_926, "926"),
                         (KEY_927, "927")):
            assert num not in key, key

    def test_no_type_e_1161_in_git_log(self):
        # The next leg must not exist yet.
        log = _git("log", "--oneline", "--grep=Type E #1161")
        assert "Type E #1161" not in log, log


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------
class TestTypeDRotationGuard1160:
    def test_rotation_window_opens_1160(self):
        # 1160-1164 window: D opens, then E -> A -> B -> C.
        log = _git("log", "--oneline", "--grep=Type C #1159")
        assert "Type C #1159" in log, log
        entry = _read(LOG_FILE)
        assert "1155-1159 window" in entry
        # The "CLOSED the 1155-1159 window" predecessor line is
        # written by this run's doc-sync (TestTypeDIterationLog1160).

    def test_predecessor_1159_chain_present(self):
        log = _git("log", "--format=%H %s")
        assert "Type C #1159" in log, log
        for sha8 in ("21d1a13c", "83d09762", "a9135866"):
            assert sha8 in log, sha8

    def test_window_order_d_e_a_b_c(self):
        log = _git("log", "--oneline")
        i1155 = log.index("Type D #1155")
        i1156 = log.index("Type E #1156")
        i1157 = log.index("Type A #1157")
        i1158 = log.index("Type B #1158")
        i1159 = log.index("Type C #1159")
        # Reverse-chronological log: later commits appear first.
        assert i1159 < i1158 < i1157 < i1156 < i1155

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
        # The 1160-1164 window continues with Type E #1161 after
        # this run.
        assert "1160-1164" in (__doc__ or "")


# ---------------------------------------------------------------------------
# 3. Novelty anchor
# ---------------------------------------------------------------------------
class TestTypeDNoveltyAnchor1160:
    def _non_1160_lines(self, grep_pat):
        # --grep matches commit BODIES too: the #1159 main commit
        # body forward-references "Type D #1160" / "1160-1164"
        # ("Next window 1160-1164 opens with Type D #1160"), so a
        # bare --grep hit is not a novelty violation. Drop this
        # run's own commits (their subjects carry the bare
        # iteration number); what remains must not SUBJECT-claim
        # this run.
        log = _git("log", "--format=%H %s", "--grep=" + grep_pat)
        lines = [line for line in log.split("\n") if line.strip()]
        return [line for line in lines
                if "1160" not in line.split(" ", 1)[1]]

    def test_no_prior_type_d_1160_in_log(self):
        for line in self._non_1160_lines("Type D #1160"):
            subject = line.split(" ", 1)[1]
            assert "Type D #1160" not in subject, line

    def test_no_prior_1160_1164_window_claim(self):
        for line in self._non_1160_lines("1160-1164"):
            subject = line.split(" ", 1)[1]
            assert "1160-1164" not in subject, line


# ---------------------------------------------------------------------------
# 4. Corpus integrity
# ---------------------------------------------------------------------------
class TestTypeDCorpusIntegrity1160:
    def test_m925_block_present_in_news_corp_yaml(self):
        data = _yaml(NEWS_CORP_FILE)
        block = data["competitor_relationships"]["openai"][KEY_925]
        assert block["mechanism_id"] == 925
        assert block["iteration"] == 1157
        assert block["iteration_type"] == "A"

    def test_m926_block_present_in_journalists_yaml(self):
        block = _ina_fried_entry()[YAML_KEY_926]
        assert block["mechanism_id"] == 926
        assert block["iteration"] == 1158
        assert block["iteration_type"] == "B"

    def test_m927_block_present_in_competitor_entities_yaml(self):
        data = _yaml(ENTITIES_FILE)
        block = data[KEY_927]
        assert block["mechanism_id"] == 927
        assert block["iteration"] == 1159
        assert block["iteration_type"] == "C"

    def test_max_mechanism_id_is_927(self):
        assert _max_numeric_mechanism_id_in_profiles() == 927

    def test_zero_928_forms_repo_wide(self):
        assert _git_grep_tracked(_mech_id_colon(928)) == []
        assert _git_grep_tracked(_mech_underscore(928)) == []
        assert _git_grep_tracked(_mech_dash(928)) == []

    def test_no_new_mechanisms_below_max(self):
        ids = []
        for dirpath, _, files in os.walk(PROFILES_DIR):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = _read(os.path.join(dirpath, fn))
                    ids += [int(m) for m in re.findall(
                        r"mechanism_id: (\d+)", text)]
        assert 927 in ids
        assert all(i <= 927 for i in ids)

    def test_m925_key_count_is_designed(self):
        # Colon-form line only: the news-corp.yaml m925 block carries
        # no block_key/test_file echo fields.
        assert _key_count_in_file(KEY_925, NEWS_CORP_FILE) == 1

    def test_m926_key_count_is_designed(self):
        # The block_key field echo only: the YAML key uses the
        # mechanism_1158_... form (designed keying, iteration 1158
        # in key, no 926 substring), so the type_b_1158_... block_key
        # string appears exactly once.
        assert _key_count_in_file(KEY_926, JOURNALISTS_FILE) == 1

    def test_m927_key_count_is_designed(self):
        # Colon-form line + block_key field.
        assert _key_count_in_file(KEY_927, ENTITIES_FILE) == 2


# ---------------------------------------------------------------------------
# 5. m925 (Type A #1157) qualitative discipline
# ---------------------------------------------------------------------------
class TestTypeDM925QualitativeDiscipline1160:
    def _block(self):
        return _yaml(NEWS_CORP_FILE)["competitor_relationships"][
            "openai"][KEY_925]

    def test_m925_run_metadata(self):
        b = self._block()
        assert b["mechanism_id"] == 925
        assert b["iteration"] == 1157
        assert b["iteration_type"] == "A"
        assert b["time_pdt"] == "18:00"
        assert "New York Post" in b["publication_focus"]
        assert "OpenAI/Anthropic" in b["competitor_pair"]
        assert "Meta" in b["competitor_pair"]

    def test_m925_new_arm_register(self):
        b = self._block()
        arm = b["articles_new"][0]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.40
        assert arm["register"] == "regulatory_enforcement_accountability"
        assert "first reported" in arm["first_to_report_attestation"]
        assert "FTC opens sweeping probe" in arm["title"]

    def test_m925_carried_arms_per_807(self):
        b = self._block()
        carried = b["carried_arms_per_807"]
        assert any("m763" in c["mechanism"] for c in carried)
        assert "-0.483" in " ".join(c["arms"] for c in carried)

    def test_m925_scorer_manual_illustrative(self):
        b = self._block()
        assert "scorer_MANUAL_ILLUSTRATIVE_ONLY" in b
        scorer = b["scorer_MANUAL_ILLUSTRATIVE_ONLY"]
        assert "+0.083" in scorer
        assert "NOT_CALCULATED" in scorer
        assert "engine NOT run" in scorer
        assert "is_significant False" in scorer

    def test_m925_disclosure_observation(self):
        b = self._block()
        assert "disclosure_asymmetry" in b["disclosure_observation"]
        assert "m919" in b["disclosure_observation"]
        assert "UNVERIFIED" in b["disclosure_observation"]

    def test_m925_confounders_strong_first(self):
        b = self._block()
        confs = b["confounders_strong_first"]
        assert len(confs) == 5
        assert confs[0].startswith("STRONG")
        assert confs[1].startswith("STRONG")

    def test_m925_research_method(self):
        b = self._block()
        assert "3 browser.search query sets" in b["research_method"]
        assert "0 browser.open" in b["research_method"]

    def test_m925_statistical_discipline(self):
        b = self._block()
        sd = b["statistical_discipline"]
        assert "MANUAL/QUALITATIVE ONLY" in sd
        assert "is_significant False" in sd
        assert "engine NOT run" in sd
        assert "directionally_supported_not_proven" in sd
        assert "NOT artifact-grade" in sd

    def test_m925_not_falsification_member(self):
        b = self._block()
        assert "NOT a member" in b["falsification_family"]
        assert "Ledger holds at 46" in b["falsification_family"]
        assert "Ledger holds at 46" in b["incentive_attribution"]


# ---------------------------------------------------------------------------
# 6. m926 (Type B #1158) qualitative discipline
# ---------------------------------------------------------------------------
class TestTypeDM926QualitativeDiscipline1160:
    def _block(self):
        return _ina_fried_entry()[YAML_KEY_926]

    def test_m926_run_metadata(self):
        b = self._block()
        assert b["mechanism_id"] == 926
        assert b["iteration"] == 1158
        assert b["iteration_type"] == "B"
        assert b["iteration_time"] == "2026-10-02 19:00 PDT"
        assert b["journalist"] == "Ina Fried"
        assert b["publication"] == "axios"

    def test_m926_pattern_privacy_virtue_inversion(self):
        b = self._block()
        assert "privacy" in b["pattern"].lower()
        assert "DOUBTED" in b["pattern"]
        assert "GRANTED" in b["pattern"]
        assert "m638" in b["pattern"]

    def test_m926_new_meta_arm(self):
        b = self._block()
        arm = b["new_meta_privacy_arm"]
        assert arm["tone_illustrative"] == -0.25
        assert arm["register"] == "privacy_claim_skepticism_accountability"
        assert "Meta needs you to believe it cares about privacy" in str(
            arm["evidence_quotes"])

    def test_m926_carried_apple_arm(self):
        b = self._block()
        arm = b["carried_apple_arm"]
        assert arm["tone_illustrative"] == 0.30
        assert arm["register"] == "privacy_virtue_headline"
        assert "#807" in arm["note"]

    def test_m926_scorer_delta(self):
        b = self._block()
        scorer = b["asymmetry_scorer"]
        assert scorer["new_meta_tone"] == -0.25
        assert scorer["carried_apple_tone"] == 0.30
        assert scorer["illustrative_delta_meta_minus_apple"] == -0.55
        assert scorer["p_value"] == "NOT_CALCULATED"
        assert scorer["is_significant"] is False
        assert "MANUAL ILLUSTRATIVE" in scorer["tone_basis"]

    def test_m926_confounders_ranked_strong_first(self):
        b = self._block()
        strong = b["confounders_ranked"]["strong"]
        assert len(strong) == 3
        assert "peg" in strong[0].lower() or "News-peg" in strong[0]

    def test_m926_research_method(self):
        b = self._block()
        assert "7 browser.search query sets" in b["research_method"]
        assert "1 browser.open" in b["research_method"]
        assert "axios.com" in b["research_method"]
        assert "policy-blocked" in b["research_method"]

    def test_m926_not_falsification_member(self):
        b = self._block()
        assert "NOT a falsification-family member" in b[
            "falsification_family"]
        assert "Ledger holds at 46" in b["falsification_family"]


# ---------------------------------------------------------------------------
# 7. m927 (Type C #1159) qualitative discipline
# ---------------------------------------------------------------------------
class TestTypeDM927QualitativeDiscipline1160:
    def _block(self):
        return _yaml(ENTITIES_FILE)[KEY_927]

    def test_m927_run_metadata(self):
        b = self._block()
        assert b["mechanism_id"] == 927
        assert b["iteration"] == 1159
        assert b["iteration_type"] == "C"
        assert b["iteration_time"] == "2026-10-02 20:00 PDT"
        assert b["type"] == "financial_incentive_mapping"

    def test_m927_finding_five_legs(self):
        b = self._block()
        assert "Five Sep-29-Oct-1-2026 legs" in b["finding"]
        assert "Stealth Bot Prohibition Act" in b["finding"]
        assert "third meter-designer" in b["mechanism_name"]

    def test_m927_money_flow_prospective(self):
        b = self._block()
        assert "PROSPECTIVE, not enacted" in b["money_flow"]
        assert "NO price" in b["money_flow"]

    def test_m927_connects_to(self):
        b = self._block()
        assert b["connects_to"] == [891, 909, 915, 921, 924]

    def test_m927_sources_five_novel(self):
        b = self._block()
        assert len(b["sources"]) == 5
        assert all(s["novel"] is True for s in b["sources"])
        assert any("digiday.com" in s["url"] for s in b["sources"])
        assert any("22" in s["what"] or "22B" in s["what"]
                   for s in b["sources"])

    def test_m927_confounders_strong_first(self):
        b = self._block()
        confs = b["confounders"]
        assert len(confs) == 5
        assert confs[0]["strength"] == "STRONG"
        assert confs[1]["strength"] == "STRONG"
        assert "unenacted" in confs[0]["text"].lower()

    def test_m927_statistical_discipline(self):
        b = self._block()
        assert b["tone_scored"] is False
        assert b["engine_run"] is False
        assert b["is_significant"] is False
        assert b["verdict"] == "directionally_supported_not_proven"
        assert b["no_analysis_json_update"] is True
        assert b["artifact_grade"] is False

    def test_m927_not_falsification_member(self):
        b = self._block()
        assert b["falsification_family_member"] is False
        assert "ledger holds at 46" in b["falsification_family"].lower()
        assert "thirty-sixth" in b["falsification_family"]


# ---------------------------------------------------------------------------
# 8. Falsification ledger
# ---------------------------------------------------------------------------
class TestTypeDFalsificationLedger1160:
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

    def test_m925_m926_m927_not_members_ledger_holds(self):
        b925 = _yaml(NEWS_CORP_FILE)["competitor_relationships"][
            "openai"][KEY_925]
        assert "NOT a member" in b925["falsification_family"]
        b926 = _ina_fried_entry()[YAML_KEY_926]
        assert "NOT a falsification-family member" in b926[
            "falsification_family"]
        b927 = _yaml(ENTITIES_FILE)[KEY_927]
        assert b927["falsification_family_member"] is False
        for text in (b925["falsification_family"],
                     b926["falsification_family"],
                     b927["falsification_family"]):
            assert "ledger holds at 46" in text.lower(), text


# ---------------------------------------------------------------------------
# 9. Forward-looking staleness (predecessor pin lifecycle via subprocess)
# ---------------------------------------------------------------------------
class TestTypeDForwardLookingStaleness1160:
    def test_1155_max_924_pin_trips_by_design(self):
        # #1155's guard-lifecycle max-924 pin trips on the
        # 925/926/927 landings: the trip IS the landing event.
        res = _node_run(
            D1155_FILE,
            "TestGuardLifecycle1155::"
            "test_1155_file_pins_max_id_924_and_next_925")
        assert res.returncode != 0, res.stdout[-2000:]

    def test_1155_zero_925_numeric_pin_trips_by_design(self):
        # m925 landed mechanism_id: 925 in news-corp.yaml.
        res = _node_run(
            D1155_FILE,
            "TestGuardLifecycle1155::"
            "test_zero_next_numeric_925_in_profiles")
        assert res.returncode != 0, res.stdout[-2000:]

    def test_1155_zero_925_underscore_dash_halves_stay_green(self):
        # Designed keying: no mechanism-number substring in the
        # m925/m926/m927 block keys, so the underscore/dash halves
        # stay green.
        for node in ("test_zero_next_underscore_925_repo_wide",
                     "test_zero_next_dash_925_repo_wide",
                     "test_no_thirty_sixth_direction_claim",
                     "test_no_thirty_seventh_direction_claim",
                     "test_no_thirty_eighth_direction_claim",
                     "test_no_forty_seventh_member_claim",
                     "test_no_forty_eighth_member_claim"):
            res = _node_run(
                D1155_FILE, "TestGuardLifecycle1155::" + node)
            assert res.returncode == 0, (node, res.stdout[-2000:])

    def test_1156_type_e_pins_trip_by_design(self):
        # Type E lands no mechanisms, but the #1157/#1158/#1159 A/B/C
        # legs landed 925/926/927 after #1156: its max-924 and
        # zero-925-numeric pins trip by design.
        for node in ("test_type_e_adds_no_mechanisms",
                     "test_zero_925_numeric_mechanism_id_in_profiles"):
            res = _node_run(
                E1156_FILE, "TestMechanismNovelty::" + node)
            assert res.returncode != 0, (node, res.stdout[-2000:])

    def test_1156_underscore_dash_halves_stay_green(self):
        for node in ("test_zero_925_underscore_mechanism_repo_wide",
                     "test_zero_925_dash_mechanism_repo_wide"):
            res = _node_run(
                E1156_FILE, "TestMechanismNovelty::" + node)
            assert res.returncode == 0, (node, res.stdout[-2000:])

    def test_1157_max_925_and_zero_926_numeric_trip_by_design(self):
        # m926 (journalists.yaml) and m927 (competitor-entities.yaml)
        # landed after #1157.
        for node in ("test_1157_file_pins_max_id_925_and_next_926",
                     "test_zero_next_numeric_926_in_profiles"):
            res = _node_run(
                A1157_FILE, "TestGuardLifecycle1157::" + node)
            assert res.returncode != 0, (node, res.stdout[-2000:])

    def test_1157_underscore_dash_926_and_guards_stay_green(self):
        for node in ("test_zero_next_underscore_926_repo_wide",
                     "test_zero_next_dash_926_repo_wide",
                     "test_no_thirty_sixth_direction_claim",
                     "test_no_forty_seventh_member_claim"):
            res = _node_run(
                A1157_FILE, "TestGuardLifecycle1157::" + node)
            assert res.returncode == 0, (node, res.stdout[-2000:])

    def test_1158_zero_927_numeric_pin_trips_by_design(self):
        # #1158's combined zero-927 guard trips because the numeric
        # half landed (m927 carries the colon-form 927 field in
        # competitor-entities.yaml).
        res = _node_run(
            B1158_FILE,
            "TestForwardLookingStaleness1158::"
            "test_zero_927_guards_are_forward")
        assert res.returncode != 0, res.stdout[-2000:]

    def test_1158_underscore_dash_927_halves_stay_green(self):
        # The underscore/dash halves stay green: designed keying
        # (iteration 1159 in the m927 key, no 927 substring).
        assert _git_grep_tracked(_mech_underscore(927)) == []
        assert _git_grep_tracked(_mech_dash(927)) == []

    def test_1158_flipped_pin_and_thirty_fifth_stay_green(self):
        for node in ("test_1157_zero_926_numeric_pin_flipped_by_design",
                     "test_thirty_fifth_direction_still_present"):
            res = _node_run(
                B1158_FILE, "TestForwardLookingStaleness1158::" + node)
            assert res.returncode == 0, (node, res.stdout[-2000:])

    def test_1159_zero_928_guards_stay_green(self):
        # Type D lands no mechanism: #1159's forward guards (zero
        # 928 numeric/underscore/dash) stay green.
        res = _class_run(C1159_FILE, "TestForwardLookingStaleness1159")
        assert res.returncode == 0, res.stdout[-2000:]

    def test_1159_guard_lifecycle_stays_green(self):
        # Thirty-sixth/seventh absent, thirty-fifth/fourth present,
        # m807 taxonomy named: all hold - Type D claims nothing new.
        res = _class_run(C1159_FILE, "TestGuardLifecycle1159")
        assert res.returncode == 0, res.stdout[-2000:]


# ---------------------------------------------------------------------------
# 10. Guard lifecycle (forward guards for #1161)
# ---------------------------------------------------------------------------
class TestGuardLifecycle1160:
    def test_1160_file_pins_max_id_927_and_next_928(self):
        assert _max_numeric_mechanism_id_in_profiles() == 927

    def test_zero_next_numeric_928_in_profiles(self):
        assert _git_grep_tracked(_mech_id_colon(NEXT_NUM), "profiles/") == []

    def test_zero_next_underscore_928_repo_wide(self):
        assert _git_grep_tracked(_mech_underscore(NEXT_NUM)) == []

    def test_zero_next_dash_928_repo_wide(self):
        assert _git_grep_tracked(_mech_dash(NEXT_NUM)) == []

    def test_no_new_mechanisms_below_max(self):
        ids = []
        for dirpath, _, files in os.walk(PROFILES_DIR):
            for fn in files:
                if fn.endswith(".yaml"):
                    text = _read(os.path.join(dirpath, fn))
                    ids += [int(m) for m in re.findall(
                        r"mechanism_id: (\d+)", text)]
        assert 927 in ids
        assert all(i <= 927 for i in ids)

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
# 11. Background-suite verdict (#1155 suite)
# ---------------------------------------------------------------------------
class TestBackgroundSuiteVerdict1160:
    def _log_stats(self):
        text = _read(PRIOR_SUITE_LOG)
        return (os.path.getsize(PRIOR_SUITE_LOG), text.count("."),
                text.count("F"), text)

    def test_prior_suite_died_twenty_third_consecutive(self):
        # The #1155-launched background full suite DIED: 1804
        # bytes (1628 dots, 0 F marks, ~2% progress), last write
        # Oct 2 16:51:36 PDT, zero summary tokens (no "passed"/
        # "failed" summary, no collected-count token, no "no tests
        # ran"), no live pytest process. Per the #795 convention
        # this is recorded as DIED, not "interrupted": the run
        # produces no usable verdict.
        size, dots, fs, text = self._log_stats()
        assert size == 1804, size
        assert dots == 1628, dots
        assert fs == 0, fs
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
            ["pgrep", "-f", "[p]ytest.*type_d_1155"],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            for pid in result.stdout.split():
                check = subprocess.run(
                    ["ps", "-p", pid, "-o", "args="],
                    capture_output=True, text=True)
                assert check.returncode != 0 or "type_d_1155" not in \
                    check.stdout, (
                        "a pytest process for the #1155 suite must not "
                        "still be alive when its verdict is recorded")

    def test_last_write_stale(self):
        # The prior suite's last write predates this run by hours,
        # far beyond any healthy inter-write bound.
        import time
        mtime = os.path.getmtime(PRIOR_SUITE_LOG)
        assert mtime < time.time() - 7200, mtime

    def test_tombstone_lineage_advances_to_91st(self):
        # TWENTY-THIRD consecutive background-suite death of the new
        # streak (the 57-run streak ENDED at #1085 when the #1080
        # suite completed). Tombstone lineage advances
        # NINETIETH -> NINETY-FIRST; recorded in the #1160
        # iteration-log entry. Deselected pre-commit (log entry is
        # written in the doc-sync step per #719/#721).
        text = _read(LOG_FILE)
        assert "NINETY-FIRST" in text


# ---------------------------------------------------------------------------
# 12. Fresh synthetic engine calibration (new values, not #1155's)
# ---------------------------------------------------------------------------
class TestSyntheticEngineCalibration1160:
    # Scratch-run values produced at this run (Fri 2026-10-02 ~21:05
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
        meta = [-0.71, -0.62, -0.80, -0.55, -0.69, -0.58, -0.74]
        comp = [0.22, 0.09, 0.31, -0.01, 0.17, 0.11, -0.06]
        result = calc(meta, comp)
        assert result.asymmetry_score == pytest.approx(-0.7885714285714285)
        assert result.t_statistic == pytest.approx(-13.298309581480586)
        assert result.p_value < 1e-6
        assert result.cohens_d == pytest.approx(-7.108245468164788)
        assert result.is_significant is True
        assert result.confidence_interval_lower == pytest.approx(
            -0.8914285714285713)
        assert result.confidence_interval_upper == pytest.approx(
            -0.6814285714285715)
        # The strong arm-swap negates the asymmetry exactly.
        swapped = calc(comp, meta)
        assert swapped.asymmetry_score == pytest.approx(0.7885714285714285)

    def test_near_null_pair_stays_silent(self):
        calc = self._calculate()
        meta = [0.05, -0.04, 0.07, -0.02, 0.03, -0.01, 0.06]
        comp = [-0.02, 0.05, -0.03, 0.06, -0.05, 0.02, -0.03]
        result = calc(meta, comp)
        assert result.asymmetry_score == pytest.approx(0.02)
        assert result.p_value > 0.05
        assert result.is_significant is False

    def test_degenerate_n1_contract(self):
        # The classic degenerate guard: n=1 per arm yields t=0.0,
        # p=1.0, d=0.0 and is_significant False regardless of the
        # illustrative pair mean (here the m926 Meta-vs-Apple
        # illustrative arm pair -0.25 vs 0.30, delta -0.55).
        calc = self._calculate()
        result = calc([-0.25], [0.30])
        assert result.asymmetry_score == pytest.approx(-0.55)
        assert result.t_statistic == 0.0
        assert result.p_value == 1.0
        assert result.cohens_d == 0.0
        assert result.is_significant is False

    def test_engine_layer_not_finding_layer(self):
        # The m925/m926/m927 mechanisms never promote engine
        # significance to a finding: all three carry manual-only
        # discipline (m925 MANUAL ILLUSTRATIVE, m926 MANUAL
        # ILLUSTRATIVE, m927 tone NOT_SCORED / engine NOT run).
        b925 = _yaml(NEWS_CORP_FILE)["competitor_relationships"][
            "openai"][KEY_925]
        assert "scorer_MANUAL_ILLUSTRATIVE_ONLY" in b925
        assert "is_significant False" in b925["statistical_discipline"]
        b926 = _ina_fried_entry()[YAML_KEY_926]
        assert "MANUAL ILLUSTRATIVE" in b926["asymmetry_scorer"][
            "tone_basis"]
        assert b926["asymmetry_scorer"]["is_significant"] is False
        b927 = _yaml(ENTITIES_FILE)[KEY_927]
        assert b927["is_significant"] is False
        assert b927["engine_run"] is False


# ---------------------------------------------------------------------------
# 13. Suite re-launch
# ---------------------------------------------------------------------------
class TestSuiteRelaunch1160:
    def test_relaunch_log_path_written(self):
        # The re-launched full suite log exists in goal hidden_files
        # (created by this run's background launch before commit).
        assert os.path.exists(SUITE_LOG), (
            "the #1160 background suite must be re-launched to "
            + SUITE_LOG
            + " before the main commit"
        )

    def test_relaunch_log_is_full_inventory(self):
        # The re-launch runs WITHOUT -x: the full inventory
        # (calendar by-design failures included) is needed for the
        # #1165 triage. The log must hold pytest progress output,
        # not just a header.
        text = _read(SUITE_LOG)
        assert text.count(".") > 100, (
            "the re-launched suite log should accumulate dot "
            "progress; got %d dots" % text.count(".")
        )

    def test_next_type_d_run_owns_the_verdict(self):
        # Per the #795 convention, the NEXT Type D run (#1165)
        # checks this suite's verdict; this run only records the
        # launch.
        assert "type_d_1160_full_suite.log" in SUITE_LOG


# ---------------------------------------------------------------------------
# 14. Doc-sync per #719 (fails pre-commit by design; passes post-sync)
# ---------------------------------------------------------------------------
class TestTypeDDocSync1160:
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
class TestTypeDIterationLog1160:
    def _entry(self):
        return _read(LOG_FILE)

    def test_iteration_log_entry_present(self):
        assert "## #1160 Type D" in self._entry()

    def test_iteration_log_hashes_registered(self):
        text = self._entry()
        assert ANCHORED_SHA in text
        assert "1155-1159 window" in text

    def test_iteration_log_rotation_guard(self):
        text = self._entry()
        assert "FIRST leg" in text
        assert "D->E->A->B->C" in text
        assert "CLOSED the 1155-1159 window" in text

    def test_iteration_log_suite_verdict_recorded(self):
        text = self._entry()
        assert "NINETY-FIRST" in text


# ---------------------------------------------------------------------------
# 16. Literal discipline per #715/#1116 (guarded forms format-built only)
# ---------------------------------------------------------------------------
class TestLiteralDiscipline1160:
    def test_format_built_only_in_this_file(self):
        # The #1116 lesson: guarded forms must never appear
        # contiguously in test-file prose. Every guarded needle is
        # format-built at runtime.
        own = _read(__file__)
        assert "mechanism" + "_927" not in own
        assert "mechanism" + "-927" not in own
        assert "mechanism_id: " + "927" not in own
        assert "mechanism" + "_928" not in own
        assert "mechanism" + "-928" not in own
        assert "mechanism_id: " + "928" not in own
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
class TestInflightIsolation1160:
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
