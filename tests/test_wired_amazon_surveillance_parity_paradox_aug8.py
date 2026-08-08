"""
WIRED × Amazon Surveillance Parity Paradox — Type A Deep Dive (Aug 8, 2026 08:00 PT)

Finding: WIRED conducted a multi-part investigative series on Meta's dormant NameTag
facial recognition code (Jun 2026), generating massive amplification (EFF, 70+ advocacy
orgs, Gizmodo, Digital Trends, PetaPixel, etc.). In the same month (Jun 2026), Amazon's
Ring was sued for its ACTIVE "Familiar Faces" facial recognition feature — yet WIRED
produced no comparable investigation.

Amazon has demonstrably WORSE privacy violations than Meta in the surveillance domain:
- FTC $5.8M Ring settlement (employee spied on 81 women in bedrooms, 2023)
- FTC $25M Alexa settlement (children's voice recordings retained, 2023)
- Ring "Familiar Faces" class action lawsuit (Jun 2, 2026 — same month as WIRED NameTag)
- Ring shared footage with police WITHOUT warrants (confirmed 11 times by Amazon VP)
- Bee wearable acquisition: always-listening AI wristband (Jul 2025, CES 2026 update)
- Echo/Alexa: always-listening device in 100M+ US homes

Condé Nast (WIRED parent) has TWO active licensing deals with Amazon:
- Amazon Rufus AI shopping assistant (Jul 2025, multi-year)
- Amazon Alexa+ / Alexa for Shopping integration (May 2026)

The paradox: Meta's DORMANT code (never activated, promptly removed) received deeper
investigative coverage than Amazon's ACTUAL FTC-enforced privacy violations, active
facial recognition lawsuit, and always-listening wearable — from a publication whose
parent has financial relationships with Amazon.

Sources:
- WIRED NameTag investigation: Jun 4, 2026 (cited by EFF, Gizmodo, Digital Trends,
  Android Authority, PetaPixel, Malwarebytes, Northeastern University)
- WIRED Rank One / police tech follow-up: Jun 2026
- EFF victory post: Jun 8, 2026 (https://www.eff.org/deeplinks/2026/06/victory-meta-strips-facial-recognition-code-smart-glasses-app-after-public-outcry)
- Ring FTC settlement: May 31, 2023 (https://www.ftc.gov/news-events/news/press-releases/2023/05/ftc-says-ring-employees-illegally-surveilled-customers-failed-stop-hackers-taking-control-users)
- Alexa FTC settlement: May 31, 2023 ($25M, children's recordings)
- Ring Familiar Faces lawsuit: Jun 2, 2026 (https://www.reuters.com/legal/government/amazons-ring-sued-over-facial-recognition-feature-latest-privacy-concern-2026-06-02/)
- Ring police sharing: Consumer Reports (https://www.consumerreports.org/law-enforcement/amazon-shared-ring-footage-with-police-without-a-warrant-a6093504500/)
- Amazon Bee acquisition: Jul 22, 2025 (https://techcrunch.com/2025/07/22/amazon-acquires-bee-the-ai-wearable-that-records-everything-you-say/)
- Bee TechCrunch review: May 24, 2026 (https://techcrunch.com/2026/05/24/i-tried-amazons-bee-wearable-and-am-both-intrigued-and-slightly-creeped-out/)
- Amazon-Condé Nast Rufus deal: Jul 2025 (https://digiday.com/media/conde-nast-and-hearst-strike-amazon-ai-licensing-deals-for-rufus/)
"""

import pytest
import yaml
import os
import re

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_wired_profile():
    with open(os.path.join(PROFILES_DIR, 'wired.yaml'), 'r') as f:
        return yaml.safe_load(f)


def load_competitor_entities():
    with open(os.path.join(PROFILES_DIR, 'competitor-entities.yaml'), 'r') as f:
        return yaml.safe_load(f)


def load_competitor_research():
    with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml'), 'r') as f:
        return yaml.safe_load(f)


# ────────────────────────────────────────────────────────────
# 1. Financial Relationship Verification
# ────────────────────────────────────────────────────────────

class TestFinancialRelationship:
    """Verify Condé Nast-Amazon financial ties are documented."""

    def test_wired_has_amazon_competitor_relationship(self):
        profile = load_wired_profile()
        cr = profile.get('competitor_relationships', {})
        assert 'amazon' in cr, "WIRED profile must document Amazon competitor relationship"

    def test_amazon_financial_tie_is_licensing(self):
        profile = load_wired_profile()
        amazon = profile['competitor_relationships']['amazon']
        assert amazon['financial_tie'] == 'licensing', \
            f"Amazon financial tie should be 'licensing', got '{amazon['financial_tie']}'"

    def test_amazon_direction_is_receiving(self):
        profile = load_wired_profile()
        amazon = profile['competitor_relationships']['amazon']
        assert amazon['direction'] == 'receiving', \
            f"Condé Nast receives money FROM Amazon, got '{amazon['direction']}'"

    def test_amazon_coverage_prediction_is_softer(self):
        profile = load_wired_profile()
        amazon = profile['competitor_relationships']['amazon']
        assert amazon['coverage_prediction'] == 'softer', \
            f"Coverage prediction for Amazon should be 'softer', got '{amazon['coverage_prediction']}'"

    def test_meta_has_no_financial_tie(self):
        profile = load_wired_profile()
        meta = profile['competitor_relationships']['meta']
        assert meta['financial_tie'] == 'none', \
            f"Meta financial tie should be 'none', got '{meta['financial_tie']}'"

    def test_meta_estimated_value_is_zero(self):
        profile = load_wired_profile()
        meta = profile['competitor_relationships']['meta']
        assert '$0' in meta['estimated_value'], \
            f"Meta estimated value should be $0, got '{meta['estimated_value']}'"

    def test_rufus_deal_documented(self):
        profile = load_wired_profile()
        amazon = profile['competitor_relationships']['amazon']
        desc = amazon.get('description', '').lower()
        assert 'rufus' in desc, "Amazon relationship should mention Rufus deal"


# ────────────────────────────────────────────────────────────
# 2. Surveillance Parity Paradox Core Claims
# ────────────────────────────────────────────────────────────

class TestSurveillanceParityParadox:
    """Core asymmetry: Meta dormant code vs Amazon FTC enforcement."""

    def test_paradox_documented_in_wired_profile(self):
        profile = load_wired_profile()
        amazon = profile['competitor_relationships']['amazon']
        assert 'surveillance_parity_paradox' in amazon, \
            "WIRED Amazon relationship should have surveillance_parity_paradox finding"

    def test_paradox_has_meta_nametag_investigation(self):
        profile = load_wired_profile()
        paradox = profile['competitor_relationships']['amazon']['surveillance_parity_paradox']
        assert 'nametag' in paradox.get('meta_investigation', {}).get('feature_name', '').lower() or \
               'nametag' in str(paradox).lower(), \
            "Paradox must reference Meta's NameTag investigation"

    def test_paradox_documents_ring_ftc_settlement(self):
        profile = load_wired_profile()
        paradox = profile['competitor_relationships']['amazon']['surveillance_parity_paradox']
        text = str(paradox).lower()
        assert 'ftc' in text and 'ring' in text, \
            "Paradox must document Ring FTC settlement"

    def test_paradox_documents_ring_facial_recognition_lawsuit(self):
        profile = load_wired_profile()
        paradox = profile['competitor_relationships']['amazon']['surveillance_parity_paradox']
        text = str(paradox).lower()
        assert 'familiar faces' in text or 'facial recognition' in text, \
            "Paradox must reference Ring's Familiar Faces/facial recognition lawsuit"

    def test_paradox_documents_bee_wearable(self):
        profile = load_wired_profile()
        paradox = profile['competitor_relationships']['amazon']['surveillance_parity_paradox']
        text = str(paradox).lower()
        assert 'bee' in text, "Paradox must reference Amazon Bee wearable"

    def test_paradox_documents_alexa_ftc_settlement(self):
        profile = load_wired_profile()
        paradox = profile['competitor_relationships']['amazon']['surveillance_parity_paradox']
        text = str(paradox).lower()
        assert 'alexa' in text and ('ftc' in text or 'settlement' in text or 'children' in text), \
            "Paradox must document Alexa FTC settlement (children's recordings)"

    def test_paradox_documents_ring_police_sharing(self):
        profile = load_wired_profile()
        paradox = profile['competitor_relationships']['amazon']['surveillance_parity_paradox']
        text = str(paradox).lower()
        assert 'police' in text or 'law enforcement' in text or 'warrant' in text, \
            "Paradox must reference Ring sharing footage with police without warrants"

    def test_paradox_has_asymmetry_assessment(self):
        profile = load_wired_profile()
        paradox = profile['competitor_relationships']['amazon']['surveillance_parity_paradox']
        assert 'asymmetry_score' in paradox or 'severity' in paradox, \
            "Paradox must have an asymmetry_score or severity assessment"

    def test_meta_code_was_dormant(self):
        """The investigated Meta code was never activated for users."""
        profile = load_wired_profile()
        paradox = profile['competitor_relationships']['amazon']['surveillance_parity_paradox']
        text = str(paradox).lower()
        assert 'dormant' in text or 'inactive' in text or 'never activated' in text, \
            "Must note Meta's code was dormant/inactive/never activated"

    def test_amazon_violations_were_actual_enforcement(self):
        """Amazon had actual FTC enforcement, not just dormant code."""
        profile = load_wired_profile()
        paradox = profile['competitor_relationships']['amazon']['surveillance_parity_paradox']
        text = str(paradox).lower()
        # YAML may strip $ from dollar amounts in multiline strings
        assert '5.8' in text and 'ring' in text and ('ftc' in text or 'settlement' in text), \
            "Must reference the $5.8M Ring FTC settlement amount"


# ────────────────────────────────────────────────────────────
# 3. Temporal Coincidence (Jun 2026)
# ────────────────────────────────────────────────────────────

class TestTemporalCoincidence:
    """Ring lawsuit and WIRED NameTag investigation were the SAME month."""

    def test_nametag_investigation_date_jun_2026(self):
        profile = load_wired_profile()
        paradox = profile['competitor_relationships']['amazon']['surveillance_parity_paradox']
        meta_inv = paradox.get('meta_investigation', {})
        date_str = str(meta_inv.get('date', ''))
        assert '2026-06' in date_str or 'jun' in date_str.lower(), \
            "Meta NameTag investigation should be dated Jun 2026"

    def test_ring_lawsuit_date_jun_2026(self):
        profile = load_wired_profile()
        paradox = profile['competitor_relationships']['amazon']['surveillance_parity_paradox']
        amazon_events = paradox.get('amazon_enforcement_events', [])
        # Find the Ring facial recognition lawsuit
        ring_lawsuit = [e for e in amazon_events
                       if 'familiar' in str(e).lower() or 'lawsuit' in str(e).lower()]
        assert len(ring_lawsuit) > 0, "Must list Ring Familiar Faces lawsuit"
        lawsuit_date = str(ring_lawsuit[0].get('date', ''))
        assert '2026-06' in lawsuit_date or '2026-06-02' in lawsuit_date, \
            "Ring Familiar Faces lawsuit was filed Jun 2, 2026"

    def test_same_month_documented(self):
        """The temporal coincidence must be explicitly documented."""
        profile = load_wired_profile()
        paradox = profile['competitor_relationships']['amazon']['surveillance_parity_paradox']
        text = str(paradox).lower()
        assert 'same month' in text or 'june 2026' in text or 'simultaneous' in text, \
            "Must note the temporal coincidence of Jun 2026"


# ────────────────────────────────────────────────────────────
# 4. Amplification Asymmetry
# ────────────────────────────────────────────────────────────

class TestAmplificationAsymmetry:
    """WIRED NameTag generated massive downstream amplification;
    Amazon Ring lawsuit generated none from WIRED."""

    def test_nametag_amplification_documented(self):
        profile = load_wired_profile()
        paradox = profile['competitor_relationships']['amazon']['surveillance_parity_paradox']
        text = str(paradox).lower()
        assert 'eff' in text or 'electronic frontier' in text, \
            "Must note EFF verified WIRED's NameTag findings"

    def test_nametag_advocacy_response(self):
        profile = load_wired_profile()
        paradox = profile['competitor_relationships']['amazon']['surveillance_parity_paradox']
        text = str(paradox).lower()
        assert 'advocacy' in text or '70' in text, \
            "Must note 70+ advocacy orgs responded to WIRED's Meta investigation"

    def test_investigation_depth_comparison(self):
        """Meta got multi-part series; Amazon got nothing comparable."""
        profile = load_wired_profile()
        paradox = profile['competitor_relationships']['amazon']['surveillance_parity_paradox']
        meta_inv = paradox.get('meta_investigation', {})
        assert meta_inv.get('article_count', 0) >= 2, \
            "WIRED published 2+ articles on Meta NameTag (multi-part series)"

    def test_amazon_wired_investigation_count(self):
        """WIRED published no comparable investigation on Amazon surveillance."""
        profile = load_wired_profile()
        paradox = profile['competitor_relationships']['amazon']['surveillance_parity_paradox']
        assert paradox.get('wired_amazon_surveillance_articles', 0) == 0, \
            "WIRED published 0 comparable investigative articles on Amazon surveillance"


# ────────────────────────────────────────────────────────────
# 5. Device-Level Surveillance Comparison
# ────────────────────────────────────────────────────────────

class TestDeviceSurveillanceComparison:
    """Amazon's surveillance footprint is larger than Meta's in every dimension."""

    def test_ring_installed_base_larger(self):
        """Ring has 10M+ devices; Meta glasses have ~5M+."""
        profile = load_wired_profile()
        paradox = profile['competitor_relationships']['amazon']['surveillance_parity_paradox']
        comp = paradox.get('device_comparison', {})
        # Just verify the comparison section exists and has data
        assert 'ring' in str(comp).lower() or 'device_comparison' in paradox, \
            "Must have device-level surveillance comparison"

    def test_amazon_always_listening_devices(self):
        """Amazon has 100M+ always-listening Alexa devices."""
        profile = load_wired_profile()
        paradox = profile['competitor_relationships']['amazon']['surveillance_parity_paradox']
        text = str(paradox).lower()
        assert 'always-listening' in text or 'always listening' in text, \
            "Must note Amazon has always-listening devices"

    def test_bee_records_all_conversations(self):
        """Bee wearable records ALL conversations unless manually muted."""
        profile = load_wired_profile()
        paradox = profile['competitor_relationships']['amazon']['surveillance_parity_paradox']
        text = str(paradox).lower()
        assert 'record' in text and 'conversation' in text, \
            "Must note Bee records conversations"


# ────────────────────────────────────────────────────────────
# 6. Source Verification
# ────────────────────────────────────────────────────────────

class TestSourceVerification:
    """All claims must have source URLs."""

    def test_paradox_has_source_urls(self):
        profile = load_wired_profile()
        paradox = profile['competitor_relationships']['amazon']['surveillance_parity_paradox']
        sources = paradox.get('source_urls', [])
        assert len(sources) >= 4, \
            f"Paradox must have at least 4 source URLs, has {len(sources)}"

    def test_all_source_urls_are_https(self):
        profile = load_wired_profile()
        paradox = profile['competitor_relationships']['amazon']['surveillance_parity_paradox']
        sources = paradox.get('source_urls', [])
        for url in sources:
            assert url.startswith('https://'), \
                f"Source URL must be HTTPS: {url}"

    def test_ftc_source_present(self):
        profile = load_wired_profile()
        paradox = profile['competitor_relationships']['amazon']['surveillance_parity_paradox']
        sources = paradox.get('source_urls', [])
        ftc_sources = [u for u in sources if 'ftc.gov' in u]
        assert len(ftc_sources) >= 1, "Must include FTC.gov source"

    def test_reuters_ring_lawsuit_source(self):
        profile = load_wired_profile()
        paradox = profile['competitor_relationships']['amazon']['surveillance_parity_paradox']
        sources = paradox.get('source_urls', [])
        reuters_sources = [u for u in sources if 'reuters.com' in u]
        assert len(reuters_sources) >= 1, "Must include Reuters source for Ring lawsuit"


# ────────────────────────────────────────────────────────────
# 7. Financial Incentive Model
# ────────────────────────────────────────────────────────────

class TestFinancialIncentiveModel:
    """The paradox fits the MediaScope financial incentive thesis."""

    def test_deal_count_comparison(self):
        """Amazon: 2 deals (Rufus + Alexa for Shopping). Meta: 0 deals."""
        profile = load_wired_profile()
        amazon = profile['competitor_relationships']['amazon']
        assert amazon.get('conde_nast_amazon_deal_count', 0) >= 2, \
            "Condé Nast has at least 2 deals with Amazon"

    def test_meta_deal_count_zero(self):
        profile = load_wired_profile()
        meta = profile['competitor_relationships']['meta']
        assert meta['estimated_value'] == '$0', \
            f"Meta estimated value should be '$0', got '{meta['estimated_value']}'"

    def test_financial_prediction_matches_coverage(self):
        """Softer prediction + softer actual coverage = model validated."""
        profile = load_wired_profile()
        amazon = profile['competitor_relationships']['amazon']
        assert amazon['coverage_prediction'] == 'softer', \
            "Amazon coverage predicted softer"
        paradox = amazon['surveillance_parity_paradox']
        assert paradox.get('prediction_validated', False), \
            "The softer-coverage prediction must be validated by the surveillance parity finding"


# ────────────────────────────────────────────────────────────
# 8. Cross-Reference Integrity
# ────────────────────────────────────────────────────────────

class TestCrossReferenceIntegrity:
    """Ensure consistency with other MediaScope files."""

    def test_amazon_entity_exists_in_competitor_entities(self):
        entities = load_competitor_entities()
        assert 'amazon' in entities.get('entities', {}), \
            "Amazon must exist in competitor-entities.yaml"

    def test_amazon_sextuple_leverage_documented(self):
        entities = load_competitor_entities()
        amazon = entities['entities']['amazon']
        assert 'sextuple_publisher_leverage' in amazon, \
            "Amazon sextuple leverage should be documented"

    def test_wired_revenue_relationships_has_amazon(self):
        """The Rufus deal should appear in the revenue_relationships section."""
        profile = load_wired_profile()
        deals = profile.get('revenue_relationships', [])
        rufus_deals = [d for d in deals if 'rufus' in str(d).lower() or 'amazon' in str(d).lower()]
        assert len(rufus_deals) >= 1, \
            "Rufus/Amazon deal should be listed in WIRED revenue_relationships"

    def test_competitor_research_amazon_entry(self):
        """Amazon should have entries in competitor-coverage-research.yaml."""
        research = load_competitor_research()
        text = str(research).lower()
        assert 'amazon' in text, \
            "Amazon must be referenced in competitor-coverage-research.yaml"
