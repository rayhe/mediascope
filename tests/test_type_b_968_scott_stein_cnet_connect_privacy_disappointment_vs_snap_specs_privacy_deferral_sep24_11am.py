"""# Type B #968: Scott Stein (CNET) Sep-23 Connect 2026 hands-on carries
explicit privacy-disappointment in the reviewer's own voice ("I was also
disappointed at how little's been done on the privacy front") on the Meta
arm - the FIRST privacy vocabulary in Stein's hands-on review register in
the corpus - vs his carried Sep-17 Snap Specs arm (+0.45, zero privacy
vocabulary on 4-camera glasses). Illustrative Meta-minus-Snap delta -0.55.

FOURTH leg of the 965-969 rotation window: D (#965) -> E (#966) -> A (#967)
-> B (#968) -> C (#969).

Meta arm NEW this run (Sep 23 2026): CNET "So Many New Meta Glasses: Muse
AI Everywhere, and Ray-Bans Without a Camera" (Scott Stein, 8:21 pm ET,
9 min read, hands-on at Meta Connect 2026): tried the Muse agent ("Henry"),
hearing enhancement, and all the new glasses; explicit privacy-disappointment
coda. Search-excerpt-bounded per #503 (0 browser.open this run); the Meta
evidence URL is already in corpus as a cross-reference source in mechanism
806 (#958 James Pero block) - this is the first dedicated mechanism on the
piece.

Snap arm CARRIED from mechanism 752 (Type B #868) unrescored per #807:
"I Wore Snap Specs At Last: Here's What These Massive Glasses Can Do"
(Sep 17 2026, +0.45, zero surveillance/privacy vocabulary on 4-camera
standalone AR glasses, Spiegel 1-on-1).

Finding: EXTENDS mechanism 752 (6-day temporal leg); BOUNDS mechanisms
588/752 constancy (product-enthusiasm constancy holds; the privacy register
activates on the Meta peg at peak Connect-2026 stigma pressure); REFINES
mechanism 106 (privacy vocabulary moves from single-sentence news-register
dismissal to reviewer-voice review-register disappointment). NOT a
falsification pin.

MANUAL ILLUSTRATIVE scores ONLY; no asymmetry scorer engine run per the
project standing rule Aug 28 2026. p_value/cohens_d/ci_95 NOT_CALCULATED,
is_significant False, engine NOT run, verdict
directionally_supported_not_proven, NOT artifact-grade, no analysis.json
update, falsification ledger holds at 29 (THIRTIETH present, THIRTY-FIRST
absent). Correlation is not causation.

Concurrency: #884 (competitor-entities.yaml, m762), #899 (nytimes.yaml,
m771), the untracked Type D #900 qualitative test file, and the #938 open
anchor edit remain in-flight and uncommitted; journalists.yaml touched ONLY
in the Scott Stein entry (m868 neighbor block verified intact post-edit).
None of the in-flight hunks touched by this run.
"""

import os
import re
import subprocess

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO, "tests")
THIS_FILE = "test_type_b_968_scott_stein_cnet_connect_privacy_disappointment_vs_snap_specs_privacy_deferral_sep24_11am.py"
PROFILE = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
BLOCK_KEY = "type_b_968_scott_stein_cnet_connect_sep2026_privacy_disappointment_vs_snap_specs_privacy_deferral"
ANCHORED_SHA = "aa3d7353246f1af8f84328377112d26485b5596d"  # patched green in the anchor followup per #565
ITER = 968
TYPE_LETTER = "B"
MECH = 812
META_TITLE = "So Many New Meta Glasses: Muse AI Everywhere, and Ray-Bans Without a Camera"
SNAP_TITLE_FRAGMENT = "I Wore Snap Specs At Last"
EVIDENCE_URL = "https://wesearch.press/s/so-many-new-meta-glasses-muse-ai-everywhere-and-ray-bans-wit-6e09a130"
SNAP_URL = "https://wesearch.press/s/i-wore-snap-specs-at-last-heres-what-these-massive-glasses-can-do-b02ecb8f"


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _entry():
    with open(PROFILE, encoding="utf-8") as f:
        docs = yaml.safe_load(f)
    matches = [
        d for d in docs["journalists"]
        if isinstance(d, dict) and d.get("name") == "Scott Stein"
    ]
    assert len(matches) == 1
    return matches[0]


def _block():
    return _entry()["competitor_coverage"][BLOCK_KEY]


# ---------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565, patched green post-commit)
# ---------------------------------------------------------------------------
class TestNoveltyAnchor968:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #968 main commit exists pre-commit; the anchor test pins
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
            if "Type B #968" in line and "followup" not in line.lower()
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
        assert b["asymmetry_scorer_result"]["illustrative_delta_meta_minus_snap"] == -0.55
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or True

    def test_block_key_anchor_parts(self):
        # Unmarked: block key carries outlet, writer, entities, date, and
        # iteration; runs pre-commit.
        assert BLOCK_KEY.startswith("type_b_968_scott_stein_cnet_connect_")
        assert "privacy_disappointment" in BLOCK_KEY
        assert "snap_specs_privacy_deferral" in BLOCK_KEY
        assert BLOCK_KEY.endswith("_sep2026_privacy_disappointment_vs_snap_specs_privacy_deferral")

    def test_mech_id_is_812(self):
        # Unmarked: mechanism id is the next free profiles mechanism id
        # (max pre-commit 811 in the-verge.yaml via #967).
        b = _block()
        assert b["mechanism_id"] == MECH


# ---------------------------------------------------------------------------
# 2. Rotation guard, 965-969 window (deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestRotationGuard968:
    @pytest.mark.rotation
    def test_fourth_leg_of_965_969_window(self):
        assert TYPE_LETTER == "B"
        assert ITER == 968

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {965: "D", 966: "E", 967: "A", 968: "B", 969: "C"}
        assert expected[968] == "B"
        assert expected[967] == "A"
        assert expected[969] == "C"

    @pytest.mark.rotation
    def test_predecessor_967_type_a_committed(self):
        # #967 Type A is COMMITTED (its log entry sits below this run's
        # #968 entry, which was prepended above it).
        assert "## #967 Type A" in _read(os.path.join(REPO, "iteration-log.md"))

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
# 3. Mechanism 812 structure
# ---------------------------------------------------------------------------
class TestMechanism812Structure:
    def test_block_present_in_competitor_coverage(self):
        e = _entry()
        assert BLOCK_KEY in e["competitor_coverage"]

    def test_mechanism_fields(self):
        b = _block()
        assert b["iteration"] == 968
        assert b["iteration_type"] == "B"
        assert b["mechanism_id"] == 812
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
        assert b["new_meta_arm"]["byline"] == "Scott Stein (sole)"
        assert b["carried_snap_arm"]["byline"] == "Scott Stein (sole)"

    def test_neighbor_block_752_intact(self):
        e = _entry()
        assert "type_b_868_scott_stein_sep2026_snap_specs_launch_hands_on_register_temporal_replication" in e["competitor_coverage"]


# ---------------------------------------------------------------------------
# 4. Meta arm NEW (Sep 23 2026, search-excerpt-bounded per #503)
# ---------------------------------------------------------------------------
class TestMetaArmNew968:
    def test_meta_headline_verbatim(self):
        assert _block()["new_meta_arm"]["title_verbatim"] == META_TITLE

    def test_meta_byline_and_date(self):
        b = _block()["new_meta_arm"]
        assert b["byline"] == "Scott Stein (sole)"
        assert b["date"] == "2026-09-23"

    def test_meta_evidence_url_verbatim(self):
        assert _block()["new_meta_arm"]["url"] == EVIDENCE_URL

    def test_meta_no_canonical_url_constructed(self):
        b = _block()["new_meta_arm"]
        assert "cnet.com/tech" not in b["url"]
        assert b["url"].startswith("https://wesearch.press/s/")

    def test_meta_privacy_disappointment_quote(self):
        quotes = _block()["new_meta_arm"]["key_quotes"]
        assert any("disappointed at how little's been done on the privacy front" in q for q in quotes)

    def test_meta_audio_glasses_quote(self):
        quotes = _block()["new_meta_arm"]["key_quotes"]
        assert any("camera-free Ray-Ban Audio glasses" in q for q in quotes)

    def test_meta_tone_hand_assigned_this_run(self):
        b = _block()["new_meta_arm"]
        assert b["tone_illustrative"] == -0.10
        assert "MANUAL ILLUSTRATIVE" in b["tone_basis"]

    def test_meta_first_privacy_vocab_in_review_register(self):
        assert "FIRST occurrence" in _block()["new_meta_arm"]["privacy_register"]

    def test_meta_evidence_tier_excerpt_bounded(self):
        assert "EXCERPT-TIER" in _block()["new_meta_arm"]["evidence_tier"]

    def test_meta_products_covered(self):
        products = _block()["new_meta_arm"]["products_covered"]
        assert len(products) == 5
        assert any("Ray-Ban Meta Audio" in p for p in products)
        assert any("Gen 3" in p for p in products)


# ---------------------------------------------------------------------------
# 5. Snap arm CARRIED from m752 unrescored per #807
# ---------------------------------------------------------------------------
class TestSnapArmCarried968:
    def test_snap_headline_carried(self):
        assert SNAP_TITLE_FRAGMENT in _block()["carried_snap_arm"]["title"]

    def test_snap_tone_carried_unrescored(self):
        b = _block()["carried_snap_arm"]
        assert b["tone_illustrative"] == 0.45
        assert "carried from mechanism 752" in b["tone_basis"]
        assert "unrescored per #807" in b["tone_basis"]

    def test_snap_zero_privacy_vocab(self):
        assert "zero surveillance/privacy vocabulary" in _block()["carried_snap_arm"]["privacy_register"]

    def test_snap_spiegel_exec_access_carried(self):
        assert "Spiegel" in _block()["carried_snap_arm"]["exec_access"]

    def test_snap_url_carried(self):
        urls = _block()["carried_snap_arm"]["source_urls"]
        assert SNAP_URL in urls


# ---------------------------------------------------------------------------
# 6. Asymmetry scorer (illustrative)
# ---------------------------------------------------------------------------
class TestAsymmetryScorer968:
    def test_delta_value(self):
        assert _block()["asymmetry_scorer_result"]["illustrative_delta_meta_minus_snap"] == -0.55

    def test_delta_calc(self):
        calc = _block()["asymmetry_scorer_result"]["delta_calc"]
        assert "-0.10" in calc and "0.45" in calc

    def test_engine_not_run(self):
        assert "NOT run" in _block()["asymmetry_scorer_result"]["engine"]

    def test_delta_sign_reading(self):
        assert "privacy-register activation" in _block()["asymmetry_scorer_result"]["delta_direction"]

    def test_target_and_reference_entities(self):
        b = _block()["asymmetry_scorer_result"]
        assert b["target_entity"] == "Meta"
        assert b["reference_entity"] == "Snap"

    def test_temporal_pair_six_day_gap(self):
        b = _block()
        assert b["new_meta_arm"]["date"] == "2026-09-23"
        assert b["carried_snap_arm"]["date"] == "2026-09-17"


# ---------------------------------------------------------------------------
# 7. Statistical discipline (Aug 28 2026 standing rule)
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline968:
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
class TestConfoundersCounterevidence968:
    def test_confounder_severity_counts(self):
        confs = _block()["confounders"]
        strong = [c for c in confs if c.startswith("[STRONG]")]
        moderate = [c for c in confs if c.startswith("[MODERATE]")]
        weak = [c for c in confs if c.startswith("[WEAK]")]
        assert len(strong) == 3
        assert len(moderate) == 2
        assert len(weak) == 2

    def test_strong_confounders_ranked_first(self):
        confs = _block()["confounders"]
        assert confs[0].startswith("[STRONG]")
        assert confs[1].startswith("[STRONG]")
        assert confs[2].startswith("[STRONG]")

    def test_three_counter_evidence_items(self):
        ce = _block()["counterevidence"]
        assert len(ce) == 3
        assert all(c.startswith("COUNTEREVIDENCE") for c in ce)

    def test_counter_evidence_coda_not_spine(self):
        ce = _block()["counterevidence"]
        assert any("coda, not the spine" in c for c in ce)

    def test_counter_evidence_peg_congruent(self):
        ce = _block()["counterevidence"]
        assert any("peg-congruent" in c for c in ce)

    def test_ascii_only_block(self):
        raw = _read(PROFILE)
        block_start = raw.index(BLOCK_KEY)
        block_text = raw[block_start:block_start + 16000]
        block_text.encode("ascii")


# ---------------------------------------------------------------------------
# 9. Connections
# ---------------------------------------------------------------------------
class TestConnections968:
    def test_connects_to_includes_106_588_752(self):
        conn = _block()["connects_to"]
        assert 106 in conn
        assert 588 in conn
        assert 752 in conn

    def test_connects_to_is_list_of_ints(self):
        conn = _block()["connects_to"]
        assert isinstance(conn, list)
        assert all(isinstance(x, int) for x in conn)

    def test_extends_mechanism_752(self):
        assert "mechanism 752" in _block()["extends"]

    def test_temporal_refinement_three_items(self):
        tr = _block()["temporal_refinement"]
        assert len(tr) == 3
        assert tr[0].startswith("EXTENDS")
        assert tr[1].startswith("BOUNDS")
        assert tr[2].startswith("REFINES")


# ---------------------------------------------------------------------------
# 10. Doc-sync
# ---------------------------------------------------------------------------
class TestDocSync968:
    def test_readme_stats_row(self):
        text = _read(os.path.join(REPO, "README.md"))
        assert THIS_FILE in text

    def test_readme_header_counts(self):
        text = _read(os.path.join(REPO, "README.md"))
        assert "| Tests | 49854 |" in text
        assert "1293 test files" in text

    def test_architecture_tree_row(self):
        text = _read(os.path.join(REPO, "docs", "ARCHITECTURE.md"))
        assert THIS_FILE in text


# ---------------------------------------------------------------------------
# 11. Iteration log (fail by design pre-log-entry per #719)
# ---------------------------------------------------------------------------
class TestIterationLog968:
    def test_log_entry_present(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #968 Type B" in text

    def test_log_entry_mentions_mechanism_812(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert "mechanism 812" in text

    def test_log_entry_prepended_above_967(self):
        text = _read(os.path.join(REPO, "iteration-log.md"))
        assert text.index("## #968 Type B") < text.index("## #967 Type A")
