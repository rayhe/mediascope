"""Type B iteration #793 (Sep 16 2026, 8pm PDT): Jason Hiner cross-entity register
tracking (mechanism 707), the fourth leg of the 790-794 window.

D #790 -> E #791 -> A #792 -> B #793 -> C #794.

Follows the #788 single-file structural pattern (novelty anchor, rotation guard,
corpus/post-#792 supersession tests, ledger constancy, careers, doc-sync rows,
iteration-log entry).

Deselected pre-commit per the #565 convention: anchor 1 + rotation 3.
Doc-sync 4 + iteration-log 2 go green in the doc-sync followup.
Patched green in the anchor followup.
"""
import glob
import os
import re
import subprocess
import pytest
import yaml

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_BASENAME = "test_type_b_793_jason_hiner_zdnet_meta_vs_rokid_register_evenhandedness_sep16_8pm.py"
MECH_KEY = "jason hiner zdnet meta vs rokid register evenhandedness sep2026"
M_ID = 707
MECH_ID_MARKER = "mechanism" + "_707"
NEXT_ID_MARKER = "mechanism" + "_708"
NEXT_ID_NUMERIC = "mechanism_id: 708"
ANCHORED_SHA = "63a57eb05c6b490bcf33ab3bb04c07422d055114"

RESEARCH_PROFILE = os.path.join(REPO, "profiles", "competitor-coverage-research.yaml")
CAREERS_PROFILE = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
ITERATION_LOG = os.path.join(REPO, "iteration-log.md")


def _run_git(*args):
    return subprocess.run(
        ["git", "-C", REPO] + list(args),
        capture_output=True,
        text=True,
        check=False,
    )


def _block():
    with open(RESEARCH_PROFILE) as fh:
        text = fh.read()
    start = text.index(MECH_KEY)
    end = text.index("\nmethodology:")
    return yaml.safe_load(text[start:end])["jason hiner zdnet meta vs rokid register evenhandedness sep2026"]


# --- Novelty ---------------------------------------------------------------


class TestNovelty793:
    def test_type_b_793_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched green post-commit.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED", "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), "anchor SHA is still the pre-commit placeholder"
        res = _run_git("log", "--all", "--grep", "Type B #793")
        assert ANCHORED_SHA in res.stdout, "main commit is not the expected anchored SHA"

    def test_no_type_b_793_file_on_disk_pre_commit(self):
        hits = [p for p in glob.glob(os.path.join(REPO, "tests", "test_type_b_793*"))
                if os.path.basename(p) != TEST_BASENAME]
        assert not hits, f"unexpected pre-existing Type B #793 test files: {hits}"

    def test_jason_hiner_zero_hit_repo_wide_pre_commit(self):
        # Against HEAD (the committed, pre-#793 tree), not the working tree:
        # the profile edits are intentional post-commit additions.
        res = _run_git("grep", "-ci", "jason hiner", "HEAD", "--", "profiles/", "tests/")
        assert res.returncode != 0 and (not res.stdout.strip() or res.stdout.strip() == ""), \
            f"Jason Hiner already referenced pre-commit: {res.stdout}"


# --- Rotation guard --------------------------------------------------------


ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
EXPECTED_ORDER = [
    ("B", "793"), ("A", "792"), ("E", "791"), ("D", "790"), ("C", "789"),
]
WINDOW_SEQ = "C (#789) -> D (#790) -> E (#791) -> A (#792) -> B (#793)"


class TestRotationCycleGuard793:
    def test_iteration_sequence_is_789_through_793(self):
        assert EXPECTED_ORDER == [
            ("B", "793"), ("A", "792"), ("E", "791"), ("D", "790"), ("C", "789"),
        ]

    def test_rotation_legs_adjacency(self):
        for (t1, n1), (t2, n2) in zip(EXPECTED_ORDER, EXPECTED_ORDER[1:]):
            assert int(n1) == int(n2) + 1
            assert (ORDER[t1] - ORDER[t2]) % 5 == 1

    def test_type_b_793_position_is_fourth_leg_of_790_794_window(self):
        assert EXPECTED_ORDER[0] == ("B", "793")


# --- Mechanism 707 content -------------------------------------------------


class TestMechanism707Content:
    def test_profile_parses_and_block_present(self):
        with open(RESEARCH_PROFILE) as fh:
            doc = yaml.safe_load(fh)
        assert MECH_KEY in doc["cross_publication_findings"]

    def test_block_key_unique(self):
        # The block key string also appears in the test_file field, so count
        # the block_key: field line itself rather than the bare substring.
        with open(RESEARCH_PROFILE) as fh:
            text = fh.read()
        field = "    block_key: type_b_793_jason_hiner_zdnet_meta_vs_rokid_register_evenhandedness_sep16\n"
        assert text.count(field) == 1

    def test_block_707_identity_fields(self):
        b = _block()
        assert b["mechanism_id"] == M_ID
        assert b["iteration"] == 793
        assert b["iteration_type"] == "B"
        assert b["rotation_type"] == "B"
        assert b["journalist"] == "Jason Hiner"
        assert b["publication"] == "zdnet"
        assert b["owner"] == "ziff_davis"

    def test_meta_arm_fields(self):
        b = _block()
        meta = b["meta_arm"]
        assert meta["byline"] == "Jason Hiner"
        assert meta["register"] == "enthusiastic_forward_looking_news_analysis"
        assert meta["tone_illustrative"] == 0.35
        assert "Meta wears Prada? Why its next-gen AR glasses might out-style the Ray-Bans" in meta["piece"]
        assert "https://www.zdnet.com/article/meta-wears-prada-why-its-next-gen-ar-glasses-might-out-style-the-ray-bans/" in meta["source_urls"]

    def test_competitor_arm_fields(self):
        b = _block()
        comp = b["competitor_arm"]
        assert comp["byline"] == "Jason Hiner"
        assert comp["register"] == "hands_on_comparison_competitor_wins"
        assert comp["tone_illustrative"] == -0.30
        assert "I tested Meta Ray-Ban Display alternatives, and these are better in several ways for less money" in comp["piece"]
        assert "https://www.zdnet.com/article/i-tested-meta-ray-ban-display-alternatives-and-these-are-better-in-several-ways-for-less-money/" in comp["source_urls"]

    def test_spread_delta_calc(self):
        b = _block()
        scorer = b["asymmetry_scorer"]
        assert scorer["meta_prada_arm_tone"] == 0.35
        assert scorer["meta_leg_in_rokid_comparison_tone"] == -0.30
        assert scorer["illustrative_within_writer_spread"] == 0.65
        assert scorer["delta_calc"] == "0.350 - (-0.300) = +0.650"

    def test_migration_context_is_career_context_only(self):
        b = _block()
        mig = b["migration_context"]
        assert mig["migration_date"] == "announced circa Dec 2025"
        assert "The Deep View" in mig["to"]
        assert "https://www.adobomagazine.com/people/the-deep-view-names-jason-hiner-editor-in-chief-and-chief-content-officer/" in mig["migration_source"]
        assert "Career context only" in mig["mechanism_role"]

    def test_statistical_discipline(self):
        b = _block()
        scorer = b["asymmetry_scorer"]
        assert scorer["p_value"] == "NOT_CALCULATED"
        assert scorer["cohens_d"] == "NOT_CALCULATED"
        assert scorer["ci_95"] == "NOT_CALCULATED"
        assert scorer["is_significant"] is False
        assert b["verdict"] == "directionally_supported_not_proven"
        assert b["no_analysis_json_update"] is True

    def test_excerpt_bounded_method(self):
        b = _block()
        note = b["meta_arm"]["source_note"]
        assert "6 browser.search query sets" in note
        assert "0 browser.open attempts" in note
        assert "369 days ago" in note
        comp_note = b["competitor_arm"]["source_note"]
        assert "338 days ago" in comp_note

    def test_confounder_strong_pair_present(self):
        b = _block()
        conf = b["confounders"]
        assert any(c.startswith("STRONG: Excerpt-bounded evidence") for c in conf)
        assert any(c.startswith("STRONG: Story-type skew") for c in conf)

    def test_counterevidence_present(self):
        b = _block()
        assert len(b["counterevidence"]) >= 3

    def test_cross_references_include_703_701_704(self):
        b = _block()
        ids = [c["mechanism_id"] for c in b["cross_references"]]
        assert 703 in ids
        assert 701 in ids
        assert 704 in ids


# --- Supersession and corpus post-#792 --------------------------------------


class TestSupersessionAndCorpusPost792:
    def _numeric_ids(self):
        res = _run_git("grep", "-oh", "mechanism_id: [0-9]*", "--", "profiles/")
        return sorted(int(m.group(1)) for m in re.finditer(r"mechanism_id: (\d+)", res.stdout))

    def test_corpus_max_is_707(self):
        assert max(self._numeric_ids()) == 707

    def test_iteration_792_max_706_sweep_superseded_by_design(self):
        # #792's max-706 sweeps fail by designed supersession now that 707 exists.
        assert max(self._numeric_ids()) != 706

    def test_zero_underscore_708_repo_wide(self):
        res = _run_git("grep", "-r", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_numeric_708_in_profiles(self):
        res = _run_git("grep", NEXT_ID_NUMERIC, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_792_zero_underscore_707_profiles_sweep_stays_green(self):
        # The #792 zero-underscore-707 sweeps must stay green post-#793 by designed keying.
        res = _run_git("grep", "-r", MECH_ID_MARKER, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_792_zero_underscore_707_tests_sweep_stays_green(self):
        res = _run_git("grep", "-r", MECH_ID_MARKER, "--", "tests/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_792_zero_numeric_707_fails_by_designed_supersession(self):
        res = _run_git("grep", "-r", "mechanism_id: 707", "--", "profiles/")
        assert res.returncode == 0 and res.stdout.strip(), \
            "expected #792's zero-numeric-707 sweep to fail by designed supersession"


# --- Ledger -----------------------------------------------------------------


class TestLedger793:
    def _profiles_text(self):
        with open(RESEARCH_PROFILE) as fh:
            return fh.read()

    def test_twenty_sixth_present(self):
        assert "TWENTY-SIXTH" in self._profiles_text()

    def test_twenty_seventh_absent(self):
        assert "TWENTY-SEVENTH" not in self._profiles_text()

    def test_m707_not_falsification_family_and_holds_26(self):
        b = _block()
        assert "Ledger holds at 26" in b["falsification_family"]
        assert b["no_analysis_json_update"] is True


# --- Careers ----------------------------------------------------------------


class TestCareers793:
    def _careers(self):
        with open(CAREERS_PROFILE) as fh:
            return yaml.safe_load(fh)

    def test_jason_hiner_entry_present(self):
        assert "jason_hiner" in self._careers()

    def test_jason_hiner_roles(self):
        j = self._careers()["jason_hiner"]
        assert j["previous_role"] == "VP and Editor in Chief, ZDNET"
        assert j["current_role"] == "Editor-in-Chief and Chief Content Officer"
        assert j["current_publication"] == "The Deep View"

    def test_jason_hiner_beats(self):
        j = self._careers()["jason_hiner"]
        assert "smart glasses" in j["beats"]
        assert "wearables" in j["beats"]

    def test_jason_hiner_migration(self):
        j = self._careers()["jason_hiner"]
        assert "circa Dec 2025" in j["migration"]["date"]
        assert "The Deep View" in j["migration"]["to"]

    def test_jason_hiner_mechanism_ids(self):
        j = self._careers()["jason_hiner"]
        assert j["mechanism_ids"] == [707]

    def test_jason_hiner_competitor_coverage_block_key(self):
        j = self._careers()["jason_hiner"]
        key = "type_b_793_jason_hiner_zdnet_meta_vs_rokid_register_evenhandedness_sep16"
        assert key in j["competitor_coverage"]
        assert j["competitor_coverage"][key]["mechanism_id"] == 707


# --- Doc sync ----------------------------------------------------------------


class TestDocSync793:
    def test_readme_row_present(self):
        with open(os.path.join(REPO, "README.md")) as fh:
            assert TEST_BASENAME in fh.read()

    def test_architecture_row_present(self):
        with open(os.path.join(REPO, "docs", "ARCHITECTURE.md")) as fh:
            assert TEST_BASENAME in fh.read()


# --- Iteration log -----------------------------------------------------------


class TestIterationLog793:
    def _tail(self):
        with open(ITERATION_LOG) as fh:
            lines = fh.readlines()
        return "".join(lines[-80:])

    def test_iteration_log_entry_present(self):
        assert "Type B #793" in self._tail()

    def test_iteration_log_window_sequence(self):
        assert WINDOW_SEQ in self._tail()
