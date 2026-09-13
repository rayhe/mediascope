# Type C #709: OpenAI India Attribution-Deal Economics Layer (mechanism 660)
# FIRST dedicated economics-layer financial-incentive mechanism on the
# Sep 7-8 2026 India attribution deals: Medianama fee-template contrast
# (paid 2023-2025 training-licensing template vs zero-fee-disclosed
# attribution-discovery template), the BCCL internal-use exploration clause
# (archive search, research support, data analysis, translation, back-end
# processes, reader-facing products - unpriced technology-transfer option),
# and the editorial-independence clause (BCCL retains complete editorial
# control; OpenAI no role in coverage/editorial positions). Companion to
# mechanism 609 (deal blitz, iteration 624) and mechanism 657 (ANI v.
# OpenAI litigation leg, #704; Sep 14 2026 Division Bench appeal).
#
# QUALITATIVE structural mapping only. No scorer, no tone scores, no
# p-value, no effect size, no CI. NOT a falsification-family member
# (ledger stays at 22 after #708's TWENTY-SECOND; per #609/#614
# qualitative boundary). No analysis.json update.
#
# 709 = Type C (rotation window 708-712 opens B #708 -> C #709, then D #710,
# E #711, A #712). Anchor patched post-commit per #565 convention.
#
# Research method: 2 browser.search query sets this run (OpenAI publisher
# content licensing deal announced September 2026, since=2026-09-08; BCCL
# Times of India OpenAI ChatGPT content partnership terms payment fee) + 1
# browser.open first-hand read attempt (Medianama BCCL piece; failed
# upstream with an egress tool failure, terminal per turn per developer
# instruction - piece read excerpt-bounded from verbatim search-result
# excerpts per #503). URLs copied verbatim from Full-URL listings; no
# canonical URLs constructed. Novelty pre-commit greps: zero
# test_type_c_709 files, no Type C #709 in git log, zero mechanism_660
# keys in profiles/, max numeric mechanism id 659, all five new source
# URLs zero-hit repo-wide (profiles/, tests/, docs/). No zero-coverage
# claims per iteration-492 rule; bounded absence only. No em dashes;
# ASCII-only.
"""Deselected pre-commit: rotation-guard anchor, novelty anchor, and doc-sync
tests per the #565 followup convention; anchors patched in the followup
commit once the main commit SHA is known."""

import glob
import os
import re
import subprocess

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMPETITOR = os.path.join(REPO, "profiles", "competitor-entities.yaml")
TESTS_DIR = os.path.join(REPO, "tests")
TEST_BASENAME = os.path.basename(__file__)
ITERATION = 709
MECH_KEY = "mechanism_660_openai_india_attribution_deal_economics_layer_sep2026"

# Patched in the followup commit per the #565 convention once the main
# commit SHA is known. Anchor tests are deselected pre-commit.
ANCHORED_SHA = "4fb22bca5308ba7236c3aabf050c9525c507d8f2"


def load_competitor():
    with open(COMPETITOR, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def mech():
    return load_competitor()["entities"]["openai"][MECH_KEY]


def git(*args):
    return subprocess.run(
        ["git", *args],
        cwd=REPO,
        capture_output=True,
        text=True,
        timeout=120,
    )


class TestIterationMetadata709:
    def test_iteration_is_709(self):
        assert mech()["iteration"] == ITERATION

    def test_rotation_is_type_c(self):
        assert mech()["rotation"] == "Type C"

    def test_type_is_financial_incentive_mapping(self):
        assert mech()["type"] == "financial_incentive_mapping"

    def test_type_label(self):
        assert mech()["type_label"] == "Financial Incentive Mapping"

    def test_date_time_job_goal(self):
        m = mech()
        assert m["date_analyzed"] == "2026-09-12"
        assert m["time_pdt"] == "21:00"
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"

    def test_author_kit_with_ray(self):
        assert mech()["author"] == "Kit (with Ray)"

    def test_mechanism_id_660_int(self):
        assert isinstance(mech()["mechanism_id"], int)
        assert mech()["mechanism_id"] == 660

    def test_single_660_mechanism_key(self):
        hits = [k for k in load_competitor()["entities"]["openai"] if k.startswith("mechanism_660")]
        assert hits == [MECH_KEY]


class TestFeeTemplateContrast709:
    def test_verbatim_medianama_fee_text(self):
        txt = mech()["fee_template_contrast"]["verbatim_medianama"]
        assert "no confirmation of a licensing fee, revenue-sharing structure, or contract duration" in txt

    def test_medianama_names_paid_precedents(self):
        txt = mech()["fee_template_contrast"]["verbatim_medianama"]
        for name in ("Associated Press", "Axel Springer", "News Corp"):
            assert name in txt

    def test_medianama_same_model_question_unanswered(self):
        txt = mech()["fee_template_contrast"]["verbatim_medianama"]
        assert "have not stated whether this agreement follows the same model" in txt

    def test_contrast_class_two_templates(self):
        cc = mech()["fee_template_contrast"]["contrast_class"]
        assert "paid training-licensing template" in cc
        assert "zero-fee-disclosed attribution-discovery template" in cc

    def test_contrast_class_axel_springer_tens_of_millions(self):
        cc = mech()["fee_template_contrast"]["contrast_class"]
        assert "tens of millions" in cc

    def test_contrast_class_newscorp_250m(self):
        cc = mech()["fee_template_contrast"]["contrast_class"]
        assert "$250M/5yr" in cc

    def test_caveat_no_fee_not_confirmed(self):
        cav = mech()["fee_template_contrast"]["caveat"]
        assert "not confirmation of no fee" in cav
        assert "unanswered" in cav


class TestInternalUseExploration709:
    def test_verbatim_lists_operations(self):
        txt = mech()["internal_use_exploration"]["verbatim_medianama"]
        for op in ("archive search", "research support", "data analysis", "translation", "back-end processes", "reader-facing products"):
            assert op in txt

    def test_no_timeline_names_terms(self):
        txt = mech()["internal_use_exploration"]["verbatim_medianama"]
        assert "No timeline, product names, or financial terms have been disclosed" in txt

    def test_significance_technology_transfer_option(self):
        sig = mech()["internal_use_exploration"]["significance"]
        assert "technology-transfer option" in sig
        assert "newsroom dependency" in sig

    def test_novelty_first_internal_use_clause(self):
        assert "FIRST documentation" in mech()["internal_use_exploration"]["novelty"]
        assert "India" in mech()["internal_use_exploration"]["novelty"]

    def test_not_in_parent_609(self):
        # The internal-use clause is the delta over mechanism 609; pin the
        # verbatim is captured here, not merely referenced.
        assert "explore how OpenAI" in mech()["internal_use_exploration"]["verbatim_medianama"]


class TestEditorialIndependenceClause709:
    def test_bccL_retains_control(self):
        txt = mech()["editorial_independence_clause"]["verbatim_theoutpost"]
        assert "complete editorial control" in txt

    def test_openai_no_role_in_coverage(self):
        txt = mech()["editorial_independence_clause"]["verbatim_theoutpost"]
        assert "no role in determining coverage or editorial positions" in txt

    def test_newsroom_ai_use_human_oversight(self):
        txt = mech()["editorial_independence_clause"]["verbatim_theoutpost"]
        assert "human oversight" in txt

    def test_significance_carve_out_boundary(self):
        sig = mech()["editorial_independence_clause"]["significance"]
        assert "carve-out" in sig


class TestTradePressFramingAndQuotes709:
    def test_adtribe_narrow_fix(self):
        ad = mech()["trade_press_framing"][0]
        assert ad["surface"] == "adtribe.world"
        assert "narrow fix" in ad["verbatim"]
        assert "publishers have been asking for" in ad["verbatim"]

    def test_adtribe_separates_two_demands(self):
        ad = mech()["trade_press_framing"][0]
        assert "discovery/attribution demand" in ad["significance"]
        assert "training-compensation demand" in ad["significance"]

    def test_mohit_jain_quote_public_trust(self):
        q = mech()["executive_quotes"][0]
        assert "Mohit Jain" in q["speaker"]
        assert "journalism is a public trust" in q["text"]

    def test_mohit_jain_quote_source_context_identity(self):
        q = mech()["executive_quotes"][0]
        assert "preserving the source, context, and identity of the original reporting" in q["text"]

    def test_varun_shetty_quote_attribution_links(self):
        q = mech()["executive_quotes"][1]
        assert "Varun Shetty" in q["speaker"]
        assert "clear attribution and direct links" in q["text"]

    def test_varun_shetty_quote_editorial_independence(self):
        q = mech()["executive_quotes"][1]
        assert "respecting editorial independence" in q["text"]


class TestNewDealSweep709:
    def test_sweep_query_since_filter(self):
        sw = mech()["new_deal_sweep_sep8_sep12"]
        assert "since=2026-09-08" in sw["query"]

    def test_zero_new_deals(self):
        sw = mech()["new_deal_sweep_sep8_sep12"]
        assert "ZERO new AI publisher licensing deals announced Sep 8-12 2026" in sw["result"]

    def test_reindex_examples_named(self):
        res = mech()["new_deal_sweep_sep8_sep12"]["result"]
        for deal in ("Hearst Oct 2024", "Atlantic/Vox May 2024", "News Corp May 2024", "Axel Springer Dec 2023"):
            assert deal in res

    def test_bounded_absence_rule(self):
        sw = mech()["new_deal_sweep_sep8_sep12"]
        assert "iteration-492" in sw["rule"]
        assert "no zero-coverage claim" in sw["rule"]

    def test_corpus_invariant_fourweekmba_shared(self):
        res = mech()["new_deal_sweep_sep8_sep12"]["result"]
        assert "FourWeekMBA" in res
        assert "shared with mechanism 609" in res


class TestStatisticalDiscipline709:
    def test_scope_qualitative(self):
        assert "qualitative" in mech()["statistical_discipline"]["scope"]

    def test_correlation_not_causation(self):
        assert mech()["statistical_discipline"]["correlation_not_causation"] is True

    def test_p_value_not_calculated(self):
        assert mech()["statistical_discipline"]["p_value"] == "NOT_CALCULATED"

    def test_is_significant_false(self):
        assert mech()["statistical_discipline"]["is_significant"] is False

    def test_tone_scores_not_scored(self):
        assert mech()["statistical_discipline"]["tone_scores"] == "NOT_SCORED"

    def test_not_falsification_family_member(self):
        assert "NOT a member" in mech()["falsification_family"]

    def test_ledger_stays_22(self):
        ff = mech()["falsification_family"]
        assert "ledger stays at 22" in ff
        assert "TWENTY-SECOND" in ff
        assert "#609/#614 qualitative boundary" in ff


class TestConfounderRanking709:
    def test_five_confounders_ranked(self):
        conf = mech()["ranked_confounders"]
        assert len(conf) == 5
        assert [c["rank"] for c in conf] == [1, 2, 3, 4, 5]

    def test_strong_1_excerpt_bounded(self):
        c = mech()["ranked_confounders"][0]
        assert c["strength"] == "strong"
        assert "excerpt-bounded" in c["confounder"]
        assert "#503" in c["confounder"]

    def test_strong_2_fee_undisclosed_overclaim(self):
        c = mech()["ranked_confounders"][1]
        assert c["strength"] == "strong"
        assert "overclaim" in c["confounder"]

    def test_moderate_3_surface_mismatch(self):
        c = mech()["ranked_confounders"][2]
        assert c["strength"] == "moderate"
        assert "training-data licences" in c["confounder"]

    def test_moderate_4_evidence_grade(self):
        c = mech()["ranked_confounders"][3]
        assert c["strength"] == "moderate"
        assert "Storyboard18" in c["confounder"]

    def test_weak_5_bccl_only(self):
        c = mech()["ranked_confounders"][4]
        assert c["strength"] == "weak"
        assert "BCCL-only" in c["confounder"]


class TestNoveltyAndSources709:
    def test_five_sources_all_new_urls(self):
        srcs = mech()["sources"]
        assert len(srcs) == 5
        for u in (
            "medianama.com/2026/09/223-bccl-openai-content-partnership-toi",
            "storyboard18.com/brand-marketing/bccl-openai-partner",
            "mediabrief.com/bccl-openai-partner-on-journalism-discovery",
            "adtribe.world/bccl-and-openai-sign-partnership",
            "theoutpost.ai/news-story/bccl-partners-with-open-ai",
        ):
            assert any(u in s for s in srcs), u

    def test_sources_verbatim_full_urls(self):
        srcs = mech()["sources"]
        assert srcs[0] == "https://www.medianama.com/2026/09/223-bccl-openai-content-partnership-toi/"
        assert srcs[1] == "https://www.storyboard18.com/brand-marketing/bccl-openai-partner-to-expand-journalism-discovery-via-chatgpt-ws-l-109959.htm"

    def test_fourweekmba_not_in_sources(self):
        srcs = mech()["sources"]
        assert not any("fourweekmba" in s for s in srcs)

    def test_novelty_first_economics_layer(self):
        assert "FIRST dedicated economics-layer" in mech()["novelty"]

    def test_novelty_zero_660_precommit(self):
        assert "Zero mechanism_660 keys repo-wide pre-commit" in mech()["novelty"]

    def test_counterparties_both_legs(self):
        cps = mech()["counterparties"]
        assert len(cps) == 2
        assert any("BCCL" in c and "Sep 7" in c for c in cps)
        assert any("Indian Express Group" in c and "Sep 8" in c for c in cps)


class TestRotationCycleGuard709:
    """Deselected pre-commit for the anchor test; anchor patched in followup."""

    WINDOW = {708: "B", 709: "C", 710: "D", 711: "E", 712: "A"}
    ANCHORED_SHA = ANCHORED_SHA

    def test_window_708_712_opens_b(self):
        assert self.WINDOW[708] == "B"
        assert self.WINDOW[709] == "C"

    def test_rotation_order_cyclic(self):
        order = ["A", "B", "C", "D", "E"]
        for it, typ in self.WINDOW.items():
            assert typ in order
        assert order[(order.index(self.WINDOW[708]) + 1) % 5] == self.WINDOW[709]
        assert self.WINDOW[710] == "D" and self.WINDOW[711] == "E" and self.WINDOW[712] == "A"

    def test_708_committed_in_git_log(self):
        out = git("log", "--oneline", "--grep", "Type B #708")
        assert out.stdout.strip() != "", "missing committed iteration #708"

    def test_anchor_is_main_commit_709(self):
        # Per #565 convention the anchor is patched to the #709 main commit
        # in the followup; verify the patch landed.
        assert git("cat-file", "-e", f"{self.ANCHORED_SHA}^{{commit}}").returncode == 0
        msg = git("log", "-1", "--format=%s", self.ANCHORED_SHA).stdout.strip()
        assert "Type C #709" in msg

    def test_iteration_log_entry_regex_self_check(self):
        sample = "#709 Type C: OpenAI India attribution-deal economics layer"
        assert re.match(r"^#709 Type C:", sample)


class TestDocSyncRatchet709:
    README = os.path.join(REPO, "README.md")
    ARCH = os.path.join(REPO, "docs", "ARCHITECTURE.md")
    LOG = os.path.join(REPO, "iteration-log.md")

    def test_readme_has_709_row(self):
        text = open(self.README, encoding="utf-8").read()
        assert TEST_BASENAME in text

    def test_architecture_has_709_tree_row(self):
        text = open(self.ARCH, encoding="utf-8").read()
        assert TEST_BASENAME in text

    def test_iteration_log_top_entry_709(self):
        text = open(self.LOG, encoding="utf-8").read()
        assert text.lstrip().startswith("#709 Type C:")

    def test_readme_row_mentions_fee_template(self):
        text = open(self.README, encoding="utf-8").read()
        seg = text[text.index(TEST_BASENAME):]
        seg = seg[:5000]
        assert "fee" in seg.lower() and "internal-use" in seg

    def test_doc_count_stats_sync(self):
        readme = open(self.README, encoding="utf-8").read()
        assert "| Tests | 37351 | Across 1037 test files |" in readme
        assert "MediaScope has **37351 tests** across 1037 test files" in readme
        arch = open(self.ARCH, encoding="utf-8").read()
        assert "# 37351 tests across 1037 test files" in arch
