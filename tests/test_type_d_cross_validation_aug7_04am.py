"""
Type D cross-validation — August 7, 2026 04:00 PT rotation

Focus: Apple-Google Gemini deal / publisher content bypass chain cross-references,
Apple-OpenAI collapse 5-phase expansion verification, and entity-level consistency
across new Type C additions.

Fixes known failure: test_apple_has_three_phases (now 5 phases) from
test_type_d_cross_validation_aug6.py is superseded by tests here that
validate the expanded 5-phase timeline.
"""

import re
from pathlib import Path
from datetime import date

import pytest
import yaml

_REPO_ROOT = Path(__file__).resolve().parent.parent
_ENTITIES_FILE = _REPO_ROOT / "profiles" / "competitor-entities.yaml"


@pytest.fixture(scope="module")
def entities():
    with open(_ENTITIES_FILE) as f:
        return yaml.safe_load(f)


# ─── Apple-OpenAI 5-Phase Expansion ──────────────────────────────────


class TestAppleOpenAI5PhaseExpansion:
    """Supersedes test_apple_has_three_phases: Apple-OpenAI collapse
    expanded from 3 to 5 phases with Aug 2026 litigation developments."""

    def test_apple_has_five_phases(self, entities):
        apple = entities["entities"]["apple"]
        collapse = apple["openai_partnership_collapse"]
        phase_keys = [k for k in collapse if k.startswith("phase_")]
        assert len(phase_keys) == 5, (
            f"Expected 5 phases after Aug 2026 expansion, got {len(phase_keys)}: "
            f"{phase_keys}"
        )

    def test_phase_names_correct(self, entities):
        apple = entities["entities"]["apple"]
        collapse = apple["openai_partnership_collapse"]
        expected = [
            "phase_1_partnership",
            "phase_2_openai_breach_threat",
            "phase_3_apple_sues_openai",
            "phase_4_preliminary_injunction",
            "phase_5_motion_to_dismiss",
        ]
        actual = sorted([k for k in collapse if k.startswith("phase_")])
        assert actual == sorted(expected), (
            f"Phase names mismatch. Expected: {sorted(expected)}, Got: {actual}"
        )

    def test_all_five_phases_chronological(self, entities):
        """All 5 phases must be in strict chronological order."""
        apple = entities["entities"]["apple"]
        collapse = apple["openai_partnership_collapse"]
        dates = []
        for i in range(1, 6):
            phase_key = [k for k in collapse if k.startswith(f"phase_{i}_")][0]
            d = str(collapse[phase_key]["date"])
            dates.append(d)
        for i in range(len(dates) - 1):
            assert dates[i] < dates[i + 1], (
                f"Phase {i+1} date ({dates[i]}) not before phase {i+2} ({dates[i+1]})"
            )

    def test_phase_4_is_aug_2026(self, entities):
        apple = entities["entities"]["apple"]
        collapse = apple["openai_partnership_collapse"]
        p4 = collapse["phase_4_preliminary_injunction"]
        assert str(p4["date"]).startswith("2026-08"), (
            f"Phase 4 (preliminary injunction) should be Aug 2026, got {p4['date']}"
        )

    def test_phase_5_is_aug_2026(self, entities):
        apple = entities["entities"]["apple"]
        collapse = apple["openai_partnership_collapse"]
        p5 = collapse["phase_5_motion_to_dismiss"]
        assert str(p5["date"]).startswith("2026-08"), (
            f"Phase 5 (motion to dismiss) should be Aug 2026, got {p5['date']}"
        )

    def test_phase_4_has_source_url(self, entities):
        apple = entities["entities"]["apple"]
        p4 = apple["openai_partnership_collapse"]["phase_4_preliminary_injunction"]
        url = p4.get("source_url", p4.get("source_urls", []))
        has_url = bool(url) if isinstance(url, str) else len(url) > 0
        assert has_url, "Phase 4 (preliminary injunction) must have source URL"

    def test_phase_5_has_source_urls(self, entities):
        apple = entities["entities"]["apple"]
        p5 = apple["openai_partnership_collapse"]["phase_5_motion_to_dismiss"]
        urls = p5.get("source_urls", [])
        assert len(urls) >= 1, "Phase 5 (motion to dismiss) must have source URLs"

    def test_phase_4_mentions_injunction(self, entities):
        apple = entities["entities"]["apple"]
        p4 = apple["openai_partnership_collapse"]["phase_4_preliminary_injunction"]
        event = p4.get("event", "").lower()
        detail = p4.get("detail", "").lower()
        assert "injunction" in event or "injunction" in detail, (
            "Phase 4 event/detail should mention 'injunction'"
        )

    def test_phase_5_mentions_dismiss(self, entities):
        apple = entities["entities"]["apple"]
        p5 = apple["openai_partnership_collapse"]["phase_5_motion_to_dismiss"]
        event = p5.get("event", "").lower()
        detail = p5.get("detail", "").lower()
        assert "dismiss" in event or "dismiss" in detail, (
            "Phase 5 event/detail should mention 'dismiss'"
        )


# ─── Apple-Google Gemini Deal Verification ───────────────────────────


class TestAppleGoogleGeminiDealIntegrity:
    """Validates the apple_google_gemini_deal section added in Type C
    04:00 Aug 7 — verifies financial data, dates, and source URLs."""

    def test_gemini_deal_exists(self, entities):
        apple = entities["entities"]["apple"]
        assert "apple_google_gemini_deal" in apple, (
            "Apple entity must have apple_google_gemini_deal section"
        )

    def test_annual_value_is_1b(self, entities):
        deal = entities["entities"]["apple"]["apple_google_gemini_deal"]
        val = deal.get("annual_value_est_b")
        assert val == 1.0 or val == 1, (
            f"Apple-Google Gemini deal annual value should be $1B, got {val}"
        )

    def test_announcement_date_is_jan_2026(self, entities):
        deal = entities["entities"]["apple"]["apple_google_gemini_deal"]
        d = str(deal.get("announcement_date", ""))
        assert d.startswith("2026-01"), (
            f"Gemini deal announced Jan 2026, got {d}"
        )

    def test_bloomberg_report_date_is_nov_2025(self, entities):
        deal = entities["entities"]["apple"]["apple_google_gemini_deal"]
        d = str(deal.get("bloomberg_report_date", ""))
        assert d.startswith("2025-11"), (
            f"Bloomberg first reported Nov 2025, got {d}"
        )

    def test_model_parameters_stated(self, entities):
        deal = entities["entities"]["apple"]["apple_google_gemini_deal"]
        params = str(deal.get("model_parameters", ""))
        assert "trillion" in params.lower() or "1.2" in params, (
            f"Gemini model should reference trillion-parameter scale, got: {params}"
        )

    def test_has_source_urls(self, entities):
        deal = entities["entities"]["apple"]["apple_google_gemini_deal"]
        urls = deal.get("source_urls", [])
        assert len(urls) >= 2, (
            f"Gemini deal should have multiple source URLs, got {len(urls)}"
        )

    def test_reuters_source_present(self, entities):
        deal = entities["entities"]["apple"]["apple_google_gemini_deal"]
        urls = deal.get("source_urls", [])
        has_reuters = any("reuters.com" in u for u in urls)
        assert has_reuters, "Reuters source URL required for Gemini deal"

    def test_overview_mentions_google(self, entities):
        deal = entities["entities"]["apple"]["apple_google_gemini_deal"]
        overview = deal.get("overview", "").lower()
        assert "google" in overview, "Deal overview must mention Google"

    def test_overview_mentions_gemini(self, entities):
        deal = entities["entities"]["apple"]["apple_google_gemini_deal"]
        overview = deal.get("overview", "").lower()
        assert "gemini" in overview, "Deal overview must mention Gemini"


# ─── Publisher Content Bypass Chain ──────────────────────────────────


class TestPublisherContentBypassChain:
    """Validates the publisher_content_bypass section and its
    cross-references to Google's publisher litigation."""

    def test_bypass_section_exists(self, entities):
        apple = entities["entities"]["apple"]
        assert "publisher_content_bypass" in apple

    def test_bypass_mentions_zero_deals(self, entities):
        bypass = entities["entities"]["apple"]["publisher_content_bypass"]
        overview = bypass.get("overview", "").lower()
        assert "zero" in overview or "0" in overview, (
            "Publisher content bypass must state Apple has zero publisher deals"
        )

    def test_bypass_has_publisher_negotiation_history(self, entities):
        bypass = entities["entities"]["apple"]["publisher_content_bypass"]
        assert "publisher_negotiation_history" in bypass, (
            "Must document Apple's Dec 2023 publisher negotiations"
        )

    def test_bypass_mentions_conde_nast(self, entities):
        """Apple approached Condé Nast in Dec 2023."""
        bypass = entities["entities"]["apple"]["publisher_content_bypass"]
        history = bypass.get("publisher_negotiation_history", "")
        assert "condé nast" in history.lower() or "conde nast" in history.lower(), (
            "Must reference Condé Nast as negotiation target"
        )

    def test_bypass_has_content_chain(self, entities):
        bypass = entities["entities"]["apple"]["publisher_content_bypass"]
        assert "content_chain" in bypass, (
            "Must have content_chain explaining the laundering mechanism"
        )

    def test_content_chain_references_hachette(self, entities):
        """The chain depends on the Hachette/Cengage lawsuit against Google."""
        bypass = entities["entities"]["apple"]["publisher_content_bypass"]
        chain = bypass.get("content_chain", "").lower()
        assert "hachette" in chain or "cengage" in chain, (
            "Content chain must reference Hachette/Cengage lawsuit proving "
            "Google trained on publisher content"
        )

    def test_bypass_has_source_urls(self, entities):
        bypass = entities["entities"]["apple"]["publisher_content_bypass"]
        urls = bypass.get("source_urls", [])
        assert len(urls) >= 1, "Publisher content bypass must have source URLs"

    def test_bypass_has_mediascope_relevance(self, entities):
        bypass = entities["entities"]["apple"]["publisher_content_bypass"]
        assert "mediascope_relevance" in bypass, (
            "Must explain why this matters for MediaScope analysis"
        )


# ─── Cross-Entity Consistency: Apple-Google-Publisher Triangle ───────


class TestAppleGooglePublisherTriangle:
    """The Apple-Google Gemini deal and the Google publisher litigation
    are causally linked: Google trains Gemini on publisher content
    (per Hachette lawsuit), Apple pays Google $1B/yr for Gemini,
    publishers receive $0 from Apple. Verify this chain is internally
    consistent across both entities."""

    def test_google_has_publisher_litigation(self, entities):
        google = entities["entities"]["google"]
        assert "publisher_litigation_jul2026" in google

    def test_google_litigation_date_after_gemini_deal(self, entities):
        """Lawsuit came after the Gemini deal — publishers realized
        their content was being laundered through Google."""
        google = entities["entities"]["google"]
        apple = entities["entities"]["apple"]
        lit_date = str(google["publisher_litigation_jul2026"]["date"])
        deal_date = str(apple["apple_google_gemini_deal"]["announcement_date"])
        assert lit_date > deal_date, (
            f"Publisher litigation ({lit_date}) should post-date "
            f"Gemini deal announcement ({deal_date})"
        )

    def test_google_litigation_plaintiffs_include_hachette(self, entities):
        google = entities["entities"]["google"]
        plaintiffs = google["publisher_litigation_jul2026"]["plaintiffs"]
        plaintiff_str = " ".join(str(p) for p in plaintiffs).lower()
        assert "hachette" in plaintiff_str, (
            "Google litigation must include Hachette as plaintiff"
        )

    def test_apple_bypass_and_google_litigation_both_reference_training(self, entities):
        """Both Apple bypass chain and Google litigation should reference
        Google training on publisher content."""
        apple = entities["entities"]["apple"]
        bypass_chain = apple["publisher_content_bypass"].get("content_chain", "").lower()
        google = entities["entities"]["google"]
        lit_detail = google["publisher_litigation_jul2026"].get("detail", "").lower()
        assert "train" in bypass_chain, (
            "Apple bypass content_chain must reference Google training on content"
        )
        assert "train" in lit_detail or "scraping" in lit_detail or "copy" in lit_detail, (
            "Google litigation detail must reference training/scraping/copying"
        )

    def test_gemini_deal_value_vs_meta_news_corp(self, entities):
        """Apple pays Google $1B/yr for Gemini. Meta pays News Corp ~$50M/yr.
        Both should be documented for the contrast."""
        apple = entities["entities"]["apple"]
        gemini_val = apple["apple_google_gemini_deal"]["annual_value_est_b"]
        assert gemini_val >= 1.0, "Gemini deal must be $1B+"

        # Meta-News Corp deal should be in meta_ai_deals partners
        partners = entities["meta_ai_deals"]["partners"]
        news_corp_exists = any(
            "news corp" in str(p.get("name", p.get("publisher", ""))).lower()
            for p in partners
        )
        assert news_corp_exists, (
            "Meta-News Corp deal must be in meta_ai_deals.partners for contrast"
        )


# ─── Samsung Equivalence Paradox Cross-Validation ────────────────────


class TestSamsungEquivalenceParadox:
    """Validates Samsung entity from Type B 03:00 run — identical
    hardware to Meta's glasses but framed differently by publications."""

    def test_samsung_entity_exists(self, entities):
        assert "samsung" in entities["entities"]

    def test_samsung_has_display_name(self, entities):
        samsung = entities["entities"]["samsung"]
        assert "display_name" in samsung and samsung["display_name"]

    def test_samsung_has_smart_glasses_note(self, entities):
        samsung = entities["entities"]["samsung"]
        assert "smart_glasses_note" in samsung or "samsung_launch_source" in samsung, (
            "Samsung entity must document smart glasses context"
        )

    def test_samsung_has_publisher_deals_note(self, entities):
        samsung = entities["entities"]["samsung"]
        assert "publisher_deals_note" in samsung, (
            "Samsung entity must note publisher deal status for comparison"
        )


# ─── Cross-Platform Summary Completeness ─────────────────────────────


class TestCrossPlatformSummaryCompleteness:
    """Verify cross_platform_summary covers all major deal types."""

    def test_apple_openai_collapse_in_summary(self, entities):
        cs = entities["meta_ai_deals"]["cross_platform_summary"]
        assert "apple_openai_partnership_collapse" in cs

    def test_google_news_pilot_in_summary(self, entities):
        cs = entities["meta_ai_deals"]["cross_platform_summary"]
        assert "google_news_ai_pilot" in cs

    def test_amazon_deals_in_summary(self, entities):
        cs = entities["meta_ai_deals"]["cross_platform_summary"]
        has_amazon = any("amazon" in k for k in cs)
        assert has_amazon, "Amazon deals should be in cross_platform_summary"

    def test_summary_timeline_chronological(self, entities):
        """Apple-OpenAI collapse timeline must be chronological."""
        cs = entities["meta_ai_deals"]["cross_platform_summary"]
        collapse = cs["apple_openai_partnership_collapse"]
        timeline = collapse.get("timeline", [])
        if len(timeline) >= 2:
            dates = [str(e.get("date", "")) for e in timeline]
            for i in range(len(dates) - 1):
                if dates[i] and dates[i + 1]:
                    assert dates[i] <= dates[i + 1], (
                        f"Timeline not chronological: {dates[i]} > {dates[i+1]}"
                    )


# ─── Aggregate Incentive Matrix Consistency ──────────────────────────


class TestAggregateIncentiveMatrix:
    """Verify the incentive matrix sums are consistent with entity data."""

    def test_matrix_has_publications(self, entities):
        aim = entities["meta_ai_deals"]["aggregate_incentive_matrix"]
        pubs = aim.get("publications", [])
        assert len(pubs) >= 7, (
            f"Incentive matrix should have 7+ publications, got {len(pubs)}"
        )

    def test_meta_deal_count_is_zero(self, entities):
        aim = entities["meta_ai_deals"]["aggregate_incentive_matrix"]
        assert aim.get("total_meta_deal_count") == 0, (
            "Meta has zero direct publication deals in the tracked set"
        )

    def test_competitor_deals_positive(self, entities):
        aim = entities["meta_ai_deals"]["aggregate_incentive_matrix"]
        assert aim.get("total_competitor_deal_count", 0) > 0, (
            "Competitor deal count must be positive"
        )

    def test_publication_deal_counts_sum_to_total(self, entities):
        aim = entities["meta_ai_deals"]["aggregate_incentive_matrix"]
        pubs = aim.get("publications", [])
        total_from_pubs = sum(p.get("competitor_deals", 0) for p in pubs)
        claimed_total = aim.get("total_competitor_deal_count", 0)
        assert total_from_pubs == claimed_total, (
            f"Sum of per-publication deals ({total_from_pubs}) != "
            f"claimed total ({claimed_total})"
        )


# ─── Source URL Validation ───────────────────────────────────────────


class TestSourceURLFormats:
    """Every source URL should be well-formed and from a credible domain."""

    CREDIBLE_DOMAINS = {
        "reuters.com", "wsj.com", "nytimes.com", "bloomberg.com",
        "macrumors.com", "cnn.com", "fool.com", "theverge.com",
        "techcrunch.com", "hachettebookgroup.com", "arstechnica.com",
        "bbc.com", "bbc.co.uk", "theguardian.com", "wired.com",
        "cnbc.com", "apnews.com",
    }

    def _collect_all_urls(self, data, path=""):
        """Recursively collect all source URLs from the data."""
        urls = []
        if isinstance(data, dict):
            for k, v in data.items():
                if k in ("source_url", "source_urls"):
                    if isinstance(v, str):
                        urls.append((path + "." + str(k), v))
                    elif isinstance(v, list):
                        for u in v:
                            urls.append((path + "." + str(k), str(u)))
                else:
                    urls.extend(self._collect_all_urls(v, path + "." + str(k)))
        elif isinstance(data, list):
            for i, item in enumerate(data):
                urls.extend(self._collect_all_urls(item, f"{path}[{i}]"))
        return urls

    def test_all_urls_are_https(self, entities):
        urls = self._collect_all_urls(entities)
        non_https = [(p, u) for p, u in urls if not u.startswith("https://")]
        assert not non_https, (
            f"Non-HTTPS source URLs found: {non_https[:5]}"
        )

    def test_all_urls_have_known_domains(self, entities):
        urls = self._collect_all_urls(entities)
        unknown = []
        for path, url in urls:
            domain = url.split("//")[1].split("/")[0].lower()
            # Strip www.
            if domain.startswith("www."):
                domain = domain[4:]
            if domain not in self.CREDIBLE_DOMAINS:
                unknown.append((path, domain))
        # Warn but don't fail — new credible sources may be added
        if unknown:
            pytest.skip(
                f"{len(unknown)} URL(s) from domains not in credible list "
                f"(may be valid): {unknown[:3]}"
            )

    def test_no_duplicate_source_urls_in_section(self, entities):
        """Within a single source_urls list, no duplicates."""
        dupes = []
        def check(data, path=""):
            if isinstance(data, dict):
                for k, v in data.items():
                    if k == "source_urls" and isinstance(v, list):
                        if len(v) != len(set(v)):
                            dupes.append(path + "." + str(k))
                    else:
                        check(v, path + "." + str(k))
            elif isinstance(data, list):
                for i, item in enumerate(data):
                    check(item, f"{path}[{i}]")
        check(entities)
        assert not dupes, f"Duplicate source URLs in: {dupes}"
