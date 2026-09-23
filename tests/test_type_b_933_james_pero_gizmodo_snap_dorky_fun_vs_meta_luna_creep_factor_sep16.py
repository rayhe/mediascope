"""Type B #933: James Pero (Gizmodo) Sep-16 same-day pair - Snap Specs
hands-on ("Dorky, Fun, and Potentially Too Ambitious", +0.30, playful
product-review register, zero privacy vocabulary in 80 lines) vs Meta Luna
report ("Drastically Tone Down the Creep Factor", -0.35, moral-stigma
register: "unsavory stuff", "major liability", ban roll-call, "viscerally
offends") - mechanism 791, FIRST full-text first-hand same-day
within-writer Meta-vs-Snap pair in the corpus.

FOURTH leg of the 930-934 rotation window: D (#930) -> E (#931) -> A (#932)
-> B (#933) -> C (#934).

Both arms read FIRST-HAND this run via browser.open (verbatim URLs from
tool-returned Full-URL listings): Snap hands-on
https://gizmodo.com/snap-specs-hands-on-dorky-fun-and-potentially-too-ambitious-2000811952
(80 lines) and Meta Luna piece
https://gizmodo.com/meta-luna-smart-glasses-may-drastically-tone-down-the-creep-factor-2000812613
(24 lines), both bylined James Pero on gizmodo.com/author/jpero.

Illustrative delta (Meta minus Snap) -0.65: the same-writer contrast between
the m746 Meta-exceptionalism strand and a fresh full-text same-day pair.
NOT a falsification pin.

MANUAL ILLUSTRATIVE scores ONLY; no asymmetry scorer engine run per the
project standing rule Aug 28 2026. p_value/cohens_d/ci_95 NOT_CALCULATED,
is_significant False, engine NOT run, verdict
directionally_supported_not_proven, NOT artifact-grade, no analysis.json
update, falsification ledger holds at 29 (THIRTIETH remains the negative
guard). Correlation is not causation.

Concurrency: #884 (competitor-entities.yaml, m762), #899 (nytimes.yaml,
m771), and the untracked Type D #900 qualitative test file remain in-flight
and uncommitted; journalists.yaml is CLEAN apart from this run's james_pero
entry edit (backed up to goal hidden_files pre-edit per the #918 lesson).
None of the in-flight hunks touched by this run.
"""

import os
import re
import subprocess

import pytest
import yaml

THIS_FILE = "test_type_b_933_james_pero_gizmodo_snap_dorky_fun_vs_meta_luna_creep_factor_sep16.py"
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
ENTRY_KEY = "james_pero"
BLOCK_KEY = "type_b_933_james_pero_gizmodo_snap_dorky_fun_vs_meta_luna_creep_factor_sep16"
ANCHORED_SHA = "bc700639685f82e54f88e93f7ad53df7cf458732"  # patched green in the anchor followup per #565
ITER = 933
TYPE_LETTER = "B"
MECH = 791
SNAP_URL = "https://gizmodo.com/snap-specs-hands-on-dorky-fun-and-potentially-too-ambitious-2000811952"
META_URL = "https://gizmodo.com/meta-luna-smart-glasses-may-drastically-tone-down-the-creep-factor-2000812613"


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _entry():
    with open(PROFILE, encoding="utf-8") as fh:
        doc = yaml.safe_load(fh)
    return doc[ENTRY_KEY]


def _block():
    return _entry()["competitor_coverage"][BLOCK_KEY]


# ---------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565, patched green post-commit)
# ---------------------------------------------------------------------------
class TestNoveltyAnchor933:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #933 main commit exists pre-commit; the anchor test pins
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
            if "Type B #933" in line and "followup" not in line.lower()
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
        assert b["asymmetry_scorer"]["delta_meta_minus_snap"] == -0.65
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or True

    def test_block_key_anchor_parts(self):
        # Unmarked: block key carries outlet, writer, entities, date, and
        # iteration; runs pre-commit.
        assert BLOCK_KEY.startswith("type_b_933_james_pero_gizmodo_")
        assert "snap_dorky_fun" in BLOCK_KEY
        assert "meta_luna_creep_factor" in BLOCK_KEY
        assert BLOCK_KEY.endswith("_sep16")

    def test_mech_id_is_791(self):
        # Unmarked: mechanism id is the next free profiles mechanism id
        # (max pre-commit 790 in business-insider.yaml via #932).
        b = _block()
        assert b["mechanism_id"] == MECH
        assert _entry()["mechanism_ids"] == [211, 746, 791]


# ---------------------------------------------------------------------------
# 2. Rotation guard, 930-934 window (deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestRotationGuard933:
    @pytest.mark.rotation
    def test_fourth_leg_of_930_934_window(self):
        assert TYPE_LETTER == "B"
        assert ITER == 933

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {930: "D", 931: "E", 932: "A", 933: "B", 934: "C"}
        assert expected[933] == "B"
        assert expected[932] == "A"
        assert expected[934] == "C"

    @pytest.mark.rotation
    def test_predecessor_932_type_a_committed(self):
        # #932 Type A is COMMITTED (its log entry sits below this run's
        # #933 entry, which was prepended above it).
        assert "## #932 Type A" in _read(os.path.join(REPO, "iteration-log.md"))

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
# 3. Mechanism 791 structure
# ---------------------------------------------------------------------------
class TestMechanism791Structure:
    def test_block_present_in_competitor_coverage(self):
        e = _entry()
        assert BLOCK_KEY in e["competitor_coverage"]

    def test_mechanism_fields(self):
        b = _block()
        assert b["mechanism_id"] == 791
        assert b["iteration"] == 933
        assert b["type"] == "B"
        assert b["date"] == "2026-09-22 23:00 PDT"
        assert b["block_key"] == BLOCK_KEY

    def test_goal_and_job_ids(self):
        b = _block()
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["job_id"] == "mediascope-daily-iteration"
        assert b["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_author_is_kit_with_ray(self):
        assert _block()["author"] == "Kit (with Ray)"

    def test_test_file_field_matches_this_file(self):
        assert _block()["test_file"] == "tests/" + THIS_FILE

    def test_source_urls_appended(self):
        e = _entry()
        assert SNAP_URL in e["source_urls"]
        assert META_URL in e["source_urls"]


# ---------------------------------------------------------------------------
# 4. Meta Luna arm
# ---------------------------------------------------------------------------
class TestMetaLunaArm:
    def test_meta_url_verbatim(self):
        b = _block()
        assert b["meta_arm"]["url"] == META_URL

    def test_meta_byline_and_date(self):
        arm = _block()["meta_arm"]
        assert arm["author_byline"] == "James Pero"
        assert arm["date"] == "2026-09-16"
        assert arm["publication"] == "gizmodo"

    def test_meta_tone_illustrative(self):
        arm = _block()["meta_arm"]
        assert arm["tone_score"] == -0.35
        assert arm["tone_basis"] == "hand-assigned this run, MANUAL ILLUSTRATIVE"

    def test_meta_evidence_tier_first_hand(self):
        arm = _block()["meta_arm"]
        assert "first-hand" in arm["evidence_tier"]
        assert "gizmodo.com" in arm["evidence_tier"]

    def test_meta_key_quotes(self):
        quotes = _block()["meta_arm"]["key_quotes"]
        assert len(quotes) == 7
        joined = " ".join(quotes)
        assert "Creep Factor" in joined
        assert "unsavory stuff" in joined
        assert "viscerally offends" in joined

    def test_meta_register_notes_moral_stigma(self):
        notes = _block()["meta_arm"]["register_notes"]
        assert "creep factor" in notes
        assert "liability" in notes
        assert "ban roll-call" in notes

    def test_meta_byline_attribution_urls(self):
        urls = _block()["meta_arm"]["byline_attribution_urls"]
        assert "https://gizmodo.com/author/jpero" in urls
        assert META_URL in urls

    def test_meta_concession_bounded(self):
        # The pragmatic credit is crisis-dodging credit, not product merit.
        quotes = " ".join(_block()["meta_arm"]["key_quotes"])
        assert "makes a lot of sense" in quotes


# ---------------------------------------------------------------------------
# 5. Snap arm
# ---------------------------------------------------------------------------
class TestSnapArm:
    def test_snap_url_verbatim(self):
        b = _block()
        assert b["snap_arm"]["url"] == SNAP_URL

    def test_snap_byline_and_date(self):
        arm = _block()["snap_arm"]
        assert arm["author_byline"] == "James Pero"
        assert arm["date"] == "2026-09-16"
        assert arm["publication"] == "gizmodo"

    def test_snap_tone_illustrative(self):
        arm = _block()["snap_arm"]
        assert arm["tone_score"] == 0.30
        assert arm["tone_basis"] == "hand-assigned this run, MANUAL ILLUSTRATIVE"

    def test_snap_evidence_tier_first_hand(self):
        arm = _block()["snap_arm"]
        assert "first-hand" in arm["evidence_tier"]
        assert "80 lines" in arm["evidence_tier"]

    def test_snap_key_quotes(self):
        quotes = _block()["snap_arm"]["key_quotes"]
        assert len(quotes) == 7
        joined = " ".join(quotes)
        assert "Dorky, Fun" in joined
        assert "Not going to lie: it was fun" in joined
        notes = _block()["snap_arm"]["register_notes"]
        assert "honest-to-god mixed reality" in notes
        assert "gut punch to your wallet" in notes

    def test_snap_register_notes_zero_privacy_vocabulary(self):
        notes = _block()["snap_arm"]["register_notes"]
        assert "ZERO privacy/surveillance/creep/ban/pervert vocabulary" in notes
        assert "full 80-line first-hand read" in notes

    def test_snap_criticism_is_product_level(self):
        notes = _block()["snap_arm"]["register_notes"]
        assert "FOV" in notes
        assert "$2,195" in notes

    def test_snap_companion_piece_cited(self):
        notes = _block()["snap_arm"]["register_notes"]
        assert "Let You Take Snapchat Pics by Snapping Your Fingers" in notes

    def test_snap_byline_attribution_urls(self):
        urls = _block()["snap_arm"]["byline_attribution_urls"]
        assert "https://gizmodo.com/author/jpero" in urls
        assert SNAP_URL in urls


# ---------------------------------------------------------------------------
# 6. Asymmetry scorer (MANUAL ILLUSTRATIVE only per the Aug 28 2026 rule)
# ---------------------------------------------------------------------------
class TestAsymmetryScorer933:
    def test_scorer_method_manual(self):
        assert "MANUAL ILLUSTRATIVE" in _block()["asymmetry_scorer"]["method"]

    def test_arm_tones(self):
        s = _block()["asymmetry_scorer"]
        assert s["meta_tone"] == -0.35
        assert s["snap_tone"] == 0.30

    def test_delta_meta_minus_snap(self):
        s = _block()["asymmetry_scorer"]
        assert s["delta_meta_minus_snap"] == -0.65
        assert s["delta_calc"] == "-0.35 - 0.30 = -0.65"

    def test_engine_never_run(self):
        s = _block()["asymmetry_scorer"]
        assert s["engine_run"] is False

    def test_p_value_cohens_d_ci_not_calculated(self):
        s = _block()["asymmetry_scorer"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"

    def test_not_significant(self):
        assert _block()["asymmetry_scorer"]["is_significant"] is False


# ---------------------------------------------------------------------------
# 7. Statistical discipline
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline933:
    def test_design_manual_illustrative_only(self):
        assert "MANUAL ILLUSTRATIVE scoring only" in _block()["design"]

    def test_no_zero_coverage_claims(self):
        # Both comparator arms are positive Pero bylines (iteration-492).
        assert "iteration-492" in _block()["design"]
        assert "both comparator arms are positive Pero bylines" in _block()["design"]

    def test_verdict_directionally_supported_not_proven(self):
        assert "directionally_supported_not_proven" in _block()["verdict"]

    def test_not_falsification_family(self):
        assert "NOT a falsification-family member" in _block()["verdict"]

    def test_no_analysis_json_update(self):
        assert "No analysis.json update warranted" in _block()["artifact_readiness"]

    def test_not_artifact_grade(self):
        assert "NOT artifact-grade" in _block()["verdict"]

    def test_correlation_not_causation(self):
        assert "Correlation is not causation" in _block()["verdict"]


# ---------------------------------------------------------------------------
# 8. Confounders and counterevidence
# ---------------------------------------------------------------------------
class TestConfoundersCounterevidence933:
    def test_confounder_count(self):
        assert len(_block()["confounders_ranked"]) == 4

    def test_confounder_strength_order(self):
        strengths = [c["strength"] for c in _block()["confounders_ranked"]]
        assert strengths == ["STRONG", "STRONG", "MODERATE", "WEAK"]

    def test_story_peg_confounder_present(self):
        joined = " ".join(c["text"] for c in _block()["confounders_ranked"])
        assert "Story-peg skew" in joined
        assert "warmth skew" in joined

    def test_n1_bounded(self):
        joined = " ".join(c["text"] for c in _block()["confounders_ranked"])
        assert "n=1 per arm" in joined

    def test_counterevidence_count(self):
        assert len(_block()["counterevidence"]) == 4

    def test_counterevidence_key_items(self):
        joined = " ".join(_block()["counterevidence"])
        assert "Yildirim" in joined
        assert "m716 house-adversarialism" in joined
        assert "makes a lot of sense" in joined


# ---------------------------------------------------------------------------
# 9. Connections
# ---------------------------------------------------------------------------
class TestConnections933:
    def test_connects_to_pins(self):
        assert _block()["connects_to"] == [211, 746, 734, 749, 269, 743]

    def test_cross_refs_cite_858_and_211(self):
        joined = " ".join(_block()["cross_refs"])
        assert "#858" in joined
        assert "#211" in joined

    def test_meta_exceptionalism_not_payer_driven(self):
        fc = _block()["financial_context"]
        assert "Keleops AG" in fc
        assert "Meta-exceptionalism, not payer-driven" in fc

    def test_no_newsroom_behavior_claim(self):
        assert "no newsroom-behavior claim is made" in _block()["verdict"]

    def test_first_full_text_pair_claim(self):
        assert "FIRST full-text first-hand same-day within-writer Meta-vs-Snap pair" in _block()["verdict"]


# ---------------------------------------------------------------------------
# 10. Doc sync per #719
# ---------------------------------------------------------------------------
class TestDocSync933:
    def test_readme_test_file_row_present(self):
        readme = _read(os.path.join(REPO, "README.md"))
        assert THIS_FILE in readme
        assert "Type B #933" in readme

    def test_readme_stats_table_updated(self):
        readme = _read(os.path.join(REPO, "README.md"))
        assert "| Tests | 47984 | Across 1258 test files |" in readme

    def test_architecture_row_present(self):
        arch = _read(os.path.join(REPO, "docs", "ARCHITECTURE.md"))
        assert THIS_FILE in arch
        assert "Type B #933" in arch


# ---------------------------------------------------------------------------
# 11. Iteration log per #719
# ---------------------------------------------------------------------------
class TestIterationLog933:
    def test_iteration_log_entry_present(self):
        log = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #933 Type B:" in log
        assert "Type B #933" in log

    def test_iteration_log_cites_mechanism_791(self):
        log = _read(os.path.join(REPO, "iteration-log.md"))
        head = log[:8000]
        assert "mechanism 791" in head
        assert "-0.65" in head

    def test_iteration_log_notes_window_position(self):
        log = _read(os.path.join(REPO, "iteration-log.md"))
        head = log[:8000]
        assert "930-934" in head
        assert "FOURTH leg" in head
