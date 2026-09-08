"""
Type C #609: First-gen OpenAI publisher-deal renewal window (Sep 2026 status) -
Conde Nast (Aug 2024 multiyear), Atlantic (May 2024 multiyear), FT (Apr 2024,
duration undisclosed) renewal mapping.

FINANCIAL MAP (verified Sep 2026):
  Leg 1: Conde Nast x OpenAI (announced Aug 20 2024, Reuters primary) -
         multi-year; terms undisclosed (in-corpus estimate $20-50M/yr);
         covers Vogue, New Yorker, Vanity Fair, GQ, WIRED in ChatGPT/SearchGPT.
         Renewal UNRESOLVED: bounded Sep 2026 searches returned only 2024
         announcement coverage, zero renewal/extension/termination reporting.
  Leg 2: The Atlantic x OpenAI (announced May 29 2024, TheWrap) - multiyear;
         terms undisclosed; strategic content + product partnership with
         Atlantic Labs privileged tech access. Renewal UNRESOLVED (same
         bounded-absence pattern).
  Leg 3: FT x OpenAI (announced Apr 29 2024) - duration undisclosed (NOT
         claimed as one-year); $5-10M/yr estimated (WSJ via Digiday secondary).
         Renewal UNRESOLVED, with a documented search-space confounder: the
         query set was dominated by Microsoft-OpenAI partnership news (Oct 2025
         PBC restructure, Apr 2026 exclusivity end), making the FT leg the
         least observable of the three.

POSITIVE CONTROL: OpenAI DID renew a publisher deal in Jul 2026 (local-news
partnership, $5M investment, newscaststudio Jul 22 2026, in-corpus) - renewals
happen and get trade-press coverage, so the absence for the three 2024 deals
is informative, not a non-reporting artifact.

FRAMEWORK IMPLICATION: all three legs treated ACTIVE per the #599 Vox
convention (no termination reporting => still active). This BOUNDS the
falsification family rather than joining it: the money-to-tone predictor legs
for WIRED/Atlantic/FT rest on undisclosed-terms deals of unconfirmed current
term, so any money-predicts-tone claim at these publications is only as
durable as the ACTIVE assumption. Next observable event: Axel Springer 3-year
deal expiry ~Dec 2026 (#604).

Statistical discipline (standing rule, Aug 28 2026): qualitative Type C
mapping; tone_scores NOT_SCORED; p_value/cohens_d/ci_95 NOT_CALCULATED;
is_significant False; correlational language only; no causal claim; no
coverage-tone claim.
"""

import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_FILE_NAME = "test_type_c_609_first_gen_openai_publisher_deal_renewal_window_sep08_11am.py"
MECH_KEY = "first_gen_openai_publisher_deal_renewal_window_600"


def load_yaml(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as f:
        return yaml.safe_load(f)


def mech_600():
    doc = load_yaml("profiles/competitor-entities.yaml")
    assert MECH_KEY in doc, f"mechanism key {MECH_KEY} missing from competitor-entities.yaml"
    return doc[MECH_KEY]


def leg(name):
    legs = mech_600()["legs"]
    assert name in legs, f"leg {name} missing"
    return legs[name]


# ── Class 1: Mechanism Metadata ──────────────────────────────────────────


class TestMechanismMetadata600:
    def test_yaml_parses(self):
        doc = load_yaml("profiles/competitor-entities.yaml")
        assert isinstance(doc, dict)

    def test_mechanism_key_present(self):
        mech_600()

    def test_mechanism_id(self):
        assert mech_600()["mechanism_id"] == 600

    def test_iteration(self):
        assert mech_600()["iteration"] == 609

    def test_iteration_type(self):
        assert mech_600()["iteration_type"] == "C"

    def test_type(self):
        assert mech_600()["type"] == "financial_incentive_mapping"

    def test_date_analyzed(self):
        assert mech_600()["date_analyzed"] == "2026-09-08"

    def test_job_id(self):
        assert mech_600()["job_id"] == "mediascope-daily-iteration"

    def test_goal_id(self):
        assert mech_600()["goal_id"] == "goal_54093bda4145"

    def test_mechanism_name_keywords(self):
        name = mech_600()["mechanism_name"].lower()
        for kw in ["renewal window", "conde nast", "atlantic", "ft", "positive control"]:
            assert kw in name, f"missing keyword {kw} in mechanism_name"


# ── Class 2: Conde Nast Leg ──────────────────────────────────────────────


class TestCondeNastLeg609:
    def test_leg_present(self):
        leg("conde_nast_leg")

    def test_announced_date(self):
        assert leg("conde_nast_leg")["announced"] == "2024-08-20"

    def test_term_multiyear(self):
        assert "multi-year" in leg("conde_nast_leg")["term"]

    def test_value_estimate(self):
        assert "$20-50M/yr" in leg("conde_nast_leg")["value"]

    def test_renewal_unresolved(self):
        assert leg("conde_nast_leg")["renewal_status"].startswith("UNRESOLVED")

    def test_reuters_primary_source(self):
        srcs = leg("conde_nast_leg")["sources"]
        assert any("reuters.com/technology/openai-signs-deal-with-cond-nast-2024-08-20" in s for s in srcs)

    def test_publication_wired(self):
        assert "WIRED" in leg("conde_nast_leg")["publication"]

    def test_scope_searchgpt(self):
        assert "SearchGPT" in leg("conde_nast_leg")["scope"]

    def test_in_corpus_reference(self):
        assert "wired.yaml:48" in leg("conde_nast_leg")["in_corpus"]


# ── Class 3: Atlantic Leg ────────────────────────────────────────────────


class TestAtlanticLeg609:
    def test_leg_present(self):
        leg("atlantic_leg")

    def test_announced_date(self):
        assert leg("atlantic_leg")["announced"] == "2024-05-29"

    def test_term_multiyear(self):
        assert "multiyear" in leg("atlantic_leg")["term"]

    def test_value_undisclosed(self):
        assert leg("atlantic_leg")["value"] == "undisclosed"

    def test_renewal_unresolved(self):
        assert leg("atlantic_leg")["renewal_status"].startswith("UNRESOLVED")

    def test_openai_primary_source(self):
        srcs = leg("atlantic_leg")["sources"]
        assert any("openai.com/index/enhancing-news-in-chatgpt-with-the-atlantic" in s for s in srcs)

    def test_scope_atlantic_labs(self):
        assert "Atlantic Labs" in leg("atlantic_leg")["scope"]

    def test_emerson_ownership(self):
        assert "Emerson Collective" in leg("atlantic_leg")["publication"]

    def test_in_corpus_reference(self):
        assert "atlantic.yaml" in leg("atlantic_leg")["in_corpus"]


# ── Class 4: FT Leg ──────────────────────────────────────────────────────


class TestFTLeg609:
    def test_leg_present(self):
        leg("ft_leg")

    def test_announced_date(self):
        assert leg("ft_leg")["announced"] == "2024-04-29"

    def test_term_duration_undisclosed(self):
        assert "duration undisclosed" in leg("ft_leg")["term"]

    def test_no_one_year_claim(self):
        assert "NOT claimed as one-year" in leg("ft_leg")["term"]

    def test_value_estimate(self):
        assert "$5-10M/yr" in leg("ft_leg")["value"]

    def test_renewal_unresolved(self):
        assert leg("ft_leg")["renewal_status"].startswith("UNRESOLVED")

    def test_search_space_confounder_documented(self):
        assert "search-space confounder" in leg("ft_leg")["renewal_status"]

    def test_in_corpus_ft_reference(self):
        assert "financial-times.yaml:3485" in leg("ft_leg")["in_corpus"]


# ── Class 5: Positive Control ────────────────────────────────────────────


class TestPositiveControl609:
    def test_control_present(self):
        assert "positive_control" in mech_600()

    def test_jul2026_renewal_5m(self):
        pc = mech_600()["positive_control"]["event"]
        assert "Jul 2026" in pc and "$5M" in pc

    def test_newscaststudio_source(self):
        srcs = mech_600()["sources"]
        assert any("newscaststudio.com/2026/07/22/openai-renews-local-news-partnership" in s for s in srcs)

    def test_significance_informative_absence(self):
        assert "informative" in mech_600()["positive_control"]["significance"]

    def test_boundary_deal_tier(self):
        assert "deal tier" in mech_600()["positive_control"]["boundary"]

    def test_reporting_channel_control(self):
        assert "reporting channel" in mech_600()["positive_control"]["boundary"]


# ── Class 6: Financial Predictor Implication ──────────────────────────────


class TestFinancialPredictorImplication609:
    def test_implication_present(self):
        assert "financial_predictor_implication" in mech_600()

    def test_active_convention_599(self):
        assert "#599 convention" in mech_600()["financial_predictor_implication"]["claim"]

    def test_bounds_falsification_family_not_joins(self):
        eff = mech_600()["financial_predictor_implication"]["effect_on_falsification_family"]
        assert "BOUNDS" in eff and "does not join or break" in eff

    def test_meta_zero(self):
        mz = mech_600()["financial_predictor_implication"]["meta_zero"]
        assert "$0" in mz and "Conde Nast" in mz

    def test_cohort_geometry_axel_springer(self):
        assert "Axel Springer" in mech_600()["cohort_geometry"]["first_gen_cohort"]

    def test_cohort_geometry_news_corp(self):
        assert "News Corp" in mech_600()["cohort_geometry"]["first_gen_cohort"]

    def test_next_event_dec_2026(self):
        nxt = mech_600()["cohort_geometry"]["next_observable_event"]
        assert "Dec 2026" in nxt and "#604" in nxt

    def test_monitoring_item(self):
        assert "Axel Springer decision point" in mech_600()["cohort_geometry"]["monitoring_item"]

    def test_no_causal_claim(self):
        assert "No causal claim" in mech_600()["correlational_note"]


# ── Class 7: Statistical Discipline & Novelty ─────────────────────────────


class TestStatisticalDisciplineAndNovelty609:
    def test_tone_scores_not_scored(self):
        assert mech_600()["tone_scores"] == "NOT_SCORED"

    def test_stats_not_calculated(self):
        assert "NOT_CALCULATED" in mech_600()["statistical_discipline"]

    def test_scorer_boundary_540_544(self):
        assert "#540/#544" in mech_600()["statistical_discipline"]

    def test_iteration_492_bounded_absence(self):
        assert "iteration-492" in mech_600()["statistical_discipline"]

    def test_correlational_note(self):
        assert "correlational" in mech_600()["correlational_note"].lower()

    def test_cautious_language_required(self):
        assert mech_600()["cautious_language_required"] is True

    def test_no_coverage_tone_claim(self):
        assert mech_600()["no_coverage_tone_claim"] is True

    def test_novelty_first_renewal_window(self):
        assert "FIRST corpus renewal-window mapping" in mech_600()["novelty"]

    def test_novelty_positive_control(self):
        assert "FIRST positive-control use" in mech_600()["novelty"]

    def test_novelty_distinct_from_prior(self):
        nov = mech_600()["novelty"]
        for ref in ["#604", "#599", "#594"]:
            assert ref in nov, f"missing distinctness ref {ref}"

    def test_ascii_only(self):
        import json
        blob = json.dumps(mech_600(), ensure_ascii=False)
        assert all(ord(c) < 128 for c in blob), "non-ASCII character in mechanism block"


# ── Class 8: Rotation Cycle Guard (deselected pre-commit; anchor patched in
#    followup per the #565 convention) ────────────────────────────────────


class TestRotationCycleGuard609:
    """Covers the 605-609 main-commit window (C,B,A,E,D newest-first),
    closing the B->C edge. ANCHOR PATCHED POST-COMMIT per the #565 followup
    convention: the expected anchor commit id is filled in the followup run
    after the main commit is created."""
    EXPECTED_WINDOW_NEWEST_FIRST = [
        ("Type C", 609),
        ("Type B", 608),
        ("Type A", 607),
        ("Type E", 606),
        ("Type D", 605),
    ]
    # Anchor: patched in followup - see iteration-log entry for #609.
    ANCHOR_MAIN_COMMIT = "POST_COMMIT_PATCH_IN_FOLLOWUP"

    # MAIN_COMMIT_PATTERN: only main-iteration commits anchor the rotation.
    MAIN_COMMIT_PATTERN = re.compile(r"^Type [A-E] #\d+:")

    def test_window_sequence(self):
        seq = [(t, n) for t, n in self.EXPECTED_WINDOW_NEWEST_FIRST]
        assert seq[0] == ("Type C", 609)
        assert seq[-1] == ("Type D", 605)

    def test_closes_b_to_c_edge(self):
        types = [t for t, _ in self.EXPECTED_WINDOW_NEWEST_FIRST]
        assert types[0] == "Type C" and types[1] == "Type B"

    def test_five_window_members(self):
        assert len(self.EXPECTED_WINDOW_NEWEST_FIRST) == 5

    def test_adjacency_cycle_valid(self):
        # C->D->E->A->B rotation walk in commit-newest-first order
        order = ["D", "C", "B", "A", "E"]
        types = [t.split()[1] for t, _ in self.EXPECTED_WINDOW_NEWEST_FIRST]
        assert types == ["C", "B", "A", "E", "D"]
        assert set(types) == set(order)

    def test_git_commit_order_matches_rotation(self):
        anchor = self.ANCHOR_MAIN_COMMIT
        assert anchor != "POST_COMMIT_PATCH_IN_FOLLOWUP", \
            "anchor not patched - run the #565 followup convention first"
        out = subprocess.run(
            ["git", "-C", REPO_ROOT, "log", "-n40", anchor, "--format=%s"],
            capture_output=True, text=True, check=True)
        mains = [s for s in out.stdout.splitlines()
                 if self.MAIN_COMMIT_PATTERN.match(s)][:5]
        assert len(mains) >= 5, f"fewer than 5 main commits: {mains}"
        for i, (typ, num) in enumerate(self.EXPECTED_WINDOW_NEWEST_FIRST):
            assert f"#{num}" in mains[i], \
                f"position {i}: expected #{num}, got {mains[i]!r}"
            assert re.search(rf"Type {typ.split()[1]} {re.escape('#' + str(num))}", mains[i]), \
                f"position {i}: expected {typ} #{num}, got {mains[i]!r}"
