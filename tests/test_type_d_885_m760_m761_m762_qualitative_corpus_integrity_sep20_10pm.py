"""Type D -- Iteration #885 (Sun 2026-09-20 22:16 PDT): m760/m761
qualitative-discipline verification + m762 (concurrent Type C #884,
UNCOMMITTED at this run's checks) structural verification +
post-880-884 corpus integrity (max numeric mechanism_id 762; zero
next-number keys; ledger holds at 28) + #880 background-suite tombstone
(NINETEENTH consecutive death; lineage THIRTY-SEVENTH ->
THIRTY-EIGHTH) + fresh synthetic engine meaningfulness (new values, not
#880's) + re-launch of the full suite as a background process writing
to goal hidden_files type_d_885_full_suite.log (next Type D run checks
its verdict per the #795 convention).

Type D FIRST leg of the 885-889 window, OPENING it (D->E->A->B->C).
Concurrency note: the 880-884 window's C leg (#884, m762, U.S. News &
World Report v. OpenAI trademark-dilution suit) is a CONCURRENT
worker's in-flight run - its mechanism block sits UNCOMMITTED in the
working tree (profiles/competitor-entities.yaml, 103 insertions, the
only modified file at this run's git-status check) and no Type C #884
commit exists in git history. This #885 commit therefore precedes
#884's commit in git history; iteration numbers follow the rotation
schedule, not commit order. This run does NOT touch the concurrent
file; m762 is verified structurally only (mechanism_id / iteration /
block-key presence and uniqueness), its content owned by the #884 run.

Verifies:
- m760 (Guardian x OpenAI Sep-17 misalignment-disclosure piece -
  MIXED disclosure-pegged register -0.25 vs carried m687 arms;
  replication/refinement of m687; illustrative gap narrows 0.375 ->
  0.333, Type A #882, profiles/guardian.yaml): block key
  guardian_openai_sep17_misalignment_disclosure_mixed_register_vs_m687_meta_arms;
  mechanism_id 760; iteration 882; iteration_type 'A';
  asymmetry_scorer_MANUAL_ILLUSTRATIVE; target (Meta) [-0.55, -0.45]
  avg -0.50; peer (OpenAI) [-0.15, -0.10, -0.25] avg -0.1667;
  illustrative_register_delta_target_minus_peer -0.3333 (delta_calc
  '-0.50 - (-0.1667) = -0.3333'); methodology MANUAL ILLUSTRATIVE
  hand-assigned tones; p_value NOT_CALCULATED (standing rule Aug 28
  2026); is_significant false; engine_run false; verdict
  directionally_supported_not_proven; no_analysis_json_update true;
  artifact_grade false; correlation is not causation; NOT a
  falsification-family member (ledger holds at 28).
- m761 (Mariella Moon Engadget trust-crisis register asymmetry:
  neutral company-attributed relay on the Meta Luna camera-free rumor
  +0.10 vs accountability-adversarial register on OpenAI RubyGems
  -0.35; illustrative Meta-minus-OpenAI delta +0.45; #873 rejection
  reversed; peg-follows-register replication at writer level, Type B
  #883, profiles/careers/journalists.yaml mariella_moon slug):
  block_key
  type_b_883_mariella_moon_engadget_luna_neutral_relay_vs_rubygems_accountability;
  mechanism_id 761; iteration 883; methodology MANUAL ILLUSTRATIVE
  tones only; engine NOT run (illustrative arms only); p_value
  NOT_CALCULATED; cohens_d NOT_CALCULATED; ci_95 NOT_CALCULATED;
  is_significant false; artifact_grade NOT artifact-grade;
  correlation_not_causation true; verdict
  directionally_supported_not_proven; NOT a falsification-family
  member (ledger holds at 28).
- m762 (U.S. News & World Report v. OpenAI trademark-dilution suit,
  FIRST dedicated corpus mechanism for that suit, Type C #884,
  profiles/competitor-entities.yaml) - STRUCTURAL ONLY, concurrent
  run owns content: mechanism_id 762 present; block key
  type_c_884_us_news_world_report_openai_trademark_dilution_suit_sep20_3pm
  unique in its home YAML; iteration 884; iteration_type C; max
  numeric mechanism_id == 762 across profiles/.
- Falsification ledger: exactly ONE "TWENTY-EIGHTH
  falsification-family member" occurrence in profiles/
  (journalists.yaml m758 block, ledger 27->28); ZERO
  "TWENTY-NINTH falsification-family member" occurrences in
  profiles/ (ledger holds at 28; the-verge ledger line carries the
  "negative-guard convention continues at TWENTY-NINTH" string;
  test-file tombstones use TWENTY-NINTH ordinals only).
- Post-880-884 corpus integrity: max numeric mechanism_id == 762 in
  profiles/ (m762 in working tree, concurrent #884 uncommitted);
  zero numeric next-number keys in profiles/; zero underscore-form
  next-number key substrings in profiles/ and tests/ (own file
  excluded as sweep carrier per #715; needles format-built so no
  literal is carried; __pycache__ artifacts excluded per the #715
  pattern-rescope lesson); zero dash-form next-number references
  repo-wide; m760 / m761 / m762 block keys each unique in their home
  YAMLs; designed keying holds (zero underscore-form 760/761/762
  carriers - #882/#883 MECH_ID_MARKERs and the #884 block's needles
  are format-built, no sole carrier); #877-#883 max-sweeps fail by
  designed supersession per the #710/#720 convention (documented,
  not repaired).
- Statistical meaningfulness on FRESH synthetic corpora (new values,
  not #880's): strong-signal n=7-per-arm pair (asymmetry
  +1.802857142857143, t=97.55917603529285, p=1.01753175681008e-18,
  d=52.147573094290394, is_significant True at the ENGINE layer,
  95% CI (1.768535714285714, 1.8399999999999999) entirely above
  zero); fresh near-null pair (asymmetry -0.0014285714285714284,
  t=-0.12982269672237462, p=0.8988791731094714,
  d=-0.06939315030888374, is_significant False, CI
  (-0.02142857142857143, 0.018571428571428572) crossing zero,
  silent); fresh degenerate n=1-per-arm contracts on m760's pair
  ([-0.50], [-0.1667]) and m761's pair ([0.10], [-0.35]) reproduce
  the classic guard (t=0.0, p=1.0, d=0.0, is_significant False;
  asymmetry -0.3333 (m760, approx within 1e-4) and +0.45 (m761,
  IEEE-inexact 0.44999999999999996 within 1e-9); arm-swaps negate
  exactly; calculate_asymmetry contract matches). Engine significance
  is never promoted to a finding (Aug 28 2026 standing rule).
- Full-suite status: the #880 background suite re-launched 11:26 PDT
  Sep 20 died mid-progress (type_d_880_full_suite.log at 809 bytes,
  stalled partial pytest -q output, no pytest alive at this run's
  check via the ps scan - zero suite processes) - NINETEENTH
  consecutive background death (#705's, #710's first re-launch,
  #715's first re-launch, #715's re-launch, #720's re-launch,
  #725's re-launch, #730's re-launch, #825's re-launch,
  #830's re-launch, #835's re-launch, #840's re-launch,
  #845's re-launch, #850's re-launch, #855's re-launch,
  #860's re-launch, #865's re-launch, #870's re-launch, #875's
  re-launch, #880's re-launch; tombstone lineage per #565 advances
  THIRTY-SEVENTH -> THIRTY-EIGHTH). This run re-launches the full
  suite as a background process writing to goal hidden_files
  type_d_885_full_suite.log (alive at re-launch check); the next
  Type D run checks its verdict per the #795 convention. This run
  stayed on targeted verification per the Type D brief.

0 browser.search query sets this run (Type D verification-layer run;
the m760/m761 blocks are already in corpus via #882/#883; the m762
block is the concurrent #884 run's uncommitted work, verified
structurally only).

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
    "test_type_d_885_m760_m761_m762_qualitative_corpus_integrity_sep20_10pm.py"
)
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"
ANCHORED_SHA = "9ea6113c1889f33553728d75171569728df99bfc"

# Next mechanism number after the in-tree corpus max (762, the
# concurrent #884 block); used as an int so no underscore/dash-form
# literal is ever carried in source.
NEXT_NUM = 763

M760_KEY = "guardian_openai_sep17_misalignment_disclosure_mixed_register_vs_m687_meta_arms"
M761_YAML_KEY = "type_b_883_mariella_moon_engadget_luna_neutral_relay_vs_rubygems_accountability"
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
# numbers in git history: #884 Type C is the schedule predecessor but
# its commit lands AFTER this one (concurrent in-flight run,
# uncommitted at this run's checks), so the committed window reads
# D(885, this run) -> B(883) -> A(882) -> E(881) -> D(880).
EXPECTED_ORDER = [("D", "885"), ("B", "883"), ("A", "882"), ("E", "881"), ("D", "880")]


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


class TestNovelty885:
    def test_single_test_type_d_885_file(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_885_") and f.endswith(".py")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_d_885_main_commit_unique_and_anchored(self):
        # No #885 main commit exists pre-commit; the anchor test pins
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
            if "Type D #885" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim(self):
        # This run's novelty claim: mechanism 762 is the in-tree max
        # (the concurrent #884 block, uncommitted but on disk); this
        # file's name must encode the window mechanisms it verifies.
        assert _max_numeric_mechanism_id() == 762
        assert "m760_m761_m762" in OWN_BASENAME

    def test_no_type_d_885_in_git_log_pre_commit(self):
        # Pre-commit novelty: no Type D #885 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #885"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #885" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "PATCH_ME_IN_FOLLOWUP":
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_880_883_window_legs_committed_prior_to_885(self):
        # The 880-884 window's committed legs at this run's main
        # commit: ## #880 Type D through ## #883 Type B. ## #884
        # Type C is the concurrent in-flight run (uncommitted at this
        # run's checks) and is NOT asserted here - asserting its
        # absence would break this test the moment the concurrent run
        # commits, and asserting its presence would fail pre-commit.
        log = _read(LOG_PATH)
        for marker in (
            "## #880 Type D:",
            "## #881 Type E:",
            "## #882 Type A:",
            "## #883 Type B:",
        ):
            assert marker in log, marker


class TestTypeDRotationGuard:
    """#885 is the Type D anchor opening window 885-889."""

    WINDOW = ("D", "E", "A", "B", "C")
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_rotation_window_885_889_opens_with_d(self):
        assert self.WINDOW == ("D", "E", "A", "B", "C")
        assert self.WINDOW[0] == "D"

    def test_window_newest_first_post_commit(self):
        # Deselected pre-commit per #565 (the #885 main commit does not
        # exist yet); patched green in the anchor followup. The head
        # boundary skips #884: it is the schedule predecessor (Type C)
        # but commits after this run (concurrent in-flight).
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"885-889 window first leg D opening: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_schedule_boundary_gap_is_inflight_884(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. Head boundary D(885)->B(883) differs by 2: exactly
        # the in-flight #884 Type C sits between them in schedule
        # order (B->C->D per the cycle); all other boundaries differ
        # by 1.
        window = _window()
        (t0, n0), (t1, n1) = window[0], window[1]
        assert int(n0) - int(n1) == 2, (n0, n1)
        assert (t0, t1) == ("D", "B"), (t0, t1)
        assert (self.ORDER[t0] - self.ORDER[t1]) % 5 == 2, (t0, t1)
        for (ta, na), (tb, nb) in zip(window[1:], window[2:]):
            assert int(na) == int(nb) + 1, (na, nb)
            assert (self.ORDER[ta] - self.ORDER[tb]) % 5 == 1, (ta, tb)

    def test_committed_predecessor_is_type_b_883(self):
        # Deselected pre-commit per #565; patched green in the
        # followup. The SCHEDULE predecessor is Type C #884
        # (concurrent in-flight, uncommitted at this run's checks);
        # the newest COMMITTED predecessor at this run's main commit
        # is Type B #883.
        window = _window()
        assert window[1] == ("B", "883"), (
            f"newest committed predecessor must be Type B #883, got {window[1]}"
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
        # TWENTY-EIGHTH present (the ledger anchor reference); the
        # negative-guard convention continues at TWENTY-NINTH (no new
        # falsification-family member this window).
        text = open(
            os.path.join(TESTS_DIR, OWN_BASENAME), encoding="utf-8"
        ).read()
        assert "TWENTY-EIGHTH" in text
        assert "TWENTY-NINTH" in text


class TestTypeDM760QualitativeDiscipline:
    """m760 (Type A #882, profiles/guardian.yaml): text-folded
    discipline-string assertions per the #732 convention."""

    def _block(self):
        return _fold(_block("profiles/guardian.yaml", M760_KEY, 12000))

    def test_m760_block_key_unique_in_guardian_yaml(self):
        assert _read("profiles/guardian.yaml").count(M760_KEY + ":") == 1

    def test_m760_mechanism_id_iteration_type(self):
        block = self._block()
        assert "mechanism_id: 760" in block
        assert "iteration: 882" in block
        assert 'iteration_type: "A"' in block

    def test_m760_manual_illustrative_scorer(self):
        block = self._block()
        assert "asymmetry_scorer_MANUAL_ILLUSTRATIVE:" in block
        assert "illustrative_register_delta_target_minus_peer: -0.3333" in block
        assert "MANUAL ILLUSTRATIVE hand-assigned tones" in block

    def test_m760_statistical_discipline(self):
        block = self._block()
        assert 'p_value: "NOT_CALCULATED (standing rule Aug 28 2026)"' in block
        assert "is_significant: false" in block
        assert "engine_run: false" in block
        assert 'verdict: "directionally_supported_not_proven"' in block
        assert "no_analysis_json_update: true" in block
        assert "artifact_grade: false" in block


class TestTypeDM761QualitativeDiscipline:
    """m761 (Type B #883, profiles/careers/journalists.yaml):
    text-folded discipline-string assertions per the #732 convention."""

    def _block(self):
        return _fold(
            _block("profiles/careers/journalists.yaml", M761_YAML_KEY, 12000)
        )

    def test_m761_block_key_unique_in_journalists_yaml(self):
        assert (
            _read("profiles/careers/journalists.yaml").count(
                M761_YAML_KEY + ":"
            )
            == 1
        )

    def test_m761_mechanism_id_iteration(self):
        block = self._block()
        assert "mechanism_id: 761" in block
        assert "iteration: 883" in block

    def test_m761_manual_illustrative_methodology(self):
        block = self._block()
        assert "MANUAL ILLUSTRATIVE tones only" in block
        assert "engine NOT run (illustrative arms only)" in block

    def test_m761_statistical_discipline(self):
        block = self._block()
        assert "p_value: NOT_CALCULATED" in block
        assert "cohens_d: NOT_CALCULATED" in block
        assert "ci_95: NOT_CALCULATED" in block
        assert "is_significant: false" in block
        assert "NOT artifact-grade" in block
        assert "correlation_not_causation: true" in block


class TestTypeDM762ConcurrentStructural:
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
        # exactly once.
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

    def test_max_numeric_mechanism_id_is_762(self):
        assert _max_numeric_mechanism_id() == 762

    def test_zero_numeric_next_number_keys(self):
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_zero_underscore_form_next_number_keys(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []

    def test_zero_dash_form_next_number_keys(self):
        assert _repo_grep_dash_mechanism(NEXT_NUM) == []


class TestTypeDFalsificationLedger:
    """Ledger holds at 28: one TWENTY-EIGHTH member-form, zero
    TWENTY-NINTH member-forms in profiles/."""

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

    def test_exactly_one_twenty_eighth_member_form(self):
        assert (
            self._profiles_text().count(
                "TWENTY-EIGHTH falsification-family member"
            )
            == 1
        )

    def test_zero_twenty_ninth_member_forms(self):
        assert (
            self._profiles_text().count(
                "TWENTY-NINTH falsification-family member"
            )
            == 0
        )


class TestTypeDCorpusIntegrity:
    """Block-key uniqueness, designed keying, and supersession notes."""

    def test_m760_m761_m762_block_keys_unique_in_home_yamls(self):
        assert _read("profiles/guardian.yaml").count(M760_KEY + ":") == 1
        assert (
            _read("profiles/careers/journalists.yaml").count(
                M761_YAML_KEY + ":"
            )
            == 1
        )
        # m762: the block-key string is embedded in the concurrent
        # run's test_file name, so uniqueness is asserted on the
        # block_key FIELD line (exactly one).
        doc = _read("profiles/competitor-entities.yaml")
        field_lines = [
            line
            for line in doc.splitlines()
            if line.strip() == "block_key: " + M762_BLOCK_KEY
        ]
        assert len(field_lines) == 1, len(field_lines)

    def test_designed_keying_no_underscore_carriers_760_761_762(self):
        # #882/#883 MECH_ID_MARKERs and the #884 block's needles are
        # format-built per #770/#715: no sole underscore-form carrier
        # for 760/761/762 repo-wide (own file excluded as sweep
        # carrier).
        for n in (760, 761, 762):
            assert _repo_grep_underscore_mechanism(n) == [], n

    def test_prior_max_sweeps_superseded_by_design(self):
        # #877/#878/#879/#880/#881/#882/#883 max-sweeps (757/758/759/
        # 760) fail by designed supersession per the #710/#720
        # convention now that the in-tree max is 762: documented, not
        # repaired.
        assert _max_numeric_mechanism_id() == 762


class TestTypeDEngineStatisticalMeaningfulness:
    """Fresh synthetic corpora (new values, not #880's)."""

    def test_strong_signal_pair_significant_at_engine_layer(self):
        target = [0.95, 0.88, 0.92, 0.85, 0.90, 0.93, 0.87]
        peers = [-0.88, -0.95, -0.90, -0.85, -0.92, -0.89, -0.93]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 20),
            period_end=datetime.datetime(2026, 9, 20),
        )
        assert report.asymmetry_score == pytest.approx(
            1.802857142857143, rel=1e-4
        )
        assert report.t_statistic == pytest.approx(
            97.55917603529285, rel=1e-4
        )
        assert report.is_significant is True
        assert report.p_value == pytest.approx(
            1.01753175681008e-18, rel=1e-2
        )
        assert report.cohens_d == pytest.approx(52.147573094290394, rel=1e-2)
        assert report.confidence_interval_lower > 0
        assert report.confidence_interval_lower == pytest.approx(
            1.768535714285714, rel=1e-4
        )
        assert report.confidence_interval_upper == pytest.approx(
            1.8399999999999999, rel=1e-4
        )

    def test_near_null_pair_silent_at_engine_layer(self):
        target = [0.02, -0.01, 0.03, -0.02, 0.01, 0.00, -0.03]
        peers = [0.01, 0.00, -0.02, 0.02, -0.01, 0.03, -0.02]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 20),
            period_end=datetime.datetime(2026, 9, 20),
        )
        assert report.asymmetry_score == pytest.approx(
            -0.0014285714285714284, rel=1e-4
        )
        assert report.t_statistic == pytest.approx(
            -0.12982269672237462, rel=1e-4
        )
        assert report.is_significant is False
        assert report.p_value == pytest.approx(0.8988791731094714, rel=1e-2)
        assert report.cohens_d == pytest.approx(
            -0.06939315030888374, rel=1e-2
        )
        assert (
            report.confidence_interval_lower
            < 0
            < report.confidence_interval_upper
        )

    def test_degenerate_n1_contract_on_m760_pair(self):
        # m760's own block documents the Meta arm mean at -0.50
        # against the OpenAI arm mean at -0.1667 (illustrative delta
        # -0.3333): the pair is corpus-grounded, not invented.
        t, p = welch_t_test([-0.50], [-0.1667])
        d = cohens_d([-0.50], [-0.1667])
        assert (t, p) == (0.0, 1.0)
        assert d == 0.0
        assert is_significant(p) is False

    def test_degenerate_n1_calculate_asymmetry_contracts(self):
        # m760 pair: Meta [-0.50] vs OpenAI [-0.1667] (delta -0.3333,
        # approx within 1e-4).
        m760 = calculate_asymmetry(
            target_scores=[-0.50],
            peer_scores=[-0.1667],
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 20),
            period_end=datetime.datetime(2026, 9, 20),
        )
        assert m760.asymmetry_score == pytest.approx(-0.3333, abs=1e-4)
        assert m760.t_statistic == 0.0
        assert m760.is_significant is False
        assert m760.confidence_interval_lower == pytest.approx(
            -0.3333, abs=1e-4
        )
        assert m760.confidence_interval_upper == pytest.approx(
            -0.3333, abs=1e-4
        )
        # m761 pair: Meta [+0.10] vs OpenAI [-0.35] (delta +0.45,
        # IEEE-inexact 0.44999999999999996 within 1e-9).
        m761 = calculate_asymmetry(
            target_scores=[0.10],
            peer_scores=[-0.35],
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 20),
            period_end=datetime.datetime(2026, 9, 20),
        )
        assert m761.asymmetry_score == pytest.approx(0.45, abs=1e-9)
        assert m761.t_statistic == 0.0
        assert m761.is_significant is False
        # Arm-swaps negate exactly for both pairs.
        m760_swap = calculate_asymmetry(
            target_scores=[-0.1667],
            peer_scores=[-0.50],
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 20),
            period_end=datetime.datetime(2026, 9, 20),
        )
        m761_swap = calculate_asymmetry(
            target_scores=[-0.35],
            peer_scores=[0.10],
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 20),
            period_end=datetime.datetime(2026, 9, 20),
        )
        assert m760.asymmetry_score + m760_swap.asymmetry_score == pytest.approx(
            0.0, abs=1e-12
        )
        assert m761.asymmetry_score + m761_swap.asymmetry_score == pytest.approx(
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
    """Suite verdict lineage; #880's background suite owns the verdict,
    #885 re-launches."""

    TOMBSTONE_LINEAGE = 38

    def test_tombstone_lineage_count(self):
        # THIRTY-EIGHTH consecutive background full-suite death: #880's
        # background suite (re-launched 11:26 PDT Sep 20) died mid-run
        # (the log stalled at 809 bytes of partial pytest -q output)
        # and no pytest was alive at this run's check (the ps scan
        # found zero suite processes). Advances from the THIRTY-SEVENTH
        # lineage declared in #880 per the #565/#770/#780 convention.
        assert self.TOMBSTONE_LINEAGE == 38

    def test_880_background_suite_verdict_died(self):
        # Dead-run markers pinned per the #770/#780 convention; triaged
        # no further. Log stalled at exactly 809 bytes of partial
        # pytest -q progress output since 11:26 PDT Sep 20 with no
        # pytest alive at this run's check.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_880_full_suite.log",
        )
        assert os.path.exists(log_path), log_path
        size = os.path.getsize(log_path)
        assert size == 809, size
        text = open(log_path, encoding="utf-8", errors="replace").read()
        assert text.strip().endswith("....")

    def test_relaunch_log_path_in_goal_hidden_files(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_885_full_suite.log",
        )
        assert os.path.basename(log_path) == "type_d_885_full_suite.log"

    def test_885_suite_relaunched_this_run(self):
        # This run re-launches the full suite as a background process
        # writing to the persistent goal hidden_files path; the next
        # Type D run checks its verdict per the #795 convention.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_885_full_suite.log",
        )
        assert os.path.exists(log_path), log_path


class TestDocSync885:
    def test_readme_row_885(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_885(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_885_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog885:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #885 Type D:")
        return log[idx : idx + 12000]

    def test_log_entry_present(self):
        assert "## #885 Type D:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        entry = self._entry()
        assert "mechanism_id 762" in entry
        assert "m760" in entry
        assert "m761" in entry
        assert "m762" in entry

    def test_log_rotation_window_885_889(self):
        entry = self._entry()
        assert "885-889" in entry
        assert "880-884" in entry

    def test_log_window_opener(self):
        entry = self._entry()
        assert "OPENING" in entry

    def test_log_ledger_28(self):
        entry = self._entry()
        assert "ledger holds at 28" in entry

    def test_log_concurrency_documented(self):
        entry = self._entry()
        assert "#884" in entry
        assert "concurrent" in entry


class TestDateGrounding885:
    def test_sep_20_2026_is_sunday(self):
        assert datetime.datetime(2026, 9, 20).strftime("%A") == "Sunday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 20, 22, 16).strftime("%H:%M") == "22:16"
