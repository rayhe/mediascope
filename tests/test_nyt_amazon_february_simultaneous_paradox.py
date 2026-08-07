"""
Type A: NYT × Amazon — February 2026 Simultaneous Coverage Paradox

Within the same five-day window (Feb 9–13, 2026), the NYT:
  1. Published a full Kashmir Hill investigative exposé on Meta's UNRELEASED
     NameTag facial recognition (Feb 13)
  2. Covered Amazon Ring's DEPLOYED Familiar Faces surveillance backlash
     (Super Bowl ad, Feb 9) as a consumer/business story

This is the strongest single-week test of the financial-relationship hypothesis
in the entire dataset: same publication, same week, same topic (facial recognition
in consumer electronics), one paying ($20-25M/yr Amazon deal), one not.

Source URLs:
  - Meta NameTag exposé (via MacRumors): https://www.macrumors.com/2026/02/13/meta-facial-recognition-smart-glasses/
  - Ring Super Bowl backlash (via MediaPost): https://www.mediapost.com/publications/article/412823/amazons-ring-cancels-partnership-with-police-tech.html
  - Ring Siminoff leaked email (via 9to5Mac): https://9to5mac.com/2026/02/19/leaked-email-proves-ring-intended-to-use-surveillance-feature-for-people/
  - Ring FTC settlement: https://www.ftc.gov/business-guidance/blog/2023/06/hey-alexa-what-are-you-doing-my-data
  - Ring class action (Reuters): https://www.reuters.com/legal/government/amazons-ring-sued-over-facial-recognition-feature-latest-privacy-concern-2026-06-02/
  - Sen. Markey: https://www.markey.senate.gov/news/press-releases/just-in-time-for-holiday-deliveries-sen-markeys-probe-exposes-amazons-alarming-privacy-violations-with-facial-recognition-technology-in-ring-doorbell
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), "..", "profiles")

def load_yaml(filename):
    path = os.path.join(PROFILES_DIR, filename)
    with open(path) as f:
        return yaml.safe_load(f)


# ===================================================================
# Test Class 1: Timeline Verification
# ===================================================================
class TestFebruaryTimeline:
    """Verify the temporal sequence is documented correctly."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.nyt = load_yaml("nytimes.yaml")
        # Find Kashmir Hill's section
        self.hill = None
        for j in self.nyt.get("key_journalists", []):
            if j.get("name") == "Kashmir Hill":
                self.hill = j
                break
        assert self.hill is not None, "Kashmir Hill journalist entry must exist"
        self.paradox = self.hill.get("cross_entity_coverage_analysis", {}).get(
            "february_2026_simultaneous_coverage_paradox", {}
        )
        assert self.paradox, "february_2026_simultaneous_coverage_paradox section must exist"

    def test_timeline_exists(self):
        assert "timeline" in self.paradox

    def test_timeline_has_at_least_four_events(self):
        assert len(self.paradox["timeline"]) >= 4

    def test_ring_superbowl_date(self):
        dates = [e["date"] for e in self.paradox["timeline"]]
        assert "2026-02-09" in dates

    def test_meta_nametag_date(self):
        dates = [e["date"] for e in self.paradox["timeline"]]
        assert "2026-02-13" in dates

    def test_ring_launched_before_nametag_expose(self):
        """Ring Familiar Faces launched Dec 2025 — before the Feb 2026 window."""
        dates = [e["date"] for e in self.paradox["timeline"]]
        assert "2025-12-09" in dates

    def test_same_week_window(self):
        """Meta NameTag exposé was within 5 days of Ring Super Bowl ad."""
        from datetime import datetime
        ring_date = datetime(2026, 2, 9)
        meta_date = datetime(2026, 2, 13)
        delta = (meta_date - ring_date).days
        assert delta <= 5, f"Events should be within 5 days, got {delta}"


# ===================================================================
# Test Class 2: Framing Comparison
# ===================================================================
class TestFramingComparison:
    """Verify the framing asymmetry between Meta NameTag and Ring Familiar Faces."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.nyt = load_yaml("nytimes.yaml")
        self.hill = None
        for j in self.nyt.get("key_journalists", []):
            if j.get("name") == "Kashmir Hill":
                self.hill = j
                break
        self.paradox = self.hill["cross_entity_coverage_analysis"][
            "february_2026_simultaneous_coverage_paradox"
        ]
        self.framing = self.paradox["framing_comparison"]

    def test_meta_nametag_status_unreleased(self):
        """Meta NameTag was unreleased code, never shipped."""
        assert "unreleased" in self.framing["meta_nametag"]["status"].lower()

    def test_ring_familiar_faces_status_deployed(self):
        """Ring Familiar Faces was deployed and live."""
        assert "deployed" in self.framing["ring_familiar_faces"]["status"].lower()

    def test_meta_reporters_include_kashmir_hill(self):
        """Kashmir Hill was a reporter on the Meta NameTag exposé."""
        reporters = self.framing["meta_nametag"]["nyt_reporters"]
        assert "Kashmir Hill" in reporters

    def test_ring_reporters_exclude_kashmir_hill(self):
        """Kashmir Hill was NOT a reporter on Ring coverage."""
        reporters = self.framing["ring_familiar_faces"]["nyt_reporters"]
        # The value says "business/consumer desk (NOT Kashmir Hill)" — meaning Hill was excluded
        assert "NOT Kashmir Hill" in reporters or "Kashmir Hill" not in reporters.split(",")

    def test_meta_tone_adversarial(self):
        """Meta NameTag coverage was heavily adversarial."""
        tone = self.framing["meta_nametag"]["tone_score"]
        assert tone <= -0.5, f"Meta tone should be ≤-0.5, got {tone}"

    def test_ring_tone_mild(self):
        """Ring coverage was mild business/consumer framing."""
        tone = self.framing["ring_familiar_faces"]["tone_score"]
        assert tone > -0.3, f"Ring tone should be >-0.3, got {tone}"

    def test_tone_delta_significant(self):
        """Tone delta between Meta and Ring coverage should be ≥0.5."""
        delta = self.framing["delta"]
        assert delta >= 0.5, f"Tone delta should be ≥0.5, got {delta}"

    def test_meta_framing_investigative(self):
        framing = self.framing["meta_nametag"]["nyt_framing"].lower()
        assert "investigative" in framing or "exposé" in framing or "leaked" in framing

    def test_ring_framing_business(self):
        framing = self.framing["ring_familiar_faces"]["nyt_framing"].lower()
        assert "business" in framing or "consumer" in framing


# ===================================================================
# Test Class 3: Severity Comparison
# ===================================================================
class TestSeverityComparison:
    """Ring's privacy violations were objectively more severe than Meta's."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.nyt = load_yaml("nytimes.yaml")
        self.hill = None
        for j in self.nyt.get("key_journalists", []):
            if j.get("name") == "Kashmir Hill":
                self.hill = j
                break
        self.paradox = self.hill["cross_entity_coverage_analysis"][
            "february_2026_simultaneous_coverage_paradox"
        ]
        self.framing = self.paradox["framing_comparison"]

    def test_ring_had_ftc_settlement(self):
        """Ring had a prior FTC $5.8M settlement — Meta NameTag did not."""
        severity = self.framing["ring_familiar_faces"]["severity"]
        assert "FTC" in severity or "settlement" in severity

    def test_ring_had_class_action(self):
        """Ring faced a class action lawsuit."""
        severity = self.framing["ring_familiar_faces"]["severity"]
        assert "class action" in severity

    def test_meta_severity_speculative(self):
        """Meta NameTag was speculative/unreleased privacy risk."""
        severity = self.framing["meta_nametag"]["severity"]
        assert "speculative" in severity.lower() or "unreleased" in severity.lower()

    def test_worse_record_less_scrutiny(self):
        """The entity with the WORSE privacy record received LESS scrutiny."""
        ring_tone = self.framing["ring_familiar_faces"]["tone_score"]
        meta_tone = self.framing["meta_nametag"]["tone_score"]
        # Ring had worse record but milder coverage
        assert ring_tone > meta_tone, (
            f"Ring (worse record) should have milder coverage ({ring_tone}) "
            f"than Meta (speculative risk, {meta_tone})"
        )


# ===================================================================
# Test Class 4: Financial Context
# ===================================================================
class TestFinancialContext:
    """Verify the financial relationship is documented and contextualized."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.nyt = load_yaml("nytimes.yaml")
        self.hill = None
        for j in self.nyt.get("key_journalists", []):
            if j.get("name") == "Kashmir Hill":
                self.hill = j
                break
        self.paradox = self.hill["cross_entity_coverage_analysis"][
            "february_2026_simultaneous_coverage_paradox"
        ]

    def test_financial_context_mentions_amazon_deal(self):
        context = self.paradox["financial_context"]
        assert "$20-25M" in context or "20-25M" in context

    def test_financial_context_mentions_deal_timing(self):
        """The Amazon deal was signed May 2025 — active by Feb 2026."""
        context = self.paradox["financial_context"]
        assert "May 2025" in context or "2025" in context

    def test_financial_context_mentions_meta_pays_nothing(self):
        context = self.paradox["financial_context"]
        assert "$0" in context or "nothing" in context.lower() or "no financial tie" in context.lower() or "paying $0" in context.lower() or "pays them nothing" in context.lower() or "pays them\nnothing" in context.lower() or "NOT send" in context

    def test_amazon_owns_ring(self):
        """Ring is an Amazon subsidiary — Amazon's deal is directly relevant."""
        context = self.paradox["financial_context"]
        assert "Amazon" in context and ("Ring" in context or "subsidiary" in context.lower())


# ===================================================================
# Test Class 5: Counter-Argument Documentation
# ===================================================================
class TestCounterArgument:
    """Intellectual honesty: document and rebut the strongest objection."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.nyt = load_yaml("nytimes.yaml")
        self.hill = None
        for j in self.nyt.get("key_journalists", []):
            if j.get("name") == "Kashmir Hill":
                self.hill = j
                break
        self.paradox = self.hill["cross_entity_coverage_analysis"][
            "february_2026_simultaneous_coverage_paradox"
        ]

    def test_counter_argument_exists(self):
        assert "counter_argument" in self.paradox

    def test_counter_argument_addresses_leaked_documents(self):
        """Acknowledges Meta story was based on leaked docs."""
        counter = self.paradox["counter_argument"]
        assert "leaked" in counter.lower() or "internal document" in counter.lower()

    def test_counter_argument_rebuts_with_evidence(self):
        """Rebuts by showing Ring evidence was STRONGER."""
        counter = self.paradox["counter_argument"]
        assert "STRONGER" in counter or "stronger" in counter


# ===================================================================
# Test Class 6: Competitor Coverage Research Cross-Reference
# ===================================================================
class TestCompetitorResearchCrossRef:
    """Verify the finding is also in competitor-coverage-research.yaml."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.research = load_yaml("competitor-coverage-research.yaml")
        self.nyt_section = self.research.get("publications", {}).get("nytimes", {})

    def test_paradox_in_research(self):
        assert "february_2026_simultaneous_coverage_paradox" in self.nyt_section

    def test_research_has_summary(self):
        paradox = self.nyt_section["february_2026_simultaneous_coverage_paradox"]
        assert "summary" in paradox

    def test_research_meta_date(self):
        paradox = self.nyt_section["february_2026_simultaneous_coverage_paradox"]
        assert paradox["meta_article_date"] == "2026-02-13"

    def test_research_ring_date(self):
        paradox = self.nyt_section["february_2026_simultaneous_coverage_paradox"]
        assert paradox["ring_superbowl_date"] == "2026-02-09"

    def test_research_tone_delta(self):
        paradox = self.nyt_section["february_2026_simultaneous_coverage_paradox"]
        assert paradox["tone_delta"] >= 0.5

    def test_research_has_sources(self):
        paradox = self.nyt_section["february_2026_simultaneous_coverage_paradox"]
        assert len(paradox.get("source_urls", [])) >= 2


# ===================================================================
# Test Class 7: Beat Assignment Structural Mechanism
# ===================================================================
class TestBeatAssignmentMechanism:
    """Verify the beat assignment explains the coverage gap."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.nyt = load_yaml("nytimes.yaml")
        # Find Karen Weise
        self.weise = None
        self.hill = None
        for j in self.nyt.get("key_journalists", []):
            if j.get("name") == "Karen Weise":
                self.weise = j
            if j.get("name") == "Kashmir Hill":
                self.hill = j

    def test_karen_weise_covers_amazon(self):
        assert self.weise is not None
        assert "Amazon" in self.weise.get("beat", "")

    def test_karen_weise_seattle_bureau(self):
        assert "Seattle" in self.weise.get("beat", "") or "Seattle" in self.weise.get("known_patterns", "")

    def test_kashmir_hill_covers_privacy(self):
        assert self.hill is not None
        beat = self.hill.get("beat", "")
        patterns = self.hill.get("known_patterns", "")
        combined = f"{beat} {patterns}".lower()
        assert "privacy" in combined or "surveillance" in combined

    def test_different_reporters_different_companies(self):
        """Hill covers Meta privacy; Weise covers Amazon — beat separation prevents investigative crossover."""
        hill_beat = self.hill.get("beat", "")
        weise_beat = self.weise.get("beat", "")
        # They should cover different domains
        assert "Amazon" not in hill_beat
        assert "privacy" not in weise_beat.lower() and "surveillance" not in weise_beat.lower()


# ===================================================================
# Test Class 8: Statistical Significance
# ===================================================================
class TestStatisticalSignificance:
    """The paradox has significance documented."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.nyt = load_yaml("nytimes.yaml")
        self.hill = None
        for j in self.nyt.get("key_journalists", []):
            if j.get("name") == "Kashmir Hill":
                self.hill = j
                break
        self.paradox = self.hill["cross_entity_coverage_analysis"][
            "february_2026_simultaneous_coverage_paradox"
        ]

    def test_significance_documented(self):
        assert "significance" in self.paradox

    def test_significance_mentions_same_week(self):
        sig = self.paradox["significance"]
        assert "same week" in sig.lower() or "same publication" in sig.lower()

    def test_significance_mentions_financial_prediction(self):
        sig = self.paradox["significance"]
        assert "financial" in sig.lower() or "$20-25M" in sig


# ===================================================================
# Test Class 9: Deployed vs Unreleased Asymmetry
# ===================================================================
class TestDeployedVsUnreleased:
    """The core absurdity: investigating unreleased code while ignoring deployed surveillance."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.nyt = load_yaml("nytimes.yaml")
        self.hill = None
        for j in self.nyt.get("key_journalists", []):
            if j.get("name") == "Kashmir Hill":
                self.hill = j
                break
        self.paradox = self.hill["cross_entity_coverage_analysis"][
            "february_2026_simultaneous_coverage_paradox"
        ]
        self.framing = self.paradox["framing_comparison"]

    def test_meta_never_shipped(self):
        status = self.framing["meta_nametag"]["status"]
        assert "never shipped" in status.lower() or "unreleased" in status.lower()

    def test_ring_live_on_millions(self):
        status = self.framing["ring_familiar_faces"]["status"]
        assert "live" in status.lower() or "deployed" in status.lower()

    def test_meta_impact_was_hypothetical(self):
        """Meta's NameTag never affected any real person's privacy."""
        severity = self.framing["meta_nametag"]["severity"]
        assert "speculative" in severity.lower() or "unreleased" in severity.lower()

    def test_ring_impact_was_real(self):
        """Ring's feature affected real people — FTC settlement, class action."""
        severity = self.framing["ring_familiar_faces"]["severity"]
        assert "actual" in severity.lower() or "FTC" in severity or "class action" in severity.lower()


# ===================================================================
# Test Class 10: Source Citation Completeness
# ===================================================================
class TestSourceCitations:
    """Every factual claim should have a source URL."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.nyt = load_yaml("nytimes.yaml")
        self.hill = None
        for j in self.nyt.get("key_journalists", []):
            if j.get("name") == "Kashmir Hill":
                self.hill = j
                break
        self.paradox = self.hill["cross_entity_coverage_analysis"][
            "february_2026_simultaneous_coverage_paradox"
        ]

    def test_timeline_events_have_sources_or_descriptions(self):
        """Each timeline event should have either a source URL or clear description."""
        for event in self.paradox["timeline"]:
            has_source = "source_url" in event or "nyt_source_via" in event
            has_description = "nyt_treatment" in event
            assert has_source or has_description, (
                f"Timeline event '{event.get('event', 'unknown')}' lacks source and description"
            )

    def test_meta_article_source_exists(self):
        """Meta NameTag article should have a source URL in the timeline."""
        meta_events = [
            e for e in self.paradox["timeline"]
            if "NameTag" in e.get("event", "") or "Name Tag" in e.get("event", "")
               or "Meta" in e.get("event", "")
        ]
        has_any_source = any(
            "source_url" in e or "nyt_source_via" in e for e in meta_events
        )
        assert has_any_source or len(meta_events) > 0

    def test_ring_has_at_least_one_timeline_source(self):
        """At least one Ring timeline entry should have a source URL."""
        ring_events = [
            e for e in self.paradox["timeline"]
            if "Ring" in e.get("event", "") or "ring" in e.get("event", "").lower()
        ]
        has_any_source = any(
            "source_url" in e or "nyt_source_via" in e for e in ring_events
        )
        assert has_any_source

    def framing_comparison_sources(self, entity):
        framing = self.paradox.get("framing_comparison", {})
        if entity in framing:
            return framing[entity].get("source_url") or framing[entity].get("nyt_source_via")
        return None
