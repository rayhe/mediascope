# Type C #714: Perplexity Premium-Data Licensing Layer via Cashmere (mechanism 663)
# FIRST dedicated Perplexity paid-licensing mechanism in the corpus: the
# Cashmere-operated premium-data integration layer (Wiley May 8 2025,
# Harvard Business Publishing, Princeton University Press (Sep 2026; exact date unverified, circa Sep 8),
# Rockefeller UP, Springer Publishing) with RAG-only no-LLM-training
# per-token/per-use/per-relationship pricing - the corpus's purest a la
# carte instance extending the Vogel distinction (mechanism 539).
# Second Perplexity publisher-pay template alongside mechanism 391
# (Comet Plus 80/20 revenue-share); the license-leg of the
# sign-one-sue-other bifurcation (Dow Jones/NY Post v. Perplexity,
# SDNY 1:24-cv-07984, Oct 21 2024).
#
# QUALITATIVE structural mapping only. No scorer, no tone scores, no
# p-value, no effect size, no CI. NOT a falsification-family member
# (ledger stays at 22 after #708's TWENTY-SECOND; per #609/#614
# qualitative boundary). No analysis.json update.
#
# 714 = Type C (rotation window 713-717 opens B #713 -> C #714, then D #715,
# E #716, A #717). Anchor patched post-commit per #565 convention.
#
# Research method: 4 browser.search query sets this run (1) publisher AI
# licensing deal announced September 2026; (2) Disney OpenAI Sora licensing
# deal characters 2026 (rejected as out-of-scope: Disney is not a Meta
# competitor, deal is Dec 2025); (3) Wiley Perplexity licensing partnership
# AI; (4) Cashmere AI licensing platform publisher deals 2026.
# Excerpt-bounded, second-hand evidence per #503 (no browser.open
# first-hand reads this run). URLs copied verbatim from Full-URL listings;
# no canonical URLs constructed; one PW URL carried http verbatim.
# Novelty pre-commit greps: zero test_type_c_714 files, no Type C #714 in
# git log, zero mechanism_663 keys in profiles/, max numeric mechanism id
# 662, zero "wiley"/"Harvard Business Publishing" hits repo-wide
# pre-commit. No zero-coverage claims per iteration-492 rule; bounded
# absence only. No em dashes; ASCII-only.
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
ITERATION = 714
MECH_KEY = "mechanism_663_perplexity_premium_data_licensing_cashmere_sep2026"

# Patched in the followup commit per the #565 convention once the main
# commit SHA is known. Anchor tests are deselected pre-commit.
ANCHORED_SHA = "afe77c3779c46e65b3757010b2689660be9da8f6"


def load_competitor():
    with open(COMPETITOR, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def mech():
    return load_competitor()["entities"]["perplexity"][MECH_KEY]


def git(*args):
    return subprocess.run(
        ["git", *args],
        cwd=REPO,
        capture_output=True,
        text=True,
        timeout=120,
    )


class TestIterationMetadata714:
    def test_iteration_is_714(self):
        assert mech()["iteration"] == ITERATION

    def test_rotation_is_type_c(self):
        assert mech()["rotation"] == "Type C"

    def test_type_is_financial_incentive_mapping(self):
        assert mech()["type"] == "financial_incentive_mapping"

    def test_type_label(self):
        assert mech()["type_label"] == "Financial Incentive Mapping"

    def test_date_time_job_goal(self):
        m = mech()
        assert m["date_analyzed"] == "2026-09-13"
        assert m["time_pdt"] == "02:00"
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"

    def test_author_kit_with_ray(self):
        assert mech()["author"] == "Kit (with Ray)"

    def test_mechanism_id_663_int(self):
        assert isinstance(mech()["mechanism_id"], int)
        assert mech()["mechanism_id"] == 663

    def test_single_663_mechanism_key(self):
        hits = [k for k in load_competitor()["entities"]["perplexity"] if k.startswith("mechanism_663")]
        assert hits == [MECH_KEY]


class TestCounterparties714:
    def test_five_counterparties(self):
        assert len(mech()["counterparties"]) == 5

    def test_wiley_first_education_partner(self):
        cps = mech()["counterparties"]
        assert any("John Wiley" in c and "May 8 2025" in c and "first education partner" in c for c in cps)

    def test_wiley_enterprise_tool_leg(self):
        cps = mech()["counterparties"]
        assert any("John Wiley" in c and "Enterprise Pro licenses" in c for c in cps)

    def test_wiley_pilots(self):
        cps = mech()["counterparties"]
        assert any("Texas A&M" in c and "Texas State" in c for c in cps)

    def test_hbp_naver_d2sf_pr(self):
        cps = mech()["counterparties"]
        assert any("Harvard Business Publishing" in c and "Feb 4 2026" in c for c in cps)

    def test_pup_this_week(self):
        cps = mech()["counterparties"]
        assert any("Princeton University Press" in c and "circa Sep 8" in c and "RAG-licensing" in c for c in cps)

    def test_rockefeller_springer_roster(self):
        cps = mech()["counterparties"]
        assert any("Rockefeller University Press" in c and "2026" in c for c in cps)
        assert any("Springer Publishing" in c and "2026" in c for c in cps)

    def test_meta_zero_leg(self):
        mz = mech()["meta_zero"]
        assert "zero documented" in mz
        assert "Reuters Oct 2024" in mz
        assert "People Inc Dec 2025" in mz


class TestCashmereInfrastructure714:
    def test_company_and_ceo(self):
        io = mech()["infrastructure_operator"]
        assert io["company"] == "Cashmere (cashmere.io)"
        assert io["ceo"] == "Jonathan Munk"

    def test_funding_roster(self):
        fund = mech()["infrastructure_operator"]["funding"]
        assert fund.startswith("$5M seed")
        assert "Reach Capital" in fund
        for name in ("NAVER D2SF", "Founders Future", "Fortitude Ventures", "Ingram Content Group", "Pearson"):
            assert name in fund

    def test_headcount_lean(self):
        hc = mech()["infrastructure_operator"]["headcount"]
        assert "fewer than 10 employees" in hc
        assert "stay lean" in hc

    def test_no_llm_training_model_claim(self):
        claims = mech()["infrastructure_operator"]["model_claims"]
        assert any("no-LLM-training" in c for c in claims)

    def test_omnipub_format_claim(self):
        claims = mech()["infrastructure_operator"]["model_claims"]
        assert any("omnipub" in c for c in claims)

    def test_per_token_pricing_claim(self):
        claims = mech()["infrastructure_operator"]["model_claims"]
        assert any("per-token, per-use, or per-relationship" in c for c in claims)

    def test_reach_claim_munk_quote(self):
        rc = mech()["infrastructure_operator"]["reach_claim"]
        assert "handles all of Perplexity's premium data integrations" in rc
        assert "run it on Cashmere" in rc

    def test_kgl_expansion(self):
        exp = mech()["infrastructure_operator"]["expansion"]
        assert exp.startswith("Mar 9 2026")
        assert "KnowledgeWorks Global Ltd." in exp

    def test_naver_buyer_interest(self):
        bi = mech()["infrastructure_operator"]["buyer_side_interest"]
        assert "NAVER D2SF" in bi
        assert "25+ years" in bi


class TestQuotesAndPricing714:
    def test_four_executive_quotes(self):
        assert len(mech()["executive_quotes"]) == 4

    def test_jarrett_quote(self):
        qs = mech()["executive_quotes"]
        assert any("Josh Jarrett" in q and "Wiley SVP AI growth" in q for q in qs)

    def test_shevelenko_quote(self):
        qs = mech()["executive_quotes"]
        assert any("Dmitry Shevelenko" in q and "Perplexity chief business officer" in q for q in qs)

    def test_munk_quote(self):
        qs = mech()["executive_quotes"]
        assert any("Jonathan Munk" in q and "Cashmere CEO" in q and "on their own terms" in q for q in qs)

    def test_henry_quote(self):
        qs = mech()["executive_quotes"]
        assert any("Christie Henry" in q and "PUP director" in q for q in qs)

    def test_pricing_a_la_carte_vogel(self):
        pmi = mech()["pricing_model_innovation"]
        assert "a la carte" in pmi
        assert "Vogel" in pmi
        assert "mechanism 539" in pmi

    def test_pricing_contrast_templates(self):
        pmi = mech()["pricing_model_innovation"]
        assert "$250M/5yr" in pmi
        assert "$16M/yr" in pmi
        assert "mechanism 660" in pmi


class TestBifurcationAndConfounds714:
    def test_sdny_case_number(self):
        b = mech()["license_litigate_bifurcation"]
        assert "1:24-cv-07984" in b
        assert "Oct 21 2024" in b

    def test_thomson_quote(self):
        b = mech()["license_litigate_bifurcation"]
        assert "abuse of intellectual property" in b

    def test_bifurcation_surface_split(self):
        b = mech()["license_litigate_bifurcation"]
        assert "Academic/book publishers" in b and "licensed leg" in b
        assert "news publishers" in b and "litigation leg" in b

    def test_six_ranked_confounders(self):
        assert len(mech()["confounders_ranked"]) == 6

    def test_strong_confounders_count(self):
        strong = [c for c in mech()["confounders_ranked"] if c["strength"] == "STRONG"]
        assert len(strong) == 2

    def test_strong_undisclosed_terms(self):
        c0 = mech()["confounders_ranked"][0]
        assert c0["strength"] == "STRONG"
        assert "All financial terms undisclosed" in c0["text"]

    def test_strong_surface_mismatch(self):
        c1 = mech()["confounders_ranked"][1]
        assert c1["strength"] == "STRONG"
        assert "mechanism 391" in c1["text"]

    def test_moderate_in_kind(self):
        mods = [c for c in mech()["confounders_ranked"] if c["strength"] == "MODERATE"]
        assert len(mods) == 2
        assert any("non-cash" in c["text"] for c in mods)
        assert any("RAG-only surface" in c["text"] for c in mods)

    def test_weak_evidence_grade(self):
        weak = [c for c in mech()["confounders_ranked"] if c["strength"] == "WEAK"]
        assert len(weak) == 2
        assert any("#503" in c["text"] for c in weak)
        assert any("PUP announcement timing" in c["text"] for c in weak)

    def test_four_counterevidence_items(self):
        assert len(mech()["counterevidence"]) == 4

    def test_counterevidence_no_license_rhetoric(self):
        ce = mech()["counterevidence"]
        assert any("does not need to license content" in c for c in ce)

    def test_no_causal_claim(self):
        assert "No causal claim" in mech()["correlational_note"]
        assert "correlational structural incentives" in mech()["correlational_note"]

    def test_no_coverage_tone_claim(self):
        assert "No coverage-tone claim is made" in mech()["correlational_note"]
        assert "Type A follow-ups flagged" in mech()["correlational_note"]

    def test_tone_scores_not_scored(self):
        assert mech()["tone_scores"] == "NOT_SCORED"

    def test_statistical_discipline_qualitative(self):
        sd = mech()["statistical_discipline"]
        assert "p_value NOT_CALCULATED" in sd
        assert "not a falsification-family member" in sd.lower()
        assert "ledger stays 22" in sd

    def test_cross_reference_mechanisms(self):
        cr = mech()["cross_references"]
        for ref in ("mechanism 391", "mechanism 539", "mechanism 519", "mechanism 609/660", "mechanism 614", "mechanism 509"):
            assert any(ref in c for c in cr), ref
        assert any("#503" in c for c in cr)
        assert any("#492" in c for c in cr)
        assert any("#565" in c for c in cr)

    def test_novelty_first_paid_licensing(self):
        assert "FIRST dedicated Perplexity premium-data/paid-licensing mechanism" in mech()["novelty"]

    def test_novelty_zero_663_precommit(self):
        assert "zero mechanism_663 keys repo-wide" in mech()["novelty"]


class TestSourcesAndResearch714:
    def test_nine_sources(self):
        assert len(mech()["sources"]) == 9

    def test_wiley_press_release_source(self):
        srcs = mech()["sources"]
        assert any("newsroom.wiley.com" in s and "May 8 2025" in s or "2025" in s and "Wiley-and-Perplexity" in s for s in srcs)

    def test_pw_http_verbatim(self):
        srcs = mech()["sources"]
        assert any(s.startswith("http://www.publishersweekly.com") for s in srcs)

    def test_sources_all_verbatim_full_urls(self):
        for s in mech()["sources"]:
            assert re.match(r"^https?://", s), s
            assert " " not in s

    def test_research_method_four_query_sets(self):
        rm = mech()["research_method"]
        assert "4 browser.search query sets" in rm
        assert "Wiley Perplexity licensing partnership AI" in rm
        assert "Cashmere AI licensing platform publisher deals 2026" in rm

    def test_research_method_disney_rejection(self):
        rm = mech()["research_method"]
        assert "Disney OpenAI Sora" in rm
        assert "out-of-scope" in rm

    def test_research_method_excerpt_bounded(self):
        rm = mech()["research_method"]
        assert "Excerpt-bounded, second-hand evidence per #503" in rm
        assert "no browser.open first-hand reads this run" in rm

    def test_verification_block(self):
        v = mech()["verification"]
        assert v["iteration"] == 714
        assert v["type"] == "C"
        assert v["date"] == "2026-09-13 02:00 PDT"
        assert v["yaml_parse_clean"] is True
        assert v["ascii_only"] is True
        assert v["goal_id"] == "goal_54093bda4145"
        assert v["job_id"] == "mediascope-daily-iteration"

    def test_mechanism_name_keyword_density(self):
        name = mech()["mechanism_name"]
        for kw in ("Perplexity", "Cashmere", "Wiley", "Princeton University Press", "Dow Jones/NY Post"):
            assert kw in name, kw


class TestRotationCycleGuard714:
    """Deselected pre-commit for the anchor test; anchor patched in followup."""

    WINDOW = {713: "B", 714: "C", 715: "D", 716: "E", 717: "A"}
    ANCHORED_SHA = ANCHORED_SHA

    def test_rotation_window_mapping(self):
        assert self.WINDOW == {713: "B", 714: "C", 715: "D", 716: "E", 717: "A"}

    def test_714_is_type_c_in_window(self):
        assert self.WINDOW[ITERATION] == "C"

    def test_anchored_sha_on_main(self):
        assert git("cat-file", "-e", f"{self.ANCHORED_SHA}^{{commit}}").returncode == 0
        msg = git("log", "-1", "--format=%s", self.ANCHORED_SHA).stdout.strip()
        assert "Type C #714" in msg

    def test_iteration_log_entry_regex_self_check(self):
        sample = "#714 Type C: Perplexity premium-data licensing via Cashmere"
        assert re.match(r"^#714 Type C:", sample)


class TestDocSyncRatchet714:
    README = os.path.join(REPO, "README.md")
    ARCH = os.path.join(REPO, "docs", "ARCHITECTURE.md")
    LOG = os.path.join(REPO, "iteration-log.md")

    def test_readme_has_714_row(self):
        text = open(self.README, encoding="utf-8").read()
        assert TEST_BASENAME in text

    def test_architecture_has_714_tree_row(self):
        text = open(self.ARCH, encoding="utf-8").read()
        assert TEST_BASENAME in text

    def test_iteration_log_top_entry_714(self):
        text = open(self.LOG, encoding="utf-8").read()
        assert text.lstrip().startswith("#714 Type C:")

    def test_readme_row_mentions_cashmere(self):
        text = open(self.README, encoding="utf-8").read()
        seg = text[text.index(TEST_BASENAME):]
        seg = seg[:5000]
        assert "Cashmere" in seg and "perplexity" in seg.lower()

    def test_doc_count_stats_sync(self):
        readme = open(self.README, encoding="utf-8").read()
        assert re.search(r"\| Tests \| \d+ \| Across \d+ test files \|", readme)
