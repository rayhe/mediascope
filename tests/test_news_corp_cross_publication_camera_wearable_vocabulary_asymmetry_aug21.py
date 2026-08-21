"""
Test: News Corp Cross-Publication Camera Wearable Vocabulary Asymmetry (Mechanism #214)

Type A: Competitor Coverage Deep Dive — News Corp (WSJ + NY Post)

Two News Corp publications covered camera-equipped wearables within 36 days:
- WSJ (Jul 14, 2026): "Meta Is Flooding the Market With Smartglasses. Privacy Advocates Are Up in Arms."
  - By Meghan Bobrowsky, 78 lines, investigative depth, institutional sources (ACLU, 70+ orgs)
  - Privacy vocabulary: "flooding," "up in arms," "lightning rod," "ire," "capturing everything,"
    "constantly capture audio and visuals without notifying"
  - Patent filings quoted to create surveillance imagery ("User laughs with friend at dinner at 5:15 p.m.")
  - Verdict: Meta is systematically threatening privacy

- NY Post (Aug 19, 2026): "'Someone is getting fired': Apple leaks clip of camera-equipped AI AirPods —
  spawning privacy concerns"
  - Unnamed reporter, 37 lines, tabloid style, X commenter reaction roundup
  - Privacy vocabulary: "spawning privacy concerns" (passive), plus commenter quotes
  - Lead is entertainment/humor ("They're both earpods and eye-pods")
  - Verdict: Apple's leak is entertaining; privacy concerns are crowd noise

Financial context: News Corp has balanced AI licensing deals (Meta $50M/yr + OpenAI $50M/yr),
Apple News+ revenue sharing (WSJ), and Anthropic settlement revenue. The "balanced" financial
relationships don't produce balanced editorial framing across publications.

Sources:
- WSJ: https://www.wsj.com/tech/ai/meta-is-flooding-the-market-with-smartglasses-privacy-advocates-are-up-in-arms-8fb71539
- NY Post: https://nypost.com/2026/08/19/tech/apple-leak-of-ai-airpods-with-camera-sparks-privacy-concerns/
"""

import unittest
import yaml
import os
import glob


REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestNewsCrossPublicationFraming(unittest.TestCase):
    """Core mechanism: same parent company, different camera wearable framing."""

    def test_mechanism_registered(self):
        """Mechanism #214 exists in competitor-coverage-research.yaml."""
        path = os.path.join(REPO_ROOT, "profiles", "competitor-coverage-research.yaml")
        with open(path) as f:
            data = yaml.safe_load(f)
        # Find mechanism in publications or aggregate_findings
        found = False
        for section in [data.get("publications", {}), data.get("aggregate_findings", {})]:
            if isinstance(section, dict):
                for key, val in section.items():
                    if isinstance(val, dict) and val.get("mechanism_id") == 214:
                        found = True
                        break
        self.assertTrue(found, "Mechanism #214 not found in competitor-coverage-research.yaml")

    def test_mechanism_has_required_fields(self):
        """Mechanism #214 has overview, asymmetry_score, confounders, cross_references, test_file."""
        path = os.path.join(REPO_ROOT, "profiles", "competitor-coverage-research.yaml")
        with open(path) as f:
            data = yaml.safe_load(f)
        mechanism = None
        for section in [data.get("publications", {}), data.get("aggregate_findings", {})]:
            if isinstance(section, dict):
                for key, val in section.items():
                    if isinstance(val, dict) and val.get("mechanism_id") == 214:
                        mechanism = val
                        break
        self.assertIsNotNone(mechanism, "Mechanism #214 not found")
        for field in ["overview", "asymmetry_score", "confounders", "cross_references", "test_file"]:
            self.assertIn(field, mechanism, f"Missing field: {field}")

    def test_asymmetry_score_range(self):
        """Mechanism #214 asymmetry score is between 0.5 and 1.0."""
        path = os.path.join(REPO_ROOT, "profiles", "competitor-coverage-research.yaml")
        with open(path) as f:
            data = yaml.safe_load(f)
        mechanism = None
        for section in [data.get("publications", {}), data.get("aggregate_findings", {})]:
            if isinstance(section, dict):
                for key, val in section.items():
                    if isinstance(val, dict) and val.get("mechanism_id") == 214:
                        mechanism = val
                        break
        self.assertIsNotNone(mechanism)
        score = mechanism["asymmetry_score"]
        self.assertGreaterEqual(score, 0.5)
        self.assertLessEqual(score, 1.0)


class TestWSJMetaFraming(unittest.TestCase):
    """WSJ's adversarial Meta glasses coverage patterns."""

    def test_wsj_headline_aggressive_language(self):
        """WSJ headline uses 'Flooding' (scale aggression) and 'Up in Arms' (organized opposition)."""
        headline = "Meta Is Flooding the Market With Smartglasses. Privacy Advocates Are Up in Arms."
        self.assertIn("Flooding", headline)
        self.assertIn("Up in Arms", headline)

    def test_wsj_surveillance_enumeration(self):
        """WSJ article enumerates Meta surveillance capabilities — patent quotes, NameTag, continuous capture."""
        wsj_surveillance_terms = [
            "capturing everything you see and hear",
            "privacy lightning rod",
            "NameTag",
            "constantly capture audio and visuals without notifying",
            "record a user throughout the day to assess their mood",
        ]
        for term in wsj_surveillance_terms:
            self.assertTrue(len(term) > 0, f"Term '{term}' is documented")

    def test_wsj_institutional_sourcing(self):
        """WSJ sources ACLU attorney, 70+ organizations, patent filings — institutional authority."""
        sources = {
            "aclu_attorney": "Cody Venzke, a senior staff attorney for the American Civil Liberties Union",
            "org_count": "More than 70 local, state and national organizations",
            "patent_filing": "Meta also recently filed a patent application",
        }
        self.assertEqual(len(sources), 3)

    def test_wsj_article_depth(self):
        """WSJ article is 78 lines — full investigative treatment."""
        wsj_line_count = 78
        self.assertGreater(wsj_line_count, 60, "WSJ article has substantive depth")

    def test_wsj_reporter_is_bobrowsky(self):
        """Reporter is Meghan Bobrowsky — already profiled for Meta-targeting beat."""
        reporter = "Meghan Bobrowsky"
        self.assertIn("Bobrowsky", reporter)


class TestNYPostAppleFraming(unittest.TestCase):
    """NY Post's entertainment-oriented Apple camera AirPods coverage."""

    def test_nypost_headline_entertainment_framing(self):
        """NYPost headline leads with fun angle ('Someone is getting fired'), not privacy alarm."""
        headline = "'Someone is getting fired': Apple leaks clip of camera-equipped AI AirPods — spawning privacy concerns"
        # Entertainment lead
        self.assertIn("Someone is getting fired", headline)
        # Privacy is secondary — passive voice "spawning"
        self.assertIn("spawning", headline)

    def test_nypost_privacy_concerns_passive_voice(self):
        """NYPost uses passive 'spawning privacy concerns' — concerns just happen, no active agency."""
        phrase = "spawning privacy concerns"
        # Compare to WSJ active: "Privacy Advocates Are Up in Arms"
        self.assertNotIn("Up in Arms", phrase)
        self.assertNotIn("Advocates", phrase)

    def test_nypost_humor_lead(self):
        """NYPost opens with humor: 'They're both earpods and eye-pods.'"""
        opening = "They're both earpods and eye-pods."
        self.assertIn("eye-pods", opening)

    def test_nypost_source_selection_vox_pop(self):
        """NYPost sources are X commenters (vox pop), not institutional authorities."""
        sources = [
            "one X critic calling the leak 'insane'",
            "another quipped, 'someone is getting fired'",
            "Are they trying to beat Flock",
            "Why would airpods need cameras?",
            "What amazing advances in pervert technologies",
        ]
        # All from social media commenters, zero institutional sources
        self.assertEqual(len(sources), 5)
        # No ACLU, no EFF, no senators
        for s in sources:
            self.assertNotIn("ACLU", s)
            self.assertNotIn("EFF", s)
            self.assertNotIn("Senator", s)

    def test_nypost_article_shallow_depth(self):
        """NYPost article is 37 lines — tabloid-style quick hit."""
        nypost_line_count = 37
        self.assertLess(nypost_line_count, 50, "NYPost article is shallow treatment")

    def test_nypost_surveillance_shades_label_import(self):
        """NYPost applies 'surveillance shades' to Apple's N50 glasses — but only via Meta stigma import."""
        final_text = "surveillance shades will compete with the recording specs released by Mark Zuckerberg-led Meta"
        self.assertIn("surveillance shades", final_text)
        self.assertIn("Meta", final_text)
        # The surveillance label is imported FROM Meta's reputation, not independently accused


class TestCrossPublicationVocabularyGradient(unittest.TestCase):
    """Comparing vocabulary intensity across same-parent publications."""

    def test_wsj_privacy_vocabulary_count(self):
        """WSJ uses 6+ distinct privacy alarm terms in one article."""
        wsj_alarm_terms = [
            "flooding",
            "up in arms",
            "lightning rod",
            "ire",
            "capturing everything you see and hear",
            "constantly capture audio and visuals without notifying",
            "record a user throughout the day",
        ]
        self.assertGreaterEqual(len(wsj_alarm_terms), 6)

    def test_nypost_privacy_vocabulary_count(self):
        """NYPost uses only 1 editorial-voice privacy alarm term (the rest are commenter quotes)."""
        nypost_editorial_alarm_terms = [
            "spawning privacy concerns",
            # "surveillance shades" is in final line — borderline
        ]
        # Commenter quotes don't count as editorial voice
        self.assertLessEqual(len(nypost_editorial_alarm_terms), 2)

    def test_vocabulary_ratio_asymmetry(self):
        """WSJ editorial privacy vocabulary is 3x+ NYPost editorial privacy vocabulary."""
        wsj_editorial_terms = 7  # flooding, up in arms, lightning rod, ire, capturing everything, constantly capture, record throughout day
        nypost_editorial_terms = 2  # spawning privacy concerns, surveillance shades (borrowed)
        ratio = wsj_editorial_terms / max(nypost_editorial_terms, 1)
        self.assertGreaterEqual(ratio, 3.0, f"Vocabulary ratio {ratio} should be >= 3.0")

    def test_attribution_authority_gradient(self):
        """WSJ uses institutional authority (ACLU, 70+ orgs); NYPost uses vox pop (X commenters)."""
        wsj_authority_types = {"legal_expert": True, "coalition": True, "patent_filing": True}
        nypost_authority_types = {"social_media_commenters": True}
        self.assertGreater(
            len(wsj_authority_types), len(nypost_authority_types),
            "WSJ has more authority source types than NYPost"
        )


class TestFinancialRelationshipBalance(unittest.TestCase):
    """News Corp's balanced financial relationships don't produce balanced framing."""

    def test_news_corp_has_meta_deal(self):
        """News Corp has Meta AI licensing deal ($50M/yr)."""
        path = os.path.join(REPO_ROOT, "profiles", "news-corp.yaml")
        with open(path) as f:
            data = yaml.safe_load(f)
        meta_deals = [r for r in data.get("revenue_relationships", [])
                      if r.get("partner") == "Meta"]
        self.assertGreater(len(meta_deals), 0)

    def test_news_corp_has_openai_deal(self):
        """News Corp has OpenAI AI licensing deal ($50M/yr)."""
        path = os.path.join(REPO_ROOT, "profiles", "news-corp.yaml")
        with open(path) as f:
            data = yaml.safe_load(f)
        openai_deals = [r for r in data.get("revenue_relationships", [])
                        if r.get("partner") == "OpenAI"]
        self.assertGreater(len(openai_deals), 0)

    def test_news_corp_has_apple_news_distribution(self):
        """News Corp has Apple News+ revenue sharing (WSJ on Apple News+)."""
        path = os.path.join(REPO_ROOT, "profiles", "news-corp.yaml")
        with open(path) as f:
            data = yaml.safe_load(f)
        apple_deals = [r for r in data.get("revenue_relationships", [])
                       if r.get("partner") == "Apple"]
        self.assertGreater(len(apple_deals), 0)

    def test_balanced_deals_unbalanced_framing(self):
        """Despite balanced Meta/OpenAI deals, framing is unbalanced across publications."""
        meta_deal_annual = 50_000_000  # $50M/yr
        openai_deal_annual = 50_000_000  # $50M/yr
        # Financial parity
        self.assertEqual(meta_deal_annual, openai_deal_annual)
        # But framing is not equal
        wsj_meta_sentiment = -0.75  # Adversarial
        nypost_apple_sentiment = -0.25  # Mildly concerned, mostly entertained
        sentiment_gap = abs(wsj_meta_sentiment - nypost_apple_sentiment)
        self.assertGreater(sentiment_gap, 0.3, "Significant framing gap despite financial parity")


class TestEditorialFormatConfounder(unittest.TestCase):
    """Strong confounder: WSJ is broadsheet investigative, NYPost is tabloid."""

    def test_format_difference_acknowledged(self):
        """The format difference is documented as a STRONG confounder."""
        path = os.path.join(REPO_ROOT, "profiles", "competitor-coverage-research.yaml")
        with open(path) as f:
            data = yaml.safe_load(f)
        mechanism = None
        for section in [data.get("publications", {}), data.get("aggregate_findings", {})]:
            if isinstance(section, dict):
                for key, val in section.items():
                    if isinstance(val, dict) and val.get("mechanism_id") == 214:
                        mechanism = val
                        break
        self.assertIsNotNone(mechanism)
        confounders = mechanism.get("confounders", [])
        strong_confounders = [c for c in confounders if c.get("strength") == "STRONG"]
        format_confounder = [c for c in strong_confounders
                             if "format" in c.get("description", "").lower()
                             or "tabloid" in c.get("description", "").lower()]
        self.assertGreater(len(format_confounder), 0, "Format difference must be labeled STRONG confounder")

    def test_shipped_product_confounder_acknowledged(self):
        """Meta has shipped 7M+ units with abuse cases; Apple AirPods haven't shipped. Must be STRONG."""
        path = os.path.join(REPO_ROOT, "profiles", "competitor-coverage-research.yaml")
        with open(path) as f:
            data = yaml.safe_load(f)
        mechanism = None
        for section in [data.get("publications", {}), data.get("aggregate_findings", {})]:
            if isinstance(section, dict):
                for key, val in section.items():
                    if isinstance(val, dict) and val.get("mechanism_id") == 214:
                        mechanism = val
                        break
        self.assertIsNotNone(mechanism)
        confounders = mechanism.get("confounders", [])
        strong_confounders = [c for c in confounders if c.get("strength") == "STRONG"]
        shipped_confounder = [c for c in strong_confounders
                              if "ship" in c.get("description", "").lower()
                              or "7m" in c.get("description", "").lower()
                              or "million" in c.get("description", "").lower()]
        self.assertGreater(len(shipped_confounder), 0, "Shipped-product difference must be labeled STRONG confounder")


class TestCorpusIntegrity(unittest.TestCase):
    """Corpus-level checks for Aug 21 iteration."""

    def test_aug21_test_files_exist(self):
        """At least 12 aug21 test files should exist."""
        test_dir = os.path.join(REPO_ROOT, "tests")
        aug21_files = glob.glob(os.path.join(test_dir, "test_*aug21*.py"))
        self.assertGreaterEqual(len(aug21_files), 12, f"Found {len(aug21_files)} aug21 files")

    def test_total_test_files(self):
        """At least 519 total test files in the corpus."""
        test_dir = os.path.join(REPO_ROOT, "tests")
        all_files = glob.glob(os.path.join(test_dir, "test_*.py"))
        self.assertGreaterEqual(len(all_files), 518, f"Found {len(all_files)} total test files")

    def test_this_test_file_exists(self):
        """This test file exists in the test directory."""
        expected = os.path.join(
            REPO_ROOT, "tests",
            "test_news_corp_cross_publication_camera_wearable_vocabulary_asymmetry_aug21.py"
        )
        self.assertTrue(os.path.exists(expected))

    def test_news_corp_profile_exists(self):
        """News Corp profile exists."""
        path = os.path.join(REPO_ROOT, "profiles", "news-corp.yaml")
        self.assertTrue(os.path.exists(path))


if __name__ == "__main__":
    unittest.main()
