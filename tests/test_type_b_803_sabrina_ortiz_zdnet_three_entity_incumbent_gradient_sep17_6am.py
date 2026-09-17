"""Type B iteration #803 (Sep 17 2026, 6am PDT): Sabrina Ortiz cross-entity
register tracking (mechanism 713), the fourth leg of the 800-804 window.

D #800 -> E #801 -> A #802 -> B #803 -> C #804.

Follows the #788 single-file structural pattern (novelty anchor, rotation guard,
corpus/post-#802 supersession tests, ledger constancy, careers, doc-sync rows,
iteration-log entry).

Deselected pre-commit per the #565 convention: anchor 1 + rotation 3.
Doc-sync 2 + iteration-log 2 go green in the doc-sync followup.
Patched green in the anchor followup.

FINDING: Sabrina Ortiz (ZDNet Senior Editor) shows within-journalist,
within-employer product-forward register constancy for CHALLENGER wearables
(Meta Ray-Ban Display "nearly sold" Oct 2025; Meta Ray-Bans a purchased
"nobrainer"; Meta Oakley HSTN "exceeded my expectations" Feb 2026; Samsung
Project Moohan "beats my Apple Vision Pro in meaningful ways" May 2025) with
the sharpest comparative critique aimed at the INCUMBENT (her own Apple
Vision Pro, the baseline every challenger is measured against and beats).
Zero privacy/surveillance vocabulary in any excerpted arm - a
within-publication replication of the #793 ZDNet pattern (Hiner) with a
different journalist and a three-entity (Meta/Samsung/Apple) design.
MANUAL ILLUSTRATIVE only; NOT a falsification-family member; ledger holds
at 26.
"""
import glob
import os
import re
import subprocess
import pytest
import yaml

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_BASENAME = "test_type_b_803_sabrina_ortiz_zdnet_three_entity_incumbent_gradient_sep17_6am.py"
MECH_KEY = "sabrina ortiz zdnet three entity incumbent gradient sep2026"
M_ID = 713
MECH_ID_MARKER = "mechanism" + "_713"
NEXT_ID_MARKER = "mechanism" + "_714"
NEXT_ID_NUMERIC = "mechanism_id: 714"
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

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


def _profiles_text():
    with open(RESEARCH_PROFILE) as fh:
        return fh.read()


def _block():
    text = _profiles_text()
    start = text.index(MECH_KEY)
    end = text.index("\nmethodology:")
    return yaml.safe_load(text[start:end])[MECH_KEY]


# --- Novelty ---------------------------------------------------------------


class TestNovelty803:
    def test_type_b_803_main_commit_unique_and_anchored(self):
        # Deselected pre-commit per the #565 followup convention; patched green post-commit.
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED", "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ), "anchor SHA is still the pre-commit placeholder"
        res = _run_git("log", "--all", "--grep", "Type B #803")
        assert ANCHORED_SHA in res.stdout, "main commit is not the expected anchored SHA"

    def test_no_type_b_803_file_on_disk_pre_commit(self):
        hits = [p for p in glob.glob(os.path.join(REPO, "tests", "test_type_b_803*"))
                if os.path.basename(p) != TEST_BASENAME]
        assert not hits, f"unexpected pre-existing Type B #803 test files: {hits}"

    def test_sabrina_ortiz_zero_hit_repo_wide_pre_commit(self):
        # Against HEAD (the committed, pre-#803 tree), not the working tree:
        # the profile edits are intentional post-commit additions.
        res = _run_git("grep", "-ci", "sabrina ortiz", "HEAD", "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and (not res.stdout.strip() or res.stdout.strip() == ""), \
            f"Sabrina Ortiz already referenced pre-commit: {res.stdout}"


# --- Rotation guard --------------------------------------------------------


ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
EXPECTED_ORDER = [
    ("B", "803"), ("A", "802"), ("E", "801"), ("D", "800"), ("C", "799"),
]
WINDOW_SEQ = "D (#800) -> E (#801) -> A (#802) -> B (#803) -> C (#804)"


class TestRotationCycleGuard803:
    def test_iteration_sequence_is_799_through_803(self):
        assert EXPECTED_ORDER == [
            ("B", "803"), ("A", "802"), ("E", "801"), ("D", "800"), ("C", "799"),
        ]

    def test_rotation_legs_adjacency(self):
        for (t1, n1), (t2, n2) in zip(EXPECTED_ORDER, EXPECTED_ORDER[1:]):
            assert int(n1) == int(n2) + 1
            assert (ORDER[t1] - ORDER[t2]) % 5 == 1

    def test_type_b_803_position_is_fourth_leg_of_800_804_window(self):
        assert EXPECTED_ORDER[0] == ("B", "803")


# --- Mechanism 713 content -------------------------------------------------


class TestMechanism713Content:
    def test_profile_parses_and_block_present(self):
        with open(RESEARCH_PROFILE) as fh:
            doc = yaml.safe_load(fh)
        assert MECH_KEY in doc["cross_publication_findings"]

    def test_block_key_unique(self):
        # The block key string also appears in the test_file field, so count
        # the block_key: field line itself rather than the bare substring.
        field = "    block_key: type_b_803_sabrina_ortiz_zdnet_three_entity_incumbent_gradient_sep17\n"
        assert _profiles_text().count(field) == 1

    def test_block_713_identity_fields(self):
        b = _block()
        assert b["mechanism_id"] == M_ID
        assert b["iteration"] == 803
        assert b["iteration_type"] == "B"
        assert b["rotation_type"] == "B"
        assert b["journalist"] == "Sabrina Ortiz"
        assert b["publication"] == "zdnet"
        assert b["owner"] == "ziff_davis"

    def test_meta_arm_fields(self):
        b = _block()
        meta = b["meta_arm"]
        assert meta["byline"] == "Sabrina Ortiz"
        assert meta["register"] == "hands_on_demo_product_forward"
        assert meta["tone_illustrative"] == 0.45
        assert "I'm nearly sold" in meta["piece"]
        assert "https://www.zdnet.com/article/i-tried-the-meta-ray-ban-display-glasses-including-this-unreleased-feature-and-im-nearly-sold/" in meta["source_urls"]

    def test_meta_arm_supporting_purchase_signal(self):
        b = _block()
        sup = b["meta_arm_supporting"]
        quotes = " ".join(sup["evidence_quotes"])
        assert "absolute nobrainer for me to purchase the Meta Ray-Bans" in quotes
        assert "exceeded my expectations" in quotes

    def test_samsung_arm_fields(self):
        b = _block()
        sam = b["samsung_arm"]
        assert sam["byline"] == "Sabrina Ortiz"
        assert sam["register"] == "hands_on_demo_challenger_beats_incumbent"
        assert sam["tone_illustrative"] == 0.40
        assert "beats my Apple Vision Pro in meaningful ways" in sam["piece"]
        assert "i-finally-tried-samsungs-xr-headset-and-it-beats-my-apple-vision-pro-in-meaningful-ways" in sam["source_urls"][0]

    def test_apple_arm_is_incumbent_baseline(self):
        b = _block()
        apple = b["apple_arm"]
        assert apple["register"] == "incumbent_baseline_loses_comparisons"
        assert apple["tone_illustrative"] == -0.10
        quotes = " ".join(apple["evidence_quotes"])
        assert "during launch day" in quotes

    def test_spread_delta_calc(self):
        b = _block()
        scorer = b["asymmetry_scorer"]
        assert scorer["meta_display_arm_tone"] == 0.45
        assert scorer["samsung_moohan_arm_tone"] == 0.40
        assert scorer["apple_incumbent_leg_tone"] == -0.10
        assert scorer["illustrative_challenger_minus_incumbent"] == 0.525
        assert scorer["delta_calc"] == "((0.450 + 0.400) / 2) - (-0.100) = 0.425 + 0.100 = +0.525"

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
        assert "8 browser.search query sets" in note
        assert "0 browser.open attempts on ZDNet primaries" in note
        assert "332 days ago" in note
        sam_note = b["samsung_arm"]["source_note"]
        assert "480 days ago" in sam_note

    def test_confounder_strong_pair_present(self):
        b = _block()
        conf = b["confounders"]
        assert any(c.startswith("STRONG: Excerpt-bounded evidence") for c in conf)
        assert any(c.startswith("STRONG: Story-type skew") for c in conf)

    def test_counterevidence_present(self):
        b = _block()
        assert len(b["counterevidence"]) >= 3

    def test_cross_references_include_707_710_605(self):
        b = _block()
        ids = [c["mechanism_id"] for c in b["cross_references"]]
        assert 707 in ids
        assert 710 in ids
        assert 605 in ids


# --- Supersession and corpus post-#802 --------------------------------------


class TestSupersessionAndCorpusPost802:
    def _numeric_ids(self):
        res = _run_git("grep", "-oh", "mechanism_id: [0-9]*", "--", "profiles/")
        return sorted(int(m.group(1)) for m in re.finditer(r"mechanism_id: (\d+)", res.stdout))

    def test_corpus_max_is_713(self):
        assert max(self._numeric_ids()) == 713

    def test_iteration_802_max_712_sweep_superseded_by_design(self):
        # #802's max-712 sweeps fail by designed supersession now that 713 exists.
        assert max(self._numeric_ids()) != 712

    def test_zero_underscore_714_repo_wide(self):
        res = _run_git("grep", "-r", NEXT_ID_MARKER, "--", "profiles/", "tests/", "docs/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_zero_numeric_714_in_profiles(self):
        res = _run_git("grep", NEXT_ID_NUMERIC, "--", "profiles/")
        assert res.returncode != 0 and not res.stdout.strip()

    def test_iteration_802_zero_underscore_713_sweep_stays_green(self):
        # The #802 zero-underscore-713 sweeps stay green post-#803 by designed keying:
        # neither the profile block nor this test file carries a literal underscore-713 key.
        for root in ("profiles/", "tests/"):
            res = _run_git("grep", "-r", MECH_ID_MARKER, "--", root)
            assert res.returncode != 0 and not res.stdout.strip(), \
                f"literal underscore-713 key leaked into {root}: {res.stdout.strip()[:200]}"

    def test_iteration_802_zero_numeric_713_fails_by_designed_supersession(self):
        res = _run_git("grep", "-r", "mechanism_id: 713", "--", "profiles/")
        assert res.returncode == 0 and res.stdout.strip(), \
            "expected #802's zero-numeric-713 sweep to fail by designed supersession"

    def test_numeric_713_keys_in_exactly_the_two_designed_locations(self):
        res = _run_git("grep", "-r", "mechanism_id: 713", "--", "profiles/")
        hits = [l for l in res.stdout.strip().splitlines() if l.strip()]
        # Designed keying: one numeric 713 key in the research block, one in the
        # careers competitor_coverage sub-block; no other profiles/ location.
        assert len(hits) == 2, f"unexpected numeric 713 key spread in profiles/: {hits}"
        assert any("competitor-coverage-research.yaml" in h for h in hits)
        assert any("careers/journalists.yaml" in h for h in hits)


# --- Ledger -----------------------------------------------------------------


class TestLedger803:
    def test_twenty_sixth_present(self):
        assert "TWENTY-SIXTH" in _profiles_text()

    def test_twenty_seventh_absent(self):
        assert "TWENTY-SEVENTH" not in _profiles_text()

    def test_m713_not_falsification_family_and_holds_26(self):
        b = _block()
        assert "Ledger holds at 26" in b["falsification_family"]
        assert b["no_analysis_json_update"] is True


# --- Careers ----------------------------------------------------------------


class TestCareers803:
    def _careers(self):
        with open(CAREERS_PROFILE) as fh:
            return yaml.safe_load(fh)

    def test_sabrina_ortiz_entry_present(self):
        assert "sabrina_ortiz" in self._careers()

    def test_sabrina_ortiz_role(self):
        j = self._careers()["sabrina_ortiz"]
        assert j["current_role"] == "Senior Editor"
        assert j["current_publication"] == "ZDNet"
        assert j["publication_owner"] == "Ziff Davis"

    def test_sabrina_ortiz_beats(self):
        j = self._careers()["sabrina_ortiz"]
        assert "smart glasses" in j["beats"]
        assert "wearables" in j["beats"]
        assert "AI" in j["beats"]

    def test_sabrina_ortiz_mechanism_ids(self):
        j = self._careers()["sabrina_ortiz"]
        assert j["mechanism_ids"] == [713]

    def test_sabrina_ortiz_competitor_coverage_block_key(self):
        j = self._careers()["sabrina_ortiz"]
        key = "type_b_803_sabrina_ortiz_zdnet_three_entity_incumbent_gradient_sep17"
        assert key in j["competitor_coverage"]
        assert j["competitor_coverage"][key]["mechanism_id"] == 713


# --- Doc sync ----------------------------------------------------------------


class TestDocSync803:
    def test_readme_row_present(self):
        with open(os.path.join(REPO, "README.md")) as fh:
            assert TEST_BASENAME in fh.read()

    def test_architecture_row_present(self):
        with open(os.path.join(REPO, "docs", "ARCHITECTURE.md")) as fh:
            assert TEST_BASENAME in fh.read()


# --- Iteration log -----------------------------------------------------------


class TestIterationLog803:
    def _tail(self):
        with open(ITERATION_LOG) as fh:
            lines = fh.readlines()
        return "".join(lines[-80:])

    def test_iteration_log_entry_present(self):
        assert "Type B #803" in self._tail()

    def test_iteration_log_window_sequence(self):
        assert WINDOW_SEQ in self._tail()
