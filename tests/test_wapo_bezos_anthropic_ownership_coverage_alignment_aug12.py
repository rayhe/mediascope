"""
Mechanism #65: WaPo Bezos Ownership Chain — Amazon → Anthropic Pre-IPO Coverage Alignment

Type A: Competitor Coverage Deep Dive
Publication: The Washington Post
Competitor: Anthropic (vs Meta)
Date: 2026-08-12

FINDING: The Washington Post has the STRONGEST ownership-conflict chain in
the MediaScope dataset for Anthropic coverage. Jeff Bezos owns WaPo outright
($250M purchase, 2013). Bezos founded Amazon and remains executive chairman
and largest shareholder. Amazon has invested $13B+ in Anthropic — its largest
external investment in history — and holds 15-20% equity (worth ~$150-200B
at Anthropic's ~$965B secondary valuation). Anthropic filed a confidential
S-1 in June 2026 for an IPO targeting ~$1T valuation.

This is DIRECT OWNERSHIP — not a content licensing deal (like FT-OpenAI or
WIRED-OpenAI via Condé Nast), not advertising revenue dependency (like
Google-Guardian), and not a multi-hop endowment chain (like MIT-Anthropic
via Google/Amazon stock). The proprietor of the publication has a direct,
material financial interest in Anthropic's success and public perception.

At IPO, Amazon's Anthropic stake could be worth 150-200x the purchase price
of the Washington Post itself. This creates an unprecedented asymmetry where
the financial significance of Anthropic's success to WaPo's owner dwarfs
the financial value of the publication.

Coverage evidence (2026):
  - WaPo (Gerrit De Vynck, Jun 2026): AI political bias study positions
    Claude as the MOST balanced chatbot (57% both-sides answers) while
    ChatGPT is "skewed" (80% left-leaning). Claude gets complimentary framing.
  - WaPo headline (Mar 2026): "Anthropic lost the Pentagon but won over
    America" — heroic defiance framing for Anthropic's refusal to remove
    AI safety guardrails for military use.
  - WaPo (Apr 2026): Anthropic meeting with Christian leaders for Claude's
    morality — neutral-curious, respectful framing of moral seriousness.
  - WaPo (Jul 2026, De Vynck): OpenAI-Anthropic AI slowdown petition —
    both framed as responsible leaders calling for government coordination.
  - WaPo (Aug 2025): Smart glasses Gen Z backlash — "a stream of critical
    videos" about Meta glasses, amplifying opposition.
  - WaPo (Jun 2026): Claude persuasion study — Claude outperforming human
    fundraisers framed as scientifically interesting, not alarming.

Meta coverage: WaPo covers Meta through adversarial/privacy-alarm lens
(Gen Z backlash, glasses surveillance, Meta spokesperson declining
"broader questions about privacy risks"). Meta pays publishers $0.

CONFOUNDING FACTORS:
1. WaPo has editorial independence policies; Bezos has stated he doesn't
   interfere with editorial decisions — MODERATE (but ownership IS the
   conflict; editorial independence policies don't eliminate structural
   incentives)
2. Anthropic's Pentagon stance genuinely was newsworthy and heroic to
   many — STRONG
3. WaPo covers all major tech companies across a range of tones — MODERATE
4. Amazon's Anthropic investment is managed by separate teams from WaPo
   operations — WEAK (ownership, not operational control, is the conflict)
5. Other publications without Bezos ownership also frame Anthropic
   positively (MIT TR, FT) — MODERATE (reduces WaPo-specific attribution)
6. WaPo has published critical coverage of Amazon itself (labor, antitrust)
   — STRONG (genuine editorial independence on direct-employer coverage)
7. WaPo political bias study applied identical methodology to all chatbots
   — the Claude ranking reflects actual performance, not editorial choice
   — STRONG

TESTABLE PREDICTIONS:
1. WaPo coverage of Anthropic's IPO filing/pricing will use aspirational/
   validating framing (vs neutral/skeptical for other AI IPOs)
2. WaPo will underreport Anthropic's Fable 5 sabotage incident relative
   to Meta's equivalent AI rogue agent incidents
3. WaPo will frame Amazon-Anthropic partnership deals as innovation
   stories, not as conflict-of-interest for WaPo's own coverage
4. WaPo AI beat reporter (De Vynck) will receive greater Anthropic access
   (interviews, exclusives) than Meta access

CROSS-REFERENCES:
- Mechanism #22: NYT-Anthropic Triple-Chain (similar multi-hop incentive;
  WaPo is DIRECT ownership vs NYT's indirect chains)
- Mechanism #54: FT Capital-Raise Framing Asymmetry (comparable capital/
  valuation framing context, but FT's deal is licensing, not ownership)
- Mechanism #15: MIT TR Pre-IPO Product Validation (same pre-IPO window
  dynamic, but MIT's chain goes through endowment, not direct ownership)

Sources:
- WaPo AI political bias study: referenced by Fox News, NY Post, attributed
  to Washington Post / Gerrit De Vynck (Jun 2026)
  https://foxnews.com/media/most-prominent-ai-chatbots-have-liberal-bias-new-study-finds
- Anthropic vs government timeline (eWeek):
  https://www.eweek.com/news/anthropic-washington-timeline-2026/
- Amazon Anthropic investment timeline: Reuters, multiple sources ($13B+
  total including $11B Project Rainier, Dec 2025)
- WaPo Gen Z smart glasses backlash: referenced by Slashdot, TechSpot
  https://yro.slashdot.org/story/25/08/30/0618242
- Anthropic confidential S-1 filing (Jun 2026): TechCrunch
  https://techcrunch.com/2026/06/08/following-anthropic-openai-files-confidentially-for-ipo/
- WaPo ownership: Jeff Bezos purchased 2013 for $250M (common knowledge)
- Amazon Anthropic stake value: secondary market ~$965B valuation (Reuters,
  Jun 2026); 15-20% Amazon stake
- Claude persuasion study (WaPo, Jun 2026): referenced by Daily Guardian
  https://dailyguardian.ae/claude-ai-is-better-at-raising-funds-for-humans-than-humans-finds-worrying-experiment/
"""

import pytest
import yaml
import os
import glob

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


# ─────────────────────────────────────────────────────────────────────
#  Helpers
# ─────────────────────────────────────────────────────────────────────

def load_yaml(filename):
    path = os.path.join(PROFILES_DIR, filename)
    with open(path) as f:
        return yaml.safe_load(f)


def get_mechanism_65(data):
    """Find mechanism #65 in cross_publication_findings."""
    findings = data.get('cross_publication_findings', {})
    if isinstance(findings, dict):
        for key, val in findings.items():
            if isinstance(val, dict) and val.get('mechanism_id') == 65:
                return val
    elif isinstance(findings, list):
        for item in findings:
            if isinstance(item, dict) and item.get('mechanism_id') == 65:
                return item
    return None


# ─────────────────────────────────────────────────────────────────────
#  Test Classes
# ─────────────────────────────────────────────────────────────────────

class TestMechanismDocumentation:
    """Verify mechanism #65 is properly documented."""

    @pytest.fixture(autouse=True)
    def load_data(self):
        self.research = load_yaml('competitor-coverage-research.yaml')
        self.entities = load_yaml('competitor-entities.yaml')

    def test_mechanism_65_exists(self):
        m = get_mechanism_65(self.research)
        assert m is not None, "Mechanism #65 not found in competitor-coverage-research.yaml"

    def test_mechanism_has_name(self):
        m = get_mechanism_65(self.research)
        assert m is not None
        name = m.get('name', m.get('mechanism_name', ''))
        assert 'bezos' in name.lower() or 'wapo' in name.lower() or 'washington' in name.lower(), \
            f"Mechanism name should reference Bezos/WaPo: {name}"

    def test_mechanism_has_publication(self):
        m = get_mechanism_65(self.research)
        assert m is not None
        pub = str(m.get('publication', '')).lower()
        assert 'washington' in pub or 'wapo' in pub, \
            f"Publication should be Washington Post: {m.get('publication')}"

    def test_mechanism_has_source_urls(self):
        m = get_mechanism_65(self.research)
        assert m is not None
        urls = m.get('source_urls', [])
        assert len(urls) >= 3, f"Expected at least 3 source URLs, got {len(urls)}"

    def test_mechanism_has_confounding_factors(self):
        m = get_mechanism_65(self.research)
        assert m is not None
        factors = m.get('confounding_factors', [])
        assert len(factors) >= 4, f"Expected at least 4 confounding factors, got {len(factors)}"

    def test_mechanism_has_cross_references(self):
        m = get_mechanism_65(self.research)
        assert m is not None
        xrefs = m.get('cross_references', [])
        assert len(xrefs) >= 2, f"Expected at least 2 cross-references, got {len(xrefs)}"


class TestOwnershipChain:
    """Verify the Bezos → Amazon → Anthropic ownership chain is documented."""

    @pytest.fixture(autouse=True)
    def load_data(self):
        self.research = load_yaml('competitor-coverage-research.yaml')
        self.entities = load_yaml('competitor-entities.yaml')

    def test_ownership_chain_bezos_wapo(self):
        m = get_mechanism_65(self.research)
        assert m is not None
        chain = str(m.get('ownership_chain', m.get('finding_summary', '')))
        assert 'bezos' in chain.lower(), "Ownership chain must mention Bezos"

    def test_ownership_chain_amazon(self):
        m = get_mechanism_65(self.research)
        assert m is not None
        chain = str(m.get('ownership_chain', m.get('finding_summary', '')))
        assert 'amazon' in chain.lower(), "Ownership chain must mention Amazon"

    def test_ownership_chain_anthropic_investment(self):
        m = get_mechanism_65(self.research)
        assert m is not None
        chain = str(m.get('ownership_chain', m.get('finding_summary', '')))
        assert 'anthropic' in chain.lower(), "Ownership chain must mention Anthropic"

    def test_ownership_is_direct_not_licensing(self):
        m = get_mechanism_65(self.research)
        assert m is not None
        text = str(m.get('finding_summary', m.get('overview', '')))
        # Should distinguish from licensing deals
        assert 'ownership' in text.lower() or 'owns' in text.lower() or 'direct' in text.lower(), \
            "Finding should emphasize DIRECT ownership (vs content licensing deals)"

    def test_amazon_investment_amount_documented(self):
        m = get_mechanism_65(self.research)
        assert m is not None
        text = str(m)
        assert '13' in text or '19' in text, \
            "Amazon's $13B+ or $19B total investment should be documented"

    def test_anthropic_stake_percentage_documented(self):
        m = get_mechanism_65(self.research)
        assert m is not None
        text = str(m)
        assert '15' in text or '20' in text, \
            "Amazon's 15-20% Anthropic stake should be documented"


class TestCoverageFramingAnalysis:
    """Verify coverage framing evidence is documented."""

    @pytest.fixture(autouse=True)
    def load_data(self):
        self.research = load_yaml('competitor-coverage-research.yaml')

    def test_anthropic_coverage_examples_exist(self):
        m = get_mechanism_65(self.research)
        assert m is not None
        text = str(m)
        assert 'claude' in text.lower() or 'anthropic' in text.lower(), \
            "Must include Anthropic/Claude coverage examples"

    def test_meta_coverage_examples_exist(self):
        m = get_mechanism_65(self.research)
        assert m is not None
        text = str(m)
        assert 'meta' in text.lower() or 'glasses' in text.lower(), \
            "Must include Meta coverage examples for comparison"

    def test_political_bias_study_mentioned(self):
        m = get_mechanism_65(self.research)
        assert m is not None
        text = str(m)
        assert 'bias' in text.lower() or 'balanced' in text.lower() or 'political' in text.lower(), \
            "Should reference the AI political bias study"

    def test_pentagon_coverage_mentioned(self):
        m = get_mechanism_65(self.research)
        assert m is not None
        text = str(m)
        assert 'pentagon' in text.lower() or 'military' in text.lower(), \
            "Should reference Pentagon/military coverage"


class TestCrossEntityComparison:
    """Verify the mechanism includes cross-entity comparison."""

    @pytest.fixture(autouse=True)
    def load_data(self):
        self.research = load_yaml('competitor-coverage-research.yaml')
        self.entities = load_yaml('competitor-entities.yaml')

    def test_meta_zero_financial_relationship(self):
        m = get_mechanism_65(self.research)
        assert m is not None
        text = str(m)
        # Meta pays publishers $0
        assert 'zero' in text.lower() or '$0' in text or 'no financial' in text.lower() or \
               'no deal' in text.lower() or 'no relationship' in text.lower(), \
            "Should document Meta's zero financial relationship with WaPo"

    def test_comparison_with_other_publication_mechanisms(self):
        m = get_mechanism_65(self.research)
        assert m is not None
        xrefs = m.get('cross_references', [])
        # Should reference at least one of: #22 (NYT), #54 (FT), #15 (MIT TR)
        xref_ids = set()
        for xref in xrefs:
            if isinstance(xref, dict):
                xref_ids.add(xref.get('mechanism_id'))
            elif isinstance(xref, (int, str)):
                try:
                    xref_ids.add(int(xref))
                except (ValueError, TypeError):
                    pass
        assert xref_ids & {15, 22, 54}, \
            f"Should cross-reference mechanisms #15, #22, or #54; got: {xref_ids}"


class TestConfoundingFactors:
    """Verify confounding factors are thorough and honest."""

    @pytest.fixture(autouse=True)
    def load_data(self):
        self.research = load_yaml('competitor-coverage-research.yaml')

    def test_editorial_independence_confound(self):
        m = get_mechanism_65(self.research)
        assert m is not None
        factors = m.get('confounding_factors', [])
        text = ' '.join(str(f) for f in factors).lower()
        assert 'editorial independence' in text or 'independent' in text or \
               'interfere' in text or 'autonomy' in text, \
            "Must acknowledge editorial independence as a confounding factor"

    def test_pentagon_newsworthiness_confound(self):
        m = get_mechanism_65(self.research)
        assert m is not None
        factors = m.get('confounding_factors', [])
        text = ' '.join(str(f) for f in factors).lower()
        assert 'newsworthy' in text or 'genuine' in text or 'legitimate' in text, \
            "Must acknowledge genuine newsworthiness of Anthropic's Pentagon stance"

    def test_amazon_critical_coverage_confound(self):
        m = get_mechanism_65(self.research)
        assert m is not None
        factors = m.get('confounding_factors', [])
        text = ' '.join(str(f) for f in factors).lower()
        assert 'amazon' in text or 'critical' in text or 'labor' in text, \
            "Must acknowledge WaPo's critical coverage of Amazon itself"

    def test_at_least_one_strong_confound(self):
        m = get_mechanism_65(self.research)
        assert m is not None
        factors = m.get('confounding_factors', [])
        text = ' '.join(str(f) for f in factors).lower()
        assert 'strong' in text, \
            "At least one confounding factor should be rated STRONG"


class TestTestablePredictions:
    """Verify testable predictions exist."""

    @pytest.fixture(autouse=True)
    def load_data(self):
        self.research = load_yaml('competitor-coverage-research.yaml')

    def test_predictions_exist(self):
        m = get_mechanism_65(self.research)
        assert m is not None
        preds = m.get('testable_predictions', [])
        assert len(preds) >= 2, f"Expected at least 2 testable predictions, got {len(preds)}"

    def test_ipo_prediction_exists(self):
        m = get_mechanism_65(self.research)
        assert m is not None
        preds = m.get('testable_predictions', [])
        text = ' '.join(str(p) for p in preds).lower()
        assert 'ipo' in text, "Should include a prediction about IPO coverage framing"


class TestPreIPOWindow:
    """Verify the pre-IPO timing context is documented."""

    @pytest.fixture(autouse=True)
    def load_data(self):
        self.research = load_yaml('competitor-coverage-research.yaml')

    def test_ipo_filing_date_documented(self):
        m = get_mechanism_65(self.research)
        assert m is not None
        text = str(m)
        assert 's-1' in text.lower() or 'ipo' in text.lower() or 'filing' in text.lower(), \
            "Should document Anthropic's S-1/IPO filing"

    def test_valuation_context_documented(self):
        m = get_mechanism_65(self.research)
        assert m is not None
        text = str(m)
        assert '965' in text or '1t' in text.lower() or 'trillion' in text.lower() or \
               '900' in text or '850' in text, \
            "Should document Anthropic's approximate valuation"


class TestEntityIntegration:
    """Verify the finding is integrated into competitor-entities.yaml."""

    @pytest.fixture(autouse=True)
    def load_data(self):
        self.entities = load_yaml('competitor-entities.yaml')

    def test_anthropic_entity_has_wapo_section(self):
        entities = self.entities.get('entities', {})
        anthropic = entities.get('anthropic', {})
        text = str(anthropic).lower()
        # Check for any reference to WaPo/Bezos/Washington Post
        assert 'wapo' in text or 'washington post' in text or 'bezos' in text, \
            "anthropic entity should reference WaPo/Bezos ownership chain"


class TestMechanismSequenceIntegrity:
    """Verify mechanism #65 fits in the sequence."""

    @pytest.fixture(autouse=True)
    def load_data(self):
        self.research = load_yaml('competitor-coverage-research.yaml')

    def test_mechanism_id_is_65(self):
        m = get_mechanism_65(self.research)
        assert m is not None, "Mechanism #65 must exist"
        assert m.get('mechanism_id') == 65

    def test_max_mechanism_id_at_least_65(self):
        findings = self.research.get('cross_publication_findings', {})
        max_id = 0
        if isinstance(findings, dict):
            for val in findings.values():
                if isinstance(val, dict) and isinstance(val.get('mechanism_id'), int):
                    max_id = max(max_id, val['mechanism_id'])
        assert max_id >= 65, f"Max mechanism ID should be >= 65, got {max_id}"
