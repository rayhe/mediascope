"""
Mechanism #67: WSJ Beat Assignment Asymmetry — Consumer Tech vs Investigative
Channels Create Parallel Coverage Voices for Apple and Meta at the Same Publication

JOURNALIST: Nicole Nguyen (WSJ Personal Technology Columnist)
PUBLICATION: Wall Street Journal (News Corp)
CROSS-REFERENCE: Mechanism #56 (Verge beat segregation), #11 (Gurman access dependency),
    #66 (Cameron/Mehrotra investigative resource allocation)

CORE FINDING:

The Wall Street Journal assigns DIFFERENT reporters to cover DIFFERENT aspects
of the same wearables/AI category, producing systematically different framing
for Apple vs Meta — despite News Corp having BALANCED financial deals with both
companies ($50M/yr OpenAI content licensing, May 2024 + up to $50M/yr Meta
content licensing, Mar 2026).

THREE DISTINCT COVERAGE CHANNELS:

1. CONSUMER TECH (Nicole Nguyen, personal tech columnist):
   - Apple products: promotional/product-utility framing ("tech marvel,"
     "affordable," "five big differences," WWDC event coverage)
   - Samsung: comparative/respectful ("Apple needs to copy Samsung")
   - Amazon Ring / Google Nest: privacy-conscious ("dragnet era of home
     security cameras") — notably targets Amazon/Google surveillance
     cameras, NOT Meta glasses cameras
   - Meta: limited direct coverage; WhatsApp framed as "breaking through
     Apple's walled garden" (Nov 2025)
   - AI chatbots: platform-neutral privacy coverage (OpenAI, Anthropic, Google)

2. INVESTIGATIVE/ENTERPRISE (Meghan Bobrowsky, tech reporter):
   - Meta glasses: adversarial privacy/surveillance framing ("flooding the
     market," "privacy advocates up in arms," "privacy lightning rod")
   - Covers NameTag facial recognition concerns, LED disabling, patent filings
   - Apple glasses: ZERO investigative coverage despite identical camera hardware
   - Google/Samsung glasses: ZERO investigative coverage despite identical
     privacy implications

3. INDUSTRY ANALYSIS (Christopher Mims, columnist):
   - Balanced landscape coverage ("Smartglasses Are Inevitable. But What—
     or Who—Are They For?")
   - Gives Meta credit for market leadership (82% share)
   - Acknowledges privacy concerns across ALL companies

THE ASYMMETRY: When Nicole Nguyen covers surveillance cameras (Feb 2026), she
targets Ring (Amazon) and Nest (Google) — NOT Meta glasses. When Meghan
Bobrowsky covers smart glasses privacy (Jul 2026), she targets Meta exclusively
— NOT Apple, Google, or Samsung's upcoming glasses (which will have identical
camera hardware). Christopher Mims provides balanced industry analysis.

The READER EXPERIENCE at WSJ is: Apple smart glasses = exciting upcoming product
category (via Gurman/Bloomberg syndication and Mims industry analysis), Meta
smart glasses = privacy threat that "privacy advocates are up in arms" about
(via Bobrowsky investigative coverage).

NEWS CORP BALANCED-DEAL PARADOX: Despite News Corp having roughly symmetric
financial relationships with OpenAI ($50M/yr) and Meta ($50M/yr), the
beat assignment structure produces asymmetric coverage because:
- The CONSUMER tech voice (Nguyen) covers Apple products with product-utility framing
- The INVESTIGATIVE voice (Bobrowsky) covers Meta products with adversarial framing
- No reporter applies BOTH framings to BOTH companies

This extends Mechanism #56 (Verge beat segregation) from Penske/Vox Media
to News Corp/WSJ, demonstrating that beat assignment asymmetry is an
INDUSTRY-WIDE structural pattern, not unique to any one publication or
ownership structure.

CAREER PATH — Nicole Nguyen:
- PopSugar Tech (assistant tech editor, ~2013-2015)
- BuzzFeed News (tech reporter, Mar 2015 - Feb 2019, SF bureau under Mat Honan)
- WSJ (personal tech columnist, Feb 2019 - present, alongside Joanna Stern
  until Stern's departure May 2026)

BEAT MIGRATION NOTE: BuzzFeed News under Mat Honan (formerly of WIRED)
covered ALL tech companies adversarially. At WSJ, Nguyen's beat narrowed
to consumer product reviews and personal tech — the adversarial investigation
voice was structurally assigned to other reporters (Bobrowsky, Horwitz).

CONFOUNDING FACTORS:
1. STRONG: Ring/Nest ARE larger deployed surveillance networks than Meta glasses
   (millions of fixed cameras vs millions of wearable glasses) — legitimate editorial
   priority for a home surveillance article.
2. STRONG: Beat assignments are editorially rational — consumer tech columnists
   review products, investigative reporters investigate companies.
3. MODERATE: Nguyen may have covered Meta glasses in articles not found in this search.
4. MODERATE: Bobrowsky's Meta beat means she naturally covers Meta-specific issues.
5. WEAK: Consumer tech columnists at ALL publications tend toward product-positive
   framing — this is genre convention, not WSJ-specific.
6. WEAK: Nguyen covers Apple WWDC because of Apple event access, not editorial direction.

TESTABLE PREDICTIONS:
1. When Apple ships smart glasses with cameras (2027), WSJ's consumer tech column
   (Nguyen or successor) will frame them as product reviews with utility language.
   WSJ's investigative reporter will NOT apply the same "flooding the market" /
   "privacy advocates up in arms" framing to Apple glasses.
2. When Google/Samsung ship camera glasses (Fall 2026), Bobrowsky will NOT
   produce comparable adversarial coverage despite identical privacy implications.
3. Nguyen's coverage of Apple smart glasses will focus on features, design, and
   ecosystem integration — not on the privacy implications of always-on face cameras.
4. WSJ will not produce a "dragnet era" article about Meta glasses surveillance
   in the consumer tech column, even though Meta glasses are deployed at 7M+ units.

SOURCE URLS:
- Muck Rack profile: https://muckrack.com/nicole-nguyen-43/articles
- "The Dragnet Era of Home Security Cameras" (Feb 13, 2026):
  WSJ, Nicole Nguyen — targets Ring/Nest, not Meta glasses
- "WhatsApp Breaks Through Apple's Walled Garden" (Nov 20, 2025):
  WSJ, Nicole Nguyen — Meta WhatsApp in positive competitive framing
- "Apple's Tech Marvel Comes With Sacrifices" (Sep 11, 2025):
  WSJ, Nicole Nguyen — admiring iPhone Air review
- "Apple needs to copy Samsung" (Jan 2026):
  WSJ, Nicole Nguyen — framing Apple as needing to catch up
- Apple WWDC 2026 video report (Jun 2026):
  WSJ YouTube, Nicole Nguyen — event access coverage
- "Meta Is Flooding the Market With Smartglasses. Privacy Advocates Are Up in Arms."
  (Jul 14, 2026): WSJ, Meghan Bobrowsky — adversarial Meta glasses coverage
  https://www.wsj.com/tech/ai/meta-is-flooding-the-market-with-smartglasses-privacy-advocates-are-up-in-arms-8fb71539
- "Smartglasses Are Inevitable. But What—or Who—Are They For?" (Jun 26, 2026):
  WSJ, Christopher Mims — balanced industry analysis
  https://www.wsj.com/tech/ai/smart-glasses-market-meta-ai-8e6510b8
- WSJ hire announcement (Feb 2019):
  https://talkingbiznews.com/they-talk-biz-news/wsj-hires-buzzfeeds-nguyen-to-write-tech-column/amp/
- BuzzFeed SF bureau hire (2015):
  https://talkingbiznews.com/business-media-news/buzzfeed-hires-tech-journalists-for-san-francisco/
- Katch University interview:
  https://www.katchuniversity.com/post/nicole-nguyen
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
RESEARCH_FILE = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
NEWS_CORP_FILE = os.path.join(PROFILES_DIR, 'news-corp.yaml')
JOURNALISTS_FILE = os.path.join(PROFILES_DIR, 'careers', 'journalists.yaml')
ENTITIES_FILE = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')


def load_yaml(filepath):
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)


# ────────────────────────────────────────────────────────────────────
# 1. Nicole Nguyen Career Profile
# ────────────────────────────────────────────────────────────────────

class TestNguyenCareerProfile:
    """Nicole Nguyen's career profile must be complete in journalists.yaml."""

    def test_nguyen_exists_in_profiles(self):
        data = load_yaml(JOURNALISTS_FILE)
        names = [j.get('name') for j in data.get('journalists', [])]
        assert 'Nicole Nguyen' in names, \
            "Nicole Nguyen must be in journalists.yaml"

    def test_career_has_at_least_three_positions(self):
        data = load_yaml(JOURNALISTS_FILE)
        nguyen = next(j for j in data['journalists'] if j['name'] == 'Nicole Nguyen')
        assert len(nguyen.get('career', [])) >= 3, \
            "Career must include PopSugar, BuzzFeed, WSJ"

    def test_buzzfeed_position_documented(self):
        data = load_yaml(JOURNALISTS_FILE)
        nguyen = next(j for j in data['journalists'] if j['name'] == 'Nicole Nguyen')
        pubs = [c.get('publication', '').lower() for c in nguyen.get('career', [])]
        assert any('buzzfeed' in p for p in pubs), \
            "BuzzFeed News position must be documented"

    def test_wsj_current_position(self):
        data = load_yaml(JOURNALISTS_FILE)
        nguyen = next(j for j in data['journalists'] if j['name'] == 'Nicole Nguyen')
        career = nguyen.get('career', [])
        latest = career[-1]
        pub = latest.get('publication', '').lower()
        assert 'wsj' in pub or 'wall street journal' in pub, \
            "Current position must be at WSJ"

    def test_wsj_role_is_personal_tech(self):
        data = load_yaml(JOURNALISTS_FILE)
        nguyen = next(j for j in data['journalists'] if j['name'] == 'Nicole Nguyen')
        career = nguyen.get('career', [])
        latest = career[-1]
        role_or_beat = (latest.get('role', '') + ' ' + latest.get('beat', '')).lower()
        assert 'personal' in role_or_beat or 'consumer' in role_or_beat or 'columnist' in role_or_beat, \
            "WSJ role must reference personal tech / consumer tech / columnist"

    def test_multi_publication_flag(self):
        data = load_yaml(JOURNALISTS_FILE)
        nguyen = next(j for j in data['journalists'] if j['name'] == 'Nicole Nguyen')
        assert nguyen.get('multi_publication') is True, \
            "multi_publication must be True"

    def test_source_urls_present(self):
        data = load_yaml(JOURNALISTS_FILE)
        nguyen = next(j for j in data['journalists'] if j['name'] == 'Nicole Nguyen')
        urls = nguyen.get('source_urls', [])
        assert len(urls) >= 3, f"At least 3 source URLs needed, got {len(urls)}"


# ────────────────────────────────────────────────────────────────────
# 2. Competitor Coverage Section
# ────────────────────────────────────────────────────────────────────

class TestNguyenCompetitorCoverage:
    """Nicole Nguyen's competitor_coverage section must be documented."""

    def test_has_competitor_coverage(self):
        data = load_yaml(JOURNALISTS_FILE)
        nguyen = next(j for j in data['journalists'] if j['name'] == 'Nicole Nguyen')
        assert 'competitor_coverage' in nguyen, \
            "Must have competitor_coverage section"

    def test_has_cross_entity_analysis(self):
        data = load_yaml(JOURNALISTS_FILE)
        nguyen = next(j for j in data['journalists'] if j['name'] == 'Nicole Nguyen')
        cc = nguyen.get('competitor_coverage', {})
        assert 'cross_entity_analysis' in cc, \
            "Must have cross_entity_analysis"

    def test_mechanism_id_is_67(self):
        data = load_yaml(JOURNALISTS_FILE)
        nguyen = next(j for j in data['journalists'] if j['name'] == 'Nicole Nguyen')
        cc = nguyen.get('competitor_coverage', {})
        cea = cc.get('cross_entity_analysis', {})
        assert cea.get('mechanism_id') == 67, \
            f"Mechanism ID should be 67, got {cea.get('mechanism_id')}"

    def test_pattern_is_beat_assignment(self):
        data = load_yaml(JOURNALISTS_FILE)
        nguyen = next(j for j in data['journalists'] if j['name'] == 'Nicole Nguyen')
        cc = nguyen.get('competitor_coverage', {})
        cea = cc.get('cross_entity_analysis', {})
        pattern = cea.get('pattern', '')
        assert 'beat' in pattern.lower() or 'assignment' in pattern.lower(), \
            f"Pattern should reference beat assignment, got {pattern}"


# ────────────────────────────────────────────────────────────────────
# 3. Coverage Channel Analysis
# ────────────────────────────────────────────────────────────────────

class TestWSJCoverageChannels:
    """Verify the three WSJ coverage channels are documented."""

    def test_research_entry_exists(self):
        data = load_yaml(RESEARCH_FILE)
        findings = data.get('cross_publication_findings', {})
        assert 'wsj_beat_assignment_asymmetry' in findings, \
            "wsj_beat_assignment_asymmetry must exist in cross_publication_findings"

    def test_mechanism_id_67(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        assert entry.get('mechanism_id') == 67

    def test_three_coverage_channels(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        channels = entry.get('coverage_channels', [])
        assert len(channels) >= 3, f"Expected 3 channels, got {len(channels)}"

    def test_consumer_channel_is_nguyen(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        channels = entry.get('coverage_channels', [])
        consumer = [c for c in channels if c.get('type') == 'consumer_tech']
        assert len(consumer) >= 1, "Must have consumer_tech channel"
        assert 'Nguyen' in consumer[0].get('journalist', '')

    def test_investigative_channel_is_bobrowsky(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        channels = entry.get('coverage_channels', [])
        inv = [c for c in channels if c.get('type') == 'investigative']
        assert len(inv) >= 1, "Must have investigative channel"
        assert 'Bobrowsky' in inv[0].get('journalist', '')

    def test_industry_channel_is_mims(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        channels = entry.get('coverage_channels', [])
        industry = [c for c in channels if c.get('type') == 'industry_analysis']
        assert len(industry) >= 1, "Must have industry_analysis channel"
        assert 'Mims' in industry[0].get('journalist', '')


# ────────────────────────────────────────────────────────────────────
# 4. Nguyen Apple Coverage — Product-Utility Framing
# ────────────────────────────────────────────────────────────────────

class TestNguyenAppleCoverage:
    """Nicole Nguyen's Apple coverage uses product-utility framing."""

    def test_apple_coverage_documented(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        channels = entry.get('coverage_channels', [])
        consumer = [c for c in channels if c.get('type') == 'consumer_tech'][0]
        apple = consumer.get('apple_coverage', {})
        assert apple, "Apple coverage must be documented"

    def test_apple_framing_product_utility(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        channels = entry.get('coverage_channels', [])
        consumer = [c for c in channels if c.get('type') == 'consumer_tech'][0]
        apple = consumer.get('apple_coverage', {})
        framing = apple.get('framing', '').lower()
        assert 'product' in framing or 'utility' in framing or 'promotional' in framing, \
            f"Apple framing should be product/utility, got: {framing}"

    def test_apple_tone_neutral_to_positive(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        channels = entry.get('coverage_channels', [])
        consumer = [c for c in channels if c.get('type') == 'consumer_tech'][0]
        apple = consumer.get('apple_coverage', {})
        tone = apple.get('tone', 0)
        assert tone >= 0, f"Apple tone should be ≥ 0, got {tone}"

    def test_apple_wwdc_access(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        channels = entry.get('coverage_channels', [])
        consumer = [c for c in channels if c.get('type') == 'consumer_tech'][0]
        apple = consumer.get('apple_coverage', {})
        apple_str = str(apple).lower()
        assert 'wwdc' in apple_str, "WWDC coverage must be documented"

    def test_iphone_reviews_documented(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        channels = entry.get('coverage_channels', [])
        consumer = [c for c in channels if c.get('type') == 'consumer_tech'][0]
        apple = consumer.get('apple_coverage', {})
        articles = apple.get('sample_articles', [])
        assert len(articles) >= 2, f"At least 2 Apple articles needed, got {len(articles)}"


# ────────────────────────────────────────────────────────────────────
# 5. Nguyen Surveillance Coverage — Ring/Nest, NOT Meta Glasses
# ────────────────────────────────────────────────────────────────────

class TestNguyenSurveillanceCoverage:
    """Nguyen's surveillance coverage targets Ring/Nest, not Meta glasses."""

    def test_dragnet_article_documented(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        channels = entry.get('coverage_channels', [])
        consumer = [c for c in channels if c.get('type') == 'consumer_tech'][0]
        surveillance = consumer.get('surveillance_coverage', {})
        assert surveillance, "Surveillance coverage must be documented"

    def test_ring_nest_targeted(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        channels = entry.get('coverage_channels', [])
        consumer = [c for c in channels if c.get('type') == 'consumer_tech'][0]
        surveillance = consumer.get('surveillance_coverage', {})
        targets = str(surveillance.get('targets', '')).lower()
        assert 'ring' in targets or 'nest' in targets or 'amazon' in targets or 'google' in targets, \
            "Surveillance targets should include Ring or Nest"

    def test_meta_glasses_not_targeted(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        channels = entry.get('coverage_channels', [])
        consumer = [c for c in channels if c.get('type') == 'consumer_tech'][0]
        surveillance = consumer.get('surveillance_coverage', {})
        meta_targeted = surveillance.get('meta_glasses_targeted', False)
        assert meta_targeted is False, \
            "Nguyen's surveillance article should NOT target Meta glasses"


# ────────────────────────────────────────────────────────────────────
# 6. Bobrowsky Meta Coverage — Adversarial Framing
# ────────────────────────────────────────────────────────────────────

class TestBobrowskyMetaCoverage:
    """Bobrowsky's Meta coverage uses adversarial/surveillance framing."""

    def test_meta_framing_adversarial(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        channels = entry.get('coverage_channels', [])
        inv = [c for c in channels if c.get('type') == 'investigative'][0]
        meta = inv.get('meta_coverage', {})
        framing = meta.get('framing', '').lower()
        assert 'adversarial' in framing or 'surveillance' in framing or 'privacy' in framing, \
            f"Meta framing should be adversarial/surveillance, got: {framing}"

    def test_meta_tone_negative(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        channels = entry.get('coverage_channels', [])
        inv = [c for c in channels if c.get('type') == 'investigative'][0]
        meta = inv.get('meta_coverage', {})
        tone = meta.get('tone', 0)
        assert tone < 0, f"Meta tone should be negative, got {tone}"

    def test_flooding_article_documented(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        channels = entry.get('coverage_channels', [])
        inv = [c for c in channels if c.get('type') == 'investigative'][0]
        meta = inv.get('meta_coverage', {})
        articles = meta.get('sample_articles', [])
        titles = [a.get('title', '').lower() for a in articles]
        assert any('flooding' in t for t in titles), \
            "Must include 'flooding the market' article"

    def test_apple_investigative_coverage_zero(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        channels = entry.get('coverage_channels', [])
        inv = [c for c in channels if c.get('type') == 'investigative'][0]
        apple = inv.get('apple_coverage', {})
        articles = apple.get('investigative_articles', 0)
        assert articles == 0, \
            "Apple should have zero investigative articles from Bobrowsky"

    def test_google_samsung_investigative_coverage_zero(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        channels = entry.get('coverage_channels', [])
        inv = [c for c in channels if c.get('type') == 'investigative'][0]
        google = inv.get('google_coverage', {}).get('investigative_articles', 0)
        samsung = inv.get('samsung_coverage', {}).get('investigative_articles', 0)
        assert google == 0, "Google should have zero investigative articles"
        assert samsung == 0, "Samsung should have zero investigative articles"


# ────────────────────────────────────────────────────────────────────
# 7. News Corp Balanced-Deal Paradox
# ────────────────────────────────────────────────────────────────────

class TestNewsCorporpBalancedDealParadox:
    """Despite balanced deals, beat assignment produces asymmetric coverage."""

    def test_paradox_documented(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        assert 'balanced_deal_paradox' in entry, \
            "Balanced deal paradox must be documented"

    def test_openai_deal_amount(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        paradox = entry.get('balanced_deal_paradox', {})
        paradox_str = str(paradox).lower()
        assert '50m' in paradox_str or '50 million' in paradox_str or '$50m' in paradox_str, \
            "OpenAI deal amount ($50M/yr) should be documented"

    def test_meta_deal_amount(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        paradox = entry.get('balanced_deal_paradox', {})
        paradox_str = str(paradox)
        # Meta deal referenced
        assert 'Meta' in paradox_str, "Meta deal must be referenced"

    def test_asymmetry_despite_balance(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        paradox = entry.get('balanced_deal_paradox', {})
        finding = paradox.get('finding', '').lower()
        assert 'asymmetric' in finding or 'despite' in finding or 'paradox' in finding, \
            "Must note asymmetric coverage despite balanced deals"


# ────────────────────────────────────────────────────────────────────
# 8. Cross-References to Other Mechanisms
# ────────────────────────────────────────────────────────────────────

class TestCrossReferences:
    """Mechanism #67 must cross-reference related mechanisms."""

    def test_cross_references_exist(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        xrefs = entry.get('cross_references', [])
        assert len(xrefs) >= 3, f"At least 3 cross-references needed, got {len(xrefs)}"

    def test_references_verge_beat_segregation(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        xrefs = entry.get('cross_references', [])
        ref_ids = set()
        for xref in xrefs:
            if isinstance(xref, dict):
                ref_ids.add(xref.get('mechanism_id'))
            elif isinstance(xref, int):
                ref_ids.add(xref)
        assert 56 in ref_ids, "Must reference mechanism #56 (Verge beat segregation)"

    def test_references_gurman_access(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        xrefs = entry.get('cross_references', [])
        ref_ids = set()
        for xref in xrefs:
            if isinstance(xref, dict):
                ref_ids.add(xref.get('mechanism_id'))
            elif isinstance(xref, int):
                ref_ids.add(xref)
        assert 11 in ref_ids, "Must reference mechanism #11 (Gurman access dependency)"

    def test_references_cameron_mehrotra(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        xrefs = entry.get('cross_references', [])
        ref_ids = set()
        for xref in xrefs:
            if isinstance(xref, dict):
                ref_ids.add(xref.get('mechanism_id'))
            elif isinstance(xref, int):
                ref_ids.add(xref)
        assert 66 in ref_ids, "Must reference mechanism #66 (Cameron/Mehrotra investigative allocation)"


# ────────────────────────────────────────────────────────────────────
# 9. Confounding Factors
# ────────────────────────────────────────────────────────────────────

class TestConfoundingFactors:
    """Confounding factors must be documented for intellectual honesty."""

    def test_confounding_factors_exist(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        factors = entry.get('confounding_factors', [])
        assert len(factors) >= 4, f"At least 4 confounding factors needed, got {len(factors)}"

    def test_ring_nest_scale_acknowledged(self):
        """Ring/Nest ARE larger surveillance networks — legitimate editorial target."""
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        factors = entry.get('confounding_factors', [])
        factor_str = str(factors).lower()
        assert 'ring' in factor_str or 'nest' in factor_str or 'scale' in factor_str or 'deployed' in factor_str, \
            "Must acknowledge Ring/Nest scale as legitimate editorial priority"

    def test_beat_assignment_rationality_acknowledged(self):
        """Beat assignments are editorially rational."""
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        factors = entry.get('confounding_factors', [])
        factor_str = str(factors).lower()
        assert 'rational' in factor_str or 'editorial' in factor_str or 'convention' in factor_str, \
            "Must acknowledge beat assignments are editorially rational"

    def test_genre_convention_acknowledged(self):
        """Consumer tech columns inherently use product-positive framing."""
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        factors = entry.get('confounding_factors', [])
        factor_str = str(factors).lower()
        assert 'genre' in factor_str or 'convention' in factor_str or 'product' in factor_str, \
            "Must acknowledge genre convention"


# ────────────────────────────────────────────────────────────────────
# 10. Source URLs
# ────────────────────────────────────────────────────────────────────

class TestSourceURLs:
    """Source URLs must be present and properly formatted."""

    def test_at_least_seven_source_urls(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        urls = entry.get('source_urls', [])
        assert len(urls) >= 7, f"At least 7 source URLs needed, got {len(urls)}"

    def test_source_urls_start_with_http(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        urls = entry.get('source_urls', [])
        for url in urls:
            assert url.startswith('http'), f"URL must start with http: {url}"

    @pytest.mark.parametrize("expected_domain", [
        "wsj.com",
        "muckrack.com",
        "talkingbiznews.com",
    ])
    def test_key_domains_present(self, expected_domain):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        urls = entry.get('source_urls', [])
        found = [u for u in urls if expected_domain in u]
        assert len(found) > 0, f"Expected at least one URL from {expected_domain}"


# ────────────────────────────────────────────────────────────────────
# 11. Testable Predictions
# ────────────────────────────────────────────────────────────────────

class TestTestablePredictions:
    """Testable predictions must be documented."""

    def test_predictions_exist(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        predictions = entry.get('testable_predictions', [])
        assert len(predictions) >= 3, f"At least 3 predictions needed, got {len(predictions)}"

    def test_apple_glasses_prediction(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        predictions = entry.get('testable_predictions', [])
        pred_str = str(predictions).lower()
        assert 'apple' in pred_str and 'glasses' in pred_str, \
            "Must have Apple glasses prediction"

    def test_google_samsung_prediction(self):
        data = load_yaml(RESEARCH_FILE)
        entry = data['cross_publication_findings']['wsj_beat_assignment_asymmetry']
        predictions = entry.get('testable_predictions', [])
        pred_str = str(predictions).lower()
        assert 'google' in pred_str or 'samsung' in pred_str, \
            "Must have Google/Samsung prediction"


# ────────────────────────────────────────────────────────────────────
# 12. BuzzFeed Migration Effect
# ────────────────────────────────────────────────────────────────────

class TestBuzzFeedMigration:
    """BuzzFeed→WSJ career migration narrows adversarial beat scope."""

    def test_buzzfeed_adversarial_context(self):
        data = load_yaml(JOURNALISTS_FILE)
        nguyen = next(j for j in data['journalists'] if j['name'] == 'Nicole Nguyen')
        career = nguyen.get('career', [])
        bf = [c for c in career if 'buzzfeed' in c.get('publication', '').lower()]
        assert len(bf) >= 1, "BuzzFeed career must be documented"
        bf_notes = bf[0].get('notes', '').lower()
        assert 'adversarial' in bf_notes or 'investigative' in bf_notes or 'all tech' in bf_notes or \
               'mat honan' in bf_notes, \
            "BuzzFeed context should note adversarial/investigative scope under Mat Honan"

    def test_wsj_beat_narrowed(self):
        data = load_yaml(JOURNALISTS_FILE)
        nguyen = next(j for j in data['journalists'] if j['name'] == 'Nicole Nguyen')
        career = nguyen.get('career', [])
        wsj = [c for c in career if 'wsj' in c.get('publication', '').lower() or
               'wall street journal' in c.get('publication', '').lower()]
        assert len(wsj) >= 1, "WSJ career must be documented"
        wsj_beat = wsj[0].get('beat', '').lower()
        assert 'personal' in wsj_beat or 'consumer' in wsj_beat or 'product' in wsj_beat, \
            "WSJ beat should be personal tech / consumer products"
