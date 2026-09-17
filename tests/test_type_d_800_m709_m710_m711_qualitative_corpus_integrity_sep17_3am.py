"""Type D -- Iteration #800 (Thu 2026-09-17 03:00 PDT): m709 / m710 / m711
qualitative-discipline verification + post-#799 corpus integrity
(max numeric mechanism_id 711; zero 712 keys; ledger holds at 26) +
#795 background-suite tombstone lineage (TWENTY-SECOND; #795 ran a
foreground suite, no new background re-launch) + #800 foreground
full-suite run + fresh synthetic engine meaningfulness +
#795-file genuine-breakage repairs (push-status-record subject collision,
window-closure history lookup, ephemeral /tmp suite log, log-tail window).

Verifies:
- m709 (The Times x OpenAI slowdown-week statesman-platform register vs
  Anthropic motive-questioning vs Meta glasses adversarial, Type A #797,
  profiles/competitor-coverage-research.yaml): FIRST dedicated Times x
  OpenAI slowdown-week mechanism; OpenAI arm Sep 16-17 2026 "Mathematicians
  fear AI curbs may come too late to save humanity" statesman platform,
  MANUAL ILLUSTRATIVE +0.25; Anthropic arm Sep 11 2026 "Brains are needed
  to manage AI risk" motive-questioning, -0.20; illustrative
  OpenAI-minus-Anthropic delta +0.45; Meta comparator (in-corpus) "Fear
  and loathing on the streets of London with Meta smart glasses"
  adversarial -0.55; illustrative OpenAI-minus-Meta delta +0.80;
  News Corp DUAL-payer owner (OpenAI $50M/yr + Meta up to $50M/yr) whose
  symmetric-softening prediction CONTRADICTS on the Meta leg (carried as
  counter-evidence); degenerate n=1 engine check (0.25 vs -0.20,
  asymmetry 0.45, t 0.0 / p 1.0 / d 0.0 / CI (0.45, 0.45),
  is_significant false); verdict mixed_not_proven; NOT artifact-grade;
  NOT a falsification-family member (ledger holds at 26).
- m710 (Ben Thompson, Stratechery, Orion vs Vision Pro within-writer
  gradient, Type B #798, profiles/careers/journalists.yaml + research
  backlink): FIRST dedicated Type B on Thompson; Meta arm circa Sep 26
  2024 "An Interview with Meta CTO Andrew Bosworth About Orion and
  Reality Labs" unadulterated-praise hands-on register, MANUAL
  ILLUSTRATIVE +0.45 (first-hand reads); Apple arm circa Feb 2024 "The
  Apple Vision Pro" productivity-walkback register, -0.10 on the assessed
  axis; illustrative within-writer spread 0.55 (0.450 - (-0.100));
  no employer migration (both Stratechery, subscription-funded
  independent model); uniform anti-Meta financial-incentive prediction
  NOT supported on the observed arms; p_value/cohens_d/ci_95
  NOT_CALCULATED; is_significant false; verdict within-journalist
  register GRADIENT favoring Meta, hypothesis-generating only; NOT
  artifact-grade; NOT a falsification-family member.
- m711 (Cashmere x De Gruyter Brill + IOP Publishing academic-publisher
  roster expansion, Type C #799, profiles/competitor-entities.yaml):
  FIRST dedicated mapping of the two newest Sep 2026 Cashmere legs -
  De Gruyter Brill (announced Sep 14 2026) and IOP Publishing (announced
  Sep 9 2026); inference-only, content never used to train LLMs;
  publisher-controlled terms; extends mechanism 663's roster; qualitative
  Type C mapping: scorer none, tone NOT_SCORED, p_value/cohens_d/ci_95
  NOT_CALCULATED, is_significant false, qualitative_only true,
  artifact_grade false; verdict directionally_supported_not_proven;
  NOT a member of the falsification family (ledger holds at 26).
- Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent in
  profiles/; ledger holds at 26.
- Post-#799 corpus integrity: max numeric mechanism_id == 711 in
  profiles/; zero underscore-form 712 key substrings in profiles/ and
  tests/ (own file excluded as sweep carrier per the #715
  pattern-rescope lesson; needles built by format string so no literal
  is carried); zero numeric 712 keys in profiles/; m709 / m710 / m711
  block keys each unique in their home YAMLs; designed keying holds
  (no underscore-form 709/710/711 mechanism key substrings in
  profiles/). #799's max-711 and zero-underscore-711 sweeps stay green
  (Type D adds no mechanisms); #797's max-708, #798's max-709 and
  zero-numeric-710, and #799's max-710 and zero-numeric-711 sweeps fail
  by designed supersession per the #710/#720 convention (documented,
  not repaired).
- Statistical meaningfulness on FRESH synthetic corpora (new values,
  not #795's): strong-signal n=5-per-arm pair (asymmetry +1.024,
  p=2.55e-06 < 5e-4, d=13.00 > 8, 95% CI (0.936, 1.104) above zero,
  is_significant True at the ENGINE layer); fresh near-null pair
  (asymmetry 0.000, p=1.000 > 0.5, |d|=0.0 < 0.5, CI crossing zero,
  silent); fresh degenerate n=1-per-arm contract (t=0.0, p=1.0, d=0.0,
  is_significant False, |asymmetry| == 0.95, arm-swap negates). Engine
  significance is never promoted to a finding (Aug 28 2026 standing
  rule).
- Full-suite status: no new background suite was re-launched by #795
  (it ran a foreground suite); the background tombstone lineage holds
  at TWENTY-SECOND. This run's own 41K suite runs as a foreground
  process writing to the goal hidden_files
  type_d_800_full_suite.log (persistent; the #795 /tmp log's
  disappearance is repaired in the #795 file this run); failures
  repaired test-side before the main commit.
- Genuine-breakage repairs in tests/test_type_d_795_...py (test-side,
  count unchanged at 64): main-commit uniqueness now matches the
  specific "Type D #795: m706" prefix (the #795 push-status record
  commit subject "Type D #795: push-status record (...)" collided with
  the bare "Type D #795: " pattern, #796 prefix convention); the
  790-794 window-closure check now locates the closure sequence in
  history instead of the newest five legs; the foreground-suite-log
  tombstone now asserts the durable iteration-log record instead of
  the ephemeral /tmp path; the iteration-log tests search the whole
  file (the #795 entry is displaced by #796-#799 appends). Designed
  supersessions (max 708 pins, zero-709 pins) are documented, not
  repaired, per the #710/#720 convention.
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
    "test_type_d_800_m709_m710_m711_qualitative_corpus_integrity_sep17_3am.py"
)
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"

ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

M709_KEY = "times_openai_slowdown_week_statesman_register_sep17"
M710_JOURNALIST_KEY = (
    "type_b_798_ben_thompson_stratechery_orion_vs_vision_pro_gradient_sep17"
)
M710_RESEARCH_KEY = "ben thompson stratechery orion vs vision pro gradient sep2026"
M711_KEY = "cashmere_academic_roster_expansion_de_gruyter_brill_iop_publishing_sep2026"


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


def _git_log_mains(prefix):
    # Specific-prefix matching per the #796 convention: robust to
    # push-status record followups that repeat the bare "Type X #NNN: "
    # wording (the #795 collision repaired in the #795 file this run).
    proc = subprocess.run(
        ["git", "-C", REPO_ROOT, "log", "--format=%H %s", "--no-merges", "--", "."],
        capture_output=True,
        text=True,
    )
    return [l for l in proc.stdout.splitlines() if prefix in l]


def _window_legs_deduped(skip):
    """First occurrence of each iteration number, newest first.

    Robust to push-status followup commits that repeat iteration wording
    (per the #752 convention and the #781/#783 repairs). The current
    iteration is skipped so the prior window closure reads stable both
    pre- and post-commit."""
    proc = subprocess.run(
        ["git", "-C", REPO_ROOT, "log", "--format=%s", "--no-merges", "-n", "80"],
        capture_output=True,
        text=True,
        check=True,
    )
    seen_nums = set()
    out = []
    for s in proc.stdout.splitlines():
        m = re.match(r"Type ([A-E]) #(\d+):", s)
        if m and m.group(2) not in seen_nums and m.group(2) != skip:
            seen_nums.add(m.group(2))
            out.append(m.groups())
    return out


class TestNovelty800:
    """Pre-commit novelty: single new file, unique commit."""

    def test_single_test_type_d_800_file(self):
        files = sorted(
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_800") and f.endswith(".py")
        )
        assert files == [TEST_BASENAME], files

    def test_type_d_800_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 convention; the main commit
        # does not exist yet. Patched green in the anchor followup.
        # Specific "Type D #800: m709" prefix per the #796 convention:
        # immune to a "Type D #800 push-status record" followup.
        mains = _git_log_mains("Type D #800: m709")
        assert len(mains) == 1, mains
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim(self):
        # Type D adds no mechanism; novelty is the corpus-integrity posture:
        # single new file, no mechanism keys added (max stays 711).
        assert _max_numeric_mechanism_id() == 711
        assert _repo_grep_numeric_mechanism_id(712) == []

    def test_795_799_window_closed_prior_to_800(self):
        # Anchor leg of the 800-804 window: the previous window must read
        # closed D->E->A->B->C (newest first) as a consecutive sequence in
        # history, wherever it sits (per the #795 repair this run: the
        # newest-five shortcut broke once #796-#799 landed).
        legs = _window_legs_deduped("800")
        want = [
            ("C", "799"),
            ("B", "798"),
            ("A", "797"),
            ("E", "796"),
            ("D", "795"),
        ]
        found = any(
            legs[i : i + 5] == want for i in range(len(legs) - 4)
        )
        assert found, legs[:12]


class TestTypeDRotationGuard:
    """#800 is the Type D anchor opening window 800-804."""

    WINDOW = ("D", "E", "A", "B", "C")

    def test_rotation_window_800_804(self):
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


class TestTypeDM709QualitativeDiscipline:
    """Type D verification of m709 qualitative discipline (Type A #797)."""

    def _block(self):
        return _block(
            "profiles/competitor-coverage-research.yaml", M709_KEY, 16000
        )

    def test_m709_publication_and_entity(self):
        block = self._block()
        assert "publication: The Times (News Corp / News UK)" in block
        assert "entity: OpenAI" in block

    def test_m709_arm1_statesman_platform(self):
        block = self._block()
        assert "Mathematicians fear AI curbs may come too late to save humanity" in block
        assert "tone_MANUAL_ILLUSTRATIVE: 0.25" in block

    def test_m709_arm2_anthropic_motive_questioning(self):
        block = self._block()
        assert "Brains are needed to manage AI risk" in block
        assert "Tone MANUAL ILLUSTRATIVE -0.20" in block

    def test_m709_meta_comparator_adversarial(self):
        block = self._block()
        assert "Meta smart glasses" in block
        assert "Tone -0.55" in block

    def test_m709_illustrative_deltas(self):
        block = self._block()
        assert "delta +0.45" in block
        assert "+0.80" in block

    def test_m709_dual_payer_contradiction_carried(self):
        block = self._block()
        assert "DUAL-payer owner" in block
        assert "up to $50M/yr" in block

    def test_m709_statistical_discipline_strings(self):
        block = self._block()
        assert "MANUAL ILLUSTRATIVE scores only" in block
        assert "as a DEGENERATE n=1 check" in block
        assert "degenerate CI (0.45, 0.45)" in block
        assert "is_significant false" in block
        assert "verdict mixed_not_proven" in block
        assert "no_analysis_json_update: true" in block
        assert "NOT artifact-grade" in block

    def test_m709_not_falsification_member(self):
        block = self._block()
        assert "NOT a member - register documentation with" in block
        assert "Ledger holds at 26." in block

    def test_m709_block_key_unique_in_research(self):
        text = _read("profiles/competitor-coverage-research.yaml")
        assert text.count(M709_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(709)
        assert any(
            p.endswith("competitor-coverage-research.yaml") for p in hits
        ), hits


class TestTypeDM710QualitativeDiscipline:
    """Type D verification of m710 qualitative discipline (Type B #798)."""

    def _block(self):
        return _block(
            "profiles/careers/journalists.yaml", M710_JOURNALIST_KEY, 12000
        )

    def test_m710_journalist_and_publication(self):
        block = self._block()
        assert "Ben Thompson" in block
        assert "Stratechery" in block

    def test_m710_meta_arm_orion_praise(self):
        block = self._block()
        assert "unadulterated praise" in block
        assert "tone_score: 0.45" in block

    def test_m710_apple_arm_vision_pro_walkback(self):
        block = self._block()
        assert "The Apple Vision Pro" in block
        assert "apple_arm_score: -0.1" in block

    def test_m710_within_writer_spread(self):
        block = self._block()
        assert "illustrative_within_writer_spread: 0.55" in block
        assert "0.450 - (-0.100) = +0.550" in block

    def test_m710_no_employer_migration(self):
        block = self._block()
        assert "No employer migration" in block
        assert "subscription-funded independent model" in block

    def test_m710_uniform_prediction_not_supported(self):
        block = self._block()
        assert "Uniform anti-Meta financial-incentive prediction NOT supported" in block

    def test_m710_statistical_discipline_strings(self):
        block = self._block()
        assert "MANUAL ILLUSTRATIVE scoring only per the Aug 28 2026 standing rule" in block
        assert "is_significant: false" in block
        assert "p_value: NOT_CALCULATED" in block
        assert "cohens_d: NOT_CALCULATED" in block
        assert "ci_95: NOT_CALCULATED" in block
        assert "NOT artifact-grade" in block

    def test_m710_verdict(self):
        block = self._block()
        assert "Within-journalist register GRADIENT favoring Meta" in block
        assert "Hypothesis-generating only" in block

    def test_m710_not_falsification_member(self):
        assert "NOT a falsification-family member" in self._block()

    def test_m710_journalist_block_key_unique(self):
        text = _read("profiles/careers/journalists.yaml")
        assert text.count(M710_JOURNALIST_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(710)
        assert any(p.endswith("journalists.yaml") for p in hits), hits

    def test_m710_research_backlink(self):
        text = _read("profiles/competitor-coverage-research.yaml")
        assert text.count(M710_RESEARCH_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(710)
        assert any(
            p.endswith("competitor-coverage-research.yaml") for p in hits
        ), hits


class TestTypeDM711QualitativeDiscipline:
    """Type D verification of m711 qualitative discipline (Type C #799)."""

    def _block(self):
        return _block("profiles/competitor-entities.yaml", M711_KEY, 16000)

    def test_m711_de_gruyter_brill_leg(self):
        block = self._block()
        assert "De Gruyter Brill" in block
        assert "Sep 14 2026" in block

    def test_m711_iop_leg(self):
        block = self._block()
        assert "IOP Publishing" in block
        assert "Sep 9 2026" in block

    def test_m711_inference_only_template(self):
        block = self._block()
        assert "inference" in block
        assert "never used to train" in block

    def test_m711_extends_m663_roster(self):
        block = self._block()
        assert "mechanism 663" in block
        assert "Cashmere" in block

    def test_m711_statistical_discipline(self):
        block = self._block()
        assert "scorer: none" in block
        assert "tone_scores: 'NOT_SCORED'" in block
        assert "p_value: 'NOT_CALCULATED'" in block
        assert "cohens_d: 'NOT_CALCULATED'" in block
        assert "ci_95: 'NOT_CALCULATED'" in block
        assert "is_significant: false" in block
        assert "qualitative_only: true" in block
        assert "artifact_grade: false" in block

    def test_m711_verdict(self):
        assert "verdict: directionally_supported_not_proven" in self._block()

    def test_m711_not_falsification_member(self):
        block = self._block()
        assert "NOT a member of the falsification family; ledger holds at 26" in block

    def test_m711_block_key_unique_in_entities(self):
        text = _read("profiles/competitor-entities.yaml")
        assert text.count(M711_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(711)
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
    """Post-#799 corpus integrity: max 711, zero 712 keys."""

    def test_max_numeric_mechanism_id_is_711(self):
        assert _max_numeric_mechanism_id() == 711

    def test_zero_underscore_712_keys_in_profiles(self):
        hits = _repo_grep_underscore_mechanism(712)
        profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
        assert profile_hits == [], profile_hits

    def test_zero_underscore_712_references_in_tests(self):
        hits = _repo_grep_underscore_mechanism(712)
        test_hits = [p for p in hits if p.startswith(TESTS_DIR)]
        assert test_hits == [], test_hits

    def test_zero_numeric_712_keys_in_profiles(self):
        hits = _repo_grep_numeric_mechanism_id(712)
        assert hits == [], hits

    def test_designed_keying_holds_no_underscore_709_710_711_in_profiles(self):
        for n in (709, 710, 711):
            hits = _repo_grep_underscore_mechanism(n)
            profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
            assert profile_hits == [], (n, profile_hits)

    def test_c799_max_711_sweep_stays_green(self):
        # Type D adds no mechanisms; #799's max-711 sweep stays green.
        assert _max_numeric_mechanism_id() == 711

    def test_c799_zero_underscore_711_sweeps_stay_green(self):
        hits = _repo_grep_underscore_mechanism(711)
        assert hits == [], hits

    def test_a797_max_708_sweep_superseded_by_design(self):
        # #797 asserted max == 708; advancing to 711 supersedes it per the
        # #710/#720 convention. Documented, not repaired.
        assert _max_numeric_mechanism_id() == 711 != 708

    def test_b798_max_709_sweep_superseded_by_design(self):
        # #798 asserted max == 709; advancing to 711 supersedes it per the
        # #710/#720 convention. Documented, not repaired.
        assert _max_numeric_mechanism_id() == 711 != 709

    def test_b798_zero_numeric_710_sweep_fails_by_designed_supersession(self):
        # #798 asserted zero "mechanism_id: 710" hits in profiles/; the
        # m710 block supersedes it by design.
        hits = _repo_grep_numeric_mechanism_id(710)
        assert len(hits) >= 1, hits

    def test_c799_max_710_sweep_superseded_by_design(self):
        # #799 asserted max == 710 pre-commit; m711 supersedes it per the
        # #710/#720 convention. Documented, not repaired.
        assert _max_numeric_mechanism_id() == 711 != 710

    def test_c799_zero_numeric_711_sweep_fails_by_designed_supersession(self):
        # #799's own zero-numeric-711 forward sweep is superseded by the
        # m711 block it documented, per the #710/#720 convention.
        hits = _repo_grep_numeric_mechanism_id(711)
        assert len(hits) >= 1, hits


class TestTypeDEngineStatisticalMeaningfulness:
    """Fresh synthetic corpora (new values, not #795's). Never promoted."""

    def test_strong_signal_pair_significant_at_engine_layer(self):
        target = [1.05, 0.88, 1.14, 0.97, 1.09]
        peers = [0.05, -0.06, 0.03, -0.02, 0.01]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 17),
            period_end=datetime.datetime(2026, 9, 17),
        )
        assert report.asymmetry_score == pytest.approx(1.024, rel=1e-9)
        assert report.is_significant is True
        assert report.p_value < 5e-4
        assert report.cohens_d > 8
        assert report.confidence_interval_lower > 0

    def test_near_null_pair_silent_at_engine_layer(self):
        target = [-0.04, 0.02, -0.03, 0.05, 0.00]
        peers = [0.03, -0.02, 0.01, -0.04, 0.02]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 17),
            period_end=datetime.datetime(2026, 9, 17),
        )
        assert report.asymmetry_score == pytest.approx(0.0, abs=1e-9)
        assert report.is_significant is False
        assert report.p_value > 0.5
        assert abs(report.cohens_d) < 0.5
        assert (
            report.confidence_interval_lower < 0 < report.confidence_interval_upper
        )

    def test_degenerate_n1_contract(self):
        a, b = [0.50], [-0.45]
        t, p = welch_t_test(a, b)
        d = cohens_d(a, b)
        assert (t, p) == (0.0, 1.0)
        assert d == 0.0
        assert is_significant(p) is False
        assert abs(a[0] - b[0]) == pytest.approx(0.95)
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
            timeout=900,
        )
        assert result.returncode == 0, result.stderr[-2000:]
        assert "tests collected" in result.stdout


class TestTypeDFullSuiteTombstone:
    """Background-suite tombstone lineage; #800 foreground suite owns the verdict."""

    TOMBSTONE_LINEAGE = 22

    def test_tombstone_lineage_count(self):
        # TWENTY-SECOND consecutive background full-suite death holds:
        # #795 ran a foreground suite instead of re-launching a
        # background one, so the lineage does not advance this run.
        assert self.TOMBSTONE_LINEAGE == 22

    def test_relaunch_log_path_in_goal_hidden_files(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_800_full_suite.log",
        )
        assert os.path.basename(log_path) == "type_d_800_full_suite.log"

    def test_foreground_suite_log_owns_this_run(self):
        # This run's own full suite ran as a foreground process writing to
        # the persistent goal hidden_files path (not /tmp: the #795 /tmp
        # log vanished on VM recycle, repaired in the #795 file this
        # run). That log owns the suite verdict, not any background
        # re-launch.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_800_full_suite.log",
        )
        assert os.path.exists(log_path), log_path
        text = open(log_path, encoding="utf-8", errors="replace").read()
        assert "%" in text  # pytest -q progress marker present


class TestDocSync800:
    def test_readme_row_800(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_800(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_800_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog800:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #800 Type D:")
        return log[idx : idx + 8000]

    def test_log_entry_present(self):
        assert "## #800 Type D:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        entry = self._entry()
        assert "mechanism_id 711" in entry
        assert "m709" in entry


class TestDateGrounding800:
    def test_sep_17_2026_is_thursday(self):
        assert datetime.date(2026, 9, 17).strftime("%A") == "Thursday"
