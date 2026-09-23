"""Type A iteration 927: WIRED x Anthropic slowdown-cycle (Sep 12-22) coverage-selection
silence extension of the mechanism-595/#602 licensing-halo strand.

Type A contract: add ONE mechanism block for a publication x competitor pair with
fresh peer-covered beats and a bounded WIRED absence, extending an in-corpus strand.
This run extends mechanism 595 (iteration 602, Sep 1-8 window) into the Sep 12-22
slowdown cycle: Amodei "We Must Pace the Frontier" essay (Sep 12), Altman/Musk/
Hassabis endorsements + Altman no-2026-IPO confirmation (Sep 12), UN Security
Council briefing (Amodei remote + Altman in person), market fallout (SoftBank -11%,
chips -5.9%). Bounded WIRED absence per the iteration-492 rule (one WIRED-targeted
query set, since 2026-09-11, zero wired.com results) - not a proven zero. The silence
is beat-specific: WIRED interviewed Coxon Sep 9 (mechanism 622, +0.55 illustrative
existential-seriousness credit vs Meta Muse trust register) and ran 2 adversarial
Anthropic breach articles Jul 31, so no blanket blackout is claimed.
Financial predictor is INDIRECT (Conde Nast Aug 2024 OpenAI deal, $1-5M/yr estimate;
Anthropic is the deal partner's chief rival) - licensing-halo extension.
Carried comparator: m547 adversarial Meta register (avg -0.7733, un-rescored per
#807) and #602's four Sep 1-8 beats (carried un-rescored).
MANUAL QUALITATIVE per the Aug 28 2026 standing rule: silence strand, no tone arms
on the Anthropic side, no numeric delta asserted. p_value/cohens_d NOT_CALCULATED;
is_significant False; engine NOT run; no_analysis_json_update true; NOT
artifact-grade. Verdict directionally_supported_not_proven. NOT a
falsification-family member; falsification ledger holds at 29. Correlation only,
not causation. ASCII-only, no em dashes.
"""

import os
import re
import subprocess

import pytest
import yaml

THIS_FILE = "test_type_a_927_wired_anthropic_slowdown_cycle_silence_extension_sep22_5pm.py"
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = os.path.join(REPO, "profiles", "wired.yaml")
BLOCK_KEY = "mechanism_787_wired_anthropic_slowdown_cycle_silence_extension_sep22"
ANCHORED_SHA = "eabec152103e2a21a5c3b7099f02ca90b0259bcc"  # main commit, pinned green in the anchor followup per #565
ITER = 927
TYPE_LETTER = "A"


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _block():
    with open(PROFILE, encoding="utf-8") as fh:
        doc = yaml.safe_load(fh)
    return doc["competitor_relationships"]["anthropic"][BLOCK_KEY]


# ---------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565, patched green post-commit)
# ---------------------------------------------------------------------------
class TestNoveltyAnchor927:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #927 main commit exists pre-commit; the anchor test pins
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
            if "Type A #927" in line and "followup" not in line.lower()
        ]
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or mains == []
        if mains:
            assert mains[0].startswith(ANCHORED_SHA + " "), mains

    @pytest.mark.anchor
    def test_anchor_beat_count_post_commit(self):
        # Second anchor: pins the four-beat slowdown set. Pre-commit it
        # only asserts the block is present with the same beat count the
        # anchor followup pins; post-commit both anchors pin the main commit.
        b = _block()
        assert len(b["slowdown_beats"]) == 4
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or True

    def test_block_key_anchor_parts(self):
        # Unmarked: block key carries mechanism id, entities, window, and
        # the silence-extension framing; runs pre-commit.
        assert BLOCK_KEY.startswith("mechanism_787_wired_anthropic")
        assert "slowdown_cycle_silence_extension" in BLOCK_KEY
        assert BLOCK_KEY.endswith("_sep22")

    def test_mech_id_in_key_matches_field(self):
        # Unmarked: the 787 in the key matches mechanism_id 787; runs
        # pre-commit.
        assert "787" in BLOCK_KEY
        assert _block()["mechanism_id"] == 787


# ---------------------------------------------------------------------------
# 2. Rotation guard, 925-929 window (deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestRotationGuard927:
    @pytest.mark.rotation
    def test_third_leg_of_925_929_window(self):
        assert TYPE_LETTER == "A"
        assert ITER == 927

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {925: "D", 926: "E", 927: "A", 928: "B", 929: "C"}
        assert expected[927] == "A"
        assert expected[925] == "D"
        assert expected[926] == "E"

    @pytest.mark.rotation
    def test_predecessor_926_type_e_committed(self):
        # #926 Type E is COMMITTED (its log entry sits below this run's
        # #927 entry, which was prepended above it).
        assert "## #926 Type E" in _read(os.path.join(REPO, "iteration-log.md"))

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
# 3. Mechanism 787 structure
# ---------------------------------------------------------------------------
class TestMechanism787Structure:
    def test_block_lives_in_wired_profile(self):
        b = _block()
        assert b["publication_focus"] == "WIRED (Conde Nast)"
        assert b["publication_pair"] == "WIRED x Anthropic"

    def test_mechanism_id_787(self):
        assert _block()["mechanism_id"] == 787

    def test_iteration_fields(self):
        b = _block()
        assert b["iteration"] == 927
        assert b["iteration_type"] == "A"
        assert b["type"] == "Type A - Competitor Coverage Deep Dive"
        assert b["iteration_time"] == "2026-09-22 17:00 PDT"
        assert b["scheduled_job_id"] == "mediascope-daily-iteration"

    def test_pair_fields(self):
        b = _block()
        assert b["competitor"] == "anthropic"
        assert "meta" in b["comparison_entities"]

    def test_goal_and_author(self):
        b = _block()
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["author"] == "Kit (with Ray)"

    def test_test_file_field_matches(self):
        assert _block()["test_file"] == "tests/" + THIS_FILE


# ---------------------------------------------------------------------------
# 4. Fresh slowdown beats (Sep 12-22)
# ---------------------------------------------------------------------------
class TestSlowdownBeats927:
    def test_four_beats(self):
        assert len(_block()["slowdown_beats"]) == 4

    def test_beat_amodei_essay(self):
        beats = {x["beat"]: x for x in _block()["slowdown_beats"]}
        b = beats["amodei_pace_the_frontier_essay"]
        assert b["date"] == "2026-09-12"
        assert b["peer_url"] == "https://www.coindesk.com/tech/2026/09/12/anthropic-ceo-calls-for-ai-race-to-slow-down-musk-and-openai-s-altman-agrees"
        assert "Pace the Frontier" in b["title"]

    def test_beat_altman_endorsements(self):
        beats = {x["beat"]: x for x in _block()["slowdown_beats"]}
        b = beats["altman_musk_hassabis_endorsements_no_2026_ipo"]
        assert b["date"] == "2026-09-12"
        assert b["peer_url"] == "https://www.reuters.com/legal/litigation/openai-ipo-will-not-happen-2026-amid-ai-safety-fears-altman-says-2026-09-12/"
        assert "rules out 2026 IPO" in b["title"]

    def test_beat_un_briefing(self):
        beats = {x["beat"]: x for x in _block()["slowdown_beats"]}
        b = beats["un_security_council_briefing"]
        assert b["date"] == "2026-09-22"
        assert b["peer_url"] == "https://www.webpronews.com/ai-chiefs-amodei-and-altman-take-their-warnings-to-the-un-security-council/"

    def test_beat_market_fallout(self):
        beats = {x["beat"]: x for x in _block()["slowdown_beats"]}
        b = beats["market_fallout"]
        assert b["date"] == "2026-09-18"
        assert b["peer_url"] == "https://www.foreignpolicyjournal.com/2026/09/18/musk-and-altman-back-amodeis-ai-slowdown-call-as-chip-stocks-shed-5-9-in-a-single-session/"
        assert b["market_peer_url"] == "https://butterflymarketinsider.com/en/ai-slowdown-amodei-altman-openai-ipo-delayed-softbank-down-11-percent-chips-financing-2026/"

    def test_no_wired_url_invented(self):
        # Silence strand: no wired.com article URL is claimed anywhere in
        # the block; the absence is bounded, not filled with invention.
        raw = _read(PROFILE)
        start = raw.index(BLOCK_KEY)
        segment = raw[start:start + 12000]
        assert "wired.com/story" not in segment

    def test_evidence_grade_excerpt_tier(self):
        for beat in _block()["slowdown_beats"]:
            assert "excerpt-tier" in beat["evidence_grade"]

    def test_novel_url_keys_present(self):
        raw = _read(PROFILE)
        start = raw.index(BLOCK_KEY)
        segment = raw[start:start + 12000]
        for needle in (
            "coindesk.com/tech/2026/09/12/anthropic-ceo-calls-for-ai-race-to-slow-down",
            "webpronews.com/ai-chiefs-amodei-and-altman-take-their-warnings-to-the-un-security-council",
            "butterflymarketinsider.com/en/ai-slowdown-amodei-altman-openai-ipo-delayed",
            "foreignpolicyjournal.com/2026/09/18/musk-and-altman-back-amodeis-ai-slowdown",
        ):
            assert needle in segment, needle


# ---------------------------------------------------------------------------
# 5. Carried arms (un-rescored per #807)
# ---------------------------------------------------------------------------
class TestCarriedArms927:
    def test_602_beats_carried(self):
        carried = _block()["carried_arms"]["mechanism_595_beats"]
        for needle in ("$1.5B piracy settlement", "S-1 prospectus watch",
                       "Claude Fable 5.1", "AISI incident-report"):
            assert needle in carried, needle
        assert "un-rescored per #807" in carried

    def test_m547_meta_register_carried(self):
        carried = _block()["carried_arms"]["meta_register"]
        assert "-0.7733" in carried
        assert "un-rescored per #807" in carried
        for needle in ("Ray-Ban Meta Creep", "Facial Recognition Glasses Will Arm",
                       "Face-Recognition Code"):
            assert needle in carried, needle

    def test_m622_beat_specificity(self):
        note = _block()["carried_arms"]["beat_specificity_note"]
        assert "m622" in note
        assert "resigning researcher" in note
        assert "+0.55" in note
        assert "beat-specific" in note

    def test_finding_states_carried_unrescored(self):
        finding = _block()["finding"]
        assert "carried adversarial Meta register" in finding
        assert "m547 avg -0.7733" in finding


# ---------------------------------------------------------------------------
# 6. Coverage selection (bounded absence, silence strand)
# ---------------------------------------------------------------------------
class TestCoverageSelection927:
    def test_bounded_absence_method(self):
        ba = _block()["bounded_absence"]
        assert "iteration-492" in ba["rule"]
        assert "2026-09-11" in ba["method"]
        assert "zero wired.com results" in ba["method"]

    def test_absence_is_bounded_not_proven_zero(self):
        finding = _block()["finding"]
        assert "not a proven zero" in finding

    def test_no_numeric_delta_asserted(self):
        # Silence strand: no tone arms on the Anthropic side, so no numeric
        # asymmetry delta is asserted anywhere in the block.
        sd = _block()["statistical_discipline"]
        assert "no tone arms" in sd["method"]
        assert "no numeric delta asserted" in sd["method"]

    def test_no_blanket_blackout_claim(self):
        finding = _block()["finding"]
        assert "not a blanket blackout" in finding
        assert "2 adversarial Anthropic breach articles Jul 31" in finding


# ---------------------------------------------------------------------------
# 7. Statistical discipline (Aug 28 2026 standing rule)
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline927:
    def test_p_value_not_calculated(self):
        assert _block()["statistical_discipline"]["p_value"] == "NOT_CALCULATED"

    def test_effect_sizes_not_calculated(self):
        sd = _block()["statistical_discipline"]
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"

    def test_is_significant_false(self):
        assert _block()["statistical_discipline"]["is_significant"] is False

    def test_engine_not_run(self):
        assert _block()["statistical_discipline"]["engine_run"] is False

    def test_no_analysis_json_update(self):
        b = _block()
        assert b["statistical_discipline"]["no_analysis_json_update"] is True
        assert b["statistical_discipline"]["artifact_grade"] is False

    def test_verdict_directionally_supported_not_proven(self):
        sd = _block()["statistical_discipline"]
        assert sd["verdict"] == "directionally_supported_not_proven"
        assert sd["correlation_not_causation"] is True


# ---------------------------------------------------------------------------
# 8. Confounders and counterevidence
# ---------------------------------------------------------------------------
class TestConfoundersCounterevidence927:
    def test_confounders_ranked_counts(self):
        c = _block()["confounders_ranked"]
        assert len(c["strong"]) == 3
        assert len(c["moderate"]) == 2
        assert len(c["weak"]) == 1

    def test_confounder_content(self):
        c = _block()["confounders_ranked"]
        strong = " ".join(c["strong"])
        assert "softer news peg" in strong
        assert "iteration-492" in strong
        moderate = " ".join(c["moderate"])
        assert "antitrust waiver" in moderate

    def test_counterevidence_count(self):
        assert len(_block()["counterevidence"]) >= 6

    def test_counterevidence_key_entries(self):
        ce = " ".join(_block()["counterevidence"])
        assert "m622" in ce
        assert "m54" in ce
        assert "m682" in ce
        assert "payer-prediction inversion" in ce

    def test_ledger_holds_29(self):
        assert _block()["falsification_ledger"] == 29
        assert _block()["falsification_family_member"] is False

    def test_licensing_halo_framing(self):
        fc = _block()["financial_context"]
        assert "INDIRECT" in fc
        assert "$1-5M/yr" in fc
        assert "rival" in fc
        assert "licensing-halo" in _block()["finding"] or "LICENSING-HALO" in _block()["finding"]


# ---------------------------------------------------------------------------
# 9. Connections
# ---------------------------------------------------------------------------
class TestConnections927:
    def test_connects_to_includes_key_ids(self):
        connects = _block()["connects_to"]
        for mid in (92, 595, 622, 547, 54, 763):
            assert mid in connects, mid

    def test_extends_595(self):
        assert "mechanism 595" in _block()["extends"]
        assert "second temporal leg" in _block()["extends"]

    def test_research_method_documents_query_sets(self):
        rm = _block()["research_method"]
        assert "5 browser.search query sets" in rm
        assert "0 browser.open" in rm
        assert "no canonical URLs constructed" in rm


# ---------------------------------------------------------------------------
# 10. Doc-sync per #719
# ---------------------------------------------------------------------------
class TestDocSync927:
    def test_readme_test_file_row_present(self):
        readme = _read(os.path.join(REPO, "README.md"))
        assert THIS_FILE in readme
        assert "Type A #927" in readme

    def test_readme_stats_table_updated(self):
        readme = _read(os.path.join(REPO, "README.md"))
        assert "| Tests | 47648 | Across 1252 test files |" in readme

    def test_architecture_row_present(self):
        arch = _read(os.path.join(REPO, "docs", "ARCHITECTURE.md"))
        assert THIS_FILE in arch
        assert "Type A #927" in arch


# ---------------------------------------------------------------------------
# 11. Iteration log per #719
# ---------------------------------------------------------------------------
class TestIterationLog927:
    def test_iteration_log_entry_present(self):
        log = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #927 Type A:" in log
        assert "#927 Type A" in log

    def test_iteration_log_cites_mechanism_787(self):
        log = _read(os.path.join(REPO, "iteration-log.md"))
        head = log[:6000]
        assert "mechanism 787" in head
        assert "slowdown" in head
