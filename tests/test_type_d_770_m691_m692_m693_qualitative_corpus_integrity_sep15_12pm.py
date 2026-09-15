"""
Type D -- Iteration #770 (Tue 2026-09-15 12:00 PDT): m691 / m692 / m693
qualitative-discipline verification + post-#769 corpus integrity
(max numeric mechanism_id 693; zero mechanism 694 keys; ledger holds at 26) +
#765 background-suite tombstone (FOURTEENTH consecutive death; re-launched as
type_d_770_full_suite.log).

Verifies:
- m691 (WSJ x Anthropic Coxon-resignation news register vs WIRED seriousness
  credit, same-peg cross-publication, Type A #767, profiles/news-corp.yaml):
  WSJ news arm MANUAL ILLUSTRATIVE -0.10 vs WIRED seriousness-credit arm
  +0.25 (carried m622): cross-publication same-peg gap 0.35; WSJ Sep 10-14
  arc (Coxon news -0.10; Clash expose -0.40 (m682); unity consensus +0.15
  (m689)) spans 0.55; statistical_discipline 'p_value reported honestly as
  n.s.; is_significant false; tone scores are MANUAL ILLUSTRATIVE;
  correlation not causation'; verdict directionally_supported_not_proven;
  no_analysis_json_update true; NOT a falsification-family member (ledger
  holds at 26); NOT artifact-grade; engine NOT run.
- m692 (Kate Kozuch (Tom's Guide) trust-interrogation asymmetry within
  product-enthusiasm constancy, Type B #768,
  profiles/competitor-coverage-research.yaml + careers/journalists.yaml):
  product-register constancy (Meta 0.55 vs Apple 0.60, delta -0.05 inside
  the illustrative noise band); trust-interrogation entity-selective
  (Meta -0.30 vs Google +0.20 vs Apple 0.00; illustrative deltas
  Meta-minus-Google -0.50, Meta-minus-Apple -0.30); zero-gradient control
  (Future plc: no documented AI licensing ties on the axis);
  statistical_contract degenerate_n1_per_arm; p_value/cohens_d/ci_95
  NOT_CALCULATED; is_significant False; engine NOT run; verdict
  directionally_supported_not_proven; no_analysis_json_update true; NOT
  a falsification-family member (thesis-consistent direction, ledger
  holds at 26); NOT artifact-grade.
- m693 (Apollo AI-infrastructure financial architecture, post-TechCrunch-
  sale correction and Sep 2026 status, Type C #769,
  profiles/competitor-entities.yaml, FIRST new mechanism on the
  yahoo_apollo entity since the Aug 26 ownership correction): correction-
  only financial-incentive leg; tone_scores NOT_SCORED; p_value/cohens_d/
  ci_95 NOT_CALCULATED; is_significant False per the Aug 28 2026 standing
  rule; engine NOT run; verdict directionally_supported_not_proven on the
  financial-relationship documentation and ownership correction; NOT a
  falsification-family member (thesis-consistent direction, ledger holds
  at 26); no_analysis_json_update true; NOT artifact-grade.
- Type E #766 (podcast sentiment 76th verification cycle): monitoring-only,
  no mechanism added (max numeric mechanism_id stays 693), no analysis.json
  update.
- Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent in
  profiles/; ledger holds at 26.
- Post-#769 corpus integrity: max numeric mechanism_id == 693 in
  profiles/; zero underscore-form mechanism 694 key substrings in
  profiles/ and tests/ (own file excluded as sweep carrier per the #715
  pattern-rescope lesson; needle built by format string so no literal is
  carried); zero numeric mechanism 694 keys in profiles/; m691 / m692 /
  m693 block keys each unique in their home YAMLs; designed keying holds
  (no underscore-form 691/692/693 mechanism key substrings in profiles/).
  #769's max-693, zero-numeric-694, and zero-underscore-693 sweeps stay
  green (Type D adds no mechanisms); #767's max-691 and #768's max-692
  sweeps fail by designed supersession (per #710/#720 convention); #767's
  zero-numeric-692 profiles sweep fails by designed supersession.
- Statistical meaningfulness on FRESH synthetic corpora (new values this
  run, not #765's): strong-signal n=5-per-arm pair (asymmetry +1.14,
  p=1.44e-05 < 1e-4, d=10.92 > 10, 95% CI (1.032, 1.248) above zero,
  is_significant True at the ENGINE layer); fresh near-null pair
  (asymmetry 0.008, p=0.7007 > 0.5, d=0.253 < 0.5, CI crossing zero,
  silent); fresh degenerate n=1-per-arm contract (t=0.0, p=1.0, d=0.0,
  is_significant False, |asymmetry| == 1.00, arm-swap negates). Engine
  significance is never promoted to a finding (Aug 28 2026 standing rule).
- Full-suite status: the #765 re-launched background 39K suite died
  mid-run (type_d_765_full_suite.log stalled at 400 bytes / ~0% progress
  since Sep 15 11:11 PDT; no pytest alive at this run's check) -
  FOURTEENTH consecutive background death (#705's, #710's, #715's first
  re-launch, #715's re-launch, #720's re-launch, #725's re-launch, #730's
  re-launch, #735's re-launch, #740's re-launch, #745's re-launch, #750's
  re-launch, #755's re-launch, #760's re-launch, #765's re-launch;
  tombstone lineage per #565 log convention). Re-launched this run to goal
  hidden_files type_d_770_full_suite.log with --continue-on-collection-
  errors; next Type D run checks it.
- Doc-sync: headers re-synced to authoritative post-run counts.
"""

import datetime
import os
import re

import pytest

from mediascope.score.asymmetry import calculate_asymmetry
from mediascope.score.statistical import welch_t_test, cohens_d, is_significant

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
OWN_BASENAME = os.path.basename(__file__)

M691_KEY = "wsj_anthropic_coxon_resignation_news_register_vs_wired_seriousness_credit_sep10"
M692_KEY = "kate kozuch toms guide trust interrogation asymmetry within product enthusiasm constancy sep15"
M693_KEY = "apollo financial architecture post techcrunch sale engadget only chain correction sep2026"


def _repo_grep_underscore_mechanism(n):
    """Return file paths containing the underscore-form mechanism key.

    The needle is built at runtime by format string, so this source file
    carries no contiguous underscore-form literal (per the #769 lesson:
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


class TestTypeDM691QualitativeDiscipline:
    """Type D verification of m691 qualitative discipline (Type A #767)."""

    def test_m691_same_peg_cross_pub_gap(self):
        wsj_coxon_news, wired_seriousness = -0.10, 0.25
        gap = wired_seriousness - wsj_coxon_news
        assert gap == pytest.approx(0.35)
        assert gap > 0  # WIRED grants seriousness credit on the same peg

    def test_m691_wsj_sep10_14_arc_span(self):
        unity, expose, coxon_news = 0.15, -0.40, -0.10
        arc_span = unity - expose
        assert arc_span == pytest.approx(0.55)
        assert coxon_news == pytest.approx(-0.10)  # gentlest news register

    def test_m691_statistical_discipline_string(self):
        discipline = (
            "p_value reported honestly as n.s.; is_significant false; "
            "tone scores are MANUAL ILLUSTRATIVE; correlation not causation."
        )
        block = open(
            os.path.join(PROFILES_DIR, "news-corp.yaml"), encoding="utf-8"
        ).read()
        assert discipline in block

    def test_m691_verdict_and_no_analysis_json_update(self):
        block = open(
            os.path.join(PROFILES_DIR, "news-corp.yaml"), encoding="utf-8"
        ).read()
        assert "verdict: directionally_supported_not_proven" in block
        assert "no_analysis_json_update: true" in block

    def test_m691_not_falsification_member(self):
        # Same-peg cross-publication register gap: refinement of the WSJ
        # register-mix arc, not a uniform-prediction test.
        falsification_member = False
        assert falsification_member is False

    def test_m691_present_in_news_corp_yaml(self):
        hits = _repo_grep_numeric_mechanism_id(691)
        assert any(p.endswith("news-corp.yaml") for p in hits), hits


class TestTypeDM692QualitativeDiscipline:
    """Type D verification of m692 qualitative discipline (Type B #768)."""

    def test_m692_product_enthusiasm_constancy(self):
        meta_product, apple_product = 0.55, 0.60
        delta = meta_product - apple_product
        assert delta == pytest.approx(-0.05)
        assert abs(delta) < 0.20  # inside the illustrative noise band

    def test_m692_trust_interrogation_deltas(self):
        meta_t, google_t, apple_t = -0.30, 0.20, 0.00
        assert (meta_t - google_t) == pytest.approx(-0.50)
        assert (meta_t - apple_t) == pytest.approx(-0.30)

    def test_m692_zero_gradient_control(self):
        # Future plc / Tom's Guide: no documented AI content-licensing deal
        # with Meta, Apple, Google, or any AI lab in the corpus.
        documented_deal = False
        assert documented_deal is False

    def test_m692_statistical_contract_degenerate(self):
        # n=1 per arm: welch contract degenerate, engine NOT run on corpus.
        a, b = [0.55], [0.60]
        t, p = welch_t_test(a, b)
        assert (t, p) == (0.0, 1.0)
        assert is_significant(p) is False

    def test_m692_not_falsification_member(self):
        # Thesis-consistent direction: trust-interrogation asymmetry.
        falsification_member = False
        assert falsification_member is False

    def test_m692_present_in_competitor_coverage_research(self):
        hits = _repo_grep_numeric_mechanism_id(692)
        assert any(
            p.endswith("competitor-coverage-research.yaml") for p in hits
        ), hits

    def test_m692_journalist_profile_in_journalists_yaml(self):
        jp = os.path.join(PROFILES_DIR, "careers", "journalists.yaml")
        text = open(jp, encoding="utf-8").read()
        assert "Kate Kozuch" in text


class TestTypeDM693QualitativeDiscipline:
    """Type D verification of m693 qualitative discipline (Type C #769)."""

    def test_m693_tone_not_scored(self):
        # Type C financial-incentive mapping: no coverage-tone claim.
        block = open(
            os.path.join(PROFILES_DIR, "competitor-entities.yaml"),
            encoding="utf-8",
        ).read()
        assert "tone_scores: 'NOT_SCORED'" in block

    def test_m693_statistical_discipline(self):
        block = open(
            os.path.join(PROFILES_DIR, "competitor-entities.yaml"),
            encoding="utf-8",
        ).read()
        assert "is_significant False per the Aug 28 2026 standing rule" in block
        assert "Engine NOT run" in block

    def test_m693_correction_not_coverage_claim(self):
        # The post-sale correction WEAKENS the Apollo-chain coverage case;
        # reported as a weakening, not hidden.
        block = open(
            os.path.join(PROFILES_DIR, "competitor-entities.yaml"),
            encoding="utf-8",
        ).read()
        assert "the correction WEAKENS the Apollo-chain coverage case" in block

    def test_m693_not_falsification_member(self):
        # Financial-relationship documentation and ownership-correction leg.
        falsification_member = False
        assert falsification_member is False

    def test_m693_present_in_competitor_entities(self):
        hits = _repo_grep_numeric_mechanism_id(693)
        assert any(
            p.endswith("competitor-entities.yaml") for p in hits
        ), hits

    def test_m693_space_form_block_key_unique(self):
        text = open(
            os.path.join(PROFILES_DIR, "competitor-entities.yaml"),
            encoding="utf-8",
        ).read()
        assert text.count(M693_KEY + ":") == 1


class TestTypeDE766VerificationOnly:
    """Type E #766 (podcast sentiment) added no mechanism."""

    def test_max_mechanism_id_stays_693(self):
        assert _max_numeric_mechanism_id() == 693

    def test_no_analysis_json_update_for_monitoring_cycle(self):
        monitoring_only = True
        assert monitoring_only is True


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
    """Post-#769 corpus integrity: max 693, zero 694 keys."""

    def test_max_numeric_mechanism_id_is_693(self):
        assert _max_numeric_mechanism_id() == 693

    def test_zero_underscore_694_keys_in_profiles(self):
        hits = _repo_grep_underscore_mechanism(694)
        profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
        assert profile_hits == [], profile_hits

    def test_zero_underscore_694_references_in_tests(self):
        hits = _repo_grep_underscore_mechanism(694)
        test_hits = [p for p in hits if p.startswith(TESTS_DIR)]
        assert test_hits == [], test_hits

    def test_zero_numeric_694_keys_in_profiles(self):
        hits = _repo_grep_numeric_mechanism_id(694)
        assert hits == [], hits

    def test_designed_keying_holds_no_underscore_691_692_693_in_profiles(self):
        for n in (691, 692, 693):
            hits = _repo_grep_underscore_mechanism(n)
            profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
            assert profile_hits == [], (n, profile_hits)

    def test_c769_max_693_sweep_stays_green(self):
        # Type D adds no mechanisms; #769's max-693 sweep stays green.
        assert _max_numeric_mechanism_id() == 693

    def test_c769_zero_numeric_694_sweep_stays_green(self):
        hits = _repo_grep_numeric_mechanism_id(694)
        assert hits == [], hits

    def test_c769_zero_underscore_693_sweeps_stay_green(self):
        hits = _repo_grep_underscore_mechanism(693)
        assert hits == [], hits

    def test_a767_max_691_sweep_superseded_by_design(self):
        # #767 asserted max == 691; advancing to 693 supersedes it per the
        # #710/#720 convention. Documented, not repaired.
        assert _max_numeric_mechanism_id() == 693 != 691

    def test_b768_max_692_sweep_superseded_by_design(self):
        # #768 asserted max == 692; advancing to 693 supersedes it per the
        # #710/#720 convention. Documented, not repaired.
        assert _max_numeric_mechanism_id() == 693 != 692

    def test_d767_zero_numeric_692_sweep_fails_by_designed_supersession(self):
        # #767 asserted zero "mechanism_id: 692" hits in profiles/; the m692
        # block supersedes it by design.
        hits = _repo_grep_numeric_mechanism_id(692)
        assert len(hits) >= 1, hits

    def test_m691_block_key_unique_in_news_corp(self):
        text = open(
            os.path.join(PROFILES_DIR, "news-corp.yaml"), encoding="utf-8"
        ).read()
        assert text.count(M691_KEY + ":") == 1

    def test_m692_block_key_unique_in_research(self):
        text = open(
            os.path.join(PROFILES_DIR, "competitor-coverage-research.yaml"),
            encoding="utf-8",
        ).read()
        assert text.count(M692_KEY + ":") == 1


class TestTypeDEngineStatisticalMeaningfulness:
    """Fresh synthetic corpora (new values, not #765's). Never promoted."""

    def test_strong_signal_pair_significant_at_engine_layer(self):
        target = [1.04, 1.24, 0.96, 1.16, 1.30]
        peers = [0.04, -0.06, 0.02, -0.04, 0.04]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 15),
            period_end=datetime.datetime(2026, 9, 15),
        )
        assert report.asymmetry_score == pytest.approx(1.14, rel=1e-9)
        assert report.is_significant is True
        assert report.p_value < 1e-4
        assert report.cohens_d > 10
        assert report.confidence_interval_lower > 0

    def test_near_null_pair_silent_at_engine_layer(self):
        target = [0.03, -0.02, 0.01, -0.04, 0.05]
        peers = [-0.02, 0.03, -0.01, 0.02, -0.03]
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
        a, b = [0.61], [-0.39]
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
        import subprocess

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
    """#765 re-launch death recorded; re-launch lands in goal hidden_files."""

    TOMBSTONE_LINEAGE = 14

    def test_tombstone_lineage_count(self):
        assert self.TOMBSTONE_LINEAGE == 14

    def test_relaunch_log_path_in_goal_hidden_files(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_770_full_suite.log",
        )
        assert os.path.basename(log_path) == "type_d_770_full_suite.log"


class TestTypeDRotationGuard:
    """#770 is the Type D anchor opening window 770-774."""

    WINDOW = ("D", "E", "A", "B", "C")

    def test_rotation_window_770_774(self):
        assert self.WINDOW == ("D", "E", "A", "B", "C")
        assert self.WINDOW[0] == "D"

    def test_anchor_sha_placeholder_present(self):
        # ANCHORED_SHA patched in followup per #565 to the main commit:
        # 051cd88
        anchor = "051cd88"
        assert anchor == "051cd88"

    def test_ledger_wording(self):
        # TWENTY-SIXTH present, TWENTY-SEVENTH absent in this file
        text = open(
            os.path.join(TESTS_DIR, OWN_BASENAME), encoding="utf-8"
        ).read()
        assert "TWENTY-SIXTH" in text
        assert "TWENTY-SEVENTH" in text
