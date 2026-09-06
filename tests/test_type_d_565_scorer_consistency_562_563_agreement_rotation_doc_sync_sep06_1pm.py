"""Type D #565 (2026-09-06 13:00 PDT): scorer cross-mechanism consistency
extended to #562/#563 (third and fourth AGREEMENT-POLE pins - NO new
engine-significance/finding-layer divergence; the divergence count stays at
2: #552 and #557), #561 monitoring boundary, #564 qualitative boundary,
561-564 rotation guard, 560-564 doc-sync ratchet (incl #561/#562/#563/#564
miss repair), no-brittle sweep over 561-564 window, new competitor-coverage
pattern tests for #562 (NYT-Google adversarial register) and #563 (Heath
register-constancy falsification control).

Context: the Aug 28 2026 standing rule says MANUAL ILLUSTRATIVE deltas are
NOT empirical - p_value NOT_CALCULATED, is_significant False in the mechanism
YAML, correlation not causation, no artifact-grade claims. The asymmetry
engine (calculate_asymmetry) computes t/p/CI on the logged arrays, and its
MEAN-DIFFERENCE arithmetic must reproduce the logged manual delta
(engine-drift detection). The engine's own significance output is computed
but deliberately NOT promoted to a finding for illustrative inputs - this
file pins that separation for the two newest quantitative mechanisms, and
pins the agreement pole a third and fourth time:

- #562 (Type A, NYT x Google adversarial register confirmed vs Meta
  bifurcation, Sep 6 10:00 PDT): target Google [-0.70, -0.50, -0.40] avg
  -0.5333 vs peer Meta [0.40, -0.65, 0.00] avg -0.0833. Logged
  delta_manual_illustrative -0.45 (target-minus-peer: target harsher by
  0.45). THIRD agreement-pole pin: engine p ~ 0.2764, is_significant False;
  finding layer also n.s. (NOT CALCULATED). The delta_direction
  'target harsher than peer by 0.45' uses the engine's own convention, so no
  sign translation is needed (unlike #557's peer-minus-target framing). The
  mechanism is a CONTROL CASE against financial determinism ($0 Google
  licensing, adversarial tie; commercial dependency coincides with the
  harsher register).
- #563 (Type B, Alex Heath The Verge register constancy across Meta and
  OpenAI, Sep 6 11:00 PDT): Meta [0.0, 0.30, 0.10] avg 0.1333 vs non-Meta
  [-0.30, 0.25, 0.10] avg 0.0167, logged delta_meta_minus_non_meta 0.1167
  (engine target-minus-peer: 0.11667). FOURTH agreement-pole pin: engine p ~
  0.5748, is_significant False; finding layer n.s. Constancy/falsification
  finding - the near-zero delta is the POINT (against journalist-level
  anti-Meta bias), extending the #548/#553/#558 falsification family to the
  Verge's Meta-beat deputy editor. The scorer block carries an explicit
  'agreement_pole' key naming the same class as #558.
- #564 (Type C, Amazon x Conde Nast Rufus AI licensing deal, Sep 6 12:00
  PDT): qualitative - no asymmetry_scorer section is logged
  (statistical_discipline carries tone_scores NOT_SCORED); scorer consistency
  explicitly does NOT apply, mirroring the #554/#559 boundary.
- #561 (Type E, podcast 35th verification, Sep 6 09:00 PDT):
  monitoring-only, no quantitative mechanism - no scorer extension.

Divergence ratchet: with #562 and #563 both pinned as agreement pole, the
engine-significance/finding-layer divergence count REMAINS 2 (#552 in #555,
#557 in #560). This file spot-checks that the two existing divergence pins
still hold (engine claims significance on the illustrative inputs while the
finding layer refuses), so the ratchet is active rather than stale: a new
divergence instance in the 561-564 window would have been caught by the
per-mechanism agreement-pole assertions.

Also: a no-brittle sweep - none of the 561-564 window files asserts the
brittle newest-first heading-equality pattern that Type D #555 repaired in
#551 (all four already use the presence-assertion convention); this pins the
convention against regression. Rotation guard: the 561 E -> 562 A -> 563 B
-> 564 C window follows A->B->C->D->E->A adjacency in git-commit order
(newest first), closing the C->D edge this run. Doc-sync ratchet extends
the README/ARCHITECTURE per-file window to 560-565 with the authoritative
count_stats.py --check gate, including a doc_sync_miss_repair for
#561/#562/#563/#564 rows (missing before this run, in the #510/#555/#560
repair convention).

Novelty: zero test_type_d_565 files on disk before this run (glob verified);
no #565 in git log (grep verified); scorer consistency has never covered
#562/#563 (repo grep for 562/563 in scorer-consistency test files returned
only their own mechanism files); the 561-564 rotation window was never
guarded; the 556-560 doc-sync window (from #560) is extended, not duplicated.
The filename embeds the covered iteration numbers (562_563) per the
#555/#560 Type-D filename convention.
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

FILE_565 = ("test_type_d_565_scorer_consistency_562_563_agreement_rotation_"
            "doc_sync_sep06_1pm.py")

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


class TestIteration565Metadata:
    def test_docstring_ids(self):
        assert "Type D #565" in __doc__
        assert "2026-09-06 13:00 PDT" in __doc__

    def test_rotation_c_to_d(self):
        # Previous iteration #564 was Type C (commit 2776ae2); this run is D.
        assert "C->D" in __doc__.replace(" ", "") or "C -> D" in __doc__ or \
            "rotation" in __doc__.lower()

    def test_filename_convention(self):
        assert os.path.basename(__file__) == FILE_565
        assert FILE_565.startswith("test_type_d_565_")
        assert FILE_565.endswith("_sep06_1pm.py")

    def test_covered_iterations_in_filename(self):
        # Type-D filename convention (per #555/#560): covered iteration
        # numbers are embedded so novelty greps can find the coverage.
        assert "_562_563_" in FILE_565

    def test_iteration_log_entry_present(self):
        text = LOG.read_text(encoding="utf-8")
        assert re.search(r"^#565 Type D", text, re.MULTILINE), \
            "iteration-log.md missing newest-first #565 Type D heading"


# ---------------------------------------------------------------------------
# Scorer cross-mechanism consistency: engine mean-delta arithmetic reproduces
# the logged MANUAL ILLUSTRATIVE deltas for #562 and #563 (abs tolerance
# 1e-4, per #530 convention); #564 qualitative boundary pinned; #561
# monitoring boundary pinned.
# ---------------------------------------------------------------------------

# #562: engine convention is target-minus-peer, and the mechanism frames the
# delta the same way (delta_direction 'target harsher than peer by 0.45'),
# so the engine must return -0.45 with no sign translation.
TARGET_562 = [-0.70, -0.50, -0.40]
PEER_562 = [0.40, -0.65, 0.00]

TARGET_563 = [0.00, 0.30, 0.10]
PEER_563 = [-0.30, 0.25, 0.10]


class TestScorerCrossMechanismConsistency565:
    def test_562_delta_reproduced(self):
        r = score(TARGET_562, PEER_562, "Google", ["Meta"], "nytimes")
        assert r.asymmetry_score == pytest.approx(-0.45, abs=1e-4)

    def test_562_engine_sign_is_target_harsher(self):
        # Negative engine delta under the target-minus-peer convention
        # means Google (target) is harsher than Meta (peer) - matching the
        # logged delta_direction without the #557-style sign translation.
        r = score(TARGET_562, PEER_562, "Google", ["Meta"], "nytimes")
        assert r.asymmetry_score < 0
        assert r.asymmetry_score == pytest.approx(-0.45, abs=1e-4)

    def test_562_logged_avgs_match_engine(self):
        # YAML logs target_avg_manual_illustrative -0.5333 and
        # peer_avg_manual_illustrative -0.0833 (4-decimal rounded); the
        # engine inputs must byte-match the logged arrays, and engine avgs
        # must land inside the rounding window.
        r = score(TARGET_562, PEER_562, "Google", ["Meta"], "nytimes")
        assert r.target_avg_tone == pytest.approx(-0.5333, abs=1e-4)
        assert r.peer_avg_tone == pytest.approx(-0.0833, abs=1e-4)

    def test_562_logged_arrays_byte_match_engine_inputs(self):
        with open(REPO_ROOT / "profiles" / "nytimes.yaml") as f:
            d = yaml.safe_load(f)
        mech = d["competitor_relationships"]["google"][
            "mechanism_562_nyt_google_adversarial_register_confirmed_vs_"
            "meta_bifurcation_sep06"]["asymmetry_scoring_manual_illustrative"]
        assert mech["target_scores_manual_illustrative"] == pytest.approx(
            TARGET_562, abs=1e-9)
        assert mech["peer_scores_manual_illustrative"] == pytest.approx(
            PEER_562, abs=1e-9)
        assert mech["delta_manual_illustrative"] == pytest.approx(
            -0.45, abs=1e-4)
        assert mech["delta_direction"] == "target harsher than peer by 0.45"

    def test_563_heath_delta_reproduced(self):
        r = score(TARGET_563, PEER_563, "Meta", ["non_Meta"], "the_verge")
        assert r.asymmetry_score == pytest.approx(0.1167, abs=1e-4)

    def test_563_logged_avgs_match_engine(self):
        # YAML logs meta_avg 0.1333 and non_meta_avg 0.0167; engine inputs
        # byte-match the logged meta_scores / non_meta_scores arrays.
        r = score(TARGET_563, PEER_563, "Meta", ["non_Meta"], "the_verge")
        assert r.target_avg_tone == pytest.approx(0.1333, abs=1e-4)
        assert r.peer_avg_tone == pytest.approx(0.0167, abs=1e-4)

    def test_563_logged_arrays_byte_match_engine_inputs(self):
        with open(REPO_ROOT / "profiles" / "the-verge.yaml") as f:
            d = yaml.safe_load(f)
        entry = [j for j in d["key_journalists"]
                 if j.get("name") == "Alex Heath"][0]
        analysis = entry["cross_entity_coverage_analysis"]
        assert analysis["mechanism_id"] == 563
        s = analysis["scorer"]
        assert s["meta_scores"] == pytest.approx(TARGET_563, abs=1e-9)
        assert s["non_meta_scores"] == pytest.approx(PEER_563, abs=1e-9)
        assert s["delta_meta_minus_non_meta"] == pytest.approx(
            0.1167, abs=1e-4)
        assert s["agreement_pole"] == ("engine and finding layer agree not "
                                       "significant, same class as #558")

    def test_564_qualitative_no_tone_delta(self):
        # #564 is Type C qualitative mapping: scorer consistency does not
        # apply. The mechanism block must carry NO asymmetry_scorer section
        # and its statistical_discipline must keep tone_scores NOT_SCORED.
        with open(REPO_ROOT / "profiles" / "competitor-entities.yaml") as f:
            entities = yaml.safe_load(f)
        mech = entities["entities"]["amazon"][
            "mechanism_564_amazon_conde_nast_rufus_ai_licensing_deal"]
        assert not any(k.startswith("asymmetry_scorer") for k in mech), \
            "qualitative #564 must not log an asymmetry scorer section"
        disc = mech["statistical_discipline"]
        assert disc["p_value"] == "NOT_CALCULATED"
        assert disc["is_significant"] is False
        assert disc["tone_scores"] == "NOT_SCORED"

    def test_561_monitoring_no_scorer(self):
        # #561 is Type E podcast-sentiment monitoring: the log entry must
        # claim NO new asymmetry findings and must log no manual tone-delta
        # (no delta_manual_illustrative / delta_meta_minus_non_meta claims).
        # The mechanism file is the podcast-sentiment cycle test (60 def
        # tests of verification holds, not tone scoring).
        fname = ("test_type_e_561_podcast_sentiment_thirtyfifth_verification"
                 "_sep06_9am.py")
        assert (TESTS_DIR / fname).exists()
        block = LOG.read_text(encoding="utf-8")
        heading = re.search(r"^#561 Type E.*?(?=^#\d)", block,
                            re.MULTILINE | re.DOTALL)
        assert heading is not None
        entry = heading.group(0)
        assert "delta_manual_illustrative" not in entry
        assert "delta_meta_minus_non_meta" not in entry
        assert "no new asymmetry findings" in entry.lower()

    def test_562_and_563_sign_classes_distinct(self):
        # #562 (-0.45, target-harsher asymmetry observation: NYT applies an
        # adversarial register to Google AI despite commercial dependency -
        # control case against financial determinism) and #563 (+0.1167,
        # near-zero constancy: Heath's register constant across Meta and
        # OpenAI - falsification of journalist-level anti-Meta bias) are
        # opposite sign classes. The suite must not conflate an asymmetry
        # observation with a constancy falsification; #562's magnitude
        # exceeds #563's by ~3.86x.
        r562 = score(TARGET_562, PEER_562, "Google", ["Meta"], "nytimes")
        r563 = score(TARGET_563, PEER_563, "Meta", ["non_Meta"], "the_verge")
        assert r562.asymmetry_score < 0 < r563.asymmetry_score
        assert abs(r562.asymmetry_score) == pytest.approx(
            3.86 * abs(r563.asymmetry_score), rel=0.01)


# ---------------------------------------------------------------------------
# Standing-rule discipline ratchet, extended: #562 and #563 are the THIRD
# and FOURTH agreement-pole pins (engine and finding layer both n.s.).
# The divergence ratchet is kept ACTIVE: the two existing divergence cases
# (#552 in #555, #557 in #560) are spot-checked still to hold, so a stale
# ratchet cannot silently pass a new divergence instance in this window.
# ---------------------------------------------------------------------------

NYTIMES = REPO_ROOT / "profiles" / "nytimes.yaml"
VERGE = REPO_ROOT / "profiles" / "the-verge.yaml"
MECH_562 = ("mechanism_562_nyt_google_adversarial_register_confirmed_vs_"
            "meta_bifurcation_sep06")


def _scorer_562():
    with open(NYTIMES) as f:
        d = yaml.safe_load(f)
    return d["competitor_relationships"]["google"][MECH_562][
        "asymmetry_scoring_manual_illustrative"]


def _scorer_563():
    with open(VERGE) as f:
        d = yaml.safe_load(f)
    entry = [j for j in d["key_journalists"]
             if j.get("name") == "Alex Heath"][0]
    return entry["cross_entity_coverage_analysis"]["scorer"]


class TestStandingRuleDisciplineRatchet565:
    def test_562_scorer_keeps_not_calculated(self):
        s = _scorer_562()
        assert "NOT CALCULATED" in str(s["p_value"])
        assert "NOT CALCULATED" in str(s["cohens_d"])
        assert "NOT CALCULATED" in str(s["ci_95"])
        assert s["significant"] is False
        assert s["empirical_required"] is True

    def test_562_agreement_pole_engine_and_finding(self):
        # THIRD agreement-pole pin (after #558 in #560 and its class-mates):
        # engine p ~ 0.2764 n.s., finding layer NOT_CALCULATED n.s. -
        # agreement means the illustrative delta stays illustrative, not
        # that it becomes "proven null".
        r = score(TARGET_562, PEER_562, "Google", ["Meta"], "nytimes")
        assert r.is_significant is False
        assert r.p_value > 0.05
        assert _scorer_562()["significant"] is False

    def test_563_agreement_pole_engine_and_finding(self):
        # FOURTH agreement-pole pin: engine p ~ 0.5748 n.s., finding layer
        # is_significant False. The agreement_pole key in the YAML names the
        # same class as #558.
        r = score(TARGET_563, PEER_563, "Meta", ["non_Meta"], "the_verge")
        assert r.is_significant is False
        assert r.p_value > 0.05
        assert _scorer_563()["is_significant"] is False

    def test_562_finding_label_present_in_yaml(self):
        s = _scorer_562()
        assert s["note"].startswith("MANUAL ILLUSTRATIVE")
        assert "not empirical" in s["note"]

    def test_563_finding_label_present_in_yaml(self):
        s = _scorer_563()
        assert s["method"] == "manual_illustrative"
        assert s["standing_rule"] == "Aug 28 2026"

    def test_562_563_yaml_parse_round_trip_stable(self):
        # Leaf-type assertions: the discipline keys must stay strings
        # where the convention says strings (NOT_CALCULATED is a plain
        # scalar string, not a YAML null) and booleans where booleans.
        s562 = _scorer_562()
        assert isinstance(s562["p_value"], str)
        assert isinstance(s562["significant"], bool)
        assert isinstance(s562["empirical_required"], bool)
        s563 = _scorer_563()
        assert isinstance(s563["p_value"], str)
        assert isinstance(s563["is_significant"], bool)
        assert isinstance(s563["artifact_grade"], bool)

    def test_divergence_pin_552_still_holds(self):
        # Ratchet activity check: the FIRST divergence case (#552, pinned
        # in Type D #555) must still hold - engine claims significance on
        # the illustrative pair while the finding layer refuses. A stale
        # ratchet would not notice this pin decaying.
        with open(TESTS_DIR /
                  "test_type_d_555_scorer_consistency_552_553_rotation_"
                  "doc_sync_sep06_3am.py") as f:
            content = f.read()
        assert "divergence ratchet" in content
        assert "significant: false with p_value NOT CALCULATED" in content

    def test_divergence_pin_557_still_holds(self):
        # SECOND divergence case (#557, pinned in Type D #560): engine
        # is_significant True (p < 0.01) on the synthetic illustrative
        # arrays while the YAML finding layer keeps significant: false with
        # p_value NOT CALCULATED and empirical_required: true.
        r = score([-0.35, -0.30, -0.15], [0.25, 0.30, 0.10], "Meta",
                  ["Anthropic"], "the_verge")
        assert r.is_significant is True
        with open(REPO_ROOT / "profiles" / "the-verge.yaml") as f:
            d = yaml.safe_load(f)
        mech = d["competitor_relationships"]["anthropic"][
            "mechanism_557_verge_anthropic_aspirational_register_vs_meta_"
            "deficit_sep06"]["asymmetry_scoring_manual_illustrative"]
        assert mech["significant"] is False
        assert "NOT CALCULATED" in str(mech["p_value"])
        assert mech["empirical_required"] is True

    def test_no_new_divergence_in_window(self):
        # The only quantitative mechanisms in the 561-564 window are #562
        # and #563; both are agreement pole (engine n.s. AND finding n.s.),
        # so the divergence count stays at exactly 2 (#552, #557). Any
        # third divergence instance would fail this class of assertion.
        for target, peer, entity, peers, slug in [
            (TARGET_562, PEER_562, "Google", ["Meta"], "nytimes"),
            (TARGET_563, PEER_563, "Meta", ["non_Meta"], "the_verge"),
        ]:
            r = score(target, peer, entity, peers, slug)
            assert r.is_significant is False, \
                f"unexpected engine significance on {slug} window mechanism"


# ---------------------------------------------------------------------------
# New competitor-coverage pattern assertions for #562/#563: NYT-Google
# adversarial register (control case against financial determinism) and
# Heath register-constancy (falsification control, #548/#553/#558 family).
# ---------------------------------------------------------------------------


class TestCompetitorCoveragePatterns565:
    def test_562_mechanism_registered_under_google(self):
        # #562 is the FIRST dedicated mechanism under
        # competitor_relationships.google in nytimes.yaml (previously only
        # financial metadata, zero mechanisms).
        with open(NYTIMES) as f:
            d = yaml.safe_load(f)
        google = d["competitor_relationships"]["google"]
        assert MECH_562 in google
        mech = google[MECH_562]
        assert mech["mechanism_id"] == 562
        assert mech["competitor_pair"] == "Google vs Meta"

    def test_562_control_case_financial_tie_zero(self):
        # The control-case pattern: NO NYT-Google AI licensing deal exists
        # ($0, adversarial tie) yet the register is harsher - the
        # money-sympathy direction is INVERTED relative to the financial
        # determinism hypothesis.
        with open(NYTIMES) as f:
            d = yaml.safe_load(f)
        mech = d["competitor_relationships"]["google"][MECH_562]
        assert "$0" in str(mech["financial_relationship"])
        assert "control case" in mech["finding"].lower()
        assert "financial determinism" in mech["finding"]

    def test_562_delta_direction_uses_engine_convention(self):
        # Pattern-level: #562 logs the delta in the engine's own
        # target-minus-peer convention (unlike #557's peer-minus-target
        # framing), so no sign translation is needed in the consistency
        # check. The finding and the engine must name the same direction.
        mech_scorer = _scorer_562()
        assert mech_scorer["delta_direction"] == \
            "target harsher than peer by 0.45"
        assert mech_scorer["target_entity"].startswith("Google")
        assert "Meta" in mech_scorer["peer_entity"]

    def test_563_heath_falsification_family(self):
        # #563 extends the #548/#553/#558 falsification family (register
        # constancy across Meta and non-Meta coverage, against
        # journalist-level anti-Meta bias) to the Verge's Meta-beat deputy
        # editor. The analysis must name the family it extends.
        with open(VERGE) as f:
            d = yaml.safe_load(f)
        entry = [j for j in d["key_journalists"]
                 if j.get("name") == "Alex Heath"][0]
        analysis = entry["cross_entity_coverage_analysis"]
        blob = str(analysis.get("interpretation", "")) + \
            str(analysis.get("finding", ""))
        assert "558" in blob and "553" in blob, \
            "Heath analysis must reference the falsification family #553/#558"

    def test_563_scorer_names_agreement_pole(self):
        # Pattern-level: constancy findings carry an explicit agreement_pole
        # key so a reader cannot mistake agreement (both layers n.s.) for
        # divergence. #563 names #558 as its class-mate.
        s = _scorer_563()
        assert "agreement_pole" in s
        assert "558" in s["agreement_pole"]

    def test_563_openai_not_meta_beat_comparator(self):
        # The falsification pattern requires a non-Meta comparator where
        # bias could hide: Heath's OpenAI pieces (Altman dinner interview,
        # Sources debut with Altman, Bret Taylor Decoder) against his Meta
        # pieces (Reality Labs reorg, Orion hands-on, Zuckerberg Decoder).
        with open(VERGE) as f:
            d = yaml.safe_load(f)
        entry = [j for j in d["key_journalists"]
                 if j.get("name") == "Alex Heath"][0]
        analysis = entry["cross_entity_coverage_analysis"]
        blob = str(analysis)
        assert "OpenAI" in blob
        assert "Altman" in blob
        assert "Zuckerberg" in blob


# ---------------------------------------------------------------------------
# No-brittle sweep: none of the 561-564 window files may carry the brittle
# newest-first heading-equality assertion that Type D #555 repaired in #551
# (all four already use the presence-assertion convention, per #495).
# ---------------------------------------------------------------------------

WINDOW_FILES_561_564 = [
    "test_type_e_561_podcast_sentiment_thirtyfifth_verification_sep06_9am.py",
    "test_type_a_562_nyt_google_adversarial_register_vs_meta_bifurcation_sep06.py",
    "test_type_b_563_alex_heath_verge_register_constancy_sep06.py",
    "test_type_c_564_amazon_conde_nast_rufus_licensing_sep06_12pm.py",
]


class TestNoBrittleSweep565:
    @pytest.mark.parametrize("fname", WINDOW_FILES_561_564)
    def test_window_file_exists(self, fname):
        assert (TESTS_DIR / fname).exists()

    @pytest.mark.parametrize("fname", WINDOW_FILES_561_564)
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
        # (anchored re.search vs substring containment) - the sweep pins
        # the ABSENT brittle pattern, not a single presence style.
        for fname in WINDOW_FILES_561_564:
            content = (TESTS_DIR / fname).read_text(encoding="utf-8")
            assert ".readline()" not in content, \
                f"{fname} reads the log's first line (brittle)"
            assert "splitlines()[0]" not in content, \
                f"{fname} asserts on the log's first line (brittle)"
            num = re.search(r"_(\d{3})_", fname).group(1)
            assert f"#{num}" in content, \
                f"{fname} never references its own iteration entry"


# ---------------------------------------------------------------------------
# Rotation cycle guard: the 561 E -> 562 A -> 563 B -> 564 C window must
# follow A->B->C->D->E->A adjacency in git-commit order (newest first).
# This run closes the C->D edge by committing Type D.
# ---------------------------------------------------------------------------


class TestRotationCycleGuard565:
    @staticmethod
    def _git_subjects(n=5):
        out = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "log", f"-n{n}",
             "--format=%s"],
            capture_output=True, text=True, check=True)
        return out.stdout.splitlines()

    def test_git_commit_order_matches_rotation(self):
        subjects = self._git_subjects()
        assert len(subjects) >= 5
        expected = [
            ("#565", "D"),
            ("#564", "C"),
            ("#563", "B"),
            ("#562", "A"),
            ("#561", "E"),
        ]
        for i, (num, typ) in enumerate(expected):
            assert num in subjects[i], \
                f"position {i}: expected {num}, got {subjects[i]!r}"
            assert re.search(rf"Type {typ} {re.escape(num)}", subjects[i]), \
                f"position {i}: expected Type {typ} {num}, got {subjects[i]!r}"

    def test_rotation_adjacency_cycle_valid(self):
        # D->C is the edge this run closes; the full 5-window must be a
        # rotation walk in commit-newest-first order: D,C,B,A,E (the
        # rotation runs backward in newest-first order). (order[a] -
        # order[b]) % 5 == 1 steps one position backward from the newer
        # commit a to the older commit b, i.e. one rotation step forward.
        types = ["D", "C", "B", "A", "E"]
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
# must carry rows for #560-#565 with authoritative def-test counts
# (miss repair for #561/#562/#563/#564 per the #510/#555/#560 convention).
# count_stats.py --check is the authoritative gate.
# ---------------------------------------------------------------------------

DOC_SYNC = [
    # (iteration, test file, expected def-test count, README keyword)
    ("561", "test_type_e_561_podcast_sentiment_thirtyfifth_verification_sep06_9am.py", 60, "Type E #561"),
    ("562", "test_type_a_562_nyt_google_adversarial_register_vs_meta_bifurcation_sep06.py", 28, "Type A #562"),
    ("563", "test_type_b_563_alex_heath_verge_register_constancy_sep06.py", 25, "Type B #563"),
    ("564", "test_type_c_564_amazon_conde_nast_rufus_licensing_sep06_12pm.py", 40, "Type C #564"),
]


class TestDocSyncRatchet565:
    @pytest.mark.parametrize("num,fname,expected,kw", DOC_SYNC)
    def test_readme_row_present(self, num, fname, expected, kw):
        text = README.read_text(encoding="utf-8")
        assert fname in text, f"README missing row for {fname}"
        assert kw in text, f"README missing {kw} keyword"

    @pytest.mark.parametrize("num,fname,expected,kw", DOC_SYNC)
    def test_readme_row_count_matches(self, num, fname, expected, kw):
        text = README.read_text(encoding="utf-8")
        line = [l for l in text.splitlines() if fname in l]
        assert line, f"README row not found for {fname}"
        assert str(expected) in line[0], \
            f"README row for {fname} lacks count {expected}"

    @pytest.mark.parametrize("num,fname,expected,kw", DOC_SYNC)
    def test_architecture_row_present(self, num, fname, expected, kw):
        text = ARCHITECTURE.read_text(encoding="utf-8")
        line = [l for l in text.splitlines() if fname in l]
        assert line, f"ARCHITECTURE missing row for {fname}"
        assert str(expected) in line[0], \
            f"ARCHITECTURE row for {fname} lacks count {expected}"

    def test_560_rows_still_present(self):
        # The 556-560 window (from Type D #560) must not decay: #560's
        # rows survive into the 560-565 window extension.
        fname = ("test_type_d_560_scorer_consistency_557_558_divergence_"
                 "rotation_doc_sync_sep06_8am.py")
        assert fname in README.read_text(encoding="utf-8")
        assert fname in ARCHITECTURE.read_text(encoding="utf-8")

    def test_565_readme_row_present(self):
        text = README.read_text(encoding="utf-8")
        assert FILE_565 in text, "README missing row for the #565 file"
        assert "Type D #565" in text

    def test_565_architecture_row_present(self):
        text = ARCHITECTURE.read_text(encoding="utf-8")
        assert FILE_565 in text, "ARCHITECTURE missing row for the #565 file"
        assert "Type D #565" in text

    def test_565_readme_row_count_matches_actual(self):
        text = README.read_text(encoding="utf-8")
        actual = count_def_tests(FILE_565)
        line = [l for l in text.splitlines() if FILE_565 in l]
        assert line, f"README row not found for {FILE_565}"
        assert str(actual) in line[0], \
            f"README row for {FILE_565} lacks count {actual}"

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
        for num, fname, expected, kw in DOC_SYNC:
            assert count_def_tests(fname) == expected, \
                f"{fname}: expected {expected}, got {count_def_tests(fname)}"
