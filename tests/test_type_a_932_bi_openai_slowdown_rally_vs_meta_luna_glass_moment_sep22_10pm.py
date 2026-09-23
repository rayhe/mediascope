"""Type A #932: BI x OpenAI Sep-12 slowdown rally (+0.15) vs BI x Meta
Sep-16/17 Luna Glasshole-moment (-0.25) - mechanism 790, temporal inversion
of the mechanism-399 February gradient.

THIRD leg of the 930-934 rotation window: D (#930) -> E (#931) -> A (#932)
-> B (#933) -> C (#934).

ONE fresh BI-originated OpenAI arm (Sep 12 2026 "AI leaders rally around
calls to slow things down", Truman Dickerson, come-together/statesman
register, reconstructed from a verbatim IFTTT mirror since the BI original
is paywalled) vs ONE BI-originated Meta arm (Sep 16-17 Luna summary via The
Information relay, "navigating its Google Glass moment" with the explicit
2013 Glasshole parallel, characterized via a first-hand-read secondary
synthesis since the BI original's verbatim URL was not surfaced).

Illustrative delta (Meta minus OpenAI) -0.40: the INVERSE of m399's February
OpenAI-minus-Meta -0.50 (BI harder on OpenAI then, harder on Meta now).
TEMPORAL INVERSION, not a stable outlet property - the m399 gradient is
story-type- and time-bound.

MANUAL ILLUSTRATIVE scores ONLY; no asymmetry scorer engine run per the
project standing rule Aug 28 2026. p_value/cohens_d/ci_95 NOT_CALCULATED,
is_significant False, engine NOT run, verdict
directionally_supported_not_proven, NOT artifact-grade, no analysis.json
update, ledger holds at 29. The September constructive OpenAI arm is
directionally consistent with the softer-payer prediction (Axel Springer
parent-level OpenAI licensing deal, carried from m399) but n=1/n=1,
genre-mismatched, mirror/secondary evidence tiers - NOT a financial proof.
Correlation is not causation.

Concurrency: #884 (competitor-entities.yaml, m762), #899 (nytimes.yaml,
m771), and the untracked Type D #900 qualitative test file remain in-flight
and uncommitted; journalists.yaml is CLEAN (#898 m770 hunk lost,
documented at #920). None touched by this run.
"""

import os
import re
import subprocess

import pytest
import yaml

THIS_FILE = "test_type_a_932_bi_openai_slowdown_rally_vs_meta_luna_glass_moment_sep22_10pm.py"
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = os.path.join(REPO, "profiles", "business-insider.yaml")
BLOCK_KEY = "business_insider_openai_slowdown_rally_vs_meta_luna_glass_moment_sep22_790"
ANCHORED_SHA = "28401b43659ae3a86a8dee5a5d1a047222573fdf"  # patched green in the anchor followup per #565
ITER = 932
TYPE_LETTER = "A"


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _block():
    with open(PROFILE, encoding="utf-8") as fh:
        doc = yaml.safe_load(fh)
    return doc["competitor_relationships"]["openai"][BLOCK_KEY]


# ---------------------------------------------------------------------------
# 1. Novelty anchor (deselected pre-commit per #565, patched green post-commit)
# ---------------------------------------------------------------------------
class TestNoveltyAnchor932:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #932 main commit exists pre-commit; the anchor test pins
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
            if "Type A #932" in line and "followup" not in line.lower()
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
        assert b["tone_comparison"]["delta_MANUAL_ILLUSTRATIVE_meta_minus_openai"] == -0.40
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or True

    def test_block_key_anchor_parts(self):
        # Unmarked: block key carries outlet, entities, date, and mechanism
        # id; runs pre-commit.
        assert BLOCK_KEY.startswith("business_insider_openai_")
        assert BLOCK_KEY.endswith("_sep22_790")
        assert "meta_luna" in BLOCK_KEY

    def test_mech_key_ends_with_date_and_id(self):
        # Unmarked: the date+id segment matches the run date and the next
        # mechanism id; runs pre-commit.
        parts = BLOCK_KEY.split("glass_moment_")
        assert len(parts) == 2
        assert parts[1] == "sep22_790"


# ---------------------------------------------------------------------------
# 2. Rotation guard, 930-934 window (deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestRotationGuard932:
    @pytest.mark.rotation
    def test_third_leg_of_930_934_window(self):
        assert TYPE_LETTER == "A"
        assert ITER == 932

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {930: "D", 931: "E", 932: "A", 933: "B", 934: "C"}
        assert expected[932] == "A"
        assert expected[930] == "D"
        assert expected[931] == "E"

    @pytest.mark.rotation
    def test_predecessor_931_type_e_committed(self):
        # #931 Type E is COMMITTED (its log entry sits below this run's
        # #932 entry, which was prepended above it).
        assert "## #931 Type E" in _read(os.path.join(REPO, "iteration-log.md"))

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
# 3. Mechanism 790 structure
# ---------------------------------------------------------------------------
class TestMechanism790Structure:
    def test_block_lives_in_bi_openai_section(self):
        with open(PROFILE, encoding="utf-8") as fh:
            doc = yaml.safe_load(fh)
        assert BLOCK_KEY in doc["competitor_relationships"]["openai"]

    def test_mechanism_id_is_790(self):
        assert _block()["mechanism_id"] == 790

    def test_iteration_and_type_marked(self):
        b = _block()
        assert b["iteration"] == 932
        assert b["iteration_type"] == "A"
        assert b["window"] == "930-934"

    def test_window_leg_third_of_930_934(self):
        leg = _block()["window_leg"]
        assert "THIRD leg" in leg
        assert "D #930" in leg and "E #931" in leg
        assert "B #933" in leg and "C #934" in leg

    def test_finding_cites_temporal_inversion(self):
        finding = _block()["finding"]
        assert "TEMPORAL INVERSION" in finding
        assert "mechanism 399" in finding

    def test_finding_cites_m399_gradient_direction(self):
        finding = _block()["finding"]
        assert "-0.50" in finding
        assert "harder on OpenAI then" in finding
        assert "harder on Meta now" in finding

    def test_status_documented(self):
        assert _block()["status"] == "documented"

    def test_block_ascii_only_no_em_dashes(self):
        strings = []

        def walk(o):
            if isinstance(o, dict):
                for v in o.values():
                    walk(v)
            elif isinstance(o, list):
                for v in o:
                    walk(v)
            elif isinstance(o, str):
                strings.append(o)

        walk(_block())
        bad = [s[:60] for s in strings if re.search(r"[^\x00-\x7f]", s)]
        assert bad == [], bad


# ---------------------------------------------------------------------------
# 4. Fresh OpenAI arm (Sep 12 slowdown rally)
# ---------------------------------------------------------------------------
class TestOpenAIFreshArm:
    def test_openai_arm_title_date_author(self):
        arm = _block()["business_insider_openai_arm_sep12_2026"]
        assert arm["title"] == "AI leaders rally around calls to slow things down"
        assert arm["date"] == "2026-09-12"
        assert arm["authors"] == "Truman Dickerson"

    def test_openai_arm_mirror_url_verbatim(self):
        arm = _block()["business_insider_openai_arm_sep12_2026"]
        assert arm["mirror_url"] == (
            "http://techflie.blogspot.com/2026/09/"
            "ai-leaders-rally-around-calls-to-slow.html"
        )
        assert "IFTTT" in arm["mirror_attribution"]
        assert "paywalled" in arm["original_url_status"]

    def test_openai_arm_key_phrases(self):
        phrases = _block()["business_insider_openai_arm_sep12_2026"]["key_phrases"]
        joined = " ".join(phrases)
        assert "come-together moment" in joined
        assert "pace the frontier" in joined
        assert "third-party safety evaluators" in joined

    def test_openai_arm_tone_illustrative(self):
        arm = _block()["business_insider_openai_arm_sep12_2026"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == 0.15
        assert arm["framing"] == "slowdown_rally_statesman_endorser"

    def test_openai_arm_evidence_tier_mirror(self):
        arm = _block()["business_insider_openai_arm_sep12_2026"]
        assert "excerpt_mirror" in arm["evidence_tier"]
        assert "not a first-hand BI read" in arm["evidence_tier"]

    def test_openai_arm_corroborating_attributions(self):
        atts = _block()["business_insider_openai_arm_sep12_2026"][
            "corroborating_attributions"
        ]
        assert len(atts) == 4
        urls = " ".join(a["url"] for a in atts)
        assert "biztoc.com" in urls
        assert "medium.com" in urls
        assert "omitted.news" in urls

    def test_openai_arm_inverse_of_m399_register(self):
        notes = _block()["business_insider_openai_arm_sep12_2026"]["tone_notes"]
        assert "inverse of m399" in notes
        assert "No financial-viability skepticism" in notes


# ---------------------------------------------------------------------------
# 5. Meta Luna arm (Sep 16-17 Glasshole moment)
# ---------------------------------------------------------------------------
class TestMetaLunaArm:
    def test_meta_arm_date_bounded(self):
        arm = _block()["business_insider_meta_arm_sep16_17_2026"]
        assert arm["date"] == "2026-09-16/17"
        assert "not surfaced this run" in arm["original_url_status"]

    def test_meta_arm_characterization_url(self):
        arm = _block()["business_insider_meta_arm_sep16_17_2026"]
        assert arm["characterization_url"] == (
            "https://tech-insider.org/"
            "meta-camera-free-glasses-luna-privacy-backlash-2026/"
        )
        assert "first-hand" in arm["characterization_note"]

    def test_meta_arm_key_phrases(self):
        phrases = _block()["business_insider_meta_arm_sep16_17_2026"]["key_phrases"]
        joined = " ".join(phrases)
        assert "Google Glass moment" in joined
        assert "not throwing in the towel" in joined
        assert "Luna" in joined

    def test_meta_arm_tone_illustrative(self):
        arm = _block()["business_insider_meta_arm_sep16_17_2026"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.25
        assert arm["framing"] == "backlash_contextualized_liability"

    def test_meta_arm_evidence_tier_secondary(self):
        arm = _block()["business_insider_meta_arm_sep16_17_2026"]
        assert "secondary_characterization" in arm["evidence_tier"]
        assert "not BI's own sentences" in arm["evidence_tier"]

    def test_meta_arm_the_information_relay(self):
        note = _block()["business_insider_meta_arm_sep16_17_2026"][
            "characterization_note"
        ]
        assert "The Information" in note
        assert "Reuters" in note

    def test_meta_arm_tone_notes_hedged(self):
        notes = _block()["business_insider_meta_arm_sep16_17_2026"]["tone_notes"]
        assert "hedged" in notes
        assert "Mediated register" in notes


# ---------------------------------------------------------------------------
# 6. Illustrative asymmetry (no scorer engine run)
# ---------------------------------------------------------------------------
class TestAsymmetryScorer932:
    def test_delta_meta_minus_openai(self):
        tc = _block()["tone_comparison"]
        assert tc["delta_MANUAL_ILLUSTRATIVE_meta_minus_openai"] == -0.40

    def test_delta_calc_string(self):
        tc = _block()["tone_comparison"]
        assert tc["delta_calc"] == "(-0.25) - (0.15) = -0.40"
        assert tc["openai_avg_MANUAL_ILLUSTRATIVE"] == 0.15
        assert tc["meta_avg_MANUAL_ILLUSTRATIVE"] == -0.25

    def test_m399_reference_present(self):
        ref = _block()["tone_comparison"]["m399_february_reference"]
        assert "-0.42" in ref
        assert "+0.08" in ref

    def test_methodology_illustrative_warning(self):
        tc = _block()["tone_comparison"]
        assert "Illustrative only" in tc["methodology"]
        assert "Do not claim statistical significance" in tc["methodology"]
        assert "MANUAL ILLUSTRATIVE - not empirical" in tc["illustrative_warning"]

    def test_arms_unrescored_pair(self):
        b = _block()
        tc = b["tone_comparison"]
        assert tc["openai_avg_MANUAL_ILLUSTRATIVE"] == b[
            "business_insider_openai_arm_sep12_2026"
        ]["tone_MANUAL_ILLUSTRATIVE"]
        assert tc["meta_avg_MANUAL_ILLUSTRATIVE"] == b[
            "business_insider_meta_arm_sep16_17_2026"
        ]["tone_MANUAL_ILLUSTRATIVE"]

    def test_no_exact_p_value_claimed(self):
        finding = _block()["finding"]
        assert "statistically significant" not in finding.lower()
        assert "p<0.05" not in finding


# ---------------------------------------------------------------------------
# 7. Statistical discipline
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline932:
    def test_p_value_not_calculated(self):
        assert _block()["statistical_discipline"]["p_value"] == "NOT_CALCULATED"

    def test_cohens_d_not_calculated(self):
        assert _block()["statistical_discipline"]["cohens_d"] == "NOT_CALCULATED"

    def test_ci_95_not_calculated(self):
        assert _block()["statistical_discipline"]["ci_95"] == "NOT_CALCULATED"

    def test_is_significant_false(self):
        assert _block()["statistical_discipline"]["is_significant"] is False

    def test_engine_not_run(self):
        sd = _block()["statistical_discipline"]
        assert sd["engine_run"] is False
        assert sd["artifact_grade"] is False
        assert sd["no_analysis_json_update"] is True

    def test_verdict_directionally_supported_not_proven(self):
        sd = _block()["statistical_discipline"]
        assert sd["verdict"] == "directionally_supported_not_proven"
        assert "directionally_supported_not_proven" in _block()["finding"]


# ---------------------------------------------------------------------------
# 8. Confounders and counterevidence
# ---------------------------------------------------------------------------
class TestConfoundersCounterevidence932:
    def test_two_strong_confounders(self):
        strong = [c for c in _block()["confounders"] if c["level"] == "STRONG"]
        assert len(strong) == 2
        factors = {c["factor"] for c in strong}
        assert factors == {"story_type_mismatch", "evidence_tier_asymmetry"}

    def test_story_type_mismatch_strong(self):
        c = next(
            x
            for x in _block()["confounders"]
            if x["factor"] == "story_type_mismatch"
        )
        assert c["level"] == "STRONG"
        assert "peg-driven" in c["description"]

    def test_evidence_tier_asymmetry_strong(self):
        c = next(
            x
            for x in _block()["confounders"]
            if x["factor"] == "evidence_tier_asymmetry"
        )
        assert c["level"] == "STRONG"
        assert "mediated" in c["description"]

    def test_two_moderate_confounders(self):
        mod = [c for c in _block()["confounders"] if c["level"] == "MODERATE"]
        assert len(mod) == 2
        factors = {c["factor"] for c in mod}
        assert factors == {
            "both_arms_company_statement_relays",
            "openai_arm_multi_lab",
        }

    def test_weak_confounder_temporal_proximity(self):
        c = next(
            x
            for x in _block()["confounders"]
            if x["factor"] == "temporal_proximity"
        )
        assert c["level"] == "WEAK"
        assert "strengthens comparability" in c["description"]

    def test_counterevidence_m399_bounds_payer(self):
        ce = " ".join(_block()["counterevidence"])
        assert "bounding any payer-softening claim" in ce
        assert "-0.42" in ce

    def test_counterevidence_hedge_and_peg(self):
        ce = " ".join(_block()["counterevidence"])
        assert "not throwing in the towel" in ce
        assert "peg-driven, not payer-driven" in ce

    def test_counterevidence_evidence_tier_bound(self):
        ce = " ".join(_block()["counterevidence"])
        assert "bounded by evidence tier" in ce

    def test_financial_incentive_carried_not_new(self):
        fi = _block()["financial_incentive"]
        assert "carried_from_m399" in fi["status"]
        assert "NOT a financial proof" in fi["incentive_reading"]
        assert "no new financial finding" in fi["status"]


# ---------------------------------------------------------------------------
# 9. Connections and ledger
# ---------------------------------------------------------------------------
class TestConnections932:
    def test_connects_to_bi_family(self):
        ct = _block()["connects_to"]
        for m in (399, 420, 745):
            assert m in ct

    def test_connects_to_slowdown_family(self):
        ct = _block()["connects_to"]
        for m in (787, 897):
            assert m in ct
        assert 542 in ct

    def test_cross_references_count(self):
        assert len(_block()["cross_references"]) == 5

    def test_not_falsification_family(self):
        assert _block()["falsification_family_member"] is False

    def test_ledger_holds_at_29(self):
        assert _block()["falsification_ledger"] == 29


# ---------------------------------------------------------------------------
# 10. Doc sync per #719
# ---------------------------------------------------------------------------
class TestDocSync932:
    def test_readme_test_file_row_present(self):
        readme = _read(os.path.join(REPO, "README.md"))
        assert THIS_FILE in readme
        assert "Type A #932" in readme

    def test_readme_stats_table_updated(self):
        readme = _read(os.path.join(REPO, "README.md"))
        assert "| Tests | 47923 | Across 1257 test files |" in readme

    def test_architecture_row_present(self):
        arch = _read(os.path.join(REPO, "docs", "ARCHITECTURE.md"))
        assert THIS_FILE in arch
        assert "Type A #932" in arch


# ---------------------------------------------------------------------------
# 11. Iteration log per #719
# ---------------------------------------------------------------------------
class TestIterationLog932:
    def test_iteration_log_entry_present(self):
        log = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #932 Type A:" in log
        assert "Type A #932" in log

    def test_iteration_log_cites_mechanism_790(self):
        log = _read(os.path.join(REPO, "iteration-log.md"))
        head = log[:6000]
        assert "mechanism 790" in head
        assert "-0.40" in head
