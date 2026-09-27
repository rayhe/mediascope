"""Type B #1023: Lucas Ropek within-writer 9-day temporal register shift - Meta Connect hands-on product-curious (+0.15) vs Sep-16 Luna own-voice stigma register (-0.50), mechanism 845, Sep 26 2026 20:00 PDT.

Reasoning: 1020-1024 window FOURTH leg (D #1020 -> E #1021 -> A #1022 -> B #1023 -> C #1024, rotation per #565). THIRD dedicated Type B mechanism on Lucas Ropek (m728/#828 Snap launch regime, m749/#863 Luna cross-entity privacy pair). New arm: Ropek's Sep 25 2026 TechCrunch Connect piece "At Meta Connect, the company's smart glasses were everywhere" (first corpus mechanismization; zero pre-commit hits on URL, headline, and digest mirror). Carried arms per #807: his Sep 16 1:12 PM PDT Luna In Brief (m749, MANUAL ILLUSTRATIVE -0.50, own-voice stigma vocabulary "perv glasses"/"dystopian surveillance society run amok"/"integrated spy equipment" on a camera-free product) and his Sep 16 Snap Specs piece (m728, MANUAL ILLUSTRATIVE -0.45, adversarial price/utility/business, zero privacy vocabulary on 4 cameras). Finding: stigma-register DISAPPEARS at the same writer, same entity, nine days later - the Connect piece runs hands-on product-curious (wore the glasses, earplug hearing-loss simulation, $1,600-hearing-aid vs $150-glasses value framing, gently skeptical market kicker) with ZERO stigma vocabulary in the surfaced excerpt. Illustrative temporal delta (Meta vs Meta) +0.65; illustrative cross-entity delta (new Meta arm vs carried Snap arm) +0.60, inverting the Sep-16 pair direction (delta -0.05). Register follows the NEWS PEG, not the entity - EXTENDS the corpus peg-follows-register pattern (m637 Regalado, m743 Ashworth) to a third TechCrunch glasses writer. 2 browser.search query sets this run ((1) Lucas Ropek TechCrunch Meta Connect Sep 2026 camera-free glasses - SELECTED; (2) TechCrunch Sep 23 2026 Meta camera-free AI glasses byline - rejected as primary), 0 browser.open per #503 (excerpt-bounded: search excerpts + wesearch.press digest ~120 words attesting Ropek byline, Sep 26 2026 1:08 AM UTC crawl, 4 min read). Max numeric mechanism_id 844 pre-commit -> 845 post-commit; zero next-after-max forms repo-wide (format-built needles, no literals carried, per #715). Block key carries no numeric mechanism-id substring by designed keying. MANUAL ILLUSTRATIVE scoring only; p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant False; engine NOT run; NOT artifact-grade; NOT falsification-family member; ledger holds at 30; no analysis.json update. Verdict directionally_supported_not_proven. Doc-sync 3 tests fail pre-commit per #719 (README stats 52524/1347 + new table row; ARCHITECTURE.md tree row). Push-readiness 3: leaner #1021 shape in the anchor followup (ascii-only/no-em-dash, no-blob-url, inflight-concurrency guards; the main-commit-state-only exact-staged-set and hash-placeholder gates do not survive followup state). Rotation 4 marked rotation, anchor 1 marked anchor, both deselected pre-commit.
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
    "type_b_1023_lucas_ropek_techcrunch_sep25_connect_glasses_everywhere_"
    "vs_sep16_luna_stigma_temporal_shift"
)
NEXT_FREE_PRE = 844  # max numeric mechanism_id before this run's insert
THIS_MECH = NEXT_FREE_PRE + 1
THIS_ITER = 1022 + 1
NEXT_AFTER = THIS_MECH + 1  # format-built; no literals carried per #715
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
 ANCHORED_SHA = "af7c36a36ee956a34efe6c9d7b50f3e5e4899461"


def _load_block():
    data = yaml.safe_load(JOURNALISTS_YAML.read_text())
    return data["lucas_ropek"]["competitor_coverage"][BLOCK_KEY]


def _git(*args):
    return subprocess.run(
        ["git", "-C", str(REPO), *args],
        capture_output=True, text=True, check=False,
    )


class TestNovelty1023:
    """Uniqueness of this run: exactly one test file, no prior Type B #1023 commit."""

    def test_single_type_b_1023_test_file(self):
        hits = sorted(glob.glob(str(REPO / "tests" / "test_type_b_1023_*.py")))
        assert len(hits) == 1, hits
        assert Path(hits[0]).name == THIS_TEST

    def test_no_type_b_1023_in_git_log(self):
        out = _git("log", "--oneline", "--grep", "Type B #1023").stdout
        assert out.strip() == "", out

    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        """Per #716/#565: ANCHORED_SHA must equal the main commit; fails pre-commit."""
        assert ANCHORED_SHA != "PATCH_ME_IN_FOLLOWUP", "anchor followup not yet applied per #565"
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA), ANCHORED_SHA
        r = _git("cat-file", "-t", ANCHORED_SHA)
        assert r.stdout.strip() == "commit", ANCHORED_SHA


class TestRotationGuard1023:
    """1020-1024 window: FOURTH leg D->E->A->B->C. Marked tests deselected pre-commit."""

    def test_window_legs_in_iteration_log(self):
        text = (REPO / "iteration-log.md").read_text()
        assert "## #1020 Type D" in text
        assert "## #1021 Type E" in text
        assert "## #1022 Type A" in text
        assert "1020-1024" in text

    @pytest.mark.rotation
    def test_fourth_leg_of_1020_to_1024_window(self):
        text = (REPO / "iteration-log.md").read_text()
        assert "FOURTH leg of the 1020-1024 window" in text

    @pytest.mark.rotation
    def test_predecessor_1022_type_a_committed(self):
        assert _git("log", "--oneline", "--grep", "Type A #1022").stdout.strip() != ""
        assert (REPO / "tests").glob("test_type_a_1022_*.py")

    @pytest.mark.rotation
    def test_no_successor_1024_type_c_commit_yet(self):
        out = _git("log", "--oneline", "--grep", "Type C #1024").stdout
        assert out.strip() == "", out

    @pytest.mark.rotation
    def test_no_concurrent_type_b_1023_by_commit_time(self):
        out = _git("log", "--all", "--oneline", "--grep", "Type B #1023").stdout
        assert len(out.strip().splitlines()) <= 1, out


class TestMechanism845Content:
    """Profile block structure and field-level content for mechanism 845."""

    def test_block_key_unique_at_indent_4(self):
        text = JOURNALISTS_YAML.read_text()
        assert text.count("\n    " + BLOCK_KEY + ":") == 1
        assert text.count("block_key: " + BLOCK_KEY) == 1

    def test_mechanism_id_845_iteration_1023_type_b(self):
        b = _load_block()
        assert b["mechanism_id"] == THIS_MECH == NEXT_FREE_PRE + 1
        assert b["iteration"] == THIS_ITER == 1023
        assert b["iteration_type"] == "B"
        assert b["test_file"].endswith(THIS_TEST)

    def test_journalist_and_publication(self):
        data = yaml.safe_load(JOURNALISTS_YAML.read_text())
        jr = data["lucas_ropek"]
        assert jr["name"] == "Lucas Ropek"
        assert jr["current_publication"] == "TechCrunch"
        b = _load_block()
        assert b["new_meta_arm_sep25"]["byline"] == "Lucas Ropek (sole)"
        assert b["new_meta_arm_sep25"]["publication"] == "techcrunch"

    def test_publication_author_goal_job_fields(self):
        b = _load_block()
        assert b["author"] == "Kit (with Ray)"
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["job_id"] == "mediascope-daily-iteration"
        assert b["scheduled_job_id"] == "mediascope-daily-iteration"
        assert b["date"] == "2026-09-26 20:00 PDT"

    def test_key_design_note_no_numeric_substring(self):
        b = _load_block()
        assert str(THIS_MECH) not in BLOCK_KEY
        assert b["key_design_note"].startswith("Colon-form key only")

    def test_connects_to_all_exist_in_profiles(self):
        corpus = ""
        for p in (REPO / "profiles").rglob("*.yaml"):
            corpus += p.read_text()
        for mid in _load_block()["connects_to"]:
            assert "mechanism_id: %d" % mid in corpus, mid

    def test_rotation_transparency_names_window_and_predecessor(self):
        rt = _load_block()["rotation_transparency"]
        assert "1020-1024" in rt
        assert "7cdb3856" in rt  # #1022 main short sha, predecessor
        assert "30af39aa" in rt  # #1022 anchor short sha
        assert "#1024 will be Type C" in rt

    def test_mechanism_ids_list_updated(self):
        data = yaml.safe_load(JOURNALISTS_YAML.read_text())
        assert data["lucas_ropek"]["mechanism_ids"] == [727 + 1, 748 + 1, THIS_MECH]


class TestEvidence1023:
    """Two Meta arms plus Snap control: dates, URLs, quotes, carried-arm sourcing."""

    def test_two_meta_arms_plus_snap_control(self):
        b = _load_block()
        assert b["new_meta_arm_sep25"]["tone_illustrative"] == pytest.approx(0.15)
        assert b["carried_meta_arm_sep16"]["tone_illustrative"] == pytest.approx(-0.50)
        assert b["carried_snap_arm_sep16"]["tone_illustrative"] == pytest.approx(-0.45)

    def test_new_arm_url_in_corpus_post_insert(self):
        url = "https://techcrunch.com/2026/09/25/at-meta-connect-the-companys-smart-glasses-were-everywhere/"
        b = _load_block()
        assert b["new_meta_arm_sep25"]["url"] == url
        assert url in JOURNALISTS_YAML.read_text()
        assert "wesearch.press" in b["new_meta_arm_sep25"]["url_attestation"]

    def test_carried_arms_from_749_and_728(self):
        b = _load_block()
        assert "mechanism 749" in b["carried_meta_arm_sep16"]["note"]
        assert "mechanism 728" in b["carried_snap_arm_sep16"]["note"]

    def test_arm_dates(self):
        b = _load_block()
        assert b["new_meta_arm_sep25"]["date"] == "2026-09-25"
        assert b["carried_meta_arm_sep16"]["date"] == "2026-09-16"
        assert b["carried_snap_arm_sep16"]["date"] == "2026-09-16"

    def test_new_arm_quotes_present(self):
        quotes = _load_block()["new_meta_arm_sep25"]["evidence_quotes"]
        assert len(quotes) >= 5
        joined = " ".join(quotes)
        assert "$150" in joined
        assert "follows suit" in joined
        assert "smart glasses are the future" in joined

    def test_zero_stigma_vocabulary_in_new_arm_excerpt(self):
        joined = " ".join(_load_block()["new_meta_arm_sep25"]["evidence_quotes"])
        assert "perv glasses" not in joined
        assert "dystopian surveillance" not in joined
        assert "integrated spy equipment" not in joined


class TestScores1023:
    """Illustrative deltas: temporal +0.65, cross-entity inversion +0.60."""

    def test_temporal_delta_plus_0_65(self):
        r = _load_block()["asymmetry_scorer_result"]
        assert r["illustrative_temporal_delta_meta_sep25_minus_sep16"] == pytest.approx(0.65)
        assert "+0.65" in r["temporal_delta_calc"]

    def test_cross_entity_inversion_delta_plus_0_60(self):
        r = _load_block()["asymmetry_scorer_result"]
        assert r["illustrative_cross_entity_delta_meta_minus_snap"] == pytest.approx(0.60)
        assert "+0.60" in r["cross_entity_delta_calc"]
        assert "inversion" in r["cross_entity_delta_direction"]

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


class TestStatisticalDiscipline1023:
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


class TestCorpusNovelty1023:
    """Corpus-wide guards: max id 845, zero next-after-max forms."""

    def _all_mechanism_ids(self):
        ids = []
        for p in (REPO / "profiles").rglob("*.yaml"):
            ids += [int(x) for x in re.findall(r"mechanism_id:\s*(\d+)", p.read_text())]
        return ids

    def test_max_numeric_mechanism_id_is_845(self):
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

    def test_zero_next_after_max_numeric_form_in_profiles(self):
        needle = "mechanism_id" + ": " + str(NEXT_AFTER)
        for p in (REPO / "profiles").rglob("*.yaml"):
            assert needle not in p.read_text(), p


class TestLedger1023:
    """Falsification discipline: ledger holds at 30, not a family member."""

    def test_not_falsification_family_member(self):
        b = _load_block()
        assert b["falsification_family_member"] is False

    def test_ledger_holds_at_30(self):
        b = _load_block()
        assert b["falsification_ledger"] == 29 + 1
        corpus = "".join(p.read_text() for p in (REPO / "profiles").rglob("*.yaml"))
        assert "THIRTIETH" in corpus


class TestDocSync1023:
    """Doc-sync: README stats + test-file table row; ARCHITECTURE.md tree row. Fail pre-commit per #719."""

    def test_readme_pre_run_values_still_present(self):
        text = (REPO / "README.md").read_text()
        assert "52524" in text
        assert "1347" in text

    def test_readme_table_row_for_1023(self):
        assert THIS_TEST in (REPO / "README.md").read_text()

    def test_architecture_tree_row_for_1023(self):
        assert THIS_TEST in (REPO / "docs" / "ARCHITECTURE.md").read_text()


class TestPushReadiness1023:
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
        main_sha = _git("rev-list", "-n", "1", "--grep", "Type B #1023", "main").stdout.strip()
        assert main_sha, "main #1023 commit not found"
        files = _git("show", "--name-only", "--format=", main_sha).stdout.split()
        for other in (
            "profiles/nytimes.yaml",
            "tests/test_type_a_1012_mittr_anthropic_sep2026_doomer_turn_agenda_setting_register_vs_carried_meta_india_havoc_m817_pairing_sep26_7am.py",
            "tests/test_type_b_938_dominic_preston_verge_pixel_watch_gemini_personalization_vs_meta_luna_stigma_sep16.py",
        ):
            assert other not in files, other
        untracked = _git("ls-files", "--others", "--exclude-standard").stdout.split()
        assert "tests/test_type_d_900_m769_qualitative_corpus_integrity_sep21_1pm.py" in untracked
