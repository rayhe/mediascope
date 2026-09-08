"""
Type C #604: Axel Springer dual-AI-payer architecture (Sep 2026 status) -
Microsoft four-channel partnership (Apr 29 2024) formalized; KKR-split
ownership correction (finalized Apr 29 2025); Telegraph Media Group
acquisition closed Jun 30 2026 (GBP 575M); OpenAI 3-year deal expiry Dec 2026
with renewal UNRESOLVED; Business Insider control-case persistence.

FINANCIAL MAP (verified Sep 2026):
  Leg 1: Axel Springer-OpenAI content licensing (Dec 13 2023, 3-year, tens of
         millions EUR across the deal per Bloomberg Law source-familiar; NOT
         per year). Expires ~Dec 2026; renewal UNRESOLVED (bounded searches
         surfaced no renewal/extension/termination reporting).
  Leg 2: Axel Springer-Microsoft four-channel partnership (Apr 29 2024,
         PR Newswire): adtech, AI chat pilot + Chat Ads API, Start-MSN content,
         Azure SAP migration. FIRST corpus formalization. Makes Axel Springer
         dual-AI-payer (OpenAI + Microsoft).
  Leg 3 (CORRECTED): KKR PE-ownership leg of mechanism 143's triple-layer is
         REMOVED for the media business - KKR split finalized Apr 29 2025
         (Reuters): media (Bild, Politico, BI, Welt) closely held by CEO
         Mathias Doepfner and Friede Springer; KKR/CPP Investments hold the
         classifieds (Stepstone, Aviv) majority. Corpus majority-owned-by-KKR
         wording was stale as of Apr 2025; corrected with dated notes,
         mechanism 143 preserved as historical record.
  Leg 4 (NEW): Telegraph Media Group acquisition CLOSED Jun 30 2026, GBP 575M
         (Reuters) - second-largest Axel Springer investment since 1946;
         Doepfner ties it to AI-powered digital transformation. NEW TO CORPUS.
  Meta: $0 AI licensing with Axel Springer (in-corpus).

BEHAVIORAL PIN: Business Insider in-corpus control case persists - OpenAI -0.42
(deal partner, HARDEST, #399); Anthropic +0.12 ($0, aspirational, #420);
Meta +0.08 ($0, product-execution, #399/#420); Google -0.075 ($0, chase-deficit,
#542). With TWO AI payers (OpenAI licensing + Microsoft partnership) the money
predicts OpenAI/Microsoft softest, but the observed pattern has OpenAI hardest.
The control case against financial determinism STANDS and is now cleaner - the
payer set is correctly identified. MANUAL ILLUSTRATIVE context only; no new tone
arrays scored this run (standing rule Aug 28 2026).

Statistical discipline (standing rule, Aug 28 2026): qualitative Type C mapping;
tone_scores NOT_SCORED; p_value/cohens_d/ci_95 NOT_CALCULATED; is_significant
False; correlational language only; no causal claim; no coverage-tone claim.
"""

import os
import re
import subprocess

import pytest
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEST_FILE_NAME = "test_type_c_604_axel_springer_dual_ai_payer_microsoft_kkr_split_telegraph_sep08_6am.py"
MECH_KEY = "axel_springer_dual_ai_payer_microsoft_four_channel_kkr_split_telegraph_597"


def load_yaml(rel):
    with open(os.path.join(REPO_ROOT, rel), encoding="utf-8") as f:
        return yaml.safe_load(f)


def mech_597():
    doc = load_yaml("profiles/competitor-entities.yaml")
    assert MECH_KEY in doc, f"mechanism key {MECH_KEY} missing from competitor-entities.yaml"
    return doc[MECH_KEY]


def axel_springer_entity():
    doc = load_yaml("profiles/competitor-entities.yaml")
    ent = doc.get("publisher_entities", {}).get("axel_springer_business_insider")
    assert ent, "axel_springer_business_insider missing from publisher_entities"
    return ent


def bi_doc():
    return load_yaml("profiles/business-insider.yaml")


# ── Class 1: Mechanism Metadata ──────────────────────────────────────────


class TestMechanismMetadata597:
    def test_yaml_parses(self):
        doc = load_yaml("profiles/competitor-entities.yaml")
        assert isinstance(doc, dict)

    def test_mechanism_key_present(self):
        mech_597()

    def test_mechanism_id(self):
        assert mech_597()["mechanism_id"] == 597

    def test_iteration(self):
        assert mech_597()["iteration"] == 604

    def test_iteration_type(self):
        assert mech_597()["iteration_type"] == "C"

    def test_type(self):
        assert mech_597()["type"] == "financial_incentive_mapping"

    def test_date_analyzed(self):
        assert mech_597()["date_analyzed"] == "2026-09-08"

    def test_job_id(self):
        assert mech_597()["job_id"] == "mediascope-daily-iteration"

    def test_goal_id(self):
        assert mech_597()["goal_id"] == "goal_54093bda4145"

    def test_mechanism_name_keywords(self):
        name = mech_597()["mechanism_name"].lower()
        for kw in ["dual-ai-payer", "microsoft", "kkr", "telegraph", "openai"]:
            assert kw in name, f"missing keyword {kw} in mechanism_name"


# ── Class 2: OpenAI Leg (expiry mapping) ─────────────────────────────────


class TestOpenAILeg604:
    def test_announced_date(self):
        assert mech_597()["legs"]["openai_leg"]["announced"] == "2023-12-13"

    def test_three_year_term(self):
        assert "3-year" in mech_597()["legs"]["openai_leg"]["term"]

    def test_expiry_window(self):
        assert mech_597()["legs"]["openai_leg"]["expiry"] == "~2026-12"

    def test_renewal_unresolved(self):
        leg = mech_597()["legs"]["openai_leg"]
        assert "UNRESOLVED" in leg["renewal_status"]

    def test_not_per_year_wording(self):
        leg = mech_597()["legs"]["openai_leg"]
        assert "NOT" in leg["value"] and "year" in leg["value"].lower()

    def test_expiry_mapping_section(self):
        mapping = mech_597()["openai_expiry_renewal_mapping"]
        assert mapping["expiry_window"] == "~Dec 2026 (approx 3 months from Sep 8 2026)"
        assert "UNRESOLVED" in mapping["status"]
        assert "disclosed, not claimed" in mapping["status"]

    def test_bounded_absence_language(self):
        mapping = mech_597()["openai_expiry_renewal_mapping"]
        assert "bounded Sep 2026 searches" in mapping["renewal_search"]
        assert "NO renewal" in mapping["renewal_search"]


# ── Class 3: Microsoft Leg (four-channel formalization) ──────────────────


class TestMicrosoftLeg604:
    def test_announced_date(self):
        assert mech_597()["legs"]["microsoft_leg"]["announced"] == "2024-04-29"

    def test_pr_newswire_form(self):
        assert "PR Newswire" in mech_597()["legs"]["microsoft_leg"]["form"]

    def test_channel_1_adtech(self):
        ch = mech_597()["legs"]["microsoft_leg"]["channel_1_adtech"]
        assert "Microsoft Advertising" in ch and "POLITICO" in ch

    def test_channel_2_ai(self):
        ch = mech_597()["legs"]["microsoft_leg"]["channel_2_ai"]
        assert "Chat Ads API" in ch and "Azure OpenAI" in ch

    def test_channel_3_content(self):
        ch = mech_597()["legs"]["microsoft_leg"]["channel_3_content"]
        assert "Business Insider" in ch and "Start-MSN" in ch

    def test_channel_4_cloud(self):
        ch = mech_597()["legs"]["microsoft_leg"]["channel_4_cloud"]
        assert "Azure" in ch

    def test_first_corpus_formalization(self):
        sig = mech_597()["legs"]["microsoft_leg"]["significance"]
        assert "FIRST corpus formalization" in sig

    def test_dual_ai_payer_significance(self):
        sig = mech_597()["legs"]["microsoft_leg"]["significance"]
        assert "dual-AI-payer" in sig

    def test_pr_newswire_source_url(self):
        urls = mech_597()["sources"]
        assert any("prnewswire.co.uk" in u and "302128889" in u for u in urls), \
            "PR Newswire Apr 29 2024 partnership URL missing from sources"


# ── Class 4: KKR-Split Ownership Correction ─────────────────────────────


class TestOwnershipCorrection604:
    def test_split_finalized_date(self):
        corr = mech_597()["legs"]["ownership_correction"]
        assert "Apr 29 2025" in corr["correction"]

    def test_doepfner_friede_springer(self):
        corr = mech_597()["legs"]["ownership_correction"]
        assert "Doepfner" in corr["correction"] and "Friede Springer" in corr["correction"]

    def test_kkr_classifieds_majority(self):
        corr = mech_597()["legs"]["ownership_correction"]
        assert "CPP Investments" in corr["correction"] and "classifieds" in corr["correction"]

    def test_kkr_leg_removed_for_media(self):
        corr = mech_597()["legs"]["ownership_correction"]
        assert "REMOVED" in corr["effect"]

    def test_mechanism_143_preserved(self):
        corr = mech_597()["legs"]["ownership_correction"]
        assert "historical record" in corr["effect"]

    def test_entity_parent_company_corrected(self):
        parent = axel_springer_entity()["parent_company"]
        assert "Axel Springer" in parent
        assert "majority-owned by KKR" not in parent, \
            "stale majority-owned-by-KKR wording still present in parent_company"

    def test_entity_correction_note_present(self):
        assert "ownership_correction_2026_09_08" in axel_springer_entity()

    def test_entity_pe_owner_status_removed(self):
        status = axel_springer_entity()["pe_owner"]["status"]
        assert "REMOVED" in status and "Apr 29 2025" in status

    def test_reuters_split_sources(self):
        corr = mech_597()["legs"]["ownership_correction"]["sources"]
        assert any("axel-springer-split-deal-with-kkr-2024-09-19" in u for u in corr)
        assert any("finalize-division-of-media-group" in u for u in corr)

    def test_bi_profile_ownership_correction(self):
        assert "ownership_correction_2026_09_08" in bi_doc()


# ── Class 5: Telegraph Acquisition ────────────────────────────────────────


class TestTelegraphAcquisition604:
    def test_closed_date(self):
        assert mech_597()["legs"]["telegraph_acquisition"]["closed"] == "2026-06-30"

    def test_value(self):
        assert "575M" in mech_597()["legs"]["telegraph_acquisition"]["value"]

    def test_new_to_corpus(self):
        sig = mech_597()["legs"]["telegraph_acquisition"]["significance"]
        assert "NEW TO CORPUS" in sig

    def test_ai_transformation_quote(self):
        sig = mech_597()["legs"]["telegraph_acquisition"]["significance"]
        assert "AI-powered digital transformation" in sig

    def test_reuters_close_source(self):
        srcs = mech_597()["legs"]["telegraph_acquisition"]["sources"]
        assert any("closes-acquisition-telegraph-media-group-2026-06-30" in u for u in srcs)

    def test_entity_publications_include_telegraph(self):
        pubs = axel_springer_entity()["publications"]
        assert any("Telegraph" in p for p in pubs)


# ── Class 6: BI Control-Case Persistence ─────────────────────────────────


class TestBIControlCase604:
    def test_in_corpus_scores_cited(self):
        ctx = mech_597()["bi_control_case_persistence"]["in_corpus_scores"]
        for token in ["-0.42", "+0.12", "+0.08", "-0.075"]:
            assert token in ctx, f"missing in-corpus score {token}"

    def test_openai_hardest_noted(self):
        ctx = mech_597()["bi_control_case_persistence"]["in_corpus_scores"]
        assert "HARDEST" in ctx

    def test_control_case_stands(self):
        impl = mech_597()["bi_control_case_persistence"]["implication"]
        assert "STANDS" in impl

    def test_no_new_tone_arrays(self):
        impl = mech_597()["bi_control_case_persistence"]["implication"]
        assert "no new tone arrays scored this run" in impl

    def test_falsification_family(self):
        fam = mech_597()["bi_control_case_persistence"]["falsification_family"]
        assert "#599" in fam

    def test_bi_profile_microsoft_entry(self):
        ms = bi_doc()["competitor_relationships"]["microsoft"]
        assert ms["financial_tie"] == "strategic_partnership_via_parent"
        assert ms["verification_date"] == "2026-09-08"

    def test_meta_zero(self):
        assert "$0" in mech_597()["meta_zero"]["status"]


# ── Class 7: Statistical Discipline + Novelty ────────────────────────────


class TestStatisticalDisciplineAndNovelty604:
    def test_tone_scores_not_scored(self):
        assert mech_597()["tone_scores"] == "NOT_SCORED"

    def test_no_causal_claim(self):
        assert mech_597()["no_coverage_tone_claim"] is True
        assert "No causal claim" in mech_597()["correlational_note"]

    def test_correlational_language(self):
        note = mech_597()["correlational_note"].lower()
        assert "correlational" in note

    def test_p_value_not_calculated(self):
        disc = mech_597()["statistical_discipline"]
        assert "NOT_CALCULATED" in disc

    def test_scorer_boundary(self):
        disc = mech_597()["statistical_discipline"]
        assert "#540/#544 boundary" in disc

    def test_novelty_firsts(self):
        nov = mech_597()["novelty"]
        assert nov.count("FIRST") >= 4, f"expected >=4 FIRST claims, got: {nov[:120]}"

    def test_novelty_distinct_from_143(self):
        assert "mechanism 143" in mech_597()["novelty"]

    def test_all_source_urls_http(self):
        for u in mech_597()["sources"]:
            assert u.startswith("https://"), f"non-https source: {u}"

    def test_no_constructed_urls(self):
        # every source URL must be verbatim from the run's Full-URL listings
        known = [
            "prnewswire.co.uk",
            "reuters.com/legal/transactional/germanys-axel-springer-closes-acquisition-telegraph-media-group-2026-06-30",
            "reuters.com/markets/deals/german-media-empire-axel-springer-split-deal-with-kkr-2024-09-19",
            "947thebeast.com/2025/04/29/axel-springer-and-kkr-finalize-division-of-media-group",
            "fipp.com/news/axel-springer-announces-new-corporate-structure",
            "thetimes.com/business/companies-markets/article/axel-springer-completes-575m-telegraph-takeover-pzgx8ghhh",
            "news.bloomberglaw.com/tech-and-telecom-law/openai-to-pay-axel-springer-tens-of-millions-to-use-news-content",
            "axelspringer.com/en/press-releases/axel-springer-and-openai-partner-to-deepen-beneficial-use-of-ai-in-journalism",
            "llmpulse.ai/blog/ai-content-licensing-deals",
        ]
        for u in mech_597()["sources"]:
            assert any(k in u for k in known), f"source not from run's URL listings: {u}"


# ── Class 8: Rotation-Cycle Guard ────────────────────────────────────────


class TestRotationCycleGuard604:
    """Covers the 600-604 main-commit window (C,B,A,E,D newest-first),
    closing the B->C edge. ANCHOR PATCHED POST-COMMIT per the #565 followup
    convention: the expected anchor commit id is filled in the followup run
    after the main commit is created."""
    EXPECTED_WINDOW_NEWEST_FIRST = [
        ("Type C", 604),
        ("Type B", 603),
        ("Type A", 602),
        ("Type E", 601),
        ("Type D", 600),
    ]
    # Anchor: patched in followup - see iteration-log entry for #604.
    ANCHOR_MAIN_COMMIT = "7c8cf66"

    # MAIN_COMMIT_PATTERN: only main-iteration commits anchor the rotation.
    MAIN_COMMIT_PATTERN = re.compile(r"^Type [A-E] #\d+:")

    def test_window_sequence(self):
        seq = [(t, n) for t, n in self.EXPECTED_WINDOW_NEWEST_FIRST]
        assert seq[0] == ("Type C", 604)
        assert seq[-1] == ("Type D", 600)

    def test_closes_b_to_c_edge(self):
        types = [t for t, _ in self.EXPECTED_WINDOW_NEWEST_FIRST]
        assert types[0] == "Type C" and types[1] == "Type B"

    def test_five_window_members(self):
        assert len(self.EXPECTED_WINDOW_NEWEST_FIRST) == 5

    def test_adjacency_cycle_valid(self):
        # D->C->B->A->E->D rotation walk in commit-newest-first order
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
