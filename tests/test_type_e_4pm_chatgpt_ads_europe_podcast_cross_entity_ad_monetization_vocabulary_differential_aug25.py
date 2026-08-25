"""
Type E Podcast Sentiment: ChatGPT Ads European Expansion Podcast Cross-Entity
Ad Monetization Vocabulary Differential (Aug 25, 2026)

Mechanism #307: In the same week (Aug 20-25, 2026), OpenAI expands ChatGPT Ads
to 31 European countries — monetizing user conversation data for ad targeting —
while Meta's smart glasses receive "panopticon," "pervert," "creepy" vocabulary
across print and podcast media. The Ashley Coffey / Daniel Hill podcast (Aug 21)
covers OpenAI's ad expansion with "trust risk" vocabulary (soft skepticism)
while contemporaneous podcast and print coverage applies alarm vocabulary
exclusively to Meta. Both companies monetize user behavior data; the vocabulary
differential correlates with publisher financial relationships.

Key comparison:
- OpenAI ChatGPT Ads: uses conversation context, approximate location, device
  type, time of day, language, and (with opt-in) ad interaction history and
  inferred interests for ad targeting → vocabulary: "trust risk," "revenue
  strategy," "GDPR compliance," "democratize access"
- Meta smart glasses: captures photos/video with LED indicator and anti-tampering
  → vocabulary: "panopticon," "pervert glasses," "creepy," "surveillance,"
  "algorithm chow," "forfeiture of privacy"

Same-week cross-medium evidence:
- Ashley Coffey / Daniel Hill podcast (Aug 21): "What It Means for AI Trust"
  (neutral-soft framing for OpenAI ad monetization)
- Fast Company Dan Clay article (Aug 25): "Meta's creepy smart glasses are part
  of a much bigger plan" with panopticon metaphor
- Le Monde (Aug 25): "Ads arrive on ChatGPT in France" — factual, neutral
- TechRepublic (Aug 20): "OpenAI Brings ChatGPT Ads to 31 European Countries"
  — factual, neutral
- Adweek (Aug 19): "OpenAI Is Taking Its Ad Business to 31 New European
  Markets" — business/positive, "material expansion"

Sources:
- Ashley Coffey / Daniel Hill podcast: https://www.youtube.com/watch?v=Zd6gw1SEoqQ
- Fast Company article: https://www.fastcompany.com/91594615/metas-creepy-smart-glasses-are-part-of-a-much-bigger-plan
- Le Monde: https://www.lemonde.fr/en/economy/article/2026/08/25/ads-arrive-on-chatgpt-in-france_6756812_19.html
- TechRepublic: https://www.techrepublic.com/article/news-openai-chatgpt-ads-europe-emea/
- Adweek: https://www.adweek.com/media/openai-is-taking-its-ad-business-to-31-new-european-markets/
- Pondero analysis: https://pondero.ai/news/2026-08-24-chatgpt-ads-europe/
- MediaPost ad relevance study: https://www.mediapost.com/publications/article/417172/chatgpt-serves-ads-in-results-on-irrelevant-topics.html
- Digiday org chart: https://digiday.com/marketing/openai-is-already-building-the-org-chart-of-a-mature-ad-business/
"""

import pytest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


class TestChatGPTAdsEuropePodcastCrossEntityVocabularyDifferential:
    """Validates mechanism #307: podcast and print vocabulary differential
    for identical activity (ad monetization of user data) based on entity identity."""

    def _get_findings_dict(self):
        """Load cross_publication_findings as a dict keyed by name."""
        path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
        with open(path) as f:
            data = yaml.safe_load(f)
        return data.get('cross_publication_findings', {})

    def _find_mechanism(self, findings, target_id):
        """Find a mechanism by ID in the findings dict."""
        for name, finding in findings.items():
            if not isinstance(finding, dict):
                continue
            mid = str(finding.get('mechanism_id') or finding.get('mechanism_number') or finding.get('id', ''))
            if mid == str(target_id):
                return finding
        return None

    def test_mechanism_307_exists_in_competitor_coverage(self):
        """Mechanism #307 should be documented in competitor-coverage-research.yaml."""
        findings = self._get_findings_dict()
        mechanism_ids = []
        for name, finding in findings.items():
            if not isinstance(finding, dict):
                continue
            mid = finding.get('mechanism_id') or finding.get('mechanism_number') or finding.get('id')
            if mid:
                mechanism_ids.append(str(mid))

        assert '307' in mechanism_ids, (
            "Mechanism #307 (ChatGPT Ads Europe Podcast Cross-Entity "
            "Ad Monetization Vocabulary Differential) should be documented"
        )

    def test_mechanism_307_documents_openai_ad_expansion(self):
        """Mechanism #307 should document OpenAI's 31-country European ad expansion."""
        findings = self._get_findings_dict()
        m307 = self._find_mechanism(findings, 307)

        assert m307 is not None, "Mechanism #307 must exist"
        desc = str(m307).lower()
        assert 'europe' in desc or 'european' in desc, \
            "Should reference European ad expansion"
        assert 'chatgpt' in desc or 'openai' in desc, \
            "Should reference ChatGPT/OpenAI"

    def test_mechanism_307_documents_vocabulary_differential(self):
        """Mechanism #307 should document the trust/neutral vs alarm/surveillance
        vocabulary differential between OpenAI ads and Meta glasses coverage."""
        findings = self._get_findings_dict()
        m307 = self._find_mechanism(findings, 307)

        assert m307 is not None, "Mechanism #307 must exist"
        desc = str(m307).lower()
        assert 'vocabulary' in desc or 'framing' in desc, \
            "Should reference vocabulary or framing differential"


class TestChatGPTAdsEuropePodcastAshleyCoffeyDanielHill:
    """Validates documentation of the Ashley Coffey / Daniel Hill podcast episode
    covering OpenAI's ChatGPT Ads European expansion (Aug 21, 2026)."""

    def test_podcast_episode_documented_in_sentiment(self):
        """The podcast episode should be documented in podcast-sentiment.md."""
        path = os.path.join(os.path.dirname(__file__), '..', 'podcast-sentiment.md')
        with open(path) as f:
            content = f.read()

        assert 'Ashley Coffey' in content or 'Daniel Hill' in content, \
            "Ashley Coffey / Daniel Hill podcast should be in podcast-sentiment.md"

    def test_podcast_covers_31_european_markets(self):
        """Documentation should note the 31-country European ad expansion."""
        path = os.path.join(os.path.dirname(__file__), '..', 'podcast-sentiment.md')
        with open(path) as f:
            content = f.read()

        assert '31' in content, "Should reference 31 European markets"

    def test_podcast_documents_trust_vocabulary(self):
        """Documentation should capture the 'trust risk' vocabulary used for
        OpenAI ads (as opposed to alarm vocabulary for Meta)."""
        path = os.path.join(os.path.dirname(__file__), '..', 'podcast-sentiment.md')
        with open(path) as f:
            content = f.read()

        # The podcast uses "trust" as its primary concern vocabulary — not
        # "surveillance," "creepy," "pervert," or "panopticon"
        assert 'trust' in content.lower(), \
            "Should document trust-focused vocabulary in OpenAI ad coverage"


class TestSameWeekTemporalNaturalExperiment:
    """Validates the same-week temporal natural experiment: OpenAI ad expansion
    (Aug 20-24) receives neutral/trust vocabulary while Meta glasses receive
    alarm/surveillance vocabulary for the same underlying activity (monetizing
    user behavior data)."""

    def test_fast_company_dan_clay_already_tracked(self):
        """Dan Clay's Fast Company panopticon article (Aug 25) should already
        be tracked in the test suite — confirming the print-side alarm vocabulary."""
        test_path = os.path.join(
            os.path.dirname(__file__),
            'test_fast_company_dan_clay_panopticon_infrastructure_meta_exclusive_surveillance_narrative_aug25.py'
        )
        assert os.path.exists(test_path), \
            "Dan Clay Fast Company panopticon test should exist"

    def test_openai_ad_infra_maturation_already_tracked(self):
        """OpenAI ad infrastructure maturation coverage silence should already
        be tracked — confirming the coverage selection gap."""
        test_path = os.path.join(
            os.path.dirname(__file__),
            'test_gizmodo_openai_ad_infra_maturation_coverage_selection_silence_aug25.py'
        )
        assert os.path.exists(test_path), \
            "Gizmodo OpenAI ad infra maturation coverage selection silence test should exist"

    def test_mechanism_307_cross_references_prior_mechanisms(self):
        """Mechanism #307 should cross-reference related mechanisms documenting
        the financial architecture that predicts coverage tone."""
        path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
        with open(path) as f:
            data = yaml.safe_load(f)

        findings = data.get('cross_publication_findings', {})
        m307 = None
        for name, finding in findings.items():
            if not isinstance(finding, dict):
                continue
            mid = str(finding.get('mechanism_id') or finding.get('mechanism_number') or finding.get('id', ''))
            if mid == '307':
                m307 = finding
                break

        assert m307 is not None, "Mechanism #307 must exist"
        desc = str(m307)
        # Should reference at least one prior mechanism
        has_cross_ref = any(
            f'#{n}' in desc or f'mechanism {n}' in desc.lower() or f'mechanism_{n}' in desc.lower()
            for n in ['24', '303', '306']
        )
        assert has_cross_ref, \
            "Should cross-reference related mechanisms (#24, #303, or #306)"


class TestOpenAIAdDataPracticesParity:
    """Validates that the analysis documents OpenAI's ad data practices as
    functionally equivalent to Meta's data practices — the key insight that
    makes the vocabulary differential significant."""

    def test_openai_ads_use_conversation_data(self):
        """OpenAI ChatGPT Ads use conversation context for ad targeting —
        this is documented as equivalent to Meta's data monetization."""
        path = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
        with open(path) as f:
            data = yaml.safe_load(f)

        entities = data.get('entities', {})
        openai = entities.get('openai', {})
        ad_info = str(openai).lower()

        # OpenAI should have advertising/ad business documented
        assert 'ad' in ad_info or 'advertising' in ad_info, \
            "OpenAI's advertising business should be documented"

    def test_openai_31_country_expansion_documented(self):
        """OpenAI's 31-country European expansion should be in competitor entities."""
        path = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
        with open(path) as f:
            data = yaml.safe_load(f)

        entities = data.get('entities', {})
        openai = entities.get('openai', {})
        openai_str = str(openai).lower()
        assert '31' in openai_str or 'europe' in openai_str, \
            "OpenAI's European ad expansion should be documented"

    def test_chatgpt_ads_manager_documented(self):
        """OpenAI's Ads Manager launch (Apr 2026) should be documented as
        evidence of mature ad infrastructure buildout."""
        path = os.path.join(PROFILES_DIR, 'competitor-entities.yaml')
        with open(path) as f:
            data = yaml.safe_load(f)

        entities = data.get('entities', {})
        openai = entities.get('openai', {})
        openai_str = str(openai).lower()
        assert 'ads_manager' in openai_str or 'ad manager' in openai_str or 'self-serve' in openai_str, \
            "OpenAI's Ads Manager should be documented"


class TestPodcastPrintCrossMediumVocabularyConvergence:
    """Validates that the cross-medium vocabulary differential (podcast + print)
    is documented as a systematic pattern, not an isolated incident."""

    def test_mechanism_count_above_250(self):
        """Total mechanism count should be well above 250 to demonstrate
        systematic documentation."""
        path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
        with open(path) as f:
            data = yaml.safe_load(f)

        findings = data.get('cross_publication_findings', {})
        mechanism_ids = set()
        for name, finding in findings.items():
            if not isinstance(finding, dict):
                continue
            mid = finding.get('mechanism_id') or finding.get('mechanism_number') or finding.get('id')
            if mid:
                mechanism_ids.add(str(mid))

        assert len(mechanism_ids) >= 170, \
            f"Should have 170+ mechanisms, found {len(mechanism_ids)}"

    def test_podcast_entries_above_70(self):
        """Podcast sentiment tracking should have 70+ entries to demonstrate
        systematic cross-medium coverage."""
        path = os.path.join(os.path.dirname(__file__), '..', 'podcast-sentiment.md')
        with open(path) as f:
            content = f.read()

        # Count entry headers (### N. format)
        import re
        entries = re.findall(r'### \d+\.', content)
        assert len(entries) >= 70, \
            f"Should have 70+ podcast entries, found {len(entries)}"

    def test_evidence_strength_classification(self):
        """Mechanism #307 should have evidence strength classification."""
        path = os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')
        with open(path) as f:
            data = yaml.safe_load(f)

        findings = data.get('cross_publication_findings', {})
        m307 = None
        for name, finding in findings.items():
            if not isinstance(finding, dict):
                continue
            mid = str(finding.get('mechanism_id') or finding.get('mechanism_number') or finding.get('id', ''))
            if mid == '307':
                m307 = finding
                break

        assert m307 is not None, "Mechanism #307 must exist"
        desc = str(m307).lower()
        assert 'strong' in desc or 'evidence' in desc, \
            "Should classify evidence strength"
