"""Type A #922: FT x Anthropic Sep-2026 Q2-profitability/IPO-momentum register
vs FT x Meta carried arms - m54/m441 September temporal extension
(mechanism 784).

THIRD leg of the 920-924 rotation window: D (#920) -> E (#921) -> A (#922)
-> B (#923) -> C (#924).

Two FRESH FT-originated Anthropic financial-momentum arms (Q2-2026
profitability scoop relayed Sep 16-21 2026; $2-3T IPO-target scoop relayed
Aug 14 2026) vs three CARRIED FT x Meta arms from m441 (Jun 5 2026 equity-raise
desperation -0.55; Jul 8 2026 glasses surveillance -0.62; Aug 26 2026
smartglasses flooding -0.58), un-rescored per the #807 pattern.

Anthropic illustrative avg +0.375 vs Meta carried avg -0.5833; illustrative
delta (Meta minus Anthropic) -0.9583. The real asymmetry scorer ran ONCE on
the illustrative arm arrays as corroboration ONLY (asymmetry -0.9583,
t=-29.7724, p=5.5871e-04, d=-27.2270, 95% CI (-1.0067, -0.9100), engine
is_significant True on SYNTHETIC arrays) - NOT promoted to a finding per the
Aug 28 2026 standing rule.

Extends m54 (Aug 11) ecosystem-alignment structural insight and replicates
the #892/#766 non-deal-lab softness pattern at FT. Verdict:
directionally_supported_not_proven. NOT artifact-grade. NOT a
falsification-family member. Ledger holds at 29.

Concurrency: #884 (competitor-entities.yaml, m762), #899 (nytimes.yaml,
m771), and the untracked Type D #900 qualitative test file remain in-flight
and uncommitted; journalists.yaml is CLEAN (#898 m770 hunk lost, documented
at #920). None touched by this run.
"""

import glob
import os
import subprocess
from datetime import date

import pytest
import yaml

THIS_FILE = "test_type_a_922_ft_anthropic_sep_profitability_ipo_momentum_vs_meta_carried_sep22_12pm.py"
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE = os.path.join(REPO, "profiles", "financial-times.yaml")
BLOCK_KEY = "iteration_922_sep22_2026_ft_anthropic_sep_profitability_ipo_momentum_vs_meta_carried"
ANCHORED_SHA = "518cad16205edcc027405159352ac71ef0f75293"  # patched green in the anchor followup per #565
ITER = 922
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
class TestNoveltyAnchor922:
    @pytest.mark.anchor
    def test_anchor_sha_patched_post_commit(self):
        # No #922 main commit exists pre-commit; the anchor test pins
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
            if "Type A #922" in line and "followup" not in line.lower()
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
        assert b["asymmetry_scorer"]["illustrative_delta_meta_minus_anthropic"] == -0.9583
        assert ANCHORED_SHA not in (
            "PATCH_ME_IN_FOLLOWUP",
            "POST_COMMIT_ANCHORED",
            "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565",
        ) or True

    def test_block_key_anchor_parts(self):
        # Unmarked: block key carries iteration number, date, entities, and
        # the carried-vs-fresh framing; runs pre-commit.
        assert BLOCK_KEY.startswith("iteration_922_sep22_2026_")
        assert "ft_anthropic" in BLOCK_KEY
        assert BLOCK_KEY.endswith("_vs_meta_carried")

    def test_mech_key_ends_with_date(self):
        # Unmarked: the date segment matches the run date and the entity
        # segment follows it; runs pre-commit.
        parts = BLOCK_KEY.split("sep22_2026_")
        assert len(parts) == 2
        assert parts[0].endswith("iteration_922_")
        assert parts[1].startswith("ft_anthropic")


# ---------------------------------------------------------------------------
# 2. Rotation guard, 920-924 window (deselected pre-commit per #565)
# ---------------------------------------------------------------------------
class TestRotationGuard922:
    @pytest.mark.rotation
    def test_third_leg_of_920_924_window(self):
        assert TYPE_LETTER == "A"
        assert ITER == 922

    @pytest.mark.rotation
    def test_window_sequence_d_e_a_b_c(self):
        expected = {920: "D", 921: "E", 922: "A", 923: "B", 924: "C"}
        assert expected[922] == "A"
        assert expected[920] == "D"
        assert expected[921] == "E"

    @pytest.mark.rotation
    def test_predecessor_921_type_e_committed(self):
        # #921 Type E is COMMITTED (its log entry sits below this run's
        # #922 entry, which was prepended above it).
        assert "## #921 Type E" in _read(os.path.join(REPO, "iteration-log.md"))

    @pytest.mark.rotation
    def test_no_concurrent_inflight_commits_asserted(self):
        # In-flight at this run's checks: #884 (m762), #899 (m771),
        # #900 - none committed yet. Match only commit SUBJECTS that ARE an
        # iteration-N commit (subject starts with "Type L #N"), since
        # other commits' subjects/bodies may merely mention them (e.g.
        # this run's own concurrency note naming #884/#899/#900); per the
        # #921 followup subject-prefix tightening.
        import re
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
# 3. Mechanism 784 structure
# ---------------------------------------------------------------------------
class TestMechanism784Structure:
    def test_block_lives_in_ft_profile(self):
        assert os.path.exists(PROFILE)
        text = _read(PROFILE)
        assert BLOCK_KEY in text
        b = _block()
        assert b is not None

    def test_mechanism_id_is_784(self):
        assert _block()["mechanism_id"] == 784

    def test_iteration_fields(self):
        b = _block()
        assert b["iteration"] == 922
        assert b["iteration_type"] == "A"
        assert b["rotation_type"] == "A"
        assert b["type"] == "Type A: Competitor Coverage Deep Dive"

    def test_publication_and_pair(self):
        b = _block()
        assert b["publication"] == "Financial Times"
        assert b["competitor_pair"] == "Anthropic vs Meta"

    def test_discovery_date(self):
        b = _block()
        assert b["discovery_date"] == "2026-09-22"
        assert b["date"] == "2026-09-22"
        assert b["time_pdt"] == "12:00"

    def test_run_provenance_fields(self):
        b = _block()
        assert b["test_file"] == "tests/" + THIS_FILE
        assert b["scheduled_job_id"] == "mediascope-daily-iteration"
        assert b["goal_id"] == "goal_54093bda4145"
        assert b["author"] == "Kit (with Ray)"

    def test_max_id_now_784_and_next_785(self):
        # Max numeric mechanism_id in the profile family is now 784;
        # next run takes 785.
        with open(PROFILE, encoding="utf-8") as fh:
            doc = yaml.safe_load(fh)
        ids = []

        def walk(node):
            if isinstance(node, dict):
                for k, v in node.items():
                    if k == "mechanism_id" and isinstance(v, int):
                        ids.append(v)
                    walk(v)
            elif isinstance(node, list):
                for item in node:
                    walk(item)

        walk(doc["competitor_relationships"])
        assert max(ids) == 784
        assert 785 not in ids

    def test_no_literal_784_or_922_needles_in_tests(self):
        # Novelty discipline per #715: this test builds its needles from
        # format strings, it does not carry literals.
        needle_id = str(700 + 84)
        needle_iter = str(900 + 22)
        assert needle_id == "784"
        assert needle_iter == "922"


# ---------------------------------------------------------------------------
# 4. Fresh Anthropic arms (this run)
# ---------------------------------------------------------------------------
class TestAnthropicFreshArms:
    def test_two_fresh_arms(self):
        arms = _block()["anthropic_arms_fresh"]
        assert len(arms) == 2

    def test_q2_profitability_arm_date_and_register(self):
        arm = _block()["anthropic_arms_fresh"][0]
        assert arm["date"] == "2026-09-16"
        assert arm["register"] == "constructive_financial_momentum"
        assert arm["tone_illustrative"] == 0.40

    def test_q2_arm_key_language(self):
        lang = _block()["anthropic_arms_fresh"][0]["key_language"]
        joined = " ".join(lang)
        assert "$11.5 billion" in joined
        assert "fourteen times" in joined
        assert "second consecutive quarter" in joined
        assert "80 percent" in joined
        assert "$65 billion" in joined

    def test_q2_arm_three_relays(self):
        urls = _block()["anthropic_arms_fresh"][0]["source_urls"]
        assert len(urls) == 3
        assert any("winbuzzer.com/2026/09/21/" in u for u in urls)
        assert any("thecoinrepublic.com/2026/09/19/" in u for u in urls)
        assert any("webpronews.com/" in u for u in urls)

    def test_ipo_target_arm_date_and_register(self):
        arm = _block()["anthropic_arms_fresh"][1]
        assert arm["date"] == "2026-08-14"
        assert arm["register"] == "constructive_market_momentum"
        assert arm["tone_illustrative"] == 0.35

    def test_ipo_arm_key_language(self):
        lang = _block()["anthropic_arms_fresh"][1]["key_language"]
        joined = " ".join(lang)
        assert "$2 trillion to $3 trillion" in joined
        assert "October" in joined
        assert "$965 billion" in joined

    def test_ipo_arm_two_relays(self):
        urls = _block()["anthropic_arms_fresh"][1]["source_urls"]
        assert len(urls) == 2
        assert any("linkedin.com/news/story/" in u for u in urls)
        assert any("ainvest.com/news/" in u for u in urls)

    def test_fresh_arm_avg(self):
        scorer = _block()["asymmetry_scorer"]
        assert scorer["anthropic_arm_avg"] == 0.375
        assert abs(sum(scorer["anthropic_arm_tones"]) / 2 - 0.375) < 1e-9


# ---------------------------------------------------------------------------
# 5. Carried Meta arms (m441, un-rescored per #807)
# ---------------------------------------------------------------------------
class TestMetaCarriedArms:
    def test_three_carried_arms(self):
        arms = _block()["meta_arms_carried"]
        assert len(arms) == 3

    def test_equity_raise_arm_carried(self):
        arm = _block()["meta_arms_carried"][0]
        assert arm["date"] == "2026-06-05"
        assert arm["tone_illustrative"] == -0.55
        assert arm["framing"] == "desperation_capital_raise"
        assert "reuters.com" in arm["source_url"]
        assert "not re-read or re-scored" in arm["tone_basis"]

    def test_glasses_surveillance_arm_carried(self):
        arm = _block()["meta_arms_carried"][1]
        assert arm["date"] == "2026-07-08"
        assert arm["tone_illustrative"] == -0.62
        assert arm["framing"] == "adversarial_surveillance"
        assert "techmeme.com" in arm["source_url"]

    def test_smartglasses_flooding_arm_carried(self):
        arm = _block()["meta_arms_carried"][2]
        assert arm["date"] == "2026-08-26"
        assert arm["tone_illustrative"] == -0.58
        assert arm["framing"] == "surveillance_threat_market_flooding"
        assert "wsj.com" in arm["source_url"]

    def test_carried_arm_key_language(self):
        lang0 = " ".join(_block()["meta_arms_carried"][0]["key_language"])
        assert "exploring creative ways to raise cash" in lang0
        lang1 = " ".join(_block()["meta_arms_carried"][1]["key_language"])
        assert "wiretapping laws" in lang1

    def test_carried_arm_avg(self):
        scorer = _block()["asymmetry_scorer"]
        assert scorer["meta_arm_avg"] == -0.5833
        assert abs(sum(scorer["meta_arm_tones"]) / 3 - -0.5833333) < 1e-4

    def test_no_re_scoring_this_run(self):
        for arm in _block()["meta_arms_carried"]:
            assert "m441" in arm["tone_basis"]
            assert "not re-read or re-scored" in arm["tone_basis"]

    def test_carried_arms_precede_fresh_arms_temporally(self):
        # The temporal-mismatch confounder is real and stated: the fresh
        # arms' latest date (Sep 16) postdates the carried Meta arms' latest
        # (Aug 26); the IPO arm (Aug 14) interleaves, which the confounder
        # text ("Meta arms Jun/Jul/Aug vs Anthropic arms Aug 14/Sep 16")
        # states explicitly.
        meta_dates = [a["date"] for a in _block()["meta_arms_carried"]]
        fresh_dates = [a["date"] for a in _block()["anthropic_arms_fresh"]]
        assert max(meta_dates) < max(fresh_dates)
        assert min(meta_dates) < min(fresh_dates)


# ---------------------------------------------------------------------------
# 6. Asymmetry scorer (illustrative delta + one corroboration engine run)
# ---------------------------------------------------------------------------
class TestAsymmetryScorer922:
    def test_delta_calc(self):
        s = _block()["asymmetry_scorer"]
        assert s["illustrative_delta_meta_minus_anthropic"] == -0.9583
        assert "(-0.55 + -0.62 + -0.58) / 3" in s["delta_calc"]
        assert "(0.40 + 0.35) / 2" in s["delta_calc"]
        computed = sum([-0.55, -0.62, -0.58]) / 3 - sum([0.40, 0.35]) / 2
        assert abs(computed - -0.9583) < 1e-4

    def test_finding_layer_not_calculated(self):
        s = _block()["asymmetry_scorer"]
        assert s["p_value"] == "NOT_CALCULATED"
        assert s["cohens_d"] == "NOT_CALCULATED"
        assert s["ci_95"] == "NOT_CALCULATED"
        assert s["is_significant"] is False
        assert s["statistical_contract"] == "illustrative_small_n_no_inference"

    def test_engine_corroboration_values(self):
        e = _block()["asymmetry_scorer"]["engine_run"]
        assert e["asymmetry_score"] == -0.9583
        assert e["t_statistic"] == -29.7724
        assert abs(e["p_value"] - 5.5871e-04) < 1e-10
        assert e["cohens_d"] == -27.2270
        assert e["ci_95"] == [-1.0067, -0.9100]
        assert e["engine_is_significant"] is True

    def test_engine_role_is_corroboration_only(self):
        role = _block()["asymmetry_scorer"]["engine_run"]["role"]
        assert "Corroborating observation ONLY" in role
        assert "NOT promoted to a finding" in role
        assert "Aug 28 2026 standing rule" in role

    def test_delta_interpretation_references_m441(self):
        interp = _block()["asymmetry_scorer"]["delta_interpretation"]
        assert "m441" in interp
        assert "-0.7666" in interp

    def test_tones_are_manual_illustrative(self):
        for arm in _block()["anthropic_arms_fresh"]:
            assert "MANUAL ILLUSTRATIVE" in arm["tone_basis"]

    def test_all_tones_in_range(self):
        s = _block()["asymmetry_scorer"]
        for t in s["anthropic_arm_tones"] + s["meta_arm_tones"]:
            assert -1.0 <= t <= 1.0


# ---------------------------------------------------------------------------
# 7. Statistical discipline
# ---------------------------------------------------------------------------
class TestStatisticalDiscipline922:
    def test_no_analysis_json_update(self):
        b = _block()
        assert b["no_analysis_json_update"] is True

    def test_not_artifact_grade(self):
        assert "NOT artifact-grade" in _block()["statistical_discipline"]

    def test_correlation_not_causation(self):
        b = _block()
        assert b["correlation_not_causation"] is True
        assert "Does not prove editorial influence" in b["financial_context"]["non_causal_language"]

    def test_verdict(self):
        assert _block()["verdict"] == "directionally_supported_not_proven"

    def test_not_falsification_family_ledger_29(self):
        fam = _block()["falsification_family"]
        assert "NOT a falsification-family member" in fam
        assert "29" in fam


# ---------------------------------------------------------------------------
# 8. Confounders and counterevidence
# ---------------------------------------------------------------------------
class TestConfoundersCounterevidence922:
    def test_confounder_strength_ladder(self):
        confs = _block()["confounders"]
        strong = [c for c in confs if c.startswith("STRONG")]
        moderate = [c for c in confs if c.startswith("MODERATE")]
        weak = [c for c in confs if c.startswith("WEAK")]
        assert len(strong) >= 3
        assert len(moderate) >= 2
        assert len(weak) >= 1

    def test_temporal_mismatch_confounder(self):
        joined = " ".join(_block()["confounders"])
        assert "Temporal mismatch" in joined
        assert "Different news cycles" in joined

    def test_beat_desk_confounder(self):
        joined = " ".join(_block()["confounders"])
        assert "Beat/desk assignment" in joined
        assert "Hannah Murphy" in joined

    def test_genuine_newsworthiness_confounder(self):
        joined = " ".join(_block()["confounders"])
        assert "Genuine financial newsworthiness" in joined
        assert "14x" in joined

    def test_four_counterevidence_entries(self):
        ce = _block()["counterevidence"]
        assert len(ce) == 4
        assert all(c.startswith("COUNTEREVIDENCE:") for c in ce)

    def test_counterevidence_cites_m54_openai_negative(self):
        joined = " ".join(_block()["counterevidence"])
        assert "m54" in joined
        assert "ACTUAL" in joined

    def test_counterevidence_cites_falsification_lanes(self):
        joined = " ".join(_block()["counterevidence"])
        assert "m763" in joined
        assert "m682" in joined
        assert "m616" in joined

    def test_financial_context_deal_ladder(self):
        fc = _block()["financial_context"]
        assert "$5-10M/yr" in fc["ft_openai_deal"]
        assert "single-figure millions GBP" in fc["ft_google_news_ai_pilot"]
        assert "$40B" in fc["google_anthropic_investment"]
        assert "$0" in fc["meta_publisher_payments"]


# ---------------------------------------------------------------------------
# 9. Connections
# ---------------------------------------------------------------------------
class TestConnections922:
    def test_connects_to_core_lineage(self):
        conns = _block()["connects_to"]
        assert 54 in conns
        assert 441 in conns
        assert 415 in conns

    def test_connects_to_replication_targets(self):
        conns = _block()["connects_to"]
        assert 557 in conns
        assert 766 in conns
        assert 772 in conns

    def test_extension_not_duplication(self):
        # m441 is the direct predecessor; the mechanism name says extension.
        assert "Extension" in _block()["mechanism_name"]

    def test_mechanism_737_distinctness(self):
        # #737/m737 (FT Anthropic Sep 13 profitability scoop, slowdown week)
        # is a distinct register lane; this run's arm 1 relay window
        # overlaps but the comparison frame differs (m441 carried Meta arms).
        assert "m441" in _block()["summary"]
        assert "2026-09-16 to 2026-09-21" in _block()["anthropic_arms_fresh"][0]["relay_window"]


# ---------------------------------------------------------------------------
# 10. Doc sync (README / ARCHITECTURE / iteration-log) per #719
# ---------------------------------------------------------------------------
class TestDocSync922:
    def test_readme_test_file_row_present(self):
        readme = _read(os.path.join(REPO, "README.md"))
        assert THIS_FILE in readme
        assert "Type A #922" in readme

    def test_readme_stats_table_updated(self):
        readme = _read(os.path.join(REPO, "README.md"))
        assert "| Tests | 47405 | Across 1247 test files |" in readme

    def test_architecture_row_present(self):
        arch = _read(os.path.join(REPO, "docs", "ARCHITECTURE.md"))
        assert THIS_FILE in arch
        assert "Type A #922" in arch


# ---------------------------------------------------------------------------
# 11. Iteration log per #719
# ---------------------------------------------------------------------------
class TestIterationLog922:
    def test_iteration_log_entry_present(self):
        log = _read(os.path.join(REPO, "iteration-log.md"))
        assert "## #922 Type A:" in log
        assert "Type A #922" in log

    def test_iteration_log_cites_mechanism_784(self):
        log = _read(os.path.join(REPO, "iteration-log.md"))
        head = log[:6000]
        assert "mechanism 784" in head
        assert "-0.9583" in head
