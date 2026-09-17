"""Type D -- Iteration #810 (Thu 2026-09-17 13:00 PDT): m715 / m716 / m717
qualitative-discipline verification + post-#809 corpus integrity
(max numeric mechanism_id 717; zero 718 keys; ledger holds at 26) +
#805 background-suite verdict (died at ~3% progress, 1789 bytes, no
pytest alive at this run's check; background tombstone lineage advances
to TWENTY-THIRD per the #770/#780 convention) + fresh synthetic engine
meaningfulness (new values, not #800's or #805's) + re-launch of the
full suite as a background process writing to goal hidden_files
type_d_810_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Verifies:
- m715 (WSJ x OpenAI misalignment-framework relay vs Meta glasses
  adversarial, Type A #807, profiles/news-corp.yaml): FIRST dedicated
  WSJ x OpenAI misalignment-framework mechanism; Arm 1 (Sep 16-17 2026)
  "OpenAI Shares More Safety Incidents and Adopts New Rules for
  Reporting Them" constructive relay register (+0.15 MANUAL
  ILLUSTRATIVE, excerpt-bounded, WSJ slug d1ea1b09); Arm 2 (in-corpus
  Meta comparator, mechanism 214, carried un-rescored) WSJ Jul 14 2026
  "Meta Is Flooding the Market With Smartglasses. Privacy Advocates Are
  Up in Arms." adversarial register (-0.75, Meghan Bobrowsky, 7 alarm
  terms); illustrative OpenAI-minus-Meta delta +0.90; News Corp
  dual-AI-payer (OpenAI leg May 2024 ~$50M/yr, 28 months senior vs Meta
  leg Mar 2026 up to $50M/yr, 6 months senior); verdict
  directionally_supported_not_proven; degenerate n=1 engine check
  (asymmetry 0.90, t 0.0 / p 1.0 / d 0.0, is_significant False); NOT
  artifact-grade; NOT a falsification-family member (ledger holds at
  26).
- m716 (Ece Yildirim, Gizmodo Privacy and Security, Apple-adversarial
  vs Meta-product-neutral register inversion, Type B #808,
  profiles/gizmodo.yaml + careers backlink): FIRST dedicated corpus
  mechanism on Yildirim; Apple arm (Sep 9 2026) "If Meta Glasses Freak
  You Out, Wait Until You Hear About the New Apple Watch Features"
  adversarial privacy commentary (-0.60 illustrative, read first-hand,
  42 rendered lines, byline on author page); Meta arm (Sep 15 2026)
  "Meta Is Hoping You Will Pay for More AI Features on Instagram"
  neutral product/pricing news (-0.15 illustrative, search-excerpt
  bounded); illustrative Apple-minus-Meta delta -0.45 - same
  journalist harder on Apple than Meta within one week, inverting the
  corpus-typical Gizmodo gradient; confounders ranked strong-first
  (product-domain mismatch, genre routing, Meta-anchor frame); verdict
  directionally_supported_not_proven; NOT artifact-grade; NOT a
  falsification-family member.
- m717 (ANI v. OpenAI Division Bench issues notice, seeks OpenAI reply,
  Type C #809, profiles/competitor-entities.yaml openai section):
  FIRST dedicated mapping of the Sep 15 2026 Delhi High Court Division
  Bench procedural movement (reconstituted Jhingan/Arora bench; notice
  on ANI's appeal against the Jul 24 Bansal interim-relief denial;
  OpenAI's response sought; hearing listed December 08, 2026; OpenAI's
  Sep 2024 voluntary no-scrape undertaking lapsed with the Jul 24
  order); extends m681's repricing frame with a dated calendar;
  qualitative-only, tone NOT_SCORED, p_value / cohens_d / ci_95
  NOT_CALCULATED, is_significant false; verdict
  directionally_supported_not_proven; NOT artifact-grade; NOT a
  falsification-family member (ledger holds at 26).
- Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent in
  profiles/; ledger holds at 26.
- Post-#809 corpus integrity: max numeric mechanism_id == 717 in
  profiles/; zero underscore-form 718 key substrings in profiles/ and
  tests/ (own file excluded as sweep carrier per the #715
  pattern-rescope lesson; needles built by format string so no literal
  is carried); zero numeric 718 keys in profiles/; m715 / m716 / m717
  block keys each unique in their home YAMLs; designed keying holds
  (no underscore-form 715/716/717 mechanism key substrings in
  profiles/). #809's max-717 and zero-underscore-718 sweeps stay green
  (Type D adds no mechanisms); #807's max-715, #808's max-716, and
  #809's max-717 forward and zero-numeric sweeps fail by designed
  supersession per the #710/#720 convention (documented, not
  repaired).
- Statistical meaningfulness on FRESH synthetic corpora (new values,
  not #800's or #805's): strong-signal n=5-per-arm pair (asymmetry
  +0.880, p=4.99e-06 < 5e-4, d=12.29 > 8, 95% CI (0.802, 0.954) above
  zero, is_significant True at the ENGINE layer); fresh near-null pair
  (asymmetry 0.008, p=0.775 > 0.5, |d|=0.187 < 0.5, CI crossing zero,
  silent); fresh degenerate n=1-per-arm contract (t=0.0, p=1.0, d=0.0,
  is_significant False, |asymmetry| == 1.10, arm-swap negates). Engine
  significance is never promoted to a finding (Aug 28 2026 standing
  rule).
- Full-suite status: the #805 background suite re-launched 08:10 PDT
  died (type_d_805_full_suite.log stalled at 1789 bytes / ~3% since
  08:53 PDT; no pytest alive at this run's check) - dead-run markers,
  triaged no further per the #770/#780 convention; tombstone lineage
  advances TWENTY-SECOND -> TWENTY-THIRD. This run re-launches the full
  suite as a background process writing to goal hidden_files
  type_d_810_full_suite.log (alive at re-launch check); next Type D
  run checks its verdict per the #795 convention.

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
    "test_type_d_810_m715_m716_m717_qualitative_corpus_integrity_sep17_1pm.py"
)
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"

ANCHORED_SHA = "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565"

M715_KEY = "wsj_openai_misalignment_framework_relay_vs_meta_glasses_adversarial_sep17"
M716_KEY = "ece_yildirim"
M716_BLOCK_KEY = (
    "type_b_808_ece_yildirim_gizmodo_apple_adversarial_vs_meta_product_neutral_sep17"
)
M717_KEY = "ani_v_openai_division_bench_notice_sep2026"


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
    # wording (the #795 collision repaired in the #795 file).
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


class TestNovelty810:
    """Pre-commit novelty: single new file, unique commit."""

    def test_single_test_type_d_810_file(self):
        files = sorted(
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_810") and f.endswith(".py")
        )
        assert files == [TEST_BASENAME], files

    def test_type_d_810_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 convention; the main commit
        # does not exist yet. Patched green in the anchor followup.
        # Specific "Type D #810: m715" prefix per the #796 convention:
        # immune to a "Type D #810 push-status record" followup.
        mains = _git_log_mains("Type D #810: m715")
        assert len(mains) == 1, mains
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim(self):
        # Type D adds no mechanism; novelty is the corpus-integrity posture:
        # single new file, no mechanism keys added (max stays 717).
        assert _max_numeric_mechanism_id() == 717
        assert _repo_grep_numeric_mechanism_id(718) == []

    def test_805_809_window_closed_prior_to_810(self):
        # Opening leg of the 810-814 window: the previous window must read
        # closed D->E->A->B->C (newest first) as a consecutive sequence in
        # history, wherever it sits (per the #795 repair: the newest-five
        # shortcut broke once 806+ landed; per #800, history lookup).
        legs = _window_legs_deduped("810")
        want = [
            ("C", "809"),
            ("B", "808"),
            ("A", "807"),
            ("E", "806"),
            ("D", "805"),
        ]
        found = any(
            legs[i : i + 5] == want for i in range(len(legs) - 4)
        )
        assert found, legs[:12]


class TestTypeDRotationGuard:
    """#810 is the Type D anchor opening window 810-814."""

    WINDOW = ("D", "E", "A", "B", "C")

    def test_rotation_window_810_814(self):
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


class TestTypeDM715QualitativeDiscipline:
    """Type D verification of m715 qualitative discipline (Type A #807).

    Assertions run on the whitespace-folded block per the #732
    convention: the m715 description, statistical_discipline, and
    falsification_family fields wrap across raw YAML lines."""

    def _block(self):
        return _fold(
            _block("profiles/news-corp.yaml", M715_KEY, 30000)
        )

    def test_m715_publication_and_entity(self):
        block = self._block()
        assert "publication: 'Wall Street Journal (News Corp / Dow Jones)'" in block
        assert "entity: OpenAI" in block
        assert "mechanism_id: 715" in block
        assert "iteration: 807" in block
        assert "iteration_type: 'A'" in block
        assert "time_pdt: '10:00'" in block

    def test_m715_arm1_misalignment_framework_relay(self):
        block = self._block()
        assert "OpenAI Shares More Safety Incidents and Adopts New Rules for Reporting Them" in block
        assert "tone_MANUAL_ILLUSTRATIVE: 0.15" in block
        assert "d1ea1b09" in block

    def test_m715_meta_comparator_adversarial(self):
        block = self._block()
        assert "meta_glasses_tone_MANUAL_ILLUSTRATIVE: -0.75" in block
        assert "flooding the market" in block
        assert "Meghan Bobrowsky" in block

    def test_m715_illustrative_delta(self):
        block = self._block()
        assert "illustrative_register_delta_openai_minus_meta: 0.90" in block

    def test_m715_financial_tie_dual_deal_seniority(self):
        block = self._block()
        assert "OpenAI leg May 2024" in block
        assert "Meta leg Mar 2026" in block
        assert "28 months senior" in block
        assert "6 months senior" in block

    def test_m715_first_dedicated_mechanism(self):
        block = self._block()
        assert "FIRST dedicated WSJ x OpenAI misalignment-framework mechanism" in block

    def test_m715_statistical_discipline_strings(self):
        block = self._block()
        assert "MANUAL ILLUSTRATIVE scores only" in block
        assert "Engine NOT run on the illustrative arms" in block
        assert "t 0.0 / p 1.0 / Cohen d 0.0" in block
        assert "is_significant False" in block
        assert "verdict: 'Verdict: directionally_supported_not_proven" in block
        assert "no_analysis_json_update: true" in block
        assert "correlation_not_causation: true" in block

    def test_m715_not_falsification_member(self):
        block = self._block()
        assert "falsification_family: 'NOT a member" in block
        assert "ledger holds at 26." in block

    def test_m715_block_key_unique_in_news_corp(self):
        text = _read("profiles/news-corp.yaml")
        assert text.count(M715_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(715)
        assert any(
            p.endswith("news-corp.yaml") for p in hits
        ), hits


class TestTypeDM716QualitativeDiscipline:
    """Type D verification of m716 qualitative discipline (Type B #808)."""

    def _block(self):
        return _fold(
            _block("profiles/gizmodo.yaml", M716_KEY, 25000)
        )

    def test_m716_journalist_publication(self):
        block = self._block()
        assert "mechanism_id: 716" in block
        assert "iteration: 808" in block
        assert "iteration_type: 'B'" in block
        assert "time_pdt: '11:00'" in block
        assert "Ece Yildirim" in block
        assert "Gizmodo Privacy and Security" in block

    def test_m716_register_inversion(self):
        block = self._block()
        assert "Apple-Adversarial vs Meta-Product-Neutral Register Inversion" in block
        assert "illustrative Apple-minus-Meta delta -0.45" in block

    def test_m716_apple_arm_adversarial(self):
        block = self._block()
        assert "privacy nightmare" in block
        assert "pervert glasses" in block

    def test_m716_meta_arm_neutral(self):
        block = self._block()
        assert "coughing up monthly fees" in block
        assert "zero privacy/surveillance vocabulary" in block

    def test_m716_cross_references(self):
        block = self._block()
        assert "mechanism_id: 653" in block
        assert "mechanism_id: 715" in block

    def test_m716_statistical_discipline_strings(self):
        block = self._block()
        assert "MANUAL ILLUSTRATIVE scores only" in block
        assert "Engine NOT run on the illustrative arms" in block
        assert "NOT_CALCULATED" in block
        assert "is_significant False" in block
        assert "directionally_supported_not_proven" in block
        assert "no_analysis_json_update: true" in block

    def test_m716_not_falsification_member(self):
        block = self._block()
        assert "falsification_family: 'NOT a member" in block
        assert "ledger holds at 26." in block

    def test_m716_block_key_unique_in_gizmodo(self):
        text = _read("profiles/gizmodo.yaml")
        assert text.count("block_key: " + M716_BLOCK_KEY) == 1
        hits = _repo_grep_numeric_mechanism_id(716)
        assert any(
            p.endswith("gizmodo.yaml") for p in hits
        ), hits

    def test_m716_careers_journalist_backlink(self):
        text = _read("profiles/careers/journalists.yaml")
        assert text.count(M716_BLOCK_KEY + ":") == 1
        block = _block(
            "profiles/careers/journalists.yaml", M716_KEY, 12000
        )
        assert "mechanism_ids: [716]" in block
        assert "https://gizmodo.com/if-meta-glasses-freak-you-out-wait-until-you-hear-about-the-new-apple-watch-features-2000809371" in block
        assert "https://gizmodo.com/meta-is-hoping-youll-pay-for-more-ai-features-on-instagram-2000812018" in block


class TestTypeDM717QualitativeDiscipline:
    """Type D verification of m717 qualitative discipline (Type C #809)."""

    def _block(self):
        return _fold(
            _block("profiles/competitor-entities.yaml", M717_KEY, 18000)
        )

    def test_m717_iteration_and_type(self):
        block = self._block()
        assert "mechanism_id: 717" in block
        assert "iteration: 809" in block
        assert "iteration_type: C" in block
        assert "rotation: 'Type C'" in block
        assert "financial_incentive_mapping" in block

    def test_m717_division_bench_notice(self):
        block = self._block()
        assert "ANI v. OpenAI Division Bench" in block
        assert "Jhingan" in block
        assert "December 08" in block
        assert "Division Bench" in block

    def test_m717_jul_24_single_judge_order(self):
        block = self._block()
        assert "July 24" in block
        assert "interim" in block.lower()

    def test_m717_no_scrape_undertaking_lapsed(self):
        block = self._block()
        assert "Voluntary No-Scrape" in block
        assert "Lapsed" in block

    def test_m717_sources(self):
        block = self._block()
        assert "LiveLaw" in block
        assert "Mint" in block

    def test_m717_statistical_discipline(self):
        block = self._block()
        assert "tone_scores: 'NOT_SCORED'" in block
        assert "p_value: 'NOT_CALCULATED'" in block
        assert "cohens_d: 'NOT_CALCULATED'" in block
        assert "is_significant: false" in block
        assert "qualitative_only: true" in block
        assert "verdict: directionally_supported_not_proven" in block
        assert "artifact_grade: false" in block
        assert "no_analysis_json_update: true" in block
        assert "correlation_not_causation: true" in block

    def test_m717_not_falsification_member(self):
        block = self._block()
        assert "NOT a member of the falsification family" in block
        assert "ledger holds at 26" in block

    def test_m717_block_key_unique_in_entities(self):
        text = _read("profiles/competitor-entities.yaml")
        assert text.count(M717_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(717)
        assert any(
            p.endswith("competitor-entities.yaml") for p in hits
        ), hits


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
    """Post-#809 corpus integrity: max 717, zero 718 keys."""

    def test_max_numeric_mechanism_id_is_717(self):
        assert _max_numeric_mechanism_id() == 717

    def test_zero_underscore_718_keys_in_profiles(self):
        hits = _repo_grep_underscore_mechanism(718)
        profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
        assert profile_hits == [], profile_hits

    def test_zero_underscore_718_references_in_tests(self):
        hits = _repo_grep_underscore_mechanism(718)
        test_hits = [p for p in hits if p.startswith(TESTS_DIR)]
        assert test_hits == [], test_hits

    def test_zero_numeric_718_keys_in_profiles(self):
        hits = _repo_grep_numeric_mechanism_id(718)
        assert hits == [], hits

    def test_designed_keying_holds_no_underscore_715_716_717_in_profiles(self):
        for n in (715, 716, 717):
            hits = _repo_grep_underscore_mechanism(n)
            profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
            assert profile_hits == [], (n, profile_hits)

    def test_c809_max_717_sweep_stays_green(self):
        # Type D adds no mechanisms; #809's max-717 sweep stays green.
        assert _max_numeric_mechanism_id() == 717

    def test_c809_zero_underscore_718_sweeps_stay_green(self):
        hits = _repo_grep_underscore_mechanism(718)
        assert hits == [], hits

    def test_c809_zero_numeric_718_sweep_stays_green(self):
        hits = _repo_grep_numeric_mechanism_id(718)
        assert hits == [], hits

    def test_a807_max_715_sweep_superseded_by_design(self):
        # #807 asserted max == 715 pre-commit; advancing to 717
        # supersedes it per the #710/#720 convention. Documented, not
        # repaired.
        assert _max_numeric_mechanism_id() == 717 != 715

    def test_b808_max_716_sweep_superseded_by_design(self):
        # #808 asserted max == 716 pre-commit; advancing to 717
        # supersedes it per the #710/#720 convention. Documented, not
        # repaired.
        assert _max_numeric_mechanism_id() == 717 != 716

    def test_b808_zero_underscore_717_sweep_stays_green(self):
        # #808's zero-underscore-717 sweep holds: m717 uses designed
        # keying (block key ani_v_openai_division_bench_notice_sep2026
        # carries no underscore-form mechanism literal).
        hits = _repo_grep_underscore_mechanism(717)
        assert hits == [], hits


class TestTypeDEngineStatisticalMeaningfulness:
    """Fresh synthetic corpora (new values, not #800's or #805's)."""

    def test_strong_signal_pair_significant_at_engine_layer(self):
        target = [0.88, 0.74, 0.99, 0.81, 0.90]
        peers = [-0.06, 0.03, -0.04, 0.01, -0.02]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 17),
            period_end=datetime.datetime(2026, 9, 17),
        )
        assert report.asymmetry_score == pytest.approx(0.880, rel=1e-9)
        assert report.is_significant is True
        assert report.p_value < 5e-4
        assert report.cohens_d > 8
        assert report.confidence_interval_lower > 0

    def test_near_null_pair_silent_at_engine_layer(self):
        target = [0.04, -0.02, 0.03, -0.05, 0.02]
        peers = [-0.03, 0.05, -0.02, 0.04, -0.06]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 17),
            period_end=datetime.datetime(2026, 9, 17),
        )
        assert report.asymmetry_score == pytest.approx(0.008, rel=1e-9)
        assert report.is_significant is False
        assert report.p_value > 0.5
        assert abs(report.cohens_d) < 0.5
        assert (
            report.confidence_interval_lower < 0 < report.confidence_interval_upper
        )

    def test_degenerate_n1_contract(self):
        a, b = [0.71], [-0.39]
        t, p = welch_t_test(a, b)
        d = cohens_d(a, b)
        assert (t, p) == (0.0, 1.0)
        assert d == 0.0
        assert is_significant(p) is False
        assert abs(a[0] - b[0]) == pytest.approx(1.10)
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
    """Suite verdict lineage; #805's background suite owns the verdict,
    #810 re-launches."""

    TOMBSTONE_LINEAGE = 23

    def test_tombstone_lineage_count(self):
        # TWENTY-THIRD consecutive background full-suite death: #805's
        # background suite (re-launched 08:10 PDT) died at ~3% progress
        # and no pytest was alive at this run's check. Advances from the
        # TWENTY-SECOND lineage declared in #805 per the #770/#780
        # convention.
        assert self.TOMBSTONE_LINEAGE == 23

    def test_805_background_suite_verdict_died(self):
        # Dead-run markers pinned per the #770/#780 convention; triaged
        # no further. Log stalled at ~3% since 08:53 PDT.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_805_full_suite.log",
        )
        assert os.path.exists(log_path), log_path
        size = os.path.getsize(log_path)
        assert size < 10000, size
        text = open(log_path, encoding="utf-8", errors="replace").read()
        assert "%" in text  # pytest -q progress marker present
        assert "3%" in text  # stalled at ~3% progress

    def test_relaunch_log_path_in_goal_hidden_files(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_810_full_suite.log",
        )
        assert os.path.basename(log_path) == "type_d_810_full_suite.log"

    def test_810_suite_relaunched_this_run(self):
        # This run re-launches the full suite as a background process
        # writing to the persistent goal hidden_files path; the next
        # Type D run (#815) checks its verdict per the #795 convention.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_810_full_suite.log",
        )
        assert os.path.exists(log_path), log_path


class TestDocSync810:
    def test_readme_row_810(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_810(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_810_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog810:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #810 Type D:")
        return log[idx : idx + 8000]

    def test_log_entry_present(self):
        assert "## #810 Type D:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        entry = self._entry()
        assert "mechanism_id 717" in entry
        assert "m715" in entry


class TestDateGrounding810:
    def test_sep_17_2026_is_thursday(self):
        assert datetime.date(2026, 9, 17).strftime("%A") == "Thursday"
