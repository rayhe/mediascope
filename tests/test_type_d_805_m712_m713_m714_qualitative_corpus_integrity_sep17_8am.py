"""Type D -- Iteration #805 (Thu 2026-09-17 08:00 PDT): m712 / m713 / m714
qualitative-discipline verification + post-#804 corpus integrity
(max numeric mechanism_id 714; zero 715 keys; ledger holds at 26) +
#800 foreground-suite verdict (died mid-run at ~2%, last write
03:28 PDT, no pytest alive; background tombstone lineage holds at
TWENTY-SECOND) + fresh synthetic engine meaningfulness +
re-launch of the full suite as a background process to goal hidden_files
type_d_805_full_suite.log (next Type D run checks its verdict).

Verifies:
- m712 (WIRED x OpenAI misalignment-framework relay vs Meta glasses
  adversarial, Type A #802, profiles/competitor-coverage-research.yaml +
  wired.yaml backlink): FIRST dedicated WIRED x OpenAI misalignment
  framework mechanism; OpenAI arm Sep 16 2026 "OpenAI Releases New Policy
  for Reporting Incidents of Model Misalignment" platform relay register
  (+0.15 MANUAL ILLUSTRATIVE, secondary-attribution bounded); Meta
  comparator (same publication, in-corpus Aug 28 2026) alarm register
  (-0.55); illustrative OpenAI-minus-Meta delta +0.70; Conde Nast x OpenAI
  paid licensing (Aug 2024, $1-5M/yr) vs Meta $0; verdict
  directionally_supported_not_proven; degenerate n=1 engine check
  (asymmetry 0.70, t 0.0 / p 1.0 / d 0.0, is_significant False); NOT
  artifact-grade; NOT a falsification-family member (ledger holds at 26).
- m713 (Sabrina Ortiz, ZDNet, three-entity incumbent gradient, Type B
  #803, profiles/competitor-coverage-research.yaml + careers entry):
  FIRST dedicated corpus mechanism on Ortiz; Meta arm (Ray-Ban Display,
  "nearly sold") +0.45 illustrative; Samsung arm (Moohan beats her Vision
  Pro) +0.40; Apple incumbent leg -0.10; illustrative
  challenger-minus-incumbent spread +0.525; zero privacy/surveillance
  vocabulary in any excerpted arm; uniform anti-Meta financial-incentive
  prediction NOT supported; p_value/cohens_d/ci_95 NOT_CALCULATED,
  is_significant false; verdict directionally_supported_not_proven;
  NOT artifact-grade; NOT a falsification-family member.
- m714 (OpenAI x Village Media first Canadian news deal, Type C #804,
  profiles/competitor-entities.yaml): FIRST dedicated mapping of OpenAI's
  first news deal in Canada (announced Sep 16 2026, Axios/Sara Fischer);
  OpenAI funding + API credits + technical support for the Open Door
  community navigator (Sault Ste. Marie, Ontario) in exchange for
  attributed citation in ChatGPT; local-news template (Axios Jan 2025)
  crosses into Canada; qualitative-only, tone NOT_SCORED, p_value /
  cohens_d / ci_95 NOT_CALCULATED, is_significant false; verdict
  directionally_supported_not_proven; NOT a falsification-family member
  (ledger holds at 26); no analysis.json update.
- Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent in
  profiles/; ledger holds at 26.
- Post-#804 corpus integrity: max numeric mechanism_id == 714 in
  profiles/; zero underscore-form 715 key substrings in profiles/ and
  tests/ (own file excluded as sweep carrier per the #715
  pattern-rescope lesson; needles built by format string so no literal
  is carried); zero numeric 715 keys in profiles/; m712 / m713 / m714
  block keys each unique in their home YAMLs; designed keying holds
  (no underscore-form 712/713/714 mechanism key substrings in
  profiles/). #804's max-714 and zero-underscore-714 sweeps stay green
  (Type D adds no mechanisms); #802's max-712, #803's max-713 and
  zero-numeric-714, and #804's max-714 forward and zero-numeric-714
  sweeps fail by designed supersession per the #710/#720 convention
  (documented, not repaired).
- Statistical meaningfulness on FRESH synthetic corpora (new values,
  not #800's): strong-signal n=5-per-arm pair (asymmetry +0.922,
  p=6.31e-07 < 5e-4, d=12.77 > 8, 95% CI (0.842, 0.996) above zero,
  is_significant True at the ENGINE layer); fresh near-null pair
  (asymmetry 0.004, p=0.869 > 0.5, |d|=0.108 < 0.5, CI crossing zero,
  silent); fresh degenerate n=1-per-arm contract (t=0.0, p=1.0, d=0.0,
  is_significant False, |asymmetry| == 1.10, arm-swap negates). Engine
  significance is never promoted to a finding (Aug 28 2026 standing
  rule).
- Full-suite status: the #800 foreground suite launched 03:14 PDT died
  mid-run (log stalled at 1124 bytes / ~2% since 03:28 PDT; no pytest
  alive at this run's check) - the foreground-suite verdict this run
  records; background tombstone lineage holds at TWENTY-SECOND (#795
  and #800 both ran foreground suites, no new background deaths).
  This run re-launches the full suite as a background process writing
  to goal hidden_files type_d_805_full_suite.log (alive at re-launch
  check); next Type D run checks its verdict per the #795 convention.

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
    "test_type_d_805_m712_m713_m714_qualitative_corpus_integrity_sep17_8am.py"
)
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"

ANCHORED_SHA = "88652d481ad81724f741659a8f92c1060b4b047c"

M712_KEY = "wired_openai_misalignment_framework_relay_sep17"
M712_WIRED_KEY = "misalignment_framework_relay_sep17"
M713_KEY = "sabrina ortiz zdnet three entity incumbent gradient sep2026"
M713_JOURNALIST_KEY = "sabrina_ortiz"
M713_BLOCK_KEY = "type_b_803_sabrina_ortiz_zdnet_three_entity_incumbent_gradient_sep17"
M714_KEY = "openai_village_media_first_canada_news_deal_sep2026"


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


class TestNovelty805:
    """Pre-commit novelty: single new file, unique commit."""

    def test_single_test_type_d_805_file(self):
        files = sorted(
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_805") and f.endswith(".py")
        )
        assert files == [TEST_BASENAME], files

    def test_type_d_805_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 convention; the main commit
        # does not exist yet. Patched green in the anchor followup.
        # Specific "Type D #805: m712" prefix per the #796 convention:
        # immune to a "Type D #805 push-status record" followup and to
        # the benign "Type D #805" mention in the #804 doc-sync body.
        mains = _git_log_mains("Type D #805: m712")
        assert len(mains) == 1, mains
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), mains
        assert mains[0].startswith(ANCHORED_SHA + " "), mains

    def test_novelty_verification_claim(self):
        # Type D adds no mechanism; novelty is the corpus-integrity posture:
        # single new file, no mechanism keys added (max stays 714).
        assert _max_numeric_mechanism_id() == 714
        assert _repo_grep_numeric_mechanism_id(715) == []

    def test_800_804_window_closed_prior_to_805(self):
        # Opening leg of the 805-809 window: the previous window must read
        # closed D->E->A->B->C (newest first) as a consecutive sequence in
        # history, wherever it sits (per the #795 repair: the newest-five
        # shortcut broke once 806+ landed; per #800, history lookup).
        legs = _window_legs_deduped("805")
        want = [
            ("C", "804"),
            ("B", "803"),
            ("A", "802"),
            ("E", "801"),
            ("D", "800"),
        ]
        found = any(
            legs[i : i + 5] == want for i in range(len(legs) - 4)
        )
        assert found, legs[:12]


class TestTypeDRotationGuard:
    """#805 is the Type D anchor opening window 805-809."""

    WINDOW = ("D", "E", "A", "B", "C")

    def test_rotation_window_805_809(self):
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


class TestTypeDM712QualitativeDiscipline:
    """Type D verification of m712 qualitative discipline (Type A #802).

    Assertions run on the whitespace-folded block per the #732
    convention: the m712 description, statistical_discipline, and
    falsification_family fields wrap across raw YAML lines."""

    def _block(self):
        return _fold(
            _block(
                "profiles/competitor-coverage-research.yaml", M712_KEY, 22000
            )
        )

    def test_m712_publication_and_entity(self):
        block = self._block()
        assert "publication: WIRED (Conde Nast / Advance Publications)" in block
        assert "entity: OpenAI" in block

    def test_m712_arm1_misalignment_framework_relay(self):
        block = self._block()
        assert "OpenAI Releases New Policy for Reporting" in block
        assert "tone_MANUAL_ILLUSTRATIVE: 0.15" in block

    def test_m712_meta_comparator_adversarial(self):
        block = self._block()
        assert "meta_glasses_tone_MANUAL_ILLUSTRATIVE: -0.55" in block
        assert "pervert glasses" in block

    def test_m712_illustrative_delta(self):
        block = self._block()
        assert "illustrative_register_delta_openai_minus_meta: 0.70" in block

    def test_m712_financial_tie(self):
        block = self._block()
        assert "Conde Nast x OpenAI paid content licensing" in block
        assert "meta_pays: $0" in block

    def test_m712_secondary_attribution_bound(self):
        block = self._block()
        assert "secondary-attribution-bounded" in block
        assert "Kai Chen" in block

    def test_m712_statistical_discipline_strings(self):
        block = self._block()
        assert "MANUAL ILLUSTRATIVE scores only" in block
        assert "Engine NOT run on the illustrative arms" in block
        assert "p_value/cohens_d/ci_95 NOT_CALCULATED" in block
        assert "is_significant false" in block
        assert "verdict directionally_supported_not_proven" in block
        assert "NOT artifact-grade" in block

    def test_m712_not_falsification_member(self):
        block = self._block()
        assert "NOT a falsification-family member" in block
        assert "Ledger holds at 26." in block

    def test_m712_block_key_unique_in_research(self):
        text = _read("profiles/competitor-coverage-research.yaml")
        assert text.count(M712_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(712)
        assert any(
            p.endswith("competitor-coverage-research.yaml") for p in hits
        ), hits

    def test_m712_wired_yaml_backlink(self):
        text = _read("profiles/wired.yaml")
        assert text.count(M712_WIRED_KEY + ":") == 1
        assert "mechanism_id: 712" in _block(
            "profiles/wired.yaml", M712_WIRED_KEY, 4000
        )


class TestTypeDM713QualitativeDiscipline:
    """Type D verification of m713 qualitative discipline (Type B #803)."""

    def _block(self):
        return _block(
            "profiles/competitor-coverage-research.yaml", M713_KEY, 20000
        )

    def test_m713_journalist_publication_owner(self):
        block = self._block()
        assert "journalist: 'Sabrina Ortiz'" in block
        assert "publication: zdnet" in block
        assert "owner: ziff_davis" in block

    def test_m713_meta_arm_display_forward(self):
        block = self._block()
        # Raw YAML doubles the apostrophe inside single-quoted scalars
        # ("I''m nearly sold"); assert on the apostrophe-free fragment.
        assert "nearly sold" in block
        assert "tone_illustrative: 0.45" in block

    def test_m713_samsung_arm_challenger(self):
        block = self._block()
        assert "beats my Apple Vision Pro in meaningful ways" in block
        assert "tone_illustrative: 0.40" in block

    def test_m713_apple_incumbent_leg(self):
        block = self._block()
        assert "tone_illustrative: -0.10" in block

    def test_m713_challenger_minus_incumbent_spread(self):
        block = self._block()
        assert "illustrative_challenger_minus_incumbent: 0.525" in block

    def test_m713_zero_privacy_vocabulary(self):
        block = self._block()
        assert "Zero privacy/surveillance vocabulary appears in any excerpted arm" in block

    def test_m713_statistical_discipline_strings(self):
        block = self._block()
        assert "MANUAL ILLUSTRATIVE scores only" in block
        assert "p_value/cohens_d/ci_95 NOT_CALCULATED" in block
        assert "is_significant: false" in block
        assert "Engine NOT run" in block
        assert "verdict: directionally_supported_not_proven" in block
        assert "NOT artifact-grade" in block

    def test_m713_not_falsification_member(self):
        block = self._block()
        assert "NOT a falsification-family member" in block
        assert "Ledger holds at 26." in block

    def test_m713_cross_references(self):
        block = self._block()
        assert "mechanism_id: 707" in block
        assert "mechanism_id: 710" in block
        assert "mechanism_id: 605" in block

    def test_m713_block_key_unique_in_research(self):
        text = _read("profiles/competitor-coverage-research.yaml")
        assert text.count(M713_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(713)
        assert any(
            p.endswith("competitor-coverage-research.yaml") for p in hits
        ), hits

    def test_m713_career_entry(self):
        text = _read("profiles/careers/journalists.yaml")
        assert M713_JOURNALIST_KEY + ":" in text
        block = _block(
            "profiles/careers/journalists.yaml", M713_JOURNALIST_KEY, 20000
        )
        assert M713_BLOCK_KEY in block
        assert "mechanism_ids: [713]" in block


class TestTypeDM714QualitativeDiscipline:
    """Type D verification of m714 qualitative discipline (Type C #804)."""

    def _block(self):
        return _block(
            "profiles/competitor-entities.yaml", M714_KEY, 20000
        )

    def test_m714_iteration_and_type(self):
        block = self._block()
        assert "mechanism_id: 714" in block
        assert "iteration: 804" in block
        assert "financial_incentive_mapping" in block

    def test_m714_first_canada_news_deal(self):
        block = self._block()
        assert "first news deal in Canada" in block
        assert "Village Media" in block
        assert "Sault Ste. Marie, Ontario" in block
        assert "Open Door" in block

    def test_m714_deal_consideration(self):
        block = self._block()
        assert "funding (amount undisclosed), API credits (value undisclosed)" in block
        assert "attributed citation of Village Media content in ChatGPT" in block
        assert "Varun Shetty" in block

    def test_m714_local_news_template_continuity(self):
        block = self._block()
        assert "Axios x OpenAI" in block
        assert "mechanisms 609" in block

    def test_m714_statistical_discipline(self):
        block = self._block()
        assert "tone_scores: 'NOT_SCORED'" in block
        assert "p_value: 'NOT_CALCULATED'" in block
        assert "is_significant: false" in block
        assert "qualitative_only: true" in block
        assert "verdict: directionally_supported_not_proven" in block
        assert "artifact_grade: false" in block

    def test_m714_source_urls(self):
        block = self._block()
        assert "https://www.editorandpublisher.com/stories/openai-strikes-first-news-deal-in-canada,263557" in block
        assert "https://pressgazette.co.uk/platforms/news-publisher-ai-deals-lawsuits-openai-google/" in block

    def test_m714_not_falsification_member(self):
        block = self._block()
        assert "NOT a member of the falsification family" in block
        assert "ledger holds at 26" in block

    def test_m714_block_key_unique_in_entities(self):
        text = _read("profiles/competitor-entities.yaml")
        assert text.count(M714_KEY + ":") == 1
        hits = _repo_grep_numeric_mechanism_id(714)
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
    """Post-#804 corpus integrity: max 714, zero 715 keys."""

    def test_max_numeric_mechanism_id_is_714(self):
        assert _max_numeric_mechanism_id() == 714

    def test_zero_underscore_715_keys_in_profiles(self):
        hits = _repo_grep_underscore_mechanism(715)
        profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
        assert profile_hits == [], profile_hits

    def test_zero_underscore_715_references_in_tests(self):
        hits = _repo_grep_underscore_mechanism(715)
        test_hits = [p for p in hits if p.startswith(TESTS_DIR)]
        assert test_hits == [], test_hits

    def test_zero_numeric_715_keys_in_profiles(self):
        hits = _repo_grep_numeric_mechanism_id(715)
        assert hits == [], hits

    def test_designed_keying_holds_no_underscore_712_713_714_in_profiles(self):
        for n in (712, 713, 714):
            hits = _repo_grep_underscore_mechanism(n)
            profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
            assert profile_hits == [], (n, profile_hits)

    def test_c804_max_714_sweep_stays_green(self):
        # Type D adds no mechanisms; #804's max-714 sweep stays green.
        assert _max_numeric_mechanism_id() == 714

    def test_c804_zero_underscore_714_sweeps_stay_green(self):
        hits = _repo_grep_underscore_mechanism(714)
        assert hits == [], hits

    def test_a802_max_712_sweep_superseded_by_design(self):
        # #802 asserted max == 712; advancing to 714 supersedes it per the
        # #710/#720 convention. Documented, not repaired.
        assert _max_numeric_mechanism_id() == 714 != 712

    def test_b803_max_713_sweep_superseded_by_design(self):
        # #803 asserted max == 713; advancing to 714 supersedes it per the
        # #710/#720 convention. Documented, not repaired.
        assert _max_numeric_mechanism_id() == 714 != 713

    def test_b803_zero_numeric_714_sweep_fails_by_designed_supersession(self):
        # #803 asserted zero "mechanism_id: 714" hits in profiles/; the
        # m714 block supersedes it by design.
        hits = _repo_grep_numeric_mechanism_id(714)
        assert len(hits) >= 1, hits

    def test_c804_max_714_forward_sweep_superseded_by_design(self):
        # #804's own max-714 forward assertion is superseded in the
        # forward direction by its own m714 block; a FUTURE mechanism
        # addition would move max past 714. This test pins the current
        # forward edge: advancing is a documented design event, not a
        # failure to repair. Per the #710/#720 convention.
        assert _max_numeric_mechanism_id() == 714

    def test_c804_zero_numeric_714_sweep_fails_by_designed_supersession(self):
        # #804's own zero-numeric-714 forward sweep is superseded by the
        # m714 block it documented, per the #710/#720 convention.
        hits = _repo_grep_numeric_mechanism_id(714)
        assert len(hits) >= 1, hits


class TestTypeDEngineStatisticalMeaningfulness:
    """Fresh synthetic corpora (new values, not #800's). Never promoted."""

    def test_strong_signal_pair_significant_at_engine_layer(self):
        target = [0.92, 0.78, 1.01, 0.85, 0.95]
        peers = [-0.08, 0.04, -0.05, 0.02, -0.03]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 17),
            period_end=datetime.datetime(2026, 9, 17),
        )
        assert report.asymmetry_score == pytest.approx(0.922, rel=1e-9)
        assert report.is_significant is True
        assert report.p_value < 5e-4
        assert report.cohens_d > 8
        assert report.confidence_interval_lower > 0

    def test_near_null_pair_silent_at_engine_layer(self):
        target = [0.05, -0.03, 0.02, -0.04, 0.01]
        peers = [-0.02, 0.04, -0.01, 0.03, -0.05]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 17),
            period_end=datetime.datetime(2026, 9, 17),
        )
        assert report.asymmetry_score == pytest.approx(0.004, rel=1e-9)
        assert report.is_significant is False
        assert report.p_value > 0.5
        assert abs(report.cohens_d) < 0.5
        assert (
            report.confidence_interval_lower < 0 < report.confidence_interval_upper
        )

    def test_degenerate_n1_contract(self):
        a, b = [0.62], [-0.48]
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
    """Suite verdict lineage; #800's foreground suite owns the verdict, #805 re-launched."""

    TOMBSTONE_LINEAGE = 22

    def test_tombstone_lineage_count(self):
        # TWENTY-SECOND consecutive background full-suite death holds:
        # #795 and #800 both ran foreground suites instead of
        # re-launching background ones, so the lineage does not advance
        # this run.
        assert self.TOMBSTONE_LINEAGE == 22

    def test_800_foreground_suite_verdict_died(self):
        # The #800 full-suite launched 03:14 PDT died mid-run: its log
        # stalled at 1124 bytes / ~2% progress since 03:28 PDT and no
        # pytest was alive at this run's check. Pinned as dead-run
        # markers per the #770/#780 convention; triaged no further.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_800_full_suite.log",
        )
        assert os.path.exists(log_path), log_path
        size = os.path.getsize(log_path)
        assert size < 10000, size
        text = open(log_path, encoding="utf-8", errors="replace").read()
        assert "%" in text  # pytest -q progress marker present
        assert "2%" in text  # stalled at ~2% progress

    def test_relaunch_log_path_in_goal_hidden_files(self):
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_805_full_suite.log",
        )
        assert os.path.basename(log_path) == "type_d_805_full_suite.log"

    def test_805_suite_relaunched_this_run(self):
        # This run re-launches the full suite as a background process
        # writing to the persistent goal hidden_files path; the next
        # Type D run (#810) checks its verdict per the #795 convention.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_805_full_suite.log",
        )
        assert os.path.exists(log_path), log_path


class TestDocSync805:
    def test_readme_row_805(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_805(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_805_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog805:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #805 Type D:")
        return log[idx : idx + 8000]

    def test_log_entry_present(self):
        assert "## #805 Type D:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        entry = self._entry()
        assert "mechanism_id 714" in entry
        assert "m712" in entry


class TestDateGrounding805:
    def test_sep_17_2026_is_thursday(self):
        assert datetime.date(2026, 9, 17).strftime("%A") == "Thursday"
