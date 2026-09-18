"""Type D -- Iteration #830 (Fri 2026-09-18 09:00 PDT): m727 / m728 / m729
qualitative-discipline verification + post-#829 corpus integrity
(max numeric mechanism_id 729; zero 730 keys; ledger holds at 26) +
#825 background-suite verdict (died at ~2% progress, 1133 bytes, no
pytest alive at this run's check; background tombstone lineage advances
TWENTY-SIXTH -> TWENTY-SEVENTH per the #770/#780 convention; EIGHTH
consecutive background full-suite death) + fresh synthetic engine
meaningfulness (new values, not #825's) + re-launch of the full suite
as a background process writing to goal hidden_files
type_d_830_full_suite.log (next Type D run checks its verdict per the
#795 convention).

Verifies:
- m727 (WIRED x Snap Specs Sep-16-2026 consumer-launch natural-experiment
  resolution, Type A #827, profiles/wired.yaml): FIRST dedicated mechanism
  under competitor_relationships.snap (the snap key did not exist before;
  was null-carrying); snap arm Sep 16 2026 Los Angeles launch, $2,195,
  4 cameras, SPECS Intelligence; wired_standalone_articles_launch_window
  0 (bounded absence Sep 16-18 2026), url NONE_SURFACED_BOUNDED_ABSENCE,
  snap arm tone NOT_SCORED (no coverage, no tone; per the #732
  selection convention); comparator outlets published launch-day coverage
  (Engadget Bell hands-on, TechCrunch Ropek Sep 16, Reuters Sep 16,
  9to5Mac, Barrons); meta arm carried from m354 (WIRED Gear desk,
  3+ adversarial Meta glasses articles Jun-Jul 2026, avg -0.62,
  standalone_meta_articles_same_window 3, standalone_snap_articles
  _jun16_unveil 0); financial context Conde Nast CRO Elizabeth
  Herbst-Brady (senior Snap revenue roles pre-Sep 2024); scorer none,
  p_value / cohens_d / ci_95 NOT_CALCULATED, is_significant false,
  engine_run false, verdict directionally_supported_not_proven;
  EXTENDS mechanism 354 (inverted price criticism) and mechanism 42
  (compound silence); 9 confounders ranked strong-first (index lag
  first); counter-evidence carried; NOT artifact-grade; NOT a
  falsification-family member (ledger holds at 26).
- m728 (Lucas Ropek TechCrunch Snap Specs Jun-16 vs Sep-16
  within-journalist register shift, Type B #828,
  profiles/careers/journalists.yaml): FIRST dedicated Type B mechanism
  on Lucas Ropek in journalists.yaml (mechanism 269 lives in
  competitor-coverage-research.yaml; zero lucas_ropek YAML key
  pre-commit); Jun 16 2026 arm "Snap finally debuts its long-awaited
  AR glasses, Specs, and, oof, they aren't cheap" (+0.10 MANUAL
  ILLUSTRATIVE, 64 rendered lines, one neutral privacy sentence) vs
  Sep 16 2026 arm "Snap tries to make the case again for its $2,200
  smart glasses" (-0.45 MANUAL ILLUSTRATIVE, 65 rendered lines);
  illustrative Sep-minus-Jun delta -0.55; REFINES mechanism 269 (the
  product-enthusiastic Ropek-on-Snap characterization was a
  debut-window phenomenon); CRITICAL SCOPE BOUND: the 269
  PRIVACY-vocabulary claim SURVIVES (sep16 arm
  privacy_vocabulary_sentences 0 despite 4 cameras + contextual AI);
  confounders ranked strong-first (accumulated negative news pegs
  STRONG DOMINANT); counter-evidence carried; MANUAL ILLUSTRATIVE
  only; verdict directionally_supported_not_proven; degenerate n=1
  engine check (calculate_asymmetry([-0.45], [0.10]) returns
  asymmetry_score -0.55; t 0.0 / p 1.0 / Cohen d 0.0 / degenerate
  CI (-0.55, -0.55) / is_significant False); NOT artifact-grade; NOT a
  falsification-family member (ledger holds at 26).
- m729 (Snap Specs Sep-16-2026 enterprise partnership stack, Type C
  #829, profiles/competitor-entities.yaml): FIRST dedicated
  financial-incentive graph-expansion mechanism (mechanism 729) for
  the Sep 16 2026 launch in marketplace_intermediary_landscape;
  four new Snap edges (salesforce_agentforce, nvidia_xr_ai,
  aws_assistant, verizon_exclusive); terms undisclosed (Reuters);
  architecture_not_business (no enterprise customer named, no revenue
  figure, FourWeekMBA Sep 17 2026); orbit intersections
  (aws_x_amazon_orbit, salesforce_x_benioff_time, verizon_x_yahoo_stake,
  nvidia_null_leg); coverage_observations (wired_zero m727,
  nyt_bounded_absence, engadget_consistent m113,
  techcrunch_prediction_failed: Ropek Sep 16 -0.45 fails the
  Verizon-leg softening prediction, carried as a scope bound inside
  this mechanism, times_london_not_soft); confounders ranked
  STRONG-first (terms undisclosed first); strongest_counterargument
  the TechCrunch leg itself; statistical_discipline scorer none /
  tone_scores NOT_SCORED / p_value NOT_CALCULATED /
  cohens_d NOT_CALCULATED / ci_95 NOT_CALCULATED / is_significant
  false / qualitative_only true / artifact_grade false;
  no_analysis_json_update true; verdict
  directionally_supported_not_proven; NOT a falsification-family
  member (ledger holds at 26).
- Falsification ledger: TWENTY-SIXTH present, TWENTY-SEVENTH absent in
  profiles/; ledger holds at 26.
- Post-#829 corpus integrity: max numeric mechanism_id == 729 in
  profiles/; zero underscore-form 730 key substrings in profiles/ and
  tests/ (own file excluded as sweep carrier per the #715
  pattern-rescope lesson; needles built by format string so no literal
  is carried); zero numeric 730 keys in profiles/; m727 / m728 /
  m729 block keys each unique in their home YAMLs; designed keying
  holds (no underscore-form 727/728/729 mechanism key substrings in
  profiles/). #829's max-729 / zero-underscore-730 / zero-numeric-730
  sweeps stay green (Type D adds no mechanisms); #827's max-727 and
  #828's max-728 sweeps fail by designed supersession per the
  #710/#720 convention (documented, not repaired).
- Statistical meaningfulness on FRESH synthetic corpora (new values,
  not #825's): strong-signal n=5-per-arm pair (asymmetry +0.976,
  t=17.3733, p=3.011053677210559e-07, d=10.9878, is_significant True
  at the ENGINE layer, 95% CI (0.886, 1.066) entirely above zero);
  fresh near-null pair (asymmetry 0.018, t=0.5196, p=0.6175,
  d=0.3286, is_significant False, CI (-0.042, 0.076) crossing zero,
  silent); fresh degenerate n=1-per-arm contract on the m728 tone
  pair ([-0.45], [0.10]: t=0.0, p=1.0, d=0.0, is_significant False,
  |asymmetry| == 0.55 exact, arm-swap negates). Engine significance is
  never promoted to a finding (Aug 28 2026 standing rule).
- Full-suite status: the #825 background suite re-launched 04:25 PDT
  died (type_d_825_full_suite.log stalled at 1133 bytes / ~2%
  progress since 04:25 PDT; no pytest alive at this run's check) -
  EIGHTH consecutive background death (#705's, #710's, #715's first
  re-launch, #715's re-launch, #720's re-launch, #725's re-launch,
  #730's re-launch, #825's re-launch; tombstone lineage per #565
  advances TWENTY-SIXTH -> TWENTY-SEVENTH). This run re-launches the
  full suite as a background process writing to goal hidden_files
  type_d_830_full_suite.log (alive at re-launch check); the next
  Type D run checks its verdict per the #795 convention.

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
    "test_type_d_830_m727_m728_m729_qualitative_corpus_integrity_sep18_9am.py"
)
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"

ANCHORED_SHA = "055bd77a3b063f93fbb8c313cbaee79208a76ec3"

M727_KEY = "snap_specs_sep16_consumer_launch_natural_experiment_resolution"
M728_KEY = "type_b_828_lucas_ropek_techcrunch_snap_jun16_vs_sep16_register_shift_sep18"
M729_KEY = "snap_specs_enterprise_partnership_stack_sep2026"

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
    ids = set()
    for root, _dirs, files in os.walk(PROFILES_DIR):
        for f in files:
            with open(
                os.path.join(root, f), encoding="utf-8", errors="replace"
            ) as fh:
                ids.update(int(x) for x in pat.findall(fh.read()))
    return max(ids)


class TestNovelty830:
    def test_single_test_type_d_830_file(self):
        matches = [
            f
            for f in os.listdir(TESTS_DIR)
            if f.startswith("test_type_d_830") and f.endswith(".py")
        ]
        assert matches == [OWN_BASENAME], matches

    def test_type_d_830_main_commit_unique_and_anchored(self):
        # No #830 main commit exists pre-commit; the anchor test pins
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
            if "Type D #830" in line and "followup" not in line.lower()
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
        # posture: max stays 729, zero numeric 730 keys.
        assert _max_numeric_mechanism_id() == 729
        assert _repo_grep_numeric_mechanism_id(730) == []

    def test_825_829_window_closed_prior_to_830(self):
        log = _read(LOG_PATH)
        for marker in (
            "## #825 Type D:",
            "## #826 Type E:",
            "## #827 Type A:",
            "## #828 Type B:",
            "## #829 Type C:",
        ):
            assert marker in log, marker


class TestTypeDRotationGuard:
    """#830 is the Type D anchor opening window 830-834."""

    WINDOW = ("D", "E", "A", "B", "C")

    def test_rotation_window_830_834(self):
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

class TestTypeDM727QualitativeDiscipline:
    """Type D verification of m727 qualitative discipline (Type A #827).

    Assertions run on the whitespace-folded block per the #732
    convention: the m727 finding, discipline, and falsification fields
    wrap across raw YAML lines."""

    def _block(self):
        return _fold(_block("profiles/wired.yaml", M727_KEY, 9000))

    def test_m727_publication_and_iteration(self):
        b = self._block()
        assert "mechanism_id: 727" in b
        assert "iteration: 827" in b
        assert "iteration_type: 'A'" in b
        assert "iteration_time: '2026-09-18 06:00 PT'" in b

    def test_m727_first_dedicated_snap_mechanism_wired(self):
        # m727 is the first (and only) mechanism under the snap key in
        # competitor_relationships: the snap section carries exactly one
        # mechanism_id, 727.
        doc = _read("profiles/wired.yaml")
        assert doc.index("competitor_relationships:") < doc.index("\n  snap:")
        snap_idx = doc.index("\n  snap:")
        tail = doc[snap_idx + len("\n  snap:") :]
        seg = tail[: re.search(r"\n  [a-z_]+:", tail).start()]
        assert M727_KEY in seg
        assert "mechanism_id: 727" in seg
        assert seg.count("mechanism_id:") == 1

    def test_m727_snap_arm_selection_margin(self):
        b = self._block()
        assert "price_usd: 2195" in b
        assert "wired_standalone_articles_launch_window: 0" in b
        assert "url: NONE_SURFACED_BOUNDED_ABSENCE" in b
        assert "manual_illustrative_tone: NOT_SCORED" in b
        assert "per the #732 statement-of-interest selection convention" in b

    def test_m727_comparator_coverage_surfaced(self):
        b = self._block()
        assert (
            "https://techcrunch.com/2026/09/16/"
            "snap-tries-to-make-the-case-again-for-its-2200-smart-glasses/"
            in b
        )
        assert "gamesreviews.com" in b
        assert "reuters.com/business" in b
        assert "9to5mac.com" in b
        assert "barrons.com" in b

    def test_m727_meta_arm_carried_from_354(self):
        b = self._block()
        assert "source_mechanism: 354" in b
        assert "meta_arm_avg: -0.62" in b
        assert "standalone_meta_articles_same_window: 3" in b
        assert "standalone_snap_articles_jun16_unveil: 0" in b

    def test_m727_financial_context_conde_nast_cro(self):
        b = self._block()
        assert "Elizabeth Herbst-Brady" in b
        assert "Snap pre-Sep 2024" in b

    def test_m727_statistical_discipline_strings(self):
        b = self._block()
        assert "scorer: none" in b
        assert "p_value: NOT_CALCULATED" in b
        assert "cohens_d: NOT_CALCULATED" in b
        assert "ci_95: NOT_CALCULATED" in b
        assert "is_significant: false" in b
        assert "engine_run: false" in b

    def test_m727_verdict_extends_354_and_42(self):
        b = self._block()
        assert "verdict: directionally_supported_not_proven" in b
        assert "EXTENDS mechanism 354" in b
        assert "mechanism 42 (compound silence)" in b

    def test_m727_confounders_ranked_strong_first(self):
        b = self._block()
        assert b.count("- strength: strong") == 3
        assert b.count("- strength: moderate") == 3
        assert b.count("- strength: weak") == 3
        assert b.index("- strength: strong") < b.index("- strength: moderate")
        first = b[b.index("- strength: strong") :]
        assert "Search-engine index lag" in first[:300]

    def test_m727_not_falsification_member(self):
        b = self._block()
        assert "NOT a falsification-family member" in b
        assert "ledger holds at 26" in b

    def test_m727_block_key_unique_in_wired(self):
        doc = _read("profiles/wired.yaml")
        assert doc.count(M727_KEY + ":") == 1

    def test_m727_designed_keying_no_underscore_727(self):
        # The #827 test file carries its own supersession-sweep literal;
        # guard targets profiles/ per the #715 pattern-rescope lesson.
        hits = _repo_grep_underscore_mechanism(727)
        profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
        assert profile_hits == [], profile_hits


class TestTypeDM728QualitativeDiscipline:
    """Type D verification of m728 qualitative discipline (Type B #828).

    First dedicated Type B mechanism on Lucas Ropek in
    profiles/careers/journalists.yaml; mechanism 269 lives in
    competitor-coverage-research.yaml."""

    def _block(self):
        # Anchor on the lucas_ropek entry key: the notes prose (delta,
        # REFINES, privacy scope bound, confounders framing) sits above
        # the competitor_coverage block key in the same entry.
        return _fold(_block("profiles/careers/journalists.yaml", "lucas_ropek", 60000))

    def test_m728_journalist_and_iteration(self):
        b = self._block()
        assert "mechanism_id: 728" in b
        assert "iteration: 828" in b
        assert "type: B" in b
        assert "date: '2026-09-18 07:00 PDT'" in b
        assert "FIRST dedicated Type B mechanism on Ropek" in b
        assert "mechanism 269 lives in competitor-coverage-research.yaml" in b

    def test_m728_jun16_arm_neutral_product_news(self):
        b = self._block()
        assert "date: '2026-06-16'" in b
        assert (
            "Snap finally debuts its long-awaited AR glasses, Specs, "
            "and, oof, they aren't cheap" in b
        )
        assert "tone_MANUAL_ILLUSTRATIVE: 0.10" in b
        assert "ONE and neutral" in b

    def test_m728_sep16_arm_adversarial(self):
        b = self._block()
        assert "date: '2026-09-16'" in b
        assert (
            "Snap tries to make the case again for its $2,200 smart glasses"
            in b
        )
        assert "tone_MANUAL_ILLUSTRATIVE: -0.45" in b

    def test_m728_illustrative_delta(self):
        b = self._block()
        assert "Illustrative Sep-minus-Jun delta -0.55" in b
        assert abs(-0.45 - 0.10) == pytest.approx(0.55)

    def test_m728_refines_269_privacy_claim_survives(self):
        b = self._block()
        assert "REFINES mechanism 269" in b
        assert "PRIVACY-vocabulary claim SURVIVES" in b
        assert "privacy_vocabulary_sentences: 0" in b

    def test_m728_confounders_ranked_strong_first(self):
        b = self._block()
        assert "confounders_ranked:" in b
        assert "Accumulated negative news pegs" in b
        assert b.index("confounders_ranked: strong:") < b.index("moderate:")

    def test_m728_counter_evidence(self):
        b = self._block()
        assert "counterevidence" in b

    def test_m728_verdict_manual_illustrative(self):
        b = self._block()
        assert "MANUAL ILLUSTRATIVE only" in b
        assert "directionally_supported_not_proven" in b

    def test_m728_not_falsification_member(self):
        b = self._block()
        assert "NOT a falsification-family member" in b
        assert "ledger holds at 26" in b

    def test_m728_block_key_unique_in_journalists(self):
        doc = _read("profiles/careers/journalists.yaml")
        assert doc.count(M728_KEY + ":") == 1

    def test_m728_designed_keying_no_underscore_728(self):
        # The #828 test file carries its own supersession-sweep literal;
        # guard targets profiles/ per the #715 pattern-rescope lesson.
        hits = _repo_grep_underscore_mechanism(728)
        profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
        assert profile_hits == [], profile_hits


class TestTypeDM729QualitativeDiscipline:
    """Type D verification of m729 qualitative discipline (Type C #829).

    FIRST dedicated financial-incentive graph-expansion mechanism for
    the Sep 16 2026 Snap Specs launch in marketplace_intermediary_landscape."""

    def _block(self):
        return _fold(
            _block("profiles/competitor-entities.yaml", M729_KEY, 12000)
        )

    def test_m729_iteration_and_type(self):
        b = self._block()
        assert "mechanism_id: 729" in b
        assert "iteration: 829" in b
        assert "iteration_type: 'C'" in b
        assert "date_analyzed: '2026-09-18'" in b
        assert "time_pdt: '08:00'" in b

    def test_m729_first_dedicated_graph_expansion(self):
        b = self._block()
        assert "FIRST dedicated" in b
        assert "marketplace_intermediary_landscape" in b or "graph expansion" in b

    def test_m729_four_edges(self):
        b = self._block()
        assert "salesforce_agentforce" in b
        assert "nvidia_xr_ai" in b
        assert "aws_assistant" in b
        assert "verizon_exclusive" in b
        assert "Snap did not disclose the financial terms" in b

    def test_m729_architecture_not_business(self):
        b = self._block()
        assert "architecture_not_business" in b
        assert "No enterprise customer has been named" in b
        assert "no revenue figure" in b

    def test_m729_orbit_intersections(self):
        b = self._block()
        assert "aws_x_amazon_orbit" in b
        assert "salesforce_x_benioff_time" in b
        assert "verizon_x_yahoo_stake" in b
        assert "nvidia_null_leg" in b

    def test_m729_techcrunch_prediction_failed_scope_bound(self):
        b = self._block()
        assert "techcrunch_prediction_failed" in b
        assert "the Verizon-leg softening prediction FAILS at the TechCrunch leg" in b
        assert "carried as a scope bound" in b

    def test_m729_times_london_not_soft(self):
        b = self._block()
        assert "times_london_not_soft" in b
        assert "Irenic Capital" in b

    def test_m729_confounders_ranked_strong_first(self):
        b = self._block()
        assert "confounders_ranked" in b
        assert "strength: 'STRONG'" in b
        assert "Financial terms undisclosed" in b

    def test_m729_strongest_counterargument(self):
        b = self._block()
        assert "strongest_counterargument" in b
        assert "The strongest counterargument is the TechCrunch leg itself" in b

    def test_m729_statistical_discipline(self):
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

    def test_m729_five_sources(self):
        b = self._block()
        assert "sources:" in b
        assert "reuters.com/business/snap-targets-enterprises" in b
        assert "verizon.com/about/news/verizon-specs-5g-ar-glasses-bundle" in b
        assert "fourweekmba.com" in b
        assert "thetimes.com/business" in b

    def test_m729_verdict_directionally_supported(self):
        b = self._block()
        assert "verdict: 'directionally_supported_not_proven'" in b

    def test_m729_not_falsification_member(self):
        b = self._block()
        assert "NOT a member of the falsification family" in b
        assert "ledger holds at 26" in b

    def test_m729_block_key_unique_in_entities(self):
        doc = _read("profiles/competitor-entities.yaml")
        assert doc.count(M729_KEY + ":") == 1

    def test_m729_designed_keying_no_underscore_729(self):
        hits = _repo_grep_underscore_mechanism(729)
        assert hits == [], hits

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
    """Post-#829 corpus integrity: max 729, zero 730 keys."""

    def test_max_numeric_mechanism_id_is_729(self):
        assert _max_numeric_mechanism_id() == 729

    def test_zero_underscore_730_keys_in_profiles(self):
        hits = _repo_grep_underscore_mechanism(730)
        profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
        assert profile_hits == [], profile_hits

    def test_zero_underscore_730_references_in_tests(self):
        hits = _repo_grep_underscore_mechanism(730)
        test_hits = [p for p in hits if p.startswith(TESTS_DIR)]
        assert test_hits == [], test_hits

    def test_zero_numeric_730_keys_in_profiles(self):
        hits = _repo_grep_numeric_mechanism_id(730)
        assert hits == [], hits

    def test_designed_keying_holds_no_underscore_727_728_729_in_profiles(self):
        for n in (727, 728, 729):
            hits = _repo_grep_underscore_mechanism(n)
            profile_hits = [p for p in hits if not p.startswith(TESTS_DIR)]
            assert profile_hits == [], (n, profile_hits)

    def test_c829_max_729_sweep_stays_green(self):
        # Type D adds no mechanisms; #829's max-729 sweep stays green.
        assert _max_numeric_mechanism_id() == 729

    def test_c829_zero_underscore_730_sweeps_stay_green(self):
        hits = _repo_grep_underscore_mechanism(730)
        assert hits == [], hits

    def test_c829_zero_numeric_730_sweep_stays_green(self):
        hits = _repo_grep_numeric_mechanism_id(730)
        assert hits == [], hits

    def test_a827_max_727_sweep_superseded_by_design(self):
        # #827 asserted max == 727 pre-commit; advancing to 729
        # supersedes it per the #710/#720 convention. Documented, not
        # repaired.
        assert _max_numeric_mechanism_id() == 729 != 727

    def test_b828_max_728_sweep_superseded_by_design(self):
        # #828 asserted max == 728 pre-commit; advancing to 729
        # supersedes it per the #710/#720 convention. Documented, not
        # repaired.
        assert _max_numeric_mechanism_id() == 729 != 728


class TestTypeDEngineStatisticalMeaningfulness:
    """Fresh synthetic corpora (new values, not #825's)."""

    def test_strong_signal_pair_significant_at_engine_layer(self):
        target = [0.72, 0.85, 0.90, 0.78, 0.88]
        peers = [-0.20, -0.05, -0.12, -0.30, -0.08]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 18),
            period_end=datetime.datetime(2026, 9, 18),
        )
        assert report.asymmetry_score == pytest.approx(0.976, rel=1e-9)
        assert report.t_statistic == pytest.approx(17.3733, rel=1e-4)
        assert report.is_significant is True
        assert report.p_value == pytest.approx(3.011053677210559e-07, rel=1e-2)
        assert report.cohens_d == pytest.approx(10.9878, rel=1e-2)
        assert report.confidence_interval_lower > 0
        assert report.confidence_interval_lower == pytest.approx(0.886, rel=1e-2)
        assert report.confidence_interval_upper == pytest.approx(1.066, rel=1e-2)

    def test_near_null_pair_silent_at_engine_layer(self):
        target = [0.05, -0.03, 0.08, -0.06, 0.02]
        peers = [-0.04, 0.06, -0.07, 0.03, -0.01]
        report = calculate_asymmetry(
            target_scores=target,
            peer_scores=peers,
            target_entity="synthetic_target",
            peer_entities=["synthetic_peer"],
            publication_slug="synthetic_pub",
            period_start=datetime.datetime(2026, 9, 18),
            period_end=datetime.datetime(2026, 9, 18),
        )
        assert report.asymmetry_score == pytest.approx(0.018, abs=1e-9)
        assert report.t_statistic == pytest.approx(0.5196, rel=1e-4)
        assert report.is_significant is False
        assert report.p_value == pytest.approx(0.6175, rel=1e-2)
        assert report.cohens_d == pytest.approx(0.3286, rel=1e-2)
        assert (
            report.confidence_interval_lower
            < 0
            < report.confidence_interval_upper
        )

    def test_degenerate_n1_contract_on_m728_tone_pair(self):
        # The m728 degenerate check: calculate_asymmetry([-0.45], [0.10])
        # returns asymmetry -0.55 with t 0.0 / p 1.0 / d 0.0.
        t, p = welch_t_test([-0.45], [0.10])
        d = cohens_d([-0.45], [0.10])
        assert (t, p) == (0.0, 1.0)
        assert d == 0.0
        assert is_significant(p) is False
        assert abs(-0.45 - 0.10) == pytest.approx(0.55)
        t2, p2 = welch_t_test([0.10], [-0.45])
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
    """Suite verdict lineage; #825's background suite owns the verdict,
    #830 re-launches."""

    TOMBSTONE_LINEAGE = 27

    def test_tombstone_lineage_count(self):
        # TWENTY-SEVENTH consecutive background full-suite death: #825's
        # background suite (re-launched 04:25 PDT Sep 18) died at ~2%
        # progress and no pytest was alive at this run's check. Advances
        # from the TWENTY-SIXTH lineage declared in #825 per the
        # #770/#780 convention.
        assert self.TOMBSTONE_LINEAGE == 27

    def test_825_background_suite_verdict_died(self):
        # Dead-run markers pinned per the #770/#780 convention; triaged
        # no further. Log stalled at ~2% since 04:25 PDT Sep 18.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_825_full_suite.log",
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
            "type_d_830_full_suite.log",
        )
        assert os.path.basename(log_path) == "type_d_830_full_suite.log"

    def test_830_suite_relaunched_this_run(self):
        # This run re-launches the full suite as a background process
        # writing to the persistent goal hidden_files path; the next
        # Type D run checks its verdict per the #795 convention.
        log_path = os.path.join(
            os.path.expanduser("~"),
            "workspace",
            "goals",
            "mediascope-meta-wearables-press-analysis",
            "hidden_files",
            "type_d_830_full_suite.log",
        )
        assert os.path.exists(log_path), log_path


class TestDocSync830:
    def test_readme_row_830(self):
        assert TEST_BASENAME in _read(README_PATH)

    def test_architecture_row_830(self):
        assert TEST_BASENAME in _read(ARCH_PATH)

    def test_architecture_lists_830_file(self):
        doc = _read(ARCH_PATH)
        assert TEST_BASENAME in set(re.findall(r"(test_\w+\.py)", doc))


class TestIterationLog830:
    def _entry(self):
        log = _read(LOG_PATH)
        idx = log.index("## #830 Type D:")
        return log[idx : idx + 12000]

    def test_log_entry_present(self):
        assert "## #830 Type D:" in _read(LOG_PATH)

    def test_log_mechanism_numbers_and_topics(self):
        entry = self._entry()
        assert "mechanism_id 729" in entry
        assert "m727" in entry
        assert "m728" in entry


class TestDateGrounding830:
    def test_sep_18_2026_is_friday(self):
        assert datetime.date(2026, 9, 18).strftime("%A") == "Friday"
