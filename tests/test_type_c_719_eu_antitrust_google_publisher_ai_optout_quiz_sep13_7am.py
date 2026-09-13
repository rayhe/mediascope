# Type C #719: EU Antitrust Probe into Google Publisher-AI Content Use (mechanism 666)
# FIRST dedicated regulatory-adversarial mechanism on the Google x publisher
# financial vector: the Dec 9 2025 European Commission antitrust investigation
# into Google's use of publisher online content and YouTube videos to train AI
# models and power AI Overviews/AI Mode, plus the Sep 1 2026 Reuters-reported
# publisher opt-out questionnaire arc (opt-out announced June 2026, global
# rollout completed Aug 31 2026, EC questionnaire sent July with Aug 28
# deadline, feedback may determine the outcome and a hefty fine remains
# possible if the proposal fails).
#
# Distinct from the cooperative licensing legs (OpenAI, Meta, Microsoft,
# Google AP/Reddit) and from the copyright-litigation adversarial legs
# (mechanism 589 Ziff Davis v OpenAI). The regulatory-adversarial vector
# REDUCES Google's publisher-hostile leverage rather than softening coverage.
#
# QUALITATIVE structural mapping only. No scorer, no tone scores, no
# p-value, no effect size, no CI. NOT a falsification-family member
# (ledger stays at 24 after #718's TWENTY-FOURTH; per #609/#614
# qualitative boundary). No analysis.json update.
#
# 719 = Type C (rotation window 715-719 closes D #715 -> E #716 -> A #717
# -> B #718 -> C #719). Anchor patched post-commit per #565 convention.
#
# Research method: 9 browser.search query sets this run: (1) xAI publisher
# licensing deal 2026 - no deal signal, zero-deal posture re-affirmed;
# (2) Anthropic publisher licensing deal 2026 - zero-deal posture
# re-confirmed via llmpulse tracker (updated Sep 7 2026); (3) Conde Nast
# Cohere lawsuit status - covered in corpus (Press Gazette Sep 2 2026
# tracker, mechanism 514 context); (4) Ziff Davis OpenAI lawsuit update -
# covered (mechanism 589, updated Sep 7); (5) Penske Google lawsuit - covered
# (mechanism 112 block); (6) News Corp Google AI licensing talks - m630
# watch unchanged, no Sep 2026 closure; (7) Cloudflare pay-per-crawl -
# covered (mechanism 64); (8) Yahoo Microsoft PCM - covered (tier_2
# marketplace); (9) EU Google publisher-AI antitrust - SELECTED.
# Excerpt-bounded, second-hand evidence per #503 (no browser.open
# first-hand reads this run). All URLs copied verbatim from Full-URL
# listings; no canonical URLs constructed. Novelty pre-commit greps: zero
# test_type_c_719 files on disk, no Type C #719 in git log, zero
# mechanism_666 keys repo-wide (the test_type_e_666 file carries iteration
# 666, not a mechanism key, per the #715 lesson), max numeric mechanism id
# 665 pre-commit, zero "European Commission" antitrust/AI hits in
# profiles/competitor-entities.yaml pre-commit. No zero-coverage claims per
# iteration-492 rule; bounded absence only. No em dashes; ASCII-only.
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
ITERATION = 719
MECH_KEY = "mechanism_666_eu_antitrust_google_publisher_ai_optout_quiz_sep2026"

# Patched in the followup commit per the #565 convention once the main
# commit SHA is known. Anchor tests are deselected pre-commit.
ANCHORED_SHA = "cd71ea2de130d14817ac15decd6da68b0249c96a"


def load_competitor():
    with open(COMPETITOR, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def mech():
    return load_competitor()["entities"]["google"][MECH_KEY]


def git(*args):
    return subprocess.run(
        ["git", *args],
        cwd=REPO,
        capture_output=True,
        text=True,
        timeout=120,
    )


class TestIterationMetadata719:
    def test_iteration_is_719(self):
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
        assert m["time_pdt"] == "07:00"
        assert m["job_id"] == "mediascope-daily-iteration"
        assert m["goal_id"] == "goal_54093bda4145"

    def test_mechanism_id_666_int(self):
        assert isinstance(mech()["mechanism_id"], int)
        assert mech()["mechanism_id"] == 666

    def test_single_666_mechanism_key(self):
        hits = [k for k in load_competitor()["entities"]["google"] if k.startswith("mechanism_666")]
        assert hits == [MECH_KEY]

    def test_iteration_type_matches_rotation(self):
        assert mech()["iteration_type"] == "C"


class TestInvestigationArc719:
    def test_dec_9_2025_probe_opened(self):
        arc = " ".join(mech()["investigation_arc"])
        assert "2025-12-09" in arc
        assert "European Commission" in arc
        assert "antitrust investigation" in arc

    def test_complainants_named(self):
        arc = " ".join(mech()["investigation_arc"])
        assert "Independent Publishers Alliance" in arc
        assert "Movement for an Open Web" in arc
        assert "Foxglove" in arc

    def test_ribera_unfair_trading_quote(self):
        arc = " ".join(mech()["investigation_arc"])
        assert "unfair trading conditions" in arc
        assert "dominant position" in arc

    def test_ribera_healthy_ecosystem_quote(self):
        arc = " ".join(mech()["investigation_arc"])
        assert "healthy information ecosystem" in arc

    def test_google_stifling_innovation_response(self):
        arc = " ".join(mech()["investigation_arc"])
        assert "stifling innovation" in arc

    def test_fifth_probe_prior_fines(self):
        arc = " ".join(mech()["investigation_arc"])
        assert "fifth EU antitrust probe" in arc
        assert "10 billion euros" in arc

    def test_second_probe_in_a_month(self):
        arc = " ".join(mech()["investigation_arc"])
        assert "second investigation into Google in less than a month" in arc

    def test_optout_announced_june_2026(self):
        arc = " ".join(mech()["investigation_arc"])
        assert "2026-06" in arc
        assert "AI opt-out" in arc

    def test_global_rollout_completed_aug_31(self):
        arc = " ".join(mech()["investigation_arc"])
        assert "Aug 31 2026" in arc

    def test_sep_1_reuters_questionnaire_report(self):
        arc = " ".join(mech()["investigation_arc"])
        assert "2026-09-01" in arc
        assert "hefty fine" in arc


class TestOptoutRemedy719:
    def test_optout_block_present(self):
        assert "optout_remedy" in mech()

    def test_rankings_unaffected(self):
        assert "without affecting their rankings" in mech()["optout_remedy"]["what"]

    def test_global_rollout_date(self):
        assert mech()["optout_remedy"]["global_rollout_complete"] == "2026-08-31"

    def test_questionnaire_deadline_aug_28(self):
        assert "Aug 28" in mech()["optout_remedy"]["questionnaire_sent"]

    def test_three_questionnaire_asks(self):
        asks = " ".join(mech()["optout_remedy"]["questionnaire_asks"])
        assert "make use of the opt-out" in asks
        assert "Factors influencing" in asks
        assert "AI Overviews and AI Mode" in asks

    def test_stakes_fine_possible(self):
        assert "fine" in mech()["optout_remedy"]["stakes"]

    def test_uptake_caveat(self):
        caveat = mech()["optout_remedy"]["uptake_caveat"]
        assert "uptake is uncertain" in caveat
        assert "traffic" in caveat

    def test_cma_same_day_order_noted(self):
        arc = " ".join(mech()["investigation_arc"])
        assert "UK antitrust watchdog" in arc or "UK CMA" in arc

    def test_google_declined_comment_june_3_blog(self):
        arc = " ".join(mech()["investigation_arc"])
        assert "declined comment" in arc
        assert "June 3" in arc


class TestYoutubeLegAndParallels719:
    def test_youtube_leg_present(self):
        assert "youtube_leg" in mech()

    def test_youtube_training_scope(self):
        assert "YouTube videos" in mech()["youtube_leg"]["scope"]

    def test_youtube_asymmetric_cost(self):
        assert "barred" in mech()["youtube_leg"]["asymmetry"]
        assert "pay YouTube" in mech()["youtube_leg"]["asymmetry"]

    def test_meta_whatsapp_parallel_bounded(self):
        note = mech()["meta_whatsapp_parallel"]["note"]
        assert "Meta" in note and "WhatsApp" in note

    def test_no_equivalence_claimed(self):
        assert "no equivalence claimed" in mech()["meta_whatsapp_parallel"]["bounded"]

    def test_demotion_probe_note(self):
        assert "demoted" in mech()["meta_whatsapp_parallel"]["also"] or "demot" in mech()["meta_whatsapp_parallel"]["also"]

    def test_parallels_are_cross_entity_only(self):
        assert "regulatory-context" in mech()["meta_whatsapp_parallel"]["bounded"]


class TestTheoryAndConfounds719:
    def test_regulatory_adversarial_class(self):
        assert "regulatory-adversarial" in mech()["theory_prediction"]["mechanism_class"]

    def test_direction_reduces_leverage(self):
        assert "REDUCES" in mech()["theory_prediction"]["direction"]

    def test_no_tone_claim(self):
        assert "No tone claim" in mech()["theory_prediction"]["bounded"]

    def test_five_ranked_confounders(self):
        confs = mech()["ranked_confounders"]
        assert len(confs) == 5
        assert [c["rank"] for c in confs] == [1, 2, 3, 4, 5]
        assert confs[0]["strength"] == "strong"
        assert confs[1]["strength"] == "strong"

    def test_confounder_process_not_outcome(self):
        assert "no fine or compensation term exists yet" in mech()["ranked_confounders"][0]["confounder"]

    def test_strongest_counterargument(self):
        assert "mutual-benefit" in mech()["strongest_counterargument"]
        assert "toothless" in mech()["strongest_counterargument"]

    def test_statistical_discipline_qualitative(self):
        sd = mech()["statistical_discipline"]
        assert sd["tone_scores"] == "NOT_SCORED"
        assert sd["p_value"] == "NOT_CALCULATED"
        assert sd["cohens_d"] == "NOT_CALCULATED"
        assert sd["ci_95"] == "NOT_CALCULATED"
        assert sd["is_significant"] is False

    def test_not_falsification_family_ledger_24(self):
        nov = " ".join(mech()["novelty_verification"])
        assert "NOT a falsification-family member" in nov
        assert "ledger stays at 24" in nov

    def test_correlational_note_present(self):
        assert "correlational" in mech()["correlational_note"]
        assert mech()["cautious_language_required"] is True
        assert mech()["no_coverage_tone_claim"] is True


class TestPilotCoercionCrossref719:
    def test_pilot_block_present(self):
        assert "pilot_coercion_crossref" in mech()

    def test_june_25_2026_pilot_terms(self):
        note = mech()["pilot_coercion_crossref"]["note"]
        assert "Jun 25 2026" in note
        assert "broad rights" in note

    def test_3000_partnerships(self):
        assert "3,000" in mech()["pilot_coercion_crossref"]["note"]

    def test_cma_neutralization_corpus_link(self):
        assert "google_news_ai_pilot_deal_structure_cma_neutralization" in mech()["pilot_coercion_crossref"]["corpus_link"]


class TestSourcesAndResearch719:
    def test_five_source_urls(self):
        assert len(mech()["source_urls"]) == 5

    def test_reuters_dec_9_url(self):
        urls = " ".join(mech()["source_urls"])
        assert "eu-launches-antitrust-probe-into-googles-use-online-content-ai-purposes-2025-12-09" in urls

    def test_reuters_sep_1_url(self):
        urls = " ".join(mech()["source_urls"])
        assert "eu-antitrust-regulators-quiz-publishers-googles-ai-search-opt-out-2026-09-01" in urls

    def test_pymnts_url(self):
        urls = " ".join(mech()["source_urls"])
        assert "google-tells-news-publishers-to-share-content-for-ai-training-or-lose-fees" in urls

    def test_thecurrent_url(self):
        urls = " ".join(mech()["source_urls"])
        assert "thecurrent.com/marketing/data-privacy-google-new-eu-antitrust-probe" in urls

    def test_morningstar_url(self):
        urls = " ".join(mech()["source_urls"])
        assert "european-commission-opens-another-antitrust-investigation-into-google-this-time-its-ai" in urls

    def test_research_method_nine_query_sets(self):
        rm = mech()["research_method"]
        assert "(9)" in rm or "9 browser.search" in rm
        assert "#503" in rm

    def test_mechanism_block_ascii_only(self):
        yaml.safe_dump(mech()).encode("ascii")

    def test_novelty_verification_distinct_from_prior(self):
        nov = " ".join(mech()["novelty_verification"])
        for token in ("mechanism 589", "mechanism 64", "mechanism 112", "mechanism 529"):
            assert token in nov, token


class TestRotationCycleGuard719:
    """Deselected pre-commit for the anchor test; anchor patched in followup."""

    WINDOW = {715: "D", 716: "E", 717: "A", 718: "B", 719: "C"}
    ANCHORED_SHA = ANCHORED_SHA

    def test_rotation_window_mapping(self):
        assert self.WINDOW == {715: "D", 716: "E", 717: "A", 718: "B", 719: "C"}

    def test_719_is_type_c_in_window(self):
        assert self.WINDOW[ITERATION] == "C"

    def test_718_was_type_b_in_window(self):
        assert self.WINDOW[718] == "B"

    def test_anchored_sha_on_main(self):
        assert git("cat-file", "-e", f"{self.ANCHORED_SHA}^{{commit}}").returncode == 0
        msg = git("log", "-1", "--format=%s", self.ANCHORED_SHA).stdout.strip()
        assert "Type C #719" in msg

    def test_iteration_log_entry_regex_self_check(self):
        sample = "#719 Type C: EU antitrust probe into Google publisher-AI content use"
        assert re.match(r"^#719 Type C:", sample)

    def test_single_719_test_file_pre_commit(self):
        hits = [os.path.basename(p) for p in glob.glob(os.path.join(TESTS_DIR, "test_type_c_719*.py"))]
        assert hits == [TEST_BASENAME]


class TestDocSyncRatchet719:
    README = os.path.join(REPO, "README.md")
    ARCH = os.path.join(REPO, "docs", "ARCHITECTURE.md")
    LOG = os.path.join(REPO, "iteration-log.md")

    def test_readme_has_719_row(self):
        text = open(self.README, encoding="utf-8").read()
        assert TEST_BASENAME in text

    def test_architecture_has_719_tree_row(self):
        text = open(self.ARCH, encoding="utf-8").read()
        assert TEST_BASENAME in text

    def test_iteration_log_top_entry_719(self):
        text = open(self.LOG, encoding="utf-8").read()
        assert text.lstrip().startswith("#719 Type C:")

    def test_readme_row_mentions_optout(self):
        text = open(self.README, encoding="utf-8").read()
        seg = text[text.index(TEST_BASENAME):]
        seg = seg[:5000]
        assert "opt-out" in seg or "optout" in seg or "opt out" in seg

    def test_doc_count_stats_sync(self):
        readme = open(self.README, encoding="utf-8").read()
        assert re.search(r"\| Tests \| \d+ \| Across \d+ test files \|", readme)
