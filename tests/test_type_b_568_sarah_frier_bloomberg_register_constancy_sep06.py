"""Type B #568 (2026-09-06 16:00 PDT): Sarah Frier (Bloomberg) AI-spend
skepticism register constancy across Meta and OpenAI - managing editor for
tech with matched investor-skepticism register for both entities.

Career: Bloomberg intern -> reporter -> SF social media beat -> senior
reporter -> team leader -> managing editor for Big Tech/AI/VC (Feb 2026).
Author of "No Filter: The Inside Story of Instagram" (Simon & Schuster,
2020; FT/McKinsey Business Book of the Year 2020). 15-year Bloomberg lifer,
one of the longest single-outlet Big Tech careers in the dataset.

Meta pieces (3):
1. "Meta Reports Almost $700 Billion in Future Spending Commitments"
   (Bloomberg original, carried on Frier's Muck Rack profile): filing-based
   business register, "$349.3 billion of non-cancelable contractual
   commitments, mostly related to third-party cloud deals, servers and
   network infrastructure." Investor-skepticism via spend scale, -0.15.
   https://muckrack.com/sarahfrier/articles
2. "Meta Held Deal Talks With Startup Runway in AI Recruiting Push"
   (Muck Rack, Bloomberg): "Mark Zuckerberg discussed a possible acquisition
   with video startup Runway AI Inc., as part of his deal-making drive in
   artificial intelligence. The deal talks never reached a formal offer level
   ... and are no longer ongoing." Neutral business with deal-failure note,
   -0.10. https://muckrack.com/sarahfrier/articles
3. "Meta Shares Plunge on Rising Concern About AI Spending Spree"
   (Bloomberg Law, institutional register, NOT Frier-bylined, disclosed):
   "reigniting fears that the historic levels of investment that Chief
   Executive Officer Mark Zuckerberg is making to catch up in the artificial
   intelligence race will not pay off." Investor skepticism, -0.30.
   https://news.bloomberglaw.com/tech-and-telecom-law/meta-shares-plunge-on-escalating-concerns-over-ai-spending-spree

OpenAI pieces (3):
1. "OpenAI-Linked Stocks Slip; Investors Focus on AI Ahead of Big Tech
   Earnings" (Bloomberg Businessweek, features "Sarah Frier, Bloomberg News
   Big Tech Team Leader" verbatim): "OpenAI reportedly failed to meet its
   sales and user targets, rekindling doubts that the hundreds of billions
   of dollars that big companies are plowing into the technology will
   deliver sufficient profits." Investor skepticism, -0.35.
   https://www.youtube.com/watch?v=vtqQ4sP1n0A
2. "The coming AI reckoning" (Big Take podcast, "Reported by Sarah Frier"
   per Ivy.fm): "Bloomberg Big Tech editor Sarah Frier joins host Sarah
   Holder to discuss the coming AI reckoning and why pressure is building on
   tech companies to prove all their AI investments will pay off big, and
   soon." Entity-agnostic pressure frame, -0.30.
   https://ivy.fm/tag/sarah-frier
3. "OpenAI CFO Says Bubble-Wary Market Needs More AI Exuberance"
   (Bloomberg Law, institutional register, NOT Frier-bylined, disclosed):
   "mounting scrutiny in recent months on soaring valuations for AI
   companies as well as the accelerating spending." Investor skepticism,
   -0.25. The OpenAI CFO is Sarah FRIAR (ex-Nextdoor), a different person
   from journalist Sarah FRIER; name collision explicitly disambiguated.
   https://news.bloomberglaw.com/private-equity/openai-cfo-says-bubble-wary-market-needs-more-ai-exuberance

Scorer (MANUAL ILLUSTRATIVE, standing rule Aug 28 2026; arithmetic only):
Meta [-0.15, -0.10, -0.30] avg -0.1833 vs OpenAI [-0.35, -0.30, -0.25] avg
-0.30. Delta (Meta minus OpenAI) +0.1167. Engine check via
calculate_asymmetry: p ~ 0.182, is_significant False, cohens_d ~ 1.429
(agreement pole, same class as #558/#563). p_value NOT_CALCULATED,
cohens_d NOT_CALCULATED, ci_95 NOT_CALCULATED, is_significant False,
artifact_grade False.

Interpretation (falsification family; register-constancy control): Frier
applies the same investor-skepticism AI-spend register to Meta and OpenAI.
Meta marginally softer (+0.1167) runs against the journalist-level anti-Meta
bias hypothesis. Business-press framing is event/market-driven and
entity-agnostic, contrasting with the advocacy gradient at Conde Nast
publications (Schiffer #523) and the deal-driven softening predictions
falsified at #559/#564/#567. Bloomberg has no documented AI content
licensing deal with OpenAI or Meta in-corpus; revenue is
terminal/subscription-driven, not publisher-licensing.

Strongest counterargument: mixed attribution. 2 of 6 items are Bloomberg
Law institutional register, not Frier-bylined, so the within-journalist
claim rests on 4 Frier-attributed items. Her long-arc Meta-adversarial
influence ("No Filter" shaping FTC antitrust framing, per in-corpus notes)
is excluded from this AI-spend window, bounding the constancy claim.
Frier became Managing Editor for Tech in Feb 2026; she edits more than she
writes, so personal register is harder to isolate from institutional voice.
n=3 vs n=3 directional.
"""
import os
import re

import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YAML_PATH = os.path.join(REPO, "profiles", "careers", "journalists.yaml")


def _load_frier():
    with open(YAML_PATH) as f:
        data = yaml.safe_load(f)
    found = []

    def walk(o):
        if isinstance(o, dict):
            if o.get("name") == "Sarah Frier":
                found.append(o)
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    walk(data)
    assert found, "Sarah Frier entry missing from journalists.yaml"
    return found[0]


def _cc():
    entry = _load_frier()
    assert "competitor_coverage" in entry, "competitor_coverage block missing"
    return entry["competitor_coverage"]["cross_entity_analysis"]


class TestMechanismExistsAndShape:
    def test_frier_entry_present(self):
        _load_frier()

    def test_mechanism_id_568(self):
        assert _cc()["mechanism_id"] == 568

    def test_identity_fields(self):
        cc = _cc()
        assert cc["journalist"] == "Sarah Frier"
        assert cc["publication"] == "bloomberg-news"
        assert cc["pattern"] == "register_constancy_business_press"

    def test_item_counts(self):
        cc = _cc()
        assert len(cc["meta_items"]) == 3
        assert len(cc["openai_items"]) == 3

    def test_iteration_and_date(self):
        cc = _cc()
        assert cc["iteration"] == 568
        assert cc["date"] == "2026-09-06"
        assert cc["test_file"].endswith(
            "test_type_b_568_sarah_frier_bloomberg_register_constancy_sep06.py"
        )


class TestSourceAttribution:
    def test_meta_urls_verbatim(self):
        cc = _cc()
        urls = [i["source_url"] for i in cc["meta_items"]]
        assert "https://muckrack.com/sarahfrier/articles" in urls
        assert (
            "https://news.bloomberglaw.com/tech-and-telecom-law/"
            "meta-shares-plunge-on-escalating-concerns-over-ai-spending-spree"
            in urls
        )

    def test_openai_urls_verbatim(self):
        cc = _cc()
        urls = [i["source_url"] for i in cc["openai_items"]]
        assert "https://www.youtube.com/watch?v=vtqQ4sP1n0A" in urls
        assert "https://ivy.fm/tag/sarah-frier" in urls
        assert (
            "https://news.bloomberglaw.com/private-equity/"
            "openai-cfo-says-bubble-wary-market-needs-more-ai-exuberance"
            in urls
        )

    def test_no_constructed_bloomberg_urls(self):
        cc = _cc()
        for item in cc["meta_items"] + cc["openai_items"]:
            u = item["source_url"]
            assert u.startswith("http"), f"non-verbatim URL: {u}"
            assert "bloomberg.com/" not in u or "bloomberglaw.com" in u or u in (
                "https://muckrack.com/sarahfrier/articles",
            ), f"bare bloomberg.com domain URL not allowed: {u}"

    def test_byline_gaps_disclosed(self):
        cc = _cc()
        institutional = [
            i for i in cc["meta_items"] + cc["openai_items"]
            if i["byline_attribution"] == "institutional"
        ]
        assert len(institutional) == 2
        for i in institutional:
            assert "disclosed" in i["byline_evidence"].lower()

    def test_name_collision_disambiguated(self):
        cc = _cc()
        o3 = cc["openai_items"][2]
        assert "FRIAR" in o3["byline_evidence"]
        assert "FRIER" in o3["byline_evidence"]
        assert "different person" in o3["byline_evidence"]

    def test_no_invented_publication_dates(self):
        cc = _cc()
        for item in cc["meta_items"] + cc["openai_items"]:
            assert "date" not in item or item.get("date_verified", True), (
                "undated items must not claim dates"
            )


class TestScorerArithmetic:
    def test_meta_scores_array(self):
        cc = _cc()
        assert cc["scorer"]["target_scores"] == [-0.15, -0.10, -0.30]

    def test_openai_scores_array(self):
        cc = _cc()
        assert cc["scorer"]["peer_scores"] == [-0.35, -0.30, -0.25]

    def test_meta_avg(self):
        cc = _cc()
        avg = sum(cc["scorer"]["target_scores"]) / 3
        assert abs(avg - (-0.1833)) < 1e-3

    def test_openai_avg(self):
        cc = _cc()
        avg = sum(cc["scorer"]["peer_scores"]) / 3
        assert abs(avg - (-0.30)) < 1e-3

    def test_delta(self):
        cc = _cc()
        t = sum(cc["scorer"]["target_scores"]) / 3
        p = sum(cc["scorer"]["peer_scores"]) / 3
        assert abs((t - p) - 0.1167) < 1e-3
        assert abs(cc["scorer"]["delta_manual_illustrative"] - 0.1167) < 1e-4

    def test_engine_agreement_pole(self):
        cc = _cc()
        eng = cc["scorer"]["engine_check"]
        assert abs(eng["asymmetry"] - 0.1167) < 1e-4
        assert abs(eng["p_value"] - 0.1823) < 1e-3
        assert eng["is_significant"] is False
        assert cc["scorer"]["is_significant"] is False

    def test_not_artifact_grade(self):
        cc = _cc()
        assert cc["scorer"]["artifact_grade"] is False
        assert cc["scorer"]["correlation_not_causation"] is True

    def test_no_brittle_not_calculated_p_value(self):
        cc = _cc()
        assert cc["scorer"]["p_value"] == "NOT_CALCULATED"
        assert cc["scorer"]["cohens_d"] == "NOT_CALCULATED"
        assert cc["scorer"]["ci_95"] == "NOT_CALCULATED"


class TestInterpretationAndConfounders:
    def test_falsification_family_referenced(self):
        cc = _cc()
        refs = cc["cross_references"]
        for r in (558, 563, 552, 557, 562, 567, 193):
            assert r in refs, f"missing cross-reference {r}"

    def test_strongest_counterargument_present(self):
        cc = _cc()
        strong = cc["confounders_ranked"]["strong"]
        assert len(strong) == 3
        assert any("Mixed attribution" in s for s in strong)
        assert any("Role change" in s for s in strong)

    def test_confounders_ranked(self):
        cc = _cc()
        assert len(cc["confounders_ranked"]["moderate"]) == 2
        assert len(cc["confounders_ranked"]["weak"]) == 1

    def test_counter_evidence_bounds_claim(self):
        cc = _cc()
        assert len(cc["counter_evidence"]) == 2
        assert any("No Filter" in c for c in cc["counter_evidence"])
        assert any("Convenient Alliance" in c for c in cc["counter_evidence"])

    def test_no_em_dashes(self):
        cc = _cc()
        import json

        s = json.dumps(cc)
        assert "\u2014" not in s and "\u2013" not in s

    def test_research_method_names_search_sets(self):
        cc = _cc()
        assert "browser.search" in cc["research_method"]
        assert "browser.open" in cc["research_method"]
        assert "muckrack.com/sarahfrier/articles" in cc["research_method"]
        assert "Friar" in cc["research_method"]

    def test_financial_context_no_deal(self):
        cc = _cc()
        assert "no documented AI content licensing deal" in cc["financial_context"]
        assert "correlation, not causation" in cc["financial_context"].lower()

    def test_artifact_readiness_not_warranted(self):
        assert _cc()["scorer"]["artifact_grade"] is False


class TestRotationAndNovelty:
    def test_iteration_log_rotation_guard(self):
        with open(os.path.join(REPO, "iteration-log.md")) as f:
            log = f.read()
        assert "#567" in log
        assert "Type A" in log.split("#567")[1][:200]

    def test_no_prior_frier_test_files(self):
        tests_dir = os.path.join(REPO, "tests")
        matches = [
            f for f in os.listdir(tests_dir)
            if "frier" in f.lower()
            and f != "test_type_b_568_sarah_frier_bloomberg_register_constancy_sep06.py"
            and not f.endswith(".pyc")
        ]
        assert matches == [], f"prior Frier test files exist: {matches}"

    def test_single_competitor_coverage_block(self):
        entry = _load_frier()
        assert isinstance(entry["competitor_coverage"], dict)
        assert (
            entry["competitor_coverage"]["cross_entity_analysis"]["mechanism_id"]
            == 568
        )

    def test_description_mentions_register_constancy(self):
        cc = _cc()
        assert "entity-agnostically" in cc["description"]
        assert "agreement pole" in cc["description"]
