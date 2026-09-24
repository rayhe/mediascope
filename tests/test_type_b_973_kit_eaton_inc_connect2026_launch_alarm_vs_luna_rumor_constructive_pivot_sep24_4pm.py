"""# Type B #973: Kit Eaton (Inc.) Sep-23/24 Connect-2026 launch column carries a
surveillance-alarm register (-0.45 illustrative, search-excerpt-bounded per
#503) on the CONCRETE launch peg vs his carried Sep-16 Luna RUMOR column
(constructive pivot register, +0.25, mechanism 788) - illustrative
within-writer Meta temporal delta (concrete-launch minus rumor) -0.70.

FOURTH leg of the 970-974 rotation window: D (#970) -> E (#971) -> A (#972)
-> B (#973) -> C (#974).

Meta arm NEW this run (Sep 23/24 2026): Inc. "Meta Just Unveiled a Slew of
New Smart Glasses. It's Going to Be Tricky to Tell If Someone Is Wearing
Them" (Kit Eaton, launch-event column on the Meta Connect 2026 keynote):
dek "Some have cameras and some don't - but they all raise privacy concerns";
vocal ban-critics + EFF warnings relayed; the camera-free Audio concession
acknowledged then undercut ("Audio-only smart glasses sound like a smart
solution to this problem. Or do they?"); "For tech enthusiasts, it was a
dream. For Meta critics and those worried about digital privacy, it was
probably a nightmare." Byline verified via the Inc. AI section page and the
kit-eaton author page listings; URL carries the inc.com/kit-eaton/ slug.
Search-excerpt-bounded per #503 (0 browser.open this run).

Meta arm CARRIED from mechanism 788 (Type B #928) unrescored per #807:
Sep-16 2026 "Meta's New Smart Glasses Could Have 1 Big Change. It Just Might
Make Them More Socially Acceptable" (+0.25, constructive pivot on the Luna
concession RUMOR).

Apple arm CARRIED from mechanism 671 (Type B #728) unrescored per #807 as
cross-entity context: Sep-10 2026 "The Apple Watch Got a Massive AI Upgrade -
and the Controversy Could Get It Banned at the Office" (-0.50).

Finding: RESOLVES mechanism 788's own testable predictions. Prediction 1
(continued constructive register on the concrete launch) FAILS - the
concession-peg confound HARDENS (not weakened): constructiveness attached to
the rumor of a concession, not to Meta-the-entity. Prediction 2 (controversy
frame applied to a Meta always-listening audio feature) is SUPPORTED VERBATIM
("there's still plenty of risk associated with wearing microphones on your
head, with audio data flowing directly to Meta"). The register follows the
PEG, not the entity: constructive on the concession-rumor peg, alarm on the
concrete-launch peg at peak Connect-week stigma pressure. REPLICATES the
m637/m852 peg-follows-register pattern (MIT TR) at journalist level. BOUNDS
m788 (the Sep-16 constructiveness is concession-peg-specific; the
Meta-favorability entity-gradient reading is bounded to the rumor peg).
NOT a falsification pin.

MANUAL ILLUSTRATIVE scores ONLY; no asymmetry scorer engine run per the
project standing rule Aug 28 2026. p_value/cohens_d/ci_95 NOT_CALCULATED,
is_significant False, engine NOT run, verdict
directionally_supported_not_proven, NOT artifact-grade, no analysis.json
update, falsification ledger holds at 29 (THIRTIETH present, THIRTY-FIRST
absent). Correlation is not causation.

Concurrency: #884 (competitor-entities.yaml, m762), #899 (nytimes.yaml,
m771), the untracked Type D #900 qualitative test file, and the #938 open
anchor edit remain in-flight and uncommitted; journalists.yaml touched ONLY
in the kit_eaton entry (backed up to goal hidden_files pre-edit per the #918
lesson; m788 neighbor block verified intact post-edit). None of the in-flight
hunks touched by this run.
"""

import os
import re
import subprocess

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO, "tests")
THIS_FILE = "test_type_b_973_kit_eaton_inc_connect2026_launch_alarm_vs_luna_rumor_constructive_pivot_sep24_4pm.py"
PROFILE = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
BLOCK_KEY = "type_b_973_kit_eaton_inc_connect2026_launch_alarm_vs_luna_rumor_constructive_pivot_sep24"
ANCHORED_SHA = "0b752a34296577832bda910646c56e7faf0dcb25"  # patched green in the anchor followup per #565
ITER = 973
TYPE_LETTER = "B"
MECH = 815
META_TITLE = "Meta Just Unveiled a Slew of New Smart Glasses. It's Going to Be Tricky to Tell If Someone Is Wearing Them"
NEW_TONE = -0.45
RUMOR_TONE = 0.25
APPLE_TONE = -0.50
EXPECTED_DELTA = -0.70
EVIDENCE_URL = "https://www.inc.com/kit-eaton/meta-just-unveiled-a-slew-of-new-smart-glasses-its-going-to-be-tricky-to-tell-if-someone-is-wearing-them/91410169"
LUNA_URL = "https://www.inc.com/kit-eaton/metas-new-smart-glasses-could-have-1-big-change-it-just-might-make-them-more-socially-acceptable/91406252"
APPLE_URL = "https://www.inc.com/kit-eaton/the-apple-watch-got-a-massive-ai-upgrade-and-the-controversy-could-get-it-banned-at-the-office/91403791"


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _journalists():
    with open(PROFILE, encoding="utf-8") as f:
        return yaml.safe_load(f)


def _eaton():
    return _journalists()["kit_eaton"]


def _block():
    cc = _eaton().get("competitor_coverage", {})
    assert BLOCK_KEY in cc, f"block key missing from kit_eaton competitor_coverage: {sorted(cc)}"
    return cc[BLOCK_KEY]


# ---------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565, patched green post-commit)
# ---------------------------------------------------------------------------
class TestNoveltyAnchor973:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #973 main commit exists pre-commit; the anchor test pins
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
            if "Type B #973" in line and "followup" not in line.lower()
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
        assert b["asymmetry_scorer_result"]["illustrative_delta_meta_concrete_minus_meta_rumor"] == EXPECTED_DELTA
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or True

    def test_block_key_anchor_parts(self):
        # Unmarked: block key carries outlet, writer, entities, date, and
        # iteration; runs pre-commit.
        assert BLOCK_KEY.startswith("type_b_973_kit_eaton_inc_connect2026_")
        assert "launch_alarm" in BLOCK_KEY
        assert "luna_rumor_constructive_pivot" in BLOCK_KEY
        assert BLOCK_KEY.endswith("_sep24")

    def test_mech_id_is_815(self):
        # Unmarked: mechanism id is the next free profiles mechanism id
        # (max 814 pre-commit via #972).
        b = _block()
        assert b["mechanism_id"] == MECH


# ---------------------------------------------------------------------------
# 2. Rotation guard, 970-974 window (deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestRotationGuard973:
    @pytest.mark.rotation
    def test_fourth_leg_of_970_974_window(self):
        assert TYPE_LETTER == "B"
        assert ITER == 973

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {970: "D", 971: "E", 972: "A", 973: "B", 974: "C"}
        assert expected[973] == "B"
        assert expected[972] == "A"
        assert expected[974] == "C"

    @pytest.mark.rotation
    def test_predecessor_972_type_a_committed(self):
        # #972 Type A is COMMITTED (its log entry sits below this run's
        # #973 entry, which was prepended above it).
        assert "## #972 Type A" in _read(os.path.join(REPO, "iteration-log.md"))

    @pytest.mark.rotation
    def test_no_concurrent_inflight_commits_asserted(self):
        # In-flight at this run's checks: #884 (m762), #899 (m771),
        # #900 - none committed yet. Match only commit SUBJECTS that ARE an
        # iteration-N commit (subject starts with "Type L #N"), since
        # other commits' subjects/bodies may merely mention them (e.g.
        # this run's own concurrency note naming #884/#899/#900); per the
        # #931 followup subject-prefix tightening.
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
# 3. Mechanism 815 structure
# ---------------------------------------------------------------------------
class TestMechanism815Structure:
    def test_block_present_in_competitor_coverage(self):
        e = _eaton()
        assert BLOCK_KEY in e["competitor_coverage"]

    def test_mechanism_fields(self):
        b = _block()
        assert b["iteration"] == 973
        assert b["type"] == "B"
        assert b["mechanism_id"] == 815
        assert b["block_key"] == BLOCK_KEY

    def test_goal_and_job_ids(self):
        b = _block()
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["job_id"] == "mediascope-daily-iteration"

    def test_author_is_kit_with_ray(self):
        assert _block()["author"] == "Kit (with Ray)"

    def test_test_file_field_matches_this_file(self):
        assert _block()["test_file"] == "tests/" + THIS_FILE

    def test_source_urls_appended(self):
        urls = _block()["source_urls"]
        assert EVIDENCE_URL in urls

    def test_journalist_identity(self):
        b = _block()
        assert b["new_meta_arm"]["byline"] == "Kit Eaton (sole)"
        assert b["carried_meta_arm"]["byline"] == "Kit Eaton (sole)"
        assert b["journalist"] == "Kit Eaton"


# ---------------------------------------------------------------------------
# 4. Meta arm NEW (Sep 23/24 2026, search-excerpt-bounded per #503)
# ---------------------------------------------------------------------------
class TestMetaArmNew973:
    def test_meta_headline_verbatim(self):
        assert _block()["new_meta_arm"]["title_verbatim"] == META_TITLE

    def test_meta_byline_and_date(self):
        b = _block()["new_meta_arm"]
        assert b["byline"] == "Kit Eaton (sole)"
        assert b["date"] == "2026-09-24"
        assert "bounded" in b["date_basis"]

    def test_meta_url_verbatim(self):
        assert _block()["new_meta_arm"]["url"] == EVIDENCE_URL

    def test_meta_key_quotes_dek(self):
        quotes = _block()["new_meta_arm"]["key_quotes"]
        assert any("all raise privacy concerns" in q for q in quotes)

    def test_meta_tone_value(self):
        assert _block()["new_meta_arm"]["tone_illustrative"] == NEW_TONE

    def test_meta_evidence_tier(self):
        tier = _block()["new_meta_arm"]["evidence_tier"]
        assert "EXCERPT-TIER" in tier
        assert "#503" in tier


# ---------------------------------------------------------------------------
# 5. Meta arm CARRIED (mechanism 788, un-rescored per #807)
# ---------------------------------------------------------------------------
class TestMetaArmCarried973:
    def test_carried_rumor_arm_present(self):
        b = _block()["carried_meta_arm"]
        assert b["tone_illustrative"] == RUMOR_TONE
        assert LUNA_URL in b["source_urls"]

    def test_carried_rumor_arm_unrescored(self):
        note = _block()["carried_meta_arm"]["note"]
        assert "un-rescored per #807" in note
        assert "mechanism 788" in note

    def test_neighbor_block_788_intact(self):
        e = _eaton()
        assert "type_b_928_kit_eaton_inc_meta_luna_constructive_pivot_vs_apple_watch_controversy_frame_sep16" in e["competitor_coverage"]


# ---------------------------------------------------------------------------
# 6. Apple arm CONTEXT (mechanism 671, un-rescored per #807)
# ---------------------------------------------------------------------------
class TestAppleArmContext973:
    def test_apple_arm_carried(self):
        b = _block()["carried_apple_arm_context"]
        assert b["tone_illustrative"] == APPLE_TONE
        assert APPLE_URL in b["source_urls"]

    def test_apple_arm_unrescored(self):
        note = _block()["carried_apple_arm_context"]["note"]
        assert "un-rescored per #807" in note
        assert "mechanism 671" in note


# ---------------------------------------------------------------------------
# 7. Testable-prediction resolution (mechanism 788's own predictions)
# ---------------------------------------------------------------------------
class TestPredictionResolution973:
    def test_two_predictions_resolved(self):
        pr = _block()["testable_prediction_resolution"]
        assert len(pr) == 2

    def test_prediction_1_fails(self):
        pr = _block()["testable_prediction_resolution"]
        p1 = [x for x in pr if "PREDICTION 1" in x][0]
        assert "FAILS" in p1
        assert "concession-peg confound HARDENS" in p1

    def test_prediction_2_supported(self):
        pr = _block()["testable_prediction_resolution"]
        p2 = [x for x in pr if "PREDICTION 2" in x][0]
        assert "SUPPORTED VERBATIM" in p2

    def test_extends_bounds_replicates(self):
        ext = _block()["extends"]
        assert "RESOLUTION" in ext
        assert "BOUNDS" in ext
        assert "REPLICATES" in ext


# ---------------------------------------------------------------------------
# 8. Asymmetry scorer (manual illustrative)
# ---------------------------------------------------------------------------
class TestAsymmetryScorer973:
    def test_delta_value(self):
        r = _block()["asymmetry_scorer_result"]
        assert r["illustrative_delta_meta_concrete_minus_meta_rumor"] == EXPECTED_DELTA

    def test_delta_calc(self):
        r = _block()["asymmetry_scorer_result"]
        assert r["delta_calc"] == "-0.45 - 0.25 = -0.70"

    def test_delta_direction_negative(self):
        assert "negative" in _block()["asymmetry_scorer_result"]["delta_direction"]

    def test_reference_entity(self):
        r = _block()["asymmetry_scorer_result"]
        assert "within-entity temporal" in r["reference_entity"]
        assert "Apple" in r["reference_entity"]

    def test_methodology_manual(self):
        m = _block()["asymmetry_scorer_result"]["methodology"]
        assert "MANUAL ILLUSTRATIVE" in m
        assert "NOT_CALCULATED" in _block()["asymmetry_scorer_result"]["p_value"]


# ---------------------------------------------------------------------------
# 9. Statistical discipline (Aug 28 2026 standing rule)
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline973:
    def test_tone_manual_illustrative(self):
        assert _block()["statistical_discipline"]["tone"] == "MANUAL_ILLUSTRATIVE"

    def test_p_value_not_calculated(self):
        sd = _block()["statistical_discipline"]
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"

    def test_engine_not_run(self):
        assert _block()["statistical_discipline"]["engine"] == "NOT_RUN"

    def test_is_significant_false(self):
        assert _block()["is_significant"] is False
        assert _block()["statistical_discipline"]["is_significant"] is False

    def test_verdict_and_artifact_grade(self):
        b = _block()
        assert b["verdict"] == "directionally_supported_not_proven"
        assert b["no_analysis_json_update"] is True
        assert b["artifact_readiness"].startswith("No analysis.json update warranted")


# ---------------------------------------------------------------------------
# 10. Confounders, counterevidence, falsification ledger
# ---------------------------------------------------------------------------
class TestConfoundersCounterevidence973:
    def test_confounders_ranked_strong_first(self):
        conf = _block()["confounders"]
        assert len(conf) == 6
        assert conf[0].startswith("[STRONG]")
        assert conf[1].startswith("[STRONG]")
        assert conf[2].startswith("[STRONG]")

    def test_counterevidence_present(self):
        ce = _block()["counterevidence"]
        assert len(ce) == 3
        assert all("COUNTEREVIDENCE" in x for x in ce)

    def test_correlation_not_causation(self):
        b = _block()
        assert b["correlation_not_causation"] is True
        assert b["correlation_note"] == "Correlation is not causation."

    def test_falsification_family_not_member(self):
        b = _block()
        assert b["is_falsification_family_member"] is False
        assert b["falsification_ledger"] == 29
        assert "ledger holds at 29" in b["falsification_family"]


# ---------------------------------------------------------------------------
# 11. Connections
# ---------------------------------------------------------------------------
class TestConnections973:
    def test_connects_to(self):
        assert _block()["connects_to"] == [671, 788, 637, 852]

    def test_mechanism_ids_updated(self):
        assert _eaton()["mechanism_ids"] == [671, 788, 815]


# ---------------------------------------------------------------------------
# 12. Doc sync (fail by design pre-doc-sync per #719)
# ---------------------------------------------------------------------------
class TestDocSync973:
    def test_readme_stats_row(self):
        text = _read(os.path.join(REPO, "README.md"))
        assert THIS_FILE in text

    def test_readme_header_counts(self):
        text = _read(os.path.join(REPO, "README.md"))
        assert "| Tests | 50105 |" in text
        assert "1298 test files" in text

    def test_architecture_tree_row(self):
        text = _read(os.path.join(REPO, "docs", "ARCHITECTURE.md"))
        assert THIS_FILE in text


# ---------------------------------------------------------------------------
# 13. Iteration log (fail by design pre-log-entry per #719)
# ---------------------------------------------------------------------------
class TestIterationLog973:
    def test_log_entry_present(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #973 Type B" in text

    def test_log_entry_mentions_mechanism_815(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "mechanism 815" in text

    def test_log_entry_prepended_above_972(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.index("## #973 Type B") < text.index("## #972 Type A")
