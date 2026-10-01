"""Type D -- Iteration #1105 (Wed 2026-09-30 18:00 PDT): m892/m893/m894
qualitative-discipline verification + post-1100-1104 corpus integrity
(max numeric mechanism_id 894; zero next-number 895 keys in
numeric/underscore/dash mechanism forms; underscore/dash 895 needles
are format-built per #715 so no guard-literal carrier file exists -
the repo-wide 895 sweep is pure zero on source files (the local
tests/__pycache__ .pyc artifacts carry concatenated needle strings
from their own guards; untracked build artifacts, excluded per the
#715 pattern-rescope lesson); the m892/m893/m894 block keys are
fragment-built or literal-only per the #1091 carrier-sweep
precedent - the m892 block key carries the underscore-form 892
mechanism key string in profiles/financial-times.yaml, so it is
built at runtime in this file per #715; the #1101/#1102/#1103 window
files are NOT edited by this run - their now-stale forward-looking
numeric guards are pinned as fail-by-design via subprocess in the
staleness class; ledger holds at 38 with the THIRTY-EIGHTH
member-claim form present once (journalists.yaml m893
falsification_family) and the THIRTY-NINTH member-claim form absent
in profiles/ (the THIRTY-NINTH hits are negative-guard notes,
designed); TWENTY-SEVENTH relationship direction present in
competitor-entities.yaml (m891 UNILATERAL PRICING
relationship_direction_taxonomy); TWENTY-EIGHTH relationship
direction present in competitor-entities.yaml (m894
DIVIDE-AND-CONQUER relationship_direction_taxonomy); the
TWENTY-NINTH relationship-direction claim form is absent
repo-wide) + the #1100 background-suite verdict (DIED at 1745 bytes /
1577 dots ~2.8% with last write Sep 30 13:41:29 PDT and zero summary
tokens, no live pytest process - FOURTH consecutive
background-suite death of the new streak; the 57-run streak ENDED at
#1085 when the #1080 suite completed; tombstone lineage advances
SEVENTY-NINTH -> EIGHTIETH) + fresh synthetic engine calibration
(new values, not #1100's) + re-launch of the full suite as a
background process writing to goal hidden_files
type_d_1105_full_suite.log WITHOUT -x (the full inventory, calendar
by-design failures included, is needed for the #1110 triage; the next
Type D run checks its verdict per the #795 convention).

Type D FIRST leg of the 1105-1109 window, OPENING it
(D->E->A->B->C). Committed predecessor #1104 Type C (17:00 PDT Sep
30) CLOSED the 1100-1104 window (D #1100, E #1101, A #1102, B #1103,
C #1104). Rotation per the #565 anchor + rotation guard.
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
- m892 (Type A #1102, financial-times.yaml 4-space block key,
  `mechanism_id: 892` field form; block key count 1 - colon-form
  line only, designed; the underscore-form 892 needle in the block
  key is format-built in this file per #715): FT x Anthropic
  Sep-2026 S-1 existential-risk register vs carried FT x Meta arms
  from m625 (un-rescored per #807). MANUAL ILLUSTRATIVE Anthropic
  Sep mean -0.225 vs Meta carried mean -0.285, delta +0.06
  near-null parity (the FT applies the accountability register to
  the $0-tie lab and Meta in the same register band); A1-only
  read -0.35 vs the Verge S-1 register -0.40 (m883) = 0.05
  cross-publication near-parity at two null-tie outlets;
  within-entity swing m676 +0.20 to -0.35 = -0.55 in 16 days,
  register follows the peg not the tie; m883 same-event
  second-publication leg pairing per the m847/m856 precedent.
  NOT a falsification-family member.
- m893 (Type B #1103, journalists.yaml 4-space block key under
  nicole_nguyen competitor_coverage, `mechanism_id: 893` field
  form): Nicole Nguyen (WSJ) Sep-2026 Meta Muse trust-history
  register (+0.10 MANUAL ILLUSTRATIVE, excerpt-tier) vs Jul-16-2026
  Anthropic Claude password-agent functional-caution register
  (+0.20, Claude-facing split documented in this mechanism for the
  first time, per #522 the Perplexity-facing register was -0.4).
  Illustrative delta (Anthropic minus Meta) +0.10: the paid
  cooperative counterparty (Meta, $50M/yr News Corp licensing)
  draws the HARDER trust register than the zero-cooperative-deal
  entity (Anthropic); deal-softness prediction FAILS on ordering
  at the journalist level. THIRTY-EIGHTH falsification-family
  member; ledger 37->38. Extends the #693/m650 NINETEENTH
  constancy lineage to the AI-agent review genre.
- m894 (Type C #1104, competitor-entities.yaml zero-indent block
  key, `mechanism_id: 894` field form): Google AI-answer payment
  pilot divide-and-conquer (The Decoder Sep 30 2026, first-hand)
  - DIVIDE-AND-CONQUER (fragmented-counterparty pricing) as the
  TWENTY-EIGHTH relationship direction: the payer defeats
  counterparty pricing power not by setting a low price (that is
  #27 UNILATERAL PRICING, m891) but by structuring every
  economic transfer as bilateral and individual, so publishers
  negotiate separately rather than collectively and no market
  price can form; substitutability ("other sources fill the gap")
  makes any individual holdout worthless. Tone NOT_SCORED.
  NOT a falsification-family member.

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
    "test_type_d_1105_m892_m893_m894_qualitative_corpus_"
    "integrity_sep30_6pm.py"
)

MAX_ID = 894
NEXT_NUM = 895

# Patched by the anchor followup commit per #565 (post-main-commit).
ANCHORED_SHA = "2161fb382ad7bc5ac177aa63b5b0b6051a919c53"  # patched by the anchor followup commit per #565

# Doc-sync constants per #719 (patched post-first-run with the true
# collected count).
README_TEST_COUNT = 56327
README_FILE_COUNT = 1430

# Format-built per the #715 convention: this source file carries no
# contiguous underscore-form mechanism key literal for the landed
# window mechanisms (892) or the next number (895).
M892_KEY = (
    "mechanism" + "_" + "892" + "_ft_anthropic_s1_existential_risk_"
    "register_vs_meta_carried_arms_sep30"
)
M892_INDENT = 4
M892_HOME = "profiles/financial-times.yaml"
M893_KEY = (
    "type_b_1103_nicole_nguyen_wsj_muse_trust_history_"
    "vs_claude_password_agent_functional_caution_sep30"
)
M893_INDENT = 4
M893_HOME = "profiles/careers/journalists.yaml"
M894_KEY = (
    "type_c_1104_google_ai_answer_pilot_divide_and_conquer_"
    "twentyeighth_direction_sep30_5pm"
)
M894_INDENT = 0
M894_HOME = "profiles/competitor-entities.yaml"

MECH_ID_MARKER = "mechanism" + "_"  # built at runtime per #770

SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1105_full_suite.log"
)
PRIOR_SUITE_LOG = os.path.expanduser(
    "~/workspace/goals/mediascope-meta-wearables-press-analysis/"
    "hidden_files/type_d_1100_full_suite.log"
)
A1102_FILE = (
    "tests/test_type_a_1102_ft_anthropic_s1_existential_risk_"
    "register_vs_meta_carried_arms_sep30_3pm.py"
)
B1103_FILE = (
    "tests/test_type_b_1103_nicole_nguyen_wsj_muse_trust_history_"
    "vs_claude_password_agent_functional_caution_sep30_4pm.py"
)
C1104_FILE = (
    "tests/test_type_c_1104_google_ai_answer_pilot_divide_and_conquer_"
    "twentyeighth_direction_sep30_5pm.py"
)

_DOC = __doc__

# The twenty-eighth-direction needle is fragment-built per #715 so
# this file carries no contiguous literal.
_TW28 = "TWENTY-" + "EIGHTH relationship direction"


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
# numbers in git history: #1105 Type D opens the 1105-1109 window;
# #1104 Type C (committed 17:00 PDT Sep 30) is the schedule
# predecessor and CLOSED the 1100-1104 window. The in-flight runs
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
    file carries a contiguous 895-form mechanism literal (verified
    pre-commit), so the 895 sweeps run repo-wide with only this file
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


def _m892_data():
    return _block_data(M892_HOME, M892_KEY, M892_INDENT)


def _m893_data():
    return _block_data(M893_HOME, M893_KEY, M893_INDENT)


def _m894_data():
    return _block_data(M894_HOME, M894_KEY, M894_INDENT)


# ---------------------------------------------------------------------------
# 1. Novelty
# ---------------------------------------------------------------------------
class TestNovelty1105:
    def test_no_type_d_1105_test_file_preexisting(self):
        assert glob.glob(os.path.join(TESTS_DIR, "test_type_d_1105*.py")) == [
            os.path.join(TESTS_DIR, OWN_BASENAME)
        ], "only this file may match the test_type_d_1105 glob"

    def test_no_type_d_1105_in_git_log(self):
        # Pre-commit novelty guard: no commit may already claim this slot.
        # SUPERSEDED BY DESIGN once this run's main commit ("Type D #1105:")
        # lands; post-commit, TestTypeDRotationGuard1105 asserts the anchor
        # and window instead. Deselect this test in post-commit full runs.
        log = _git("log", "--format=%s", "--grep=Type D #1105")
        assert "Type D #1105" not in log

    def test_max_id_is_894(self):
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_895_numeric_forms_in_profiles(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_block_keys_unique_in_home_yamls(self):
        # Each block key appears exactly once in colon-form at its
        # designed indent (no block_key: repeat checks here - the
        # count-design classes below pin the exact multiplicities).
        for home, key, indent in (
            (M892_HOME, M892_KEY, M892_INDENT),
            (M893_HOME, M893_KEY, M893_INDENT),
            (M894_HOME, M894_KEY, M894_INDENT),
        ):
            text = _read(os.path.join(REPO_ROOT, home))
            assert text.count("\n" + " " * indent + key + ":") == 1, (
                home,
                key,
            )


# ---------------------------------------------------------------------------
# 2. Rotation guard
# ---------------------------------------------------------------------------
class TestTypeDRotationGuard1105:
    def test_rotation_window_opens_1105(self):
        # FIRST leg of the 1105-1109 window, OPENING it (per #565:
        # D #1105 -> E #1106 -> A #1107 -> B #1108 -> C #1109).
        # Deselected pre-commit (this run's main commit is not yet
        # in history); passes post-commit.
        w = _window()
        assert w[0] == ("D", "1105"), w
        # Newest-first distinct sequence: D #1105 (this run) opens the
        # window after the closed 1100-1104 window (C #1104, B #1103,
        # A #1102, E #1101).
        assert [t for t, _ in w[:5]] == ["D", "C", "B", "A", "E"], w

    def test_predecessor_1104_chain_present(self):
        # #1104 Type C CLOSED the 1100-1104 window; its main/anchor/
        # log-hash chain must be in history before this run commits.
        log = _git("log", "--format=%H %s")
        assert "9bb80079" in log
        assert "041b62f1" in log
        assert "35ea0fcc" in log

    def test_no_type_e_1106_in_git_log(self):
        log = _git("log", "--format=%s", "--grep=Type E #1106")
        assert "Type E #1106" not in log

    def test_anchor_sha_is_real(self):
        # Patched post-main-commit by the anchor followup per #565.
        # Deselected pre-commit (placeholder by design); passes
        # post-patch.
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA
        assert ANCHORED_SHA != "0" * 40


# ---------------------------------------------------------------------------
# 3. Corpus integrity
# ---------------------------------------------------------------------------
class TestTypeDCorpusIntegrity1105:
    def test_m892_block_present_in_financial_times_yaml(self):
        data = _m892_data()
        assert data["mechanism_id"] == 892
        assert data["iteration"] == 1102

    def test_m893_block_present_in_journalists_yaml(self):
        data = _m893_data()
        assert data["mechanism_id"] == 893
        assert data["iteration"] == 1103
        assert data["journalist"] == "Nicole Nguyen"

    def test_m894_block_present_in_competitor_entities_yaml(self):
        data = _m894_data()
        assert data["mechanism_id"] == 894
        assert data["iteration"] == 1104

    def test_max_mechanism_id_is_894(self):
        assert _max_numeric_mechanism_id() == 894

    def test_zero_895_forms_repo_wide(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_m892_key_count_is_designed(self):
        # The m892 block key appears exactly once (colon-form line)
        # at indent 4 in financial-times.yaml; the underscore-form
        # 892 needle inside it is the designed keying note, kept out
        # of this file's literals per #715.
        text = _read(os.path.join(REPO_ROOT, M892_HOME))
        key_lines = [
            l
            for l in text.splitlines()
            if l.strip() == M892_KEY + ":"
        ]
        assert len(key_lines) == 1
        assert all(
            len(l) - len(l.lstrip(" ")) == M892_INDENT for l in key_lines
        )

    def test_m893_key_count_is_designed(self):
        text = _read(os.path.join(REPO_ROOT, M893_HOME))
        key_lines = [
            l
            for l in text.splitlines()
            if l.strip() == M893_KEY + ":"
        ]
        assert len(key_lines) == 1
        assert all(
            len(l) - len(l.lstrip(" ")) == M893_INDENT for l in key_lines
        )

    def test_m894_key_count_is_designed(self):
        text = _read(os.path.join(REPO_ROOT, M894_HOME))
        key_lines = [
            l
            for l in text.splitlines()
            if l.strip() == M894_KEY + ":"
        ]
        assert len(key_lines) == 1
        assert all(
            len(l) - len(l.lstrip(" ")) == M894_INDENT for l in key_lines
        )

# ---------------------------------------------------------------------------
# 4. m892 qualitative discipline (Type A #1102, FT x Anthropic S-1)
# ---------------------------------------------------------------------------
class TestTypeDM892QualitativeDiscipline:
    def test_m892_iteration_fields(self):
        data = _m892_data()
        assert data["mechanism_id"] == 892
        assert data["date_analyzed"] == "2026-09-30"
        assert data["iteration"] == 1102
        assert data["iteration_type"] == "A"

    def test_m892_scorer_values_and_delta(self):
        data = _m892_data()
        scorer = data["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["target_scores"] == [-0.35, -0.1]
        assert abs(scorer["target_avg"] - (-0.225)) < 1e-9
        assert abs(scorer["peer_avg"] - (-0.285)) < 1e-9
        assert abs(scorer["delta"] - 0.06) < 1e-9
        assert "+0.06" in scorer["delta_calc"]
        assert "Aug 28 2026" in scorer["scorer"]

    def test_m892_m676_family_extension(self):
        # m676 Sep-13 +0.20 (constructive, company-briefed) to Sep-29
        # -0.35 (accountability) = -0.55 in 16 days: the register
        # follows the peg, not the tie.
        data = _m892_data()
        pair = data["competitor_pair"]
        assert "m676" in pair
        assert "m883" in pair
        assert "same-event second-publication leg" in pair
        assert "m676" in data["finding"]
        assert "m883" in data["finding"]

    def test_m892_register_entities(self):
        data = _m892_data()
        assert "Anthropic vs Meta" in data["competitor_pair"]

    def test_m892_not_falsification_member(self):
        data = _m892_data()
        assert "NOT a falsification-family member" in data[
            "falsification_family"
        ]
        assert "THIRTY-EIGHTH" in data["falsification_family"]

    def test_m892_statistical_discipline(self):
        data = _m892_data()
        disc = data["statistical_discipline"]
        for marker in (
            "MANUAL ILLUSTRATIVE ONLY",
            "NOT_CALCULATED",
            "verdict directionally_supported_not_proven",
        ):
            assert marker in disc, marker
        assert data["no_analysis_json_update"] is True
        assert data["correlation_not_causation"] is not None

    def test_m892_research_method(self):
        data = _m892_data()
        assert "zero-hit repo-wide pre-commit" in data["novelty"]


# ---------------------------------------------------------------------------
# 5. m893 qualitative discipline (Type B #1103, Nicole Nguyen WSJ)
# ---------------------------------------------------------------------------
class TestTypeDM893QualitativeDiscipline:
    def test_m893_iteration_fields(self):
        data = _m893_data()
        assert data["mechanism_id"] == 893
        assert data["date_analyzed"] == "2026-09-30"
        assert data["iteration"] == 1103
        assert data["type"] == "Type B: Journalist Cross-Entity Tracking"

    def test_m893_thirty_eighth_falsification_member(self):
        data = _m893_data()
        assert "THIRTY-EIGHTH falsification-family member" in data[
            "falsification_family"
        ]
        assert data["falsification_ledger"] == "38"

    def test_m893_illustrative_delta_and_inversion(self):
        # +0.20 (Anthropic) minus +0.10 (Meta) = +0.10: the paid
        # cooperative counterparty draws the HARDER trust register;
        # the deal-softness prediction FAILS on ordering.
        data = _m893_data()
        delta = data["illustrative_delta"]
        assert "+0.10" in delta
        assert "HARDER trust register" in delta
        assert data["meta_arm"]["manual_illustrative_tone"] == 0.10

    def test_m893_register_split_first_documented(self):
        # The Claude-facing register split is documented for the
        # first time here; the Perplexity-facing register (-0.4) was
        # in-corpus per #522.
        data = _m893_data()
        assert "didn't do anything nefarious" in data["anthropic_arm"][
            "register_summary"
        ]
        assert "#522" in data["novelty"]

    def test_m893_constancy_lineage_extension(self):
        # Extends the #693/m650 NINETEENTH constancy lineage to the
        # AI-agent review genre.
        data = _m893_data()
        assert "NINETEENTH" in data["novelty"]
        assert "m650" in data["novelty"]

    def test_m893_statistical_discipline(self):
        data = _m893_data()
        disc = data["statistical_discipline"]
        for marker in (
            "MANUAL ILLUSTRATIVE ONLY",
            "NOT_CALCULATED",
            "NOT artifact-grade",
        ):
            assert marker in disc, marker
        assert data["no_analysis_json_update"] is True
        assert data["correlation_not_causation"] is not None

    def test_m893_research_method(self):
        data = _m893_data()
        assert "0 browser.open this run" in data["research_method"]
        assert "excerpt/relay-bounded per #503" in data["research_method"]


# ---------------------------------------------------------------------------
# 6. m894 qualitative discipline (Type C #1104, divide-and-conquer)
# ---------------------------------------------------------------------------
class TestTypeDM894QualitativeDiscipline:
    def test_m894_iteration_fields(self):
        data = _m894_data()
        assert data["mechanism_id"] == 894
        assert data["iteration"] == 1104
        assert data["type_label"] == "Financial Incentive Mapping"

    def test_m894_twenty_eighth_direction(self):
        # DIVIDE-AND-CONQUER (fragmented-counterparty pricing) as the
        # TWENTY-EIGHTH relationship direction per the m807
        # enumeration; distinct from #27 UNILATERAL PRICING (m891).
        data = _m894_data()
        taxonomy = data["relationship_direction_taxonomy"]
        assert "TWENTY-EIGHTH relationship direction" in taxonomy
        assert "DIVIDE-AND-CONQUER" in taxonomy
        assert "fragmented-counterparty pricing" in taxonomy
        assert "unilateral pricing m891" in taxonomy

    def test_m894_substitution_geometry(self):
        data = _m894_data()
        assert "other sources fill the gap" in data[
            "substitution_geometry_leg"
        ]

    def test_m894_falsifiable_legs(self):
        data = _m894_data()
        taxonomy = data["relationship_direction_taxonomy"]
        for leg in (
            "collective AI-answer licensing vehicle",
            "own-content theory goes wide",
            "bilateral holdout deals price materially above",
        ):
            assert leg in taxonomy, leg

    def test_m894_tone_not_scored(self):
        data = _m894_data()
        assert data["tone_scored"] is False
        assert data["artifact_grade"] is False
        assert data["engine_run"] is False
        assert data["verdict"] == "directionally_supported_not_proven"
        assert data["no_analysis_json_update"] is True

    def test_m894_not_falsification_member(self):
        data = _m894_data()
        assert "NOT a member" in data["falsification_family"]
        assert "ledger holds at 38" in data["falsification_family"]
        assert "THIRTY-NINTH member-claim form absent repo-wide" in data[
            "falsification_family"
        ]

    def test_m894_novelty_and_sources(self):
        data = _m894_data()
        assert "first-hand opened this run" in data["novelty"]
        assert "4 novel URLs, all zero-hit repo-wide pre-commit" in data[
            "novelty"
        ]
        assert len(data["sources"]) == 4

    def test_m894_m737_tension_carried(self):
        # The m737 taxonomy-count tension note is carried, not
        # resolved.
        data = _m894_data()
        assert "m737" in data["relationship_direction_taxonomy"]
        assert "Not resolved this run" in data[
            "relationship_direction_taxonomy"
        ]

# ---------------------------------------------------------------------------
# 7. Falsification ledger
# ---------------------------------------------------------------------------
class TestTypeDFalsificationLedger1105:
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

    def test_thirty_eighth_member_claim_once(self):
        # The THIRTY-EIGHTH member-claim form is the m893
        # falsification_family line, present exactly once.
        text = self._profiles_text()
        assert text.count("THIRTY-EIGHTH falsification-family member") == 1

    def test_thirty_ninth_member_claim_absent(self):
        # No THIRTY-NINTH member-claim exists; the only
        # THIRTY-NINTH hits are negative-guard wordings (designed).
        text = self._profiles_text()
        assert text.count("THIRTY-NINTH member-claim form absent") >= 1
        assert "THIRTY-NINTH falsification-family member" not in text

    def test_ledger_holds_at_38(self):
        data = _m893_data()
        assert data["falsification_ledger"] == "38"
        data_894 = _m894_data()
        assert "ledger holds at 38" in data_894["falsification_family"]

    def test_twenty_eighth_direction_present(self):
        text = _read(os.path.join(REPO_ROOT, M894_HOME))
        assert "TWENTY-EIGHTH relationship direction" in text
        assert "DIVIDE-AND-CONQUER" in text

    def test_twenty_ninth_direction_absent(self):
        text = self._profiles_text()
        # Needle format-built per #715: the claim form must not
        # appear contiguously in this file or the #1104 zero-slot
        # guard sweep (which covers committed tests/) trips on it.
        assert ("TWENTY-" + "NINTH relationship direction") not in text


# ---------------------------------------------------------------------------
# 8. Forward-looking staleness (subprocess pins, fail-by-design)
# ---------------------------------------------------------------------------
class TestTypeDForwardLookingStaleness1105:
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

    def test_1102_max_892_guards_failed_by_design(self):
        # The #1102 Type A file's max-892 guards must FAIL in a
        # subprocess: mechanisms 893 (#1103) and 894 (#1104) have
        # landed since, so max numeric mechanism_id is 894.
        result = self._stale_run(
            A1102_FILE,
            "TestRotationGuard1102",
            "TestNoveltyAnchor1102",
            "TestMechanism892Structure",
            "TestMechanism892AnthropicArms",
            "TestMechanism892MetaArms",
            "TestFinancialRelationship892",
            "TestMechanism892Scorer",
            "TestMechanism892Discipline",
            "TestLedgerHoldsAt37",
            "TestDocSync1102",
            "TestIterationLog1102",
            "TestInFlightIsolation1102",
        )
        assert result.returncode != 0
        failed = self._failed(result)
        for name in (
            "TestNovelty1102::test_max_numeric_mechanism_id_is_892",
            "TestSupersessionPins1102::test_max_numeric_is_892_not_891",
        ):
            assert any(name in line for line in failed), (name, failed)

    def test_1103_max_893_guards_failed_by_design(self):
        # The #1103 Type B file's max-893 guard must FAIL in a
        # subprocess: mechanism 894 landed at #1104 Type C.
        result = self._stale_run(
            B1103_FILE,
            "TestRotationGuard1103",
            "TestNoveltyAnchor1103",
            "TestMechanism893Structure",
            "TestMetaArm1103",
            "TestAnthropicArm1103",
            "TestFinancialGeometry1103",
            "TestStatisticalDiscipline1103",
            "TestFalsificationLedger1103",
            "TestDocSync1103",
            "TestIterationLog1103",
            "TestInFlightIsolation1103",
        )
        assert result.returncode != 0
        failed = self._failed(result)
        name = "TestNovelty1103::test_max_numeric_mechanism_id_is_893"
        assert any(name in line for line in failed), (name, failed)

    def _class_run(self, path, cls):
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

    def test_1104_zero_895_guards_still_pass(self):
        # The #1104 Type C file's zero-895 forward guards must still
        # PASS: mechanism 895 has not landed. They fail BY DESIGN
        # when the next A/B/C leg lands it. (Runs the post-commit
        # novelty class only - the pre-commit guards are designed
        # to fail after the #1104 main commit landed.)
        result = self._class_run(C1104_FILE, "TestCorpusNoveltyPostCommit")
        assert result.returncode == 0, result.stdout[-2000:]

    def test_1105_zero_895_needles_pass_here(self):
        # This run pins the zero-895 forward guards (they fail BY
        # DESIGN when mechanism 895 lands at a future A/B/C leg of
        # the 1105-1109 window).
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []


# ---------------------------------------------------------------------------
# 9. Guard lifecycle: mechanisms 892/893/894 land this window
# ---------------------------------------------------------------------------
class TestGuardLifecycle1105:
    def test_892_893_894_landed_this_window(self):
        # All three window mechanisms landed in their commits: 892 at
        # #1102 Type A, 893 at #1103 Type B, 894 at #1104 Type C.
        data_892 = _m892_data()
        data_893 = _m893_data()
        data_894 = _m894_data()
        assert data_892["mechanism_id"] == 892
        assert data_893["mechanism_id"] == 893
        assert data_894["mechanism_id"] == 894
        assert data_892["iteration"] == 1102
        assert data_893["iteration"] == 1103
        assert data_894["iteration"] == 1104

    def test_1105_file_pins_max_id_894_and_next_895(self):
        # This file is the new window-opener pinning zero-895
        # forward guards (per the fail-forward cadence: each
        # window's opener supersedes the prior file's NEXT_NUM pin).
        assert MAX_ID == 894
        assert NEXT_NUM == 895
        assert _max_numeric_mechanism_id() == MAX_ID

    def test_zero_next_numeric_895_in_profiles(self):
        # Forward guard: zero numeric 895 mechanism ids in
        # profiles/ - will fail by design at the run that lands
        # mechanism 895.
        assert _repo_grep_numeric_mechanism_id(895) == []

    def test_no_new_mechanisms_below_max(self):
        # No numeric mechanism id in profiles/ may exceed 894 -
        # corpus max is pinned.
        assert _max_numeric_mechanism_id() <= 894


# ---------------------------------------------------------------------------
# 10. Background suite verdict per #795
# ---------------------------------------------------------------------------
class TestBackgroundSuiteVerdict1105:
    def _log_stats(self):
        size = os.path.getsize(PRIOR_SUITE_LOG)
        text = _read(PRIOR_SUITE_LOG)
        return size, text.count("."), text.count("F"), text.count("E"), text

    def test_prior_suite_died_fourth_consecutive(self):
        # The #1100-launched background full suite DIED: 1745 bytes
        # (1577 dots, ~2.8% of the 56255 corpus), last write Sep 30
        # 13:41:29 PDT, zero summary tokens (no "passed"/"failed"
        # summary, no collected-count token), no live pytest process.
        # Per the #795 convention this is recorded as DIED, not
        # "interrupted": the run produces no usable verdict.
        size, dots, fails, errors, text = self._log_stats()
        assert size == 1745, size
        assert dots == 1577, dots
        assert fails == 0, fails
        assert errors == 0, errors
        assert "passed" not in text
        assert "failed" not in text
        assert " collected " not in text
        assert "no tests ran" not in text

    def test_no_live_pytest_process(self):
        result = subprocess.run(
            ["pgrep", "-f", "pytest.*type_d_1100"],
            capture_output=True,
            text=True,
        )
        assert result.returncode != 0, (
            "a pytest process for the #1100 suite must not still be "
            "alive when its verdict is recorded"
        )

    def test_tombstone_lineage_advances_to_80th(self):
        # FOURTH consecutive background-suite death of the new streak
        # (the 57-run streak ENDED at #1085 when the #1080 suite
        # completed). Tombstone lineage advances SEVENTY-NINTH ->
        # EIGHTIETH; recorded in the #1105 iteration-log entry.
        # Deselected pre-commit (log entry is written in the
        # doc-sync step).
        text = _read(LOG_PATH)
        assert "EIGHTIETH" in text


# ---------------------------------------------------------------------------
# 11. Fresh synthetic engine calibration (new values, not #1100's)
# ---------------------------------------------------------------------------
class TestSyntheticEngineCalibration1105:
    # Scratch-run values produced at this run (Wed 2026-09-30 ~18:05
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
        meta = [-0.62, -0.57, -0.52, -0.60, -0.55, -0.58, -0.53, -0.61]
        comp = [0.02, -0.08, 0.06, -0.04, 0.08, -0.02, 0.10, -0.06]
        result = calc(meta, comp)
        assert result.asymmetry_score == pytest.approx(-0.58)
        assert result.t_statistic == pytest.approx(-21.305805532708458)
        assert result.p_value < 1e-9
        assert result.cohens_d == pytest.approx(-10.652902766354229)
        assert result.is_significant is True
        # The strong arm-swap negates the asymmetry exactly.
        swapped = calc(comp, meta)
        assert swapped.asymmetry_score == pytest.approx(
            -result.asymmetry_score
        )

    def test_null_effect_is_not_significant(self):
        calc = self._calculate()
        arm_a = [-0.03, 0.04, -0.02, 0.05, -0.04, 0.03, -0.05, 0.02]
        arm_b = [-0.02, 0.03, -0.01, 0.06, -0.05, 0.04, -0.04, 0.01]
        result = calc(arm_a, arm_b)
        assert result.asymmetry_score == pytest.approx(-0.0025)
        assert result.p_value > 0.9
        assert result.is_significant is False
        lo = result.confidence_interval_lower
        hi = result.confidence_interval_upper
        assert lo < 0 < hi

    def test_degenerate_single_tone_inputs(self):
        # Single-tone arms: t 0.0, p 1.0, d 0.0, not significant.
        calc = self._calculate()
        result = calc([-0.55], [-0.35])
        assert result.asymmetry_score == pytest.approx(-0.20)
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
class TestSuiteRelaunch1105:
    def test_relaunch_log_path_written(self):
        # The re-launched full suite log exists in goal hidden_files
        # (created by this run's background launch before commit).
        assert os.path.exists(SUITE_LOG), (
            "the #1105 background suite must be re-launched to "
            + SUITE_LOG
            + " before the main commit"
        )

    def test_relaunch_log_is_full_inventory(self):
        # The re-launch runs WITHOUT -x: the full inventory
        # (calendar by-design failures included) is needed for the
        # #1110 triage. The log must hold pytest progress output,
        # not just a header.
        text = _read(SUITE_LOG)
        assert text.count(".") > 100, (
            "the re-launched suite log should accumulate dot "
            "progress; got %d dots" % text.count(".")
        )

    def test_next_type_d_run_owns_the_verdict(self):
        # Per the #795 convention, the NEXT Type D run (#1110)
        # checks this suite's verdict; this run only records the
        # launch.
        assert "type_d_1105_full_suite.log" in SUITE_LOG


# ---------------------------------------------------------------------------
# 13. Doc-sync per #719 (fails pre-commit by design; passes post-sync)
# ---------------------------------------------------------------------------
class TestTypeDDocSync1105:
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
class TestTypeDIterationLog1105:
    def test_1105_entry_leads_log(self):
        # The "## #1105 Type D:" entry leads the log (newest-first
        # ordering); hashes are TBD until the anchor followup patches
        # them per #565. Deselected pre-commit per #721.
        assert _read(LOG_PATH).startswith("## #1105 Type D:")

    def test_1105_entry_names_window_and_predecessors(self):
        text = _read(LOG_PATH)
        entry = text.split("## #1104 Type C:")[0]
        assert "1105-1109" in entry
        assert "9bb80079" in entry
        assert "EIGHTIETH" in entry

    def test_1104_entry_present(self):
        # The #1104 entry is present in the log (the #1105 entry
        # prepends above it).
        assert "## #1104 Type C:" in _read(LOG_PATH)


# ---------------------------------------------------------------------------
# 15. In-flight isolation
# ---------------------------------------------------------------------------
class TestInflightIsolation1105:
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
        # This run's staged set is the #1105 test file and the
        # doc-sync files only.
        status = _git("status", "--short")
        staged = [l for l in status.splitlines() if l.startswith(("M ", "A "))]
        allowed = (
            "test_type_d_1105_",
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
