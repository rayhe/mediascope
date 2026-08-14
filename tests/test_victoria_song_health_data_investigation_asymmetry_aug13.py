"""
Victoria Song Health Data Privacy Investigation Asymmetry — Mechanism #90
Type B: Journalist Cross-Entity Tracking — Thu Aug 13, 2026 20:00 PT
Iteration #92

THESIS: Victoria Song (The Verge) writes standalone privacy investigations
about Meta's smart glasses camera data practices but published ZERO coverage
of Samsung Health's July 2026 AI training data coercion — despite being
The Verge's primary reviewer of Samsung wearable health products (Galaxy
Watch, Galaxy Ring, Galaxy Watch Ultra).

KEY COMPARISON:
  Meta glasses camera data:
    - Song wrote standalone doxing investigation (Oct 2024): "College students
      used Meta's smart glasses to dox people in real time" — "eerie,"
      "unsettling," "privacy nightmare"
    - Song covered LED tamper-proof update (Jul 7, 2026): dedicated article
      about Meta's proactive response to privacy light circumvention
    - Song questioned smart glasses in bedrooms (Vergecast Jul 2025):
      dedicated discussion about Meta glasses privacy in intimate spaces
    - Song reviewed Meta AI subscription (Jul 2026): "Live AI is a solution
      looking for a problem" — questioning Meta's data value extraction
    Privacy vocabulary density: 8+ surveillance/privacy terms across pieces

  Samsung Health AI data coercion (Jul 13-14, 2026):
    - Samsung Health app forced users to consent to health data use for AI
      training and modeling, INCLUDING human review
    - Data categories: menstrual cycle tracking, medication records (prescriptions
      and dosages), full health records (diagnoses, test results), sleep data,
      body measurements, biological aging indicators, body fat %, heart rate
      variability, skin temperature, blood oxygen
    - Opt-out threatened to DELETE all synced health data AND disable cloud sync
    - Samsung later clarified/walked back the threat (Jul 15-16)
    - Story covered by: Digital Trends, Android Authority, 9to5Google, GSMArena,
      SamMobile, How-To Geek, Cybernews
    - Victoria Song coverage: ZERO
    - The Verge coverage: ZERO
    - WIRED coverage: ZERO
    - NYT coverage: ZERO

PRIVACY SEVERITY GRADIENT:
  Samsung Health data (menstrual cycles, medication, diagnoses) is categorized
  as SENSITIVE health data under GDPR Art. 9, HIPAA, and most US state privacy
  laws — a HIGHER sensitivity tier than Meta's camera photos/videos. Post-Dobbs,
  menstrual cycle data has explicit political salience. Samsung's coercion
  model (consent or lose your data) is MORE aggressive than Meta's opt-in
  AI training, which preserves data regardless of consent choice.

SONG'S SAMSUNG HEALTH EXPERTISE:
  Victoria Song reviews Samsung Galaxy Watch and Galaxy Ring health features
  at The Verge. She publishes "Optimizer," a weekly Verge newsletter covering
  wearable health tech. She tested Galaxy Watch 7 health metrics, Galaxy Ring
  sleep/cycle tracking, and Galaxy Watch Ultra fitness features. She is the
  MOST natural reporter at The Verge to cover Samsung Health data practices.

FINANCIAL CONTEXT:
  - Vox Media (The Verge parent) depends on Google programmatic advertising
  - Samsung is the 4th-largest global advertiser (~$9.7B/yr measured media)
  - Samsung's glasses run Google's Android XR + Gemini AI
  - Meta has $0 content/advertising deals with The Verge/Vox Media
  - Covering Samsung Health adversarially risks alienating two major revenue
    sources simultaneously (Samsung ad spend + Google platform partner)

EXTENDS: Mechanism #75 (Song privacy vocabulary bifurcation), #81 (Samsung
Unpacked beat assignment paradox), #76 (Samsung-Google compound leverage)

CONFOUNDING FACTORS (4):
  1. MODERATE: Samsung clarified within 48 hours that only AI-specific data
     would be deleted, reducing the story's severity window
  2. WEAK: The story broke on a weekend (Jul 13 is Sunday in 2026) — but
     follow-up articles published Mon-Wed were also absent from The Verge
  3. WEAK: Song may have been on vacation/assignment the week of Jul 13
  4. WEAK: The Verge may consider Samsung Health a "phone" story, not a
     "wearables" story — but Galaxy Watch and Galaxy Ring sync through
     Samsung Health, making it directly relevant to Song's beat

Sources:
  - Digital Trends (Jul 14, 2026): Samsung Health threatens to delete data
    https://www.digitaltrends.com/phones/samsung-health-threatens-to-delete-your-data-if-you-opt-out-of-ai-training/
  - Android Authority (Jul 13, 2026): Samsung Health AI training consent
    https://www.androidauthority.com/samsung-health-train-ai-data-3686684/
  - 9to5Google (Jul 15, 2026): Samsung Health will delete data without consent
    https://9to5google.com/2026/07/15/samsung-health-ai-training-data-consent/
  - Digital Trends (Jul 16, 2026): Samsung clarification
    https://www.digitaltrends.com/phones/refusing-samsung-health-ai-training-will-not-wipe-your-health-history-after-all/
  - GSMArena: Samsung Health data AI training consent
    https://www.gsmarena.com/samsung_health_data_ai_training_consent-news-73683.php
  - SamMobile: Samsung Health data deletion
    https://www.sammobile.com/news/samsung-health-data-deleted-dont-consent-use-ai-training/
  - TechTimes (May 20, 2026): Samsung+Google glasses no data policy disclosed
    https://www.techtimes.com/articles/316904/20260520/samsung-google-reveal-gemini-smart-glasses-fall-2026-launch-ios-support-no-data-policy-disclosed.htm
  - Samsung Galaxy Unpacked YouTube (The Verge channel, Jul 22, 2026):
    https://www.youtube.com/watch?v=c-MWq-DFTwo
  - Victoria Song doxing piece (Oct 2024, via Techmeme):
    https://vuink.com/post/guriretr-d-dpbz/2024/10/2/24260262/ray-ban-meta-smart-glasses-doxxing-privacy
  - Victoria Song LED tamper piece (Jul 7, 2026, via Techmeme):
    https://www.techmeme.com/260707/p41
"""

import pytest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_verge_profile():
    with open(os.path.join(PROFILES_DIR, 'the-verge.yaml')) as f:
        return yaml.safe_load(f)


def load_competitor_research():
    with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')) as f:
        return yaml.safe_load(f)


def load_competitor_entities():
    with open(os.path.join(PROFILES_DIR, 'competitor-entities.yaml')) as f:
        return yaml.safe_load(f)


def get_song_profile(verge_profile):
    journalists = verge_profile.get('key_journalists', [])
    song_list = [j for j in journalists if j.get('name') == 'Victoria Song']
    assert len(song_list) == 1, "Victoria Song should appear exactly once"
    return song_list[0]


def get_song_health_gap(verge_profile):
    song = get_song_profile(verge_profile)
    analysis = song.get('competitor_coverage_analysis', {})
    return analysis.get('samsung_health_data_investigation_gap', {})


def get_mechanism_90(research):
    """Find mechanism #90 anywhere in the YAML structure."""
    def find(d, target_id):
        if isinstance(d, dict):
            if d.get('mechanism_id') == target_id:
                return d
            for v in d.values():
                result = find(v, target_id)
                if result:
                    return result
        elif isinstance(d, list):
            for item in d:
                result = find(item, target_id)
                if result:
                    return result
        return None
    return find(research, 90)


class TestMechanism90ExistsInResearch:
    """Mechanism #90 should be documented in competitor-coverage-research.yaml."""

    def test_mechanism_90_exists(self):
        research = load_competitor_research()
        m90 = get_mechanism_90(research)
        assert m90 is not None, "Mechanism #90 should exist"

    def test_mechanism_90_type_b(self):
        research = load_competitor_research()
        m90 = get_mechanism_90(research)
        assert m90.get('type') == 'B', f"Expected type B, got {m90.get('type')}"

    def test_mechanism_90_journalist_is_victoria_song(self):
        research = load_competitor_research()
        m90 = get_mechanism_90(research)
        assert 'Victoria Song' in m90.get('journalist', ''), \
            f"Expected Victoria Song, got {m90.get('journalist')}"

    def test_mechanism_90_publication_is_verge(self):
        research = load_competitor_research()
        m90 = get_mechanism_90(research)
        pub = m90.get('publication', '')
        assert 'Verge' in pub, f"Expected The Verge, got {pub}"

    def test_mechanism_90_has_confounding_factors(self):
        research = load_competitor_research()
        m90 = get_mechanism_90(research)
        factors = m90.get('confounding_factors', [])
        assert len(factors) >= 3, f"Expected >= 3 confounding factors, got {len(factors)}"

    def test_mechanism_90_has_sources(self):
        research = load_competitor_research()
        m90 = get_mechanism_90(research)
        sources = m90.get('source_urls', [])
        assert len(sources) >= 4, f"Expected >= 4 source URLs, got {len(sources)}"


class TestSongMetaPrivacyPiecesDocumented:
    """Victoria Song's Meta privacy pieces should be documented in the-verge.yaml."""

    def test_song_has_meta_privacy_pieces(self):
        verge = load_verge_profile()
        song = get_song_profile(verge)
        analysis = song.get('competitor_coverage_analysis', {})
        bifurcation = analysis.get('privacy_vocabulary_bifurcation', {})
        meta_pieces = bifurcation.get('meta_privacy_pieces', [])
        assert len(meta_pieces) >= 2, (
            f"Found {len(meta_pieces)} Meta privacy pieces, expected >= 2"
        )

    def test_meta_doxing_piece_has_surveillance_vocabulary(self):
        verge = load_verge_profile()
        song = get_song_profile(verge)
        analysis = song.get('competitor_coverage_analysis', {})
        bifurcation = analysis.get('privacy_vocabulary_bifurcation', {})
        meta_pieces = bifurcation.get('meta_privacy_pieces', [])
        doxing_pieces = [p for p in meta_pieces
                         if 'dox' in p.get('title', '').lower()]
        assert len(doxing_pieces) >= 1, "Doxing investigation should be documented"
        doxing = doxing_pieces[0]
        framing = doxing.get('framing', '').lower()
        alarm_terms = ['eerie', 'unsettling', 'privacy nightmare',
                       'chilling', 'dox', 'surveillance']
        found = [t for t in alarm_terms if t in framing]
        assert len(found) >= 2, (
            f"Expected >= 2 alarm terms in doxing piece, found {found}"
        )

    def test_meta_led_tamper_piece_documented(self):
        verge = load_verge_profile()
        song = get_song_profile(verge)
        analysis = song.get('competitor_coverage_analysis', {})
        bifurcation = analysis.get('privacy_vocabulary_bifurcation', {})
        meta_pieces = bifurcation.get('meta_privacy_pieces', [])
        led_pieces = [p for p in meta_pieces
                      if 'tamper' in p.get('title', '').lower()
                      or 'privacy light' in p.get('title', '').lower()
                      or 'turn off' in p.get('title', '').lower()]
        assert len(led_pieces) >= 1, "LED tamper-proof piece should be documented"


class TestSamsungHealthDataCoercionDocumented:
    """Samsung Health AI training data coercion should be documented."""

    def test_samsung_health_coercion_in_verge_profile(self):
        verge = load_verge_profile()
        health_gap = get_song_health_gap(verge)
        assert health_gap, "Samsung Health investigation gap should be documented"

    def test_samsung_health_coercion_event_date(self):
        verge = load_verge_profile()
        health_gap = get_song_health_gap(verge)
        event = health_gap.get('event', {})
        date = event.get('date', '')
        assert '2026-07' in date, f"Expected Jul 2026 date, got {date}"

    def test_samsung_health_data_categories_documented(self):
        verge = load_verge_profile()
        health_gap = get_song_health_gap(verge)
        categories = health_gap.get('data_categories', [])
        assert len(categories) >= 5, (
            f"Expected >= 5 data categories, got {len(categories)}"
        )
        cats_text = ' '.join(c.lower() for c in categories)
        assert 'menstrual' in cats_text or 'cycle' in cats_text, \
            "Menstrual cycle data should be listed"
        assert 'medication' in cats_text, "Medication data should be listed"

    def test_samsung_health_coercion_mechanism(self):
        verge = load_verge_profile()
        health_gap = get_song_health_gap(verge)
        coercion = health_gap.get('coercion_description', '')
        assert 'delete' in coercion.lower() or 'deletion' in coercion.lower(), \
            "Data deletion threat should be described"

    def test_samsung_health_song_coverage_count_zero(self):
        verge = load_verge_profile()
        health_gap = get_song_health_gap(verge)
        song_coverage = health_gap.get('song_articles_count', -1)
        assert song_coverage == 0, (
            f"Expected 0 Song articles on Samsung Health coercion, got {song_coverage}"
        )

    def test_verge_coverage_count_zero(self):
        verge = load_verge_profile()
        health_gap = get_song_health_gap(verge)
        verge_total = health_gap.get('verge_total_articles', -1)
        assert verge_total == 0, (
            f"Expected 0 Verge articles on Samsung Health coercion, got {verge_total}"
        )


class TestCoverageComparisonWithOtherPublications:
    """Publications WITHOUT financial ties covered the Samsung Health story."""

    def test_samsung_health_covered_by_independent_outlets(self):
        verge = load_verge_profile()
        health_gap = get_song_health_gap(verge)
        covered_by = health_gap.get('publications_that_covered', [])
        assert len(covered_by) >= 4, (
            f"Expected >= 4 outlets that covered the story, got {len(covered_by)}"
        )

    def test_digital_trends_covered(self):
        verge = load_verge_profile()
        health_gap = get_song_health_gap(verge)
        covered_by = health_gap.get('publications_that_covered', [])
        names = [c.get('name', '') if isinstance(c, dict) else c for c in covered_by]
        dt = [n for n in names if 'digital trends' in n.lower()]
        assert len(dt) >= 1, "Digital Trends should be listed"

    def test_android_authority_covered(self):
        verge = load_verge_profile()
        health_gap = get_song_health_gap(verge)
        covered_by = health_gap.get('publications_that_covered', [])
        names = [c.get('name', '') if isinstance(c, dict) else c for c in covered_by]
        aa = [n for n in names if 'android authority' in n.lower()]
        assert len(aa) >= 1, "Android Authority should be listed"


class TestPrivacySeverityGradient:
    """Health data is a higher sensitivity tier than camera photos."""

    def test_health_data_sensitivity_documented(self):
        verge = load_verge_profile()
        health_gap = get_song_health_gap(verge)
        severity = health_gap.get('privacy_severity_comparison', {})
        assert severity, "Privacy severity comparison should be documented"

    def test_samsung_coercion_more_aggressive_than_meta(self):
        verge = load_verge_profile()
        health_gap = get_song_health_gap(verge)
        severity = health_gap.get('privacy_severity_comparison', {})
        samsung_level = severity.get('samsung_aggressiveness', '')
        assert samsung_level, "Samsung aggressiveness level should be documented"

    def test_regulatory_sensitivity_category(self):
        verge = load_verge_profile()
        health_gap = get_song_health_gap(verge)
        severity = health_gap.get('privacy_severity_comparison', {})
        regulations = severity.get('applicable_regulations', [])
        assert len(regulations) >= 1, "At least one regulation should be listed"


class TestSongSamsungWearablesExpertise:
    """Song reviews Samsung wearable health products — she's the natural reporter."""

    def test_song_reviews_samsung_galaxy_watch(self):
        verge = load_verge_profile()
        health_gap = get_song_health_gap(verge)
        expertise = health_gap.get('song_samsung_health_expertise', {})
        products = expertise.get('products_reviewed', [])
        watch = [p for p in products if 'watch' in p.lower()]
        assert len(watch) >= 1, "Song should be documented reviewing Galaxy Watch"

    def test_song_reviews_samsung_galaxy_ring(self):
        verge = load_verge_profile()
        health_gap = get_song_health_gap(verge)
        expertise = health_gap.get('song_samsung_health_expertise', {})
        products = expertise.get('products_reviewed', [])
        ring = [p for p in products if 'ring' in p.lower()]
        assert len(ring) >= 1, "Song should be documented reviewing Galaxy Ring"

    def test_song_writes_optimizer_newsletter(self):
        verge = load_verge_profile()
        health_gap = get_song_health_gap(verge)
        expertise = health_gap.get('song_samsung_health_expertise', {})
        newsletter = expertise.get('newsletter', '')
        assert 'optimizer' in newsletter.lower(), \
            "Optimizer newsletter should be documented"


class TestMultiPublicationSilence:
    """WIRED and NYT also had zero coverage of Samsung Health coercion."""

    def test_wired_zero_coverage_documented(self):
        research = load_competitor_research()
        m90 = get_mechanism_90(research)
        multi = m90.get('multi_publication_silence', {})
        wired = multi.get('wired_coverage_count', -1)
        assert wired == 0, f"Expected 0 WIRED articles, got {wired}"

    def test_nyt_zero_coverage_documented(self):
        research = load_competitor_research()
        m90 = get_mechanism_90(research)
        multi = m90.get('multi_publication_silence', {})
        nyt = multi.get('nyt_coverage_count', -1)
        assert nyt == 0, f"Expected 0 NYT articles, got {nyt}"

    def test_all_adversarial_publications_missed_story(self):
        research = load_competitor_research()
        m90 = get_mechanism_90(research)
        multi = m90.get('multi_publication_silence', {})
        total = (multi.get('verge_coverage_count', 0) +
                 multi.get('wired_coverage_count', 0) +
                 multi.get('nyt_coverage_count', 0))
        assert total == 0, (
            f"Expected 0 total articles across Verge+WIRED+NYT, got {total}"
        )


class TestFinancialContext:
    """Financial incentives align with coverage silence."""

    def test_samsung_ad_spend_documented(self):
        research = load_competitor_research()
        m90 = get_mechanism_90(research)
        financial = m90.get('financial_context', {})
        samsung_spend = financial.get('samsung_global_ad_spend_billions', 0)
        assert samsung_spend >= 9, (
            f"Expected Samsung ad spend >= $9B, got {samsung_spend}"
        )

    def test_google_dependency_documented(self):
        research = load_competitor_research()
        m90 = get_mechanism_90(research)
        financial = m90.get('financial_context', {})
        google_dep = financial.get('vox_media_google_ad_dependency', False)
        assert google_dep is True, "Vox Media Google ad dependency should be True"

    def test_meta_zero_deals_documented(self):
        research = load_competitor_research()
        m90 = get_mechanism_90(research)
        financial = m90.get('financial_context', {})
        meta_deals = financial.get('meta_verge_deals_count', -1)
        assert meta_deals == 0, f"Expected 0 Meta-Verge deals, got {meta_deals}"


class TestCrossReferences:
    """Mechanism #90 should cross-reference related mechanisms."""

    def test_cross_references_mechanism_75(self):
        research = load_competitor_research()
        m90 = get_mechanism_90(research)
        xrefs = m90.get('cross_references', [])
        assert 75 in xrefs, "Should cross-reference mechanism #75"

    def test_cross_references_mechanism_81(self):
        research = load_competitor_research()
        m90 = get_mechanism_90(research)
        xrefs = m90.get('cross_references', [])
        assert 81 in xrefs, "Should cross-reference mechanism #81"

    def test_cross_references_mechanism_76(self):
        research = load_competitor_research()
        m90 = get_mechanism_90(research)
        xrefs = m90.get('cross_references', [])
        assert 76 in xrefs, "Should cross-reference mechanism #76"
