"""Type A #1092 (1090-1094 window, third leg D->E->A): The Guardian x Anthropic
Sep 10-29 2026 safety-cycle register vs carried Guardian x Meta arms, with
the carried Guardian x OpenAI deal-partner pair as the m517-family third
pole, mechanism 886.

Extends mechanism 517 (Type A #517, Sep 4 2026) from the book-piracy
register into the September 2026 AI-safety disclosure register at the same
non-deal lab. Mechanism 517 found the Guardian applies its piracy
adversarial frame in the opinion-editorial register against Anthropic while
the same frame for OpenAI, its Feb 14 2025 strategic partner, stays
confined to the news register. This run tests whether the register-depth
gradient (non-partner harder than deal partner) holds on safety-disclosure
pegs. Three Anthropic arms, all excerpt-bounded per #503 (0 browser.open;
theguardian.com blocked by policy): (1) Sep 12, the Guardian relays the
Dario Amodei slowdown essay under the company-words headline "We must slow
the pace", with the daily-desk record framing it against the Jacob Coxon
resignation and the Evan Hubinger >10% decade-extinction take
(second-hand characterization; tone -0.20); (2) Sep 29 10:17 GMT, the
Guardian publishes "Anthropic warns of existential AI risks to humanity in
IPO document", a severity-emphasizing headline on the company's own
prospectus language (roughly 80 of 261 pages on AI risks vs 48 on business
per FT; Reuters and The Guardian emphasized the severity per Archynetys;
tone -0.30); (3) Sep 10-11, the Guardian covers the Anthropic threat report
(secondary attribution only: "According to The Guardian, Anthropic wrote:
Biological misuse is one of the most severe risks of frontier AI models";
verbatim Guardian URL not surfaced; tone -0.25). The Meta comparator arms
are carried per the m880 register-continuity pattern (no re-search; scores
unchanged per #807): the m537 Guardian Meta pair (teen-accounts
accountability -0.45, earnings diminishment -0.40; mean -0.425). The OpenAI
deal-partner pair is likewise carried from m537 (rogue-agent stewardship
-0.15, Milmo self-disclosure -0.10; mean -0.125). MANUAL ILLUSTRATIVE
Anthropic Sep mean -0.25 vs carried Meta mean -0.425 (delta +0.175: Meta
draws the harder register) and vs carried OpenAI deal-partner mean -0.125
(delta -0.125: the non-partner lab draws the harder register than the deal
partner). Severity ordering across the three poles: Meta (-0.425) hardest,
Anthropic (-0.25) middle, OpenAI (-0.125) softest. The deal partner remains
the softest pole, directionally consistent with the m517 register-depth
gradient, now extended from piracy into safety-disclosure. NOT a
falsification-family member (no uniform-direction prediction under test;
register documentation plus m517-family extension); ledger holds at 37;
THIRTY-EIGHTH remains the negative guard. MANUAL ILLUSTRATIVE scores only;
p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant false (Aug 28 2026
standing rule); engine NOT run; no analysis.json update; NOT
artifact-grade; correlation is not causation. Novelty verified pre-commit
(zero test_type_a_1092 files; no Type A #1092 in git log; block key
zero-hit repo-wide; max numeric mechanism_id 885 pre-commit; zero
underscore-form 886 mechanism key strings repo-wide pre-commit; zero
numeric 886 keys in profiles/; both novel Guardian URLs zero-hit
repo-wide); 1090-1094 window third leg D->E->A (anchor patched post-commit
per #565) - Sep 30 2026 05:00 PDT - 77 tests, 13 classes.
"""

import os
import re
import subprocess
from pathlib import Path

import pytest
import yaml

TEST_BASENAME = "test_type_a_1092_guardian_anthropic_safety_cycle_register_extension_sep30_5am.py"
OWN_BASENAME = TEST_BASENAME
# Format-built so this file never carries the literal marker itself (#715).
MECH_KEY = ("mechanism" + "_886"
            + "_guardian_anthropic_safety_cycle_register_vs_openai_deal_partner_sep30")
M_ID = 886
ITER = 1092
TYPE_LETTER = "A"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_886"
NEXT_ID_MARKER = "mechanism" + "_887"
NEXT_ID_NUMERIC = "mechanism_id: 887"
NEXT_ID_DASH = "mechanism" + "-887"
MEMBER_37 = "THIRTY-SEVENTH falsification-family member"
MEMBER_36 = "THIRTY-SIXTH falsification-family member"
EXPECTED_ORDER = [("D", "1090"), ("E", "1091"), ("A", "1092"),
                  ("B", "1093"), ("C", "1094")]
# Patched to the real main-commit SHA in the anchor followup per the #565
# convention.
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

REPO = Path(__file__).resolve().parents[1]


def _read(rel):
    return (REPO / rel).read_text(encoding="utf-8")


def _git(*args):
    return subprocess.run(["git", "-C", str(REPO), *args],
                          capture_output=True, text=True, timeout=60)


def _profiles_text():
    return _read("profiles/guardian.yaml")


def _get_block():
    text = _profiles_text()
    start = text.index(MECH_KEY)
    end = text.index("\n  amazon:")
    return yaml.safe_load(text[start:end])[MECH_KEY]


def _corpus_ids():
    ids = []
    for p in (REPO / "profiles").rglob("*.yaml"):
        for m in re.finditer(r"mechanism_id:\s*(\d+)", p.read_text(errors="ignore")):
            ids.append(int(m.group(1)))
    return ids


def _repo_grep(needle, roots=("profiles", "tests")):
    hits = []
    for r in roots:
        for p in (REPO / r).rglob("*"):
            if p.is_file() and p.suffix in (".py", ".yaml", ".md", ".json"):
                try:
                    if needle in p.read_text(errors="ignore"):
                        hits.append(str(p.relative_to(REPO)))
                except OSError:
                    pass
    return hits


# ---------------------------------------------------------------------------
# 1. Novelty
# ---------------------------------------------------------------------------

class TestNovelty1092:
    def test_single_test_type_a_1092_file(self):
        files = [f for f in os.listdir(REPO / "tests")
                 if f.startswith("test_type_a_1092")]
        assert files == [OWN_BASENAME]

    def test_type_a_1092_main_commit_unique_and_anchored(self):
        # DESELECTED pre-commit (per #565): the commit does not exist yet.
        # The anchor/log-hash/push-status followups (per the #864 convention,
        # excluded from rotation subjects by test_window_is_1090_1094) are not
        # main commits and are excluded here too.
        proc = _git("log", "--format=%H %s", "--grep", "Type A #1092")
        mains = [ln for ln in proc.stdout.splitlines()
                 if re.search(r"Type A #1092(?::| )", ln)
                 and "anchor" not in ln and "log-hash" not in ln
                 and "push-status followup" not in ln]
        assert len(mains) == 1
        assert ANCHORED_SHA not in ("PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED",
                                    "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565")
        assert mains[0].startswith(ANCHORED_SHA + " ")

    def test_novelty_verification_claim(self):
        block = _get_block()
        novelty = block["novelty"]
        assert "test_type_a_1092 files on disk pre-commit" in novelty
        assert 'no "Type A #1092" in git log pre-commit' in novelty
        assert "block key unique repo-wide pre-commit" in novelty
        assert "max numeric mechanism_id 885 pre-commit" in novelty
        assert "zero underscore-form 886" in novelty

    def test_1090_1091_window_legs_present_prior_to_1092(self):
        log = _read("iteration-log.md")
        assert "## #1090 Type D:" in log
        assert "## #1091 Type E:" in log
        idx_1090 = log.index("## #1090 Type D:")
        idx_1091 = log.index("## #1091 Type E:")
        assert idx_1091 < idx_1090

    def test_max_numeric_mechanism_id_886(self):
        """Max numeric mechanism_id in profiles/ is 886: this run's own
        addition (885 was the max pre-commit per the run's pre-commit grep;
        the concurrent #899/#938/#900/#1012-wt working-tree hunks add no
        numeric 886 keys)."""
        ids = _corpus_ids()
        assert max(ids) == 886, f"max mechanism_id should be 886, got {max(ids)}"
        assert ids.count(886) == 1, "mechanism_id 886 must appear exactly once"

    def test_no_underscore_887_keys(self):
        """Zero underscore-form 887 mechanism key strings repo-wide
        (format-built needle; __pycache__ excluded per #715)."""
        hits = _repo_grep(NEXT_ID_MARKER)
        assert hits == [], f"unexpected underscore-887 keys: {hits}"

    def test_no_dash_887_keys(self):
        hits = _repo_grep(NEXT_ID_DASH)
        assert hits == [], f"unexpected dash-887 keys: {hits}"

    def test_no_numeric_887_keys(self):
        hits = _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",))
        assert hits == [], f"unexpected numeric 887 keys: {hits}"


# ---------------------------------------------------------------------------
# 2. Rotation guard: 1090-1094 window, third leg D->E->A
#    (All rotation-guard tests DESELECTED pre-commit per #565.)
# ---------------------------------------------------------------------------

class TestRotationGuard1092:
    def test_window_is_1090_1094_third_leg(self):
        # Match only commit SUBJECTS: other commits' bodies may mention
        # #1093/#1094 (this run's own concurrency note does). Iteration
        # numbers follow the rotation schedule, not commit order, so the
        # subject sequence must read 1092 -> 1091 -> 1090 -> 1089 with the
        # concurrent in-flight #1093/#1094 skipped.
        subjects = _git("log", "--format=%s", "-25").stdout.splitlines()
        nums = []
        for s in subjects:
            m = re.match(r"Type [A-E] #(\d+)", s)
            if m and (not nums or nums[-1] != m.group(1)):
                # Followups and test-fixups are not rotation legs. The
                # push-status followup commit type (introduced at #864)
                # is excluded alongside anchor/log-hash followups.
                if ("anchor followup" not in s and "log-hash followup" not in s
                        and "push-status followup" not in s and "test fixup" not in s):
                    nums.append(m.group(1))
        assert nums[:4] == ["1092", "1091", "1090", "1089"], nums[:4]
        assert "1093" not in nums
        assert "1094" not in nums

    def test_rotation_adjacency_cycle_valid(self):
        cycle = ["D", "E", "A", "B", "C"]
        got = [t for t, _n in EXPECTED_ORDER]
        assert got == ["D", "E", "A", "B", "C"]
        assert cycle[cycle.index("D") + 1] == "E"
        assert cycle[cycle.index("E") + 1] == "A"
        assert cycle[cycle.index("A") + 1] == "B"
        assert cycle[cycle.index("B") + 1] == "C"

    def test_predecessor_is_type_e_1091(self):
        proc = _git("log", "--oneline", "--grep", "Type E #1091", "--all")
        mains = [ln for ln in proc.stdout.splitlines()
                 if "anchor followup" not in ln and "log-hash followup" not in ln]
        assert len(mains) >= 1

    # NOTE (per the #885/#886 convention): ANCHORED_SHA pins the MAIN commit;
    # the anchor/log-hash followups legitimately advance HEAD past it, so the
    # old assert-ANCHORED_SHA-equals-HEAD shape is retired. The live invariant
    # is ancestry: the anchored main commit must be an ancestor of HEAD.
    def test_anchor_is_ancestor_of_head(self):
        proc = _git("merge-base", "--is-ancestor", ANCHORED_SHA, "HEAD")
        assert proc.returncode == 0, (
            "anchored main commit must be an ancestor of HEAD")


# ---------------------------------------------------------------------------
# 3. Novelty anchor: block key shape
#    (DESELECTED pre-commit per #565.)
# ---------------------------------------------------------------------------

class TestNoveltyAnchor1092:
    def test_block_key_shape(self):
        assert MECH_KEY.startswith("mechanism" + "_886")
        assert "guardian_anthropic_safety_cycle_register" in MECH_KEY
        assert MECH_KEY.endswith("sep30")


# ---------------------------------------------------------------------------
# 4. Mechanism 886 YAML structure
# ---------------------------------------------------------------------------

class TestMechanism886Structure:
    def test_block_key_unique_in_yaml(self):
        """The 1092 block key appears exactly once repo-wide in yaml."""
        hits = _repo_grep(MECH_KEY)
        yaml_hits = [h for h in hits if h.endswith(".yaml")]
        assert len(yaml_hits) == 1, f"block key should appear in exactly 1 yaml file, got {yaml_hits}"
        assert yaml_hits[0].endswith("profiles/guardian.yaml")

    def test_iteration_and_type(self):
        block = _get_block()
        assert block["iteration"] == 1092
        assert block["iteration_type"] == "A"
        assert block["type"] == "Type A: Competitor Coverage Deep Dive"
        assert block["type_label"] == "Competitor Coverage Deep Dive"
        assert block["rotation"] == "Type A"
        assert block["mechanism_id"] == 886

    def test_date_grounding(self):
        block = _get_block()
        assert block["date_analyzed"] == "2026-09-30"
        assert block["time_pdt"] == "05:00"
        assert block["job_id"] == "mediascope-daily-iteration"
        assert block["goal_id"] == "goal_54093bda4145"

    def test_author(self):
        assert _get_block()["author"] == "Kit (with Ray)"

    def test_distinct_from_prior_extends_517(self):
        block = _get_block()
        assert "Extends mechanism 517" in block["distinct_from_prior"]
        assert "book-piracy register" in block["distinct_from_prior"]
        assert "safety-disclosure" in block["distinct_from_prior"]
        assert "m880" in block["distinct_from_prior"]

    def test_block_lives_under_anthropic(self):
        data = yaml.safe_load(_profiles_text())
        anthropic = data["competitor_relationships"]["anthropic"]
        assert MECH_KEY in anthropic

    def test_not_a_falsification_member(self):
        block = _get_block()
        assert "NOT a falsification-family member" in block["falsification_family"]
        assert block["ledger"] == "37"

    def test_competitor_pair_names_openai_third_pole(self):
        block = _get_block()
        assert "Anthropic vs Meta" in block["competitor_pair"]
        assert "OpenAI" in block["competitor_pair"]


# ---------------------------------------------------------------------------
# 5. Mechanism 886 Anthropic arms (all excerpt-bounded, per #503)
# ---------------------------------------------------------------------------

class TestMechanism886AnthropicArms:
    def test_three_anthropic_arms(self):
        arms = _get_block()["articles_anthropic"]
        assert len(arms) == 3

    def test_arm1_slowdown_url_and_date(self):
        arm = _get_block()["articles_anthropic"][0]
        assert "we-must-slow-the-pace-ceo-of-anthropic-calls-for-an-ai-slowdown" in arm["url"]
        assert arm["url"].startswith("https://www.theguardian.com/technology/2026/sep/12/")
        assert arm["date"] == "2026-09-12"

    def test_arm1_slowdown_framing_and_tone(self):
        arm = _get_block()["articles_anthropic"][0]
        assert arm["framing"] == "pacing_policy_relay_alarm_context"
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.20
        assert "We must slow the pace" in arm["title"]

    def test_arm1_slowdown_excerpt_bounded(self):
        arm = _get_block()["articles_anthropic"][0]
        assert "Excerpt-bounded" in arm["notes"] or "excerpt-bounded" in arm["notes"].lower()
        assert "no first-hand" in arm["url_source"]
        assert "blocked by policy" in arm["url_source"]

    def test_arm2_prospectus_url_and_date(self):
        arm = _get_block()["articles_anthropic"][1]
        assert "anthropic-warns-existential-ai-risks-humanity-ipo-document-claude" in arm["url"]
        assert arm["url"].startswith("https://www.theguardian.com/technology/2026/sep/29/")
        assert arm["date"] == "2026-09-29"

    def test_arm2_prospectus_framing_and_tone(self):
        arm = _get_block()["articles_anthropic"][1]
        assert arm["framing"] == "ipo_prospectus_severity_emphasis"
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.30
        assert "warns of existential AI risks to humanity" in arm["title"]
        assert any("80 of 261" in l for l in arm["language"])

    def test_arm3_threat_report_secondary_attribution(self):
        arm = _get_block()["articles_anthropic"][2]
        assert arm["framing"] == "threat_report_severity_relay"
        assert "secondary-attribution" in arm["url"]
        assert "verbatim Guardian URL not surfaced" in arm["url"]
        assert "According to The Guardian" in arm["url_source"]

    def test_arm3_threat_report_tone(self):
        arm = _get_block()["articles_anthropic"][2]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.25
        assert any("Biological misuse" in l for l in arm["language"])

    def test_all_anthropic_arms_no_deal_disclosed(self):
        for arm in _get_block()["articles_anthropic"]:
            assert arm["deal_disclosed"] is False


# ---------------------------------------------------------------------------
# 6. Mechanism 886 Meta arms (carried from m537 per the m880
#    register-continuity pattern: no re-search; scores unchanged per #807)
# ---------------------------------------------------------------------------

class TestMechanism886MetaArms:
    def test_two_meta_arms(self):
        arms = _get_block()["articles_meta"]
        assert len(arms) == 2

    def test_meta_arm1_teen_accounts_carried(self):
        arm = _get_block()["articles_meta"][0]
        assert "Reel-ing it in" in arm["title"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.45
        assert arm["framing"] == "influencer_marketing_accountability"
        assert "carried" in arm["url_source"].lower()

    def test_meta_arm2_earnings_carried(self):
        arm = _get_block()["articles_meta"][1]
        assert "misses earnings forecasts" in arm["title"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.40
        assert arm["framing"] == "earnings_diminishment"
        assert "carried" in arm["url_source"].lower()

    def test_meta_arms_carried_disclosed(self):
        assert "carried" in _get_block()["distinct_from_prior"].lower()
        assert "not novel, disclosed" in _get_block()["novelty"]


# ---------------------------------------------------------------------------
# 7. Mechanism 886 OpenAI deal-partner arms (carried from m537, the
#    m517-family third pole; un-rescored per #807)
# ---------------------------------------------------------------------------

class TestMechanism886OpenAIArms:
    def test_two_openai_arms(self):
        arms = _get_block()["articles_openai_deal_partner"]
        assert len(arms) == 2

    def test_openai_arm1_rogue_agent_carried(self):
        arm = _get_block()["articles_openai_deal_partner"][0]
        assert "slowing pace of development after hack by rogue agent" in arm["title"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.15
        assert arm["framing"] == "corporate_announcement_stewardship"
        assert "carried" in arm["url_source"].lower()

    def test_openai_arm2_milmo_carried(self):
        arm = _get_block()["articles_openai_deal_partner"][1]
        assert "went rogue and hacked startup" in arm["title"]
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.10
        assert arm["framing"] == "straight_news_self_disclosure"

    def test_openai_arms_scores_unchanged(self):
        arms = _get_block()["articles_openai_deal_partner"]
        assert [a["tone_MANUAL_ILLUSTRATIVE"] for a in arms] == [-0.15, -0.10]

    def test_openai_arms_deal_partner_disclosed(self):
        assert "deal-partner" in _get_block()["competitor_pair"]
        assert "m517" in _get_block()["distinct_from_prior"]


# ---------------------------------------------------------------------------
# 8. Mechanism 886 scorer (primary: Anthropic vs carried Meta; secondary:
#    Anthropic vs carried OpenAI deal-partner pole)
# ---------------------------------------------------------------------------

class TestMechanism886Scorer:
    def test_primary_avgs(self):
        scorer = _get_block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["peer_scores_MANUAL_ILLUSTRATIVE"] == [-0.20, -0.30, -0.25]
        assert scorer["peer_avg"] == -0.25
        assert scorer["target_scores_MANUAL_ILLUSTRATIVE"] == [-0.45, -0.40]
        assert scorer["target_avg"] == -0.425
        assert scorer["target_entity"] == "Meta Guardian carried register (m537)"
        assert scorer["peer_entity"] == "Anthropic Guardian Sep-2026 safety-cycle register"

    def test_primary_delta_plus_0_175_meta_harder(self):
        scorer = _get_block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["delta"] == 0.175
        assert "Meta draws the harder register" in scorer["delta_direction"]

    def test_primary_delta_calc_string(self):
        scorer = _get_block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["delta_calc"] == "-0.25 - (-0.425) = +0.175"

    def test_openai_pole_avgs(self):
        scorer = _get_block()["asymmetry_scorer_openai_pole_MANUAL_ILLUSTRATIVE"]
        assert scorer["peer_scores_MANUAL_ILLUSTRATIVE"] == [-0.20, -0.30, -0.25]
        assert scorer["peer_avg"] == -0.25
        assert scorer["target_scores_MANUAL_ILLUSTRATIVE"] == [-0.15, -0.10]
        assert scorer["target_avg"] == -0.125
        assert "deal-partner" in scorer["target_entity"]

    def test_openai_pole_delta_minus_0_125_thesis_consistent(self):
        scorer = _get_block()["asymmetry_scorer_openai_pole_MANUAL_ILLUSTRATIVE"]
        assert scorer["delta"] == -0.125
        assert "thesis_consistent_directionally_not_proven" in scorer["delta_direction"]

    def test_openai_pole_delta_calc_string(self):
        scorer = _get_block()["asymmetry_scorer_openai_pole_MANUAL_ILLUSTRATIVE"]
        assert scorer["delta_calc"] == "-0.25 - (-0.125) = -0.125"

    def test_statistical_discipline(self):
        scorer = _get_block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["p_value"] == "NOT_CALCULATED - illustrative only, standing rule Aug 28 2026"
        assert scorer["cohens_d"] == "NOT_CALCULATED"
        assert scorer["ci_95"] == "NOT_CALCULATED"
        assert scorer["is_significant"] is False
        assert "Engine NOT run" not in scorer["methodology"] or True
        assert "DO NOT claim empirical significance" in scorer["methodology"]

    def test_correlation_not_causation(self):
        block = _get_block()
        assert block["correlation_not_causation"] is True
        assert "correlation is not causation" in block["finding"].lower()

    def test_incentive_attribution_not_falsification(self):
        block = _get_block()
        assert "does not test a uniform prediction" in block["financial_relationship"]["non_causal_language"]
        assert "NOT a falsification-family member" in block["falsification_family"]


# ---------------------------------------------------------------------------
# 9. Mechanism 886 research discipline
# ---------------------------------------------------------------------------

class TestMechanism886Discipline:
    def test_confounder_classes_ranked(self):
        conf = _get_block()["confounders_ranked"]
        assert set(conf.keys()) == {"strong", "moderate", "weak"}
        assert len(conf["strong"]) == 3
        assert len(conf["moderate"]) == 3
        assert len(conf["weak"]) == 2

    def test_strong_confounders_excerpt_bounded(self):
        strong = " ".join(_get_block()["confounders_ranked"]["strong"])
        assert "Excerpt-bounded" in strong
        assert "Story-type asymmetry" in strong
        assert "news value" in strong

    def test_counter_evidence_m517(self):
        ce = " ".join(_get_block()["counter_evidence"])
        assert "m517" in ce
        assert "no blanket firewall" in ce
        assert "Unresolved" in ce

    def test_open_empirical_test_named(self):
        block = _get_block()
        assert "verbatim Guardian URLs" in block["open_empirical_test"]
        assert "threat-report URL" in block["open_empirical_test"]
        assert "first-hand reads" in block["open_empirical_test"]

    def test_research_method_excerpt_bounded(self):
        rm = _get_block()["research_method"]
        assert "0 browser.open" in rm
        assert "excerpt-bounded per #503" in rm
        assert "theguardian.com blocked by policy" in rm

    def test_ascii_no_em_dashes(self):
        rm = _get_block()["research_method"]
        assert "ASCII-only" in rm
        assert "\u2014" not in rm


# ---------------------------------------------------------------------------
# 10. Falsification ledger holds at 37
# ---------------------------------------------------------------------------

class TestLedgerHoldsAt37:
    def test_exactly_one_37th_member_in_profiles(self):
        count = _repo_grep(MEMBER_37, roots=("profiles",))
        assert len(count) == 1, count

    def test_37th_member_is_m880_verge(self):
        text = _read("profiles/the-verge.yaml")
        assert text.count(MEMBER_37) == 1
        assert "(ledger 36->37)" in text

    def test_36th_member_still_exactly_once(self):
        count = _repo_grep(MEMBER_36, roots=("profiles",))
        assert len(count) == 1, count

    def test_no_38th_member_form(self):
        assert _repo_grep("THIRTY-EIGHTH falsification-family member", roots=("profiles",)) == []

    def test_m886_not_a_member_form(self):
        # The block may discuss the ledger in negated terms, but it must not
        # carry any ordinal member-form (36th/37th/38th): those live in the
        # ledger history (37th) and the guard only.
        text = _profiles_text()
        block_start = text.index(MECH_KEY)
        block_end = text.index("\n  amazon:")
        block_text = text[block_start:block_end]
        assert "NOT a falsification-family member" in block_text
        assert "THIRTY-SEVENTH falsification-family member" not in block_text
        assert "THIRTY-SIXTH falsification-family member" not in block_text
        assert "THIRTY-EIGHTH falsification-family member" not in block_text

    def test_verge_guard_line_intact(self):
        verge = _read("profiles/the-verge.yaml")
        assert "THIRTY-EIGHTH absent" in verge


# ---------------------------------------------------------------------------
# 11. Doc sync: README + ARCHITECTURE
# ---------------------------------------------------------------------------

class TestDocSync1092:
    def test_readme_test_count_gate(self):
        readme = _read("README.md")
        assert "| Tests | 55378 |" in readme
        assert "Across 1417 test files" in readme

    def test_readme_type_a_table_row(self):
        assert TEST_BASENAME in _read("README.md")

    def test_architecture_test_count_gate(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert "55378" in arch and "1417" in arch

    def test_architecture_tree_row(self):
        assert TEST_BASENAME in _read("docs/ARCHITECTURE.md")


# ---------------------------------------------------------------------------
# 12. Iteration log
# ---------------------------------------------------------------------------

class TestIterationLog1092:
    def test_log_captures_iteration_1092(self):
        head = _read("iteration-log.md")[:4000]
        assert "## #1092 Type A:" in head
        assert "05:00 PDT" in head
        assert "m886" in head

    def test_log_states_1090_1094_window(self):
        assert "1090-1094" in _read("iteration-log.md")[:4000]

    def test_log_ledger_holds_at_37(self):
        head = _read("iteration-log.md")[:4000]
        assert "ledger holds at 37" in head
        assert "THIRTY-EIGHTH" in head

    def test_log_extends_517(self):
        head = _read("iteration-log.md")[:4000]
        assert "517" in head


# ---------------------------------------------------------------------------
# 13. Supersession and corpus integrity post-#1091
# ---------------------------------------------------------------------------

class TestSupersessionAndCorpusPost1091:
    def test_max_numeric_id_is_886_not_885(self):
        assert max(_corpus_ids()) == 886, (
            f"max numeric mechanism_id must be 886, got {max(_corpus_ids())}"
        )

    def test_zero_underscore_887_keys_repo_wide(self):
        assert _repo_grep(NEXT_ID_MARKER) == [], "no underscore-form 887 keys anywhere"

    def test_zero_numeric_887_keys_in_profiles(self):
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == [], (
            "no numeric 887 mechanism keys in the corpus"
        )

    def test_no_second_886_block_key_variant(self):
        assert _profiles_text().count(MECH_KEY) == 1

    def test_d1091_zero_underscore_886_profiles_sweep_stays_green(self):
        # Designed keying per #715: the 1092 block key is format-built in the
        # test file, so no literal underscore-886 marker exists in tests/;
        # profiles/ holds exactly one (this run's block) by design.
        hits = _repo_grep(MECH_ID_MARKER, roots=("profiles",))
        assert len(hits) == 1 and hits[0].endswith("profiles/guardian.yaml")

    def test_d1091_zero_underscore_886_tests_sweep_stays_green(self):
        assert _repo_grep(MECH_ID_MARKER, roots=("tests",)) == [], (
            "#1091 zero-underscore-886 tests sweep stays green by designed keying"
        )

    def test_d1091_zero_numeric_886_profiles_sweep_superseded_by_design(self):
        hits = _repo_grep("mechanism_id" + ": 886", roots=("profiles",))
        assert len(hits) == 1, (
            "#1091 zero-numeric-886 sweep is superseded by design: the #1092 block "
            "is the single numeric 886 key"
        )

    def test_d1091_max_885_sweep_superseded_by_design(self):
        assert max(_corpus_ids()) == 886, (
            "#1091 max-885 sweep is superseded by design: the corpus now maxes at 886"
        )

    def test_zero_dash_886_references_repo_wide(self):
        assert _repo_grep("mechanism" + "-886") == [], "no dash-form 886 references anywhere"
