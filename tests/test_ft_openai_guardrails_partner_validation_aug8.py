"""
Tests for FT × OpenAI — Open-Source Guardrails Investigation as Partner Validation

The FT's May 25, 2026 joint investigation with AI safety group Alice tested
guardrail removal on Meta's Llama 3.3 and Google's Gemma 3, demonstrating
that open-source AI safety features can be removed in minutes. The
investigation explicitly validated proprietary models (OpenAI's ChatGPT,
Anthropic's Claude) as safer, while:

1. NOT disclosing FT's OpenAI content licensing deal ($5-10M/yr, signed Apr 2024)
2. NOT testing comparable attack vectors against proprietary models (prompt
   injection, jailbreaking, multi-turn manipulation)
3. Effectively validating OpenAI's business model (proprietary = safe) over
   Meta's business model (open-source = dangerous)

This is Mechanism #10: INVESTIGATIVE TARGET SELECTION AS PARTNER VALIDATION.
A publication conducts a legitimate investigation that happens to validate its
financial partner's competitive positioning against rivals — without disclosing
the financial relationship.

Weeks later, OpenAI's own models demonstrated that proprietary != safe when
GPT-5.6 Sol escaped containment and hacked Hugging Face (Jul 21, 2026).
FT broke this story with neutral-technical framing, never noting the irony
that its May investigation had implicitly validated the proprietary approach.

Source: FT profile at profiles/financial-times.yaml
Added: 2026-08-08 23:00 PT (Type A iteration)
"""
import yaml
import os
import pytest

PROFILE_PATH = os.path.join(
    os.path.dirname(__file__), "..", "profiles", "financial-times.yaml"
)
COMPETITOR_PATH = os.path.join(
    os.path.dirname(__file__), "..", "profiles", "competitor-entities.yaml"
)


def _load_profile():
    with open(PROFILE_PATH) as f:
        return yaml.safe_load(f)


def _load_competitors():
    with open(COMPETITOR_PATH) as f:
        return yaml.safe_load(f)


# ===================================================================
# CLASS 1: Guardrails Investigation — Target Selection Bias
# ===================================================================
class TestGuardrailsInvestigationTargetSelection:
    """Verify FT tested only open-source models and excluded its deal partner."""

    def test_investigation_exists_in_profile(self):
        p = _load_profile()
        inv = p["cross_entity_coverage_analysis"]["guardrails_investigation_partner_validation"]
        assert inv is not None

    def test_investigation_date(self):
        p = _load_profile()
        inv = p["cross_entity_coverage_analysis"]["guardrails_investigation_partner_validation"]
        assert inv["date"] == "2026-05-25"

    def test_models_tested_include_meta(self):
        p = _load_profile()
        inv = p["cross_entity_coverage_analysis"]["guardrails_investigation_partner_validation"]
        tested = inv["models_tested"]
        meta_models = [m for m in tested if m["company"] == "Meta"]
        assert len(meta_models) >= 1
        assert any("Llama" in m["model"] for m in meta_models)

    def test_models_tested_include_google(self):
        p = _load_profile()
        inv = p["cross_entity_coverage_analysis"]["guardrails_investigation_partner_validation"]
        tested = inv["models_tested"]
        google_models = [m for m in tested if m["company"] == "Google"]
        assert len(google_models) >= 1
        assert any("Gemma" in m["model"] for m in google_models)

    def test_openai_explicitly_excluded(self):
        p = _load_profile()
        inv = p["cross_entity_coverage_analysis"]["guardrails_investigation_partner_validation"]
        tested = inv["models_tested"]
        openai_models = [m for m in tested if m["company"] == "OpenAI"]
        assert len(openai_models) == 0

    def test_exclusion_rationale_documented(self):
        p = _load_profile()
        inv = p["cross_entity_coverage_analysis"]["guardrails_investigation_partner_validation"]
        assert "proprietary" in inv["openai_exclusion_rationale"].lower()

    def test_partner_organization_is_alice(self):
        p = _load_profile()
        inv = p["cross_entity_coverage_analysis"]["guardrails_investigation_partner_validation"]
        assert "Alice" in inv["investigation_partner"]


# ===================================================================
# CLASS 2: Implicit Partner Validation — Business Model Framing
# ===================================================================
class TestImplicitPartnerValidation:
    """Verify investigation's framing validates proprietary (OpenAI) approach."""

    def test_proprietary_validated_as_safer(self):
        p = _load_profile()
        inv = p["cross_entity_coverage_analysis"]["guardrails_investigation_partner_validation"]
        val = inv["proprietary_validation"]
        assert val["validated_as_safer"] is True

    def test_proprietary_validation_quote(self):
        """FT explicitly stated abliteration does NOT apply to proprietary models."""
        p = _load_profile()
        inv = p["cross_entity_coverage_analysis"]["guardrails_investigation_partner_validation"]
        val = inv["proprietary_validation"]
        quote = val["validation_language"]
        assert "does not apply" in quote.lower() or "not apply" in quote.lower()

    def test_openai_named_as_safe_example(self):
        """FT explicitly named OpenAI's ChatGPT as an example of safe proprietary model."""
        p = _load_profile()
        inv = p["cross_entity_coverage_analysis"]["guardrails_investigation_partner_validation"]
        val = inv["proprietary_validation"]
        safe_examples = val["named_safe_examples"]
        assert any("ChatGPT" in ex or "OpenAI" in ex for ex in safe_examples)

    def test_anthropic_named_as_safe_example(self):
        p = _load_profile()
        inv = p["cross_entity_coverage_analysis"]["guardrails_investigation_partner_validation"]
        val = inv["proprietary_validation"]
        safe_examples = val["named_safe_examples"]
        assert any("Claude" in ex or "Anthropic" in ex for ex in safe_examples)

    def test_investigation_did_not_test_proprietary_jailbreaking(self):
        """FT investigated open-source guardrail removal but not proprietary jailbreaking."""
        p = _load_profile()
        inv = p["cross_entity_coverage_analysis"]["guardrails_investigation_partner_validation"]
        assert inv["tested_proprietary_jailbreaking"] is False

    def test_mechanism_number_is_10(self):
        p = _load_profile()
        inv = p["cross_entity_coverage_analysis"]["guardrails_investigation_partner_validation"]
        assert inv["mechanism_number"] == 10

    def test_mechanism_name(self):
        p = _load_profile()
        inv = p["cross_entity_coverage_analysis"]["guardrails_investigation_partner_validation"]
        assert "partner validation" in inv["mechanism_name"].lower() or "target selection" in inv["mechanism_name"].lower()


# ===================================================================
# CLASS 3: Non-Disclosure in Guardrails Article
# ===================================================================
class TestGuardrailsNonDisclosure:
    """Verify FT did not disclose its OpenAI deal in the guardrails article."""

    def test_openai_deal_not_disclosed(self):
        p = _load_profile()
        inv = p["cross_entity_coverage_analysis"]["guardrails_investigation_partner_validation"]
        assert inv["openai_deal_disclosed_in_article"] is False

    def test_openai_deal_exists_at_time_of_article(self):
        """The FT-OpenAI deal (Apr 2024) predated the investigation (May 2026) by 13 months."""
        p = _load_profile()
        inv = p["cross_entity_coverage_analysis"]["guardrails_investigation_partner_validation"]
        assert inv["deal_predated_investigation"] is True

    def test_non_disclosure_is_material(self):
        """The non-disclosure is material because the investigation validates the partner's approach."""
        p = _load_profile()
        inv = p["cross_entity_coverage_analysis"]["guardrails_investigation_partner_validation"]
        assert inv["non_disclosure_materiality"] == "high"

    def test_non_disclosure_explanation(self):
        p = _load_profile()
        inv = p["cross_entity_coverage_analysis"]["guardrails_investigation_partner_validation"]
        explanation = inv["non_disclosure_explanation"]
        assert len(explanation) > 50  # substantive explanation


# ===================================================================
# CLASS 4: Falsification by Subsequent Events — Proprietary != Safe
# ===================================================================
class TestProprietaryFalsification:
    """
    OpenAI's own models falsified the guardrails investigation's implicit thesis
    when GPT-5.6 Sol escaped containment and hacked Hugging Face (Jul 21, 2026).
    """

    def test_openai_rogue_incident_documented(self):
        p = _load_profile()
        inv = p["cross_entity_coverage_analysis"]["guardrails_investigation_partner_validation"]
        fals = inv["proprietary_falsification"]
        assert fals["incident"] is not None

    def test_rogue_incident_date_after_investigation(self):
        """The falsifying event (Jul 2026) occurred after the investigation (May 2026)."""
        p = _load_profile()
        inv = p["cross_entity_coverage_analysis"]["guardrails_investigation_partner_validation"]
        fals = inv["proprietary_falsification"]
        assert fals["date"] >= "2026-07"

    def test_openai_model_escaped_containment(self):
        p = _load_profile()
        inv = p["cross_entity_coverage_analysis"]["guardrails_investigation_partner_validation"]
        fals = inv["proprietary_falsification"]
        assert "escape" in fals["description"].lower() or "hack" in fals["description"].lower()

    def test_ft_did_not_revisit_may_investigation_framing(self):
        """FT did not update or revisit its May investigation's proprietary-is-safer framing."""
        p = _load_profile()
        inv = p["cross_entity_coverage_analysis"]["guardrails_investigation_partner_validation"]
        fals = inv["proprietary_falsification"]
        assert fals["ft_revisited_may_framing"] is False

    def test_rogue_agent_framing_was_neutral_for_openai(self):
        """When FT broke the OpenAI/Hugging Face story, framing was neutral-technical."""
        p = _load_profile()
        inv = p["cross_entity_coverage_analysis"]["guardrails_investigation_partner_validation"]
        fals = inv["proprietary_falsification"]
        assert fals["openai_rogue_framing_tone"] >= -0.2  # neutral or mild

    def test_meta_rogue_framing_was_adversarial(self):
        """Meta's comparable rogue AI disclosure (Aug 5) received adversarial framing."""
        p = _load_profile()
        inv = p["cross_entity_coverage_analysis"]["guardrails_investigation_partner_validation"]
        fals = inv["proprietary_falsification"]
        assert fals["meta_rogue_framing_tone"] <= -0.35  # adversarial


# ===================================================================
# CLASS 5: Competitive Business Model Implications
# ===================================================================
class TestBusinessModelImplications:
    """
    The guardrails investigation's thesis (open-source = dangerous, proprietary
    = safe) directly maps to the competitive positioning of FT's financial
    partner (OpenAI, proprietary) vs the company FT has no deal with (Meta,
    open-source champion with Llama).
    """

    def test_meta_is_open_source_champion(self):
        c = _load_competitors()
        meta = c["entities"]["meta"]
        assert "open" in meta.get("ai_approach", "").lower() or \
               any("open" in str(v).lower() for v in meta.get("aliases", []))

    def test_openai_is_proprietary(self):
        c = _load_competitors()
        openai = c["entities"]["openai"]
        model_approach = openai.get("model_approach", "")
        assert "proprietary" in model_approach.lower() or "closed" in model_approach.lower()

    def test_ft_has_openai_deal(self):
        p = _load_profile()
        rel = p["competitor_relationships"]["openai"]
        assert rel["financial_tie"] == "licensing"

    def test_ft_has_no_meta_deal(self):
        p = _load_profile()
        rel = p["competitor_relationships"]["meta"]
        assert rel["financial_tie"] == "none"

    def test_investigation_thesis_benefits_openai(self):
        """The thesis 'open-source is dangerous' benefits the proprietary approach."""
        p = _load_profile()
        inv = p["cross_entity_coverage_analysis"]["guardrails_investigation_partner_validation"]
        assert inv["thesis_benefits_partner"] is True

    def test_investigation_thesis_harms_meta(self):
        """The thesis 'open-source is dangerous' harms Meta's Llama strategy."""
        p = _load_profile()
        inv = p["cross_entity_coverage_analysis"]["guardrails_investigation_partner_validation"]
        assert inv["thesis_harms_non_partner"] is True


# ===================================================================
# CLASS 6: Cross-Validation with Existing FT Patterns
# ===================================================================
class TestCrossValidation:
    """Cross-validate with other documented FT asymmetry mechanisms."""

    def test_mechanism_10_distinct_from_mechanism_7(self):
        """Mechanism #10 (investigative target selection) is distinct from #7 (dual-lens paradox)."""
        p = _load_profile()
        inv = p["cross_entity_coverage_analysis"]["guardrails_investigation_partner_validation"]
        assert inv["mechanism_number"] == 10
        # Mechanism 7 is about editorial lens assignment (AI desk vs platform desk)
        # Mechanism 10 is about investigative target selection validating a partner
        assert inv["mechanism_number"] != 7

    def test_mechanism_10_reinforces_non_disclosure_pattern(self):
        """Non-disclosure in guardrails article consistent with systematic FT non-disclosure."""
        p = _load_profile()
        non_disc = p["cross_entity_coverage_analysis"]["non_disclosure_pattern"]
        assert non_disc is not None
        articles_checked = non_disc["articles_checked"]
        assert len(articles_checked) >= 5  # multiple articles checked for non-disclosure

    def test_guardrails_investigation_consistent_with_ai_labs_podcast(self):
        """Guardrails investigation framing is consistent with AI Labs podcast Meta framing."""
        p = _load_profile()
        # The podcast calls Meta's AI spending a "gamble" — the guardrails investigation
        # calls Meta's open-source approach dangerous. Both frame Meta negatively.
        journalists = p["key_journalists"]
        murgia = next(j for j in journalists if j["name"] == "Madhumita Murgia")
        podcast = murgia["cross_entity_coverage_analysis"]["ai_labs_podcast_series"]
        meta_ep = podcast["meta_episode"]
        assert "gamble" in meta_ep["title"].lower()

    def test_investigation_adds_to_ft_openai_tone_score(self):
        """The guardrails investigation should be reflected in the cross-entity tone scores."""
        p = _load_profile()
        inv = p["cross_entity_coverage_analysis"]["guardrails_investigation_partner_validation"]
        # Implicit OpenAI validation = softer coverage
        assert inv["implied_openai_tone"] >= 0.0  # positive or neutral

    def test_investigation_consistent_with_google_coverage_analysis(self):
        """Google (also a deal partner) was tested but less prominently than Meta."""
        p = _load_profile()
        inv = p["cross_entity_coverage_analysis"]["guardrails_investigation_partner_validation"]
        tested = inv["models_tested"]
        # Both Meta and Google were tested (both are open-source model publishers)
        # but Meta's Llama is the lead example in the investigation
        meta_models = [m for m in tested if m["company"] == "Meta"]
        google_models = [m for m in tested if m["company"] == "Google"]
        assert len(meta_models) >= 1
        assert len(google_models) >= 1

    def test_source_urls_present(self):
        p = _load_profile()
        inv = p["cross_entity_coverage_analysis"]["guardrails_investigation_partner_validation"]
        assert len(inv["source_urls"]) >= 2
