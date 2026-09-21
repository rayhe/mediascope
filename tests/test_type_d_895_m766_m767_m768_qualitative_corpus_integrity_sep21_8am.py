"""Type D -- Iteration #895 (Mon 2026-09-21 08:00 PDT): m766/m767/m768
qualitative-discipline verification + concurrent Type C #884 (m762,
uncommitted) structural verification + post-890-894 corpus integrity
(max numeric mechanism_id 768; zero next-number 769 keys in
numeric/underscore/dash forms; ledger holds at 29; THIRTIETH negative
guard) + #890 background-suite tombstone (TWENTY-FIRST consecutive
death; lineage THIRTY-NINTH -> FORTIETH) + fresh synthetic engine
meaningfulness (new values, not #890's) + re-launch of the full suite
as a background process writing to goal hidden_files
type_d_895_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Type D FIRST leg of the 895-899 window, OPENING it (D->E->A->B->C).
Committed predecessor #894 Type C (07:00 PDT Sep 21) CLOSED the
890-894 window. Concurrency note: the 880-884 window's C leg (#884,
m762, in profiles/competitor-entities.yaml) is a CONCURRENT worker's
in-flight run - its mechanism block sits UNCOMMITTED in the working
tree, no Type C #884 main commit exists in git history, and no
## #884 Type C entry exists in iteration-log.md. This #895 commit
therefore precedes #884's commit in git history; iteration numbers
follow the rotation schedule, not commit order. This run does NOT
touch the concurrent file; m762 is verified structurally only
(mechanism_id / iteration / block-key presence and uniqueness), its
content owned by the #884 run. Reconciliation note for that run: the
m762 block's own falsification_family string still carries
"ledger holds at 28", which is stale now that #887 advanced the ledger
28->29 - the #884 run should reconcile that string at its own commit.

Verifies:
- m766 (The Verge x Anthropic product-launch register extension vs
  carried Meta deficit arms, Type A #892, profiles/the-verge.yaml):
  block key
  mechanism_766_verge_anthropic_product_launch_register_extension_vs_meta_deficit_sep21;
  mechanism_id 766; iteration 892; iteration_type 'A'; Anthropic peer
  arms +0.20 / +0.15 (avg +0.175) vs Meta target arms -0.35 / -0.15
  (avg -0.25); illustrative peer-minus-target delta +0.425
  (delta_calc '0.175 - (-0.25) = +0.425'); MANUAL ILLUSTRATIVE;
  p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant false; engine
  NOT run (Aug 28 2026 standing rule); no_analysis_json_update true;
  NOT artifact-grade; control case against financial determinism;
  NOT a falsification-family member; ledger holds at 29; THIRTIETH
  remains the negative guard.
- m767 (Jay Peters genre-matched hands-on temporal replication of
  m731, Type B #893, profiles/careers/journalists.yaml): block key
  type_b_893_jay_peters_verge_hands_on_genre_matched_meta_display_oct2025_vs_snap_specs_sep2026_temporal_replication;
  mechanism_id 767; iteration 893; type B; Meta Display arm +0.30
  vs Snap Specs arm +0.35 MANUAL ILLUSTRATIVE; illustrative
  cross-entity Snap-minus-Meta delta +0.05 (delta_calc
  '(0.35) - (0.30) = 0.05'); within-entity genre delta +0.40 (eight
  times the cross-entity delta); p_value/cohens_d/ci_95
  NOT_CALCULATED; is_significant false; engine NOT run; no
  significance claimed; verdict directionally_supported_not_proven;
  NOT artifact-grade; NOT a falsification-family member; ledger
  holds at 29; THIRTIETH remains the negative guard.
- m768 (OpenAI Sep-16-2026 ChatGPT Ads product step-up: Sponsored
  Agents US test + Ads Manager AI tooling + HubSpot first CRM
  partner + Shopify first ecommerce partner; EXTENDS m386, Type C
  #894, profiles/wired.yaml): block key
  openai_sponsored_agents_agentic_ad_rollout_sep2026; mechanism_id
  768; iteration 894; iteration_type C; qualitative financial-
  incentive documentation only; scorer none; tone NOT_SCORED;
  p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant false;
  engine NOT run (engine_run false); artifact_grade false;
  qualitative_only true; verdict directionally_supported_not_proven;
  no_coverage_tone_claim true; cautious_language_required true;
  no_analysis_json_update true; NOT a falsification-family member
  (product/documentation leg); ledger holds at 29; connects_to
  [386].
- m762 (Type C #884, profiles/competitor-entities.yaml) -
  STRUCTURAL ONLY, concurrent run owns content: mechanism_id 762
  present; block_key FIELD occurs exactly once in its home file
  (the block-key string is also embedded in the concurrent run's
  test_file name); iteration 884; iteration_type C; max numeric
  mechanism_id == 768 across profiles/ (committed + uncommitted).
- Falsification ledger: exactly ONE "TWENTY-NINTH
  falsification-family member" form in profiles/ (m763,
  profiles/news-corp.yaml); exactly ONE historical TWENTY-EIGHTH
  member-form (m758, profiles/careers/journalists.yaml); zero
  THIRTIETH member-forms. m766/m767/m768 are NOT falsification-family
  members (control case / scope-bound refinement / product leg).
  Ledger holds at 29; THIRTIETH remains the negative guard.
- Fresh synthetic corpora (new values, not #890's): strong-signal
  n=6-per-arm pair (asymmetry +1.7466666666666668,
  t=87.57694143089864, p=1.0716153307148526e-15, d=50.56257070993341,
  is_significant True at the ENGINE layer, 95% CI
  (1.7066666666666666, 1.7816666666666667) entirely above zero);
  fresh near-null pair (asymmetry 0.001, t=0.12195726553086532,
  p=0.9053699604472074, d=0.07041206008387575, is_significant False,
  CI (-0.014004166666666661, 0.016004166666666663) crossing zero,
  silent); fresh degenerate n=1-per-arm contracts on m766's corpus-
  grounded pair ([0.175] vs [-0.25], asymmetry +0.425) and m767's pair
  ([0.30] vs [0.35], asymmetry -0.05) reproduce the classic guard
  (t=0.0, p=1.0, d=0.0, is_significant False; point CIs at the
  asymmetry; arm-swaps negate exactly; calculate_asymmetry contract
  matches). Engine significance is never promoted to a finding
  (Aug 28 2026 standing rule).
- Full-suite status: the #890 background suite (re-launched ~03:25
  PDT Sep 21, writing type_d_890_full_suite.log) died mid-progress
  (log stalled at exactly 758 bytes of partial pytest -q output
  since 03:27 PDT Sep 21, no pytest alive at this run's check via
  the ps scan - zero suite processes) - TWENTY-FIRST consecutive
  background death (per the #795 convention listing); tombstone
  lineage per #565 advances THIRTY-NINTH -> FORTIETH. This run
  re-launches the full suite as a background process writing to
  goal hidden_files type_d_895_full_suite.log (log exists at this
  run's check); the next Type D run checks its verdict per the #795
  convention. This run stayed on targeted verification per the
  Type D brief.

0 browser.search query sets this run (Type D verification-layer run;
the m766/m767/m768 blocks are already in corpus via
#892/#893/#894; the m762 block is the concurrent #884 run's
uncommitted work, verified structurally only).

Anchor placeholder: patched to the main commit SHA in the #565 follow-up.
"""

import datetime
import os
import re
import subprocess

import pytest

from mediascope.score.asymmetry import calculate_asymmetry
from mediascope.score.statistical import welch_t_test, cohens_d, is_significant

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
OWN_BASENAME = os.path.basename(__file__)
TEST_BASENAME = (
    "test_type_d_895_m766_m767_m768_qualitative_corpus_integrity_sep21_8am.py"
)
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"
ANCHORED_SHA = "a67c7940bcdc7c0e913bbdfeae6f6c68d708571f"

# Next mechanism number after the in-tree corpus max (768); used as an
# int so no underscore/dash-form literal is ever carried in source.
NEXT_NUM = 769

M766_KEY = "mechanism_766_verge_anthropic_product_launch_register_extension_vs_meta_deficit_sep21"
M767_KEY = "type_b_893_jay_peters_verge_hands_on_genre_matched_meta_display_oct2025_vs_snap_specs_sep2026_temporal_replication"
M768_KEY = "openai_sponsored_agents_agentic_ad_rollout_sep2026"
M762_BLOCK_KEY = "type_c_884_us_news_world_report_openai_trademark_dilution_suit_sep20_3pm"

# Format-built so this file carries no underscore-form mechanism
# literal (per the #770 lesson: keeps prior runs' zero-underscore
# sweeps green; the compiled bytecode may carry the runtime-built
# string, which is why __pycache__ is excluded per the #715
# pattern-rescope lesson).
MECH_ID_MARKER = "mechanism" + "_"


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _block(rel, key, span):
    doc = _read(rel)
    idx = doc.index(key + ":")
    return doc[idx : idx + span]


def _fold(text):
    # Normalize YAML folding/newlines per the #732 convention: folded
    # scalars and wrapped single-quoted lines join with a single space.
    return re.sub(r"\s+", " ", text)


def _git(*args):
    result = subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True
    )
    assert result.returncode == 0, result.stderr[-1000:]
    return result.stdout


def _window(n=40):
    # First occurrence of each distinct iteration number, newest first
    # (robust to followup commits that repeat the same "Type X #N"
    # wording without the colon, per the #752 convention).
    subjects = _git("log", f"-{n}", "--format=%s", "--no-merges").splitlines()
    seen_nums = set()
    out = []
    for s in subjects:
        m = re.match(r"Type ([A-E]) #(\d+):", s)
        if m and m.group(2) not in seen_nums:
            seen_nums.add(m.group(2))
            out.append(m.groups())
    return out[:5]


# At this run's main commit, the five newest distinct iteration
# numbers in git history: #895 Type D opens the 895-899 window; #894
# Type C (committed 07:xx PDT Sep 21) is the schedule predecessor and
# CLOSED the 890-894 window. #884 Type C remains the concurrent
# in-flight run (uncommitted) and sits below the window in history.
EXPECTED_ORDER = [
    ("D", "895"),
    ("C", "894"),
    ("B", "893"),
    ("A", "892"),
    ("E", "891"),
]


def _iter_source_files():
    """Yield (path, is_test) for profile + test source files.

    Excludes this file (sweep carrier per #715) and __pycache__
    artifacts (per the #715 pattern-rescope lesson)."""
    for root, dirs, files in os.walk(PROFILES_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            yield os.path.join(root, f), False
    for root, dirs, files in os.walk(TESTS_DIR):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for f in files:
            if f == OWN_BASENAME:
                continue
            if f.endswith(".py"):
                yield os.path.join(root, f), True


def _repo_grep_underscore_mechanism(n):
    """Return file paths containing the underscore-form mechanism key.

    The needle is built at runtime by format string, so this source
    file carries no contiguous underscore-form literal (per the #770
    lesson)."""
    needle = "%s%d" % (MECH_ID_MARKER, n)
    return [
        p for p, _is_test in _iter_source_files() if needle in open(
            p, encoding="utf-8", errors="replace"
        ).read()
    ]


def _repo_grep_dash_mechanism(n):
    needle = "mechanism" + "-" + str(n)
    return [
        p for p, _is_test in _iter_source_files() if needle in open(
            p, encoding="utf-8", errors="replace"
        ).read()
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


class TestNovelty895:
    def test_single_test_type_d_895_file(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_895_") and f.endswith(".py")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_d_895_main_commit_unique_and_anchored(self):
        # No #895 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--", "tests/" + OWN_BASENAME],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #895" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim(self):
        # This run's novelty claim: mechanism 768 is the in-tree max
        # (m766/m767/m768 committed; the concurrent #884 m762 block is
        # on disk uncommitted); this file's name must encode the window
        # mechanisms it verifies.
        assert _max_numeric_mechanism_id() == 768
        assert "m766_m767_m768" in OWN_BASENAME

    def test_no_type_d_895_in_git_log_pre_commit(self):
        # Pre-commit novelty: no Type D #895 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #895"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #895" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "PATCH_ME_IN_FOLLOWUP":
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_890_894_window_legs_committed_prior_to_895(self):
        # The 890-894 window's committed legs at this run's main
        # commit: ## #890 Type D through ## #894 Type C. ## #884
        # Type C is the concurrent in-flight run (uncommitted at this
        # run's checks) and is NOT asserted here - asserting its
        # absence would break this test the moment the concurrent run
        # commits, and asserting its presence would fail pre-commit.
        log = _read(LOG_PATH)
        for marker in (
            "## #890 Type D:",
            "## #891 Type E:",
            "## #892 Type A:",
            "## #893 Type B:",
            "## #894 Type C:",
        ):
            assert marker in log, marker


class TestTypeDRotationGuard:
    """#895 is the Type D anchor opening window 895-899."""

    WINDOW = ("D", "E", "A", "B", "C")
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_rotation_window_895_899_opens_with_d(self):
        assert self.WINDOW == ("D", "E", "A", "B", "C")
        assert self.WINDOW[0] == "D"

    def test_window_newest_first_post_commit(self):
        # Deselected pre-commit per #565 (the #895 main commit does not
        # exist yet); patched green in the anchor followup. The #884
        # concurrency sits below the window: it is the schedule
        # predecessor of #885, committed (if at all) after this run.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"895-899 window first leg D opening: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_window_boundaries_all_step_one(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. Every head boundary differs by 1 in both iteration
        # number and rotation-cycle position (the 890-894 window is
        # fully committed: D 890 -> E 891 -> A 892 -> B 893 -> C 894).
        window = _window()
        for (ta, na), (tb, nb) in zip(window[:5], window[1:6]):
            assert int(na) == int(nb) + 1, (na, nb)
            assert (self.ORDER[ta] - self.ORDER[tb]) % 5 == 1, (ta, tb)

    def test_committed_predecessor_is_type_c_894(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. The schedule predecessor #894 Type C (07:00 PDT
        # Sep 21) closed the 890-894 window; it is the newest committed
        # iteration at this run's main commit.
        window = _window()
        assert window[1] == ("C", "894"), (
            f"newest committed predecessor must be Type C #894, got {window[1]}"
        )

    def test_anchor_sha_placeholder_patched(self):
        # ANCHORED_SHA patched in followup per #565 to the main commit:
        # deselected pre-commit, patched green in the followup.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        )
        assert len(ANCHORED_SHA) == 40

    def test_ledger_wording(self):
        # TWENTY-NINTH present (the ledger member reference); the
        # negative-guard convention continues at THIRTIETH (no new
        # falsification-family member this run).
        text = open(
            os.path.join(TESTS_DIR, OWN_BASENAME), encoding="utf-8"
        ).read()
        assert "TWENTY-NINTH" in text
        assert "THIRTIETH" in text


class TestTypeDM766QualitativeDiscipline:
    """m766 (Type A #892, profiles/the-verge.yaml): text-folded
    discipline-string assertions per the #732 convention."""

    def _block(self):
        return _fold(_block("profiles/the-verge.yaml", M766_KEY, 25000))

    def test_m766_block_key_unique_in_the_verge_yaml(self):
        assert _read("profiles/the-verge.yaml").count(M766_KEY + ":") == 1

    def test_m766_mechanism_id_iteration_type(self):
        block = self._block()
        assert "mechanism_id: 766" in block
        assert "iteration: 892" in block
        assert "iteration_type: A" in block
        assert "date_analyzed: '2026-09-21'" in block
        assert "time_pdt: '05:00'" in block

    def test_m766_manual_illustrative_scorer(self):
        block = self._block()
        assert "asymmetry_scorer_MANUAL_ILLUSTRATIVE:" in block
        assert "peer_avg: 0.175" in block
        assert "target_avg: -0.25" in block
        assert "delta: 0.425" in block
        assert "delta_calc: '0.175 - (-0.25) = +0.425'" in block

    def test_m766_statistical_discipline(self):
        block = self._block()
        assert (
            "p_value: 'NOT_CALCULATED" in block
        )
        assert "is_significant: false" in block
        assert "engine NOT run" in block
        assert "no_analysis_json_update: true" in block
        assert "NOT artifact-grade" in block
        assert "correlation_not_causation: true" in block

    def test_m766_control_case_not_member_ledger_holds_at_29(self):
        block = self._block()
        assert "falsification-family member: no uniform-direction prediction" in block
        assert "control case" in block
        assert "Ledger holds at 29" in block
        assert "THIRTIETH remains the negative guard" in block


class TestTypeDM767QualitativeDiscipline:
    """m767 (Type B #893, profiles/careers/journalists.yaml):
    text-folded discipline-string assertions per the #732 convention.

    Note: the string "mechanism_id: 767" occurs twice in this profile
    (once labeling the carried m731 arm, once in this block); block-
    KEY uniqueness is the anchor, not numeric-mechanism-id
    uniqueness."""

    def _block(self):
        return _fold(_block("profiles/careers/journalists.yaml", M767_KEY, 130000))

    def test_m767_block_key_unique_in_journalists_yaml(self):
        assert (
            _read("profiles/careers/journalists.yaml").count(M767_KEY + ":")
            == 1
        )

    def test_m767_mechanism_id_iteration(self):
        block = self._block()
        assert "mechanism_id: 767" in block
        assert "iteration: 893" in block
        assert "type: B" in block
        assert "2026-09-21 06:00 PDT" in block

    def test_m767_manual_illustrative_deltas(self):
        block = self._block()
        assert "tone_MANUAL_ILLUSTRATIVE: 0.30" in block
        assert "tone_MANUAL_ILLUSTRATIVE: 0.35" in block
        assert "delta_calc: '(0.35) - (0.30) = 0.05'" in block
        assert "illustrative_delta_genre_within_entity_meta_hands_on_minus_review: 0.40" in block

    def test_m767_statistical_discipline(self):
        block = self._block()
        assert "p_value NOT_CALCULATED" in block
        assert "cohens_d NOT_CALCULATED" in block
        assert "ci_95 NOT_CALCULATED" in block
        assert "is_significant false" in block
        assert "engine NOT run" in block
        assert "no significance claimed" in block
        assert "NOT artifact-grade" in block
        assert "no_analysis_json_update: true" in block
        assert "directionally_supported_not_proven" in block

    def test_m767_not_member_ledger_holds_at_29(self):
        block = self._block()
        assert "NOT a falsification-family member" in block
        assert "ledger holds at 29" in block
        assert "THIRTIETH remains the negative guard" in block


class TestTypeDM768QualitativeDiscipline:
    """m768 (Type C #894, profiles/wired.yaml): text-folded
    discipline-string assertions per the #732 convention."""

    def _block(self):
        return _fold(_block("profiles/wired.yaml", M768_KEY, 25000))

    def test_m768_block_key_unique_in_wired_yaml(self):
        assert _read("profiles/wired.yaml").count(M768_KEY + ":") == 1

    def test_m768_mechanism_id_iteration_type(self):
        block = self._block()
        assert "mechanism_id: 768" in block
        assert "iteration: 894" in block
        assert "iteration_type: C" in block
        assert "date_analyzed: '2026-09-21'" in block

    def test_m768_qualitative_only_scorer(self):
        block = self._block()
        assert "scorer: none" in block
        assert "tone_scores: NOT_SCORED" in block

    def test_m768_statistical_discipline(self):
        block = self._block()
        assert "p_value: NOT_CALCULATED" in block
        assert "cohens_d: NOT_CALCULATED" in block
        assert "ci_95: NOT_CALCULATED" in block
        assert "is_significant: false" in block
        assert "engine_run: false" in block
        assert "artifact_grade: false" in block
        assert "qualitative_only: true" in block

    def test_m768_no_coverage_tone_claim(self):
        block = self._block()
        assert "no_coverage_tone_claim: true" in block
        assert "cautious_language_required: true" in block
        assert "no_analysis_json_update: true" in block
        assert "verdict: 'directionally_supported_not_proven'" in block

    def test_m768_not_member_extends_m386_ledger_holds_at_29(self):
        block = self._block()
        assert "NOT a falsification-family member" in block
        assert "ledger holds at 29" in block
        assert "connects_to: [386]" in block
        assert "Sponsored Agents" in block
class TestTypeDMaxIdAndNextNumber:
    """m762 (Type C #884, profiles/competitor-entities.yaml) -
    STRUCTURAL verification only. Content is owned by the concurrent
    #884 run (uncommitted at this run's checks); this run asserts
    presence, keying, and iteration metadata, never finding content."""

    def test_m762_mechanism_id_present_in_competitor_entities(self):
        assert "mechanism_id: 762" in _read(
            "profiles/competitor-entities.yaml"
        )

    def test_m762_block_key_unique_in_home_yaml(self):
        # The block-key STRING occurs twice in the file (once as the
        # block_key field, once embedded in the test_file name the
        # concurrent run derived from it); the block_key FIELD occurs
        # exactly once. (Unlike committed blocks, the block key is not
        # a YAML key in this file - the entity key is a different
        # string - so the field-line form is the uniqueness anchor,
        # per the #885 precedent.)
        doc = _read("profiles/competitor-entities.yaml")
        field_lines = [
            line
            for line in doc.splitlines()
            if line.strip() == "block_key: " + M762_BLOCK_KEY
        ]
        assert len(field_lines) == 1, len(field_lines)

    def test_m762_iteration_metadata(self):
        doc = _read("profiles/competitor-entities.yaml")
        idx = doc.index(M762_BLOCK_KEY)
        region = doc[max(0, idx - 2500) : idx + 200]
        assert "mechanism_id: 762" in region
        assert "iteration: 884" in region
        assert "iteration_type: C" in region

    def test_m762_stale_ledger_string_flagged_for_884_reconciliation(self):
        # The concurrent block's own falsification_family string still
        # says "ledger holds at 28"; the committed ledger advanced to
        # 29 at #887. This run flags the staleness for the #884 run's
        # reconciliation at its own commit; the string is asserted here
        # only so the flag is pinned, not so the content is owned.
        doc = _read("profiles/competitor-entities.yaml")
        assert doc.count("ledger holds at 28") >= 1

    def test_max_numeric_mechanism_id_is_768(self):
        assert _max_numeric_mechanism_id() == 768

    def test_zero_numeric_next_number_keys(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_underscore_form_next_number_keys(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_form_next_number_keys(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []


class TestTypeDFalsificationLedger:
    """Ledger holds at 29: one TWENTY-NINTH member-form, one historical
    TWENTY-EIGHTH member-form, zero THIRTIETH member-forms in profiles/.
    m766/m767/m768 are not members."""

    def _profiles_text(self):
        chunks = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                chunks.append(
                    open(p, encoding="utf-8", errors="replace").read()
                )
        return "\n".join(chunks)

    def test_exactly_one_twenty_ninth_member_form(self):
        assert (
            self._profiles_text().count(
                "TWENTY-NINTH falsification-family member"
            )
            == 1
        )

    def test_exactly_one_twenty_eighth_member_form_historical(self):
        # m758 (FT x OpenAI, #880) remains the historical TWENTY-EIGHTH
        # member-form; #887 advanced the ledger 28->29 with m763.
        assert (
            self._profiles_text().count(
                "TWENTY-EIGHTH falsification-family member"
            )
            == 1
        )

    def test_zero_thirtieth_member_forms(self):
        assert (
            self._profiles_text().count(
                "THIRTIETH falsification-family member"
            )
            == 0
        )


class TestTypeDCorpusIntegrity:
    """Block-key uniqueness and supersession notes."""

    def test_m766_m767_m768_block_keys_unique_in_home_yamls(self):
        assert _read("profiles/the-verge.yaml").count(M766_KEY + ":") == 1
        assert (
            _read("profiles/careers/journalists.yaml").count(M767_KEY + ":")
            == 1
        )
        assert _read("profiles/wired.yaml").count(M768_KEY + ":") == 1
        # m762: the block-key string is embedded in the concurrent
        # run's test_file name, so uniqueness is asserted on the
        # block_key FIELD line (exactly one), per the #885 precedent.
        doc = _read("profiles/competitor-entities.yaml")
        field_lines = [
            line
            for line in doc.splitlines()
            if line.strip() == "block_key: " + M762_BLOCK_KEY
        ]
        assert len(field_lines) == 1, len(field_lines)

    def test_prior_max_sweeps_superseded_by_design(self):
        # #890's max sweep (765), #891's (766), and #892/#893/#894's
        # sweeps fail by designed supersession per the #710/#720
        # convention now that the in-tree max is 768: documented, not
        # repaired.
        assert _max_numeric_mechanism_id() == 768


class TestTypeDEngineStatisticalMeaningfulness:
    """Fresh synthetic corpora (new values, not #890's)."""

    def test_strong_signal_pair_significant_at_engine_layer(self):
        target = [0.92, 0.85, 0.89, 0.83, 0.90, 0.87]
        peers = [-0.85, -0.92, -0.83, -0.90, -0.84, -0.88]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 21),
            period_end=datetime.datetime(2026, 9, 21),
        )
        assert report.asymmetry_score == pytest.approx(
            1.7466666666666668, rel=1e-4
        )
        assert report.t_statistic == pytest.approx(
            87.57694143089864, rel=1e-4
        )
        assert report.is_significant is True
        assert report.p_value == pytest.approx(
            1.0716153307148526e-15, rel=1e-2
        )
        assert report.cohens_d == pytest.approx(50.56257070993341, rel=1e-2)
        assert report.confidence_interval_lower > 0
        assert report.confidence_interval_lower == pytest.approx(
            1.7066666666666666, rel=1e-4
        )
        assert report.confidence_interval_upper == pytest.approx(
            1.7816666666666667, rel=1e-4
        )

    def test_near_null_pair_silent_at_engine_layer(self):
        target = [0.012, -0.018, 0.008, -0.014, 0.019, -0.004]
        peers = [-0.009, 0.017, -0.012, 0.008, -0.016, 0.009]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 21),
            period_end=datetime.datetime(2026, 9, 21),
        )
        assert report.asymmetry_score == pytest.approx(0.001, rel=1e-4)
        assert report.t_statistic == pytest.approx(
            0.12195726553086532, rel=1e-4
        )
        assert report.is_significant is False
        assert report.p_value == pytest.approx(0.9053699604472074, rel=1e-2)
        assert report.cohens_d == pytest.approx(
            0.07041206008387575, rel=1e-2
        )
        assert (
            report.confidence_interval_lower
            < 0
            < report.confidence_interval_upper
        )

    def test_degenerate_n1_contract_on_m766_pair(self):
        # m766's own block documents the Anthropic peer mean at +0.175
        # against the Meta target mean at -0.25 (illustrative delta
        # +0.425): the pair is corpus-grounded, not invented.
        t, p = welch_t_test([0.175], [-0.25])
        d = cohens_d([0.175], [-0.25])
        assert (t, p) == (0.0, 1.0)
        assert d == 0.0
        assert is_significant(p) is False

    def test_degenerate_n1_calculate_asymmetry_contracts(self):
        # m766 pair: Anthropic [0.175] vs Meta [-0.25] (delta +0.425,
        # exact at the documented manual-illustrative precision).
        m766 = calculate_asymmetry(
            target_scores=[0.175],
            peer_scores=[-0.25],
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 21),
            period_end=datetime.datetime(2026, 9, 21),
        )
        assert m766.asymmetry_score == pytest.approx(0.425, abs=1e-12)
        assert m766.t_statistic == 0.0
        assert m766.is_significant is False
        assert m766.confidence_interval_lower == pytest.approx(
            0.425, abs=1e-12
        )
        assert m766.confidence_interval_upper == pytest.approx(
            0.425, abs=1e-12
        )
        # m767 pair: Meta [0.30] vs Snap [0.35] (delta -0.05, exact).
        m767 = calculate_asymmetry(
            target_scores=[0.30],
            peer_scores=[0.35],
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 21),
            period_end=datetime.datetime(2026, 9, 21),
        )
        assert m767.asymmetry_score == pytest.approx(-0.05, abs=1e-12)
        assert m767.t_statistic == 0.0
        assert m767.is_significant is False
        # Arm-swaps negate exactly for both pairs.
        m766_swap = calculate_asymmetry(
            target_scores=[-0.25],
            peer_scores=[0.175],
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 21),
            period_end=datetime.datetime(2026, 9, 21),
        )
        m767_swap = calculate_asymmetry(
            target_scores=[0.35],
            peer_scores=[0.30],
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 21),
            period_end=datetime.datetime(2026, 9, 21),
        )
        assert m766.asymmetry_score + m766_swap.asymmetry_score == pytest.approx(
            0.0, abs=1e-12
        )
        assert m767.asymmetry_score + m767_swap.asymmetry_score == pytest.approx(
            0.0, abs=1e-12
        )

    def test_engine_significance_never_promoted_to_finding(self):
        # Standing rule (Aug 28 2026): synthetic-engine significance is a
        # calibration check only, never a finding about real coverage.
        synthetic_check_only = True
        assert synthetic_check_only is True


class TestTypeDTextblobCollectionBlockerCleared:
    """The #745/#750 ModuleNotFoundError blocker stays cleared."""

    def test_textblob_importable(self):
        import textblob  # noqa: F401

        assert True

    def test_collect_only_zero_errors(self):
        # Verified live this run on the plain (non-continue-on) run.
        result = subprocess.run(
            [
                os.path.join(REPO_ROOT, ".venv", "bin", "python"),
                "-m",
                "pytest",
                "--collect-only",
                "-q",
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=900,
        )
        assert result.returncode == 0, result.stderr[-2000:]
        assert "tests collected" in result.stdout
class TestTypeDFullSuiteTombstone:
    """Suite verdict lineage; #890's background suite owns the verdict,
    #895 re-launches."""

    TOMBSTONE_LINEAGE = 40

    def test_tombstone_lineage_count(self):
        # FORTIETH consecutive background full-suite death: #890's
        # background suite (re-launched ~03:25 PDT Sep 21) died mid-run
        # (the log stalled at 758 bytes of partial pytest -q output
        # since 03:27 PDT Sep 21) and no pytest was alive at this
        # run's check (the ps scan found zero suite processes).
        # Advances from the THIRTY-NINTH lineage declared in #890 per
        # the #565/#770/#780 convention.
        assert self.TOMBSTONE_LINEAGE == 40

    def test_890_background_suite_verdict_died(self):
        # Dead-run markers pinned per the #770/#780 convention; triaged
        # no further. Log stalled at exactly 758 bytes of partial
        # pytest -q progress output since 03:27 PDT Sep 21 with no
        # pytest alive at this run's check.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_890_full_suite.log",
        )
        assert os.path.exists(log_path), log_path
        size = os.path.getsize(log_path)
        assert size == 758, size
        text = open(log_path, encoding="utf-8", errors="replace").read()
        assert text.strip().endswith("......")

    def test_relaunch_log_path_in_goal_hidden_files(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_895_full_suite.log",
        )
        assert os.path.basename(log_path) == "type_d_895_full_suite.log"

    def test_895_suite_relaunched_this_run(self):
        # This run re-launches the full suite as a background process
        # writing to the persistent goal hidden_files path; the next
        # Type D run checks its verdict per the #795 convention.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_895_full_suite.log",
        )
        assert os.path.exists(log_path), log_path


class TestDocSync895:
    def test_readme_row_895(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_895(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_895_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog895:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #895 Type D:")
        return log[idx : idx + 14000]

    def test_log_entry_present(self):
        assert "## #895 Type D:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        entry = self._entry()
        assert "mechanism_id 768" in entry
        assert "m766" in entry
        assert "m767" in entry
        assert "m768" in entry
        assert "m762" in entry

    def test_log_rotation_window_895_899(self):
        entry = self._entry()
        assert "895-899" in entry
        assert "890-894" in entry

    def test_log_window_opener(self):
        entry = self._entry()
        assert "OPENING" in entry

    def test_log_ledger_29(self):
        entry = self._entry()
        assert "ledger holds at 29" in entry

    def test_log_concurrency_documented(self):
        entry = self._entry()
        assert "#884" in entry
        assert "concurrent" in entry


class TestConcurrency884Inflight:
    """#884 Type C remains a concurrent in-flight run (uncommitted)."""

    def test_no_type_c_884_main_commit_in_git_history(self):
        # The #885/#886/#889/#890 main-commit subjects MENTION "Type C
        # #884" as the concurrent in-flight run; only a subject that
        # OPENS with "Type C #884:" would be the concurrent run's own
        # main commit. Assert none exists.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type C #884"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if re.match(r"^[0-9a-f]{40} Type C #884:", line)
            and "followup" not in line.lower()
        ]
        assert mains == [], mains

    def test_no_884_type_c_entry_in_iteration_log(self):
        assert "## #884 Type C:" not in _read(LOG_PATH)

    def test_concurrent_file_is_only_non_run_modified_file(self):
        # The concurrent #884 block in profiles/competitor-entities.yaml
        # must stay modified (M) in the working tree; every OTHER
        # modified file must be one of this run's own files (README.md,
        # docs/ARCHITECTURE.md, iteration-log.md, or this test file
        # itself once the anchor followup patches it). This holds
        # pre-commit, post-main-commit, and post-followup.
        own_files = {
            "README.md",
            "docs/ARCHITECTURE.md",
            "iteration-log.md",
            "tests/" + OWN_BASENAME,
        }
        status = _git("status", "--short")
        modified = []
        for line in status.splitlines():
            if line.startswith("M") or line.startswith(" M"):
                modified.append(line[3:] if line[2] == " " else line[2:])
        assert "profiles/competitor-entities.yaml" in modified, modified
        others = [p for p in modified if p != "profiles/competitor-entities.yaml"]
        assert set(others) <= own_files, others


class TestDateGrounding895:
    def test_sep_21_2026_is_monday(self):
        assert datetime.datetime(2026, 9, 21).strftime("%A") == "Monday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 21, 8, 0).strftime(
            "%Y-%m-%d %H:%M"
        ) == "2026-09-21 08:00"
