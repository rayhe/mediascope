"""Type D #555 (2026-09-06 03:00 PDT): scorer cross-mechanism consistency
extended to #552/#553, standing-rule divergence ratchet (engine significance
NOT promoted), #551 brittle-assertion repair, 551-554 rotation guard,
551-555 doc-sync ratchet.

Context: the Aug 28 2026 standing rule says MANUAL ILLUSTRATIVE deltas are
NOT empirical - p_value NOT_CALCULATED, is_significant False in the mechanism
YAML, correlation not causation, no artifact-grade claims. The asymmetry
engine (calculate_asymmetry) computes t/p/CI on the logged arrays, and its
MEAN-DIFFERENCE arithmetic must reproduce the logged manual delta
(engine-drift detection). The engine's own significance output is computed
but deliberately NOT promoted to a finding for illustrative inputs - this
file pins that separation for the two newest quantitative mechanisms, and
extends it in a NEW direction for #552:

- #552 (Type A, FT x Anthropic surveillance-refusal register inversion, Sep
  6 00:00 PDT): target Meta [-0.62, -0.58] avg -0.6 vs peer Anthropic
  [0.22, 0.15, 0.12] avg 0.1633. The mechanism logs delta_manual_illustrative
  0.7633 with delta_direction 'peer softer than target by 0.76' - the
  peer-minus-target framing, because the narrative is about the PEER's
  softness. The engine's target-minus-peer convention returns -0.7633, so
  the consistency check pins |engine delta| == logged 0.7633 and the
  negative sign (target harsher). This is the first mechanism in the
  consistency suite where the engine's raw significance output (p ~ 0.00023,
  is_significant True) DIVERGES from the finding layer: the YAML still
  carries significant: false with p_value 'NOT CALCULATED no observed
  corpus' and empirical_required: true, because the inputs are synthetic
  illustrative scores. The standing rule holds even when the engine would
  claim significance - arithmetic layer vs finding layer separation.
- #553 (Type B, Haskins WIRED surveillance-register constancy, Sep 6
  01:00 PDT): Meta [-0.80, -0.35, -0.25] avg -0.467 vs non-Meta
  [-0.65, -0.60, -0.45] avg -0.567, logged delta_meta_minus_non_meta 0.10
  (engine target-minus-peer: 0.10000000000000003). Constancy/falsification
  finding - near-zero delta is the POINT, not a weak asymmetry.
- #554 (Type C, Mistral x AFP wire-service licensing, Sep 6 02:00 PDT):
  qualitative - no asymmetry_scorer section is logged
  (statistical_discipline carries tone_scores NOT_SCORED); scorer consistency
  explicitly does NOT apply, mirroring the #549 boundary pinned in #550.
- #551 (Type E, podcast 33rd verification, Sep 5 23:00 PDT):
  monitoring-only, no quantitative mechanism - no scorer extension.

Also: a #551 brittle-assertion repair - its test_iteration_log_entry_newest_first
asserted the newest-first heading is still #551, which breaks every hour as new
entries are prepended (falsy at this run: first heading is #554). Repaired to
assert presence of the #551 entry, following the #495 brittle-repair convention.

Rotation guard: the 551 E -> 552 A -> 553 B -> 554 C window follows
A->B->C->D->E->A adjacency in git-commit order (newest first), extending #550's
546-549 window guard; and the doc-sync ratchet extends the README/ARCHITECTURE
per-file window to 551-555 with the authoritative count_stats.py --check gate,
including a doc_sync_miss_repair for #552 and #553 rows (missing before this
run, in the #510 repair convention).

Novelty: zero test_type_d_555 files on disk before this run (glob verified);
no #555 in git log (grep verified); scorer consistency has never covered
#552/#553 (repo grep for 552/553 in scorer-consistency test files returned
only their own mechanism files); the 551-554 rotation window was never
guarded; the 546-550 doc-sync window (from #550) is extended, not duplicated.
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

FILE_555 = ("test_type_d_555_scorer_consistency_552_553_rotation_doc_sync"
            "_sep06_3am.py")

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


class TestIteration555Metadata:
    def test_docstring_ids(self):
        assert "Type D #555" in __doc__
        assert "2026-09-06 03:00 PDT" in __doc__

    def test_rotation_c_to_d(self):
        # Previous iteration #554 was Type C (commit 0f2ac52); this run is D.
        assert "C->D" in __doc__.replace(" ", "") or "C -> D" in __doc__ or \
            "rotation" in __doc__.lower()

    def test_filename_convention(self):
        assert os.path.basename(__file__) == FILE_555
        assert FILE_555.startswith("test_type_d_555_")
        assert FILE_555.endswith("_sep06_3am.py")

    def test_iteration_log_entry_present(self):
        text = LOG.read_text(encoding="utf-8")
        assert re.search(r"^#555 Type D", text, re.MULTILINE), \
            "iteration-log.md missing newest-first #555 Type D heading"


# ---------------------------------------------------------------------------
# Scorer cross-mechanism consistency: engine mean-delta arithmetic reproduces
# the logged MANUAL ILLUSTRATIVE deltas for #552 and #553 (abs tolerance
# 1e-4, per #530 convention); #554 qualitative boundary pinned.
# ---------------------------------------------------------------------------

# #552: engine convention is target-minus-peer. The mechanism frames the
# delta as peer-minus-target (peer softer), logging 0.7633 - so the engine
# must return -0.7633 and |delta| must match.
TARGET_552 = [-0.62, -0.58]
PEER_552 = [0.22, 0.15, 0.12]

TARGET_553 = [-0.80, -0.35, -0.25]
PEER_553 = [-0.65, -0.60, -0.45]


class TestScorerCrossMechanismConsistency555:
    def test_552_abs_delta_reproduced(self):
        r = score(TARGET_552, PEER_552, "Meta", ["Anthropic"],
                  "financial_times")
        assert abs(r.asymmetry_score) == pytest.approx(0.7633, abs=1e-4)

    def test_552_engine_sign_is_target_minus_peer(self):
        # Engine convention: negative means the target (Meta) is harsher
        # than the peer (Anthropic) - consistent with the logged
        # delta_direction 'peer softer than target by 0.76'.
        r = score(TARGET_552, PEER_552, "Meta", ["Anthropic"],
                  "financial_times")
        assert r.asymmetry_score == pytest.approx(-0.7633, abs=1e-4)
        assert r.asymmetry_score < 0

    def test_552_logged_avgs_match_engine(self):
        r = score(TARGET_552, PEER_552, "Meta", ["Anthropic"],
                  "financial_times")
        assert r.target_avg_tone == pytest.approx(-0.6, abs=1e-9)
        assert r.peer_avg_tone == pytest.approx(0.1633, abs=1e-4)

    def test_552_second_positive_magnitude_sign_pair_in_suite(self):
        # #547 was the first POSITIVE-sign target-minus-peer delta (+0.923,
        # target Google softer). #552 is the mirror: target-minus-peer
        # NEGATIVE (-0.7633, target Meta harsher). The suite now covers
        # both sign directions at comparable magnitude (0.76 vs 0.92).
        r = score(TARGET_552, PEER_552, "Meta", ["Anthropic"],
                  "financial_times")
        assert r.asymmetry_score < 0
        assert abs(r.asymmetry_score) > 0.75

    def test_553_haskins_delta_reproduced(self):
        r = score(TARGET_553, PEER_553, "Meta",
                  ["non_Meta_surveillance_targets"], "wired")
        assert r.asymmetry_score == pytest.approx(0.10, abs=1e-4)

    def test_553_logged_rounded_delta_within_rounding(self):
        # YAML logs delta_meta_minus_non_meta 0.10; engine computes
        # 0.10000000000000003 - byte-compatible at 1e-4.
        r = score(TARGET_553, PEER_553, "Meta",
                  ["non_Meta_surveillance_targets"], "wired")
        assert abs(r.asymmetry_score - 0.10) < 1e-4

    def test_553_near_zero_delta_not_significant(self):
        # The constancy finding's near-zero delta is the POINT
        # (falsification of reporter-level anti-Meta bias), not a weak
        # asymmetry; both layers agree it is not distinguishable from zero.
        r = score(TARGET_553, PEER_553, "Meta",
                  ["non_Meta_surveillance_targets"], "wired")
        assert r.is_significant is False

    def test_554_qualitative_no_tone_delta(self):
        # #554 is Type C qualitative mapping: scorer consistency does not
        # apply. The mechanism block must carry NO asymmetry_scorer section
        # and its statistical_discipline must keep tone_scores NOT_SCORED.
        with open(REPO_ROOT / "profiles" / "competitor-entities.yaml") as f:
            entities = yaml.safe_load(f)
        mech = entities["entities"]["mistral"][
            "mechanism_554_mistral_afp_wire_service_licensing"]
        assert not any(k.startswith("asymmetry_scorer") for k in mech), \
            "qualitative #554 must not log an asymmetry scorer section"
        disc = mech["statistical_discipline"]
        assert disc["p_value"] == "NOT_CALCULATED"
        assert disc["is_significant"] is False
        assert disc["tone_scores"] == "NOT_SCORED"

    def test_552_and_553_deltas_directionally_distinct(self):
        # #552 (-0.7633, target-harsher inversion) and #553 (+0.10,
        # near-zero constancy) are opposite sign classes: one is an
        # asymmetry observation, the other a falsification. The suite must
        # not conflate them; #552's magnitude exceeds #553's by > 7x.
        r552 = score(TARGET_552, PEER_552, "Meta", ["Anthropic"],
                     "financial_times")
        r553 = score(TARGET_553, PEER_553, "Meta",
                     ["non_Meta_surveillance_targets"], "wired")
        assert r552.asymmetry_score < 0 < r553.asymmetry_score
        assert abs(r552.asymmetry_score) > 7 * abs(r553.asymmetry_score)


# ---------------------------------------------------------------------------
# Standing-rule discipline ratchet, extended: #552 is the first mechanism
# where the ENGINE's raw significance output diverges from the finding layer
# (engine p ~ 0.00023, is_significant True) while the YAML still carries
# significant: false with p_value NOT CALCULATED and empirical_required: true.
# The standing rule holds the finding layer even when the engine would claim
# significance - the separation is deliberate, not an oversight.
# ---------------------------------------------------------------------------

FT = REPO_ROOT / "profiles" / "financial-times.yaml"
WIRED = REPO_ROOT / "profiles" / "wired.yaml"
MECH_552 = ("iteration_552_sep06_2026_ft_anthropic_surveillance_refusal_"
            "register_inversion")


def _scorer_552():
    with open(FT) as f:
        d = yaml.safe_load(f)
    return d["competitor_relationships"]["anthropic"][MECH_552][
        "asymmetry_scoring_manual_illustrative"]


def _scorer_553():
    with open(WIRED) as f:
        d = yaml.safe_load(f)
    return d["journalist_cross_entity_coverage"]["caroline_haskins"][
        "asymmetry_scorer_result"]


class TestStandingRuleDisciplineRatchet555:
    def test_552_scorer_keeps_not_calculated(self):
        s = _scorer_552()
        assert "NOT CALCULATED" in str(s["p_value"])
        assert "NOT CALCULATED" in str(s["cohens_d"])
        assert "NOT CALCULATED" in str(s["ci_95"])

    def test_552_scorer_not_significant_in_finding_layer(self):
        assert _scorer_552()["significant"] is False

    def test_552_engine_significance_not_promoted(self):
        # The crux of the divergence ratchet: the engine computes
        # is_significant True for this input pair, but the finding layer
        # deliberately does not promote it. Both facts must be true at
        # once - the engine is not broken and the rule is not forgotten.
        r = score(TARGET_552, PEER_552, "Meta", ["Anthropic"],
                  "financial_times")
        assert r.is_significant is True, \
            "engine must still compute significance on the logged arrays"
        assert _scorer_552()["significant"] is False, \
            "finding layer must not promote it (synthetic inputs)"
        assert _scorer_552()["empirical_required"] is True

    def test_552_logged_arrays_match_engine_inputs(self):
        s = _scorer_552()
        assert list(s["target_scores_manual_illustrative"]) == TARGET_552
        assert list(s["peer_scores_manual_illustrative"]) == PEER_552
        assert s["delta_manual_illustrative"] == pytest.approx(0.7633)
        assert s["target_avg_manual_illustrative"] == pytest.approx(-0.6)
        assert s["peer_avg_manual_illustrative"] == pytest.approx(0.1633)

    def test_552_synthetic_discipline_labels(self):
        s = _scorer_552()
        assert "MANUAL ILLUSTRATIVE" in str(s["note"]), \
            "note must carry the MANUAL ILLUSTRATIVE label"
        assert "illustrative only" in str(s["synthetic_note"]).lower()
        assert s["p_value"] != 0.00022740128636493896, \
            "YAML p_value must not equal the engine's computed p"

    def test_553_scorer_keeps_not_calculated(self):
        s = _scorer_553()
        assert "NOT_CALCULATED" in str(s["p_value"])
        assert "NOT_CALCULATED" in str(s["cohens_d"])
        assert "NOT_CALCULATED" in str(s["ci"])

    def test_553_scorer_not_significant(self):
        assert _scorer_553()["is_significant"] is False

    def test_553_logged_arrays_match_engine_inputs(self):
        s = _scorer_553()
        assert list(s["target_tones_manual_illustrative"]) == TARGET_553
        assert list(s["reference_tones_manual_illustrative"]) == PEER_553
        assert s["delta_meta_minus_non_meta"] == pytest.approx(0.10)

    def test_553_discipline_illustrative_only(self):
        disc = None
        with open(WIRED) as f:
            d = yaml.safe_load(f)
        disc = d["journalist_cross_entity_coverage"]["caroline_haskins"][
            "statistical_discipline"]
        assert "MANUAL_ILLUSTRATIVE_ONLY" in str(disc["tone_scores"])
        assert "NOT_CALCULATED" in str(disc["p_value"])


# ---------------------------------------------------------------------------
# Brittle-assertion repair: #551's test_iteration_log_entry_newest_first
# asserted the newest-first heading is still #551 - false at this run
# (first heading is #554). Repaired this run to assert presence of the #551
# entry (following the #495 brittle-repair convention).
# ---------------------------------------------------------------------------


class TestBrittleRepair555:
    def test_551_repair_present_in_file(self):
        path = TESTS_DIR / (
            "test_type_e_551_podcast_sentiment_thirtythird_verification"
            "_sep05_11pm.py")
        text = path.read_text(encoding="utf-8")
        assert "Brittle-assertion repair (Type D #555)" in text, \
            "#551 file must carry the #555 repair note"
        assert 're.search(r"^#551 Type E"' in text, \
            "#551 file must assert presence, not newest-first"

    def test_551_entry_present_in_log(self):
        text = LOG.read_text(encoding="utf-8")
        assert re.search(r"^#551 Type E", text, re.MULTILINE), \
            "iteration-log.md lost the #551 Type E entry"

    def test_551_repair_passes(self):
        text = LOG.read_text(encoding="utf-8")
        m = re.search(r"^#551 Type E", text, re.MULTILINE)
        assert m is not None


# ---------------------------------------------------------------------------
# Rotation-cycle guard: the 551 E -> 552 A -> 553 B -> 554 C window follows
# A->B->C->D->E->A adjacency in git-commit order (newest first), plus this
# run's #555 D closing the cycle. Extends #550's 546-549 window guard.
# ---------------------------------------------------------------------------

_CYCLE = {"A": "B", "B": "C", "C": "D", "D": "E", "E": "A"}


class TestRotationCycleGuard555:
    _SUBJECT_PATTERNS = (
        re.compile(r"Type ([A-E]) #(\d+)"),
        re.compile(r"#(\d+) Type ([A-E])\b"),
        re.compile(r"#(\d+) \(Type ([A-E])\)"),
    )

    @classmethod
    def _parse_subject(cls, subject):
        for pat in cls._SUBJECT_PATTERNS:
            m = pat.search(subject)
            if m:
                groups = m.groups()
                if pat is cls._SUBJECT_PATTERNS[0]:
                    return int(groups[1]), groups[0]
                return int(groups[0]), groups[1]
        return None

    def _recent_type_commits(self, n):
        proc = subprocess.run(
            ["git", "log", "--format=%s", "-25"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=60,
        )
        commits = []
        for line in proc.stdout.splitlines():
            parsed = self._parse_subject(line)
            if parsed:
                commits.append(parsed)
            if len(commits) == n:
                break
        return commits

    def test_551_through_554_types_in_order(self):
        commits = self._recent_type_commits(4)
        assert commits == [(554, "C"), (553, "B"), (552, "A"),
                           (551, "E")], (
            f"expected 554 C / 553 B / 552 A / 551 E newest-first, got "
            f"{commits}"
        )

    def test_cycle_adjacency_holds(self):
        commits = self._recent_type_commits(4)
        for (num_newer, type_newer), (num_older, type_older) in zip(
                commits, commits[1:]):
            assert num_newer == num_older + 1, (
                f"non-consecutive: #{num_newer} after #{num_older}"
            )
            assert _CYCLE[type_older] == type_newer, (
                f"rotation broken: #{num_older} Type {type_older} -> "
                f"#{num_newer} Type {type_newer}, expected "
                f"{_CYCLE[type_older]}"
            )

    def test_550_precedes_551_as_d_before_e(self):
        commits = self._recent_type_commits(5)
        assert commits == [(554, "C"), (553, "B"), (552, "A"), (551, "E"),
                           (550, "D")], (
            f"expected 554 C / 553 B / 552 A / 551 E / 550 D newest-first, "
            f"got {commits}"
        )
        assert _CYCLE["D"] == "E", "D must precede E in the cycle"

    def test_this_run_closes_cycle_as_d(self):
        # This run is #555 Type D: C->D closes the 551-554 window
        # (asserted on the current code's metadata, not on a commit that
        # does not exist until this run is committed).
        assert "Type D #555" in __doc__
        newest = self._recent_type_commits(1)
        assert newest == [(554, "C")], f"expected newest commit (554, C)"
        assert _CYCLE["C"] == "D", "C must be followed by D in the cycle"


# ---------------------------------------------------------------------------
# Doc-sync ratchet: per-file README/ARCHITECTURE rows for the 551-555
# window with true counts; authoritative count gate green. Includes the
# doc_sync_miss_repair for #552 and #553 (rows were missing before this
# run, #510 repair convention).
# ---------------------------------------------------------------------------

FILE_552 = ("test_type_a_552_ft_anthropic_surveillance_refusal_register_"
            "inversion_sep06.py")
FILE_553 = ("test_type_b_553_caroline_haskins_wired_surveillance_register_"
            "constancy_sep06.py")
FILE_554 = ("test_type_c_554_mistral_afp_wire_service_licensing_sep06_2am.py")
FILE_551 = ("test_type_e_551_podcast_sentiment_thirtythird_verification"
            "_sep05_11pm.py")

DOC_SYNC_WINDOW_555 = [FILE_551, FILE_552, FILE_553, FILE_554, FILE_555]


class TestDocSyncRatchet555:
    """Per-file README/ARCHITECTURE rows exist with true counts (551-555)."""

    def test_readme_row_for_555_with_true_count(self):
        readme = README.read_text()
        pattern = re.compile(
            r"\|\s*`" + re.escape(FILE_555) + r"`\s*\|\s*(\d+)\s*\|"
        )
        m = pattern.search(readme)
        assert m, f"README row missing for {FILE_555}"
        assert int(m.group(1)) == count_def_tests(FILE_555)

    def test_architecture_row_for_555_with_true_count(self):
        arch = ARCHITECTURE.read_text()
        assert FILE_555 in arch, f"ARCHITECTURE row missing for {FILE_555}"
        row = next(line for line in arch.splitlines() if FILE_555 in line)
        assert str(count_def_tests(FILE_555)) in row, (
            f"count mismatch in ARCHITECTURE row for {FILE_555}"
        )

    def test_recent_window_rows_present_in_both_docs(self):
        readme = README.read_text()
        arch = ARCHITECTURE.read_text()
        for fname in DOC_SYNC_WINDOW_555:
            assert fname in readme, f"README row missing for {fname}"
            assert fname in arch, f"ARCHITECTURE row missing for {fname}"

    def test_window_rows_have_true_counts(self):
        readme = README.read_text()
        for fname in DOC_SYNC_WINDOW_555:
            pattern = re.compile(
                r"\|\s*`" + re.escape(fname) + r"`\s*\|\s*(\d+)\s*\|"
            )
            m = pattern.search(readme)
            assert m, f"README row missing for {fname}"
            assert int(m.group(1)) == count_def_tests(fname), (
                f"README count for {fname}: {m.group(1)} != "
                f"{count_def_tests(fname)}"
            )

    def test_count_gate_green_under_venv_python(self):
        out = subprocess.run(
            [str(VENV_PYTHON), "scripts/count_stats.py", "--check"],
            capture_output=True,
            text=True,
            timeout=600,
            cwd=REPO_ROOT,
        )
        assert out.returncode == 0, out.stderr[-2000:]
