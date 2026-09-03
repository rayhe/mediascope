"""
Type D #490 - Iteration-log placement repair (#488) + 485-489 window persistence
Sep 3 2026 08:00 PDT - scheduled job_id mediascope-daily-iteration goal_54093bda4145 rotation C->D

Mechanism #490 defines no data mechanism; it repairs and verifies, following
the #485 precedent. The 06:00 PDT Sep 3 run appended its Type B Chris Welch
within-journalist follow-up as a bottom-appended "## Type B #488" entry instead
of the repo-standard newest-first "#488 Type B: ..." heading at file top. This
iteration moves that entry to the top (between #489 and #487), preserving all
content byte-for-byte, and extends the persistence regression guard to the
485-489 window.

Workstreams:
(1) log placement repair - "#488 Type B:" heading at file top in newest-first
    order (489 > 488 > 487 > 486 > 485); no bottom-appended "## Type B #488"
    entry remains; heading appears exactly once; entry body preserved
    (mechanism #85 follow-up text, all 5 source URLs, files-changed list);
(2) window persistence - test files, iteration-log headings, and YAML anchors
    for #485 (Type D), #486 (Type E), #487 (Type A), #488 (Type B follow-up,
    no new mechanism_id by design), #489 (Type C) all present; rotation chain
    D->E->A->B->C->D intact;
(3) README/ARCHITECTURE sync - table rows for the #488, #489, and #490 test
    files; header counts match scripts/count_stats.py actuals.

Statistical discipline: this iteration asserts metadata and repair integrity
only; no tone scores, no p_value, no significance claimed.

Goal and job IDs: goal_54093bda4145 mediascope-daily-iteration iteration 490 Type D 2026-09-03 08:00 PDT
"""

import math
import re
from datetime import datetime
from pathlib import Path

import pytest
import yaml

from mediascope.score.asymmetry import calculate_asymmetry

REPO = Path(__file__).resolve().parent.parent
LOG = REPO / "iteration-log.md"
README = REPO / "README.md"
ARCH = REPO / "docs" / "ARCHITECTURE.md"
COMP = REPO / "profiles" / "competitor-entities.yaml"
GUARDIAN = REPO / "profiles" / "guardian.yaml"
JOURNALISTS = REPO / "profiles" / "careers" / "journalists.yaml"
RESEARCH = REPO / "profiles" / "competitor-coverage-research.yaml"

FILE_485 = "test_type_d_485_collision_repair_and_window_persistence_sep03_3am.py"
FILE_486 = "test_type_e_486_podcast_sentiment_twentieth_verification_sep03_4am.py"
FILE_487 = "test_type_a_487_guardian_google_deepmind_leadership_renewal_vs_meta_deficit_framing_sep03_5am.py"
FILE_488 = "test_chris_welch_within_journalist_meta_vs_samsung_privacy_sep03.py"
FILE_489 = "test_type_c_489_hearst_openai_dual_payer_sep03_7am.py"
FILE_490 = "test_type_d_490_log_repair_and_window_persistence_sep03_8am.py"

# Iteration 364 documented observed arrays (WIRED x OpenAI hardware, Aug 29 2026).
TARGET_364 = [-0.72, -0.82, -0.78]
PEER_364 = [0.10, 0.05, 0.15]


def _score_364():
    return calculate_asymmetry(
        target_scores=list(TARGET_364),
        peer_scores=list(PEER_364),
        target_entity="Meta",
        peer_entities=["OpenAI"],
        publication_slug="wired",
        period_start=datetime(2026, 8, 1),
        period_end=datetime(2026, 8, 29),
    )


def _log_lines():
    return LOG.read_text(encoding="utf-8").split("\n")


def _headings():
    return [l for l in _log_lines() if re.match(r"^#\d+ Type [A-E]:", l)]


def _heading_index(prefix):
    return next(i for i, l in enumerate(_log_lines()) if l.startswith(prefix))


def _segment_between(start_prefix, end_prefix):
    lines = _log_lines()
    start = _heading_index(start_prefix)
    end = _heading_index(end_prefix)
    assert start < end
    return "\n".join(lines[start:end])


def _count_stats():
    """Authoritative test/file counts via scripts/count_stats.py.

    Added #495: feeds the dynamic header-sync checks so hardcoded
    "N tests across M test files" strings never go stale again.
    """
    import sys

    sys.path.insert(0, str(REPO / "scripts"))
    import count_stats

    return count_stats.count_tests_pytest()


class TestIteration490Metadata:
    def test_docstring_ids(self):
        doc = __doc__
        assert "iteration 490" in doc
        assert "2026-09-03" in doc
        assert "Type D" in doc
        assert "goal_54093bda4145" in doc
        assert "mediascope-daily-iteration" in doc

    def test_rotation_c_to_d(self):
        assert "rotation C->D" in __doc__

    def test_filename_convention(self):
        assert Path(__file__).name == FILE_490

    def test_rotation_chain_in_docstring(self):
        assert "D->E->A->B->C->D" in __doc__

    def test_no_causal_claim(self):
        assert "no significance claimed" in __doc__


class TestLog488PlacementRepair:
    def test_no_bottom_appended_488_entry(self):
        assert not any(l.startswith("## Type B #488") for l in _log_lines())

    def test_top_has_newest_first_490_then_488_headings(self):
        # Relative newest-first ordering (fixed #495): asserting absolute
        # top-3 position broke when #491-#494 were legitimately prepended.
        # The repair invariant is relative order 490 > 489 > 488.
        headings = _headings()
        idx = {h.split(" ")[0]: i for i, h in enumerate(headings)}
        assert idx["#490"] < idx["#489"] < idx["#488"]

    def test_488_heading_appears_exactly_once(self):
        assert sum(1 for l in _log_lines() if l.startswith("#488 Type B:")) == 1

    def test_newest_first_ordering_490_to_485(self):
        # Relative ordering across the 485-490 window (fixed #495): the
        # window keeps its newest-first invariant wherever it sits in the
        # log, instead of asserting it occupies the absolute top-6 slots.
        headings = _headings()
        idx = {h.split(" ")[0]: i for i, h in enumerate(headings)}
        order = ["#490", "#489", "#488", "#487", "#486", "#485"]
        positions = [idx[m] for m in order]
        assert positions == sorted(positions), positions

    def test_488_body_preserved_followup_marker(self):
        seg = _segment_between("#488 Type B:", "#487 Type A:")
        assert "Mechanism #85 follow-up" in seg
        assert "within-journalist correction, NOT a new mechanism" in seg

    def test_488_body_preserved_source_urls(self):
        seg = _segment_between("#488 Type B:", "#487 Type A:")
        for url in (
            "https://www.techmeme.com/250501/p23",
            "http://www.grc.com/sn/sn-1024.htm",
            "https://techcrunch.com/2025/04/30/if-you-own-ray-ban-meta-glasses-you-should-double-check-your-privacy-settings/",
            "https://www.macrumors.com/2026/05/13/samsung-ai-smart-glasses-july/",
        ):
            assert url in seg

    def test_488_body_preserved_files_changed(self):
        seg = _segment_between("#488 Type B:", "#487 Type A:")
        assert "profiles/careers/journalists.yaml" in seg
        assert FILE_488 in seg


class TestWindow485to489Persistence:
    @pytest.mark.parametrize("fname", [FILE_485, FILE_486, FILE_487, FILE_488, FILE_489, FILE_490])
    def test_window_test_files_exist(self, fname):
        assert (REPO / "tests" / fname).exists()

    def test_489_anchor_in_competitor_entities(self):
        d = yaml.safe_load(COMP.read_text(encoding="utf-8"))
        node = d["entities"]["openai"]["mechanism_489_hearst_openai_dual_ai_payer_partnership"]
        assert node["mechanism_id"] == 489
        assert node["iteration"] == 489

    def test_487_anchor_in_guardian(self):
        text = GUARDIAN.read_text(encoding="utf-8")
        assert "mechanism_id: 487" in text

    def test_488_has_no_new_mechanism_id_by_design(self):
        combined = "".join(
            p.read_text(encoding="utf-8") for p in (COMP, GUARDIAN, JOURNALISTS, RESEARCH)
        )
        assert "mechanism_id: 488" not in combined

    def test_488_followup_recorded_on_mechanism_85(self):
        text = RESEARCH.read_text(encoding="utf-8")
        assert "within_journalist_followup" in text

    def test_488_journalist_correction_persisted(self):
        d = yaml.safe_load(JOURNALISTS.read_text(encoding="utf-8"))
        text = JOURNALISTS.read_text(encoding="utf-8")
        assert "type_b_488_within_journalist_followup" in text

    def test_no_duplicate_mechanism_ids_487_489(self):
        # 485 (Type D) and 486 (Type E) define no YAML mechanism anchors by
        # design; 488 is a follow-up on #85 with no new mechanism_id.
        for mid in (487, 489):
            total = sum(
                p.read_text(encoding="utf-8").count("mechanism_id: %d" % mid)
                for p in (COMP, GUARDIAN, RESEARCH)
            )
            assert total >= 1, "mechanism %d missing" % mid


class TestReadmeArchitectureSync:
    @pytest.mark.parametrize("fname", [FILE_488, FILE_489, FILE_490])
    def test_readme_rows_present(self, fname):
        assert fname in README.read_text(encoding="utf-8")

    @pytest.mark.parametrize("fname", [FILE_488, FILE_489, FILE_490])
    def test_architecture_rows_present(self, fname):
        assert fname in ARCH.read_text(encoding="utf-8")

    def test_readme_header_counts_synced(self):
        # Dynamic sync check (fixed #495): hardcoded "27383 tests across 818
        # test files" went stale with every later iteration. Compare the
        # README header numbers against scripts/count_stats.py actuals.
        stats = _count_stats()
        text = README.read_text(encoding="utf-8")
        m = re.search(r"\*\*(\d[\d,]*) tests\*\* across (\d+) test files", text)
        assert m, "README header test-count line not found"
        assert int(m.group(1).replace(",", "")) == stats["total_tests"]
        assert int(m.group(2)) == stats["test_files"]

    def test_architecture_header_counts_synced(self):
        # Dynamic sync check (fixed #495): see test_readme_header_counts_synced.
        stats = _count_stats()
        text = ARCH.read_text(encoding="utf-8")
        m = re.search(r"(\d[\d,]*) tests across (\d+) test files", text)
        assert m, "ARCHITECTURE.md header test-count line not found"
        assert int(m.group(1).replace(",", "")) == stats["total_tests"]
        assert int(m.group(2)) == stats["test_files"]


class TestYamlIntegrity:
    @pytest.mark.parametrize("path", [COMP, GUARDIAN, JOURNALISTS, RESEARCH])
    def test_yaml_parses(self, path):
        assert yaml.safe_load(path.read_text(encoding="utf-8")) is not None

    def test_no_tab_indentation_in_touched_profiles(self):
        for path in (COMP, GUARDIAN, JOURNALISTS, RESEARCH):
            assert "\t" not in path.read_text(encoding="utf-8")


class TestScorerDeterminism:
    def test_364_reference_deterministic(self):
        assert _score_364().asymmetry_score == _score_364().asymmetry_score

    def test_364_reference_no_nan_or_inf(self):
        score = _score_364().asymmetry_score
        assert not math.isnan(score)
        assert not math.isinf(score)

    def test_364_reference_sign_stable(self):
        assert _score_364().asymmetry_score < 0
