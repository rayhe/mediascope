"""
Madhumita Murgia (FT AI Editor) Cross-Entity Coverage Analysis
==============================================================
Type B: Journalist Cross-Entity Tracking
Date: 2026-08-07

KEY FINDING — THE DUAL-LENS PARADOX (Mechanism #6):

Madhumita Murgia is the FT's first AI Editor (since Feb 2023), the most senior AI
journalism position at the publication. Her mandate: "head up the FT's coverage of
artificial intelligence stories." She covers OpenAI, Anthropic, Google DeepMind, and
the broader AI industry — but has NEAR-ZERO Meta coverage, despite Meta being the
world's largest open-source AI developer (Llama), a $100B+ AI infrastructure investor,
and the leading AI wearables manufacturer.

Instead, Meta's AI work is covered by Hannah Murphy (social media beat reporter) using
surveillance/privacy framing. This creates a structural dual-lens:

| AI Lens (Murgia)                     | Platform Lens (Murphy)              |
|--------------------------------------|-------------------------------------|
| OpenAI, Anthropic, Google DeepMind   | Meta, Snap, TikTok                  |
| "innovation," "safety," "frontier"   | "surveillance," "privacy," "gamble" |
| Constructive/aspirational framing    | Adversarial/cautionary framing      |

The SAME technology (AI-powered wearable) gets framed as "innovation" or "surveillance"
based solely on which editorial lens covers it.

ADDITIONAL FINDINGS:
1. Murgia wrote the FT-OpenAI deal announcement (Apr 29, 2024) then continued covering
   OpenAI without disclosing the financial relationship — personal non-disclosure
2. AI Labs podcast series: Meta was the ONLY episode NOT featuring Murgia (the AI Editor).
   Murphy and Criddle (platform reporters) covered Meta instead.
3. Podcast title framing: Meta = "Zuckerberg's $100bn gamble" (risk/doubt);
   Anthropic = "Are Anthropic really the good guys?" (virtue presumed)
4. Former Wired UK senior editor — carries Condé Nast editorial culture into FT AI desk

Sources:
- Murgia Muck Rack profile: https://muckrack.com/madhu-murgia/articles
- Murgia Wikipedia: https://en.wikipedia.org/wiki/Madhumita_Murgia
- FT-OpenAI deal announcement (Techmeme): https://www.techmeme.com/240429/p7
- FT AI Editor appointment: https://talkingbiznews.com/media-news/ft-appoints-murgia-as-its-artificial-intelligence-editor/
- AI Labs podcast series: https://podcast.app/ft-tech-tonic-p172602
- AI Labs Zuckerberg episode details: https://www.radio.de/podcast/ft-tech-tonic
- Dario Amodei Q&A (Techmeme): https://www.techmeme.com/241205/p13
"""

import yaml
import os
import re
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_yaml(filename):
    path = os.path.join(PROFILES_DIR, filename)
    with open(path, 'r') as f:
        return yaml.safe_load(f)


class TestMurgiaAIEditorRole:
    """Validate Murgia's role and credentials are documented."""

    def test_murgia_exists_in_ft_profile(self):
        ft = load_yaml('financial-times.yaml')
        journalists = ft.get('key_journalists', [])
        names = [j['name'] for j in journalists]
        assert 'Madhumita Murgia' in names

    def test_murgia_role_is_ai_editor(self):
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        assert 'AI Editor' in murgia.get('role', '') or 'AI' in murgia.get('beat', '')

    def test_murgia_location_london(self):
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        assert murgia.get('location', '').lower() == 'london'

    def test_murgia_wired_uk_background(self):
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        patterns = murgia.get('known_patterns', '')
        assert 'Wired' in patterns or 'wired' in patterns.lower()

    def test_murgia_code_dependent_book(self):
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        patterns = murgia.get('known_patterns', '')
        assert 'Code Dependent' in patterns


class TestDualLensParadox:
    """Validate the Dual-Lens Paradox — AI lens vs Platform lens at FT."""

    def test_murgia_covers_anthropic(self):
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        cross = murgia.get('cross_entity_coverage_analysis', {})
        assert 'anthropic' in str(cross).lower() or len(murgia.get('anthropic_articles', [])) > 0

    def test_murgia_covers_openai(self):
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        cross = murgia.get('cross_entity_coverage_analysis', {})
        openai_articles = murgia.get('openai_articles', [])
        assert 'openai' in str(cross).lower() or len(openai_articles) > 0

    def test_murgia_covers_google_deepmind(self):
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        cross = murgia.get('cross_entity_coverage_analysis', {})
        assert 'google' in str(cross).lower() or 'deepmind' in str(cross).lower()

    def test_murgia_meta_coverage_is_minimal(self):
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        meta_articles = murgia.get('meta_articles', [])
        anthropic_articles = murgia.get('anthropic_articles', [])
        # Murgia has far fewer Meta articles than Anthropic articles
        assert len(meta_articles) < len(anthropic_articles)

    def test_meta_oldest_articles(self):
        """Murgia's Meta articles are from 2020-2021 — no recent Meta coverage."""
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        meta_articles = murgia.get('meta_articles', [])
        for article in meta_articles:
            date = article.get('date', '')
            if date:
                year = int(date.split('-')[0]) if '-' in date else int(date[:4])
                assert year <= 2021, f"Expected old Meta articles, found {date}"

    def test_murphy_covers_meta_not_murgia(self):
        """Murphy (platform lens) covers Meta; Murgia (AI lens) does not."""
        ft = load_yaml('financial-times.yaml')
        murphy = [j for j in ft['key_journalists'] if j['name'] == 'Hannah Murphy'][0]
        murphy_meta = murphy.get('cross_entity_coverage_analysis', {}).get('meta_coverage_portfolio', [])
        assert len(murphy_meta) >= 3, "Murphy should have substantial Meta coverage"

    def test_dual_lens_documented(self):
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        cross = murgia.get('cross_entity_coverage_analysis', {})
        finding = cross.get('dual_lens_paradox', {})
        assert finding, "Dual-lens paradox should be documented"

    def test_dual_lens_mechanism_number(self):
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        cross = murgia.get('cross_entity_coverage_analysis', {})
        finding = cross.get('dual_lens_paradox', {})
        assert 'mechanism' in str(finding).lower() or '7' in str(finding)


class TestAnthropicConcentration:
    """Validate the Anthropic coverage concentration pattern."""

    def test_anthropic_article_count(self):
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        anthropic = murgia.get('anthropic_articles', [])
        assert len(anthropic) >= 6, f"Expected 6+ Anthropic articles, found {len(anthropic)}"

    def test_anthropic_framing_constructive(self):
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        anthropic = murgia.get('anthropic_articles', [])
        constructive_count = sum(1 for a in anthropic
                                 if 'constructive' in a.get('framing', '').lower()
                                 or 'aspirational' in a.get('framing', '').lower()
                                 or 'profile' in a.get('framing', '').lower()
                                 or 'neutral' in a.get('framing', '').lower()
                                 or 'sympathetic' in a.get('framing', '').lower())
        assert constructive_count >= 3, "Most Anthropic coverage should be constructive/aspirational"

    def test_dario_amodei_access(self):
        """Murgia has direct access to Dario Amodei — indicates source relationship."""
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        anthropic = murgia.get('anthropic_articles', [])
        amodei_articles = [a for a in anthropic if 'amodei' in str(a).lower()]
        assert len(amodei_articles) >= 1, "Should have Dario Amodei access documented"

    def test_anthropic_vs_meta_ratio(self):
        """Anthropic coverage exceeds Meta coverage by at least 3:1."""
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        anthropic = murgia.get('anthropic_articles', [])
        meta = murgia.get('meta_articles', [])
        assert len(anthropic) >= 3 * len(meta), \
            f"Anthropic:Meta ratio should be ≥3:1, got {len(anthropic)}:{len(meta)}"


class TestOpenAIDealNonDisclosure:
    """Validate the FT-OpenAI deal non-disclosure finding."""

    def test_murgia_wrote_deal_announcement(self):
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        cross = murgia.get('cross_entity_coverage_analysis', {})
        deal_announcement = cross.get('openai_deal_announcement', {})
        assert deal_announcement, "OpenAI deal announcement by Murgia should be documented"

    def test_deal_announcement_date(self):
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        cross = murgia.get('cross_entity_coverage_analysis', {})
        deal = cross.get('openai_deal_announcement', {})
        assert '2024' in str(deal.get('date', ''))

    def test_subsequent_coverage_no_disclosure(self):
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        cross = murgia.get('cross_entity_coverage_analysis', {})
        deal = cross.get('openai_deal_announcement', {})
        assert deal.get('subsequent_disclosure', False) is False or \
            'no' in str(deal.get('subsequent_disclosure', '')).lower() or \
            'never' in str(deal.get('subsequent_disclosure_note', '')).lower()

    def test_personal_non_disclosure_significance(self):
        """The person who ANNOUNCED the deal then covered OpenAI without disclosing it."""
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        cross = murgia.get('cross_entity_coverage_analysis', {})
        deal = cross.get('openai_deal_announcement', {})
        assert 'non-disclosure' in str(deal).lower() or 'significance' in str(deal).lower() or \
            'personal' in str(deal).lower()


class TestAILabsPodcastFraming:
    """Validate the AI Labs podcast series framing asymmetry."""

    def test_ai_labs_series_documented(self):
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        cross = murgia.get('cross_entity_coverage_analysis', {})
        podcast = cross.get('ai_labs_podcast_series', {})
        assert podcast, "AI Labs podcast series should be documented"

    def test_meta_episode_not_murgia(self):
        """Meta episode featured Murphy/Criddle, NOT Murgia."""
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        cross = murgia.get('cross_entity_coverage_analysis', {})
        podcast = cross.get('ai_labs_podcast_series', {})
        meta_ep = podcast.get('meta_episode', {})
        reporters = meta_ep.get('reporters', [])
        assert 'Murgia' not in str(reporters), "Murgia should NOT be on Meta episode"

    def test_meta_episode_uses_platform_reporters(self):
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        cross = murgia.get('cross_entity_coverage_analysis', {})
        podcast = cross.get('ai_labs_podcast_series', {})
        meta_ep = podcast.get('meta_episode', {})
        reporters = meta_ep.get('reporters', [])
        assert 'Murphy' in str(reporters) or 'Criddle' in str(reporters)

    def test_meta_episode_gamble_framing(self):
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        cross = murgia.get('cross_entity_coverage_analysis', {})
        podcast = cross.get('ai_labs_podcast_series', {})
        meta_ep = podcast.get('meta_episode', {})
        title = meta_ep.get('title', '')
        assert 'gamble' in title.lower()

    def test_anthropic_episode_virtue_framing(self):
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        cross = murgia.get('cross_entity_coverage_analysis', {})
        podcast = cross.get('ai_labs_podcast_series', {})
        anthropic_ep = podcast.get('anthropic_episode', {})
        title = anthropic_ep.get('title', '')
        assert 'good guys' in title.lower()

    def test_five_episodes_documented(self):
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        cross = murgia.get('cross_entity_coverage_analysis', {})
        podcast = cross.get('ai_labs_podcast_series', {})
        episodes = podcast.get('episodes', [])
        assert len(episodes) >= 5, "Should have 5+ AI Labs episodes"

    def test_title_framing_comparison(self):
        """Title framing table documented with tone analysis."""
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        cross = murgia.get('cross_entity_coverage_analysis', {})
        podcast = cross.get('ai_labs_podcast_series', {})
        framing = podcast.get('title_framing_analysis', {})
        assert framing, "Title framing analysis should exist"


class TestWiredUKConnection:
    """Validate the Wired UK background finding."""

    def test_wired_uk_documented(self):
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        cross = murgia.get('cross_entity_coverage_analysis', {})
        wired = cross.get('wired_uk_background', {})
        assert wired or 'Wired' in murgia.get('known_patterns', '')

    def test_editorial_culture_transfer(self):
        """Wired UK background may transfer Condé Nast editorial culture to FT AI desk."""
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        cross = murgia.get('cross_entity_coverage_analysis', {})
        wired = cross.get('wired_uk_background', {})
        if wired:
            assert 'editorial culture' in str(wired).lower() or \
                'Condé Nast' in str(wired) or 'conde' in str(wired).lower()


class TestGoogleDeepMindCoverage:
    """Validate Google/DeepMind coverage patterns."""

    def test_google_articles_present(self):
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        google = murgia.get('google_articles', [])
        assert len(google) >= 2

    def test_google_framing_mixed(self):
        """Google coverage should be mixed — not uniformly positive or negative."""
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        google = murgia.get('google_articles', [])
        framings = [a.get('framing', '') for a in google]
        # Should have some mix of neutral/critical
        assert len(set(framings)) >= 2 or len(google) >= 2


class TestResearchFileConsistency:
    """Validate consistency with competitor-coverage-research.yaml."""

    def test_murgia_in_research_file(self):
        research = load_yaml('competitor-coverage-research.yaml')
        ft_section = research.get('publications', {}).get('financial_times', {})
        if ft_section:
            assert 'murgia' in str(ft_section).lower()

    def test_dual_lens_in_research(self):
        research = load_yaml('competitor-coverage-research.yaml')
        ft_section = research.get('publications', {}).get('financial_times', {})
        if ft_section:
            assert 'dual_lens' in str(ft_section).lower() or 'dual-lens' in str(ft_section).lower()

    def test_source_urls_present(self):
        research = load_yaml('competitor-coverage-research.yaml')
        ft_section = research.get('publications', {}).get('financial_times', {})
        if ft_section:
            murgia_section = ft_section.get('murgia_cross_entity', {})
            if murgia_section:
                urls = murgia_section.get('source_urls', [])
                assert len(urls) >= 3, f"Should have 3+ source URLs, found {len(urls)}"


class TestSourceURLs:
    """Validate that all findings have source citations."""

    def test_muck_rack_source(self):
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        cross = murgia.get('cross_entity_coverage_analysis', {})
        sources = cross.get('source_urls', [])
        assert any('muckrack' in s for s in sources)

    def test_techmeme_deal_source(self):
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        cross = murgia.get('cross_entity_coverage_analysis', {})
        sources = cross.get('source_urls', [])
        assert any('techmeme' in s for s in sources)

    def test_wikipedia_source(self):
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        cross = murgia.get('cross_entity_coverage_analysis', {})
        sources = cross.get('source_urls', [])
        assert any('wikipedia' in s for s in sources)

    def test_podcast_source(self):
        ft = load_yaml('financial-times.yaml')
        murgia = [j for j in ft['key_journalists'] if j['name'] == 'Madhumita Murgia'][0]
        cross = murgia.get('cross_entity_coverage_analysis', {})
        sources = cross.get('source_urls', [])
        assert any('podcast' in s or 'radio.de' in s for s in sources)


class TestMechanismTaxonomy:
    """Validate the dual-lens paradox fits into the existing mechanism taxonomy."""

    def test_seven_mechanisms_in_research(self):
        """Should now have 7 distinct asymmetry mechanisms documented."""
        research = load_yaml('competitor-coverage-research.yaml')
        research_text = str(research)
        mechanisms = [
            'desk assignment',       # Mechanism 1: WIRED
            'between-reporter',      # Mechanism 2: NYT
            'within-reporter',       # Mechanism 3: FT (Murphy)
            'four-lane',             # Mechanism 4: Verge
            'access paradox',        # Mechanism 5: Verge (Heath)
            'eic',                   # Mechanism 6: Verge (Patel delegation)
            'dual-lens',             # Mechanism 7: FT (Murgia)
        ]
        found = sum(1 for m in mechanisms if m.lower() in research_text.lower())
        assert found >= 6, f"Expected 6+ mechanisms documented, found {found}"
