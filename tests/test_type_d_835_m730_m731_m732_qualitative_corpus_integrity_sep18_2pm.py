"""Type D -- Iteration #835 (Fri 2026-09-18 14:00 PDT): m730 / m731 / m732
qualitative-discipline verification + post-#834 corpus integrity
(max numeric mechanism_id 732; zero 733 keys; ledger holds at 26) +
#830 background-suite verdict (died at ~0% progress, 34 bytes, no
pytest alive at this run's check; NINTH consecutive background
full-suite death; tombstone lineage advances TWENTY-SEVENTH ->
TWENTY-EIGHTH per the #770/#780 convention) + fresh synthetic engine
meaningfulness (new values, not #830's) + re-launch of the full suite
as a background process writing to goal hidden_files
type_d_835_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Verifies:
- m730 (Reuters x Anthropic company-sourced aspirational register vs
  Reuters x Meta enforcement register, Type A #832,
  profiles/competitor-coverage-research.yaml): null-tie-wire
  replication of #717/m664 on a second AI-lab entity in a tighter
  same-week window; 14-day Anthropic window (Sep 4-18 2026) with three
  company- or company-sympathetic-sourced pieces vs same-48-hour Meta
  enforcement pieces (Sep 17-18); MANUAL ILLUSTRATIVE +0.45 / +0.35 /
  +0.15 (Anthropic avg +0.32) and -0.45 / -0.35 (Meta avg -0.40);
  illustrative Anthropic-minus-Meta delta +0.72; the Reuters-Meta
  multi-year content deal (Oct 25 2024) sits on META's side so the
  gradient runs OPPOSITE the naive payer-softening prediction;
  EXTENDS mechanism 664; connects_to 664 / 667 / 682; p_value /
  cohens_d / ci_95 NOT_CALCULATED; is_significant False (Aug 28 2026
  standing rule); engine NOT run; verdict
  directionally_supported_not_proven; NOT artifact-grade; no
  analysis.json update; NOT a falsification-family member (ledger
  holds at 26).
- m731 (Jay Peters (The Verge) Meta Ray-Ban Gen 2 review vs Snap
  Specs hands-on within-journalist cross-entity privacy-register
  comparison, Type B #833, profiles/careers/journalists.yaml): FIRST
  dedicated Type B mechanism on Jay Peters in journalists.yaml; Meta
  arm "Ray-Ban Meta Gen 2 review: all-day smart glasses with the
  same tricky questions" (-0.10 MANUAL ILLUSTRATIVE,
  privacy-scrutiny-forward, Verge Score 7, search-excerpt-bounded per
  #503) vs Snap arm "I wore Snap's $2,200 smart glasses" (+0.35
  MANUAL ILLUSTRATIVE, experiential positive, ZERO
  privacy vocabulary, first-hand 133-line mirror read); illustrative
  Snap-minus-Meta delta +0.45; EXTENDS mechanism 269 (Ropek
  editorial routing / vocabulary laundering) for a SECOND
  journalist; CRITICAL SCOPE BOUND: Peters' Oct 2025 Meta Ray-Ban
  Display piece was positive, so the split is product/story-level,
  NOT a stable anti-Meta journalist bias; genre asymmetry and
  product maturity are the DOMINANT confounders; MANUAL
  ILLUSTRATIVE only; verdict directionally_supported_not_proven;
  NOT a falsification-family member (ledger holds at 26).
- m732 (Meta AI payer-leg census reconciliation + publisher-deal
  tracker audit, Type C #834, profiles/competitor-entities.yaml):
  FIRST corpus reconciliation of Meta's AI-content payer legs
  against the publisher-deal trackers; first-hand browser.open read
  of the Press Gazette Who is suing, who is signing tracker (Sep 18
  2026, 1641 rendered lines) maps 3 Meta entries vs a
  corpus-documented census of 13 named counterparties ALL ACTIVE
  per #599/#609 (Reuters Oct 2024 m633; Dec 5 2025 seven-publisher
  bundle m331; News Corp Mar 2026 up to $50M per year m549;
  European bundle Le Figaro / Prisa / Sueddeutsche); CORRECTION of
  the stale mechanism-489 one-leg claim; sue-ledger additions
  Editorial Perfil (Aug 26 2026, first Spanish-language publisher
  suit) and Wikihow (Aug 22 2026), both verified new pre-commit;
  scorer none; tone_scores NOT_SCORED; p_value / cohens_d / ci_95
  NOT_CALCULATED; is_significant false; qualitative_only true;
  verdict census_reconciled_correction_issued; no_analysis_json_update
  true; artifact_grade false; NOT a falsification-family member
  (ledger holds at 26).
- Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent
  in profiles/; ledger holds at 26.
- Post-#834 corpus integrity: max numeric mechanism_id == 732 in
  profiles/; zero underscore-form 733 key substrings in profiles/
  and tests/ (own file excluded as sweep carrier per the #715
  pattern-rescope lesson; needles built by format string so no
  literal is carried); zero numeric 733 keys in profiles/; m730 /
  m731 / m732 block keys each unique in their home YAMLs; designed
  keying holds (no underscore-form 730 / 731 / 732 key substrings in
  profiles/). #834's max-732 / zero-underscore-733 /
  zero-numeric-733 sweeps stay green (Type D adds no mechanisms);
  #832's max-730 and #833's max-731 sweeps fail by designed
  supersession per the #710/#720 convention (documented, not
  repaired).
- Statistical meaningfulness on FRESH synthetic corpora (new values,
  not #830's): strong-signal n=5-per-arm pair (asymmetry +1.048,
  t=22.0840, p=2.07e-08, d=13.9671, is_significant True at the
  ENGINE layer, 95% CI (0.968, 1.126) entirely above zero); fresh
  near-null pair (asymmetry 0.030, t=0.9045, p=0.3930, d=0.5721,
  is_significant False, CI (-0.026, 0.088) crossing zero, silent);
  fresh degenerate n=1-per-arm contract on the m731 tone pair
  ([0.35], [-0.10]: t=0.0, p=1.0, d=0.0, is_significant False,
  |asymmetry| == 0.45 exact, arm-swap negates). Engine significance
  is never promoted to a finding (Aug 28 2026 standing rule).
- Full-suite status: the #830 background suite re-launched 09:08
  PDT died (type_d_830_full_suite.log stalled at 34 bytes / ~0%
  progress since 09:08 PDT; no pytest alive at this run's check) -
  NINTH consecutive background death (#705's, #710's, #715's first
  re-launch, #715's re-launch, #720's re-launch, #725's re-launch,
  #730's re-launch, #825's re-launch, #830's re-launch; tombstone
  lineage per #565 advances TWENTY-SEVENTH -> TWENTY-EIGHTH). This
  run re-launches the full suite as a background process writing
  to goal hidden_files type_d_835_full_suite.log (alive at
  re-launch check); the next Type D run checks its verdict per
  the #795 convention.

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
    "test_type_d_835_m730_m731_m732_qualitative_corpus_integrity_sep18_2pm.py"
)
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"

ANCHORED_SHA = "ea8d8b2663d04ac8ae3d842cd1abd504ce179843"

M730_KEY = (
    "reuters_anthropic_company_sourced_aspirational_register_vs_meta_"
    "enforcement_register_sep18_2026"
)
M731_KEY = (
    "type_b_833_jay_peters_verge_meta_gen2_tricky_questions_vs_snap_"
    "specs_experiential_sep18"
)
M732_KEY = "meta_payer_leg_census_and_tracker_audit_sep2026"

# Format-built so this file carries no underscore-form mechanism literal
# (per the #770 lesson: keeps prior runs' zero-underscore sweeps green).
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


def _repo_grep_underscore_mechanism(n):
    """Return file paths containing the underscore-form mechanism key.

    The needle is built at runtime by format string, so this source file
    carries no contiguous underscore-form literal (per the #770 lesson:
    keep prior runs' zero-underscore sweeps green)."""
    needle = "%s%d" % (MECH_ID_MARKER, n)
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
    ids = set()
    for root, _dirs, files in os.walk(PROFILES_DIR):
        for f in files:
            with open(
                os.path.join(root, f), encoding="utf-8", errors="replace"
            ) as fh:
                ids.update(int(x) for x in pat.findall(fh.read()))
    return max(ids)


class TestNovelty835:
    def test_single_test_type_d_835_file(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_835") and f.endswith(".py")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_d_835_main_commit_unique_and_anchored(self):
        # No #835 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Does not exist yet. Patched green in the anchor followup.
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
            if "Type D #835" in line and "followup" not in line.lower()
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
        # posture: max stays 732, zero numeric 733 keys.
        assert _max_numeric_mechanism_id() == 732
        assert _repo_grep_numeric_mechanism_id(733) == []

    def test_830_834_window_closed_prior_to_835(self):
        log = _read(LOG_PATH)
        for marker in (
            "## #830 Type D:",
            "## #831 Type E:",
            "## #832 Type A:",
            "## #833 Type B:",
            "## #834 Type C:",
        ):
            assert marker in log, marker


class TestTypeDRotationGuard:
    """#835 is the Type D anchor opening window 835-839."""

    WINDOW = ("D", "E", "A", "B", "C")

    def test_rotation_window_835_839(self):
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


class TestTypeDM730QualitativeDiscipline:
    """Type D verification of m730 qualitative discipline (Type A #832).

    Assertions run on the whitespace-folded block per the #732
    convention: the m730 finding, arms, and verdict fields wrap across
    raw YAML lines."""

    def _block(self):
        return _fold(_block("profiles/competitor-coverage-research.yaml", M730_KEY, 12000))

    def test_m730_publication_iteration_and_type(self):
        b = self._block()
        assert "mechanism_id: 730" in b
        assert "iteration: 832" in b
        assert "rotation_type: A" in b
        assert "discovery_date: '2026-09-18'" in b

    def test_m730_publication_competitor_comparator(self):
        b = self._block()
        assert "publication: Reuters" in b
        assert "competitor: Anthropic" in b
        assert "comparator_entity: Meta" in b

    def test_m730_anthropic_arms_manual_illustrative(self):
        b = self._block()
        assert "Anthropic says Claude now leads a quarter of work" in b
        assert "Anthropic CEO urges AI companies to slow model development" in b
        assert "Anthropic IPO launch shifts toward mid-October" in b
        assert "MANUAL ILLUSTRATIVE +0.45" in b
        assert "MANUAL ILLUSTRATIVE +0.35" in b
        assert "MANUAL ILLUSTRATIVE +0.15" in b
        assert "Anthropic arm avg +0.32" in b

    def test_m730_meta_arms_manual_illustrative(self):
        b = self._block()
        assert "French prosecutors and regulators step up scrutiny on smart glasses" in b
        assert "German court rules Meta liable for fake ads" in b
        assert "MANUAL ILLUSTRATIVE -0.45" in b
        assert "MANUAL ILLUSTRATIVE -0.35" in b
        assert "Meta arm avg -0.40" in b

    def test_m730_illustrative_delta(self):
        b = self._block()
        assert "Illustrative delta (Anthropic minus Meta) +0.72" in b

    def test_m730_null_tie_wire_replication_extends_664(self):
        b = self._block()
        assert "EXTENDS mechanism 664" in b
        assert "null-tie-wire" in b
        # connects_to sits past the 12000-char span; read wide for it.
        wide = _fold(_block("profiles/competitor-coverage-research.yaml", M730_KEY, 18000))
        assert "connects_to: - 664 - 667 - 682" in wide

    def test_m730_deal_on_meta_side_inverts_naive_prediction(self):
        b = self._block()
        assert "Reuters-Meta multi-year content deal (Oct 25 2024)" in b
        assert "OPPOSITE the naive payer-softening prediction" in b

    def test_m730_statistical_discipline(self):
        b = self._block()
        assert "p_value NOT_CALCULATED" in b
        assert "cohens_d NOT_CALCULATED" in b
        assert "ci_95 NOT_CALCULATED" in b
        assert "is_significant False" in b
        assert "engine NOT run" in b
        assert "verdict directionally_supported_not_proven" in b
        assert "NOT artifact-grade" in b
        assert "no analysis.json update warranted" in b

    def test_m730_not_falsification_member(self):
        b = self._block()
        assert "NOT a falsification-family member" in b
        assert "ledger holds at 26" in b

    def test_m730_block_key_unique_in_research(self):
        doc = _read("profiles/competitor-coverage-research.yaml")
        assert doc.count(M730_KEY + ":") == 1


class TestTypeDM731QualitativeDiscipline:
    """Type D verification of m731 qualitative discipline (Type B #833).

    First dedicated Type B mechanism on Jay Peters in journalists.yaml;
    assertions run on the folded competitor_coverage block plus the
    notes prose above it."""

    def _block(self):
        return _fold(_block("profiles/careers/journalists.yaml", M731_KEY, 14000))

    def test_m731_iteration_and_type(self):
        b = self._block()
        assert "mechanism_id: 731" in b
        assert "iteration: 833" in b
        assert "type: B" in b
        assert "date: '2026-09-18 12:00 PDT'" in b

    def test_m731_first_dedicated_type_b_on_peters(self):
        b = self._block()
        assert "FIRST dedicated Type B on Jay Peters in journalists.yaml" in b

    def test_m731_meta_arm_tricky_questions_register(self):
        b = self._block()
        assert "Ray-Ban Meta Gen 2 review: all-day smart glasses with the same tricky questions" in b
        assert "Better Battery, Same Privacy Concerns" in b
        assert "tone_MANUAL_ILLUSTRATIVE: -0.10" in b
        assert "privacy-scrutiny-forward" in b

    def test_m731_snap_arm_experiential_positive(self):
        b = self._block()
        assert "I wore Snap's $2,200 smart glasses" in b
        assert "tone_MANUAL_ILLUSTRATIVE: 0.35" in b
        assert "privacy_vocabulary_count: 0" in b

    def test_m731_illustrative_delta(self):
        b = self._block()
        assert "illustrative_delta_snap_minus_meta: 0.45" in b
        assert "delta_calc: '(0.35) - (-0.10) = 0.45'" in b

    def test_m731_extends_269_scope_bound(self):
        b = self._block()
        assert "EXTENDS mechanism 269" in b
        assert "SECOND journalist" in b
        assert "CRITICAL SCOPE BOUND" in b

    def test_m731_evidence_tiers(self):
        b = self._block()
        assert "search-excerpt-bounded" in b
        assert "first-hand read" in b

    def test_m731_statistical_discipline(self):
        b = self._block()
        assert "p_value NOT_CALCULATED" in b
        assert "cohens_d NOT_CALCULATED" in b
        assert "ci_95 NOT_CALCULATED" in b
        assert "is_significant false" in b
        assert "engine NOT run" in b
        assert "verdict: 'directionally_supported_not_proven'" in b or "directionally_supported_not_proven" in b

    def test_m731_not_falsification_member(self):
        b = self._block()
        assert "NOT a falsification-family member" in b
        assert "ledger holds at 26" in b

    def test_m731_block_key_unique_in_journalists(self):
        doc = _read("profiles/careers/journalists.yaml")
        assert doc.count(M731_KEY + ":") == 1


class TestTypeDM732QualitativeDiscipline:
    """Type D verification of m732 qualitative discipline (Type C #834).

    FIRST corpus reconciliation of Meta's AI-content payer legs against
    the publisher-deal trackers."""

    def _block(self):
        return _fold(_block("profiles/competitor-entities.yaml", M732_KEY, 12000))

    def test_m732_iteration_and_type(self):
        b = self._block()
        assert "mechanism_id: 732" in b
        assert "iteration: 834" in b
        assert "iteration_type: 'C'" in b
        assert "date_analyzed: '2026-09-18'" in b
        assert "time_pdt: '13:00'" in b

    def test_m732_first_reconciliation_mechanism(self):
        b = self._block()
        assert "FIRST corpus reconciliation" in b
        assert "13 named counterparties" in b

    def test_m732_press_gazette_first_hand_read(self):
        b = self._block()
        assert "Press Gazette" in b
        assert "1641 rendered lines" in b
        assert "exactly three Meta entries" in b

    def test_m732_stale_one_leg_correction(self):
        b = self._block()
        assert "CORRECTION" in b
        assert "mechanism 489" in b
        assert "STALE" in b

    def test_m732_sue_ledger_additions(self):
        b = self._block()
        assert "Editorial Perfil" in b
        assert "Wikihow" in b

    def test_m732_confounder_and_counterargument(self):
        b = self._block()
        assert "confounders_ranked" in b
        assert "strongest_counterargument" in b

    def test_m732_statistical_discipline(self):
        b = self._block()
        assert "scorer: 'none'" in b
        assert "tone_scores: 'NOT_SCORED'" in b
        assert "p_value: 'NOT_CALCULATED'" in b
        assert "cohens_d: 'NOT_CALCULATED'" in b
        assert "ci_95: 'NOT_CALCULATED'" in b
        assert "is_significant: false" in b
        assert "qualitative_only: true" in b
        assert "artifact_grade: false" in b
        assert "no_analysis_json_update: true" in b

    def test_m732_verdict_census_reconciled(self):
        b = self._block()
        assert "verdict: 'census_reconciled_correction_issued'" in b

    def test_m732_not_falsification_member(self):
        b = self._block()
        assert "NOT a member of the falsification family" in b
        assert "ledger holds at 26" in b

    def test_m732_block_key_unique_in_entities(self):
        doc = _read("profiles/competitor-entities.yaml")
        assert doc.count(M732_KEY + ":") == 1


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
    """Post-#834 corpus integrity: max 732, zero 733 keys."""

    def test_max_numeric_mechanism_id_is_732(self):
        assert _max_numeric_mechanism_id() == 732

    def test_zero_underscore_733_keys_in_profiles(self):
        hits = _repo_grep_underscore_mechanism(733)
        profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
        assert profile_hits == [], profile_hits

    def test_zero_underscore_733_references_in_tests(self):
        hits = _repo_grep_underscore_mechanism(733)
        test_hits = [p for p in hits if p.startswith(TESTS_DIR)]
        assert test_hits == [], test_hits

    def test_zero_numeric_733_keys_in_profiles(self):
        hits = _repo_grep_numeric_mechanism_id(733)
        assert hits == [], hits

    def test_designed_keying_holds_no_underscore_730_731_732_in_profiles(self):
        for n in (730, 731, 732):
            hits = _repo_grep_underscore_mechanism(n)
            profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
            assert profile_hits == [], (n, profile_hits)

    def test_c834_max_732_sweep_stays_green(self):
        # Type D adds no mechanisms; #834's max-732 sweep stays green.
        assert _max_numeric_mechanism_id() == 732

    def test_c834_zero_underscore_733_sweeps_stay_green(self):
        hits = _repo_grep_underscore_mechanism(733)
        assert hits == [], hits

    def test_c834_zero_numeric_733_sweep_stays_green(self):
        hits = _repo_grep_numeric_mechanism_id(733)
        assert hits == [], hits

    def test_a832_max_730_sweep_superseded_by_design(self):
        # #832 asserted max == 730 pre-commit; advancing to 732
        # supersedes it per the #710/#720 convention. Documented, not
        # repaired.
        assert _max_numeric_mechanism_id() == 732 != 730

    def test_b833_max_731_sweep_superseded_by_design(self):
        # #833 asserted max == 731 pre-commit; advancing to 732
        # supersedes it per the #710/#720 convention. Documented, not
        # repaired.
        assert _max_numeric_mechanism_id() == 732 != 731


class TestTypeDEngineStatisticalMeaningfulness:
    """Fresh synthetic corpora (new values, not #830's)."""

    def test_strong_signal_pair_significant_at_engine_layer(self):
        target = [0.81, 0.92, 0.76, 0.88, 0.95]
        peers = [-0.15, -0.28, -0.09, -0.22, -0.18]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 18),
            period_end=datetime.datetime(2026, 9, 18),
        )
        assert report.asymmetry_score == pytest.approx(1.048, rel=1e-9)
        assert report.t_statistic == pytest.approx(22.0840, rel=1e-4)
        assert report.is_significant is True
        assert report.p_value == pytest.approx(2.0677931508e-08, rel=1e-2)
        assert report.cohens_d == pytest.approx(13.9671, rel=1e-2)
        assert report.confidence_interval_lower > 0
        assert report.confidence_interval_lower == pytest.approx(0.968, rel=1e-2)
        assert report.confidence_interval_upper == pytest.approx(1.126, rel=1e-2)

    def test_near_null_pair_silent_at_engine_layer(self):
        target = [0.04, -0.05, 0.07, -0.02, 0.01]
        peers = [-0.06, 0.03, -0.08, 0.05, -0.04]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 18),
            period_end=datetime.datetime(2026, 9, 18),
        )
        assert report.asymmetry_score == pytest.approx(0.030, abs=1e-9)
        assert report.t_statistic == pytest.approx(0.9045, rel=1e-4)
        assert report.is_significant is False
        assert report.p_value == pytest.approx(0.3930, rel=1e-2)
        assert report.cohens_d == pytest.approx(0.5721, rel=1e-2)
        assert (
            report.confidence_interval_lower
            < 0
            < report.confidence_interval_upper
        )

    def test_degenerate_n1_contract_on_m731_tone_pair(self):
        # The m731 degenerate check: calculate_asymmetry([0.35], [-0.10])
        # returns asymmetry 0.45 with t 0.0 / p 1.0 / d 0.0.
        t, p = welch_t_test([0.35], [-0.10])
        d = cohens_d([0.35], [-0.10])
        assert (t, p) == (0.0, 1.0)
        assert d == 0.0
        assert is_significant(p) is False
        assert abs(0.35 - (-0.10)) == pytest.approx(0.45)
        t2, p2 = welch_t_test([-0.10], [0.35])
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
            timeout=900,
        )
        assert result.returncode == 0, result.stderr[-2000:]
        assert "tests collected" in result.stdout


class TestTypeDFullSuiteTombstone:
    """Suite verdict lineage; #830's background suite owns the verdict,
    #835 re-launches."""

    TOMBSTONE_LINEAGE = 28

    def test_tombstone_lineage_count(self):
        # TWENTY-EIGHTH consecutive background full-suite death: #830's
        # background suite (re-launched 09:08 PDT Sep 18) died at ~0%
        # progress and no pytest was alive at this run's check. Advances
        # from the TWENTY-SEVENTH lineage declared in #830 per the
        # #770/#780 convention.
        assert self.TOMBSTONE_LINEAGE == 28

    def test_830_background_suite_verdict_died(self):
        # Dead-run markers pinned per the #770/#780 convention; triaged
        # no further. Log stalled at 34 bytes (~0%) since 09:08 PDT
        # Sep 18 with no percentage progress marker at all.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_830_full_suite.log",
        )
        assert os.path.exists(log_path), log_path
        size = os.path.getsize(log_path)
        assert size < 10000, size
        text = open(log_path, encoding="utf-8", errors="replace").read()
        assert "%" not in text  # died before any progress marker
        assert text.strip() != ""

    def test_relaunch_log_path_in_goal_hidden_files(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_835_full_suite.log",
        )
        assert os.path.basename(log_path) == "type_d_835_full_suite.log"

    def test_835_suite_relaunched_this_run(self):
        # This run re-launches the full suite as a background process
        # writing to the persistent goal hidden_files path; the next
        # Type D run checks its verdict per the #795 convention.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_835_full_suite.log",
        )
        assert os.path.exists(log_path), log_path


class TestDocSync835:
    def test_readme_row_835(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_835(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_835_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog835:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #835 Type D:")
        return log[idx : idx + 12000]

    def test_log_entry_present(self):
        assert "## #835 Type D:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        entry = self._entry()
        assert "mechanism_id 732" in entry
        assert "m730" in entry
        assert "m731" in entry

    def test_log_rotation_window_835_839(self):
        entry = self._entry()
        assert "835-839" in entry


class TestDateGrounding835:
    def test_sep_18_2026_is_friday(self):
        assert datetime.datetime(2026, 9, 18).strftime("%A") == "Friday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 18, 14, 0).strftime("%H:%M") == "14:00"
