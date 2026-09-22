"""Type A #907 (905-909 window, third leg D->E->A): Bloomberg x OpenAI
Sep-2026 financial-momentum register vs Bloomberg x Meta product-momentum
register (mechanism id 775).

Genre-matched financial/product-momentum control complementing m772 (Type A
#902, delta +0.725 Anthropic-vs-Meta, story-type-mismatched). Once story
genres are matched, Bloomberg's OpenAI and Meta coverage sits near parity
and positive on both sides: OpenAI arms Sep 16 2026 Bloomberg $1.2T
funding-talks scoop (mirror-attested, byline "By Bloomberg") and the
Bloomberg Law $852B/$122B closed-round piece (first-hand, paywall-truncated,
date not visible in fetched excerpt); Meta arms Bloomberg Law Muse AI-agent
chip-stock rally piece ("soared Monday", date inferred Sep 21 2026) and the
Sep 15 2026 Bloomberg-routed MTIA 450/500 roadmap story (TheFly relay via
Let's Data Science, explicitly caveated as plans not benchmarks).
MANUAL ILLUSTRATIVE tones: OpenAI +0.35/+0.30 (avg +0.325), Meta
+0.45/+0.25 (avg +0.35); illustrative delta (OpenAI minus Meta) -0.025.
The real asymmetry scorer was run once on the two illustrative arm arrays
(asymmetry -0.025, t=-0.2425, p=0.8450, d=-0.2425, 95% CI (-0.15, 0.10),
engine is_significant False) as a corroborating observation - NOT promoted
to a finding. NULL gradient: weakens entity-specific readings of m772's
spread; the register split tracks story type (desk-routing confound).
Zero-payer control case: no mapped Bloomberg-OpenAI or Bloomberg-Meta
content-licensing deal (bounded absence); NOT evidence financial
relationships cause tone; NOT a falsification-family member; ledger holds
at 29; THIRTIETH remains the negative guard. MANUAL ILLUSTRATIVE scores
only; p_value/cohens_d/ci_95 NOT_CALCULATED at the finding layer;
is_significant false (Aug 28 2026 standing rule); verdict
directionally_supported_not_proven; no analysis.json update; NOT
artifact-grade; correlation is not causation. Novelty verified pre-commit
(zero test_type_a_907 files; no 'Type A #907' in git log; block key
zero-hit repo-wide; max numeric mechanism id 774 pre-commit; zero
underscore-form 775 keys by designed keying per #715; zero dash-form 775
refs; zero numeric 775 keys in profiles/; all 4 arm URL slugs zero-hit
pre-commit; dead-end candidates rejected: Verge/Google glasses pair -
insufficient novelty per #492/#592/#677/#657; teen-social-media-harm
Bloomberg route - 3 corpus hits); 905-909 window THIRD leg D->E->A
(anchor patched post-commit per #565) - Sep 21 2026 21:00 PDT.
"""

import os
import re
import subprocess
from pathlib import Path

import pytest
import yaml

TEST_BASENAME = "test_type_a_907_bloomberg_openai_vs_meta_financial_product_momentum_genre_matched_null_gradient_sep21_9pm.py"
OWN_BASENAME = TEST_BASENAME
# The block key follows the m739-style convention: no mechanism_NNN prefix (the
# numeric mechanism_id field carries the ID). Unlike older files, there is no
# underscore-form 775 marker in the corpus at all - designed keying per #715.
MECH_KEY = "bloomberg_openai_vs_meta_financial_product_momentum_genre_matched_null_gradient_sep21_2026"
M_ID = 775
ITER = 907
TYPE_LETTER = "A"
# Concatenated so this file never contains the literal marker itself.
MECH_ID_MARKER = "mechanism" + "_775"
NEXT_ID_MARKER = "mechanism" + "_776"
NEXT_ID_NUMERIC = "mechanism_id: 776"
NEXT_ID_DASH = "mechanism" + "-776"
MEMBER_29 = "TWENTY-NINTH falsification-family member"
MEMBER_28 = "TWENTY-EIGHTH falsification-family member"
EXPECTED_ORDER = [("A", "907"), ("E", "906"), ("D", "905"), ("C", "904")]
# Note: ("D", "900"), ("C", "899"), and ("B", "898") are absent from
# EXPECTED_ORDER - the concurrent Type D #900 / Type C #899 / Type B #898
# runs are in-flight (m762/m770/m771 uncommitted in the working tree at this
# run's checks) and commit after this run; see test_window_is_905_909_third_leg.
# Patched to the real main-commit SHA in the anchor followup per the #565 convention.
ANCHORED_SHA = "cc81f0a6bc181f4767e9acd60455cfdc2db69051"

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

class TestNovelty907:
    def test_single_test_type_a_907_file(self):
        files = [f for f in os.listdir(REPO / "tests")
                 if f.startswith("test_type_a_907")]
        assert files == [OWN_BASENAME]

    def test_type_a_907_main_commit_unique_and_anchored(self):
        # DESELECTED pre-commit (per #565): the commit does not exist yet.
        proc = _git("log", "--format=%H %s", "--grep", "Type A #907")
        mains = [ln for ln in proc.stdout.splitlines()
                 if re.search(r"Type A #907(?::| )", ln)
                 and "anchor followup" not in ln and "log-hash followup" not in ln
                 and "push-status followup" not in ln]
        assert len(mains) == 1
        assert ANCHORED_SHA not in ("PATCH_ME_IN_FOLLOWUP", "POST_COMMIT_ANCHORED",
                                    "PLACEHOLDER_PATCHED_POST_COMMIT_PER_565")
        assert mains[0].startswith(ANCHORED_SHA + " ")

    def test_novelty_verification_claim(self):
        block = _get_block()
        method = block["research_method"]
        assert "4 browser.open first-hand reads this run" in method
        assert "no 'Type A #907' in git log" in method
        assert "block key zero-hit repo-wide pre-commit" in method
        assert "max numeric mechanism id 774 pre-commit" in method
        assert "zero underscore-form 775" in method

    def test_906_905_904_window_legs_present_prior_to_907(self):
        # #900 Type D is in flight (uncommitted, no log entry); the committed
        # schedule legs must order 906 -> 905 -> 904 at the log head.
        log = _read("iteration-log.md")
        assert "## #906 Type E:" in log
        assert "## #905 Type D:" in log
        assert "## #904 Type C:" in log
        idx_906 = log.index("## #906 Type E:")
        idx_905 = log.index("## #905 Type D:")
        idx_904 = log.index("## #904 Type C:")
        assert idx_906 < idx_905 < idx_904

    def test_max_numeric_mechanism_id_775(self):
        """Max numeric mechanism_id in profiles/ is 775: this run's own
        addition (774 was the max pre-commit per the run's pre-commit grep;
        the concurrent m762/m770/m771 blocks stay uncommitted in the working
        tree and are all below 775)."""
        ids = _corpus_ids()
        assert max(ids) == 775, f"max mechanism_id should be 775, got {max(ids)}"
        assert ids.count(775) == 1, "mechanism_id 775 must appear exactly once"

    def test_no_underscore_776_keys(self):
        """Zero underscore-form 776 mechanism key strings repo-wide
        (format-built needle; __pycache__ excluded per #715)."""
        hits = _repo_grep(NEXT_ID_MARKER)
        assert hits == [], f"unexpected underscore-776 keys: {hits}"

    def test_no_dash_776_keys(self):
        hits = _repo_grep(NEXT_ID_DASH)
        assert hits == [], f"unexpected dash-776 keys: {hits}"

    def test_no_numeric_776_keys(self):
        hits = _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",))
        assert hits == [], f"unexpected numeric 776 keys: {hits}"


# ---------------------------------------------------------------------------
# 2. Rotation guard: 905-909 window, third leg D->E->A
#    (All rotation-guard tests DESELECTED pre-commit per #565.)
# ---------------------------------------------------------------------------

class TestRotationGuard907:
    def test_window_is_905_909_third_leg(self):
        # The concurrent Type D #900 / Type C #899 / Type B #898 runs commit
        # after this run; their main commits are absent from git history.
        # Match only commit SUBJECTS: other commits' bodies may mention #900
        # (this run's own concurrency note does). Iteration numbers follow
        # the rotation schedule, not commit order, so the subject sequence
        # must read 907 -> 906 -> 905 -> 904 with the in-flight legs skipped.
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
        assert nums[:4] == ["907", "906", "905", "904"], nums[:4]
        assert "900" not in nums
        assert "899" not in nums
        assert "898" not in nums

    def test_rotation_adjacency_cycle_valid(self):
        cycle = ["D", "E", "A", "B", "C"]
        got = [t for t, _n in EXPECTED_ORDER]
        assert got == ["A", "E", "D", "C"]
        assert cycle[cycle.index("D") + 1] == "E"
        assert cycle[cycle.index("E") + 1] == "A"
        assert cycle[cycle.index("A") + 1] == "B"
        assert cycle[cycle.index("B") + 1] == "C"

    def test_predecessor_is_type_e_906(self):
        proc = _git("log", "--oneline", "--grep", "Type E #906", "--all")
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

class TestNoveltyAnchor907:
    def test_block_key_shape(self):
        assert MECH_KEY.startswith("bloomberg_")
        assert "openai_vs_meta" in MECH_KEY
        assert "financial_product_momentum" in MECH_KEY
        assert "genre_matched_null_gradient" in MECH_KEY
        assert MECH_KEY.endswith("sep21_2026")
        # No mechanism_NNN prefix: m739-style keying; the numeric
        # mechanism_id field carries the ID instead (designed keying per #715).


# ---------------------------------------------------------------------------
# 4. Mechanism 775 YAML structure
# ---------------------------------------------------------------------------

class TestMechanism775Structure:
    def test_block_key_unique_in_yaml(self):
        assert _profiles_text().count(MECH_KEY) == 1

    def test_iteration_and_type(self):
        block = _get_block()
        assert block["iteration"] == 907
        assert block["rotation_type"] == "A"
        assert block["mechanism_id"] == 775
        assert block["discovery_date"] == "2026-09-21"

    def test_pair_and_publication(self):
        block = _get_block()
        assert block["publication"] == "Bloomberg"
        assert block["competitor"] == "OpenAI"
        assert block["comparator_entity"] == "Meta"
        assert block["finding_type"] == "cross_publication_coverage_asymmetry"

    def test_cross_references(self):
        block = _get_block()
        assert block["connects_to"] == [772, 334]

    def test_new_test_file_field(self):
        block = _get_block()
        assert block["test_file"] == "tests/" + TEST_BASENAME


# ---------------------------------------------------------------------------
# 5. Mechanism 775 arms
# ---------------------------------------------------------------------------

class TestMechanism775Arms:
    def test_two_openai_arms(self):
        block = _get_block()
        arms = block["openai_arms"]
        assert len(arms) == 2
        registers = [a["register"] for a in arms]
        assert registers == ["financing_momentum_ipo_optionality",
                             "financing_momentum_closed_round"]

    def test_two_meta_arms(self):
        block = _get_block()
        arms = block["meta_arms"]
        assert len(arms) == 2
        registers = [a["register"] for a in arms]
        assert registers == ["product_momentum_market_rally",
                             "product_roadmap_forward_momentum"]

    def test_arm_source_routing_documented(self):
        block = _get_block()
        for a in block["openai_arms"] + block["meta_arms"]:
            assert "source_routing" in a
            assert "tone_basis" in a
            assert "source_url" in a
            assert a["source_url"].startswith("http")

    def test_openai_852b_arm_date_caveat(self):
        # The Bloomberg Law $852B/$122B piece was fetched first-hand but the
        # publication date was not visible in the excerpt - the block must
        # carry the date caveat explicitly rather than asserting a date.
        block = _get_block()
        arm = [a for a in block["openai_arms"]
               if a["source_url"].endswith(
                   "openai-valued-at-852-billion-after-closing-122-billion-round")][0]
        assert arm["date"] == "date_not_visible_in_fetched_excerpt"
        assert "date_caveat" in arm

    def test_meta_muse_arm_date_inferred(self):
        # The Muse chip-rally piece says "soared Monday"; the block labels
        # the Sep 21 2026 date as inferred, not verified.
        block = _get_block()
        arm = [a for a in block["meta_arms"]
               if "muse-ai-agent-spurs" in a["source_url"]][0]
        assert "inferred" in arm["date_basis"]

    def test_source_urls_novel_and_verbatim(self):
        block = _get_block()
        urls = [a["source_url"] for a in block["openai_arms"] + block["meta_arms"]]
        assert len(urls) == 4
        assert urls[0] == "https://www.thehindubusinessline.com/info-tech/openai-weighing-funding-round-at-over-12-trillion-valuation/article71470879.ece/amp/"
        assert urls[1] == "https://news.bloomberglaw.com/tech-and-telecom-law/openai-valued-at-852-billion-after-closing-122-billion-round"
        assert urls[2] == "https://news.bloomberglaw.com/international-trade/amd-intel-soar-as-metas-muse-ai-agent-spurs-chip-stock-rally"
        assert urls[3] == "https://letsdatascience.com/news/meta-schedules-arke-and-astrid-data-center-deployments-4bdafdec"

    def test_mtia_arm_bloomberg_attribution_verified(self):
        block = _get_block()
        arm = [a for a in block["meta_arms"]
               if "arke-and-astrid" in a["source_url"]][0]
        assert "Bloomberg" in arm["secondary_attribution"]
        assert "TheFly" in arm["secondary_attribution"]


# ---------------------------------------------------------------------------
# 6. Mechanism 775 asymmetry scorer
# ---------------------------------------------------------------------------

class TestMechanism775Scorer:
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
        assert scorer["openai_arm_tones"] == [0.35, 0.30]
        assert scorer["openai_arm_avg"] == 0.325
        assert scorer["meta_arm_tones"] == [0.45, 0.25]
        assert scorer["meta_arm_avg"] == 0.35

    def test_delta_calc(self):
        scorer = _get_block()["asymmetry_scorer"]
        assert scorer["illustrative_delta_openai_minus_meta"] == -0.025
        assert scorer["delta_calc"] == (
            "((0.35 + 0.30) / 2) - ((0.45 + 0.25) / 2) = 0.325 - 0.35 = -0.025")

    def test_engine_run_recorded_as_corroboration(self):
        # The real scorer was run once on the two illustrative arm arrays;
        # the engine output is recorded as a corroborating observation and
        # must NOT be promoted to a finding.
        engine = _get_block()["asymmetry_scorer"]["engine_run"]
        assert engine["target_scores"] == [0.35, 0.30]
        assert engine["peer_scores"] == [0.45, 0.25]
        assert engine["asymmetry_score"] == -0.025
        assert engine["t_statistic"] == -0.2425
        assert engine["p_value"] == 0.845
        assert engine["cohens_d"] == -0.2425
        assert engine["ci_95"] == [-0.15, 0.10]
        assert engine["engine_is_significant"] is False
        assert "NOT promoted to a finding" in engine["role"]

    def test_no_significance_claim(self):
        block = _get_block()
        assert block["verdict"] == "directionally_supported_not_proven"
        assert "directionally_supported_not_proven" in block["statistical_discipline"]

    def test_no_analysis_json_update(self):
        block = _get_block()
        assert block["no_analysis_json_update"] is True

    def test_null_gradient_weaks_m772_reading(self):
        scorer = _get_block()["asymmetry_scorer"]
        assert abs(scorer["illustrative_delta_openai_minus_meta"]) < 0.05
        assert "near parity" in scorer["delta_interpretation"]


# ---------------------------------------------------------------------------
# 7. Qualitative discipline
# ---------------------------------------------------------------------------

class TestMechanism775Discipline:
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
        assert "n=2 per arm" in joined
        assert "no verified publication date" in joined
        assert "INFERRED" in joined

    def test_counter_evidence_three(self):
        counter = _get_block().get("counterevidence", [])
        assert len(counter) == 3
        joined = " ".join(counter)
        assert "weakens" in joined
        assert "m772" in joined
        assert "ceiling reading" in joined

    def test_research_method_firsthand_reads(self):
        method = _get_block()["research_method"]
        assert "4 browser.open first-hand reads this run" in method
        assert "Verge/Google camera-glasses pair rejected" in method
        assert "teen-social-media-harm" in method
        assert "no canonical URLs constructed" in method

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

    def test_financial_zero_payer_control_documented(self):
        fin = _get_block()["financial_context"]
        assert "No documented Bloomberg-OpenAI content-licensing deal" in fin["bloomberg_openai_content_deal"]
        assert "No documented Bloomberg-Meta content-licensing deal" in fin["bloomberg_meta_content_deal"]
        assert "terminal subscriptions" in fin["bloomberg_revenue_model"]
        assert "Zero-payer control" in fin["prediction"]
        assert "NOT evidence that financial relationships cause tone" in fin["prediction"]
        assert "772" in fin["m772_linkage"]
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

    def test_m775_not_a_member_form(self):
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

    def test_m772_block_intact(self):
        text = _profiles_text()
        assert "bloomberg_anthropic_sep2026_profitability_ipo_momentum_vs_meta_layoffs_partner_clash_m334_temporal_extension_sep21_2026" in text
        assert "mechanism_id: 772" in text


# ---------------------------------------------------------------------------
# 9. Doc sync: README + ARCHITECTURE
#    (Counts patched post-collect-only per the #719 convention.)
# ---------------------------------------------------------------------------

class TestDocSync907:
    def test_readme_test_count_gate(self):
        readme = _read("README.md")
        assert "| Tests | 46472 |" in readme
        assert "Across 1232 test files" in readme

    def test_readme_type_a_table_row(self):
        assert TEST_BASENAME in _read("README.md")

    def test_architecture_test_count_gate(self):
        arch = _read("docs/ARCHITECTURE.md")
        assert "46472" in arch and "1232" in arch

    def test_architecture_tree_row(self):
        assert TEST_BASENAME in _read("docs/ARCHITECTURE.md")


# ---------------------------------------------------------------------------
# 10. Iteration log
# ---------------------------------------------------------------------------

class TestIterationLog907:
    def test_log_captures_iteration_907(self):
        head = _read("iteration-log.md")[:4000]
        assert "## #907 Type A:" in head
        assert "21:00 PDT" in head
        assert "m775" in head

    def test_log_states_905_909_window(self):
        assert "905-909" in _read("iteration-log.md")[:4000]

    def test_log_ledger_holds_at_29(self):
        head = _read("iteration-log.md")[:4000]
        assert "ledger holds at 29" in head
        assert "THIRTIETH" in _read("iteration-log.md")[:9000]

    def test_log_connects_772_334(self):
        head = _read("iteration-log.md")[:4000]
        assert "772" in head
        assert "334" in head

    def test_log_rotation_third_leg(self):
        assert "D->E->A" in _read("iteration-log.md")[:4000]

    def test_log_concurrency_noted(self):
        head = _read("iteration-log.md")[:4000]
        assert "#898" in head or "#899" in head or "#900" in head


# ---------------------------------------------------------------------------
# 11. Supersession and corpus integrity post-#906
# ---------------------------------------------------------------------------

class TestSupersessionAndCorpusPost906:
    def test_max_numeric_id_is_775_not_774(self):
        assert max(_corpus_ids()) == 775, (
            f"max numeric mechanism_id must be 775, got {max(_corpus_ids())}")
        assert _corpus_ids().count(775) == 1

    def test_zero_underscore_776_keys_repo_wide(self):
        assert _repo_grep(NEXT_ID_MARKER) == [], "no underscore-form 776 keys anywhere"

    def test_zero_numeric_776_keys_in_profiles(self):
        assert _repo_grep(NEXT_ID_NUMERIC, roots=("profiles",)) == [], (
            "no numeric 776 mechanism keys in the corpus")

    def test_no_second_775_block_key_variant(self):
        assert _profiles_text().count(MECH_KEY) == 1

    def test_zero_underscore_775_profiles_sweep_stays_green(self):
        # m739-style keying: the block key carries no mechanism_NNN prefix
        # (the numeric mechanism_id field carries the ID), so the corpus holds
        # ZERO underscore-form 775 keys by design (#715).
        assert _repo_grep(MECH_ID_MARKER, roots=("profiles",)) == [], (
            "zero underscore-form 775 keys in profiles by designed keying")
