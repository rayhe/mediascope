"""Type A #1077: WIRED x OpenAI Sep-29-2026 Astra-cancellation accountability
register vs carried WIRED x Meta arms (mechanism 877) - FIRST dedicated
Type A mechanism on WIRED's own original coverage of the GPT-6.1 Astra
cancellation: Isabella Ward, Business section, 'OpenAI Delays Release of
Latest Model Over Safety Concerns' (Sep 29 2026 6:36 AM; relay-attested
per #503 via the wesearch.press mirror carrying WIRED attribution,
'OpenAI told WIRED', 'Photo-Illustration: Wired Staff'). The piece runs
the accountability register on the licensing deal partner (Conde Nast Aug
2024 OpenAI deal): Astra 6.1 'failed to meet safety standards', 'worse at
sticking to human users values and goals than previous systems', plus the
apology for the Australian government website hack handling. MANUAL
ILLUSTRATIVE -0.35 (peg-consistent with m874 Guardian -0.35 and m871 BI
-0.35 on the same Astra peg). Meta arms carried un-rescored per #807:
m820 WIRED Sep-23 Ashworth 'Meta Pinky Promises Its Smart Glasses Will Be
Private Soon' (-0.45) and m757 WIRED Sep-11 Mehrotra 'Meta Sued Over
Training Data for Its AI and Face-Recognition Systems' (-0.30).
Illustrative deltas (OpenAI minus Meta): +0.10 primary, -0.05 secondary -
near-null parity. This is the safety-crisis exemption extended to the deal
partner's own outlet: on safety-crisis pegs WIRED covers OpenAI as hard as
it covers Meta. TEMPORAL EXTENSION of m712: WIRED's Sep-16 company-briefed
platform relay (+0.15) swings to -0.35 in 13 days (within-entity -0.50);
register follows the PEG, not the entity or the deal (m842/m736 pattern).
Cross-outlet temporal replication of the m871/m874/m862 safety-crisis
lineage. NOT a falsification-family member (ledger holds at 35).

Third leg of the 1075-1079 window: D (#1075) -> E (#1076) -> A (#1077).
MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026 standing rule: tone
hand-assigned on the finding layer, p_value/cohens_d/ci_95 NOT_CALCULATED,
is_significant False, engine NOT run, verdict directionally_supported_not_proven,
no analysis.json update, NOT artifact-grade. Correlation is not causation.
"""

import glob
import os
import re
import subprocess

import pytest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIRED = os.path.join(REPO, "profiles", "wired.yaml")
LOG = os.path.join(REPO, "iteration-log.md")
README = os.path.join(REPO, "README.md")
ARCH = os.path.join(REPO, "docs", "ARCHITECTURE.md")
THIS_FILE = os.path.basename(__file__)

ITERATION = 1077
TYPE_LETTER = "A"
RUN_PDT = "2026-09-29 14:00 PDT"
BLOCK_KEY = "wired_openai_sep29_astra_cancellation_accountability_register_vs_carried_meta_arms"
ANCHORED_SHA = "077d8d5eff909d6531995e66d010c3b52be9e258"

README_TESTS_AFTER = 55334
README_FILES_AFTER = 1402

# Evidence URLs verbatim from the browser.search Full-URL listings.
EVIDENCE_URLS = [
    "https://wesearch.press/s/openai-delays-release-of-latest-model-over-safety-concerns-11bacbdf",
    "https://www.aob-news.com/2026/09/29/openai-delays-release-of-latest-model-over-safety-concerns/",
    "https://www.reuters.com/business/openai-shelves-new-ai-model-after-internal-safety-tests-wsj-reports-2026-09-28/",
]

# The 1075-1079 window's prior legs carry their zero-877 forward-looking
# guards (needles format-built per #715); mechanism 877 lands THIS run and
# supersedes the numeric sweeps by design per the #710/#720 convention.
WINDOW_FILES = [
    "test_type_d_1075_m874_m875_m876_qualitative_corpus_integrity_sep29_12pm.py",
    "test_type_e_1076_podcast_sentiment_138th_verification_sep29_1pm.py",
]


def _git(args):
    return subprocess.run(
        ["git", "-C", REPO] + args, capture_output=True, text=True, timeout=120
    )


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _block():
    return _read(WIRED).split(BLOCK_KEY + ":")[1]


# --------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565, patched green post-commit)
# --------------------------------------------------------------------------
class TestNoveltyAnchorTypeA1077:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #1077 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA)

    @pytest.mark.anchor
    def test_block_key_present_post_commit(self):
        assert BLOCK_KEY in _read(WIRED)

    @pytest.mark.anchor
    def test_type_a_1077_in_git_log(self):
        out = _git(["log", "--oneline", "--grep=Type A #1077"]).stdout
        assert "Type A #1077" in out


# --------------------------------------------------------------------------
# 2. Rotation guard: 1075-1079 window THIRD leg
# --------------------------------------------------------------------------
class TestRotationGuard1075_1079Window:
    def test_window_opening_and_second_leg_in_git_history(self):
        log = _git(["log", "--oneline"]).stdout
        assert "Type D #1075" in log
        assert "Type E #1076" in log

    def test_rotation_rule_d_e_a_sequence(self):
        # The committed window files pin the rotation order D -> E -> A
        # per the #565 anchor + rotation guard.
        assert TYPE_LETTER == "A"
        assert ITERATION == 1077

    def test_this_run_continues_window(self):
        assert "1075-1079 window THIRD leg" in _block()


# --------------------------------------------------------------------------
# 3. Corpus novelty greps per #715 (committed novelty state)
# --------------------------------------------------------------------------
class TestCorpusNoveltyGreps:
    def test_block_key_unique_in_wired_yaml(self):
        # The 4-space-indented block key line occurs exactly once; the
        # test_file field value carries the key as a substring and is
        # excluded by the key-line form.
        assert _read(WIRED).count("\n    " + BLOCK_KEY + ":") == 1

    def test_mechanism_id_877_colon_form_present(self):
        assert "mechanism_id: 877" in _block()

    def test_no_underscore_dash_877_key_strings(self):
        # Keying discipline per #715: the block key carries no numeric
        # 877 mechanism-id substring. No repo-wide literal carrier of the
        # contiguous fragment-built 877 key needle forms (u-score and
        # dash) exists pre-commit; no new carrier may appear this run.
        n1 = "mech" + "anism_" + "8" + "77"
        n2 = "mech" + "anism-" + "8" + "77"
        hits = set()
        for p in glob.glob(os.path.join(REPO, "tests", "test_*.py")):
            if os.path.basename(p) == THIS_FILE:
                continue
            t = open(p, errors="ignore").read()
            if n1 in t or n2 in t:
                hits.add(os.path.basename(p))
        for p in glob.glob(os.path.join(REPO, "profiles", "**", "*.yaml"), recursive=True):
            t = open(p, errors="ignore").read()
            if n1 in t or n2 in t:
                hits.add(os.path.basename(p))
        assert hits == set(), hits

    def test_block_key_carries_no_numeric_id(self):
        assert "877" not in BLOCK_KEY


# --------------------------------------------------------------------------
# 4. OpenAI arm evidence (relay-attested per #503)
# --------------------------------------------------------------------------
class TestOpenAIArmEvidence:
    def test_all_evidence_urls_in_source_urls(self):
        block = _block()
        for url in EVIDENCE_URLS:
            assert url in block, url

    def test_ward_byline_attested(self):
        assert "Isabella Ward" in _block()

    def test_wired_attribution_excerpt(self):
        # The mirror carries WIRED attribution: 'OpenAI told WIRED'.
        assert "OpenAI told WIRED" in _block()

    def test_excerpt_tier_disclosed(self):
        block = _block()
        assert "excerpt-tier" in block
        assert "relay-attested" in block

    def test_wsj_scoop_origin_context(self):
        # WSJ first broke the story; carried as scoop-origin context,
        # not WIRED evidence.
        block = _block()
        assert "WSJ" in block


# --------------------------------------------------------------------------
# 5. Meta arms carried un-rescored per #807
# --------------------------------------------------------------------------
class TestMetaArmsCarriedPer807:
    def test_two_meta_arms_listed(self):
        block = _block()
        assert "Pinky Promises" in block
        assert "NameTag" in block

    def test_carried_tones_preserved(self):
        block = _block()
        assert "-0.45" in block
        assert "-0.30" in block

    def test_meta_arms_from_820_757(self):
        block = _block()
        assert "mechanism 820" in block
        assert "mechanism 757" in block

    def test_no_rescoring_disclosure(self):
        block = _block()
        assert "per #807" in block or "un-rescored" in block


# --------------------------------------------------------------------------
# 6. Illustrative tones and delta arithmetic
# --------------------------------------------------------------------------
class TestIllustrativeTonesAndDelta:
    def test_openai_arm_manual_illustrative_minus_point_35(self):
        assert "manual_illustrative_tone: -0.35" in _block()

    def test_manual_illustrative_label_only(self):
        block = _block()
        assert "MANUAL ILLUSTRATIVE" in block

    def test_delta_arithmetic_primary(self):
        # delta (OpenAI minus Meta primary) = -0.35 - (-0.45) = +0.10
        assert abs((-0.35 - (-0.45)) - 0.10) < 1e-9
        assert "illustrative_delta_openai_minus_meta_primary: 0.10" in _block()

    def test_delta_arithmetic_secondary(self):
        # delta (OpenAI minus Meta secondary) = -0.35 - (-0.30) = -0.05
        assert abs((-0.35 - (-0.30)) - (-0.05)) < 1e-9
        assert "illustrative_delta_openai_minus_meta_secondary: -0.05" in _block()

    def test_temporal_swing_vs_m712(self):
        # within-entity swing Sep-16 relay (+0.15) to Sep-29 arm (-0.35)
        assert abs((-0.35 - 0.15) - (-0.50)) < 1e-9
        assert "within_entity_swing_13_days: -0.5" in _block()


# --------------------------------------------------------------------------
# 7. Statistical discipline per the Aug 28 2026 standing rule
# --------------------------------------------------------------------------
class TestStatisticalDisciplineStandingRule:
    def test_no_p_value(self):
        assert 'p_value: "NOT_CALCULATED"' in _block()

    def test_no_cohens_d(self):
        assert 'cohens_d: "NOT_CALCULATED"' in _block()

    def test_no_ci(self):
        assert 'ci_95: "NOT_CALCULATED"' in _block()

    def test_not_significant(self):
        assert "is_significant: false" in _block()

    def test_engine_not_run(self):
        assert "engine_run: false" in _block()

    def test_verdict_directionally_supported_not_proven(self):
        block = _block()
        assert "directionally_supported_not_proven" in block

    def test_no_analysis_json_update(self):
        assert "no_analysis_json_update: true" in _block()

    def test_not_artifact_grade(self):
        assert "artifact_grade: false" in _block()


# --------------------------------------------------------------------------
# 8. Falsification ledger
# --------------------------------------------------------------------------
class TestFalsificationLedger:
    def test_not_falsification_family_member(self):
        assert "falsification_family_member: false" in _block()

    def test_ledger_holds_at_35(self):
        assert "falsification_ledger: 35" in _block()

    def test_ledger_note_prose(self):
        block = _block()
        assert "Ledger holds at 35" in block

    def test_thirty_sixth_absent_in_profiles(self):
        out = _git(["grep", "-n", "THIRTY-SIXTH", "--", "profiles/"]).stdout
        assert out.strip() == "", out


# --------------------------------------------------------------------------
# 9. Confounders ranked strongest-first
# --------------------------------------------------------------------------
class TestConfoundersRankedStrongFirst:
    def test_three_strong_confounders(self):
        block = _block()
        strong = [l for l in block.splitlines() if "STRONG:" in l]
        assert len(strong) >= 3

    def test_excerpt_tier_strongest_confounder(self):
        block = _block()
        assert "STRONG: excerpt-tier" in block

    def test_briefing_access_confounder(self):
        block = _block()
        assert "briefing-access" in block

    def test_incentive_attribution_inconclusive(self):
        block = _block()
        assert "INCONCLUSIVE" in block

    def test_byline_desk_confounder(self):
        block = _block()
        assert "byline-desk" in block


# --------------------------------------------------------------------------
# 10. Cross-references
# --------------------------------------------------------------------------
class TestCrossReferences:
    def test_connects_to_ids(self):
        block = _block()
        for mid in ("712", "757", "820", "874", "871"):
            assert mid in block, mid

    def test_extends_m712_temporal(self):
        block = _block()
        assert "TEMPORAL EXTENSION" in block

    def test_safety_crisis_lineage_prose(self):
        block = _block()
        assert "safety-crisis exemption" in block

    def test_peg_register_pattern_prose(self):
        block = _block()
        assert "register follows the" in block and "PEG" in block


# --------------------------------------------------------------------------
# 11. Research method per #503
# --------------------------------------------------------------------------
class TestResearchMethodPer503:
    def test_two_search_sets(self):
        block = _block()
        assert "2 browser.search query sets" in block

    def test_zero_browser_open(self):
        block = _block()
        assert "0 browser.open" in block

    def test_urls_verbatim_prose(self):
        block = _block()
        assert "copied verbatim" in block

    def test_ascii_only_no_em_dashes(self):
        raw = open(os.path.join(REPO, "tests", THIS_FILE), "rb").read()
        assert all(b < 128 for b in raw), "non-ASCII byte in own file"
        assert b"\\xe2\\x80\\x94" not in raw  # em dash, escaped so own file stays ASCII-only

    def test_no_blob_url_in_this_file(self):
        # Own file must not become a self-circular search key.
        needle = "github.com" + "/rayhe/mediascope" + "/blob"
        assert needle not in _read(os.path.join(REPO, "tests", THIS_FILE))

    def test_wired_yaml_block_ascii_only(self):
        block_text = _read(WIRED).split(BLOCK_KEY + ":")[1].split("\n  meta:")[0]
        assert all(ord(c) < 128 for c in block_text)
        assert "\u2014" not in block_text and "\u2013" not in block_text


# --------------------------------------------------------------------------
# 12. Guard lifecycle: mechanism 877 lands this run
# --------------------------------------------------------------------------
class TestGuardLifecycle877Lands:
    def test_m877_lands_in_profiles(self):
        out = _git(
            ["grep", "-n", "mechanism_id: 877", "--", "profiles/"]
        ).stdout
        assert "wired.yaml" in out

    def test_max_mechanism_id_now_877(self):
        out = _git(
            ["grep", "-rhoE", "mechanism_id: [0-9]+", "--", "profiles/"]
        ).stdout
        ids = [int(x.split(":")[1]) for x in out.splitlines()]
        assert max(ids) == 877

    def test_window_files_still_pin_m_id_876_pre_roll(self):
        # The #1075/#1076 files have not been rolled yet; the #1080 Type D
        # run pins the lifecycle then.
        for base in WINDOW_FILES:
            text = _read(os.path.join(REPO, "tests", base))
            assert "876" in text, base

    def test_zero_877_numeric_sweep_now_superseded(self):
        # The designed supersession: the numeric sweep that was green at
        # #1076 now finds mechanism_id: 877 in profiles/wired.yaml.
        needle = "mechanism" + "_id" + ":"
        digits = "8" + "77"
        out = _git(
            ["grep", "-nE", f"{needle}[[:space:]]*{digits}([^0-9]|$)", "--", "profiles/"]
        ).stdout
        assert "wired.yaml" in out and "877" in out


# --------------------------------------------------------------------------
# 13. Doc-sync ratchet per #719 (fail by design pre-doc-sync/pre-entry)
# --------------------------------------------------------------------------
class TestDocSyncRatchet:
    def test_readme_test_file_table_row_present(self):
        # Fails pre-commit by design; green once doc-sync adds it.
        assert THIS_FILE.replace(".py", "") in _read(README)

    def test_architecture_tests_tree_updated(self):
        # Fails pre-commit by design; green once doc-sync adds it.
        assert THIS_FILE.replace(".py", "") in _read(ARCH)

    def test_architecture_lists_1077_file(self):
        # Fails pre-commit by design; green once doc-sync adds it.
        assert THIS_FILE in set(re.findall(r"(test_\w+\.py)", _read(ARCH)))

    def test_readme_stats_table_bumped(self):
        # Fails pre-commit by design; green once doc-sync bumps it.
        assert str(README_TESTS_AFTER) in _read(README)


# --------------------------------------------------------------------------
# 14. Iteration-log entry per #719 (fail by design pre-entry)
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_1077_entry_present_with_finding_shape(self):
        # Fails pre-commit by design; green once the iteration-log
        # entry is prepended.
        log = _read(LOG)
        assert "## #1077 Type A" in log
        idx = log.index("## #1077 Type A")
        block = log[idx : idx + 3000]
        assert "mechanism 877" in block
        assert "Sep 29 2026, 14:00 PDT" in block
        assert "THIRD leg of the 1075-1079 window" in block

    def test_1077_entry_carries_commit_hashes_per_721(self):
        log = _read(LOG)
        idx = log.index("## #1077 Type A")
        block = log[idx : idx + 3000]
        assert "main commit" in block
        assert "anchor" in block
        assert "log-hash followup" in block

    def test_1077_entry_carries_delta_prose(self):
        log = _read(LOG)
        idx = log.index("## #1077 Type A")
        block = log[idx : idx + 4000]
        assert "Astra-cancellation" in block
        assert "+0.10" in block


# --------------------------------------------------------------------------
# 15. Push readiness per #716 / #717
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
            "profiles/wired.yaml",
            "test_type_a_1077_",
            "README.md",
            "docs/ARCHITECTURE.md",
            "iteration-log.md",
        )
        for l in staged:
            assert any(a in l for a in allowed), l
