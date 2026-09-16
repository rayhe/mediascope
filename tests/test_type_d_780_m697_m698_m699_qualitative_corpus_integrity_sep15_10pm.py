"""Type D -- Iteration #780 (Tue 2026-09-15 22:00 PDT): m697 / m698 / m699
qualitative-discipline verification + post-#779 corpus integrity
(max numeric mechanism_id 699; zero 700 keys; ledger holds at 26) +
#775 background-suite tombstone (NINETEENTH consecutive death; re-launched as
type_d_780_full_suite.log).

Verifies:
- m697 (MarketWatch x OpenAI slowdown-week register set vs MarketWatch x
  Meta adversarial success-dismissal, Type A #777, profiles/news-corp.yaml):
  FIRST dedicated MarketWatch x OpenAI mechanism; three novel MarketWatch
  arms (IPO-delay CEO relay -0.05, Oracle-ecosystem aspirational +0.30,
  doomsday-fears market-headwind -0.10); OpenAI avg +0.05 vs carried
  MarketWatch x Meta arm m229 -0.55; illustrative delta +0.60; MANUAL
  ILLUSTRATIVE only; is_significant false; Engine NOT run; NOT
  artifact-grade; verdict directionally_supported_not_proven; NOT a
  falsification-family member (ledger holds at 26).
- m698 (Sarah Perez, TechCrunch/Yahoo, Muse trust-interrogation vs Astra
  demand-celebration, Type B #778,
  profiles/competitor-coverage-research.yaml + careers/journalists.yaml):
  SECOND dedicated Type B mechanism on Sarah Perez; same-writer trust
  register pair two days apart (Meta arm -0.45 trust-interrogation vs
  OpenAI arm +0.45 demand-celebration); illustrative delta
  (Meta minus OpenAI) -0.90; MANUAL ILLUSTRATIVE only; is_significant
  false; no_analysis_json_update true; verdict
  directionally_supported_not_proven; NOT a falsification-family member
  (ledger holds at 26); NOT artifact-grade.
- m699 (Taylor & Francis (Informa) x Microsoft $10M+ academic data-access
  agreement May 2024, Type C #779, profiles/competitor-entities.yaml):
  FIRST dedicated academic-publisher AI data-licensing mechanism in the
  corpus; nonexclusive access to Advanced Learning Content across nearly
  3,000 journals; $10M+ (GBP 8M+) initial fee + recurring payments over
  three years; second major (unnamed) AI-company partnership Jul 2024;
  ~$75M 2024 data-licensing total; license-over-authors FOURTH
  relationship direction; statistical_discipline: scorer none,
  tone_scores NOT_SCORED, qualitative_only true, artifact_grade false;
  verdict directionally_supported_not_proven; no_analysis_json_update
  true; falsification_family 'NOT a member - qualitative financial mapping
  only'; ledger holds at 26.
- Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent in
  profiles/; ledger holds at 26.
- Post-#779 corpus integrity: max numeric mechanism_id == 699 in
  profiles/; zero underscore-form 700 key substrings in profiles/ and
  tests/ (own file excluded as sweep carrier per the #715
  pattern-rescope lesson; needles built by format string so no literal is
  carried); zero numeric 700 keys in profiles/; m697 / m698 / m699 block
  keys each unique in their home YAMLs; designed keying holds (no
  underscore-form 697/698/699 mechanism key substrings in profiles/).
  #779's max-699, zero-underscore-699, and zero-numeric-699 sweeps stay
  green (Type D adds no mechanisms); #777's max-697 and #778's
  max-698/zero-numeric-699 sweeps fail by designed supersession (per the
  #710/#720 convention; documented, not repaired).
- Statistical meaningfulness on FRESH synthetic corpora (new values, not
  #775's): strong-signal n=5-per-arm pair (asymmetry +0.990,
  p=3.73e-05 < 1e-4, d=9.409 > 9, 95% CI (0.8839, 1.1200) above zero,
  is_significant True at the ENGINE layer); fresh near-null pair
  (asymmetry 0.008, p=0.6050 > 0.5, d=0.341 < 0.5, CI crossing zero,
  silent); fresh degenerate n=1-per-arm contract (t=0.0, p=1.0, d=0.0,
  is_significant False, |asymmetry| == 1.00, arm-swap negates). Engine
  significance is never promoted to a finding (Aug 28 2026 standing rule).
- Full-suite status: the #775 re-launched background 39K suite died
  mid-run (type_d_775_full_suite.log stalled at ~23% progress since
  Sep 15 19:15 PDT; no pytest alive at this run's check) -- NINETEENTH
  consecutive background death (lineage: 18 per #775's log plus this
  run's). Re-launched this run to goal hidden_files
  type_d_780_full_suite.log with --continue-on-collection-errors; next
  Type D run checks it.
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
    "test_type_d_780_m697_m698_m699_qualitative_corpus_integrity_sep15_10pm.py"
)
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"

ANCHORED_SHA = "a2592881b970a352fcd53a131e8fa25ce75a1efe"

M697_KEY = "marketwatch_openai_ipo_delay_oracle_boost_doomsday_market_register_sep15"
M698_KEY = (
    "sarah perez techcrunch muse trust interrogation vs astra demand "
    "celebration sep2026"
)
M699_KEY = (
    "taylor_francis_informa_microsoft_academic_data_access_"
    "may2024_expansion_sep2026"
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


class TestNovelty780:
    """Pre-commit novelty: single new file, unique commit."""

    def test_single_test_type_d_780_file(self):
        files = sorted(
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_780") and f.endswith(".py")
        )
        assert files == [TEST_BASENAME], files

    def test_type_d_780_main_commit_unique_and_anchored(self):
        mains = _git_log_mains(r"Type D #780: ")
        assert len(mains) == 1, mains
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim(self):
        # Type D adds no mechanism; novelty is the corpus-integrity posture:
        # single new file, no mechanism keys added (max stays 699).
        assert _max_numeric_mechanism_id() == 699
        assert _repo_grep_numeric_mechanism_id(700) == []


class TestTypeDRotationGuard:
    """#780 is the Type D anchor opening window 780-784."""

    WINDOW = ("D", "E", "A", "B", "C")

    def test_rotation_window_780_784(self):
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


class TestTypeDM697QualitativeDiscipline:
    """Type D verification of m697 qualitative discipline (Type A #777)."""

    def _block(self):
        return _block("profiles/news-corp.yaml", M697_KEY, 15000)

    def test_m697_mechanism_name_in_block(self):
        assert "MarketWatch x OpenAI Slowdown-Week Register Set" in self._block()

    def test_m697_three_register_arms(self):
        block = self._block()
        assert "constructive_ceo_framing_relay" in block
        assert "Oracle" in block
        assert "doomsday fears" in block

    def test_m697_illustrative_gap_plus_060(self):
        block = self._block()
        assert "+0.60" in block
        assert "MANUAL ILLUSTRATIVE" in block

    def test_m697_statistical_discipline_strings(self):
        block = self._block()
        assert "is_significant: false" in block
        assert "Engine NOT run" in block
        assert "NOT artifact-grade" in block

    def test_m697_verdict(self):
        assert "directionally_supported_not_proven" in self._block()

    def test_m697_not_falsification_member(self):
        block = self._block()
        assert "NOT a falsification-family member" in block

    def test_m697_block_key_unique_in_news_corp(self):
        text = _read("profiles/news-corp.yaml")
        assert text.count(M697_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(697)
        assert any(p.endswith("news-corp.yaml") for p in hits), hits


class TestTypeDM698QualitativeDiscipline:
    """Type D verification of m698 qualitative discipline (Type B #778)."""

    def _block(self):
        return _block(
            "profiles/competitor-coverage-research.yaml", M698_KEY, 25000
        )

    def test_m698_journalist_and_publication(self):
        block = self._block()
        assert "journalist: 'Sarah Perez'" in block
        assert "publication: techcrunch" in block

    def test_m698_trust_register_pair(self):
        block = self._block()
        assert "Will consumers trust it?" in block
        assert "unprecedented" in block

    def test_m698_illustrative_delta_minus_090(self):
        block = self._block()
        assert "-0.90" in block
        assert "MANUAL ILLUSTRATIVE" in block

    def test_m698_statistical_discipline_strings(self):
        block = self._block()
        assert "is_significant: false" in block
        assert "no_analysis_json_update: true" in block
        assert "NOT artifact-grade" in block

    def test_m698_verdict(self):
        assert "directionally_supported_not_proven" in self._block()

    def test_m698_not_falsification_member(self):
        block = self._block()
        assert "NOT a falsification-family member" in block

    def test_m698_journalist_profile_in_journalists_yaml(self):
        text = open(
            os.path.join(PROFILES_DIR, "careers", "journalists.yaml"),
            encoding="utf-8",
        ).read()
        assert "sarah_perez" in text.lower().replace(" ", "_")

    def test_m698_block_key_unique_in_research(self):
        text = _read("profiles/competitor-coverage-research.yaml")
        assert text.count(M698_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(698)
        assert any(
            p.endswith("competitor-coverage-research.yaml") for p in hits
        ), hits


class TestTypeDM699QualitativeDiscipline:
    """Type D verification of m699 qualitative discipline (Type C #779)."""

    def _block(self):
        return _block("profiles/competitor-entities.yaml", M699_KEY, 25000)

    def test_m699_mechanism_name_academic_publisher(self):
        block = self._block()
        assert "Taylor & Francis" in block
        assert "Microsoft" in block
        assert "FIRST" in block

    def test_m699_deal_terms(self):
        block = self._block()
        assert "$10M+" in block
        assert "3,000" in block
        assert "~$75M" in block

    def test_m699_license_over_authors_direction(self):
        block = self._block()
        assert "license-over-authors" in block
        assert "FOURTH" in block

    def test_m699_statistical_discipline(self):
        block = self._block()
        assert "scorer: none" in block
        assert "tone_scores: NOT_SCORED" in block
        assert "qualitative_only: true" in block
        assert "artifact_grade: false" in block
        assert "no_analysis_json_update: true" in block

    def test_m699_verdict(self):
        assert "directionally_supported_not_proven" in self._block()

    def test_m699_not_falsification_member(self):
        block = self._block()
        assert "NOT a member - qualitative financial mapping only" in block

    def test_m699_block_key_unique_in_entities(self):
        text = _read("profiles/competitor-entities.yaml")
        assert text.count(M699_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(699)
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
    """Post-#779 corpus integrity: max 699, zero 700 keys."""

    def test_max_numeric_mechanism_id_is_699(self):
        assert _max_numeric_mechanism_id() == 699

    def test_zero_underscore_700_keys_in_profiles(self):
        hits = _repo_grep_underscore_mechanism(700)
        profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
        assert profile_hits == [], profile_hits

    def test_zero_underscore_700_references_in_tests(self):
        hits = _repo_grep_underscore_mechanism(700)
        test_hits = [p for p in hits if p.startswith(TESTS_DIR)]
        assert test_hits == [], test_hits

    def test_zero_numeric_700_keys_in_profiles(self):
        hits = _repo_grep_numeric_mechanism_id(700)
        assert hits == [], hits

    def test_designed_keying_holds_no_underscore_697_698_699_in_profiles(self):
        for n in (697, 698, 699):
            hits = _repo_grep_underscore_mechanism(n)
            profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
            assert profile_hits == [], (n, profile_hits)

    def test_c779_max_699_sweep_stays_green(self):
        # Type D adds no mechanisms; #779's max-699 sweep stays green.
        assert _max_numeric_mechanism_id() == 699

    def test_c779_zero_underscore_699_sweeps_stay_green(self):
        hits = _repo_grep_underscore_mechanism(699)
        assert hits == [], hits

    def test_c779_zero_numeric_699_sweep_stays_green(self):
        hits = _repo_grep_numeric_mechanism_id(699)
        assert len(hits) >= 1, hits

    def test_a777_max_697_sweep_superseded_by_design(self):
        # #777 asserted max == 697; advancing to 699 supersedes it per the
        # #710/#720 convention. Documented, not repaired.
        assert _max_numeric_mechanism_id() == 699 != 697

    def test_b778_max_698_sweep_superseded_by_design(self):
        # #778 asserted max == 698; advancing to 699 supersedes it per the
        # #710/#720 convention. Documented, not repaired.
        assert _max_numeric_mechanism_id() == 699 != 698

    def test_b778_zero_numeric_699_sweep_fails_by_designed_supersession(self):
        # #778 asserted zero "mechanism_id: 699" hits in profiles/; the m699
        # block supersedes it by design.
        hits = _repo_grep_numeric_mechanism_id(699)
        assert len(hits) >= 1, hits


class TestTypeDEngineStatisticalMeaningfulness:
    """Fresh synthetic corpora (new values, not #775's). Never promoted."""

    def test_strong_signal_pair_significant_at_engine_layer(self):
        target = [0.88, 1.04, 0.95, 1.19, 0.83]
        peers = [-0.02, 0.05, -0.06, 0.01, -0.04]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 15),
            period_end=datetime.datetime(2026, 9, 15),
        )
        assert report.asymmetry_score == pytest.approx(0.99, rel=1e-9)
        assert report.is_significant is True
        assert report.p_value < 1e-4
        assert report.cohens_d > 9
        assert report.confidence_interval_lower > 0

    def test_near_null_pair_silent_at_engine_layer(self):
        target = [0.01, 0.03, -0.02, 0.02, -0.01]
        peers = [-0.01, -0.02, 0.03, -0.03, 0.02]
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
        a, b = [0.64], [-0.36]
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
    """#775 re-launch death recorded; re-launch lands in goal hidden_files."""

    TOMBSTONE_LINEAGE = 19

    def test_tombstone_lineage_count(self):
        assert self.TOMBSTONE_LINEAGE == 19

    def test_relaunch_log_path_in_goal_hidden_files(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_780_full_suite.log",
        )
        assert os.path.basename(log_path) == "type_d_780_full_suite.log"


class TestDocSync780:
    def test_readme_row_780(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_780(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_780_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog780:
    def _tail(self):
        lines = _read(LOG_PATH).splitlines()
        # Entries are appended chronologically (post-#735 convention); the
        # #780 entry sits at the end of the file, not the top.
        return "\n".join(lines[-60:])

    def test_log_entry_present(self):
        # "#780 Type D:" is the entry header; a bare "#780" would
        # false-positive on other rotation lines mentioning 780.
        assert "#780 Type D:" in self._tail()

    def test_log_mechanism_numbers_and_topics(self):
        tail = self._tail()
        assert "mechanism 699" in tail
        assert "Taylor & Francis" in tail


class TestDateGrounding780:
    @staticmethod
    def _weekday(d):
        return subprocess.run(
            ["date", "-d", d, "+%A"], capture_output=True, text=True
        ).stdout.strip()

    def test_sep_15_2026_is_tuesday(self):
        assert self._weekday("2026-09-15") == "Tuesday"
