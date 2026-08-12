"""
Deepa Seetharaman Cross-Entity Analysis: Reporter Frame-Lock Across Institutional Boundaries

Mechanism #57: When a reporter builds a decade of professional reputation on adversarial
coverage of one company, that frame persists even after migrating to a new publication —
including one that has a direct financial relationship with the covered company. Meanwhile,
the new beat mandate shapes aspirational framing for the companies named in it.

Natural experiment: Seetharaman spent 10 years at WSJ (News Corp, $250M OpenAI deal) as
the primary Meta/Facebook beat reporter, winning a George Polk Award for the Facebook Files.
In May 2025, she moved to Reuters (Thomson Reuters has a multi-year Meta AI content deal
since Oct 2024 AND is in licensing talks with other AI providers). At Reuters, she was
explicitly hired to cover "AI and OpenAI" — the company literally named in her job
description.

Key finding: Despite Reuters having a direct Meta content licensing deal, Seetharaman's
Meta coverage at Reuters retains adversarial framing (costs, layoffs, model failures).
Meanwhile, her OpenAI and Anthropic coverage at Reuters uses growth/aspiration language.
This suggests professional identity capture is a more powerful framing determinant than
institutional financial incentives.

Sources:
- Reuters hiring announcement (Ken Li, via Talking Biz News):
  https://talkingbiznews.com/media-news/reuters-hires-seetharaman-to-cover-artificial-intelligence/
- Meta-Reuters content deal (Oct 25, 2024):
  https://www.reuters.com/technology/artificial-intelligence/meta-platforms-use-reuters-news-content-ai-chatbot-2024-10-25/
  https://siliconangle.com/2024/10/25/meta-inks-multiyear-ai-content-licensing-deal-reuters/
- Thomson Reuters in licensing talks with AI firms:
  https://news.bloomberglaw.com/ip-law/thomson-reuters-in-talks-with-ai-firms-over-licensing-deals-2
- Meta layoffs exclusive (Mar 2026, Seetharaman + Horwitz + Paul):
  https://srnnews.com/exclusive-meta-planning-sweeping-layoffs-as-ai-costs-mount/
- Anthropic revenue exclusive (Oct 2025, Seetharaman):
  https://muckrack.com/dseetharaman/articles
- "Anthropic v. OpenAI" feature (Jun 2026, Seetharaman + Wang):
  https://www.lapost.com/content/anthropic-v-openai-behind-the-bitter-battle-for-the-future-of-ai
- "OpenAI super app" (Jul 2026, Seetharaman + Babu):
  https://www.lapost.com/content/openai-launches-chatgpt-work
- Meta additional content deals (Dec 2025, 7 publishers):
  http://digiday.com/media/meta-enters-ai-licensing-fray-striking-deals-with-people-inc-usa-today-co-and-more/
- Meta in talks with Axel Springer, Fox, News Corp for AI licensing (Sep 2025):
  https://www.reuters.com/business/meta-talks-with-axel-springer-fox-others-ai-news-licensing-wsj-reports-2025-09-18/
- WSJ departure (May 2025):
  https://talkingbiznews.com/media-news/wsj-tech-reporter-seetharaman-departs/amp/
- Wisconsin BJIR (2025):
  https://business.wisc.edu/news/wisconsin-school-of-business-hosts-award-winning-journalist-deepa-seetharaman/
- News Corp $250M/5yr OpenAI deal:
  Documented in profiles/news-corp.yaml
"""

import unittest
import yaml
import os
import glob


def load_yaml(path):
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(base, path)) as f:
        return yaml.safe_load(f)


class TestSeetharamanCareerMigration(unittest.TestCase):
    """Verify career migration data is documented in journalist profiles."""

    def setUp(self):
        self.journalists = load_yaml('profiles/careers/journalists.yaml')
        self.ds = None
        jlist = self.journalists.get('journalists', self.journalists)
        if isinstance(jlist, list):
            for j in jlist:
                if isinstance(j, dict) and j.get('name') == 'Deepa Seetharaman':
                    self.ds = j
                    break
        self.assertIsNotNone(self.ds, "Deepa Seetharaman must exist in journalists.yaml")

    def test_career_has_three_phases(self):
        """Career trajectory: Reuters → WSJ → Reuters (boomerang)."""
        career = self.ds.get('career', [])
        self.assertGreaterEqual(len(career), 3,
            "Must document at least 3 career phases (Reuters, WSJ, Reuters return)")

    def test_wsj_decade_documented(self):
        """10-year WSJ tenure covering Meta/Facebook must be documented."""
        career = self.ds.get('career', [])
        wsj_stints = [c for c in career if c.get('publication') == 'wall-street-journal']
        self.assertGreaterEqual(len(wsj_stints), 1)
        wsj = wsj_stints[0]
        notes = wsj.get('notes', '')
        # Should mention decade or 10 years
        self.assertTrue('decade' in notes.lower() or '10 year' in notes.lower(),
            "WSJ stint must note the 10-year tenure")

    def test_reuters_return_documented(self):
        """Return to Reuters in 2025 for AI coverage must be documented."""
        career = self.ds.get('career', [])
        reuters_stints = [c for c in career if c.get('publication') == 'reuters']
        # Should have 2 Reuters stints (original + return)
        self.assertGreaterEqual(len(reuters_stints), 2,
            "Must document both original Reuters stint and 2025 return")
        return_stint = reuters_stints[-1]
        self.assertIn('2025', str(return_stint.get('start', '')))

    def test_facebook_files_award_documented(self):
        """George Polk Award for Facebook Files must be documented."""
        awards = self.ds.get('awards', [])
        polk_awards = [a for a in awards if 'polk' in a.get('name', '').lower()]
        self.assertGreaterEqual(len(polk_awards), 1,
            "George Polk Award for Facebook Files must be documented")

    def test_beats_include_meta_and_ai(self):
        """Beats must include both facebook_meta and AI coverage."""
        beats = self.ds.get('beats', [])
        beat_str = ' '.join(beats).lower()
        self.assertTrue('facebook' in beat_str or 'meta' in beat_str,
            "Beats must include Facebook/Meta")
        self.assertTrue('ai' in beat_str or 'artificial_intelligence' in beat_str,
            "Beats must include AI")


class TestReporterFrameLockMechanism(unittest.TestCase):
    """Verify mechanism #57 is documented in competitor-coverage-research.yaml."""

    def setUp(self):
        self.research = load_yaml('profiles/competitor-coverage-research.yaml')
        self.cpf = self.research.get('cross_publication_findings', {})
        self.mechanism = None
        if isinstance(self.cpf, dict):
            for key, val in self.cpf.items():
                if isinstance(val, dict) and val.get('mechanism_id') == 57:
                    self.mechanism = val
                    break
        elif isinstance(self.cpf, list):
            for m in self.cpf:
                if isinstance(m, dict) and m.get('mechanism_id') == 57:
                    self.mechanism = m
                    break

    def test_mechanism_57_exists(self):
        """Mechanism #57 must exist in cross_publication_findings."""
        self.assertIsNotNone(self.mechanism,
            "Mechanism #57 (Reporter Frame-Lock) must exist in cross_publication_findings")

    def test_mechanism_has_journalist(self):
        """Mechanism must name Deepa Seetharaman."""
        m = self.mechanism
        self.assertIsNotNone(m)
        content = str(m).lower()
        self.assertIn('seetharaman', content)

    def test_mechanism_has_source_urls(self):
        """Mechanism must have source URLs."""
        m = self.mechanism
        self.assertIsNotNone(m)
        sources = m.get('source_urls', m.get('sources', []))
        self.assertGreaterEqual(len(sources), 3,
            "Must have at least 3 source URLs")

    def test_mechanism_documents_migration(self):
        """Mechanism must document the WSJ→Reuters migration."""
        m = self.mechanism
        self.assertIsNotNone(m)
        content = str(m).lower()
        self.assertTrue('wsj' in content or 'wall street journal' in content,
            "Must reference WSJ")
        self.assertIn('reuters', content, "Must reference Reuters")

    def test_mechanism_has_date_added(self):
        """Mechanism must have date_added."""
        m = self.mechanism
        self.assertIsNotNone(m)
        self.assertIn('date_added', m)

    def test_mechanism_has_test_file(self):
        """Mechanism must reference this test file."""
        m = self.mechanism
        self.assertIsNotNone(m)
        tf = m.get('test_file', '')
        self.assertIn('deepa_seetharaman', tf)


class TestMetaReutersFinancialRelationship(unittest.TestCase):
    """Verify the Meta-Reuters content licensing deal is documented."""

    def setUp(self):
        self.research = load_yaml('profiles/competitor-coverage-research.yaml')
        self.cpf = self.research.get('cross_publication_findings', {})
        self.mechanism = None
        if isinstance(self.cpf, dict):
            for key, val in self.cpf.items():
                if isinstance(val, dict) and val.get('mechanism_id') == 57:
                    self.mechanism = val
                    break
        elif isinstance(self.cpf, list):
            for m in self.cpf:
                if isinstance(m, dict) and m.get('mechanism_id') == 57:
                    self.mechanism = m
                    break

    def test_meta_reuters_deal_documented(self):
        """Meta-Reuters multi-year content licensing deal (Oct 2024) must be documented."""
        m = self.mechanism
        self.assertIsNotNone(m)
        content = str(m).lower()
        self.assertTrue('content licensing' in content or 'content deal' in content or
                       'licensing deal' in content,
            "Must document Meta-Reuters content licensing deal")

    def test_reuters_meta_ai_integration(self):
        """Reuters content in Meta AI chatbot must be documented."""
        m = self.mechanism
        self.assertIsNotNone(m)
        content = str(m).lower()
        self.assertTrue('meta ai' in content or 'chatbot' in content,
            "Must document Reuters content integration in Meta AI")

    def test_dual_financial_relationship_noted(self):
        """Reuters' dual position (Meta deal + AI provider licensing talks) must be noted."""
        m = self.mechanism
        self.assertIsNotNone(m)
        content = str(m).lower()
        # Should note that Reuters has financial relationships with multiple AI entities
        self.assertTrue('thomson reuters' in content or 'dual' in content or
                       'licensing talks' in content or 'multiple' in content,
            "Must note Reuters' dual/multiple financial relationships")


class TestWSJNewsCorpOpenAIDeal(unittest.TestCase):
    """Verify News Corp-OpenAI financial relationship documented as context."""

    def setUp(self):
        self.research = load_yaml('profiles/competitor-coverage-research.yaml')
        self.cpf = self.research.get('cross_publication_findings', {})
        self.mechanism = None
        if isinstance(self.cpf, dict):
            for key, val in self.cpf.items():
                if isinstance(val, dict) and val.get('mechanism_id') == 57:
                    self.mechanism = val
                    break
        elif isinstance(self.cpf, list):
            for m in self.cpf:
                if isinstance(m, dict) and m.get('mechanism_id') == 57:
                    self.mechanism = m
                    break

    def test_news_corp_openai_deal_referenced(self):
        """News Corp $250M OpenAI deal must be referenced as prior-publication context."""
        m = self.mechanism
        self.assertIsNotNone(m)
        content = str(m).lower()
        self.assertTrue('news corp' in content or 'openai' in content,
            "Must reference News Corp/OpenAI deal as WSJ-era context")


class TestMetaCoverageFramingAtReuters(unittest.TestCase):
    """Verify Meta coverage framing analysis at Reuters is documented."""

    def setUp(self):
        self.research = load_yaml('profiles/competitor-coverage-research.yaml')
        self.cpf = self.research.get('cross_publication_findings', {})
        self.mechanism = None
        if isinstance(self.cpf, dict):
            for key, val in self.cpf.items():
                if isinstance(val, dict) and val.get('mechanism_id') == 57:
                    self.mechanism = val
                    break
        elif isinstance(self.cpf, list):
            for m in self.cpf:
                if isinstance(m, dict) and m.get('mechanism_id') == 57:
                    self.mechanism = m
                    break

    def test_meta_stress_framing_documented(self):
        """Adversarial/stress framing of Meta at Reuters must be documented."""
        m = self.mechanism
        self.assertIsNotNone(m)
        content = str(m).lower()
        self.assertTrue('layoff' in content or 'stress' in content or
                       'adversarial' in content or 'setback' in content,
            "Must document stress/adversarial framing of Meta coverage")

    def test_anthropic_growth_framing_documented(self):
        """Growth/aspiration framing of Anthropic at Reuters must be documented."""
        m = self.mechanism
        self.assertIsNotNone(m)
        content = str(m).lower()
        self.assertTrue('growth' in content or 'aspiration' in content or
                       'triple' in content or 'revenue' in content,
            "Must document growth/aspiration framing of Anthropic")

    def test_openai_product_framing_documented(self):
        """Product/ambition framing of OpenAI at Reuters must be documented."""
        m = self.mechanism
        self.assertIsNotNone(m)
        content = str(m).lower()
        self.assertTrue('openai' in content,
            "Must document OpenAI coverage framing")

    def test_framing_delta_across_entities(self):
        """Cross-entity framing difference must be explicitly documented."""
        m = self.mechanism
        self.assertIsNotNone(m)
        content = str(m).lower()
        self.assertTrue('asymmetry' in content or 'delta' in content or
                       'different' in content or 'contrast' in content,
            "Must document framing delta across covered entities")


class TestProfessionalIdentityCapture(unittest.TestCase):
    """Verify the professional identity capture mechanism is documented."""

    def setUp(self):
        self.research = load_yaml('profiles/competitor-coverage-research.yaml')
        self.cpf = self.research.get('cross_publication_findings', {})
        self.mechanism = None
        if isinstance(self.cpf, dict):
            for key, val in self.cpf.items():
                if isinstance(val, dict) and val.get('mechanism_id') == 57:
                    self.mechanism = val
                    break
        elif isinstance(self.cpf, list):
            for m in self.cpf:
                if isinstance(m, dict) and m.get('mechanism_id') == 57:
                    self.mechanism = m
                    break

    def test_frame_lock_concept_documented(self):
        """Frame-lock or professional identity capture must be named."""
        m = self.mechanism
        self.assertIsNotNone(m)
        content = str(m).lower()
        self.assertTrue('frame' in content or 'professional identity' in content or
                       'reputation' in content or 'career' in content,
            "Must document frame-lock or professional identity capture concept")

    def test_overrides_institutional_incentive(self):
        """Must document that professional frame persists despite institutional financial incentive."""
        m = self.mechanism
        self.assertIsNotNone(m)
        content = str(m).lower()
        # Key insight: despite Reuters having Meta deal, coverage stayed adversarial
        self.assertTrue('despite' in content or 'persist' in content or
                       'independent' in content or 'override' in content or
                       'regardless' in content,
            "Must document that professional frame persists despite institutional incentives")

    def test_beat_mandate_effect(self):
        """Must document how beat mandate ('AI and OpenAI') shapes framing."""
        m = self.mechanism
        self.assertIsNotNone(m)
        content = str(m).lower()
        self.assertTrue('beat' in content or 'mandate' in content or
                       'hired to cover' in content or 'job description' in content,
            "Must document how beat mandate shapes coverage direction")


class TestConfoundingFactors(unittest.TestCase):
    """Verify confounding factors are documented."""

    def setUp(self):
        self.research = load_yaml('profiles/competitor-coverage-research.yaml')
        self.cpf = self.research.get('cross_publication_findings', {})
        self.mechanism = None
        if isinstance(self.cpf, dict):
            for key, val in self.cpf.items():
                if isinstance(val, dict) and val.get('mechanism_id') == 57:
                    self.mechanism = val
                    break
        elif isinstance(self.cpf, list):
            for m in self.cpf:
                if isinstance(m, dict) and m.get('mechanism_id') == 57:
                    self.mechanism = m
                    break

    def test_confounding_factors_exist(self):
        """Must document confounding factors."""
        m = self.mechanism
        self.assertIsNotNone(m)
        cf = m.get('confounding_factors', m.get('legitimate_factors', []))
        self.assertGreaterEqual(len(cf), 4,
            "Must document at least 4 confounding factors")

    def test_wire_style_constraint_noted(self):
        """Wire service style constraints should be a confounding factor."""
        m = self.mechanism
        self.assertIsNotNone(m)
        content = str(m).lower()
        self.assertTrue('wire' in content or 'reuters style' in content or
                       'wire service' in content or 'editorial style' in content,
            "Must note wire service style constraints as confounding factor")

    def test_co_authorship_noted(self):
        """Co-authorship on Meta layoffs piece should be noted."""
        m = self.mechanism
        self.assertIsNotNone(m)
        content = str(m).lower()
        self.assertTrue('horwitz' in content or 'co-author' in content or
                       'paul' in content,
            "Must note co-authorship as confounding factor")


class TestTestablePredicitions(unittest.TestCase):
    """Verify falsifiable predictions are documented."""

    def setUp(self):
        self.research = load_yaml('profiles/competitor-coverage-research.yaml')
        self.cpf = self.research.get('cross_publication_findings', {})
        self.mechanism = None
        if isinstance(self.cpf, dict):
            for key, val in self.cpf.items():
                if isinstance(val, dict) and val.get('mechanism_id') == 57:
                    self.mechanism = val
                    break
        elif isinstance(self.cpf, list):
            for m in self.cpf:
                if isinstance(m, dict) and m.get('mechanism_id') == 57:
                    self.mechanism = m
                    break

    def test_testable_predictions_exist(self):
        """Must include falsifiable predictions."""
        m = self.mechanism
        self.assertIsNotNone(m)
        preds = m.get('testable_predictions', m.get('predictions', []))
        self.assertGreaterEqual(len(preds), 2,
            "Must have at least 2 testable predictions")


class TestWireServiceAmplificationEffect(unittest.TestCase):
    """Verify wire service amplification effect is documented."""

    def setUp(self):
        self.research = load_yaml('profiles/competitor-coverage-research.yaml')
        self.cpf = self.research.get('cross_publication_findings', {})
        self.mechanism = None
        if isinstance(self.cpf, dict):
            for key, val in self.cpf.items():
                if isinstance(val, dict) and val.get('mechanism_id') == 57:
                    self.mechanism = val
                    break
        elif isinstance(self.cpf, list):
            for m in self.cpf:
                if isinstance(m, dict) and m.get('mechanism_id') == 57:
                    self.mechanism = m
                    break

    def test_syndication_effect_documented(self):
        """Wire service syndication amplification must be documented."""
        m = self.mechanism
        self.assertIsNotNone(m)
        content = str(m).lower()
        self.assertTrue('syndic' in content or 'amplif' in content or
                       'propagat' in content or 'hundreds of outlets' in content or
                       'wire service' in content,
            "Must document wire service syndication amplification effect")

    def test_global_reach_noted(self):
        """Global reach of Reuters framing must be noted."""
        m = self.mechanism
        self.assertIsNotNone(m)
        content = str(m).lower()
        self.assertTrue('global' in content or 'worldwide' in content or
                       'international' in content,
            "Must note global reach of Reuters framing")


class TestCrossReferenceWithExistingMechanisms(unittest.TestCase):
    """Verify cross-references with related mechanisms."""

    def setUp(self):
        self.research = load_yaml('profiles/competitor-coverage-research.yaml')
        self.cpf = self.research.get('cross_publication_findings', {})
        self.mechanism = None
        if isinstance(self.cpf, dict):
            for key, val in self.cpf.items():
                if isinstance(val, dict) and val.get('mechanism_id') == 57:
                    self.mechanism = val
                    break
        elif isinstance(self.cpf, list):
            for m in self.cpf:
                if isinstance(m, dict) and m.get('mechanism_id') == 57:
                    self.mechanism = m
                    break

    def test_references_beat_concentration_pattern(self):
        """Should reference the AI beat concentration pattern (mechanisms #52, Cade Metz)."""
        m = self.mechanism
        self.assertIsNotNone(m)
        content = str(m).lower()
        # Should connect to the broader pattern of AI beats = OpenAI beats
        self.assertTrue('beat concentration' in content or 'hayden field' in content or
                       'cade metz' in content or '#52' in content or
                       'ai beat' in content or 'openai beat' in content,
            "Should reference the AI beat concentration pattern")

    def test_contrasts_with_institutional_mechanisms(self):
        """Should contrast with purely institutional financial mechanisms."""
        m = self.mechanism
        self.assertIsNotNone(m)
        content = str(m).lower()
        self.assertTrue('institutional' in content or 'publication-level' in content or
                       'individual' in content or 'reporter-level' in content,
            "Should contrast individual vs institutional framing determinants")


if __name__ == '__main__':
    unittest.main()
