"""
Test Mechanism #102: Adrienne So (WIRED) — Wearables Privacy Vocabulary
Bifurcation Across Entities

Type B: Journalist Cross-Entity Tracking — August 14, 2026

KEY FINDING: Adrienne So, WIRED's primary wearables reviewer (smartwatches,
fitness trackers, smart glasses), applies ENTITY-SELECTIVE privacy vocabulary
when reviewing structurally identical product categories. In her Oakley Meta
Vanguard review (Oct 21, 2025), she inserts an explicit parenthetical attack
— "(which are garbage)" — about Meta's AI and privacy policies within a
PRODUCT REVIEW of fitness glasses. When reviewing Google's Pixel Watch 4
(Oct 8, 2025), which collects identical categories of sensitive data (health,
fitness, location, biometrics), she writes ZERO privacy caveats about Google's
data practices. The Pixel Watch 4 review headline — "Surprisingly Close"
(to Apple Watch Ultra 3) — actively elevates Google's competitive position.

This establishes a WEARABLES-SPECIFIC instance of the privacy vocabulary
bifurcation pattern already documented for WIRED's smart glasses/tech
reporters (Chokkattu #93/#91, Ashworth #73/#87, Rogers #97). Adrienne So
covers the FITNESS wearables lane, meaning the bifurcation extends across
WIRED's entire wearables editorial team, not just the tech/glasses beat.

ENTITY-SPECIFIC FRAMING EVIDENCE:

Meta (Oakley Meta Vanguard, Oct 21, 2025):
- Parenthetical: "Whatever you may think of Meta's AI and privacy policies
  (which are garbage)"
- Inserted into a PRODUCT REVIEW, not an editorial or opinion piece
- Camera specs foregrounded in Techmeme headline as limitation: "camera
  specs aren't too impressive"
- Despite body text being substantially positive ("sound amazing," "might
  just replace your action cam," "I can't wait to take the Vanguards out
  snowboarding this year")

Google (Pixel Watch 4, Oct 8, 2025):
- Headline: "Surprisingly Close" (to Apple Watch Ultra 3) — promotional frame
- Zero privacy caveats about Google Health Connect data collection
- Zero parenthetical commentary on Google's advertising business model
- Zero mention of Google's documented history of health data controversies
  (Project Nightingale/Ascension 2019, Fitbit acquisition FTC concerns 2021)
- "Fitbit is still one of the best fitness platforms available and Google's
  integration with it is virtually perfect" — frictionless praise
- Pixel Watch 3 running features assessment: critical of training algorithms
  ("which wasn't great") but NEVER frames this as a privacy or data concern

Apple (Apple Watch Series 10, 2024-2025):
- Rated 8/10 WIRED Recommends
- Standard positive review language, no privacy caveats

STRUCTURAL SIGNIFICANCE:
Adrienne So's beat (fitness/wearables) handles products that collect some of
the MOST sensitive user data — heart rate, blood oxygen, sleep stages,
menstrual cycles, GPS tracks, body composition. Google's Pixel Watch feeds
this directly into Google's advertising ecosystem via Fitbit/Google Health
Connect. Meta's Oakley Vanguard is a CAMERA product with NO biometric health
sensors. Yet So applies privacy alarm vocabulary ONLY to Meta.

FINANCIAL CONTEXT:
WIRED (Condé Nast/Advance) has documented financial relationships with Google:
- Google News Showcase payments (mechanism #17)
- Google advertising revenue dependency (mechanism #22)
- Google News Initiative participation
No equivalent Meta financial relationship exists.

CONFOUNDING FACTORS:
1. STRONG: Meta has a genuinely worse privacy reputation from Cambridge Analytica,
   Facebook Papers, etc. — this is a real prior that justifies some differential.
2. MODERATE: The Oakley Vanguard has a camera (more visible privacy surface area
   than a watch), though the parenthetical attacks Meta's "AI and privacy policies"
   broadly, not the camera specifically.
3. MODERATE: Google's Pixel Watch is primarily a health/fitness product where
   privacy context is less expected by readers.
4. WEAK: Different product categories may invite different editorial framings.
5. WEAK: So may have personal Meta-specific negative experiences.

TESTABLE PREDICTIONS:
1. If Adrienne So reviews Samsung/Google smart glasses (which have cameras
   identical to Meta's), she will NOT insert equivalent privacy parentheticals.
2. If a Google wearable faces a data breach or privacy controversy, So's
   coverage will use euphemistic/passive language compared to active/accusatory
   language for equivalent Meta incidents.
3. Future WIRED wearable roundups by So will position Google products without
   privacy caveats that accompany Meta products in the same list.

CROSS-REFERENCES:
- Mechanism #93: Samsung-WIRED same-chip privacy presupposition (Chokkattu)
- Mechanism #91: Chokkattu Samsung coverage selection gap
- Mechanism #73: Ashworth category headline Meta substance
- Mechanism #87: Boone Ashworth cross-entity framing
- Mechanism #97: Reece Rogers privacy investigation topic routing asymmetry
- Mechanism #75: Victoria Song privacy vocabulary bifurcation
- Mechanism #17: Google News Showcase financial relationship
- Mechanism #22: Google advertising dependency

Sources:
- WIRED Oakley Meta Vanguard review by Adrienne So (Oct 21, 2025):
  https://www.techmeme.com/251021/p19 (Techmeme entry with headline framing)
- WIRED best Garmin watch guide (reference to Vanguard integration):
  https://web.archive.org/web/20260328113528/https://www.wired.com/story/best-garmin-watch/
- WIRED gift guide excerpt with "(which are garbage)" parenthetical:
  via CBInsights syndication of WIRED content
- WIRED Pixel Watch 4 vs Apple Watch Ultra 3 by Adrienne So (Oct 8, 2025):
  via TechNewsTube syndication
- WIRED best sleep trackers 2026 (Adrienne So contributor references):
  https://web.archive.org/web/20260601130916/https://www.wired.com/story/best-sleep-trackers/
- Julian Chokkattu Pixel Watch 3 review referencing Adrienne So's running
  feature experience: via WIRED, Aug 2024
- Google Project Nightingale/Ascension health data controversy (2019):
  https://www.wsj.com/articles/google-s-secret-project-nightingale-gathers-personal-health-data-on-millions-of-americans-11573496790
- Fitbit acquisition FTC antitrust concerns (2021):
  https://www.ftc.gov/legal-library/browse/cases-proceedings/public-statements/statement-chair-lina-khan-joined-commissioner-slaughter-regarding-googles-acquisition-fitbit
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_competitor_research():
    with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')) as f:
        return yaml.safe_load(f)


def load_journalists():
    with open(os.path.join(PROFILES_DIR, 'careers', 'journalists.yaml')) as f:
        return yaml.safe_load(f)


def load_wired_profile():
    with open(os.path.join(PROFILES_DIR, 'wired.yaml')) as f:
        return yaml.safe_load(f)


def get_so_profile(data):
    for j in data.get('journalists', []):
        if j.get('name') == 'Adrienne So':
            return j
    return None


def find_mechanism(research, mechanism_id):
    """Find mechanism by ID across all publications and cross-publication findings."""
    candidates = []

    # Check publications
    for pub_key, pub_val in research.items():
        if isinstance(pub_val, dict):
            for mech in pub_val.get('competitor_coverage_mechanisms', []):
                if isinstance(mech, dict) and mech.get('mechanism_id') == mechanism_id:
                    candidates.append(mech)

    # Check cross-publication findings
    cpf = research.get('cross_publication_findings', {})
    if isinstance(cpf, dict):
        for key, val in cpf.items():
            if isinstance(val, dict) and val.get('mechanism_id') == mechanism_id:
                candidates.append(val)

    # Return the most complete entry (most keys)
    if candidates:
        return max(candidates, key=lambda x: len(x))
    return None


# ===================================================================
# Test Class 1: Adrienne So Profile Exists in Journalist Database
# ===================================================================
class TestSoProfileExists:
    """Adrienne So must exist in journalists.yaml with wearables beat data."""

    def test_so_exists(self):
        data = load_journalists()
        profile = get_so_profile(data)
        assert profile is not None, "Adrienne So must exist in journalists.yaml"

    def test_so_publication_is_wired(self):
        data = load_journalists()
        profile = get_so_profile(data)
        assert profile is not None
        pubs = profile.get('publications', [])
        pub_names = [p.get('name', '') if isinstance(p, dict) else p for p in pubs]
        assert any('WIRED' in str(p).upper() or 'WIRED' in str(p) for p in pub_names), \
            "Adrienne So must be associated with WIRED"

    def test_so_has_wearables_beat(self):
        data = load_journalists()
        profile = get_so_profile(data)
        assert profile is not None
        beats = profile.get('beats', [])
        beat_str = ' '.join(str(b) for b in beats).lower()
        assert any(term in beat_str for term in ['wearable', 'fitness', 'smartwatch', 'watch']), \
            "Adrienne So must have wearables/fitness beat designation"

    def test_so_has_meta_coverage_section(self):
        data = load_journalists()
        profile = get_so_profile(data)
        assert profile is not None
        assert profile.get('meta_coverage') is not None, \
            "Adrienne So must have meta_coverage section"

    def test_so_has_google_coverage_section(self):
        data = load_journalists()
        profile = get_so_profile(data)
        assert profile is not None
        assert profile.get('google_coverage') is not None, \
            "Adrienne So must have google_coverage section"


# ===================================================================
# Test Class 2: Privacy Vocabulary Bifurcation Evidence
# ===================================================================
class TestPrivacyVocabularyBifurcation:
    """The core finding: entity-selective privacy vocabulary in product reviews."""

    def test_meta_coverage_has_privacy_parenthetical(self):
        """Meta Oakley Vanguard review contains explicit privacy attack."""
        data = load_journalists()
        profile = get_so_profile(data)
        assert profile is not None
        meta_coverage = profile.get('meta_coverage', [])
        vanguard_entries = [e for e in meta_coverage
                          if isinstance(e, dict) and
                          'vanguard' in str(e.get('title', '')).lower()]
        assert len(vanguard_entries) >= 1, \
            "Must have Oakley Meta Vanguard coverage entry"

        vanguard = vanguard_entries[0]
        notes = str(vanguard.get('notes', '')) + str(vanguard.get('privacy_parenthetical', ''))
        assert any(term in notes.lower() for term in ['garbage', 'privacy parenthetical',
                                                       'explicit privacy attack']), \
            "Vanguard entry must document the '(which are garbage)' parenthetical"

    def test_meta_coverage_has_limitation_framing(self):
        """Meta product headline leads with limitations despite positive body."""
        data = load_journalists()
        profile = get_so_profile(data)
        assert profile is not None
        meta_coverage = profile.get('meta_coverage', [])
        vanguard_entries = [e for e in meta_coverage
                          if isinstance(e, dict) and
                          'vanguard' in str(e.get('title', '')).lower()]
        assert len(vanguard_entries) >= 1
        vanguard = vanguard_entries[0]
        headline_framing = str(vanguard.get('headline_framing', ''))
        assert any(term in headline_framing.lower()
                  for term in ['limitation', 'camera specs', 'not impressive', 'qualification']), \
            "Vanguard headline framing must document limitation-first pattern"

    def test_google_coverage_has_zero_privacy_caveats(self):
        """Google Pixel Watch review contains zero privacy caveats."""
        data = load_journalists()
        profile = get_so_profile(data)
        assert profile is not None
        google_coverage = profile.get('google_coverage', [])
        pixel_watch_entries = [e for e in google_coverage
                              if isinstance(e, dict) and
                              'pixel watch' in str(e.get('title', '')).lower()]
        assert len(pixel_watch_entries) >= 1, \
            "Must have Pixel Watch coverage entry"

        pixel_watch = pixel_watch_entries[0]
        framing = str(pixel_watch.get('framing', ''))
        assert any(term in framing.lower()
                  for term in ['promotional', 'positive', 'elevating', 'no privacy']), \
            "Pixel Watch framing must document absence of privacy caveats"

    def test_google_coverage_has_promotional_headline(self):
        """Google Pixel Watch 4 headline actively elevates Google's competitive position."""
        data = load_journalists()
        profile = get_so_profile(data)
        assert profile is not None
        google_coverage = profile.get('google_coverage', [])
        pw4_entries = [e for e in google_coverage
                      if isinstance(e, dict) and
                      ('pixel watch 4' in str(e.get('title', '')).lower() or
                       'surprisingly close' in str(e.get('title', '')).lower())]
        assert len(pw4_entries) >= 1, \
            "Must have Pixel Watch 4 'Surprisingly Close' entry"

        pw4 = pw4_entries[0]
        assert 'surprisingly close' in str(pw4.get('title', '')).lower() or \
               'promotional' in str(pw4.get('framing', '')).lower() or \
               'elevating' in str(pw4.get('notes', '')).lower(), \
            "Pixel Watch 4 headline must document promotional/elevating frame"

    def test_privacy_vocabulary_asymmetry_documented(self):
        """Cross-entity analysis must explicitly document the vocabulary asymmetry."""
        data = load_journalists()
        profile = get_so_profile(data)
        assert profile is not None
        cross_entity = profile.get('cross_entity_analysis', {})
        assert cross_entity.get('mechanism_id') == 102, \
            "Cross-entity analysis must reference mechanism #102"
        pattern = str(cross_entity.get('pattern', ''))
        assert any(term in pattern.lower()
                  for term in ['privacy_vocabulary_bifurcation',
                              'vocabulary_bifurcation',
                              'entity_selective_privacy']), \
            "Pattern must identify privacy vocabulary bifurcation"


# ===================================================================
# Test Class 3: Data Sensitivity Inversion
# ===================================================================
class TestDataSensitivityInversion:
    """Meta's camera product gets privacy alarm while Google's biometric
    health product gets frictionless praise — an inversion of actual
    data sensitivity."""

    def test_mechanism_documents_data_sensitivity_inversion(self):
        """Mechanism #102 must note that Google Watch collects MORE sensitive
        data than Meta camera glasses."""
        research = load_competitor_research()
        mech = find_mechanism(research, 102)
        assert mech is not None, "Mechanism #102 must exist"
        summary = str(mech.get('finding_summary', '')) + str(mech.get('data_sensitivity_inversion', ''))
        assert any(term in summary.lower()
                  for term in ['biometric', 'health data', 'heart rate',
                              'blood oxygen', 'sensitivity inversion']), \
            "Mechanism must document that Google collects more sensitive biometric data"

    def test_oakley_vanguard_is_camera_not_health_product(self):
        """Oakley Meta Vanguard has NO biometric health sensors — privacy attack
        targets Meta's company reputation, not the product's data collection."""
        data = load_journalists()
        profile = get_so_profile(data)
        assert profile is not None
        meta_coverage = profile.get('meta_coverage', [])
        vanguard_entries = [e for e in meta_coverage
                          if isinstance(e, dict) and
                          'vanguard' in str(e.get('title', '')).lower()]
        assert len(vanguard_entries) >= 1
        vanguard = vanguard_entries[0]
        notes = str(vanguard.get('notes', ''))
        assert any(term in notes.lower()
                  for term in ['camera', 'no biometric', 'no health sensor',
                              'fitness glasses', 'action cam']), \
            "Vanguard entry must note it's a camera product, not a health/biometric device"

    def test_pixel_watch_collects_health_biometrics(self):
        """Pixel Watch collects heart rate, blood oxygen, sleep stages,
        GPS, menstrual cycles — far more sensitive than camera footage."""
        data = load_journalists()
        profile = get_so_profile(data)
        assert profile is not None
        google_coverage = profile.get('google_coverage', [])
        pixel_watch_entries = [e for e in google_coverage
                              if isinstance(e, dict) and
                              'pixel watch' in str(e.get('title', '')).lower()]
        assert len(pixel_watch_entries) >= 1
        pw = pixel_watch_entries[0]
        notes = str(pw.get('notes', ''))
        assert any(term in notes.lower()
                  for term in ['health', 'biometric', 'heart rate',
                              'fitbit', 'advertising']), \
            "Pixel Watch entry must note the health/biometric data collection"


# ===================================================================
# Test Class 4: WIRED Wearables Team Coverage Pattern
# ===================================================================
class TestWiredWearablesTeamPattern:
    """Adrienne So extends the privacy vocabulary bifurcation to the
    fitness/wearables lane, complementing Chokkattu (glasses/phones),
    Ashworth (glasses/tech), and Rogers (privacy/investigations)."""

    def test_mechanism_references_other_wired_journalists(self):
        """Mechanism #102 must cross-reference other WIRED journalist mechanisms."""
        research = load_competitor_research()
        mech = find_mechanism(research, 102)
        assert mech is not None, "Mechanism #102 must exist"
        xrefs = mech.get('cross_references', [])
        xref_ids = set()
        for x in xrefs:
            if isinstance(x, dict):
                xref_ids.add(x.get('mechanism_id'))
            elif isinstance(x, int):
                xref_ids.add(x)
        # Must reference at least 2 other WIRED journalist mechanisms
        wired_journalist_mechanisms = {73, 87, 91, 93, 97}
        overlap = xref_ids & wired_journalist_mechanisms
        assert len(overlap) >= 2, \
            f"Must cross-reference at least 2 other WIRED journalist mechanisms, found {overlap}"

    def test_mechanism_identifies_editorial_team_scope(self):
        """The finding must establish that the bifurcation extends across
        WIRED's entire wearables editorial team, not just one beat."""
        research = load_competitor_research()
        mech = find_mechanism(research, 102)
        assert mech is not None
        summary = str(mech.get('finding_summary', '')) + str(mech.get('editorial_team_scope', ''))
        assert any(term in summary.lower()
                  for term in ['editorial team', 'entire wearables',
                              'fitness lane', 'team-wide', 'institutional']), \
            "Mechanism must identify team-wide/institutional scope"


# ===================================================================
# Test Class 5: Financial Context
# ===================================================================
class TestFinancialContext:
    """Google advertising/Showcase payments flow to WIRED/Condé Nast/Advance."""

    def test_mechanism_has_financial_context(self):
        """Mechanism #102 must document Google-Advance financial relationships."""
        research = load_competitor_research()
        mech = find_mechanism(research, 102)
        assert mech is not None
        financial = mech.get('financial_context', {})
        financial_str = str(financial).lower()
        assert any(term in financial_str
                  for term in ['google', 'showcase', 'advertising',
                              'advance', 'conde nast']), \
            "Financial context must reference Google-Advance/Condé Nast relationships"

    def test_mechanism_notes_no_meta_financial_relationship(self):
        """No equivalent Meta → WIRED/Condé Nast/Advance financial deal."""
        research = load_competitor_research()
        mech = find_mechanism(research, 102)
        assert mech is not None
        financial = mech.get('financial_context', {})
        financial_str = str(financial).lower()
        assert any(term in financial_str
                  for term in ['no meta', 'no equivalent', 'meta relationship']), \
            "Financial context must note absence of Meta financial relationship"


# ===================================================================
# Test Class 6: Confounding Factors
# ===================================================================
class TestConfoundingFactors:
    """Mechanism must honestly document confounding factors."""

    def test_has_confounding_factors(self):
        research = load_competitor_research()
        mech = find_mechanism(research, 102)
        assert mech is not None
        confounds = mech.get('confounding_factors', [])
        assert len(confounds) >= 3, \
            f"Must have at least 3 confounding factors, found {len(confounds)}"

    def test_strongest_confound_is_meta_reputation(self):
        """Strongest confounding factor should be Meta's genuinely worse
        privacy reputation from Cambridge Analytica, etc."""
        research = load_competitor_research()
        mech = find_mechanism(research, 102)
        assert mech is not None
        confounds = mech.get('confounding_factors', [])
        strong_confounds = [c for c in confounds
                          if isinstance(c, dict) and
                          c.get('strength', '').lower() == 'strong']
        assert len(strong_confounds) >= 1, "Must have at least one STRONG confound"
        strong_text = ' '.join(str(c) for c in strong_confounds).lower()
        assert any(term in strong_text
                  for term in ['reputation', 'cambridge analytica',
                              'privacy scandal', 'genuine']), \
            "Strongest confound must acknowledge Meta's genuine privacy reputation"

    def test_camera_vs_watch_confound(self):
        """Must acknowledge camera products invite more privacy scrutiny
        than watches."""
        research = load_competitor_research()
        mech = find_mechanism(research, 102)
        assert mech is not None
        confounds = mech.get('confounding_factors', [])
        confound_text = ' '.join(str(c) for c in confounds).lower()
        assert any(term in confound_text
                  for term in ['camera', 'visible privacy', 'form factor']), \
            "Must acknowledge camera vs watch privacy surface area difference"


# ===================================================================
# Test Class 7: Testable Predictions
# ===================================================================
class TestTestablePredictions:
    """Mechanism must include testable predictions."""

    def test_has_testable_predictions(self):
        research = load_competitor_research()
        mech = find_mechanism(research, 102)
        assert mech is not None
        predictions = mech.get('testable_predictions', [])
        assert len(predictions) >= 2, \
            f"Must have at least 2 testable predictions, found {len(predictions)}"

    def test_predictions_are_falsifiable(self):
        """Each prediction must specify an observable outcome."""
        research = load_competitor_research()
        mech = find_mechanism(research, 102)
        assert mech is not None
        predictions = mech.get('testable_predictions', [])
        for i, pred in enumerate(predictions):
            pred_str = str(pred).lower()
            assert any(term in pred_str
                      for term in ['if', 'will', 'when', 'should', 'would']), \
                f"Prediction {i} must be conditional/falsifiable"


# ===================================================================
# Test Class 8: Source Quality
# ===================================================================
class TestSourceQuality:
    """All evidence must have verifiable source URLs."""

    def test_mechanism_has_source_urls(self):
        research = load_competitor_research()
        mech = find_mechanism(research, 102)
        assert mech is not None
        sources = mech.get('sources', [])
        assert len(sources) >= 3, \
            f"Must have at least 3 source URLs, found {len(sources)}"

    def test_sources_are_https(self):
        research = load_competitor_research()
        mech = find_mechanism(research, 102)
        assert mech is not None
        sources = mech.get('sources', [])
        for s in sources:
            url = s.get('url', '') if isinstance(s, dict) else str(s)
            if url and 'http' in url:
                assert url.startswith('https://'), \
                    f"Source URL must use HTTPS: {url}"

    def test_journalist_meta_coverage_has_urls(self):
        data = load_journalists()
        profile = get_so_profile(data)
        assert profile is not None
        meta_coverage = profile.get('meta_coverage', [])
        for entry in meta_coverage:
            if isinstance(entry, dict):
                # At least one URL reference per entry
                has_url = bool(entry.get('url') or entry.get('source_url') or
                             entry.get('techmeme_url'))
                assert has_url, \
                    f"Meta coverage entry '{entry.get('title', '?')}' must have a URL"


# ===================================================================
# Test Class 9: Google Nightingale/Fitbit History Gap
# ===================================================================
class TestGoogleHealthDataHistory:
    """So's omission of Google's health data controversies (Project Nightingale,
    Fitbit FTC concerns) in the context of a health/fitness product review
    contrasts with her unprompted Meta privacy parenthetical in a camera
    product review."""

    def test_mechanism_documents_nightingale_gap(self):
        """Mechanism must note Google's Project Nightingale health data
        controversy was not mentioned in So's Pixel Watch coverage."""
        research = load_competitor_research()
        mech = find_mechanism(research, 102)
        assert mech is not None
        summary = str(mech.get('finding_summary', ''))
        evidence = str(mech.get('google_health_data_history_gap', ''))
        combined = (summary + evidence).lower()
        assert any(term in combined
                  for term in ['nightingale', 'fitbit', 'ascension',
                              'health data controvers']), \
            "Mechanism must document Google's health data controversy omission"


# ===================================================================
# Test Class 10: Pattern Consistency with WIRED Team
# ===================================================================
class TestPatternConsistency:
    """The bifurcation pattern must be consistent across the WIRED team."""

    def test_at_least_four_wired_journalists_show_bifurcation(self):
        """With Adrienne So, at least 4 WIRED journalists demonstrate
        entity-selective privacy vocabulary."""
        research = load_competitor_research()
        # Mechanisms known to document WIRED journalist bifurcation:
        # #93 Chokkattu, #73/#87 Ashworth, #97 Rogers, #102 So
        wired_bifurcation_mechanisms = [93, 73, 87, 97, 102]
        found = 0
        for mid in wired_bifurcation_mechanisms:
            mech = find_mechanism(research, mid)
            if mech is not None:
                found += 1
        assert found >= 4, \
            f"At least 4 WIRED journalist bifurcation mechanisms must exist, found {found}"

    def test_mechanism_has_correct_id(self):
        research = load_competitor_research()
        mech = find_mechanism(research, 102)
        assert mech is not None, "Mechanism #102 must exist in competitor-coverage-research.yaml"
        assert mech.get('mechanism_id') == 102

    def test_mechanism_has_date(self):
        research = load_competitor_research()
        mech = find_mechanism(research, 102)
        assert mech is not None
        assert mech.get('date_added') == '2026-08-14', \
            "Mechanism must be dated 2026-08-14"
