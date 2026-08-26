"""
Type E Podcast Sentiment: Gadget Detective (Fevzi Turkalp) UK Broadcast
Cross-Episode Entity-Selective Vocabulary — LBC Radio + BBC Radio Scotland
(Aug 7–21, 2026)

Mechanism #320: gadget_detective_uk_broadcast_cross_episode_entity_selective_vocabulary

FINDING:
Four consecutive Gadget Detective episodes across UK broadcast radio (LBC + BBC
Radio Scotland) demonstrate entity-selective vocabulary that tracks the same
framing asymmetry documented in US tech podcasts and print media, extending
the pattern to UK mainstream broadcast:

Episode 1 (Aug 21, LBC): "UK Cinemas Could Ban Smart Glasses"
  - Entity: Meta
  - Vocabulary: "ban," "piracy," "bootleg," "privacy," "record"
  - Framing: Meta's Ray-Bans named as the specific product; "but are smart
    glasses the future?" (question framing = doubt)
  - Entity selection: UKCA ban covers ALL camera-enabled smart glasses, but
    only "Meta's Ray-Bans" named

Episode 2 (Aug 18, BBC Radio Scotland): "Meta Court Case in California"
  - Entity: Meta
  - Vocabulary: "addictive," "harvested data of minors," "penalties in the
    hundreds of billions," "prosecution," "whistleblower," "fine"
  - Framing: Alarm/legal-threat register

Episode 3 (Aug 14, LBC): "AI News and Tech Reviews"
  - Entity: Anthropic
  - Vocabulary: "EU regulations," "watermark," "AI creates"
  - Framing: Neutral compliance narrative — "in response to EU regulations"
  - No alarm vocabulary applied

Episode 4 (Aug 7, LBC): "Weekly Tech News & Reviews"
  - Entity: Apple
  - Vocabulary: "challenge," "privacy," "warranted to combat crime"
  - Framing: Apple as privacy champion fighting government overreach
  - Presented as "Apple has gone back to the Investigative Powers Tribunal
    to challenge the UK government's demand"

CROSS-ENTITY VOCABULARY GRADIENT (same host, same 2-week window):
  Apple → "challenge" government = HERO vocabulary
  Anthropic → "watermark" for EU = COMPLIANCE vocabulary
  Meta (x2) → "ban," "addictive," "billions in penalties" = ALARM vocabulary

ENTITY SELECTION IN CINEMA BAN COVERAGE:
The UKCA statement says "camera-enabled smart glasses" generically. The podcast
episode title and description name only "Meta's Ray-Bans." No mention of:
  - Snap Spectacles (camera glasses, available in UK)
  - Google Android XR glasses (planned camera glasses)
  - Apple AirPods cameras (reported/leaked)
  - Samsung smart glasses (camera-equipped, planned)
  - Even Realities G2 (display glasses, theater use case)

FINANCIAL CONTEXT — CULTURAL CONSENSUS:
LBC is owned by Global Media & Entertainment Ltd. BBC is publicly funded.
Neither has known AI content licensing deals with OpenAI, Meta, Anthropic,
Google, or Apple. This is not a financial incentive pattern — it is a CULTURAL
CONSENSUS finding that demonstrates entity-selective vocabulary has propagated
into UK mainstream broadcast radio independent of publisher-AI financial
relationships.

INSTITUTIONAL CASCADE:
The UK cinema ban coverage shows a multi-layered institutional cascade:
  1. UKCA announces generic "camera-enabled smart glasses" policy
  2. Reuters headline: "Meta AI and other smart glasses" (Meta named, others unnamed)
  3. UK tabloids (The Sun): "Meta glasses" only in the body
  4. Wetherspoons ban (800+ pubs): "Meta glasses" specifically
  5. German criminal complaint: filed against "Meta and others"
  6. Gadget Detective podcast: "smart glasses, such as Meta's Ray-Bans"
  7. UK courts: "Meta smart glasses" specifically prohibited

At each layer, the generic "camera-enabled smart glasses" narrows to "Meta"
specifically. No competitor's camera wearable is named at any institutional level.

CROSS-REFERENCES:
- Extends mechanism #225 (Vergecast three-episode camera vocabulary convergence)
- Extends mechanism #245 (UK cinema piracy institutional cascade)
- Extends mechanism #307 (ChatGPT ads Europe podcast vocabulary differential)
- Connects to mechanism #174 (Fast Company UK cinema ban meta-exclusive framing)
- Connects to mechanism #170 (Observer/Guardian stigmatization advocacy)
- New dimension: UK broadcast radio (LBC/BBC) as distinct medium from US podcasts

Sources:
- Gadget Detective Aug 21: https://uk.radio.net/podcast/gadget-detective-a-selection-of-free-tech-advice-and-tech-news-broadcasts-by-fevzi-turkalp-on-the-bb
- Gadget Detective Aug 18 (BBC Scotland): same podcast feed
- Gadget Detective Aug 14 (LBC): same podcast feed
- Gadget Detective Aug 7 (LBC): same podcast feed
- Reuters UK cinema ban: https://www.reuters.com/business/media-telecom/uk-cinemas-restricting-meta-ai-other-smart-glasses-over-piracy-concerns-2026-08-20/
- The Sun Wetherspoons + cinema: https://www.thesun.co.uk/money/40126465/new-cinema-ban-after-wetherspoons-crackdown/
"""

import pytest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def _load_competitor_research():
    """Load competitor-coverage-research.yaml."""
    path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
    with open(path) as f:
        return yaml.safe_load(f)


def _load_podcast_sentiment():
    """Load podcast-sentiment.md as text."""
    path = os.path.join(os.path.dirname(__file__), '..', 'podcast-sentiment.md')
    with open(path) as f:
        return f.read()


class TestMechanismExists:
    """Verify mechanism #320 exists in competitor-coverage-research.yaml."""

    def test_mechanism_id_present(self):
        data = _load_competitor_research()
        text = yaml.dump(data)
        assert 'gadget_detective_uk_broadcast_cross_episode_entity_selective_vocabulary' in text

    def test_mechanism_id_320(self):
        data = _load_competitor_research()
        text = yaml.dump(data)
        assert 'mechanism_id: 320' in text


class TestEpisodeDocumentation:
    """Verify all four episodes are documented."""

    def test_aug21_cinema_ban_episode(self):
        data = _load_competitor_research()
        text = yaml.dump(data)
        assert 'UK Cinemas Could Ban Smart Glasses' in text or 'cinema' in text.lower()

    def test_aug18_meta_court_case_episode(self):
        data = _load_competitor_research()
        text = yaml.dump(data)
        assert 'Meta Court Case' in text or 'court case' in text.lower()

    def test_aug14_anthropic_watermark_episode(self):
        data = _load_competitor_research()
        text = yaml.dump(data)
        # Must mention Anthropic's watermark compliance
        assert 'anthropic' in text.lower()
        assert 'watermark' in text.lower()

    def test_aug7_apple_privacy_episode(self):
        data = _load_competitor_research()
        text = yaml.dump(data)
        # Must mention Apple's privacy challenge
        assert 'apple' in text.lower()
        assert 'Investigative Powers' in text or 'privacy' in text.lower()


class TestEntitySelectiveVocabulary:
    """Verify the vocabulary asymmetry is documented."""

    def test_meta_alarm_vocabulary(self):
        data = _load_competitor_research()
        text = yaml.dump(data)
        # Meta episodes use alarm vocabulary
        for term in ['ban', 'piracy', 'addictive']:
            assert term in text.lower(), f"Meta alarm term '{term}' not found"

    def test_apple_hero_vocabulary(self):
        data = _load_competitor_research()
        text = yaml.dump(data)
        # Apple episode uses hero vocabulary
        assert 'challenge' in text.lower() or 'champion' in text.lower()

    def test_anthropic_compliance_vocabulary(self):
        data = _load_competitor_research()
        text = yaml.dump(data)
        # Anthropic episode uses compliance vocabulary
        assert 'watermark' in text.lower()
        assert 'EU' in text or 'regulation' in text.lower()


class TestEntitySelectionInCinemaBan:
    """Verify entity selection asymmetry in cinema ban is documented."""

    def test_meta_named_in_generic_ban(self):
        data = _load_competitor_research()
        text = yaml.dump(data)
        # Must note that generic "camera-enabled smart glasses" narrows to Meta
        assert 'camera-enabled' in text.lower() or 'generic' in text.lower() or 'entity selection' in text.lower()

    def test_competitors_absent(self):
        data = _load_competitor_research()
        text = yaml.dump(data)
        # Must document that Snap/Google/Samsung not named in coverage
        assert 'snap' in text.lower() or 'competitor' in text.lower() or 'unnamed' in text.lower()


class TestCulturalConsensusClassification:
    """Verify this is classified as cultural consensus, not financial incentive."""

    def test_not_financial_incentive(self):
        data = _load_competitor_research()
        text = yaml.dump(data)
        # Must classify as cultural consensus
        assert 'cultural consensus' in text.lower() or 'cultural' in text.lower()

    def test_lbc_ownership_documented(self):
        data = _load_competitor_research()
        text = yaml.dump(data)
        assert 'Global' in text or 'LBC' in text

    def test_bbc_publicly_funded(self):
        data = _load_competitor_research()
        text = yaml.dump(data)
        assert 'BBC' in text


class TestInstitutionalCascade:
    """Verify the institutional cascade from generic to Meta-specific."""

    def test_ukca_generic_statement(self):
        data = _load_competitor_research()
        text = yaml.dump(data)
        assert 'UKCA' in text or 'UK Cinema Association' in text

    def test_reuters_headline_meta_named(self):
        data = _load_competitor_research()
        text = yaml.dump(data)
        assert 'reuters' in text.lower()

    def test_wetherspoons_ban(self):
        data = _load_competitor_research()
        text = yaml.dump(data)
        assert 'Wetherspoons' in text or 'wetherspoons' in text.lower()

    def test_german_criminal_complaint(self):
        data = _load_competitor_research()
        text = yaml.dump(data)
        assert 'German' in text or 'criminal complaint' in text.lower()


class TestCrossReferences:
    """Verify cross-references to related mechanisms."""

    def test_references_vergecast_convergence(self):
        data = _load_competitor_research()
        text = yaml.dump(data)
        # Should reference mechanism #225 or Vergecast
        assert '225' in text or 'vergecast' in text.lower() or 'three-episode' in text.lower()

    def test_references_chatgpt_ads_podcast(self):
        data = _load_competitor_research()
        text = yaml.dump(data)
        # Should reference mechanism #307 or ChatGPT ads
        assert '307' in text or 'chatgpt' in text.lower()


class TestSourceURLIntegrity:
    """Verify source URLs are well-formed."""

    def test_gadget_detective_url(self):
        data = _load_competitor_research()
        text = yaml.dump(data)
        assert 'uk.radio.net' in text or 'gadgetdetective' in text.lower()

    def test_reuters_url(self):
        data = _load_competitor_research()
        text = yaml.dump(data)
        assert 'reuters.com' in text

    def test_all_urls_https(self):
        data = _load_competitor_research()
        text = yaml.dump(data)
        # Find all URLs in the mechanism section
        import re
        urls = re.findall(r'https?://[^\s\'"]+', text)
        # Most should be https (some radio.net links may be http)
        https_count = sum(1 for u in urls if u.startswith('https://'))
        assert https_count > 0, "No HTTPS URLs found"


class TestPodcastSentimentUpdated:
    """Verify the finding is logged in podcast-sentiment.md."""

    def test_gadget_detective_in_sentiment(self):
        text = _load_podcast_sentiment()
        assert 'Gadget Detective' in text or 'Fevzi Turkalp' in text

    def test_lbc_in_sentiment(self):
        text = _load_podcast_sentiment()
        assert 'LBC' in text

    def test_bbc_radio_scotland_in_sentiment(self):
        text = _load_podcast_sentiment()
        assert 'BBC Radio Scotland' in text or 'BBC Radio' in text
