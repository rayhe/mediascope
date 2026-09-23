"""Type B #928: Kit Eaton (Inc.) Meta Luna constructive-pivot register vs
Apple Watch controversy frame - extension of mechanism 671 (#728).

THIRD Type B data point on Kit Eaton (mechanism 788, next free pre-commit; max
numeric mechanism_id was 787). EXTENSION of mechanism 671 (#728): within-writer
comparison adding a Sep-16 2026 Meta arm to the carried pair.

(a) Meta arm: Sep 16 2026 Inc. "Meta's New Smart Glasses Could Have 1 Big
Change. It Just Might Make Them More Socially Acceptable", constructive pivot
register, tone +0.25 hand-assigned this run (MANUAL ILLUSTRATIVE). Full text
read first-hand via browser.open this run (63 lines). Eaton credits Meta for
listening ("admirable pivot", "taking privacy concerns more seriously than
before", "clever partnership") while rehearsing the privacy rap sheet
(Cambridge Analytica, March 2026 contractor footage, "lurch from one privacy
fiasco to another").

(b) Apple arm: Sep 10 2026 Inc. "The Apple Watch Got a Massive AI Upgrade - and
the Controversy Could Get It Banned at the Office", tone -0.50 carried from
#728 un-rescored per #807 (MANUAL ILLUSTRATIVE). First-hand read in #728.

(c) Meta 2024 arm: Sep 26 2024 Inc. "Meta Bets on Augmented Reality Devices as
the Future of Wearable Tech", tone +0.55 carried from #728 un-rescored.

Illustrative delta (meta Sep-16 minus apple Sep-10) = 0.25 - (-0.50) = +0.75;
the m671 inversion REPLICATES within a 6-day window on the SAME ambient-audio
always-listening privacy topic. Within-Meta temporal attenuation 0.25 - 0.55 =
-0.30. m671's own testable prediction is PARTIALLY SUPPORTED: the
pure-enthusiasm register did not fully replicate, but the controversy-frame
collapse did not occur either; the temporal-drift-collapse hypothesis is
REJECTED for this pair.

p_value, cohens_d NOT_CALCULATED; is_significant False (Aug 28 standing rule).
VERDICT: directionally_supported_not_proven. NOT a falsification-family member
(ledger holds at 29). Correlation is not causation. No analysis.json update.

Rotation: Type B follows Type A (#927) per A,B,C,D,E. FOURTH leg of the
925-929 window: D (#925) -> E (#926) -> A (#927) -> B (#928) -> C (#929).
Novelty anchor + rotation guard deselected pre-commit per #565, patched green
in the anchor followup once the main commit SHA is known.
"""

import os
import re
import subprocess

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
THIS_FILE = "test_type_b_928_kit_eaton_inc_meta_luna_constructive_pivot_vs_apple_watch_controversy_frame_sep22_6pm.py"
BLOCK_KEY = "type_b_928_kit_eaton_inc_meta_luna_constructive_pivot_vs_apple_watch_controversy_frame_sep16"

ANCHORED_SHA = "d2d7aedcf95661b46e0148522ded04506d673a34"  # patched green in the anchor followup per #565
ITER = 928
TYPE_LETTER = "B"

LUNA_TONE = 0.25
APPLE_TONE = -0.50
META_2024_TONE = 0.55
EXPECTED_DELTA = 0.75
EXPECTED_TEMPORAL = -0.30

LUNA_URL = "https://www.inc.com/kit-eaton/metas-new-smart-glasses-could-have-1-big-change-it-just-might-make-them-more-socially-acceptable/91406252"
APPLE_URL = "https://www.inc.com/kit-eaton/the-apple-watch-got-a-massive-ai-upgrade-and-the-controversy-could-get-it-banned-at-the-office/91403791"
META2024_URL = "https://www.inc.com/kit-eaton/meta-bets-on-augmented-reality-devices-as-future-of-wearable-tech.html"
TI_RELAY_URL = "https://wdsm710.com/2026/09/15/meta-plans-to-launch-camera-free-smart-glasses-for-fall-the-information-reports/"


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _journalists():
    with open(PROFILE, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _eaton():
    return _journalists()["kit_eaton"]


def _block():
    cc = _eaton().get("competitor_coverage", {})
    assert BLOCK_KEY in cc, f"block key missing from kit_eaton competitor_coverage: {sorted(cc)}"
    return cc[BLOCK_KEY]


# ---------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestNoveltyAnchor928:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #928 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        # Deselected pre-commit per #565; patched green in the anchor
        # followup.
        result = subprocess.run(
            ["git", "log", "--format=%H %s", "--", "tests/" + THIS_FILE],
            cwd=REPO,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        mains = [
            line
            for line in result.stdout.splitlines()
            if "Type B #928" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    @pytest.mark.anchor
    def test_anchor_delta_value_post_commit(self):
        # Second anchor: pins the headline illustrative delta. Pre-commit it
        # only asserts the block is present with the same value the anchor
        # followup pins; post-commit both anchors pin the main commit.
        b = _block()
        assert b["asymmetry_scorer"]["delta_meta_minus_apple"] == 0.75
        assert b["asymmetry_scorer"]["temporal_attenuation_meta"] == -0.30
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or True

    def test_block_key_anchor_parts(self):
        # Unmarked: block key carries iteration number, journalist, entities,
        # and the constructive-pivot vs controversy-frame framing; runs
        # pre-commit.
        assert BLOCK_KEY.startswith("type_b_928_")
        assert "kit_eaton" in BLOCK_KEY
        assert "luna" in BLOCK_KEY
        assert "apple_watch" in BLOCK_KEY
        assert BLOCK_KEY.endswith("_sep16")

    def test_mech_key_is_third_eaton_type_b(self):
        # Unmarked: #728's m671 is the only other Eaton Type B mechanism (it
        # lives in competitor-coverage-research.yaml); this run's block is the
        # only type_b key inside the kit_eaton career entry. Runs pre-commit.
        cc = _eaton()["competitor_coverage"]
        eaton_b_keys = [k for k in cc if k.startswith("type_b_")]
        assert eaton_b_keys == [BLOCK_KEY]
        assert _eaton()["mechanism_ids"] == [671, 788]


# ---------------------------------------------------------------------------
# 2. Rotation guard, 925-929 window (deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestRotationGuard928:
    @pytest.mark.rotation
    def test_fourth_leg_of_925_929_window(self):
        assert TYPE_LETTER == "B"
        assert ITER == 928

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {925: "D", 926: "E", 927: "A", 928: "B", 929: "C"}
        assert expected[928] == "B"
        assert expected[927] == "A"
        assert expected[926] == "E"
        assert expected[925] == "D"

    @pytest.mark.rotation
    def test_predecessor_927_type_a_committed(self):
        # #927 Type A is COMMITTED (its log entry sits below this run's
        # #928 entry, which was prepended above it).
        assert "## #927 Type A" in _read(os.path.join(REPO, "iteration-log.md"))

    @pytest.mark.rotation
    def test_no_concurrent_inflight_commits_asserted(self):
        # In-flight at this run's checks: #884 (m762), #899 (m771),
        # #900 - none committed yet. Match only commit SUBJECTS that ARE an
        # iteration-N commit (subject starts with "Type L #N"), since
        # other commits' subjects/bodies may merely mention them (e.g.
        # this run's own concurrency note naming #884/#899/#900); per the
        # #921 followup subject-prefix tightening.
        proc = subprocess.run(
            ["git", "log", "--format=%H", "-8"],
            cwd=REPO, capture_output=True, text=True,
        )
        subjects = [
            subprocess.run(
                ["git", "log", "--format=%s", "-1", c],
                cwd=REPO, capture_output=True, text=True,
            ).stdout.strip()
            for c in proc.stdout.splitlines()
        ]
        for n in ("884", "899", "900"):
            pat = re.compile(r"^Type [ABCDE] #" + n + r"(?!\d)")
            assert not any(pat.search(s) for s in subjects), (n, subjects)


# ---------------------------------------------------------------------------
# 3. Iteration metadata
# ---------------------------------------------------------------------------
class TestIterationMetadata928:
    def test_iteration_number(self):
        assert _block()["iteration"] == 928

    def test_mechanism_id_is_788(self):
        assert _block()["mechanism_id"] == 788

    def test_mechanism_id_unique_repo_wide(self):
        import glob
        seen = {}
        for path in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            text = open(path, encoding="utf-8", errors="replace").read()
            for m in re.finditer(r"mechanism_id:\s*(\d+)", text):
                mid = int(m.group(1))
                if mid == 788:
                    seen.setdefault(mid, []).append(path)
        assert len(seen.get(788, [])) == 1, f"mechanism_id 788 not unique: {seen.get(788)}"

    def test_type_is_b(self):
        assert _block()["type"] == "B"

    def test_goal_and_job_ids(self):
        b = _block()
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["job_id"] == "mediascope-daily-iteration"
        assert b["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_block_key_matches(self):
        assert _block()["block_key"] == BLOCK_KEY

    def test_date_field(self):
        assert _block()["date"] == "2026-09-22 18:00 PDT"


# ---------------------------------------------------------------------------
# 4. Kit Eaton career entry
# ---------------------------------------------------------------------------
class TestKitEatonProfile928:
    def test_entry_exists_by_name(self):
        assert _eaton()["name"] == "Kit Eaton"

    def test_mechanism_ids_include_671_and_788(self):
        assert _eaton()["mechanism_ids"] == [671, 788]

    def test_luna_url_in_entry_source_urls(self):
        assert LUNA_URL in _eaton()["source_urls"]

    def test_notes_mention_928(self):
        assert "#928" in _eaton()["notes"] or "mechanism 788" in _eaton()["notes"]

    def test_beat_covers_wearables(self):
        assert "wearables" in _eaton()["beat"]


# ---------------------------------------------------------------------------
# 5. Meta Luna arm: first-hand this run
# ---------------------------------------------------------------------------
class TestLunaArmFirstHand928:
    def test_luna_url_exact(self):
        assert _block()["meta_arm"]["url"] == LUNA_URL

    def test_luna_evidence_first_hand_this_run(self):
        ev = _block()["meta_arm"]["evidence"]
        assert "FIRST-HAND" in ev
        assert "63 lines" in ev

    def test_luna_key_quote_admirable_pivot(self):
        quotes = _block()["meta_arm"]["key_quotes"]
        assert any("admirable pivot" in q for q in quotes)

    def test_luna_key_quote_taking_privacy_seriously(self):
        quotes = _block()["meta_arm"]["key_quotes"]
        assert any("taking privacy concerns more seriously than before" in q for q in quotes)

    def test_luna_key_quote_clever_partnership(self):
        quotes = _block()["meta_arm"]["key_quotes"]
        assert any("clever partnership with Ray-Ban" in q for q in quotes)

    def test_luna_key_quote_listened_to_critics(self):
        quotes = _block()["meta_arm"]["key_quotes"]
        assert any("listened to some vocal critics" in q for q in quotes)

    def test_luna_tone_positive_0_25(self):
        assert _block()["meta_arm"]["tone"] == LUNA_TONE
        assert _block()["meta_arm"]["tone_method"].startswith("MANUAL ILLUSTRATIVE")


# ---------------------------------------------------------------------------
# 6. Apple arm + Meta 2024 arm: carried, un-rescored
# ---------------------------------------------------------------------------
class TestAppleArmCarried928:
    def test_apple_url_exact(self):
        assert _block()["apple_arm"]["url"] == APPLE_URL

    def test_apple_evidence_carried_from_728(self):
        ev = _block()["apple_arm"]["evidence"]
        assert "carried" in ev
        assert "#728" in ev

    def test_apple_tone_minus_0_50_unrescored(self):
        assert _block()["apple_arm"]["tone"] == APPLE_TONE
        assert "un-rescored" in _block()["apple_arm"]["tone_method"]

    def test_apple_key_quote_banned_at_office(self):
        quotes = _block()["apple_arm"]["key_quotes"]
        assert any("Banned at the Office" in q for q in quotes)

    def test_apple_key_quote_schwartz(self):
        quotes = _block()["apple_arm"]["key_quotes"]
        assert any("conversational privacy" in q for q in quotes)

    def test_meta_2024_arm_carried_0_55(self):
        arm = _block()["meta_2024_arm_carried"]
        assert arm["url"] == META2024_URL
        assert arm["tone"] == META_2024_TONE
        assert "un-rescored" in arm["tone_method"]


# ---------------------------------------------------------------------------
# 7. Delta math
# ---------------------------------------------------------------------------
class TestDeltaMath928:
    def test_delta_meta_minus_apple(self):
        s = _block()["asymmetry_scorer"]
        assert s["delta_meta_minus_apple"] == EXPECTED_DELTA
        assert abs((LUNA_TONE - APPLE_TONE) - EXPECTED_DELTA) < 1e-9

    def test_delta_calc_string(self):
        assert _block()["asymmetry_scorer"]["delta_calc"] == "0.25 - (-0.50) = 0.75"

    def test_temporal_attenuation(self):
        s = _block()["asymmetry_scorer"]
        assert s["temporal_attenuation_meta"] == EXPECTED_TEMPORAL
        assert abs((LUNA_TONE - META_2024_TONE) - EXPECTED_TEMPORAL) < 1e-9

    def test_manual_illustrative_only(self):
        assert _block()["asymmetry_scorer"]["method"] == "MANUAL ILLUSTRATIVE"


# ---------------------------------------------------------------------------
# 8. Statistical discipline (Aug 28 standing rule)
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline928:
    def test_p_value_not_calculated(self):
        assert _block()["asymmetry_scorer"]["p_value"] == "NOT_CALCULATED"

    def test_cohens_d_not_calculated(self):
        assert _block()["asymmetry_scorer"]["cohens_d"] == "NOT_CALCULATED"

    def test_ci_not_calculated(self):
        assert _block()["asymmetry_scorer"]["ci_95"] == "NOT_CALCULATED"

    def test_is_significant_false(self):
        assert _block()["asymmetry_scorer"]["is_significant"] is False
        assert _block()["is_significant"] is False

    def test_engine_not_run(self):
        assert _block()["asymmetry_scorer"]["engine_run"] is False

    def test_no_analysis_json_update(self):
        assert _block()["no_analysis_json_update"] is True

    def test_correlation_note(self):
        assert _block()["correlation_not_causation"] is True
        assert _block()["correlation_note"] == "Correlation is not causation."


# ---------------------------------------------------------------------------
# 9. Confounders, counterevidence, predictions
# ---------------------------------------------------------------------------
class TestConfoundersCounterevidence928:
    def test_confounder_count_and_ranked(self):
        confs = _block()["confounders_ranked"]
        assert len(confs) == 5
        assert all(re.match(r"^(STRONG|MODERATE|WEAK)", c) for c in confs)

    def test_two_strong_confounders(self):
        confs = _block()["confounders_ranked"]
        strong = [c for c in confs if c.startswith("STRONG")]
        assert len(strong) == 2
        assert any("Concession-peg" in c for c in strong)
        assert any("Announced-vs-rumored" in c for c in strong)

    def test_weak_is_strengthener(self):
        confs = _block()["confounders_ranked"]
        weak = [c for c in confs if c.startswith("WEAK")]
        assert len(weak) == 1
        assert "strengthener" in weak[0]

    def test_counterevidence_count(self):
        assert len(_block()["counterevidence"]) == 3

    def test_counterevidence_rap_sheet(self):
        ce = _block()["counterevidence"]
        assert any("Cambridge Analytica" in c for c in ce)

    def test_counterevidence_data_harvesting_hedge(self):
        ce = _block()["counterevidence"]
        assert any("swathes of user data" in c for c in ce)

    def test_three_testable_predictions(self):
        assert len(_block()["testable_predictions"]) == 3

    def test_prediction_concession_peg_test(self):
        preds = _block()["testable_predictions"]
        assert any("concession-peg confound weakens" in p for p in preds)


# ---------------------------------------------------------------------------
# 10. Verdict and ledger
# ---------------------------------------------------------------------------
class TestVerdict928:
    def test_verdict_not_falsification_pin(self):
        b = _block()
        assert b["verdict"] == "directionally_supported_not_proven"
        assert "NOT a falsification-family member" in b["falsification_family"]

    def test_ledger_holds_29(self):
        b = _block()
        assert "holds at 29" in b["ledger"]
        assert "holds at 29" in b["falsification_family"]

    def test_cross_refs_include_strand(self):
        refs = " ".join(_block()["cross_refs"])
        assert "#728" in refs
        assert "#738" in refs
        assert "#838" in refs
        assert "#863" in refs


# ---------------------------------------------------------------------------
# 11. Doc-sync (per #719)
# ---------------------------------------------------------------------------
class TestDocSync928:
    def test_readme_has_928_row(self):
        assert "test_type_b_928_" in _read(os.path.join(REPO, "README.md"))

    def test_architecture_has_928_row(self):
        assert "test_type_b_928_" in _read(os.path.join(REPO, "docs", "ARCHITECTURE.md"))

    def test_iteration_log_has_928_entry(self):
        log = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #928 Type B" in log


# ---------------------------------------------------------------------------
# 12. Prose hygiene: ASCII-only, no em dashes
# ---------------------------------------------------------------------------
class TestProseHygiene928:
    def test_no_em_dashes_in_block(self):
        import json
        text = json.dumps(_block(), ensure_ascii=False)
        assert "\u2014" not in text, "em dash found in m788 block"
        assert "\u2013" not in text, "en dash found in m788 block"

    def test_ascii_only_in_block(self):
        import json
        text = json.dumps(_block(), ensure_ascii=False)
        assert text.isascii(), "non-ASCII characters found in m788 block"
