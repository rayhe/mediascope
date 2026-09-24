"""Type A #967 (2026-09-24 10:00 PDT): The Verge x Apple September-2026
event-window register vs The Verge x Meta September-2026 Connect register.
Temporal extension of mechanism 646 (iteration #687) into the full September
launch-event windows.

NEW-TO-CORPUS items: (a1) Tom Warren Sep 9 2026 2:19 pm "Apple skips the base
iPhone 18 at its fall launch event" (mirror-attested, TechNewsTube Verge feed)
register skeptical product-cadence news-analysis (-0.25); (m1) The Verge's
Connect-week on-the-record relay via Yanko Design Sep 24 2026: Meta VP for
wearables Alex Himel "told The Verge" the Ray-Ban Meta Audio glasses "do not
record... listen for the wake word and begin recording only after hearing it"
register privacy-positive measured on-the-record (+0.10), corroborated by the
world-today-journal relay "According to The Verge, the Ray-Ban Meta Audio
glasses prioritize privacy by removing photo and video capture functions
entirely". Carried per #807: m646 Apple Duo launch arm avg +0.38 (0.25 /
0.50), m646 Meta Muse launch arm -0.35.

Event-window illustrative delta (Apple minus Meta): -0.25 - 0.10 = -0.35.
Within-entity deltas: Apple new vs carried -0.63; Meta new vs carried +0.45.
The gradient REVERSES m646's launch-window meta-minus-apple -0.73: on the
event-window pegs (cadence-break criticism for Apple, camera-removal privacy
concession for Meta), The Verge applies the harsher register to APPLE.
EXTENDS m646; REPLICATES the m587 null-tie symmetric-adversarial family in a
THIRD publication (Gizmodo x2, now Verge); contrasts m604 (Samsung
product-forward vs Meta deficit).

Statistical discipline per the Aug 28 2026 standing rule: MANUAL ILLUSTRATIVE
scores only, p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False,
engine NOT run at the finding layer; verdict directionally_supported_not_proven;
no analysis.json update; NOT artifact-grade.

Deselected pre-commit per the #565 convention: anchor 1 + rotation guard 4
(patched green in the anchor followup); doc-sync 3 green post-doc-sync and
iteration-log entry tests green with the entry per #719.

Anchor placeholder: patched to the main commit SHA in the #565 follow-up.
"""

import os
import re
import subprocess
from pathlib import Path

import pytest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TESTS_DIR = Path(REPO_ROOT) / "tests"
VERGE_PATH = "profiles/the-verge.yaml"
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"
TEST_BASENAME = (
    "test_type_a_967_verge_apple_sep2026_event_window_"
    "vs_meta_connect_sep24_10am.py"
)
MECH_NUM = 811
# Built by concatenation so the underscore-form marker never sits contiguously
# in this file: the #715 sweep-instrument convention. The YAML block key is
# descriptive by the #723/#738/#739 designed-keying convention (no
# underscore-form mechanism key substring), keeping the zero-underscore
# sweeps green post-commit.
MECH_ID_MARKER = "mechanism" + "_811"
NEXT_ID_MARKER = "mechanism" + "_812"
NEXT_ID_NUMERIC = "mechanism_id: 812"
MECH_KEY = (
    "verge_apple_sep2026_event_window_"
    "cadence_break_register_vs_meta_connect_"
    "audio_privacy_positive_sep24_2026"
)
NEXT_SIBLING = "\n  google:"
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"
ITERATION = 967
TYPE_LETTER = "A"

URL_WARREN = (
    "https://technewstube.com/theverge/1865859/"
    "apple-skips-base-iphone-18-fall-launch-event/"
)
URL_YANKO = (
    "https://www.yankodesign.com/2026/09/24/"
    "ray-ban-meta-audio-glasses-launched-without-the-controversial-camera/"
)
URL_WTJ = (
    "https://world-today-journal.com/meta-connect-2026-"
    "meta-vr-glasses-ray-ban-meta-gen-3-and-new-ai-audio-specs-announced/"
)


def _read(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def _fold(s):
    return re.sub(r"\s+", " ", s.lower())


def _run_git(*args):
    return subprocess.run(
        ["git", "-C", REPO_ROOT] + list(args),
        capture_output=True,
        text=True,
    )


def _block():
    doc = _read(VERGE_PATH)
    start = doc.index(MECH_KEY + ":")
    end = doc.index(NEXT_SIBLING, start)
    return doc[start:end]


def _block_data():
    import yaml

    return yaml.safe_load(_block())[MECH_KEY]


def _profiles_corpus():
    out = []
    for root, _dirs, files in os.walk(os.path.join(REPO_ROOT, "profiles")):
        for fn in files:
            if fn.endswith((".yaml", ".yml", ".md")):
                out.append(_read(os.path.join(root, fn)))
    return "\n".join(out)


# --- Novelty ---------------------------------------------------------------


class TestNovelty967:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    def test_single_test_type_a_967_file(self):
        files = sorted(str(p) for p in TESTS_DIR.glob("test_type_a_967*.py"))
        assert len(files) == 1, files
        assert files[0].endswith(TEST_BASENAME), files

    @pytest.mark.anchor
    def test_type_a_967_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched green post-commit.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), "anchor SHA is still the pre-commit placeholder"
        res = _run_git("log", "--all", "--grep", "Type A #967")
        assert ANCHORED_SHA in res.stdout, "main commit is not the expected anchored SHA"

    def test_novelty_verification_claim_present_in_block(self):
        # The block pins the pre-commit novelty greps (zero test_type_a_967
        # files on disk, no "Type A #967" in git log, max numeric
        # mechanism_id 810 in profiles/ pre-commit, zero underscore-form 811
        # strings in profiles/ and tests/, zero numeric 811-form mechanism
        # keys in profiles/, zero dash-form 811 references in profiles/,
        # block key zero-hit repo-wide pre-commit, the three new URLs
        # zero-hit repo-wide pre-commit); this test pins the claim in
        # the committed block, per the #752 convention.
        data = _block_data()
        # Folded block text doubles single quotes inside YAML single-quoted
        # scalars; normalize before asserting the prose claims.
        rm = _fold(data["research_method"]).replace("''", "'")
        assert "zero test_type_a_967 files on disk" in rm
        assert 'no "type a #967" in git log' in rm
        assert "max numeric mechanism_id 810 in profiles/" in rm
        assert "zero underscore-form 811" in rm
        assert "zero numeric 811-form mechanism keys in profiles/" in rm
        assert "zero dash-form 811 references in profiles/" in rm
        assert "block key zero-hit repo-wide" in rm
        assert "three new urls zero-hit repo-wide" in rm


# --- Rotation guard ---------------------------------------------------------


class TestRotationCycleGuard967:
    """Rotation: 965-969 window third leg D->E->A->B->C."""

    @pytest.mark.rotation
    def test_third_leg_of_965_969_window(self):
        assert TYPE_LETTER == "A"
        assert ITERATION == 967

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {965: "D", 966: "E", 967: "A", 968: "B", 969: "C"}
        assert expected[967] == "A"
        assert list(expected.values()) == ["D", "E", "A", "B", "C"]

    @pytest.mark.rotation
    def test_predecessor_966_committed(self):
        res = _run_git("log", "--format=%H %s", "--grep", "Type E #966")
        mains = [
            line
            for line in res.stdout.splitlines()
            if "Type E #966" in line and "followup" not in line.lower()
        ]
        assert mains, "predecessor #966 main commit not found"

    @pytest.mark.rotation
    def test_successor_968_not_yet_run(self):
        res = _run_git("log", "--oneline", "--grep", "Type B #968")
        assert not res.stdout.strip(), "successor #968 already present"


# --- Mechanism content ------------------------------------------------------


class TestMechanism811Content:
    def test_block_key_unique_and_parses(self):
        import yaml

        doc = yaml.safe_load(_read(VERGE_PATH))
        apple = doc["competitor_relationships"]["apple"]
        assert apple[MECH_KEY]["mechanism_id"] == 811
        assert sum(1 for k in apple if k == MECH_KEY) == 1

    def test_mechanism_identity_fields(self):
        data = _block_data()
        assert data["mechanism_id"] == 811
        assert data["iteration"] == 967
        assert data["iteration_type"] == "A"
        assert data["type"] == "Type A - Competitor Coverage Deep Dive"
        assert data["scheduled_job_id"] == "mediascope-daily-iteration"
        assert data["goal_id"] == "goal_54093bda4145"

    def test_apple_arm_register_and_tones(self):
        data = _block_data()
        finding = data["finding"]
        assert "Tom Warren" in finding
        assert "skips the base iPhone 18" in finding
        assert "-0.25" in finding
        assert "m646" in finding
        assert "+0.38" in finding
        res = data["asymmetry_scorer_result"]
        assert res["apple_new_arm_tone"] == -0.25
        assert res["apple_carried_m646_avg"] == 0.38

    def test_meta_arm_register_and_tones(self):
        data = _block_data()
        finding = data["finding"]
        assert "Alex Himel" in finding
        assert "Ray-Ban Meta Audio" in finding
        assert "+0.10" in finding
        assert "-0.35" in finding
        res = data["asymmetry_scorer_result"]
        assert res["meta_new_arm_tone"] == 0.10
        assert res["meta_carried_m646_avg"] == -0.35

    def test_arm_provenance_urls_verbatim(self):
        data = _block_data()
        urls = data["source_urls"]
        assert URL_WARREN in urls
        assert URL_YANKO in urls
        assert URL_WTJ in urls
        assert len(urls) == 3

    def test_financial_context_zero_ties(self):
        import yaml

        doc = yaml.safe_load(_read(VERGE_PATH))
        apple = doc["competitor_relationships"]["apple"]
        assert apple["financial_tie"] == "none"
        assert apple["estimated_value"] == "$0"
        assert apple["coverage_prediction"] == "softer"
        assert "$0 documented financial ties" in _block_data()["finding"]

    def test_extension_claims_present(self):
        finding = _block_data()["finding"]
        assert "EXTENDS m646" in finding
        assert "REPLICATES" in finding
        assert "m587" in finding
        assert "m604" in finding
        connects = _block_data()["connects_to"]
        for mid in (646, 587, 808, 604, 628, 626, 644):
            assert mid in connects


# --- Asymmetry math ----------------------------------------------------------


class TestAsymmetryScorerMath:
    def test_event_window_delta(self):
        res = _block_data()["asymmetry_scorer_result"]
        delta = round(res["apple_new_arm_tone"] - res["meta_new_arm_tone"], 2)
        assert delta == res["event_window_delta_apple_minus_meta"] == -0.35

    def test_within_entity_deltas(self):
        res = _block_data()["asymmetry_scorer_result"]
        assert round(res["apple_new_arm_tone"] - res["apple_carried_m646_avg"], 2) == (
            res["apple_within_entity_delta"]
        ) == -0.63
        assert round(res["meta_new_arm_tone"] - res["meta_carried_m646_avg"], 2) == (
            res["meta_within_entity_delta"]
        ) == 0.45

    def test_confounders_ranked_strong_first(self):
        confs = _block_data()["confounders"]
        assert len(confs) == 6
        assert all(c.startswith("STRONG") for c in confs[:3])
        assert confs[3].startswith("MODERATE")
        assert confs[4].startswith("MODERATE")
        assert confs[5].startswith("WEAK")


# --- Statistical discipline --------------------------------------------------


class TestStatisticalDiscipline967:
    def test_manual_illustrative_only(self):
        res = _block_data()["asymmetry_scorer_result"]
        assert res["p_value"] == "NOT_CALCULATED"
        assert res["cohens_d"] == "NOT_CALCULATED"
        assert res["confidence_interval"] == "NOT_CALCULATED"
        sd = _block_data()["statistical_discipline"]
        assert "MANUAL ILLUSTRATIVE" in sd
        assert "NOT_CALCULATED" in sd

    def test_engine_not_run_no_significance(self):
        res = _block_data()["asymmetry_scorer_result"]
        assert res["is_significant"] is False
        sd = _block_data()["statistical_discipline"]
        assert "is_significant False" in sd
        assert "engine NOT run" in sd

    def test_not_artifact_grade_correlation_not_causation(self):
        data = _block_data()
        assert data["no_analysis_json_update"] is True
        assert "NOT artifact-grade" in data["finding"]
        assert "correlation is not causation" in data["statistical_discipline"].lower()

    def test_verdict_directionally_supported_not_proven(self):
        data = _block_data()
        assert data["verdict"] == "directionally_supported_not_proven"
        assert "verdict directionally_supported_not_proven" in data["statistical_discipline"]


# --- Supersession ------------------------------------------------------------


class TestSupersessionAndCorpusPost966:
    def _numeric_ids(self):
        res = _run_git("grep", "-oh", "mechanism_id: [0-9]*", "--", "profiles/")
        return sorted(
            int(m.group(1)) for m in re.finditer(r"mechanism_id: (\d+)", res.stdout)
        )

    def test_corpus_max_is_811(self):
        assert max(self._numeric_ids()) == 811

    def test_iteration_966_max_810_sweep_superseded_by_design(self):
        # #966's max-810 sweeps fail by designed supersession now that 811 exists.
        assert max(self._numeric_ids()) != 810

    def test_zero_underscore_812_repo_wide(self):
        res = _run_git("grep", "-r", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_numeric_812_in_profiles(self):
        res = _run_git("grep", NEXT_ID_NUMERIC, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_966_zero_underscore_811_sweep_stays_green(self):
        # #966's zero-underscore-811 sweeps stay green post-#967 by designed
        # keying: neither the profile block nor this test file carries a
        # literal contiguous underscore-811 key (format-built needles only).
        for root in ("profiles/", "tests/"):
            res = _run_git("grep", "-r", MECH_ID_MARKER, "--", root)
            assert res.returncode != 0 and not res.stdout.strip(), (
                "literal underscore-811 key leaked into %s" % root
            )

    def test_iteration_966_zero_numeric_811_fails_by_designed_supersession(self):
        res = _run_git("grep", "-r", "mechanism_id: 811", "--", "profiles/")
        assert res.returncode == 0 and res.stdout.strip(), (
            "expected #966's zero-numeric-811 sweep to fail by designed supersession"
        )

    def test_numeric_811_keys_in_exactly_the_designed_location(self):
        res = _run_git("grep", "-r", "mechanism_id: 811", "--", "profiles/")
        hits = [line for line in res.stdout.strip().splitlines() if line.strip()]
        # Designed keying: one numeric 811 key in the verge apple block;
        # no other profiles/ location.
        assert len(hits) == 1, "unexpected numeric 811 key spread in profiles/: %s" % hits
        assert "profiles/the-verge.yaml" in hits[0]


# --- Ledger -----------------------------------------------------------------


class TestLedger967:
    def test_thirtieth_present_and_thirty_first_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference their own negative guards inside their
        # own negative-guard tests, so a tests/ sweep would false-positive).
        corpus = _profiles_corpus()
        assert "THIRTIETH" in corpus
        assert "THIRTY-FIRST" not in corpus
        assert "ledger holds at 29" in _block().lower()

    def test_m811_block_key_unique_and_parses(self):
        import yaml

        doc = yaml.safe_load(_read(VERGE_PATH))
        apple = doc["competitor_relationships"]["apple"]
        assert apple[MECH_KEY]["mechanism_id"] == 811
        assert sum(1 for k in apple if k == MECH_KEY) == 1

    def test_m811_not_a_falsification_family_member(self):
        data = _block_data()
        assert data["falsification_family_member"] is False
        assert data["falsification_ledger"] == 29
        assert "THIRTIETH" in data["ledger_note"]


# --- Doc-sync ----------------------------------------------------------------


class TestDocSync967:
    def test_readme_stats_table_updated(self):
        readme = _read(README_PATH)
        assert "49793" in readme and "1292" in readme

    def test_readme_test_file_table_row_present(self):
        assert TEST_BASENAME.replace(".py", "") in _read(README_PATH)

    def test_architecture_tests_tree_updated(self):
        assert TEST_BASENAME.replace(".py", "") in _read(ARCH_PATH)


# --- Iteration log ----------------------------------------------------------


class TestIterationLog967:
    def test_log_has_967_marker(self):
        assert "## #967 Type A" in _read(LOG_PATH)

    def test_log_entry_names_window_leg(self):
        assert "965-969 window" in _read(LOG_PATH)


# --- Push readiness ---------------------------------------------------------


class TestPushReadiness967:
    def test_ascii_only_no_em_dashes(self):
        text = _read(os.path.join("tests", TEST_BASENAME))
        assert "\u2014" not in text
        assert all(ord(c) < 128 for c in text)

    def test_verge_yaml_block_ascii_only_no_em_dashes(self):
        text = _block()
        assert "\u2014" not in text
        assert all(ord(c) < 128 for c in text)

    def test_no_literal_underscore_811_in_test_file(self):
        # The #715 sweep-instrument convention: the literal contiguous
        # underscore-form key must not appear in this file.
        text = _read(os.path.join("tests", TEST_BASENAME))
        assert MECH_ID_MARKER not in text

    def test_concurrent_files_untouched_by_this_run(self):
        # git diffs on the in-flight files must show only their own
        # blocks (m762 / m771); this run adds no 967 hunks to them.
        # #938's test file carries #938's own open anchor-followup working-tree
        # edit (owned by #938's chain, untouched by #967). The untracked
        # #900 Type D file is not in any diff; assert no 967 marker in it.
        for f, own in (
            ("profiles/competitor-entities.yaml", "762"),
            ("profiles/nytimes.yaml", "771"),
        ):
            diff = _run_git("diff", "--", f).stdout
            assert ("mechanism" + "_id" + ": " + own) in diff
            assert "967" not in diff
        rdiff = _run_git(
            "diff", "--",
            "tests/test_type_b_938_dominic_preston_verge_pixel_watch_"
            "gemini_personalization_vs_meta_luna_stigma_sep16.py",
        ).stdout
        assert "967" not in rdiff
        d900 = _read(
            "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py"
        )
        assert "967" not in d900
        assert MECH_ID_MARKER not in d900
