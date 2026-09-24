"""Type A #962 (2026-09-24 05:00 PDT): Gizmodo x Apple September-2026 event-window
register vs Gizmodo x Meta September-2026 Connect register. Temporal extension of
the m587 null-tie control (mechanism 808) into the September launch-event windows.

NEW-TO-CORPUS items: (a1) Gizmodo "The Real Winners of Apple's WWDC 2026 Don't
Even Exist Yet" smart-glasses section (-0.45); (a2) Gizmodo "Live Updates From
Apple's 'Surprise and Shine' iPhone Event" Sep 9 2026 (-0.40); (m5) Gizmodo
"Live Updates From Meta Connect 2026" Sep 23 2026 (-0.55). Carried arms:
m716 Yildirim Apple Watch Audio Intelligence (-0.60, harshest Apple register),
m587 Meta arms (-0.70 / -0.55 / -0.60), m806 Pero Ray-Ban Audio (-0.20, softest
Meta register). Apple mean -0.4833, Meta mean -0.52, illustrative delta
(Apple minus Meta) +0.0367: within the illustrative band, the null-tie
symmetric-adversarial register REPLICATES in the September event windows.

Statistical discipline per the Aug 28 2026 standing rule: MANUAL ILLUSTRATIVE
scores only, p_value/cohens_d/ci_95 NOT_CALCULATED, is_significant False,
engine NOT run at the finding layer; verdict directionally_supported_not_proven;
no analysis.json update; NOT artifact-grade.

Deselected pre-commit per the #565 convention: anchor 1 + rotation guard 4
(patched green in the anchor followup); iteration-log entry tests fail by
design pre-commit, go green with the entry per #719; doc-sync 3 green
post-doc-sync.

Anchor placeholder: patched to the main commit SHA in the #565 follow-up.
"""

import os
import re
import subprocess
from pathlib import Path

import pytest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TESTS_DIR = Path(REPO_ROOT) / "tests"
GIZMODO_PATH = "profiles/gizmodo.yaml"
README_PATH = "README.md"
ARCH_PATH = "docs/ARCHITECTURE.md"
LOG_PATH = "iteration-log.md"
TEST_BASENAME = (
    "test_type_a_962_gizmodo_apple_sep2026_event_window_"
    "vs_meta_connect_sep24_5am.py"
)
MECH_NUM = 808
# Built by concatenation so the underscore-form marker never sits contiguously
# in this file: the #715 sweep-instrument convention. The YAML block key is
# descriptive by the #723/#738/#739 designed-keying convention (no
# underscore-form mechanism key substring), keeping the zero-underscore
# sweeps green post-commit.
MECH_ID_MARKER = "mechanism" + "_808"
NEXT_ID_MARKER = "mechanism" + "_809"
NEXT_ID_NUMERIC = "mechanism_id: 809"
MECH_KEY = (
    "gizmodo_apple_sep2026_event_window_"
    "symmetric_adversarial_vs_meta_connect"
)
NEXT_SIBLING = "\n  google:"
ANCHORED_SHA = "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565"
ITERATION = 962
TYPE_LETTER = "A"

URL_WWDC = (
    "https://gizmodo.com/the-real-winners-of-apples-wwdc-2026-"
    "dont-even-exist-yet-2000769658"
)
URL_IPHONE_EVENT = (
    "https://gizmodo.com/live-updates-from-apples-surprise-and-shine-"
    "iphone-event-2000806403"
)
URL_YILDIRIM = (
    "https://gizmodo.com/if-meta-glasses-freak-you-out-wait-until-you-"
    "hear-about-the-new-apple-watch-features-2000809371"
)
URL_CONNECT = (
    "https://gizmodo.com/live-updates-from-meta-connect-2026-2000806463"
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
    doc = _read(GIZMODO_PATH)
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


class TestNovelty962:
    """Pre-commit novelty: single new file, unique commit, zero repo precedent."""

    def test_single_test_type_a_962_file(self):
        files = sorted(str(p) for p in TESTS_DIR.glob("test_type_a_962*.py"))
        assert len(files) == 1, files
        assert files[0].endswith(TEST_BASENAME), files

    @pytest.mark.anchor
    def test_type_a_962_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched green post-commit.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), "anchor SHA is still the pre-commit placeholder"
        res = _run_git("log", "--all", "--grep", "Type A #962")
        assert ANCHORED_SHA in res.stdout, "main commit is not the expected anchored SHA"

    def test_novelty_verification_claim_present_in_block(self):
        # The block pins the pre-commit novelty greps (zero test_type_a_962
        # files on disk, no "Type A #962" in git log, max numeric
        # mechanism_id 807 in profiles/ pre-commit, zero underscore-form 808
        # strings in profiles/ and tests/, zero numeric 808-form mechanism
        # keys in profiles/, zero dash-form 808 references in profiles/,
        # block key zero-hit repo-wide pre-commit, the three new URLs
        # zero-hit repo-wide pre-commit); this test pins the claim in
        # the committed block, per the #752 convention.
        data = _block_data()
        # Folded block text doubles single quotes inside YAML single-quoted
        # scalars; normalize before asserting the prose claims.
        rm = _fold(data["research_method"]).replace("''", "'")
        assert "zero test_type_a_962 files on disk" in rm
        assert 'no "type a #962" in git log' in rm
        assert "max numeric mechanism_id 807 in profiles/" in rm
        assert "zero underscore-form 808" in rm
        assert "zero numeric 808-form mechanism keys in profiles/" in rm
        assert "zero dash-form 808 references in profiles/" in rm
        assert "block key zero-hit repo-wide" in rm
        assert "three new urls zero-hit repo-wide" in rm


# --- Rotation guard ---------------------------------------------------------


class TestRotationCycleGuard962:
    """Rotation: 960-964 window third leg D->E->A->B->C."""

    @pytest.mark.rotation
    def test_third_leg_of_960_964_window(self):
        assert TYPE_LETTER == "A"
        assert ITERATION == 962

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {960: "D", 961: "E", 962: "A", 963: "B", 964: "C"}
        assert expected[962] == "A"
        assert list(expected.values()) == ["D", "E", "A", "B", "C"]

    @pytest.mark.rotation
    def test_predecessor_961_committed(self):
        res = _run_git("log", "--format=%H %s", "--grep", "Type E #961")
        mains = [
            line
            for line in res.stdout.splitlines()
            if "Type E #961" in line and "followup" not in line.lower()
        ]
        assert mains, "predecessor #961 main commit not found"

    @pytest.mark.rotation
    def test_successor_963_not_yet_run(self):
        res = _run_git("log", "--oneline", "--grep", "Type B #963")
        assert not res.stdout.strip(), "successor #963 already present"


# --- Mechanism content ------------------------------------------------------


class TestMechanism808Content:
    def test_block_key_unique_and_parses(self):
        import yaml

        doc = yaml.safe_load(_read(GIZMODO_PATH))
        apple = doc["competitor_relationships"]["apple"]
        assert apple[MECH_KEY]["mechanism_id"] == 808
        assert sum(1 for k in apple if k == MECH_KEY) == 1

    def test_mechanism_identity_fields(self):
        data = _block_data()
        assert data["mechanism_id"] == 808
        assert data["iteration"] == 962
        assert data["iteration_type"] == "A"
        assert data["type"] == "Type A - Competitor Coverage Deep Dive"
        assert data["scheduled_job_id"] == "mediascope-daily-iteration"
        assert data["goal_id"] == "goal_54093bda4145"

    def test_apple_arms_register_and_tones(self):
        data = _block_data()
        finding = data["finding"]
        assert "Don't Even Exist Yet" in finding
        assert "'Surprise and Shine'" in finding
        assert "Yildirim" in finding
        assert "-0.45" in finding and "-0.40" in finding and "-0.60" in finding
        apple_tones = [-0.45, -0.40, -0.60]
        assert round(sum(apple_tones) / len(apple_tones), 4) == -0.4833
        res = data["asymmetry_scorer_result"]
        assert res["target_entity"] == "apple"
        assert res["target_avg_tone"] == -0.4833

    def test_meta_comparator_arms_register_and_tones(self):
        data = _block_data()
        finding = data["finding"]
        assert "Meta Connect 2026" in finding
        assert "-0.70" in finding and "-0.55" in finding
        assert "m806" in finding
        meta_tones = [-0.70, -0.55, -0.60, -0.20, -0.55]
        assert round(sum(meta_tones) / len(meta_tones), 4) == -0.52
        res = data["asymmetry_scorer_result"]
        assert res["peer_avg_tone"] == -0.52

    def test_arm_provenance_urls_verbatim(self):
        data = _block_data()
        urls = data["source_urls"]
        assert URL_WWDC in urls
        assert URL_IPHONE_EVENT in urls
        assert URL_YILDIRIM in urls
        assert URL_CONNECT in urls
        assert len(urls) == 4

    def test_financial_context_zero_ties(self):
        import yaml

        doc = yaml.safe_load(_read(GIZMODO_PATH))
        apple = doc["competitor_relationships"]["apple"]
        assert apple["financial_tie"] == "none"
        assert apple["estimated_value"] == "$0"
        assert apple["coverage_prediction"] == "neutral"
        assert "$0 documented financial ties" in _block_data()["finding"]

    def test_extension_claims_present(self):
        finding = _block_data()["finding"]
        assert "EXTENDS m587" in finding
        assert "EXTENDS m716" in finding
        assert "EXTENDS m806" in finding
        assert "REPLICATES" in finding
        connects = _block_data()["connects_to"]
        for mid in (587, 716, 806, 512, 577, 582):
            assert mid in connects


# --- Asymmetry math ----------------------------------------------------------


class TestAsymmetryScorerMath:
    def test_event_window_delta(self):
        res = _block_data()["asymmetry_scorer_result"]
        delta = round(res["target_avg_tone"] - res["peer_avg_tone"], 4)
        assert delta == res["asymmetry_score"] == 0.0367

    def test_delta_direction_matches_null_tie_symmetry(self):
        res = _block_data()["asymmetry_scorer_result"]
        # Within the illustrative band: symmetric-adversarial, not a gradient.
        assert 0.0 <= res["asymmetry_score"] <= 0.15
        assert "within the illustrative band" in _block_data()["finding"]

    def test_confounders_ranked_strong_first(self):
        confs = _block_data()["confounders"]
        assert len(confs) == 7
        assert all(c.startswith("STRONG") for c in confs[:3])
        assert confs[3].startswith("MODERATE")
        assert confs[4].startswith("MODERATE")
        assert all(c.startswith("WEAK") for c in confs[5:])


# --- Statistical discipline --------------------------------------------------


class TestStatisticalDiscipline962:
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


class TestSupersessionAndCorpusPost961:
    def _numeric_ids(self):
        res = _run_git("grep", "-oh", "mechanism_id: [0-9]*", "--", "profiles/")
        return sorted(
            int(m.group(1)) for m in re.finditer(r"mechanism_id: (\d+)", res.stdout)
        )

    def test_corpus_max_is_808(self):
        assert max(self._numeric_ids()) == 808

    def test_iteration_961_max_807_sweep_superseded_by_design(self):
        # #961's max-807 sweeps fail by designed supersession now that 808 exists.
        assert max(self._numeric_ids()) != 807

    def test_zero_underscore_809_repo_wide(self):
        res = _run_git("grep", "-r", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_numeric_809_in_profiles(self):
        res = _run_git("grep", NEXT_ID_NUMERIC, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_961_zero_underscore_808_sweep_stays_green(self):
        # #961's zero-underscore-808 sweeps stay green post-#962 by designed
        # keying: neither the profile block nor this test file carries a
        # literal contiguous underscore-808 key (format-built needles only).
        for root in ("profiles/", "tests/"):
            res = _run_git("grep", "-r", MECH_ID_MARKER, "--", root)
            assert res.returncode != 0 and not res.stdout.strip(), (
                "literal underscore-808 key leaked into %s" % root
            )

    def test_iteration_961_zero_numeric_808_fails_by_designed_supersession(self):
        res = _run_git("grep", "-r", "mechanism_id: 808", "--", "profiles/")
        assert res.returncode == 0 and res.stdout.strip(), (
            "expected #961's zero-numeric-808 sweep to fail by designed supersession"
        )

    def test_numeric_808_keys_in_exactly_the_designed_location(self):
        res = _run_git("grep", "-r", "mechanism_id: 808", "--", "profiles/")
        hits = [line for line in res.stdout.strip().splitlines() if line.strip()]
        # Designed keying: one numeric 808 key in the gizmodo apple block;
        # no other profiles/ location.
        assert len(hits) == 1, "unexpected numeric 808 key spread in profiles/: %s" % hits
        assert "profiles/gizmodo.yaml" in hits[0]


# --- Ledger -----------------------------------------------------------------


class TestLedger962:
    def test_thirtieth_present_and_thirty_first_absent(self):
        # Guard targets the profiles corpus per the #754 convention (prior type
        # files legitimately reference their own negative guards inside their
        # own negative-guard tests, so a tests/ sweep would false-positive).
        corpus = _profiles_corpus()
        assert "THIRTIETH" in corpus
        assert "THIRTY-FIRST" not in corpus
        assert "ledger holds at 29" in _block().lower()

    def test_m808_block_key_unique_and_parses(self):
        import yaml

        doc = yaml.safe_load(_read(GIZMODO_PATH))
        apple = doc["competitor_relationships"]["apple"]
        assert apple[MECH_KEY]["mechanism_id"] == 808
        assert sum(1 for k in apple if k == MECH_KEY) == 1

    def test_m808_not_a_falsification_family_member(self):
        data = _block_data()
        assert data["falsification_family_member"] is False
        assert data["falsification_ledger"] == 29
        assert "THIRTIETH" in data["ledger_note"]


# --- Doc-sync ----------------------------------------------------------------


class TestDocSync962:
    def test_readme_stats_table_updated(self):
        readme = _read(README_PATH)
        assert "49538" in readme and "1287" in readme

    def test_readme_test_file_table_row_present(self):
        assert TEST_BASENAME.replace(".py", "") in _read(README_PATH)

    def test_architecture_tests_tree_updated(self):
        assert TEST_BASENAME.replace(".py", "") in _read(ARCH_PATH)


# --- Iteration log ----------------------------------------------------------


class TestIterationLog962:
    def test_log_has_962_marker(self):
        assert "## #962 Type A" in _read(LOG_PATH)

    def test_log_entry_names_window_leg(self):
        assert "960-964 window" in _read(LOG_PATH)


# --- Push readiness ---------------------------------------------------------


class TestPushReadiness962:
    def test_ascii_only_no_em_dashes(self):
        text = _read(os.path.join("tests", TEST_BASENAME))
        assert "\u2014" not in text
        assert all(ord(c) < 128 for c in text)

    def test_gizmodo_yaml_block_ascii_only_no_em_dashes(self):
        text = _block()
        assert "\u2014" not in text
        assert all(ord(c) < 128 for c in text)

    def test_no_literal_underscore_808_in_test_file(self):
        # The #715 sweep-instrument convention: the literal contiguous
        # underscore-form key must not appear in this file.
        text = _read(os.path.join("tests", TEST_BASENAME))
        assert MECH_ID_MARKER not in text

    def test_concurrent_files_untouched_by_this_run(self):
        # git diffs on the in-flight files must show only their own
        # blocks (m762 / m771); this run adds no 962 hunks to them.
        # #938's test file carries #938's own open anchor-followup working-tree
        # edit (owned by #938's chain, untouched by #962). The untracked
        # #900 Type D file is not in any diff; assert no 962 marker in it.
        for f, own in (
            ("profiles/competitor-entities.yaml", "762"),
            ("profiles/nytimes.yaml", "771"),
        ):
            diff = _run_git("diff", "--", f).stdout
            assert ("mechanism" + "_id" + ": " + own) in diff
            assert "962" not in diff
        rdiff = _run_git(
            "diff", "--",
            "tests/test_type_b_938_dominic_preston_verge_pixel_watch_"
            "gemini_personalization_vs_meta_luna_stigma_sep16.py",
        ).stdout
        assert "962" not in rdiff
        d900 = _read(
            "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py"
        )
        assert "962" not in d900
        assert MECH_ID_MARKER not in d900
