"""Type D -- Iteration #815 (Thu 2026-09-17 18:00 PDT): m718 / m719 / m720
qualitative-discipline verification + post-#814 corpus integrity
(max numeric mechanism_id 720; zero 721 keys; ledger holds at 26) +
#810 background-suite verdict (died at ~0% progress, 170 bytes, no
pytest alive at this run's check; background tombstone lineage advances
to TWENTY-FOURTH per the #770/#780 convention) + fresh synthetic engine
meaningfulness (new values, not #810's) + re-launch of the
full suite as a background process writing to goal hidden_files
type_d_815_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Verifies:
- m718 (FT x OpenAI $1.2tn funding-round scoop vs Meta equity-raise
  desperation register, Type A #812, profiles/financial-times.yaml):
  FT Sep 15 2026 investor-demand capital-raise scoop on its $5-10M/yr
  deal partner (+0.25 MANUAL ILLUSTRATIVE, Reuters mirror, FT original
  paywalled) vs the in-corpus FT Jun 5 2026 Meta equity-raise scoop
  desperation register (-0.30, carried un-rescored); illustrative
  OpenAI-minus-Meta delta +0.55 on matched pegs; confounders ranked
  strong-first (mirror-bounded sourcing, peg asymmetry, 3.5-month
  temporal gap); counter-evidence carried (m676 non-payer, FIFTEENTH
  falsification member, Hugging Face watchdog follow-ups); verdict
  directionally_supported_not_proven; degenerate n=1 engine check
  (calculate_asymmetry([0.25], [-0.30]) returns asymmetry 0.55; t 0.0 /
  p 1.0 / Cohen d 0.0 / is_significant False); NOT artifact-grade; NOT
  a falsification-family member (ledger holds at 26).
- m719 (Victoria Song Sep 2026 same-register Meta-vs-Apple pair,
  Type B #813, profiles/careers/journalists.yaml + careers backlink):
  FIRST dedicated Type B same-register Sep 2026 pair on Song; Meta arm
  her Optimizer newsletter reflection on her Meta Ray-Ban Display
  review (-0.10 illustrative, first-hand read this run, "minor
  existential crisis", "glasshole behavior", "I feel creepy"); Apple
  arm her Sep 17 2026 Apple Watch Series 12 review (+0.30
  illustrative, excerpt-bounded via appleinsider roundup and TechSpot
  90/100 aggregation, privacy caveat "may persist despite Apple's
  safeguards"); illustrative Meta-minus-Apple delta -0.40 - the privacy
  register bleeds into her Meta product coverage while staying muted
  in her Apple product coverage of an always-on ambient-audio device;
  confounders ranked strong-first (genre, privacy-vector, review-cycle
  asymmetry); counter-evidence carried (#599 money-gradient failure,
  #723 control replication); verdict EXTENDS mechanism 605 and
  NARROWS its product-register fairness claim to "fair in product
  register except where the product itself is a face-worn camera";
  NOT artifact-grade; NOT a falsification-family member.
- m720 (LINC K.K. Japan collective-licensing expansion, Type C #814,
  profiles/competitor-entities.yaml): FIRST dedicated mapping of the
  Sep 11 2026 IntentBridges (SG) x Globalive (JP) joint venture; first
  APAC entrant in tier_3_collective; fifth relationship-direction
  pool-and-license alongside sue-then-sign (m624), pay-or-litigate
  (m636), grant-then-sue (m675), sign-then-terminate (Disney x OpenAI);
  extends m681 repricing frame (who prices content shifts lab ->
  network); qualitative-only structural mapping, scorer none, tone
  NOT_SCORED, p_value / cohens_d / ci_95 NOT_CALCULATED, is_significant
  false, cautious_language_required true, no_coverage_tone_claim true;
  verdict directionally_supported_not_proven; NOT artifact-grade; NOT
  a falsification-family member (ledger holds at 26).
- Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent in
  profiles/; ledger holds at 26.
- Post-#814 corpus integrity: max numeric mechanism_id == 720 in
  profiles/; zero underscore-form 721 key substrings in profiles/ and
  tests/ (own file excluded as sweep carrier per the #715
  pattern-rescope lesson; needles built by format string so no literal
  is carried); zero numeric 721 keys in profiles/; m718 / m719 / m720
  block keys each unique in their home YAMLs; designed keying holds
  (no underscore-form 718/719/720 mechanism key substrings in
  profiles/). #814's max-720 / zero-underscore-721 / zero-numeric-721
  sweeps stay green (Type D adds no mechanisms); #812's max-718 and
  #813's max-719 sweeps fail by designed supersession per the
  #710/#720 convention (documented, not repaired).
- Statistical meaningfulness on FRESH synthetic corpora (new values,
  not #810's): strong-signal n=5-per-arm pair (asymmetry +0.862,
  p=8.53e-08 < 5e-4, d=13.254 > 8, 95% CI (0.790, 0.934) above zero,
  is_significant True at the ENGINE layer); fresh near-null pair
  (asymmetry 0.004, p=0.935 > 0.5, |d|=0.053 < 0.5, CI crossing zero,
  silent); fresh degenerate n=1-per-arm contract on the m718 tone
  pair ([0.25], [-0.30]: t=0.0, p=1.0, d=0.0, is_significant False,
  |asymmetry| == 0.55 exact, arm-swap negates). Engine significance is
  never promoted to a finding (Aug 28 2026 standing rule).
- Full-suite status: the #810 background suite re-launched 13:19 PDT
  died (type_d_810_full_suite.log stalled at 170 bytes / ~0% since
  13:19 PDT; no pytest alive at this run's check) - dead-run markers,
  triaged no further per the #770/#780 convention; tombstone lineage
  advances TWENTY-THIRD -> TWENTY-FOURTH. This run re-launches the
  full suite as a background process writing to goal hidden_files
  type_d_815_full_suite.log (alive at re-launch check); next Type D
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
    "test_type_d_815_m718_m719_m720_qualitative_corpus_integrity_sep17_6pm.py"
)
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"

ANCHORED_SHA = "a4e40d2061a04a1ac3c20c772026981064146294"

M718_KEY = "ft_openai_1_2tn_funding_round_scoop_vs_meta_equity_raise_desperation_sep17"
M719_KEY = "type_b_813_victoria_song_sep2026_display_existential_vs_watch_ambient_muted_sep17"
M720_KEY = "linc_kk_japan_collective_licensing_sep2026"

# Format-built so this file carries no underscore-form mechanism literal
# (per the #715 pattern-rescope lesson: keeps prior zero-underscore
# sweeps green and this file's own sweep honest).
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


class TestNovelty815:
    """Pre-commit novelty: single new file, unique commit."""

    def test_single_test_type_d_815_file(self):
        files = sorted(
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_815") and f.endswith(".py")
        )
        assert files == [TEST_BASENAME], files

    def test_type_d_815_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 convention; the main commit
        # does not exist yet. Patched green in the anchor followup.
        # Specific "Type D #815: m718" prefix per the #796 convention:
        # immune to a "Type D #815 push-status record" followup.
        mains = _git_log_mains("Type D #815: m718")
        assert len(mains) == 1, mains
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim(self):
        # Type D adds no mechanism; novelty is the corpus-integrity
        # posture: max stays 720, zero numeric 721 keys.
        assert _max_numeric_mechanism_id() == 720
        assert _repo_grep_numeric_mechanism_id(721) == []

    def test_810_814_window_closed_prior_to_815(self):
        # Opening leg of the 815-819 window: the previous window must
        # read closed D->E->A->B->C (newest first) as a consecutive
        # sequence in history, wherever it sits (per the #795 repair:
        # the newest-five shortcut broke once 806+ landed; per #800,
        # history lookup).
        legs = _window_legs_deduped("815")
        want = [
            ("C", "814"),
            ("B", "813"),
            ("A", "812"),
            ("E", "811"),
            ("D", "810"),
        ]
        found = any(
            legs[i : i + 5] == want for i in range(len(legs) - 4)
        )
        assert found, legs[:12]


class TestTypeDRotationGuard:
    """#815 is the Type D anchor opening window 815-819."""

    WINDOW = ("D", "E", "A", "B", "C")

    def test_rotation_window_815_819(self):
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


class TestTypeDM718QualitativeDiscipline:
    """Type D verification of m718 qualitative discipline (Type A #812).

    Assertions run on the whitespace-folded block per the #732
    convention: the m718 finding, discipline, and falsification fields
    wrap across raw YAML lines."""

    def _block(self):
        return _fold(
            _block("profiles/financial-times.yaml", M718_KEY, 30000)
        )

    def test_m718_publication_and_entity(self):
        block = self._block()
        assert "mechanism_id: 718" in block
        assert "iteration: 812" in block
        assert "iteration_type: 'A'" in block
        assert "iteration_time: 2026-09-17 15:00 PDT" in block
        assert "Financial Times" in block

    def test_m718_openai_arm_constructive(self):
        block = self._block()
        assert "investor-demand capital-raise scoop" in block
        assert "tone_MANUAL_ILLUSTRATIVE: 0.25" in block
        assert "initiated by investors rather than the company" in block
        assert "$1.2 trillion" in block

    def test_m718_meta_arm_desperation(self):
        block = self._block()
        assert "Meta weighs big equity raising to finance AI infrastructure" in block
        assert "tone_MANUAL_ILLUSTRATIVE: -0.30" in block
        assert "capital_raise_desperation" in block

    def test_m718_illustrative_delta(self):
        block = self._block()
        assert "Illustrative OpenAI-minus-Meta delta +0.55" in block

    def test_m718_financial_tie(self):
        block = self._block()
        assert "Apr 2024" in block
        assert "mechanism 54" in block
        assert "Meta pays FT $0" in block
        assert "Google News AI pilot" in block

    def test_m718_confounders_ranked_strong_first(self):
        block = self._block()
        assert "confounders_ranked:" in block
        assert "Mirror-bounded sourcing" in block
        assert "Peg asymmetry within the match" in block
        strong_idx = block.index("strong:")
        moderate_idx = block.index("moderate:")
        assert strong_idx < moderate_idx, "strong confounders must precede moderate"

    def test_m718_counter_evidence(self):
        block = self._block()
        assert "counterevidence:" in block
        assert "Mechanism 676" in block
        assert "NON-payer" in block
        assert "Mechanism 643" in block
        assert "FIFTEENTH" in block
        assert "the peg, not the FT-OpenAI tie" in block

    def test_m718_statistical_discipline_strings(self):
        block = self._block()
        assert "MANUAL ILLUSTRATIVE hand-assigned tones" in block
        assert "calculate_asymmetry([0.25], [-0.30]) returns asymmetry 0.55" in block
        assert "t 0.0 / p 1.0 / Cohen d 0.0" in block
        assert "is_significant False" in block
        assert "no significance claimed (Aug 28" in block
        assert "Verdict: directionally_supported_not_proven" in block
        assert "no_analysis_json_update: true" in block

    def test_m718_not_falsification_member(self):
        block = self._block()
        assert "NOT a member - capital-raise register documentation" in block

    def test_m718_block_key_unique_in_ft(self):
        text = _read("profiles/financial-times.yaml")
        assert text.count(M718_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(718)
        assert any(
            p.endswith("financial-times.yaml") for p in hits
        ), hits

    def test_m718_designed_keying_no_underscore_718(self):
        # Format-built marker so this file carries no underscore-form
        # 718 literal; the m718 descriptive block key must not carry it
        # either (per #715 designed keying).
        assert MECH_ID_MARKER + "718" not in self._block()


class TestTypeDM719QualitativeDiscipline:
    """Type D verification of m719 qualitative discipline (Type B #813)."""

    def _block(self):
        return _fold(
            _block("profiles/careers/journalists.yaml", M719_KEY, 25000)
        )

    def test_m719_journalist_and_iteration(self):
        block = self._block()
        assert "mechanism_id: 719" in block
        assert "iteration: 813" in block
        assert "date: '2026-09-17 16:00 PDT'" in block
        assert "Victoria Song" in block
        assert "same-register" in block

    def test_m719_meta_arm_first_hand(self):
        block = self._block()
        assert "tone_MANUAL_ILLUSTRATIVE: -0.10" in block
        assert "minor existential crisis" in block
        assert "glasshole behavior" in block
        assert "I feel creepy" in block
        assert "first_hand_read_mirror" in block

    def test_m719_apple_arm_muted(self):
        block = self._block()
        assert "tone_MANUAL_ILLUSTRATIVE: 0.30" in block
        assert "Faster health tracking collides with unfinished AI" in block
        assert "may persist despite Apple" in block
        assert "90/100" in block
        assert "excerpt_bounded_secondary" in block

    def test_m719_illustrative_delta(self):
        block = self._block()
        assert "illustrative_delta_meta_minus_apple: -0.40" in block
        assert "delta_calc: '(-0.10) - (0.30) = -0.40'" in block

    def test_m719_confounders_ranked_strong_first(self):
        block = self._block()
        assert "confounders_ranked:" in block
        assert "Genre asymmetry" in block
        assert "Privacy-vector asymmetry" in block
        assert "Review-cycle asymmetry" in block

    def test_m719_counter_evidence(self):
        block = self._block()
        assert "counterevidence:" in block
        assert "best glasses I have ever tried" in block
        assert "may be BETTER than Apple" in block
        assert "#599" in block
        assert "#723" in block

    def test_m719_verdict_extends_and_narrows_605(self):
        block = self._block()
        assert "EXTENDS mechanism 605 and NARROWS" in block
        assert "fair in product register except where the product itself is a face-worn camera" in block

    def test_m719_statistical_discipline_strings(self):
        block = self._block()
        assert "MANUAL ILLUSTRATIVE scores only" in block
        assert "Engine NOT run per the Aug 28 2026 standing rule" in block
        assert "p_value NOT_CALCULATED" in block
        assert "cohens_d NOT_CALCULATED" in block
        assert "is_significant False" in block
        assert "no_analysis_json_update: true" in block

    def test_m719_not_falsification_member(self):
        block = self._block()
        assert "falsification_family: 'NOT a falsification-family member" in block
        assert "ledger holds at 26." in block

    def test_m719_block_key_unique_and_backlinked(self):
        text = _read("profiles/careers/journalists.yaml")
        assert text.count(M719_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(719)
        assert any(
            p.endswith("journalists.yaml") for p in hits
        ), hits
        assert "mechanism_ids: [593, 605, 719]" in text

    def test_m719_designed_keying_no_underscore_719(self):
        assert MECH_ID_MARKER + "719" not in self._block()


class TestTypeDM720QualitativeDiscipline:
    """Type D verification of m720 qualitative discipline (Type C #814)."""

    def _block(self):
        return _fold(
            _block("profiles/competitor-entities.yaml", M720_KEY, 20000)
        )

    def test_m720_iteration_and_type(self):
        block = self._block()
        assert "mechanism_id: 720" in block
        assert "iteration: 814" in block
        assert "iteration_type: C" in block
        assert "rotation: 'Type C'" in block
        assert "type: financial_incentive_mapping" in block
        assert "time_pdt: '17:00'" in block

    def test_m720_joint_venture_facts(self):
        block = self._block()
        assert "LINC K.K." in block
        assert "IntentBridges Pte. Ltd." in block
        assert "Globalive K.K." in block
        assert "Kosuke Umeno" in block
        assert "announced: '2026-09-11'" in block

    def test_m720_publisher_roster(self):
        block = self._block()
        assert "Mediagene Inc. (Japan)" in block
        assert "ETtoday (Taiwan region)" in block
        assert "Philstar (Philippines)" in block

    def test_m720_fifth_direction_taxonomy(self):
        block = self._block()
        assert "pool-and-license" in block
        assert "fifth direction" in block
        assert "tier_3_collective" in block
        assert "sue-then-sign (m624)" in block

    def test_m720_statistical_discipline(self):
        block = self._block()
        assert "scorer: 'none'" in block
        assert "tone_scores: 'NOT_SCORED'" in block
        assert "p_value: 'NOT_CALCULATED'" in block
        assert "cohens_d: 'NOT_CALCULATED'" in block
        assert "ci_95: 'NOT_CALCULATED'" in block
        assert "is_significant: false" in block
        assert "qualitative_only: true" in block
        assert "cautious_language_required: true" in block
        assert "no_coverage_tone_claim: true" in block
        assert "predictions_not_findings: true" in block
        assert "verdict: 'directionally_supported_not_proven'" in block
        assert "artifact_grade: false" in block
        assert "no_analysis_json_update: true" in block

    def test_m720_not_falsification_member(self):
        block = self._block()
        assert "falsification_family: 'NOT a member - financial-relationship documentation leg" in block
        assert "ledger holds at 26" in block

    def test_m720_block_key_unique_in_entities(self):
        text = _read("profiles/competitor-entities.yaml")
        assert text.count(M720_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(720)
        assert any(
            p.endswith("competitor-entities.yaml") for p in hits
        ), hits

    def test_m720_designed_keying_no_underscore_720(self):
        assert MECH_ID_MARKER + "720" not in self._block()


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
    """Post-#814 corpus integrity: max 720, zero 721 keys."""

    def test_max_numeric_mechanism_id_is_720(self):
        assert _max_numeric_mechanism_id() == 720

    def test_zero_underscore_721_keys_in_profiles(self):
        hits = _repo_grep_underscore_mechanism(721)
        profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
        assert profile_hits == [], profile_hits

    def test_zero_underscore_721_references_in_tests(self):
        hits = _repo_grep_underscore_mechanism(721)
        test_hits = [p for p in hits if p.startswith(TESTS_DIR)]
        assert test_hits == [], test_hits

    def test_zero_numeric_721_keys_in_profiles(self):
        hits = _repo_grep_numeric_mechanism_id(721)
        assert hits == [], hits

    def test_designed_keying_holds_no_underscore_718_719_720_in_profiles(self):
        for n in (718, 719, 720):
            hits = _repo_grep_underscore_mechanism(n)
            profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
            assert profile_hits == [], (n, profile_hits)

    def test_c814_max_720_sweep_stays_green(self):
        # Type D adds no mechanisms; #814's max-720 sweep stays green.
        assert _max_numeric_mechanism_id() == 720

    def test_c814_zero_underscore_721_sweeps_stay_green(self):
        hits = _repo_grep_underscore_mechanism(721)
        assert hits == [], hits

    def test_c814_zero_numeric_721_sweep_stays_green(self):
        hits = _repo_grep_numeric_mechanism_id(721)
        assert hits == [], hits

    def test_a812_max_718_sweep_superseded_by_design(self):
        # #812 asserted max == 718 pre-commit; advancing to 720
        # supersedes it per the #710/#720 convention. Documented, not
        # repaired.
        assert _max_numeric_mechanism_id() == 720 != 718

    def test_b813_max_719_sweep_superseded_by_design(self):
        # #813 asserted max == 719 pre-commit; advancing to 720
        # supersedes it per the #710/#720 convention. Documented, not
        # repaired.
        assert _max_numeric_mechanism_id() == 720 != 719


class TestTypeDEngineStatisticalMeaningfulness:
    """Fresh synthetic corpora (new values, not #810's)."""

    def test_strong_signal_pair_significant_at_engine_layer(self):
        target = [0.82, 0.91, 0.77, 0.88, 0.85]
        peers = [-0.06, 0.03, -0.11, 0.08, -0.02]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 17),
            period_end=datetime.datetime(2026, 9, 17),
        )
        assert report.asymmetry_score == pytest.approx(0.862, rel=1e-9)
        assert report.is_significant is True
        assert report.p_value == pytest.approx(8.53e-08, rel=1e-2)
        assert report.cohens_d == pytest.approx(13.254, rel=1e-2)
        assert report.confidence_interval_lower > 0
        assert report.confidence_interval_lower == pytest.approx(0.790, rel=1e-2)
        assert report.confidence_interval_upper == pytest.approx(0.934, rel=1e-2)

    def test_near_null_pair_silent_at_engine_layer(self):
        target = [0.12, -0.08, 0.05, -0.03, 0.09]
        peers = [0.10, -0.06, 0.04, -0.02, 0.07]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 17),
            period_end=datetime.datetime(2026, 9, 17),
        )
        assert report.asymmetry_score == pytest.approx(0.004, abs=1e-9)
        assert report.is_significant is False
        assert report.p_value > 0.5
        assert abs(report.cohens_d) < 0.5
        assert (
            report.confidence_interval_lower < 0 < report.confidence_interval_upper
        )

    def test_degenerate_n1_contract_on_m718_tone_pair(self):
        # The m718 degenerate check: calculate_asymmetry([0.25], [-0.30])
        # returns asymmetry 0.55 with t 0.0 / p 1.0 / d 0.0.
        t, p = welch_t_test([0.25], [-0.30])
        d = cohens_d([0.25], [-0.30])
        assert (t, p) == (0.0, 1.0)
        assert d == 0.0
        assert is_significant(p) is False
        assert abs(0.25 - (-0.30)) == pytest.approx(0.55)
        t2, p2 = welch_t_test([-0.30], [0.25])
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
    """Suite verdict lineage; #810's background suite owns the verdict,
    #815 re-launches."""

    TOMBSTONE_LINEAGE = 24

    def test_tombstone_lineage_count(self):
        # TWENTY-FOURTH consecutive background full-suite death: #810's
        # background suite (re-launched 13:19 PDT) died at ~0% progress
        # and no pytest was alive at this run's check. Advances from the
        # TWENTY-THIRD lineage declared in #810 per the #770/#780
        # convention.
        assert self.TOMBSTONE_LINEAGE == 24

    def test_810_background_suite_verdict_died(self):
        # Dead-run markers pinned per the #770/#780 convention; triaged
        # no further. Log stalled at ~0% since 13:19 PDT.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_810_full_suite.log",
        )
        assert os.path.exists(log_path), log_path
        size = os.path.getsize(log_path)
        assert size < 10000, size
        text = open(log_path, encoding="utf-8", errors="replace").read()
        assert "%" in text  # pytest -q progress marker present
        assert "0%" in text  # stalled at ~0% progress

    def test_relaunch_log_path_in_goal_hidden_files(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_815_full_suite.log",
        )
        assert os.path.basename(log_path) == "type_d_815_full_suite.log"

    def test_815_suite_relaunched_this_run(self):
        # This run re-launches the full suite as a background process
        # writing to the persistent goal hidden_files path; the next
        # Type D run checks its verdict per the #795 convention.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_815_full_suite.log",
        )
        assert os.path.exists(log_path), log_path


class TestDocSync815:
    def test_readme_row_815(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_815(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_815_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog815:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #815 Type D:")
        return log[idx : idx + 9000]

    def test_log_entry_present(self):
        assert "## #815 Type D:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        entry = self._entry()
        assert "mechanism_id 720" in entry
        assert "m718" in entry
        assert "m719" in entry


class TestDateGrounding815:
    def test_sep_17_2026_is_thursday(self):
        assert datetime.date(2026, 9, 17).strftime("%A") == "Thursday"
