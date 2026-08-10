"""
Financial Times × OpenAI Hardware Privacy Double Standard — Mechanism #18

Type A: Competitor Coverage Deep Dive (Aug 9, 2026 23:00 PT)

Publication: Financial Times (Nikkei Inc.)
Competitor: OpenAI (io hardware device)
Comparison: Same publication's Meta Ray-Ban glasses coverage

FINDING — Mechanism #18: Hardware Privacy Framing Inversion

The FT's documented always_on_device_dual_standard shows that the same publication
frames functionally identical always-on sensing technology with opposite privacy
registers depending on manufacturer identity:

- OpenAI device (camera, mic, always-on, contextual memory): "normal development,"
  "a friend who's a computer," "iPhone of AI." Privacy = design challenge.
- Meta glasses (camera, mic, always-on, contextual memory): "surveillance infrastructure,"
  "wiretapping laws," "biometric data laws." Privacy = societal threat.

Financial chain: FT-OpenAI content deal ($5-10M/yr, announced Apr 2024). No FT-Meta deal.

This formalizes the existing always_on_device_dual_standard as Mechanism #18 in the
MediaScope mechanism catalogue, extending the Dual-Lens Paradox (Mechanism #7) with
a specific hardware privacy framing inversion.

Sources:
- FT George Hammond/Murgia: OpenAI Jony Ive device (Oct 5, 2025) — paywalled,
  corroborated by TechCrunch, Livemint, PYMNTS, Notebookcheck, Android Authority
- FT George Hammond/Murgia: OpenAI Jony Ive device update (Jun 2026) — paywalled,
  corroborated by Outlook Business, Windows Central
- FT Hannah Murphy: Meta glasses continuous recording (Jul 8, 2026) — Techmeme #1
- FT Murgia: FT-OpenAI deal announcement (Apr 29, 2024)
"""

import yaml
import os
import pytest

PROFILE_PATH = os.path.join(
    os.path.dirname(__file__), '..', 'profiles', 'financial-times.yaml'
)


@pytest.fixture(scope='module')
def ft_profile():
    with open(PROFILE_PATH) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='module')
def dual_standard(ft_profile):
    """Find the always_on_device_dual_standard section."""
    section = _find_section(ft_profile, 'always_on_device_dual_standard')
    assert section is not None, (
        "Missing always_on_device_dual_standard section in financial-times.yaml"
    )
    return section


# ── Class 1: Section Structure ──────────────────────────────────────


class TestSectionStructure:
    """Verify the always_on_device_dual_standard section has required structural fields."""

    def test_section_exists(self, dual_standard):
        assert dual_standard is not None

    def test_has_finding(self, dual_standard):
        assert 'finding' in dual_standard
        assert len(dual_standard['finding']) > 100

    def test_has_mechanism_id(self, dual_standard):
        """Mechanism #18 formalization must be present."""
        assert 'mechanism_id' in dual_standard
        assert str(dual_standard['mechanism_id']) == '18'

    def test_has_mechanism_name(self, dual_standard):
        assert 'name' in dual_standard
        name = dual_standard['name'].lower()
        assert 'privacy' in name or 'hardware' in name or 'framing' in name

    def test_has_date_analyzed(self, dual_standard):
        assert 'date_analyzed' in dual_standard
        assert '2026-08' in dual_standard['date_analyzed']


# ── Class 2: OpenAI Device Coverage ─────────────────────────────────


class TestOpenAIDeviceCoverage:
    """Verify the OpenAI hardware device coverage data."""

    def test_openai_section_exists(self, dual_standard):
        assert 'openai_device_coverage' in dual_standard

    def test_openai_has_reporter(self, dual_standard):
        device = dual_standard['openai_device_coverage']
        assert 'reporter' in device
        reporter = device['reporter'].lower()
        assert any(name in reporter for name in ['hammond', 'murgia'])

    def test_openai_has_articles(self, dual_standard):
        device = dual_standard['openai_device_coverage']
        assert 'articles' in device
        assert len(device['articles']) >= 1

    def test_openai_article_has_url(self, dual_standard):
        device = dual_standard['openai_device_coverage']
        first_article = device['articles'][0]
        assert 'url' in first_article

    def test_openai_article_has_framing(self, dual_standard):
        device = dual_standard['openai_device_coverage']
        first_article = device['articles'][0]
        assert 'framing' in first_article
        framing = first_article['framing'].lower()
        assert 'constructive' in framing or 'neutral' in framing

    def test_openai_article_has_language_examples(self, dual_standard):
        device = dual_standard['openai_device_coverage']
        first_article = device['articles'][0]
        assert 'language' in first_article
        assert len(first_article['language']) >= 3

    def test_openai_privacy_is_design_challenge(self, dual_standard):
        """Privacy must be framed as design challenge, not threat."""
        device = dual_standard['openai_device_coverage']
        first_article = device['articles'][0]
        treatment = str(first_article.get('privacy_treatment', '')).lower()
        assert 'challenge' in treatment or 'not threat' in treatment

    def test_openai_language_contains_aspirational_terms(self, dual_standard):
        """Language should include at least one aspirational/sympathetic term."""
        device = dual_standard['openai_device_coverage']
        all_language = []
        for article in device['articles']:
            all_language.extend(article.get('language', []))
        lang_text = ' '.join(all_language).lower()
        aspirational = ['friend', 'iphone', 'assistant', 'normal', 'better']
        assert any(term in lang_text for term in aspirational), \
            f"Expected aspirational language, got: {lang_text[:200]}"

    def test_openai_language_lacks_surveillance_terms(self, dual_standard):
        """OpenAI coverage should NOT use surveillance-coded language as applied framing.
        Negation contexts like 'not surveillance implications' are acceptable."""
        device = dual_standard['openai_device_coverage']
        all_language = []
        for article in device['articles']:
            all_language.extend(article.get('language', []))
        # Check each language item individually — negation contexts are OK
        for item in all_language:
            item_lower = item.lower()
            # Skip items that explicitly negate the term (e.g., "not surveillance")
            if any(neg in item_lower for neg in ['not surveillance', 'not privacy violation',
                                                   'not wiretapping', 'not biometric']):
                continue
            for alarm in ['surveillance infrastructure', 'wiretapping laws', 'biometric data laws']:
                assert alarm not in item_lower, \
                    f"OpenAI coverage should not use '{alarm}' as applied framing, but found in: {item}"


# ── Class 3: Meta Glasses Coverage ──────────────────────────────────


class TestMetaGlassesCoverage:
    """Verify the Meta glasses coverage data."""

    def test_meta_section_exists(self, dual_standard):
        assert 'meta_glasses_coverage' in dual_standard

    def test_meta_has_reporter(self, dual_standard):
        meta = dual_standard['meta_glasses_coverage']
        assert 'reporter' in meta
        assert 'murphy' in meta['reporter'].lower()

    def test_meta_has_articles(self, dual_standard):
        meta = dual_standard['meta_glasses_coverage']
        assert 'articles' in meta
        assert len(meta['articles']) >= 1

    def test_meta_article_has_url(self, dual_standard):
        meta = dual_standard['meta_glasses_coverage']
        first_article = meta['articles'][0]
        assert 'url' in first_article

    def test_meta_article_framing_is_adversarial(self, dual_standard):
        meta = dual_standard['meta_glasses_coverage']
        first_article = meta['articles'][0]
        framing = first_article.get('framing', '').lower()
        assert 'adversarial' in framing or 'surveillance' in framing

    def test_meta_article_has_surveillance_language(self, dual_standard):
        meta = dual_standard['meta_glasses_coverage']
        first_article = meta['articles'][0]
        lang = first_article.get('language', [])
        lang_text = ' '.join(lang).lower()
        assert any(term in lang_text for term in ['wiretapping', 'biometric', 'surveillance', 'civil liberty']), \
            f"Meta coverage must contain surveillance language: {lang_text[:200]}"

    def test_meta_privacy_is_central_frame(self, dual_standard):
        """Privacy must be the central narrative frame, not a side note."""
        meta = dual_standard['meta_glasses_coverage']
        first_article = meta['articles'][0]
        treatment = str(first_article.get('privacy_treatment', '')).lower()
        assert 'central' in treatment or 'leading' in treatment


# ── Class 4: Hardware Parity ────────────────────────────────────────


class TestHardwareParity:
    """Verify that both devices' capabilities are documented as functionally equivalent."""

    def test_comparison_section_exists(self, dual_standard):
        assert 'comparison' in dual_standard or 'hardware_parity' in dual_standard

    def test_identical_capability_documented(self, dual_standard):
        comparison = dual_standard.get('comparison', dual_standard.get('hardware_parity', {}))
        text = str(comparison).lower()
        assert any(word in text for word in ['identical', 'equivalent', 'same', 'both'])

    def test_camera_in_both(self, dual_standard):
        comparison = dual_standard.get('comparison', dual_standard.get('hardware_parity', {}))
        text = str(comparison).lower()
        assert 'camera' in text or 'visual' in text or 'audio/visual' in text

    def test_always_on_in_both(self, dual_standard):
        comparison = dual_standard.get('comparison', dual_standard.get('hardware_parity', {}))
        text = str(comparison).lower()
        assert any(phrase in text for phrase in ['always-on', 'continuous', 'always on', 'sensing'])


# ── Class 5: Financial Incentive ────────────────────────────────────


class TestFinancialIncentive:
    """Verify the financial relationship is documented as the explanatory variable."""

    def test_undisclosed_conflict_documented(self, dual_standard):
        comparison = dual_standard.get('comparison', {})
        text = str(comparison).lower()
        assert any(word in text for word in ['financial', 'deal', 'undisclosed', 'licensing', 'revenue'])

    def test_ft_openai_deal_referenced(self, dual_standard):
        text = str(dual_standard).lower()
        assert 'openai' in text
        assert any(word in text for word in ['deal', 'licensing', 'revenue'])

    def test_ft_meta_no_deal_noted(self, dual_standard):
        text = str(dual_standard).lower()
        assert any(phrase in text for phrase in ['$0 from', 'no meta', 'zero meta', 'no ft-meta', 'not meta'])

    def test_deal_value_documented(self, dual_standard):
        text = str(dual_standard).lower()
        assert any(val in text for val in ['5-10m', '$5', '$10', 'million'])


# ── Class 6: Non-Disclosure Pattern ─────────────────────────────────


class TestNonDisclosurePattern:
    """Verify that FT's failure to disclose the OpenAI deal is documented."""

    def test_openai_deal_not_disclosed_in_device_article(self, dual_standard):
        device = dual_standard['openai_device_coverage']
        for article in device['articles']:
            disclosed = article.get('openai_deal_disclosed', None)
            if disclosed is not None:
                assert disclosed is False, \
                    f"Article should document non-disclosure of OpenAI deal"

    def test_non_disclosure_in_comparison(self, dual_standard):
        comparison = dual_standard.get('comparison', {})
        text = str(comparison).lower()
        assert any(word in text for word in ['undisclosed', 'did not disclose', 'unaware', 'not disclosed'])


# ── Class 7: Mechanism Integration ──────────────────────────────────


class TestMechanismIntegration:
    """Verify this mechanism integrates into the broader mechanism catalogue."""

    def test_extends_dual_lens_paradox(self, dual_standard):
        """Should reference the Dual-Lens Paradox (Mechanism #7)."""
        text = str(dual_standard).lower()
        assert any(phrase in text for phrase in [
            'dual-lens', 'dual lens', 'mechanism #7', 'mechanism 7',
            'extends', 'hardware-specific', 'privacy framing'
        ])

    def test_mechanism_id_is_18(self, dual_standard):
        assert str(dual_standard.get('mechanism_id', '')) == '18'

    def test_finding_mentions_both_companies(self, dual_standard):
        finding = str(dual_standard.get('finding', '')).lower()
        assert 'openai' in finding
        assert 'meta' in finding


# ── Class 8: Corroboration Sources ──────────────────────────────────


class TestCorroborationSources:
    """Verify the paywalled FT article has documented corroboration sources."""

    def test_corroboration_sources_exist(self, dual_standard):
        """FT articles are paywalled; corroboration sources must be documented."""
        text = str(dual_standard).lower()
        assert any(source in text for source in [
            'techcrunch', 'livemint', 'pymnts', 'notebookcheck',
            'android authority', 'windows central', 'outlook business',
            'corroboration', 'secondary'
        ])

    def test_openai_article_date_is_oct_2025(self, dual_standard):
        device = dual_standard['openai_device_coverage']
        first_article = device['articles'][0]
        date = str(first_article.get('date', ''))
        assert '2025-10' in date or '2025/10' in date or 'Oct' in date or '10-05' in date

    def test_meta_article_date_is_jul_2026(self, dual_standard):
        meta = dual_standard['meta_glasses_coverage']
        first_article = meta['articles'][0]
        date = str(first_article.get('date', ''))
        assert '2026-07' in date or '2026/07' in date or 'Jul' in date or '07-08' in date


# ── Helpers ──────────────────────────────────────────────────────────


def _find_section(profile, target_key):
    """Recursively search for a key in the YAML profile."""
    if isinstance(profile, dict):
        if target_key in profile:
            return profile[target_key]
        for v in profile.values():
            result = _find_section(v, target_key)
            if result is not None:
                return result
    elif isinstance(profile, list):
        for item in profile:
            result = _find_section(item, target_key)
            if result is not None:
                return result
    return None
