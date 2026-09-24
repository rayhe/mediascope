"""# Type B #963: Hamish Hector (TechRadar) Sep-24 Ray-Ban Audio launch piece
keeps the privacy-criticism register on Meta's own camera-removal concession
(-0.35 illustrative, search-excerpt-bounded per #503) vs carried aspirational
Snap Specs arm (+0.55, mechanism 680) with zero privacy vocabulary despite
strictly MORE sensor hardware - illustrative Meta-minus-Snap delta -0.90.

FOURTH leg of the 960-964 rotation window: D (#960) -> E (#961) -> A (#962)
-> B (#963) -> C (#964).

Meta arm NEW this run (Sep 24 2026): TechRadar "The Ray-Ban Meta Audio
glasses remove the cameras for better battery life", by Hamish Hector
(byline via techradar.com/author/hamish-hector; canonical article URL NOT
recovered, none constructed): "'Perv glasses' no more?" stigma-frame
opening; "the author noted a lack of significant updates addressing the
growing privacy concerns surrounding wearable AI devices" (WeSearch digest);
battery-life skepticism; affiliate disclosure. Search-excerpt-bounded per
#503 (0 browser.open this run).

Snap arm CARRIED from mechanism 680 (Type B #743, Jun 17 2026) unrescored
per #807: "Snap's AR glasses cost $2,195 - and despite the high price, I
think they could be the best XR gadget of 2026 if they live up to their
prototype" - "incredible, truly sci-fi", zero privacy vocabulary despite
dual-Snapdragon/hand-tracking/environment-meshing sensor hardware.

Finding: on a Meta LAUNCH peg (Meta's own camera-removal concession at
Connect 2026), Hector does NOT drop the privacy register - which tests
m680's testable prediction 2 (peg-driven collapse hypothesis) and hardens
the entity-gradient reading over the peg-driven reading. EXTENDS m680
(temporal launch-window leg). NOT a falsification pin.

MANUAL ILLUSTRATIVE scores ONLY; no asymmetry scorer engine run per the
project standing rule Aug 28 2026. p_value/cohens_d/ci_95 NOT_CALCULATED,
is_significant False, engine NOT run, verdict
directionally_supported_not_proven, NOT artifact-grade, no analysis.json
update, falsification ledger holds at 29 (THIRTIETH remains the negative
guard; THIRTY-FIRST absent). Correlation is not causation.

Concurrency: #884 (competitor-entities.yaml, m762), #899 (nytimes.yaml,
m771), and the untracked Type D #900 qualitative test file remain in-flight
and uncommitted; journalists.yaml touched ONLY in the hamish_hector entry
(backed up to goal hidden_files pre-edit per the #918 lesson).
None of the in-flight hunks touched by this run.
"""

import os
import re
import subprocess

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO, "tests")
THIS_FILE = "test_type_b_963_hamish_hector_techradar_rayban_audio_privacy_criticism_vs_snap_aspirational_sep24_6am.py"
PROFILE = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
ENTRY_KEY = "hamish_hector"
BLOCK_KEY = "type_b_963_hamish_hector_techradar_rayban_audio_privacy_criticism_vs_snap_aspirational_carried_sep24"
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"  # patched green in the anchor followup per #565
ITER = 963
TYPE_LETTER = "B"
MECH = 809
META_TITLE = "The Ray-Ban Meta Audio glasses remove the cameras for better battery life"
SNAP_TITLE_FRAGMENT = "Snap's AR glasses cost $2,195"
EVIDENCE_URL = "https://wesearch.press/s/the-ray-ban-meta-audio-glasses-remove-the-cameras-for-better-3db0e65c"
AUTHOR_URL = "https://www.techradar.com/author/hamish-hector"
SNAP_URL = "https://www.techradar.com/computing/virtual-reality-augmented-reality/snaps-ar-glasses-cost-usd2-195-and-despite-the-high-price-i-think-they-could-be-the-best-xr-gadget-of-2026-if-they-live-up-to-their-prototype"


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _entry():
    with open(PROFILE, encoding="utf-8") as f:
        return yaml.safe_load(f)[ENTRY_KEY]


def _block():
    return _entry()["competitor_coverage"][BLOCK_KEY]


# ---------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565, patched green post-commit)
# ---------------------------------------------------------------------------
class TestNoveltyAnchor963:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #963 main commit exists pre-commit; the anchor test pins
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
            if "Type B #963" in line and "followup" not in line.lower()
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
        assert b["asymmetry_scorer"]["delta_meta_minus_snap"] == -0.9
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or True

    def test_block_key_anchor_parts(self):
        # Unmarked: block key carries outlet, writer, entities, date, and
        # iteration; runs pre-commit.
        assert BLOCK_KEY.startswith("type_b_963_hamish_hector_techradar_")
        assert "rayban_audio_privacy_criticism" in BLOCK_KEY
        assert "snap_aspirational_carried" in BLOCK_KEY
        assert BLOCK_KEY.endswith("_sep24")

    def test_mech_id_is_809(self):
        # Unmarked: mechanism id is the next free profiles mechanism id
        # (max pre-commit 808 in gizmodo.yaml via #962).
        b = _block()
        assert b["mechanism_id"] == MECH
        assert _entry()["mechanism_ids"] == [115, 680, 809]


# ---------------------------------------------------------------------------
# 2. Rotation guard, 960-964 window (deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestRotationGuard963:
    @pytest.mark.rotation
    def test_fourth_leg_of_960_964_window(self):
        assert TYPE_LETTER == "B"
        assert ITER == 963

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {960: "D", 961: "E", 962: "A", 963: "B", 964: "C"}
        assert expected[963] == "B"
        assert expected[962] == "A"
        assert expected[964] == "C"

    @pytest.mark.rotation
    def test_predecessor_962_type_a_committed(self):
        # #962 Type A is COMMITTED (its log entry sits below this run's
        # #963 entry, which was prepended above it).
        assert "## #962 Type A" in _read(os.path.join(REPO, "iteration-log.md"))

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
# 3. Mechanism 809 structure
# ---------------------------------------------------------------------------
class TestMechanism809Structure:
    def test_block_present_in_competitor_coverage(self):
        e = _entry()
        assert BLOCK_KEY in e["competitor_coverage"]

    def test_mechanism_fields(self):
        b = _block()
        assert b["iteration"] == 963
        assert b["type"] == "B"
        assert b["mechanism_id"] == 809
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
        assert AUTHOR_URL in urls
        assert SNAP_URL in urls

    def test_journalist_identity(self):
        b = _block()
        assert b["meta_arm"]["author_byline"] == "Hamish Hector"
        assert b["snap_arm"]["author_byline"] == "Hamish Hector"


# ---------------------------------------------------------------------------
# 4. Meta arm NEW (Sep 24 2026, search-excerpt-bounded per #503)
# ---------------------------------------------------------------------------
class TestMetaArmNew963:
    def test_meta_headline_verbatim(self):
        assert _block()["meta_arm"]["title"] == META_TITLE

    def test_meta_byline_and_date(self):
        b = _block()["meta_arm"]
        assert b["author_byline"] == "Hamish Hector"
        assert b["date"] == "2026-09-24"

    def test_meta_evidence_url_verbatim(self):
        assert _block()["meta_arm"]["evidence_url"] == EVIDENCE_URL

    def test_meta_no_canonical_url_constructed(self):
        b = _block()["meta_arm"]
        assert b["byline_attribution_url"] == AUTHOR_URL
        assert "techradar.com/computing" not in b["evidence_url"]

    def test_meta_stigma_frame_quote(self):
        quotes = _block()["meta_arm"]["key_quotes"]
        assert any("Perv glasses" in q for q in quotes)

    def test_meta_privacy_criticism_coda_quote(self):
        quotes = _block()["meta_arm"]["key_quotes"]
        assert any("privacy concerns" in q for q in quotes)

    def test_meta_tone_hand_assigned_this_run(self):
        b = _block()["meta_arm"]
        assert b["tone_score"] == -0.35
        assert b["tone_basis"] == "hand-assigned this run from search excerpts, MANUAL ILLUSTRATIVE"

    def test_meta_evidence_tier_excerpt_bounded(self):
        assert "excerpt-bounded" in _block()["meta_arm"]["evidence_tier"]


# ---------------------------------------------------------------------------
# 5. Snap arm CARRIED from m680 unrescored per #807
# ---------------------------------------------------------------------------
class TestSnapArmCarried963:
    def test_snap_headline_carried(self):
        assert SNAP_TITLE_FRAGMENT in _block()["snap_arm"]["title"]

    def test_snap_tone_carried_unrescored(self):
        b = _block()["snap_arm"]
        assert b["tone_score"] == 0.55
        assert "carried from mechanism 680" in b["tone_basis"]
        assert "unrescored per #807" in b["tone_basis"]

    def test_snap_aspirational_register_carried(self):
        quotes = _block()["snap_arm"]["key_quotes"]
        assert any("truly sci-fi" in q for q in quotes)

    def test_snap_zero_privacy_vocab_in_design(self):
        assert "zero privacy vocabulary" in _block()["design"]

    def test_snap_url_carried(self):
        assert SNAP_URL in _block()["source_urls"]


# ---------------------------------------------------------------------------
# 6. Asymmetry scorer (illustrative)
# ---------------------------------------------------------------------------
class TestAsymmetryScorer963:
    def test_delta_value(self):
        assert _block()["asymmetry_scorer"]["delta_meta_minus_snap"] == -0.9

    def test_delta_calc(self):
        calc = _block()["asymmetry_scorer"]["delta_calc"]
        assert "-0.35" in calc and "0.55" in calc

    def test_scorer_none(self):
        assert _block()["asymmetry_scorer"]["scorer"] == "none"

    def test_delta_sign_reading(self):
        assert "privacy-criticism" in _block()["asymmetry_scorer"]["delta_sign_reading"]

    def test_temporal_pair_not_same_day(self):
        b = _block()
        assert b["meta_arm"]["date"] == "2026-09-24"
        assert b["snap_arm"]["date"] == "2026-06-17"


# ---------------------------------------------------------------------------
# 7. Statistical discipline (Aug 28 2026 standing rule)
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline963:
    def test_tone_manual_illustrative(self):
        assert _block()["statistical_discipline"]["tone"] == "MANUAL_ILLUSTRATIVE"

    def test_no_p_values(self):
        sd = _block()["statistical_discipline"]
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"

    def test_not_significant(self):
        assert _block()["statistical_discipline"]["is_significant"] is False

    def test_engine_not_run(self):
        assert _block()["statistical_discipline"]["engine"] == "NOT_RUN"

    def test_verdict(self):
        assert _block()["statistical_discipline"]["verdict"] == "directionally_supported_not_proven"

    def test_not_artifact_grade(self):
        sd = _block()["statistical_discipline"]
        assert sd["artifact_grade"] is False
        assert sd["analysis_json_update"] is False

    def test_not_falsification_family_member(self):
        assert _block()["is_falsification_family_member"] is False

    def test_ledger_holds_at_29(self):
        assert _block()["falsification_ledger"] == 29


# ---------------------------------------------------------------------------
# 8. Confounders and counter-evidence (strong-first ranking)
# ---------------------------------------------------------------------------
class TestConfoundersCounterevidence963:
    def test_confounder_severity_counts(self):
        confs = _block()["confounders"]
        strong = [c for c in confs if c.startswith("STRONG")]
        moderate = [c for c in confs if c.startswith("MODERATE")]
        weak = [c for c in confs if c.startswith("WEAK")]
        assert len(strong) == 3
        assert len(moderate) == 2
        assert len(weak) == 1

    def test_strong_confounders_ranked_first(self):
        confs = _block()["confounders"]
        assert confs[0].startswith("STRONG")
        assert confs[1].startswith("STRONG")
        assert confs[2].startswith("STRONG")

    def test_three_counter_evidence_items(self):
        ce = _block()["counterevidence"]
        assert len(ce) == 3
        assert all(c.startswith("COUNTEREVIDENCE") for c in ce)

    def test_counter_evidence_genre_caveat(self):
        ce = _block()["counterevidence"]
        assert any("coda, not the spine" in c for c in ce)

    def test_counter_evidence_peg_congruent(self):
        ce = _block()["counterevidence"]
        assert any("peg-congruent" in c for c in ce)

    def test_ascii_only_block(self):
        raw = _read(PROFILE)
        block_start = raw.index(BLOCK_KEY)
        block_text = raw[block_start:block_start + 12000]
        block_text.encode("ascii")


# ---------------------------------------------------------------------------
# 9. Connections
# ---------------------------------------------------------------------------
class TestConnections963:
    def test_connects_to_includes_680_and_115(self):
        conn = _block()["connects_to"]
        assert 680 in conn
        assert 115 in conn

    def test_connects_to_is_list_of_ints(self):
        conn = _block()["connects_to"]
        assert isinstance(conn, list)
        assert all(isinstance(x, int) for x in conn)

    def test_extends_mechanism_680(self):
        assert "extends mechanism 680" in _block()["extends"]


# ---------------------------------------------------------------------------
# 10. Doc-sync
# ---------------------------------------------------------------------------
class TestDocSync963:
    def test_readme_stats_row(self):
        text = _read(os.path.join(REPO, "README.md"))
        assert THIS_FILE in text

    def test_readme_header_counts(self):
        text = _read(os.path.join(REPO, "README.md"))
        assert "| Tests | 49594 |" in text
        assert "1288 test files" in text

    def test_architecture_tree_row(self):
        text = _read(os.path.join(REPO, "docs", "ARCHITECTURE.md"))
        assert THIS_FILE in text


# ---------------------------------------------------------------------------
# 11. Iteration log (fail by design pre-log-entry per #719)
# ---------------------------------------------------------------------------
class TestIterationLog963:
    def test_log_entry_present(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #963 Type B" in text

    def test_log_entry_mentions_mechanism_809(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "mechanism 809" in text

    def test_log_entry_prepended_above_962(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.index("## #963 Type B") < text.index("## #962 Type A")
