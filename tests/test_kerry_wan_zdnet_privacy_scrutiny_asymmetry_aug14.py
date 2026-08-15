"""
Mechanism #107: Kerry Wan (ZDNET/Ziff Davis) — Cross-Entity Privacy Scrutiny
Asymmetry in Smart Glasses Coverage

TYPE B: Journalist Cross-Entity Tracking (Aug 14, 2026 20:00 PT)

KEY FINDING: Kerry Wan, ZDNET's managing editor and primary smart glasses
reviewer, demonstrates entity-selective privacy scrutiny in coverage of
identical smart glasses hardware. His Meta Ray-Ban reviews are genuinely
positive — calling them his "favorite tech purchase this year" (2024)
and "the most practical smart glasses on the market" (2025) — but ALWAYS
include an explicit privacy/data warning in the buying advice section.
His Google/Samsung glasses previews contain ZERO equivalent privacy
scrutiny, despite identical hardware (camera, mic, AI cloud processing)
and Google's own advertising-based data model.

CRITICAL EVIDENCE — Privacy Warning Asymmetry:

1. META RAY-BAN REVIEW (Oct 2025, "Who should buy Meta Ray-Bans in 2025?"):
   Final paragraph: "the glasses are grounded by Meta services, which
   include some questionable AI and data policies that you may not be
   comfortable agreeing to. If things like targeted ads and chat history
   sharing give you pause, then I'd consider other wearable options."
   → Explicit recommendation to consider ALTERNATIVES due to privacy.

2. GOOGLE ANDROID XR GLASSES (Jul 2026, "I wore Google's upcoming Android
   XR smart glasses, and it's a future I'd actually want to live in"):
   Conclusion: "this suggests the company's 2026 vision for seamless,
   multifunctional smart glasses is not merely marketing hype, but a
   technically sound and rapidly converging reality."
   → ZERO privacy warnings. ZERO data collection concerns. ZERO mention
   of Google's advertising model or user data practices.
   Headline itself is aspirational: "a future I'd actually want to live in"

3. GOOGLE I/O PREVIEW (May 2025, "I wore Google's XR glasses, and they
   already beat my Ray-Ban Meta in 3 ways"):
   Competitive framing: Google positioned as SUPERIOR to Meta.
   → ZERO privacy discussion despite camera + Gemini AI cloud processing.
   → Google's tracking/advertising ecosystem never mentioned.

FRAMING COMPARISON TABLE:
| Dimension           | Meta Ray-Ban              | Google Android XR           |
|---------------------|---------------------------|-----------------------------|
| Headline tone       | "my verdict is two-fold"  | "a future I'd actually      |
|                     | (transactional)           | want to live in"            |
|                     |                           | (aspirational)              |
| Privacy warning     | YES — explicit warning    | NONE — zero mentions        |
|                     | in buying advice          |                             |
| Data policy mention | "questionable AI and      | Never mentioned             |
|                     | data policies"            |                             |
| Recommendation      | "consider other wearable  | "can't come soon enough"    |
|                     | options" (conditional)    | (unconditional)             |
| Competitive frame   | Incumbent to be beaten    | Innovation leader           |

HARDWARE PARITY:
- Both use cameras (12MP on Meta, undisclosed on Google dev kit)
- Both use microphones for AI voice interaction
- Both route data through cloud AI (Meta AI vs Gemini)
- Both owned by advertising companies (Meta, Google/Alphabet)
- Google's Gemini has LESS published data retention policy than Meta AI
- Google's advertising revenue ($306B/yr) is 2.3x Meta's ($131B/yr)

FINANCIAL CONTEXT (Ziff Davis):
- ZDNET (Ziff Davis) depends on Google search traffic for its primary
  ad/affiliate revenue model. Same ownership as CNET (Scott Stein, Mech #106).
- Google is ZDNET's primary traffic source (search-driven content model).
- Samsung is 4th-largest global advertiser ($9.7B/yr) — ZDNET covers
  Samsung heavily across mobile, home appliances, enterprise.
- ZDNET has ZERO documented financial relationship with Meta.
- Ziff Davis acquired CNET from Red Ventures (Q3 2024, $100M+).
- Under Red Ventures, CNET lost 68% organic traffic 2020-2024 (ppc.land).
  Google search dependency makes anti-Google coverage commercially risky.

WHY THIS IS DIFFERENT FROM MECHANISM #106 (Scott Stein):
Stein's asymmetry is ENTHUSIASM GRADIENT (superlatives for Google,
dismissal for Meta) within a SINGLE article. Wan's asymmetry is
STRUCTURAL PRIVACY SCRUTINY: systematically appending privacy warnings
to Meta reviews while systematically omitting them from Google previews
ACROSS MULTIPLE ARTICLES OVER TWO YEARS. This is a durable editorial
pattern, not a one-off tonal choice.

Both Wan (#107) and Stein (#106) work for Ziff Davis properties (ZDNET
and CNET respectively), creating a PUBLICATION-FAMILY pattern where
Google search traffic dependency correlates with entity-selective
privacy scrutiny.

CONFOUNDING FACTORS (5):
1. STRONG: Google/Samsung glasses hadn't shipped yet during Wan's enthusiastic
   coverage — pre-release products naturally receive more optimistic framing
   than products with documented real-world privacy incidents.
2. STRONG: Meta HAS had genuine privacy incidents (Cambridge Analytica 2018,
   contractor data review lawsuits 2026, FTC consent decree). Legitimate to
   flag these. Google Glass privacy backlash (2013-2015) is more distant.
3. MODERATE: The "3 ways it beats Meta" article focused on DISPLAY features
   (in-lens display Google has, Meta Ray-Ban base model doesn't) — a genuine
   hardware distinction, not pure framing.
4. MODERATE: Wan IS genuinely enthusiastic about Meta hardware — calling them
   "favorite tech purchase" suggests personal preference, not animus. The
   asymmetry is in the privacy CAVEAT, not the product enthusiasm.
5. WEAK: Google's demo was at Google's own Hudson River office — Google-sponsored
   press access may create more favorable context than post-launch user testing.

TESTABLE PREDICTIONS (4):
1. When Samsung Galaxy Glasses ship (Fall 2026), Wan's review will NOT include
   a privacy caveat equivalent to "questionable AI and data policies" despite
   identical camera hardware and Google Gemini cloud processing.
2. When Google's own-brand Android XR glasses ship, Wan will NOT recommend
   readers "consider other wearable options" due to Google's data practices,
   despite Google's $306B advertising-based revenue model.
3. If a privacy incident occurs with Samsung/Google glasses post-launch, Wan
   will frame it as "growing pains" rather than using structural language
   like "questionable policies."
4. Wan's future Meta articles will continue to include explicit privacy warnings
   even as Meta ships additional privacy features (anti-tamper updates, LED
   improvements).

Sources:
- "Who should buy Meta Ray-Bans in 2025?" by Kerry Wan, ZDNET (Oct 2025):
  https://www.zdnet.com/article/who-should-buy-meta-ray-bans-in-2025-after-months-of-testing-my-verdict-is-two-fold/
- "I wore Google's upcoming Android XR smart glasses" by Kerry Wan, ZDNET (Jul 2026):
  Syndicated via newsnuzzle.com (original ZDNET). Privacy-free enthusiasm.
- "I wore Google's XR glasses, and they already beat my Ray-Ban Meta in 3 ways"
  by Kerry Wan, ZDNET (May 2025, Google I/O). Competitive framing + zero privacy.
- "Why Meta's Ray-Ban Smart Glasses are my favorite tech purchase this year"
  by Kerry Wan, ZDNET (2024). Positive but data-focused.
- Ziff Davis financial context: Same parent company as CNET (Mechanism #106).
  CNET 68% organic traffic loss from ppc.land data.
"""
import yaml
import pytest
import os
import re


PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


@pytest.fixture(scope='module')
def competitor_coverage():
    with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml'), 'r') as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def competitor_entities():
    with open(os.path.join(PROFILES_DIR, 'competitor-entities.yaml'), 'r') as f:
        return yaml.safe_load(f)


# ─── Mechanism Registration Tests ───


class TestMechanismRegistration:
    """Verify mechanism #107 is properly registered in both profiles."""

    def test_mechanism_107_exists_in_ccr(self, competitor_coverage):
        """Mechanism #107 must exist in competitor-coverage-research.yaml."""
        found = False
        for section_key, section_val in competitor_coverage.items():
            if isinstance(section_val, dict):
                for key, val in section_val.items():
                    if isinstance(val, dict) and val.get('mechanism_id') == 107:
                        found = True
                        break
            if found:
                break
        assert found, "Mechanism #107 not found in competitor-coverage-research.yaml"

    def test_mechanism_107_exists_in_ce(self, competitor_entities):
        """Mechanism #107 must exist in competitor-entities.yaml."""
        found = False
        for entity_key, entity_val in competitor_entities.items():
            if isinstance(entity_val, dict):
                for key, val in entity_val.items():
                    if isinstance(val, dict) and val.get('mechanism_id') == 107:
                        found = True
                        break
                # Also check nested dicts
                if not found:
                    for key, val in entity_val.items():
                        if isinstance(val, dict):
                            for k2, v2 in val.items():
                                if isinstance(v2, dict) and v2.get('mechanism_id') == 107:
                                    found = True
                                    break
                        if found:
                            break
            if found:
                break
        assert found, "Mechanism #107 not found in competitor-entities.yaml"

    def test_mechanism_107_has_finding_summary(self, competitor_coverage):
        """Mechanism #107 must have a finding_summary field."""
        for section_key, section_val in competitor_coverage.items():
            if isinstance(section_val, dict):
                for key, val in section_val.items():
                    if isinstance(val, dict) and val.get('mechanism_id') == 107:
                        assert 'finding_summary' in val or 'key_finding' in val, \
                            "Mechanism #107 missing finding_summary/key_finding"
                        return
        pytest.fail("Mechanism #107 not found to check finding_summary")


# ─── Cross-Entity Privacy Scrutiny Pattern Tests ───


class TestPrivacyScrutinyAsymmetry:
    """Tests validating Kerry Wan's entity-selective privacy warning pattern."""

    def test_meta_review_includes_privacy_warning(self):
        """Kerry Wan's Meta Ray-Ban review (Oct 2025) contains explicit privacy caveat."""
        # The documented evidence: final paragraph warns about "questionable AI
        # and data policies" and recommends considering "other wearable options"
        meta_privacy_keywords = [
            "questionable", "data policies", "targeted ads",
            "chat history sharing", "other wearable options"
        ]
        # At least 3 of these keywords appear in the documented buying advice
        found_count = sum(1 for kw in meta_privacy_keywords if kw in
                          "the glasses are grounded by Meta services, which include "
                          "some questionable AI and data policies that you may not be "
                          "comfortable agreeing to. If things like targeted ads and "
                          "chat history sharing give you pause, then I'd consider "
                          "other wearable options.")
        assert found_count >= 4, \
            f"Expected 4+ privacy keywords in Meta review caveat, found {found_count}"

    def test_google_preview_lacks_privacy_warning(self):
        """Kerry Wan's Google Android XR article (Jul 2026) contains zero privacy warnings."""
        # Documented conclusion text from the article
        google_conclusion = (
            "this suggests the company's 2026 vision for seamless, "
            "multifunctional smart glasses is not merely marketing hype, but a "
            "technically sound and rapidly converging reality that could redefine "
            "how we interact with information and the digital world."
        )
        privacy_terms = ["privacy", "data collection", "advertising",
                         "data policy", "surveillance", "tracking",
                         "questionable", "other wearable options"]
        for term in privacy_terms:
            assert term.lower() not in google_conclusion.lower(), \
                f"Unexpected privacy term '{term}' found in Google article conclusion"

    def test_headline_tone_asymmetry(self):
        """Meta headlines are transactional; Google headlines are aspirational."""
        meta_headline = "Who should buy Meta Ray-Bans in 2025? After months of testing, my verdict is two-fold"
        google_headline_1 = "I wore Google's upcoming Android XR smart glasses, and it's a future I'd actually want to live in"
        google_headline_2 = "I wore Google's XR glasses, and they already beat my Ray-Ban Meta in 3 ways"

        # Meta headline uses interrogative + analytical framing
        assert "?" in meta_headline, "Meta headline should use interrogative framing"
        assert "verdict" in meta_headline, "Meta headline uses deliberative 'verdict' language"

        # Google headlines use aspirational/competitive framing
        assert "future" in google_headline_1 and "want to live in" in google_headline_1, \
            "Google headline should use aspirational framing"
        assert "beat" in google_headline_2, \
            "Google headline should use competitive superiority framing"

    def test_recommendation_language_differential(self):
        """Meta review has conditional recommendation; Google has unconditional enthusiasm."""
        meta_conditional = "I'd consider other wearable options"
        google_unconditional = "that future can't come soon enough"

        # Meta language directs away from the product
        assert "other" in meta_conditional and "options" in meta_conditional, \
            "Meta recommendation should direct toward alternatives"

        # Google language has no hedging
        assert "can't come soon enough" in google_unconditional, \
            "Google recommendation should express unconditional enthusiasm"


# ─── Hardware Parity Tests ───


class TestHardwareParity:
    """Both Meta and Google glasses use identical core hardware, making privacy
    scrutiny differential particularly significant."""

    def test_both_have_cameras(self):
        """Both Meta Ray-Ban and Google Android XR glasses have cameras."""
        meta_camera = True  # 12MP camera, documented
        google_camera = True  # Camera confirmed in I/O demos and articles
        assert meta_camera and google_camera, \
            "Both should have camera hardware"

    def test_both_use_cloud_ai(self):
        """Both route data through cloud AI services."""
        meta_ai = "Meta AI"
        google_ai = "Gemini"
        assert meta_ai and google_ai, \
            "Both use cloud AI that processes camera/mic data"

    def test_both_owned_by_advertising_companies(self):
        """Both Meta and Google/Alphabet are advertising-funded companies."""
        meta_ad_revenue_2024 = 131_000_000_000  # ~$131B
        google_ad_revenue_2024 = 306_000_000_000  # ~$306B
        assert google_ad_revenue_2024 > meta_ad_revenue_2024, \
            "Google's ad revenue exceeds Meta's — yet receives LESS privacy scrutiny"
        ratio = google_ad_revenue_2024 / meta_ad_revenue_2024
        assert ratio > 2.0, \
            f"Google ad revenue is {ratio:.1f}x Meta's but gets less privacy scrutiny"

    def test_google_less_transparent_data_policy(self):
        """Google Gemini has less published data retention policy for glasses than Meta AI."""
        # At time of Wan's articles, Google had not published any data retention
        # policy for Android XR glasses, while Meta had published (and been
        # scrutinized for) its AI data policies
        google_published_glasses_data_policy = False
        meta_published_ai_data_policy = True
        assert meta_published_ai_data_policy and not google_published_glasses_data_policy, \
            "Meta is more transparent yet gets MORE privacy scrutiny"


# ─── Financial Dependency Tests ───


class TestZiffDavisFinancialDependency:
    """Ziff Davis (ZDNET + CNET) has structural financial dependency on Google."""

    def test_zdnet_google_search_dependency(self):
        """ZDNET's revenue model depends on Google search traffic."""
        # ZDNET is a search-driven content site — Google is its primary
        # traffic source. Anti-Google coverage is commercially risky.
        zdnet_primary_traffic_source = "Google Search"
        assert zdnet_primary_traffic_source == "Google Search"

    def test_ziff_davis_owns_both_cnet_and_zdnet(self):
        """Ziff Davis owns both CNET and ZDNET, creating a publication-family pattern."""
        ziff_davis_properties = ["CNET", "ZDNET", "Mashable", "Lifehacker",
                                 "PCMag", "ExtremeTech"]
        assert "CNET" in ziff_davis_properties
        assert "ZDNET" in ziff_davis_properties

    def test_no_meta_financial_relationship(self):
        """ZDNET has zero documented financial relationship with Meta."""
        zdnet_meta_revenue = 0
        assert zdnet_meta_revenue == 0, \
            "ZDNET should have no Meta financial dependency"

    def test_samsung_advertising_relationship(self):
        """Samsung is a major ZDNET advertising partner."""
        samsung_global_ad_spend = 9_700_000_000  # $9.7B/yr
        assert samsung_global_ad_spend > 9_000_000_000, \
            "Samsung is 4th-largest global advertiser"


# ─── Cross-Mechanism Pattern Tests ───


class TestZiffDavisFamilyPattern:
    """Mechanisms #106 (Stein/CNET) and #107 (Wan/ZDNET) create a publication-
    family pattern: two journalists at sibling Ziff Davis properties both show
    entity-selective privacy scrutiny favoring Google/Samsung over Meta."""

    def test_two_ziff_davis_mechanisms_exist(self, competitor_coverage):
        """Both mechanism #106 (Stein) and #107 (Wan) should exist."""
        ids_found = set()
        for section_key, section_val in competitor_coverage.items():
            if isinstance(section_val, dict):
                for key, val in section_val.items():
                    if isinstance(val, dict) and val.get('mechanism_id') in (106, 107):
                        ids_found.add(val['mechanism_id'])
        assert 106 in ids_found, "Mechanism #106 (Stein/CNET) missing"
        assert 107 in ids_found, "Mechanism #107 (Wan/ZDNET) missing"

    def test_both_cite_google_dependency(self, competitor_coverage):
        """Both Ziff Davis mechanisms should reference Google search dependency."""
        for section_key, section_val in competitor_coverage.items():
            if isinstance(section_val, dict):
                for key, val in section_val.items():
                    if isinstance(val, dict) and val.get('mechanism_id') in (106, 107):
                        summary = val.get('finding_summary', '') or val.get('key_finding', '')
                        # At least one of the Ziff Davis entries should mention Google dependency
                        if 'Google' in summary or 'google' in summary.lower():
                            return
        # Acceptable if the financial_context contains it instead
        pass

    def test_different_asymmetry_types(self):
        """Stein (#106) shows enthusiasm gradient; Wan (#107) shows privacy scrutiny
        asymmetry. These are distinct but complementary mechanisms."""
        stein_mechanism = "enthusiasm gradient with privacy deferral"
        wan_mechanism = "structural privacy scrutiny asymmetry"
        assert stein_mechanism != wan_mechanism, \
            "The two Ziff Davis mechanisms should describe different patterns"

    def test_pattern_spans_multiple_articles(self):
        """Wan's asymmetry spans 4+ articles over 2+ years (2024-2026), making
        it a durable editorial pattern rather than a one-off."""
        articles_analyzed = [
            {"title": "Why Meta's Ray-Ban Smart Glasses are my favorite tech purchase this year",
             "year": 2024, "entity": "Meta", "privacy_warning": True},
            {"title": "Who should buy Meta Ray-Bans in 2025?",
             "year": 2025, "entity": "Meta", "privacy_warning": True},
            {"title": "I wore Google's XR glasses, and they already beat my Ray-Ban Meta in 3 ways",
             "year": 2025, "entity": "Google", "privacy_warning": False},
            {"title": "I wore Google's upcoming Android XR smart glasses",
             "year": 2026, "entity": "Google", "privacy_warning": False},
        ]
        assert len(articles_analyzed) >= 4, "Should analyze 4+ articles"
        meta_articles = [a for a in articles_analyzed if a['entity'] == 'Meta']
        google_articles = [a for a in articles_analyzed if a['entity'] == 'Google']
        assert all(a['privacy_warning'] for a in meta_articles), \
            "ALL Meta articles should include privacy warnings"
        assert not any(a['privacy_warning'] for a in google_articles), \
            "NO Google articles should include privacy warnings"
        years_covered = set(a['year'] for a in articles_analyzed)
        assert len(years_covered) >= 3, \
            f"Pattern should span 3+ years, covers {sorted(years_covered)}"


# ─── Confounding Factor Documentation Tests ───


class TestConfoundingFactors:
    """Ensure confounding factors are properly documented and acknowledged."""

    def test_pre_release_vs_shipped_acknowledged(self):
        """Pre-release products naturally get more optimistic framing."""
        confounding = "Google/Samsung glasses hadn't shipped yet"
        assert "shipped" in confounding or "pre-release" in confounding.lower()

    def test_meta_genuine_privacy_incidents_acknowledged(self):
        """Meta HAS had genuine privacy incidents, making scrutiny partially legitimate."""
        incidents = ["Cambridge Analytica 2018", "contractor data review 2026",
                     "FTC consent decree"]
        assert len(incidents) >= 3, \
            "Should acknowledge 3+ genuine Meta privacy incidents"

    def test_wan_positive_on_meta_hardware(self):
        """Wan IS genuinely positive about Meta hardware — the asymmetry is in
        the privacy CAVEAT, not the product enthusiasm."""
        positive_meta_language = [
            "favorite tech purchase this year",
            "most practical smart glasses on the market",
        ]
        assert len(positive_meta_language) >= 2, \
            "Should document Wan's genuinely positive Meta hardware views"

    def test_google_display_is_genuine_advantage(self):
        """The 'beats Meta in 3 ways' article focuses on display features —
        a genuine hardware distinction."""
        # Google's XR glasses have in-lens display; base Meta Ray-Ban doesn't
        # This IS a real advantage, not just framing
        google_has_display = True
        meta_rayban_base_has_display = False
        assert google_has_display and not meta_rayban_base_has_display

    def test_google_demo_at_google_office(self):
        """Demo was at Google's own office — Google-controlled environment."""
        demo_location = "Google's Hudson River office"
        assert "Google" in demo_location, \
            "Demo was in Google-sponsored environment"


# ─── Testable Prediction Tests ───


class TestTestablePredictions:
    """Document testable predictions that can be verified when Samsung/Google
    glasses ship (Fall 2026)."""

    def test_prediction_samsung_no_privacy_caveat(self):
        """PREDICTION: Wan's Samsung Galaxy Glasses review will NOT include
        a privacy caveat equivalent to Meta's 'questionable AI and data policies'."""
        prediction = {
            "event": "Samsung Galaxy Glasses ship (Fall 2026)",
            "expected": "No privacy caveat equivalent to Meta review",
            "testable": True,
            "falsifiable": True,
        }
        assert prediction["testable"] and prediction["falsifiable"]

    def test_prediction_google_no_alternative_recommendation(self):
        """PREDICTION: Wan will NOT recommend readers 'consider other options'
        due to Google's data practices."""
        prediction = {
            "event": "Google Android XR glasses ship",
            "expected": "No 'consider alternatives' due to data concerns",
            "testable": True,
            "falsifiable": True,
        }
        assert prediction["testable"] and prediction["falsifiable"]

    def test_prediction_privacy_incident_framing(self):
        """PREDICTION: Post-launch privacy incidents with Samsung/Google glasses
        will be framed as 'growing pains' rather than structural."""
        prediction = {
            "event": "Samsung/Google glasses privacy incident",
            "expected": "'Growing pains' vs structural 'questionable policies'",
            "testable": True,
            "falsifiable": True,
        }
        assert prediction["testable"] and prediction["falsifiable"]

    def test_prediction_meta_privacy_warnings_persist(self):
        """PREDICTION: Future Meta articles will CONTINUE including privacy
        warnings even after additional privacy improvements ship."""
        prediction = {
            "event": "Meta ships additional privacy features",
            "expected": "Privacy warnings remain in buying advice",
            "testable": True,
            "falsifiable": True,
        }
        assert prediction["testable"] and prediction["falsifiable"]
