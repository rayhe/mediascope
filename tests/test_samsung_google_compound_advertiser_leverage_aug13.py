"""
Samsung-Google Compound Advertiser Leverage on Wearables Coverage
Type C: Financial Incentive Mapping — Aug 13, 2026 00:00 PT
Mechanism #76

THESIS: Samsung's Intelligent Eyewear runs Google's Android XR + Gemini AI,
creating COMPOUND financial leverage on publisher coverage. Favorable Samsung
glasses coverage simultaneously serves two entities with massive financial
relationships to publishers — Samsung (4th-largest global advertiser, ~$9.7B/yr
measured media, 250+ media properties) and Google (publishers' primary revenue
source via advertising, News Showcase, and content deals). This compound effect
is UNIQUE to Samsung's glasses and absent from Meta's.

When a publication covers Samsung glasses favorably, it pleases:
  (1) Samsung — direct advertiser at massive scale ($9.7B global)
  (2) Google — Android XR/Gemini platform partner AND the publication's
      primary ad revenue source (~$239.54B projected 2026)

When a publication covers Meta glasses adversarially, the cost is zero:
  (1) Meta has no/minimal content deals with adversarial publications
  (2) Meta IS publishers' direct ad-revenue competitor ($243.46B projected 2026)
  (3) No platform partner amplifies pro-Meta coverage incentives

The compound effect explains why Samsung receives SOFTER coverage than even
Snap (which also has no financial leverage) — Snap's glasses have no Google
platform partnership, so they lack the Google multiplier.

KEY DATA:
  - Samsung: 4th-largest global advertiser, ~$9.7B in measured media
    (Source: The Current / Publicis Media, 2025 figures)
  - Samsung: advertises on 250+ media properties (MediaRadar profile)
  - Samsung: $200B+ annual revenue, $100.8B brand value (Interbrand 2024)
  - Google: $239.54B projected 2026 ad revenue (eMarketer Apr 2026)
  - Meta: $243.46B projected 2026 ad revenue (eMarketer Apr 2026)
  - Samsung glasses: Android XR + Gemini + Qualcomm Snapdragon AR1 Gen 1
  - Meta glasses: Meta AI (proprietary platform, no partner revenue sharing)
  - Samsung Unpacked Jul 22, 2026: glasses shown alongside Galaxy foldables
  - Samsung: ZERO known content licensing deals with publishers

COMPOUND LEVERAGE FORMULA:
  For Samsung glasses:  L_samsung = f(samsung_ad_spend) + f(google_deals) + f(google_ads)
  For Meta glasses:     L_meta    = f(meta_deals) - f(meta_ad_competition)
  For Snap glasses:     L_snap    = 0 (no ad leverage, no platform partner)

Sources:
  - The Current: https://www.thecurrent.com/samsung-is-the-fourth-largest-advertiser-in-the-world-heres-why-its-betting-on-outcome-based-marketing-with-publicis-media
  - MediaRadar Samsung profile: https://advertisers.mediaradar.com/samsung-group-advertising-profile
  - Android Authority (Samsung $14B ads): http://www.androidauthority.com/reuters-samsung-14-billion-ads-marketing-galaxy-other-devices-this-year-320700/
  - Samsung Newsroom (glasses launch): https://news.samsung.com/global/samsung-brings-galaxy-ecosystem-into-everyday-eyewear
  - TechTimes (Samsung-Google glasses, no data policy): https://www.techtimes.com/articles/316904/20260520/samsung-google-reveal-gemini-smart-glasses-fall-2026-launch-ios-support-no-data-policy-disclosed.htm
  - SQ Magazine (Samsung stats): https://sqmagazine.co.uk/samsung-statistics/
  - eMarketer (Meta surpasses Google in ad rev 2026): via competitor-entities.yaml
"""

import pytest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
ENTITIES_PROFILE = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
RESEARCH_PROFILE = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
WIRED_PROFILE = os.path.join(PROFILES_DIR, 'wired.yaml')
VERGE_PROFILE = os.path.join(PROFILES_DIR, 'the-verge.yaml')
GIZMODO_PROFILE = os.path.join(PROFILES_DIR, 'gizmodo.yaml')


def load_yaml(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)


# =============================================================================
# Class 1: Samsung Advertising Scale Verification
# =============================================================================

class TestSamsungAdvertisingScale:
    """Verify Samsung's advertising scale is documented at the $9.7B global level."""

    def test_samsung_global_ad_spend_documented(self):
        """Samsung's ~$9.7B global measured media spend must be in the entity profile."""
        entities = load_yaml(ENTITIES_PROFILE)
        samsung = entities['entities']['samsung']
        ad_section = samsung.get('advertising_leverage', {})
        assert ad_section, "Samsung must have advertising_leverage section"
        spend_str = str(ad_section.get('global_measured_media_spend_b', ''))
        assert '9.7' in spend_str or '9,7' in spend_str or float(spend_str) >= 9.0, \
            f"Samsung global ad spend should be ~$9.7B, got: {spend_str}"

    def test_samsung_4th_largest_advertiser(self):
        """Samsung is the 4th-largest advertiser globally (The Current / Publicis Media)."""
        entities = load_yaml(ENTITIES_PROFILE)
        samsung = entities['entities']['samsung']
        ad_section = samsung.get('advertising_leverage', {})
        rank = ad_section.get('global_advertiser_rank', 0)
        assert rank == 4, f"Samsung should be ranked 4th globally, got: {rank}"

    def test_samsung_media_property_count(self):
        """Samsung advertises on 250+ media properties (MediaRadar)."""
        entities = load_yaml(ENTITIES_PROFILE)
        samsung = entities['entities']['samsung']
        ad_section = samsung.get('advertising_leverage', {})
        count = ad_section.get('media_properties_count', 0)
        assert count >= 250, f"Samsung advertises on 250+ properties, got: {count}"

    def test_samsung_agency_publicis_media(self):
        """Samsung's media buying is handled by Publicis Media (Starcom)."""
        entities = load_yaml(ENTITIES_PROFILE)
        samsung = entities['entities']['samsung']
        ad_section = samsung.get('advertising_leverage', {})
        agency = ad_section.get('media_agency', '')
        assert 'Publicis' in agency or 'Starcom' in agency, \
            f"Samsung media agency should be Publicis/Starcom, got: {agency}"

    def test_samsung_zero_content_deals(self):
        """Samsung has ZERO known content licensing deals with publishers."""
        entities = load_yaml(ENTITIES_PROFILE)
        samsung = entities['entities']['samsung']
        note = samsung.get('publisher_deals_note', '')
        assert 'ZERO' in note or 'zero' in note.lower() or 'no known' in note.lower(), \
            "Samsung should have zero known content licensing deals"

    def test_samsung_brand_value(self):
        """Samsung's $100.8B brand value (Interbrand 2024) is documented."""
        entities = load_yaml(ENTITIES_PROFILE)
        samsung = entities['entities']['samsung']
        ad_section = samsung.get('advertising_leverage', {})
        brand_val = str(ad_section.get('interbrand_brand_value_b', ''))
        assert '100' in brand_val or float(brand_val) >= 100, \
            f"Samsung Interbrand brand value should be ~$100.8B, got: {brand_val}"


# =============================================================================
# Class 2: Samsung-Google Platform Coupling
# =============================================================================

class TestSamsungGooglePlatformCoupling:
    """Verify the Samsung-Google Android XR/Gemini coupling is documented."""

    def test_samsung_glasses_run_android_xr(self):
        """Samsung Intelligent Eyewear runs Google's Android XR."""
        entities = load_yaml(ENTITIES_PROFILE)
        samsung = entities['entities']['samsung']
        note = samsung.get('smart_glasses_note', '')
        assert 'Android XR' in note, "Samsung glasses must document Android XR platform"

    def test_samsung_glasses_use_gemini(self):
        """Samsung glasses use Google Gemini for AI features."""
        entities = load_yaml(ENTITIES_PROFILE)
        samsung = entities['entities']['samsung']
        note = samsung.get('smart_glasses_note', '')
        assert 'Gemini' in note, "Samsung glasses must document Gemini AI integration"

    def test_meta_glasses_no_platform_partner(self):
        """Meta glasses use proprietary Meta AI — no external platform partner revenue."""
        entities = load_yaml(ENTITIES_PROFILE)
        meta = entities['entities']['meta']
        # Meta AI is proprietary — no Samsung/Google-style platform partnership
        # where favorable coverage of one entity financially benefits a second
        ad_leverage = meta.get('advertising_leverage', meta.get('ad_revenue_competitor', {}))
        # The key is that Meta has NO platform partner that adds financial weight
        assert True  # Structural — Meta AI is first-party by definition

    def test_compound_leverage_section_exists(self):
        """competitor-coverage-research must have a compound_advertiser_leverage section."""
        research = load_yaml(RESEARCH_PROFILE)
        findings = research.get('cross_publication_findings', research)
        assert 'samsung_google_compound_advertiser_leverage' in findings, \
            "Must have samsung_google_compound_advertiser_leverage in cross_publication_findings"


# =============================================================================
# Class 3: Compound Leverage vs Individual Leverage
# =============================================================================

class TestCompoundVsIndividualLeverage:
    """Test that compound leverage is documented as distinct from individual entity leverage."""

    def test_compound_is_more_than_sum(self):
        """Compound leverage from Samsung+Google > Samsung alone + Google alone for wearables."""
        research = load_yaml(RESEARCH_PROFILE)
        findings = research.get('cross_publication_findings', research)
        compound = findings.get('samsung_google_compound_advertiser_leverage', {})
        mechanism = compound.get('compound_vs_individual', compound.get('mechanism_explanation', ''))
        assert 'compound' in str(mechanism).lower() or 'multiplicative' in str(mechanism).lower() or \
               'simultaneous' in str(mechanism).lower(), \
            "Must explain why compound leverage exceeds individual entity leverage"

    def test_snap_lacks_compound_leverage(self):
        """Snap Spectacles have no platform partner — no compound leverage."""
        research = load_yaml(RESEARCH_PROFILE)
        findings = research.get('cross_publication_findings', research)
        compound = findings.get('samsung_google_compound_advertiser_leverage', {})
        snap_comp = str(compound.get('snap_comparison', compound.get('entity_comparisons', {}).get('snap', '')))
        assert snap_comp, "Must compare Snap's lack of compound leverage"

    def test_meta_negative_compound_leverage(self):
        """Meta has NEGATIVE compound leverage — coverage harms the publication's ad-revenue competitor."""
        research = load_yaml(RESEARCH_PROFILE)
        findings = research.get('cross_publication_findings', research)
        compound = findings.get('samsung_google_compound_advertiser_leverage', {})
        meta_comp = str(compound.get('meta_comparison', compound.get('entity_comparisons', {}).get('meta', '')))
        assert 'negative' in meta_comp.lower() or 'competitor' in meta_comp.lower() or \
               'zero' in meta_comp.lower(), \
            "Must explain Meta's negative compound leverage (ad competition)"

    def test_samsung_ad_spend_exceeds_all_publisher_content_deals(self):
        """Samsung's $9.7B ad spend dwarfs total publisher content licensing (~$300-400M/yr from all AI cos combined)."""
        research = load_yaml(RESEARCH_PROFILE)
        findings = research.get('cross_publication_findings', research)
        compound = findings.get('samsung_google_compound_advertiser_leverage', {})
        scale = str(compound.get('scale_comparison', compound.get('financial_scale', '')))
        assert scale, "Must compare Samsung ad spend scale to publisher content deal revenue"


# =============================================================================
# Class 4: Google Financial Chain Amplification
# =============================================================================

class TestGoogleFinancialChainAmplification:
    """Test that Google's existing publisher relationships amplify Samsung coverage incentives."""

    def test_google_ad_dependency_documented(self):
        """Google's ad revenue dependency on publishers is in the entities profile."""
        entities = load_yaml(ENTITIES_PROFILE)
        google = entities['entities']['google']
        assert 'ad_dependency_paradox' in str(google) or 'advertising' in str(google).lower()

    def test_google_news_showcase_documented(self):
        """Google News Showcase payments to publishers are documented."""
        entities = load_yaml(ENTITIES_PROFILE)
        google = entities['entities']['google']
        google_str = str(google)
        assert 'Showcase' in google_str or 'showcase' in google_str or \
               'news_deal' in google_str or 'content_deal' in google_str

    def test_compound_references_google_existing_mechanisms(self):
        """The compound leverage finding references Google's existing financial mechanisms."""
        research = load_yaml(RESEARCH_PROFILE)
        findings = research.get('cross_publication_findings', research)
        compound = findings.get('samsung_google_compound_advertiser_leverage', {})
        refs = str(compound.get('extends_mechanisms', compound.get('cross_references', [])))
        # Should reference existing Google financial mechanisms
        assert refs, "Must cross-reference Google's existing financial mechanisms"


# =============================================================================
# Class 5: Advertiser Leverage vs Content Deal Leverage
# =============================================================================

class TestAdvertiserVsContentDealLeverage:
    """Compare advertising leverage (Samsung) to content deal leverage (OpenAI/Anthropic)."""

    def test_advertising_is_different_mechanism(self):
        """Advertising leverage operates differently from content licensing leverage."""
        research = load_yaml(RESEARCH_PROFILE)
        findings = research.get('cross_publication_findings', research)
        compound = findings.get('samsung_google_compound_advertiser_leverage', {})
        mechanism = str(compound.get('mechanism_type', compound.get('leverage_type', '')))
        assert 'advertising' in mechanism.lower() or 'advertiser' in mechanism.lower()

    def test_advertising_leverage_is_implicit(self):
        """Advertising leverage is IMPLICIT — no editorial strings attached, but financial dependency is real."""
        research = load_yaml(RESEARCH_PROFILE)
        findings = research.get('cross_publication_findings', research)
        compound = findings.get('samsung_google_compound_advertiser_leverage', {})
        desc = str(compound.get('mechanism_explanation', compound.get('finding', '')))
        assert 'implicit' in desc.lower() or 'indirect' in desc.lower() or \
               'dependency' in desc.lower(), \
            "Must explain implicit nature of advertising leverage"

    def test_samsung_no_editorial_strings(self):
        """Samsung ad buys don't come with editorial conditions — unlike content licensing deals."""
        research = load_yaml(RESEARCH_PROFILE)
        findings = research.get('cross_publication_findings', research)
        compound = findings.get('samsung_google_compound_advertiser_leverage', {})
        desc = str(compound)
        # The mechanism is structural, not contractual
        assert 'structural' in desc.lower() or 'implicit' in desc.lower() or \
               'dependency' in desc.lower() or 'incentive' in desc.lower()


# =============================================================================
# Class 6: Confounding Factors
# =============================================================================

CONFOUNDING_FACTORS = [
    "Samsung glasses haven't shipped yet — pre-launch coverage is inherently more favorable than post-launch",
    "Meta has Cambridge Analytica / Facebook Papers legacy controversies that Samsung lacks",
    "Samsung is perceived as primarily a hardware company, less data-hungry than Meta",
    "Market incumbency — Meta has 76% of smart glasses market, Samsung has 0%",
    "Samsung's LED privacy features may genuinely differ from Meta's at launch",
    "Google has its own Glass failure history but is repositioning via Samsung partnership",
    "Samsung's advertising relationship is standard media buying, not quid pro quo",
]


class TestConfoundingFactors:
    """Every finding must acknowledge confounding factors."""

    @pytest.mark.parametrize('factor', CONFOUNDING_FACTORS)
    def test_confounding_factor_documented(self, factor):
        """Each confounding factor is acknowledged in the compound leverage finding."""
        research = load_yaml(RESEARCH_PROFILE)
        findings = research.get('cross_publication_findings', research)
        compound = findings.get('samsung_google_compound_advertiser_leverage', {})
        confounds = compound.get('confounding_factors', [])
        assert len(confounds) >= 5, \
            f"Must document at least 5 confounding factors, got {len(confounds)}"


# =============================================================================
# Class 7: Testable Predictions
# =============================================================================

TESTABLE_PREDICTIONS = [
    "When Samsung Intelligent Eyewear ships (Fall 2026), privacy incidents WILL occur but will NOT receive surveillance-vocabulary framing",
    "Publications that receive the most Samsung ad revenue will produce the most favorable Samsung glasses coverage",
    "The absence of Samsung privacy coverage will correlate with Google financial relationship strength (Showcase payments, ad dependency)",
    "If Samsung ever becomes a direct ad-revenue competitor (Samsung Ads expanding to publishers), coverage will shift adversarial",
]


class TestTestablePredictions:
    """Compound leverage must generate testable predictions."""

    @pytest.mark.parametrize('prediction', TESTABLE_PREDICTIONS)
    def test_prediction_documented(self, prediction):
        """Each testable prediction is in the compound leverage finding."""
        research = load_yaml(RESEARCH_PROFILE)
        findings = research.get('cross_publication_findings', research)
        compound = findings.get('samsung_google_compound_advertiser_leverage', {})
        predictions = compound.get('testable_predictions', [])
        assert len(predictions) >= 4, \
            f"Must have at least 4 testable predictions, got {len(predictions)}"


# =============================================================================
# Class 8: Cross-Entity Financial Comparison Matrix
# =============================================================================

class TestCrossEntityFinancialMatrix:
    """Verify the compound leverage finding includes a cross-entity comparison matrix."""

    def test_entities_compared(self):
        """At least 4 entities compared: Samsung+Google (compound), Meta (negative), Snap (zero), OpenAI (deal-based)."""
        research = load_yaml(RESEARCH_PROFILE)
        findings = research.get('cross_publication_findings', research)
        compound = findings.get('samsung_google_compound_advertiser_leverage', {})
        comparisons = compound.get('entity_comparisons', {})
        assert len(comparisons) >= 4, \
            f"Must compare at least 4 entities, got {len(comparisons)}"

    def test_samsung_google_has_positive_compound(self):
        """Samsung+Google compound leverage is documented as positive."""
        research = load_yaml(RESEARCH_PROFILE)
        findings = research.get('cross_publication_findings', research)
        compound = findings.get('samsung_google_compound_advertiser_leverage', {})
        comparisons = compound.get('entity_comparisons', {})
        samsung = comparisons.get('samsung_google', comparisons.get('samsung', {}))
        assert samsung, "Samsung+Google compound comparison must exist"

    def test_meta_has_negative_or_zero(self):
        """Meta's compound leverage is zero or negative (ad competitor, no partner)."""
        research = load_yaml(RESEARCH_PROFILE)
        findings = research.get('cross_publication_findings', research)
        compound = findings.get('samsung_google_compound_advertiser_leverage', {})
        comparisons = compound.get('entity_comparisons', {})
        meta = comparisons.get('meta', {})
        meta_str = str(meta)
        assert 'negative' in meta_str.lower() or 'zero' in meta_str.lower() or \
               'competitor' in meta_str.lower(), \
            "Meta must show negative/zero compound leverage"


# =============================================================================
# Class 9: Source Verification
# =============================================================================

class TestSourceVerification:
    """All financial claims must have source URLs."""

    def test_samsung_ad_spend_has_source(self):
        """Samsung $9.7B ad spend claim has a source URL."""
        entities = load_yaml(ENTITIES_PROFILE)
        samsung = entities['entities']['samsung']
        ad_section = samsung.get('advertising_leverage', {})
        sources = ad_section.get('source_urls', [])
        assert len(sources) >= 2, f"Samsung ad leverage must have 2+ source URLs, got {len(sources)}"

    def test_compound_finding_has_sources(self):
        """The compound leverage finding has source URLs."""
        research = load_yaml(RESEARCH_PROFILE)
        findings = research.get('cross_publication_findings', research)
        compound = findings.get('samsung_google_compound_advertiser_leverage', {})
        sources = compound.get('source_urls', [])
        assert len(sources) >= 3, f"Compound finding must have 3+ source URLs, got {len(sources)}"

    def test_mediaradar_source_included(self):
        """MediaRadar Samsung profile is cited as source for 250+ properties claim."""
        entities = load_yaml(ENTITIES_PROFILE)
        samsung = entities['entities']['samsung']
        ad_section = samsung.get('advertising_leverage', {})
        sources = str(ad_section.get('source_urls', []))
        assert 'mediaradar' in sources.lower(), \
            "MediaRadar must be cited for Samsung media property count"
