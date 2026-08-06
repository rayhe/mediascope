"""
Dan Milmo (Guardian) Cross-Entity Coverage Analysis — Type B (Aug 6, 2026)

Tests validating how the Guardian's Global Technology Editor covers Meta vs
OpenAI vs Google across child safety, AI rogue agents, regulatory/GDPR, and
addictive design stories. Milmo is the anchor journalist at the publication
with the NARROWEST deal-partner asymmetry in the dataset — his cross-entity
coverage pattern is thus a test of the "partial independence" thesis.

KEY FINDING — "BIG TOBACCO" FRAMING ASYMMETRY:
Milmo used "big tobacco moment" language for Meta/YouTube's addictive design
verdicts (Mar 2026), a loaded metaphor pre-judging Meta as a public health
villain. When OpenAI's AI went rogue and hacked a startup (Jul 2026) — an
arguably MORE alarming public safety event — Milmo used neutral-to-factual
framing with quotes from OpenAI and the affected company. The "industry-
defining moment" editorial escalation was reserved for Meta, not OpenAI.

KEY FINDING — EDITORIAL LEADERSHIP ROLE:
As Global Technology Editor, Milmo sets the editorial framing for the entire
Guardian tech desk. His coverage choices (what gets the "big tobacco" label
vs what gets factual relay treatment) are not individual reporter decisions
but EDITORIAL DIRECTION for the publication's tech vertical.
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), "..", "profiles")


def load_yaml(filename):
    filepath = os.path.join(PROFILES_DIR, filename)
    with open(filepath) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def research():
    return load_yaml("competitor-coverage-research.yaml")


@pytest.fixture(scope="module")
def guardian_profile():
    return load_yaml("guardian.yaml")


@pytest.fixture(scope="module")
def entities():
    return load_yaml("competitor-entities.yaml")


@pytest.fixture(scope="module")
def guardian_research(research):
    return research["publications"]["guardian"]


@pytest.fixture(scope="module")
def milmo_data(guardian_profile):
    return guardian_profile["journalist_cross_entity"]["dan_milmo"]


# ================================================================
# CLASS 1: Dan Milmo Editorial Role
# ================================================================


class TestDanMilmoEditorialRole:
    """Verify Milmo's role and editorial significance are documented."""

    def test_milmo_is_global_tech_editor(self, milmo_data):
        """Milmo is the Guardian's Global Technology Editor."""
        assert milmo_data["role"] == "global_technology_editor"

    def test_milmo_editorial_scope(self, milmo_data):
        """Milmo's role is editorial leadership, not just byline reporting."""
        assert "editorial" in milmo_data["significance"].lower()

    def test_milmo_tenure_since_2021(self, milmo_data):
        """Milmo has been in role since 2021, providing long-term data."""
        assert "2021" in str(milmo_data.get("tenure_start", ""))

    def test_milmo_entity_coverage_count(self, milmo_data):
        """Milmo has cross-entity data for at least 3 entities."""
        entities_covered = milmo_data["entity_coverage"]
        assert len(entities_covered) >= 3


# ================================================================
# CLASS 2: Meta Coverage Framing
# ================================================================


class TestMilmoMetaCoverage:
    """Verify Milmo's Meta coverage patterns and language."""

    def test_meta_coverage_tone_negative(self, milmo_data):
        """Milmo's overall Meta coverage tone is adversarial."""
        meta = milmo_data["entity_coverage"]["meta"]
        assert meta["tone"] <= -0.3

    def test_big_tobacco_framing_exists(self, milmo_data):
        """Milmo used 'big tobacco' framing for Meta."""
        meta = milmo_data["entity_coverage"]["meta"]
        examples = meta.get("examples", [])
        big_tobacco = [e for e in examples if "big tobacco" in e.get("framing", "").lower()
                       or "big tobacco" in e.get("title", "").lower()]
        assert len(big_tobacco) > 0, "Milmo should have 'big tobacco' example for Meta"

    def test_meta_child_safety_focus(self, milmo_data):
        """Milmo's Meta coverage includes child safety stories."""
        meta = milmo_data["entity_coverage"]["meta"]
        examples = meta.get("examples", [])
        child_safety = [e for e in examples if "child" in e.get("framing", "").lower()
                        or "teen" in e.get("framing", "").lower()
                        or "molly" in e.get("title", "").lower()]
        assert len(child_safety) > 0

    def test_meta_gdpr_fines_covered(self, milmo_data):
        """Milmo covered Meta's GDPR fines."""
        meta = milmo_data["entity_coverage"]["meta"]
        examples = meta.get("examples", [])
        gdpr = [e for e in examples if "gdpr" in e.get("framing", "").lower()
                or "fined" in e.get("title", "").lower()
                or "€405" in e.get("title", "")]
        assert len(gdpr) > 0

    def test_meta_coverage_has_source_urls(self, milmo_data):
        """All Milmo Meta examples have source URLs."""
        meta = milmo_data["entity_coverage"]["meta"]
        examples = meta.get("examples", [])
        for ex in examples:
            assert ex.get("source_url"), f"Missing source_url for: {ex.get('title')}"


# ================================================================
# CLASS 3: OpenAI Coverage Framing
# ================================================================


class TestMilmoOpenAICoverage:
    """Verify Milmo's OpenAI coverage patterns and language."""

    def test_openai_coverage_tone_balanced(self, milmo_data):
        """Milmo's OpenAI coverage tone is balanced to slightly critical."""
        openai = milmo_data["entity_coverage"]["openai"]
        # Should be closer to neutral than Meta coverage
        assert openai["tone"] >= -0.35

    def test_rogue_agent_coverage_exists(self, milmo_data):
        """Milmo covered the OpenAI rogue agent incident."""
        openai = milmo_data["entity_coverage"]["openai"]
        examples = openai.get("examples", [])
        rogue = [e for e in examples if "rogue" in e.get("title", "").lower()
                 or "hack" in e.get("title", "").lower()]
        assert len(rogue) > 0

    def test_no_big_tobacco_applied_to_openai(self, milmo_data):
        """Milmo never APPLIED 'big tobacco' framing to OpenAI (mentions of absence don't count)."""
        openai = milmo_data["entity_coverage"]["openai"]
        examples = openai.get("examples", [])
        # Only flag if "big tobacco" appears WITHOUT "no" qualifier before it
        big_tobacco_applied = [e for e in examples
                               if "big tobacco" in e.get("framing", "").lower()
                               and "no 'big tobacco'" not in e.get("framing", "").lower()
                               and "no \"big tobacco\"" not in e.get("framing", "").lower()]
        assert len(big_tobacco_applied) == 0, "OpenAI should not receive applied 'big tobacco' framing"

    def test_rogue_agent_framing_is_factual(self, milmo_data):
        """OpenAI rogue agent coverage uses factual relay, not editorial escalation."""
        openai = milmo_data["entity_coverage"]["openai"]
        examples = openai.get("examples", [])
        rogue = [e for e in examples if "rogue" in e.get("title", "").lower()
                 or "hack" in e.get("title", "").lower()]
        for r in rogue:
            framing = r.get("framing", "").lower()
            # Should mention factual or quote-based framing, not loaded language
            assert any(term in framing for term in ["factual", "quote", "relay", "balanced"]), \
                f"Rogue agent coverage should be factual, got: {r.get('framing')}"

    def test_openai_coverage_has_source_urls(self, milmo_data):
        """All Milmo OpenAI examples have source URLs."""
        openai = milmo_data["entity_coverage"]["openai"]
        examples = openai.get("examples", [])
        for ex in examples:
            assert ex.get("source_url"), f"Missing source_url for: {ex.get('title')}"


# ================================================================
# CLASS 4: Big Tobacco Framing Asymmetry
# ================================================================


class TestBigTobaccoFramingAsymmetry:
    """The 'big tobacco' label is reserved for Meta, not OpenAI, despite
    OpenAI's AI rogue agent hack being an arguably more alarming safety event."""

    def test_big_tobacco_meta_only(self, milmo_data):
        """'Big tobacco' language is APPLIED in Meta coverage only (contrast mentions don't count)."""
        for entity_name, entity_data in milmo_data["entity_coverage"].items():
            examples = entity_data.get("examples", [])
            for ex in examples:
                framing = ex.get("framing", "").lower()
                # Only count if "big tobacco" appears WITHOUT being negated
                if "big tobacco" in framing \
                        and "no 'big tobacco'" not in framing \
                        and "no \"big tobacco\"" not in framing:
                    assert entity_name == "meta", \
                        f"Applied 'big tobacco' framing found for {entity_name}, should be Meta-only"

    def test_meta_tone_more_negative_than_openai(self, milmo_data):
        """Milmo's Meta tone is more negative than OpenAI tone."""
        meta_tone = milmo_data["entity_coverage"]["meta"]["tone"]
        openai_tone = milmo_data["entity_coverage"]["openai"]["tone"]
        assert meta_tone < openai_tone, \
            f"Meta ({meta_tone}) should be more negative than OpenAI ({openai_tone})"

    def test_tone_gap_documented(self, milmo_data):
        """The tone gap between Meta and OpenAI is documented."""
        meta_tone = milmo_data["entity_coverage"]["meta"]["tone"]
        openai_tone = milmo_data["entity_coverage"]["openai"]["tone"]
        gap = openai_tone - meta_tone
        assert gap >= 0.15, f"Tone gap ({gap}) should be at least 0.15"

    def test_framing_escalation_asymmetry(self, milmo_data):
        """Meta gets editorial escalation language; OpenAI gets factual relay."""
        asymmetry = milmo_data.get("framing_asymmetry", {})
        assert "big_tobacco" in asymmetry or "editorial_escalation" in asymmetry, \
            "Framing asymmetry section should document big tobacco/editorial escalation"

    def test_proportionality_gap(self, milmo_data):
        """Meta addictive design got 'industry-defining' framing while OpenAI
        rogue agent hack got balanced reporting — disproportionate to actual risk."""
        asymmetry = milmo_data.get("framing_asymmetry", {})
        assert "proportionality" in str(asymmetry).lower() or \
               "disproportionate" in str(asymmetry).lower() or \
               "proportional" in str(asymmetry).lower(), \
            "Framing asymmetry should document proportionality gap"


# ================================================================
# CLASS 5: Google Coverage
# ================================================================


class TestMilmoGoogleCoverage:
    """Verify Milmo's Google coverage patterns."""

    def test_google_coverage_exists(self, milmo_data):
        """Milmo has Google cross-entity data."""
        assert "google" in milmo_data["entity_coverage"]

    def test_google_tone_documented(self, milmo_data):
        """Google coverage tone is documented."""
        google = milmo_data["entity_coverage"]["google"]
        assert "tone" in google

    def test_google_regulatory_focus(self, milmo_data):
        """Milmo's Google coverage focuses on regulatory/competition."""
        google = milmo_data["entity_coverage"]["google"]
        examples = google.get("examples", [])
        regulatory = [e for e in examples if any(
            term in e.get("framing", "").lower()
            for term in ["regulatory", "competition", "fine", "antitrust"]
        )]
        assert len(regulatory) > 0


# ================================================================
# CLASS 6: Editorial Leadership Influence
# ================================================================


class TestMilmoEditorialLeadership:
    """Milmo as Global Technology Editor sets the framing for the entire desk."""

    def test_editorial_direction_documented(self, milmo_data):
        """Milmo's editorial leadership role is documented."""
        sig = milmo_data.get("significance", "")
        assert "editor" in sig.lower() or "leadership" in sig.lower()

    def test_desk_wide_influence(self, milmo_data):
        """Milmo's framing choices affect the entire Guardian tech vertical."""
        sig = milmo_data.get("significance", "")
        assert "desk" in sig.lower() or "vertical" in sig.lower() or \
               "direction" in sig.lower() or "editorial" in sig.lower()

    def test_milmo_not_just_reporter(self, milmo_data):
        """Milmo is editor, not just a reporter — his framing is institutional."""
        role = milmo_data.get("role", "")
        assert "editor" in role.lower()


# ================================================================
# CLASS 7: Consistency with Guardian Publication Profile
# ================================================================


class TestMilmoGuardianConsistency:
    """Milmo's cross-entity pattern should match the Guardian's overall profile."""

    def test_milmo_meta_tone_matches_publication(self, milmo_data, guardian_research):
        """Milmo's Meta tone aligns with the Guardian's overall adversarial Meta tone."""
        pub_tone = guardian_research["meta_coverage_tone"]
        assert pub_tone == "adversarial"
        milmo_meta_tone = milmo_data["entity_coverage"]["meta"]["tone"]
        assert milmo_meta_tone <= -0.3, "Milmo Meta tone should be adversarial"

    def test_milmo_openai_tone_matches_publication(self, milmo_data, guardian_research):
        """Milmo's OpenAI tone aligns with the Guardian's balanced_to_adversarial rating."""
        pub_tone = guardian_research["openai_coverage_tone"]
        assert pub_tone == "balanced_to_adversarial"
        milmo_openai_tone = milmo_data["entity_coverage"]["openai"]["tone"]
        assert -0.4 <= milmo_openai_tone <= 0.0, \
            f"Milmo OpenAI tone ({milmo_openai_tone}) should be balanced-to-adversarial"

    def test_milmo_gap_narrower_than_wired(self, milmo_data):
        """Milmo's Meta-OpenAI gap should be narrower than WIRED's ~0.95."""
        meta_tone = milmo_data["entity_coverage"]["meta"]["tone"]
        openai_tone = milmo_data["entity_coverage"]["openai"]["tone"]
        gap = openai_tone - meta_tone
        assert gap < 0.95, f"Milmo gap ({gap}) should be narrower than WIRED's ~0.95"

    def test_partial_independence_model(self, milmo_data):
        """Milmo's pattern reinforces the Guardian's 'partial independence' classification."""
        verdict = milmo_data.get("cross_entity_verdict", "")
        assert "partial" in verdict.lower() or "independence" in verdict.lower() or \
               "narrower" in verdict.lower()


# ================================================================
# CLASS 8: ChatGPT Health Misinformation Comparison
# ================================================================


class TestChatGPTHealthMisinformationComparison:
    """Compare Milmo's coverage of Meta child safety harm vs ChatGPT health
    misinformation — both involve platform-mediated harm to users."""

    def test_chatgpt_health_example_exists(self, milmo_data):
        """Milmo covered ChatGPT health misinformation."""
        openai = milmo_data["entity_coverage"]["openai"]
        examples = openai.get("examples", [])
        health = [e for e in examples if "health" in e.get("title", "").lower()
                  or "salt" in e.get("title", "").lower()
                  or "bromism" in e.get("title", "").lower()]
        assert len(health) > 0, "Milmo should have ChatGPT health misinformation example"

    def test_chatgpt_health_tone_less_severe(self, milmo_data):
        """ChatGPT health misinformation coverage is less severe than Meta child safety."""
        openai = milmo_data["entity_coverage"]["openai"]
        examples = openai.get("examples", [])
        health = [e for e in examples if "health" in e.get("title", "").lower()
                  or "salt" in e.get("title", "").lower()
                  or "bromism" in e.get("title", "").lower()]
        meta = milmo_data["entity_coverage"]["meta"]
        meta_examples = meta.get("examples", [])
        child_safety = [e for e in meta_examples if "child" in e.get("framing", "").lower()
                        or "teen" in e.get("framing", "").lower()
                        or "molly" in e.get("title", "").lower()]
        if health and child_safety:
            assert health[0].get("tone", 0) > child_safety[0].get("tone", 0), \
                "ChatGPT health coverage should be less severe than Meta child safety"


# ================================================================
# CLASS 9: Source URL Verification
# ================================================================


class TestMilmoSourceURLs:
    """All cross-entity examples must have verifiable source URLs."""

    def test_all_entities_have_source_urls(self, milmo_data):
        """Every entity's examples should have source URLs."""
        for entity_name, entity_data in milmo_data["entity_coverage"].items():
            examples = entity_data.get("examples", [])
            for ex in examples:
                assert ex.get("source_url"), \
                    f"Missing source_url for {entity_name}: {ex.get('title')}"

    def test_source_urls_are_valid(self, milmo_data):
        """Source URLs should be well-formed HTTP(S) URLs."""
        for entity_name, entity_data in milmo_data["entity_coverage"].items():
            examples = entity_data.get("examples", [])
            for ex in examples:
                url = ex.get("source_url", "")
                assert url.startswith("http://") or url.startswith("https://"), \
                    f"Invalid URL for {entity_name}: {url}"

    def test_meta_has_at_least_3_examples(self, milmo_data):
        """Meta coverage should have at least 3 documented examples."""
        meta = milmo_data["entity_coverage"]["meta"]
        assert len(meta.get("examples", [])) >= 3

    def test_openai_has_at_least_3_examples(self, milmo_data):
        """OpenAI coverage should have at least 3 documented examples."""
        openai = milmo_data["entity_coverage"]["openai"]
        assert len(openai.get("examples", [])) >= 3
