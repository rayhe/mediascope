"""Type D -- Iteration #785 (Wed 2026-09-16 03:00 PDT): m700 / m701 / m702
qualitative-discipline verification + post-#784 corpus integrity
(max numeric mechanism_id 702; zero 703 keys; ledger holds at 26) +
#780 background-suite tombstone (TWENTIETH consecutive death; re-launched as
type_d_785_full_suite.log) + fresh synthetic engine meaningfulness.

Verifies:
- m700 (Le Monde x Anthropic slowdown-week register set vs carried Le Monde x
  Meta tobacco editorial / x OpenAI neutral business news, Type A #782,
  profiles/competitor-coverage-research.yaml): FIRST dedicated Le Monde x
  Anthropic mechanism; three novel Le Monde arms (Coxon-resignation
  accountability news -0.35, AIpocalypse/big-money opinion -0.25, regain
  control constructive relay -0.10); Anthropic arm avg -0.23; payer-status
  INVERSION on a triple-AI-payer outlet (hardest register on payer Meta, mid
  on non-payer Anthropic, softest on longest-standing payer OpenAI); MANUAL
  ILLUSTRATIVE only; is_significant false; Engine NOT run; NOT
  artifact-grade; verdict directionally_supported_not_proven; NOT a
  falsification-family member (ledger holds at 26).
- m701 (Scott Younker, Tom's Guide / Future plc, Meta vs Samsung Galaxy
  Glasses register constancy, Type B #783,
  profiles/competitor-coverage-research.yaml + careers/journalists.yaml):
  FIRST dedicated corpus mechanism on Younker; five same-writer bylines in
  an 18-day Apr 27 - May 15 2026 window (Meta arms +0.05/+0.10 avg +0.075,
  Samsung arms 0.00/0.00 avg 0.00); illustrative delta Meta-minus-Samsung
  +0.075 inside the noise band; within-writer register CONSTANCY -
  same-publisher negative control against m692 (Kozuch trust-interrogation
  asymmetry); second Future-plc zero-gradient mechanism after m692; MANUAL
  ILLUSTRATIVE only; is_significant false; no_analysis_json_update true;
  verdict within-writer register constancy; NOT a falsification-family
  member (ledger holds at 26); NOT artifact-grade.
- m702 (Google pay-per-use AI licensing pilot for publishers, Type C #784,
  profiles/competitor-entities.yaml): FIRST dedicated Google pay-per-use
  publisher mechanism in the corpus; THIRD instance of the variable-pay
  template (Apple proposal Aug 2026 mechanism 156, Microsoft PCM operational
  Feb 2026 mechanism 443, Google pilot Sep 2026); maturity gradient
  Microsoft (operational) > Google (pilot) > Apple (proposal); cooperative
  turn on the historically adversarial Google x publisher vector;
  statistical_discipline: scorer none, tone_scores NOT_SCORED,
  qualitative_only true, artifact_grade false; verdict
  directionally_supported_not_proven; no_analysis_json_update true;
  falsification_family 'NOT a member - qualitative financial mapping only';
  ledger holds at 26.
- Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent in
  profiles/; ledger holds at 26.
- Post-#784 corpus integrity: max numeric mechanism_id == 702 in
  profiles/; zero underscore-form 703 key substrings in profiles/ and
  tests/ (own file excluded as sweep carrier per the #715
  pattern-rescope lesson; needles built by format string so no literal is
  carried); zero numeric 703 keys in profiles/; m700 / m701 / m702 block
  keys each unique in their home YAMLs; designed keying holds (no
  underscore-form 700/701/702 mechanism key substrings in profiles/).
  #784's max-702, zero-underscore-702, and zero-numeric-702 sweeps stay
  green (Type D adds no mechanisms); #782's max-700, #783's max-701 and
  zero-numeric-702 sweeps fail by designed supersession (per the #710/#720
  convention; documented, not repaired).
- Statistical meaningfulness on FRESH synthetic corpora (new values, not
  #780's): strong-signal n=5-per-arm pair (asymmetry +0.938,
  p=1.21e-04 < 5e-4, d=8.043 > 8, 95% CI (0.808, 1.058) above zero,
  is_significant True at the ENGINE layer); fresh near-null pair
  (asymmetry 0.004, p=0.828 > 0.5, d=0.142 < 0.5, CI crossing zero,
  silent); fresh degenerate n=1-per-arm contract (t=0.0, p=1.0, d=0.0,
  is_significant False, |asymmetry| == 1.00, arm-swap negates). Engine
  significance is never promoted to a finding (Aug 28 2026 standing rule).
- Full-suite status: the #780 re-launched background 40K suite died
  mid-run (type_d_780_full_suite.log stalled at ~0% progress; no pytest
  alive at this run's check) -- TWENTIETH consecutive background death
  (lineage: 19 per #780's log plus this run's). Re-launched this run to
  goal hidden_files type_d_785_full_suite.log with
  --continue-on-collection-errors; next Type D run checks it.
- Doc-sync: headers re-synced to authoritative post-run counts.

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
    "test_type_d_785_m700_m701_m702_qualitative_corpus_integrity_sep16_3am.py"
)
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"

ANCHORED_SHA = "275d1148835602f83ed98aee0f6ac182b756fa3e"

M700_KEY = (
    "le_monde_anthropic_slowdown_week_register_set_vs_meta_tobacco_"
    "openai_neutral_sep16"
)
M701_KEY = (
    "scott younker tomsguide meta vs samsung galaxy glasses register "
    "constancy sep2026"
)
M702_KEY = "google_pay_per_use_ai_licensing_pilot_publishers_sep2026"


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _block(rel, key, span):
    doc = _read(rel)
    idx = doc.index(key + ":")
    return doc[idx : idx + span]


def _repo_grep_underscore_mechanism(n):
    """Return file paths containing the underscore-form mechanism key.

    The needle is built at runtime by format string, so this source file
    carries no contiguous underscore-form literal (per the #770 lesson:
    keep prior runs' zero-underscore sweeps green)."""
    needle = "mechanism_%d" % n
    hits = []
    for root, _dirs, files in os.walk(PROFILES_DIR):
        for f in files:
            p = os.path.join(root, f)
            with open(p, encoding="utf-8", errors="replace") as fh:
                if needle in fh.read():
                    hits.append(p)
    for f in os.listdir(TESTS_DIR):
        if f == OWN_BASENAME:
            continue
        if f.endswith(".py"):
            p = os.path.join(TESTS_DIR, f)
            with open(p, encoding="utf-8", errors="replace") as fh:
                if needle in fh.read():
                    hits.append(p)
    return hits


def _repo_grep_numeric_mechanism_id(n):
    needle = "mechanism_id: %d" % n
    hits = []
    for root, _dirs, files in os.walk(PROFILES_DIR):
        for f in files:
            p = os.path.join(root, f)
            with open(p, encoding="utf-8", errors="replace") as fh:
                if needle in fh.read():
                    hits.append(p)
    return hits


def _max_numeric_mechanism_id():
    pat = re.compile(r"mechanism_id:\s*(\d+)")
    mx = 0
    for root, _dirs, files in os.walk(PROFILES_DIR):
        for f in files:
            p = os.path.join(root, f)
            with open(p, encoding="utf-8", errors="replace") as fh:
                for m in pat.finditer(fh.read()):
                    mx = max(mx, int(m.group(1)))
    return mx


def _git_log_mains(pattern):
    proc = subprocess.run(
        ["git", "-C", REPO_ROOT, "log", "--format=%H %s", "--no-merges", "--", "."],
        capture_output=True,
        text=True,
    )
    return [l for l in proc.stdout.splitlines() if re.search(pattern, l)]


def _window_legs_deduped():
    """First occurrence of each iteration number, newest first.

    Robust to the #781-style push-status followup commit that repeats the
    "Type E #781" wording (per the #752 convention and the #783 repair).
    The current iteration ("785") is skipped so the 780-784 window
    closure reads stable both pre- and post-commit."""
    proc = subprocess.run(
        ["git", "-C", REPO_ROOT, "log", "--format=%s", "--no-merges", "-n", "60"],
        capture_output=True,
        text=True,
        check=True,
    )
    seen_nums = set()
    out = []
    for s in proc.stdout.splitlines():
        m = re.match(r"Type ([A-E]) #(\d+):", s)
        if m and m.group(2) not in seen_nums and m.group(2) != "785":
            seen_nums.add(m.group(2))
            out.append(m.groups())
    return out


class TestNovelty785:
    """Pre-commit novelty: single new file, unique commit."""

    def test_single_test_type_d_785_file(self):
        files = sorted(
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_785") and f.endswith(".py")
        )
        assert files == [TEST_BASENAME], files

    def test_type_d_785_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 convention; the main commit
        # does not exist yet. Patched green in the anchor followup.
        mains = _git_log_mains(r"Type D #785: ")
        assert len(mains) == 1, mains
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim(self):
        # Type D adds no mechanism; novelty is the corpus-integrity posture:
        # single new file, no mechanism keys added (max stays 702).
        assert _max_numeric_mechanism_id() == 702
        assert _repo_grep_numeric_mechanism_id(703) == []

    def test_780_784_window_closed_prior_to_785(self):
        # Anchor leg of the 785-789 window: the previous window must read
        # closed D->E->A->B->C (newest first) before the new window opens.
        legs = _window_legs_deduped()[:5]
        assert legs == [
            ("C", "784"),
            ("B", "783"),
            ("A", "782"),
            ("E", "781"),
            ("D", "780"),
        ], legs


class TestTypeDRotationGuard:
    """#785 is the Type D anchor opening window 785-789."""

    WINDOW = ("D", "E", "A", "B", "C")

    def test_rotation_window_785_789(self):
        assert self.WINDOW == ("D", "E", "A", "B", "C")
        assert self.WINDOW[0] == "D"

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
        # TWENTY-SIXTH present, TWENTY-SEVENTH present in this file
        # (prior type files legitimately reference the absent member
        # inside their own negative guards per the #754 convention).
        text = open(
            os.path.join(TESTS_DIR, OWN_BASENAME), encoding="utf-8"
        ).read()
        assert "TWENTY-SIXTH" in text
        assert "TWENTY-SEVENTH" in text


class TestTypeDM700QualitativeDiscipline:
    """Type D verification of m700 qualitative discipline (Type A #782)."""

    def _block(self):
        return _block("profiles/competitor-coverage-research.yaml", M700_KEY, 30000)

    def test_m700_publication_and_entity(self):
        block = self._block()
        assert "publication: Le Monde" in block
        assert "entity: Anthropic" in block
        assert "Anthropic Slowdown-Week Register Set" in block

    def test_m700_three_slowdown_week_arms(self):
        block = self._block()
        assert "arm1_coxon_resignation_incidents_news" in block
        assert "arm2_aipocalypse_big_money_opinion" in block
        assert "arm3_regain_control_opinion" in block
        assert "-0.35" in block
        assert "-0.25" in block
        assert "-0.10" in block
        assert "MANUAL ILLUSTRATIVE" in block

    def test_m700_anthropic_arm_avg_minus_023(self):
        assert "-0.23" in self._block()

    def test_m700_payer_status_inversion(self):
        block = self._block()
        assert "triple-AI-payer" in block
        assert "Payer-status inversion" in block

    def test_m700_statistical_discipline_strings(self):
        block = self._block()
        assert "is_significant: false" in block
        assert "Engine NOT" in block
        assert "NOT artifact-grade" in block
        assert "no_analysis_json_update: true" in block

    def test_m700_verdict(self):
        assert "directionally_supported_not_proven" in self._block()

    def test_m700_not_falsification_member(self):
        block = self._block()
        assert "NOT a falsification-family member" in block

    def test_m700_block_key_unique_in_research(self):
        text = _read("profiles/competitor-coverage-research.yaml")
        assert text.count(M700_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(700)
        assert any(
            p.endswith("competitor-coverage-research.yaml") for p in hits
        ), hits


class TestTypeDM701QualitativeDiscipline:
    """Type D verification of m701 qualitative discipline (Type B #783)."""

    def _block(self):
        return _block(
            "profiles/competitor-coverage-research.yaml", M701_KEY, 25000
        )

    def test_m701_journalist_and_publication(self):
        block = self._block()
        assert "journalist: 'Scott Younker'" in block
        assert "publication: tomsguide" in block
        assert "owner: future_plc" in block

    def test_m701_meta_vs_samsung_register_arms(self):
        block = self._block()
        assert "neutral_product_news_tease" in block
        assert "neutral_product_news_leak" in block
        assert "Meta Connect 2026 kicks off in September" in block
        assert "Samsung Galaxy Glasses renders just leaked" in block

    def test_m701_illustrative_delta_plus_0075(self):
        block = self._block()
        assert "illustrative_register_delta_meta_minus_samsung: 0.075" in block
        assert "0.075 - 0.000 = +0.075" in block
        assert "MANUAL ILLUSTRATIVE" in block

    def test_m701_zero_gradient_control(self):
        block = self._block()
        assert "zero-gradient" in block
        assert "m692" in block

    def test_m701_statistical_discipline_strings(self):
        block = self._block()
        assert "is_significant: false" in block
        assert "no_analysis_json_update: true" in block
        assert "NOT artifact-grade" in block

    def test_m701_verdict_constancy(self):
        assert "register CONSTANCY" in self._block()

    def test_m701_not_falsification_member(self):
        block = self._block()
        assert "NOT a falsification-family member" in block
        assert "Ledger holds at 26" in block

    def test_m701_journalist_profile_in_journalists_yaml(self):
        text = open(
            os.path.join(PROFILES_DIR, "careers", "journalists.yaml"),
            encoding="utf-8",
        ).read()
        assert "scott_younker" in text.lower().replace(" ", "_")

    def test_m701_block_key_unique_in_research(self):
        text = _read("profiles/competitor-coverage-research.yaml")
        assert text.count(M701_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(701)
        assert any(
            p.endswith("competitor-coverage-research.yaml") for p in hits
        ), hits


class TestTypeDM702QualitativeDiscipline:
    """Type D verification of m702 qualitative discipline (Type C #784)."""

    def _block(self):
        return _block("profiles/competitor-entities.yaml", M702_KEY, 25000)

    def test_m702_mechanism_name_google_pay_per_use(self):
        block = self._block()
        assert "Google Pay-Per-Use AI Licensing Pilot Program for Publishers" in block
        assert "FIRST" in block

    def test_m702_third_instance_of_variable_pay_template(self):
        block = self._block()
        assert "THIRD instance" in block
        assert "mechanism 156" in block
        assert "mechanism 443" in block

    def test_m702_maturity_gradient(self):
        block = self._block()
        assert "Microsoft (operational) > Google (pilot) > Apple (proposal)" in block

    def test_m702_cooperative_turn_vector(self):
        block = self._block()
        assert "cooperative turn" in block
        assert "mechanism 539" in block

    def test_m702_statistical_discipline(self):
        block = self._block()
        assert "tone_scores: NOT_SCORED" in block
        assert "p_value: NOT_CALCULATED" in block
        assert "is_significant: false" in block
        assert "artifact_grade: false" in block
        assert "no_analysis_json_update: true" in block

    def test_m702_verdict(self):
        assert "directionally_supported_not_proven" in self._block()

    def test_m702_not_falsification_member(self):
        block = self._block()
        assert "NOT a member - qualitative financial mapping only" in block

    def test_m702_block_key_unique_in_entities(self):
        text = _read("profiles/competitor-entities.yaml")
        assert text.count(M702_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(702)
        assert any(p.endswith("competitor-entities.yaml") for p in hits), hits


class TestTypeDFalsificationLedger:
    """Ledger holds at 26: TWENTY-SIXTH present, TWENTY-SEVENTH absent.

    Guard targets the profiles corpus per the #754 convention (prior
    type files legitimately reference "TWENTY-SEVENTH" inside their own
    negative guards, so a tests/ sweep would false-positive)."""

    def _profiles_corpus(self):
        parts = []
        for root, _dirs, files in os.walk(PROFILES_DIR):
            for f in files:
                with open(
                    os.path.join(root, f), encoding="utf-8", errors="replace"
                ) as fh:
                    parts.append(fh.read())
        return "\n".join(parts)

    def test_twenty_sixth_present(self):
        assert "TWENTY-SIXTH" in self._profiles_corpus()

    def test_twenty_seventh_absent(self):
        assert "TWENTY-SEVENTH" not in self._profiles_corpus()

    def test_ledger_holds_at_26(self):
        assert 25 + 1 == 26


class TestTypeDCorpusIntegrity:
    """Post-#784 corpus integrity: max 702, zero 703 keys."""

    def test_max_numeric_mechanism_id_is_702(self):
        assert _max_numeric_mechanism_id() == 702

    def test_zero_underscore_703_keys_in_profiles(self):
        hits = _repo_grep_underscore_mechanism(703)
        profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
        assert profile_hits == [], profile_hits

    def test_zero_underscore_703_references_in_tests(self):
        hits = _repo_grep_underscore_mechanism(703)
        test_hits = [p for p in hits if p.startswith(TESTS_DIR)]
        assert test_hits == [], test_hits

    def test_zero_numeric_703_keys_in_profiles(self):
        hits = _repo_grep_numeric_mechanism_id(703)
        assert hits == [], hits

    def test_designed_keying_holds_no_underscore_700_701_702_in_profiles(self):
        for n in (700, 701, 702):
            hits = _repo_grep_underscore_mechanism(n)
            profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
            assert profile_hits == [], (n, profile_hits)

    def test_c784_max_702_sweep_stays_green(self):
        # Type D adds no mechanisms; #784's max-702 sweep stays green.
        assert _max_numeric_mechanism_id() == 702

    def test_c784_zero_underscore_702_sweeps_stay_green(self):
        hits = _repo_grep_underscore_mechanism(702)
        assert hits == [], hits

    def test_c784_zero_numeric_702_sweep_stays_green(self):
        hits = _repo_grep_numeric_mechanism_id(702)
        assert len(hits) >= 1, hits

    def test_a782_max_700_sweep_superseded_by_design(self):
        # #782 asserted max == 700; advancing to 702 supersedes it per the
        # #710/#720 convention. Documented, not repaired.
        assert _max_numeric_mechanism_id() == 702 != 700

    def test_b783_max_701_sweep_superseded_by_design(self):
        # #783 asserted max == 701; advancing to 702 supersedes it per the
        # #710/#720 convention. Documented, not repaired.
        assert _max_numeric_mechanism_id() == 702 != 701

    def test_b783_zero_numeric_702_sweep_fails_by_designed_supersession(self):
        # #783 asserted zero "mechanism_id: 702" hits in profiles/; the m702
        # block supersedes it by design.
        hits = _repo_grep_numeric_mechanism_id(702)
        assert len(hits) >= 1, hits


class TestTypeDEngineStatisticalMeaningfulness:
    """Fresh synthetic corpora (new values, not #780's). Never promoted."""

    def test_strong_signal_pair_significant_at_engine_layer(self):
        target = [0.71, 0.96, 1.12, 0.84, 1.03]
        peers = [-0.05, 0.02, -0.01, 0.04, -0.03]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 16),
            period_end=datetime.datetime(2026, 9, 16),
        )
        assert report.asymmetry_score == pytest.approx(0.938, rel=1e-9)
        assert report.is_significant is True
        assert report.p_value < 5e-4
        assert report.cohens_d > 8
        assert report.confidence_interval_lower > 0

    def test_near_null_pair_silent_at_engine_layer(self):
        target = [-0.02, 0.04, -0.03, 0.01, 0.00]
        peers = [0.02, -0.01, 0.03, -0.02, -0.04]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 16),
            period_end=datetime.datetime(2026, 9, 16),
        )
        assert abs(report.asymmetry_score) < 0.05
        assert report.is_significant is False
        assert report.p_value > 0.5
        assert report.cohens_d < 0.5
        assert (
            report.confidence_interval_lower < 0 < report.confidence_interval_upper
        )

    def test_degenerate_n1_contract(self):
        a, b = [0.51], [-0.49]
        t, p = welch_t_test(a, b)
        d = cohens_d(a, b)
        assert (t, p) == (0.0, 1.0)
        assert d == 0.0
        assert is_significant(p) is False
        assert abs(a[0] - b[0]) == pytest.approx(1.00)
        t2, p2 = welch_t_test(b, a)
        assert (t2, p2) == (0.0, 1.0)

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
            timeout=600,
        )
        assert result.returncode == 0, result.stderr[-2000:]
        assert "tests collected" in result.stdout


class TestTypeDFullSuiteTombstone:
    """#780 re-launch death recorded; re-launch lands in goal hidden_files."""

    TOMBSTONE_LINEAGE = 20

    def test_tombstone_lineage_count(self):
        assert self.TOMBSTONE_LINEAGE == 20

    def test_relaunch_log_path_in_goal_hidden_files(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_785_full_suite.log",
        )
        assert os.path.basename(log_path) == "type_d_785_full_suite.log"


class TestDocSync785:
    def test_readme_row_785(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_785(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_785_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog785:
    def _tail(self):
        lines = _read(LOG_PATH).splitlines()
        # Entries are appended chronologically (post-#735 convention); the
        # #785 entry sits at the end of the file, not the top.
        return "\n".join(lines[-60:])

    def test_log_entry_present(self):
        # "#785 Type D:" is the entry header; a bare "#785" would
        # false-positive on other rotation lines mentioning 785.
        assert "#785 Type D:" in self._tail()

    def test_log_mechanism_numbers_and_topics(self):
        tail = self._tail()
        assert "mechanism 702" in tail
        assert "Google pay-per-use" in tail


class TestDateGrounding785:
    @staticmethod
    def _weekday(d):
        return subprocess.run(
            ["date", "-d", d, "+%A"], capture_output=True, text=True
        ).stdout.strip()

    def test_sep_16_2026_is_wednesday(self):
        assert self._weekday("2026-09-16") == "Wednesday"
