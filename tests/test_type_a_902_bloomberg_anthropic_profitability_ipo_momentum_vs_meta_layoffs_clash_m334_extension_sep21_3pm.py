"""Type A #902 (900-904 window, third leg D->E->A): Bloomberg x Anthropic
Sep-2026 profitability/IPO-momentum register vs Bloomberg x Meta
layoffs/partner-clash register (m334 temporal extension; mechanism id 772).

FIRST dedicated corpus mechanism on Bloomberg's Sep 13 2026 profitability
scoop (second straight quarter of positive adjusted operating income
expected; Q2 2026 revenue exceeding $11.5B, ~14x the Q2 2025 figure;
>80% gross margins before rev-share and training costs; ~$2T IPO target,
up to $100B raise; Nvidia up-to-$10B anchor talks) and the Sep 19 2026
$100B-annualized-revenue scoop (run rate $65B end of July, up from $9B end
2025; Nasdaq debut as soon as November; catastrophic-harm anxiety caveat
included) - both Bloomberg-reported, both secondary/mirror-attested
(Bloomberg originals paywalled; 0 browser.open this turn per developer
constraint). The Meta arms are Bloomberg-routed too: Jan 13 2026 Reality
Labs layoffs (>1,000 jobs, ~10%, $60B+ burned since 2020, Bloomberg Law
original) and the early-2026 Bloomberg-reported Meta/EssilorLuxottica
pricing-strategy clash (margin compression, 2.6pp to 60.9%).
MANUAL ILLUSTRATIVE tones: Anthropic +0.45/+0.35 (avg +0.40), Meta
-0.35/-0.30 (avg -0.325); illustrative delta (Anthropic minus Meta)
+0.725. EXTENDS mechanism 334 (Bloomberg LP upstream narrative
originator, Aug 26 2026) into the pre-IPO window. The financial-incentive
leg is a documented NULL-tie: no mapped Bloomberg-Anthropic content deal
(bounded absence); Bloomberg LP runs on terminal subscriptions, not
publisher-style ad dependency, so the payer-softening vector has no mapped
payer here - register documentation and replication, NOT a
falsification-family member; ledger holds at 29; THIRTIETH remains the
negative guard. MANUAL ILLUSTRATIVE scores only;
p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant false (Aug 28 2026
standing rule); engine NOT run; verdict directionally_supported_not_proven;
no analysis.json update; NOT artifact-grade; correlation is not causation.
Novelty verified pre-commit (zero test_type_a_902 files; no 'Type A #902'
in git log; block key zero-hit repo-wide; max numeric mechanism id 771
pre-commit (includes concurrent uncommitted m770/m771/m762); zero
underscore-form 772 keys by designed keying per #715; zero dash-form 772
refs; zero numeric 772 keys in profiles/; all 4 arm URLs zero-hit
repo-wide pre-commit; dead-end candidates rejected: Guardian x OpenAI
Sep-2026 route duplicates Type A #757/m687; Bloomberg $299-glasses
product-positive route cut against the Meta-arm selection); 900-904 window
THIRD leg D->E->A (anchor patched post-commit per #565) - Sep 21 2026
15:00 PDT - 59 tests, 11 classes.
"""

import os
import re
import subprocess
from pathlib import Path

import pytest
import yaml

TEST_BASENAME = "test_type_a_902_bloomberg_anthropic_profitability_ipo_momentum_vs_meta_layoffs_clash_m334_extension_sep21_3pm.py"
OWN_BASENAME = TEST_BASENAME
# The block key follows the m739-style convention: no mechanism_NNN prefix (the
# numeric mechanism_id field carries the ID). Unlike older files, there is no
# underscore-form 772 marker in the corpus at all - designed keying per #715.
MECH_KEY = "bloomberg_anthropic_sep2026_profitability_ipo_momentum_vs_meta_layoffs_partner_clash_m334_temporal_extension_sep21_2026"
M_ID = 772
ITER = 902
TYPE_LETTER = "A"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_772"
NEXT_ID_MARKER = "mechanism" + "_773"
NEXT_ID_NUMERIC = "mechanism_id: 773"
NEXT_ID_DASH = "mechanism" + "-773"
MEMBER_29 = "TWENTY-NINTH falsification-family member"
MEMBER_28 = "TWENTY-EIGHTH falsification-family member"
EXPECTED_ORDER = [("A", "902"), ("E", "901"), ("A", "897"), ("E", "896")]
# Note: ("D", "900"), ("C", "899"), and ("B", "898") are absent from
# EXPECTED_ORDER - the concurrent Type D #900 / Type C #899 / Type B #898
# runs are in-flight (m762/m770/m771 uncommitted in the working tree at this
# run's checks) and commit after this run; see test_window_is_900_904_third_leg.
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "PATCH_ME_IN_FOLLOWUP"

REPO = Path(__file__).resolve().parents[1]


def _read(rel):
    return (REPO / rel).read_text(encoding="utf-8")


def _git(*args):
    return subprocess.run(["git", "-C", str(REPO), *args],
                          capture_output=True, text=True, timeout=60)


def _profiles_text():
    return _read("profiles/competitor-coverage-research.yaml")


def _get_block():
    text = _profiles_text()
    start = text.index(MECH_KEY)
    end = text.index("\nmethodology:")
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

class TestNovelty902:
    def test_single_test_type_a_902_file(self):
        files = [f for f in os.listdir(REPO / "tests")
                 if f.startswith("test_type_a_902")]
        assert files == [OWN_BASENAME]

    def test_type_a_902_main_commit_unique_and_anchored(self):
        # DESELECTED pre-commit (per #565): the commit does not exist yet.
        proc = _git("log", "--format=%H %s", "--grep", "Type A #902")
        mains = [ln for ln in proc.stdout.splitlines()
                 if re.search(r"Type A #902(?::| )", ln)
                 and "anchor followup" not in ln and "log-hash followup" not in ln
                 and "push-status followup" not in ln]
        assert len(mains) == 1
        assert ANCHORED_SHA not in ("PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED",
                                    "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565")
        assert mains[0].startswith(ANCHORED_SHA + " ")

    def test_novelty_verification_claim(self):
        block = _get_block()
        method = block["research_method"]
        assert "4 browser.search query sets this run" in method
        assert "no 'Type A #902' in git log" in method
        assert "block key zero-hit repo-wide pre-commit" in method
        assert "max numeric mechanism id 771 pre-commit" in method
        assert "zero underscore-form 772" in method

    def test_900_901_window_legs_present_prior_to_902(self):
        # #900 Type D is in flight (uncommitted, no log entry); the committed
        # schedule legs must order 901 -> 897 at the log head.
        log = _read("iteration-log.md")
        assert "## #901 Type E:" in log
        assert "## #897 Type A:" in log
        idx_901 = log.index("## #901 Type E:")
        idx_897 = log.index("## #897 Type A:")
        assert idx_901 < idx_897

    def test_max_numeric_mechanism_id_772(self):
        """Max numeric mechanism_id in profiles/ is 772: this run's own
        addition (771 was the max pre-commit per the run's pre-commit grep;
        the concurrent m762/m770/m771 blocks stay uncommitted in the working
        tree and are all below 772)."""
        ids = _corpus_ids()
        assert max(ids) == 772, f"max mechanism_id should be 772, got {max(ids)}"
        assert ids.count(772) == 1, "mechanism_id 772 must appear exactly once"

    def test_no_underscore_773_keys(self):
        """Zero underscore-form 773 mechanism key strings repo-wide
        (format-built needle; __pycache__ excluded per #715)."""
        hits = _repo_grep(NEXT_ID_MARKER)
        assert hits == [], f"unexpected underscore-773 keys: {hits}"

    def test_no_dash_773_keys(self):
        hits = _repo_grep(NEXT_ID_DASH)
        assert hits == [], f"unexpected dash-773 keys: {hits}"

    def test_no_numeric_773_keys(self):
        hits = _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",))
        assert hits == [], f"unexpected numeric 773 keys: {hits}"


# ---------------------------------------------------------------------------
# 2. Rotation guard: 900-904 window, third leg D->E->A
#    (All rotation-guard tests DESELECTED pre-commit per #565.)
# ---------------------------------------------------------------------------

class TestRotationGuard902:
    def test_window_is_900_904_third_leg(self):
        # The concurrent Type D #900 / Type C #899 / Type B #898 runs commit
        # after this run; their main commits are absent from git history.
        # Match only commit SUBJECTS: other commits' bodies may mention #900
        # (this run's own concurrency note does). Iteration numbers follow
        # the rotation schedule, not commit order, so the subject sequence
        # must read 902 -> 901 -> 897 -> 896 with the in-flight legs skipped.
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
        assert nums[:4] == ["902", "901", "897", "896"], nums[:4]
        assert "900" not in nums
        assert "899" not in nums
        assert "898" not in nums

    def test_rotation_adjacency_cycle_valid(self):
        cycle = ["D", "E", "A", "B", "C"]
        got = [t for t, _n in EXPECTED_ORDER]
        assert got == ["A", "E", "A", "E"]
        assert cycle[cycle.index("D") + 1] == "E"
        assert cycle[cycle.index("E") + 1] == "A"
        assert cycle[cycle.index("A") + 1] == "B"
        assert cycle[cycle.index("B") + 1] == "C"

    def test_predecessor_is_type_e_901(self):
        proc = _git("log", "--oneline", "--grep", "Type E #901", "--all")
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

class TestNoveltyAnchor902:
    def test_block_key_shape(self):
        assert MECH_KEY.startswith("bloomberg_")
        assert "anthropic_sep2026_profitability_ipo_momentum" in MECH_KEY
        assert "vs_meta_layoffs_partner_clash" in MECH_KEY
        assert "m334_temporal_extension" in MECH_KEY
        assert MECH_KEY.endswith("sep21_2026")
        # No mechanism_NNN prefix: m739-style keying; the numeric
        # mechanism_id field carries the ID instead (designed keying per #715).


# ---------------------------------------------------------------------------
# 4. Mechanism 772 YAML structure
# ---------------------------------------------------------------------------

class TestMechanism772Structure:
    def test_block_key_unique_in_yaml(self):
        assert _profiles_text().count(MECH_KEY) == 1

    def test_iteration_and_type(self):
        block = _get_block()
        assert block["iteration"] == 902
        assert block["rotation_type"] == "A"
        assert block["mechanism_id"] == 772
        assert block["discovery_date"] == "2026-09-21"

    def test_pair_and_publication(self):
        block = _get_block()
        assert block["publication"] == "Bloomberg"
        assert block["competitor"] == "Anthropic"
        assert block["comparator_entity"] == "Meta"
        assert block["finding_type"] == "cross_publication_coverage_asymmetry"

    def test_cross_references(self):
        block = _get_block()
        assert block["connects_to"] == [334]

    def test_new_test_file_field(self):
        block = _get_block()
        assert block["test_file"] == "tests/" + TEST_BASENAME


# ---------------------------------------------------------------------------
# 5. Mechanism 772 arms
# ---------------------------------------------------------------------------

class TestMechanism772Arms:
    def test_two_anthropic_arms(self):
        block = _get_block()
        arms = block["anthropic_arms"]
        assert len(arms) == 2
        dates = [a["date"] for a in arms]
        assert dates == ["2026-09-13", "2026-09-19"]

    def test_two_meta_arms(self):
        block = _get_block()
        arms = block["meta_arms"]
        assert len(arms) == 2
        registers = [a["register"] for a in arms]
        assert registers == ["layoffs_cost_burn", "internal_partner_conflict"]

    def test_anthropic_arm_registers(self):
        block = _get_block()
        registers = [a["register"] for a in block["anthropic_arms"]]
        assert registers == ["profitability_momentum_ipo_runway",
                             "growth_momentum_with_caveat"]

    def test_arm_source_routing_documented(self):
        block = _get_block()
        for a in block["anthropic_arms"] + block["meta_arms"]:
            assert "source_routing" in a
            assert "tone_basis" in a
            assert "source_url" in a
            assert a["source_url"].startswith("http")

    def test_anthropic_arms_secondary_attested(self):
        # Bloomberg originals are paywalled; the arms are excerpt-bounded
        # secondaries per #503, and the block says so on each arm.
        block = _get_block()
        for a in block["anthropic_arms"]:
            assert "secondary_attribution" in a

    def test_source_urls_novel_and_verbatim(self):
        block = _get_block()
        urls = [a["source_url"] for a in block["anthropic_arms"] + block["meta_arms"]]
        assert len(urls) == 4
        assert urls[0] == "https://temperature2.com/p/2026-09-14-anthropic-second-profitable-quarter-11-5-billion/"
        assert urls[1] == "https://www.thehindubusinessline.com/info-tech/anthropics-annualised-revenue-to-top-100-billion-in-2026/article71483703.ece/amp/"
        assert urls[2] == "https://news.bloomberglaw.com/california-brief/meta-begins-job-cuts-as-it-shifts-from-metaverse-to-ai-devices"
        assert urls[3] == "https://cryptoaimeta.com/meta-smart-glasses/"


# ---------------------------------------------------------------------------
# 6. Mechanism 772 asymmetry scorer
# ---------------------------------------------------------------------------

class TestMechanism772Scorer:
    def test_manual_illustrative_label(self):
        block = _get_block()
        scorer = block["asymmetry_scorer"]
        assert scorer["tone_basis"].startswith("MANUAL ILLUSTRATIVE")
        assert scorer["p_value"] == "NOT_CALCULATED"
        assert scorer["cohens_d"] == "NOT_CALCULATED"
        assert scorer["ci_95"] == "NOT_CALCULATED"
        assert scorer["is_significant"] is False

    def test_arm_scores_and_avg(self):
        scorer = _get_block()["asymmetry_scorer"]
        assert scorer["anthropic_arm_tones"] == [0.45, 0.35]
        assert scorer["anthropic_arm_avg"] == 0.40
        assert scorer["meta_arm_tones"] == [-0.35, -0.30]
        assert scorer["meta_arm_avg"] == -0.325

    def test_delta_calc(self):
        scorer = _get_block()["asymmetry_scorer"]
        assert scorer["illustrative_delta_anthropic_minus_meta"] == 0.725
        assert scorer["delta_calc"] == (
            "((0.45 + 0.35) / 2) - ((-0.35 + -0.30) / 2) = 0.40 + 0.325 = +0.725")

    def test_no_significance_claim(self):
        block = _get_block()
        assert block["verdict"] == "directionally_supported_not_proven"
        assert "directionally_supported_not_proven" in block["statistical_discipline"]

    def test_engine_not_run(self):
        assert "Engine NOT run" in _get_block()["statistical_discipline"]

    def test_no_analysis_json_update(self):
        block = _get_block()
        assert block["no_analysis_json_update"] is True


# ---------------------------------------------------------------------------
# 7. Qualitative discipline
# ---------------------------------------------------------------------------

class TestMechanism772Discipline:
    def test_confounder_classes_ranked(self):
        block = _get_block()
        confs = block["confounders"]
        counter = block.get("counterevidence", [])
        assert len(counter) == 3, len(counter)
        assert len(confs) == 7, len(confs)
        strengths = [c.split(":")[0] for c in confs]
        assert strengths[:3] == ["STRONG", "STRONG", "STRONG"]
        assert strengths[3:5] == ["MODERATE", "MODERATE"]
        assert strengths[5:] == ["WEAK", "WEAK"]

    def test_strong_confounders_evidence_tier(self):
        block = _get_block()
        strong = [c for c in block["confounders"] if c.startswith("STRONG")]
        joined = " ".join(strong)
        assert "browser.open refused" in joined
        assert "Temporal skew" in joined

    def test_counter_evidence_three(self):
        counter = _get_block().get("counterevidence", [])
        assert len(counter) == 3
        joined = " ".join(counter)
        assert "EXTENDS" in joined
        assert "adversarial Meta capacity" in joined
        assert "caveated" in joined

    def test_research_method_excerpt_bounded(self):
        method = _get_block()["research_method"]
        assert "0 browser.open this turn per developer constraint" in method
        assert "excerpt-bounded" in method
        assert "no canonical URLs constructed" in method

    def test_research_method_rejects_duplicates(self):
        method = _get_block()["research_method"]
        assert "Guardian x OpenAI" in method
        assert "Type A #757/m687" in method
        assert "product-positive register cuts against the Meta-arm selection" in method

    def test_ascii_no_em_dashes(self):
        block = _get_block()
        blob = str(block)
        assert "\u2014" not in blob, "no em dashes"
        assert "\u2013" not in blob, "no en dashes"
        blob.encode("ascii")

    def test_correlation_not_causation(self):
        block = _get_block()
        assert "Correlation is not causation" in block["finding"]
        assert "Hypothesis-generating only" in block["asymmetry_scorer"]["verdict"]

    def test_financial_null_tie_documented(self):
        fin = _get_block()["financial_context"]
        assert "No documented Bloomberg-Anthropic content-licensing deal" in fin["bloomberg_anthropic_content_deal"]
        assert "terminal subscriptions" in fin["bloomberg_revenue_model"]
        assert "NULL-tie financial-model documentation" in fin["prediction"]
        assert "334" in fin["m334_linkage"]


# ---------------------------------------------------------------------------
# 8. Falsification ledger holds at 29
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

    def test_m772_not_a_member_form(self):
        # The block may discuss the ledger in negated terms, but it must not
        # carry any ordinal member-form (29th/28th/30th): those live in
        # news-corp.yaml (29th), journalists.yaml (28th), and the guard only.
        text = _profiles_text()
        block_start = text.index(MECH_KEY)
        block_end = text.index("\nmethodology:")
        block_text = text[block_start:block_end]
        assert "NOT a falsification-family member" in block_text
        assert "TWENTY-NINTH falsification-family member" not in block_text
        assert "TWENTY-EIGHTH falsification-family member" not in block_text
        assert "THIRTIETH falsification-family member" not in block_text

    def test_m334_block_intact(self):
        text = _profiles_text()
        assert "bloomberg_lp_upstream_narrative_originator_meta_settlement_anthropic_ipo" in text
        assert "mechanism_id: 334" in text


# ---------------------------------------------------------------------------
# 9. Doc sync: README + ARCHITECTURE
#    (Counts patched post-collect-only per the #719 convention.)
# ---------------------------------------------------------------------------

class TestDocSync902:
    def test_readme_test_count_gate(self):
        readme = _read("README.md")
        assert "| Tests | 46117 |" in readme
        assert "Across 1226 test files" in readme

    def test_readme_type_a_table_row(self):
        assert TEST_BASENAME in _read("README.md")

    def test_architecture_test_count_gate(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert "46117" in arch and "1226" in arch

    def test_architecture_tree_row(self):
        assert TEST_BASENAME in _read("docs/ARCHITECTURE.md")


# ---------------------------------------------------------------------------
# 10. Iteration log
# ---------------------------------------------------------------------------

class TestIterationLog902:
    def test_log_captures_iteration_902(self):
        head = _read("iteration-log.md")[:4000]
        assert "## #902 Type A:" in head
        assert "15:00 PDT" in head
        assert "m772" in head

    def test_log_states_900_904_window(self):
        assert "900-904" in _read("iteration-log.md")[:4000]

    def test_log_ledger_holds_at_29(self):
        head = _read("iteration-log.md")[:4000]
        assert "ledger holds at 29" in head
        assert "THIRTIETH" in _read("iteration-log.md")[:9000]

    def test_log_extends_334(self):
        head = _read("iteration-log.md")[:4000]
        assert "334" in head

    def test_log_rotation_third_leg(self):
        assert "D->E->A" in _read("iteration-log.md")[:4000]

    def test_log_concurrency_noted(self):
        head = _read("iteration-log.md")[:4000]
        assert "#898" in head or "#899" in head or "#900" in head


# ---------------------------------------------------------------------------
# 11. Supersession and corpus integrity post-#901
# ---------------------------------------------------------------------------

class TestSupersessionAndCorpusPost901:
    def test_max_numeric_id_is_772_not_771(self):
        assert max(_corpus_ids()) == 772, (
            f"max numeric mechanism_id must be 772, got {max(_corpus_ids())}")
        assert _corpus_ids().count(772) == 1

    def test_zero_underscore_773_keys_repo_wide(self):
        assert _repo_grep(NEXT_ID_MARKER) == [], "no underscore-form 773 keys anywhere"

    def test_zero_numeric_773_keys_in_profiles(self):
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == [], (
            "no numeric 773 mechanism keys in the corpus")

    def test_no_second_772_block_key_variant(self):
        assert _profiles_text().count(MECH_KEY) == 1

    def test_d901_zero_underscore_772_profiles_sweep_stays_green(self):
        # m739-style keying: the block key carries no mechanism_NNN prefix
        # (the numeric mechanism_id field carries the ID), so the corpus holds
        # ZERO underscore-form 772 keys by design (#715).
        assert _repo_grep(MECH_ID_MARKER, roots=("profiles",)) == [], (
            "zero underscore-form 772 keys in profiles by designed keying")
