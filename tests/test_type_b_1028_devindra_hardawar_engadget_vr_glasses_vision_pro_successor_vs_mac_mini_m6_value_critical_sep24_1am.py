"""Type B #1028: Devindra Hardawar (Engadget) Sep-2026 same-week cross-entity pair - Meta VR Glasses opinion pro-Meta (+0.55) vs Mac Mini M6 review value-critical (+0.10), mechanism 848, Sep 27 2026 01:00 PDT.

Reasoning: 1025-1029 window FOURTH leg (D #1025 -> E #1026 -> A #1027 -> B #1028 -> C #1029, rotation per #565). SECOND dedicated Type B mechanism on Devindra Hardawar (m686/#753 review-register constancy). Two NEW arms, both Engadget, both Hardawar sole byline, three days apart: (a) Meta arm Sep 24 2026 opinion piece "Meta's $1,300 VR Glasses Look Like The Vision Pro Sequel Apple Should Be Making" (first-hand browser.open 64 lines this run; "a true successor to the Vision Pro", "lighter, cheaper and more consumer-friendly", with honest trust caveats); (b) Apple arm Sep 21 2026 Mac Mini M6 review "The best compact desktop is no longer a great deal" (verbatim URL from search Full-URL listing; "loses the fun factor", "a lot less fun", 8.7/10). Finding: Hardawar's pro-Meta XR register holds 2.5 years after m686 and extends from review into opinion/editorial genre - illustrative Meta-minus-Apple delta +0.45, direction-consistent with m686's +0.20. Tests m686's register-constancy prediction: HOLDS. THIRTY-FIRST falsification-family member (ledger 30->31). 13 browser.search query sets + 2 browser.open this run. Max numeric mechanism_id 847 pre-commit -> 848 post-commit; zero next-after-max forms repo-wide (format-built needles, no literals carried, per #715). Block key carries no numeric mechanism-id substring by designed keying. MANUAL ILLUSTRATIVE scoring only; p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant False; engine NOT run; NOT artifact-grade; no analysis.json update. Verdict directionally_supported_not_proven. Doc-sync 3 tests fail pre-commit per #719 (README stats 52769/1352 + new table row; ARCHITECTURE.md tree row). Push-readiness 3: leaner #1021 shape in the anchor followup (ascii-only/no-em-dash, no-blob-url, inflight-concurrency guards; the main-commit-state-only exact-staged-set and hash-placeholder gates do not survive followup state). Rotation 3 marked rotation, anchor 1 marked anchor, both deselected pre-commit.
"""
import glob
import re
import subprocess
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parents[1]
JOURNALISTS_YAML = REPO / "profiles" / "careers" / "journalists.yaml"
THIS_TEST = Path(__file__).name
BLOCK_KEY = (
    "type_b_1028_devindra_hardawar_engadget_vr_glasses_vision_pro_successor_"
    "vs_mac_mini_m6_value_critical_sep24"
)
NEXT_FREE_PRE = 847  # max numeric mechanism_id before this run's insert
THIS_MECH = NEXT_FREE_PRE + 1
THIS_ITER = 1027 + 1
NEXT_AFTER = THIS_MECH + 1  # format-built; no literals carried per #715
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "8f3263e8e077cce9849705a3dbfa61fba8168142"


def _load_block():
    data = yaml.safe_load(JOURNALISTS_YAML.read_text())
    for item in data["journalists"]:
        if isinstance(item, dict) and item.get("name") == "Devindra Hardawar":
            return item["competitor_coverage"][BLOCK_KEY]
    raise KeyError("Devindra Hardawar block not found")


def _hardawar_item():
    data = yaml.safe_load(JOURNALISTS_YAML.read_text())
    for item in data["journalists"]:
        if isinstance(item, dict) and item.get("name") == "Devindra Hardawar":
            return item
    raise KeyError("Devindra Hardawar not found")


def _git(*args):
    return subprocess.run(
        ["git", "-C", str(REPO), *args],
        capture_output=True, text=True, check=False,
    )


class TestNovelty1028:
    """Uniqueness of this run: exactly one test file, no prior Type B #1028 commit."""

    def test_single_type_b_1028_test_file(self):
        hits = sorted(glob.glob(str(REPO / "tests" / "test_type_b_1028_*.py")))
        assert len(hits) == 1, hits
        assert Path(hits[0]).name == THIS_TEST

    def test_no_foreign_type_b_1028_by_commit_time(self):
        """Post-commit form: every "Type B #1028" commit must be this run's own chain."""
        lines = _git("log", "--format=%an <%ae> %s", "--grep", "Type B #1028").stdout.strip().splitlines()
        assert lines, "expected this run's Type B #1028 commits"
        for line in lines:
            assert line.startswith("Ray He <rayche@gmail.com>"), line

    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        """Per #716/#565: ANCHORED_SHA must equal the main commit; fails pre-commit."""
        assert ANCHORED_SHA != "PATCH_ME_IN_FOLLOWUP", "anchor followup not yet applied per #565"
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA
        r = _git("cat-file", "-t", ANCHORED_SHA)
        assert r.stdout.strip() == "commit", ANCHORED_SHA


class TestRotationGuard1028:
    """1025-1029 window: FOURTH leg D->E->A->B->C. Marked tests deselected pre-commit."""

    def test_window_legs_in_iteration_log(self):
        text = (REPO / "iteration-log.md").read_text()
        assert "## #1025 Type D" in text
        assert "## #1026 Type E" in text
        assert "## #1027 Type A" in text
        assert "1025-1029" in text

    @pytest.mark.rotation
    def test_fourth_leg_of_1025_to_1029_window(self):
        text = (REPO / "iteration-log.md").read_text()
        assert "FOURTH leg of the 1025-1029 window" in text

    @pytest.mark.rotation
    def test_predecessor_1027_type_a_committed(self):
        assert _git("log", "--oneline", "--grep", "Type A #1027").stdout.strip() != ""
        assert list((REPO / "tests").glob("test_type_a_1027_*.py"))

    @pytest.mark.rotation
    def test_no_successor_1029_type_c_commit_yet(self):
        out = _git("log", "--oneline", "--grep", "Type C #1029").stdout
        assert out.strip() == "", out


class TestMechanism848Content:
    """Profile block structure and field-level content for mechanism 848."""

    def test_block_key_unique(self):
        text = JOURNALISTS_YAML.read_text()
        assert text.count(BLOCK_KEY + ":") == 1
        assert text.count("block_key: " + BLOCK_KEY) == 1

    def test_mechanism_id_848_iteration_1028_type_b(self):
        b = _load_block()
        assert b["mechanism_id"] == THIS_MECH == NEXT_FREE_PRE + 1
        assert b["iteration"] == THIS_ITER == 1028
        assert b["iteration_type"] == "B"
        assert b["test_file"].endswith(THIS_TEST)

    def test_journalist_and_publication(self):
        jr = _hardawar_item()
        assert jr["name"] == "Devindra Hardawar"
        assert jr["publication"] == "Engadget"
        b = _load_block()
        assert b["new_meta_arm_sep24"]["byline"] == "Devindra Hardawar (sole)"
        assert b["new_apple_arm_sep21"]["byline"] == "Devindra Hardawar (sole)"
        assert b["new_meta_arm_sep24"]["publication"] == "engadget"
        assert b["new_apple_arm_sep21"]["publication"] == "engadget"

    def test_publication_author_goal_job_fields(self):
        b = _load_block()
        assert b["author"] == "Kit (with Ray)"
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["job_id"] == "mediascope-daily-iteration"
        assert b["scheduled_job_id"] == "mediascope-daily-iteration"
        assert b["date"] == "2026-09-27 01:00 PDT"

    def test_key_design_note_no_numeric_substring(self):
        b = _load_block()
        assert str(THIS_MECH) not in BLOCK_KEY
        assert b["key_design_note"].startswith("Colon-form key only")

    def test_connects_to_all_exist_in_profiles(self):
        corpus = ""
        for p in (REPO / "profiles").rglob("*.yaml"):
            corpus += p.read_text()
        for mid in _load_block()["connects_to"]:
            assert ("mechanism_id: %d" % mid in corpus) or ("mechanism: %d" % mid in corpus), mid

    def test_rotation_transparency_names_window_and_predecessor(self):
        rt = _load_block()["rotation_transparency"]
        assert "1025-1029" in rt
        assert "e60a320b" in rt  # #1027 main short sha, predecessor
        assert "14219940" in rt  # #1027 anchor short sha
        assert "#1029 Type C" in rt

    def test_mechanism_ids_list_updated(self):
        assert _hardawar_item()["mechanism_ids"] == [686, THIS_MECH]


class TestEvidence1028:
    """Two NEW same-week arms: dates, URLs, quotes, attestation tiers."""

    def test_two_new_arms_tones(self):
        b = _load_block()
        assert b["new_meta_arm_sep24"]["tone_illustrative"] == pytest.approx(0.55)
        assert b["new_apple_arm_sep21"]["tone_illustrative"] == pytest.approx(0.10)

    def test_meta_arm_url_first_hand(self):
        url = "https://www.engadget.com/2267218/meta-vr-glasses-price-specs-apple-vision-pro-comparison/"
        b = _load_block()
        assert b["new_meta_arm_sep24"]["url"] == url
        assert url in JOURNALISTS_YAML.read_text()
        assert "First-hand browser.open" in b["new_meta_arm_sep24"]["url_attestation"]

    def test_apple_arm_url_verbatim(self):
        url = "https://www.engadget.com/2263471/apple-mac-mini-m6-review/"
        b = _load_block()
        assert b["new_apple_arm_sep21"]["url"] == url
        assert url in JOURNALISTS_YAML.read_text()
        assert "Full-URL listing" in b["new_apple_arm_sep21"]["url_attestation"]

    def test_arm_dates_three_days_apart(self):
        b = _load_block()
        assert b["new_meta_arm_sep24"]["date"] == "2026-09-24"
        assert b["new_apple_arm_sep21"]["date"] == "2026-09-21"

    def test_meta_arm_quotes_present(self):
        quotes = _load_block()["new_meta_arm_sep24"]["evidence_quotes"]
        assert len(quotes) >= 5
        joined = " ".join(quotes)
        assert "true successor to the Vision Pro" in joined
        assert "lighter, cheaper and more consumer-friendly" in joined
        assert "poisoned the idea" in joined

    def test_apple_arm_quotes_present(self):
        quotes = _load_block()["new_apple_arm_sep21"]["evidence_quotes"]
        assert len(quotes) >= 4
        joined = " ".join(quotes)
        assert "loses the fun factor" in joined
        assert "a lot less fun" in joined
        assert "8.7 / 10" in joined

    def test_extends_686_documented(self):
        ext = _load_block()["extends_mechanism_686"]
        assert "HOLDS" in ext["prediction_test"]
        assert "+0.20" in ext["prior"]


class TestScores1028:
    """Illustrative delta: cross-entity +0.45 Meta-favoring."""

    def test_cross_entity_delta_plus_0_45(self):
        r = _load_block()["asymmetry_scorer_result"]
        assert r["illustrative_cross_entity_delta_meta_minus_apple"] == pytest.approx(0.45)
        assert "+0.45" in r["meta_minus_apple_calc"]
        assert "Meta-favoring" in r["cross_entity_delta_direction"]

    def test_no_scorer_run(self):
        r = _load_block()["asymmetry_scorer_result"]
        assert "NOT run" in r["engine"]
        assert "NOT artifact-grade" in r["artifact_grade"]

    def test_scorer_result_fields_not_calculated(self):
        r = _load_block()["asymmetry_scorer_result"]
        assert r["p_value"] == "NOT_CALCULATED"
        assert r["cohens_d"] == "NOT_CALCULATED"
        assert r["ci_95"] == "NOT_CALCULATED"
        assert _load_block()["is_significant"] is False


class TestStatisticalDiscipline1028:
    """Manual illustrative discipline: no manufactured significance."""

    def test_manual_illustrative_only(self):
        m = _load_block()["asymmetry_scorer_result"]["methodology"]
        assert "MANUAL ILLUSTRATIVE" in m
        assert "NOT an empirical measurement" in m

    def test_is_significant_false_engine_not_run(self):
        assert _load_block()["is_significant"] is False
        assert "no inference can be drawn" in _load_block()["asymmetry_scorer_result"]["methodology"]

    def test_verdict_directionally_supported_not_proven(self):
        assert _load_block()["verdict"] == "directionally_supported_not_proven"

    def test_no_analysis_json_update(self):
        assert _load_block()["no_analysis_json_update"] is True

    def test_cautious_language_required(self):
        m = _load_block()["asymmetry_scorer_result"]["methodology"]
        assert "correlation_not_causation" in m
        assert "correlation not causation" in _load_block()["incentive_context"]


class TestCorpusNovelty1028:
    """Corpus-wide guards: max id 848, zero next-after-max forms."""

    def _all_mechanism_ids(self):
        ids = []
        for p in (REPO / "profiles").rglob("*.yaml"):
            ids += [int(x) for x in re.findall(r"mechanism_id:\s*(\d+)", p.read_text())]
            ids += [int(x) for x in re.findall(r"mechanism:\s*(\d+)", p.read_text())]
        return ids

    def test_max_numeric_mechanism_id_is_848(self):
        assert max(self._all_mechanism_ids()) == THIS_MECH

    def test_zero_next_after_max_underscore_repo_wide(self):
        needle = "mechanism" + "_" + str(NEXT_AFTER)
        for p in REPO.rglob("*"):
            if p.is_file() and p.name != THIS_TEST and ".git/" not in str(p):
                try:
                    assert needle not in p.read_text(errors="ignore"), p
                except (UnicodeDecodeError, OSError):
                    pass

    def test_zero_next_after_max_dash_repo_wide(self):
        needle = "mechanism" + "-" + str(NEXT_AFTER)
        for p in REPO.rglob("*"):
            if p.is_file() and p.name != THIS_TEST and ".git/" not in str(p):
                try:
                    assert needle not in p.read_text(errors="ignore"), p
                except (UnicodeDecodeError, OSError):
                    pass

    def test_zero_next_after_max_numeric_forms_in_profiles(self):
        for p in (REPO / "profiles").rglob("*.yaml"):
            text = p.read_text()
            assert ("mechanism_id" + ": " + str(NEXT_AFTER)) not in text, p
            assert ("mechanism" + ": " + str(NEXT_AFTER)) not in text, p


class TestLedger1028:
    """Falsification discipline: THIRTY-FIRST member, ledger 30->31."""

    def test_is_falsification_family_member(self):
        b = _load_block()
        assert b["falsification_family_member"] is True
        assert b["falsification_family_ordinal"] == "THIRTY-FIRST"

    def test_ledger_advances_30_to_31(self):
        b = _load_block()
        assert b["falsification_ledger"] == 30 + 1
        corpus = "".join(p.read_text() for p in (REPO / "profiles").rglob("*.yaml"))
        assert "THIRTY-FIRST" in corpus


class TestDocSync1028:
    """Doc-sync: README stats + test-file table row; ARCHITECTURE.md tree row. Fail pre-commit per #719."""

    def test_readme_pre_run_values_still_present(self):
        text = (REPO / "README.md").read_text()
        assert "52769" in text
        assert "1352" in text

    def test_readme_table_row_for_1028(self):
        assert THIS_TEST in (REPO / "README.md").read_text()

    def test_architecture_tree_row_for_1028(self):
        assert THIS_TEST in (REPO / "docs" / "ARCHITECTURE.md").read_text()


class TestPushReadiness1028:
    """Push readiness, leaner #1021 shape: the main-commit-state-only gates (exact
    staged set, log hash placeholders) cannot stay green in followup state, so the
    anchor followup keeps ascii-only/no-em-dash, no-blob-url, and inflight-concurrency
    guards."""

    def test_ascii_only_no_em_dashes(self):
        block_text = yaml.safe_dump(_load_block(), allow_unicode=True)
        for payload, label in ((block_text, "block"), (Path(__file__).read_text(), "test file")):
            assert all(ord(c) < 128 for c in payload), label
            assert "\u2014" not in payload and "\u2013" not in payload, label

    def test_no_blob_url_in_block(self):
        assert "github.com/rayhe/mediascope/blob" not in yaml.safe_dump(_load_block())

    def test_inflight_concurrency_untouched(self):
        main_sha = _git("rev-list", "-n", "1", "--grep", "Type B #1028", "main").stdout.strip()
        assert main_sha, "main #1028 commit not found"
        files = _git("show", "--name-only", "--format=", main_sha).stdout.split()
        for other in (
            "profiles/nytimes.yaml",
            "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_india_havoc_m817_pairing_sep26_7am.py",
            "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",
        ):
            assert other not in files, other
        untracked = _git("ls-files", "--others", "--exclude-standard").stdout.split()
        assert "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py" in untracked
