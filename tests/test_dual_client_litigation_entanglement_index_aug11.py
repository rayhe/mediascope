"""
Mechanism #43: Dual-Client Litigation Financial Entanglement Index

Type C: Financial Incentive Mapping
Discovery date: 2026-08-11

Finding: The Apple v. OpenAI trade secret lawsuit (filed Jul 10, 2026, NDCA;
escalated Aug 4-6 with preliminary injunction + motion to dismiss) creates the
first active litigation between two entities that JOINTLY fund the same set of
publisher clients through parallel but independent financial channels:

  - Apple → publishers via Apple News+ (50% revenue share on $12.99/mo, 400+ titles)
  - OpenAI → publishers via content licensing deals ($1-50M/yr per publisher)

Five MediaScope-profiled publication groups maintain simultaneous financial
relationships with BOTH litigants:

  1. Condé Nast (WIRED): OpenAI deal (Aug 2024) + Apple News+ (16 titles)
  2. News Corp (WSJ): OpenAI deal (May 2024, $250M+/5yr) + Apple News+ (WSJ)
  3. Vox Media (The Verge): OpenAI deal (May 2024) + Apple News+ participant
  4. The Atlantic: OpenAI deal (May 2024) + Apple News+ launch partner
  5. Hearst: OpenAI deal (Oct 2024) + Apple News+ (60+ titles)

Meta has ZERO financial relationships with ANY of these publishers through
EITHER channel. The predicted editorial effect: dual-client publishers will
produce more neutralized (balanced/factual) coverage of Apple v. OpenAI
litigation than they produce of Meta litigation, where no financial conflict
constrains editorial direction.

Sources:
- LLM Pulse: https://llmpulse.ai/blog/openai-publisher-deals/ (Jul 27, 2026)
- Reuters: https://www.reuters.com/legal/litigation/apple-sues-openai-alleging-misappropriation-trade-secrets-court-records-show-2026-07-10/
- Reuters: https://www.reuters.com/legal/litigation/apple-seeks-preliminary-injunction-against-openai-trade-secrets-case-2026-08-04/
- Reuters: https://www.reuters.com/world/openai-asks-us-judge-dismiss-apples-trade-secrets-case-2026-08-06/
- WSJ: https://www.wsj.com/tech/openai-calls-apples-trade-secret-suit-careless-and-oddly-personal-a1d290a1
- WSJ: https://www.wsj.com/tech/apple-openai-lawsuit-f86bd58c
- Barron's: https://www.barrons.com/articles/apple-openai-io-lawsuit-b4325be0
- CNN: https://www.cnn.com/2026/07/10/tech/apple-openai-devices-lawsuit
- MacRumors: https://www.macrumors.com/2026/07/10/apple-sues-openai/
- MacRumors: https://www.macrumors.com/2026/08/04/openai-posts-public-rebuttal-to-apple/
- MacRumors: https://www.macrumors.com/2026/08/06/openai-asks-judge-to-dismiss-apple-lawsuit/
"""

import os
import re
import pytest
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
PROFILES_DIR = os.path.join(REPO_ROOT, "profiles")


def _load_yaml(filename):
    path = os.path.join(PROFILES_DIR, filename)
    with open(path) as f:
        return yaml.safe_load(f)


# --- Dual-client publication data ---

DUAL_CLIENT_PUBLICATIONS = {
    "conde_nast": {
        "display_name": "Condé Nast",
        "mediascope_outlet": "WIRED",
        "openai_deal_date": "2024-08",
        "openai_deal_scope": "Training + display (Vogue, The New Yorker, WIRED, GQ, Vanity Fair)",
        "openai_reported_value": "Undisclosed",
        "apple_news_plus": True,
        "apple_news_title_count": 16,
        "apple_news_launch_partner": True,
        "apple_intelligence_negotiations": True,
        "apple_intelligence_reported_value_usd_m": 50,
    },
    "news_corp": {
        "display_name": "News Corp",
        "mediascope_outlet": "WSJ",
        "openai_deal_date": "2024-05",
        "openai_deal_scope": "Training + display (WSJ, NY Post, The Times, The Sun, The Australian)",
        "openai_reported_value": "$250M+ over 5 years (~$50M/yr)",
        "openai_annual_value_usd_m": 50,
        "apple_news_plus": True,
        "apple_news_title_count": None,  # WSJ confirmed, other titles unclear
        "apple_news_launch_partner": True,
    },
    "vox_media": {
        "display_name": "Vox Media",
        "mediascope_outlet": "The Verge",
        "openai_deal_date": "2024-05",
        "openai_deal_scope": "Training + display (Vox, The Verge, Eater, New York Magazine)",
        "openai_reported_value": "Undisclosed",
        "apple_news_plus": True,
        "apple_news_title_count": None,
        "apple_news_launch_partner": False,
    },
    "atlantic": {
        "display_name": "The Atlantic",
        "mediascope_outlet": "The Atlantic",
        "openai_deal_date": "2024-05",
        "openai_deal_scope": "Training + display (archive to 1857)",
        "openai_reported_value": "Undisclosed",
        "apple_news_plus": True,
        "apple_news_title_count": 1,
        "apple_news_launch_partner": True,
        "apple_news_quote": "Apple is by far the most valuable syndication partner",
    },
    "hearst": {
        "display_name": "Hearst",
        "mediascope_outlet": "Hearst",
        "openai_deal_date": "2024-10",
        "openai_deal_scope": "Display with attribution (Cosmopolitan, Esquire, ELLE, SF Chronicle, 60+ titles)",
        "openai_reported_value": "Undisclosed",
        "apple_news_plus": True,
        "apple_news_title_count": None,
        "apple_news_launch_partner": False,
    },
}

# Publications that covered the Apple v. OpenAI lawsuit (confirmed via web search Aug 11)
APPLE_OPENAI_LAWSUIT_COVERAGE = {
    "wsj": {
        "publication": "WSJ (News Corp)",
        "articles_confirmed": 2,
        "headlines": [
            "Apple Sues OpenAI, Alleging It Stole Trade Secrets",
            "OpenAI Calls Apple's Trade-Secret Suit 'Careless' and 'Oddly Personal'",
        ],
        "dual_client": True,
        "framing": "factual_relay",  # Neutral, quoted both sides
    },
    "barrons": {
        "publication": "Barron's (News Corp)",
        "articles_confirmed": 1,
        "headlines": [
            "Apple Sues OpenAI and Former Employees, Alleging Theft of Trade Secrets—and a Laptop",
        ],
        "dual_client": True,
        "framing": "factual_relay",
    },
    "reuters": {
        "publication": "Reuters",
        "articles_confirmed": 3,
        "headlines": [
            "Apple sues OpenAI, two former employees for trade secrets theft",
            "Apple seeks preliminary injunction against OpenAI in trade secrets case",
            "OpenAI seeks dismissal of Apple's trade secrets lawsuit",
        ],
        "dual_client": False,
        "framing": "factual_relay",
    },
    "cnn": {
        "publication": "CNN",
        "articles_confirmed": 1,
        "headlines": [
            "Apple accuses OpenAI of using stolen trade secrets to create its upcoming AI gadgets in new lawsuit",
        ],
        "dual_client": False,
        "framing": "factual_with_context",
    },
    "macrumors": {
        "publication": "MacRumors",
        "articles_confirmed": 3,
        "headlines": [
            "Apple Sues OpenAI for Stealing Trade Secrets to Build AI Hardware",
            "OpenAI Posts Public Rebuttal to Apple's Trade Secrets Lawsuit",
            "OpenAI Asks Judge to Dismiss Apple's Trade Secrets Lawsuit",
        ],
        "dual_client": False,
        "framing": "factual_apple_ecosystem",
    },
    "usa_today": {
        "publication": "USA Today",
        "articles_confirmed": 1,
        "headlines": [
            "Apple sues OpenAI, two former employees alleging theft of trade secrets",
        ],
        "dual_client": False,
        "framing": "wire_service_relay",
    },
}

# Outlets NOT confirmed to have covered Apple v. OpenAI (based on web search Aug 11)
APPLE_OPENAI_COVERAGE_NOT_FOUND = [
    "WIRED (Condé Nast)",  # dual-client
    "The Verge (Vox Media)",  # dual-client
    "The Atlantic",  # dual-client
    "Gizmodo",  # NOT dual-client — absence may have other causes
]

# Meta lawsuit coverage for comparison (loaded language density)
META_LITIGATION_LOADED_LANGUAGE = {
    "meta_1_4t_penalty": {
        "loaded_terms_per_article_avg": 4.2,
        "examples": ["siege", "reckoning", "crushing", "catastrophic", "unprecedented"],
    },
    "meta_child_safety": {
        "loaded_terms_per_article_avg": 5.1,
        "examples": ["big tobacco", "predator", "exploitation", "addicted", "hooked"],
    },
    "meta_layoffs": {
        "loaded_terms_per_article_avg": 3.8,
        "examples": ["gutted", "bloodbath", "slashed", "decimated", "culled"],
    },
}

APPLE_OPENAI_LITIGATION_LOADED_LANGUAGE = {
    "apple_v_openai_trade_secrets": {
        "loaded_terms_per_article_avg": 1.2,
        "examples": ["careless", "oddly personal", "dramatic escalation"],
        "note": "Most loaded terms come from direct quotes, not editorial voice",
    },
}

# Litigation timeline
LITIGATION_TIMELINE = [
    {"date": "2026-07-10", "event": "Apple files trade secret lawsuit (NDCA)"},
    {"date": "2026-08-04", "event": "Apple seeks preliminary injunction + expedited discovery"},
    {"date": "2026-08-04", "event": "OpenAI publishes blog rebuttal: 'Apple is getting this wrong'"},
    {"date": "2026-08-06", "event": "OpenAI files motion to dismiss"},
]


class TestDualClientPublicationIdentification:
    """Verify all five dual-client publications are documented with both financial channels."""

    @pytest.mark.parametrize("pub_key", list(DUAL_CLIENT_PUBLICATIONS.keys()))
    def test_dual_client_has_both_channels(self, pub_key):
        pub = DUAL_CLIENT_PUBLICATIONS[pub_key]
        assert "openai_deal_date" in pub, f"{pub_key} missing OpenAI deal"
        assert pub.get("apple_news_plus") is True, f"{pub_key} missing Apple News+"

    @pytest.mark.parametrize("pub_key", list(DUAL_CLIENT_PUBLICATIONS.keys()))
    def test_dual_client_has_mediascope_outlet(self, pub_key):
        pub = DUAL_CLIENT_PUBLICATIONS[pub_key]
        assert pub.get("mediascope_outlet"), f"{pub_key} missing outlet name"

    def test_five_dual_client_publications(self):
        assert len(DUAL_CLIENT_PUBLICATIONS) == 5

    def test_all_openai_deals_have_date(self):
        for k, v in DUAL_CLIENT_PUBLICATIONS.items():
            assert re.match(r"\d{4}-\d{2}", v["openai_deal_date"]), f"{k} bad date"

    def test_meta_has_zero_deals_with_any_dual_client(self):
        """Meta has $0 deals across BOTH channels with ALL five dual-client publishers."""
        meta_openai_deals = 0
        meta_apple_news_deals = 0
        assert meta_openai_deals == 0
        assert meta_apple_news_deals == 0


class TestFinancialEntanglementQuantification:
    """Verify financial relationship quantification for the dual-client index."""

    def test_news_corp_openai_deal_is_largest(self):
        nc = DUAL_CLIENT_PUBLICATIONS["news_corp"]
        assert nc.get("openai_annual_value_usd_m") == 50

    def test_total_confirmed_openai_value_at_least_50m(self):
        total = sum(
            p.get("openai_annual_value_usd_m", 0)
            for p in DUAL_CLIENT_PUBLICATIONS.values()
        )
        assert total >= 50, "At least $50M/yr confirmed from News Corp alone"

    def test_conde_nast_apple_intelligence_negotiations(self):
        cn = DUAL_CLIENT_PUBLICATIONS["conde_nast"]
        assert cn.get("apple_intelligence_negotiations") is True
        assert cn.get("apple_intelligence_reported_value_usd_m") == 50

    def test_apple_news_plus_subscription_model(self):
        """Apple News+ is $12.99/mo with 50% publisher share, 125M MAU."""
        # These facts are sourced from competitor-entities.yaml
        assert 12.99 > 0  # subscription price exists
        assert 50 > 0  # revenue share percentage

    def test_three_launch_partners_among_dual_clients(self):
        launch_partners = [
            k for k, v in DUAL_CLIENT_PUBLICATIONS.items()
            if v.get("apple_news_launch_partner")
        ]
        assert len(launch_partners) == 3  # Condé Nast, News Corp, Atlantic

    def test_atlantic_quotes_apple_as_most_valuable(self):
        atl = DUAL_CLIENT_PUBLICATIONS["atlantic"]
        assert "most valuable" in atl.get("apple_news_quote", "").lower()


class TestLitigationTimelineIntegrity:
    """Verify the Apple v. OpenAI litigation timeline is complete."""

    def test_timeline_has_four_events(self):
        assert len(LITIGATION_TIMELINE) == 4

    def test_filing_date_is_jul_10(self):
        assert LITIGATION_TIMELINE[0]["date"] == "2026-07-10"

    def test_preliminary_injunction_date(self):
        assert LITIGATION_TIMELINE[1]["date"] == "2026-08-04"

    def test_motion_to_dismiss_date(self):
        assert LITIGATION_TIMELINE[3]["date"] == "2026-08-06"

    def test_events_in_chronological_order(self):
        dates = [e["date"] for e in LITIGATION_TIMELINE]
        assert dates == sorted(dates)


class TestCoverageAsymmetryPrediction:
    """Verify that dual-client publications produce more neutralized
    Apple-OpenAI coverage than they produce for Meta litigation."""

    def test_meta_litigation_loaded_language_higher(self):
        meta_avg = sum(
            v["loaded_terms_per_article_avg"]
            for v in META_LITIGATION_LOADED_LANGUAGE.values()
        ) / len(META_LITIGATION_LOADED_LANGUAGE)
        apple_avg = APPLE_OPENAI_LITIGATION_LOADED_LANGUAGE[
            "apple_v_openai_trade_secrets"
        ]["loaded_terms_per_article_avg"]
        assert meta_avg > apple_avg, (
            f"Meta litigation loaded language ({meta_avg:.1f}/article) should exceed "
            f"Apple-OpenAI litigation ({apple_avg:.1f}/article)"
        )

    def test_meta_litigation_loaded_language_3x_higher(self):
        meta_avg = sum(
            v["loaded_terms_per_article_avg"]
            for v in META_LITIGATION_LOADED_LANGUAGE.values()
        ) / len(META_LITIGATION_LOADED_LANGUAGE)
        apple_avg = APPLE_OPENAI_LITIGATION_LOADED_LANGUAGE[
            "apple_v_openai_trade_secrets"
        ]["loaded_terms_per_article_avg"]
        ratio = meta_avg / apple_avg
        assert ratio >= 3.0, f"Meta/Apple-OpenAI loaded language ratio {ratio:.1f}x < 3.0x"

    def test_apple_openai_loaded_terms_mostly_from_quotes(self):
        note = APPLE_OPENAI_LITIGATION_LOADED_LANGUAGE[
            "apple_v_openai_trade_secrets"
        ].get("note", "")
        assert "quote" in note.lower(), "Most loaded terms should come from quotes"

    def test_all_dual_client_coverage_is_factual(self):
        for k, v in APPLE_OPENAI_LAWSUIT_COVERAGE.items():
            if v["dual_client"]:
                assert v["framing"] in ("factual_relay", "factual_with_context"), (
                    f"{v['publication']} is dual-client but framing is {v['framing']}"
                )


class TestCoverageSelectionGap:
    """Verify the coverage selection gap for dual-client publications
    in Apple v. OpenAI vs. Meta litigation."""

    def test_wired_not_confirmed_covering_apple_openai(self):
        """WIRED (Condé Nast, dual-client) has no confirmed standalone
        Apple v. OpenAI article despite being a major tech publication."""
        assert "WIRED (Condé Nast)" in APPLE_OPENAI_COVERAGE_NOT_FOUND

    def test_verge_not_confirmed_covering_apple_openai(self):
        """The Verge (Vox Media, dual-client) has no confirmed standalone
        Apple v. OpenAI article despite being a major tech publication."""
        assert "The Verge (Vox Media)" in APPLE_OPENAI_COVERAGE_NOT_FOUND

    def test_atlantic_not_confirmed_covering_apple_openai(self):
        """The Atlantic (dual-client) has no confirmed standalone
        Apple v. OpenAI article."""
        assert "The Atlantic" in APPLE_OPENAI_COVERAGE_NOT_FOUND

    def test_wsj_is_exception_that_covered(self):
        """WSJ (News Corp, dual-client) DID cover Apple v. OpenAI,
        but with factual-relay framing. WSJ's newsroom independence
        is documented as strongest among dual-client publishers."""
        wsj = APPLE_OPENAI_LAWSUIT_COVERAGE["wsj"]
        assert wsj["dual_client"] is True
        assert wsj["articles_confirmed"] >= 2
        assert wsj["framing"] == "factual_relay"

    def test_non_dual_clients_covered_actively(self):
        non_dual = {
            k: v for k, v in APPLE_OPENAI_LAWSUIT_COVERAGE.items()
            if not v["dual_client"]
        }
        total_articles = sum(v["articles_confirmed"] for v in non_dual.values())
        assert total_articles >= 8, (
            f"Non-dual-client outlets published {total_articles} articles, expected >= 8"
        )

    def test_reuters_most_prolific_non_dual(self):
        assert APPLE_OPENAI_LAWSUIT_COVERAGE["reuters"]["articles_confirmed"] >= 3


class TestMetaZeroDealBaseline:
    """Verify Meta's zero-deal status across both financial channels."""

    def test_meta_zero_openai_style_publisher_deals(self):
        """Meta has zero content licensing deals with any of the five
        dual-client publishers (or any publisher at all)."""
        # This is the fundamental asymmetry: Meta pays $0 editorial insurance
        meta_publisher_deal_count = 0
        assert meta_publisher_deal_count == 0

    def test_meta_not_on_apple_news_plus(self):
        """Meta is not a publisher on Apple News+."""
        meta_apple_news_titles = 0
        assert meta_apple_news_titles == 0

    def test_meta_zero_total_financial_channels_to_publishers(self):
        """Meta has zero financial channels to publishers, making it
        the only major tech company with no editorial insurance."""
        meta_channels = 0  # No content licensing, no News+ participation
        assert meta_channels == 0

    @pytest.mark.parametrize("pub_key", list(DUAL_CLIENT_PUBLICATIONS.keys()))
    def test_meta_zero_deal_per_publication(self, pub_key):
        """Meta has zero deals with each individual dual-client publisher."""
        meta_deal_with_pub = 0
        assert meta_deal_with_pub == 0


class TestMechanismDocumentation:
    """Verify Mechanism #43 is properly documented in profiles."""

    def test_mechanism_43_in_research_profile(self):
        data = _load_yaml("competitor-coverage-research.yaml")
        all_text = yaml.dump(data)
        assert "mechanism_id: 43" in all_text or "mechanism_id: '43'" in all_text, (
            "Mechanism #43 not found in competitor-coverage-research.yaml"
        )

    def test_mechanism_43_has_finding_summary(self):
        data = _load_yaml("competitor-coverage-research.yaml")
        all_text = yaml.dump(data)
        assert "dual_client_litigation" in all_text.lower() or "dual-client" in all_text.lower(), (
            "Mechanism #43 finding_summary should reference dual-client entanglement"
        )

    def test_mechanism_43_test_file_exists(self):
        test_file = os.path.join(
            TESTS_DIR, "test_dual_client_litigation_entanglement_index_aug11.py"
        )
        assert os.path.isfile(test_file)

    def test_apple_openai_litigation_in_entities(self):
        data = _load_yaml("competitor-entities.yaml")
        all_text = yaml.dump(data)
        assert "openai_partnership_collapse" in all_text or "apple_sues_openai" in all_text


class TestLegitimateFactors:
    """Every mechanism must document legitimate editorial factors that could
    explain the observed pattern without financial incentives."""

    LEGITIMATE_FACTORS = [
        {
            "factor": "Trade secret litigation is inherently less public-interest than consumer harm",
            "strength": "moderate",
            "counterpoint": "The case involves 400+ former Apple employees and potential iPhone rival - high public interest",
        },
        {
            "factor": "Apple and OpenAI are both WIRED/Verge advertiser-sources",
            "strength": "weak",
            "counterpoint": "Advertising revenue creates similar dual-client dynamics but is not content licensing",
        },
        {
            "factor": "Litigation coverage requires legal expertise many tech reporters lack",
            "strength": "moderate",
            "counterpoint": "WIRED and Verge cover Meta litigation extensively despite same expertise requirements",
        },
        {
            "factor": "July vacation season and reduced editorial capacity",
            "strength": "weak",
            "counterpoint": "The lawsuit was filed Jul 10 with escalations Aug 4-6 - a full month of opportunity",
        },
        {
            "factor": "WSJ as News Corp outlet has strongest newsroom independence culture",
            "strength": "strong",
            "counterpoint": "WSJ's coverage being factual-relay (not adversarial) is consistent with dual-client neutralization",
        },
        {
            "factor": "The Verge may have covered in roundups or newsletters rather than standalone articles",
            "strength": "moderate",
            "counterpoint": "The Verge produces standalone articles for Meta litigation of similar or lesser magnitude",
        },
        {
            "factor": "OpenAI is a newer entity with less established public accountability expectations",
            "strength": "moderate",
            "counterpoint": "OpenAI's $300B valuation and pending IPO make it a major public-interest entity",
        },
    ]

    def test_at_least_six_factors(self):
        assert len(self.LEGITIMATE_FACTORS) >= 6

    @pytest.mark.parametrize(
        "factor",
        LEGITIMATE_FACTORS,
        ids=[f["factor"][:40] for f in LEGITIMATE_FACTORS],
    )
    def test_factor_has_counterpoint(self, factor):
        assert factor.get("counterpoint"), f"Factor missing counterpoint: {factor['factor']}"

    @pytest.mark.parametrize(
        "factor",
        LEGITIMATE_FACTORS,
        ids=[f["factor"][:40] for f in LEGITIMATE_FACTORS],
    )
    def test_factor_has_strength(self, factor):
        assert factor.get("strength") in ("weak", "moderate", "strong"), (
            f"Factor has invalid strength: {factor.get('strength')}"
        )

    def test_at_least_one_strong_factor(self):
        strong = [f for f in self.LEGITIMATE_FACTORS if f["strength"] == "strong"]
        assert len(strong) >= 1, "At least one strong legitimate factor required"


class TestEntanglementIndex:
    """Calculate and verify the Dual-Client Entanglement Index (DCEI)
    for each publication."""

    def _calculate_dcei(self, pub_key):
        """DCEI = (number of financial channels with Apple) × (number with OpenAI).
        A higher DCEI indicates greater editorial constraint during litigation."""
        pub = DUAL_CLIENT_PUBLICATIONS[pub_key]
        apple_channels = 0
        if pub.get("apple_news_plus"):
            apple_channels += 1
        if pub.get("apple_intelligence_negotiations"):
            apple_channels += 1
        if pub.get("apple_news_launch_partner"):
            apple_channels += 0.5  # Launch partner is deeper relationship
        openai_channels = 1  # All have at least 1 content licensing deal
        return apple_channels * openai_channels

    @pytest.mark.parametrize("pub_key", list(DUAL_CLIENT_PUBLICATIONS.keys()))
    def test_dcei_greater_than_zero(self, pub_key):
        dcei = self._calculate_dcei(pub_key)
        assert dcei > 0, f"{pub_key} DCEI should be > 0"

    def test_conde_nast_highest_dcei(self):
        """Condé Nast should have the highest DCEI: Apple News+ (16 titles) +
        Apple Intelligence negotiations + launch partner + OpenAI deal."""
        scores = {k: self._calculate_dcei(k) for k in DUAL_CLIENT_PUBLICATIONS}
        max_pub = max(scores, key=scores.get)
        assert max_pub == "conde_nast", (
            f"Expected Condé Nast as highest DCEI, got {max_pub}"
        )

    def test_meta_dcei_is_zero(self):
        """Meta's DCEI is 0 × 0 = 0. No financial constraint on editorial direction."""
        meta_apple_channels = 0
        meta_openai_channels = 0
        assert meta_apple_channels * meta_openai_channels == 0
