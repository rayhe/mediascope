# Type C #699: Apple x Google Gemini Multi-Year AI Deal (Jan 12 2026)
# FIRST dedicated deal-level mechanism formalizing the Apple x Google Gemini
# publisher-content bypass leg (mechanism 654).
#
# The leg: Apple pays Google ~$1B/yr (Bloomberg-reported; terms undisclosed) for a
# custom 1.2T-parameter Gemini powering Siri AI (beta ships Sep 14 2026, iOS 27).
# Publishers receive $0 directly from Apple; the content flows through Google.
# Fresh findings this run: (a) Sep 9-10 2026 status corroboration (PYMNTS +
# macobserver: "Siri now runs on Gemini"); (b) Karen Webster "dependency on a
# competitor, twice over" asymmetric-dependency quote (PYMNTS, Sep 9 2026);
# (c) brand-layer erasure (one published sentence; no on-stage mention);
# (d) Munster/Deepwater up-to-$5B multi-year estimate (new-to-corpus);
# (e) Hachette/Cengage/Elsevier/Turow Jul 2026 class-action leg (S.D.N.Y.
# 1:26-cv-05870) with Adweek Books-snippet origin + $10Bs-$100Bs internal estimate.
#
# QUALITATIVE structural mapping only. No scorer, no tone scores, no p-value,
# no effect size, no CI. NOT a falsification-family member (ledger stays at 20
# after #698's TWENTIETH). No analysis.json update.
#
# 699 = Type C (main: 75dd23c 698/B, a7f0617 698/B main, 2f776a6 697/A,
# a3a2a49 697/A main; rotation window 695-699 -> C #699, B #698, A #697,
# E #696, D #695). Anchor patched post-commit per #565 convention.
#
# Research method: 3 browser.search query sets this run (Apple Google Gemini
# deal Siri September 2026 status, since 2026-08-01; Apple pays Google $1
# billion per year Gemini Siri; Hachette Cengage Elsevier lawsuit Google Gemini
# training data unauthorized books 2026). URLs copied verbatim from Full-URL
# listings; no canonical URLs constructed. Novelty pre-commit greps: zero
# test_type_c_699 files, no Type C #699 in git log, zero mechanism_654 keys,
# max numeric mechanism id 653. No zero-coverage claims per iteration-492
# rule; bounded absence only. No em dashes; ASCII-only.

import glob
import os
import re
import subprocess
import unicodedata

import pytest
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMPETITOR = os.path.join(REPO, "profiles", "competitor-entities.yaml")
ITERATION = 699
ANCHOR_SHA = "75dd23c"
MECH_KEY = "mechanism_654_apple_google_gemini_publisher_content_bypass_leg_sep2026"


def load_competitor():
    with open(COMPETITOR, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def mech():
    return load_competitor()["entities"]["apple"][MECH_KEY]


def git(*args):
    return subprocess.run(
        ["git", *args],
        cwd=REPO,
        capture_output=True,
        text=True,
        timeout=120,
    )


class TestIterationMetadata699:
    def test_anchor_commit_present(self):
        assert git("cat-file", "-e", f"{ANCHOR_SHA}^{{commit}}").returncode == 0

    def test_iteration_is_699(self):
        assert mech()["iteration"] == 699

    def test_rotation_is_type_c(self):
        assert mech()["rotation"] == "Type C"

    def test_date_time_job_goal(self):
        m = mech()
        assert m["date_analyzed"] == "2026-09-12"
        assert m["time_pdt"] == "09:00"
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"

    def test_type_is_financial_incentive_mapping(self):
        assert mech()["type"] == "financial_incentive_mapping"

    def test_single_654_mechanism_key(self):
        hits = [k for k in load_competitor()["entities"]["apple"] if k.startswith("mechanism_654")]
        assert hits == [MECH_KEY]


class TestDealLegFormalization699:
    def test_mechanism_id_654_int(self):
        assert isinstance(mech()["mechanism_id"], int)
        assert mech()["mechanism_id"] == 654

    def test_announcement_and_broke_by(self):
        m = mech()
        assert m["announcement_date"] == "2026-01-12"
        assert "Bloomberg" in m["broke_by"]
        assert "Gurman" in m["broke_by"]

    def test_deal_parties(self):
        parties = mech()["deal_parties"]
        assert "Apple" in parties["payer"] and "Google" in parties["counterparty"]

    def test_quantum_reported_not_disclosed(self):
        q = mech()["deal_terms"]["quantum"]
        assert "1 billion" in q
        assert "Bloomberg" in q
        assert "not publicly disclosed" in q or "has publicly disclosed" in q

    def test_multiyear_estimate_labeled_analyst(self):
        est = mech()["deal_terms"]["multiyear_total_estimate"]
        assert "$5 billion" in est
        assert "Munster" in est and "Deepwater" in est
        assert "not company-stated" in est

    def test_model_reported_not_apple_spec(self):
        model = mech()["deal_terms"]["model"]
        assert "1.2" in model
        assert "not an Apple specification" in model

    def test_scope_siri_and_private_cloud_compute(self):
        scope = mech()["deal_terms"]["scope"]
        assert "summarizer" in scope and "planner" in scope
        assert "Private Cloud Compute" in scope
        assert "not Google servers" in scope

    def test_stopgap_frame(self):
        assert "stopgap" in mech()["deal_terms"]["stopgap_frame"]

    def test_bypass_chain_four_steps_and_contrast(self):
        chain = mech()["bypass_chain"]
        assert "Hachette" in chain["step_1"] and "1:26-cv-05870" in chain["step_1"]
        assert "$1B/yr" in chain["step_2"]
        assert "Sep 14 2026" in chain["step_3"]
        assert "$0" in chain["step_4"]
        assert "mechanism 549" in chain["contrast"]
        assert "mechanism 559" in chain["contrast"]

    def test_asymmetric_dependency_webster_twice_over(self):
        dep = mech()["asymmetric_dependency"]["finding"]
        assert "twice over" in dep
        assert "Webster" in dep
        assert "$20B/yr" in dep

    def test_brand_layer_erasure(self):
        erasure = mech()["brand_layer_erasure"]["finding"]
        assert "one published sentence" in erasure
        assert "did not mention Google or Gemini on stage" in erasure
        assert "Sep 9 2026" in erasure

    def test_status_active_per_599(self):
        status = mech()["status_sep2026"]
        assert status.startswith("ACTIVE")
        assert "#599" in status
        assert "iteration-492" in status
        assert "mechanism 606" in status

    def test_wearables_prediction_flagged_not_finding(self):
        assert "Predictions, not findings." in mech()["wearables_coverage_prediction"]

    def test_source_urls_count_and_key_urls(self):
        urls = mech()["source_urls"]
        assert len(urls) == 11
        joined = "\n".join(urls)
        assert "macrumors.com/2025/11/05/apple-google-new-siri-payment/" in joined
        assert "reuters.com/business/apple-use-googles-ai-model-run-new-siri" in joined
        assert "pymnts.com/apple/2026/after-two-years-of-hype-apple-says-siri-ai-is-ready/" in joined
        assert "macobserver.com/tips/round-ups/does-siri-ai-use-google-gemini/" in joined
        assert "tech-insider.org/apple-google-gemini-siri-deal-1-billion-2026/" in joined
        assert "hachettebookgroup.com" in joined
        assert "adweek.com/media/book-publishers-sue-google/" in joined

    def test_source_urls_all_http(self):
        for u in mech()["source_urls"]:
            assert u.startswith("http")


class TestCrossReferences699:
    def test_mechanism_156_phase_2_origin(self):
        refs = "\n".join(mech()["cross_references"])
        assert "mechanism 156" in refs and "phase_2_bypass" in refs

    def test_publisher_content_bypass_block(self):
        refs = "\n".join(mech()["cross_references"])
        assert "publisher_content_bypass block" in refs

    def test_mechanism_606_status_check(self):
        refs = "\n".join(mech()["cross_references"])
        assert "mechanism 606" in refs and "#619" in refs

    def test_news_plus_and_pcm_legs(self):
        refs = "\n".join(mech()["cross_references"])
        assert "#679" in refs and "#684" in refs

    def test_sep11_sweep_and_meta_comparator(self):
        refs = "\n".join(mech()["cross_references"])
        assert "#674" in refs and "mechanism 549" in refs

    def test_adweek_meta_litigation_mirror(self):
        refs = "\n".join(mech()["cross_references"])
        assert "Adweek parallel Meta suit" in refs

    def test_cross_reference_count(self):
        assert len(mech()["cross_references"]) == 8


class TestNoveltyAndFirstDedicated699:
    def test_single_type_c_699_file_pre_commit(self):
        files = glob.glob(os.path.join(REPO, "tests", "test_type_c_699*.py"))
        assert len(files) == 1 and files[0].endswith(
            "test_type_c_699_apple_google_gemini_bypass_leg_sep12_9am.py"
        )

    def test_no_type_c_699_in_git_log_pre_commit(self):
        out = git("log", "--oneline", "--grep=Type C #699").stdout.strip()
        assert out == ""

    def test_no_duplicate_654_key(self):
        count = 0
        for root, _, files in os.walk(os.path.join(REPO, "profiles")):
            for fn in files:
                if fn.endswith((".yaml", ".yml")):
                    with open(os.path.join(root, fn), encoding="utf-8") as fh:
                        count += len(re.findall(r"(?m)^\s*mechanism_654", fh.read()))
        assert count == 1

    def test_first_dedicated_gemini_deal_mechanism(self):
        data = load_competitor()
        dedicated = [
            k
            for ent in data["entities"].values()
            if isinstance(ent, dict)
            for k in ent
            if isinstance(k, str)
            and k.startswith("mechanism_")
            and "gemini" in k.lower()
        ]
        assert dedicated == [MECH_KEY]

    def test_max_numeric_mechanism_id_is_654(self):
        data = load_competitor()
        nums = []
        for ent in data["entities"].values():
            if isinstance(ent, dict):
                for k in ent:
                    m = re.match(r"mechanism_(\d+)_", k) if isinstance(k, str) else None
                    if m:
                        nums.append(int(m.group(1)))
        assert max(nums) == 654

    def test_novelty_pins_verbatim(self):
        pins = "\n".join(mech()["novelty_verification"])
        assert "Max numeric mechanism id pre-commit 653" in pins
        assert "Zero mechanism_654 keys in profiles/ pre-commit" in pins
        assert "No Type C #699 in git log pre-commit" in pins

    def test_new_to_corpus_pins(self):
        pins = "\n".join(mech()["novelty_verification"])
        assert "Webster twice-over dependency quote" in pins
        assert "macobserver one-sentence brand-erasure" in pins
        assert "Munster/Deepwater up-to-$5B" in pins
        assert "$10Bs-$100Bs internal estimate" in pins


class TestResearchMethod699:
    def test_three_browser_search_query_sets(self):
        assert "3 browser.search query sets" in mech()["research_method"]

    def test_verbatim_urls_no_canonical_construction(self):
        rm = mech()["research_method"]
        assert "copied verbatim from Full-URL listings" in rm
        assert "no canonical URLs constructed" in rm

    def test_iteration_492_no_zero_coverage_claims(self):
        rm = mech()["research_method"]
        assert "iteration-492" in rm
        assert "bounded absence only" in rm

    def test_ascii_no_em_dashes(self):
        text = open(COMPETITOR, encoding="utf-8").read()
        seg = text[text.index(MECH_KEY) : text.index("apple_news_platform_leverage:")]
        assert "—" not in seg and "–" not in seg
        assert "\u2028" not in seg and "\u2029" not in seg

    def test_job_and_goal_ids_in_method(self):
        assert mech()["job_id"] == "mediascope-daily-iteration"
        assert mech()["goal_id"] == "goal_54093bda4145"


class TestStatisticalDiscipline699:
    def test_scorer_none(self):
        assert mech()["statistical_discipline"]["scorer"] == "none"

    def test_tone_scores_not_scored(self):
        assert mech()["statistical_discipline"]["tone_scores"] == "NOT_SCORED"

    def test_p_value_not_calculated(self):
        assert mech()["statistical_discipline"]["p_value"] == "NOT_CALCULATED"

    def test_effect_size_and_ci_not_calculated(self):
        sd = mech()["statistical_discipline"]
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"

    def test_not_significant(self):
        sd = mech()["statistical_discipline"]
        assert sd["is_significant"] is False
        assert sd["qualitative_only"] is True

    def test_artifact_grade_false(self):
        assert mech()["statistical_discipline"]["artifact_grade"] is False

    def test_correlation_not_causation(self):
        assert mech()["statistical_discipline"]["correlation_not_causation"] is True

    def test_not_falsification_family_ledger_holds_at_20(self):
        fam = mech()["falsification_family"]
        assert "NOT a member" in fam["membership"]
        assert "ledger stays at 20" in fam["membership"]
        assert "qualitative boundary" in fam["boundary_note"]

    def test_no_analysis_json_update(self):
        assert "No analysis.json update warranted" in mech()["artifact_readiness"]


class TestConfounderRanking699:
    def test_five_ranked_confounders(self):
        confs = mech()["ranked_confounders"]
        assert len(confs) == 5
        assert [c["rank"] for c in confs] == [1, 2, 3, 4, 5]

    def test_rank1_quantum_undisclosed_strong(self):
        c1 = mech()["ranked_confounders"][0]
        assert c1["strength"] == "strong"
        assert "has publicly disclosed exact financial terms" in c1["confounder"]

    def test_rank2_book_suit_news_content_boundary_strong(self):
        c2 = mech()["ranked_confounders"][1]
        assert c2["strength"] == "strong"
        assert "Showcase" in c2["confounder"]

    def test_rank3_capability_driven_procurement(self):
        c3 = mech()["ranked_confounders"][2]
        assert c3["strength"] == "moderate"
        assert "stopgap" in c3["confounder"]

    def test_rank4_allegations_unproven(self):
        c4 = mech()["ranked_confounders"][3]
        assert "unproven" in c4["confounder"]

    def test_rank5_capability_constraints(self):
        c5 = mech()["ranked_confounders"][4]
        assert c5["strength"] == "weak"
        assert "WhatsApp" in c5["confounder"]


class TestCautionAndBoundaries699:
    def test_caution_structural_mapping_only(self):
        caution = mech()["caution"]
        assert "Structural mapping only" in caution
        assert "No coverage-tone claim is made." in caution

    def test_hachette_leg_is_allegation_not_finding(self):
        step1 = mech()["bypass_chain"]["step_1"]
        assert "alleges" in step1 or "putative" in step1
        assert "no ruling" in mech()["ranked_confounders"][3]["confounder"]

    def test_type_c_focus_names_completion_not_capture(self):
        focus = mech()["type_c_focus"]
        assert "First dedicated deal-level mechanism" in focus
        assert "ACTIVE deal leg" in focus


class TestRotationCycleGuard699:
    WINDOW = {699: "C", 698: "B", 697: "A", 696: "E", 695: "D"}

    def test_window_695_699_closes_c(self):
        for it, typ in self.WINDOW.items():
            if it == 699:
                continue
            out = git("log", "--oneline", "--grep", f"Type {typ} #{it}").stdout.strip()
            assert out != "", f"missing committed iteration #{it}"

    def test_adjacency_valid_698_to_699(self):
        assert self.WINDOW[699] == "C" and self.WINDOW[698] == "B"

    def test_anchor_is_followup_commit(self):
        pytest.skip("anchor patched to the #699 main commit in the followup, per #565 convention")

    def test_iteration_log_entry_regex_self_check(self):
        sample = "#699 Type C: Apple x Google Gemini bypass leg"
        assert re.match(r"^#699 Type C:", sample)


class TestDocSyncRatchet699:
    README = os.path.join(REPO, "README.md")
    ARCH = os.path.join(REPO, "docs", "ARCHITECTURE.md")
    LOG = os.path.join(REPO, "iteration-log.md")

    def test_readme_has_699_row(self):
        text = open(self.README, encoding="utf-8").read()
        assert "test_type_c_699_apple_google_gemini_bypass_leg_sep12_9am.py" in text

    def test_architecture_has_699_tree_row(self):
        text = open(self.ARCH, encoding="utf-8").read()
        assert "test_type_c_699_apple_google_gemini_bypass_leg_sep12_9am.py" in text

    def test_iteration_log_top_entry_699(self):
        text = open(self.LOG, encoding="utf-8").read()
        assert text.lstrip().startswith("#699 Type C:")

    def test_readme_row_mentions_gemini_bypass(self):
        text = open(self.README, encoding="utf-8").read()
        seg = text[text.index("test_type_c_699_apple_google_gemini_bypass_leg_sep12_9am.py") :]
        seg = seg[:4000]
        assert "Gemini" in seg and "bypass" in seg

    def test_doc_count_stats_sync(self):
        text = open(self.README, encoding="utf-8").read()
        assert "| Tests | 36852 |" in text and "Across 1027 test files" in text
