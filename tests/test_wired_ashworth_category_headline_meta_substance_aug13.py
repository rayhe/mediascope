"""
Cross-entity analysis: Boone Ashworth (WIRED) — Mechanism #89
Category-Universal Privacy Headline with Entity-Specific Substance

KEY PATTERN: WIRED publishes "Is It Possible to Make Smart Glasses That
Aren't Creepy?" (Aug 2, 2026) — a headline framing the ENTIRE smart
glasses category as a privacy question — but delivers substance that is
overwhelmingly Meta-specific. Samsung Galaxy Glasses, announced with
hands-on demos 11 days earlier at Galaxy Unpacked (Jul 22, 2026) using
IDENTICAL privacy-relevant hardware (same Snapdragon AR1 Gen 1, 12MP
camera, LED indicator), receive a single dismissive sentence treating
them as future entrants. Apple is framed sympathetically for delaying
glasses "to address the privacy issues."

This is a measurable headline-substance gap: the headline asks a
universal question, the substance answers it as a Meta-specific
indictment while exempting competitors with identical hardware.

Evidence chain:

1. WIRED article "Is It Possible to Make Smart Glasses That Aren't
   Creepy?" (Boone Ashworth, Aug 2, 2026):
   - Headline: category-universal ("smart glasses")
   - Opening: "companies, massive and tiny, are all vying for nuggets
     in the smart-glasses gold rush" — category framing
   - Paragraph 2: "The prime target for such criticism is the biggest
     company in the space, Meta" — shifts to Meta-specific
   - Paragraphs 2-4: Meta camera capabilities, LED bypass, NameTag FR,
     WIRED's own June 4 investigation self-cited, anti-tamper update
   - Samsung/Google: ONE sentence — "This conversation around privacy
     and smart glasses is only going to grow as other big tech
     companies—notably Google and Samsung—enter the space later this year."
   - Apple: ONE sentence, sympathetic — "reportedly delayed production
     to address the privacy issues"
   - Small companies (Even Realities, Solos, Vuzix): framed as
     privacy-first alternatives to Meta — "anti-Meta crowd"
   - Source: https://www.wired.com/story/is-it-possible-to-make-privacy-friendly-smart-glasses/
   - Mirror: https://gokawiil.com/article/325902

2. Samsung Galaxy Unpacked (Jul 22, 2026, London) — 11 days before article:
   - Samsung showcased Galaxy Glasses with hands-on demos
   - Same Snapdragon AR1 Gen 1 chip as Meta Ray-Ban
   - 12MP camera (same as Meta)
   - LED indicator with anti-tamper (same as Meta)
   - Google Gemini AI processes camera queries via cloud
   - Fall 2026 launch confirmed
   - Source: https://news.samsung.com/us/samsung-interview-galaxy-unpacked-july-2026-inside-engineering-intelligent-eyewear

3. Google Gemini data retention — ZERO investigation:
   - Samsung glasses route camera/AI queries through Google Gemini cloud
   - Google's Gemini data retention policies for wearable queries undisclosed
   - WIRED has NOT investigated what Google does with glasses camera data
   - Contrast: WIRED spent multiple articles investigating Meta's Kenya
     subcontractor video review and NameTag facial recognition

4. Self-citation pattern:
   - Article cites "a WIRED report exposed this feature" re: NameTag
   - WIRED (Condé Nast) has OpenAI content licensing deal since Aug 2024
   - Self-referential investigation chain: investigate Meta → cite own
     investigation → build narrative momentum that excludes competitors

5. "Later this year" temporal dismissal:
   - Samsung Galaxy Glasses were publicly announced with specs, hands-on
     demos, confirmed fall launch, and detailed privacy features (LED,
     anti-tamper, wear detection, camera disable) ELEVEN days before
   - Framing them as entering "later this year" erases the fact that
     Samsung's privacy-relevant hardware decisions were ALREADY public
   - A privacy article published Aug 2 could have compared Samsung's
     identical LED + anti-tamper + wear detection against Meta's
   - Instead, Samsung's existence is treated as hypothetical/future

Distinct from existing mechanisms:
- #70 (Ashworth accessibility inversion): Different domain — #70 is about
  accessibility features receiving opposite framing by entity; #89 is
  about the headline-substance gap in a category-level privacy article
- #30 (Chokkattu temporal framing oscillation): Different journalist,
  different pattern — #30 is same-journalist genre-shift; #89 is about
  a single article's internal structure (headline vs substance)
- #45 (Ashworth WWDC PCC privacy framing): Different event — #45 is
  about Apple WWDC PCC architecture coverage; #89 is about a standalone
  smart glasses privacy industry piece
- #12 (Boone Ashworth cross-entity general): #89 adds a specific new
  sub-mechanism not previously documented

Confounding factors:
- STRONG: Meta has 69% market share (IDC Q1 2026) — legitimate to focus
  on the market leader in an industry privacy piece
- STRONG: Samsung glasses hadn't shipped yet — fewer real-world privacy
  incidents to report
- MODERATE: WIRED's own NameTag investigation gives them unique source
  material that naturally centers Meta
- MODERATE: Article is short (~450 words visible) — space constraints
  limit competitor coverage depth
- WEAK: Samsung privacy features (LED, anti-tamper, wear detection)
  were announced at Unpacked but detailed specs emerged gradually
- WEAK: Ashworth may genuinely believe the privacy question is about
  Meta's scale, not the hardware category

Testable predictions:
1. When Samsung glasses ship (Fall 2026), WIRED will NOT publish a
   "Samsung glasses privacy investigation" comparable to NameTag
2. If Samsung's Gemini data retention is exposed as problematic, WIRED
   will frame it as a "Google problem" not a "Samsung glasses problem"
3. WIRED will NOT self-reference this article when covering Samsung
   glasses privacy, the way they self-reference their NameTag investigation
4. Future WIRED "industry" privacy articles about smart glasses will
   continue to use Meta as primary/sole substantive example

Cross-references:
- Mechanism #70: Ashworth Accessibility Framing Inversion
- Mechanism #45: Ashworth WWDC PCC Privacy Framing Asymmetry
- Mechanism #30: Chokkattu Temporal Framing Oscillation
- Mechanism #84: WIRED OpenAI Hardware FR Investigation Gap
- Mechanism #80: Gizmodo 4-Entity Clean Control
- Mechanism #81: Multi-Journalist Samsung Unpacked Beat Assignment
"""

import unittest
import os
import yaml

PROFILES_DIR = os.path.join(os.path.dirname(__file__), '..', 'profiles')


def load_wired_profile():
    with open(os.path.join(PROFILES_DIR, 'wired.yaml')) as f:
        return yaml.safe_load(f)


def load_competitor_research():
    with open(os.path.join(PROFILES_DIR, 'competitor-coverage-research.yaml')) as f:
        return yaml.safe_load(f)


def load_entities():
    with open(os.path.join(PROFILES_DIR, 'competitor-entities.yaml')) as f:
        return yaml.safe_load(f)


class TestArticleExists(unittest.TestCase):
    """Verify the WIRED article data is in the profiles."""

    def test_mechanism_89_exists_in_competitor_research(self):
        data = load_competitor_research()
        mechanism_ids = []
        for key, val in data.get('cross_publication_findings', {}).items():
            mid = val.get('mechanism_id')
            if mid is not None:
                mechanism_ids.append(mid)
        self.assertIn(89, mechanism_ids,
                      "Mechanism #89 must exist in competitor-coverage-research.yaml")

    def test_mechanism_89_has_required_fields(self):
        data = load_competitor_research()
        mech = data['cross_publication_findings'].get('ashworth_category_headline_meta_substance')
        self.assertIsNotNone(mech, "Mechanism key must exist")
        self.assertEqual(mech['mechanism_id'], 89)
        self.assertIn('finding_summary', mech)
        self.assertGreaterEqual(len(mech['finding_summary']), 100,
                                "Finding summary must be substantive (≥100 chars)")
        self.assertIn('confounding_factors', mech)
        self.assertGreaterEqual(len(mech['confounding_factors']), 3)
        self.assertIn('testable_predictions', mech)
        self.assertGreaterEqual(len(mech['testable_predictions']), 2)

    def test_mechanism_89_has_date_added(self):
        data = load_competitor_research()
        mech = data['cross_publication_findings']['ashworth_category_headline_meta_substance']
        self.assertIn('date_added', mech)
        self.assertEqual(mech['date_added'], '2026-08-13')

    def test_mechanism_89_has_test_file(self):
        data = load_competitor_research()
        mech = data['cross_publication_findings']['ashworth_category_headline_meta_substance']
        self.assertIn('test_file', mech)
        # test_file value is relative to repo root (e.g., "tests/foo.py")
        repo_root = os.path.join(os.path.dirname(__file__), '..')
        test_path = os.path.join(repo_root, mech['test_file'])
        self.assertTrue(os.path.exists(test_path),
                        f"Test file {mech['test_file']} must exist on disk")


class TestHeadlineSubstanceGap(unittest.TestCase):
    """Verify the headline-substance asymmetry pattern is documented."""

    def test_headline_is_category_universal(self):
        """The headline asks about 'smart glasses' generically, not Meta specifically."""
        data = load_competitor_research()
        mech = data['cross_publication_findings']['ashworth_category_headline_meta_substance']
        headline = mech.get('article_headline', '')
        # Headline should NOT contain "Meta" — it's category-universal
        self.assertNotIn('Meta', headline,
                         "Category-universal headline should not mention Meta by name")
        # Headline SHOULD reference the category
        headline_lower = headline.lower()
        self.assertTrue(
            'smart glasses' in headline_lower or 'glasses' in headline_lower,
            "Headline should reference the smart glasses category")

    def test_meta_mention_count_dominates(self):
        """Meta receives overwhelmingly more substantive coverage than competitors."""
        data = load_competitor_research()
        mech = data['cross_publication_findings']['ashworth_category_headline_meta_substance']
        entity_mentions = mech.get('entity_mention_analysis', {})
        meta_mentions = entity_mentions.get('meta_substantive_paragraphs', 0)
        samsung_mentions = entity_mentions.get('samsung_substantive_paragraphs', 0)
        google_mentions = entity_mentions.get('google_substantive_paragraphs', 0)
        apple_mentions = entity_mentions.get('apple_substantive_paragraphs', 0)

        self.assertGreaterEqual(meta_mentions, 3,
                                "Meta should have ≥3 substantive paragraphs")
        self.assertLessEqual(samsung_mentions, 1,
                             "Samsung should have ≤1 substantive paragraph")
        self.assertLessEqual(google_mentions, 1,
                             "Google should have ≤1 substantive paragraph")

    def test_samsung_framed_as_future(self):
        """Samsung is treated as a future entrant despite being publicly announced."""
        data = load_competitor_research()
        mech = data['cross_publication_findings']['ashworth_category_headline_meta_substance']
        samsung_framing = mech.get('samsung_framing', '')
        self.assertIn('later this year', samsung_framing.lower(),
                      "Samsung framing should include 'later this year' temporal dismissal")

    def test_apple_framed_sympathetically(self):
        """Apple is framed positively for delaying glasses for privacy."""
        data = load_competitor_research()
        mech = data['cross_publication_findings']['ashworth_category_headline_meta_substance']
        apple_framing = mech.get('apple_framing', '')
        # Apple's delay is framed as addressing privacy — positive connotation
        self.assertIn('privacy', apple_framing.lower(),
                      "Apple framing should reference privacy positively")

    def test_self_citation_pattern(self):
        """WIRED cites its own investigation as evidence within the article."""
        data = load_competitor_research()
        mech = data['cross_publication_findings']['ashworth_category_headline_meta_substance']
        self.assertTrue(mech.get('self_citation_present', False),
                        "Article must document WIRED self-citing its NameTag investigation")


class TestTemporalContext(unittest.TestCase):
    """Verify the timing relationship between Samsung announcement and article."""

    def test_article_date_after_samsung_unpacked(self):
        """Article published after Samsung Galaxy Unpacked."""
        data = load_competitor_research()
        mech = data['cross_publication_findings']['ashworth_category_headline_meta_substance']
        article_date = mech.get('article_date', '')
        samsung_unpacked_date = mech.get('samsung_unpacked_date', '')
        self.assertEqual(article_date, '2026-08-02')
        self.assertEqual(samsung_unpacked_date, '2026-07-22')

    def test_days_between_unpacked_and_article(self):
        """Article published 11 days after Samsung's public announcement."""
        data = load_competitor_research()
        mech = data['cross_publication_findings']['ashworth_category_headline_meta_substance']
        days_gap = mech.get('days_after_samsung_unpacked', 0)
        self.assertEqual(days_gap, 11,
                         "Article should be 11 days after Galaxy Unpacked")

    def test_samsung_hardware_was_public(self):
        """Samsung's privacy-relevant hardware specs were public before the article."""
        data = load_competitor_research()
        mech = data['cross_publication_findings']['ashworth_category_headline_meta_substance']
        samsung_specs = mech.get('samsung_specs_public_before_article', {})
        self.assertTrue(samsung_specs.get('snapdragon_ar1_gen1', False))
        self.assertTrue(samsung_specs.get('12mp_camera', False))
        self.assertTrue(samsung_specs.get('led_indicator', False))
        self.assertTrue(samsung_specs.get('anti_tamper', False))
        self.assertTrue(samsung_specs.get('wear_detection', False))


class TestHardwareParity(unittest.TestCase):
    """Verify that Samsung and Meta glasses share identical privacy-relevant hardware."""

    def test_same_chip(self):
        """Both use Snapdragon AR1 Gen 1."""
        entities = load_entities()
        samsung = entities.get('entities', {}).get('samsung', {})
        # Check that Samsung glasses hardware is documented
        glasses = samsung.get('hardware_devices', {}).get('galaxy_glasses', {})
        if glasses:
            self.assertIn('AR1', str(glasses.get('processor', '')),
                          "Samsung Galaxy Glasses should use Snapdragon AR1")

    def test_identical_camera_resolution(self):
        """Both have 12MP cameras — identical privacy-relevant capability."""
        data = load_competitor_research()
        mech = data['cross_publication_findings']['ashworth_category_headline_meta_substance']
        hw = mech.get('hardware_parity', {})
        self.assertEqual(hw.get('meta_camera_mp'), hw.get('samsung_camera_mp'),
                         "Camera resolution must be identical between Meta and Samsung")

    def test_identical_led_indicator(self):
        """Both have LED recording indicators with anti-tamper detection."""
        data = load_competitor_research()
        mech = data['cross_publication_findings']['ashworth_category_headline_meta_substance']
        hw = mech.get('hardware_parity', {})
        self.assertTrue(hw.get('meta_led_indicator', False))
        self.assertTrue(hw.get('samsung_led_indicator', False))
        self.assertTrue(hw.get('meta_anti_tamper', False))
        self.assertTrue(hw.get('samsung_anti_tamper', False))


class TestSelfCitationChain(unittest.TestCase):
    """Verify the self-referential investigation chain."""

    def test_wired_cites_own_nametag_investigation(self):
        """Article references WIRED's June 4 NameTag exposé."""
        data = load_competitor_research()
        mech = data['cross_publication_findings']['ashworth_category_headline_meta_substance']
        self.assertTrue(mech.get('self_citation_present', False))
        self_cite = mech.get('self_citation_detail', '')
        self.assertIn('NameTag', self_cite,
                      "Self-citation should reference the NameTag investigation")

    def test_conde_nast_openai_deal_context(self):
        """Condé Nast (WIRED parent) has OpenAI content licensing deal."""
        wired = load_wired_profile()
        # OpenAI deal is documented in narrative text, not just financial_relationships
        import json
        full_text = json.dumps(wired).lower()
        self.assertIn('openai', full_text,
                      "WIRED profile should reference OpenAI deal")


class TestConfoundingFactors(unittest.TestCase):
    """Verify confounding factors are documented with scholarly rigor."""

    def test_at_least_three_confounding_factors(self):
        data = load_competitor_research()
        mech = data['cross_publication_findings']['ashworth_category_headline_meta_substance']
        factors = mech.get('confounding_factors', [])
        self.assertGreaterEqual(len(factors), 3)

    def test_at_least_one_strong_confound(self):
        data = load_competitor_research()
        mech = data['cross_publication_findings']['ashworth_category_headline_meta_substance']
        factors = mech.get('confounding_factors', [])
        strong_count = sum(1 for f in factors
                           if isinstance(f, dict) and f.get('strength') == 'STRONG')
        self.assertGreaterEqual(strong_count, 1,
                                "Must have ≥1 STRONG confounding factor")

    def test_multiple_strength_levels(self):
        data = load_competitor_research()
        mech = data['cross_publication_findings']['ashworth_category_headline_meta_substance']
        factors = mech.get('confounding_factors', [])
        strengths = set()
        for f in factors:
            if isinstance(f, dict):
                strengths.add(f.get('strength', ''))
        self.assertGreaterEqual(len(strengths), 2,
                                "Must have ≥2 distinct strength levels")


class TestTestablePredictions(unittest.TestCase):
    """Verify testable predictions are specific and falsifiable."""

    def test_at_least_two_predictions(self):
        data = load_competitor_research()
        mech = data['cross_publication_findings']['ashworth_category_headline_meta_substance']
        predictions = mech.get('testable_predictions', [])
        self.assertGreaterEqual(len(predictions), 2)

    def test_predictions_mention_specific_entities(self):
        data = load_competitor_research()
        mech = data['cross_publication_findings']['ashworth_category_headline_meta_substance']
        predictions = mech.get('testable_predictions', [])
        all_text = ' '.join(predictions).lower()
        self.assertTrue(
            'samsung' in all_text or 'google' in all_text or 'apple' in all_text,
            "Predictions should reference specific competitor entities")


class TestCrossReferences(unittest.TestCase):
    """Verify cross-references point to existing mechanisms."""

    def test_cross_references_exist(self):
        data = load_competitor_research()
        mech = data['cross_publication_findings']['ashworth_category_headline_meta_substance']
        cross_refs = mech.get('cross_references', [])
        self.assertGreaterEqual(len(cross_refs), 3,
                                "Should have ≥3 cross-references to related mechanisms")

    def test_cross_references_are_valid_ids(self):
        """All cross-referenced mechanism IDs should exist in the dataset."""
        data = load_competitor_research()
        mech = data['cross_publication_findings']['ashworth_category_headline_meta_substance']
        cross_refs = mech.get('cross_references', [])
        all_ids = set()
        for section in ['aggregate_findings', 'cross_publication_findings']:
            for key, val in data.get(section, {}).items():
                if isinstance(val, dict):
                    mid = val.get('mechanism_id')
                    if mid is not None:
                        all_ids.add(mid)
        for ref in cross_refs:
            ref_id = ref.get('mechanism_id')
            if ref_id and ref_id >= 17:  # Pre-17 refs predate YAML
                self.assertIn(ref_id, all_ids,
                              f"Cross-reference mechanism #{ref_id} must exist")

    def test_distinct_from_mechanism_70(self):
        """This mechanism is distinct from #70 (Ashworth accessibility inversion)."""
        data = load_competitor_research()
        mech_89 = data['cross_publication_findings']['ashworth_category_headline_meta_substance']
        # Find mechanism #70 in either section
        mech_70 = None
        for section in ['aggregate_findings', 'cross_publication_findings']:
            for key, val in data.get(section, {}).items():
                if isinstance(val, dict) and val.get('mechanism_id') == 70:
                    mech_70 = val
                    break
            if mech_70:
                break
        self.assertIsNotNone(mech_70, "Mechanism #70 must exist for comparison")
        # Different mechanism names
        self.assertNotEqual(
            mech_89.get('mechanism', ''), mech_70.get('mechanism', ''),
            "Mechanism #89 must have a different mechanism type than #70")
        # Different key findings
        from difflib import SequenceMatcher
        sim = SequenceMatcher(None,
                              mech_89.get('finding_summary', ''),
                              mech_70.get('finding_summary', '')).ratio()
        self.assertLess(sim, 0.7,
                        f"Finding summaries should be distinct (similarity={sim:.2f}")


class TestEntityMentionDistribution(unittest.TestCase):
    """Verify the entity mention distribution reflects the asymmetry."""

    def test_meta_dominates_word_count(self):
        data = load_competitor_research()
        mech = data['cross_publication_findings']['ashworth_category_headline_meta_substance']
        mentions = mech.get('entity_mention_analysis', {})
        meta_words = mentions.get('meta_approximate_word_count', 0)
        samsung_words = mentions.get('samsung_approximate_word_count', 0)
        self.assertGreater(meta_words, samsung_words * 5,
                           "Meta word count should be >5x Samsung's in a 'category' article")

    def test_meta_negative_tone(self):
        data = load_competitor_research()
        mech = data['cross_publication_findings']['ashworth_category_headline_meta_substance']
        tones = mech.get('tone_scores', {})
        meta_tone = tones.get('meta', 0)
        self.assertLess(meta_tone, 0,
                        "Meta tone should be negative in this article")

    def test_apple_neutral_or_positive_tone(self):
        data = load_competitor_research()
        mech = data['cross_publication_findings']['ashworth_category_headline_meta_substance']
        tones = mech.get('tone_scores', {})
        apple_tone = tones.get('apple', 0)
        self.assertGreaterEqual(apple_tone, 0,
                                "Apple tone should be neutral or positive")


class TestSourceURLs(unittest.TestCase):
    """Verify source URLs are documented."""

    def test_wired_source_url(self):
        data = load_competitor_research()
        mech = data['cross_publication_findings']['ashworth_category_headline_meta_substance']
        sources = mech.get('source_urls', [])
        wired_sources = [s for s in sources
                         if isinstance(s, dict) and 'wired.com' in s.get('url', '')]
        if not wired_sources:
            wired_sources = [s for s in sources
                             if isinstance(s, str) and 'wired.com' in s]
        self.assertGreater(len(wired_sources), 0,
                           "Must include the WIRED article URL as a source")

    def test_samsung_unpacked_source(self):
        data = load_competitor_research()
        mech = data['cross_publication_findings']['ashworth_category_headline_meta_substance']
        sources = mech.get('source_urls', [])
        samsung_sources = [s for s in sources
                           if isinstance(s, dict) and 'samsung' in s.get('url', '').lower()]
        if not samsung_sources:
            samsung_sources = [s for s in sources
                               if isinstance(s, str) and 'samsung' in s.lower()]
        self.assertGreater(len(samsung_sources), 0,
                           "Must include Samsung Unpacked source URL")


if __name__ == '__main__':
    unittest.main()
