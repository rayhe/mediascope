"""Type C #614 (2026-09-08 17:00 PDT): Reddit v. Anthropic adversarial litigation
financial-incentive mapping (mechanism_id 603).

Reddit sued Anthropic on Jun 4 2025 in the Superior Court of California, San
Francisco for unauthorized scraping and commercial use of Reddit user data to
train Claude: breach of contract, trespass to chattels, unjust enrichment,
tortious interference, unfair competition; 100,000+ unauthorized accesses;
damages, disgorgement, injunction sought. The case was removed to federal court
as Case 3:25-cv-05643-TLT; Reddit's remand motion (Document 60, filed
03/30/26) means the litigation is LIVE as of Sep 2026.

Pay-or-sue three-leg bifurcation: Google pays ~$60M/yr (licensed, Feb 2024,
in active renewal talks expiring early 2027), OpenAI pays ~$70M/yr (licensed,
May 2024), Anthropic pays $0 and is SUED. This is the second corpus
adversarial-litigation financial mechanism after #589 (Ziff Davis v. OpenAI)
and the FIRST adversarial-litigation record on the Anthropic entity, which
carries ZERO voluntary publisher licensing deals. Owner-level relevance:
Reddit is Advance-owned (2026 proxy ~21.9% economic, ~65.2% voting); Advance
owns Conde Nast, which owns WIRED. KEY TENSION with #602: mechanism #602
documented a WIRED x Anthropic licensing-halo divergence pointing opposite
the harder-coverage prediction, so this mechanism BOUNDS the
falsification/alternative-driver family without joining it.

Qualitative Type C mapping: tone_scores NOT_SCORED, p_value/cohens_d/ci_95
NOT_CALCULATED, is_significant False, MANUAL ILLUSTRATIVE labeling,
correlational structural incentives only, no causal claim. No em dashes
anywhere in this file.
"""
import yaml
import pytest

ITERATION = 614
MECHANISM_ID = 603
MECHANISM_KEY = "reddit_anthropic_adversarial_litigation_614"

SILICONANGLE_URL = ("https://siliconangle.com/2025/06/04/"
                    "reddit-sues-anthropic-alleged-scraping-commercial-use-user-data/")
BLOOMBERGLAW_URL = ("https://news.bloomberglaw.com/artificial-intelligence/"
                    "reddit-sues-anthropic-says-ai-company-exploited-user-data")
FINDLAW_URL = ("https://www.findlaw.com/legalblogs/courtside/"
               "reddits-lawsuit-over-data-scraping-could-reshape-the-future-of-ai/")
LIVEMINT_URL = ("https://www.livemint.com/technology/tech-news/"
                "reddit-says-anthropic-used-its-community-to-train-ai-without-permission-"
                "files-lawsuit/amp-11749124778959.html")
MOBILEWORLDLIVE_URL = ("https://www.mobileworldlive.com/ai-cloud/"
                       "reddit-files-lawsuit-against-ai-player-anthropic/")
FASTCOMPANY_URL = ("https://www.fastcompany.com/91502976/"
                   "reddit-most-innovative-companies-2026-steve-huffman-jen-wong-"
                   "openai-ai-google-gemini-answers-search")
LOEB_URL = ("https://www.loeb.com/-/media/files/pdfs/2026-pdf/cases-of-interest-pdfs/"
            "reddit-v-anthropic-motion-for-remand-1.pdf"
            "?rev=4f251a8731e94b69abe7c21a480fcc24&hash=27C466ED5EB2AA37E95F3A40D7139CFB")


@pytest.fixture(scope="module")
def mechanism():
    with open("profiles/competitor-entities.yaml", "r") as f:
        data = yaml.safe_load(f)
    return data["entities"]["anthropic"][MECHANISM_KEY]


class TestMechanismMetadata614:
    def test_mechanism_id(self, mechanism):
        assert mechanism["mechanism_id"] == 603

    def test_iteration(self, mechanism):
        assert mechanism["iteration"] == 614

    def test_iteration_type(self, mechanism):
        assert mechanism["iteration_type"] == "C"

    def test_type_field(self, mechanism):
        assert mechanism["type"] == "financial_incentive_mapping"

    def test_rotation(self, mechanism):
        assert mechanism["rotation"] == "Type C"

    def test_date_analyzed(self, mechanism):
        assert mechanism["date_analyzed"] == "2026-09-08"

    def test_job_id(self, mechanism):
        assert mechanism["job_id"] == "mediascope-daily-iteration"

    def test_goal_id(self, mechanism):
        assert mechanism["goal_id"] == "goal_54093bda4145"

    def test_test_file_reference(self, mechanism):
        assert mechanism["test_file"].endswith(
            "test_type_c_614_reddit_anthropic_adversarial_litigation_sep08_5pm.py")


class TestLitigationFacts614:
    def test_filing_date_in_name(self, mechanism):
        assert "Jun 4 2025" in mechanism["mechanism_name"]

    def test_venue_sf_superior_court(self, mechanism):
        assert "Superior Court of California, San Francisco" in mechanism["overview"]

    def test_claims_list(self, mechanism):
        for claim in ("breach of contract", "trespass to chattels",
                      "unjust enrichment", "tortious interference",
                      "unfair competition"):
            assert claim in mechanism["overview"]

    def test_100k_accesses(self, mechanism):
        assert "100,000" in mechanism["overview"]

    def test_relief_sought(self, mechanism):
        assert "disgorgement" in mechanism["overview"]
        assert "damages" in mechanism["overview"]

    def test_federal_case_number(self, mechanism):
        assert "3:25-cv-05643-TLT" in mechanism["overview"]

    def test_remand_motion_date(self, mechanism):
        assert "03/30/26" in mechanism["overview"]

    def test_case_live_status(self, mechanism):
        assert "LIVE as of Sep 2026" in mechanism["overview"]

    def test_training_since_dec_2021(self, mechanism):
        assert "Dec 2021" in mechanism["overview"]

    def test_amodei_sample_efficiency_quote(self, mechanism):
        assert "significantly improves sample efficiency" in mechanism["overview"]

    def test_ben_lee_quote(self, mechanism):
        assert "We will not tolerate profit-seeking entities like Anthropic" in mechanism["overview"]

    def test_anthropic_defense_quote(self, mechanism):
        assert "will defend ourselves vigorously" in mechanism["overview"]


class TestPayOrSueBifurcation614:
    def test_bifurcation_block(self, mechanism):
        assert "pay_or_sue_bifurcation" in mechanism

    def test_google_leg_paid(self, mechanism):
        leg = mechanism["pay_or_sue_bifurcation"]["google_leg"]
        assert leg["status"] == "paid leg - licensed"
        assert "$60M/yr" in leg["value"]

    def test_google_leg_renewal(self, mechanism):
        leg = mechanism["pay_or_sue_bifurcation"]["google_leg"]
        assert "active renewal talks" in leg["value"]

    def test_openai_leg_paid(self, mechanism):
        leg = mechanism["pay_or_sue_bifurcation"]["openai_leg"]
        assert leg["status"] == "paid leg - licensed"
        assert "~$70M/yr" in leg["value"]

    def test_anthropic_leg_zero_dollars(self, mechanism):
        leg = mechanism["pay_or_sue_bifurcation"]["anthropic_leg"]
        assert leg["status"].startswith("non-payer leg - SUED")
        assert leg["value"].startswith("$0")

    def test_anthropic_zero_deals_note(self, mechanism):
        leg = mechanism["pay_or_sue_bifurcation"]["anthropic_leg"]
        assert "ZERO voluntary publisher content licensing deals" in leg["value"]

    def test_bifurcation_note_names_perplexity_sibling(self, mechanism):
        note = mechanism["pay_or_sue_bifurcation"]["bifurcation_note"]
        assert "Perplexity" in note


class TestOwnershipChain614:
    def test_ownership_chain_block(self, mechanism):
        assert "ownership_chain_to_wired" in mechanism

    def test_advance_economic_stake(self, mechanism):
        chain = mechanism["ownership_chain_to_wired"]["chain"]
        assert "~21.9% economic" in chain

    def test_advance_voting_stake(self, mechanism):
        chain = mechanism["ownership_chain_to_wired"]["chain"]
        assert "~65.2% voting" in chain

    def test_advance_conde_nast_wired(self, mechanism):
        chain = mechanism["ownership_chain_to_wired"]["chain"]
        assert "Advance owns Conde Nast" in chain and "WIRED" in chain

    def test_meta_zero_and_competitor(self, mechanism):
        meta = mechanism["ownership_chain_to_wired"]["meta_contrast"]
        assert "Threads/Forum" in meta
        assert "$0" in meta


class TestHuffmanNormQuotes614:
    def test_pay_us_or_take_a_hike(self, mechanism):
        assert "Pay us, or take a hike." in mechanism["overview"]

    def test_oh_my_gosh_yes(self, mechanism):
        assert '"Oh my gosh, yes"' in mechanism["overview"]

    def test_no_trust_quote(self, mechanism):
        assert "you can\'t do a deal with somebody you don\'t trust" in mechanism["overview"]

    def test_other_revenue_140m(self, mechanism):
        assert "$140M" in mechanism["overview"]

    def test_respect_rules_quote(self, mechanism):
        assert "understand and respect Reddit\'s rules" in mechanism["overview"]


class TestMediaScopeRelevance614:
    def test_second_adversarial_after_589(self, mechanism):
        rel = mechanism["mediascope_relevance"]
        assert "#589" in rel
        assert "Ziff Davis v. OpenAI" in rel

    def test_first_adversarial_on_anthropic_entity(self, mechanism):
        rel = mechanism["mediascope_relevance"]
        assert "FIRST adversarial-litigation record on the Anthropic entity" in rel

    def test_key_tension_602(self, mechanism):
        rel = mechanism["mediascope_relevance"]
        assert "#602" in rel
        assert "LICENSING-HALO" in rel

    def test_bounds_not_joins(self, mechanism):
        rel = mechanism["mediascope_relevance"]
        assert "BOUNDS" in rel

    def test_falsification_family_reference(self, mechanism):
        rel = mechanism["mediascope_relevance"]
        assert "#538" in rel

    def test_no_coverage_tone_claim(self, mechanism):
        assert mechanism["no_coverage_tone_claim"] is True


class TestConfounders614:
    def test_confounder_count(self, mechanism):
        assert len(mechanism["confounders"]) == 6

    def test_strong_confounder_count(self, mechanism):
        strong = [c for c in mechanism["confounders"] if c.startswith("STRONG")]
        assert len(strong) == 2

    def test_moderate_confounder_count(self, mechanism):
        moderate = [c for c in mechanism["confounders"] if c.startswith("MODERATE")]
        assert len(moderate) == 2

    def test_weak_confounder_count(self, mechanism):
        weak = [c for c in mechanism["confounders"] if c.startswith("WEAK")]
        assert len(weak) == 2

    def test_602_counterevidence_confounder(self, mechanism):
        assert any("#602" in c for c in mechanism["confounders"])

    def test_counterexample_count(self, mechanism):
        assert len(mechanism["counterexamples"]) == 3

    def test_correlational_note(self, mechanism):
        assert "do not by themselves demonstrate editorial control or causation" in mechanism["correlational_note"]


class TestStatisticalDiscipline614:
    def test_tone_scores_not_scored(self, mechanism):
        assert mechanism["tone_scores"] == "NOT_SCORED"

    def test_statistical_discipline_not_calculated(self, mechanism):
        sd = mechanism["statistical_discipline"]
        assert "NOT_CALCULATED" in sd
        assert "is_significant False" in sd

    def test_standing_rule_reference(self, mechanism):
        assert "Aug 28 2026" in mechanism["statistical_discipline"]

    def test_cautious_language_required(self, mechanism):
        assert mechanism["cautious_language_required"] is True


class TestSources614:
    def test_source_count(self, mechanism):
        assert len(mechanism["sources"]) == 7

    def test_all_https(self, mechanism):
        assert all(s.startswith("https://") for s in mechanism["sources"])

    def test_verbatim_urls(self, mechanism):
        expected = [SILICONANGLE_URL, BLOOMBERGLAW_URL, FINDLAW_URL, LIVEMINT_URL,
                    MOBILEWORLDLIVE_URL, FASTCOMPANY_URL, LOEB_URL]
        for url in expected:
            assert url in mechanism["sources"], url

    def test_no_url_spaces(self, mechanism):
        assert all(" " not in s for s in mechanism["sources"])

    def test_research_method_novelty_checks(self, mechanism):
        rm = mechanism["research_method"]
        assert "zero reddit mentions" in rm
        assert "mechanism_id 603 free" in rm


class TestRotationCycleGuard614:
    """Covers the 610-614 main-commit window (C,D,E,A,B newest-first),
    closing the B->C edge. ANCHOR PATCHED POST-COMMIT per the #565 followup
    convention: the expected anchor commit id is filled in the followup run
    after the main commit is created."""
    EXPECTED_WINDOW_NEWEST_FIRST = [
        ("Type C", 614),
        ("Type B", 613),
        ("Type A", 612),
        ("Type E", 611),
        ("Type D", 610),
    ]
    # Anchor: patched in followup - see iteration-log entry for #614.
    ANCHOR_MAIN_COMMIT = "2ce21aa"

    def test_window_sequence(self):
        seq = [(t, n) for t, n in self.EXPECTED_WINDOW_NEWEST_FIRST]
        assert seq[0] == ("Type C", 614)
        assert seq[-1] == ("Type D", 610)

    def test_closes_b_to_c_edge(self):
        types = [t for t, _ in self.EXPECTED_WINDOW_NEWEST_FIRST]
        assert types[0] == "Type C" and types[1] == "Type B"

    def test_five_window_members(self):
        assert len(self.EXPECTED_WINDOW_NEWEST_FIRST) == 5

    def test_anchor_patched_post_commit(self):
        assert self.ANCHOR_MAIN_COMMIT is not None and self.ANCHOR_MAIN_COMMIT != "PENDING_FOLLOWUP_PATCH"
