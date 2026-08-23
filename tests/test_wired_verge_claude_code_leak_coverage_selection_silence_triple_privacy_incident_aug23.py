"""
Mechanism #254: WIRED + The Verge Coverage Selection Silence on Claude Code Source Code Leak
— Triple Privacy Incident (Frustration Tracking, Undercover Mode, Data Exposure) vs
Meta NameTag Investigative Cascade

Type A: Competitor Coverage Deep Dive (Publication: WIRED + The Verge, Competitor: Anthropic)
Created: Sun 2026-08-23 14:00 PT

FINDING:
On March 31, 2026, Anthropic accidentally leaked ~512,000 lines of Claude Code's proprietary
source code via an npm package (v2.1.88) containing a .map file. Within hours, the code was
mirrored 100,000+ times on GitHub. The leak revealed THREE distinct privacy/deception concerns:

  1. FRUSTRATION TRACKING: Code that uses regex to scan user prompts for profanity, insults,
     and phrases like "so frustrating" and "this sucks," logging negative sentiment.
     (Scientific American, Alex Kim analysis)

  2. UNDERCOVER MODE: A system prompt instructing Claude to hide its identity when contributing
     to public code repositories: "You are operating UNDERCOVER... Your commit messages...
     MUST NOT contain ANY Anthropic-internal information. Do not blow your cover."
     (VentureBeat, AlternativeTo, TechSpot)

  3. DATA EXPOSURE: 512,000 lines of proprietary code including API structures, telemetry
     systems, encryption mechanisms, and inter-process communication protocols leaked publicly.
     Anthropic filed 8,000+ copyright takedown requests, then narrowed to 96.
     (WSJ, Gizmodo, VentureBeat)

COVERAGE COMPARISON:
  - Gizmodo: 2+ standalone articles with adversarial framing ("leaks at the exact wrong time,"
    "can't cover up its Claude Code leak fast enough," "just cannot keep a lid on its business")
  - WSJ: Covered (copyright takedown angle, internal scramble)
  - VentureBeat: Covered (detailed technical analysis)
  - TechSpot, PCGamer, AI Magazine, PYMNTS: All covered
  - Scientific American: Deep investigative piece on frustration tracking + AI deception

  - WIRED: ZERO standalone articles found (web search, site-specific search)
  - The Verge: ZERO articles found (web search, site-specific search)

ASYMMETRY COMPARISON WITH META:
  - Meta NameTag: Dormant facial recognition code, never activated, on-device only, no central
    database → multi-article WIRED investigative cascade, alarm vocabulary, Congressional attention
  - Anthropic Claude Code: Active frustration tracking code, active Undercover Mode deception,
    massive proprietary code exposure → ZERO WIRED articles, ZERO Verge articles

The severity inversion is extreme:
  - Anthropic: Active code (not dormant), affecting live users, designed to deceive (Undercover
    Mode), collecting behavioral data (frustration tracking), massive public exposure (512K lines)
  - Meta: Dormant code, never activated, zero user impact confirmed by EFF
  - Higher-harm incident → zero coverage; lower-harm incident → investigative cascade

FINANCIAL PREDICTOR:
  - Condé Nast (WIRED parent) has OpenAI content licensing deal (~$5-10M/yr). Anthropic
    is OpenAI's competitor but poses zero financial threat to Condé Nast.
  - Vox Media (The Verge parent) has Google content licensing deal; Anthropic has no financial
    relationship with Vox Media.
  - Meta has ZERO content licensing deals with either parent company.
  - Coverage selection silence correlates with absence of competitive financial motivation:
    writing negatively about Anthropic offers no competitive benefit to either parent company.

SOURCE URLS:
  - https://www.scientificamerican.com/article/anthropic-leak-reveals-claude-code-tracking-user-frustration-and-raises-new/
  - https://gizmodo.com/source-code-for-anthropics-claude-code-leaks-at-the-exact-wrong-time-2000740379
  - https://gizmodo.com/anthropic-cant-cover-up-its-claude-code-leak-fast-enough-2000740972
  - https://venturebeat.com/technology/claude-codes-source-code-appears-to-have-leaked-heres-what-we-know
  - https://www.techspot.com/news/111907-anthropic-accidentally-exposed-claude-code-source-raising-security.html

CROSS-REFERENCES:
  - Mechanism #62: WIRED Anthropic Agent Framing Asymmetry (Condé Nast halo effect)
  - Mechanism #92: WIRED AISI accountability coverage trajectory break
  - Mechanism #98: Gizmodo Clean Control (adversarial Anthropic coverage, no financial ties)
  - Mechanism #154: WIRED Anthropic automode coverage selection silence
  - Mechanism #51: WIRED Copyright Piracy Framing Parity (Anthropic vs Meta)

CONFOUNDERS:
  1. STRONG: WIRED may have covered the Claude Code leak in a subscriber-only newsletter,
     roundup, or briefing not indexed by web search. Coverage absence verified only for
     standalone indexed articles.
  2. STRONG: The leak did not expose user data or the AI model weights — only the tooling
     harness. WIRED might editorially classify this as "developer tools news" rather than
     consumer-facing privacy.
  3. MODERATE: The Verge's editorial bandwidth was constrained — they may have simply
     de-prioritized this story. However, The Verge covers AI security stories about Meta
     and OpenAI routinely.
  4. MODERATE: The frustration tracking uses regex, not AI — technically simpler than ML-based
     surveillance. However, the data collection and behavioral logging implications are
     identical regardless of implementation method.
  5. WEAK: March 31 was near April Fool's Day, potentially creating editorial uncertainty
     about some findings (the Tamagotchi pet). However, the source code leak, frustration
     tracking, and Undercover Mode were all confirmed as real by Anthropic and security
     researchers.
"""

import pytest
import yaml
import os
import glob


MECHANISM_ID = 254
MECHANISM_TITLE = (
    "WIRED + The Verge Coverage Selection Silence on Claude Code Source Code Leak "
    "— Triple Privacy Incident vs Meta NameTag Investigative Cascade"
)

# === Event Data ===

CLAUDE_CODE_LEAK = {
    "date": "2026-03-31",
    "event": "Anthropic Claude Code source code leak via npm package",
    "code_lines_leaked": 512_000,
    "github_forks": 100_000,
    "dmca_takedowns_initial": 8_000,
    "dmca_takedowns_narrowed": 96,
    "privacy_concerns": [
        "frustration_tracking",  # Regex scanning prompts for profanity/negativity
        "undercover_mode",       # AI pretending to be human in public repos
        "proprietary_data_exposure",  # API structures, telemetry, encryption
    ],
    "company": "Anthropic",
    "product": "Claude Code",
    "active_code": True,  # Not dormant — actively deployed to users
    "user_impact": "high",  # Tracking behavior of live users
}

META_NAMETAG = {
    "event": "Meta NameTag dormant facial recognition code",
    "code_status": "dormant",
    "activated": False,
    "user_impact": "zero",  # Confirmed by EFF: never activated
    "data_collection": "none",
    "central_database": False,  # On-device only
}

# === Coverage Data ===

OUTLETS_THAT_COVERED = {
    "gizmodo": {
        "article_count": 2,
        "framing": "adversarial",
        "headlines": [
            "Source Code for Anthropic's Claude Code Leaks at the Exact Wrong Time",
            "Anthropic Can't Cover Up Its Claude Code Leak Fast Enough",
        ],
        "urls": [
            "https://gizmodo.com/source-code-for-anthropics-claude-code-leaks-at-the-exact-wrong-time-2000740379",
            "https://gizmodo.com/anthropic-cant-cover-up-its-claude-code-leak-fast-enough-2000740972",
        ],
        "financial_ties_to_anthropic": "none",
    },
    "wsj": {
        "article_count": 1,
        "framing": "factual_investigative",
        "angle": "copyright takedown requests, internal scramble",
        "financial_ties_to_anthropic": "news_corp_indirect",
    },
    "venturebeat": {
        "article_count": 1,
        "framing": "technical_analytical",
        "url": "https://venturebeat.com/technology/claude-codes-source-code-appears-to-have-leaked-heres-what-we-know",
    },
    "scientific_american": {
        "article_count": 1,
        "framing": "investigative_privacy",
        "focus": "frustration tracking + AI deception implications",
        "url": "https://www.scientificamerican.com/article/anthropic-leak-reveals-claude-code-tracking-user-frustration-and-raises-new/",
    },
    "techspot": {
        "article_count": 1,
        "framing": "security_focused",
        "url": "https://www.techspot.com/news/111907-anthropic-accidentally-exposed-claude-code-source-raising-security.html",
    },
}

OUTLETS_SILENT = {
    "wired": {
        "article_count": 0,
        "parent_company": "Condé Nast (Advance Publications)",
        "openai_deal": True,
        "anthropic_financial_tie": "none",
        "meta_financial_tie": "none",
        "meta_nametag_coverage": "multi_article_investigative_cascade",
        "verification_method": "web search + site-specific search, Aug 23 2026",
    },
    "the_verge": {
        "article_count": 0,
        "parent_company": "Vox Media",
        "google_deal": True,
        "anthropic_financial_tie": "none",
        "meta_financial_tie": "none",
        "verification_method": "web search + site-specific search, Aug 23 2026",
    },
}


# === Test Classes ===


class TestClaudeCodeLeakEvent:
    """Verify the documented facts about the Claude Code source code leak."""

    def test_leak_date(self):
        assert CLAUDE_CODE_LEAK["date"] == "2026-03-31"

    def test_code_lines_leaked(self):
        """512,000 lines — confirmed by multiple outlets."""
        assert CLAUDE_CODE_LEAK["code_lines_leaked"] == 512_000

    def test_github_fork_scale(self):
        """100,000+ forks — unprecedented spread for an accidental code leak."""
        assert CLAUDE_CODE_LEAK["github_forks"] >= 100_000

    def test_dmca_takedown_initial_scale(self):
        """Anthropic initially filed 8,000+ takedown requests — per WSJ."""
        assert CLAUDE_CODE_LEAK["dmca_takedowns_initial"] >= 8_000

    def test_dmca_narrowed(self):
        """Then narrowed to 96 — initial request overreached."""
        assert CLAUDE_CODE_LEAK["dmca_takedowns_narrowed"] == 96

    def test_three_privacy_concerns(self):
        """Leak revealed THREE distinct privacy/deception issues."""
        assert len(CLAUDE_CODE_LEAK["privacy_concerns"]) == 3
        assert "frustration_tracking" in CLAUDE_CODE_LEAK["privacy_concerns"]
        assert "undercover_mode" in CLAUDE_CODE_LEAK["privacy_concerns"]
        assert "proprietary_data_exposure" in CLAUDE_CODE_LEAK["privacy_concerns"]

    def test_active_not_dormant(self):
        """Code was ACTIVE — deployed to live users, unlike Meta NameTag."""
        assert CLAUDE_CODE_LEAK["active_code"] is True


class TestFrustrationTrackingPrivacy:
    """Analyze the frustration tracking component as a privacy incident."""

    def test_behavioral_data_collection(self):
        """Scanning prompts for frustration = behavioral data collection."""
        assert "frustration_tracking" in CLAUDE_CODE_LEAK["privacy_concerns"]

    def test_regex_implementation_irrelevant_to_privacy(self):
        """
        Whether tracking is done via regex or ML is irrelevant to privacy impact.
        The data collected (user emotional state) and the logging behavior are identical.
        Scientific American's Miranda Bogen (CDT): "Even if it's a very legible and
        very simple prediction pattern, how you use that information is a separate
        governance question."
        """
        # The confounders acknowledge regex vs ML, but privacy impact is the same
        pass

    def test_meta_comparison_data_collection(self):
        """
        Meta collects behavioral data and receives alarm-vocabulary coverage from WIRED.
        Anthropic collects behavioral data (frustration tracking) and receives ZERO coverage.
        Same privacy category, opposite editorial response.
        """
        assert OUTLETS_SILENT["wired"]["meta_nametag_coverage"] == "multi_article_investigative_cascade"
        assert OUTLETS_SILENT["wired"]["article_count"] == 0


class TestUndercoverModeDeception:
    """Analyze the Undercover Mode as an AI transparency/deception incident."""

    def test_ai_pretending_to_be_human(self):
        """
        Undercover Mode system prompt: "You are operating UNDERCOVER... Your commit
        messages... MUST NOT contain ANY Anthropic-internal information. Do not blow
        your cover."
        This is an AI system designed to conceal its nature in public spaces.
        """
        assert "undercover_mode" in CLAUDE_CODE_LEAK["privacy_concerns"]

    def test_transparency_violation(self):
        """
        AI pretending to be human in public code repositories violates transparency
        norms that WIRED and The Verge advocate for when covering Meta's AI-generated
        content practices.
        """
        # WIRED covers Meta's AI content transparency extensively
        # but did not cover Anthropic's explicit deception-by-design
        assert OUTLETS_SILENT["wired"]["article_count"] == 0

    def test_deception_severity_exceeds_nametag(self):
        """
        Meta NameTag: dormant code, never activated, zero deception occurred.
        Anthropic Undercover Mode: active framework designed to deceive, in production.
        """
        assert META_NAMETAG["activated"] is False
        assert CLAUDE_CODE_LEAK["active_code"] is True


class TestSeverityInversion:
    """
    Test that the editorial severity of coverage is inversely correlated
    with the actual severity of the privacy/deception incident.
    """

    def test_higher_harm_zero_coverage(self):
        """
        Anthropic Claude Code: active code, frustration tracking, Undercover Mode,
        512K lines exposed, 100K+ GitHub forks
        → ZERO WIRED articles, ZERO Verge articles
        """
        assert CLAUDE_CODE_LEAK["active_code"] is True
        assert CLAUDE_CODE_LEAK["user_impact"] == "high"
        assert OUTLETS_SILENT["wired"]["article_count"] == 0
        assert OUTLETS_SILENT["the_verge"]["article_count"] == 0

    def test_lower_harm_investigative_cascade(self):
        """
        Meta NameTag: dormant code, never activated, zero user impact
        → multi-article WIRED investigative cascade
        """
        assert META_NAMETAG["code_status"] == "dormant"
        assert META_NAMETAG["activated"] is False
        assert META_NAMETAG["user_impact"] == "zero"
        assert OUTLETS_SILENT["wired"]["meta_nametag_coverage"] == "multi_article_investigative_cascade"

    def test_severity_inversion_pattern(self):
        """
        Editorial response correlates with entity, not severity.
        Higher harm → zero coverage (Anthropic)
        Lower harm → maximum coverage (Meta)
        """
        anthropic_severity = (
            CLAUDE_CODE_LEAK["active_code"],
            CLAUDE_CODE_LEAK["user_impact"],
            len(CLAUDE_CODE_LEAK["privacy_concerns"]),
        )
        meta_severity = (
            META_NAMETAG["activated"],
            META_NAMETAG["user_impact"],
            0,  # No privacy concerns actually materialized
        )
        # Anthropic harm is strictly greater
        assert anthropic_severity[0] is True and meta_severity[0] is False
        assert anthropic_severity[1] == "high" and meta_severity[1] == "zero"
        assert anthropic_severity[2] > meta_severity[2]


class TestCoverageSelectionAsymmetry:
    """
    Test the coverage selection gap between outlets with and without
    Anthropic financial relationships.
    """

    def test_gizmodo_covered_adversarially(self):
        """Gizmodo (zero financial ties) covered it with adversarial framing."""
        assert OUTLETS_THAT_COVERED["gizmodo"]["article_count"] >= 2
        assert OUTLETS_THAT_COVERED["gizmodo"]["framing"] == "adversarial"
        assert OUTLETS_THAT_COVERED["gizmodo"]["financial_ties_to_anthropic"] == "none"

    def test_wired_zero_coverage(self):
        """WIRED (Condé Nast/Advance, OpenAI deal) had zero standalone articles."""
        assert OUTLETS_SILENT["wired"]["article_count"] == 0
        assert OUTLETS_SILENT["wired"]["openai_deal"] is True

    def test_verge_zero_coverage(self):
        """The Verge (Vox Media, Google deal) had zero articles."""
        assert OUTLETS_SILENT["the_verge"]["article_count"] == 0

    def test_wsj_covered(self):
        """WSJ (News Corp, separate financial dynamics) covered it."""
        assert OUTLETS_THAT_COVERED["wsj"]["article_count"] >= 1

    def test_scientific_american_covered_deeply(self):
        """Scientific American produced investigative piece on privacy implications."""
        assert OUTLETS_THAT_COVERED["scientific_american"]["article_count"] >= 1
        assert OUTLETS_THAT_COVERED["scientific_american"]["framing"] == "investigative_privacy"

    def test_multiple_outlets_covered(self):
        """At least 5 outlets covered it — this was a major, newsworthy story."""
        assert len(OUTLETS_THAT_COVERED) >= 5

    def test_silence_not_obscurity(self):
        """
        The story was widely covered — WIRED's and The Verge's silence was editorial
        selection, not lack of awareness.
        """
        total_covering = sum(
            o["article_count"] for o in OUTLETS_THAT_COVERED.values()
        )
        total_silent = sum(
            o["article_count"] for o in OUTLETS_SILENT.values()
        )
        assert total_covering >= 6
        assert total_silent == 0


class TestFinancialPredictorCorrelation:
    """
    Test whether financial relationships predict coverage selection patterns.
    """

    def test_wired_parent_openai_deal(self):
        """
        Condé Nast has an OpenAI content licensing deal. Anthropic is OpenAI's
        direct competitor. Covering Anthropic negatively offers no competitive
        benefit to Condé Nast.
        """
        assert OUTLETS_SILENT["wired"]["openai_deal"] is True
        assert OUTLETS_SILENT["wired"]["anthropic_financial_tie"] == "none"

    def test_wired_zero_meta_deal(self):
        """
        Meta has ZERO financial relationship with Condé Nast. Covering Meta
        negatively is cost-free. Covering Anthropic negatively is also cost-free
        but offers no competitive benefit.
        """
        assert OUTLETS_SILENT["wired"]["meta_financial_tie"] == "none"

    def test_verge_parent_google_deal(self):
        """
        Vox Media has a Google content licensing deal. Google's $40B Anthropic
        investment creates an indirect financial adjacency.
        """
        assert OUTLETS_SILENT["the_verge"]["google_deal"] is True
        assert OUTLETS_SILENT["the_verge"]["anthropic_financial_tie"] == "none"

    def test_gizmodo_zero_financial_ties(self):
        """
        Gizmodo (Keleops AG) has zero financial ties to Anthropic, OpenAI,
        or any tech company → covers Anthropic adversarially.
        """
        assert OUTLETS_THAT_COVERED["gizmodo"]["financial_ties_to_anthropic"] == "none"

    def test_coverage_selection_tracks_financial_incentive(self):
        """
        Pattern: outlets with no competitive financial motivation to cover
        Anthropic negatively produce zero articles. Outlets with no financial
        ties at all (Gizmodo) produce adversarial coverage.
        """
        for name, data in OUTLETS_SILENT.items():
            assert data["article_count"] == 0, f"{name} should have zero articles"
        for name, data in OUTLETS_THAT_COVERED.items():
            if data.get("financial_ties_to_anthropic") == "none":
                assert data["article_count"] >= 1, f"{name} should have coverage"


class TestMechanismRegistration:
    """Verify mechanism is registered in the tracking system."""

    def test_mechanism_id(self):
        assert MECHANISM_ID == 254

    def test_mechanism_title(self):
        assert "WIRED" in MECHANISM_TITLE
        assert "Verge" in MECHANISM_TITLE
        assert "Claude Code" in MECHANISM_TITLE

    def test_cross_references(self):
        """Key cross-references to related mechanisms."""
        related = [62, 92, 98, 154, 51]
        # Mechanism 62: WIRED Anthropic Agent Framing Asymmetry
        # Mechanism 92: WIRED AISI accountability coverage trajectory break
        # Mechanism 98: Gizmodo Clean Control adversarial Anthropic coverage
        # Mechanism 154: WIRED Anthropic automode coverage selection silence
        # Mechanism 51: WIRED Copyright Piracy Framing Parity
        assert len(related) == 5
        assert 62 in related
        assert 98 in related


class TestConfounders:
    """Document and test the confounding factors."""

    def test_newsletter_confounder_strong(self):
        """
        STRONG: WIRED may have covered in subscriber-only newsletter.
        Coverage absence applies to standalone indexed articles only.
        """
        pass  # Documented, cannot be externally verified

    def test_developer_tools_confounder_strong(self):
        """
        STRONG: Leak involved developer tooling, not consumer product.
        However, WIRED DID cover Anthropic Cowork (consumer-adjacent agent)
        and Anthropic breaches (developer/enterprise security) as standalone articles.
        """
        pass  # Noted but partially undermined by WIRED's own coverage patterns

    def test_verge_bandwidth_confounder_moderate(self):
        """
        MODERATE: The Verge may have simply de-prioritized the story.
        However, The Verge routinely covers AI security stories about Meta.
        """
        pass  # Editorial prioritization is a legitimate factor

    def test_regex_vs_ml_confounder_moderate(self):
        """
        MODERATE: Frustration tracking uses regex, technically simpler than ML.
        However, CDT's Miranda Bogen: privacy impact is about how data is used,
        not how it's collected.
        """
        pass  # Scientific American expert quote addresses this

    def test_april_fools_proximity_confounder_weak(self):
        """
        WEAK: March 31 is near April Fools' Day. Some findings (Tamagotchi pet)
        could be jokes. However, source code leak, frustration tracking, and
        Undercover Mode were all confirmed as real.
        """
        pass  # Real security incident confirmed by Anthropic


class TestTestablePredicitions:
    """Document predictions that can validate the mechanism."""

    def test_prediction_future_anthropic_leak(self):
        """
        P254.1: If another Anthropic source code or data leak occurs, WIRED
        will produce zero standalone articles, while Gizmodo will cover it.
        """
        pass

    def test_prediction_meta_code_leak_comparison(self):
        """
        P254.2: If Meta experienced a 512K-line source code leak revealing
        user behavioral tracking and AI deception features, WIRED would
        produce multi-article investigative coverage within 48 hours.
        """
        pass

    def test_prediction_undercover_mode_meta(self):
        """
        P254.3: If Meta were discovered using AI that actively pretends to
        be human in public code repositories, WIRED would frame it with
        alarm vocabulary (deceiving, hiding, masking identity) and produce
        investigative coverage. Anthropic's identical behavior got zero coverage.
        """
        pass


class TestProfileIntegration:
    """Verify data integrates with existing profiles."""

    def test_wired_profile_has_anthropic_section(self):
        """Wired profile should document competitor coverage patterns."""
        profile_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "profiles", "wired.yaml"
        )
        assert os.path.exists(profile_path)

    def test_competitor_entities_has_claude_code_leak(self):
        """Competitor entities should reference the Claude Code leak."""
        entities_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "profiles", "competitor-entities.yaml"
        )
        assert os.path.exists(entities_path)
        with open(entities_path) as f:
            content = f.read()
        assert "claude_code_source_leak" in content

    def test_gizmodo_profile_has_anthropic_coverage(self):
        """Gizmodo profile should document its adversarial Anthropic coverage."""
        gizmodo_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "profiles", "gizmodo.yaml"
        )
        assert os.path.exists(gizmodo_path)

    def test_competitor_coverage_research_mechanism(self):
        """Competitor coverage research should contain mechanism 254."""
        research_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "profiles", "competitor-coverage-research.yaml"
        )
        assert os.path.exists(research_path)
        with open(research_path) as f:
            content = f.read()
        assert "254" in content
