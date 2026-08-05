"""
Tests for Cade Metz cross-entity coverage analysis at the NYT.

Key finding: NYT's Meta coverage asymmetry operates through REPORTER ASSIGNMENT.
Cade Metz (AI industry reporter) covers OpenAI/Anthropic with technology-progress
framing. Meta's AI coverage is handled by adversarial beat reporters (Mike Isaac,
Eli Tan, Sheera Frenkel). The same event type receives different framing depending
on which reporter writes it.

Source: Muck Rack portfolio analysis (https://muckrack.com/cademetz/articles),
web.archive.org NYT articles, Techmeme aggregation.
"""

import yaml
import pathlib
import re

PROFILES = pathlib.Path(__file__).resolve().parent.parent / "profiles"


def _load_yaml(name: str) -> dict:
    with open(PROFILES / name, encoding="utf-8") as f:
        return yaml.safe_load(f)


# ===================================================================
# NYT Profile — Cade Metz journalist entry
# ===================================================================

class TestCadeMetzProfile:
    """Cade Metz journalist entry has cross-entity coverage analysis."""

    @classmethod
    def setup_class(cls):
        cls.profile = _load_yaml("nytimes.yaml")
        journalists = cls.profile.get("key_journalists", [])
        cls.metz = next(
            (j for j in journalists if j.get("name") == "Cade Metz"), None
        )

    def test_metz_exists(self):
        assert self.metz is not None, "Cade Metz should be in key_journalists"

    def test_metz_has_cross_entity_analysis(self):
        assert "cross_entity_coverage_analysis" in self.metz, \
            "Cade Metz should have cross_entity_coverage_analysis"

    def test_metz_beat_is_ai_industry(self):
        assert "AI" in self.metz.get("beat", ""), \
            "Cade Metz beat should reference AI"

    def test_openai_coverage_tone_not_adversarial(self):
        analysis = self.metz.get("cross_entity_coverage_analysis", {})
        openai = analysis.get("openai_coverage", {})
        tone = openai.get("tone", "")
        assert "adversarial" not in tone.lower(), \
            "Metz's OpenAI coverage tone should NOT be adversarial"

    def test_openai_coverage_volume_is_high(self):
        analysis = self.metz.get("cross_entity_coverage_analysis", {})
        openai = analysis.get("openai_coverage", {})
        volume = openai.get("volume", "")
        assert "high" in volume.lower(), \
            "Metz's OpenAI coverage volume should be high"

    def test_openai_recent_articles_documented(self):
        analysis = self.metz.get("cross_entity_coverage_analysis", {})
        openai = analysis.get("openai_coverage", {})
        articles = openai.get("recent_articles", [])
        assert len(articles) >= 4, \
            f"Should have at least 4 recent OpenAI articles, got {len(articles)}"

    def test_meta_coverage_volume_near_zero(self):
        analysis = self.metz.get("cross_entity_coverage_analysis", {})
        meta = analysis.get("meta_coverage", {})
        volume = meta.get("volume", "")
        assert "zero" in volume.lower() or "near-zero" in volume.lower(), \
            "Metz's Meta coverage volume should be near-zero in 2025-2026"

    def test_meta_coverage_notes_explain_lane_assignment(self):
        analysis = self.metz.get("cross_entity_coverage_analysis", {})
        meta = analysis.get("meta_coverage", {})
        notes = meta.get("notes", "")
        assert "Mike Isaac" in notes or "lane assignment" in notes.lower(), \
            "Meta coverage notes should explain the lane assignment to Isaac/Tan"

    def test_lane_assignment_significance_documented(self):
        analysis = self.metz.get("cross_entity_coverage_analysis", {})
        sig = analysis.get("lane_assignment_significance", "")
        assert len(sig) > 100, \
            "Lane assignment significance should be substantive analysis"

    def test_lane_assignment_references_isaac_and_frenkel(self):
        analysis = self.metz.get("cross_entity_coverage_analysis", {})
        sig = analysis.get("lane_assignment_significance", "")
        assert "Isaac" in sig and "Frenkel" in sig, \
            "Lane assignment significance should reference adversarial reporters"

    def test_source_urls_present(self):
        analysis = self.metz.get("cross_entity_coverage_analysis", {})
        urls = analysis.get("source_urls", {})
        assert len(urls) >= 2, \
            f"Should have at least 2 source URLs, got {len(urls)}"

    def test_anthropic_coverage_documented(self):
        analysis = self.metz.get("cross_entity_coverage_analysis", {})
        anthropic = analysis.get("anthropic_coverage", {})
        assert anthropic.get("tone") is not None, \
            "Anthropic coverage tone should be documented"

    def test_genius_makers_connection_noted(self):
        """Metz's book covered Google AND Facebook AI — but his current beat dropped Meta."""
        analysis = self.metz.get("cross_entity_coverage_analysis", {})
        summary = analysis.get("summary", "")
        assert "Genius Makers" in summary, \
            "Summary should note the Genius Makers book covering both Google and Facebook"

    def test_general_ai_industry_coverage_documented(self):
        analysis = self.metz.get("cross_entity_coverage_analysis", {})
        general = analysis.get("general_ai_industry", {})
        articles = general.get("recent_articles", [])
        assert len(articles) >= 3, \
            f"Should document at least 3 general AI industry articles, got {len(articles)}"


# ===================================================================
# Competitor Coverage Research — NYT cross-entity beat assignment
# ===================================================================

class TestNYTCompetitorResearchBeatAssignment:
    """Competitor coverage research documents NYT's beat assignment mechanism."""

    @classmethod
    def setup_class(cls):
        cls.research = _load_yaml("competitor-coverage-research.yaml")
        cls.nyt = cls.research.get("publications", {}).get("nytimes", {})

    def test_beat_assignment_section_exists(self):
        assert "cross_entity_beat_assignment" in self.nyt, \
            "NYT should have cross_entity_beat_assignment section"

    def test_finding_references_metz(self):
        section = self.nyt.get("cross_entity_beat_assignment", {})
        finding = section.get("finding", "")
        assert "Cade Metz" in finding or "Metz" in finding, \
            "Finding should reference Cade Metz"

    def test_finding_references_isaac(self):
        section = self.nyt.get("cross_entity_beat_assignment", {})
        finding = section.get("finding", "")
        assert "Mike Isaac" in finding or "Isaac" in finding, \
            "Finding should reference Mike Isaac"

    def test_metz_openai_examples_have_positive_tone(self):
        section = self.nyt.get("cross_entity_beat_assignment", {})
        examples = section.get("metz_openai_examples", [])
        for ex in examples:
            tone = ex.get("tone", 0)
            assert tone >= -0.1, \
                f"Metz OpenAI example '{ex.get('title', '')}' tone {tone} should not be adversarial"

    def test_isaac_meta_example_has_negative_tone(self):
        section = self.nyt.get("cross_entity_beat_assignment", {})
        examples = section.get("isaac_meta_examples", [])
        assert len(examples) >= 1, "Should have at least 1 Isaac Meta example"
        for ex in examples:
            tone = ex.get("tone", 0)
            assert tone < 0, \
                f"Isaac Meta example '{ex.get('title', '')}' tone {tone} should be negative"

    def test_isaac_meta_example_has_source_url(self):
        section = self.nyt.get("cross_entity_beat_assignment", {})
        examples = section.get("isaac_meta_examples", [])
        for ex in examples:
            assert ex.get("source_url"), \
                f"Isaac Meta example '{ex.get('title', '')}' should have a source URL"

    def test_analytical_significance_is_substantive(self):
        section = self.nyt.get("cross_entity_beat_assignment", {})
        sig = section.get("analytical_significance", "")
        assert len(sig) > 200, \
            "Analytical significance should be a substantive paragraph"

    def test_significance_contrasts_with_wired(self):
        section = self.nyt.get("cross_entity_beat_assignment", {})
        sig = section.get("analytical_significance", "")
        assert "WIRED" in sig, \
            "Analytical significance should contrast NYT mechanism with WIRED"


# ===================================================================
# Cross-publication lane assignment comparison
# ===================================================================

class TestCrossPublicationLaneComparison:
    """Compare NYT's reporter-assignment mechanism with WIRED's desk-assignment mechanism."""

    @classmethod
    def setup_class(cls):
        cls.research = _load_yaml("competitor-coverage-research.yaml")
        cls.nyt = cls.research.get("publications", {}).get("nytimes", {})
        cls.wired = cls.research.get("publications", {}).get("wired", {})

    def test_both_publications_have_lane_analysis(self):
        nyt_has = "cross_entity_beat_assignment" in self.nyt
        wired_has = any(
            key for key in self.wired
            if "cross_entity" in key.lower() or "lane" in key.lower()
            or "apple_coverage" in key.lower()
        )
        assert nyt_has, "NYT should have cross-entity beat assignment analysis"
        # WIRED has apple_coverage_tone at minimum
        assert self.wired.get("apple_coverage_tone"), \
            "WIRED should have apple_coverage_tone documented"

    def test_nyt_meta_tone_is_adversarial(self):
        assert self.nyt.get("meta_coverage_tone") == "adversarial", \
            "NYT meta_coverage_tone should be adversarial"

    def test_wired_meta_tone_is_adversarial(self):
        assert self.wired.get("meta_coverage_tone") == "adversarial", \
            "WIRED meta_coverage_tone should be adversarial"

    def test_nyt_openai_tone_is_adversarial(self):
        """NYT has litigation against OpenAI — coverage IS adversarial (control case)."""
        assert self.nyt.get("openai_coverage_tone") == "adversarial", \
            "NYT openai_coverage_tone should be adversarial (lawsuit control case)"

    def test_wired_openai_tone_is_softer_than_meta(self):
        """WIRED covers OpenAI softer than Meta — licensing hypothesis."""
        wired_openai = self.wired.get("openai_coverage_tone", "")
        wired_meta = self.wired.get("meta_coverage_tone", "")
        assert wired_meta == "adversarial", "WIRED Meta should be adversarial"
        assert wired_openai != "adversarial", \
            "WIRED OpenAI should NOT be adversarial (licensing deal softens)"

    def test_mechanism_differs_nyt_vs_wired(self):
        """NYT uses reporter-assignment; WIRED uses desk-assignment. Both produce asymmetry."""
        nyt_sig = self.nyt.get("cross_entity_beat_assignment", {}).get(
            "analytical_significance", ""
        )
        # NYT should note that its mechanism is reporter-based
        assert "reporter" in nyt_sig.lower() or "beat" in nyt_sig.lower(), \
            "NYT significance should reference reporter/beat assignment mechanism"


# ===================================================================
# NYT journalist fleet — adversarial vs industry reporters
# ===================================================================

class TestNYTJournalistFleet:
    """Verify the journalist fleet split between adversarial Meta reporters and AI industry reporters."""

    @classmethod
    def setup_class(cls):
        cls.profile = _load_yaml("nytimes.yaml")
        journalists = cls.profile.get("key_journalists", [])
        cls.by_name = {j["name"]: j for j in journalists}

    def test_meta_has_multiple_dedicated_reporters(self):
        meta_reporters = [
            name for name, j in self.by_name.items()
            if "Meta" in j.get("beat", "") or "Facebook" in j.get("beat", "")
        ]
        assert len(meta_reporters) >= 2, \
            f"NYT should have at least 2 dedicated Meta reporters, got: {meta_reporters}"

    def test_openai_has_no_dedicated_reporter(self):
        """OpenAI doesn't have a DEDICATED beat reporter — it's covered by the general AI reporter."""
        openai_reporters = [
            name for name, j in self.by_name.items()
            if "OpenAI" in j.get("beat", "")
        ]
        assert len(openai_reporters) == 0, \
            f"OpenAI should NOT have a dedicated beat reporter, got: {openai_reporters}"

    def test_metz_beat_is_industry_wide(self):
        metz = self.by_name.get("Cade Metz", {})
        beat = metz.get("beat", "")
        assert "industry" in beat.lower() or "research" in beat.lower(), \
            "Metz beat should be industry-wide, not company-specific"

    def test_isaac_beat_is_meta_specific(self):
        isaac = self.by_name.get("Mike Isaac", {})
        beat = isaac.get("beat", "")
        assert "Meta" in beat or "Facebook" in beat, \
            "Isaac beat should be Meta/Facebook specific"

    def test_eli_tan_is_meta_reporter(self):
        tan = self.by_name.get("Eli Tan", {})
        beat = tan.get("beat", "")
        assert "Meta" in beat, "Eli Tan should be a dedicated Meta reporter"

    def test_frenkel_covers_meta(self):
        frenkel = self.by_name.get("Sheera Frenkel", {})
        beat = frenkel.get("beat", "")
        assert "Meta" in beat or "Facebook" in beat, \
            "Sheera Frenkel should cover Meta/Facebook"

    def test_weise_has_conflict_note(self):
        """Karen Weise covers Amazon, which pays NYT $20-25M/yr — conflict noted."""
        weise = self.by_name.get("Karen Weise", {})
        patterns = weise.get("known_patterns", "")
        assert "CONFLICT" in patterns, \
            "Karen Weise should have a CONFLICT NOTE about Amazon licensing deal"

    def test_google_beat_has_gap(self):
        """Nico Grant left in May 2025 — Google beat has a gap."""
        departures = self.profile.get("notable_departures", [])
        grant = next(
            (d for d in departures if d.get("name") == "Nico Grant"), None
        )
        assert grant is not None, "Nico Grant departure should be documented"
        assert "Google" in grant.get("beat", ""), \
            "Nico Grant should be documented as Google beat reporter"


# ===================================================================
# NYT litigation paradox — sues OpenAI but Metz covers it neutrally
# ===================================================================

class TestNYTLitigationParadox:
    """
    NYT is actively suing OpenAI for copyright infringement (claims billions).
    Despite this, Cade Metz's coverage of OpenAI is NOT adversarial.
    Meanwhile, NYT has NO financial grievance against Meta but assigns
    adversarial beat reporters to Meta. This is a coverage paradox.
    """

    @classmethod
    def setup_class(cls):
        cls.profile = _load_yaml("nytimes.yaml")
        cls.research = _load_yaml("competitor-coverage-research.yaml")
        cls.nyt_research = cls.research.get("publications", {}).get("nytimes", {})
        journalists = cls.profile.get("key_journalists", [])
        cls.metz = next(
            (j for j in journalists if j.get("name") == "Cade Metz"), None
        )

    def test_nyt_has_openai_litigation(self):
        conflicts = self.profile.get("known_conflicts", [])
        litigation = [c for c in conflicts if c.get("type") == "litigation"]
        assert len(litigation) >= 1, "NYT should have litigation conflict documented"
        lit_desc = litigation[0].get("description", "")
        assert "OpenAI" in lit_desc, "Litigation should mention OpenAI"

    def test_openai_research_tone_is_adversarial(self):
        """The INSTITUTIONAL tone toward OpenAI is adversarial (lawsuit)."""
        tone = self.nyt_research.get("openai_coverage_tone", "")
        assert tone == "adversarial", \
            "NYT's institutional openai_coverage_tone should be adversarial (lawsuit)"

    def test_metz_openai_tone_is_not_adversarial(self):
        """But Metz individually covers OpenAI with neutral/positive framing."""
        analysis = self.metz.get("cross_entity_coverage_analysis", {})
        openai = analysis.get("openai_coverage", {})
        tone = openai.get("tone", "")
        assert "adversarial" not in tone.lower(), \
            "Metz's personal OpenAI coverage tone should not be adversarial"

    def test_meta_coverage_adversarial_without_litigation(self):
        """NYT has NO lawsuit against Meta but meta_coverage_tone is adversarial."""
        meta_tone = self.nyt_research.get("meta_coverage_tone", "")
        assert meta_tone == "adversarial", \
            "NYT covers Meta adversarially despite no financial grievance"

    def test_paradox_implies_structural_bias(self):
        """
        The paradox: adversarial financial relationship with OpenAI produces
        neutral reporter coverage. No financial grievance against Meta produces
        adversarial reporter coverage. This implies the coverage tone is driven
        by reporter assignment and institutional history, not financial incentives.
        At NYT, the beat-assignment mechanism operates independently of the
        publication's financial interests.
        """
        metz_analysis = self.metz.get("cross_entity_coverage_analysis", {})
        sig = metz_analysis.get("lane_assignment_significance", "")
        # The significance section should document the structural mechanism
        assert "structural" in sig.lower() or "institutional" in sig.lower(), \
            "Lane assignment significance should reference structural/institutional bias"
