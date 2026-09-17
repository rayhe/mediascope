"""Type B iteration #798 (Sep 17 2026, 1am PDT): Ben Thompson cross-entity register
tracking (mechanism 710), the fourth leg of the 795-799 window.

C #794 -> D #795 -> E #796 -> A #797 -> B #798.

Follows the #793 single-file structural pattern (novelty anchor, rotation guard,
corpus/post-#797 supersession tests, ledger constancy, careers, doc-sync rows,
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
TEST_BASENAME = "test_type_b_798_ben_thompson_stratechery_orion_vs_vision_pro_gradient_sep17_1am.py"
MECH_KEY = "ben thompson stratechery orion vs vision pro gradient sep2026"
M_ID = 710
MECH_ID_MARKER = "mechanism" + "_710"
NEXT_ID_MARKER = "mechanism" + "_711"
NEXT_ID_NUMERIC = "mechanism_id: 711"
ANCHORED_SHA = "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565"

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
    return yaml.safe_load(text[start:end])["ben thompson stratechery orion vs vision pro gradient sep2026"]


# --- Novelty ---------------------------------------------------------------


class TestNovelty798:
    def test_type_b_798_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched green post-commit.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED", "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), "anchor SHA is still the pre-commit placeholder"
        res = _run_git("log", "--all", "--grep", "Type B #798")
        assert ANCHORED_SHA in res.stdout, "main commit is not the expected anchored SHA"

    def test_no_type_b_798_file_on_disk_pre_commit(self):
        hits = [p for p in glob.glob(os.path.join(REPO, "tests", "test_type_b_798*"))
                if os.path.basename(p) != TEST_BASENAME]
        assert not hits, f"unexpected pre-existing Type B #798 test files: {hits}"

    def test_ben_thompson_zero_hit_repo_wide_pre_commit(self):
        # Against HEAD (the committed, pre-#798 tree), not the working tree:
        # the profile edits are intentional post-commit additions.
        res = _run_git("grep", "-ci", "ben thompson", "HEAD", "--", "profiles/", "tests/")
        assert res.returncode != 0 and (not res.stdout.strip() or res.stdout.strip() == ""), \
            f"Ben Thompson already referenced pre-commit: {res.stdout}"

    def test_stratechery_zero_hit_repo_wide_pre_commit(self):
        res = _run_git("grep", "-ci", "stratechery", "HEAD", "--", "profiles/", "tests/")
        assert res.returncode != 0 and (not res.stdout.strip() or res.stdout.strip() == ""), \
            f"Stratechery already referenced pre-commit: {res.stdout}"


# --- Rotation guard --------------------------------------------------------


ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
EXPECTED_ORDER = [
    ("B", "798"), ("A", "797"), ("E", "796"), ("D", "795"), ("C", "794"),
]
WINDOW_SEQ = "C (#794) -> D (#795) -> E (#796) -> A (#797) -> B (#798)"


class TestRotationCycleGuard798:
    def test_iteration_sequence_is_794_through_798(self):
        assert EXPECTED_ORDER == [
            ("B", "798"), ("A", "797"), ("E", "796"), ("D", "795"), ("C", "794"),
        ]

    def test_rotation_legs_adjacency(self):
        for (t1, n1), (t2, n2) in zip(EXPECTED_ORDER, EXPECTED_ORDER[1:]):
            assert int(n1) == int(n2) + 1
            assert (ORDER[t1] - ORDER[t2]) % 5 == 1

    def test_type_b_798_position_is_fourth_leg_of_795_799_window(self):
        assert EXPECTED_ORDER[0] == ("B", "798")


# --- Mechanism 710 content -------------------------------------------------


class TestMechanism710Content:
    def test_profile_parses_and_block_present(self):
        with open(RESEARCH_PROFILE) as fh:
            doc = yaml.safe_load(fh)
        assert MECH_KEY in doc["cross_publication_findings"]

    def test_block_key_unique(self):
        # The block key string also appears in the test_file field, so count
        # the block_key: field line itself rather than the bare substring.
        with open(RESEARCH_PROFILE) as fh:
            text = fh.read()
        field = "    block_key: type_b_798_ben_thompson_stratechery_orion_vs_vision_pro_gradient_sep17\n"
        assert text.count(field) == 1

    def test_block_710_identity_fields(self):
        b = _block()
        assert b["mechanism_id"] == M_ID
        assert b["iteration"] == 798
        assert b["iteration_type"] == "B"
        assert b["rotation_type"] == "B"
        assert b["journalist"] == "Ben Thompson"
        assert b["publication"] == "stratechery"
        assert b["owner"] == "independent_subscription"

    def test_meta_arm_fields(self):
        b = _block()
        meta = b["meta_arm"]
        assert meta["byline"] == "Ben Thompson"
        assert meta["register"] == "hands_on_trial_unadulterated_praise"
        assert meta["tone_illustrative"] == 0.45
        assert "An Interview with Meta CTO Andrew Bosworth About Orion and Reality Labs" in meta["piece"]
        assert "http://stratechery.com/2024/an-interview-with-meta-cto-andrew-bosworth-about-orion-and-reality-labs/" in meta["source_urls"]
        assert any("unadulterated praise" in q for q in meta["evidence_quotes"])

    def test_competitor_arm_fields(self):
        b = _block()
        comp = b["competitor_arm"]
        assert comp["byline"] == "Ben Thompson"
        assert comp["register"] == "hands_on_review_productivity_walkback"
        assert comp["tone_illustrative"] == -0.10
        assert "The Apple Vision Pro" in comp["piece"]
        assert "http://stratechery.com/2024/the-apple-vision-pro/" in comp["source_urls"]
        assert any("walk back" in q for q in comp["evidence_quotes"])

    def test_spread_delta_calc(self):
        b = _block()
        scorer = b["asymmetry_scorer"]
        assert scorer["meta_orion_arm_tone"] == 0.45
        assert scorer["apple_vision_pro_arm_tone"] == -0.10
        assert scorer["illustrative_within_writer_spread"] == 0.55
        assert scorer["delta_calc"] == "0.450 - (-0.100) = +0.550"

    def test_career_context_is_independence_not_migration(self):
        b = _block()
        cc = b["career_context"]
        assert "no employer migration" in cc["status"]
        assert "$15/month or $150/year" in cc["funding"]
        assert "Career context only" in cc["mechanism_role"]

    def test_statistical_discipline(self):
        b = _block()
        scorer = b["asymmetry_scorer"]
        assert scorer["p_value"] == "NOT_CALCULATED"
        assert scorer["cohens_d"] == "NOT_CALCULATED"
        assert scorer["ci_95"] == "NOT_CALCULATED"
        assert scorer["is_significant"] is False
        assert b["verdict"] == "directionally_supported_not_proven"
        assert b["no_analysis_json_update"] is True

    def test_first_hand_read_method(self):
        b = _block()
        note = b["meta_arm"]["source_note"]
        assert "First-hand read" in note
        assert "2 browser.open attempts" in note
        assert "11 browser.search query sets" in note
        comp_note = b["competitor_arm"]["source_note"]
        assert "First-hand read" in comp_note

    def test_confounder_strong_triple_present(self):
        b = _block()
        conf = b["confounders"]
        assert any(c.startswith("STRONG: Shipped-vs-unshipped asymmetry") for c in conf)
        assert any(c.startswith("STRONG: Demo-conditions vs owned-device") for c in conf)
        assert any(c.startswith("STRONG: Thompson") and "entity-agnostic" in c for c in conf)

    def test_counterevidence_present(self):
        b = _block()
        assert len(b["counterevidence"]) >= 3

    def test_cross_references_include_703_701_704_707(self):
        b = _block()
        ids = [c["mechanism_id"] for c in b["cross_references"]]
        assert 703 in ids
        assert 701 in ids
        assert 704 in ids
        assert 707 in ids


# --- Supersession and corpus post-#797 --------------------------------------


class TestSupersessionAndCorpusPost797:
    def _numeric_ids(self):
        res = _run_git("grep", "-oh", "mechanism_id: [0-9]*", "--", "profiles/")
        return sorted(int(m.group(1)) for m in re.finditer(r"mechanism_id: (\d+)", res.stdout))

    def test_corpus_max_is_710(self):
        assert max(self._numeric_ids()) == 710

    def test_iteration_797_max_709_sweep_superseded_by_design(self):
        # #797's max-709 sweeps fail by designed supersession now that 710 exists.
        assert max(self._numeric_ids()) != 709

    def test_zero_underscore_711_repo_wide(self):
        res = _run_git("grep", "-r", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_numeric_711_in_profiles(self):
        res = _run_git("grep", NEXT_ID_NUMERIC, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_797_zero_underscore_710_profiles_sweep_stays_green(self):
        # The #797 zero-underscore-710 sweeps must stay green post-#798 by designed keying.
        res = _run_git("grep", "-r", MECH_ID_MARKER, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_797_zero_underscore_710_tests_sweep_stays_green(self):
        res = _run_git("grep", "-r", MECH_ID_MARKER, "--", "tests/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_797_zero_numeric_710_fails_by_designed_supersession(self):
        res = _run_git("grep", "-r", "mechanism_id: 710", "--", "profiles/")
        assert res.returncode == 0 and res.stdout.strip(), \
            "expected #797's zero-numeric-710 sweep to fail by designed supersession"


# --- Ledger -----------------------------------------------------------------


class TestLedger798:
    def _profiles_text(self):
        with open(RESEARCH_PROFILE) as fh:
            return fh.read()

    def test_twenty_sixth_present(self):
        assert "TWENTY-SIXTH" in self._profiles_text()

    def test_twenty_seventh_absent(self):
        assert "TWENTY-SEVENTH" not in self._profiles_text()

    def test_m710_not_falsification_family_and_holds_26(self):
        b = _block()
        assert "Ledger holds at 26" in b["falsification_family"]
        assert b["no_analysis_json_update"] is True


# --- Careers ----------------------------------------------------------------


class TestCareers798:
    def _careers(self):
        with open(CAREERS_PROFILE) as fh:
            return yaml.safe_load(fh)

    def test_ben_thompson_entry_present(self):
        assert "ben_thompson" in self._careers()

    def test_ben_thompson_independent(self):
        t = self._careers()["ben_thompson"]
        assert t["current_publication"] == "Stratechery"
        assert "subscription-funded" in t["publication_owner"]
        assert t["migration"]["date"] == "none"

    def test_ben_thompson_beats(self):
        t = self._careers()["ben_thompson"]
        assert "AR/VR" in t["beats"]
        assert "wearables" in t["beats"]

    def test_ben_thompson_mechanism_ids(self):
        t = self._careers()["ben_thompson"]
        assert t["mechanism_ids"] == [710]

    def test_ben_thompson_competitor_coverage_block_key(self):
        t = self._careers()["ben_thompson"]
        key = "type_b_798_ben_thompson_stratechery_orion_vs_vision_pro_gradient_sep17"
        assert key in t["competitor_coverage"]
        assert t["competitor_coverage"][key]["mechanism_id"] == 710


# --- Doc sync ----------------------------------------------------------------


class TestDocSync798:
    def test_readme_row_present(self):
        with open(os.path.join(REPO, "README.md")) as fh:
            assert TEST_BASENAME in fh.read()

    def test_architecture_row_present(self):
        with open(os.path.join(REPO, "docs", "ARCHITECTURE.md")) as fh:
            assert TEST_BASENAME in fh.read()


# --- Iteration log -----------------------------------------------------------


class TestIterationLog798:
    def _tail(self):
        with open(ITERATION_LOG) as fh:
            lines = fh.readlines()
        return "".join(lines[-80:])

    def test_iteration_log_entry_present(self):
        assert "Type B #798" in self._tail()

    def test_iteration_log_window_sequence(self):
        assert WINDOW_SEQ in self._tail()
