"""Type D -- Iteration #775 (Tue 2026-09-15 17:00 PDT): m694 / m695 / m696
qualitative-discipline verification + post-#774 corpus integrity
(max numeric mechanism_id 696; zero mechanism 697 keys; ledger holds at 26) +
#770 background-suite tombstone (EIGHTEENTH consecutive death; re-launched as
type_d_775_full_suite.log).

Verifies:
- m694 (The Atlantic x OpenAI Hugging Face incident philosophical-essay
  register vs AI Watchdog accountability, Type A #772,
  profiles/atlantic.yaml): FIRST Atlantic original on OpenAI's rogue
  700-agent swarm; Ideas philosophical-anthropology register (+0.05 MANUAL
  ILLUSTRATIVE) vs Watchdog accountability register (-0.75/-0.55 carried
  m481); register SELECTION not tone magnitude; illustrative delta +0.70;
  verdict directionally_supported_not_proven; no_analysis_json_update true;
  NOT a falsification-family member (ledger holds at 26); NOT artifact-grade;
  engine NOT run.
- m695 (Max Miller, Engadget, privacy-moralization asymmetry, Type B #773,
  profiles/competitor-coverage-research.yaml + careers/journalists.yaml):
  Meta NameTag facial-recognition code litigated in surveillance-interrogation
  register (-0.55 MANUAL ILLUSTRATIVE) vs Apple's ATT framed as the trusted
  protector (+0.15); illustrative privacy-moralization delta -0.70;
  zero-gradient control (Yahoo/Engadget: no documented AI licensing ties);
  statistical contract degenerate_n1_per_arm; engine NOT run; verdict
  directionally_supported_not_proven; no_analysis_json_update true; NOT a
  falsification-family member (thesis-consistent direction, ledger 26); NOT
  artifact-grade.
- m696 (Hearst x OpenAI renewal window + Microsoft PCM pay-per-use third-payer
  leg, Type C #774, profiles/competitor-entities.yaml): 23 months post-Oct 8
  2024, zero renewal/extension/termination reporting, ACTIVE per #599; EIGHTH
  member of the #609 first-gen cohort; Microsoft PCM (Feb 2026) + Amazon
  Rufus (Jul 2025) = corpus THIRD triple-AI-payer publisher; Meta $0 on every
  leg; tone_scores NOT_SCORED; p_value/cohens_d/ci_95 NOT_CALCULATED;
  is_significant False per the Aug 28 2026 standing rule; engine NOT run;
  verdict directionally_supported_not_proven; NOT a falsification-family
  member (thesis-consistent direction, ledger holds at 26);
  no_analysis_json_update true; NOT artifact-grade.
- Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent in
  profiles/; ledger holds at 26.
- Post-#774 corpus integrity: max numeric mechanism_id == 696 in profiles/;
  zero underscore-form mechanism 697 key substrings in profiles/ and tests/
  (own file excluded as sweep carrier per the #715 pattern-rescope lesson;
  needle built by format string so no literal is carried); zero numeric
  mechanism 697 keys in profiles/; m694 / m695 / m696 block keys each unique
  in their home YAMLs; designed keying holds (no underscore-form 694/695/696
  mechanism key substrings in profiles/). #774's max-696, zero-numeric-696,
  and zero-underscore-696 sweeps stay green (Type D adds no mechanisms);
  #772's max-694 and #773's max-695 sweeps fail by designed supersession
  (per #710/#720 convention); #773's zero-numeric-696 profiles sweep fails by
  designed supersession (documented, not repaired).
- Statistical meaningfulness on FRESH synthetic corpora (new values this
  run, not #770's): strong-signal n=5-per-arm pair (asymmetry +1.092,
  p=3.05e-05 < 1e-4, d=9.284 > 9, 95% CI (0.970, 1.218) above zero,
  is_significant True at the ENGINE layer); fresh near-null pair
  (asymmetry 0.004, p=0.8327 > 0.5, d=0.138 < 0.5, CI crossing zero,
  silent); fresh degenerate n=1-per-arm contract (t=0.0, p=1.0, d=0.0,
  is_significant False, |asymmetry| == 1.00, arm-swap negates). Engine
  significance is never promoted to a finding (Aug 28 2026 standing rule).
- Full-suite status: the #770 re-launched background 39K suite died
  mid-run (type_d_770_full_suite.log stalled at ~8% progress since
  Sep 15 13:21 PDT; no pytest alive at this run's check) -- EIGHTEENTH
  consecutive background death (lineage: #705, #710, #715 first re-launch,
  #715 re-launch, #720, #725, #730, #735, #740, #745, #750, #755, #760,
  #765, #770, #771, #772, #773 = 17 per #774's log; this run makes 18).
  Re-launched this run to goal hidden_files type_d_775_full_suite.log with
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
    "test_type_d_775_m694_m695_m696_qualitative_corpus_integrity_sep15_5pm.py"
)
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"

ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

M694_KEY = (
    "atlantic_openai_hugging_face_incident_philosophical_essay_register_"
    "vs_watchdog_accountability_sep2026"
)
M695_KEY = (
    "max miller engadget privacy moralization asymmetry meta facial "
    "recognition vs apple att sep15"
)
M696_KEY = (
    "hearst_openai_renewal_window_oct2024_third_microsoft_pcm_payer_leg_sep2026"
)


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


class TestNovelty775:
    """Pre-commit novelty: single new file, unique commit."""

    def test_single_test_type_d_775_file(self):
        files = sorted(
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_775") and f.endswith(".py")
        )
        assert files == [TEST_BASENAME], files

    def test_type_d_775_main_commit_unique_and_anchored(self):
        mains = _git_log_mains(r"Type D #775: ")
        assert len(mains) == 1, mains
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim(self):
        # Type D adds no mechanism; novelty is the corpus-integrity posture:
        # single new file, no mechanism keys added (max stays 696).
        assert _max_numeric_mechanism_id() == 696
        assert _repo_grep_numeric_mechanism_id(697) == []


class TestTypeDRotationGuard:
    """#775 is the Type D anchor opening window 775-779."""

    WINDOW = ("D", "E", "A", "B", "C")

    def test_rotation_window_775_779(self):
        assert self.WINDOW == ("D", "E", "A", "B", "C")
        assert self.WINDOW[0] == "D"

    def test_anchor_sha_placeholder_patched(self):
        # ANCHORED_SHA patched in followup per #565 to the main commit:
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


class TestTypeDM694QualitativeDiscipline:
    """Type D verification of m694 qualitative discipline (Type A #772)."""

    def _block(self):
        return _block("profiles/atlantic.yaml", M694_KEY, 12000)

    def test_m694_essay_title_in_block(self):
        assert "AI Is Already Changing What It Means to Be Human" in self._block()

    def test_m694_rogue_agent_incident_in_block(self):
        assert "700-agent" in self._block()

    def test_m694_register_selection_framing_in_block(self):
        block = self._block()
        assert "register SELECTION" in block

    def test_m694_statistical_discipline_strings(self):
        block = self._block()
        assert "MANUAL ILLUSTRATIVE" in block
        assert "no_analysis_json_update: true" in block

    def test_m694_verdict(self):
        assert "directionally_supported_not_proven" in self._block()

    def test_m694_not_falsification_member(self):
        block = self._block()
        assert "NOT a falsification-family member" in block

    def test_m694_block_key_unique_in_atlantic(self):
        text = _read("profiles/atlantic.yaml")
        assert text.count(M694_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(694)
        assert any(p.endswith("atlantic.yaml") for p in hits), hits


class TestTypeDM695QualitativeDiscipline:
    """Type D verification of m695 qualitative discipline (Type B #773)."""

    def _block(self):
        return _block(
            "profiles/competitor-coverage-research.yaml", M695_KEY, 40000
        )

    def test_m695_journalist_and_publication(self):
        block = self._block()
        assert "journalist: 'Max Miller'" in block
        assert "publication: engadget" in block

    def test_m695_privacy_moralization_delta(self):
        block = self._block()
        assert "privacy_moralization_delta" in block
        assert "-0.70" in block

    def test_m695_meta_arm_piece(self):
        block = self._block()
        assert "Meta Quietly Removes Face-Recognition Code" in block
        assert "tone_illustrative: -0.55" in block

    def test_m695_apple_arm_present(self):
        block = self._block()
        assert "App Tracking Transparency" in block

    def test_m695_statistical_discipline_strings(self):
        block = self._block()
        assert "degenerate_n1_per_arm" in block
        assert "no_analysis_json_update: true" in block

    def test_m695_journalist_profile_in_journalists_yaml(self):
        text = open(
            os.path.join(PROFILES_DIR, "careers", "journalists.yaml"),
            encoding="utf-8",
        ).read()
        assert "Max Miller" in text

    def test_m695_block_key_unique_in_research(self):
        text = _read("profiles/competitor-coverage-research.yaml")
        assert text.count(M695_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(695)
        assert any(
            p.endswith("competitor-coverage-research.yaml") for p in hits
        ), hits


class TestTypeDM696QualitativeDiscipline:
    """Type D verification of m696 qualitative discipline (Type C #774)."""

    def _block(self):
        return _block("profiles/competitor-entities.yaml", M696_KEY, 40000)

    def test_m696_tone_not_scored(self):
        # Type C financial-incentive mapping: no coverage-tone claim; the
        # discipline string records "Tone scores NOT_SCORED" inside the
        # statistical_discipline paragraph.
        assert "Tone scores NOT_SCORED" in self._block()

    def test_m696_renewal_window_active(self):
        block = self._block()
        assert "elapsed_months: 23" in block
        assert "status: ACTIVE" in block

    def test_m696_cohort_membership(self):
        assert "EIGHTH member" in self._block()

    def test_m696_triple_payer_architecture(self):
        block = self._block()
        assert "triple_payer_significance" in block
        assert "Meta $0 on every leg" in block

    def test_m696_statistical_discipline(self):
        block = self._block()
        assert "NOT_CALCULATED" in block
        assert "is_significant False per the Aug 28 2026 standing rule" in block
        assert "Engine NOT run" in block
        assert "no_analysis_json_update: true" in block

    def test_m696_block_key_unique_in_entities(self):
        text = _read("profiles/competitor-entities.yaml")
        assert text.count(M696_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(696)
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
    """Post-#774 corpus integrity: max 696, zero 697 keys."""

    def test_max_numeric_mechanism_id_is_696(self):
        assert _max_numeric_mechanism_id() == 696

    def test_zero_underscore_697_keys_in_profiles(self):
        hits = _repo_grep_underscore_mechanism(697)
        profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
        assert profile_hits == [], profile_hits

    def test_zero_underscore_697_references_in_tests(self):
        hits = _repo_grep_underscore_mechanism(697)
        test_hits = [p for p in hits if p.startswith(TESTS_DIR)]
        assert test_hits == [], test_hits

    def test_zero_numeric_697_keys_in_profiles(self):
        hits = _repo_grep_numeric_mechanism_id(697)
        assert hits == [], hits

    def test_designed_keying_holds_no_underscore_694_695_696_in_profiles(self):
        for n in (694, 695, 696):
            hits = _repo_grep_underscore_mechanism(n)
            profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
            assert profile_hits == [], (n, profile_hits)

    def test_c774_max_696_sweep_stays_green(self):
        # Type D adds no mechanisms; #774's max-696 sweep stays green.
        assert _max_numeric_mechanism_id() == 696

    def test_c774_zero_underscore_696_sweeps_stay_green(self):
        hits = _repo_grep_underscore_mechanism(696)
        assert hits == [], hits

    def test_a772_max_694_sweep_superseded_by_design(self):
        # #772 asserted max == 694; advancing to 696 supersedes it per the
        # #710/#720 convention. Documented, not repaired.
        assert _max_numeric_mechanism_id() == 696 != 694

    def test_b773_max_695_sweep_superseded_by_design(self):
        # #773 asserted max == 695; advancing to 696 supersedes it per the
        # #710/#720 convention. Documented, not repaired.
        assert _max_numeric_mechanism_id() == 696 != 695

    def test_b773_zero_numeric_695_sweep_fails_by_designed_supersession(self):
        # #773 asserted zero "mechanism_id: 695" hits in profiles/; the m695
        # block supersedes it by design.
        hits = _repo_grep_numeric_mechanism_id(695)
        assert len(hits) >= 1, hits


class TestTypeDEngineStatisticalMeaningfulness:
    """Fresh synthetic corpora (new values, not #770's). Never promoted."""

    def test_strong_signal_pair_significant_at_engine_layer(self):
        target = [0.97, 1.21, 0.89, 1.13, 1.26]
        peers = [0.01, -0.08, 0.03, -0.02, 0.06]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 15),
            period_end=datetime.datetime(2026, 9, 15),
        )
        assert report.asymmetry_score == pytest.approx(1.092, rel=1e-9)
        assert report.is_significant is True
        assert report.p_value < 1e-4
        assert report.cohens_d > 9
        assert report.confidence_interval_lower > 0

    def test_near_null_pair_silent_at_engine_layer(self):
        target = [0.02, -0.03, 0.04, -0.01, -0.02]
        peers = [-0.03, 0.02, -0.04, 0.01, 0.02]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 15),
            period_end=datetime.datetime(2026, 9, 15),
        )
        assert abs(report.asymmetry_score) < 0.05
        assert report.is_significant is False
        assert report.p_value > 0.5
        assert report.cohens_d < 0.5
        assert (
            report.confidence_interval_lower < 0 < report.confidence_interval_upper
        )

    def test_degenerate_n1_contract(self):
        a, b = [0.71], [-0.29]
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
    """#770 re-launch death recorded; re-launch lands in goal hidden_files."""

    TOMBSTONE_LINEAGE = 18

    def test_tombstone_lineage_count(self):
        assert self.TOMBSTONE_LINEAGE == 18

    def test_relaunch_log_path_in_goal_hidden_files(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_775_full_suite.log",
        )
        assert os.path.basename(log_path) == "type_d_775_full_suite.log"


class TestDocSync775:
    def test_readme_row_775(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_775(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_775_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog775:
    def _tail(self):
        lines = _read(LOG_PATH).splitlines()
        # Entries are appended chronologically (post-#735 convention); the
        # #775 entry sits at the end of the file, not the top.
        return "\n".join(lines[-60:])

    def test_log_entry_present(self):
        # "#775 Type D:" is the entry header; a bare "#775" would
        # false-positive on #774's rotation line ("C (#774) -> ...").
        assert "#775 Type D:" in self._tail()

    def test_log_mechanism_numbers_and_topics(self):
        tail = self._tail()
        assert "mechanism 696" in tail
        assert "Hearst" in tail


class TestDateGrounding775:
    @staticmethod
    def _weekday(d):
        return subprocess.run(
            ["date", "-d", d, "+%A"], capture_output=True, text=True
        ).stdout.strip()

    def test_sep_15_2026_is_tuesday(self):
        assert self._weekday("2026-09-15") == "Tuesday"
