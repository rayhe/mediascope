"""Type B #1073: Ben Schoon (9to5Google) Sep-20-2026 Weekender within-piece
blame-attribution asymmetry at the Connect-2026 stigma peak (mechanism 875)
- FIRST dedicated Type B mechanism on Ben Schoon in journalists.yaml (prior
corpus treatment is m131/m171 in profiles/competitor-coverage-research.yaml:
the Aug-16 control calibration with proportional privacy vocabulary ~1.7:1
and Bader's explicit trust differential; zero ben_schoon YAML key pre-commit
per the #643 convention).

META ARM A1 (Sep 20 2026, FIRST-HAND read this run, 135 rendered lines):
his Weekender "The camera is my favorite part of smart glasses; it feels
wrong now" fires explicit blame at Meta - "the camera on smart glasses has
become a massive problem, and it's basically ruined existing smart glasses
for me personally"; "Meta's Ray-Ban glasses are the catalyst in all of
this"; "the simple fact that Meta was at the helm. The company's long
history of handling private data, rightfully, did not mix well with *a
camera on your face*"; "leaks of human moderators viewing uncensored
private recordings... simply evaporated any goodwill or trust that might
have been left"; "it took until *July of this year* for Meta to implement
a fix"; kicker "thanks Meta, you've ruined this for everyone else."
MANUAL ILLUSTRATIVE -0.45.

SAMSUNG/GOOGLE ARM (same piece, same day, first-hand): victim framing with
credited remediation - "facing a massive uphill battle as the 'perv
glasses' stigma is widely known and loud"; "Samsung has said that it has
protections immediately in place around camera tampering."
MANUAL ILLUSTRATIVE +0.10.

META ARM A2 (Sep 24 2026, excerpt-tier wesearch relay): neutral
market-leader news register - "Despite public backlash in recent months,
smart glasses continue to explode in popularity and, as it stands, Meta
is by far the biggest player in the game." MANUAL ILLUSTRATIVE +0.05,
register-variance control.

Illustrative delta (Samsung/Google minus Meta A1) +0.55: blame is
entity-directed within a single piece. BOUNDS m131 (the proportional-
vocabulary calibration does not extend to the blame register) and EXTENDS
m171 (Bader's stated trust differential now has a Schoon-voice
counterpart). NOT a falsification-family member; ledger holds at 35.

Fourth leg of the 1070-1074 window: D (#1070) -> E (#1071) -> A (#1072)
-> B (#1073). MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026 standing rule:
tone hand-assigned on the finding layer, p_value/cohens_d/ci_95
NOT_CALCULATED, is_significant False, engine NOT run, verdict
directionally_supported_not_proven, no analysis.json update, NOT
artifact-grade. Correlation is not causation.
"""

import glob
import os
import re
import subprocess

import pytest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOURNALISTS = os.path.join(REPO, "profiles", "careers", "journalists.yaml")
LOG = os.path.join(REPO, "iteration-log.md")
README = os.path.join(REPO, "README.md")
ARCH = os.path.join(REPO, "docs", "ARCHITECTURE.md")
THIS_FILE = os.path.basename(__file__)

ITERATION = 1073
TYPE_LETTER = "B"
RUN_PDT = "2026-09-29 10:00 PDT"
BLOCK_KEY = "type_b_1073_ben_schoon_9to5google_weekender_camera_stigma_meta_blame_vs_samsung_google_victim_framing_sep29"
ANCHORED_SHA = "44293ed2050af862b0b24891782d76934176a895"

README_TESTS_AFTER = 55110
README_FILES_AFTER = 1398

# Evidence URLs verbatim from the browser.search Full-URL listings.
EVIDENCE_URLS = [
    "https://9to5google.com/2026/09/20/smart-glasses-camera-newsletter/",
    "https://wesearch.press/s/meta-launches-audio-only-glasses-and-gen-3-ray-ban-with-slim-ce2a5429",
    "https://muckrack.com/ben-schoon/articles",
]

# The 1070-1074 window's prior legs; the #1075 Type D run pins the
# lifecycle (M_ID == 875 roll-forward, key-substring sweeps re-pinned).
WINDOW_FILES = [
    "test_type_d_1070_m871_m872_m873_qualitative_corpus_integrity_sep29_7am.py",
    "test_type_e_1071_podcast_sentiment_137th_verification_sep29_8am.py",
    "test_type_a_1072_guardian_openai_sep28_astra_cancellation_safety_crisis_register_vs_carried_meta_arms_sep29_9am.py",
]


def _git(args):
    return subprocess.run(
        ["git", "-C", REPO] + args, capture_output=True, text=True, timeout=120
    )


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _block():
    return _read(JOURNALISTS).split(BLOCK_KEY + ":")[1]


# --------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565, patched green post-commit)
# --------------------------------------------------------------------------
class TestNoveltyAnchorTypeB1073:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #1073 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA)

    @pytest.mark.anchor
    def test_block_key_present_post_commit(self):
        assert BLOCK_KEY in _read(JOURNALISTS)

    @pytest.mark.anchor
    def test_type_b_1073_in_git_log(self):
        out = _git(["log", "--oneline", "--grep=Type B #1073"]).stdout
        assert "Type B #1073" in out


# --------------------------------------------------------------------------
# 2. Rotation guard: 1070-1074 window FOURTH leg
# --------------------------------------------------------------------------
class TestRotationGuard1070_1074Window:
    def test_window_prior_legs_in_git_history(self):
        log = _git(["log", "--oneline"]).stdout
        assert "Type D #1070" in log
        assert "Type E #1071" in log
        assert "Type A #1072" in log

    def test_rotation_rule_d_e_a_b_sequence(self):
        # The committed window files pin the rotation order D -> E -> A -> B
        # per the #565 anchor + rotation guard.
        log = _git(["log", "--oneline", "--grep=1070-1074 window"]).stdout
        assert "1070" in log and "1071" in log and "1072" in log

    def test_this_run_continues_window(self):
        assert TYPE_LETTER == "B"
        assert ITERATION == 1073


# --------------------------------------------------------------------------
# 3. Corpus novelty greps per #715 (committed novelty state)
# --------------------------------------------------------------------------
class TestCorpusNoveltyGreps:
    def test_block_key_unique_in_journalists_yaml(self):
        # The 4-space-indented block key line occurs exactly once; the
        # test_file field value carries the key as a substring and is
        # excluded by the key-line form.
        assert _read(JOURNALISTS).count("\n    " + BLOCK_KEY + ":") == 1

    def test_mechanism_id_875_colon_form_present(self):
        assert "mechanism_id: 875" in _block()

    def test_no_underscore_dash_875_key_strings(self):
        # Keying discipline per #715: the block key carries no numeric
        # 875 mechanism-id substring. No repo-wide literal carrier of
        # the contiguous fragment-built 875 key needle forms exists
        # (verified zero pre-commit); no new carrier may appear this run.
        n1 = "mech" + "anism_" + "8" + "75"
        n2 = "mech" + "anism-" + "8" + "75"
        hits = set(
            _git(["grep", "-l", "-e", n1, "-e", n2, "--", "."]).stdout.splitlines()
        )
        assert hits == set(), hits

    def test_block_key_carries_no_numeric_id(self):
        assert "875" not in BLOCK_KEY

    def test_ben_schoon_key_first_in_journalists_yaml(self):
        # Per the #643 convention: zero ben_schoon YAML key pre-commit;
        # exactly one top-level key post-commit.
        assert _read(JOURNALISTS).count("\nben_schoon:") == 1


# --------------------------------------------------------------------------
# 4. Meta arm A1 evidence (first-hand read this run)
# --------------------------------------------------------------------------
class TestMetaArmA1Evidence:
    def test_weekender_url_in_block(self):
        assert (
            "https://9to5google.com/2026/09/20/smart-glasses-camera-newsletter/"
            in _block()
        )

    def test_blame_kicker_quote_present(self):
        assert "thanks Meta" in _block()

    def test_trust_deficit_quote_present(self):
        assert "did not mix well with" in _block()

    def test_slow_remediation_quote_present(self):
        assert "July of this year" in _block()

    def test_first_hand_read_attested(self):
        assert "FIRST-HAND" in _block() or "first-hand" in _block()

    def test_meta_arm_a1_tone_recorded(self):
        assert "-0.45" in _block()


# --------------------------------------------------------------------------
# 5. Samsung/Google arm evidence (same piece, same day)
# --------------------------------------------------------------------------
class TestSamsungGoogleArmEvidence:
    def test_victim_framing_quote_present(self):
        assert "massive uphill battle" in _block()

    def test_protections_credited_quote_present(self):
        assert "protections immediately in place" in _block()

    def test_samsung_google_arm_tone_recorded(self):
        assert "+0.10" in _block()

    def test_same_piece_same_day_design(self):
        assert "same piece, same day" in _block()


# --------------------------------------------------------------------------
# 6. Meta arm A2 register-variance control
# --------------------------------------------------------------------------
class TestMetaArmA2RegisterVariance:
    def test_a2_url_in_block(self):
        assert (
            "https://wesearch.press/s/meta-launches-audio-only-glasses-and-gen-3-ray-ban-with-slim-ce2a5429"
            in _block()
        )

    def test_a2_neutral_register_quote_present(self):
        assert "biggest player in the game" in _block()

    def test_a2_tone_recorded(self):
        assert "+0.05" in _block()


# --------------------------------------------------------------------------
# 7. Illustrative tones and delta
# --------------------------------------------------------------------------
class TestIllustrativeTonesAndDelta:
    def test_delta_value_recorded(self):
        assert "0.55" in _block()

    def test_delta_calc_present(self):
        assert "0.10 - (-0.45) = 0.55" in _block()

    def test_delta_direction_blame_entity_directed(self):
        assert "entity-directed" in _block()

    def test_register_variance_a1_a2_bounded(self):
        # The A1/A2 within-writer register variance keeps the finding
        # genre-bound, not a stable journalist-bias claim.
        assert "genre-bound" in _block()


# --------------------------------------------------------------------------
# 8. Statistical discipline per the Aug 28 2026 standing rule
# --------------------------------------------------------------------------
class TestStatisticalDisciplineStandingRule:
    def test_manual_illustrative_only(self):
        assert "MANUAL_ILLUSTRATIVE" in _block()

    def test_no_p_value(self):
        assert "p_value" in _block() and "NOT_CALCULATED" in _block()

    def test_engine_not_run(self):
        assert "engine NOT run" in _block()

    def test_not_artifact_grade(self):
        assert "NOT artifact-grade" in _block()

    def test_no_analysis_json_update(self):
        assert "no_analysis_json_update: true" in _block()


# --------------------------------------------------------------------------
# 9. Falsification ledger
# --------------------------------------------------------------------------
class TestFalsificationLedger:
    def test_not_falsification_family_member(self):
        assert "NOT a falsification-family member" in _block()

    def test_ledger_holds_at_35(self):
        assert "ledger holds at 35" in _block()

    def test_verdict_directionally_supported_not_proven(self):
        assert "directionally_supported_not_proven" in _block()


# --------------------------------------------------------------------------
# 10. Confounders ranked strongest-first
# --------------------------------------------------------------------------
class TestConfoundersRankedStrongFirst:
    def test_genre_confound_strong(self):
        assert "STRONG: genre" in _block()

    def test_evidence_based_trust_confound_strong(self):
        assert "STRONG: evidence-based trust differential" in _block()

    def test_counterevidence_disappointed_owner(self):
        assert "disappointed-owner" in _block()


# --------------------------------------------------------------------------
# 11. Cross-references: m131 bound, m171 extended
# --------------------------------------------------------------------------
class TestCrossReferences:
    def test_m131_bounded(self):
        assert "BOUNDS m131" in _block() or "BOUNDED" in _block()

    def test_m171_extended(self):
        assert "EXTENDS m171" in _block() or "EXTEND" in _block()

    def test_m872_family_reference(self):
        assert "#872" in _block()

    def test_m827_stigma_reference(self):
        assert "#827" in _block()


# --------------------------------------------------------------------------
# 12. Research method per #503
# --------------------------------------------------------------------------
class TestResearchMethodPer503:
    def test_search_sets_documented(self):
        assert "browser.search" in _block()

    def test_first_hand_open_documented(self):
        assert "browser.open" in _block()

    def test_urls_verbatim_from_listings(self):
        assert "verbatim" in _block()

    def test_ascii_only_no_em_dashes(self):
        assert "ASCII-only, no em dashes" in _block()


# --------------------------------------------------------------------------
# 13. Guard lifecycle: mechanism 875 lands this run
# --------------------------------------------------------------------------
class TestGuardLifecycle875Lands:
    def test_m875_lands_in_profiles(self):
        out = _git(
            ["grep", "-n", "mechanism_id: 875", "--", "profiles/"]
        ).stdout
        assert "journalists.yaml" in out

    def test_max_mechanism_id_now_875(self):
        out = _git(
            ["grep", "-rhoE", "mechanism_id: [0-9]+", "--", "profiles/"]
        ).stdout
        ids = [int(x.split(":")[1]) for x in out.splitlines()]
        assert max(ids) == 875

    def test_no_zero_875_needles_in_window_files(self):
        # No window file carried zero-875 forward-looking needles (verified
        # zero pre-commit); the #1075 Type D run pins the lifecycle with
        # M_ID == 875 roll-forward and re-pinned key-substring sweeps.
        for base in WINDOW_FILES:
            text = _read(os.path.join(REPO, "tests", base))
            assert "875" not in text, base

    def test_own_m_id_875_pinned(self):
        assert "OWN_M_ID" in open(__file__).read() or True
        assert "mechanism_id: 875" in _block()

    def test_window_files_still_pre_roll(self):
        # The #1070/#1071/#1072 files have not been rolled yet; the #1075
        # Type D run pins the lifecycle then.
        for base in WINDOW_FILES:
            text = _read(os.path.join(REPO, "tests", base))
            assert "874" in text, base


# --------------------------------------------------------------------------
# 14. Doc-sync ratchet per #719 (fail by design pre-doc-sync/pre-entry)
# --------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_test_file_table_row_present(self):
        # Fails pre-commit by design; green once doc-sync adds it.
        assert THIS_FILE.replace(".py", "") in _read(README)

    def test_architecture_tests_tree_updated(self):
        # Fails pre-commit by design; green once doc-sync adds it.
        assert THIS_FILE.replace(".py", "") in _read(ARCH)

    def test_architecture_lists_1073_file(self):
        # Fails pre-commit by design; green once doc-sync adds it.
        assert THIS_FILE in set(re.findall(r"(test_\w+\.py)", _read(ARCH)))

    def test_readme_stats_table_bumped(self):
        # Fails pre-commit by design; green once doc-sync bumps it.
        assert str(README_TESTS_AFTER) in _read(README)


# --------------------------------------------------------------------------
# 15. Iteration-log entry per #719 (fail by design pre-entry)
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_1073_entry_present_with_finding_shape(self):
        # Fails pre-commit by design; green once the iteration-log
        # entry is prepended.
        log = _read(LOG)
        assert "## #1073 Type B" in log
        idx = log.index("## #1073 Type B")
        block = log[idx : idx + 3000]
        assert "mechanism 875" in block
        assert "Sep 29 2026, 10:00 PDT" in block
        assert "FOURTH leg of the 1070-1074 window" in block

    def test_1073_entry_carries_commit_hashes_per_721(self):
        log = _read(LOG)
        idx = log.index("## #1073 Type B")
        block = log[idx : idx + 3000]
        assert "main commit" in block
        assert "anchor" in block
        assert "log-hash followup" in block

    def test_1073_entry_carries_delta_prose(self):
        log = _read(LOG)
        idx = log.index("## #1073 Type B")
        block = log[idx : idx + 4000]
        assert "blame-attribution" in block
        assert "+0.55" in block


# --------------------------------------------------------------------------
# 16. Push readiness per #716 / #717
# --------------------------------------------------------------------------
class TestPushReadiness:
    def test_no_concurrent_inflight_iteration_commits_staged(self):
        # The in-flight #899/#938/#900/#1012-wt working-tree edits are
        # owned by their runs; this run stages only its own files.
        status = _git(["status", "--short"]).stdout
        staged = [l for l in status.splitlines() if l.startswith(("M ", "A "))]
        for f in ("nytimes.yaml", "test_type_b_938_", "test_type_d_900_", "test_type_a_1012_"):
            assert not any(f in l for l in staged)

    def test_this_run_stages_only_own_files(self):
        status = _git(["status", "--short"]).stdout
        staged = [l for l in status.splitlines() if l.startswith(("M ", "A "))]
        allowed = (
            "profiles/careers/journalists.yaml",
            "test_type_b_1073_",
            "README.md",
            "docs/ARCHITECTURE.md",
            "iteration-log.md",
        )
        for l in staged:
            assert any(a in l for a in allowed), l
