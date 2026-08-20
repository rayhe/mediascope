"""
Mechanism #190: The Verge (PMC/PMX) Apple Triple Camera Wearable Ecosystem —
Privacy Vocabulary Zero vs Meta Privacy Vocabulary Saturation

Type A: Competitor Coverage Deep Dive (Aug 19, 2026 23:00 PT)
Publication: The Verge (PMC/PMX subsidiary, acquired Jun 18, 2026)
Competitor: Apple (N50 smart glasses + AI pendant + camera AirPods)

FINDING: The Verge covered Apple's announcement of THREE camera-equipped
wearables on Feb 17, 2026 (corroborating Bloomberg's Mark Gurman report),
framing all three as product news with ZERO privacy alarm vocabulary.
Apple's AI pendant specifically features an "always-on camera" described
as the "eyes and ears" of the iPhone — functionally identical to Meta's
reported "super sensing" feature (always-on camera capturing surroundings).

Yet when The Verge covers Meta's equivalent always-on camera features:
- Victoria Song wrote dedicated privacy/surveillance pieces about Meta
  glasses (doxing investigation Oct 2024, LED tamper-proof flagging Jul 2026,
  Live AI data handling critique)
- The Verge's Alex Himel interview framed Meta's LED update as addressing
  "increasing misuse amid growing adoption"
- Meta's "super sensing" feature received "nightmarish" framing across
  the publication ecosystem

THE THREE APPLE ALWAYS-ON CAMERA DEVICES:

| Device        | Camera Spec                  | Privacy Profile                | Verge Framing  |
|---------------|------------------------------|-------------------------------|----------------|
| N50 Glasses   | Dual: high-res + CV sensor   | "real-time understanding"     | Product news   |
| AI Pendant    | Always-on camera             | "eyes and ears of iPhone"     | Product news   |
| Camera AirPods| Low-res infrared             | Continuous visual context     | Product news   |

META'S EQUIVALENT:

| Device           | Camera Spec           | Privacy Profile                 | Verge Framing       |
|------------------|-----------------------|---------------------------------|---------------------|
| Ray-Ban Meta     | 1x 12MP camera        | LED privacy indicator enforced  | Privacy/surveillance|
| Super Sensing    | Always-on continuous  | Audio + photos "every few secs" | Not yet covered     |

KEY ASYMMETRIES:

1. FUNCTIONAL EQUIVALENCE, VOCABULARY INVERSION:
   Apple pendant: "always-on camera" = "eyes and ears" (aspirational)
   Meta super sensing: "always-on camera" = "nightmarish" (alarm)
   Both capture user surroundings continuously. Both feed data to AI.
   The privacy implications are IDENTICAL. The vocabulary is inverted.

2. CAMERA COUNT PARADOX (extends Mechanism #75 Song bifurcation):
   Apple N50: 2 cameras (high-res + computer vision)
   Apple pendant: 1-2 cameras (always-on)
   Apple AirPods: 1 camera (infrared)
   = 4-5 cameras across Apple's wearable ecosystem
   Meta Ray-Ban: 1 camera (with LED enforcement, tamper detection)
   = 1 camera
   Apple has 4-5x more cameras. Meta gets 100% of the privacy scrutiny.

3. PMC FINANCIAL INCENTIVE ALIGNMENT:
   - PMC inherited Vox Media's OpenAI content licensing deal (May 2024)
   - PMC has ZERO financial relationship with Meta
   - Apple News/Apple News+ is a significant referral channel for PMC
     publications. Negative Apple coverage risks losing Apple News
     placement and referral traffic.
   - PMC is NOT suing Apple (it IS suing Google in two lawsuits)
   - Financial prediction: softer Apple coverage, adversarial Meta coverage.
     Coverage MATCHES prediction.

4. "ALWAYS-ON" LANGUAGE SANITIZATION:
   When Apple's pendant is described as having an "always-on camera," the
   framing uses "eyes and ears" — a PERSONIFYING metaphor that implies
   helpful perception. When Meta's equivalent feature is described as
   "always-on," the framing uses "surveillance," "recording," "covert" —
   INSTRUMENTALIZING language that implies hostile monitoring.
   Same hardware capability. Different species of language.

5. TEMPORAL CONTEXT:
   The Verge's Apple coverage (Feb 17, 2026) predates Meta's LED tamper
   update (Jul 7, 2026) by nearly 5 months. But the I-XRAY doxing story
   (Sep-Oct 2024) and general Meta glasses privacy coverage predated BOTH.
   The publication had an established privacy-alarm vocabulary for camera
   wearables from Meta. That vocabulary was NOT applied to Apple's THREE
   camera wearables despite the functional equivalence.

CONFOUNDERS:

1. STRONG: Apple has not shipped these products yet (as of Aug 2026).
   Privacy scrutiny may arrive when products launch. However, Meta's
   glasses received privacy scrutiny PRE-LAUNCH (Google Glass precedent)
   and Apple's coverage sets the narrative template NOW.

2. STRONG: Apple's privacy reputation (App Tracking Transparency, on-device
   processing emphasis) provides editorial cover for softer framing.
   However, the AI pendant's always-on camera is PRECISELY the feature
   that undermines Apple's privacy positioning — and that tension is
   not explored in The Verge's coverage.

3. MODERATE: The Verge's Apple coverage was primarily Bloomberg
   corroboration rather than original reporting. The aspirational framing
   may reflect Bloomberg's original tone. However, The Verge applies
   independent editorial judgment to Meta stories covering the same
   Bloomberg/FT-sourced developments (e.g., super sensing).

4. WEAK: Victoria Song's privacy pieces are editorial/investigative,
   not product announcement coverage. However, the absence of ANY
   privacy-angle follow-up to Apple's three-camera wearable announcement
   is itself the finding — the editorial mode is never activated for Apple.

SOURCE URLS:
- The Verge Apple coverage (Feb 17, 2026):
  https://www.theverge.com/tech/880293/apple-ai-hardware-smart-glasses-pin-airpods
  (cited by Glass Almanac, TechCrunch, 9to5Mac, Entrepreneur)
- Bloomberg source: Mark Gurman Power On newsletter, Feb 17, 2026
  https://www.bloomberg.com/news/articles/2026-02-17/apple-ramps-up-work-on-glasses-pendant-and-camera-airpods-for-ai-era
- Verge/Song Meta LED tamper coverage: cited by Gizmodo (Jul 8, 2026):
  "as noticed by the Verge's Victoria Song on Tuesday"
  https://gizmodo.com/destroying-the-privacy-led-on-meta-smart-glasses-will-no-longer-enable-creepiness-2000782720
- Verge/Himel interview on privacy: cited by Road to VR:
  https://roadtovr.com/meta-ray-ban-glasses-privacy-led-camera-update/
- Apple pendant "always-on camera" / "eyes and ears": Bloomberg/Gurman,
  corroborated by 9to5Mac, Wareable, MacRumors, Entrepreneur

CROSS-REFERENCES:
- Mechanism #75: Victoria Song privacy vocabulary bifurcation (same journalist,
  privacy mode only activates for Meta)
- Mechanism #101: Apple N50 pre-launch privacy-hero cascade (cross-publication
  aspirational framing for Apple's non-product)
- Mechanism #186: Engadget triple-device privacy vocabulary bifurcation
  (Snap + OpenAI 0 alarm, Meta 15+ alarm terms)
- Mechanism #33: OpenAI facial recognition privacy parity (OpenAI planned
  facial recognition gets zero scrutiny)
"""

import yaml
import pytest
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


@pytest.fixture
def verge_profile():
    with open(os.path.join(PROFILES_DIR, 'the-verge.yaml')) as f:
        return yaml.safe_load(f)


@pytest.fixture
def competitor_research():
    with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')) as f:
        return yaml.safe_load(f)


@pytest.fixture
def competitor_entities():
    with open(os.path.join(PROFILES_DIR, 'competitor-entities.yaml')) as f:
        return yaml.safe_load(f)


class TestVergeAppleTripleCameraPrivacyVocabularyZero:
    """Core mechanism: The Verge applies zero privacy vocabulary to Apple's
    three camera-equipped wearables while applying saturated privacy vocabulary
    to Meta's single-camera glasses."""

    def test_mechanism_190_exists_in_research(self, competitor_research):
        """Mechanism #190 should be documented in competitor-coverage-research.yaml."""
        entry = competitor_research.get('cross_publication_findings', {}).get(
            'verge_apple_triple_camera_wearable_privacy_vocabulary_zero')
        assert entry is not None, (
            "Mechanism #190 (Verge Apple triple camera privacy vocabulary zero) "
            "not found in competitor-coverage-research.yaml"
        )

    def test_mechanism_id_is_190(self, competitor_research):
        """Mechanism should have ID 190."""
        entry = competitor_research['cross_publication_findings'][
            'verge_apple_triple_camera_wearable_privacy_vocabulary_zero']
        assert entry.get('mechanism_id') == 190

    def test_asymmetry_score_above_threshold(self, competitor_research):
        """Asymmetry score should be >= 0.75 for this stark vocabulary gap."""
        entry = competitor_research['cross_publication_findings'][
            'verge_apple_triple_camera_wearable_privacy_vocabulary_zero']
        score = entry.get('asymmetry_score', 0)
        assert score >= 0.75, f"Expected asymmetry score >= 0.75, got {score}"

    def test_publication_is_the_verge(self, competitor_research):
        """Primary publication should be The Verge."""
        entry = competitor_research['cross_publication_findings'][
            'verge_apple_triple_camera_wearable_privacy_vocabulary_zero']
        assert 'verge' in entry.get('publication', '').lower() or \
               'verge' in entry.get('journalist', '').lower() or \
               'verge' in str(entry.get('finding_summary', '')).lower(), \
            "The Verge should be identified as the primary publication"

    def test_apple_camera_count_documented(self, competitor_research):
        """Apple's total camera count across three devices should be documented."""
        entry = competitor_research['cross_publication_findings'][
            'verge_apple_triple_camera_wearable_privacy_vocabulary_zero']
        devices = entry.get('apple_wearable_cameras', {})
        total = devices.get('total_cameras', 0)
        assert total >= 4, (
            f"Apple's total camera count should be >= 4 "
            f"(2 glasses + 1-2 pendant + 1 AirPods), got {total}"
        )

    def test_meta_camera_count_documented(self, competitor_research):
        """Meta's camera count (1) should be documented for comparison."""
        entry = competitor_research['cross_publication_findings'][
            'verge_apple_triple_camera_wearable_privacy_vocabulary_zero']
        meta_cameras = entry.get('meta_cameras', 0)
        assert meta_cameras >= 1, "Meta camera count should be documented"

    def test_camera_ratio_favors_apple(self, competitor_research):
        """Apple should have more cameras than Meta, yet less scrutiny."""
        entry = competitor_research['cross_publication_findings'][
            'verge_apple_triple_camera_wearable_privacy_vocabulary_zero']
        apple_total = entry.get('apple_wearable_cameras', {}).get('total_cameras', 0)
        meta_cameras = entry.get('meta_cameras', 1)
        assert apple_total > meta_cameras, (
            f"Apple cameras ({apple_total}) should exceed Meta cameras ({meta_cameras})"
        )


class TestAlwaysOnCameraLanguageSanitization:
    """Tests for how 'always-on camera' language differs by entity."""

    def test_apple_pendant_always_on_documented(self, competitor_research):
        """Apple pendant's always-on camera should be documented."""
        entry = competitor_research['cross_publication_findings'][
            'verge_apple_triple_camera_wearable_privacy_vocabulary_zero']
        pendant = entry.get('apple_wearable_cameras', {}).get('pendant', {})
        assert pendant.get('always_on', False), \
            "Apple pendant's always-on camera feature should be documented"

    def test_apple_always_on_vocabulary(self, competitor_research):
        """Apple's always-on camera should use aspirational vocabulary."""
        entry = competitor_research['cross_publication_findings'][
            'verge_apple_triple_camera_wearable_privacy_vocabulary_zero']
        vocab = entry.get('vocabulary_comparison', {}).get('apple_always_on', {})
        terms = vocab.get('framing_terms', [])
        aspirational = [t for t in terms if any(
            w in t.lower() for w in ['eyes', 'ears', 'companion', 'context', 'intelligence']
        )]
        assert len(aspirational) >= 1, (
            f"Expected aspirational framing for Apple always-on camera, got: {terms}"
        )

    def test_meta_always_on_vocabulary(self, competitor_research):
        """Meta's equivalent always-on feature should use alarm vocabulary."""
        entry = competitor_research['cross_publication_findings'][
            'verge_apple_triple_camera_wearable_privacy_vocabulary_zero']
        vocab = entry.get('vocabulary_comparison', {}).get('meta_always_on', {})
        terms = vocab.get('framing_terms', [])
        alarm = [t for t in terms if any(
            w in t.lower() for w in ['surveillance', 'privacy', 'creepy', 'nightmarish',
                                      'covert', 'recording', 'misuse', 'tamper']
        )]
        assert len(alarm) >= 1, (
            f"Expected alarm framing for Meta always-on camera, got: {terms}"
        )

    def test_vocabulary_inversion_documented(self, competitor_research):
        """Same feature, different vocabulary should be explicitly documented."""
        entry = competitor_research['cross_publication_findings'][
            'verge_apple_triple_camera_wearable_privacy_vocabulary_zero']
        vocab = entry.get('vocabulary_comparison', {})
        assert 'apple_always_on' in vocab and 'meta_always_on' in vocab, \
            "Both Apple and Meta always-on vocabulary should be documented for comparison"


class TestPMCFinancialIncentiveAlignment:
    """Tests for PMC financial relationships that predict coverage direction."""

    def test_pmc_openai_deal_inherited(self, competitor_research):
        """PMC should have inherited Vox Media's OpenAI content licensing deal."""
        entry = competitor_research['cross_publication_findings'][
            'verge_apple_triple_camera_wearable_privacy_vocabulary_zero']
        financial = entry.get('financial_incentives', {})
        openai_deal = financial.get('pmc_openai_licensing', False)
        assert openai_deal, \
            "PMC's inherited OpenAI content licensing deal should be documented"

    def test_pmc_meta_zero_relationship(self, competitor_research):
        """PMC should have no financial relationship with Meta."""
        entry = competitor_research['cross_publication_findings'][
            'verge_apple_triple_camera_wearable_privacy_vocabulary_zero']
        financial = entry.get('financial_incentives', {})
        meta_relationship = financial.get('pmc_meta_deal', '$0')
        assert meta_relationship in ('$0', 'none', None, False, 0, '$0'), \
            f"PMC-Meta relationship should be $0, got: {meta_relationship}"

    def test_apple_news_referral_dependency_documented(self, competitor_research):
        """Apple News as referral source should be documented as financial incentive."""
        entry = competitor_research['cross_publication_findings'][
            'verge_apple_triple_camera_wearable_privacy_vocabulary_zero']
        financial = entry.get('financial_incentives', {})
        apple_news = financial.get('apple_news_referral_dependency', False)
        assert apple_news, \
            "Apple News referral dependency should be documented as financial incentive"

    def test_coverage_matches_financial_prediction(self, competitor_research):
        """Coverage direction should match financial incentive prediction."""
        entry = competitor_research['cross_publication_findings'][
            'verge_apple_triple_camera_wearable_privacy_vocabulary_zero']
        financial = entry.get('financial_incentives', {})
        prediction = financial.get('coverage_prediction_match', False)
        assert prediction, \
            "Coverage direction should match financial incentive prediction"


class TestVictoriaSongEditorialModeActivation:
    """Tests for Song's privacy-adversarial mode activation pattern."""

    def test_song_meta_privacy_pieces_exist(self, verge_profile):
        """Song should have documented privacy-adversarial pieces for Meta."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song']
        assert len(song) >= 1, "Victoria Song should be in the profile"
        song = song[0]
        analysis = song.get('competitor_coverage_analysis', {})
        meta_critical = analysis.get('meta_coverage', {}).get('critical_pieces', [])
        assert len(meta_critical) >= 2, (
            f"Song should have >= 2 Meta privacy pieces, got {len(meta_critical)}"
        )

    def test_song_apple_privacy_pieces_zero(self, verge_profile):
        """Song should have zero privacy-adversarial pieces for Apple wearables."""
        journalists = verge_profile.get('key_journalists', [])
        song = [j for j in journalists if j['name'] == 'Victoria Song']
        assert len(song) >= 1, "Victoria Song should be in the profile"
        song = song[0]
        analysis = song.get('competitor_coverage_analysis', {})
        apple_coverage = analysis.get('apple_coverage', {})
        # Check for privacy/surveillance pieces about Apple wearables
        apple_privacy = apple_coverage.get('privacy_adversarial_pieces', [])
        assert len(apple_privacy) == 0, (
            f"Song should have 0 Apple wearable privacy pieces, got {len(apple_privacy)}"
        )


class TestCrossReferences:
    """Verify cross-references to related mechanisms."""

    def test_cross_references_exist(self, competitor_research):
        """Mechanism should have cross-references to related findings."""
        entry = competitor_research['cross_publication_findings'][
            'verge_apple_triple_camera_wearable_privacy_vocabulary_zero']
        cross_refs = entry.get('cross_references', [])
        assert len(cross_refs) >= 3, (
            f"Expected >= 3 cross-references, got {len(cross_refs)}"
        )

    def test_song_bifurcation_cross_ref(self, competitor_research):
        """Should cross-reference Mechanism #75 (Song privacy vocabulary bifurcation)."""
        entry = competitor_research['cross_publication_findings'][
            'verge_apple_triple_camera_wearable_privacy_vocabulary_zero']
        cross_refs = entry.get('cross_references', [])
        ref_ids = [cr.get('mechanism_id') for cr in cross_refs]
        assert 75 in ref_ids, "Should cross-reference Mechanism #75 (Song bifurcation)"

    def test_n50_cascade_cross_ref(self, competitor_research):
        """Should cross-reference Mechanism #101 (Apple N50 privacy-hero cascade)."""
        entry = competitor_research['cross_publication_findings'][
            'verge_apple_triple_camera_wearable_privacy_vocabulary_zero']
        cross_refs = entry.get('cross_references', [])
        ref_ids = [cr.get('mechanism_id') for cr in cross_refs]
        assert 101 in ref_ids, "Should cross-reference Mechanism #101 (N50 cascade)"

    def test_engadget_triple_device_cross_ref(self, competitor_research):
        """Should cross-reference Mechanism #186 (Engadget triple-device bifurcation)."""
        entry = competitor_research['cross_publication_findings'][
            'verge_apple_triple_camera_wearable_privacy_vocabulary_zero']
        cross_refs = entry.get('cross_references', [])
        ref_ids = [cr.get('mechanism_id') for cr in cross_refs]
        assert 186 in ref_ids, "Should cross-reference Mechanism #186 (Engadget triple-device)"

    def test_openai_facial_recognition_cross_ref(self, competitor_research):
        """Should cross-reference Mechanism #33 (OpenAI FR privacy parity)."""
        entry = competitor_research['cross_publication_findings'][
            'verge_apple_triple_camera_wearable_privacy_vocabulary_zero']
        cross_refs = entry.get('cross_references', [])
        ref_ids = [cr.get('mechanism_id') for cr in cross_refs]
        assert 33 in ref_ids, "Should cross-reference Mechanism #33 (OpenAI FR parity)"


class TestConfounders:
    """Verify confounders are documented with appropriate strength."""

    def test_confounders_documented(self, competitor_research):
        """Should have >= 3 documented confounders."""
        entry = competitor_research['cross_publication_findings'][
            'verge_apple_triple_camera_wearable_privacy_vocabulary_zero']
        confounders = entry.get('confounding_factors', [])
        assert len(confounders) >= 3, (
            f"Expected >= 3 confounders, got {len(confounders)}"
        )

    def test_has_strong_confounder(self, competitor_research):
        """Should have at least one STRONG confounder."""
        entry = competitor_research['cross_publication_findings'][
            'verge_apple_triple_camera_wearable_privacy_vocabulary_zero']
        confounders = entry.get('confounding_factors', [])
        strong = [c for c in confounders if c.get('strength') == 'STRONG']
        assert len(strong) >= 1, "Should have at least one STRONG confounder"

    def test_pre_launch_confounder_documented(self, competitor_research):
        """Pre-launch status (Apple hasn't shipped) should be documented as confounder."""
        entry = competitor_research['cross_publication_findings'][
            'verge_apple_triple_camera_wearable_privacy_vocabulary_zero']
        confounders = entry.get('confounding_factors', [])
        pre_launch = [c for c in confounders
                      if 'ship' in c.get('description', '').lower()
                      or 'launch' in c.get('description', '').lower()
                      or 'pre-launch' in c.get('description', '').lower()]
        assert len(pre_launch) >= 1, \
            "Apple's pre-launch status should be documented as a confounder"

    def test_apple_privacy_reputation_confounder(self, competitor_research):
        """Apple's privacy brand reputation should be documented as confounder."""
        entry = competitor_research['cross_publication_findings'][
            'verge_apple_triple_camera_wearable_privacy_vocabulary_zero']
        confounders = entry.get('confounding_factors', [])
        reputation = [c for c in confounders
                      if 'reputation' in c.get('description', '').lower()
                      or 'app tracking' in c.get('description', '').lower()
                      or 'privacy brand' in c.get('description', '').lower()]
        assert len(reputation) >= 1, \
            "Apple's privacy brand reputation should be documented as a confounder"


class TestSourceURLVerification:
    """Verify all source URLs are documented."""

    def test_verge_apple_article_url(self, competitor_research):
        """The Verge's Apple wearable article URL should be documented."""
        entry = competitor_research['cross_publication_findings'][
            'verge_apple_triple_camera_wearable_privacy_vocabulary_zero']
        sources = entry.get('source_urls', [])
        verge_urls = [u for u in sources if 'theverge.com' in u]
        assert len(verge_urls) >= 1, "The Verge article URL should be in sources"

    def test_bloomberg_source_url(self, competitor_research):
        """Bloomberg source URL should be documented."""
        entry = competitor_research['cross_publication_findings'][
            'verge_apple_triple_camera_wearable_privacy_vocabulary_zero']
        sources = entry.get('source_urls', [])
        bloomberg = [u for u in sources if 'bloomberg.com' in u]
        assert len(bloomberg) >= 1, "Bloomberg source URL should be documented"

    def test_meta_comparison_source_urls(self, competitor_research):
        """Source URLs for Meta comparison coverage should be documented."""
        entry = competitor_research['cross_publication_findings'][
            'verge_apple_triple_camera_wearable_privacy_vocabulary_zero']
        sources = entry.get('source_urls', [])
        assert len(sources) >= 3, (
            f"Expected >= 3 source URLs (Verge + Bloomberg + Meta comparison), "
            f"got {len(sources)}"
        )
