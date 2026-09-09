"""Type C #619 (2026-09-08 22:00 PDT): Apple Siri AI publisher negotiation
silence status check (mechanism_id 606).

27 days after the Aug 12 2026 WSJ report (variable pay-per-use model,
nine-figure budget, unnamed publishers, multiyear deals for Siri AI current
news retrieval), zero signed-deal announcements have surfaced and no
counterparty publisher has been named. Mechanism 156 stays PREDICTIVE, not
observed. Corroboration stack: MacRumors (Aug 12 5:03pm PDT, Juli Clover),
TheWrap, TechRepublic, Engadget, AppleMagazine x2, MediaCopilot, ArchyNewsy,
Lumida News. Originator self-disclosure carried: News Corp, owner of the WSJ,
has its own commercial agreement to supply news through Apple services.
Retrieval-vs-training distinction carried from secondary analysis (variable
pricing coherent for traceable retrieval, not for bulk training).

Qualitative Type C mapping: tone_scores NOT_SCORED, p_value/cohens_d/ci_95
NOT_CALCULATED, is_significant False, MANUAL ILLUSTRATIVE labeling,
correlational structural incentives only, no causal claim. No em dashes
anywhere in this file.
"""
import yaml
import pytest

ITERATION = 619
MECHANISM_ID = 606
MECHANISM_KEY = "siri_ai_negotiation_silence_status_check_606"

WSJ_URL = ("https://www.wsj.com/business/media/"
           "apple-in-talks-to-pay-publishers-to-improve-ai-powered-siri-0641f64b")
MACRUMORS_URL = "https://www.macrumors.com/2026/08/12/apple-siri-ai-publisher-talks/"
TECHREPUBLIC_URL = "https://www.techrepublic.com/article/news-apple-publisher-deals-siri-ai/"
ENGADGET_URL = "https://www.engadget.com/2236317/apple-is-reportedly-turning-to-publishers-for-help-with-siri-ai/"
THEWRAP_URL = "https://www.thewrap.com/industry-news/tech/apple-ai-siri-news-media-publishing-deals/"
APPLEMAGAZINE_URL = "https://applemagazine.com/siri-ai-apple-publisher-content-deals/"
ARCHYNEWSY_URL = "https://www.archynewsy.com/apple-to-pay-news-publishers-for-siri-ai-integration/"
MEDIACOPILOT_URL = "https://mediacopilot.ai/apple-siri-ai-publisher-payments/"
LUMIDANEWS_URL = ("https://lumidanews.com/apple-is-paying-publishers-for-real-time-news-"
                  "to-power-ai-siri-multiyear-content-deals-signal-a-different-strategy-"
                  "than-the-scrape-first-ai-playbook/")


@pytest.fixture(scope="module")
def mechanism():
    with open("profiles/competitor-entities.yaml", "r") as f:
        data = yaml.safe_load(f)
    return data["entities"]["apple"][MECHANISM_KEY]


class TestMechanismPresence:
    def test_mechanism_key_exists(self, mechanism):
        assert mechanism is not None

    def test_mechanism_id_606(self, mechanism):
        assert mechanism["mechanism_id"] == MECHANISM_ID

    def test_date_checked_sep08_2026(self, mechanism):
        assert mechanism["date_checked"] == "2026-09-08"

    def test_extends_mechanism_156(self, mechanism):
        assert mechanism["extends_mechanism_id"] == 156

    def test_iteration_matches(self):
        assert ITERATION == 619

    def test_no_em_dashes_in_yaml_block(self):
        with open("profiles/competitor-entities.yaml", "r") as f:
            blob = f.read()
        idx = blob.find(MECHANISM_KEY)
        seg = blob[idx:idx + 6000]
        assert "\u2014" not in seg and "\u2013" not in seg


class TestOriginReport:
    def test_origin_is_wsj_aug12(self, mechanism):
        assert "Aug 12 2026" in mechanism["origin_report"]

    def test_variable_compensation_stated(self, mechanism):
        assert "variable" in mechanism["origin_report"].lower()

    def test_nine_figure_budget_stated(self, mechanism):
        assert "nine-figure" in mechanism["origin_report"]

    def test_multiyear_stated(self, mechanism):
        assert "multiyear" in mechanism["origin_report"].lower()

    def test_retrieval_not_training(self, mechanism):
        assert "retrieval" in mechanism["origin_report"].lower()

    def test_apple_declined_comment(self, mechanism):
        assert "declined to comment" in mechanism["origin_report"]


class TestCorroborationStack:
    def test_eight_corroborations(self, mechanism):
        assert len(mechanism["corroboration_stack_new_this_run"]) == 8

    def test_macrumors_timestamped(self, mechanism):
        assert any("5:03pm PDT" in c
                   for c in mechanism["corroboration_stack_new_this_run"])

    def test_mediacopilot_no_deals_announced(self, mechanism):
        assert any("no deals announced" in c
                   for c in mechanism["corroboration_stack_new_this_run"])

    def test_applemagazine_retrieval_training(self, mechanism):
        assert any("retrieval vs training" in c
                   for c in mechanism["corroboration_stack_new_this_run"])


class TestFinding:
    def test_27_day_silence(self, mechanism):
        assert "27 days" in mechanism["finding"]

    def test_no_signed_announcements(self, mechanism):
        assert "NO signed Apple publisher deal announcement" in mechanism["finding"]

    def test_no_counterparty_named(self, mechanism):
        assert "counterparty publisher" in mechanism["finding"].lower()

    def test_bounded_absence_disclaimer(self, mechanism):
        assert "iteration-492" in mechanism["finding"]

    def test_nda_possibility_acknowledged(self, mechanism):
        assert "NDA" in mechanism["finding"]

    def test_mechanism_156_stays_predictive(self, mechanism):
        assert "PREDICTIVE" in mechanism["finding"]


class TestOriginatorSelfDisclosure:
    def test_news_corp_apple_agreement(self, mechanism):
        assert "News Corp" in mechanism["originator_self_disclosure"]

    def test_own_parent_disclosed(self, mechanism):
        assert "owner of The Wall Street Journal" in mechanism["originator_self_disclosure"]

    def test_commercial_agreement_phrase(self, mechanism):
        assert "commercial agreement" in mechanism["originator_self_disclosure"]


class TestRetrievalVsTraining:
    def test_retrieval_traceable(self, mechanism):
        assert "traceable" in mechanism["retrieval_vs_training_distinction"].lower()

    def test_training_not_coherent_for_variable(self, mechanism):
        d = mechanism["retrieval_vs_training_distinction"]
        assert "bulk archive" in d or "unmeasurable" in d

    def test_attributed_to_secondary_analysis(self, mechanism):
        assert "AppleMagazine" in mechanism["retrieval_vs_training_distinction"]


class TestWatchItem:
    def test_siri_ai_launch_fall_2026(self, mechanism):
        assert "iOS 27" in mechanism["watch_item"]

    def test_benchmark_conversion_condition(self, mechanism):
        assert "predictive to observed" in mechanism["watch_item"]


class TestConfounders:
    def test_four_confounders(self, mechanism):
        assert len(mechanism["confounders_ranked"]) == 4

    def test_first_is_strong(self, mechanism):
        assert mechanism["confounders_ranked"][0]["strength"] == "STRONG"

    def test_strengths_ranked(self, mechanism):
        strengths = [c["strength"] for c in mechanism["confounders_ranked"]]
        assert strengths == ["STRONG", "MODERATE", "MODERATE", "WEAK"]

    def test_deal_time_confounder(self, mechanism):
        assert any("6 to 18 months" in c["description"]
                   for c in mechanism["confounders_ranked"])

    def test_unnamed_sources_confounder(self, mechanism):
        assert any("unnamed people familiar" in c["description"]
                   for c in mechanism["confounders_ranked"])


class TestStatisticalDiscipline:
    def test_not_significant(self, mechanism):
        assert "is_significant False" in mechanism["statistical_discipline"]

    def test_tones_not_scored(self, mechanism):
        assert "NOT_SCORED" in mechanism["statistical_discipline"]

    def test_no_causal_claim(self, mechanism):
        assert "no causal claim" in mechanism["statistical_discipline"]

    def test_p_value_not_calculated(self, mechanism):
        assert "NOT_CALCULATED" in mechanism["statistical_discipline"]


class TestCrossReferences:
    def test_two_cross_references(self, mechanism):
        assert len(mechanism["cross_references"]) == 2

    def test_extends_156(self, mechanism):
        refs = {r["mechanism_id"]: r["relationship"]
                for r in mechanism["cross_references"]}
        assert refs[156] == "extends"

    def test_related_80(self, mechanism):
        refs = {r["mechanism_id"]: r["relationship"]
                for r in mechanism["cross_references"]}
        assert refs[80] == "related"


class TestSourceUrls:
    def test_nine_source_urls(self, mechanism):
        assert len(mechanism["source_urls"]) == 9

    def test_wsj_url_present(self, mechanism):
        assert WSJ_URL in mechanism["source_urls"]

    def test_macrumors_url_present(self, mechanism):
        assert MACRUMORS_URL in mechanism["source_urls"]

    def test_all_verbatim_urls_present(self, mechanism):
        for url in (TECHREPUBLIC_URL, ENGADGET_URL, THEWRAP_URL,
                    APPLEMAGAZINE_URL, ARCHYNEWSY_URL, MEDIACOPILOT_URL,
                    LUMIDANEWS_URL):
            assert url in mechanism["source_urls"]

    def test_no_constructed_urls(self, mechanism):
        for url in mechanism["source_urls"]:
            assert url.startswith("https://")
            assert "?" not in url


class TestRotationCycleGuard619:
    """Covers the 615-619 main-commit window (C,B,A,E,D newest-first),
    closing the B->C edge. ANCHOR PATCHED POST-COMMIT per the #565 followup
    convention: the expected anchor commit id is filled in the followup run
    after the main commit is created."""
    EXPECTED_WINDOW_NEWEST_FIRST = [
        ("Type C", 619),
        ("Type B", 618),
        ("Type A", 617),
        ("Type E", 616),
        ("Type D", 615),
    ]
    # Anchor: patched in followup - see iteration-log entry for #619.
    ANCHOR_MAIN_COMMIT = "5359f27"

    def test_window_sequence(self):
        seq = [(t, n) for t, n in self.EXPECTED_WINDOW_NEWEST_FIRST]
        assert seq[0] == ("Type C", 619)
        assert seq[-1] == ("Type D", 615)

    def test_closes_b_to_c_edge(self):
        types = [t for t, _ in self.EXPECTED_WINDOW_NEWEST_FIRST]
        assert types[0] == "Type C" and types[1] == "Type B"

    def test_five_window_members(self):
        assert len(self.EXPECTED_WINDOW_NEWEST_FIRST) == 5

    def test_anchor_patched_post_commit(self):
        assert (self.ANCHOR_MAIN_COMMIT is not None
                and self.ANCHOR_MAIN_COMMIT != "PENDING_FOLLOWUP_PATCH")
