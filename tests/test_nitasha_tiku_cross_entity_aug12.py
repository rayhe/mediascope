"""
Test: Mechanism #72 — Nitasha Tiku Tech Culture Beat Structural Independence
Company-Agnostic Adversarial Coverage with Ownership-Chain Blind Spot

Nitasha Tiku (Valleywag → The Verge → BuzzFeed News → WIRED → Washington Post)
is one of the ONLY reporters in the MediaScope dataset who applies adversarial
framing across ALL major AI entities (Google, OpenAI, Meta, xAI, Character AI)
without the bifurcation seen in entity-specific beat reporters. Three structural
factors explain this: (1) "tech culture" beat is company-agnostic, (2) Gawker/
Valleywag adversarial DNA, (3) layoff-rehire cycle weakened institutional loyalty.

The CRITICAL finding: Despite company-agnostic adversarial coverage, Tiku has
NOT produced a dedicated adversarial investigation of Anthropic at WaPo (Bezos-
owned → Amazon → $13B Anthropic), consistent with Mechanism #65 (WaPo-Bezos-
Anthropic ownership chain). The Anthropic Gap may reflect ownership influence OR
legitimate news judgment (Anthropic has fewer consumer-facing scandals).

Source URLs:
- https://talkingbiznews.com/they-talk-biz-news/washington-post-hires-tiku-as-tech-culture-reporter/
- https://talkingbiznews.com/media-news/tiku-among-the-washington-post-layoffs/amp/
- https://muckrack.com/nitashatiku/articles
- https://theorg.com/org/the-washington-post/org-chart/nitasha-tiku
- https://clay.earth/profile/nitasha-tiku-163ac220
- https://www.cjr.org/analysis/washington-post-tries-regroup-after-major-cuts-layoffs-delayed-rehire-former-staff.php
- https://nypost.com/2026/04/02/media/washington-post-rehires-some-laid-off-staffers-after-job-cuts-decimated-newsroom-report/
- https://www.poynter.org/reporting-editing/2014/nitasha-tiku-joins-the-verge/
- https://www.adweek.com/performance-marketing/big-changes-in-tech-journalism-fake-steve-jobs-is-your-new-valleywag/
"""

import unittest
import os
import yaml

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def _load_yaml(filename):
    path = os.path.join(PROFILES_DIR, filename)
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def _get_mechanism():
    data = _load_yaml('competitor-coverage-research.yaml')
    cpf = data.get('cross_publication_findings', {})
    for key, value in cpf.items():
        if isinstance(value, dict) and value.get('mechanism_id') == 72:
            return value
    return None


class TestMechanism72Exists(unittest.TestCase):
    """Mechanism #72 exists in cross_publication_findings with required fields."""

    def test_mechanism_exists(self):
        m = _get_mechanism()
        self.assertIsNotNone(m, "Mechanism #72 not found in cross_publication_findings")

    def test_has_mechanism_id(self):
        m = _get_mechanism()
        self.assertEqual(m['mechanism_id'], 72)

    def test_has_name(self):
        m = _get_mechanism()
        self.assertIn('Nitasha Tiku', m.get('name', ''))

    def test_has_finding_summary(self):
        m = _get_mechanism()
        self.assertIn('finding_summary', m)
        self.assertGreater(len(m['finding_summary']), 100)

    def test_has_date_added(self):
        m = _get_mechanism()
        self.assertIn('date_added', m)

    def test_has_discovery_date(self):
        m = _get_mechanism()
        self.assertIn('discovery_date', m)

    def test_rotation_type_b(self):
        m = _get_mechanism()
        self.assertEqual(m.get('rotation_type'), 'B')

    def test_has_test_file(self):
        m = _get_mechanism()
        self.assertIn('test_file', m)
        self.assertIn('nitasha_tiku', m['test_file'])


class TestCareerPath(unittest.TestCase):
    """Nitasha Tiku career path: Valleywag editor → The Verge → BuzzFeed → WIRED → WaPo."""

    def test_career_length(self):
        """At least 6 positions documented."""
        data = _load_yaml('careers/journalists.yaml')
        journalist = None
        for j in data.get('journalists', []):
            if j.get('name') == 'Nitasha Tiku':
                journalist = j
                break
        self.assertIsNotNone(journalist, "Nitasha Tiku not found in journalists.yaml")
        self.assertGreaterEqual(len(journalist.get('career', [])), 6)

    def test_gawker_valleywag_presence(self):
        """Valleywag/Gawker Media career entry exists."""
        data = _load_yaml('careers/journalists.yaml')
        journalist = None
        for j in data.get('journalists', []):
            if j.get('name') == 'Nitasha Tiku':
                journalist = j
                break
        self.assertIsNotNone(journalist)
        pubs = [c.get('publication', '').lower() for c in journalist.get('career', [])]
        self.assertTrue(
            any('gawker' in p or 'valleywag' in p for p in pubs),
            f"No Gawker/Valleywag entry in career: {pubs}"
        )

    def test_wired_presence(self):
        """WIRED career entry exists."""
        data = _load_yaml('careers/journalists.yaml')
        journalist = None
        for j in data.get('journalists', []):
            if j.get('name') == 'Nitasha Tiku':
                journalist = j
                break
        self.assertIsNotNone(journalist)
        pubs = [c.get('publication', '').lower() for c in journalist.get('career', [])]
        self.assertTrue(any('wired' in p for p in pubs))

    def test_wapo_presence(self):
        """Washington Post career entry exists."""
        data = _load_yaml('careers/journalists.yaml')
        journalist = None
        for j in data.get('journalists', []):
            if j.get('name') == 'Nitasha Tiku':
                journalist = j
                break
        self.assertIsNotNone(journalist)
        pubs = [c.get('publication', '').lower() for c in journalist.get('career', [])]
        self.assertTrue(any('washington-post' in p or 'wapo' in p for p in pubs))

    def test_multi_publication(self):
        data = _load_yaml('careers/journalists.yaml')
        journalist = None
        for j in data.get('journalists', []):
            if j.get('name') == 'Nitasha Tiku':
                journalist = j
                break
        self.assertIsNotNone(journalist)
        self.assertTrue(journalist.get('multi_publication', False))

    def test_the_verge_presence(self):
        """The Verge career entry exists."""
        data = _load_yaml('careers/journalists.yaml')
        journalist = None
        for j in data.get('journalists', []):
            if j.get('name') == 'Nitasha Tiku':
                journalist = j
                break
        self.assertIsNotNone(journalist)
        pubs = [c.get('publication', '').lower() for c in journalist.get('career', [])]
        self.assertTrue(any('verge' in p for p in pubs))


class TestValleywagLineage(unittest.TestCase):
    """Valleywag editor role is the foundational adversarial credential."""

    def test_editor_role(self):
        """Tiku was EDITOR of Valleywag, not just contributor."""
        data = _load_yaml('careers/journalists.yaml')
        journalist = None
        for j in data.get('journalists', []):
            if j.get('name') == 'Nitasha Tiku':
                journalist = j
                break
        self.assertIsNotNone(journalist)
        gawker_roles = [
            c for c in journalist.get('career', [])
            if 'gawker' in c.get('publication', '').lower() or 'valleywag' in c.get('publication', '').lower()
        ]
        self.assertTrue(len(gawker_roles) > 0)
        roles = [c.get('role', '').lower() for c in gawker_roles]
        self.assertTrue(
            any('editor' in r for r in roles),
            f"Expected editor role at Gawker/Valleywag, got: {roles}"
        )

    def test_gawker_lineage_shared_with_zeff(self):
        """Maxwell Zeff (#63) and Dell Cameron also came from Gawker-descendant publications.
        Tiku's EDITOR role at the ORIGINAL Gawker property (Valleywag) is the deepest lineage."""
        m = _get_mechanism()
        self.assertIsNotNone(m)
        summary = m.get('finding_summary', '')
        self.assertIn('Valleywag', summary)

    def test_valleywag_was_adversarial(self):
        """Valleywag was the original adversarial Silicon Valley gossip blog."""
        m = _get_mechanism()
        self.assertIsNotNone(m)
        summary = m.get('finding_summary', '')
        self.assertTrue(
            'adversarial' in summary.lower() or 'gossip' in summary.lower(),
            "Finding summary should describe Valleywag's adversarial nature"
        )


class TestCompanyAgnosticAdversarialCoverage(unittest.TestCase):
    """Tiku applies adversarial framing to ALL major AI entities — unlike beat reporters."""

    def test_meta_adversarial_coverage(self):
        """Meta coverage includes adversarial framing."""
        m = _get_mechanism()
        self.assertIsNotNone(m)
        summary = m.get('finding_summary', '')
        self.assertIn('Meta', summary)

    def test_google_adversarial_coverage(self):
        """Google coverage includes adversarial framing."""
        m = _get_mechanism()
        self.assertIsNotNone(m)
        summary = m.get('finding_summary', '')
        self.assertIn('Google', summary)

    def test_openai_adversarial_coverage(self):
        """OpenAI coverage includes adversarial framing."""
        m = _get_mechanism()
        self.assertIsNotNone(m)
        summary = m.get('finding_summary', '')
        self.assertIn('OpenAI', summary)

    def test_xai_adversarial_coverage(self):
        """xAI coverage includes adversarial framing."""
        m = _get_mechanism()
        self.assertIsNotNone(m)
        summary = m.get('finding_summary', '')
        self.assertIn('xAI', summary)

    def test_character_ai_adversarial_coverage(self):
        """Character AI teen safety coverage exists."""
        m = _get_mechanism()
        self.assertIsNotNone(m)
        summary = m.get('finding_summary', '')
        self.assertIn('Character', summary)

    def test_multi_entity_count(self):
        """At least 5 distinct entities receive adversarial coverage."""
        m = _get_mechanism()
        self.assertIsNotNone(m)
        summary = m.get('finding_summary', '')
        entities_found = 0
        for entity in ['Meta', 'Google', 'OpenAI', 'xAI', 'Character']:
            if entity in summary:
                entities_found += 1
        self.assertGreaterEqual(entities_found, 5)


class TestBeatStructureDistinction(unittest.TestCase):
    """Tech culture beat is company-agnostic, unlike entity-specific beats."""

    def test_beat_is_tech_culture(self):
        """Tiku's beat is 'tech culture', not 'AI' or 'Meta'."""
        data = _load_yaml('careers/journalists.yaml')
        journalist = None
        for j in data.get('journalists', []):
            if j.get('name') == 'Nitasha Tiku':
                journalist = j
                break
        self.assertIsNotNone(journalist)
        wapo = [
            c for c in journalist.get('career', [])
            if 'washington-post' in c.get('publication', '').lower() or 'wapo' in c.get('publication', '').lower()
        ]
        self.assertTrue(len(wapo) > 0)
        beats = [c.get('beat', '').lower() for c in wapo]
        self.assertTrue(
            any('culture' in b for b in beats),
            f"Expected 'tech culture' beat at WaPo, got: {beats}"
        )

    def test_mechanism_references_beat_structure(self):
        """Finding summary discusses beat structure as explanatory factor."""
        m = _get_mechanism()
        self.assertIsNotNone(m)
        summary = m.get('finding_summary', '').lower()
        self.assertTrue(
            'beat' in summary or 'tech culture' in summary,
            "Finding should reference beat structure"
        )

    def test_contrast_with_entity_specific_beats(self):
        """Mechanism should contrast with entity-specific beat patterns (Mechanisms #56, #67)."""
        m = _get_mechanism()
        self.assertIsNotNone(m)
        extends = m.get('extends_mechanisms', [])
        cross_refs = m.get('cross_references', [])
        # Should reference at least one beat-assignment mechanism
        all_refs = extends + [
            cr.get('mechanism_id', cr) if isinstance(cr, dict) else cr
            for cr in cross_refs
        ]
        # Mechanisms 56, 67 are beat assignment mechanisms
        beat_refs = [r for r in all_refs if r in [56, 67]]
        self.assertTrue(
            len(beat_refs) > 0 or any(str(r) in ['56', '67'] for r in all_refs),
            f"Should reference beat-assignment mechanisms #56 or #67, has: {all_refs}"
        )


class TestLayoffRehireCycle(unittest.TestCase):
    """WaPo layoff (Feb 2026) and rehire (~Mar-Apr 2026) documented."""

    def test_layoff_documented(self):
        """Tiku layoff from WaPo in Feb 2026 is documented."""
        data = _load_yaml('careers/journalists.yaml')
        journalist = None
        for j in data.get('journalists', []):
            if j.get('name') == 'Nitasha Tiku':
                journalist = j
                break
        self.assertIsNotNone(journalist)
        # Check career entries for layoff event or notes
        all_text = str(journalist).lower()
        self.assertTrue(
            'laid off' in all_text or 'layoff' in all_text or 'rehire' in all_text,
            "Career should document layoff/rehire cycle"
        )

    def test_rehire_documented(self):
        """Tiku rehire at WaPo is documented."""
        data = _load_yaml('careers/journalists.yaml')
        journalist = None
        for j in data.get('journalists', []):
            if j.get('name') == 'Nitasha Tiku':
                journalist = j
                break
        self.assertIsNotNone(journalist)
        all_text = str(journalist).lower()
        self.assertTrue(
            'rehire' in all_text or 'return' in all_text or 'brought back' in all_text,
            "Career should document rehire"
        )

    def test_mechanism_mentions_layoff(self):
        """Mechanism finding references the layoff-rehire cycle."""
        m = _get_mechanism()
        self.assertIsNotNone(m)
        summary = m.get('finding_summary', '').lower()
        self.assertTrue(
            'layoff' in summary or 'laid off' in summary or 'rehire' in summary,
            "Finding summary should reference layoff-rehire cycle"
        )


class TestAnthropicGap(unittest.TestCase):
    """The Anthropic Gap: no dedicated adversarial investigation despite WaPo ownership chain."""

    def test_anthropic_gap_documented(self):
        """Finding summary documents absence of dedicated Anthropic investigation."""
        m = _get_mechanism()
        self.assertIsNotNone(m)
        summary = m.get('finding_summary', '').lower()
        self.assertTrue(
            'anthropic' in summary,
            "Finding should discuss Anthropic coverage"
        )

    def test_connects_to_mechanism_65(self):
        """Cross-references Mechanism #65 (WaPo-Bezos-Anthropic ownership chain)."""
        m = _get_mechanism()
        self.assertIsNotNone(m)
        extends = m.get('extends_mechanisms', [])
        cross_refs = m.get('cross_references', [])
        all_refs = extends + [
            cr.get('mechanism_id', cr) if isinstance(cr, dict) else cr
            for cr in cross_refs
        ]
        self.assertIn(65, all_refs, f"Should reference mechanism #65, has: {all_refs}")

    def test_documents_confounding_factor(self):
        """Confounding factor: Anthropic genuinely has fewer consumer-facing scandals."""
        m = _get_mechanism()
        self.assertIsNotNone(m)
        confounders = m.get('confounding_factors', m.get('confounders', []))
        self.assertGreater(len(confounders), 0, "Should have confounding factors")
        all_text = str(confounders).lower()
        self.assertTrue(
            'anthropic' in all_text or 'consumer' in all_text or 'scandal' in all_text,
            "Should include Anthropic confounding factor"
        )

    def test_wapo_bezos_amazon_anthropic_chain(self):
        """Finding explicitly describes the Bezos→Amazon→Anthropic financial chain."""
        m = _get_mechanism()
        self.assertIsNotNone(m)
        summary = m.get('finding_summary', '')
        self.assertTrue(
            'Bezos' in summary or 'Amazon' in summary,
            "Finding should reference Bezos/Amazon ownership chain"
        )


class TestConfoundingFactors(unittest.TestCase):
    """At least 6 confounding factors with strength ratings."""

    def test_minimum_confounders(self):
        m = _get_mechanism()
        self.assertIsNotNone(m)
        confounders = m.get('confounding_factors', m.get('confounders', []))
        self.assertGreaterEqual(len(confounders), 6, f"Expected >=6 confounders, got {len(confounders)}")

    def test_confounders_have_strength(self):
        m = _get_mechanism()
        self.assertIsNotNone(m)
        confounders = m.get('confounding_factors', m.get('confounders', []))
        for c in confounders:
            self.assertIn('strength', c, f"Confounder missing strength: {c}")

    def test_confounders_have_factor(self):
        m = _get_mechanism()
        self.assertIsNotNone(m)
        confounders = m.get('confounding_factors', m.get('confounders', []))
        for c in confounders:
            self.assertIn('factor', c, f"Confounder missing factor: {c}")

    def test_confounders_have_rebuttal(self):
        m = _get_mechanism()
        self.assertIsNotNone(m)
        confounders = m.get('confounding_factors', m.get('confounders', []))
        for c in confounders:
            self.assertIn('rebuttal', c, f"Confounder missing rebuttal: {c}")

    def test_at_least_one_strong(self):
        m = _get_mechanism()
        self.assertIsNotNone(m)
        confounders = m.get('confounding_factors', m.get('confounders', []))
        strong = [c for c in confounders if c.get('strength') == 'STRONG']
        self.assertGreater(len(strong), 0, "Should have at least one STRONG confounder")


class TestTestablePredictions(unittest.TestCase):
    """At least 4 testable predictions."""

    def test_has_predictions(self):
        m = _get_mechanism()
        self.assertIsNotNone(m)
        preds = m.get('testable_predictions', [])
        self.assertGreaterEqual(len(preds), 4)

    def test_predictions_are_falsifiable(self):
        """Predictions contain conditional/future language."""
        m = _get_mechanism()
        self.assertIsNotNone(m)
        preds = m.get('testable_predictions', [])
        for p in preds:
            p_lower = str(p).lower()
            self.assertTrue(
                any(w in p_lower for w in ['if', 'will', 'would', 'should', 'predict', 'expect']),
                f"Prediction should be falsifiable: {p}"
            )


class TestCrossReferences(unittest.TestCase):
    """Cross-references to related mechanisms."""

    def test_has_cross_references(self):
        m = _get_mechanism()
        self.assertIsNotNone(m)
        extends = m.get('extends_mechanisms', [])
        cross_refs = m.get('cross_references', [])
        total = len(extends) + len(cross_refs)
        self.assertGreaterEqual(total, 4, f"Expected >=4 cross-references, got {total}")

    def test_references_mechanism_65_wapo_bezos(self):
        """References #65 (WaPo-Bezos-Anthropic ownership chain)."""
        m = _get_mechanism()
        self.assertIsNotNone(m)
        all_refs = m.get('extends_mechanisms', []) + [
            cr.get('mechanism_id', cr) if isinstance(cr, dict) else cr
            for cr in m.get('cross_references', [])
        ]
        self.assertIn(65, all_refs)

    def test_references_mechanism_63_zeff(self):
        """References #63 (Maxwell Zeff source access asymmetry) — shared Gawker lineage."""
        m = _get_mechanism()
        self.assertIsNotNone(m)
        all_refs = m.get('extends_mechanisms', []) + [
            cr.get('mechanism_id', cr) if isinstance(cr, dict) else cr
            for cr in m.get('cross_references', [])
        ]
        self.assertIn(63, all_refs)

    def test_references_mechanism_57_seetharaman(self):
        """References #57 (Seetharaman frame-lock) — contrast pattern."""
        m = _get_mechanism()
        self.assertIsNotNone(m)
        all_refs = m.get('extends_mechanisms', []) + [
            cr.get('mechanism_id', cr) if isinstance(cr, dict) else cr
            for cr in m.get('cross_references', [])
        ]
        self.assertIn(57, all_refs)

    def test_references_beat_assignment_mechanism(self):
        """References #56 or #67 (beat assignment asymmetry patterns)."""
        m = _get_mechanism()
        self.assertIsNotNone(m)
        all_refs = m.get('extends_mechanisms', []) + [
            cr.get('mechanism_id', cr) if isinstance(cr, dict) else cr
            for cr in m.get('cross_references', [])
        ]
        self.assertTrue(
            56 in all_refs or 67 in all_refs,
            f"Should reference #56 or #67, has: {all_refs}"
        )


class TestSourceURLs(unittest.TestCase):
    """Source URLs are present and reference primary sources."""

    def test_has_source_urls(self):
        m = _get_mechanism()
        self.assertIsNotNone(m)
        urls = m.get('source_urls', [])
        self.assertGreaterEqual(len(urls), 5)

    def test_urls_are_strings(self):
        m = _get_mechanism()
        self.assertIsNotNone(m)
        urls = m.get('source_urls', [])
        for url in urls:
            self.assertIsInstance(url, str)
            self.assertTrue(url.startswith('http'), f"URL should start with http: {url}")

    def test_includes_muckrack(self):
        """Source URLs include Muck Rack (article archive)."""
        m = _get_mechanism()
        self.assertIsNotNone(m)
        urls = m.get('source_urls', [])
        self.assertTrue(
            any('muckrack' in u for u in urls),
            f"Should include muckrack URL: {urls}"
        )


class TestGawkerLineagePipeline(unittest.TestCase):
    """Track the Gawker-to-WaPo pipeline vs Gawker-to-WIRED pipeline."""

    def test_distinct_from_gawker_to_wired_pattern(self):
        """Tiku's Gawker→WaPo path produces different outcomes than
        the Gawker→WIRED path (Zeff #63, Cameron/Mehrotra)."""
        m = _get_mechanism()
        self.assertIsNotNone(m)
        summary = m.get('finding_summary', '')
        # Should distinguish the two Gawker exit paths
        self.assertTrue(
            'WIRED' in summary or 'Condé Nast' in summary,
            "Should contrast with WIRED/Condé Nast path"
        )

    def test_explains_different_outcome(self):
        """The mechanism explains WHY Tiku's outcome differs from Zeff/Cameron."""
        m = _get_mechanism()
        self.assertIsNotNone(m)
        summary = m.get('finding_summary', '').lower()
        self.assertTrue(
            'beat' in summary or 'culture' in summary or 'company-agnostic' in summary,
            "Should explain beat structure as differentiating factor"
        )


if __name__ == '__main__':
    unittest.main()
