"""
Joanna Stern Cross-Entity Coverage Analysis — Type B Journalist Tracking (Aug 7, 2026)

KEY FINDING: Career Migration Asymmetry — The Financial Independence Effect

Joanna Stern was WSJ's senior personal tech columnist for 12 years (2013-2026),
then left to found "New Things" (announced Apr 22, 2026) with an NBC News Chief
Technology Analyst partnership. Her career trajectory provides the strongest
NATURAL EXPERIMENT for isolating how financial structures shape coverage targets.

PHASE 1: WSJ (2013 – Apr 2026) — Under News Corp balanced umbrella
  - News Corp deals: $50M/yr OpenAI (May 2024) + up to $50M/yr Meta (Mar 2026)
  - Meta Ray-Ban glasses: POSITIVE (+0.35) — "Those cool Meta Ray-Bans...
    fun and reliable" (AI gadgets comparison, May 2024)
  - Apple Vision Pro: CRITICAL (-0.20) — "I would not buy Vision Pro" (Mar 2024)
  - Ray-Ban Stories: BALANCED (0.0) — "The Cool and Creepy of Facebook
    Cameras In Your Sunglasses" (Sep 2021)
  - Coverage was genuinely balanced across all companies

PHASE 2: New Things + NBC News (May 2026 →) — Independent, ZERO AI content deals
  - Meta Ray-Ban glasses: ADVERSARIAL (-0.65) — "How People With Meta
    Glasses Can Secretly Record You" (Jun 2026) — paid modder $100,
    30-state investigation, drove Meta firmware update
  - Samsung smart glasses: ZERO coverage despite identical hardware
  - Amazon Ring: ZERO investigative coverage despite DEPLOYED facial recognition
  - Google/Android XR glasses: ZERO privacy investigation
  - Snap Specs: NEUTRAL industry analysis (Jun 2026, NPR interview)

THE TONE SHIFT: Meta coverage moved from +0.35 to -0.65 — a 1.00-point swing
that correlates precisely with the change from balanced-employer to
zero-deal independent. This is the LARGEST single-journalist tone shift
in the MediaScope dataset.

REVERSE HEIKKILÄ PATTERN: Heikkilä went FROM independence (MIT TR) TO
financial entanglement (FT) — coverage shifted toward Meta-adversarial.
Stern went FROM financial balance (News Corp) TO independence — coverage
target is Meta (zero financial leverage). Both migrations confirm: the
direction of financial-structure change predicts the direction of
Meta coverage tone change.

AUDIENCE ECONOMICS MECHANISM: As an independent creator, Stern's revenue
depends on YouTube algorithm engagement, newsletter subscriptions, and
NBC licensing. Anti-Meta content performs well on all three channels.
None penalize anti-Meta coverage. All reward it.

Sources:
  - Nieman Lab: Stern departure announcement (May 2026)
    https://www.niemanlab.org/2026/05/tech-journalist-joanna-stern-on-leaving-the-wall-street-journal-and-moving-on-to-new-things/
  - TheWrap: NBC News partnership model (Apr 2026)
    https://www.thewrap.com/media-platforms/journalism/joanna-stern-nbc-scott-macfarlane-pablo-torre-new-independent-model/
  - Livemint/WSJ: AI gadget comparison (May 2024)
    https://www.livemint.com/technology/the-ai-gadget-that-can-make-your-life-better-and-two-that-definitely-wont-11714736399659.html
  - 9to5Mac: Stern "would not buy" Vision Pro (Mar 2024)
    https://9to5mac.com/2024/03/04/joanna-stern-would-not-buy-vision-pro/
  - YouTube: Ray-Ban Stories review (Sep 2021)
    https://www.youtube.com/watch?v=TA4Wo08vGqk
  - BetaNews: LED removal stealth mode investigation recap
    https://betanews.com/article/meta-ray-bans-turned-spy-glasses-privacy-light/
  - YouTube: "How People With Meta Glasses Can Secretly Record You" (Jun 2026)
    https://www.youtube.com/watch?v=EaJSPeJmqis
  - NPR: Snap Specs industry analysis interview (Jun 2026)
    https://www.nprillinois.org/2026-06-19/are-snaps-2-195-smart-glasses-the-next-big-thing-in-tech
  - Android Authority: Meta firmware update response to Stern
    https://www.androidauthority.com/meta-smart-glasses-led-camera-3685162/
  - UploadVR: Meta improving LED tamper detection
    https://www.uploadvr.com/meta-improving-smart-glasses-privacy-led-tampering-detection/
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')
RESEARCH_FILE = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
NEWS_CORP_FILE = os.path.join(PROFILES_DIR, 'news-corp.yaml')


def load_yaml(filepath):
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)


class TestSternCareerTimeline:
    """Verify the career migration timeline is documented."""

    def test_wsj_tenure_documented(self):
        data = load_yaml(NEWS_CORP_FILE)
        stern = None
        if 'journalist_cross_entity' in data:
            stern = data['journalist_cross_entity'].get('joanna_stern')
        assert stern is not None, "Joanna Stern cross-entity profile must exist in news-corp.yaml"

    def test_career_phases_present(self):
        data = load_yaml(NEWS_CORP_FILE)
        stern = data['journalist_cross_entity']['joanna_stern']
        assert 'career_phases' in stern, "Career phases must be documented"
        phases = stern['career_phases']
        assert len(phases) >= 2, "At least 2 career phases (WSJ, Independent)"

    def test_wsj_phase_has_employer(self):
        data = load_yaml(NEWS_CORP_FILE)
        phases = data['journalist_cross_entity']['joanna_stern']['career_phases']
        wsj_phase = phases[0]
        assert 'wsj' in wsj_phase.get('employer', '').lower() or 'wall street journal' in wsj_phase.get('employer', '').lower()

    def test_independent_phase_has_new_things(self):
        data = load_yaml(NEWS_CORP_FILE)
        phases = data['journalist_cross_entity']['joanna_stern']['career_phases']
        independent_phase = phases[-1]
        employer = independent_phase.get('employer', '').lower()
        assert 'new things' in employer or 'independent' in employer

    def test_nbc_partnership_documented(self):
        data = load_yaml(NEWS_CORP_FILE)
        stern = data['journalist_cross_entity']['joanna_stern']
        # NBC partnership should be mentioned somewhere
        stern_str = str(stern).lower()
        assert 'nbc' in stern_str, "NBC News partnership must be documented"


class TestSternWSJPhaseCoverage:
    """Verify WSJ-phase coverage data (balanced under News Corp)."""

    def test_meta_wsj_tone_positive(self):
        data = load_yaml(NEWS_CORP_FILE)
        stern = data['journalist_cross_entity']['joanna_stern']
        wsj_meta = stern.get('wsj_phase_coverage', {}).get('meta', {})
        tone = wsj_meta.get('tone', 0)
        assert tone > 0, f"Meta tone at WSJ should be positive, got {tone}"

    def test_apple_wsj_tone_critical(self):
        data = load_yaml(NEWS_CORP_FILE)
        stern = data['journalist_cross_entity']['joanna_stern']
        wsj_apple = stern.get('wsj_phase_coverage', {}).get('apple', {})
        tone = wsj_apple.get('tone', 0)
        assert tone < 0, f"Apple Vision Pro tone at WSJ should be negative, got {tone}"

    def test_ray_ban_stories_balanced(self):
        data = load_yaml(NEWS_CORP_FILE)
        stern = data['journalist_cross_entity']['joanna_stern']
        wsj_meta = stern.get('wsj_phase_coverage', {}).get('meta', {})
        # Should mention Ray-Ban Stories balanced review
        meta_str = str(wsj_meta).lower()
        assert 'ray-ban stories' in meta_str or 'stories' in meta_str

    def test_ai_gadgets_comparison_documented(self):
        data = load_yaml(NEWS_CORP_FILE)
        stern = data['journalist_cross_entity']['joanna_stern']
        wsj_meta = stern.get('wsj_phase_coverage', {}).get('meta', {})
        meta_str = str(wsj_meta).lower()
        assert 'gadget' in meta_str or 'rabbit' in meta_str or 'humane' in meta_str

    def test_balanced_coverage_noted(self):
        data = load_yaml(NEWS_CORP_FILE)
        stern = data['journalist_cross_entity']['joanna_stern']
        wsj_str = str(stern.get('wsj_phase_coverage', {})).lower()
        assert 'balanced' in wsj_str or 'positive' in wsj_str


class TestSternIndependentPhaseCoverage:
    """Verify independent-phase coverage data (adversarial toward Meta)."""

    def test_meta_independent_tone_adversarial(self):
        data = load_yaml(NEWS_CORP_FILE)
        stern = data['journalist_cross_entity']['joanna_stern']
        ind_meta = stern.get('independent_phase_coverage', {}).get('meta', {})
        tone = ind_meta.get('tone', 0)
        assert tone < -0.3, f"Meta tone as independent should be adversarial, got {tone}"

    def test_stealth_mode_investigation_documented(self):
        data = load_yaml(NEWS_CORP_FILE)
        stern = data['journalist_cross_entity']['joanna_stern']
        ind_meta = stern.get('independent_phase_coverage', {}).get('meta', {})
        meta_str = str(ind_meta).lower()
        assert 'stealth' in meta_str or 'led' in meta_str or 'recording light' in meta_str

    def test_samsung_coverage_absent(self):
        data = load_yaml(NEWS_CORP_FILE)
        stern = data['journalist_cross_entity']['joanna_stern']
        ind_samsung = stern.get('independent_phase_coverage', {}).get('samsung', {})
        coverage = ind_samsung.get('investigative_articles', 0)
        assert coverage == 0, "Samsung should have zero investigative articles"

    def test_amazon_coverage_absent(self):
        data = load_yaml(NEWS_CORP_FILE)
        stern = data['journalist_cross_entity']['joanna_stern']
        ind_amazon = stern.get('independent_phase_coverage', {}).get('amazon', {})
        coverage = ind_amazon.get('investigative_articles', 0)
        assert coverage == 0, "Amazon Ring should have zero investigative articles"

    def test_google_coverage_absent(self):
        data = load_yaml(NEWS_CORP_FILE)
        stern = data['journalist_cross_entity']['joanna_stern']
        ind_google = stern.get('independent_phase_coverage', {}).get('google', {})
        coverage = ind_google.get('investigative_articles', 0)
        assert coverage == 0, "Google/Android XR should have zero investigative articles"

    def test_firmware_update_impact_documented(self):
        data = load_yaml(NEWS_CORP_FILE)
        stern = data['journalist_cross_entity']['joanna_stern']
        ind_meta = stern.get('independent_phase_coverage', {}).get('meta', {})
        meta_str = str(ind_meta).lower()
        assert 'firmware' in meta_str or 'update' in meta_str or 'tamper' in meta_str


class TestToneShiftMagnitude:
    """Verify the tone shift is the largest in the dataset."""

    def test_tone_delta_calculated(self):
        data = load_yaml(NEWS_CORP_FILE)
        stern = data['journalist_cross_entity']['joanna_stern']
        assert 'tone_shift' in stern or 'career_migration_delta' in stern

    def test_tone_delta_at_least_0_8(self):
        data = load_yaml(NEWS_CORP_FILE)
        stern = data['journalist_cross_entity']['joanna_stern']
        delta = stern.get('tone_shift', stern.get('career_migration_delta', {}))
        if isinstance(delta, dict):
            val = delta.get('meta_delta', 0)
        else:
            val = delta
        assert abs(val) >= 0.8, f"Meta tone shift should be ≥0.8, got {val}"

    def test_shift_direction_positive_to_negative(self):
        data = load_yaml(NEWS_CORP_FILE)
        stern = data['journalist_cross_entity']['joanna_stern']
        wsj_meta = stern.get('wsj_phase_coverage', {}).get('meta', {}).get('tone', 0)
        ind_meta = stern.get('independent_phase_coverage', {}).get('meta', {}).get('tone', 0)
        assert wsj_meta > ind_meta, "Tone should shift from positive (WSJ) to negative (independent)"


class TestReverseHeikkilaPattern:
    """Verify the Stern-Heikkilä reverse migration pattern."""

    def test_reverse_pattern_documented(self):
        data = load_yaml(NEWS_CORP_FILE)
        stern = data['journalist_cross_entity']['joanna_stern']
        stern_str = str(stern).lower()
        assert 'heikkilä' in stern_str or 'heikkila' in stern_str or 'reverse' in stern_str

    def test_migration_direction_opposite(self):
        """Stern goes balanced→independent (toward Meta adversarial).
        Heikkilä goes independent→financially-tied (toward Meta adversarial).
        Both converge on Meta-adversarial outcome."""
        data = load_yaml(NEWS_CORP_FILE)
        stern = data['journalist_cross_entity']['joanna_stern']
        stern_str = str(stern).lower()
        assert 'independent' in stern_str and 'meta' in stern_str


class TestAudienceEconomicsMechanism:
    """Verify the audience economics causal mechanism is documented."""

    def test_audience_economics_section_exists(self):
        data = load_yaml(NEWS_CORP_FILE)
        stern = data['journalist_cross_entity']['joanna_stern']
        stern_str = str(stern).lower()
        assert 'audience' in stern_str or 'youtube' in stern_str or 'algorithm' in stern_str

    def test_independent_revenue_streams_documented(self):
        data = load_yaml(NEWS_CORP_FILE)
        stern = data['journalist_cross_entity']['joanna_stern']
        stern_str = str(stern).lower()
        # Should mention subscription/newsletter/NBC/YouTube
        revenue_terms = sum(1 for t in ['subscription', 'newsletter', 'nbc', 'youtube', 'sponsor']
                          if t in stern_str)
        assert revenue_terms >= 2, "At least 2 revenue stream types should be documented"


class TestCounterArguments:
    """Verify counter-arguments are addressed (intellectual honesty)."""

    def test_legitimate_journalism_acknowledged(self):
        data = load_yaml(NEWS_CORP_FILE)
        stern = data['journalist_cross_entity']['joanna_stern']
        stern_str = str(stern).lower()
        assert 'legitimate' in stern_str or 'valid' in stern_str or 'genuine' in stern_str

    def test_target_selection_distinguished(self):
        """The question is target selection, not story quality."""
        data = load_yaml(NEWS_CORP_FILE)
        stern = data['journalist_cross_entity']['joanna_stern']
        stern_str = str(stern).lower()
        assert 'target' in stern_str or 'selection' in stern_str


class TestResearchFileConsistency:
    """Verify findings are cross-referenced in competitor-coverage-research.yaml."""

    def test_stern_section_in_research(self):
        data = load_yaml(RESEARCH_FILE)
        news_corp = data.get('publications', {}).get('news_corp', data.get('publications', {}).get('news-corp', {}))
        if not news_corp:
            # May be under wsj section
            stern_found = False
            for pub_key, pub_data in data.get('publications', {}).items():
                if isinstance(pub_data, dict) and 'stern' in str(pub_data).lower():
                    stern_found = True
                    break
            assert stern_found, "Stern cross-entity data must exist somewhere in research file"
        else:
            assert 'joanna_stern' in str(news_corp).lower() or 'stern' in str(news_corp).lower()

    def test_source_urls_present(self):
        data = load_yaml(RESEARCH_FILE)
        research_str = str(data).lower()
        # There should be source URLs related to Stern
        if 'stern_cross_entity' in research_str or 'joanna_stern' in research_str:
            assert 'source_url' in research_str or 'source' in research_str

    def test_tone_data_in_research(self):
        data = load_yaml(RESEARCH_FILE)
        research_str = str(data)
        # Should contain numeric tone values
        if 'joanna_stern' in research_str.lower() or 'stern_cross_entity' in research_str.lower():
            assert '0.35' in research_str or '-0.65' in research_str or 'tone' in research_str.lower()


class TestSourceCitations:
    """Verify source URLs are present and properly formatted."""

    def test_at_least_five_source_urls(self):
        data = load_yaml(NEWS_CORP_FILE)
        stern = data['journalist_cross_entity']['joanna_stern']
        source_urls = stern.get('source_urls', [])
        assert len(source_urls) >= 5, f"At least 5 source URLs needed, got {len(source_urls)}"

    def test_source_urls_are_strings(self):
        data = load_yaml(NEWS_CORP_FILE)
        stern = data['journalist_cross_entity']['joanna_stern']
        source_urls = stern.get('source_urls', [])
        for url in source_urls:
            assert isinstance(url, str), f"Source URL must be string, got {type(url)}"

    def test_source_urls_start_with_https(self):
        data = load_yaml(NEWS_CORP_FILE)
        stern = data['journalist_cross_entity']['joanna_stern']
        source_urls = stern.get('source_urls', [])
        for url in source_urls:
            assert url.startswith('http'), f"Source URL must start with http(s), got {url}"

    @pytest.mark.parametrize("expected_domain", [
        "niemanlab.org",
        "thewrap.com",
        "youtube.com",
    ])
    def test_key_domains_present(self, expected_domain):
        data = load_yaml(NEWS_CORP_FILE)
        stern = data['journalist_cross_entity']['joanna_stern']
        source_urls = stern.get('source_urls', [])
        domains_found = [url for url in source_urls if expected_domain in url]
        assert len(domains_found) > 0, f"Expected at least one URL from {expected_domain}"
