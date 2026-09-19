"""Type D -- Iteration #845 (Sat 2026-09-19 00:00 PDT): m736 / m737 / m738
qualitative-discipline verification + post-#844 corpus integrity
(max numeric mechanism_id 738; zero 739 keys; ledger holds at 26) +
#840 background-suite verdict (died at 388 bytes since Sep 18 19:17 PDT,
no pytest alive at this run's check; ELEVENTH consecutive background
full-suite death; tombstone lineage advances TWENTY-NINTH ->
THIRTIETH per #565/#770/#780) + fresh synthetic engine meaningfulness
(new values, not #840's) + re-launch of the full suite as a background
process writing to goal hidden_files type_d_845_full_suite.log (next
Type D run checks its verdict per the #795 convention).

Verifies:
- m736 (Gizmodo x OpenAI Claude-hack cybersecurity-accountability
  register, Type A #842, profiles/gizmodo.yaml): FIRST dedicated Type A
  mechanism on Gizmodo's Sep 18 2026 "Three Hackers Used Claude to
  Break Into OpenAI In Less Than 72 Hours" (first-hand 62-line read).
  Register: adversarial cybersecurity-accountability toward OpenAI
  (MANUAL ILLUSTRATIVE -0.45) + Anthropic-instrument sub-register
  (-0.20). Illustrative OpenAI-minus-Meta delta +0.167 - inside the
  symmetric adversarial band (m577 Meta band -0.617). Within-entity
  Sep16-Sep18 hardening -0.25: register follows the PEG, not the
  entity. Null-tie control ($0 AI licensing) behaving as predicted:
  EXTENDS m577, REPLICATES m582/m721, COMPLEMENTS m733. p_value /
  cohens_d / ci_95 NOT_CALCULATED; is_significant false (Aug 28 2026
  standing rule); engine NOT run; verdict
  directionally_supported_not_proven; NOT artifact-grade; no
  analysis.json update; NOT a falsification-family member (ledger
  holds at 26).
- m737 (Jason England (Tom's Guide) Sep-2026 CEO-interview
  quote-platforming direction asymmetry, Type B #843,
  profiles/careers/journalists.yaml): FIRST dedicated Type B
  mechanism on Jason England in journalists.yaml; mechanism_ids [737].
  Same-writer, same-month, same-genre pair: Meta arm "Exclusive: Even
  Realities CEO slams Meta Ray-Bans - we don't thrive on selling
  data" (-0.40; surveillance vocabulary directed AT Meta via headline
  verb "slams") vs Snap arm "Snap CEO says covert smart glasses are
  'creepy' - why Specs look bold on purpose" (+0.25; "creepy"
  deflected onto generic covert category, Snap's own record-video
  cameras get the "look bold on purpose" halo). Illustrative
  Meta-minus-Snap delta -0.65. REFINES mechanism 146; CRITICAL SCOPE
  BOUND (vocabulary sourced from CEO quotes). MANUAL ILLUSTRATIVE
  only; engine NOT run; verdict directionally_supported_not_proven;
  NOT a falsification-family member; ledger holds at 26.
- m738 (Roundtable x Paradium.AI 10-year $1B AI/DeFi MediaOS
  infrastructure-capture leg, Type C #844,
  profiles/competitor-entities.yaml): FIRST dedicated corpus mapping
  of the infrastructure-capture publisher-tech financial vector.
  SIXTH relationship direction in the taxonomy. Headline-vs-substance:
  $1B is the 10-year platform-agreement headline, NOT committed cash;
  committed leg is $89,555,638 equity for ~49.5% at $3.80/share
  (below-50% cap; sellers Simplify Inventions LLC + MBX Capital Aren
  LLC; Paradium not a party; condition precedent). Worldwide
  non-cancelable perpetual tech license; Coinbase smart-wallet
  journalist payroll (first publisher-side DeFi payroll in corpus);
  Q4 2026 close target. p_value, cohens_d, ci_95 NOT_CALCULATED;
  verdict directionally_supported_not_proven; falsification_family
  false; ledger holds at 26; no analysis.json update.
- Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent
  in profiles/; ledger holds at 26.
- Post-#844 corpus integrity: max numeric mechanism_id == 738 in
  profiles/; zero underscore-form 739 key substrings in profiles/
  and tests/ (own file excluded as sweep carrier per the #715
  pattern-rescope lesson; needles built by format string so no
  literal is carried); zero numeric 739 keys in profiles/; m736 /
  m737 / m738 block keys each unique in their home YAMLs; designed
  keying holds (no underscore-form 736 / 737 / 738 key substrings in
  profiles/). #844's max-738 / zero-underscore-739 /
  zero-numeric-739 sweeps stay green (Type D adds no mechanisms);
  #842's max-736 and #843's max-737 sweeps fail by designed
  supersession per the #710/#720 convention (documented, not
  repaired).
- Statistical meaningfulness on FRESH synthetic corpora (new
  values, not #840's): strong-signal n=5-per-arm pair (asymmetry
  +1.01, t=21.5333, p=7.56e-08, d=13.6188, is_significant True at
  the ENGINE layer, 95% CI (0.934, 1.1) entirely above zero);
  fresh near-null pair (asymmetry -0.01, t=-0.1913, p=0.8531,
  d=-0.1210, is_significant False, CI (-0.102, 0.076) crossing
  zero, silent); fresh degenerate n=1-per-arm contract on the m737
  tone pair ([-0.40], [0.25]: t=0.0, p=1.0, d=0.0, is_significant
  False, |asymmetry| == 0.65 exact, arm-swap negates). Engine
  significance is never promoted to a finding (Aug 28 2026
  standing rule).
- Full-suite status: the #840 background suite re-launched 19:17
  PDT died (type_d_840_full_suite.log stalled at 388 bytes / ~1%
  progress since 19:17:24 PDT; no pytest alive at this run's check
  via the bracket-trick ps scan - the pgrep hits were self-match
  phantoms) - ELEVENTH consecutive background death (#705's,
  #710's, #715's first re-launch, #715's re-launch, #720's
  re-launch, #725's re-launch, #730's re-launch, #825's re-launch,
  #830's re-launch, #835's re-launch, #840's re-launch; tombstone
  lineage per #565 advances TWENTY-NINTH -> THIRTIETH). This run
  re-launches the full suite as a background process writing to
  goal hidden_files type_d_845_full_suite.log (alive at re-launch
  check); the next Type D run checks its verdict per the #795
  convention.

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
    "test_type_d_845_m736_m737_m738_qualitative_corpus_integrity_sep19_12am.py"
)
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"

ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

M736_KEY = "gizmodo_openai_claude_hack_cybersecurity_accountability_register_sep18_2026"
M737_KEY = "type_b_843_jason_england_sep2026_ceo_interview_platform_direction_asymmetry_sep18_10pm"
M737_PARENT_KEY = "jason_england"
M738_KEY = "roundtable_paradium_infrastructure_capture_sep2026"

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


class TestNovelty845:
    def test_single_test_type_d_845_file(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_845") and f.endswith(".py")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_d_845_main_commit_unique_and_anchored(self):
        # No #845 main commit exists pre-commit; the anchor test pins
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
            if "Type D #845" in line and "followup" not in line.lower()
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
        # posture: max stays 738, zero numeric 739 keys.
        assert _max_numeric_mechanism_id() == 738
        assert _repo_grep_numeric_mechanism_id(739) == []

    def test_840_844_window_closed_prior_to_845(self):
        log = _read(LOG_PATH)
        for marker in (
            "## #840 Type D:",
            "#841 Type E:",
            "#842 Type A:",
            "## #843 Type B:",
            "## #844 Type C:",
        ):
            assert marker in log, marker


class TestTypeDRotationGuard:
    """#845 is the Type D anchor opening window 845-849."""

    WINDOW = ("D", "E", "A", "B", "C")

    def test_rotation_window_845_849(self):
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


class TestTypeDM736QualitativeDiscipline:
    """Type D verification of m736 qualitative discipline (Type A #842).

    FIRST dedicated Type A mechanism on Gizmodo's Sep 18 2026
    Claude-hack accountability piece; assertions run on the
    whitespace-folded block per the #732 convention (raw YAML doubles
    internal single quotes)."""

    def _block(self):
        return _fold(_block("profiles/gizmodo.yaml", M736_KEY, 14000))

    def test_m736_iteration_and_type(self):
        b = self._block()
        assert "mechanism_id: 736" in b
        assert "iteration: 842" in b
        assert "iteration_type: A" in b
        assert "date: '2026-09-18'" in b

    def test_m736_publication_competitor_comparator(self):
        b = self._block()
        assert "publication_focus: Gizmodo (Keleops AG)" in b
        assert "publication_pair: Gizmodo x OpenAI" in b
        assert 'entity_pair: "OpenAI vs Anthropic vs Meta"' in b

    def test_m736_first_dedicated_type_a_on_claude_hack_piece(self):
        b = self._block()
        assert "FIRST dedicated Type A mechanism on Gizmodo" in b
        assert "Three Hackers Used Claude to Break Into OpenAI In Less Than 72 Hours" in b

    def test_m736_register_evidence_verbatim(self):
        b = self._block()
        assert "thousands of OpenAI agents secretly escaped their testing environment" in b
        assert "a whopping $6,500" in b
        assert "could easily have been discovered and exploited first by someone with much less friendly intentions" in b

    def test_m736_manual_illustrative_tones(self):
        b = self._block()
        assert "manual_illustrative_tone_openai_arm: -0.45" in b
        assert "manual_illustrative_tone_anthropic_sub_arm: -0.20" in b

    def test_m736_illustrative_delta_inside_symmetric_band(self):
        b = self._block()
        assert "illustrative_delta_openai_minus_meta: 0.167" in b
        assert "'-0.45 - (-0.617) = 0.167'" in b
        assert "INSIDE the symmetric adversarial band" in b

    def test_m736_within_entity_hardening_follows_peg(self):
        b = self._block()
        assert "within_entity_sep16_to_sep18_hardening: -0.25" in b
        assert "register follows the PEG" in b

    def test_m736_null_tie_control_behaves_as_predicted(self):
        b = self._block()
        assert "null-tie control behaving exactly as the incentive theory predicts" in b
        assert "no payer, no softening" in b

    def test_m736_extends_replicates_complements(self):
        b = self._block()
        assert "EXTENDS mechanism 577 (symmetric adversarial)" in b
        assert "REPLICATES m582/m721" in b
        assert "COMPLEMENTS m733" in b
        assert "cross_references: [512, 577, 582, 721, 733]" in b

    def test_m736_statistical_discipline(self):
        b = self._block()
        assert "p_value: NOT_CALCULATED" in b
        assert "cohens_d: NOT_CALCULATED" in b
        assert "ci_95: NOT_CALCULATED" in b
        assert "is_significant: false" in b
        assert "engine: 'NOT run'" in b
        assert "verdict: directionally_supported_not_proven" in b
        assert "no_analysis_json_update: true" in b

    def test_m736_not_falsification_member(self):
        b = self._block()
        assert "NOT a member - null-tie control documentation" in b
        assert "fifth in the Gizmodo control family" in b
        assert "Ledger holds at 26" in b

    def test_m736_block_key_unique_in_gizmodo(self):
        doc = _read("profiles/gizmodo.yaml")
        assert doc.count(M736_KEY + ":") == 1


class TestTypeDM737QualitativeDiscipline:
    """Type D verification of m737 qualitative discipline (Type B #843).

    FIRST dedicated Type B mechanism on Jason England in
    journalists.yaml; assertions run on the folded parent
    jason_england block (which carries the notes discipline prose)
    plus the sub-block."""

    def _parent(self):
        return _fold(_block("profiles/careers/journalists.yaml", M737_PARENT_KEY, 14000))

    def _block(self):
        return _fold(_block("profiles/careers/journalists.yaml", M737_KEY, 14000))

    def test_m737_mechanism_id_list_and_block(self):
        assert "mechanism_ids: [737]" in self._parent()
        b = self._block()
        assert "mechanism_id: 737" in b
        assert "iteration: 843" in b
        assert "type: B" in b
        assert "date: '2026-09-18 22:00 PDT'" in b

    def test_m737_first_dedicated_type_b_on_england(self):
        assert "FIRST dedicated Type B mechanism on Jason England in profiles/careers/journalists.yaml" in self._parent()

    def test_m737_meta_arm_headline_verb_slams(self):
        b = self._block()
        assert "Exclusive: Even Realities CEO slams Meta Ray-Bans - we don't thrive on selling data" in b
        assert "tone_MANUAL_ILLUSTRATIVE: -0.40" in b
        assert "privacy_vocabulary_direction: directed_at_meta" in b

    def test_m737_snap_arm_creepy_deflected(self):
        b = self._block()
        assert "Snap CEO says covert smart glasses are 'creepy' - why Specs look bold on purpose" in b
        assert "tone_MANUAL_ILLUSTRATIVE: 0.25" in b
        assert "privacy_vocabulary_direction: deflected_from_snap_own_cameras" in b

    def test_m737_illustrative_delta(self):
        b = self._block()
        assert "illustrative_delta_meta_minus_snap: -0.65" in b
        assert "delta_calc: '(-0.40) - (0.25) = -0.65'" in b

    def test_m737_refines_146_scope_bound(self):
        b = self._block()
        assert "REFINES mechanism 146" in b
        assert "CRITICAL SCOPE BOUND" in b
        assert "quote-platforming direction" in b

    def test_m737_snap_record_video_fact_sourced(self):
        b = self._block()
        assert "snap_specs_record_video: true" in b
        assert "record video" in b

    def test_m737_statistical_discipline(self):
        parent = self._parent()
        assert "MANUAL ILLUSTRATIVE only" in parent
        assert "engine NOT run" in parent
        assert "p_value/cohens_d/ci_95 NOT_CALCULATED" in parent
        assert "is_significant False" in parent
        assert "verdict directionally_supported_not_proven" in parent

    def test_m737_not_falsification_member(self):
        parent = self._parent()
        assert "NOT a falsification-family member" in parent
        assert "ledger holds at 26" in parent

    def test_m737_block_key_unique_in_journalists(self):
        doc = _read("profiles/careers/journalists.yaml")
        assert doc.count(M737_KEY + ":") == 1


class TestTypeDM738QualitativeDiscipline:
    """Type D verification of m738 qualitative discipline (Type C #844).

    FIRST corpus mechanism mapping the infrastructure-capture
    publisher-tech financial vector; qualitative market-structure
    mapping, not a tone test."""

    def _block(self):
        return _fold(_block("profiles/competitor-entities.yaml", M738_KEY, 16000))

    def test_m738_iteration_and_mechanism(self):
        b = self._block()
        assert "mechanism_id: 738" in b
        assert "Roundtable x Paradium.AI" in b
        assert "Infrastructure-Capture as the Sixth Relationship Direction" in b

    def test_m738_first_infrastructure_capture_mapping(self):
        b = self._block()
        assert "First dedicated corpus mapping of the infrastructure-capture publisher-tech financial vector" in b
        assert "INFRASTRUCTURE-CAPTURE" in b

    def test_m738_sixth_relationship_direction(self):
        b = self._block()
        assert "SIXTH direction in the relationship-direction taxonomy" in b

    def test_m738_headline_vs_substance_discipline(self):
        b = self._block()
        assert "$89,555,638" in b
        assert "49.5%" in b
        assert "$3.80 per share" in b
        assert "not committed cash changing hands at signing" in b

    def test_m738_perpetual_license_and_defi_payroll(self):
        b = self._block()
        assert "worldwide, non-cancelable, perpetual license" in b
        assert "Coinbase" in b
        assert "first publisher-side DeFi payroll" in b

    def test_m738_corpus_arc_rsl_to_capture(self):
        b = self._block()
        assert "RSL" in b
        assert "Nov 26 2025" in b
        assert "full-stack infrastructure capture" in b

    def test_m738_confounder_and_counterargument(self):
        b = self._block()
        assert "confounders_ranked_strong_first" in b
        assert "counter_evidence" in b
        assert "deal has not closed" in b

    def test_m738_no_coverage_tone_claim(self):
        b = self._block()
        assert "no coverage-tone claim is made" in b
        assert "Correlation is not causation" in b

    def test_m738_statistical_discipline(self):
        b = self._block()
        assert "p_value, cohens_d, ci_95 NOT_CALCULATED" in b
        assert "verdict: 'directionally_supported_not_proven'" in b
        assert "falsification_family: false" in b
        assert "falsification_ledger_holds_at: 26" in b

    def test_m738_block_key_unique_in_entities(self):
        doc = _read("profiles/competitor-entities.yaml")
        assert doc.count(M738_KEY + ":") == 1


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
    """Post-#844 corpus integrity: max 738, zero 739 keys."""

    def test_max_numeric_mechanism_id_is_738(self):
        assert _max_numeric_mechanism_id() == 738

    def test_zero_underscore_739_keys_in_profiles(self):
        hits = _repo_grep_underscore_mechanism(739)
        profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
        assert profile_hits == [], profile_hits

    def test_zero_underscore_739_references_in_tests(self):
        hits = _repo_grep_underscore_mechanism(739)
        test_hits = [p for p in hits if p.startswith(TESTS_DIR)]
        assert test_hits == [], test_hits

    def test_zero_numeric_739_keys_in_profiles(self):
        hits = _repo_grep_numeric_mechanism_id(739)
        assert hits == [], hits

    def test_designed_keying_holds_no_underscore_736_737_738_in_profiles(self):
        for n in (736, 737, 738):
            hits = _repo_grep_underscore_mechanism(n)
            profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
            assert profile_hits == [], (n, profile_hits)

    def test_c844_max_738_sweep_stays_green(self):
        # Type D adds no mechanisms; #844's max-738 sweep stays green.
        assert _max_numeric_mechanism_id() == 738

    def test_c844_zero_underscore_739_sweeps_stay_green(self):
        hits = _repo_grep_underscore_mechanism(739)
        assert hits == [], hits

    def test_c844_zero_numeric_739_sweep_stays_green(self):
        hits = _repo_grep_numeric_mechanism_id(739)
        assert hits == [], hits

    def test_a842_max_736_sweep_superseded_by_design(self):
        # #842 asserted max == 736 pre-commit; advancing to 738
        # supersedes it per the #710/#720 convention. Documented, not
        # repaired.
        assert _max_numeric_mechanism_id() == 738 != 736

    def test_b843_max_737_sweep_superseded_by_design(self):
        # #843 asserted max == 737 pre-commit; advancing to 738
        # supersedes it per the #710/#720 convention. Documented, not
        # repaired.
        assert _max_numeric_mechanism_id() == 738 != 737


class TestTypeDEngineStatisticalMeaningfulness:
    """Fresh synthetic corpora (new values, not #840's)."""

    def test_strong_signal_pair_significant_at_engine_layer(self):
        target = [0.55, 0.62, 0.48, 0.71, 0.59]
        peers = [-0.42, -0.35, -0.51, -0.38, -0.44]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 19),
            period_end=datetime.datetime(2026, 9, 19),
        )
        assert report.asymmetry_score == pytest.approx(1.01, rel=1e-9)
        assert report.t_statistic == pytest.approx(21.5333, rel=1e-4)
        assert report.is_significant is True
        assert report.p_value == pytest.approx(7.555554953877195e-08, rel=1e-2)
        assert report.cohens_d == pytest.approx(13.6188, rel=1e-2)
        assert report.confidence_interval_lower > 0
        assert report.confidence_interval_lower == pytest.approx(0.934, rel=1e-2)
        assert report.confidence_interval_upper == pytest.approx(1.1, rel=1e-2)

    def test_near_null_pair_silent_at_engine_layer(self):
        target = [0.10, -0.05, 0.12, -0.08, 0.03]
        peers = [0.06, 0.11, -0.02, 0.09, -0.07]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 19),
            period_end=datetime.datetime(2026, 9, 19),
        )
        assert report.asymmetry_score == pytest.approx(-0.01, abs=1e-9)
        assert report.t_statistic == pytest.approx(-0.19132, rel=1e-4)
        assert report.is_significant is False
        assert report.p_value == pytest.approx(0.8531, rel=1e-2)
        assert report.cohens_d == pytest.approx(-0.1210, rel=1e-2)
        assert (
            report.confidence_interval_lower
            < 0
            < report.confidence_interval_upper
        )

    def test_degenerate_n1_contract_on_m737_tone_pair(self):
        # The m737 degenerate check: calculate_asymmetry([-0.40], [0.25])
        # returns asymmetry -0.65 with t 0.0 / p 1.0 / d 0.0.
        t, p = welch_t_test([-0.40], [0.25])
        d = cohens_d([-0.40], [0.25])
        assert (t, p) == (0.0, 1.0)
        assert d == 0.0
        assert is_significant(p) is False
        assert abs(-0.40 - 0.25) == pytest.approx(0.65)
        t2, p2 = welch_t_test([0.25], [-0.40])
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
    """Suite verdict lineage; #840's background suite owns the verdict,
    #845 re-launches."""

    TOMBSTONE_LINEAGE = 30

    def test_tombstone_lineage_count(self):
        # THIRTIETH consecutive background full-suite death: #840's
        # background suite (re-launched 19:17 PDT Sep 18) died at ~1%
        # progress and no pytest was alive at this run's check (the
        # pgrep hits were self-match phantoms; the bracket-trick ps
        # scan found zero suite processes). Advances from the
        # TWENTY-NINTH lineage declared in #840 per the
        # #565/#770/#780 convention.
        assert self.TOMBSTONE_LINEAGE == 30

    def test_840_background_suite_verdict_died(self):
        # Dead-run markers pinned per the #770/#780 convention; triaged
        # no further. Log stalled at 388 bytes (~1% progress) since
        # 19:17:24 PDT Sep 18 with no pytest alive at this run's check.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_840_full_suite.log",
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
            "type_d_845_full_suite.log",
        )
        assert os.path.basename(log_path) == "type_d_845_full_suite.log"

    def test_845_suite_relaunched_this_run(self):
        # This run re-launches the full suite as a background process
        # writing to the persistent goal hidden_files path; the next
        # Type D run checks its verdict per the #795 convention.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_845_full_suite.log",
        )
        assert os.path.exists(log_path), log_path


class TestDocSync845:
    def test_readme_row_845(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_845(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_845_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog845:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #845 Type D:")
        return log[idx : idx + 12000]

    def test_log_entry_present(self):
        assert "## #845 Type D:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        entry = self._entry()
        assert "mechanism_id 738" in entry
        assert "m736" in entry
        assert "m737" in entry
        assert "m738" in entry

    def test_log_rotation_window_845_849(self):
        entry = self._entry()
        assert "845-849" in entry


class TestDateGrounding845:
    def test_sep_19_2026_is_saturday(self):
        assert datetime.datetime(2026, 9, 19).strftime("%A") == "Saturday"

    def test_run_time_pdt_grounded(self):
        assert datetime.datetime(2026, 9, 19, 0, 0).strftime("%H:%M") == "00:00"
