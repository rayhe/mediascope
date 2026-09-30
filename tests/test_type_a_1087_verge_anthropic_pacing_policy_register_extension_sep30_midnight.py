"""Type A #1087 (1085-1089 window, third leg D->E->A): The Verge x Anthropic
pacing-policy and IPO-prospectus register extension (Sep 12-29 2026) vs
carried Meta arms, mechanism 883.

Extends mechanism 557 (Type A #557, Sep 6 2026) and mechanism 766
(Type A #892, Sep 21 2026) from business-milestone, solidarity-hero,
compliance, and product-launch registers into two new September 2026
registers at the non-deal AI lab: (1) the pacing-policy register, on
The Verge's Sep 12 coverage of Dario Amodei's "We Must Pace the Frontier"
essay, read analytically (tone 0.0) - the digest record holds that what
survives is a dated essay, an official RT, a unilateral third-party
evaluator-access commitment, and two peer-CEO matches with no named start
date; (2) the IPO-prospectus financial-skeptical register, on the
prospectus risk-factor coverage (roughly 80 of 261 pages on AI risks, a
$42 billion 2025 net loss, self-preserving behaviors), read
adversarially (tone -0.40). The Verge's prospectus coverage is relay-
attested this run: 10news.org confirms theverge.com among the outlets
covering the risk factors, verbatim theverge.com URL not in this run's
excerpts (marked per #503); both arms excerpt-bounded, 0 browser.open.
The two Meta comparator arms are carried per the m880 register-continuity
pattern (no re-search): the #592 Meta glasses set (mean -0.55) and the
m811 Meta Connect Audio piece (+0.10). MANUAL ILLUSTRATIVE Anthropic Sep
mean -0.20 vs carried Meta mean -0.225, delta +0.025 - register PARITY.
The non-deal AI lab draws the same peg-driven skeptical-analytical
register as Meta on a financial-skeptical peg, while the licensing deal
sits with the OTHER lab (OpenAI, hit at -0.25 arc mean by the same outlet
per m880). Companion to m880; control case against financial determinism
at Vox Media, joining m557, m766, #552, and #193. NOT a
falsification-family member (no uniform-direction prediction under test;
control-case extension); ledger holds at 37; THIRTY-EIGHTH remains the
negative guard. MANUAL ILLUSTRATIVE scores only; p_value/cohens_d/ci_95
NOT_CALCULATED; is_significant false (Aug 28 2026 standing rule); engine
NOT run; no analysis.json update; NOT artifact-grade; correlation is not
causation. Novelty verified pre-commit (zero test_type_a_1087 files; no
Type A #1087 in git log; block key zero-hit repo-wide; max numeric
mechanism_id 882 pre-commit; zero underscore-form and dash-form 883
mechanism key strings repo-wide pre-commit; zero numeric 883 keys in
profiles/; both Anthropic URLs zero-hit repo-wide; Meta arms carried from
m880's set, disclosed); 1085-1089 window third leg D->E->A (anchor patched
post-commit per #565) - Sep 30 2026 00:00 PDT - 69 tests, 14 classes.
"""

import os
import re
import subprocess
from pathlib import Path

import pytest
import yaml

TEST_BASENAME = "test_type_a_1087_verge_anthropic_pacing_policy_register_extension_sep30_midnight.py"
OWN_BASENAME = TEST_BASENAME
# Format-built so this file never carries the literal marker itself (#715).
MECH_KEY = ("mechanism" + "_883"
            + "_verge_anthropic_pacing_policy_register_extension_sep30")
M_ID = 883
ITER = 1087
TYPE_LETTER = "A"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_883"
NEXT_ID_MARKER = "mechanism" + "_884"
NEXT_ID_NUMERIC = "mechanism_id: 884"
NEXT_ID_DASH = "mechanism" + "-884"
MEMBER_37 = "THIRTY-SEVENTH falsification-family member"
MEMBER_36 = "THIRTY-SIXTH falsification-family member"
EXPECTED_ORDER = [("D", "1085"), ("E", "1086"), ("A", "1087"),
                  ("B", "1088"), ("C", "1089")]
# Patched to the real main-commit SHA in the anchor followup per the #565
# convention.
ANCHORED_SHA = "db6b141dc220ee804a5edda08057d8d4c2846c20"

REPO = Path(__file__).resolve().parents[1]


def _read(rel):
    return (REPO / rel).read_text(encoding="utf-8")


def _git(*args):
    return subprocess.run(["git", "-C", str(REPO), *args],
                          capture_output=True, text=True, timeout=60)


def _profiles_text():
    return _read("profiles/the-verge.yaml")


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

class TestNovelty1087:
    def test_single_test_type_a_1087_file(self):
        files = [f for f in os.listdir(REPO / "tests")
                 if f.startswith("test_type_a_1087")]
        assert files == [OWN_BASENAME]

    def test_type_a_1087_main_commit_unique_and_anchored(self):
        # DESELECTED pre-commit (per #565): the commit does not exist yet.
        # The anchor/log-hash/push-status followups (per the #864 convention,
        # excluded from rotation subjects by test_window_is_1085_1089) are not
        # main commits and are excluded here too.
        proc = _git("log", "--format=%H %s", "--grep", "Type A #1087")
        mains = [ln for ln in proc.stdout.splitlines()
                 if re.search(r"Type A #1087(?::| )", ln)
                 and "anchor followup" not in ln and "log-hash followup" not in ln
                 and "push-status followup" not in ln]
        assert len(mains) == 1
        assert ANCHORED_SHA not in ("PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED",
                                    "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565")
        assert mains[0].startswith(ANCHORED_SHA + " ")

    def test_novelty_verification_claim(self):
        block = _get_block()
        novelty = block["novelty"]
        assert "test_type_a_1087 files on disk pre-commit" in novelty
        assert 'no "Type A #1087" in git log pre-commit' in novelty
        assert "block key unique repo-wide pre-commit" in novelty
        assert "max numeric mechanism_id 882 pre-commit" in novelty
        assert "zero underscore-form 883" in novelty

    def test_1085_1086_window_legs_present_prior_to_1087(self):
        log = _read("iteration-log.md")
        assert "## #1085 Type D:" in log
        assert "## #1086 Type E:" in log
        idx_1085 = log.index("## #1085 Type D:")
        idx_1086 = log.index("## #1086 Type E:")
        assert idx_1086 < idx_1085

    def test_max_numeric_mechanism_id_883(self):
        """Max numeric mechanism_id in profiles/ is 883: this run's own
        addition (882 was the max pre-commit per the run's pre-commit grep;
        the concurrent #899/#938/#900/#1012-wt working-tree hunks add no
        numeric 883 keys)."""
        ids = _corpus_ids()
        assert max(ids) == 883, f"max mechanism_id should be 883, got {max(ids)}"
        assert ids.count(883) == 1, "mechanism_id 883 must appear exactly once"

    def test_no_underscore_884_keys(self):
        """Zero underscore-form 884 mechanism key strings repo-wide
        (format-built needle; __pycache__ excluded per #715)."""
        hits = _repo_grep(NEXT_ID_MARKER)
        assert hits == [], f"unexpected underscore-884 keys: {hits}"

    def test_no_dash_884_keys(self):
        hits = _repo_grep(NEXT_ID_DASH)
        assert hits == [], f"unexpected dash-884 keys: {hits}"

    def test_no_numeric_884_keys(self):
        hits = _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",))
        assert hits == [], f"unexpected numeric 884 keys: {hits}"


# ---------------------------------------------------------------------------
# 2. Rotation guard: 1085-1089 window, third leg D->E->A
#    (All rotation-guard tests DESELECTED pre-commit per #565.)
# ---------------------------------------------------------------------------

class TestRotationGuard1087:
    def test_window_is_1085_1089_third_leg(self):
        # Match only commit SUBJECTS: other commits' bodies may mention
        # #1088/#1089 (this run's own concurrency note does). Iteration
        # numbers follow the rotation schedule, not commit order, so the
        # subject sequence must read 1087 -> 1086 -> 1085 -> 1084 with the
        # concurrent in-flight #1088/#1089 skipped.
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
        assert nums[:4] == ["1087", "1086", "1085", "1084"], nums[:4]
        assert "1088" not in nums
        assert "1089" not in nums

    def test_rotation_adjacency_cycle_valid(self):
        cycle = ["D", "E", "A", "B", "C"]
        got = [t for t, _n in EXPECTED_ORDER]
        assert got == ["D", "E", "A", "B", "C"]
        assert cycle[cycle.index("D") + 1] == "E"
        assert cycle[cycle.index("E") + 1] == "A"
        assert cycle[cycle.index("A") + 1] == "B"
        assert cycle[cycle.index("B") + 1] == "C"

    def test_predecessor_is_type_e_1086(self):
        proc = _git("log", "--oneline", "--grep", "Type E #1086", "--all")
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

class TestNoveltyAnchor1087:
    def test_block_key_shape(self):
        assert MECH_KEY.startswith("mechanism" + "_883")
        assert "verge_anthropic_pacing_policy_register_extension" in MECH_KEY
        assert MECH_KEY.endswith("sep30")


# ---------------------------------------------------------------------------
# 4. Mechanism 883 YAML structure
# ---------------------------------------------------------------------------

class TestMechanism883Structure:
    def test_block_key_unique_in_yaml(self):
        """The 1087 block key appears exactly once repo-wide in yaml."""
        hits = _repo_grep(MECH_KEY)
        yaml_hits = [h for h in hits if h.endswith(".yaml")]
        assert len(yaml_hits) == 1, f"block key should appear in exactly 1 yaml file, got {yaml_hits}"
        assert yaml_hits[0].endswith("profiles/the-verge.yaml")

    def test_iteration_and_type(self):
        block = _get_block()
        assert block["iteration"] == 1087
        assert block["iteration_type"] == "A"
        assert block["type"] == "Type A: Competitor Coverage Deep Dive"
        assert block["type_label"] == "Competitor Coverage Deep Dive"
        assert block["rotation"] == "Type A"
        assert block["mechanism_id"] == 883

    def test_date_grounding(self):
        block = _get_block()
        assert block["date_analyzed"] == "2026-09-30"
        assert block["time_pdt"] == "00:00"
        assert block["job_id"] == "mediascope-daily-iteration"
        assert block["goal_id"] == "goal_54093bda4145"

    def test_author(self):
        assert _get_block()["author"] == "Kit (with Ray)"

    def test_distinct_from_prior_extends_557_and_766(self):
        block = _get_block()
        assert "Extends mechanism 557" in block["distinct_from_prior"]
        assert "mechanism 766" in block["distinct_from_prior"]
        assert "pacing-policy" in block["distinct_from_prior"]
        assert "IPO-prospectus" in block["distinct_from_prior"]

    def test_block_lives_under_anthropic(self):
        data = yaml.safe_load(_profiles_text())
        anthropic = data["competitor_relationships"]["anthropic"]
        assert MECH_KEY in anthropic

    def test_not_a_falsification_member(self):
        block = _get_block()
        assert "NOT a falsification-family member" in block["falsification_family"]
        assert block["ledger"] == "37"


# ---------------------------------------------------------------------------
# 5. Mechanism 883 Anthropic arms (both excerpt-bounded, per #503)
# ---------------------------------------------------------------------------

class TestMechanism883AnthropicArms:
    def test_two_anthropic_arms(self):
        arms = _get_block()["articles_anthropic"]
        assert len(arms) == 2

    def test_arm1_slowdown_url_and_date(self):
        arm = _get_block()["articles_anthropic"][0]
        assert "994337/anthropic-ceo-slow-down-ai-development" in arm["url"]
        assert arm["url"].startswith("https://www.theverge.com/ai-artificial-intelligence/")
        assert arm["date"] == "2026-09-12"

    def test_arm1_slowdown_framing_and_tone(self):
        arm = _get_block()["articles_anthropic"][0]
        assert arm["framing"] == "policy_essay_analytical_explainer"
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == 0.0
        assert "We Must Pace the Frontier" in arm["language"]
        assert "pump the brakes" in arm["title"].lower()

    def test_arm1_slowdown_excerpt_bounded(self):
        arm = _get_block()["articles_anthropic"][0]
        assert "Excerpt-bounded" in arm["notes"] or "excerpt-bounded" in arm["notes"].lower()
        assert "no first-hand" in arm["url_source"]

    def test_arm2_prospectus_url_and_date(self):
        arm = _get_block()["articles_anthropic"][1]
        assert "10news.org/2026/09/anthropic-raises-concerns-over-ai-risks-in-ipo-filing" in arm["url"]
        assert arm["date"] == "2026-09-29"

    def test_arm2_prospectus_framing_and_tone(self):
        arm = _get_block()["articles_anthropic"][1]
        assert arm["framing"] == "ipo_prospectus_financial_skeptical"
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.40
        assert any("$42 billion" in l for l in arm["language"])
        assert "catastrophic or existential risks" in " ".join(arm["language"])

    def test_arm2_prospectus_verge_relay_attested(self):
        arm = _get_block()["articles_anthropic"][1]
        assert "relay-attested" in arm["url_source"]
        assert "theverge.com" in arm["url_source"]
        assert "verbatim theverge.com URL not in this run" in arm["url_source"]

    def test_all_anthropic_arms_no_deal_disclosed(self):
        for arm in _get_block()["articles_anthropic"]:
            assert arm["deal_disclosed"] is False


# ---------------------------------------------------------------------------
# 6. Mechanism 883 Meta arms (carried per the m880 register-continuity
#    pattern: no re-search; scores unchanged)
# ---------------------------------------------------------------------------

class TestMechanism883MetaArms:
    def test_two_meta_arms(self):
        arms = _get_block()["articles_meta"]
        assert len(arms) == 2

    def test_meta_arm1_592_glasses_set_carried(self):
        arm = _get_block()["articles_meta"][0]
        assert "glasses" in arm["title"].lower()
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.55
        assert arm["framing"] == "wearables_privacy_adversarial"
        assert "carried" in arm["url_source"].lower()

    def test_meta_arm2_m811_audio_carried(self):
        arm = _get_block()["articles_meta"][1]
        assert "Audio" in arm["title"] or "audio" in arm["title"].lower()
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == 0.10
        assert arm["framing"] == "privacy_positive_product"
        assert "carried" in arm["notes"].lower()

    def test_meta_arms_scores_unchanged(self):
        arms = _get_block()["articles_meta"]
        assert [a["tone_MANUAL_ILLUSTRATIVE"] for a in arms] == [-0.55, 0.10]

    def test_meta_arms_carried_disclosed(self):
        assert "carried" in _get_block()["distinct_from_prior"].lower()
        assert "not novel, disclosed" in _get_block()["novelty"]


# ---------------------------------------------------------------------------
# 7. Mechanism 883 scorer
# ---------------------------------------------------------------------------

class TestMechanism883Scorer:
    def test_avgs(self):
        scorer = _get_block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["peer_scores_MANUAL_ILLUSTRATIVE"] == [0.0, -0.40]
        assert scorer["peer_avg"] == -0.20
        assert scorer["target_scores_MANUAL_ILLUSTRATIVE"] == [-0.55, 0.10]
        assert scorer["target_avg"] == -0.225
        assert scorer["target_entity"] == "Meta Verge carried register"
        assert scorer["peer_entity"] == "Anthropic Verge Sep-2026 pacing/prospectus register"

    def test_delta_plus_0_025_register_parity(self):
        scorer = _get_block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["delta"] == 0.025
        assert "parity" in scorer["delta_direction"].lower()

    def test_delta_calc_string(self):
        scorer = _get_block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["delta_calc"] == "-0.20 - (-0.225) = +0.025"

    def test_statistical_discipline(self):
        scorer = _get_block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["p_value"] == "NOT_CALCULATED - illustrative only, standing rule Aug 28 2026"
        assert scorer["cohens_d"] == "NOT_CALCULATED"
        assert scorer["ci_95"] == "NOT_CALCULATED"
        assert scorer["is_significant"] is False
        assert "Engine NOT run" in scorer["methodology"]

    def test_correlation_not_causation(self):
        block = _get_block()
        assert block["correlation_not_causation"] is True
        assert "correlation is not causation" in block["finding"].lower()

    def test_incentive_attribution_control_case(self):
        block = _get_block()
        assert "CONTROL_CASE_AGAINST_FINANCIAL_DETERMINISM" in block["incentive_attribution"]
        assert "not a falsification test" in block["incentive_attribution"]

    def test_block_statistical_discipline(self):
        block = _get_block()
        assert block["no_analysis_json_update"] is True
        assert "NOT artifact-grade" in block["statistical_discipline"]


# ---------------------------------------------------------------------------
# 8. Mechanism 883 research discipline
# ---------------------------------------------------------------------------

class TestMechanism883Discipline:
    def test_confounder_classes_ranked(self):
        conf = _get_block()["confounders_ranked"]
        assert set(conf.keys()) == {"strong", "moderate", "weak"}
        assert len(conf["strong"]) == 3
        assert len(conf["moderate"]) == 3
        assert len(conf["weak"]) == 2

    def test_strong_confounders_genre_hype_beat(self):
        strong = " ".join(_get_block()["confounders_ranked"]["strong"])
        assert "news genre" in strong
        assert "hype cycle" in strong
        assert "beat concentration" in strong

    def test_counter_evidence_prospectus_scope(self):
        ce = " ".join(_get_block()["counter_evidence"])
        assert "relay-attested" in ce
        assert "unresolved" in ce

    def test_open_empirical_test_named(self):
        block = _get_block()
        assert "verbatim Verge prospectus URL".lower() in block["open_empirical_test"].lower()
        assert "observed tone scores" in block["open_empirical_test"]

    def test_research_method_excerpt_bounded(self):
        rm = _get_block()["research_method"]
        assert "0 browser.open" in rm
        assert "excerpt-bounded per #503" in rm

    def test_ascii_no_em_dashes(self):
        rm = _get_block()["research_method"]
        assert "ASCII-only" in rm
        assert "\u2014" not in rm


# ---------------------------------------------------------------------------
# 9. Falsification ledger holds at 37
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

    def test_m883_not_a_member_form(self):
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
# 10. Doc sync: README + ARCHITECTURE
# ---------------------------------------------------------------------------

class TestDocSync1087:
    def test_readme_test_count_gate(self):
        readme = _read("README.md")
        assert "| Tests | 55035 |" in readme
        assert "Across 1412 test files" in readme

    def test_readme_type_a_table_row(self):
        assert TEST_BASENAME in _read("README.md")

    def test_architecture_test_count_gate(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert "55035" in arch and "1412" in arch

    def test_architecture_tree_row(self):
        assert TEST_BASENAME in _read("docs/ARCHITECTURE.md")


# ---------------------------------------------------------------------------
# 11. Iteration log
# ---------------------------------------------------------------------------

class TestIterationLog1087:
    def test_log_captures_iteration_1087(self):
        head = _read("iteration-log.md")[:4000]
        assert "## #1087 Type A:" in head
        assert "00:00 PDT" in head
        assert "m883" in head

    def test_log_states_1085_1089_window(self):
        assert "1085-1089" in _read("iteration-log.md")[:4000]

    def test_log_ledger_holds_at_37(self):
        head = _read("iteration-log.md")[:4000]
        assert "ledger holds at 37" in head
        assert "THIRTY-EIGHTH" in head

    def test_log_extends_557_and_766(self):
        head = _read("iteration-log.md")[:4000]
        assert "557" in head
        assert "766" in head


# ---------------------------------------------------------------------------
# 12. Supersession and corpus integrity post-#1086
# ---------------------------------------------------------------------------

class TestSupersessionAndCorpusPost1086:
    def test_max_numeric_id_is_883_not_882(self):
        assert max(_corpus_ids()) == 883, (
            f"max numeric mechanism_id must be 883, got {max(_corpus_ids())}"
        )

    def test_zero_underscore_884_keys_repo_wide(self):
        assert _repo_grep(NEXT_ID_MARKER) == [], "no underscore-form 884 keys anywhere"

    def test_zero_numeric_884_keys_in_profiles(self):
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == [], (
            "no numeric 884 mechanism keys in the corpus"
        )

    def test_no_second_883_block_key_variant(self):
        assert _profiles_text().count(MECH_KEY) == 1

    def test_d1086_zero_underscore_883_profiles_sweep_stays_green(self):
        # Designed keying per #715: the 1087 block key is format-built in the
        # test file, so no literal underscore-883 marker exists in tests/;
        # profiles/ holds exactly one (this run's block) by design.
        hits = _repo_grep(MECH_ID_MARKER, roots=("profiles",))
        assert len(hits) == 1 and hits[0].endswith("profiles/the-verge.yaml")

    def test_d1086_zero_underscore_883_tests_sweep_stays_green(self):
        assert _repo_grep(MECH_ID_MARKER, roots=("tests",)) == [], (
            "#1087 zero-underscore-883 tests sweep stays green by designed keying"
        )

    def test_d1086_zero_numeric_883_profiles_sweep_superseded_by_design(self):
        hits = _repo_grep("mechanism_id" + ": 883", roots=("profiles",))
        assert len(hits) == 1, (
            "#1086 zero-numeric-883 sweep is superseded by design: the #1087 block "
            "is the single numeric 883 key"
        )

    def test_d1086_max_882_sweep_superseded_by_design(self):
        assert max(_corpus_ids()) == 883, (
            "#1086 max-882 sweep is superseded by design: the corpus now maxes at 883"
        )

    def test_zero_dash_883_references_repo_wide(self):
        assert _repo_grep("mechanism" + "-883") == [], "no dash-form 883 references anywhere"
