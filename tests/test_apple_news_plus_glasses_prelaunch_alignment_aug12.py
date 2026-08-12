"""
Mechanism #61: Apple News+ Smart Glasses Pre-Launch Coverage Alignment Channel

FINDING: Apple News+ creates a financial dependency between Apple and 400+
publishers (50% of $12.99/mo, engagement-weighted allocation, 125M MAU). Apple
is simultaneously preparing to launch smart glasses (N50, WWDC Jun 2027) with
an explicit strategy to "distance the launch from criticism faced by Meta's
Ray-Ban glasses" (Gurman, Bloomberg, Jul 26, 2026). This creates a TRIPLE
ALIGNMENT where publisher financial incentives converge with Apple's competitive
positioning:

  (1) FINANCIAL: Apple News+ publishers earn revenue from Apple. No publisher
      earns revenue from Meta. Adversarial Meta coverage is cost-free; adversarial
      Apple coverage risks revenue.

  (2) COMPETITIVE: Every article framing Meta glasses as a "privacy nightmare"
      simultaneously damages Apple's #1 competitor in the smart glasses market
      and strengthens Apple's "responsible alternative" positioning for N50.

  (3) EDITORIAL CURATION: Apple employs 100 editors who control Top Stories
      placement on Apple News. UK data (Enders Analysis) shows national newspapers
      get 55% of engagement despite being 5% of titles — editorial placement
      drives revenue share. Publishers who support Apple's narrative may receive
      favorable positioning.

Apple's Q3 FY2026: Services $30.7B/quarter, 1.5B paid subscriptions, 2.5B
active devices. Apple News+ is the #1 news app in US/Canada/Australia. The
Semafor/Digiday "lifeline" characterization came as publishers face declining
Google referral traffic (-34.5% from AI Overviews) and near-zero Meta referral
traffic. Apple is the last major platform growing publisher traffic.

COVERAGE FRAMING EVIDENCE: Apple's smart glasses delay received uniformly
aspirational framing from Apple News+ publishers:
  - "Privacy Focus" (TechRepublic) — virtue framing
  - "Prioritizing privacy" (Neowin) — intentional framing
  - "Beat Android XR and Meta where it matters" (Android Authority) — competitive advantage framing
  - "Can Apple make smart glasses that aren't a constant privacy threat?" (TechCrunch) — implicit: others ARE threats
  - "Apple's glasses are running late because they don't want to stir a privacy storm" (Digital Trends) — heroic delay

Meanwhile Meta's PROACTIVE privacy measures (Jul 7 2026: camera auto-disable on
LED tamper detection) received REACTIVE framing: "responded after reports" rather
than "industry-leading innovation."

META CONTRAST: Meta has ZERO financial relationships with Apple News+ publishers.
Meta's glasses are the #1 smart glasses product globally (10M+ sold). Meta
proactively shipped camera-disable (Jul 7 2026). Yet Meta is the narrative
FOIL — "demonstrated the privacy nightmare" — while Apple, which has NOT
shipped a product and may remove the camera entirely, receives aspirational
privacy framing.

CONFOUNDING FACTORS:
1. Privacy concerns about camera glasses are legitimate (STRONG)
2. Apple genuinely has a stronger public privacy track record (STRONG)
3. Apple may genuinely invest more in N50 privacy features (MODERATE)
4. Some non-Apple-News+ publications also frame the delay positively (MODERATE)
5. Bloomberg (Gurman, not on News+) is the source of most coverage (MODERATE)
6. Publisher Apple News+ revenue is modest for large publishers (MODERATE)
7. Apple's 100 editors may exercise genuine editorial judgment (WEAK)

TESTABLE PREDICTIONS:
1. WIRED (16 Condé Nast titles on Apple News+) will cover N50 launch with
   softer framing than it applied to Meta glasses — no "mass surveillance"
2. The Atlantic ("most valuable syndication partner") will position Apple
   glasses as the "responsible alternative" to Meta
3. FT (NOT on Apple News+) will apply comparable privacy scrutiny to N50
   as to Meta glasses
4. If Apple removes N50 camera, Apple News+ publishers will frame the
   removal as "principled" rather than "feature-cutting"

CROSS-REFERENCES:
- Mechanism #30: Chokkattu temporal framing oscillation (WIRED: same journalist,
  different genre = different framing; adds genre interaction with financial incentive)
- Mechanism #31: Pero at Gizmodo (industry-wide genre-determined framing; adds
  cross-publication structural explanation)
- Mechanism #43: Dual-client litigation entanglement (Apple-OpenAI lawsuit creates
  dual-client pressure on Condé Nast, WSJ, The Atlantic, Vox Media, Hearst — all
  simultaneously Apple News+ and OpenAI deal partners)
- Mechanism #47: Meta ad revenue competitor structural antagonism (Meta is
  publishers' DIRECT ad business competitor; this mechanism adds Apple News+ as
  the revenue REPLACEMENT that makes anti-Meta coverage cost-free)
- Mechanism #55: Privacy innovation attribution inversion (Meta's camera-disable
  innovation framed reactively; Apple's delay framed aspirationally)

SOURCE URLS:
- https://betanews.com/article/apple-smart-glasses-wwdc-2027-privacy/
- https://www.ghacks.net/2026/07/28/apple-delays-first-smart-glasses-to-wwdc-2027-over-privacy-concerns/
- https://www.digitaltrends.com/wearables/apples-smart-glasses-are-running-late-because-they-dont-want-to-stir-a-privacy-storm/
- https://www.neowin.net/news/report-apples-smart-glasses-delayed-due-to-privacy-concerns/
- https://www.techrepublic.com/article/news-apple-smart-glasses-privacy/
- https://techcrunch.com/2026/07/26/can-apple-make-smart-glasses-that-arent-a-constant-privacy-threat/
- https://digiday.com/media/media-briefing-publishers-see-apple-news-as-a-stable-revenue-stream-amid-volatile-referral-traffic/
- https://9to5mac.com/2024/05/22/apple-news-lifeline/
- https://9to5mac.com/2024/05/29/apple-news-subscriptions-growing-4x-faster-than-major-publishers/
- https://digiday.com/media/media-briefing-apple-news-ad-monetization-still-abysmal-for-some/
- https://www.mactech.com/2026/01/30/report-the-influence-of-apple-news-will-grow-as-ai-usage-increases/
"""

import pytest
import yaml
import os


# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────

def _profiles_dir():
    return os.path.join(os.path.dirname(__file__), '..', 'profiles')


def _load_yaml(name):
    path = os.path.join(_profiles_dir(), name)
    with open(path) as f:
        return yaml.safe_load(f)


def _load_competitor_entities():
    return _load_yaml('competitor-entities.yaml')


def _load_competitor_research():
    return _load_yaml('competitor-coverage-research.yaml')


def _load_wired_profile():
    return _load_yaml('wired.yaml')


# ─────────────────────────────────────────────────────────────────────────────
# 1. Apple News+ Platform Financial Structure
# ─────────────────────────────────────────────────────────────────────────────

class TestAppleNewsPlusPlatformFinancials:
    """Apple News+ creates measurable financial dependency for publishers."""

    def test_apple_news_plus_subscription_price(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        assert apple['apple_news_platform_leverage']['subscription_price_usd'] == 12.99

    def test_apple_revenue_share_50_percent(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        assert apple['apple_news_platform_leverage']['subscription_revenue_share_pct'] == 50

    def test_apple_news_monthly_active_users(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        mau = apple['apple_news_platform_leverage']['monthly_active_users_m']
        assert mau >= 125, f"Apple News MAU should be >= 125M, got {mau}M"

    def test_apple_news_title_count(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        titles = apple['apple_news_platform_leverage']['title_count']
        assert titles >= 400, f"Apple News+ should have 400+ titles, got {titles}"

    def test_cirp_us_penetration_growth(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        p2020 = apple['apple_news_platform_leverage']['cirp_us_penetration_pct_2020']
        p2024 = apple['apple_news_platform_leverage']['cirp_us_penetration_pct_2024']
        assert p2024 > p2020, f"News+ penetration should grow: {p2020}% → {p2024}%"
        assert p2024 - p2020 >= 9, "Growth should be at least 9pp (15% → 24%)"

    def test_apple_100_editors_curation(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        editors = apple['apple_news_platform_leverage']['editors']
        assert editors >= 100, f"Apple employs 100+ News editors, got {editors}"

    def test_meta_zero_news_plus_participation(self):
        """Meta has zero financial relationship with Apple News+ publishers."""
        ents = _load_competitor_entities()
        meta = ents['entities']['meta']
        # Meta provides zero revenue TO publishers through any distribution platform
        assert 'apple_news' not in str(meta).lower() or 'none' in str(meta.get('apple_news_platform', 'none')).lower()


# ─────────────────────────────────────────────────────────────────────────────
# 2. Apple N50 Smart Glasses Competitive Positioning
# ─────────────────────────────────────────────────────────────────────────────

class TestAppleN50CompetitivePositioning:
    """Apple explicitly positions N50 glasses against Meta's privacy reputation."""

    def test_n50_codename_documented(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        glasses = apple.get('smart_glasses_n50') or apple.get('apple_news_glasses_prelaunch_alignment', {}).get('n50')
        assert glasses is not None, "N50 smart glasses entry should exist"

    def test_privacy_priority_number_one(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        alignment = apple.get('apple_news_glasses_prelaunch_alignment', {})
        overview = str(alignment.get('overview', ''))
        assert 'priority' in overview.lower(), "Should document privacy as Apple's stated priority"

    def test_delay_attributed_to_privacy(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        alignment = apple.get('apple_news_glasses_prelaunch_alignment', {})
        overview = str(alignment.get('overview', ''))
        assert 'delay' in overview.lower() or 'postpone' in overview.lower()

    def test_explicit_meta_distancing_strategy(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        alignment = apple.get('apple_news_glasses_prelaunch_alignment', {})
        overview = str(alignment.get('overview', ''))
        assert 'meta' in overview.lower(), "Should document Apple's explicit distancing from Meta"

    def test_wwdc_2027_timeline(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        alignment = apple.get('apple_news_glasses_prelaunch_alignment', {})
        assert '2027' in str(alignment), "Should document 2027 launch timeline"


# ─────────────────────────────────────────────────────────────────────────────
# 3. Triple Alignment Channel
# ─────────────────────────────────────────────────────────────────────────────

class TestTripleAlignmentChannel:
    """Financial, competitive, and editorial curation incentives converge."""

    def test_financial_alignment_documented(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        alignment = apple.get('apple_news_glasses_prelaunch_alignment', {})
        channel = alignment.get('triple_alignment', {})
        assert 'financial' in str(channel).lower(), "Financial alignment should be documented"

    def test_competitive_alignment_documented(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        alignment = apple.get('apple_news_glasses_prelaunch_alignment', {})
        channel = alignment.get('triple_alignment', {})
        assert 'competitive' in str(channel).lower(), "Competitive alignment should be documented"

    def test_editorial_curation_alignment_documented(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        alignment = apple.get('apple_news_glasses_prelaunch_alignment', {})
        channel = alignment.get('triple_alignment', {})
        assert 'editorial' in str(channel).lower() or 'curation' in str(channel).lower()

    def test_meta_zero_dollar_cost_free_adversarial_coverage(self):
        """Anti-Meta coverage is cost-free for Apple News+ publishers."""
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        alignment = apple.get('apple_news_glasses_prelaunch_alignment', {})
        overview = str(alignment.get('overview', ''))
        assert 'cost-free' in overview.lower() or '$0' in overview or 'zero' in overview.lower()

    def test_mechanism_id_61(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        alignment = apple.get('apple_news_glasses_prelaunch_alignment', {})
        assert alignment.get('mechanism_id') == 61


# ─────────────────────────────────────────────────────────────────────────────
# 4. Coverage Framing Evidence
# ─────────────────────────────────────────────────────────────────────────────

class TestCoverageFramingEvidence:
    """Apple N50 delay received aspirational framing; Meta receives reactive framing."""

    def test_aspirational_framing_examples_documented(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        alignment = apple.get('apple_news_glasses_prelaunch_alignment', {})
        framing = alignment.get('coverage_framing_evidence', {})
        apple_framing = framing.get('apple_n50_delay_framing', [])
        assert len(apple_framing) >= 3, f"Should have 3+ Apple aspirational framing examples, got {len(apple_framing)}"

    def test_meta_reactive_framing_examples_documented(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        alignment = apple.get('apple_news_glasses_prelaunch_alignment', {})
        framing = alignment.get('coverage_framing_evidence', {})
        meta_framing = framing.get('meta_glasses_reactive_framing', [])
        assert len(meta_framing) >= 2, f"Should have 2+ Meta reactive framing examples, got {len(meta_framing)}"

    @pytest.mark.parametrize("term", [
        "privacy focus", "prioritizing privacy", "responsible",
    ])
    def test_apple_aspirational_vocabulary(self, term):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        alignment = apple.get('apple_news_glasses_prelaunch_alignment', {})
        framing_text = str(alignment.get('coverage_framing_evidence', ''))
        assert term.lower() in framing_text.lower(), \
            f"Aspirational term '{term}' should appear in framing evidence"

    @pytest.mark.parametrize("term", [
        "privacy nightmare", "privacy threat",
    ])
    def test_meta_adversarial_vocabulary_in_same_coverage(self, term):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        alignment = apple.get('apple_news_glasses_prelaunch_alignment', {})
        framing_text = str(alignment.get('coverage_framing_evidence', ''))
        assert term.lower() in framing_text.lower(), \
            f"Meta adversarial term '{term}' should appear in framing evidence"


# ─────────────────────────────────────────────────────────────────────────────
# 5. Profiled Publisher Apple News+ Participation
# ─────────────────────────────────────────────────────────────────────────────

class TestProfiledPublisherParticipation:
    """MediaScope-profiled publishers that are Apple News+ partners."""

    def test_conde_nast_wired_on_news_plus(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        publishers = apple['apple_news_platform_leverage']['profiled_publisher_participation']
        cn = [p for p in publishers if 'Condé Nast' in p['name'] or 'Conde Nast' in p['name']]
        assert len(cn) >= 1, "Condé Nast should be listed as Apple News+ partner"
        assert cn[0]['status'] == 'partner'

    def test_conde_nast_16_titles(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        publishers = apple['apple_news_platform_leverage']['profiled_publisher_participation']
        cn = [p for p in publishers if 'Condé Nast' in p['name'] or 'Conde Nast' in p['name']][0]
        assert '16' in cn.get('detail', ''), "Should document 16 Condé Nast titles on News+"

    def test_atlantic_most_valuable_partner_quote(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        publishers = apple['apple_news_platform_leverage']['profiled_publisher_participation']
        atl = [p for p in publishers if 'Atlantic' in p['name']]
        assert len(atl) >= 1, "The Atlantic should be listed as Apple News+ partner"
        assert 'most valuable' in str(atl[0]).lower(), "Should include 'most valuable syndication partner' quote"

    def test_ft_not_on_news_plus(self):
        """FT is the control case — NOT on Apple News+, financially independent."""
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        publishers = apple['apple_news_platform_leverage']['profiled_publisher_participation']
        ft = [p for p in publishers if 'Financial Times' in p['name'] or 'FT' in p['name']]
        if ft:
            assert ft[0]['status'] == 'not_available', "FT should not be on Apple News+"

    def test_no_disclosure_in_coverage(self):
        """Apple News+ partners don't disclose the financial relationship in coverage."""
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        publishers = apple['apple_news_platform_leverage']['profiled_publisher_participation']
        for pub in publishers:
            if pub['status'] == 'partner':
                assert pub.get('disclosed_in_coverage') is False, \
                    f"{pub['name']} should have disclosed_in_coverage=false"


# ─────────────────────────────────────────────────────────────────────────────
# 6. Lifeline Paradox
# ─────────────────────────────────────────────────────────────────────────────

class TestLifelineParadox:
    """Publishers increasingly depend on Apple News+ as alternatives collapse."""

    def test_lifeline_paradox_documented(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        leverage = apple.get('apple_news_platform_leverage', {})
        relevance = str(leverage.get('mediascope_relevance', ''))
        assert 'lifeline' in relevance.lower(), "Lifeline Paradox should be documented"

    def test_google_traffic_decline_context(self):
        """Apple News dependency grows as Google AI Overviews cuts referral traffic."""
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        alignment = apple.get('apple_news_glasses_prelaunch_alignment', {})
        overview = str(alignment.get('overview', ''))
        assert 'traffic' in overview.lower() or 'referral' in overview.lower() or \
               'lifeline' in overview.lower()

    def test_meta_referral_traffic_near_zero(self):
        """Meta has deprioritized news, so Meta referral traffic is near zero."""
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        alignment = apple.get('apple_news_glasses_prelaunch_alignment', {})
        overview = str(alignment.get('overview', ''))
        assert 'meta' in overview.lower(), "Should reference Meta's role in traffic context"


# ─────────────────────────────────────────────────────────────────────────────
# 7. Confounding Factors
# ─────────────────────────────────────────────────────────────────────────────

class TestConfoundingFactors:
    """At least 7 legitimate confounding factors documented."""

    def test_confounding_factors_count(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        alignment = apple.get('apple_news_glasses_prelaunch_alignment', {})
        factors = alignment.get('confounding_factors', [])
        assert len(factors) >= 7, f"Should have 7+ confounding factors, got {len(factors)}"

    def test_legitimate_privacy_concern_acknowledged(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        alignment = apple.get('apple_news_glasses_prelaunch_alignment', {})
        factors = alignment.get('confounding_factors', [])
        factor_text = str(factors)
        assert 'legitimate' in factor_text.lower() or 'genuine' in factor_text.lower()

    def test_apple_privacy_track_record_acknowledged(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        alignment = apple.get('apple_news_glasses_prelaunch_alignment', {})
        factors = alignment.get('confounding_factors', [])
        factor_text = str(factors)
        assert 'track record' in factor_text.lower() or 'reputation' in factor_text.lower()

    def test_bloomberg_source_independence_acknowledged(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        alignment = apple.get('apple_news_glasses_prelaunch_alignment', {})
        factors = alignment.get('confounding_factors', [])
        factor_text = str(factors)
        assert 'bloomberg' in factor_text.lower() or 'gurman' in factor_text.lower()


# ─────────────────────────────────────────────────────────────────────────────
# 8. Testable Predictions
# ─────────────────────────────────────────────────────────────────────────────

class TestTestablePredictions:
    """At least 4 falsifiable predictions documented."""

    def test_predictions_count(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        alignment = apple.get('apple_news_glasses_prelaunch_alignment', {})
        predictions = alignment.get('testable_predictions', [])
        assert len(predictions) >= 4, f"Should have 4+ predictions, got {len(predictions)}"

    def test_wired_n50_launch_prediction(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        alignment = apple.get('apple_news_glasses_prelaunch_alignment', {})
        predictions = str(alignment.get('testable_predictions', []))
        assert 'wired' in predictions.lower(), "Should predict WIRED's N50 coverage framing"

    def test_ft_control_case_prediction(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        alignment = apple.get('apple_news_glasses_prelaunch_alignment', {})
        predictions = str(alignment.get('testable_predictions', []))
        assert 'ft' in predictions.lower() or 'financial times' in predictions.lower()


# ─────────────────────────────────────────────────────────────────────────────
# 9. Cross-References
# ─────────────────────────────────────────────────────────────────────────────

class TestCrossReferences:
    """Connects to existing mechanisms in the framework."""

    def test_cross_references_exist(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        alignment = apple.get('apple_news_glasses_prelaunch_alignment', {})
        xrefs = alignment.get('cross_references', [])
        assert len(xrefs) >= 3, f"Should have 3+ cross-references, got {len(xrefs)}"

    @pytest.mark.parametrize("mech_id", [30, 43, 47, 55])
    def test_expected_cross_reference(self, mech_id):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        alignment = apple.get('apple_news_glasses_prelaunch_alignment', {})
        xrefs = alignment.get('cross_references', [])
        xref_ids = [x.get('mechanism_id') for x in xrefs]
        assert mech_id in xref_ids, \
            f"Mechanism #{mech_id} should be cross-referenced"


# ─────────────────────────────────────────────────────────────────────────────
# 10. Source URLs
# ─────────────────────────────────────────────────────────────────────────────

class TestSourceUrls:
    """Every fact needs a source URL or citation."""

    def test_source_urls_exist(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        alignment = apple.get('apple_news_glasses_prelaunch_alignment', {})
        urls = alignment.get('source_urls', [])
        assert len(urls) >= 6, f"Should have 6+ source URLs, got {len(urls)}"

    def test_source_urls_are_valid_format(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        alignment = apple.get('apple_news_glasses_prelaunch_alignment', {})
        urls = alignment.get('source_urls', [])
        for url in urls:
            assert url.startswith('http'), f"URL should start with http: {url}"

    def test_gurman_bloomberg_sourced(self):
        ents = _load_competitor_entities()
        apple = ents['entities']['apple']
        alignment = apple.get('apple_news_glasses_prelaunch_alignment', {})
        overview = str(alignment.get('overview', ''))
        assert 'gurman' in overview.lower() or 'bloomberg' in overview.lower()


# ─────────────────────────────────────────────────────────────────────────────
# 11. Mechanism in Competitor Coverage Research
# ─────────────────────────────────────────────────────────────────────────────

class TestMechanismInResearchProfile:
    """Mechanism #61 registered in competitor-coverage-research.yaml."""

    def test_mechanism_61_in_cross_publication_findings(self):
        research = _load_competitor_research()
        findings = research.get('cross_publication_findings', {})
        mech_ids = []
        if isinstance(findings, dict):
            for key, val in findings.items():
                if isinstance(val, dict):
                    mid = val.get('mechanism_id')
                    if mid:
                        mech_ids.append(mid)
        elif isinstance(findings, list):
            for f in findings:
                if isinstance(f, dict):
                    mid = f.get('mechanism_id')
                    if mid:
                        mech_ids.append(mid)
        assert 61 in mech_ids, f"Mechanism #61 should be in cross_publication_findings, found: {mech_ids[-10:]}"


# ─────────────────────────────────────────────────────────────────────────────
# 12. Structural Consistency
# ─────────────────────────────────────────────────────────────────────────────

class TestStructuralConsistency:
    """Test file meets MediaScope structural standards."""

    def test_readme_lists_test_file(self):
        readme_path = os.path.join(os.path.dirname(__file__), '..', 'README.md')
        with open(readme_path) as f:
            content = f.read()
        assert 'test_apple_news_plus_glasses_prelaunch_alignment_aug12' in content

    def test_architecture_doc_lists_test_file(self):
        arch_path = os.path.join(os.path.dirname(__file__), '..', 'docs', 'ARCHITECTURE.md')
        with open(arch_path) as f:
            content = f.read()
        assert 'test_apple_news_plus_glasses_prelaunch_alignment_aug12' in content
