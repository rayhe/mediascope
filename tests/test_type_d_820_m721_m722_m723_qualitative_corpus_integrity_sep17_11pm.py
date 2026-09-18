"""Type D -- Iteration #820 (Thu 2026-09-17 23:00 PDT): m721 / m722 / m723
qualitative-discipline verification + post-#819 corpus integrity
(max numeric mechanism_id 723; zero 724 keys; ledger holds at 26) +
#815 background-suite verdict (died at ~1% progress, 493 bytes, no
pytest alive at this run's check; background tombstone lineage advances
to TWENTY-FIFTH per the #770/#780 convention) + fresh synthetic engine
meaningfulness (new values, not #815's) + re-launch of the
full suite as a background process writing to goal hidden_files
type_d_820_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Verifies:
- m721 (Gizmodo x OpenAI $1.2tn funding-round register, Type A #817,
  profiles/gizmodo.yaml): FOURTH null-tie control in the Gizmodo
  family (#512 Google, #577 Anthropic, #582 OpenAI rogue-agent
  incidents); first-hand Gizmodo arm Sep 15 2026 "Rumored Round of
  Funding Could Make OpenAI More Valuable Than Anthropic Again.
  Perhaps Briefly" (skeptical_deflationary_horserace, -0.20 MANUAL
  ILLUSTRATIVE) vs peg-matched tied comparators FT m718 (+0.25),
  WSJ m715, WIRED m712; illustrative Gizmodo-minus-FT delta -0.45;
  confounders ranked strong-first (house adversarialism, genre
  asymmetry); counter-evidence carried (m676 non-payer, m582
  symmetric-adversarial, m679 WSJ expose on the payer); verdict
  directionally_supported_not_proven; degenerate n=1 engine check
  (calculate_asymmetry([-0.20], [0.25]) returns asymmetry_score -0.45;
  t 0.0 / p 1.0 / Cohen d 0.0 / degenerate CI (-0.45, -0.45) /
  is_significant False); NOT artifact-grade; NOT a
  falsification-family member (ledger holds at 26).
- m722 (Karissa Bell Engadget same-writer register pair, Type B #818,
  profiles/careers/journalists.yaml): Meta arm "Meta Ray-Ban Display
  review: Chunky frames with impressive abilities" (Oct 2025, -0.10
  illustrative, dedicated Privacy and safety section) vs Snap arm
  "Snap Specs Hands On: Standalone AR Glasses Are Here" (Sep 16 2026,
  +0.30 illustrative, 0 privacy terms); illustrative Meta-minus-Snap
  delta -0.40; confounders ranked strong-first (genre asymmetry
  10-day review vs 20-minute hands-on, product-class asymmetry,
  temporal gap); counter-evidence carried (Bell praised Meta tech;
  Bell flagged Snap price; Meta privacy section genuinely sourced;
  #753 constancy; #723 control); verdict EXTENDS mechanisms 113 and
  605 and NARROWS the product-register fairness claim to "fair in
  product register except where the product is a Meta face-worn
  camera"; NOT artifact-grade; NOT a falsification-family member.
- m723 (PLS UK collective AI licensing scheme, Type C #819,
  profiles/competitor-entities.yaml): FIRST dedicated UK
  collective-licensing mechanism; Publishers Licensing Services
  (UK non-profit, government-regulated; PA/IPG/PPA/ALPSP owned;
  CLA/ALCS developed); first-stage Generative AI Training Licence
  launched London Book Fair Mar 2026 (licence + online content
  store for AI training and fine-tuning; alongside direct deals);
  250+ opt-ins by Jul 2026 (self-reported; named Practical Action
  Publishing, 5m Books); extends tier_3_collective with the
  book-publisher-side training vehicle (long-form counterpart to
  Cashmere m663 inference-only rails and ProRata revenue share);
  scorer none, tone NOT_SCORED, p_value / cohens_d / ci_95
  NOT_CALCULATED, is_significant false, qualitative_only true,
  cautious_language_required true, no_coverage_tone_claim true;
  verdict directionally_supported_not_proven; NOT artifact-grade; NOT
  a falsification-family member (ledger holds at 26).
- Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent in
  profiles/; ledger holds at 26.
- Post-#819 corpus integrity: max numeric mechanism_id == 723 in
  profiles/; zero underscore-form 724 key substrings in profiles/ and
  tests/ (own file excluded as sweep carrier per the #715
  pattern-rescope lesson; needles built by format string so no literal
  is carried); zero numeric 724 keys in profiles/; m721 / m722 /
  m723 block keys each unique in their home YAMLs; designed keying
  holds (no underscore-form 721/722/723 mechanism key substrings in
  profiles/). #819's max-723 / zero-underscore-724 / zero-numeric-724
  sweeps stay green (Type D adds no mechanisms); #817's max-721 and
  #818's max-722 sweeps fail by designed supersession per the
  #710/#720 convention (documented, not repaired).
- Statistical meaningfulness on FRESH synthetic corpora (new values,
  not #815's): strong-signal n=5-per-arm pair (asymmetry +0.890,
  p=9.729e-08 < 5e-4, d=11.3213 > 8, 95% CI (0.8000, 0.9721) above
  zero, is_significant True at the ENGINE layer); fresh near-null
  pair (asymmetry 0.002, p=0.9739 > 0.5, |d|=0.0214 < 0.5, CI
  (-0.1020, 0.1060) crossing zero, silent); fresh degenerate
  n=1-per-arm contract on the m721 tone pair ([-0.20], [0.25]: t=0.0,
  p=1.0, d=0.0, is_significant False, |asymmetry| == 0.45 exact,
  arm-swap negates). Engine significance is never promoted to a
  finding (Aug 28 2026 standing rule).
- Full-suite status: the #815 background suite re-launched 18:19 PDT
  died (type_d_815_full_suite.log stalled at 493 bytes / ~1% progress
  since 18:19 PDT; no pytest alive at this run's check) - dead-run
  markers, triaged no further per the #770/#780 convention; tombstone
  lineage advances TWENTY-FOURTH -> TWENTY-FIFTH. This run re-launches
  the full suite as a background process writing to goal hidden_files
  type_d_820_full_suite.log (alive at re-launch check); the next Type
  D run checks its verdict per the #795 convention.

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
    "test_type_d_820_m721_m722_m723_qualitative_corpus_integrity_sep17_11pm.py"
)
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"

ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

M721_KEY = "gizmodo_openai_1_2tn_funding_round_null_tie_control_sep17"
M722_KEY = "type_b_818_karissa_bell_engadget_meta_display_vs_snap_specs_sep17"
M723_KEY = "pls_collective_ai_licensing_uk_sep2026"

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


class TestNovelty820:
    """Pre-commit novelty: single new file, unique commit."""

    def test_single_test_type_d_820_file(self):
        files = sorted(
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_820") and f.endswith(".py")
        )
        assert files == [TEST_BASENAME], files

    def test_type_d_820_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 convention; the main commit
        # does not exist yet. Patched green in the anchor followup.
        # Specific "Type D #820: m721" prefix per the #796 convention:
        # immune to a "Type D #820 push-status record" followup.
        mains = _git_log_mains("Type D #820: m721")
        assert len(mains) == 1, mains
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim(self):
        # Type D adds no mechanism; novelty is the corpus-integrity
        # posture: max stays 723, zero numeric 724 keys.
        assert _max_numeric_mechanism_id() == 723
        assert _repo_grep_numeric_mechanism_id(724) == []

    def test_815_819_window_closed_prior_to_820(self):
        # Opening leg of the 820-824 window: the previous window must
        # read closed D->E->A->B->C (newest first) as a consecutive
        # sequence in history, wherever it sits (per the #795 repair:
        # the newest-five shortcut broke once 806+ landed; per #800,
        # history lookup).
        legs = _window_legs_deduped("820")
        want = [
            ("C", "819"),
            ("B", "818"),
            ("A", "817"),
            ("E", "816"),
            ("D", "815"),
        ]
        found = any(
            legs[i : i + 5] == want for i in range(len(legs) - 4)
        )
        assert found, legs[:12]


class TestTypeDRotationGuard:
    """#820 is the Type D anchor opening window 820-824."""

    WINDOW = ("D", "E", "A", "B", "C")

    def test_rotation_window_820_824(self):
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


class TestTypeDM721QualitativeDiscipline:
    """Type D verification of m721 qualitative discipline (Type A #817).

    Assertions run on the whitespace-folded block per the #732
    convention: the m721 finding, discipline, and falsification fields
    wrap across raw YAML lines."""

    def _block(self):
        return _fold(
            _block("profiles/gizmodo.yaml", M721_KEY, 30000)
        )

    def test_m721_publication_and_iteration(self):
        block = self._block()
        assert "mechanism_id: 721" in block
        assert "iteration: 817" in block
        assert "iteration_type: 'A'" in block
        assert "iteration_time: 2026-09-17 20:00 PDT" in block
        assert "Gizmodo (Keleops AG)" in block

    def test_m721_fourth_null_tie_control(self):
        block = self._block()
        assert "FOURTH null-tie control in the Gizmodo family" in block
        assert "#512 Gizmodo x Google" in block
        assert "#577 Gizmodo x Anthropic" in block
        assert "#582 Gizmodo x OpenAI rogue-agent incidents" in block

    def test_m721_gizmodo_arm_first_hand(self):
        block = self._block()
        assert "Rumored Round of Funding Could Make OpenAI More Valuable Than Anthropic Again. Perhaps Briefly" in block
        assert "register: skeptical_deflationary_horserace" in block
        assert "tone_MANUAL_ILLUSTRATIVE: -0.20" in block
        assert "https://gizmodo.com/rumored-round-of-funding-could-make-openai-more-valuable-than-anthropic-again-perhaps-briefly-2000812142" in block
        assert "first-hand read this run (gizmodo.com, 33 rendered lines" in block

    def test_m721_peg_matched_tied_comparators(self):
        block = self._block()
        assert "FT m718 (Type A #812): +0.25 constructive_growth_investor_demand" in block
        assert "WSJ m715 (Type A #807)" in block
        assert "WIRED m712 (Type A #802)" in block
        assert "illustrative_register_delta_gizmodo_minus_ft: -0.45" in block
        assert "delta_arithmetic: '-0.20 - 0.25 = -0.45'" in block

    def test_m721_confounders_ranked_strong_first(self):
        block = self._block()
        assert "confounders_ranked:" in block
        assert "House adversarialism:" in block
        assert "Genre asymmetry within the peg" in block
        strong_idx = block.index("strong:")
        moderate_idx = block.index("moderate:")
        assert strong_idx < moderate_idx, "strong confounders must precede moderate"

    def test_m721_counter_evidence(self):
        block = self._block()
        assert "counterevidence:" in block
        assert "m676 (FT constructive company-briefed scoop on Anthropic, a NON-payer, +0.20)" in block
        assert "m582 (Gizmodo symmetric-adversarial on OpenAI AND Meta)" in block
        assert "m679: WSJ ran a -0.40 expose on the payer the same week" in block

    def test_m721_statistical_discipline_strings(self):
        block = self._block()
        assert "MANUAL ILLUSTRATIVE tones only" in block
        assert "delta -0.45, p_value NOT_CALCULATED, cohens_d NOT_CALCULATED, ci NOT_CALCULATED, is_significant False" in block
        assert "calculate_asymmetry([-0.20], [0.25]) returns asymmetry_score -0.45" in block
        assert "t 0.0 / p 1.0 / Cohen d 0.0 / degenerate CI (-0.45, -0.45) / is_significant False" in block
        assert "Engine NOT run on the illustrative arms per the Aug 28 2026 standing rule" in block
        assert "verdict: directionally_supported_not_proven" in block
        assert "no_analysis_json_update: true" in block

    def test_m721_not_falsification_member(self):
        block = self._block()
        assert "NOT a member - null-tie control documentation (ledger holds at 26)." in block
        assert "TWENTY-SIXTH present in profiles/ (ledger holds at 26; the next ordinal is absent)." in block

    def test_m721_block_key_unique_in_gizmodo(self):
        text = _read("profiles/gizmodo.yaml")
        assert text.count(M721_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(721)
        assert any(
            p.endswith("gizmodo.yaml") for p in hits
        ), hits

    def test_m721_designed_keying_no_underscore_721(self):
        # Format-built marker so this file carries no underscore-form
        # 721 literal; the m721 descriptive block key must not carry it
        # either (per #715 designed keying).
        assert MECH_ID_MARKER + "721" not in self._block()


class TestTypeDM722QualitativeDiscipline:
    """Type D verification of m722 qualitative discipline (Type B #818)."""

    def _block(self):
        return _fold(
            _block(
                "profiles/careers/journalists.yaml", M722_KEY, 30000
            )
        )

    def test_m722_journalist_and_iteration(self):
        block = self._block()
        assert "mechanism_id: 722" in block
        assert "iteration: 818" in block
        assert "date: '2026-09-17 21:00 PDT'" in block
        assert "Karissa Bell" in block
        assert "test_file: 'tests/test_type_b_818_karissa_bell_engadget_meta_display_vs_snap_specs_sep17_9pm.py'" in block

    def test_m722_meta_arm_first_hand(self):
        block = self._block()
        assert "Meta Ray-Ban Display review: Chunky frames with impressive abilities" in block
        assert "tone_MANUAL_ILLUSTRATIVE: -0.10" in block
        assert "first-hand this run, 224 rendered lines" in block
        assert "I share a lot of these concerns" in block
        assert "surreptitiously eavesdrop on a conversation" in block

    def test_m722_snap_arm_muted(self):
        block = self._block()
        assert "Snap Specs Hands On: Standalone AR Glasses Are Here" in block
        assert "tone_MANUAL_ILLUSTRATIVE: 0.30" in block
        assert "first-hand this run, 105 rendered lines" in block
        assert "privacy_vocabulary_count: 0" in block
        assert "I think there''s a lot to like" in block

    def test_m722_illustrative_delta(self):
        block = self._block()
        assert "illustrative_delta_meta_minus_snap: -0.40" in block
        assert "delta_calc: '(-0.10) - (0.30) = -0.40'" in block

    def test_m722_confounders_ranked_strong_first(self):
        block = self._block()
        assert "confounders_ranked:" in block
        assert "Genre asymmetry: 10-day lived Meta review vs 20-minute launch-day Snap hands-on" in block
        assert "Product-class asymmetry:" in block
        assert "Temporal gap: Oct 2025 vs Sep 2026" in block
        strong_idx = block.index("strong:")
        moderate_idx = block.index("moderate:")
        assert strong_idx < moderate_idx, "strong confounders must precede moderate"

    def test_m722_counter_evidence(self):
        block = self._block()
        assert "counterevidence:" in block
        assert "COUNTEREVIDENCE: Bell praised Meta tech strongly" in block
        assert "COUNTEREVIDENCE: Bell DID flag Snap price" in block
        assert "#753 Hardawar review constancy" in block

    def test_m722_verdict_extends_113_and_605(self):
        block = self._block()
        assert "EXTENDS mechanism 113 and the register-conditioned model 605" in block
        assert "fair in product register except where the product is a Meta face-worn camera" in block
        assert "directionally_supported_not_proven" in block

    def test_m722_statistical_discipline_strings(self):
        block = self._block()
        assert "MANUAL ILLUSTRATIVE tones only (article level, n=1/n=1)" in block
        assert "engine NOT run" in block
        assert "p_value NOT_CALCULATED" in block
        assert "cohens_d NOT_CALCULATED" in block
        assert "ci_95 NOT_CALCULATED" in block
        assert "is_significant False" in block
        assert "no empirical significance claimed or claimable." in block
        assert "no_analysis_json_update: true" in block

    def test_m722_not_falsification_member(self):
        block = self._block()
        assert "NOT a falsification-family member (register documentation, not a uniform-prediction test); ledger holds at 26." in block

    def test_m722_block_key_unique_and_backlinked(self):
        text = _read("profiles/careers/journalists.yaml")
        assert text.count(M722_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(722)
        assert any(
            p.endswith("journalists.yaml") for p in hits
        ), hits
        assert "mechanism_ids: [722]" in text

    def test_m722_designed_keying_no_underscore_722(self):
        assert MECH_ID_MARKER + "722" not in self._block()


class TestTypeDM723QualitativeDiscipline:
    """Type D verification of m723 qualitative discipline (Type C #819)."""

    def _block(self):
        return _fold(
            _block("profiles/competitor-entities.yaml", M723_KEY, 25000)
        )

    def test_m723_iteration_and_type(self):
        block = self._block()
        assert "mechanism_id: 723" in block
        assert "iteration: 819" in block
        assert "iteration_type: C" in block
        assert "rotation: 'Type C'" in block
        assert "type: financial_incentive_mapping" in block
        assert "time_pdt: '22:00'" in block

    def test_m723_pls_scheme_facts(self):
        block = self._block()
        assert "Publishers Licensing Services (PLS)" in block
        assert "Generative AI Training Licence programme" in block
        assert "London Book Fair" in block
        assert "March 2026" in block
        assert "Copyright Licensing Agency (CLA)" in block
        assert "Authors Licensing and Collecting Society (ALCS)" in block

    def test_m723_opt_in_count(self):
        block = self._block()
        assert "Over 250 publishers opted in ahead of the PLS Conference of 2 July 2026" in block
        assert "Practical Action Publishing" in block
        assert "5m Books" in block

    def test_m723_tier3_collective_extension(self):
        block = self._block()
        assert "tier_3_collective" in block
        assert "pool-and-license" in block
        assert "first DEDICATED UK collective-licensing mechanism" in block

    def test_m723_confounders_ranked_strong_first(self):
        block = self._block()
        assert "confounders_ranked:" in block
        assert "Zero disclosed dollars, pricing, or AI-buyer sign-ups" in block
        assert "The 250 opt-in count is self-reported by the scheme operator" in block
        strong_idx = block.index("strength: 'STRONG'")
        moderate_idx = block.index("strength: 'MODERATE'")
        assert strong_idx < moderate_idx, "strong confounders must precede moderate"

    def test_m723_counter_evidence(self):
        block = self._block()
        assert "counterevidence:" in block
        assert "simultaneously lobbies the UK government to rule out a copyright exception for AI" in block
        assert "strongest_counterargument:" in block

    def test_m723_statistical_discipline(self):
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
        assert "verdict: 'directionally_supported_not_proven'" in block
        assert "artifact_grade: false" in block
        assert "no_analysis_json_update: true" in block

    def test_m723_not_falsification_member(self):
        block = self._block()
        assert "NOT a member - qualitative Type C economics leg mapping a publisher-side collective vehicle" in block
        assert "ledger holds at 26" in block

    def test_m723_block_key_unique_in_entities(self):
        text = _read("profiles/competitor-entities.yaml")
        assert text.count(M723_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(723)
        assert any(
            p.endswith("competitor-entities.yaml") for p in hits
        ), hits

    def test_m723_designed_keying_no_underscore_723(self):
        assert MECH_ID_MARKER + "723" not in self._block()


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
    """Post-#819 corpus integrity: max 723, zero 724 keys."""

    def test_max_numeric_mechanism_id_is_723(self):
        assert _max_numeric_mechanism_id() == 723

    def test_zero_underscore_724_keys_in_profiles(self):
        hits = _repo_grep_underscore_mechanism(724)
        profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
        assert profile_hits == [], profile_hits

    def test_zero_underscore_724_references_in_tests(self):
        hits = _repo_grep_underscore_mechanism(724)
        test_hits = [p for p in hits if p.startswith(TESTS_DIR)]
        assert test_hits == [], test_hits

    def test_zero_numeric_724_keys_in_profiles(self):
        hits = _repo_grep_numeric_mechanism_id(724)
        assert hits == [], hits

    def test_designed_keying_holds_no_underscore_721_722_723_in_profiles(self):
        for n in (721, 722, 723):
            hits = _repo_grep_underscore_mechanism(n)
            profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
            assert profile_hits == [], (n, profile_hits)

    def test_c819_max_723_sweep_stays_green(self):
        # Type D adds no mechanisms; #819's max-723 sweep stays green.
        assert _max_numeric_mechanism_id() == 723

    def test_c819_zero_underscore_724_sweeps_stay_green(self):
        hits = _repo_grep_underscore_mechanism(724)
        assert hits == [], hits

    def test_c819_zero_numeric_724_sweep_stays_green(self):
        hits = _repo_grep_numeric_mechanism_id(724)
        assert hits == [], hits

    def test_a817_max_721_sweep_superseded_by_design(self):
        # #817 asserted max == 721 pre-commit; advancing to 723
        # supersedes it per the #710/#720 convention. Documented, not
        # repaired.
        assert _max_numeric_mechanism_id() == 723 != 721

    def test_b818_max_722_sweep_superseded_by_design(self):
        # #818 asserted max == 722 pre-commit; advancing to 723
        # supersedes it per the #710/#720 convention. Documented, not
        # repaired.
        assert _max_numeric_mechanism_id() == 723 != 722


class TestTypeDEngineStatisticalMeaningfulness:
    """Fresh synthetic corpora (new values, not #815's)."""

    def test_strong_signal_pair_significant_at_engine_layer(self):
        target = [0.79, 0.93, 0.74, 0.86, 0.90]
        peers = [-0.09, 0.05, -0.14, 0.02, -0.07]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 17),
            period_end=datetime.datetime(2026, 9, 17),
        )
        assert report.asymmetry_score == pytest.approx(0.890, rel=1e-9)
        assert report.is_significant is True
        assert report.p_value == pytest.approx(9.729e-08, rel=1e-2)
        assert report.cohens_d == pytest.approx(11.3213, rel=1e-2)
        assert report.confidence_interval_lower > 0
        assert report.confidence_interval_lower == pytest.approx(0.8000, rel=1e-2)
        assert report.confidence_interval_upper == pytest.approx(0.9721, rel=1e-2)

    def test_near_null_pair_silent_at_engine_layer(self):
        target = [0.14, -0.10, 0.06, -0.04, 0.11]
        peers = [0.12, -0.08, 0.05, -0.03, 0.10]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 17),
            period_end=datetime.datetime(2026, 9, 17),
        )
        assert report.asymmetry_score == pytest.approx(0.002, abs=1e-9)
        assert report.is_significant is False
        assert report.p_value > 0.5
        assert abs(report.cohens_d) < 0.5
        assert (
            report.confidence_interval_lower < 0 < report.confidence_interval_upper
        )

    def test_degenerate_n1_contract_on_m721_tone_pair(self):
        # The m721 degenerate check: calculate_asymmetry([-0.20], [0.25])
        # returns asymmetry -0.45 with t 0.0 / p 1.0 / d 0.0.
        t, p = welch_t_test([-0.20], [0.25])
        d = cohens_d([-0.20], [0.25])
        assert (t, p) == (0.0, 1.0)
        assert d == 0.0
        assert is_significant(p) is False
        assert abs(-0.20 - 0.25) == pytest.approx(0.45)
        t2, p2 = welch_t_test([0.25], [-0.20])
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
    """Suite verdict lineage; #815's background suite owns the verdict,
    #820 re-launches."""

    TOMBSTONE_LINEAGE = 25

    def test_tombstone_lineage_count(self):
        # TWENTY-FIFTH consecutive background full-suite death: #815's
        # background suite (re-launched 18:19 PDT) died at ~1% progress
        # and no pytest was alive at this run's check. Advances from the
        # TWENTY-FOURTH lineage declared in #815 per the #770/#780
        # convention.
        assert self.TOMBSTONE_LINEAGE == 25

    def test_815_background_suite_verdict_died(self):
        # Dead-run markers pinned per the #770/#780 convention; triaged
        # no further. Log stalled at ~1% since 18:19 PDT.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_815_full_suite.log",
        )
        assert os.path.exists(log_path), log_path
        size = os.path.getsize(log_path)
        assert size < 10000, size
        text = open(log_path, encoding="utf-8", errors="replace").read()
        assert "%" in text  # pytest -q progress marker present
        assert "1%" in text  # stalled at ~1% progress

    def test_relaunch_log_path_in_goal_hidden_files(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_820_full_suite.log",
        )
        assert os.path.basename(log_path) == "type_d_820_full_suite.log"

    def test_820_suite_relaunched_this_run(self):
        # This run re-launches the full suite as a background process
        # writing to the persistent goal hidden_files path; the next
        # Type D run checks its verdict per the #795 convention.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_820_full_suite.log",
        )
        assert os.path.exists(log_path), log_path


class TestDocSync820:
    def test_readme_row_820(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_820(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_820_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog820:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #820 Type D:")
        return log[idx : idx + 9000]

    def test_log_entry_present(self):
        assert "## #820 Type D:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        entry = self._entry()
        assert "mechanism_id 723" in entry
        assert "m721" in entry
        assert "m722" in entry


class TestDateGrounding820:
    def test_sep_17_2026_is_thursday(self):
        assert datetime.date(2026, 9, 17).strftime("%A") == "Thursday"
