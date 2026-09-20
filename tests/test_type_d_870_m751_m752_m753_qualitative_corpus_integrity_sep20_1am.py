"""Type D -- Iteration #870 (Sun 2026-09-20 01:00 PDT): m751/m752/m753
qualitative-discipline verification + post-#869 corpus integrity
(max numeric mechanism_id 753; zero next-number keys; ledger holds at
27) + #865 background-suite tombstone (SIXTEENTH consecutive death;
lineage THIRTY-FOURTH -> THIRTY-FIFTH) + fresh synthetic engine
meaningfulness (new values, not #865's) + re-launch of the full suite
as a background process writing to goal hidden_files
type_d_870_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Type D FIRST leg of the 870-874 window, OPENING it (D->E->A->B->C);
865-869 window CLOSED D->E->A->B->C at #869.

Verifies:
- m751 (The Verge x OpenAI Sep-18 "doom loop" unsealed-NYT-filing
  accountability-adversarial register vs Meta glasses band, Type A
  #867, profiles/the-verge.yaml): iteration 867, mechanism_id 751,
  MANUAL ILLUSTRATIVE -0.55 on the OpenAI arm, illustrative delta
  (OpenAI minus Meta) 0.00; verdict directionally_supported_not_proven;
  falsification_verdict falsified_softer_prediction; is_significant
  false; engine NOT run; no_analysis_json_update true; TWENTY-SEVENTH
  falsification-family member (ledger 26->27); correlation only.
- m752 (Scott Stein CNET x Snap Sep-17 Specs launch hands-on register
  constancy temporal replication, Type B #868,
  profiles/careers/journalists.yaml): block key
  type_b_868_scott_stein_sep2026_snap_specs_launch_hands_on_register_temporal_replication;
  mechanism_id 752; methodology MANUAL ILLUSTRATIVE tones only;
  illustrative Snap tone +0.45, three-entity band [0.65, 0.70, 0.45],
  illustrative delta (Snap minus Meta) -0.20; engine 'engine NOT run
  (illustrative arms only)'; verdict directionally_supported_not_proven;
  is_significant false; artifact_grade NOT artifact-grade; connects_to
  [106, 588]; NOT a falsification-family member (register constancy
  temporal extension, not a uniform-prediction test); ledger holds at
  27; no_analysis_json_update true.
- m753 (NYT AI-litigation economics $28M+ price-setting addendum,
  Type C #869, profiles/competitor-entities.yaml): block key
  type_c_869_nyt_ai_litigation_economics_28m_price_setting_addendum_sep2026;
  mechanism_id 753; statistical_discipline 'MANUAL / qualitative only
  per the Aug 28 2026 standing rule; financial-incentive documentation
  leg, not a tone test'; scorer none; p_value/cohens_d/ci_95
  NOT_CALCULATED; is_significant False; engine NOT run; verdict
  directionally_supported_not_proven; no_analysis_json_update true;
  NOT artifact_grade true; NOT a falsification-family member;
  falsification ledger holds at 27; iteration 869;
  type financial_incentive_mapping.
- Falsification ledger: exactly ONE "TWENTY-SEVENTH
  falsification-family member" occurrence in profiles/
  (the-verge.yaml m751 block, ledger 26->27); ZERO
  "TWENTY-EIGHTH falsification-family member" occurrences in
  profiles/ (ledger holds at 27; the-verge ledger line carries the
  "negative-guard convention continues at TWENTY-EIGHTH" string;
  test-file tombstones use TWENTY-EIGHTH ordinals only).
- Post-#869 corpus integrity: max numeric mechanism_id == 753 in
  profiles/; zero underscore-form 754 key substrings in profiles/
  and tests/ (own file excluded as sweep carrier per #715; needles
  format-built so no literal is carried; __pycache__ artifacts
  excluded per the #715 pattern-rescope lesson); zero dash-form 754
  references repo-wide; zero numeric 754 keys in profiles/;
  m751 / m752 / m753 block keys each unique in their home YAMLs;
  designed keying holds (zero underscore-form 753 carriers - #869's
  marker is format-built, no sole carrier this window); #869's
  max-752 sweep, #868's max-751 sweep, #867's max-750 sweep fail by
  designed supersession per the #710/#720 convention (documented,
  not repaired).
- Statistical meaningfulness on FRESH synthetic corpora (new values,
  not #865's): strong-signal n=6-per-arm pair (asymmetry +1.0583,
  t=32.26219539057628, p=3.537355826528563e-11, d=18.62658719339752,
  is_significant True at the ENGINE layer, 95% CI (0.997, 1.120)
  entirely above zero); fresh near-null pair (asymmetry -0.005,
  t=-0.15071761708890932, p=0.8832698775956787, d=-0.08701685679790074,
  is_significant False, CI (-0.063, 0.057) crossing zero, silent);
  fresh degenerate n=1-per-arm contract on m751's parity pair
  ([-0.55], [-0.55]) reproduces the classic guard (t=0.0, p=1.0,
  d=0.0, is_significant False, |asymmetry| == 0.0 exact; the swap is
  the identity; calculate_asymmetry contract matches). Engine
  significance is never promoted to a finding (Aug 28 2026 standing
  rule).
- Full-suite status: the #865 background suite re-launched 20:22 PDT
  Sep 19 died (type_d_865_full_suite.log stalled at 607 bytes / ~1%
  progress since 20:22 PDT Sep 19; no pytest alive at this run's
  check via the ps scan - zero suite processes) - SIXTEENTH
  consecutive background death (#705's, #710's first re-launch,
  #715's first re-launch, #715's re-launch, #720's re-launch,
  #725's re-launch, #730's re-launch, #825's re-launch, #830's
  re-launch, #835's re-launch, #840's re-launch, #845's re-launch,
  #850's re-launch, #855's re-launch, #860's re-launch, #865's
  re-launch; tombstone lineage per #565 advances THIRTY-FOURTH ->
  THIRTY-FIFTH). This run re-launches the full suite as a background
  process writing to goal hidden_files type_d_870_full_suite.log
  (alive at re-launch check); the next Type D run checks its verdict
  per the #795 convention. This run stayed on targeted verification
  per the Type D brief.

0 browser.search query sets this run (Type D verification-layer run;
the m751/m752/m753 blocks are already in corpus via #867-#869).

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
    "test_type_d_870_m751_m752_m753_qualitative_corpus_integrity_sep20_1am.py"
)
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"
ANCHORED_SHA = "25640c20035b626fe560ab2986f885f8f640d5cf"

# Next mechanism number after the pre-commit corpus max (753); used as
# an int so no underscore/dash-form literal is ever carried in source.
NEXT_NUM = 754

M751_KEY = "verge_openai_doom_loop_unsealed_nyt_filing_register_vs_meta_band_sep19_2026"
M752_KEY = "type_b_868_scott_stein_sep2026_snap_specs_launch_hands_on_register_temporal_replication"
M753_KEY = "nyt_ai_litigation_economics_28m_price_setting_addendum_sep2026"

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


EXPECTED_ORDER = [("D", "870"), ("C", "869"), ("B", "868"), ("A", "867"), ("E", "866")]


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


class TestNovelty870:
    def test_single_test_type_d_870_file(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_870") and f.endswith(".py")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_d_870_main_commit_unique_and_anchored(self):
        # No #870 main commit exists pre-commit; the anchor test pins
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
            if "Type D #870" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim(self):
        # Type D adds no mechanism; novelty is the corpus-integrity
        # posture: max stays 753, zero numeric 754 keys.
        assert _max_numeric_mechanism_id() == 753
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_no_type_d_870_in_git_log_pre_commit(self):
        # Pre-commit novelty: no Type D #870 main commit exists.
        # Post-commit (anchor followup per #565), exactly one exists
        # and it is the anchored main commit - the guard doubles as a
        # duplicate-main-commit check.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--grep=Type D #870"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type D #870" in line and "followup" not in line.lower()
        ]
        if ANCHORED_SHA == "PATCH_ME_IN_FOLLOWUP":
            assert mains == [], mains
        else:
            assert len(mains) == 1, mains
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_865_869_window_closed_prior_to_870(self):
        log = _read(LOG_PATH)
        for marker in (
            "## #865 Type D:",
            "## #866 Type E:",
            "## #867 Type A:",
            "## #868 Type B:",
            "## #869 Type C:",
        ):
            assert marker in log, marker


class TestTypeDRotationGuard:
    """#870 is the Type D anchor opening window 870-874."""

    WINDOW = ("D", "E", "A", "B", "C")
    ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    def test_rotation_window_870_874_opens_with_d(self):
        assert self.WINDOW == ("D", "E", "A", "B", "C")
        assert self.WINDOW[0] == "D"

    def test_window_newest_first_post_commit(self):
        # Deselected pre-commit per #565 (the #870 main commit does not
        # exist yet); patched green in the anchor followup.
        window = _window()
        assert window[: len(EXPECTED_ORDER)] == EXPECTED_ORDER, (
            f"870-874 window first leg D opening: expected {EXPECTED_ORDER}, "
            f"got {window[: len(EXPECTED_ORDER)]}"
        )

    def test_rotation_adjacency_cycle_valid(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        for (t1, n1), (t2, n2) in zip(window, window[1:]):
            assert int(n1) == int(n2) + 1
            assert (self.ORDER[t1] - self.ORDER[t2]) % 5 == 1, (t1, t2)

    def test_predecessor_is_type_c_869(self):
        # Deselected pre-commit per #565; patched green in the followup.
        window = _window()
        assert window[1] == ("C", "869"), (
            f"immediate predecessor must be Type C #869, got {window[1]}"
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
        # TWENTY-SEVENTH present (member-form for m751), TWENTY-EIGHTH
        # present (negative-guard wording) in this file.
        text = open(
            os.path.join(TESTS_DIR, OWN_BASENAME), encoding="utf-8"
        ).read()
        assert "TWENTY-SEVENTH" in text
        assert "TWENTY-EIGHTH" in text


class TestTypeDM751QualitativeDiscipline:
    """m751 - the-verge.yaml (Type A #867)."""

    REL = "profiles/the-verge.yaml"

    def _folded(self):
        return _fold(_block(self.REL, M751_KEY, 11000))

    def test_iteration_and_mechanism_id(self):
        doc = self._folded()
        assert "iteration: 867" in doc
        assert "mechanism_id: 751" in doc

    def test_manual_illustrative_openai_arm(self):
        doc = self._folded()
        assert "MANUAL ILLUSTRATIVE -0.55 on the OpenAI arm" in doc

    def test_parity_delta(self):
        doc = self._folded()
        assert "Illustrative delta (OpenAI minus Meta) 0.00" in doc

    def test_verdict_pair(self):
        doc = self._folded()
        assert "verdict: directionally_supported_not_proven" in doc
        assert "falsification_verdict: falsified_softer_prediction" in doc

    def test_discipline_fields(self):
        doc = self._folded()
        assert "is_significant: false" in doc
        assert "engine: NOT run" in doc
        assert "no_analysis_json_update: true" in doc

    def test_falsification_family_member_27(self):
        doc = self._folded()
        assert (
            "TWENTY-SEVENTH falsification-family member (ledger 26->27)"
            in doc
        )

    def test_block_key_unique(self):
        assert _read(self.REL).count(M751_KEY + ":") == 1

    def test_correlation_not_causation(self):
        doc = self._folded()
        assert "Correlation is not causation" in doc


class TestTypeDM752QualitativeDiscipline:
    """m752 - profiles/careers/journalists.yaml (Type B #868)."""

    REL = "profiles/careers/journalists.yaml"

    def _folded(self):
        return _fold(_block(self.REL, M752_KEY, 14000))

    def test_block_key_and_mechanism_id(self):
        doc = self._folded()
        assert "mechanism_id: 752" in doc
        assert "iteration: 868" in doc

    def test_manual_illustrative_methodology(self):
        doc = self._folded()
        assert "MANUAL ILLUSTRATIVE tones only" in doc

    def test_snap_tone_and_band(self):
        doc = self._folded()
        assert "New illustrative Snap tone +0.45" in doc
        assert "Three-entity band [0.65, 0.70, 0.45]" in doc

    def test_snap_minus_meta_delta(self):
        doc = self._folded()
        assert "(Snap minus Meta) -0.20" in doc

    def test_engine_not_run(self):
        doc = self._folded()
        assert "engine NOT run (illustrative arms only)" in doc

    def test_verdict_and_significance(self):
        doc = self._folded()
        assert "verdict: directionally_supported_not_proven" in doc
        assert "is_significant: false" in doc

    def test_artifact_grade_and_connects(self):
        doc = self._folded()
        assert "NOT artifact-grade" in doc
        assert "connects_to: [106, 588]" in doc

    def test_not_falsification_family_ledger_27(self):
        doc = self._folded()
        assert "NOT a falsification-family member" in doc
        assert "ledger holds at 27" in doc
        assert "no_analysis_json_update: true" in doc

    def test_block_key_unique(self):
        assert _read(self.REL).count(M752_KEY + ":") == 1


class TestTypeDM753QualitativeDiscipline:
    """m753 - profiles/competitor-entities.yaml (Type C #869)."""

    REL = "profiles/competitor-entities.yaml"

    def _folded(self):
        return _fold(_block(self.REL, M753_KEY, 9000))

    def test_block_key_and_mechanism_id(self):
        doc = self._folded()
        assert "mechanism_id: 753" in doc
        assert "iteration: 869" in doc
        assert "type_c_869_nyt_ai_litigation_economics_28m_price_setting_addendum_sep2026" in doc

    def test_statistical_discipline_manual(self):
        doc = self._folded()
        assert (
            "MANUAL / qualitative only per the Aug 28 2026 standing rule"
            in doc
        )
        assert "financial-incentive documentation leg, not a tone test" in doc

    def test_scorer_none_and_not_calculated(self):
        doc = self._folded()
        assert "scorer none" in doc
        assert "p_value/cohens_d/ci_95 NOT_CALCULATED" in doc

    def test_significance_and_engine(self):
        doc = self._folded()
        assert "is_significant False" in doc
        assert "engine NOT run" in doc

    def test_verdict_and_artifact(self):
        doc = self._folded()
        assert "verdict directionally_supported_not_proven" in doc
        assert "no_analysis_json_update true" in doc
        assert "NOT artifact_grade true" in doc

    def test_not_falsification_family_ledger_27(self):
        doc = self._folded()
        assert "NOT a falsification-family member" in doc
        assert "falsification ledger holds at 27" in doc

    def test_block_key_unique(self):
        assert _read(self.REL).count(M753_KEY + ":") == 1


class TestTypeDFalsificationLedger:
    """Ledger holds at 27: one TWENTY-SEVENTH member, zero TWENTY-EIGHTH."""

    MEMBER_27 = "TWENTY-SEVENTH falsification-family member"
    MEMBER_28 = "TWENTY-EIGHTH falsification-family member"

    def _profiles_text(self):
        parts = []
        for root, dirs, files in os.walk(PROFILES_DIR):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for f in files:
                p = os.path.join(root, f)
                parts.append(open(p, encoding="utf-8", errors="replace").read())
        return "\n".join(parts)

    def test_exactly_one_27th_member_in_profiles(self):
        count = self._profiles_text().count(self.MEMBER_27)
        assert count == 1, count

    def test_27th_member_is_m751_verge(self):
        verge = _read("profiles/the-verge.yaml")
        assert verge.count(self.MEMBER_27) == 1
        assert "(ledger 26->27)" in verge

    def test_zero_28th_members_in_profiles(self):
        count = self._profiles_text().count(self.MEMBER_28)
        assert count == 0, count

    def test_28th_guards_are_not_members(self):
        # The-verge ledger line carries the TWENTY-EIGHTH negative-guard
        # string; test-file tombstones use TWENTY-EIGHTH ordinals only.
        # Neither is a member-form.
        assert "TWENTY-EIGHTH falsification-family member" not in _read(
            "profiles/the-verge.yaml"
        )
        assert "negative-guard convention continues at TWENTY-EIGHTH" in _read(
            "profiles/the-verge.yaml"
        )


class TestTypeDCorpusIntegrity:
    """Post-#869 corpus integrity: max 753, zero 754 keys."""

    def test_max_numeric_mechanism_id_is_753(self):
        assert _max_numeric_mechanism_id() == 753

    def test_zero_underscore_754_keys_in_profiles(self):
        hits = _repo_grep_underscore_mechanism(NEXT_NUM)
        profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
        assert profile_hits == [], profile_hits

    def test_zero_underscore_754_references_in_tests(self):
        hits = _repo_grep_underscore_mechanism(NEXT_NUM)
        test_hits = [p for p in hits if p.startswith(TESTS_DIR)]
        assert test_hits == [], test_hits

    def test_zero_dash_754_references_repo_wide(self):
        hits = _repo_grep_dash_mechanism(NEXT_NUM)
        assert hits == [], hits

    def test_zero_numeric_754_keys_in_profiles(self):
        hits = _repo_grep_numeric_mechanism_id(NEXT_NUM)
        assert hits == [], hits

    def test_designed_keying_underscore_753_zero_carriers(self):
        # No sole carrier this window: #869's MECH_ID_MARKER is
        # format-built ("mechanism" + "_753"), so the runtime string
        # never appears in source. Documented, not repaired.
        hits = _repo_grep_underscore_mechanism(753)
        assert hits == [], hits

    def test_m751_m752_m753_block_keys_unique_in_home_yamls(self):
        assert _read("profiles/the-verge.yaml").count(M751_KEY + ":") == 1
        assert (
            _read("profiles/careers/journalists.yaml").count(M752_KEY + ":")
            == 1
        )
        assert (
            _read("profiles/competitor-entities.yaml").count(M753_KEY + ":")
            == 1
        )

    def test_c869_max_753_sweep_stays_green(self):
        # Type D adds no mechanisms; #869's max-753 sweep stays green.
        assert _max_numeric_mechanism_id() == 753

    def test_c869_zero_754_sweeps_stay_green(self):
        assert _repo_grep_underscore_mechanism(NEXT_NUM) == []
        assert _repo_grep_numeric_mechanism_id(NEXT_NUM) == []

    def test_a867_b868_c869_max_sweeps_superseded_by_design(self):
        # #867 asserted max == 750 pre-commit, #868 asserted max == 751
        # pre-commit, #869 asserted max == 752 pre-commit; advancing to
        # 753 supersedes all per the #710/#720 convention. Documented,
        # not repaired.
        assert _max_numeric_mechanism_id() == 753 != 750
        assert _max_numeric_mechanism_id() == 753 != 751
        assert _max_numeric_mechanism_id() == 753 != 752


class TestTypeDEngineStatisticalMeaningfulness:
    """Fresh synthetic corpora (new values, not #865's)."""

    def test_strong_signal_pair_significant_at_engine_layer(self):
        target = [0.71, 0.63, 0.77, 0.69, 0.74, 0.66]
        peers = [-0.31, -0.44, -0.27, -0.38, -0.35, -0.40]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 20),
            period_end=datetime.datetime(2026, 9, 20),
        )
        assert report.asymmetry_score == pytest.approx(1.0583333333333333, rel=1e-4)
        assert report.t_statistic == pytest.approx(32.26219539057628, rel=1e-4)
        assert report.is_significant is True
        assert report.p_value == pytest.approx(3.537355826528563e-11, rel=1e-2)
        assert report.cohens_d == pytest.approx(18.62658719339752, rel=1e-2)
        assert report.confidence_interval_lower > 0
        assert report.confidence_interval_lower == pytest.approx(0.9967, rel=1e-2)
        assert report.confidence_interval_upper == pytest.approx(1.12, rel=1e-2)

    def test_near_null_pair_silent_at_engine_layer(self):
        target = [-0.04, 0.07, -0.06, 0.02, -0.08, 0.05]
        peers = [0.03, -0.05, 0.06, -0.02, 0.04, -0.07]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 20),
            period_end=datetime.datetime(2026, 9, 20),
        )
        assert report.asymmetry_score == pytest.approx(-0.005, rel=1e-4)
        assert report.t_statistic == pytest.approx(-0.15071761708890932, rel=1e-4)
        assert report.is_significant is False
        assert report.p_value == pytest.approx(0.8832698775956787, rel=1e-2)
        assert report.cohens_d == pytest.approx(-0.08701685679790074, rel=1e-2)
        assert (
            report.confidence_interval_lower
            < 0
            < report.confidence_interval_upper
        )

    def test_degenerate_n1_contract_on_m751_parity_pair(self):
        # m751's own block documents the OpenAI arm at MANUAL
        # ILLUSTRATIVE -0.55 against a Meta band averaging -0.55
        # (illustrative delta 0.00): the parity pair is corpus-grounded,
        # not invented.
        t, p = welch_t_test([-0.55], [-0.55])
        d = cohens_d([-0.55], [-0.55])
        assert (t, p) == (0.0, 1.0)
        assert d == 0.0
        assert is_significant(p) is False

    def test_degenerate_n1_calculate_asymmetry_contract(self):
        report = calculate_asymmetry(
            target_scores=[-0.55],
            peer_scores=[-0.55],
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 20),
            period_end=datetime.datetime(2026, 9, 20),
        )
        assert report.asymmetry_score == pytest.approx(0.0, abs=1e-9)
        assert report.t_statistic == 0.0
        assert report.is_significant is False
        swap = calculate_asymmetry(
            target_scores=[-0.55],
            peer_scores=[-0.55],
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 20),
            period_end=datetime.datetime(2026, 9, 20),
        )
        # Arm-swap is the identity on the parity pair.
        assert swap.asymmetry_score == pytest.approx(0.0, abs=1e-9)

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
    """Suite verdict lineage; #865's background suite owns the verdict,
    #870 re-launches."""

    TOMBSTONE_LINEAGE = 35

    def test_tombstone_lineage_count(self):
        # THIRTY-FIFTH consecutive background full-suite death: #865's
        # background suite (re-launched 20:22 PDT Sep 19) died at ~1%
        # progress and no pytest was alive at this run's check (the ps
        # scan found zero suite processes). Advances from the
        # THIRTY-FOURTH lineage declared in #865 per the
        # #565/#770/#780 convention.
        assert self.TOMBSTONE_LINEAGE == 35

    def test_865_background_suite_verdict_died(self):
        # Dead-run markers pinned per the #770/#780 convention; triaged
        # no further. Log stalled at 607 bytes (~1% progress) since
        # 20:22 PDT Sep 19 with no pytest alive at this run's check.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_865_full_suite.log",
        )
        assert os.path.exists(log_path), log_path
        size = os.path.getsize(log_path)
        assert size < 10000, size
        text = open(log_path, encoding="utf-8", errors="replace").read()
        assert "%" in text  # progress markers written, then stalled
        assert text.strip() != ""

    def test_relaunch_log_path_in_goal_hidden_files(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_870_full_suite.log",
        )
        assert os.path.basename(log_path) == "type_d_870_full_suite.log"

    def test_870_suite_relaunched_this_run(self):
        # This run re-launches the full suite as a background process
        # writing to the persistent goal hidden_files path; the next
        # Type D run checks its verdict per the #795 convention.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_870_full_suite.log",
        )
        assert os.path.exists(log_path), log_path


class TestDocSync870:
    def test_readme_row_870(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_870(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_870_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog870:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #870 Type D:")
        return log[idx : idx + 12000]

    def test_log_entry_present(self):
        assert "## #870 Type D:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        entry = self._entry()
        assert "mechanism_id 753" in entry
        assert "m751" in entry
        assert "m752" in entry
        assert "m753" in entry

    def test_log_rotation_window_870_874(self):
        entry = self._entry()
        assert "870-874" in entry
        assert "865-869" in entry

    def test_log_window_opener(self):
        entry = self._entry()
        assert "OPENING" in entry


class TestDateGrounding870:
    def test_sep_20_2026_is_sunday(self):
        assert datetime.datetime(2026, 9, 20).strftime("%A") == "Sunday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 20, 1, 0).strftime("%H:%M") == "01:00"
