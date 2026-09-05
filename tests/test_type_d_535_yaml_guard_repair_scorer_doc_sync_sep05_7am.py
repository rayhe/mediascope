"""Type D #535: brittle novelty-guard repair + scorer consistency extension.

Iteration 535 (Sep 5 2026, 07:00 PDT) - Type D: Test & Verify.

BRITTLE-GUARD REPAIR: the #533 run (05:00) surfaced a pre-existing failure in
test_type_d_505's test_no_prior_repo_wide_yaml_guard, tripped by #510's
test_type_d_510_doc_sync_miss_repair_and_scorer_consistency_sep04_4am.py
(committed Sep 4 in a0a1a47). Root cause: the #505 novelty guard excluded
only itself (bare `f.name == FILE_505` self-exclusion), so the first
legitimate successor that also globbed the profiles tree broke the guard.
The guard's true intent was "no file from BEFORE iteration 505 does this";
the repaired form (in the #505 file itself, per #530's repair precedent) is
iteration-aware: it exempts #505 and every numbered successor (iteration >=
505, sequential numbering verified by git in #535), while non-numbered
legacy files and numbered files below 505 remain covered. The novelty claim
still holds on the live tree - verified below.

SCORER CROSS-MECHANISM CONSISTENCY (extends #530): the engine is checked
against the two newest quantitative MANUAL ILLUSTRATIVE deltas - #532
(WSJ dual-deal symmetry: Meta [-0.30, -0.25] vs OpenAI [-0.15, -0.25],
delta -0.075) and #533 (Hagey matched-story-type: Meta [-0.35] vs OpenAI
[-0.30], delta -0.05, n=1 vs n=1 degenerate-input path) - plus a re-lock of
#527 (-0.5167) and #528 (-1.025) against engine drift. Per the Aug 28 2026
standing rule all manual deltas remain illustrative, not empirical.

DOC-SYNC REPAIR: docs/ARCHITECTURE.md line 458 still claimed "28592 tests
across 859 test files" after #534 synced the README to 28684/862 - the
#534 run added the per-file row but missed the tree header. Repaired this
run; ratchet tests below cover the 531-535 per-file window and the
authoritative count gate.

TWO MORE STALE-TEST REPAIRS (same brittleness class, found during this
run's regression): #510's test_five_type_commits_precede_this_run_in_order
(the #515 repair's single "Type X #N" regex skipped the #530/#531
"MediaScope #N (Type X)" and #532 "#N Type X" subject formats, failing on a
healthy history) is now format-agnostic over all observed subject shapes;
#534's test_iteration_534_entry_near_top_and_descending (hardcoded
ids[0] == 534, stale the moment #535 was prepended) now asserts 534 inside
the leading descending run with 533 immediately after. Both repaired in
their owning files per the #515/#530 precedent.

Statistical discipline: metadata, guard-repair, and engine-consistency only;
no new tone scores, p_value NOT_CALCULATED for the manual deltas (standing
rule), is_significant False throughout.

Goal and job IDs: goal_54093bda4145 mediascope-daily-iteration iteration 535 Type D 2026-09-05 07:00 PDT rotation C->D
"""

import importlib.util
import re
import subprocess
from datetime import datetime
from pathlib import Path

import pytest

from mediascope.score.asymmetry import calculate_asymmetry

REPO_ROOT = Path(__file__).resolve().parent.parent
TESTS_DIR = REPO_ROOT / "tests"
README = REPO_ROOT / "README.md"
ARCHITECTURE = REPO_ROOT / "docs" / "ARCHITECTURE.md"
VENV_PYTHON = REPO_ROOT / ".venv" / "bin" / "python"

FILE_535 = "test_type_d_535_yaml_guard_repair_scorer_doc_sync_sep05_7am.py"
FILE_505 = "test_type_d_505_yaml_parse_guard_and_rotation_cycle_sep03_11pm.py"
FILE_510 = "test_type_d_510_doc_sync_miss_repair_and_scorer_consistency_sep04_4am.py"
FILE_534 = "test_type_c_534_dotdash_meredith_openai_sep05_6am.py"
FILE_410 = "test_type_a_410_ft_anthropic_ipo_aspirational_vs_meta_super_sensing_aug31.py"
LEGACY_NAME = "test_wsj_meta_ai_layoff_discrimination_jul14.py"

PERIOD = (datetime(2026, 1, 1), datetime(2026, 8, 31))


def load_mod_505():
    """Import the #505 test module as a plain module (not via pytest)."""
    spec = importlib.util.spec_from_file_location("mod_505_guard", TESTS_DIR / FILE_505)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def count_def_tests(test_file):
    """Static def-test count, same definition count_stats.count_tests uses."""
    with open(REPO_ROOT / "tests" / test_file) as f:
        content = f.read()
    return len(re.findall(r"^\s+def test_", content, re.MULTILINE))


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


class TestIteration535Metadata:
    def test_docstring_ids(self):
        doc = __doc__
        assert "iteration 535" in doc
        assert "2026-09-05" in doc
        assert "Type D" in doc
        assert "goal_54093bda4145" in doc
        assert "mediascope-daily-iteration" in doc

    def test_rotation_c_to_d(self):
        assert "rotation C->D" in __doc__

    def test_filename_convention(self):
        assert Path(__file__).name == FILE_535


# ---------------------------------------------------------------------------
# Brittle-guard repair regression: the #505 novelty guard, iteration-aware
# ---------------------------------------------------------------------------


class TestYamlGuardRepairRegression:
    """The #505 guard must be iteration-aware, and the novelty claim holds."""

    def test_iteration_number_parses_numbered_names(self):
        mod = load_mod_505()
        assert mod._iteration_number(FILE_505) == 505
        assert mod._iteration_number(FILE_510) == 510
        assert mod._iteration_number(FILE_534) == 534
        assert mod._iteration_number(FILE_410) == 410

    def test_iteration_number_none_for_legacy_names(self):
        mod = load_mod_505()
        assert mod._iteration_number(LEGACY_NAME) is None
        assert mod._iteration_number("test_structural_consistency.py") is None

    def test_successor_510_classified_exempt(self):
        # The exact case that broke the bare self-exclusion form: #510 is a
        # numbered successor (>= 505), so it cannot predate #505.
        mod = load_mod_505()
        assert mod._iteration_number(FILE_510) >= 505

    def test_repaired_guard_passes_on_live_tree(self):
        mod = load_mod_505()
        # Must not raise: exercises the repaired code path end to end.
        mod.TestRepoWideYamlParse().test_no_prior_repo_wide_yaml_guard()

    def test_prior_set_contains_no_yaml_glob_pattern(self):
        # Independent data check: no pre-#505 test file globs the profiles
        # tree for parsing, so the original novelty claim still holds.
        # (This file is numbered 535 and therefore exempt from the guard;
        # it may name the pattern freely.)
        mod = load_mod_505()
        hits = []
        for f in TESTS_DIR.glob("test_*.py"):
            num = mod._iteration_number(f.name)
            if f.name == FILE_505 or (num is not None and num >= 505):
                continue
            src = f.read_text(encoding="utf-8")
            if "rglob" in src and ".yaml" in src and "safe_load" in src:
                hits.append(f.name)
        assert not hits, f"pre-#505 yaml glob found: {hits}"


# ---------------------------------------------------------------------------
# Scorer cross-mechanism consistency: engine reproduces manual deltas
# (extends #530's lock to #532 and #533)
# ---------------------------------------------------------------------------

# #532 (WSJ dual-deal symmetry, MANUAL ILLUSTRATIVE): Meta target
# [-0.30, -0.25], OpenAI peers [-0.15, -0.25], logged delta -0.075, n.s.
TARGET_532 = [-0.30, -0.25]
PEER_532 = [-0.15, -0.25]

# #533 (Hagey matched story type, MANUAL ILLUSTRATIVE): Meta [-0.35],
# OpenAI [-0.30], logged delta -0.05, n=1 vs n=1, n.s.
TARGET_533 = [-0.35]
PEER_533 = [-0.30]

# Re-locks from #530 (engine-drift guards).
TARGET_527 = [-0.45]
PEER_527 = [-0.15, 0.10, 0.25]
TARGET_528 = [0.15, -0.65]
PEER_528 = [0.80, 0.75]


class TestScorerCrossMechanismConsistency535:
    def test_532_dual_deal_symmetry_reproduced(self):
        r = score(TARGET_532, PEER_532, "Meta", ["OpenAI"], "wsj")
        assert r.asymmetry_score == pytest.approx(-0.075, abs=1e-4)
        assert r.is_significant is False

    def test_533_matched_story_type_reproduced(self):
        # n=1 vs n=1 exercises the degenerate-input path (welch -> p 1.0,
        # cohens_d -> 0.0); the mean-difference arithmetic must still agree.
        r = score(TARGET_533, PEER_533, "Meta", ["OpenAI"], "wsj")
        assert r.asymmetry_score == pytest.approx(-0.05, abs=1e-4)
        assert r.is_significant is False

    def test_527_relock(self):
        r = score(TARGET_527, PEER_527, "Meta", ["Microsoft"], "wsj")
        assert r.asymmetry_score == pytest.approx(-0.5167, abs=1e-4)

    def test_528_relock(self):
        r = score(TARGET_528, PEER_528, "Meta", ["Apple"], "wired")
        assert r.asymmetry_score == pytest.approx(-1.025, abs=1e-4)

    def test_all_deltas_share_meta_harsher_sign(self):
        for target, peer, slug in [
            (TARGET_532, PEER_532, "wsj"),
            (TARGET_533, PEER_533, "wsj"),
            (TARGET_527, PEER_527, "wsj"),
            (TARGET_528, PEER_528, "wired"),
        ]:
            r = score(target, peer, "Meta", ["peer"], slug)
            assert r.asymmetry_score < 0, f"sign flipped for {slug}"


# ---------------------------------------------------------------------------
# Doc-sync ratchet: per-file rows + authoritative count headers
# ---------------------------------------------------------------------------

DOC_SYNC_WINDOW = [
    "test_type_e_531_podcast_sentiment_twenty_ninth_verification_sep05_3am.py",
    "test_type_a_532_wsj_openai_astra_vs_meta_settlement_dual_deal_symmetry_sep05_4am.py",
    "test_type_b_533_keach_hagey_matched_story_type_symmetry_sep05_5am.py",
    "test_type_c_534_dotdash_meredith_openai_sep05_6am.py",
    FILE_535,
]


class TestDocSyncRatchet535:
    """Per-file README/ARCHITECTURE rows exist with true counts (531-535)."""

    def test_readme_row_for_535_with_true_count(self):
        readme = README.read_text()
        pattern = re.compile(
            r"\|\s*`" + re.escape(FILE_535) + r"`\s*\|\s*(\d+)\s*\|"
        )
        m = pattern.search(readme)
        assert m, f"README row missing for {FILE_535}"
        assert int(m.group(1)) == count_def_tests(FILE_535)

    def test_architecture_row_for_535_with_true_count(self):
        arch = ARCHITECTURE.read_text()
        assert FILE_535 in arch, f"ARCHITECTURE row missing for {FILE_535}"
        row = next(line for line in arch.splitlines() if FILE_535 in line)
        assert str(count_def_tests(FILE_535)) in row, (
            f"count mismatch in ARCHITECTURE row for {FILE_535}"
        )

    def test_recent_window_rows_present_in_both_docs(self):
        readme = README.read_text()
        arch = ARCHITECTURE.read_text()
        for fname in DOC_SYNC_WINDOW:
            assert fname in readme, f"README row missing for {fname}"
            assert fname in arch, f"ARCHITECTURE row missing for {fname}"

    def test_count_gate_green_under_venv_python(self):
        # Authoritative gate: README + ARCHITECTURE headers must match the
        # pytest-collected totals (covers the #534-missed ARCHITECTURE tree
        # header repaired this run).
        out = subprocess.run(
            [str(VENV_PYTHON), "scripts/count_stats.py", "--check"],
            capture_output=True,
            text=True,
            timeout=300,
            cwd=REPO_ROOT,
        )
        assert out.returncode == 0, out.stderr[-2000:]
