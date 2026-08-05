"""
News Corp (WSJ) Balanced Control Verification — Type A Deep Dive
================================================================

Validates the News Corp balanced control hypothesis with specific
article examples. News Corp receives comparable payments from both
OpenAI ($50M/yr) and Meta (up to $50M/yr). This test suite verifies:

1. WSJ covers OpenAI critically despite being a deal partner
2. WSJ covers Meta with balanced framing despite being a deal partner
3. WSJ is the ONLY publication that consistently discloses financial ties
4. Coverage tone is balanced when financial incentives are symmetric

Articles analyzed:
- "Rogue AI Hacks Herald New Era of Cyber Chaos" (WSJ, Aug 1, 2026)
  Source: https://www.wsj.com/tech/ai/openai-anthropic-rogue-ai-models-20b6bb3c
- "Meta Is Flooding the Market With Smartglasses. Privacy Advocates Are Up in Arms." (WSJ, Jul 14, 2026)
  Source: https://www.wsj.com/tech/ai/meta-is-flooding-the-market-with-smartglasses-privacy-advocates-are-up-in-arms-8fb71539
- "Smartglasses Are Inevitable. But What—or Who—Are They For?" (WSJ, Jun 26, 2026)
  Source: https://www.wsj.com/tech/ai/smart-glasses-market-meta-ai-8e6510b8
- "Meta Stock Drops 10% on Steeper AI Costs, Missed Forecast" (WSJ, Jul 30, 2026)
  Source: https://www.wsj.com/tech/ai/meta-q2-earnings-report-2026-stock-9808dd3c

Created: 2026-08-05 (Type A: Competitor Coverage Deep Dive)
"""

import yaml
import os
import pytest

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_competitor_research():
    path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def load_competitor_entities():
    path = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
    with open(path, 'r') as f:
        return yaml.safe_load(f)


class TestNewsCorp:
    """Verify News Corp exists as a publication with both Meta and OpenAI relationships."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.research = load_competitor_research()
        self.news_corp = self.research['publications']['news-corp']

    def test_news_corp_exists(self):
        assert 'news-corp' in self.research['publications']

    def test_meta_coverage_tone_balanced(self):
        assert self.news_corp['meta_coverage_tone'] == 'balanced'

    def test_openai_coverage_tone_balanced(self):
        assert self.news_corp['openai_coverage_tone'] == 'balanced'


class TestNewsCorpMetaArticleExamples:
    """Verify specific WSJ Meta article examples exist with required fields."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.research = load_competitor_research()
        self.meta_examples = self.research['publications']['news-corp']['meta_examples']

    def test_has_meta_examples(self):
        assert len(self.meta_examples) >= 3, f"Expected at least 3 Meta examples, got {len(self.meta_examples)}"

    def test_flooding_market_article_exists(self):
        titles = [e['title'] for e in self.meta_examples]
        matches = [t for t in titles if 'Flooding' in t or 'Smartglasses' in t and 'Privacy' in t]
        assert len(matches) >= 1, f"Missing 'Flooding the Market' article in: {titles}"

    def test_smartglasses_inevitable_article_exists(self):
        titles = [e['title'] for e in self.meta_examples]
        matches = [t for t in titles if 'Inevitable' in t]
        assert len(matches) >= 1, f"Missing 'Smartglasses Are Inevitable' article in: {titles}"

    def test_meta_article_tones_balanced(self):
        """Meta article tones should be in balanced range (-0.3 to +0.2)."""
        for example in self.meta_examples:
            tone = example['tone']
            assert -0.3 <= tone <= 0.2, (
                f"Meta article '{example['title']}' tone {tone} outside balanced range"
            )

    def test_all_meta_examples_have_source_urls(self):
        for example in self.meta_examples:
            assert 'source_url' in example, f"Missing source_url in '{example['title']}'"
            assert example['source_url'], f"Empty source_url in '{example['title']}'"

    def test_all_meta_examples_have_framing(self):
        for example in self.meta_examples:
            assert 'framing' in example, f"Missing framing in '{example['title']}'"
            assert len(example['framing']) > 20, f"Framing too short in '{example['title']}'"

    def test_meta_examples_no_loaded_language(self):
        """WSJ Meta coverage should not use WIRED-style loaded language."""
        loaded_terms = ['dormant surveillance', 'wiretapping', 'gulag', 'underclass']
        for example in self.meta_examples:
            framing = example['framing'].lower()
            for term in loaded_terms:
                # Loaded terms should NOT appear in WSJ framing description
                # (they may appear in notes as comparison references)
                if term in framing:
                    # Allow if it's in a comparison context
                    assert 'compare' in framing or 'wired' in framing, (
                        f"Loaded term '{term}' in WSJ framing without comparison context"
                    )


class TestNewsCorpOpenAIArticleExamples:
    """Verify specific WSJ OpenAI article examples exist with required fields."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.research = load_competitor_research()
        self.openai_examples = self.research['publications']['news-corp']['openai_examples']

    def test_has_openai_examples(self):
        assert len(self.openai_examples) >= 2, f"Expected at least 2 OpenAI examples, got {len(self.openai_examples)}"

    def test_rogue_ai_article_exists(self):
        titles = [e['title'] for e in self.openai_examples]
        matches = [t for t in titles if 'Rogue' in t or 'Cyber Chaos' in t or 'Hack' in t]
        assert len(matches) >= 1, f"Missing 'Rogue AI Hacks' article in: {titles}"

    def test_openai_article_tones_critical(self):
        """OpenAI hacking articles should be critical (negative tone) despite deal."""
        rogue_articles = [e for e in self.openai_examples if 'Rogue' in e.get('title', '') or 'Hack' in e.get('title', '')]
        for article in rogue_articles:
            assert article['tone'] < 0, (
                f"OpenAI hacking article '{article['title']}' should have negative tone, got {article['tone']}"
            )

    def test_openai_critical_despite_deal(self):
        """WSJ runs critical OpenAI coverage despite $50M/yr deal — tone ≤ -0.30."""
        rogue_articles = [e for e in self.openai_examples if 'Rogue' in e.get('title', '') or 'Chaos' in e.get('title', '')]
        assert len(rogue_articles) >= 1, "No rogue/chaos articles found"
        for article in rogue_articles:
            assert article['tone'] <= -0.30, (
                f"WSJ OpenAI critical article should be ≤ -0.30, got {article['tone']}"
            )

    def test_all_openai_examples_have_source_urls(self):
        for example in self.openai_examples:
            assert 'source_url' in example, f"Missing source_url in '{example['title']}'"
            assert example['source_url'], f"Empty source_url in '{example['title']}'"


class TestDisclosureAnalysis:
    """Verify the financial disclosure analysis for News Corp vs other publications."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.research = load_competitor_research()
        self.news_corp = self.research['publications']['news-corp']

    def test_disclosure_analysis_exists(self):
        assert 'disclosure_analysis' in self.news_corp

    def test_disclosure_mentions_both_deals(self):
        disclosure = self.news_corp['disclosure_analysis'].lower()
        assert 'meta' in disclosure, "Disclosure analysis should mention Meta deal"
        assert 'openai' in disclosure, "Disclosure analysis should mention OpenAI deal"

    def test_disclosure_mentions_non_disclosing_publications(self):
        """Should document that WIRED, FT, The Verge, Atlantic do NOT disclose."""
        disclosure = self.news_corp['disclosure_analysis'].lower()
        for pub in ['wired', 'verge', 'atlantic', 'guardian']:
            assert pub in disclosure, f"Disclosure analysis should mention {pub}'s non-disclosure"

    def test_disclosure_mentions_only_publication(self):
        disclosure = self.news_corp['disclosure_analysis']
        assert 'ONLY' in disclosure, "Should emphasize WSJ is the ONLY disclosing publication"

    def test_disclosure_identifies_transparency_correlation(self):
        disclosure = self.news_corp['disclosure_analysis'].lower()
        assert 'transparency' in disclosure or 'correlat' in disclosure, (
            "Disclosure analysis should identify correlation between transparency and balanced coverage"
        )


class TestBalancedControlAsymmetryVerdict:
    """Verify the asymmetry verdict is updated with specific article evidence."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.research = load_competitor_research()
        self.verdict = self.research['publications']['news-corp']['asymmetry_verdict']

    def test_verdict_mentions_verified(self):
        assert 'VERIFIED' in self.verdict, "Asymmetry verdict should mention verification"

    def test_verdict_mentions_specific_articles(self):
        assert 'Jurassic Park' in self.verdict or 'Rogue' in self.verdict or '-0.40' in self.verdict, (
            "Verdict should reference specific OpenAI hacking article evidence"
        )

    def test_verdict_mentions_wired_comparison(self):
        assert 'WIRED' in self.verdict, "Verdict should compare WSJ tone to WIRED tone"

    def test_verdict_quantifies_delta(self):
        assert '0.70' in self.verdict or 'LESS ADVERSARIAL' in self.verdict, (
            "Verdict should quantify the tone delta between WSJ and WIRED on Meta glasses"
        )


class TestToneDeltaBetweenWSJAndWIRED:
    """Verify the key finding: WSJ Meta coverage is dramatically less adversarial than WIRED's."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.research = load_competitor_research()

    def test_wired_meta_tone_more_negative_than_wsj(self):
        wired = self.research['publications']['wired']
        news_corp = self.research['publications']['news-corp']

        # WIRED Meta examples should have at least one article with tone ≤ -0.7
        wired_worst = min(e['tone'] for e in wired['meta_examples'])
        # WSJ Meta examples should have no article below -0.30
        wsj_worst = min(e['tone'] for e in news_corp['meta_examples'])

        assert wired_worst < wsj_worst, (
            f"WIRED worst Meta tone ({wired_worst}) should be more negative than WSJ ({wsj_worst})"
        )

    def test_delta_at_least_half_point(self):
        """The tone delta between WIRED and WSJ Meta coverage should be ≥ 0.50."""
        wired = self.research['publications']['wired']
        news_corp = self.research['publications']['news-corp']

        wired_worst = min(e['tone'] for e in wired['meta_examples'])
        wsj_worst = min(e['tone'] for e in news_corp['meta_examples'])
        delta = wsj_worst - wired_worst  # positive means WSJ is less negative

        assert delta >= 0.50, (
            f"WSJ-WIRED Meta tone delta ({delta:.2f}) should be ≥ 0.50. "
            f"WIRED: {wired_worst}, WSJ: {wsj_worst}"
        )

    def test_wsj_openai_critical_despite_deal(self):
        """WSJ covers OpenAI critically despite deal — avg tone should be < 0."""
        news_corp = self.research['publications']['news-corp']
        avg_tone = sum(e['tone'] for e in news_corp['openai_examples']) / len(news_corp['openai_examples'])
        assert avg_tone < 0, (
            f"WSJ OpenAI avg tone ({avg_tone:.2f}) should be negative — they cover OpenAI critically despite deal"
        )


class TestAggregateFindingsDisclosure:
    """Verify disclosure finding is in aggregate findings section."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.research = load_competitor_research()
        self.findings = self.research['aggregate_findings']['key_evidence']

    def test_disclosure_finding_exists(self):
        finding_names = [f['finding'] for f in self.findings]
        disclosure_findings = [f for f in finding_names if 'disclosure' in f.lower()]
        assert len(disclosure_findings) >= 1, (
            f"No disclosure finding in aggregate findings: {finding_names}"
        )

    def test_disclosure_finding_has_significance(self):
        for finding in self.findings:
            if 'disclosure' in finding['finding'].lower():
                assert 'significance' in finding
                assert len(finding['significance']) > 10
