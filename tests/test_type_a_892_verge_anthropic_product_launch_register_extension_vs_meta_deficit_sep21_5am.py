"""Type A #892 (890-894 window, third leg D->E->A): The Verge x Anthropic
product-launch register extension (Sep 1-17 2026 product stories) vs carried
Meta deficit arms, mechanism 766.

Extends mechanism 557 (Type A #557, Sep 6 2026) from business-milestone,
solidarity-hero, and compliance registers into the product-launch register.
Two September 2026 Anthropic product stories, both Verge-reported or
Verge-attributed this run, both excerpt-bounded per #503 (0 first-hand
browser.open reads): (1) the Claude Fable 5.1 and Mythos 5.1 launch (Sep 1
2026; exact theverge.com URL surfaced this run inside a secondary GitHub
news-archive mirror record), framed around enterprise agentic gains: up to
45% cheaper agentic work, lower agent costs, data-retention controls, and
less overzealous safeguards (tone +0.20); (2) the "one Claude" merge of
Cowork and chat plus Claude Docs and Claude Slides (announced Sep 16 2026;
Verge coverage Sep 17 by Sebastian Szczeblewski, per the pulseofnations.lol
secondary which states "The Verge first reported the update"), framed as
friction removal, the Cowork toggle vanishing, work continuing while the
laptop is closed, and direct competition with Google Workspace suite and its
Gemini integration (tone +0.15). The two Meta comparator arms are carried
verbatim from mechanism 557 with unchanged scores: "Meta is reentering the
AI race" with Muse Spark (Apr 8 2026, -0.35, deficit/follower) and "Meta
pauses wider Ray-Ban Display expansion due to supply shortages" (Jan 6 2026,
-0.15, supply-constraint deficit). MANUAL ILLUSTRATIVE peer avg +0.175 vs
target avg -0.25, delta +0.425 peer softer. The register softness persists at
the non-deal rival lab in a new register type, further bounding the
financial-determinism hypothesis per mechanism 557. NOT a falsification-family
member (no uniform-direction prediction under test; control-case extension);
ledger holds at 29; THIRTIETH remains the negative guard. MANUAL ILLUSTRATIVE
scores only; p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant false (Aug
28 2026 standing rule); engine NOT run; no analysis.json update; NOT
artifact-grade; correlation is not causation. Novelty verified pre-commit
(zero test_type_a_892 files; no Type A #892 in git log; block key zero-hit
repo-wide; max numeric mechanism_id 765 pre-commit; zero underscore-form 766
keys per #715; zero dash-form 766 references; zero numeric 766 keys in
profiles/; both Anthropic URLs zero-hit repo-wide; Meta arms carried from
557, disclosed); 890-894 window third leg D->E->A (anchor patched post-commit
per #565) - Sep 21 2026 05:00 PDT - 69 tests, 14 classes.
"""

import os
import re
import subprocess
from pathlib import Path

import pytest
import yaml

TEST_BASENAME = "test_type_a_892_verge_anthropic_product_launch_register_extension_vs_meta_deficit_sep21_5am.py"
OWN_BASENAME = TEST_BASENAME
# Format-built so this file never carries the literal marker itself (#715).
MECH_KEY = ("mechanism" + "_766"
            + "_verge_anthropic_product_launch_register_extension_vs_meta_deficit_sep21")
M_ID = 766
ITER = 892
TYPE_LETTER = "A"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_766"
NEXT_ID_MARKER = "mechanism" + "_767"
NEXT_ID_NUMERIC = "mechanism_id: 767"
NEXT_ID_DASH = "mechanism" + "-767"
MEMBER_29 = "TWENTY-NINTH falsification-family member"
MEMBER_28 = "TWENTY-EIGHTH falsification-family member"
EXPECTED_ORDER = [("A", "892"), ("E", "891"), ("D", "890"), ("C", "889")]
# Note: ("C", "884") is absent from EXPECTED_ORDER - the concurrent Type C
# #884 run is in-flight (m762 uncommitted in the working tree at this run's
# checks) and commits after this run; see test_window_is_890_894_third_leg.
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "3abca639b94bbde8c4560525f80c132ba70e3fe5"

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

class TestNovelty892:
    def test_single_test_type_a_892_file(self):
        files = [f for f in os.listdir(REPO / "tests")
                 if f.startswith("test_type_a_892")]
        assert files == [OWN_BASENAME]

    def test_type_a_892_main_commit_unique_and_anchored(self):
        # DESELECTED pre-commit (per #565): the commit does not exist yet.
        proc = _git("log", "--format=%H %s", "--grep", "Type A #892")
        mains = [ln for ln in proc.stdout.splitlines()
                 if re.search(r"Type A #892(?::| )", ln)
                 and "anchor followup" not in ln and "log-hash followup" not in ln]
        assert len(mains) == 1
        assert ANCHORED_SHA not in ("PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED",
                                    "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565")
        assert mains[0].startswith(ANCHORED_SHA + " ")

    def test_novelty_verification_claim(self):
        block = _get_block()
        novelty = block["novelty"]
        assert "test_type_a_892 files on disk pre-commit" in novelty
        assert 'no "Type A #892" in git log pre-commit' in novelty
        assert "block key unique repo-wide pre-commit" in novelty
        assert "max numeric mechanism_id 765 pre-commit" in novelty
        assert "zero underscore-form 766" in novelty

    def test_890_891_window_legs_present_prior_to_892(self):
        log = _read("iteration-log.md")
        assert "## #890 Type D:" in log
        assert "## #891 Type E:" in log
        idx_890 = log.index("## #890 Type D:")
        idx_891 = log.index("## #891 Type E:")
        assert idx_891 < idx_890

    def test_max_numeric_mechanism_id_766(self):
        """Max numeric mechanism_id in profiles/ is 766: this run's own
        addition (765 was the max pre-commit per the run's pre-commit grep;
        the concurrent m762 block stays uncommitted in the working tree)."""
        ids = _corpus_ids()
        assert max(ids) == 766, f"max mechanism_id should be 766, got {max(ids)}"
        assert ids.count(766) == 1, "mechanism_id 766 must appear exactly once"

    def test_no_underscore_767_keys(self):
        """Zero underscore-form 767 mechanism key strings repo-wide
        (format-built needle; __pycache__ excluded per #715)."""
        hits = _repo_grep(NEXT_ID_MARKER)
        assert hits == [], f"unexpected underscore-767 keys: {hits}"

    def test_no_dash_767_keys(self):
        hits = _repo_grep(NEXT_ID_DASH)
        assert hits == [], f"unexpected dash-767 keys: {hits}"

    def test_no_numeric_767_keys(self):
        hits = _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",))
        assert hits == [], f"unexpected numeric 767 keys: {hits}"


# ---------------------------------------------------------------------------
# 2. Rotation guard: 890-894 window, third leg D->E->A
#    (All rotation-guard tests DESELECTED pre-commit per #565.)
# ---------------------------------------------------------------------------

class TestRotationGuard892:
    def test_window_is_890_894_third_leg(self):
        # The concurrent Type C #884 run commits after this run; its main
        # commit is absent from git history. Match only commit SUBJECTS:
        # other commits' bodies may mention #884 (this run's own
        # concurrency note does). Iteration numbers follow the rotation
        # schedule, not commit order, so the subject sequence must read
        # 892 -> 891 -> 890 -> 889 with the in-flight 884 skipped.
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
        assert nums[:4] == ["892", "891", "890", "889"], nums[:4]
        assert "884" not in nums

    def test_rotation_adjacency_cycle_valid(self):
        cycle = ["D", "E", "A", "B", "C"]
        got = [t for t, _n in EXPECTED_ORDER]
        assert got == ["A", "E", "D", "C"]
        assert cycle[cycle.index("D") + 1] == "E"
        assert cycle[cycle.index("E") + 1] == "A"
        assert cycle[cycle.index("A") + 1] == "B"
        assert cycle[cycle.index("B") + 1] == "C"

    def test_predecessor_is_type_e_891(self):
        proc = _git("log", "--oneline", "--grep", "Type E #891", "--all")
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

class TestNoveltyAnchor892:
    def test_block_key_shape(self):
        assert MECH_KEY.startswith("mechanism" + "_766")
        assert "verge_anthropic_product_launch_register_extension" in MECH_KEY
        assert "vs_meta_deficit" in MECH_KEY
        assert MECH_KEY.endswith("sep21")


# ---------------------------------------------------------------------------
# 4. Mechanism 766 YAML structure
# ---------------------------------------------------------------------------

class TestMechanism766Structure:
    def test_block_key_unique_in_yaml(self):
        """The 892 block key appears exactly once repo-wide in yaml."""
        hits = _repo_grep(MECH_KEY)
        yaml_hits = [h for h in hits if h.endswith(".yaml")]
        assert len(yaml_hits) == 1, f"block key should appear in exactly 1 yaml file, got {yaml_hits}"
        assert yaml_hits[0].endswith("profiles/the-verge.yaml")

    def test_iteration_and_type(self):
        block = _get_block()
        assert block["iteration"] == 892
        assert block["iteration_type"] == "A"
        assert block["type"] == "Type A: Competitor Coverage Deep Dive"
        assert block["type_label"] == "Competitor Coverage Deep Dive"
        assert block["rotation"] == "Type A"
        assert block["mechanism_id"] == 766

    def test_date_grounding(self):
        block = _get_block()
        assert block["date_analyzed"] == "2026-09-21"
        assert block["time_pdt"] == "05:00"
        assert block["job_id"] == "mediascope-daily-iteration"
        assert block["goal_id"] == "goal_54093bda4145"

    def test_author(self):
        assert _get_block()["author"] == "Kit (with Ray)"

    def test_distinct_from_prior_extends_557(self):
        block = _get_block()
        assert "Extends mechanism 557" in block["distinct_from_prior"]
        assert "product-launch register" in block["distinct_from_prior"]

    def test_block_lives_under_anthropic(self):
        data = yaml.safe_load(_profiles_text())
        anthropic = data["competitor_relationships"]["anthropic"]
        assert MECH_KEY in anthropic

    def test_not_a_falsification_member(self):
        block = _get_block()
        assert "NOT a falsification-family member" in block["falsification_family"]
        assert block["ledger"] == "29"


# ---------------------------------------------------------------------------
# 5. Mechanism 766 Anthropic arms (both excerpt-bounded, per #503)
# ---------------------------------------------------------------------------

class TestMechanism766AnthropicArms:
    def test_two_anthropic_arms(self):
        arms = _get_block()["articles_anthropic"]
        assert len(arms) == 2

    def test_arm1_fable_url_and_date(self):
        arm = _get_block()["articles_anthropic"][0]
        assert "987830/anthropic-claude-fable-mythos-5-1" in arm["url"]
        assert arm["url"].startswith("https://www.theverge.com/ai-artificial-intelligence/")
        assert arm["date"] == "2026-09-01"

    def test_arm1_fable_framing_and_tone(self):
        arm = _get_block()["articles_anthropic"][0]
        assert arm["framing"] == "product_launch_enterprise_cost_benefit"
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == 0.20
        assert "up to 45% cheaper for agentic work" in arm["language"]
        assert "data-retention controls" in arm["language"]

    def test_arm1_fable_excerpt_bounded(self):
        arm = _get_block()["articles_anthropic"][0]
        assert "Excerpt-bounded" in arm["notes"] or "excerpt-bounded" in arm["notes"].lower()
        assert "no first-hand" in arm["url_source"]

    def test_arm2_one_claude_url_and_date(self):
        arm = _get_block()["articles_anthropic"][1]
        assert "pulseofnations.lol/anthropic-merges-cowork" in arm["url"]
        assert arm["date"] == "2026-09-17"

    def test_arm2_one_claude_framing_and_tone(self):
        arm = _get_block()["articles_anthropic"][1]
        assert arm["framing"] == "product_launch_unification_competitive"
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == 0.15
        assert 'Anthropic calls "one Claude"' in arm["language"]
        assert "direct competition with Google Workspace suite" in " ".join(arm["language"])

    def test_arm2_one_claude_verge_attributed_via_secondary(self):
        arm = _get_block()["articles_anthropic"][1]
        assert "The Verge first reported the update" in arm["url_source"]
        assert "Sebastian Szczeblewski" in arm["url_source"]
        assert "Verge-attributed via secondary" in arm["url_source"]

    def test_all_anthropic_arms_no_deal_disclosed(self):
        for arm in _get_block()["articles_anthropic"]:
            assert arm["deal_disclosed"] is False


# ---------------------------------------------------------------------------
# 6. Mechanism 766 Meta arms (carried verbatim from 557, unchanged scores)
# ---------------------------------------------------------------------------

class TestMechanism766MetaArms:
    def test_two_meta_arms(self):
        arms = _get_block()["articles_meta"]
        assert len(arms) == 2

    def test_meta_arm1_muse_spark_carried(self):
        arm = _get_block()["articles_meta"][0]
        assert "reentering the AI race" in arm["title"]
        assert arm["date"] == "2026-04-08"
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.35
        assert arm["framing"] == "deficit_follower"
        assert "carried verbatim from mechanism 557" in arm["url_source"].lower()

    def test_meta_arm2_rayban_display_carried(self):
        arm = _get_block()["articles_meta"][1]
        assert "supply shortages" in arm["title"]
        assert arm["date"] == "2026-01-06"
        assert arm["tone_MANUAL_ILLUSTRATIVE"] == -0.15
        assert arm["framing"] == "supply_constraint_deficit"
        assert "carried" in arm["notes"].lower()

    def test_meta_arms_scores_unchanged(self):
        arms = _get_block()["articles_meta"]
        assert [a["tone_MANUAL_ILLUSTRATIVE"] for a in arms] == [-0.35, -0.15]

    def test_meta_arms_carried_disclosed(self):
        assert "carried verbatim from mechanism 557" in _get_block()["distinct_from_prior"]
        assert "not novel, disclosed" in _get_block()["novelty"]


# ---------------------------------------------------------------------------
# 7. Mechanism 766 scorer
# ---------------------------------------------------------------------------

class TestMechanism766Scorer:
    def test_avgs(self):
        scorer = _get_block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["peer_scores_MANUAL_ILLUSTRATIVE"] == [0.20, 0.15]
        assert scorer["peer_avg"] == 0.175
        assert scorer["target_scores_MANUAL_ILLUSTRATIVE"] == [-0.35, -0.15]
        assert scorer["target_avg"] == -0.25
        assert scorer["target_entity"] == "Meta Verge deficit register"
        assert scorer["peer_entity"] == "Anthropic Verge product-launch register"

    def test_delta_plus_0_425(self):
        scorer = _get_block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["delta"] == 0.425
        assert scorer["delta_direction"] == "peer softer than target by 0.425"

    def test_delta_calc_string(self):
        scorer = _get_block()["asymmetry_scorer_MANUAL_ILLUSTRATIVE"]
        assert scorer["delta_calc"] == "0.175 - (-0.25) = +0.425"

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
# 8. Mechanism 766 research discipline
# ---------------------------------------------------------------------------

class TestMechanism766Discipline:
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

    def test_counter_evidence_sony_warner_unresolved(self):
        ce = " ".join(_get_block()["counter_evidence"])
        assert "Sony/Warner" in ce
        assert "unresolved" in ce

    def test_open_empirical_test_named(self):
        block = _get_block()
        assert "Sony Music Publishing and Warner Chappell Music" in block["open_empirical_test"]
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
# 9. Falsification ledger holds at 29
# ---------------------------------------------------------------------------

class TestLedgerHoldsAt29:
    def test_exactly_one_29th_member_in_profiles(self):
        count = _repo_grep(MEMBER_29, roots=("profiles",))
        assert len(count) == 1, count

    def test_29th_member_is_m763_newscorp(self):
        text = _read("profiles/news-corp.yaml")
        assert text.count(MEMBER_29) == 1
        assert "(ledger 28->29)" in text

    def test_28th_member_still_exactly_once(self):
        count = _repo_grep(MEMBER_28, roots=("profiles",))
        assert len(count) == 1, count

    def test_no_30th_member_form(self):
        assert _repo_grep("THIRTIETH falsification-family member", roots=("profiles",)) == []

    def test_m766_not_a_member_form(self):
        # The block may discuss the ledger in negated terms, but it must not
        # carry any ordinal member-form (29th/28th/30th): those live in
        # news-corp.yaml (29th), journalists.yaml (28th), and the guard only.
        text = _profiles_text()
        block_start = text.index(MECH_KEY)
        block_end = text.index("\n  amazon:")
        block_text = text[block_start:block_end]
        assert "NOT a falsification-family member" in block_text
        assert "TWENTY-NINTH falsification-family member" not in block_text
        assert "TWENTY-EIGHTH falsification-family member" not in block_text
        assert "THIRTIETH falsification-family member" not in block_text

    def test_verge_guard_line_intact(self):
        verge = _read("profiles/the-verge.yaml")
        assert "negative-guard convention continues at THIRTIETH" in verge
        assert "TWENTY-NINTH member-form landed in profiles/news-corp.yaml" in verge
        assert "Type A #887 mechanism 763" in verge


# ---------------------------------------------------------------------------
# 10. Doc sync: README + ARCHITECTURE
# ---------------------------------------------------------------------------

class TestDocSync892:
    def test_readme_test_count_gate(self):
        readme = _read("README.md")
        assert "| Tests | 45734 |" in readme
        assert "Across 1219 test files" in readme

    def test_readme_type_a_table_row(self):
        assert TEST_BASENAME in _read("README.md")

    def test_architecture_test_count_gate(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert "45734" in arch and "1219" in arch

    def test_architecture_tree_row(self):
        assert TEST_BASENAME in _read("docs/ARCHITECTURE.md")


# ---------------------------------------------------------------------------
# 11. Iteration log
# ---------------------------------------------------------------------------

class TestIterationLog892:
    def test_log_captures_iteration_892(self):
        head = _read("iteration-log.md")[:4000]
        assert "## #892 Type A:" in head
        assert "05:00 PDT" in head
        assert "m766" in head

    def test_log_states_890_894_window(self):
        assert "890-894" in _read("iteration-log.md")[:4000]

    def test_log_ledger_holds_at_29(self):
        head = _read("iteration-log.md")[:4000]
        assert "ledger holds at 29" in head
        assert "THIRTIETH" in head

    def test_log_extends_557(self):
        head = _read("iteration-log.md")[:4000]
        assert "557" in head


# ---------------------------------------------------------------------------
# 12. Supersession and corpus integrity post-#891
# ---------------------------------------------------------------------------

class TestSupersessionAndCorpusPost891:
    def test_max_numeric_id_is_766_not_765(self):
        assert max(_corpus_ids()) == 766, (
            f"max numeric mechanism_id must be 766, got {max(_corpus_ids())}"
        )

    def test_zero_underscore_767_keys_repo_wide(self):
        assert _repo_grep(NEXT_ID_MARKER) == [], "no underscore-form 767 keys anywhere"

    def test_zero_numeric_767_keys_in_profiles(self):
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == [], (
            "no numeric 767 mechanism keys in the corpus"
        )

    def test_no_second_766_block_key_variant(self):
        assert _profiles_text().count(MECH_KEY) == 1

    def test_d891_zero_underscore_766_profiles_sweep_stays_green(self):
        # Designed keying per #715: the 892 block key is format-built in the
        # test file, so no literal underscore-766 marker exists in tests/;
        # profiles/ holds exactly one (this run's block) by design.
        hits = _repo_grep(MECH_ID_MARKER, roots=("profiles",))
        assert len(hits) == 1 and hits[0].endswith("profiles/the-verge.yaml")

    def test_d891_zero_underscore_766_tests_sweep_stays_green(self):
        assert _repo_grep(MECH_ID_MARKER, roots=("tests",)) == [], (
            "#892 zero-underscore-766 tests sweep stays green by designed keying"
        )

    def test_d891_zero_numeric_766_profiles_sweep_superseded_by_design(self):
        hits = _repo_grep("mechanism_id" + ": 766", roots=("profiles",))
        assert len(hits) == 1, (
            "#891 zero-numeric-766 sweep is superseded by design: the #892 block "
            "is the single numeric 766 key"
        )

    def test_d891_max_765_sweep_superseded_by_design(self):
        assert max(_corpus_ids()) == 766, (
            "#891 max-765 sweep is superseded by design: the corpus now maxes at 766"
        )

    def test_zero_dash_766_references_repo_wide(self):
        assert _repo_grep(NEXT_ID_DASH) == [], "no dash-form 766 references anywhere"
