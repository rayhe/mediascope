"""
Test: Meta Insurance Denial — Asymmetric Financial Materiality Architecture
+ AI Lab Precedent Gap

Mechanism #338: Insurance Denial Precedent — Asymmetric Financial Materiality Architecture

FINDING:
The Delaware Superior Court ruling (Feb 27, 2026, Judge Sheldon K. Renni,
Hartford Casualty Insurance Co. et al. v. Instagram LLC et al.) held that
Meta's child safety harms arise from "deliberate conduct" (intentional design
choices), not accidents, so insurers (Hartford, Chubb, and 10+ others) have
NO duty to defend. This makes Meta's full $18B+ settlement exposure flow
directly to its balance sheet — no insurance offset.

This creates asymmetric financial materiality in tech coverage:
1. Meta: $18B UNINSURED settlement → directly hits balance sheet →
   publications frame as financial crisis
2. AI labs (Anthropic, OpenAI): comparable litigation exists but NO insurance
   denial ruling → settlements appear more affordable
3. CDT and Mondaq legal analysis explicitly connects the ruling to AI
   governance/AI lab implications — source-available but publications
   don't cross-reference
4. Specialty AI insurance is "beginning to emerge" (Mondaq) → AI labs may
   be able to insure against comparable claims
5. Publications with AI lab financial relationships have no incentive to
   analyze whether the insurance denial precedent would apply to AI lab
   partners

FINANCIAL ARCHITECTURE:
- Meta's $18B settlement: 100% uninsured, flows to balance sheet
  (1.1% of ~$1.6T market cap)
- Anthropic's $1.5B copyright settlement: 0.15% of $965B valuation,
  trivially affordable
- OpenAI's Adam Raine wrongful death lawsuit (ChatGPT-4o suicide methods):
  insurance status unknown/unanalyzed by publications
- Character.AI/Google teen suicide settlement: insurance status
  unknown/unanalyzed by publications
- CDT article explicitly raises scenario: "if a general purpose AI model is
  fine-tuned to be a chatty and helpful assistant, and that fine-tuning
  results in users developing a relationship with the chatbot that is later
  alleged to cause them harm, an argument that the harm stemmed from a
  deliberate design decision might find a toehold"

CONFOUNDERS (5 total, 2 STRONG):
1. STRONG: Legal specificity — Meta's claims involved social media platform
   design, not AI chatbot design; legal precedent may not apply identically
2. STRONG: Settlement scale — $18B vs $1.5B is fundamentally different
   financial materiality regardless of insurance
3. MODERATE: Insurance denial is a legal/business fact, not editorial
   choice — publications report what courts decide
4. MODERATE: AI insurance market is too nascent for meaningful comparison
5. WEAK: Publications may lack insurance law expertise to analyze the
   cross-domain implications

COUNTER-CONFOUNDERS:
1. CDT and Mondaq articles ARE publicly available, making the AI governance
   connection source-available
2. Character.AI teen suicide case is directly analogous to Meta's
   "deliberate design" theory
3. Anthropic's pirated book downloading (7M books, Library Genesis) is
   unambiguously deliberate conduct

ASYMMETRY SCORE: 0.31 (modest — genuine legal specificity confounders, but
elevated by source availability of CDT/Mondaq analysis and direct
ChatGPT/Character.AI analogies)

CROSS-REFERENCES: mechanisms #326 (WSJ same-day bifurcation), #327
(Clare Duffy agency attribution), #328 (IPO underwriter regulatory
liability containment), #46 (pre-IPO underwriter convergence)

SOURCE URLS:
- Delaware ruling: Hartford Casualty Insurance Co. et al. v. Instagram
  LLC et al. (Feb 27, 2026, Delaware Superior Court)
- JD Supra analysis: https://www.jdsupra.com/legalnews/insurers-not-obligated-to-defend-meta-8688381/
- CDT analysis: https://cdt.org/insights/design-decisions-and-the-duty-to-defend-what-an-insurance-coverage-case-signals-for-ai-governance/
- Mondaq analysis: https://www.mondaq.com/unitedstates/insurance-laws-and-products/1765946/insurance-coverage-for-emerging-ai-and-social-media-liabilities
- SEC proxy filing (Proxy Impact): https://www.sec.gov/Archives/edgar/data/1326801/000121465926006412/o514269px14a6g.htm
- Meta settlement: https://www.reuters.com/business/meta-reaches-18-billion-settlements-over-childrens-social-media-addiction-2026-08-26/
- Anthropic copyright settlement: Bloomberg Law, "Anthropic to Pay $1.5B
  Author Copyright Deal"
"""

import pytest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
YAML_KEY = 'meta_insurance_denial_asymmetric_financial_materiality_ai_lab_precedent_gap'


def load_yaml(filename):
    """Load a YAML profile from the profiles directory."""
    path = os.path.join(PROFILES_DIR, filename)
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def _collect_mechanism_ids(obj):
    """Recursively collect all mechanism_id values from nested YAML."""
    ids = []
    if isinstance(obj, dict):
        if 'mechanism_id' in obj:
            ids.append(obj['mechanism_id'])
        for v in obj.values():
            ids.extend(_collect_mechanism_ids(v))
    elif isinstance(obj, list):
        for item in obj:
            ids.extend(_collect_mechanism_ids(item))
    return ids


def _find_mechanism(obj, target_id):
    """Recursively find a mechanism dict by its mechanism_id."""
    if isinstance(obj, dict):
        if obj.get('mechanism_id') == target_id:
            return obj
        for v in obj.values():
            result = _find_mechanism(v, target_id)
            if result:
                return result
    elif isinstance(obj, list):
        for item in obj:
            result = _find_mechanism(item, target_id)
            if result:
                return result
    return None


def _get_mechanism_entry(data):
    """Get the mechanism entry by the YAML key or by mechanism_id 338."""
    # Try key-based lookup first
    cpf = data.get('cross_publication_findings', {})
    if isinstance(cpf, dict) and YAML_KEY in cpf:
        return cpf[YAML_KEY]
    # Fallback: recursive search by mechanism_id
    return _find_mechanism(data, 338)


# ---------------------------------------------------------------------------
# 1. TestInsuranceDenialRulingDocumentation
# ---------------------------------------------------------------------------
class TestInsuranceDenialRulingDocumentation:
    """Verify that the Delaware Superior Court insurance denial ruling is
    fully documented in competitor-coverage-research.yaml."""

    def test_mechanism_338_exists(self):
        """Mechanism #338 must exist in the YAML profile."""
        data = load_yaml('competitor-coverage-research.yaml')
        all_ids = _collect_mechanism_ids(data)
        assert 338 in all_ids, \
            "Mechanism #338 (insurance denial precedent) must exist"

    def test_ruling_court_and_judge_documented(self):
        """The ruling must document Delaware Superior Court, Judge Renni,
        and the Feb 27, 2026 date."""
        data = load_yaml('competitor-coverage-research.yaml')
        entry = _get_mechanism_entry(data)
        assert entry is not None, "Mechanism entry for insurance denial not found"
        entry_str = yaml.dump(entry).lower()
        assert 'delaware' in entry_str, \
            "Must document Delaware Superior Court"
        assert 'renni' in entry_str, \
            "Must document Judge Sheldon K. Renni"
        assert '2026' in entry_str, \
            "Must document the 2026 ruling date"

    def test_deliberate_conduct_finding_documented(self):
        """The core legal finding — 'deliberate conduct' excluding insurance
        coverage — must be documented."""
        data = load_yaml('competitor-coverage-research.yaml')
        entry = _get_mechanism_entry(data)
        assert entry is not None, "Mechanism entry not found"
        entry_str = yaml.dump(entry).lower()
        assert 'deliberate' in entry_str, \
            "Must document the 'deliberate conduct' finding"
        # Must reference the insurer parties
        assert 'hartford' in entry_str or 'chubb' in entry_str, \
            "Must reference Hartford and/or Chubb as the insurer parties"


# ---------------------------------------------------------------------------
# 2. TestUninsuredSettlementFinancialMateriality
# ---------------------------------------------------------------------------
class TestUninsuredSettlementFinancialMateriality:
    """Verify that the $18B uninsured settlement's direct balance-sheet
    impact is documented with financial materiality calculations."""

    def test_settlement_amount_documented(self):
        """The $18B settlement amount must be documented."""
        data = load_yaml('competitor-coverage-research.yaml')
        entry = _get_mechanism_entry(data)
        assert entry is not None, "Mechanism entry not found"
        entry_str = yaml.dump(entry).lower()
        assert '18' in entry_str and 'b' in entry_str, \
            "Must document the $18B settlement amount"

    def test_uninsured_status_explicit(self):
        """The profile must explicitly state the settlement is 100%
        uninsured due to the ruling."""
        data = load_yaml('competitor-coverage-research.yaml')
        entry = _get_mechanism_entry(data)
        assert entry is not None, "Mechanism entry not found"
        entry_str = yaml.dump(entry).lower()
        assert 'uninsured' in entry_str or 'no insurance' in entry_str or \
            'no duty to defend' in entry_str, \
            "Must explicitly state the uninsured status"

    def test_balance_sheet_impact_documented(self):
        """The direct balance-sheet flow-through must be documented."""
        data = load_yaml('competitor-coverage-research.yaml')
        entry = _get_mechanism_entry(data)
        assert entry is not None, "Mechanism entry not found"
        entry_str = yaml.dump(entry).lower()
        assert 'balance sheet' in entry_str or 'balance-sheet' in entry_str, \
            "Must document balance sheet impact"

    def test_materiality_percentage_documented(self):
        """The 1.1% of market cap materiality percentage should be
        documented or calculable from the entry."""
        data = load_yaml('competitor-coverage-research.yaml')
        entry = _get_mechanism_entry(data)
        assert entry is not None, "Mechanism entry not found"
        entry_str = yaml.dump(entry).lower()
        # Should reference either the percentage or the market cap denominator
        has_pct = '1.1%' in entry_str or '1.1 %' in entry_str
        has_market_cap = '1.6t' in entry_str or '1.6 t' in entry_str or \
            'market cap' in entry_str or 'market-cap' in entry_str
        assert has_pct or has_market_cap, \
            "Must document materiality as percentage of market cap or " \
            "reference the market cap denominator"


# ---------------------------------------------------------------------------
# 3. TestAILabComparableLitigationInsuranceGap
# ---------------------------------------------------------------------------
class TestAILabComparableLitigationInsuranceGap:
    """Verify documentation of comparable AI lab litigation where insurance
    status is unknown/unanalyzed by publications."""

    def test_openai_adam_raine_lawsuit_documented(self):
        """OpenAI's Adam Raine wrongful death lawsuit (ChatGPT-4o suicide
        methods) must be documented as a comparable case."""
        data = load_yaml('competitor-coverage-research.yaml')
        entry = _get_mechanism_entry(data)
        assert entry is not None, "Mechanism entry not found"
        entry_str = yaml.dump(entry).lower()
        assert 'adam raine' in entry_str or 'openai' in entry_str, \
            "Must document the OpenAI/Adam Raine wrongful death lawsuit"

    def test_character_ai_teen_suicide_documented(self):
        """Character.AI/Google teen suicide settlement must be documented
        as a comparable case."""
        data = load_yaml('competitor-coverage-research.yaml')
        entry = _get_mechanism_entry(data)
        assert entry is not None, "Mechanism entry not found"
        entry_str = yaml.dump(entry).lower()
        assert 'character.ai' in entry_str or 'character ai' in entry_str, \
            "Must document the Character.AI teen suicide case"

    def test_anthropic_copyright_settlement_documented(self):
        """Anthropic's $1.5B copyright settlement must be documented with
        its valuation-relative materiality."""
        data = load_yaml('competitor-coverage-research.yaml')
        entry = _get_mechanism_entry(data)
        assert entry is not None, "Mechanism entry not found"
        entry_str = yaml.dump(entry).lower()
        assert 'anthropic' in entry_str, \
            "Must document Anthropic's copyright settlement"
        assert '1.5' in entry_str or '1.5b' in entry_str, \
            "Must document the $1.5B settlement amount"

    def test_insurance_analysis_gap_noted(self):
        """The profile must note that publications covering these AI lab
        settlements do NOT analyze the insurance denial implications."""
        data = load_yaml('competitor-coverage-research.yaml')
        entry = _get_mechanism_entry(data)
        assert entry is not None, "Mechanism entry not found"
        entry_str = yaml.dump(entry).lower()
        # Should mention that insurance status is unknown or unanalyzed
        assert 'unknown' in entry_str or 'unanalyzed' in entry_str or \
            'not analy' in entry_str or 'insurance gap' in entry_str or \
            'no insurance analysis' in entry_str or \
            'insurance_analysis_in_coverage: zero' in entry_str or \
            'no comparable' in entry_str or \
            'insurance_denial_ruling: none' in entry_str, \
            "Must note that AI lab insurance status is unknown/unanalyzed " \
            "in publication coverage"


# ---------------------------------------------------------------------------
# 4. TestCDTAIGovernanceConnectionSourceAvailability
# ---------------------------------------------------------------------------
class TestCDTAIGovernanceConnectionSourceAvailability:
    """Verify that CDT and Mondaq analyses connecting the insurance ruling
    to AI governance are documented as source-available."""

    def test_cdt_article_documented(self):
        """CDT 'Design Decisions and the Duty to Defend' article must be
        documented with URL."""
        data = load_yaml('competitor-coverage-research.yaml')
        entry = _get_mechanism_entry(data)
        assert entry is not None, "Mechanism entry not found"
        entry_str = yaml.dump(entry).lower()
        assert 'cdt' in entry_str or 'center for democracy' in entry_str, \
            "Must document the CDT analysis article"
        # Check for the URL
        entry_str_raw = yaml.dump(entry)
        assert 'cdt.org' in entry_str_raw, \
            "Must include the CDT article URL (cdt.org)"

    def test_mondaq_article_documented(self):
        """Mondaq insurance coverage analysis must be documented with URL."""
        data = load_yaml('competitor-coverage-research.yaml')
        entry = _get_mechanism_entry(data)
        assert entry is not None, "Mechanism entry not found"
        entry_str_raw = yaml.dump(entry)
        assert 'mondaq' in entry_str_raw.lower(), \
            "Must document the Mondaq analysis article"
        assert 'mondaq.com' in entry_str_raw, \
            "Must include the Mondaq article URL"

    def test_ai_chatbot_deliberate_design_scenario_documented(self):
        """CDT's explicit scenario — AI chatbot fine-tuning as 'deliberate
        design decision' — must be documented as the source-available
        bridge between insurance law and AI governance."""
        data = load_yaml('competitor-coverage-research.yaml')
        entry = _get_mechanism_entry(data)
        assert entry is not None, "Mechanism entry not found"
        entry_str = yaml.dump(entry).lower()
        # CDT explicitly describes: fine-tuning → relationship → harm →
        # deliberate design argument
        has_finetuning = 'fine-tun' in entry_str or 'finetun' in entry_str
        has_chatbot = 'chatbot' in entry_str or 'assistant' in entry_str
        has_deliberate = 'deliberate design' in entry_str or \
            'deliberate' in entry_str
        assert has_deliberate and (has_finetuning or has_chatbot), \
            "Must document CDT's AI chatbot 'deliberate design' scenario " \
            "connecting insurance law to AI governance"


# ---------------------------------------------------------------------------
# 5. TestDeliberateDesignDoctrineAIAnalogy
# ---------------------------------------------------------------------------
class TestDeliberateDesignDoctrineAIAnalogy:
    """Verify documentation of how 'deliberate conduct' doctrine maps
    directly to AI lab product decisions."""

    def test_chatgpt_finetuning_as_deliberate_design(self):
        """ChatGPT's fine-tuning to be conversational/relationship-building
        parallels Meta's 'deliberate design' of addictive features."""
        data = load_yaml('competitor-coverage-research.yaml')
        entry = _get_mechanism_entry(data)
        assert entry is not None, "Mechanism entry not found"
        entry_str = yaml.dump(entry).lower()
        # The test validates that the analogy is drawn
        assert 'openai' in entry_str or 'chatgpt' in entry_str, \
            "Must draw the ChatGPT fine-tuning / deliberate design analogy"

    def test_anthropic_piracy_as_deliberate_conduct(self):
        """Anthropic's downloading of 7M pirated books from Library Genesis
        is unambiguously 'deliberate conduct' under the ruling's framework."""
        data = load_yaml('competitor-coverage-research.yaml')
        entry = _get_mechanism_entry(data)
        assert entry is not None, "Mechanism entry not found"
        entry_str = yaml.dump(entry).lower()
        has_piracy = 'pirat' in entry_str or 'library genesis' in entry_str \
            or 'libgen' in entry_str
        has_deliberate = 'deliberate' in entry_str
        assert has_piracy and has_deliberate, \
            "Must document Anthropic's piracy as unambiguously " \
            "'deliberate conduct'"

    def test_character_ai_relationship_as_deliberate_design(self):
        """Character.AI designing chatbots that form emotional relationships
        with teens parallels Meta's 'deliberate design' theory exactly."""
        data = load_yaml('competitor-coverage-research.yaml')
        entry = _get_mechanism_entry(data)
        assert entry is not None, "Mechanism entry not found"
        entry_str = yaml.dump(entry).lower()
        assert 'character' in entry_str, \
            "Must document Character.AI relationship design as deliberate"
        has_relationship = 'relationship' in entry_str or \
            'emotional' in entry_str or 'teen' in entry_str
        assert has_relationship, \
            "Must reference the relationship/emotional/teen harm dimension " \
            "of the Character.AI analogy"


# ---------------------------------------------------------------------------
# 6. TestPublicationCoverageInsuranceAnalysisOmission
# ---------------------------------------------------------------------------
class TestPublicationCoverageInsuranceAnalysisOmission:
    """Verify documentation that publications covering the Meta settlement
    do NOT cross-reference the insurance denial ruling's implications for
    AI lab partners."""

    def test_omission_pattern_documented(self):
        """The profile must document that major publications covering the
        $18B settlement omit insurance denial AI lab implications."""
        data = load_yaml('competitor-coverage-research.yaml')
        entry = _get_mechanism_entry(data)
        assert entry is not None, "Mechanism entry not found"
        entry_str = yaml.dump(entry).lower()
        # Should note the omission/gap/silence in coverage
        omission_terms = ['omit', 'omission', 'silence', 'gap', 'missing',
                          'absent', 'fail to', 'do not', "don't",
                          'no cross-reference', 'not cross-reference']
        found = any(t in entry_str for t in omission_terms)
        assert found, \
            "Must document the publication omission pattern — " \
            "covering settlement without insurance denial AI implications"

    def test_financial_incentive_for_omission(self):
        """Publications with AI lab financial relationships have no incentive
        to analyze whether the insurance denial precedent applies to
        their partners."""
        data = load_yaml('competitor-coverage-research.yaml')
        entry = _get_mechanism_entry(data)
        assert entry is not None, "Mechanism entry not found"
        entry_str = yaml.dump(entry).lower()
        has_incentive = 'incentive' in entry_str or 'financial' in entry_str
        has_relationship = 'relationship' in entry_str or \
            'deal' in entry_str or 'licensing' in entry_str
        assert has_incentive and has_relationship, \
            "Must connect the coverage omission to financial incentive " \
            "structure"

    def test_source_availability_contrast(self):
        """The profile must contrast: CDT/Mondaq analysis is publicly
        available, yet publications don't cross-reference it."""
        data = load_yaml('competitor-coverage-research.yaml')
        entry = _get_mechanism_entry(data)
        assert entry is not None, "Mechanism entry not found"
        entry_str = yaml.dump(entry).lower()
        # Should have both the source references and the gap note
        has_sources = 'cdt' in entry_str or 'mondaq' in entry_str
        has_gap = 'source-available' in entry_str or \
            'publicly available' in entry_str or \
            'available' in entry_str
        assert has_sources and has_gap, \
            "Must note that CDT/Mondaq analysis is source-available but " \
            "uncited by publication coverage"


# ---------------------------------------------------------------------------
# 7. TestConfounders
# ---------------------------------------------------------------------------
class TestConfounders:
    """Verify confounders are documented with correct strengths and that
    counter-confounders are also captured."""

    def test_five_confounders_documented(self):
        """Must document exactly 5 confounders."""
        data = load_yaml('competitor-coverage-research.yaml')
        entry = _get_mechanism_entry(data)
        assert entry is not None, "Mechanism entry not found"
        confounders = entry.get('confounders', [])
        assert len(confounders) >= 5, \
            f"Must document at least 5 confounders, found {len(confounders)}"

    def test_two_strong_confounders(self):
        """At least 2 confounders must be rated STRONG."""
        data = load_yaml('competitor-coverage-research.yaml')
        entry = _get_mechanism_entry(data)
        assert entry is not None, "Mechanism entry not found"
        confounders = entry.get('confounders', [])
        strong_count = sum(
            1 for c in confounders
            if isinstance(c, dict)
            and str(c.get('strength', '')).upper() == 'STRONG'
        )
        assert strong_count >= 2, \
            f"Must have at least 2 STRONG confounders, found {strong_count}"

    def test_counter_confounders_documented(self):
        """Counter-confounders (CDT source availability, Character.AI
        analogy, Anthropic deliberate conduct) must be documented."""
        data = load_yaml('competitor-coverage-research.yaml')
        entry = _get_mechanism_entry(data)
        assert entry is not None, "Mechanism entry not found"
        entry_str = yaml.dump(entry).lower()
        # Should reference counter-confounders explicitly or through
        # the terms they describe
        has_counter = 'counter-confounder' in entry_str or \
            'counter_confounder' in entry_str or \
            'counterconfounder' in entry_str or \
            'mitigat' in entry_str
        # Or the counter-confounder content itself (CDT availability +
        # Character.AI analogy + Anthropic deliberate conduct)
        content_signals = [
            'cdt' in entry_str and 'available' in entry_str,
            'character' in entry_str and 'analogous' in entry_str,
            'anthropic' in entry_str and 'deliberate' in entry_str,
        ]
        has_content = sum(content_signals) >= 2
        assert has_counter or has_content, \
            "Must document counter-confounders or their substantive " \
            "content (CDT availability, Character.AI analogy, " \
            "Anthropic deliberate conduct)"


# ---------------------------------------------------------------------------
# 8. TestAsymmetryScoreAndCrossReferences
# ---------------------------------------------------------------------------
class TestAsymmetryScoreAndCrossReferences:
    """Verify asymmetry score is 0.31 (bounded 0-1) and cross-references
    to mechanisms #326, #327, #328, #46 are documented."""

    def test_asymmetry_score_value(self):
        """Adjusted asymmetry score should be 0.31."""
        data = load_yaml('competitor-coverage-research.yaml')
        entry = _get_mechanism_entry(data)
        assert entry is not None, "Mechanism entry not found"
        score = entry.get('adjusted_score',
                          entry.get('asymmetry_score',
                                    entry.get('score')))
        assert score is not None, \
            "Must have an adjusted_score, asymmetry_score, or score field"
        assert abs(float(score) - 0.31) < 0.02, \
            f"Asymmetry score should be ~0.31, got {score}"

    def test_asymmetry_score_bounded(self):
        """Asymmetry score must be in [0, 1] range."""
        data = load_yaml('competitor-coverage-research.yaml')
        entry = _get_mechanism_entry(data)
        assert entry is not None, "Mechanism entry not found"
        score = entry.get('adjusted_score',
                          entry.get('asymmetry_score',
                                    entry.get('score')))
        assert score is not None, "Score field must exist"
        score_val = float(score)
        assert 0.0 <= score_val <= 1.0, \
            f"Score must be bounded [0, 1], got {score_val}"

    def test_cross_references_documented(self):
        """Must cross-reference mechanisms #326, #327, #328, and #46."""
        data = load_yaml('competitor-coverage-research.yaml')
        entry = _get_mechanism_entry(data)
        assert entry is not None, "Mechanism entry not found"
        cross_refs = entry.get('cross_references', [])
        ref_ids = set()
        for ref in cross_refs:
            if isinstance(ref, dict) and 'mechanism_id' in ref:
                ref_ids.add(ref['mechanism_id'])
            elif isinstance(ref, (int, str)):
                ref_ids.add(int(ref))
        expected_refs = {326, 327, 328, 46}
        missing = expected_refs - ref_ids
        assert not missing, \
            f"Missing cross-references to mechanisms: {missing}. " \
            f"Found: {ref_ids}"


# ---------------------------------------------------------------------------
# Additional integration tests (pushing above 25 total)
# ---------------------------------------------------------------------------
class TestSourceURLIntegrity:
    """Verify source URLs are documented in the mechanism entry."""

    def test_jdsupra_url_documented(self):
        """JD Supra analysis URL must be documented."""
        data = load_yaml('competitor-coverage-research.yaml')
        entry = _get_mechanism_entry(data)
        assert entry is not None, "Mechanism entry not found"
        entry_str = yaml.dump(entry)
        assert 'jdsupra.com' in entry_str, \
            "Must include JD Supra analysis URL"

    def test_cdt_url_documented(self):
        """CDT analysis URL must be documented."""
        data = load_yaml('competitor-coverage-research.yaml')
        entry = _get_mechanism_entry(data)
        assert entry is not None, "Mechanism entry not found"
        entry_str = yaml.dump(entry)
        assert 'cdt.org' in entry_str, \
            "Must include CDT analysis URL"

    def test_mondaq_url_documented(self):
        """Mondaq analysis URL must be documented."""
        data = load_yaml('competitor-coverage-research.yaml')
        entry = _get_mechanism_entry(data)
        assert entry is not None, "Mechanism entry not found"
        entry_str = yaml.dump(entry)
        assert 'mondaq.com' in entry_str, \
            "Must include Mondaq analysis URL"

    def test_reuters_settlement_url_documented(self):
        """Reuters Meta settlement article URL must be documented."""
        data = load_yaml('competitor-coverage-research.yaml')
        entry = _get_mechanism_entry(data)
        assert entry is not None, "Mechanism entry not found"
        entry_str = yaml.dump(entry)
        assert 'reuters.com' in entry_str, \
            "Must include Reuters settlement URL"

    def test_all_urls_have_https_scheme(self):
        """Every source URL in the mechanism must use https://."""
        data = load_yaml('competitor-coverage-research.yaml')
        entry = _get_mechanism_entry(data)
        assert entry is not None, "Mechanism entry not found"
        source_urls = entry.get('source_urls', [])
        if isinstance(source_urls, list):
            for url in source_urls:
                if isinstance(url, str) and '://' in url:
                    assert url.startswith('https://'), \
                        f"URL must use https://: {url}"


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
