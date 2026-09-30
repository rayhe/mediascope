"""Type D -- Iteration #1100 (Wed 2026-09-30 13:00 PDT): m889/m890/m891
qualitative-discipline verification + post-1095-1099 corpus integrity
(max numeric mechanism_id 891; zero next-number 892 keys in
numeric/underscore/dash mechanism forms; underscore/dash 892 needles
are format-built per #715 so no guard-literal carrier file exists -
the repo-wide 892 sweep is pure zero on source files (the local
tests/__pycache__ .pyc artifacts carry concatenated needle strings
from their own guards; untracked build artifacts, excluded per the
#715 pattern-rescope lesson); the m889/m890/m891 block keys are
fragment-built in this file (no contiguous landed-window
mechanism-key literals, per the #1091 carrier-sweep
precedent); the #1095 Type D file gets its historical repin (MAX_ID
888->891, NEXT_NUM 889->892, rotation guard rewritten to the
1095-1099 window-closed-complete subsequence form,
no-Type-E-1096 inverted to Type-C-1099-landed def43924, entry
newest-first -> entry-present, anchor mechanics untouched); the
#1096/#1097/#1098 window files are NOT edited by this run -
their now-stale forward-looking numeric guards are pinned as
fail-by-design via subprocess in the staleness class; ledger holds at
37 with the THIRTY-SEVENTH member-claim form present once
(the-verge.yaml m880 falsification_family) and the THIRTY-EIGHTH
member-claim form absent in profiles/ (the THIRTY-EIGHTH hits
are negative-guard notes, designed); TWENTY-SIXTH relationship
direction present in competitor-entities.yaml (m888
relationship_direction_taxonomy); TWENTY-SEVENTH relationship
direction present in competitor-entities.yaml (m891 UNILATERAL
PRICING)) + the #1095 background-suite verdict (DIED at 3237 bytes /
~5% dots with last write Sep 30 08:59:54 PDT and zero summary
tokens, no live pytest process - THIRD consecutive
background-suite death of the new streak; the 57-run streak ENDED at
#1085 when the #1080 suite completed; tombstone lineage advances
SEVENTY-EIGHTH -> SEVENTY-NINTH) + fresh synthetic engine
calibration (new values, not #1095's) + re-launch of the full suite
as a background process writing to goal hidden_files
type_d_1100_full_suite.log WITHOUT -x (the full inventory, calendar
by-design failures included, is needed for the #1105 triage; the next
Type D run checks its verdict per the #795 convention).

Type D FIRST leg of the 1100-1104 window, OPENING it
(D->E->A->B->C). Committed predecessor #1099 Type C (12:00 PDT Sep
30) CLOSED the 1095-1099 window (D #1095, E #1096, A #1097, B #1098,
C #1099). Rotation per the #565 anchor + rotation guard.
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
- m889 (Type A #1097, wired.yaml 4-space block key,
  `mechanism_id: 889` field form; block key count 1 - colon-form
  line only, designed): WIRED x OpenAI Sep-2026 slowdown-legality
  register extension, m877-family (safety-crisis register ->
  coordination/antitrust register). Sep 10 Maxwell Zeff exclusive
  "OpenAI wants to know if an AI industry slowdown would even be
  legal" (MANUAL ILLUSTRATIVE -0.35, inquisitive accountability on
  a leak-driven peg) vs Sep 29 Reece Rogers Dots product relay
  (0.00, neutral). Carried WIRED x Meta arms from m877
  (un-rescored per #807): Pinky Promises skepticism (-0.45),
  NameTag class-action adversarial-legal (-0.30). MANUAL
  ILLUSTRATIVE OpenAI mean -0.175 vs Meta mean -0.375, delta +0.20
  (Meta draws the harder register; thesis-consistent directionally
  but small). Zeff-only read: -0.35 vs -0.375 = +0.025, near-null
  parity on the leak-driven accountability peg, extending the m877
  peg-not-entity finding. NOT a falsification-family member.
- m890 (Type B #1098, journalists.yaml 4-space block key under
  reece_rogers competitor_coverage, `mechanism_id: 890` field
  form): Reece Rogers (WIRED) Sep-2026 Muse weeklong-test
  data-collection-alarm register (-0.50 MANUAL ILLUSTRATIVE,
  excerpt-tier) vs carried Jul-7-2026 Claude Cowork playful
  register (+0.10 per #807). Illustrative delta (Anthropic minus
  Meta) +0.60, thesis-consistent (m629 same-day +0.55 holds on the
  new peg: the register gradient is peg-extensible, not a one-day
  artifact). TEMPORAL EXTENSION of m629 (Type B #658) into the
  Muse-agent peg 75 days later. NOT a falsification-family
  member.
- m891 (Type C #1099, competitor-entities.yaml zero-indent block
  key, `mechanism_id: 891` field form): Google AI-contribution
  pilot rate disclosure (The Information Sep 29 2026, relayed Sep
  30) - first disclosed payment rates (around 100 publishers;
  under $1,000 over months to over $1M/yr; under 0.1% of ad
  revenue for small-to-midsize); UNILATERAL PRICING as the
  TWENTY-SEVENTH relationship direction (m891): payer-set
  micro-compensation decoupled from consent (opt-out of payment
  does not opt out of use). Tone NOT_SCORED. NOT a
  falsification-family member.

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

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
LOG_PATH = os.path.join(REPO_ROOT, "iteration-log.md")
OWN_BASENAME = (
    "test_type_d_1100_m889_m890_m891_qualitative_corpus_"
    "integrity_sep30_1pm.py"
)

MAX_ID = 891
NEXT_NUM = 892

# Patched by the anchor followup commit per #565 (post-main-commit).
ANCHORED_SHA = "0" * 40

# Doc-sync constants per #719 (patched post-first-run with the true
# collected count).
README_TEST_COUNT = 55971
README_FILE_COUNT = 1425

# Format-built per the #715 convention: this source file carries no
# contiguous underscore-form mechanism key literal for the landed
# window mechanisms (889/890/891) or the next number (892).
M889_KEY = (
    "mechanism_%d_wired_openai_slowdown_legality_register_"
    "vs_meta_carried_arms_sep30" % 889
)
M889_INDENT = 4
M889_HOME = "profiles/wired.yaml"
M890_KEY = (
    "type_b_1098_reece_rogers_wired_muse_weeklong_data_collection_"
    "alarm_vs_carried_claude_cowork_playful_m629_temporal_"
    "extension_sep30"
)
M890_INDENT = 4
M890_HOME = "profiles/careers/journalists.yaml"
M891_KEY = (
    "type_c_1099_google_ai_contribution_pilot_rate_disclosure_"
    "unilateral_pricing_twentyseventh_direction_sep30_12pm"
)
M891_INDENT = 0
M891_HOME = "profiles/competitor-entities.yaml"

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1100_full_suite.log"
)
PRIOR_SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1095_full_suite.log"
)
D1095_FILE = (
    "tests/test_type_d_1095_m886_m887_m888_qualitative_corpus_"
    "integrity_sep30_8am.py"
)
B1098_FILE = (
    "tests/test_type_b_1098_reece_rogers_wired_muse_weeklong_data_"
    "alarm_vs_claude_cowork_m629_temporal_extension_sep30_11am.py"
)
C1099_FILE = (
    "tests/test_type_c_1099_google_ai_contribution_pilot_rate_"
    "disclosure_unilateral_pricing_twentyseventh_direction_"
    "sep30_12pm.py"
)

_DOC = __doc__

# The twenty-seventh-direction needle is fragment-built per #715 so
# this file carries no contiguous literal.
_TW27 = "TWENTY-" + "SEVENTH relationship direction"


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def _indented_block(rel_path, key, indent):
    lines = _read(os.path.join(REPO_ROOT, rel_path)).splitlines(keepends=True)
    start = None
    for i, line in enumerate(lines):
        if (
            len(line) - len(line.lstrip(" "))
            == indent
            and line.strip() == key + ":"
        ):
            start = i
            break
    assert start is not None, "block key %r not found at indent %d" % (
        key,
        indent,
    )
    out = [lines[start]]
    for line in lines[start + 1 :]:
        if not line.strip():
            out.append(line)
            continue
        line_indent = len(line) - len(line.lstrip(" "))
        if line_indent <= indent:
            break
        out.append(line)
    return "".join(out)


def _block_data(rel, key, indent):
    import yaml

    return yaml.safe_load(_indented_block(rel, key, indent))[key]


def _git(*args):
    result = subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )
    assert result.returncode == 0, result.stderr[-1000:]
    return result.stdout


def _window(n=40):
    # First occurrence of each distinct iteration number, newest first.
    subjects = _git("log", f"-{n}", "--format=%s", "--no-merges").splitlines()
    seen_nums = set()
    out = []
    for s in subjects:
        m = re.match(r"^Type ([A-E]) #(\d+)", s)
        if m and m.group(2) not in seen_nums:
            seen_nums.add(m.group(2))
            out.append(m.groups())
    return out[:5]


# At this run's anchor followup, the newest distinct iteration
# numbers in git history: #1100 Type D opens the 1100-1104 window;
# #1099 Type C (committed 12:00 PDT Sep 30) is the schedule
# predecessor and CLOSED the 1095-1099 window. The in-flight runs
# (#899 Type C, #938 Type B, #900 Type D, #1012 working-tree edit)
# have no main commits in git history at this run's checks and sit
# below the window.


def _iter_source_files():
    """Yield paths for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson: local test
    pyc files carry next-number needle strings from their own
    guards; compiled artifacts are excluded from the sweeps). No
    additional sweep-carrier exclusions this run: no in-tree SOURCE
    file carries a contiguous 892-form mechanism literal (verified
    pre-commit), so the 892 sweeps run repo-wide with only this file
    excluded.
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
            if f.endswith(".py"):
                yield os.path.join(root, f)


def _repo_grep_underscore_mechanism(n):
    """Return file paths containing the underscore-form mechanism key.

    The needle is built at runtime by format string, so this source
    file carries no contiguous underscore-form literal (per the #770
    lesson).
    """
    needle = "%s%d" % (MECH_ID_MARKER, n)
    return [
        p
        for p in _iter_source_files()
        if needle in open(p, encoding="utf-8", errors="replace").read()
    ]


def _repo_grep_dash_mechanism(n):
    needle = "mechanism" + "-" + str(n)
    return [
        p
        for p in _iter_source_files()
        if needle in open(p, encoding="utf-8", errors="replace").read()
    ]


def _repo_grep_numeric_mechanism_id(n):
    needle = "mechanism_id: %d" % n
    hits = []
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            p = os.path.join(root, f)
            if needle in open(p, encoding="utf-8", errors="replace").read():
                hits.append(p)
    return hits


def _max_numeric_mechanism_id():
    pat = re.compile(r"mechanism_id:\s*(\d+)")
    ids = set()
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            ids.update(
                int(x)
                for x in pat.findall(
                    open(
                        os.path.join(root, f), encoding="utf-8", errors="replace"
                    ).read()
                )
            )
    return max(ids)


def _m889_data():
    return _block_data(M889_HOME, M889_KEY, M889_INDENT)


def _m890_data():
    return _block_data(M890_HOME, M890_KEY, M890_INDENT)


def _m891_data():
    return _block_data(M891_HOME, M891_KEY, M891_INDENT)


# ---------------------------------------------------------------------------
# 1. Novelty
# ---------------------------------------------------------------------------
class TestNovelty1100:
    def test_no_type_d_1100_test_file_preexisting(self):
        assert glob.glob(os.path.join(TESTS_DIR, "test_type_d_1100*.py")) == [
            os.path.join(TESTS_DIR, OWN_BASENAME)
        ], "only this file may match the test_type_d_1100 glob"

    def test_no_type_d_1100_in_git_log(self):
        # Pre-commit novelty: no Type D #1100 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #1100"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #1100" in line
            and "followup" not in line.lower()
            and "push-status" not in line.lower()
            and "log-hash" not in line.lower()
        ]
        if ANCHORED_SHA == "0" * 40:
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_max_id_is_891(self):
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_892_numeric_forms_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_block_keys_unique_in_home_yamls(self):
        # m889: descriptive block key at 4-space indent in wired.yaml,
        # exactly one colon-form occurrence (no block_key: repeat for
        # m889, designed).
        assert (
            _read(os.path.join(REPO_ROOT, M889_HOME)).count(
                "\n" + " " * M889_INDENT + M889_KEY + ":"
            )
            == 1
        )
        # m890: block key at 4-space indent under reece_rogers'
        # competitor_coverage in journalists.yaml.
        assert (
            _read(os.path.join(REPO_ROOT, M890_HOME)).count(
                "\n" + " " * M890_INDENT + M890_KEY + ":"
            )
            == 1
        )
        # m891: block key at zero indent in competitor-entities.yaml.
        assert (
            _read(os.path.join(REPO_ROOT, M891_HOME)).count("\n" + M891_KEY + ":")
            == 1
        )

    def test_m889_key_count_is_designed(self):
        # The m889 key appears once in wired.yaml: the colon-form
        # block-key line only (no block_key: field - designed, not a
        # corpus duplicate).
        assert _read(os.path.join(REPO_ROOT, M889_HOME)).count(M889_KEY) == 1

    def test_m890_key_count_is_designed(self):
        # The m890 key appears twice in journalists.yaml: the
        # colon-form block-key line and the block_key: field
        # (no test_file: substring in the m890 block - designed,
        # not a corpus duplicate).
        text = _read(os.path.join(REPO_ROOT, M890_HOME))
        assert text.count("\n" + " " * M890_INDENT + M890_KEY + ":") == 1
        assert text.count("block_key: " + M890_KEY) == 1
        assert text.count(M890_KEY) == 2

    def test_m891_key_count_is_designed(self):
        # The m891 block carries its block_key: field repeating the
        # key (designed keying per #1064/#1069): exactly 2
        # occurrences in competitor-entities.yaml.
        text = _read(os.path.join(REPO_ROOT, M891_HOME))
        assert text.count("\n" + M891_KEY + ":") == 1
        assert text.count("block_key: " + M891_KEY) == 1
        assert text.count(M891_KEY) == 2


# ---------------------------------------------------------------------------
# 2. Rotation guard per #565
# ---------------------------------------------------------------------------
class TestTypeDRotationGuard1100:
    def test_rotation_window_opens_1100(self):
        # The newest distinct iteration in git history is this run's
        # #1100 Type D (window opener). The full 1095-1099 window is
        # regex-visible (no subject deviations in this window): D
        # #1100 -> C #1099 -> B #1098 -> A #1097 -> E #1096.
        # Deselected pre-commit per #565 (passes post-commit).
        window = _window()
        assert window[0] == ("D", "1100"), window
        assert window[1:5] == [
            ("C", "1099"),
            ("B", "1098"),
            ("A", "1097"),
            ("E", "1096"),
        ], window

    def test_predecessor_1099_chain_present(self):
        # The full #1099 Type C commit chain must be in git history
        # before this run's main commit (rotation transparency per
        # #565): main def43924, anchor 4eff5d5b, log-hash 81e9ff60,
        # log-hash followup e674c7a1, test-fix 28802355, push-status
        # 814fee1b.
        for sha in (
            "def43924",
            "4eff5d5b",
            "81e9ff60",
            "e674c7a1",
            "28802355",
            "814fee1b",
        ):
            assert (
                subprocess.run(
                    ["git", "cat-file", "-e", sha],
                    cwd=REPO_ROOT,
                    capture_output=True,
                ).returncode
                == 0
            ), sha

    def test_no_type_e_1101_in_git_log(self):
        # The next leg (Type E #1101) must not exist yet: this run
        # opens the window, #1101 continues it.
        result = subprocess.run(
            ["git", "log", "--format=%s", "--grep=Type E #1101"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.stdout.strip() == "", result.stdout

    def test_anchor_sha_is_real(self):
        # Deselected pre-commit per #565: the anchor followup patches
        # ANCHORED_SHA to the 40-char main commit hash.
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), (
            "ANCHORED_SHA must be patched to the 40-char main commit "
            "hash post-commit per #565"
        )
        assert ANCHORED_SHA != "0" * 40, (
            "the all-zeros placeholder must be replaced by the anchor "
            "followup per #565"
        )


# ---------------------------------------------------------------------------
# 3. Corpus integrity
# ---------------------------------------------------------------------------
class TestTypeDCorpusIntegrity1100:
    def test_m889_block_present_in_wired_yaml(self):
        data = _m889_data()
        assert data["mechanism_id"] == 889
        assert data["iteration"] == 1097
        assert data["iteration_type"] == "A"

    def test_m890_block_present_in_journalists_yaml(self):
        data = _m890_data()
        assert data["mechanism_id"] == 890
        assert data["iteration"] == 1098
        assert data["iteration_type"] == "B"

    def test_m891_block_present_in_competitor_entities_yaml(self):
        data = _m891_data()
        assert data["mechanism_id"] == 891
        assert data["iteration"] == 1099
        assert data["iteration_type"] == "C"

    def test_max_mechanism_id_is_891(self):
        assert _max_numeric_mechanism_id() == 891

    def test_zero_892_forms_repo_wide(self):
        # Numeric 892 absent from profiles/; underscore/dash 892
        # mechanism key strings absent repo-wide (needles are
        # runtime-built per #715, so this file carries no contiguous
        # 892 literals).
        assert _repo_grep_numeric_mechanism_id(892) == []
        assert _repo_grep_underscore_mechanism(892) == []
        assert _repo_grep_dash_mechanism(892) == []


# ---------------------------------------------------------------------------
# 4. m889 (Type A #1097) qualitative discipline
# ---------------------------------------------------------------------------
class TestTypeDM889QualitativeDiscipline:
    def test_m889_iteration_fields(self):
        data = _m889_data()
        assert data["iteration"] == 1097
        assert data["iteration_type"] == "A"
        assert data["iteration_time"] == "2026-09-30 10:00 PDT"
        assert data["type"] == "Type A: Competitor Coverage Deep Dive"

    def test_m889_scorer_values_and_delta(self):
        # MANUAL ILLUSTRATIVE only: OpenAI Sep mean -0.175 vs carried
        # WIRED x Meta mean -0.375, delta +0.20 (Meta draws the harder
        # register; thesis-consistent directionally but small). The
        # Zeff-only read is the sharper test: -0.35 vs -0.375 =
        # +0.025, near-null parity on the leak-driven accountability
        # peg.
        scorer = _m889_data()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["delta"] == pytest.approx(0.20)
        assert scorer["delta_calc"] == "-0.175 - (-0.375) = +0.20"
        assert "+0.025" in scorer["delta_direction"]

    def test_m889_m877_family_extension(self):
        # Extends the m877 family from the safety-crisis register into
        # the coordination/antitrust register; the Zeff exclusive is
        # the strongest in-corpus evidence against payer-driven
        # suppression at WIRED (an adversarial-tilted exclusive on the
        # deal partner).
        text = _indented_block(M889_HOME, M889_KEY, M889_INDENT)
        assert "m877" in text
        assert "coordination/antitrust" in text or "coordination" in text

    def test_m889_register_entities(self):
        # WIRED x OpenAI pair vs carried WIRED x Meta arms.
        text = _indented_block(M889_HOME, M889_KEY, M889_INDENT)
        assert "OpenAI" in text
        assert "Meta" in text

    def test_m889_not_falsification_member(self):
        data = _m889_data()
        fam = data["falsification_family"]
        assert "NOT a falsification-family member" in fam
        assert "Ledger holds at 37" in fam

    def test_m889_statistical_discipline(self):
        # MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026 standing rule.
        data = _m889_data()
        assert "MANUAL ILLUSTRATIVE ONLY" in data["statistical_discipline"]
        assert "NOT_CALCULATED" in data["statistical_discipline"]
        scorer = data["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["is_significant"] is False
        assert scorer["verdict"] == "directionally_supported_not_proven"
        assert scorer["no_analysis_json_update"] is True
        assert scorer["artifact_grade"] is False

    def test_m889_research_method(self):
        # 6 browser.search query sets, 0 browser.open per #503
        # (excerpt-bounded; WIRED paywalled).
        text = _indented_block(M889_HOME, M889_KEY, M889_INDENT)
        assert "0 browser.open" in text
        assert "#503" in text


# ---------------------------------------------------------------------------
# 5. m890 (Type B #1098) qualitative discipline
# ---------------------------------------------------------------------------
class TestTypeDM890QualitativeDiscipline:
    def test_m890_iteration_fields(self):
        data = _m890_data()
        assert data["iteration"] == 1098
        assert data["iteration_type"] == "B"
        assert data["iteration_time"] == "2026-09-30 11:00 PDT"

    def test_m890_temporal_extension_and_delta(self):
        # TEMPORAL EXTENSION of m629 (Type B #658) into the Muse-agent
        # peg 75 days later. Meta arm -0.50 (Muse weeklong-test
        # data-collection alarm, excerpt-tier) vs carried Anthropic
        # Claude Cowork playful arm +0.10. Illustrative delta
        # (Anthropic minus Meta) +0.60, thesis-consistent.
        text = _indented_block(M890_HOME, M890_KEY, M890_INDENT)
        assert "m629" in text
        assert "+0.60" in text
        tones = re.findall(r"tone_MANUAL_ILLUSTRATIVE:\s*(-?[0-9.]+)", text)
        assert "-0.50" in tones, tones
        assert "0.10" in tones, tones

    def test_m890_first_dedicated_rogers_mechanism(self):
        # FIRST dedicated mechanism-id-sequence Type B mechanism on
        # Reece Rogers in journalists.yaml (m629 lives in the legacy
        # competitor-coverage-research.yaml list item).
        text = _indented_block(M890_HOME, M890_KEY, M890_INDENT)
        assert "FIRST dedicated" in text
        assert "Reece Rogers" in text

    def test_m890_not_falsification_member(self):
        data = _m890_data()
        fam = data["falsification_family"]
        assert "NOT a falsification-family member" in fam
        assert "holds at 37" in fam

    def test_m890_statistical_discipline(self):
        # MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026 standing rule.
        text = _indented_block(M890_HOME, M890_KEY, M890_INDENT)
        assert "MANUAL ILLUSTRATIVE ONLY" in text
        assert "is_significant False" in text
        assert "Engine NOT run" in text
        assert "directionally_supported_not_proven" in text

    def test_m890_research_method(self):
        # 4 browser.search query sets, 0 browser.open per #503
        # (excerpt-bounded).
        text = _indented_block(M890_HOME, M890_KEY, M890_INDENT)
        assert "0 browser.open" in text


# ---------------------------------------------------------------------------
# 6. m891 (Type C #1099) qualitative discipline
# ---------------------------------------------------------------------------
class TestTypeDM891QualitativeDiscipline:
    def test_m891_iteration_fields(self):
        data = _m891_data()
        assert data["iteration"] == 1099
        assert data["iteration_type"] == "C"
        assert data["iteration_time"] == "2026-09-30 12:00 PDT"
        assert data["type"] == "financial_incentive_mapping"

    def test_m891_twenty_seventh_direction(self):
        # UNILATERAL PRICING as the TWENTY-SEVENTH relationship
        # direction per the m807 enumeration: payer-set
        # micro-compensation decoupled from consent.
        data = _m891_data()
        assert "UNILATERAL PRICING" in data["relationship_direction_taxonomy"]
        assert _TW27 in data["relationship_direction_taxonomy"]

    def test_m891_rate_disclosure_legs(self):
        # First disclosed payment rates for the pilot m702/m708: under
        # $1,000 over months at the tail, over $1M/yr for one early
        # entrant, under 0.1% of ad revenue for small-to-midsize.
        data = _m891_data()
        assert "rate_disclosure_leg" in data
        assert "unilateral_pricing_leg" in data
        assert "decoupling_leg" in data
        assert "0.1%" in data["rate_disclosure_leg"]

    def test_m891_corpus_lineage(self):
        # connects_to [702, 708, 539, 666].
        data = _m891_data()
        assert data["connects_to"] == [702, 708, 539, 666]

    def test_m891_tone_not_scored(self):
        # Qualitative financial mapping only: tone NOT_SCORED, engine
        # NOT run.
        data = _m891_data()
        assert data["engine_run"] is False
        assert data["is_significant"] is False
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["artifact_grade"] is False

    def test_m891_not_falsification_member(self):
        data = _m891_data()
        fam = data["falsification_family"]
        assert "NOT a falsification-family member" in fam
        assert "holds at 37" in fam

    def test_m891_novelty_and_sources(self):
        # 5 relay URLs, all zero-hit repo-wide pre-commit; 1
        # browser.open per #503 (PYMNTS first-hand, 46 lines).
        text = _indented_block(M891_HOME, M891_KEY, M891_INDENT)
        assert "5 relay URLs" in text or "5 novel" in text


# ---------------------------------------------------------------------------
# 7. Falsification ledger
# ---------------------------------------------------------------------------
class TestTypeDFalsificationLedger1100:
    def _profiles_text(self, rel):
        return _read(os.path.join(REPO_ROOT, rel))

    def test_thirty_seventh_member_claim_once(self):
        # The THIRTY-SEVENTH member-claim form is present exactly once
        # repo-wide: m880 in profiles/the-verge.yaml.
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                text = open(p, encoding="utf-8", errors="replace").read()
                if "THIRTY-SEVENTH falsification-family member" in text:
                    hits.append(p)
        assert hits == [os.path.join(PROFILES_DIR, "the-verge.yaml")], hits

    def test_thirty_eighth_member_claim_absent(self):
        # No THIRTY-EIGHTH member-claim form anywhere in profiles/:
        # every THIRTY-EIGHTH hit is a negative-guard note
        # ("absent repo-wide", "remains the negative guard"), designed.
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                for line in open(p, encoding="utf-8", errors="replace"):
                    if "THIRTY-EIGHTH" in line and "member" in line:
                        assert (
                            "absent" in line
                            or "negative guard" in line
                            or "pre-commit" in line
                        ), (p, line.strip())

    def test_no_thirty_ninth_member_claim(self):
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                text = open(p, encoding="utf-8", errors="replace").read()
                assert "THIRTY-NINTH" not in text, p

    def test_twenty_sixth_direction_present(self):
        # DUAL-ROLE RECYCLING as the TWENTY-SIXTH relationship
        # direction (m888) is in competitor-entities.yaml.
        assert (
            "TWENTY-SIXTH relationship direction"
            in self._profiles_text("profiles/competitor-entities.yaml")
        )

    def test_twenty_seventh_direction_present(self):
        # UNILATERAL PRICING as the TWENTY-SEVENTH relationship
        # direction (m891) is in competitor-entities.yaml.
        assert _TW27 in self._profiles_text("profiles/competitor-entities.yaml")


# ---------------------------------------------------------------------------
# 8. Forward-looking staleness (per #1060 / #710 / #720)
# ---------------------------------------------------------------------------
class TestTypeDForwardLookingStaleness1100:
    def _stale_run(self, path, *deselects):
        cmd = [
            ".venv/bin/python",
            "-m",
            "pytest",
            path,
            "-q",
            "--no-header",
            "-p",
            "no:cacheprovider",
            "-o",
            "addopts=",
        ]
        for d in deselects:
            cmd.extend(["--deselect", "%s::%s" % (path, d)])
        result = subprocess.run(
            cmd, cwd=REPO_ROOT, capture_output=True, text=True, timeout=600
        )
        return result

    def _failed(self, result):
        return [
            line
            for line in result.stdout.splitlines()
            if line.startswith("FAILED")
        ]

    def test_1095_zero_889_needles_failed_by_design(self):
        # The #1095 Type D file's zero-889 forward guards must FAIL in
        # a subprocess (mechanism 889 landed at #1097 Type A): the
        # fail-by-design staleness markers are pinned as failures so
        # they are never silently ignored. Deselects the anchor /
        # rotation / novelty / doc-sync / itlog / staleness / suite /
        # repin / calibration / inflight classes per
        # #565/#719/#721; keeps the corpus-integrity, ledger and
        # guard-lifecycle classes. Note: the #1095 file was repinned
        # by this run (MAX_ID 888->891), so the constant-pinning
        # tests are not asserted here - only the literal-889 guards.
        result = self._stale_run(
            D1095_FILE,
            "TestNovelty1095",
            "TestTypeDRotationGuard1095",
            "TestTypeDM886QualitativeDiscipline",
            "TestTypeDM887QualitativeDiscipline",
            "TestTypeDM888QualitativeDiscipline",
            "TestTypeDForwardLookingStaleness1095",
            "TestBackgroundSuiteVerdict1095",
            "TestSyntheticEngineCalibration1095",
            "TestSuiteRelaunch1095",
            "TestTypeD1095RepinOf1090File",
            "TestTypeDDocSync1095",
            "TestTypeDIterationLog1095",
            "TestInflightIsolation1095",
        )
        assert result.returncode != 0
        failed = self._failed(result)
        for name in (
            "TestTypeDCorpusIntegrity1095::test_zero_889_forms_repo_wide",
            "TestGuardLifecycle1095::test_zero_next_numeric_889_in_profiles",
        ):
            assert any(name in line for line in failed), (name, failed)

    def test_1095_twenty_seventh_absence_failed_by_design(self):
        # The #1095 Type D file's twenty-seventh-direction absence
        # guard must FAIL: mechanism 891 registers UNILATERAL PRICING
        # as the twenty-seventh relationship direction at #1099.
        result = self._stale_run(
            D1095_FILE,
            "TestNovelty1095",
            "TestTypeDRotationGuard1095",
            "TestTypeDCorpusIntegrity1095",
            "TestTypeDM886QualitativeDiscipline",
            "TestTypeDM887QualitativeDiscipline",
            "TestTypeDM888QualitativeDiscipline",
            "TestTypeDForwardLookingStaleness1095",
            "TestGuardLifecycle1095",
            "TestBackgroundSuiteVerdict1095",
            "TestSyntheticEngineCalibration1095",
            "TestSuiteRelaunch1095",
            "TestTypeD1095RepinOf1090File",
            "TestTypeDDocSync1095",
            "TestTypeDIterationLog1095",
            "TestInflightIsolation1095",
        )
        assert result.returncode != 0
        failed = self._failed(result)
        name = "TestTypeDFalsificationLedger1095::test_twenty_sixth_direction_present"
        assert any(name in line for line in failed), failed

    def test_1098_max_890_and_zero_891_guards_failed_by_design(self):
        # The #1098 Type B file's max-890 and zero-numeric-891 guards
        # must FAIL: mechanism 891 landed at #1099 Type C (max numeric
        # mechanism_id is now 891). The underscore-891 and dash-891
        # guards keep passing (no contiguous literals added).
        result = self._stale_run(
            B1098_FILE,
            "TestNoveltyAnchorTypeB1098",
            "TestRotationGuard1095_1099Window",
            "TestCorpusNoveltyGreps",
            "TestMechanism890Structure",
            "TestMetaArmEvidence",
            "TestAnthropicArmEvidence",
            "TestTemporalExtensionAndDelta",
            "TestStatisticalDisciplineStandingRule",
            "TestFalsificationLedger",
            "TestConfoundersRankedStrongFirst",
            "TestCrossReferences",
            "TestResearchMethodPer503",
            "TestDocSyncRatchet",
            "TestIterationLogEntry",
            "TestInflightIsolation",
            "TestBlockHygiene",
        )
        assert result.returncode != 0
        failed = self._failed(result)
        for name in (
            "TestGuardLifecycle890Lands::test_max_numeric_id_is_890_not_889",
            "TestGuardLifecycle890Lands::test_zero_numeric_891_keys_in_profiles",
        ):
            assert any(name in line for line in failed), (name, failed)
        # The underscore-891 and dash-891 guards keep passing (no
        # contiguous literals added): they appear in neither the
        # failed list nor (in -q mode) by name, so the absence from
        # `failed` is the passing signal.
        assert not any(
            "test_zero_underscore_891_keys_repo_wide" in line for line in failed
        ), failed
        assert not any(
            "test_zero_dash_891_references_repo_wide" in line for line in failed
        ), failed

    def _class_run(self, path, cls):
        # Run a single class of a predecessor file by node id.
        cmd = [
            ".venv/bin/python",
            "-m",
            "pytest",
            "%s::%s" % (path, cls),
            "-q",
            "--no-header",
            "-p",
            "no:cacheprovider",
            "-o",
            "addopts=",
        ]
        result = subprocess.run(
            cmd, cwd=REPO_ROOT, capture_output=True, text=True, timeout=600
        )
        return result

    def test_1099_zero_892_guards_still_pass(self):
        # The #1099 Type C file's zero-892 forward guards must still
        # PASS: mechanism 892 has not landed. They fail BY DESIGN when
        # the next A/B/C leg lands it.
        result = self._class_run(C1099_FILE, "TestCorpusNoveltyPostCommit")
        assert result.returncode == 0, result.stdout[-2000:]

    def test_1100_zero_892_needles_pass_here(self):
        # This run pins the zero-892 forward guards (they fail BY
        # DESIGN when mechanism 892 lands at a future A/B/C leg of
        # the 1100-1104 window).
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []


# ---------------------------------------------------------------------------
# 9. Guard lifecycle: mechanisms 889/890/891 land this window
# ---------------------------------------------------------------------------
class TestGuardLifecycle1100:
    def test_889_890_891_landed_this_window(self):
        # All three window mechanisms landed in their commits: 889 at
        # #1097 Type A, 890 at #1098 Type B, 891 at #1099 Type C.
        data_889 = _m889_data()
        data_890 = _m890_data()
        data_891 = _m891_data()
        assert data_889["mechanism_id"] == 889
        assert data_890["mechanism_id"] == 890
        assert data_891["mechanism_id"] == 891
        assert data_889["iteration"] == 1097
        assert data_890["iteration"] == 1098
        assert data_891["iteration"] == 1099

    def test_1100_file_pins_max_id_891_and_next_892(self):
        # This file is the new window-opener pinning zero-892
        # forward guards (per the fail-forward cadence: each
        # window's opener supersedes the prior file's NEXT_NUM pin).
        assert MAX_ID == 891
        assert NEXT_NUM == 892
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_next_numeric_892_in_profiles(self):
        # Forward guard: zero numeric 892 mechanism ids in
        # profiles/ - will fail by design at the run that lands
        # mechanism 892.
        assert _repo_grep_numeric_mechanism_id(892) == []

    def test_no_new_mechanisms_below_max(self):
        # No numeric mechanism id in profiles/ may exceed 891 -
        # corpus max is pinned.
        assert _max_numeric_mechanism_id() <= 891


# ---------------------------------------------------------------------------
# 10. Background suite verdict per #795
# ---------------------------------------------------------------------------
class TestBackgroundSuiteVerdict1100:
    def _log_stats(self):
        size = os.path.getsize(PRIOR_SUITE_LOG)
        text = _read(PRIOR_SUITE_LOG)
        return size, text.count("."), text.count("F"), text.count("E"), text

    def test_prior_suite_died_third_consecutive(self):
        # The #1095-launched background full suite DIED: 3237 bytes
        # (~5% dots), last write Sep 30 08:59:54 PDT, zero summary
        # tokens (no "passed"/"failed" summary, no collected-count
        # token), no live pytest process. Per the #795 convention
        # this is recorded as DIED, not "interrupted": the run
        # produces no usable verdict.
        size, dots, fails, errors, text = self._log_stats()
        assert size == 3237, size
        assert 0.04 <= dots / 55895 <= 0.06, (dots, dots / 55895)
        assert fails == 0, fails
        assert errors == 0, errors
        assert "passed" not in text
        assert "failed" not in text
        assert " collected " not in text
        assert "no tests ran" not in text

    def test_no_live_pytest_process(self):
        result = subprocess.run(
            ["pgrep", "-f", "pytest.*type_d_1095"],
            capture_output=True,
            text=True,
        )
        assert result.returncode != 0, (
            "a pytest process for the #1095 suite must not still be "
            "alive when its verdict is recorded"
        )

    def test_tombstone_lineage_advances_to_79th(self):
        # THIRD consecutive background-suite death of the new streak
        # (the 57-run streak ENDED at #1085 when the #1080 suite
        # completed). Tombstone lineage advances SEVENTY-EIGHTH ->
        # SEVENTY-NINTH; recorded in the #1100 iteration-log entry.
        # Deselected pre-commit (log entry is written in the
        # doc-sync step).
        text = _read(LOG_PATH)
        assert "SEVENTY-NINTH" in text


# ---------------------------------------------------------------------------
# 11. Fresh synthetic engine calibration (new values, not #1095's)
# ---------------------------------------------------------------------------
class TestSyntheticEngineCalibration1100:
    # Scratch-run values produced at this run (Wed 2026-09-30 ~13:05
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
                datetime(2026, 9, 30),
                datetime(2026, 9, 30),
            )

        return calc

    def test_strong_effect_is_significant(self):
        calc = self._calculate()
        meta = [-0.55, -0.60, -0.50, -0.65, -0.55, -0.60, -0.50, -0.65]
        comp = [-0.05, 0.05, 0.10, -0.10, 0.05, -0.05, 0.10, -0.05]
        result = calc(meta, comp)
        assert result.asymmetry_score == pytest.approx(-0.58125)
        assert result.t_statistic == pytest.approx(-16.7808029854715)
        assert result.p_value < 1e-9
        assert result.cohens_d == pytest.approx(-8.39040149273575)
        assert result.is_significant is True
        # The strong arm-swap negates the asymmetry exactly.
        swapped = calc(comp, meta)
        assert swapped.asymmetry_score == pytest.approx(
            -result.asymmetry_score
        )

    def test_null_effect_is_not_significant(self):
        calc = self._calculate()
        arm_a = [0.05, -0.03, 0.02, -0.04, 0.06, -0.02, 0.03, -0.05]
        arm_b = [0.04, -0.02, 0.03, -0.03, 0.05, -0.01, 0.02, -0.06]
        result = calc(arm_a, arm_b)
        assert result.asymmetry_score == pytest.approx(0.0, abs=1e-12)
        assert result.p_value > 0.9
        assert result.is_significant is False
        lo = result.confidence_interval_lower
        hi = result.confidence_interval_upper
        assert lo < 0 < hi

    def test_degenerate_single_tone_inputs(self):
        # Single-tone arms: t 0.0, p 1.0, d 0.0, not significant.
        calc = self._calculate()
        result = calc([-0.50], [-0.40])
        assert result.asymmetry_score == pytest.approx(-0.10)
        assert result.t_statistic == 0.0
        assert result.p_value == 1.0
        assert result.cohens_d == 0.0
        assert result.is_significant is False

    def test_engine_not_promoted_to_findings(self):
        # Aug 28 2026 standing rule: the finding layer is MANUAL
        # ILLUSTRATIVE ONLY; the engine is never promoted to
        # findings; no analysis.json update for verification runs.
        assert _DOC is not None
        for marker in (
            "MANUAL/QUALITATIVE ONLY",
            "engine NOT run",
            "no analysis.json update",
        ):
            assert marker in _DOC, marker


# ---------------------------------------------------------------------------
# 12. Suite re-launch (this run's background full suite)
# ---------------------------------------------------------------------------
class TestSuiteRelaunch1100:
    def test_relaunch_log_path_written(self):
        # The re-launched full suite log exists in goal hidden_files
        # (created by this run's background launch before commit).
        assert os.path.exists(SUITE_LOG), (
            "the #1100 background suite must be re-launched to "
            + SUITE_LOG
            + " before the main commit"
        )

    def test_relaunch_log_is_full_inventory(self):
        # The re-launch runs WITHOUT -x: the full inventory
        # (calendar by-design failures included) is needed for the
        # #1105 triage. The log must hold pytest progress output,
        # not just a header.
        text = _read(SUITE_LOG)
        assert text.count(".") > 100, (
            "the re-launched suite log should accumulate dot "
            "progress; got %d dots" % text.count(".")
        )

    def test_next_type_d_run_owns_the_verdict(self):
        # Per the #795 convention, the NEXT Type D run (#1105)
        # checks this suite's verdict; this run only records the
        # launch.
        assert "type_d_1100_full_suite.log" in SUITE_LOG


# ---------------------------------------------------------------------------
# 13. The #1095 Type D file's historical repin (committed with this run)
# ---------------------------------------------------------------------------
class TestTypeD1095RepinOf1095File:
    def _repin_text(self):
        return _read(os.path.join(REPO_ROOT, D1095_FILE))

    def test_1095_max_id_repinned_to_891(self):
        assert "MAX_ID = 891" in self._repin_text()

    def test_1095_next_num_repinned_to_892(self):
        assert "NEXT_NUM = 892" in self._repin_text()

    def test_1095_rotation_guard_is_window_closed_complete(self):
        # The #1095 file's rotation guard was rewritten to the
        # #1090 repin form: window-closed-complete subsequence
        # (1095-1099 closed by Type C #1099, main def43924).
        text = self._repin_text()
        assert "test_1095_window_closed_complete" in text
        assert "test_type_c_1099_landed" in text
        assert "def43924" in text
        # The opener-form tests are removed (the repin NOTE mentions
        # their names, so the def-line form is the removal check).
        assert "def test_rotation_window_opens_1095" not in text
        assert "def test_no_type_e_1096_in_git_log" not in text

    def test_1095_anchor_mechanics_untouched(self):
        # The repin touches MAX_ID/NEXT_NUM/rotation guard only; the
        # anchor line keeps the #1095 anchor followup's patched hash
        # (untouched by the repin).
        assert (
            'ANCHORED_SHA = "ed8c9cf2c0d71b34cc31fab5494f02dc828bcd42"'
            in self._repin_text()
        )

    def test_1095_landed_mechanism_assertions_untouched(self):
        # m886/887/888 landing assertions are untouched by the repin.
        text = self._repin_text()
        assert 'data["mechanism_id"] == 886' in text
        assert 'data["mechanism_id"] == 887' in text
        assert 'data["mechanism_id"] == 888' in text


# ---------------------------------------------------------------------------
# 14. Doc-sync per #719 (fails pre-commit by design; passes post-sync)
# ---------------------------------------------------------------------------
class TestTypeDDocSync1100:
    def _readme(self):
        return _read(os.path.join(REPO_ROOT, "README.md"))

    def _arch(self):
        return _read(os.path.join(REPO_ROOT, "docs/ARCHITECTURE.md"))

    def test_readme_stats_table_ratchets(self):
        # The stats table carries the new counts (README_TEST_COUNT
        # tests / README_FILE_COUNT files); the constants are patched
        # post-first-run with the true collected count.
        assert str(README_TEST_COUNT) in self._readme()
        assert str(README_FILE_COUNT) in self._readme()

    def test_readme_test_file_table_prepends_this_file(self):
        assert OWN_BASENAME in self._readme()

    def test_architecture_tests_tree_lists_this_file(self):
        assert OWN_BASENAME in self._arch()

    def test_readme_counts_match_constants(self):
        # The README stats row must match the patched constants
        # (post-first-run; pre-commit this fails by design per #719).
        text = self._readme()
        assert ("%d" % README_TEST_COUNT) in text
        assert ("%d" % README_FILE_COUNT) in text


# ---------------------------------------------------------------------------
# 15. Iteration log entry
# ---------------------------------------------------------------------------
class TestTypeDIterationLog1100:
    def test_1100_entry_leads_log(self):
        # The "## #1100 Type D:" entry leads the log (newest-first
        # ordering); hashes are TBD until the anchor followup patches
        # them per #565. Deselected pre-commit per #721.
        assert _read(LOG_PATH).startswith("## #1100 Type D:")

    def test_1100_entry_names_window_and_predecessors(self):
        text = _read(LOG_PATH)
        entry = text.split("## #1099 Type C:")[0]
        assert "1100-1104" in entry
        assert "def43924" in entry
        assert "SEVENTY-NINTH" in entry

    def test_1095_entry_present(self):
        # Repin form: the #1095 entry is present in the log (no longer
        # required to be newest-first).
        assert "## #1095 Type D:" in _read(LOG_PATH)


# ---------------------------------------------------------------------------
# 16. In-flight isolation
# ---------------------------------------------------------------------------
class TestInflightIsolation1100:
    def test_no_concurrent_inflight_iteration_commits_staged(self):
        # The in-flight #899/#938/#900/#1012-wt working-tree edits
        # are owned by their runs; this run stages only its own
        # files. (Pre-staging this passes vacuously; it guards the
        # post-staging state before commit.)
        status = _git("status", "--short")
        staged = [l for l in status.splitlines() if l.startswith(("M ", "A "))]
        for f in (
            "nytimes.yaml",
            "test_type_b_938_",
            "test_type_d_900_",
            "test_type_a_1012_",
        ):
            assert not any(f in l for l in staged), (f, staged)

    def test_this_run_stages_only_own_files(self):
        # This run's staged set is the #1100 test file, the #1095
        # repin, and the doc-sync files only.
        status = _git("status", "--short")
        staged = [l for l in status.splitlines() if l.startswith(("M ", "A "))]
        allowed = (
            "test_type_d_1100_",
            "test_type_d_1095_",
            "README.md",
            "ARCHITECTURE.md",
            "iteration-log.md",
        )
        for l in staged:
            assert any(a in l for a in allowed), l

    def test_in_flight_files_present_uncommitted(self):
        # The in-flight blocks are present in the working tree as
        # uncommitted changes (owned by their runs): the #899
        # nytimes.yaml hunk, the #938 test-file edit, the untracked
        # #900 test file, and the #1012 working-tree edit.
        status = _git("status", "--short")
        assert " M profiles/nytimes.yaml" in status
        assert " M tests/test_type_b_938_" in status
        assert "?? tests/test_type_d_900_" in status
        assert " M tests/test_type_a_1012_" in status
