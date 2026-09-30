"""Type A #1082: The Verge x OpenAI Aug-7-to-Sep-6-2026 four-piece Astra-safety
arc on the Vox-deal partner vs carried Verge x Meta arms (mechanism 880) -
FIRST dedicated Type A mechanism on The Verge's sustained Astra-safety arc:
A1 Aug 7 "OpenAI puts the brakes on a new model because it's supposedly
too powerful" (skeptical pause reportage, -0.30), A2 Sep 2 "Researchers fear
safety disaster ahead of OpenAI's Astra release" (adversarial safety-alarm,
"may be the single worst development for AI security/safety to date",
-0.55), A3 Sep 4 "OpenAI ships GPT-6 Astra, its first model to hit internal
security threshold" (factual launch relay, +0.10), A4 Sep 4 "Sam Altman
apologizes for 'messy' GPT-6 Astra rollout that's locked out paying users"
(execution-adversarial, -0.25). Arc mean -0.25. Meta arms carried un-rescored
per #807: #592 same-outlet Meta glasses set (mean -0.55) and m811 Verge Meta
Connect Audio privacy-positive (+0.10). Illustrative deltas (OpenAI arc minus
Meta): +0.30 primary (thesis-consistent), -0.35 secondary. The falsification
is register-AVAILABILITY, not mean-tone: the Vox Media x OpenAI May 29 2024
licensing deal (coverage_prediction 'softer') does not suppress the
adversarial safety register on the deal partner across a seven-week arc.
THIRTY-SEVENTH falsification-family member (ledger 36->37); EXTENDS the
m598/m853 single-piece safety-crisis falsifications into a sustained-arc
falsification; BOUNDED by m425 (+0.46 thesis-consistent) and m507.

Third leg of the 1080-1084 window: D (#1080) -> E (#1081) -> A (#1082).
MANUAL ILLUSTRATIVE ONLY per the Aug 28 2026 standing rule: tones
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
VERGE = os.path.join(REPO, "profiles", "the-verge.yaml")
LOG = os.path.join(REPO, "iteration-log.md")
README = os.path.join(REPO, "README.md")
ARCH = os.path.join(REPO, "docs", "ARCHITECTURE.md")
THIS_FILE = os.path.basename(__file__)

ITERATION = 1082
TYPE_LETTER = "A"
RUN_PDT = "2026-09-29 19:00 PDT"
BLOCK_KEY = "verge_openai_aug_sep2026_astra_safety_arc_adversarial_register_vs_carried_meta_arms"
ANCHORED_SHA = "PATCH_ME_IN_ANCHOR_FOLLOWUP"

README_TESTS_AFTER = 55646
README_FILES_AFTER = 1407

# Evidence URLs verbatim from the browser.search Full-URL listings.
EVIDENCE_URLS = [
    "https://www.theverge.com/ai-artificial-intelligence/976948/openai-astra-model-pause-critical-cyber-capabilities",
    "https://www.theverge.com/ai-artificial-intelligence/988334/openai-astra-ai-monitoring-safety",
    "https://www.theverge.com/ai-artificial-intelligence/989601/openai-gpt-6-astra-release",
    "https://www.theverge.com/ai-artificial-intelligence/990060/altman-apologizes-messy-astra-rollout",
]

# The 1080-1084 window's prior legs carry their zero-880 forward-looking
# guards; mechanism 880 lands THIS run and supersedes the numeric sweeps by
# design per the #710/#720 convention.
WINDOW_FILES = [
    "test_type_d_1080_m877_m878_m879_qualitative_corpus_integrity_sep29_5pm.py",
    "test_type_e_1081_podcast_sentiment_139th_verification_sep29_6pm.py",
]


def _git(args):
    return subprocess.run(
        ["git", "-C", REPO] + args, capture_output=True, text=True, timeout=120
    )


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _block():
    return _read(VERGE).split(BLOCK_KEY + ":")[1].split("\n  meta:")[0]


# --------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565, patched green post-commit)
# --------------------------------------------------------------------------
class TestNoveltyAnchorTypeA1082:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #1082 main commit exists pre-commit; the anchor test pins
        # the main commit SHA once the followup patches ANCHORED_SHA.
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
            if "Type A #1082" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "PATCH_ME_IN_ANCHOR_FOLLOWUP",
            "placeholder",
        )
        assert any(ANCHORED_SHA[:12] in line for line in mains)

    @pytest.mark.anchor
    def test_anchor_sha_is_full_40_hex(self):
        assert re.fullmatch(r"[0-9a-f]{40}", ANCHORED_SHA)

    @pytest.mark.anchor
    def test_block_key_present_post_commit(self):
        assert BLOCK_KEY in _read(VERGE)


# --------------------------------------------------------------------------
# 2. Rotation guard: 1080-1084 window THIRD leg
# --------------------------------------------------------------------------
class TestRotationGuard1080_1084Window:
    @pytest.mark.rotation
    def test_window_opening_and_second_leg_in_git_history(self):
        log = _git(["log", "--oneline"]).stdout
        assert "Type D #1080" in log
        assert "Type E #1081" in log

    @pytest.mark.rotation
    def test_rotation_rule_d_e_a_sequence(self):
        # The committed window files pin the rotation order D -> E -> A
        # per the #565 anchor + rotation guard.
        assert TYPE_LETTER == "A"
        assert ITERATION == 1082

    def test_this_run_continues_window(self):
        assert "1080-1084 window THIRD leg" in _block()


# --------------------------------------------------------------------------
# 3. Corpus novelty greps per #715 (committed novelty state)
# --------------------------------------------------------------------------
class TestCorpusNoveltyGreps:
    def test_block_key_unique_in_verge_yaml(self):
        # The 4-space-indented block key line occurs exactly once; the
        # test_file field value carries the key as a substring and is
        # excluded by the key-line form.
        assert _read(VERGE).count("\n    " + BLOCK_KEY + ":") == 1

    def test_mechanism_id_880_colon_form_present(self):
        assert "mechanism_id: 880" in _block()

    def test_no_underscore_dash_880_key_strings(self):
        # Keying discipline per #715: the block key carries no numeric
        # 880 mechanism-id substring. No repo-wide literal carrier of the
        # contiguous fragment-built 880 key needle forms (u-score and
        # dash) exists in tests/ or profiles/; no new carrier may appear
        # this run. iteration-log.md prose mentions of the needle forms
        # (the #1081 entry's own research-method description) are outside
        # the source sweep by design.
        n1 = "mech" + "anism_" + "8" + "80"
        n2 = "mech" + "anism-" + "8" + "80"
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
        assert "880" not in BLOCK_KEY


# --------------------------------------------------------------------------
# 4. OpenAI arc evidence (digest-attested per #503)
# --------------------------------------------------------------------------
class TestOpenAIArcEvidence:
    def test_all_evidence_urls_in_source_urls(self):
        block = _block()
        for url in EVIDENCE_URLS:
            assert url in block, url

    def test_four_arms_listed(self):
        block = _block()
        assert block.count("evidence_tier: \"excerpt-tier digest-attested\"") == 4

    def test_scare_quotes_headline_attested(self):
        assert "supposedly too powerful" in _block()

    def test_safety_disaster_line_attested(self):
        assert "single worst development for AI security/safety to date" in _block()

    def test_launch_relay_arm_attested(self):
        assert "first model to hit internal security threshold" in _block()

    def test_messy_rollout_arm_attested(self):
        assert "messy" in _block() and "locked out paying users" in _block()

    def test_excerpt_tier_disclosed(self):
        block = _block()
        assert "excerpt-tier" in block
        assert "digest-attested" in block

    def test_arc_dates_aug_to_sep(self):
        block = _block()
        assert "2026-08-07" in block
        assert "2026-09-02" in block
        assert "2026-09-04" in block


# --------------------------------------------------------------------------
# 5. Meta arms carried un-rescored per #807
# --------------------------------------------------------------------------
class TestMetaArmsCarriedPer807:
    def test_592_band_arms_listed(self):
        block = _block()
        assert "pervert glasses" in block
        assert "mass surveillance predator glasses" in block

    def test_carried_tones_preserved(self):
        block = _block()
        assert "manual_illustrative_tone: -0.55" in block
        assert "manual_illustrative_tone: -0.60" in block
        assert "manual_illustrative_tone: -0.50" in block
        assert "meta_band_mean: -0.55" in block

    def test_m811_secondary_arm(self):
        block = _block()
        assert "mechanism 811" in block
        assert "do not record" in block

    def test_no_rescoring_disclosure(self):
        block = _block()
        assert "per #807" in block and "un-rescored" in block


# --------------------------------------------------------------------------
# 6. Illustrative tones and delta arithmetic
# --------------------------------------------------------------------------
class TestIllustrativeTonesAndDelta:
    def test_arc_arm_tones(self):
        block = _block()
        assert "manual_illustrative_tone: -0.30" in block
        assert "manual_illustrative_tone: -0.55" in block
        assert "manual_illustrative_tone: 0.10" in block
        assert "manual_illustrative_tone: -0.25" in block

    def test_arc_mean_arithmetic(self):
        assert abs(((-0.30 + -0.55 + 0.10 + -0.25) / 4) - (-0.25)) < 1e-9
        assert "openai_arc_mean: -0.25" in _block()

    def test_manual_illustrative_label_only(self):
        assert "MANUAL ILLUSTRATIVE" in _block()

    def test_delta_arithmetic_primary(self):
        # delta (OpenAI arc minus Meta primary) = -0.25 - (-0.55) = +0.30
        assert abs((-0.25 - (-0.55)) - 0.30) < 1e-9
        assert "illustrative_delta_openai_minus_meta_primary: 0.30" in _block()

    def test_delta_arithmetic_secondary(self):
        # delta (OpenAI arc minus Meta secondary) = -0.25 - 0.10 = -0.35
        assert abs((-0.25 - 0.10) - (-0.35)) < 1e-9
        assert "illustrative_delta_openai_minus_meta_secondary: -0.35" in _block()

    def test_register_availability_not_mean_tone(self):
        block = _block()
        assert "register-AVAILABILITY" in block
        assert "not mean-tone" in block


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
    def test_thirty_seventh_member(self):
        assert "falsification_family_member: true" in _block()
        assert "THIRTY-SEVENTH falsification-family member (ledger 36->37)" in _block()

    def test_ledger_now_37(self):
        assert "falsification_ledger: 37" in _block()

    def test_ledger_prose(self):
        block = _block()
        assert "Ledger holds at 37" in block

    def test_thirty_eighth_absent_except_own_block_prose(self):
        # No committed 38th falsification-family member exists; the only
        # THIRTY-EIGHTH mention in profiles/ is my own block's ledger
        # prose ("THIRTY-EIGHTH absent").
        out = _git(["grep", "-n", "THIRTY-EIGHTH", "--", "profiles/"]).stdout
        lines = [l for l in out.strip().splitlines() if l.strip()]
        assert lines, "expected own-block ledger prose"
        assert all("the-verge.yaml" in l for l in lines), lines


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

    def test_event_driven_register_confounder(self):
        block = _block()
        assert "STRONG: event-driven register" in block

    def test_temporal_skew_confounder(self):
        block = _block()
        assert "temporal skew" in block

    def test_mirror_attribution_weak_confounder(self):
        block = _block()
        assert "WEAK: mirror-attribution" in block


# --------------------------------------------------------------------------
# 10. Cross-references
# --------------------------------------------------------------------------
class TestCrossReferences:
    def test_connects_to_ids(self):
        block = _block()
        for mid in ("598", "853", "867", "811", "827", "425", "507"):
            assert mid in block, mid

    def test_extends_m598_m853_arc(self):
        block = _block()
        assert "EXTENDS the m598/m853" in block

    def test_bounded_by_m425_m507(self):
        block = _block()
        assert "BOUNDED by m425" in block
        assert "m507" in block

    def test_vox_deal_prediction_named(self):
        block = _block()
        assert "May 29 2024" in block
        assert "coverage_prediction" in block


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

    def test_bounded_absence_disclosed(self):
        block = _block()
        assert "bounded absence" in block

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

    def test_verge_yaml_block_ascii_only(self):
        block_text = _block()
        assert all(ord(c) < 128 for c in block_text)
        assert "\u2014" not in block_text and "\u2013" not in block_text


# --------------------------------------------------------------------------
# 12. Guard lifecycle: mechanism 880 lands this run
# --------------------------------------------------------------------------
class TestGuardLifecycle880Lands:
    def test_m880_lands_in_profiles(self):
        out = _git(
            ["grep", "-n", "mechanism_id: 880", "--", "profiles/"]
        ).stdout
        assert "the-verge.yaml" in out

    def test_max_mechanism_id_now_880(self):
        out = _git(
            ["grep", "-rhoE", "mechanism_id: [0-9]+", "--", "profiles/"]
        ).stdout
        ids = [int(x.split(":")[1]) for x in out.splitlines()]
        assert max(ids) == 880

    def test_zero_880_numeric_sweep_now_superseded(self):
        # The designed supersession per #710/#720: the numeric sweep that
        # was green at #1080/#1081 now finds mechanism_id: 880 in
        # profiles/the-verge.yaml.
        needle = "mechanism" + "_id" + ":"
        digits = "8" + "80"
        out = _git(
            ["grep", "-nE", f"{needle}[[:space:]]*{digits}([^0-9]|$)", "--", "profiles/"]
        ).stdout
        assert "the-verge.yaml" in out and "880" in out

    def test_window_files_still_pin_879_pre_roll(self):
        # The #1080/#1081 files have not been rolled yet; the #1085 Type D
        # run pins the lifecycle then.
        for base in WINDOW_FILES:
            text = _read(os.path.join(REPO, "tests", base))
            assert "879" in text, base


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

    def test_architecture_lists_1082_file(self):
        # Fails pre-commit by design; green once doc-sync adds it.
        assert THIS_FILE in set(re.findall(r"(test_\w+\.py)", _read(ARCH)))

    def test_readme_stats_table_bumped(self):
        # Fails pre-commit by design; green once doc-sync bumps it.
        assert str(README_TESTS_AFTER) in _read(README)


# --------------------------------------------------------------------------
# 14. Iteration-log entry per #719 (fail by design pre-entry)
# --------------------------------------------------------------------------
class TestIterationLogEntry:
    def test_1082_entry_present_with_finding_shape(self):
        # Fails pre-commit by design; green once the iteration-log
        # entry is prepended.
        log = _read(LOG)
        assert "## #1082 Type A" in log
        idx = log.index("## #1082 Type A")
        block = log[idx : idx + 3000]
        assert "mechanism 880" in block
        assert "Sep 29 2026, 19:00 PDT" in block
        assert "THIRD leg of the 1080-1084 window" in block

    def test_1082_entry_carries_commit_hashes_per_721(self):
        log = _read(LOG)
        idx = log.index("## #1082 Type A")
        block = log[idx : idx + 3000]
        assert "main commit" in block
        assert "anchor" in block
        assert "log-hash followup" in block

    def test_1082_entry_carries_delta_prose(self):
        log = _read(LOG)
        idx = log.index("## #1082 Type A")
        block = log[idx : idx + 4000]
        assert "Astra-safety arc" in block
        assert "+0.30" in block
        assert "-0.35" in block


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
            "profiles/the-verge.yaml",
            "test_type_a_1082_",
            "README.md",
            "docs/ARCHITECTURE.md",
            "iteration-log.md",
        )
        for l in staged:
            assert any(a in l for a in allowed), l
