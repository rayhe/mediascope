"""
Mechanism #73: CMA Regulatory Remedy Neutralization —
Google's Private No-Sue Contracts Undermining Public Regulatory Protections

FINDING (Aug 12, 2026): The UK CMA issued a "world-first" ruling on June 4, 2026
requiring Google to let publishers opt out of AI Overviews without losing search
visibility. But Google's simultaneous News AI pilot deals (200+ publications by
Aug 2026, per Press Gazette) include no-sue clauses and NDAs. Publishers who signed
these deals effectively waive their CMA-granted bargaining power through private
contract, creating a three-layer contradiction:

Layer 1: CMA gives opt-out rights → Google's deal offers money to NOT opt out
Layer 2: CMA requires transparency → Google's deals require secrecy (NDA)
Layer 3: CMA strengthens bargaining position → Google's no-sue clause prevents using it

MEDIASCOPE SIGNIFICANCE: The Guardian and FT — both in the MediaScope dataset — have
signed Google's News AI deals (Press Gazette confirmed "single figure millions/yr"
each, Aug 3 2026). Both are members of publisher coalitions that TRIGGERED the CMA
ruling. Their editorial coverage of the CMA ruling should be assessed for whether
they disclosed their own Google AI deal and whether they can investigate Google's
deal compliance given their NDA/no-sue constraints. This creates a structural
editorial conflict unique to publications with Google AI deals.

KEY CONTRAST: Meta has ZERO coercive mechanisms over publishers. Meta's 13 AI content
deals (Dec 2025, Mar 2026) are voluntary, bilateral, with no NDA on deal existence,
no no-sue clauses, and no threat of losing existing payments if declined. Yet
publications bound by Google's coercive deal structure produce MORE adversarial coverage
of Meta than of Google. The CMA remedy was intended to strengthen publishers' hands
against Google — but the publishers most active in securing the remedy (Guardian, FT)
have already signed deals that neutralize it.

SOURCES:
- CMA ruling: https://www.barchart.com/story/news/2276635/uk-orders-google-to-allow-publishers-to-opt-out-of-ai-scraping-for-search-summaries
- Press Gazette (Aug 3, 2026): https://pressgazette.co.uk/news/google-ai-deals-uk-publishers/
- Computer Weekly (Jun 4, 2026): https://www.computerweekly.com/news/366643963/Publishers-can-now-opt-out-of-Google-AI-summaries-and-training
- Open Society Foundations (Jul 29, 2026): https://www.opensocietyfoundations.org/voices/google-ai-overviews-foxglove-uk-ruling
- PYMNTS (Jun 25, 2026): https://www.pymnts.com/news/artificial-intelligence/2026/google-tells-news-publishers-to-share-content-for-ai-training-or-lose-fees/
- Digiday (CMA opt-out analysis): http://digiday.com/media/googles-forced-ai-opt-out-what-changes-and-what-doesnt-for-publishers/
- Press Gazette AI Summit (Jun 30, 2026): https://pressgazette.co.uk/press-gazette-events/travesty-if-publishers-dont-take-up-chance-to-opt-out-of-google-ai-overviews/
"""

import pytest
import yaml
import os
import glob

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(filename):
    path = os.path.join(PROFILES_DIR, filename)
    with open(path, 'r') as f:
        return yaml.safe_load(f)


# ──────────────────────────────────────────────────────────────────
# 1. CMA Ruling and Google Deal Structure Contradictions
# ──────────────────────────────────────────────────────────────────

class TestCMARulingStructure:
    """Verify the CMA ruling's structural requirements are documented."""

    def test_cma_ruling_date(self):
        """CMA ruling issued June 4, 2026 — world-first digital market conduct requirement."""
        entities = load_yaml('competitor-entities.yaml')
        google = entities['entities']['google']
        cma = google.get('cma_regulatory_neutralization', {})
        assert cma.get('cma_ruling_date') == '2026-06-04', \
            "CMA ruling date should be June 4, 2026"

    def test_cma_opt_out_requirement(self):
        """CMA requires Google to let publishers opt out of AI features WITHOUT losing search visibility."""
        entities = load_yaml('competitor-entities.yaml')
        google = entities['entities']['google']
        cma = google.get('cma_regulatory_neutralization', {})
        assert cma.get('opt_out_without_search_penalty') is True, \
            "CMA ruling requires opt-out without search visibility penalty"

    def test_cma_implementation_deadline(self):
        """Google has 9 months from June 4, 2026 to implement — approximately March 2027."""
        entities = load_yaml('competitor-entities.yaml')
        google = entities['entities']['google']
        cma = google.get('cma_regulatory_neutralization', {})
        assert cma.get('implementation_months') == 9, \
            "Google has 9-month implementation deadline"

    def test_cma_compliance_reporting(self):
        """Google must submit compliance reports every 6 months for at least 1 year."""
        entities = load_yaml('competitor-entities.yaml')
        google = entities['entities']['google']
        cma = google.get('cma_regulatory_neutralization', {})
        assert cma.get('compliance_report_interval_months') == 6, \
            "Compliance reports required every 6 months"

    def test_cma_triggered_by_foxglove(self):
        """The CMA complaint was triggered by Foxglove, an Open Society Foundations grantee."""
        entities = load_yaml('competitor-entities.yaml')
        google = entities['entities']['google']
        cma = google.get('cma_regulatory_neutralization', {})
        assert 'Foxglove' in str(cma.get('complaint_filer', '')), \
            "CMA complaint filed by Foxglove"


class TestGoogleDealNoSueClauses:
    """Verify Google's News AI deals include no-sue clauses and NDAs."""

    def test_news_ai_pilot_global_count(self):
        """200+ publications signed Google News AI pilot globally (Press Gazette Aug 2026)."""
        entities = load_yaml('competitor-entities.yaml')
        google = entities['entities']['google']
        cma = google.get('cma_regulatory_neutralization', {})
        pilot_count = cma.get('news_ai_pilot_publications_global', 0)
        assert pilot_count >= 200, \
            f"Expected 200+ News AI pilot publications, got {pilot_count}"

    def test_deals_include_nosue_clauses(self):
        """Google News AI deals include no-sue clauses (Press Gazette confirmed)."""
        entities = load_yaml('competitor-entities.yaml')
        google = entities['entities']['google']
        cma = google.get('cma_regulatory_neutralization', {})
        assert cma.get('deal_nosue_clauses') is True, \
            "Google News AI deals must include no-sue clauses"

    def test_deals_include_ndas(self):
        """Google News AI deals include NDAs preventing disclosure of terms."""
        entities = load_yaml('competitor-entities.yaml')
        google = entities['entities']['google']
        cma = google.get('cma_regulatory_neutralization', {})
        assert cma.get('deal_nda_clauses') is True, \
            "Google News AI deals must include NDA clauses"

    def test_deal_duration_years(self):
        """Google News AI deals run for 2 years with 90-day exit clause."""
        entities = load_yaml('competitor-entities.yaml')
        google = entities['entities']['google']
        cma = google.get('cma_regulatory_neutralization', {})
        assert cma.get('deal_duration_years') == 2, \
            "Google News AI deals run for 2 years"

    def test_deal_exit_clause_days(self):
        """Publishers can exit Google News AI deals with 90 days' notice."""
        entities = load_yaml('competitor-entities.yaml')
        google = entities['entities']['google']
        cma = google.get('cma_regulatory_neutralization', {})
        assert cma.get('deal_exit_notice_days') == 90, \
            "Google News AI deals have 90-day exit clause"

    def test_showcase_sunset_confirmed(self):
        """Google plans to end Showcase and replace with News AI pilot (PYMNTS Jun 25)."""
        entities = load_yaml('competitor-entities.yaml')
        google = entities['entities']['google']
        cma = google.get('cma_regulatory_neutralization', {})
        assert cma.get('showcase_sunset_confirmed') is True, \
            "Google Showcase sunset should be confirmed"


# ──────────────────────────────────────────────────────────────────
# 2. Three-Layer Regulatory Contradiction
# ──────────────────────────────────────────────────────────────────

class TestThreeLayerContradiction:
    """Verify the three structural contradictions between CMA ruling and Google deals."""

    def test_layer_1_opt_out_vs_payment(self):
        """Layer 1: CMA gives opt-out rights → Google offers money to NOT opt out."""
        entities = load_yaml('competitor-entities.yaml')
        google = entities['entities']['google']
        cma = google.get('cma_regulatory_neutralization', {})
        layers = cma.get('contradiction_layers', [])
        layer_names = [l.get('name', '') for l in layers]
        assert 'opt_out_vs_payment' in layer_names, \
            "Layer 1 (opt-out vs payment) must be documented"

    def test_layer_2_transparency_vs_nda(self):
        """Layer 2: CMA requires transparency → Google requires secrecy (NDA)."""
        entities = load_yaml('competitor-entities.yaml')
        google = entities['entities']['google']
        cma = google.get('cma_regulatory_neutralization', {})
        layers = cma.get('contradiction_layers', [])
        layer_names = [l.get('name', '') for l in layers]
        assert 'transparency_vs_nda' in layer_names, \
            "Layer 2 (transparency vs NDA) must be documented"

    def test_layer_3_bargaining_vs_nosue(self):
        """Layer 3: CMA strengthens bargaining → Google's no-sue prevents using it."""
        entities = load_yaml('competitor-entities.yaml')
        google = entities['entities']['google']
        cma = google.get('cma_regulatory_neutralization', {})
        layers = cma.get('contradiction_layers', [])
        layer_names = [l.get('name', '') for l in layers]
        assert 'bargaining_vs_nosue' in layer_names, \
            "Layer 3 (bargaining vs no-sue) must be documented"

    def test_press_gazette_neutralization_quote(self):
        """Press Gazette: 'Google's secret AI deals could make that ruling largely irrelevant.'"""
        entities = load_yaml('competitor-entities.yaml')
        google = entities['entities']['google']
        cma = google.get('cma_regulatory_neutralization', {})
        assert 'largely irrelevant' in str(cma.get('press_gazette_assessment', '')), \
            "Press Gazette neutralization assessment should be captured"


# ──────────────────────────────────────────────────────────────────
# 3. Guardian and FT Deal Quantification
# ──────────────────────────────────────────────────────────────────

class TestGuardianFTDealQuantification:
    """New financial quantification from Press Gazette (Aug 3, 2026)."""

    def test_guardian_deal_revenue_range(self):
        """Guardian earns 'single figure millions' per year from Google News AI deal."""
        guardian = load_yaml('guardian.yaml')
        google_deal = None
        for deal in guardian.get('revenue_relationships', []):
            if 'Google' in str(deal.get('partner', '')):
                if deal.get('annual_revenue_range'):
                    google_deal = deal
                    break
        assert google_deal is not None, "Guardian Google News AI deal with revenue range must exist"
        revenue = google_deal.get('annual_revenue_range', '')
        assert 'single figure millions' in revenue.lower() or \
            'million' in revenue.lower(), \
            f"Guardian Google deal revenue should reference millions, got: {revenue}"

    def test_ft_deal_revenue_range(self):
        """FT earns 'single figure millions' per year from Google News AI deal."""
        ft = load_yaml('financial-times.yaml')
        google = ft.get('competitor_relationships', {}).get('google', {})
        revenue = google.get('annual_revenue_range', '')
        assert 'single figure millions' in revenue.lower() or \
            'million' in revenue.lower(), \
            f"FT Google deal revenue should reference millions, got: {revenue}"

    def test_guardian_coalition_member_conflict(self):
        """Guardian is part of publisher coalition that triggered CMA ruling
        AND has signed Google's AI deal — structural conflict."""
        entities = load_yaml('competitor-entities.yaml')
        google = entities['entities']['google']
        cma = google.get('cma_regulatory_neutralization', {})
        pubs = cma.get('coalition_members_who_signed_deal', [])
        assert 'Guardian' in pubs or 'The Guardian' in pubs, \
            "Guardian must be listed as both coalition member and deal signer"

    def test_ft_coalition_member_conflict(self):
        """FT signed Google's AI deal AND benefits from CMA ruling — structural conflict."""
        entities = load_yaml('competitor-entities.yaml')
        google = entities['entities']['google']
        cma = google.get('cma_regulatory_neutralization', {})
        pubs = cma.get('coalition_members_who_signed_deal', [])
        assert 'FT' in pubs or 'Financial Times' in pubs, \
            "FT must be listed as both deal signer and CMA beneficiary"


# ──────────────────────────────────────────────────────────────────
# 4. Coverage Prediction: Does the CMA Deal Conflict Affect Coverage?
# ──────────────────────────────────────────────────────────────────

class TestCoveragePredictions:
    """Testable predictions for how the CMA-deal conflict affects editorial coverage."""

    def test_prediction_guardian_google_coverage_softening(self):
        """PREDICTION: Guardian's Google coverage is softer than its Meta coverage,
        despite Google causing more financial harm (traffic collapse, AI Overviews)."""
        entities = load_yaml('competitor-entities.yaml')
        google = entities['entities']['google']
        cma = google.get('cma_regulatory_neutralization', {})
        predictions = cma.get('testable_predictions', [])
        pred_texts = [p if isinstance(p, str) else p.get('prediction', '') for p in predictions]
        guardian_pred = any('Guardian' in p and 'Google' in p for p in pred_texts)
        assert guardian_pred, \
            "Must have testable prediction about Guardian-Google coverage"

    def test_prediction_ft_google_coverage_softening(self):
        """PREDICTION: FT's Google coverage is softer than its Meta coverage,
        consistent with Google deal + OpenAI deal + consulting revenue."""
        entities = load_yaml('competitor-entities.yaml')
        google = entities['entities']['google']
        cma = google.get('cma_regulatory_neutralization', {})
        predictions = cma.get('testable_predictions', [])
        pred_texts = [p if isinstance(p, str) else p.get('prediction', '') for p in predictions]
        ft_pred = any('FT' in p or 'Financial Times' in p for p in pred_texts)
        assert ft_pred, \
            "Must have testable prediction about FT-Google coverage"

    def test_prediction_cma_disclosure_gap(self):
        """PREDICTION: Neither Guardian nor FT will disclose their Google AI deal
        when covering CMA compliance — the NDA prevents transparency."""
        entities = load_yaml('competitor-entities.yaml')
        google = entities['entities']['google']
        cma = google.get('cma_regulatory_neutralization', {})
        predictions = cma.get('testable_predictions', [])
        pred_texts = [p if isinstance(p, str) else p.get('prediction', '') for p in predictions]
        disclosure_pred = any('disclose' in p.lower() or 'NDA' in p for p in pred_texts)
        assert disclosure_pred, \
            "Must have testable prediction about CMA coverage disclosure gap"

    def test_prediction_meta_contrast(self):
        """PREDICTION: Meta (zero coercive mechanisms) receives more adversarial coverage
        than Google (coercive no-sue deals) from deal-bound publications."""
        entities = load_yaml('competitor-entities.yaml')
        google = entities['entities']['google']
        cma = google.get('cma_regulatory_neutralization', {})
        predictions = cma.get('testable_predictions', [])
        pred_texts = [p if isinstance(p, str) else p.get('prediction', '') for p in predictions]
        meta_pred = any('Meta' in p and ('adversarial' in p.lower() or 'coercive' in p.lower()) for p in pred_texts)
        assert meta_pred, \
            "Must have testable prediction contrasting Meta vs Google coverage"


# ──────────────────────────────────────────────────────────────────
# 5. Meta Deal Structure Contrast
# ──────────────────────────────────────────────────────────────────

class TestMetaDealContrastWithGoogle:
    """Verify Meta's voluntary deal structure is documented as contrast."""

    def test_meta_zero_nosue_clauses(self):
        """Meta's AI content deals have NO no-sue clauses."""
        entities = load_yaml('competitor-entities.yaml')
        google = entities['entities']['google']
        cma = google.get('cma_regulatory_neutralization', {})
        meta_contrast = cma.get('meta_contrast', {})
        assert meta_contrast.get('nosue_clauses') is False or \
            meta_contrast.get('nosue_clauses') == 0, \
            "Meta must have zero no-sue clauses"

    def test_meta_zero_coercive_mechanisms(self):
        """Meta has zero coercive mechanisms vs. Google's four."""
        entities = load_yaml('competitor-entities.yaml')
        google = entities['entities']['google']
        cma = google.get('cma_regulatory_neutralization', {})
        meta_contrast = cma.get('meta_contrast', {})
        assert meta_contrast.get('coercive_mechanisms') == 0, \
            "Meta must have zero coercive mechanisms"

    def test_google_coercive_mechanism_count(self):
        """Google has at least 4 coercive mechanisms over publishers."""
        entities = load_yaml('competitor-entities.yaml')
        google = entities['entities']['google']
        cma = google.get('cma_regulatory_neutralization', {})
        meta_contrast = cma.get('meta_contrast', {})
        assert meta_contrast.get('google_coercive_mechanisms', 0) >= 4, \
            "Google must have at least 4 coercive mechanisms documented"

    def test_meta_voluntary_deal_model(self):
        """Meta's deals are voluntary with no threat of losing existing payments."""
        entities = load_yaml('competitor-entities.yaml')
        google = entities['entities']['google']
        cma = google.get('cma_regulatory_neutralization', {})
        meta_contrast = cma.get('meta_contrast', {})
        assert meta_contrast.get('deal_model') == 'voluntary', \
            "Meta's deal model must be documented as voluntary"


# ──────────────────────────────────────────────────────────────────
# 6. Anthropic Zero-Deal Confirmation
# ──────────────────────────────────────────────────────────────────

class TestAnthropicZeroDealPressGazette:
    """Press Gazette (Aug 2026) explicitly confirmed Anthropic has zero publisher deals."""

    def test_anthropic_zero_deals_confirmed(self):
        """'Anthropic has not signed any licensing deals' — Press Gazette Aug 2026."""
        entities = load_yaml('competitor-entities.yaml')
        anthropic = entities['entities']['anthropic']
        note = anthropic.get('publisher_deals_note', '')
        assert 'ZERO' in note or 'zero' in note, \
            "Anthropic zero-deal status must be documented"

    def test_press_gazette_confirmation_source(self):
        """Press Gazette is the source for Anthropic zero-deal confirmation."""
        entities = load_yaml('competitor-entities.yaml')
        google = entities['entities']['google']
        cma = google.get('cma_regulatory_neutralization', {})
        source_urls = cma.get('source_urls', [])
        has_press_gazette = any('pressgazette' in url for url in source_urls)
        assert has_press_gazette, \
            "Press Gazette must be cited as source for deal quantification"


# ──────────────────────────────────────────────────────────────────
# 7. Cross-Reference with Existing Mechanisms
# ──────────────────────────────────────────────────────────────────

class TestMechanismCrossReferences:
    """Verify mechanism #73 cross-references related mechanisms."""

    def test_mechanism_73_exists(self):
        """Mechanism #73 exists in cross-publication findings."""
        research = load_yaml('competitor-coverage-research.yaml')
        findings = research.get('cross_publication_findings', {})
        m73 = findings.get('cma_nosue_regulatory_neutralization', {})
        assert m73.get('mechanism_id') == 73, \
            "Mechanism #73 must exist in cross-publication findings"

    def test_extends_showcase_coercive_cycle(self):
        """#73 extends the Showcase coercive cycle mechanisms."""
        research = load_yaml('competitor-coverage-research.yaml')
        findings = research.get('cross_publication_findings', {})
        m73 = findings.get('cma_nosue_regulatory_neutralization', {})
        extends = [ref.get('mechanism_id', 0) if isinstance(ref, dict) else ref
                   for ref in m73.get('extends_mechanisms', [])]
        # Should reference existing Google coercive cycle mechanisms
        assert len(extends) >= 2, \
            "Mechanism #73 must extend at least 2 existing mechanisms"

    def test_confounding_factors_documented(self):
        """Mechanism #73 must have confounding factors for intellectual honesty."""
        research = load_yaml('competitor-coverage-research.yaml')
        findings = research.get('cross_publication_findings', {})
        m73 = findings.get('cma_nosue_regulatory_neutralization', {})
        factors = m73.get('confounding_factors', [])
        assert len(factors) >= 3, \
            f"Expected at least 3 confounding factors, got {len(factors)}"

    def test_testable_predictions_documented(self):
        """Mechanism #73 must have testable predictions."""
        research = load_yaml('competitor-coverage-research.yaml')
        findings = research.get('cross_publication_findings', {})
        m73 = findings.get('cma_nosue_regulatory_neutralization', {})
        predictions = m73.get('testable_predictions', [])
        assert len(predictions) >= 3, \
            f"Expected at least 3 testable predictions, got {len(predictions)}"


# ──────────────────────────────────────────────────────────────────
# 8. Financial Quantification Completeness
# ──────────────────────────────────────────────────────────────────

class TestFinancialQuantification:
    """Verify the new Press Gazette data points are captured."""

    def test_traffic_loss_quantified(self):
        """Top-ranked site loses up to 79% traffic when AI Overview appears."""
        entities = load_yaml('competitor-entities.yaml')
        google = entities['entities']['google']
        cma = google.get('cma_regulatory_neutralization', {})
        assert cma.get('traffic_loss_top_ranked_pct', 0) >= 79, \
            "Top-ranked site traffic loss should be at least 79%"

    def test_renting_peace_characterization(self):
        """Industry source characterized Google deals as 'renting peace' — no product value."""
        entities = load_yaml('competitor-entities.yaml')
        google = entities['entities']['google']
        cma = google.get('cma_regulatory_neutralization', {})
        assert 'renting peace' in str(cma.get('deal_characterization', '')).lower(), \
            "Deal 'renting peace' characterization must be documented"

    def test_prisoner_dilemma_framing(self):
        """Industry advisors describe Google's deal structure as a 'prisoner's dilemma.'"""
        entities = load_yaml('competitor-entities.yaml')
        google = entities['entities']['google']
        cma = google.get('cma_regulatory_neutralization', {})
        assert "prisoner" in str(cma.get('deal_characterization', '')).lower(), \
            "Prisoner's dilemma framing must be documented"
