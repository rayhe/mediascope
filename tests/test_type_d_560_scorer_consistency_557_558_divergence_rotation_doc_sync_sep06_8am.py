"""Type D #560 (2026-09-06 08:00 PDT): scorer cross-mechanism consistency
extended to #557/#558, SECOND engine-significance/finding-layer divergence
ratchet (#557 engine sig=True at p ~ 0.0047 while YAML holds significant:
false + NOT CALCULATED + empirical_required: true), #558 both-layers-agree
constancy boundary, #559 qualitative boundary, #556 monitoring boundary,
no-brittle sweep over 556-559 window, 555-559 rotation guard,
556-560 doc-sync ratchet (incl #556/#557/#558/#559 miss repair).

Context: the Aug 28 2026 standing rule says MANUAL ILLUSTRATIVE deltas are
NOT empirical - p_value NOT_CALCULATED, is_significant False in the mechanism
YAML, correlation not causation, no artifact-grade claims. The asymmetry
engine (calculate_asymmetry) computes t/p/CI on the logged arrays, and its
MEAN-DIFFERENCE arithmetic must reproduce the logged manual delta
(engine-drift detection). The engine's own significance output is computed
but deliberately NOT promoted to a finding for illustrative inputs - this
file pins that separation for the two newest quantitative mechanisms, and
extends the divergence ratchet in a NEW direction for #557:

- #557 (Type A, The Verge x Anthropic aspirational-register vs Meta deficit
  register, Sep 6 05:00 PDT): target Meta [-0.35, -0.30, -0.15] avg -0.2667
  vs peer Anthropic [0.25, 0.30, 0.10] avg 0.2167. The mechanism logs
  delta_manual_illustrative 0.4833 with delta_direction 'peer softer than
  target by 0.48' - the peer-minus-target framing, because the narrative is
  about the PEER's softness under a $0 direct financial tie (control case
  against financial determinism). The engine's target-minus-peer convention
  returns -0.4833, so the consistency check pins |engine delta| == logged
  0.4833 and the negative sign (target harsher). SECOND mechanism in the
  consistency suite where the engine's raw significance output (p ~ 0.0047,
  is_significant True) DIVERGES from the finding layer: the YAML still
  carries significant: false with p_value 'NOT CALCULATED no observed
  corpus' and empirical_required: true, because the inputs are synthetic
  illustrative scores. The standing rule holds even when the engine would
  claim significance - arithmetic layer vs finding layer separation, pinned
  deliberately, not an oversight. Joins #552 as the second divergence case;
  two independent divergence pins now bound this boundary.
- #558 (Type B, Tim Bradshaw FT business-register constancy, Sep 6 06:00
  PDT): Meta [0.10, 0.20, 0.05] avg 0.1167 vs non-Meta [-0.10, 0.20, -0.15]
  avg -0.0167, logged delta_meta_minus_non_meta 0.1333 (engine
  target-minus-peer: 0.13333). The OTHER boundary: engine and finding
  layers AGREE it is not significant (engine p ~ 0.35). Constancy/
  falsification finding - near-zero delta is the POINT (against
  journalist-level anti-Meta bias and against financial determinism),
  not a weak asymmetry.
- #559 (Type C, Amazon x NYT AI licensing deal, Sep 6 07:00 PDT):
  qualitative - no asymmetry_scorer section is logged
  (statistical_discipline carries tone_scores NOT_SCORED); scorer consistency
  explicitly does NOT apply, mirroring the #554/#549 boundary.
- #556 (Type E, podcast 34th verification, Sep 6 04:00 PDT):
  monitoring-only, no quantitative mechanism - no scorer extension.

Also: a no-brittle sweep - none of the 556-559 window files asserts the
brittle newest-first heading-equality pattern that Type D #555 repaired in
#551 (all four already use the presence-assertion convention); this pins the
convention against regression. PLUS a #558 novelty-test repair this run:
test_novelty_single_558_test_file asserted exactly one file with "558" in
its name, which the Type D filename convention (covered iteration numbers
embedded, per #555's 552_553 precedent) breaks - repaired to exclude
test_type_d_* cross-reference files, documented in both files. Rotation guard: the 555 D -> 556 E -> 557 A
-> 558 B -> 559 C window follows A->B->C->D->E->A adjacency in git-commit
order (newest first), closing the C->D edge this run. Doc-sync ratchet
extends the README/ARCHITECTURE per-file window to 556-560 with the
authoritative count_stats.py --check gate, including a doc_sync_miss_repair
for #556, #557, #558, #559 rows (missing before this run, in the #510/#555
repair convention).

Novelty: zero test_type_d_560 files on disk before this run (glob verified);
no #560 in git log (grep verified); scorer consistency has never covered
#557/#558 (repo grep for 557/558 in scorer-consistency test files returned
only their own mechanism files); the #557 divergence (second case) was never
pinned; the 555-559 rotation window was never guarded; the 551-555 doc-sync
window (from #555) is extended, not duplicated.
"""

from __future__ import annotations

import os
import re
import subprocess
from datetime import datetime
from pathlib import Path

import pytest
import yaml

from mediascope.score.asymmetry import calculate_asymmetry

REPO_ROOT = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TESTS_DIR = REPO_ROOT / "tests"
README = REPO_ROOT / "README.md"
ARCHITECTURE = REPO_ROOT / "docs" / "ARCHITECTURE.md"
LOG = REPO_ROOT / "iteration-log.md"
VENV_PYTHON = REPO_ROOT / ".venv" / "bin" / "python"

FILE_560 = ("test_type_d_560_scorer_consistency_557_558_divergence_"
            "rotation_doc_sync_sep06_8am.py")

PERIOD = (datetime(2026, 1, 1), datetime(2026, 8, 31))


def score(target, peer, target_entity, peers, slug):
    return calculate_asymmetry(
        target_scores=list(target),
        peer_scores=list(peer),
        target_entity=target_entity,
        peer_entities=list(peers),
        publication_slug=slug,
        period_start=PERIOD[0],
        period_end=PERIOD[1],
    )


def count_def_tests(test_file):
    """Static def-test count, same definition count_stats.count_tests uses."""
    with open(REPO_ROOT / "tests" / test_file) as f:
        content = f.read()
    return len(re.findall(r"^\s+def test_", content, re.MULTILINE))


# ---------------------------------------------------------------------------
# Iteration metadata
# ---------------------------------------------------------------------------


class TestIteration560Metadata:
    def test_docstring_ids(self):
        assert "Type D #560" in __doc__
        assert "2026-09-06 08:00 PDT" in __doc__

    def test_rotation_c_to_d(self):
        # Previous iteration #559 was Type C (commit 79f1de3); this run is D.
        assert "C->D" in __doc__.replace(" ", "") or "C -> D" in __doc__ or \
            "rotation" in __doc__.lower()

    def test_filename_convention(self):
        assert os.path.basename(__file__) == FILE_560
        assert FILE_560.startswith("test_type_d_560_")
        assert FILE_560.endswith("_sep06_8am.py")

    def test_iteration_log_entry_present(self):
        text = LOG.read_text(encoding="utf-8")
        assert re.search(r"^#560 Type D", text, re.MULTILINE), \
            "iteration-log.md missing newest-first #560 Type D heading"


# ---------------------------------------------------------------------------
# Scorer cross-mechanism consistency: engine mean-delta arithmetic reproduces
# the logged MANUAL ILLUSTRATIVE deltas for #557 and #558 (abs tolerance
# 1e-4, per #530 convention); #559 qualitative boundary pinned; #556
# monitoring boundary pinned.
# ---------------------------------------------------------------------------

# #557: engine convention is target-minus-peer. The mechanism frames the
# delta as peer-minus-target (peer softer), logging 0.4833 - so the engine
# must return -0.4833 and |delta| must match.
TARGET_557 = [-0.35, -0.30, -0.15]
PEER_557 = [0.25, 0.30, 0.10]

TARGET_558 = [0.10, 0.20, 0.05]
PEER_558 = [-0.10, 0.20, -0.15]


class TestScorerCrossMechanismConsistency560:
    def test_557_abs_delta_reproduced(self):
        r = score(TARGET_557, PEER_557, "Meta", ["Anthropic"], "the_verge")
        assert abs(r.asymmetry_score) == pytest.approx(0.4833, abs=1e-4)

    def test_557_engine_sign_is_target_minus_peer(self):
        # Engine convention: negative means the target (Meta) is harsher
        # than the peer (Anthropic) - consistent with the logged
        # delta_direction 'peer softer than target by 0.48'.
        r = score(TARGET_557, PEER_557, "Meta", ["Anthropic"], "the_verge")
        assert r.asymmetry_score == pytest.approx(-0.4833, abs=1e-4)
        assert r.asymmetry_score < 0

    def test_557_logged_avgs_match_engine(self):
        # YAML logs target_avg_manual_illustrative -0.2667 and
        # peer_avg_manual_illustrative 0.2167 (4-decimal rounded); the engine
        # inputs must byte-match the logged arrays, and engine avgs must
        # land inside the rounding window.
        r = score(TARGET_557, PEER_557, "Meta", ["Anthropic"], "the_verge")
        assert r.target_avg_tone == pytest.approx(-0.2667, abs=1e-4)
        assert r.peer_avg_tone == pytest.approx(0.2167, abs=1e-4)

    def test_557_logged_arrays_byte_match_engine_inputs(self):
        with open(REPO_ROOT / "profiles" / "the-verge.yaml") as f:
            d = yaml.safe_load(f)
        mech = d["competitor_relationships"]["anthropic"][
            "mechanism_557_verge_anthropic_aspirational_register_vs_meta_"
            "deficit_sep06"]["asymmetry_scoring_manual_illustrative"]
        assert mech["target_scores_manual_illustrative"] == pytest.approx(
            TARGET_557, abs=1e-9)
        assert mech["peer_scores_manual_illustrative"] == pytest.approx(
            PEER_557, abs=1e-9)
        assert mech["delta_manual_illustrative"] == pytest.approx(
            0.4833, abs=1e-4)
        assert mech["delta_direction"] == "peer softer than target by 0.48"

    def test_558_bradshaw_delta_reproduced(self):
        r = score(TARGET_558, PEER_558, "Meta", ["non_Meta"], "financial_times")
        assert r.asymmetry_score == pytest.approx(0.1333, abs=1e-4)

    def test_558_logged_avgs_match_engine(self):
        # YAML logs meta_avg 0.1167 and non_meta_avg -0.0167; engine inputs
        # byte-match the logged meta_scores / non_meta_scores arrays.
        r = score(TARGET_558, PEER_558, "Meta", ["non_Meta"], "financial_times")
        assert r.target_avg_tone == pytest.approx(0.1167, abs=1e-4)
        assert r.peer_avg_tone == pytest.approx(-0.0167, abs=1e-4)

    def test_558_logged_arrays_byte_match_engine_inputs(self):
        with open(REPO_ROOT / "profiles" / "financial-times.yaml") as f:
            d = yaml.safe_load(f)
        entry = [j for j in d["key_journalists"]
                 if j.get("name") == "Tim Bradshaw"][0]
        analysis = entry["cross_entity_coverage_analysis"]
        assert analysis["mechanism_id"] == 558
        s = analysis["scorer"]
        assert s["meta_scores"] == pytest.approx(TARGET_558, abs=1e-9)
        assert s["non_meta_scores"] == pytest.approx(PEER_558, abs=1e-9)
        assert s["delta_meta_minus_non_meta"] == pytest.approx(
            0.1333, abs=1e-4)

    def test_559_qualitative_no_tone_delta(self):
        # #559 is Type C qualitative mapping: scorer consistency does not
        # apply. The mechanism block must carry NO asymmetry_scorer section
        # and its statistical_discipline must keep tone_scores NOT_SCORED.
        with open(REPO_ROOT / "profiles" / "competitor-entities.yaml") as f:
            entities = yaml.safe_load(f)
        mech = entities["entities"]["amazon"][
            "mechanism_559_amazon_nyt_ai_licensing_deal"]
        assert not any(k.startswith("asymmetry_scorer") for k in mech), \
            "qualitative #559 must not log an asymmetry scorer section"
        disc = mech["statistical_discipline"]
        assert disc["p_value"] == "NOT_CALCULATED"
        assert disc["is_significant"] is False
        assert disc["tone_scores"] == "NOT_SCORED"

    def test_556_monitoring_no_scorer(self):
        # #556 is Type E podcast-sentiment monitoring: the log entry must
        # claim NO new asymmetry findings and must log no manual tone-delta
        # (no delta_manual_illustrative / delta_meta_minus_non_meta claims).
        # The mechanism file is the podcast-sentiment cycle test (44 def
        # tests of verification holds, not tone scoring).
        fname = ("test_type_e_556_podcast_sentiment_thirtyfourth_verification"
                 "_sep06_4am.py")
        assert (TESTS_DIR / fname).exists()
        block = LOG.read_text(encoding="utf-8")
        heading = re.search(r"^#556 Type E.*?(?=^#\d)", block,
                            re.MULTILINE | re.DOTALL)
        assert heading is not None
        entry = heading.group(0)
        assert "delta_manual_illustrative" not in entry
        assert "delta_meta_minus_non_meta" not in entry
        assert "no new asymmetry findings" in entry.lower()

    def test_557_and_558_deltas_directionally_distinct(self):
        # #557 (-0.4833, target-harsher asymmetry, peer softer under $0 tie)
        # and #558 (+0.1333, near-zero constancy falsification) are opposite
        # sign classes: one is an asymmetry observation, the other a
        # falsification of journalist-level anti-Meta bias. The suite must
        # not conflate them; #557's magnitude exceeds #558's by > 3.6x.
        r557 = score(TARGET_557, PEER_557, "Meta", ["Anthropic"], "the_verge")
        r558 = score(TARGET_558, PEER_558, "Meta", ["non_Meta"],
                     "financial_times")
        assert r557.asymmetry_score < 0 < r558.asymmetry_score
        assert abs(r557.asymmetry_score) > 3.6 * abs(r558.asymmetry_score)


# ---------------------------------------------------------------------------
# Standing-rule discipline ratchet, extended: #557 is the SECOND mechanism
# where the ENGINE's raw significance output diverges from the finding layer
# (engine p ~ 0.0047, is_significant True) while the YAML still carries
# significant: false with p_value NOT CALCULATED and empirical_required:
# true. #558 is the complementary boundary where both layers AGREE it is
# not significant (engine p ~ 0.35). The standing rule holds the finding
# layer in both cases - the separation is deliberate, not an oversight.
# ---------------------------------------------------------------------------

VERGE = REPO_ROOT / "profiles" / "the-verge.yaml"
FT = REPO_ROOT / "profiles" / "financial-times.yaml"
MECH_557 = ("mechanism_557_verge_anthropic_aspirational_register_vs_meta_"
            "deficit_sep06")


def _scorer_557():
    with open(VERGE) as f:
        d = yaml.safe_load(f)
    return d["competitor_relationships"]["anthropic"][MECH_557][
        "asymmetry_scoring_manual_illustrative"]


def _scorer_558():
    with open(FT) as f:
        d = yaml.safe_load(f)
    entry = [j for j in d["key_journalists"]
             if j.get("name") == "Tim Bradshaw"][0]
    return entry["cross_entity_coverage_analysis"]["scorer"]


class TestStandingRuleDisciplineRatchet560:
    def test_557_scorer_keeps_not_calculated(self):
        s = _scorer_557()
        assert "NOT CALCULATED" in str(s["p_value"])
        assert "NOT CALCULATED" in str(s["cohens_d"])
        assert "NOT CALCULATED" in str(s["ci_95"])
        assert s["significant"] is False
        assert s["empirical_required"] is True

    def test_557_engine_claims_significance_but_finding_does_not(self):
        # SECOND engine-significance/finding-layer divergence pin (first:
        # #552 in #555). The engine treats the synthetic illustrative
        # arrays as a real sample and claims significance; the finding
        # layer deliberately does not. Magic-number coupling caveat (per
        # #555): the 'is True' assertion is engine-implementation coupled,
        # but the 'is False' finding-layer assertion is rule-coupled and
        # must hold regardless of engine changes.
        r = score(TARGET_557, PEER_557, "Meta", ["Anthropic"], "the_verge")
        assert r.is_significant is True, \
            "engine currently claims significance on the illustrative pair"
        assert r.p_value < 0.01
        assert _scorer_557()["significant"] is False

    def test_558_both_layers_agree_not_significant(self):
        # The complementary boundary: engine p ~ 0.35, n.s. - the engine
        # and the finding layer agree. This pins the agreement pole so the
        # suite covers both divergence AND agreement.
        r = score(TARGET_558, PEER_558, "Meta", ["non_Meta"], "financial_times")
        assert r.is_significant is False
        assert r.p_value > 0.05
        assert _scorer_558()["is_significant"] is False

    def test_557_finding_label_present_in_yaml(self):
        s = _scorer_557()
        assert s["note"].startswith("MANUAL ILLUSTRATIVE")
        assert "not empirical" in s["note"]

    def test_558_finding_label_present_in_yaml(self):
        s = _scorer_558()
        assert s["method"] == "manual_illustrative"
        assert s["standing_rule"] == "Aug 28 2026"

    def test_557_558_yaml_parse_round_trip_stable(self):
        # Leaf-type assertions: the discipline keys must stay strings
        # where the convention says strings (NOT_CALCULATED is a plain
        # scalar string, not a YAML null) and booleans where booleans.
        s557 = _scorer_557()
        assert isinstance(s557["p_value"], str)
        assert isinstance(s557["significant"], bool)
        assert isinstance(s557["empirical_required"], bool)
        s558 = _scorer_558()
        assert isinstance(s558["p_value"], str)
        assert isinstance(s558["is_significant"], bool)


# ---------------------------------------------------------------------------
# No-brittle sweep: none of the 556-559 window files may carry the brittle
# newest-first heading-equality assertion that Type D #555 repaired in #551
# (all four already use the presence-assertion convention, per #495).
# ---------------------------------------------------------------------------

WINDOW_FILES_556_559 = [
    "test_type_e_556_podcast_sentiment_thirtyfourth_verification_sep06_4am.py",
    "test_type_a_557_verge_anthropic_aspirational_register_vs_meta_deficit_sep06_5am.py",
    "test_type_b_558_tim_bradshaw_ft_business_register_constancy_sep06.py",
    "test_type_c_559_amazon_nyt_ai_licensing_deal_sep06_7am.py",
]


class TestNoBrittleSweep560:
    @pytest.mark.parametrize("fname", WINDOW_FILES_556_559)
    def test_window_file_exists(self, fname):
        assert (TESTS_DIR / fname).exists()

    @pytest.mark.parametrize("fname", WINDOW_FILES_556_559)
    def test_no_brittle_newest_first_heading_equality(self, fname):
        content = (TESTS_DIR / fname).read_text(encoding="utf-8")
        # The brittle pattern: a def whose name says newest_first AND whose
        # body asserts the FIRST heading of the log is still this run's own
        # heading. Presence assertions (re.search for the entry) are fine.
        assert "def test_iteration_log_entry_newest_first" not in content, \
            f"{fname} regressed to the brittle newest-first assertion"

    def test_window_files_use_presence_convention(self):
        # Each window file must reference its own iteration entry (presence)
        # and must NOT read the log's first line or assert a brittle
        # first-line/newest-first equality. Styles differ across files
        # (#556 uses an anchored re.search, #557/#558 use substring
        # containment) - the sweep pins the ABSENT brittle pattern, not a
        # single presence style.
        for fname in WINDOW_FILES_556_559:
            content = (TESTS_DIR / fname).read_text(encoding="utf-8")
            assert ".readline()" not in content, \
                f"{fname} reads the log's first line (brittle)"
            assert "splitlines()[0]" not in content, \
                f"{fname} asserts on the log's first line (brittle)"
            num = re.search(r"_(\d{3})_", fname).group(1)
            assert f"#{num}" in content, \
                f"{fname} never references its own iteration entry"

    def test_558_novelty_repair_type_d_excluded(self):
        # Type D #560 repair of test_novelty_single_558_test_file: the
        # repair excludes test_type_d_* cross-reference files from the
        # '"558" in filename' uniqueness set (the Type D consistency
        # filename embeds covered iteration numbers by convention, per
        # #555's 552_553 precedent). Verify exactly the two expected files
        # exist and the repair comment is present in the owning file.
        fname_558 = ("test_type_b_558_tim_bradshaw_ft_business_register_"
                     "constancy_sep06.py")
        matches = [f for f in os.listdir(TESTS_DIR) if "558" in f]
        non_d = [f for f in matches if not f.startswith("test_type_d_")]
        assert matches == sorted([fname_558, FILE_560]) or \
            set(matches) == {fname_558, FILE_560}, \
            f"unexpected 558 file set: {matches}"
        assert non_d == [fname_558]
        content = (TESTS_DIR / fname_558).read_text(encoding="utf-8")
        assert "Novelty-repair (Type D #560" in content


# ---------------------------------------------------------------------------
# Rotation cycle guard: the 555 D -> 556 E -> 557 A -> 558 B -> 559 C window
# must follow A->B->C->D->E->A adjacency in git-commit order (newest first).
# This run closes the C->D edge by committing Type D.
# ---------------------------------------------------------------------------


class TestRotationCycleGuard560:
    # Rotation-window decay repair (Type D #565, Sep 6 2026 13:00 PDT):
    # the rotation guard pins the commit window as of the #560 commit
    # (8c179c9), NOT HEAD. A HEAD-relative assertion decays every hour as
    # new Type D runs push the window forward - the guard's intent is to
    # verify the rotation was valid AT THAT TIME, which is immutable. The
    # anchored form is the correct convention for all future Type D
    # rotation guards. The anchor is the PARENT of the #560 commit: at the
    # #560 run's test time the #560 commit did not exist yet, so the window
    # under test was the 5 commits BEFORE it (559-555).
    ANCHORED_COMMIT = "8c179c9~1"

    @staticmethod
    def _git_subjects(n=5):
        out = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "log", f"-n{n}",
             TestRotationCycleGuard560.ANCHORED_COMMIT, "--format=%s"],
            capture_output=True, text=True, check=True)
        return out.stdout.splitlines()

    def test_git_commit_order_matches_rotation(self):
        subjects = self._git_subjects()
        assert len(subjects) >= 5
        expected = [
            ("#559", "C"),
            ("#558", "B"),
            ("#557", "A"),
            ("#556", "E"),
            ("#555", "D"),
        ]
        for i, (num, typ) in enumerate(expected):
            assert num in subjects[i], \
                f"position {i}: expected {num}, got {subjects[i]!r}"
            assert re.search(rf"Type {typ} {re.escape(num)}", subjects[i]), \
                f"position {i}: expected Type {typ} {num}, got {subjects[i]!r}"

    def test_rotation_adjacency_cycle_valid(self):
        # C->D is the edge this run closes; the full 5-window must be a
        # rotation walk in commit-newest-first order: C,B,A,E,D (the
        # rotation runs backward in newest-first order). (order[a] -
        # order[b]) % 5 == 1 steps one position backward from the newer
        # commit a to the older commit b, i.e. one rotation step forward.
        types = ["C", "B", "A", "E", "D"]
        order = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        subjects = self._git_subjects()
        observed = []
        for s in subjects[:5]:
            m = re.search(r"Type ([A-E]) #(\d+)", s)
            assert m, f"unparseable rotation subject: {s!r}"
            observed.append(m.group(1))
        assert observed == types
        for a, b in zip(observed, observed[1:]):
            assert (order[a] - order[b]) % 5 == 1, \
                f"rotation broken: {a} -> {b} is not a valid cycle edge"

    def test_no_duplicate_iteration_numbers_in_window(self):
        subjects = self._git_subjects()
        nums = [re.search(r"#(\d+)", s).group(1) for s in subjects[:5]]
        assert len(set(nums)) == 5, f"duplicate iteration in window: {nums}"


# ---------------------------------------------------------------------------
# Doc-sync ratchet: README.md test table and docs/ARCHITECTURE.md test tree
# must carry rows for #556-#560 with authoritative def-test counts
# (miss repair for #556-#559 per the #510/#555 convention). count_stats.py
# --check is the authoritative gate.
# ---------------------------------------------------------------------------

DOC_SYNC = [
    # (iteration, test file, expected def-test count, README keyword, type)
    ("556", "test_type_e_556_podcast_sentiment_thirtyfourth_verification_sep06_4am.py", 44, "Type E #556", "Type E #556"),
    ("557", "test_type_a_557_verge_anthropic_aspirational_register_vs_meta_deficit_sep06_5am.py", 26, "Type A #557", "Type A #557"),
    ("558", "test_type_b_558_tim_bradshaw_ft_business_register_constancy_sep06.py", 24, "Type B #558", "Type B #558"),
    ("559", "test_type_c_559_amazon_nyt_ai_licensing_deal_sep06_7am.py", 34, "Type C #559", "Type C #559"),
]


class TestDocSyncRatchet560:
    @pytest.mark.parametrize("num,fname,expected,kw,_typ", DOC_SYNC)
    def test_readme_row_present(self, num, fname, expected, kw, _typ):
        text = README.read_text(encoding="utf-8")
        assert fname in text, f"README missing row for {fname}"
        assert kw in text, f"README missing {kw} keyword"

    @pytest.mark.parametrize("num,fname,expected,kw,_typ", DOC_SYNC)
    def test_readme_row_count_matches(self, num, fname, expected, kw, _typ):
        text = README.read_text(encoding="utf-8")
        line = [l for l in text.splitlines() if fname in l]
        assert line, f"README row not found for {fname}"
        assert str(expected) in line[0], \
            f"README row for {fname} lacks count {expected}"

    @pytest.mark.parametrize("num,fname,expected,kw,_typ", DOC_SYNC)
    def test_architecture_row_present(self, num, fname, expected, kw, _typ):
        text = ARCHITECTURE.read_text(encoding="utf-8")
        line = [l for l in text.splitlines() if fname in l]
        assert line, f"ARCHITECTURE missing row for {fname}"
        assert str(expected) in line[0], \
            f"ARCHITECTURE row for {fname} lacks count {expected}"

    def test_560_readme_row_present(self):
        text = README.read_text(encoding="utf-8")
        assert FILE_560 in text, "README missing row for the #560 file"
        assert "Type D #560" in text

    def test_560_architecture_row_present(self):
        text = ARCHITECTURE.read_text(encoding="utf-8")
        assert FILE_560 in text, "ARCHITECTURE missing row for the #560 file"
        assert "Type D #560" in text

    def test_560_readme_row_count_matches_actual(self):
        text = README.read_text(encoding="utf-8")
        actual = count_def_tests(FILE_560)
        line = [l for l in text.splitlines() if FILE_560 in l]
        assert line, f"README row not found for {FILE_560}"
        assert str(actual) in line[0], \
            f"README row for {FILE_560} lacks count {actual}"

    def test_count_stats_check_gate(self):
        out = subprocess.run(
            [str(VENV_PYTHON), str(REPO_ROOT / "scripts" / "count_stats.py"),
             "--check"],
            capture_output=True, text=True, check=False)
        assert out.returncode == 0, \
            f"count_stats.py --check failed:\n{out.stdout}\n{out.stderr}"

    def test_window_counts_are_authoritative(self):
        # The miss-repair counts written into the docs must equal the
        # static def-test counts (same definition count_stats uses).
        for num, fname, expected, kw, _typ in DOC_SYNC:
            assert count_def_tests(fname) == expected, \
                f"{fname}: expected {expected}, got {count_def_tests(fname)}"
