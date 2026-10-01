"""Type D -- Iteration #1110 (Wed 2026-09-30 23:00 PDT): m895/m896/m897
qualitative-discipline verification + post-1105-1109 corpus integrity
(max numeric mechanism_id 897; zero next-number 898 keys in
numeric/underscore/dash mechanism forms; underscore/dash 898 needles
are format-built per #715 so no guard-literal carrier file exists -
the m895 block key carries the underscore-form 895 mechanism key
string in profiles/nytimes.yaml, so it is built at runtime in this
file per #715; the m896/m897 block keys carry no mechanism-number
substring (designed keying per #715, colon-form only); the #1106/#1107/
#1108/#1109 window files are NOT edited by this run - their now-stale
forward-looking pins are recorded as fail-by-design via subprocess in
the staleness class (#1107's max-895 pin trips on the landed 897;
#1108's zero-897 forward guards trip on the landed 897; #1109's
post-commit class stays green); ledger holds at 39 with the
THIRTY-NINTH member-claim form present once (journalists.yaml m896
falsification_family) and the FORTIETH member-claim form absent
repo-wide (needle format-built per #715); the TWENTY-NINTH
relationship direction is present in competitor-entities.yaml (m897
FRAME-THEN-PRICE); the THIRTIETH relationship-direction claim form is
absent repo-wide (needle format-built per #715)) + the #1105
background-suite verdict (DIED at 10625 bytes / 2470 dots ~4.4% with
last write Sep 30 18:59:49 PDT and zero summary tokens, no live
pytest process - FIFTH consecutive background-suite death of the new
streak; the 57-run streak ENDED at #1085 when the #1080 suite
completed; tombstone lineage advances EIGHTIETH -> EIGHTY-FIRST) +
fresh synthetic engine calibration (new values, not #1105's) +
re-launch of the full suite as a background process writing to goal
hidden_files type_d_1110_full_suite.log WITHOUT -x (the full
inventory, calendar by-design failures included, is needed for the
#1115 triage; the next Type D run checks its verdict per the #795
convention).

Type D FIRST leg of the 1110-1114 window, OPENING it
(D->E->A->B->C). Committed predecessor #1109 Type C (22:00 PDT Sep
30) CLOSED the 1105-1109 window (D #1105, E #1106, A #1107, B #1108,
C #1109). Rotation per the #565 anchor + rotation guard.
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
- m895 (Type A #1107, nytimes.yaml 4-space block key,
  `mechanism_id: 895` field form; block key count 1 - colon-form
  line only, designed; the underscore-form 895 needle in the block
  key is format-built in this file per #715): NYT x Anthropic
  Sep-2026 S-1 canary-register arm (-0.35 MANUAL ILLUSTRATIVE,
  Sorkin DealBook Sep-29, relay-attested via implicator.ai) vs
  carried NYT x Meta arms from m835 (Connect relay +0.10,
  ICE-ban memo -0.30, carried mean -0.10, un-rescored per #807).
  Illustrative delta -0.25: the accountability register lands
  HARDER on the reported-settlement counterparty than on Meta,
  inverting the naive deal-softening read. Within-entity swing
  m835 Sep-18 +0.25 to Sep-29 -0.35 = -0.60 in 11 days - THIRD
  publication-level peg-follows-register replication (m676 FT
  -0.55/16d, m712-m877 WIRED -0.50/13d). Same-event
  third-publication leg per the m847/m856 precedent (m883 Verge
  -0.40, m892 FT -0.35, NYT m895 -0.35: max pairwise 0.05).
  NOT a falsification-family member; ledger held at 38 at
  landing, THIRTY-NINTH absent then.
- m896 (Type B #1108, journalists.yaml 4-space block key under
  nicole_nguyen competitor_coverage, `mechanism_id: 896` field
  form; block key count 2 - colon-form line + block_key field,
  designed): Nicole Nguyen (WSJ) Sep-2026 Meta Muse trust-history
  register (+0.10 MANUAL ILLUSTRATIVE, IN-CORPUS via m893 carried
  un-rescored per #807) vs FRESH Apple Siri hands-on register
  (+0.40 MANUAL ILLUSTRATIVE, mid-Sep 2026, newslocker
  relay-attested, excerpt-bounded per #503). Illustrative delta
  (Apple minus Meta) +0.30: the zero-deal entity draws the SOFTER
  trust register than the paid cooperative counterparty (Meta,
  $50M/yr News Corp licensing); deal-softness prediction FAILS
  on ordering at the journalist level a SECOND time.
  THIRTY-NINTH falsification-family member; ledger 38->39.
  Extends #693/m650 NINETEENTH lineage (Nguyen Apple +0.40
  constancy across Duo hardware and Siri assistant arms).
- m897 (Type C #1109, competitor-entities.yaml zero-indent block
  key, `mechanism_id: 897` field form; block key count 2 -
  colon-form line + block_key field, designed): Google
  AI-contribution pilot June-18-2026 origination frame (NeoTeo
  Sep 30 2026, first-hand 23-line read) vs Sep-29-30 payout
  reveal - FRAME-THEN-PRICE (announced cooperation vs operating
  unilateral pricing) as the TWENTY-NINTH relationship direction:
  the announced frame (partnership model, freshness, factuality,
  grounding) enrolls counterparties before they ever see a price;
  the operating mechanics are unilateral widget-metered
  micro-pricing on a fragmented counterparty base. Two-track
  tiering FIRST for the corpus: AI Contribution Pilot (~100
  publishers, opaque widget) SEPARATE from News AI pilot (200+
  publications, commercial partnerships). Tone NOT_SCORED per
  the Aug 28 2026 standing rule. NOT a falsification-family
  member; ledger holds at 39, FORTIETH member-claim absent.

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
    "test_type_d_1110_m895_m896_m897_qualitative_corpus_"
    "integrity_sep30_11pm.py"
)

MAX_ID = 897
NEXT_NUM = 898

# Patched by the anchor followup commit per #565 (post-main-commit).
ANCHORED_SHA = "f4f5c8446b87b3c41d313ae661d9f4073b716f1e"

# Doc-sync constants per #719 (patched post-first-run with the true
# collected count).
README_TEST_COUNT = 56678
README_FILE_COUNT = 1435

# Format-built per the #715 convention: this source file carries no
# contiguous underscore-form mechanism key literal for the landed
# window mechanisms (895) or the next number (898). The m896/m897
# block keys carry no mechanism-number substring (designed keying),
# so they are plain literals.
M895_KEY = (
    "mechanism" + "_" + "895" + "_nyt_anthropic_sep2026_"
    "ipo_register_swing_vs_meta_carried_arms"
)
M895_INDENT = 4
M895_HOME = "profiles/nytimes.yaml"
M896_KEY = (
    "type_b_1108_nicole_nguyen_wsj_siri_grows_up_"
    "vs_muse_trust_register_sep30"
)
M896_INDENT = 4
M896_HOME = "profiles/careers/journalists.yaml"
M897_KEY = (
    "type_c_1109_google_pilot_grounding_origination_"
    "framethenprice_twentyninth_direction_sep30_10pm"
)
M897_INDENT = 0
M897_HOME = "profiles/competitor-entities.yaml"

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770
MID_898 = "mechanism_id: " + "898"  # fragment-built per #715

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1110_full_suite.log"
)
PRIOR_SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1105_full_suite.log"
)
A1107_FILE = (
    "tests/test_type_a_1107_nyt_anthropic_s1_canary_register_"
    "vs_meta_carried_arms_sep30_8pm.py"
)
B1108_FILE = (
    "tests/test_type_b_1108_nicole_nguyen_wsj_siri_grows_up_"
    "vs_muse_trust_register_sep30_9pm.py"
)
C1109_FILE = (
    "tests/test_type_c_1109_google_pilot_grounding_origination_"
    "framethenprice_twentyninth_direction_sep30_10pm.py"
)

_DOC = __doc__

# The twenty-ninth/thirtieth-direction and fortieth-member needles
# are fragment-built per #715 so this file carries no contiguous
# literal of a forward-guard claim form.
_TW29 = "TWENTY-" + "NINTH relationship direction"
_TW30 = "THIRTI" + "ETH relationship direction"
_T40 = "FORTI-" + "ETH falsification-family member"
_T39 = "THIRTY-NINTH falsification-family member"


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
# numbers in git history: #1110 Type D opens the 1110-1114 window;
# #1109 Type C (committed 22:00 PDT Sep 30) is the schedule
# predecessor and CLOSED the 1105-1109 window. The in-flight runs
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
    file carries a contiguous 898-form mechanism literal (verified
    pre-commit), so the 898 sweeps run repo-wide with only this file
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


def _m895_data():
    return _block_data(M895_HOME, M895_KEY, M895_INDENT)


def _m896_data():
    return _block_data(M896_HOME, M896_KEY, M896_INDENT)


def _m897_data():
    return _block_data(M897_HOME, M897_KEY, M897_INDENT)


# ---------------------------------------------------------------------------
# 1. Novelty
# ---------------------------------------------------------------------------
class TestNovelty1110:
    def test_no_type_d_1110_test_file_preexisting(self):
        files = glob.glob(
            os.path.join(TESTS_DIR, "test_type_d_1110*.py")
        )
        assert files == [os.path.join(TESTS_DIR, OWN_BASENAME)], files

    def test_no_type_d_1110_in_git_log(self):
        # Pre-commit novelty guard: no commit may already claim this slot.
        # SUPERSEDED BY DESIGN once this run's main commit ("Type D #1110:")
        # lands; post-commit, TestTypeDRotationGuard1110 asserts the anchor
        # and window instead. Deselect this test in post-commit full runs.
        log = _git("log", "--format=%s", "--grep=Type D #1110")
        assert "Type D #1110" not in log

    def test_max_id_is_897(self):
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_898_numeric_forms_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_block_keys_unique_in_home_yamls(self):
        # m895: colon-form line only (count 1, designed - no
        # block_key field in the m895 block). m896/m897: colon-form
        # line + block_key field (count 2 each, designed).
        nyt = _read(os.path.join(REPO_ROOT, M895_HOME))
        assert nyt.count(M895_KEY) == 1, nyt.count(M895_KEY)
        jou = _read(os.path.join(REPO_ROOT, M896_HOME))
        assert jou.count(M896_KEY) == 2, jou.count(M896_KEY)
        ent = _read(os.path.join(REPO_ROOT, M897_HOME))
        assert ent.count(M897_KEY) == 2, ent.count(M897_KEY)


# ---------------------------------------------------------------------------
# 2. Rotation guard (2 tests deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestTypeDRotationGuard1110:
    def test_rotation_window_opens_1110(self):
        # FIRST leg of the 1110-1114 window, OPENING it (per #565:
        # D #1110 -> E #1111 -> A #1112 -> B #1113 -> C #1114).
        # Deselected pre-commit (this run's main commit is not yet
        # in history); passes post-commit.
        w = _window()
        assert w[0] == ("D", "1110"), w
        # Newest-first distinct sequence: D #1110 (this run) opens
        # the window after the closed 1105-1109 window (C #1109,
        # B #1108, A #1107, E #1106).
        assert [t for t, _ in w[:5]] == ["D", "C", "B", "A", "E"], w

    def test_predecessor_1109_chain_present(self):
        # #1109 Type C CLOSED the 1105-1109 window; its main/anchor/
        # log-hash chain must be in history before this run commits.
        log = _git("log", "--format=%H %s")
        assert "1819ae4c" in log
        assert "1bf29ace" in log
        assert "bfec2b24" in log

    def test_no_type_e_1111_in_git_log(self):
        log = _git("log", "--format=%s", "--grep=Type E #1111")
        assert "Type E #1111" not in log

    def test_anchor_sha_is_real(self):
        # Patched post-main-commit by the anchor followup per #565.
        # Deselected pre-commit (placeholder by design); passes
        # post-patch.
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA
        assert ANCHORED_SHA != "0" * 40


# ---------------------------------------------------------------------------
# 2b. Novelty anchor (1 test, deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestTypeDNoveltyAnchor1110:
    def test_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per #565: the main commit does not
        # exist yet. Post-commit this asserts the single #1110
        # commit is the anchor and carries the test-file changes.
        log = _git("log", "--format=%H %s", "--grep=Type D #1110")
        assert "Type D #1110" in log
        assert ANCHORED_SHA in log


# ---------------------------------------------------------------------------
# 3. Corpus integrity
# ---------------------------------------------------------------------------
class TestTypeDCorpusIntegrity1110:
    def test_m895_block_present_in_nytimes_yaml(self):
        data = _m895_data()
        assert data["mechanism_id"] == 895

    def test_m896_block_present_in_journalists_yaml(self):
        data = _m896_data()
        assert data["mechanism_id"] == 896

    def test_m897_block_present_in_competitor_entities_yaml(self):
        data = _m897_data()
        assert data["mechanism_id"] == 897

    def test_max_mechanism_id_is_897(self):
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_898_forms_repo_wide(self):
        # Forward guard: zero numeric/underscore/dash 898 keys -
        # will fail by design at the run that lands mechanism 898.
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_m895_key_count_is_designed(self):
        # Colon-form key line only: the m895 block carries no
        # block_key field, and the underscore-form 895 needle is
        # format-built in this file per #715 (no literal trip).
        text = _read(os.path.join(REPO_ROOT, M895_HOME))
        lines = [
            l
            for l in text.splitlines()
            if M895_KEY in l
        ]
        assert len(lines) == 1, lines
        assert lines[0].strip() == M895_KEY + ":"

    def test_m896_key_count_is_designed(self):
        # Colon-form key line + block_key field value: exactly 2,
        # no other carrier.
        text = _read(os.path.join(REPO_ROOT, M896_HOME))
        lines = [
            l
            for l in text.splitlines()
            if M896_KEY in l
        ]
        assert len(lines) == 2, lines
        assert lines[0].strip() == M896_KEY + ":"
        assert "block_key:" in lines[1]

    def test_m897_key_count_is_designed(self):
        # Colon-form key line + block_key field value: exactly 2,
        # no other carrier.
        text = _read(os.path.join(REPO_ROOT, M897_HOME))
        lines = [
            l
            for l in text.splitlines()
            if M897_KEY in l
        ]
        assert len(lines) == 2, lines
        assert lines[0].strip() == M897_KEY + ":"
        assert "block_key:" in lines[1]


# ---------------------------------------------------------------------------
# 4. m895 qualitative discipline (Type A #1107)
# ---------------------------------------------------------------------------
class TestTypeDM895QualitativeDiscipline:
    def test_m895_iteration_fields(self):
        data = _m895_data()
        assert data["iteration"] == 1107
        assert data["iteration_type"] == "A"
        assert data["publication"] == "The New York Times"
        assert data["type"] == "Type A: Competitor Coverage Deep Dive"
        assert data["verification"]["iteration"] == 1107

    def test_m895_scorer_values_and_delta(self):
        data = _m895_data()
        scorer = data["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["target_scores"] == [-0.35]
        assert scorer["target_avg"] == -0.35
        assert scorer["peer_scores"] == [0.10, -0.30]
        assert scorer["peer_avg"] == -0.10
        assert scorer["delta"] == -0.25
        assert scorer["delta_calc"] == "-0.35 - (-0.10) = -0.25"
        # The accountability register lands HARDER on the
        # reported-settlement counterparty than on Meta: the naive
        # deal-softening read inverts on this peg window.
        assert "harder on Anthropic than Meta" in scorer["delta_direction"]

    def test_m895_temporal_swing(self):
        data = _m895_data()
        scorer = data["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert "-0.60 in 11 days" in scorer["temporal_swing"]
        assert "third publication-level" in scorer["temporal_swing"]

    def test_m895_same_event_third_publication_leg(self):
        data = _m895_data()
        scorer = data["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        triple = scorer["cross_publication_s1_triple"]
        assert "m883" in triple and "m892" in triple and "m895" in triple
        assert "0.05" in triple

    def test_m895_anthropic_arm_register(self):
        data = _m895_data()
        arm = data["articles_anthropic"][0]
        assert arm["manual_illustrative_tone"] == -0.35
        assert arm["byline"] == "Andrew Ross Sorkin"
        assert arm["date"] == "2026-09-29"
        assert arm["register"] == "market_systemic_accountability"
        assert "implicator.ai" in arm["attestation_url"]

    def test_m895_meta_arms_carried_unrescored(self):
        data = _m895_data()
        arms = data["articles_meta_carried"]
        assert len(arms) == 2
        assert arms[0]["tone_carried"] == 0.10
        assert arms[1]["tone_carried"] == -0.30
        for arm in arms:
            assert "un-rescored per #807" in arm["source"]

    def test_m895_not_falsification_member(self):
        data = _m895_data()
        assert "NOT a falsification-family member" in data[
            "falsification_family"
        ]
        assert data["ledger"] == "38"

    def test_m895_statistical_discipline(self):
        data = _m895_data()
        disc = data["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE ONLY" in disc
        assert "engine NOT run" in disc
        assert "NOT_CALCULATED" in disc
        assert "NOT artifact-grade" in disc
        assert data["no_analysis_json_update"] is True
        assert data["correlation_not_causation"] is True

    def test_m895_research_method(self):
        data = _m895_data()
        assert "2 browser.search query sets" in data["research_method"]
        assert "0 browser.open" in data["research_method"]


# ---------------------------------------------------------------------------
# 5. m896 qualitative discipline (Type B #1108)
# ---------------------------------------------------------------------------
class TestTypeDM896QualitativeDiscipline:
    def test_m896_iteration_fields(self):
        data = _m896_data()
        assert data["mechanism_id"] == 896
        assert data["iteration"] == 1108
        assert data["type"] == "Type B: Journalist Cross-Entity Tracking"
        assert data["journalist"] == "Nicole Nguyen"
        assert data["publication"] == "wall-street-journal"
        assert data["block_key"] == M896_KEY

    def test_m896_thirty_ninth_falsification_member(self):
        data = _m896_data()
        assert _T39 in data["falsification_family"]
        assert data["falsification_ledger"] == "39"

    def test_m896_illustrative_delta_and_inversion(self):
        data = _m896_data()
        assert data["meta_arm"]["manual_illustrative_tone"] == 0.10
        assert data["apple_arm"]["manual_illustrative_tone"] == 0.40
        delta = data["illustrative_delta"]
        assert "+0.30" in delta
        # The paid counterparty draws the HARDER register: the
        # deal-softness prediction fails on ordering.
        assert "FAILS on ordering" in data["financial_context"]

    def test_m896_meta_arm_carried(self):
        data = _m896_data()
        meta = data["meta_arm"]
        assert "m893" in meta["carried_per_807"]
        assert meta["novelty"] == "IN-CORPUS arm (m893). Carried, not re-scored."

    def test_m896_apple_arm_fresh(self):
        data = _m896_data()
        apple = data["apple_arm"]
        assert apple["novelty"].startswith("FRESH arm.")
        assert "newslocker.com" in apple["url"]
        assert "Sep 16/17 2026" in apple["date_bound"]

    def test_m896_constancy_lineage_extension(self):
        data = _m896_data()
        fam = data["falsification_family"]
        assert "#1103" in fam
        assert "#693" in fam
        assert "NINETEENTH" in fam

    def test_m896_strong_confounders_present(self):
        data = _m896_data()
        texts = [c for c in data["confounders"]]
        assert any("[STRONG]" in c for c in texts)
        assert any("Factual-substrate" in c for c in texts)

    def test_m896_counterevidence_present(self):
        data = _m896_data()
        assert len(data["counterevidence"]) >= 3
        assert any("COUNTEREVIDENCE" in c for c in data["counterevidence"])

    def test_m896_statistical_discipline(self):
        data = _m896_data()
        disc = data["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE ONLY" in disc
        assert "engine NOT run" in disc
        assert "is_significant false" in disc
        assert data["no_analysis_json_update"] is True
        assert data["correlation_not_causation"] is True

    def test_m896_research_method(self):
        data = _m896_data()
        assert "7 browser.search query sets" in data["research_method"]
        assert "0 browser.open on the WSJ paywalled original" in data[
            "research_method"
        ]


# ---------------------------------------------------------------------------
# 6. m897 qualitative discipline (Type C #1109)
# ---------------------------------------------------------------------------
class TestTypeDM897QualitativeDiscipline:
    def test_m897_iteration_fields(self):
        data = _m897_data()
        assert data["mechanism_id"] == 897
        assert data["iteration"] == 1109
        assert data["iteration_type"] == "C"
        assert data["type"] == "financial_incentive_mapping"
        assert data["block_key"] == M897_KEY

    def test_m897_twenty_ninth_direction(self):
        data = _m897_data()
        assert "TWENTY-NINTH" in data["mechanism_name"]
        tax = data["relationship_direction_taxonomy"]
        assert "TWENTY-NINTH" in tax
        assert "FRAME-THEN-PRICE" in tax

    def test_m897_origination_frame_leg(self):
        data = _m897_data()
        leg = data["origination_frame_leg"]
        assert "June 18, 2026" in leg
        assert "partnership model" in leg
        assert "m891" in leg

    def test_m897_two_track_tiering(self):
        data = _m897_data()
        leg = data["two_track_architecture_leg"]
        assert "AI Contribution Pilot" in leg
        assert "News AI pilot" in leg
        assert "200+" in leg

    def test_m897_frame_shift_leg(self):
        data = _m897_data()
        leg = data["frame_shift_leg"]
        assert "pricing-power infrastructure" in leg
        assert "#27" in leg and "#28" in leg

    def test_m897_falsifiable_legs(self):
        data = _m897_data()
        tax = data["relationship_direction_taxonomy"]
        assert "Falsifiable:" in tax
        assert "(1)" in tax and "(2)" in tax and "(3)" in tax

    def test_m897_tone_not_scored(self):
        # Aug 28 2026 standing rule: financial-architecture
        # mapping carries no coverage-tone pair.
        data = _m897_data()
        assert data["tone_scored"] is False
        assert data["engine_run"] is False
        assert data["is_significant"] is False
        assert data["verdict"] == "directionally_supported_not_proven"
        assert "NOT_SCORED" in data["coverage_nexus"]

    def test_m897_not_falsification_member(self):
        data = _m897_data()
        assert data["falsification_family_member"] is False
        assert "NOT a member" in data["falsification_family"]
        assert "ledger holds at 39" in data["falsification_family"]

    def test_m897_novelty_and_sources(self):
        data = _m897_data()
        assert "TWENTY-NINTH direction" in data["novelty"]
        assert "neoteo.com" in data["sources"][0]["url"]
        assert data["sources"][0]["novel"] is True

    def test_m897_six_confounders_and_counterargument(self):
        data = _m897_data()
        assert len(data["confounders"]) == 6
        strengths = [c["strength"] for c in data["confounders"]]
        assert strengths.count("STRONG") == 2
        assert strengths.count("MEDIUM") == 2
        assert strengths.count("WEAK") == 2
        assert data["counterargument"] is not None


# ---------------------------------------------------------------------------
# 7. Falsification ledger
# ---------------------------------------------------------------------------
class TestTypeDFalsificationLedger1110:
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

    def test_thirty_ninth_member_claim_once(self):
        # The THIRTY-NINTH member-claim form is the m896
        # falsification_family line, present exactly once.
        text = self._profiles_text()
        assert text.count(_T39) == 1

    def test_fortieth_member_claim_absent(self):
        # No FORTIETH member-claim exists anywhere in profiles/
        # (needle format-built per #715).
        text = self._profiles_text()
        assert _T40 not in text

    def test_ledger_holds_at_39(self):
        data = _m896_data()
        assert data["falsification_ledger"] == "39"
        data_897 = _m897_data()
        assert "ledger holds at 39" in data_897["falsification_family"]

    def test_twenty_ninth_direction_present(self):
        text = _read(os.path.join(REPO_ROOT, M897_HOME))
        assert _TW29 in text
        assert "FRAME-THEN-PRICE" in text

    def test_thirtieth_direction_absent(self):
        text = self._profiles_text()
        # Needle format-built per #715: the claim form must not
        # appear contiguously in this file or the #1109
        # no-thirtieth guard sweep trips on it.
        assert _TW30 not in text


# ---------------------------------------------------------------------------
# 8. Forward-looking staleness (subprocess pins, fail-by-design)
# ---------------------------------------------------------------------------
class TestTypeDForwardLookingStaleness1110:
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

    def test_1107_novelty_max_895_pin_stale_by_design(self):
        # #1107's TestNovelty1107 pinned max numeric id 895; the
        # landed 897 (competitor-entities.yaml, top-level) trips it.
        # Designed lifecycle; recorded, not repaired.
        result = self._stale_run(A1107_FILE, "TestNovelty1107")
        assert result.returncode != 0, result.stdout[-2000:]
        assert "test_max_numeric_mechanism_id_is_895" in result.stdout

    def test_1107_ledger_38_class_stale_by_design(self):
        # The whole TestLedgerHoldsAt38 class is stale: the ledger
        # now holds at 39 (m896 THIRTY-NINTH landed at #1108).
        # Already pinned by #1108; re-pinned here as the designed
        # end-state.
        result = self._stale_run(A1107_FILE, "TestLedgerHoldsAt38")
        assert result.returncode != 0, result.stdout[-2000:]

    def test_1107_supersession_max_pin_stale_by_design(self):
        # #1107's TestSupersessionPins1107 pinned max 895 (not 894);
        # the corpus max is now 897.
        result = self._stale_run(
            A1107_FILE,
            "TestSupersessionPins1107::test_max_numeric_is_895_not_894",
        )
        assert result.returncode != 0, result.stdout[-2000:]

    def test_1108_forward_guards_897_stale_by_design(self):
        # #1108's TestForwardGuards1108 pinned zero-897
        # (numeric/underscore/dash); this run's m897 block trips the
        # numeric guard. Designed lifecycle; recorded, not repaired.
        result = self._stale_run(B1108_FILE, "TestForwardGuards1108")
        assert result.returncode != 0, result.stdout[-2000:]
        assert "897" in result.stdout

    def test_1109_corpus_novelty_post_commit_still_green(self):
        # #1109's TestCorpusNoveltyPostCommit pins the zero-898
        # forward guards, the 897 presence, the block key, the
        # no-thirtieth guard and the no-fortieth guard: all still
        # green at #1110 (898 unlanded). Its working-tree sweeps
        # exclude its own file; this file carries no contiguous
        # 898-form literal per #715, so nothing trips.
        result = self._stale_run(C1109_FILE, "TestCorpusNoveltyPostCommit")
        assert result.returncode == 0, result.stdout[-2000:]

    def test_1109_staleness_pins_still_green(self):
        # #1109's TestStalenessPins1109 records the designed
        # end-states of the #1108 zero-897 guards and the #1104
        # no-twenty-ninth guard: all pins hold at #1110.
        result = self._stale_run(C1109_FILE, "TestStalenessPins1109")
        assert result.returncode == 0, result.stdout[-2000:]


# ---------------------------------------------------------------------------
# 9. Guard lifecycle (this file pins the new max + next number)
# ---------------------------------------------------------------------------
class TestGuardLifecycle1110:
    def test_895_896_897_landed_this_window(self):
        # All three window mechanisms landed in their commits: 895
        # at #1107 Type A, 896 at #1108 Type B, 897 at #1109 Type C.
        data_895 = _m895_data()
        data_896 = _m896_data()
        data_897 = _m897_data()
        assert data_895["mechanism_id"] == 895
        assert data_896["mechanism_id"] == 896
        assert data_897["mechanism_id"] == 897
        assert data_895["iteration"] == 1107
        assert data_896["iteration"] == 1108
        assert data_897["iteration"] == 1109

    def test_1110_file_pins_max_id_897_and_next_898(self):
        # This file is the new window-opener pinning zero-898
        # forward guards (per the fail-forward cadence: each
        # window's opener supersedes the prior file's NEXT_NUM pin).
        assert MAX_ID == 897
        assert NEXT_NUM == 898
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_next_numeric_898_in_profiles(self):
        # Forward guard: zero numeric 898 mechanism ids in
        # profiles/ - will fail by design at the run that lands
        # mechanism 898.
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_next_underscore_898_repo_wide(self):
        # Needle format-built per #715: no contiguous 898-form
        # literal may exist in this file.
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_next_dash_898_repo_wide(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []

    def test_no_new_mechanisms_below_max(self):
        # No numeric mechanism id in profiles/ may exceed 897 -
        # corpus max is pinned.
        assert _max_numeric_mechanism_id() <= MAX_ID

    def test_no_thirtieth_direction_claim(self):
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
        assert _TW30 not in "\n".join(text_parts)

    def test_no_fortieth_member_claim(self):
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
        assert _T40 not in "\n".join(text_parts)


# ---------------------------------------------------------------------------
# 10. Background suite verdict per #795
# ---------------------------------------------------------------------------
class TestBackgroundSuiteVerdict1110:
    def _log_stats(self):
        size = os.path.getsize(PRIOR_SUITE_LOG)
        text = _read(PRIOR_SUITE_LOG)
        return size, text.count("."), text.count("F"), text.count("E"), text

    def test_prior_suite_died_fifth_consecutive(self):
        # The #1105-launched background full suite DIED: 10625
        # bytes (2470 dots, ~4.4% of the 56592 corpus), last write
        # Sep 30 18:59:49 PDT, zero summary tokens (no "passed"/
        # "failed" summary, no collected-count token), no live
        # pytest process. Per the #795 convention this is recorded
        # as DIED, not "interrupted": the run produces no usable
        # verdict.
        size, dots, fails, errors, text = self._log_stats()
        assert size == 10625, size
        assert dots == 2470, dots
        assert fails == 0, fails
        assert errors == 0, errors
        assert "passed" not in text
        assert "failed" not in text
        assert " collected " not in text
        assert "no tests ran" not in text

    def test_no_live_pytest_process(self):
        result = subprocess.run(
            ["pgrep", "-f", "pytest.*type_d_1105"],
            capture_output=True,
            text=True,
        )
        assert result.returncode != 0, (
            "a pytest process for the #1105 suite must not still be "
            "alive when its verdict is recorded"
        )

    def test_tombstone_lineage_advances_to_81st(self):
        # FIFTH consecutive background-suite death of the new streak
        # (the 57-run streak ENDED at #1085 when the #1080 suite
        # completed). Tombstone lineage advances EIGHTIETH ->
        # EIGHTY-FIRST; recorded in the #1110 iteration-log entry.
        # Deselected pre-commit (log entry is written in the
        # doc-sync step).
        text = _read(LOG_PATH)
        assert "EIGHTY-FIRST" in text


# ---------------------------------------------------------------------------
# 11. Fresh synthetic engine calibration (new values, not #1105's)
# ---------------------------------------------------------------------------
class TestSyntheticEngineCalibration1110:
    # Scratch-run values produced at this run (Wed 2026-09-30 ~23:05
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
        meta = [-0.71, -0.64, -0.58, -0.69, -0.62, -0.66, -0.60, -0.68]
        comp = [0.05, -0.03, 0.09, -0.01, 0.07, -0.05, 0.03, 0.00]
        result = calc(meta, comp)
        assert result.asymmetry_score == pytest.approx(-0.66625)
        assert result.t_statistic == pytest.approx(-28.03045558213844)
        assert result.p_value < 1e-12
        assert result.cohens_d == pytest.approx(-14.015227791069224)
        assert result.is_significant is True
        # The strong arm-swap negates the asymmetry exactly.
        swapped = calc(comp, meta)
        assert swapped.asymmetry_score == pytest.approx(
            -result.asymmetry_score
        )

    def test_null_effect_is_not_significant(self):
        calc = self._calculate()
        arm_a = [-0.04, 0.03, -0.05, 0.02, -0.03, 0.04, -0.02, 0.05]
        arm_b = [-0.03, 0.02, -0.04, 0.03, -0.02, 0.05, -0.01, 0.04]
        result = calc(arm_a, arm_b)
        assert result.asymmetry_score == pytest.approx(-0.005)
        assert result.p_value > 0.79
        assert result.is_significant is False
        lo = result.confidence_interval_lower
        hi = result.confidence_interval_upper
        assert lo < 0 < hi

    def test_degenerate_single_tone_inputs(self):
        # Single-tone arms on the m895 illustrative pair
        # (Anthropic -0.35 vs Meta carried mean -0.10): t 0.0,
        # p 1.0, d 0.0, not significant - the degenerate contract
        # per #638/#643.
        calc = self._calculate()
        result = calc([-0.35], [-0.10])
        assert result.asymmetry_score == pytest.approx(-0.25)
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
class TestSuiteRelaunch1110:
    def test_relaunch_log_path_written(self):
        # The re-launched full suite log exists in goal hidden_files
        # (created by this run's background launch before commit).
        assert os.path.exists(SUITE_LOG), (
            "the #1110 background suite must be re-launched to "
            + SUITE_LOG
            + " before the main commit"
        )

    def test_relaunch_log_is_full_inventory(self):
        # The re-launch runs WITHOUT -x: the full inventory
        # (calendar by-design failures included) is needed for the
        # #1115 triage. The log must hold pytest progress output,
        # not just a header.
        text = _read(SUITE_LOG)
        assert text.count(".") > 100, (
            "the re-launched suite log should accumulate dot "
            "progress; got %d dots" % text.count(".")
        )

    def test_next_type_d_run_owns_the_verdict(self):
        # Per the #795 convention, the NEXT Type D run (#1115)
        # checks this suite's verdict; this run only records the
        # launch.
        assert "type_d_1110_full_suite.log" in SUITE_LOG


# ---------------------------------------------------------------------------
# 13. Doc-sync per #719 (fails pre-commit by design; passes post-sync)
# ---------------------------------------------------------------------------
class TestTypeDDocSync1110:
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
class TestTypeDIterationLog1110:
    def test_1110_entry_leads_log(self):
        # The "## #1110 Type D:" entry leads the log (newest-first
        # ordering); hashes are TBD until the anchor followup patches
        # them per #565. Deselected pre-commit per #721.
        assert _read(LOG_PATH).startswith("## #1110 Type D:")

    def test_1110_entry_names_window_and_predecessors(self):
        text = _read(LOG_PATH)
        entry = text.split("## #1109 Type C:")[0]
        assert "1110-1114" in entry
        assert "bfec2b24" in entry
        assert "EIGHTY-FIRST" in entry

    def test_1109_entry_present(self):
        # The #1109 entry is present in the log (the #1110 entry
        # prepends above it).
        assert "## #1109 Type C:" in _read(LOG_PATH)


# ---------------------------------------------------------------------------
# 15. In-flight isolation
# ---------------------------------------------------------------------------
class TestInflightIsolation1110:
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
        # This run's staged set is the #1110 test file and the
        # doc-sync files only.
        status = _git("status", "--short")
        staged = [l for l in status.splitlines() if l.startswith(("M ", "A "))]
        allowed = (
            "test_type_d_1110_",
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
