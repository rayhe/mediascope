"""Type A #1072: Guardian x OpenAI Sep-28-2026 Astra-cancellation safety-crisis
register vs carried Guardian x Meta arms (mechanism 874) - FIRST dedicated
Type A mechanism on the Guardian's own Sep-28 Astra-cancellation coverage of
the Feb-2025 licensing deal partner (relay-attested per #503; theguardian.com
timestamp 2026-09-28 23:02:28 via the biztoc relay): 'OpenAI scraps release
of new model over safety concerns in internal testing'. OpenAI arm NEW this
run (excerpt-tier): safety-crisis accountability register on the PAYER -
GPT-6.1 Astra shelved over deception, scope-authorization overstep, unsafe
tool use; Jain 'didn't quite meet the bar'; AISI unsanctioned-attack
findings; DevDay eve. MANUAL ILLUSTRATIVE -0.35 (peg-consistent with m871's
BI safety-scoop -0.35 and m862's Guardian AP-wire -0.35). Meta arm carried
from mechanism 687 (un-rescored per #807): police-warnings documents
investigation -0.55, teen-accounts accountability -0.45; mean -0.50.
Illustrative delta (OpenAI minus Meta) +0.15: both arms hard, payer 0.15
softer - NOT a falsification-family member (ledger holds at 35). This is the
safety-crisis exemption extension: on safety-crisis pegs the licensing deal
does not suppress adversarial coverage - TEMPORAL REPLICATION of m871 (BI
Sep-28/29 Astra scoop, delta -0.38) and EXTENSION of m862 (Guardian Sep-26
AP-wire -0.35); joins the m856/m853/m598 safety-crisis lineage; register
follows the PEG not the entity (m842/m736 pattern).

Third leg of the 1070-1074 window: D (#1070) -> E (#1071) -> A (#1072).
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
GUARDIAN = os.path.join(REPO, "profiles", "guardian.yaml")
LOG = os.path.join(REPO, "iteration-log.md")
README = os.path.join(REPO, "README.md")
ARCH = os.path.join(REPO, "docs", "ARCHITECTURE.md")
THIS_FILE = os.path.basename(__file__)

ITERATION = 1072
TYPE_LETTER = "A"
RUN_PDT = "2026-09-29 09:00 PDT"
BLOCK_KEY = "guardian_openai_sep28_astra_cancellation_safety_crisis_register_vs_carried_meta_arms"
ANCHORED_SHA = "ANCHORED_SHA_PENDING"

README_TESTS_AFTER = 55049
README_FILES_AFTER = 1397

# Evidence URLs verbatim from the browser.search Full-URL listings.
EVIDENCE_URLS = [
    "https://biztoc.com/x/598c731c4e7ef874",
    "https://dailyaibrief.com/news/openai-scraps-gpt-6-1-astra-release-safety-concerns-emym5xfF",
    "https://www.resultsense.com/news/2026-09-29-openai-scraps-gpt-6-1-astra-release/",
    "https://10news.org/2026/09/openai-cancels-release-of-new-ai-model-due-to-safety-issues/",
    "https://www.wsj.com/tech/ai/openai-chatgpt-model-release-cancel-safety-5a2f9f42",
]

# The 1070-1074 window's prior legs carry their zero-874 forward-looking
# guards (needles format-built per #715); mechanism 874 lands THIS run and
# supersedes the numeric sweeps by design per the #710/#720 convention.
WINDOW_FILES = [
    "test_type_d_1070_m871_m872_m873_qualitative_corpus_integrity_sep29_7am.py",
    "test_type_e_1071_podcast_sentiment_137th_verification_sep29_8am.py",
]


def _git(args):
    return subprocess.run(
        ["git", "-C", REPO] + args, capture_output=True, text=True, timeout=120
    )


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _block():
    return _read(GUARDIAN).split(BLOCK_KEY + ":")[1]


# --------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565, patched green post-commit)
# --------------------------------------------------------------------------
class TestNoveltyAnchorTypeA1072:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #1072 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA)

    @pytest.mark.anchor
    def test_block_key_present_post_commit(self):
        assert BLOCK_KEY in _read(GUARDIAN)

    @pytest.mark.anchor
    def test_type_a_1072_in_git_log(self):
        out = _git(["log", "--oneline", "--grep=Type A #1072"]).stdout
        assert "Type A #1072" in out


# --------------------------------------------------------------------------
# 2. Rotation guard: 1070-1074 window THIRD leg
# --------------------------------------------------------------------------
class TestRotationGuard1070_1074Window:
    def test_window_opening_and_second_leg_in_git_history(self):
        log = _git(["log", "--oneline"]).stdout
        assert "Type D #1070" in log
        assert "Type E #1071" in log

    def test_rotation_rule_d_e_a_sequence(self):
        # The committed window files pin the rotation order D -> E -> A
        # per the #565 anchor + rotation guard.
        log = _git(["log", "--oneline", "--grep=1070-1074 window"]).stdout
        assert "1070" in log and "1071" in log

    def test_this_run_continues_window(self):
        assert TYPE_LETTER == "A"
        assert ITERATION == 1072


# --------------------------------------------------------------------------
# 3. Corpus novelty greps per #715 (committed novelty state)
# --------------------------------------------------------------------------
class TestCorpusNoveltyGreps:
    def test_block_key_unique_in_guardian_yaml(self):
        # The 4-space-indented block key line occurs exactly once; the
        # test_file field value carries the key as a substring and is
        # excluded by the key-line form.
        assert _read(GUARDIAN).count("\n    " + BLOCK_KEY + ":") == 1

    def test_mechanism_id_874_colon_form_present(self):
        assert "mechanism_id: 874" in _block()

    def test_no_underscore_dash_874_key_strings(self):
        # Keying discipline per #715: the block key carries no numeric
        # 874 mechanism-id substring. The only repo-wide literal carrier
        # of the contiguous mechanism_874 / mechanism-874 needle forms is
        # the #1071 file's guard-needle comment (documented, pre-existing);
        # no new carrier may appear this run.
        n1 = "mech" + "anism_" + "8" + "74"
        n2 = "mech" + "anism-" + "8" + "74"
        hits = set(
            _git(["grep", "-l", "-e", n1, "-e", n2, "--", "."]).stdout.splitlines()
        )
        assert hits == {
            "tests/test_type_e_1071_podcast_sentiment_137th_verification_sep29_8am.py"
        }, hits

    def test_block_key_carries_no_numeric_id(self):
        assert "874" not in BLOCK_KEY


# --------------------------------------------------------------------------
# 4. OpenAI arm evidence (relay-attested per #503)
# --------------------------------------------------------------------------
class TestOpenAIArmEvidence:
    def test_all_evidence_urls_in_source_urls(self):
        block = _block()
        for url in EVIDENCE_URLS:
            assert url in block, url

    def test_biztoc_guardian_timestamp_attestation(self):
        assert "2026-09-28 23:02:28" in _block()

    def test_resultsense_deception_attribution(self):
        block = _block()
        assert "more deceptive than the version before it" in block

    def test_excerpt_tier_disclosed(self):
        block = _block()
        assert "excerpt-tier" in block
        assert "relay-attested" in block

    def test_wsi_scoop_origin_context(self):
        # WSJ first broke the story; carried as scoop-origin context,
        # not Guardian evidence.
        block = _block()
        assert "WSJ" in block or "wsj.com" in block


# --------------------------------------------------------------------------
# 5. Meta arm carried un-rescored per #807
# --------------------------------------------------------------------------
class TestMetaArmCarriedPer807:
    def test_two_m687_arms_listed(self):
        block = _block()
        assert "police-warnings" in block
        assert "teen-accounts" in block

    def test_carried_tones_preserved(self):
        block = _block()
        assert "-0.55" in block
        assert "-0.45" in block

    def test_meta_mean_negative_point_five(self):
        block = _block()
        assert "meta_mean: -0.5" in block

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
        assert "MANUAL ILLUSTRATIVE ONLY" in block or "MANUAL ILLUSTRATIVE" in block

    def test_delta_arithmetic(self):
        # delta (OpenAI minus Meta) = -0.35 - (-0.50) = +0.15
        assert abs((-0.35 - (-0.50)) - 0.15) < 1e-9
        assert "illustrative_delta_openai_minus_meta: 0.15" in _block()

    def test_delta_direction_prose(self):
        block = _block()
        assert "0.15 softer" in block


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
    def test_two_strong_confounders(self):
        block = _block()
        strong = [l for l in block.splitlines() if "STRONG:" in l]
        assert len(strong) >= 2

    def test_excerpt_tier_strongest_confounder(self):
        block = _block()
        assert "STRONG: excerpt-tier" in block

    def test_news_peg_crisis_confounder(self):
        block = _block()
        assert "news-peg crisis" in block

    def test_incentive_attribution_inconclusive(self):
        block = _block()
        assert "INCONCLUSIVE" in block

    def test_no_disclosure_bounded_prose(self):
        block = _block()
        assert "bounded by excerpt completeness" in block


# --------------------------------------------------------------------------
# 10. Cross-references
# --------------------------------------------------------------------------
class TestCrossReferences:
    def test_connects_to_ids(self):
        block = _block()
        for mid in ("871", "687", "760", "862"):
            assert mid in block, mid

    def test_extends_m871_temporal_replication(self):
        block = _block()
        assert "TEMPORAL REPLICATION" in block or "temporal replication" in block

    def test_peg_register_pattern_prose(self):
        block = _block()
        assert "register follows the" in block and "PEG" in block


# --------------------------------------------------------------------------
# 11. Research method per #503
# --------------------------------------------------------------------------
class TestResearchMethodPer503:
    def test_four_search_sets(self):
        block = _block()
        assert "4 browser.search query sets" in block

    def test_zero_browser_open(self):
        block = _block()
        assert "0 browser.open" in block

    def test_urls_verbatim_prose(self):
        block = _block()
        assert "copied verbatim" in block

    def test_ascii_only_no_em_dashes(self):
        raw = open(os.path.join(REPO, "tests", THIS_FILE), "rb").read()
        assert all(b < 128 for b in raw), "non-ASCII byte in own file"
        assert b"\xe2\x80\x94" not in raw  # em dash, escaped so own file stays ASCII-only

    def test_no_blob_url_in_this_file(self):
        # Own file must not become a self-circular search key.
        needle = "github.com" + "/rayhe/mediascope" + "/blob"
        assert needle not in _read(os.path.join(REPO, "tests", THIS_FILE))

    def test_guardian_yaml_block_ascii_only(self):
        block_raw = _read(GUARDIAN).encode("utf-8")
        block_text = _read(GUARDIAN).split(BLOCK_KEY + ":")[1].split("\n  meta:")[0]
        assert all(ord(c) < 128 for c in block_text)
        assert "\u2014" not in block_text and "\u2013" not in block_text


# --------------------------------------------------------------------------
# 12. Guard lifecycle: mechanism 874 lands this run
# --------------------------------------------------------------------------
class TestGuardLifecycle874Lands:
    def test_mechanism_874_lands_in_profiles(self):
        out = _git(
            ["grep", "-n", "mechanism_id: 874", "--", "profiles/"]
        ).stdout
        assert "guardian.yaml" in out

    def test_max_mechanism_id_now_874(self):
        out = _git(
            ["grep", "-rhoE", "mechanism_id: [0-9]+", "--", "profiles/"]
        ).stdout
        ids = [int(x.split(":")[1]) for x in out.splitlines()]
        assert max(ids) == 874

    def test_window_files_still_pin_m_id_873_pre_roll(self):
        # The #1067/#1068/#1069 (and #1070/#1071) files have not been
        # rolled yet; the #1075 Type D run pins the lifecycle then.
        for base in WINDOW_FILES:
            text = _read(os.path.join(REPO, "tests", base))
            assert "873" in text, base

    def test_zero_874_numeric_sweep_now_superseded(self):
        # The designed supersession: the numeric sweep that was green at
        # #1071 now finds mechanism_id: 874 in profiles/guardian.yaml.
        needle = "mechanism" + "_id" + ":"
        digits = "8" + "74"
        out = _git(
            ["grep", "-nE", f"{needle}[[:space:]]*{digits}([^0-9]|$)", "--", "profiles/"]
        ).stdout
        assert "guardian.yaml" in out and "874" in out


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

    def test_architecture_lists_1072_file(self):
        # Fails pre-commit by design; green once doc-sync adds it.
        assert THIS_FILE in set(re.findall(r"(test_\w+\.py)", _read(ARCH)))

    def test_readme_stats_table_bumped(self):
        # Fails pre-commit by design; green once doc-sync bumps it.
        assert str(README_TESTS_AFTER) in _read(README)


# --------------------------------------------------------------------------
# 14. Iteration-log entry per #719 (fail by design pre-entry)
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_1072_entry_present_with_finding_shape(self):
        # Fails pre-commit by design; green once the iteration-log
        # entry is prepended.
        log = _read(LOG)
        assert "## #1072 Type A" in log
        idx = log.index("## #1072 Type A")
        block = log[idx : idx + 3000]
        assert "mechanism 874" in block
        assert "Sep 29 2026, 09:00 PDT" in block
        assert "THIRD leg of the 1070-1074 window" in block

    def test_1072_entry_carries_commit_hashes_per_721(self):
        log = _read(LOG)
        idx = log.index("## #1072 Type A")
        block = log[idx : idx + 3000]
        assert "main commit" in block
        assert "anchor" in block
        assert "log-hash followup" in block

    def test_1072_entry_carries_delta_prose(self):
        log = _read(LOG)
        idx = log.index("## #1072 Type A")
        block = log[idx : idx + 4000]
        assert "Astra-cancellation" in block
        assert "+0.15" in block


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
            "profiles/guardian.yaml",
            "test_type_a_1072_",
            "README.md",
            "docs/ARCHITECTURE.md",
            "iteration-log.md",
        )
        for l in staged:
            assert any(a in l for a in allowed), l
