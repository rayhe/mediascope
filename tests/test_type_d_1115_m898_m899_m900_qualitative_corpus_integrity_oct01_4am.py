"""Type D -- Iteration #1115 (Thu 2026-10-01 04:00 PDT): m898/m899/m900
qualitative-discipline verification + post-1110-1114 corpus integrity
(max numeric mechanism_id 900; zero next-number 901 keys in
numeric/underscore/dash mechanism forms; underscore/dash 901 needles
are format-built per #715 so no guard-literal carrier file exists -
the m898 block key carries the underscore-form 898 mechanism key
string in profiles/wired.yaml, so it is built at runtime in this
file per #715; the m899/m900 block keys carry no mechanism-number
substring (designed keying per #715, colon-form only); the #1112/
#1113/#1114 window files are NOT edited by this run - their now-stale
forward-looking pins are recorded as fail-by-design via subprocess in
the staleness class (#1113's max-899 pin trips on the landed 900;
#1113's zero-900 numeric forward guard trips on the landed 900 while
its underscore/dash guards HOLD green per the #1114-recorded
designed-keying end-state; #1112's max-898 pin already stale,
re-pinned; #1114's post-commit classes stay green); ledger holds at
41 with the FORTY-FIRST member-claim form present once
(journalists.yaml m899 falsification_family) and the FORTY-SECOND
member-claim form absent repo-wide (needle format-built per #715);
the THIRTIETH relationship direction is present in
competitor-entities.yaml (m900 TRACK-SEPARATED PRICING); the
THIRTY-FIRST relationship-direction claim form is absent repo-wide
(needle format-built per #715)) + the #1110 background-suite verdict
(DIED at 1874 bytes / 1690 dots ~2% with last write Sep 30 23:42:00
PDT and zero summary tokens, no live pytest process - SIXTH
consecutive background-suite death of the new streak; the 57-run
streak ENDED at #1085 when the #1080 suite completed; tombstone
lineage advances EIGHTY-FIRST -> EIGHTY-SECOND) + fresh synthetic
engine calibration (new values, not #1110's) + re-launch of the full
suite as a background process writing to goal hidden_files
type_d_1115_full_suite.log WITHOUT -x (the full inventory, calendar
by-design failures included, is needed for the #1120 triage; the next
Type D run checks its verdict per the #795 convention).

Type D FIRST leg of the 1115-1119 window, OPENING it
(D->E->A->B->C). Committed predecessor #1114 Type C (03:00 PDT Oct 1)
CLOSED the 1110-1114 window (D #1110, E #1111, A #1112, B #1113,
C #1114). Rotation per the #565 anchor + rotation guard.
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
- m898 (Type A #1112, wired.yaml 6-space block key,
  `mechanism_id: 898` field form; block key count 1 - colon-form
  line only, designed - no block_key field in the m898 block; the
  underscore-form 898 needle in the block key is format-built in
  this file per #715): WIRED x OpenAI Sep-29 LASST Hugging Face
  lawsuit accountability register (-0.40 MANUAL ILLUSTRATIVE,
  Lily Hay Newman, explainx.ai relay-attested, excerpt-tier per
  #503) vs carried WIRED x Meta arms from m877 via m889
  (Pinky Promises skepticism -0.45, NameTag class action -0.30,
  un-rescored per #807). Illustrative pooled delta -0.025
  near-null parity: the paid licensing counterparty (Conde Nast
  Aug-2024 deal, m504) draws the marginally HARDER register than
  Meta; the clean adversarial-legal-peg read (-0.40 LASST vs
  -0.30 NameTag = -0.10) is the sharper falsification test, same
  genre, same outlet, controlled confound. Answers m889's open
  empirical test: WIRED coverage of the Sep-29 LASST California
  lawsuit EXISTS and is adversarial, not softened or suppressed.
  FORTIETH falsification-family member; ledger 39->40.
- m899 (Type B #1113, journalists.yaml 4-space block key under
  joanna_stern competitor_coverage, `mechanism_id: 899` field
  form; block key count 2 - colon-form line + block_key field,
  designed): Joanna Stern (New Things/NBC independent phase)
  Sep-24 Zuckerberg Meta Connect accountability interview
  (-0.50 MANUAL ILLUSTRATIVE, NBC News YouTube URL verbatim,
  date bounded via Techmeme 2026-09-24 02:23:05) vs FRESH Sep-10
  iPhone Duo enthusiast hands-on (+0.35 MANUAL ILLUSTRATIVE,
  macdailynews relay-attested, excerpt-bounded per #503).
  Illustrative delta (Apple minus Meta) +0.85: same journalist,
  same month, both zero-deal - Apple draws the enthusiast
  register, Meta draws the accountability register. The naive
  financial-structure prediction falsifies in BOTH directions at
  the journalist level. FORTY-FIRST falsification-family member;
  ledger 40->41. FIRST dedicated Type B mechanism on Joanna
  Stern (m105 carries no numbered Type B pair).
- m900 (Type C #1114, competitor-entities.yaml zero-indent block
  key, `mechanism_id: 900` field form; block key count 2 -
  colon-form line + block_key field, designed): Google News AI
  pilot three-instrument TRACK-SEPARATED PRICING as the
  THIRTIETH relationship direction (commercial partnerships:
  Dec 2025 deals, take-it-or-leave-it, NDAs, no-sue clauses,
  Guardian + FT at single-figure GBP millions/yr, FT joined Feb
  2026) vs AI Contribution Pilot widget-metered micro-pricing
  (m891/m894/m897) vs News Showcase legacy licensing
  conversion (2,800 publications, 33 countries) - three
  parallel pricing universes, three legal categories, so no
  unified price for AI-use of publisher content can form across
  tracks. Tone NOT_SCORED per the Aug 28 2026 standing rule.
  NOT a falsification-family member; ledger holds at 41,
  FORTY-SECOND member-claim absent.

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
    "test_type_d_1115_m898_m899_m900_qualitative_corpus_"
    "integrity_oct01_4am.py"
)

MAX_ID = 900
NEXT_NUM = 901

# Patched by the anchor followup commit per #565 (post-main-commit).
ANCHORED_SHA = "0" * 40

# Doc-sync constants per #719 (patched post-first-run with the true
# collected count).
README_TEST_COUNT = 57961
README_FILE_COUNT = 1440

# Format-built per the #715 convention: this source file carries no
# contiguous underscore-form mechanism key literal for the landed
# window mechanism 898 or the next number (901). The m899/m900
# block keys carry no mechanism-number substring (designed keying),
# so they are plain literals.
M898_KEY = (
    "mechanism" + "_898" + "_wired_openai_lasst_huggingface_"
    "lawsuit_register_vs_meta_carried_arms_sep30"
)
M898_INDENT = 4
M898_HOME = "profiles/wired.yaml"
M899_KEY = (
    "type_b_1113_joanna_stern_meta_zuckerberg_interview_"
    "vs_apple_iphone_duo_register_sep2026"
)
M899_INDENT = 4
M899_HOME = "profiles/careers/journalists.yaml"
M900_KEY = (
    "type_c_1114_google_news_ai_pilot_three_track_"
    "segmentation_trackseparatedpricing_thirtieth_"
    "direction_oct01_3am"
)
M900_INDENT = 0
M900_HOME = "profiles/competitor-entities.yaml"

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770
MID_901 = "mechanism_id: " + "901"  # fragment-built per #715

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1115_full_suite.log"
)
PRIOR_SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1110_full_suite.log"
)
A1112_FILE = (
    "tests/test_type_a_1112_wired_openai_lasst_huggingface_"
    "lawsuit_register_vs_meta_carried_arms_oct01_1am.py"
)
B1113_FILE = (
    "tests/test_type_b_1113_joanna_stern_meta_zuckerberg_"
    "interview_vs_apple_iphone_duo_register_sep2026_2am.py"
)
C1114_FILE = (
    "tests/test_type_c_1114_google_news_ai_pilot_three_track_"
    "segmentation_trackseparatedpricing_thirtieth_"
    "direction_oct01_3am.py"
)

_DOC = __doc__

# The thirty-first-direction and forty-second-member needles are
# fragment-built per #715 so this file carries no contiguous literal
# of a forward-guard claim form. The landed FORTY-FIRST member and
# THIRTIETH direction forms are plain literals (already in corpus).
_T41 = "FORTY-FIRST falsification-family member"
_TW30 = "THIRTIETH relationship direction"
_T42 = "FORTY-" + "SECOND falsification-family member"
_TW31 = "THIRTY-" + "FIRST relationship direction"


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
# numbers in git history: #1115 Type D opens the 1115-1119 window;
# #1114 Type C (committed 03:00 PDT Oct 1) is the schedule
# predecessor and CLOSED the 1110-1114 window. The in-flight runs
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
    file carries a contiguous 901-form mechanism literal (verified
    pre-commit), so the 901 sweeps run repo-wide with only this file
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


def _m898_data():
    return _block_data(M898_HOME, M898_KEY, M898_INDENT)


def _m899_data():
    return _block_data(M899_HOME, M899_KEY, M899_INDENT)


def _m900_data():
    return _block_data(M900_HOME, M900_KEY, M900_INDENT)


# ---------------------------------------------------------------------------
# 1. Novelty
# ---------------------------------------------------------------------------
class TestNovelty1115:
    def test_no_type_d_1115_test_file_preexisting(self):
        files = glob.glob(
            os.path.join(TESTS_DIR, "test_type_d_1115*.py")
        )
        assert files == [os.path.join(TESTS_DIR, OWN_BASENAME)], files

    def test_no_type_d_1115_in_git_log(self):
        # Pre-commit novelty guard: no commit may already claim this slot.
        # SUPERSEDED BY DESIGN once this run's main commit ("Type D #1115:")
        # lands; post-commit, TestTypeDRotationGuard1115 asserts the anchor
        # and window instead. Deselect this test in post-commit full runs.
        log = _git("log", "--format=%s", "--grep=Type D #1115")
        assert "Type D #1115" not in log

    def test_max_id_is_900(self):
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_901_numeric_forms_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_block_keys_unique_in_home_yamls(self):
        # m898: colon-form line only (count 1, designed - no
        # block_key field in the m898 block; the underscore-form 898
        # needle in the block key is format-built in this file per
        # #715). m899/m900: colon-form line + block_key field
        # (count 2 each, designed).
        wired = _read(os.path.join(REPO_ROOT, M898_HOME))
        assert wired.count(M898_KEY) == 1, wired.count(M898_KEY)
        jou = _read(os.path.join(REPO_ROOT, M899_HOME))
        assert jou.count(M899_KEY) == 2, jou.count(M899_KEY)
        ent = _read(os.path.join(REPO_ROOT, M900_HOME))
        assert ent.count(M900_KEY) == 2, ent.count(M900_KEY)


# ---------------------------------------------------------------------------
# 2. Rotation guard (2 tests deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestTypeDRotationGuard1115:
    def test_rotation_window_opens_1115(self):
        # FIRST leg of the 1115-1119 window, OPENING it (per #565:
        # D #1115 -> E #1116 -> A #1117 -> B #1118 -> C #1119).
        # Deselected pre-commit (this run's main commit is not yet
        # in history); passes post-commit.
        w = _window()
        assert w[0] == ("D", "1115"), w
        # Newest-first distinct sequence: D #1115 (this run) opens
        # the window after the closed 1110-1114 window (C #1114,
        # B #1113, A #1112, E #1111).
        assert [t for t, _ in w[:5]] == ["D", "C", "B", "A", "E"], w

    def test_predecessor_1114_chain_present(self):
        # #1114 Type C CLOSED the 1110-1114 window; its main/anchor/
        # log-hash chain must be in history before this run commits.
        log = _git("log", "--format=%H %s")
        assert "9ef55c47" in log
        assert "26bb3d3a" in log
        assert "5e1151e6" in log

    def test_no_type_e_1116_in_git_log(self):
        log = _git("log", "--format=%s", "--grep=Type E #1116")
        assert "Type E #1116" not in log

    def test_anchor_sha_is_real(self):
        # Patched post-main-commit by the anchor followup per #565.
        # Deselected pre-commit (placeholder by design); passes
        # post-patch.
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA
        assert ANCHORED_SHA != "0" * 40


# ---------------------------------------------------------------------------
# 2b. Novelty anchor (1 test, deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestTypeDNoveltyAnchor1115:
    def test_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per #565: the main commit does not
        # exist yet. Post-commit this asserts the single #1115
        # commit is the anchor and carries the test-file changes.
        log = _git("log", "--format=%H %s", "--grep=Type D #1115")
        assert "Type D #1115" in log
        assert ANCHORED_SHA in log


# ---------------------------------------------------------------------------
# 3. Corpus integrity
# ---------------------------------------------------------------------------
class TestTypeDCorpusIntegrity1115:
    def test_m898_block_present_in_wired_yaml(self):
        data = _m898_data()
        assert data["mechanism_id"] == 898

    def test_m899_block_present_in_journalists_yaml(self):
        data = _m899_data()
        assert data["mechanism_id"] == 899

    def test_m900_block_present_in_competitor_entities_yaml(self):
        data = _m900_data()
        assert data["mechanism_id"] == 900

    def test_max_mechanism_id_is_900(self):
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_901_forms_repo_wide(self):
        # Forward guard: zero numeric/underscore/dash 901 keys -
        # will fail by design at the run that lands mechanism 901.
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_m898_key_count_is_designed(self):
        # Colon-form key line only: the m898 block carries no
        # block_key field, and the underscore-form 898 needle is
        # format-built in this file per #715 (no literal trip).
        text = _read(os.path.join(REPO_ROOT, M898_HOME))
        lines = [
            l
            for l in text.splitlines()
            if M898_KEY in l
        ]
        assert len(lines) == 1, lines
        assert lines[0].strip() == M898_KEY + ":"

    def test_m899_key_count_is_designed(self):
        # Colon-form key line + block_key field value: exactly 2,
        # no other carrier.
        text = _read(os.path.join(REPO_ROOT, M899_HOME))
        lines = [
            l
            for l in text.splitlines()
            if M899_KEY in l
        ]
        assert len(lines) == 2, lines
        assert lines[0].strip() == M899_KEY + ":"
        assert "block_key:" in lines[1]

    def test_m900_key_count_is_designed(self):
        # Colon-form key line + block_key field value: exactly 2,
        # no other carrier.
        text = _read(os.path.join(REPO_ROOT, M900_HOME))
        lines = [
            l
            for l in text.splitlines()
            if M900_KEY in l
        ]
        assert len(lines) == 2, lines
        assert lines[0].strip() == M900_KEY + ":"
        assert "block_key:" in lines[1]


# ---------------------------------------------------------------------------
# 4. m898 qualitative discipline (Type A #1112)
# ---------------------------------------------------------------------------
class TestTypeDM898QualitativeDiscipline:
    def test_m898_iteration_fields(self):
        data = _m898_data()
        assert data["iteration"] == 1112
        assert data["iteration_type"] == "A"
        assert data["publication"] == "WIRED"
        assert data["type"] == "Type A: Competitor Coverage Deep Dive"
        assert data["mechanism_id"] == 898

    def test_m898_scorer_values_and_delta(self):
        data = _m898_data()
        scorer = data["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["target_scores"] == [-0.4]
        assert scorer["target_avg"] == -0.4
        assert scorer["peer_scores"] == [-0.45, -0.3]
        assert scorer["peer_avg"] == -0.375
        assert scorer["delta"] == -0.025
        assert scorer["delta_calc"] == "-0.40 - (-0.375) = -0.025"
        # Near-null parity, the paid licensing counterparty drawing
        # the marginally HARDER register; the clean
        # adversarial-legal-peg read (-0.40 LASST vs -0.30 NameTag =
        # -0.10) is the sharper falsification test.
        assert "HARDER register" in scorer["delta_direction"]
        assert "adversarial-legal-peg" in scorer["delta_direction"]

    def test_m898_open_empirical_test_answered(self):
        data = _m898_data()
        assert "m889" in data["competitor_pair"]
        assert "m877" in data["competitor_pair"]
        assert "Legal Advocates for Safe Science and Technology" in data[
            "finding"
        ]
        # The finding documents the adversarial register on the
        # paid licensing counterparty - m889's open test answered.
        assert "adversarial" in data["finding"]

    def test_m898_openai_arm_register(self):
        data = _m898_data()
        arm = data["articles_openai"][0]
        assert arm["manual_illustrative_tone"] == -0.4
        assert arm["date"] == "2026-09-29"
        assert arm["register"] == (
            "adversarial_accountability_enforcement_litigation"
        )
        assert "Lily Hay Newman" in arm["url_source"]

    def test_m898_meta_arms_carried_unrescored(self):
        data = _m898_data()
        arms = data["articles_meta"]
        assert len(arms) == 2
        assert arms[0]["tone_carried"] == -0.45
        assert arms[1]["tone_carried"] == -0.3
        for arm in arms:
            assert "un-rescored" in arm["source"]
            assert "#807" in arm["source"]

    def test_m898_fortieth_falsification_member(self):
        data = _m898_data()
        assert "FORTIETH falsification-family member" in data[
            "falsification_family"
        ]
        assert data["falsification_ledger"] == "40"

    def test_m898_statistical_discipline(self):
        data = _m898_data()
        disc = data["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE ONLY" in disc
        assert "engine NOT run" in disc
        assert "NOT_CALCULATED" in disc
        assert "artifact_grade false" in disc
        assert data["no_analysis_json_update"] is True
        assert data["correlation_not_causation"] is True

    def test_m898_research_method(self):
        data = _m898_data()
        assert "3 browser.search query sets" in data["research_method"]
        assert "0 browser.open" in data["research_method"]

    def test_m898_confounders_and_counterevidence(self):
        data = _m898_data()
        assert set(data["confounders_ranked"]) == {
            "strong",
            "moderate",
            "weak",
        }
        assert any(
            "Excerpt-bounded" in c for c in data["confounders_ranked"]["strong"]
        )
        assert len(data["counter_evidence"]) == 5


# ---------------------------------------------------------------------------
# 5. m899 qualitative discipline (Type B #1113)
# ---------------------------------------------------------------------------
class TestTypeDM899QualitativeDiscipline:
    def test_m899_iteration_fields(self):
        data = _m899_data()
        assert data["mechanism_id"] == 899
        assert data["iteration"] == 1113
        assert data["type"] == "Type B: Journalist Cross-Entity Tracking"
        assert data["journalist"] == "Joanna Stern"
        assert data["publication"] == "new-things"
        assert data["block_key"] == M899_KEY

    def test_m899_forty_first_falsification_member(self):
        data = _m899_data()
        assert _T41 in data["falsification_family"]
        assert data["falsification_ledger"] == "41"

    def test_m899_illustrative_delta_and_inversion(self):
        data = _m899_data()
        assert data["meta_arm"]["manual_illustrative_tone"] == -0.5
        assert data["apple_arm"]["manual_illustrative_tone"] == 0.35
        delta = data["illustrative_delta"]
        assert "+0.35 - (-0.50) = +0.85" in delta
        # The naive financial-structure prediction falsifies in BOTH
        # directions at the journalist level.
        assert "falsifies" in data["falsification_family"]

    def test_m899_meta_arm_fresh(self):
        data = _m899_data()
        meta = data["meta_arm"]
        assert meta["date"] == "2026-09-24"
        assert "youtube.com" in meta["url"]
        assert "Zuckerberg" in meta["title"]

    def test_m899_apple_arm_fresh(self):
        data = _m899_data()
        apple = data["apple_arm"]
        assert "2026-09-10" in apple["date_bound"]
        assert "macdailynews" in apple["date_bound"]

    def test_m899_first_dedicated_stern_mechanism(self):
        data = _m899_data()
        assert "FIRST dedicated Type B mechanism on Joanna Stern" in data[
            "novelty"
        ]
        assert "Mechanism 105" in data["novelty"]

    def test_m899_strong_confounders_present(self):
        data = _m899_data()
        texts = [c for c in data["confounders"]]
        assert any("[STRONG]" in c for c in texts)
        assert any("Factual-substrate" in c for c in texts)

    def test_m899_counterevidence_present(self):
        data = _m899_data()
        assert len(data["counterevidence"]) == 4

    def test_m899_statistical_discipline(self):
        data = _m899_data()
        disc = data["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE ONLY" in disc
        assert "engine NOT run" in disc
        assert "is_significant false" in disc
        assert "NOT_CALCULATED" in disc
        assert data["no_analysis_json_update"] is True
        assert data["correlation_not_causation"] is True

    def test_m899_research_method(self):
        data = _m899_data()
        assert "3 browser.search query sets" in data["research_method"]


# ---------------------------------------------------------------------------
# 6. m900 qualitative discipline (Type C #1114)
# ---------------------------------------------------------------------------
class TestTypeDM900QualitativeDiscipline:
    def test_m900_iteration_fields(self):
        data = _m900_data()
        assert data["mechanism_id"] == 900
        assert data["iteration"] == 1114
        assert data["iteration_type"] == "C"
        assert data["type"] == "financial_incentive_mapping"
        assert data["block_key"] == M900_KEY

    def test_m900_thirtieth_direction(self):
        data = _m900_data()
        assert "THIRTIETH" in data["mechanism_name"]
        tax = data["relationship_direction_taxonomy"]
        assert "THIRTIETH" in tax
        assert "TRACK-SEPARATED PRICING" in tax

    def test_m900_commercial_terms_leg(self):
        data = _m900_data()
        leg = data["commercial_terms_leg"]
        assert "Dec 11 2025" in leg
        assert "take-it-or-leave-it" in leg
        assert "single figure millions" in leg

    def test_m900_no_sue_category_leg(self):
        data = _m900_data()
        leg = data["no_sue_category_leg"]
        assert "no-sue" in leg
        assert "renting peace" in leg

    def test_m900_track_separation_leg(self):
        data = _m900_data()
        leg = data["track_separation_leg"]
        assert "Three tracks" in leg
        assert "AI Contribution Pilot" in leg
        assert "News Showcase" in leg

    def test_m900_falsifiable_legs(self):
        data = _m900_data()
        tax = data["relationship_direction_taxonomy"]
        assert "Falsifiable:" in tax
        assert "(1)" in tax and "(2)" in tax and "(3)" in tax

    def test_m900_coverage_nexus(self):
        data = _m900_data()
        nexus = data["coverage_nexus"]
        assert "FT" in nexus
        assert "Guardian" in nexus
        assert "track (a)" in nexus

    def test_m900_tone_not_scored(self):
        # Aug 28 2026 standing rule: financial-architecture
        # mapping carries no coverage-tone pair.
        data = _m900_data()
        assert data["tone_scored"] is False
        assert data["engine_run"] is False
        assert data["is_significant"] is False
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True
        assert data["artifact_grade"] is False

    def test_m900_not_falsification_member(self):
        data = _m900_data()
        assert data["falsification_family_member"] is False
        assert "NOT a member" in data["falsification_family"]
        assert "ledger holds at 41" in data["falsification_family"]
        assert _T42 not in data["falsification_family"]

    def test_m900_novelty_and_sources(self):
        data = _m900_data()
        assert "FIRST dedicated corpus mechanism" in data["novelty"]
        urls = [s["url"] for s in data["sources"]]
        assert any("forklog" in u for u in urls)
        forklog = next(s for s in data["sources"] if "forklog" in s["url"])
        assert forklog["novel"] is True

    def test_m900_six_confounders_and_counterargument(self):
        data = _m900_data()
        assert len(data["confounders"]) == 6
        strengths = [c["strength"] for c in data["confounders"]]
        assert strengths.count("STRONG") == 2
        assert strengths.count("MEDIUM") == 2
        assert strengths.count("WEAK") == 2
        assert data["counterargument"] is not None


# ---------------------------------------------------------------------------
# 7. Falsification ledger
# ---------------------------------------------------------------------------
class TestTypeDFalsificationLedger1115:
    def _profiles_text(self):
        parts = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                parts.append(
                    open(
                        os.path.join(root, f), encoding="utf-8", errors="replace"
                    ).read()
                )
        return "\n".join(parts)

    def _profiles_hits(self, needle):
        hits = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                if needle in open(p, encoding="utf-8", errors="replace").read():
                    hits.append(p)
        return hits

    def test_forty_first_member_claim_once(self):
        # The FORTY-FIRST member-claim form lives in exactly one
        # profiles file (journalists.yaml, the m899 home): the
        # falsification_family claim line plus the research_method
        # novelty prose ("...form zero-hit repo-wide pre-commit",
        # a #1113-authored self-reference, not a second member
        # claim). File-level uniqueness is the ledger convention
        # per #1113's TestLedger41.
        hits = self._profiles_hits(_T41)
        assert hits == [
            os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
        ], hits

    def test_forty_second_member_claim_absent(self):
        # No FORTY-SECOND member-claim exists anywhere in profiles/
        # (needle format-built per #715).
        text = self._profiles_text()
        assert _T42 not in text

    def test_ledger_holds_at_41(self):
        data = _m899_data()
        assert data["falsification_ledger"] == "41"
        data_900 = _m900_data()
        assert "ledger holds at 41" in data_900["falsification_family"]

    def test_thirtieth_direction_present(self):
        text = _read(os.path.join(REPO_ROOT, M900_HOME))
        assert _TW30 in text
        assert "TRACK-SEPARATED PRICING" in text

    def test_thirty_first_direction_absent(self):
        text = self._profiles_text()
        # Needle format-built per #715: the claim form must not
        # appear contiguously in this file or the #1114
        # no-thirty-first guard sweep trips on it.
        assert _TW31 not in text


# ---------------------------------------------------------------------------
# 8. Forward-looking staleness (subprocess pins, fail-by-design)
# ---------------------------------------------------------------------------
class TestTypeDForwardLookingStaleness1115:
    def _stale_run(self, path, node=None, *deselects):
        target = path if node is None else "%s::%s" % (path, node)
        cmd = [
            ".venv/bin/python",
            "-m",
            "pytest",
            target,
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

    def test_1113_novelty_max_899_pin_stale_by_design(self):
        # #1113's TestNovelty1113 pinned max numeric id 899; the
        # landed 900 (competitor-entities.yaml, top-level) trips it.
        # Designed lifecycle; recorded, not repaired.
        result = self._stale_run(B1113_FILE, "TestNovelty1113")
        assert result.returncode != 0, result.stdout[-2000:]
        assert "899" in result.stdout

    def test_1113_forward_guards_900_stale_by_design(self):
        # #1113's TestForwardGuards1113 pinned zero-900
        # (numeric/underscore/dash); this run's m900 block trips the
        # numeric guard. The underscore/dash guards HOLD green
        # (colon-form block key, designed keying) - recorded at
        # #1114, re-pinned here as the designed end-state.
        result = self._stale_run(B1113_FILE, "TestForwardGuards1113")
        assert result.returncode != 0, result.stdout[-2000:]
        assert "900" in result.stdout

    def test_1113_ledger_41_class_still_green(self):
        # The ledger holds at 41: the whole TestLedger41 class stays
        # green (FORTY-FIRST present once in journalists.yaml,
        # FORTY-SECOND absent).
        result = self._stale_run(B1113_FILE, "TestLedger41")
        assert result.returncode == 0, result.stdout[-2000:]

    def test_1114_forward_guards_901_still_green(self):
        # #1114's TestForwardGuards1114 pins zero-901
        # (numeric/underscore/dash): 901 unlanded, all green.
        result = self._stale_run(C1114_FILE, "TestForwardGuards1114")
        assert result.returncode == 0, result.stdout[-2000:]

    def test_1114_corpus_integrity_still_green(self):
        # #1114's TestCorpusIntegrity1114 pins max 900, the zero-901
        # numeric forward guard, the block key and yaml-parse-clean:
        # all hold at #1115.
        result = self._stale_run(C1114_FILE, "TestCorpusIntegrity1114")
        assert result.returncode == 0, result.stdout[-2000:]

    def test_1114_supersession_pins_still_green(self):
        # #1114's TestSupersessionPins1114 records the designed
        # end-states of the #1113 zero-900 numeric guard and the
        # #1110 no-thirtieth guards: all pins hold at #1115.
        result = self._stale_run(C1114_FILE, "TestSupersessionPins1114")
        assert result.returncode == 0, result.stdout[-2000:]

    def test_1112_novelty_max_898_pin_stale_by_design(self):
        # #1112's TestNovelty1112 pinned max 898; the landed 900
        # trips it. Already stale at #1114; re-pinned as the
        # designed end-state.
        result = self._stale_run(A1112_FILE, "TestNovelty1112")
        assert result.returncode != 0, result.stdout[-2000:]


# ---------------------------------------------------------------------------
# 9. Guard lifecycle (this file pins the new max + next number)
# ---------------------------------------------------------------------------
class TestGuardLifecycle1115:
    def test_898_899_900_landed_this_window(self):
        # All three window mechanisms landed in their commits: 898
        # at #1112 Type A, 899 at #1113 Type B, 900 at #1114 Type C.
        data_898 = _m898_data()
        data_899 = _m899_data()
        data_900 = _m900_data()
        assert data_898["mechanism_id"] == 898
        assert data_899["mechanism_id"] == 899
        assert data_900["mechanism_id"] == 900
        assert data_898["iteration"] == 1112
        assert data_899["iteration"] == 1113
        assert data_900["iteration"] == 1114

    def test_1115_file_pins_max_id_900_and_next_901(self):
        # This file is the new window-opener pinning zero-901
        # forward guards (per the fail-forward cadence: each
        # window's opener supersedes the prior file's NEXT_NUM pin).
        assert MAX_ID == 900
        assert NEXT_NUM == 901
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_next_numeric_901_in_profiles(self):
        # Forward guard: zero numeric 901 mechanism ids in
        # profiles/ - will fail by design at the run that lands
        # mechanism 901.
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_next_underscore_901_repo_wide(self):
        # Needle format-built per #715: no contiguous 901-form
        # literal may exist in this file.
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_next_dash_901_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_new_mechanisms_below_max(self):
        # No numeric mechanism id in profiles/ may exceed 900 -
        # corpus max is pinned.
        assert _max_numeric_mechanism_id() <= MAX_ID

    def test_no_thirty_first_direction_claim(self):
        # The next direction slot must be unclaimed repo-wide
        # (needle format-built per #715).
        text_parts = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                text_parts.append(
                    open(
                        os.path.join(root, f), encoding="utf-8", errors="replace"
                    ).read()
                )
        assert _TW31 not in "\n".join(text_parts)

    def test_no_forty_second_member_claim(self):
        # The next falsification slot must be unclaimed repo-wide
        # (needle format-built per #715).
        text_parts = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                text_parts.append(
                    open(
                        os.path.join(root, f), encoding="utf-8", errors="replace"
                    ).read()
                )
        assert _T42 not in "\n".join(text_parts)


# ---------------------------------------------------------------------------
# 10. Background suite verdict per #795
# ---------------------------------------------------------------------------
class TestBackgroundSuiteVerdict1115:
    def _log_stats(self):
        size = os.path.getsize(PRIOR_SUITE_LOG)
        text = _read(PRIOR_SUITE_LOG)
        return size, text.count("."), text.count("F"), text.count("E"), text

    def test_prior_suite_died_sixth_consecutive(self):
        # The #1110-launched background full suite DIED: 1874
        # bytes (1690 dots, ~2% progress), last write Sep 30
        # 23:42:00 PDT, zero summary tokens (no "passed"/"failed"
        # summary, no collected-count token), no live pytest
        # process. Per the #795 convention this is recorded as
        # DIED, not "interrupted": the run produces no usable
        # verdict.
        size, dots, fails, errors, text = self._log_stats()
        assert size == 1874, size
        assert dots == 1690, dots
        assert fails == 0, fails
        assert errors == 0, errors
        assert "passed" not in text
        assert "failed" not in text
        assert " collected " not in text
        assert "no tests ran" not in text

    def test_no_live_pytest_process(self):
        result = subprocess.run(
            ["pgrep", "-f", "pytest.*type_d_1110"],
            capture_output=True,
            text=True,
        )
        assert result.returncode != 0, (
            "a pytest process for the #1110 suite must not still be "
            "alive when its verdict is recorded"
        )

    def test_tombstone_lineage_advances_to_82nd(self):
        # SIXTH consecutive background-suite death of the new streak
        # (the 57-run streak ENDED at #1085 when the #1080 suite
        # completed). Tombstone lineage advances EIGHTY-FIRST ->
        # EIGHTY-SECOND; recorded in the #1115 iteration-log entry.
        # Deselected pre-commit (log entry is written in the
        # doc-sync step).
        text = _read(LOG_PATH)
        assert "EIGHTY-SECOND" in text


# ---------------------------------------------------------------------------
# 11. Fresh synthetic engine calibration (new values, not #1110's)
# ---------------------------------------------------------------------------
class TestSyntheticEngineCalibration1115:
    # Scratch-run values produced at this run (Thu 2026-10-01 ~04:10
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
        meta = [-0.62, -0.71, -0.58, -0.66, -0.73, -0.61, -0.69, -0.64]
        comp = [0.08, -0.02, 0.11, 0.03, -0.06, 0.09, -0.01, 0.05]
        result = calc(meta, comp)
        assert result.asymmetry_score == pytest.approx(-0.68875)
        assert result.t_statistic == pytest.approx(-24.57485621176508)
        assert result.p_value < 1e-12
        assert result.cohens_d == pytest.approx(-12.28742810588254)
        assert result.is_significant is True
        # The strong arm-swap negates the asymmetry exactly.
        swapped = calc(comp, meta)
        assert swapped.asymmetry_score == pytest.approx(
            -result.asymmetry_score
        )

    def test_null_effect_is_not_significant(self):
        calc = self._calculate()
        arm_a = [-0.05, 0.04, -0.03, 0.06, -0.04, 0.02, -0.06, 0.03]
        arm_b = [-0.04, 0.03, -0.02, 0.05, -0.03, 0.04, -0.05, 0.02]
        result = calc(arm_a, arm_b)
        assert result.asymmetry_score == pytest.approx(-0.00375)
        assert result.p_value > 0.86
        assert result.is_significant is False
        lo = result.confidence_interval_lower
        hi = result.confidence_interval_upper
        assert lo < 0 < hi

    def test_degenerate_single_tone_inputs(self):
        # Single-tone arms on the m898 illustrative pair
        # (OpenAI -0.40 vs Meta carried mean -0.375): t 0.0,
        # p 1.0, d 0.0, not significant - the degenerate contract
        # per #638/#643.
        calc = self._calculate()
        result = calc([-0.40], [-0.375])
        assert result.asymmetry_score == pytest.approx(-0.025)
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
class TestSuiteRelaunch1115:
    def test_relaunch_log_path_written(self):
        # The re-launched full suite log exists in goal hidden_files
        # (created by this run's background launch before commit).
        assert os.path.exists(SUITE_LOG), (
            "the #1115 background suite must be re-launched to "
            + SUITE_LOG
            + " before the main commit"
        )

    def test_relaunch_log_is_full_inventory(self):
        # The re-launch runs WITHOUT -x: the full inventory
        # (calendar by-design failures included) is needed for the
        # #1120 triage. The log must hold pytest progress output,
        # not just a header.
        text = _read(SUITE_LOG)
        assert text.count(".") > 100, (
            "the re-launched suite log should accumulate dot "
            "progress; got %d dots" % text.count(".")
        )

    def test_next_type_d_run_owns_the_verdict(self):
        # Per the #795 convention, the NEXT Type D run (#1120)
        # checks this suite's verdict; this run only records the
        # launch.
        assert "type_d_1115_full_suite.log" in SUITE_LOG


# ---------------------------------------------------------------------------
# 13. Doc-sync per #719 (fails pre-commit by design; passes post-sync)
# ---------------------------------------------------------------------------
class TestTypeDDocSync1115:
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
# 14. Iteration log entry
# ---------------------------------------------------------------------------
class TestTypeDIterationLog1115:
    def test_1115_entry_leads_log(self):
        # The "## #1115 Type D:" entry leads the log (newest-first
        # ordering); hashes are TBD until the anchor followup patches
        # them per #565. Deselected pre-commit per #721.
        assert _read(LOG_PATH).startswith("## #1115 Type D:")

    def test_1115_entry_names_window_and_predecessors(self):
        text = _read(LOG_PATH)
        entry = text.split("## #1114 Type C:")[0]
        assert "1115-1119" in entry
        assert "5e1151e6" in entry
        assert "EIGHTY-SECOND" in entry

    def test_1114_entry_present(self):
        # The #1114 entry is present in the log (the #1115 entry
        # prepends above it).
        assert "## #1114 Type C:" in _read(LOG_PATH)


# ---------------------------------------------------------------------------
# 15. In-flight isolation
# ---------------------------------------------------------------------------
class TestInflightIsolation1115:
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
        # This run's staged set is the #1115 test file and the
        # doc-sync files only.
        status = _git("status", "--short")
        staged = [l for l in status.splitlines() if l.startswith(("M ", "A "))]
        allowed = (
            "test_type_d_1115_",
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
