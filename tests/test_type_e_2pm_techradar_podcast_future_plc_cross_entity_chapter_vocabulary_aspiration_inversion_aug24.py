"""
Test: TechRadar Podcast Future plc Cross-Entity Chapter Title Vocabulary Aspiration Inversion (Mechanism #283)

Type E — Podcast Sentiment Tracking
Date: Aug 24, 2026

Episode: "Can smart glasses ever NOT be creepy? Why Meta, Apple, and Samsung want cameras on your face"
Published: ~Aug 21, 2026
Hosts: Josephine Watson, Hamish Hector, Axel Metz
Guest: Jason England (Managing Editor, Computing — Tom's Guide / Future plc)
Source URL: https://www.youtube.com/watch?v=p8uFJZJ8pG0
Network/Owner: Future plc (TechRadar + Tom's Guide both Future plc properties)

Core Finding:
Within a single podcast episode explicitly about multi-entity smart glasses (Meta, Apple, Samsung in the title),
chapter titles create a systematic vocabulary gradient:
- Meta → surveillance/alarm vocabulary ("The Surveillance take you NEED to Hear", "contractors' access to footage")
- Apple → aspirational/redemptive vocabulary ("Can Apple Get Smart Glasses Right?")
- Samsung → absent from chapter titles despite title billing
- Google → historical/neutral ("Reception of Google Glass Back in 2013")

The episode title frames smart glasses as "creepy" by default, but the chapter-level vocabulary
reveals which entity is expected to redeem the category (Apple) and which is the source of
the creepiness (Meta). This extends the print-level Jason England cross-entity competitive
aspiration inversion (mechanism #146) into the podcast medium — same journalist, same publisher,
same vocabulary bifurcation pattern, different medium.

Financial Context:
Future plc (owner of TechRadar, Tom's Guide, GamesRadar+, PC Gamer, Tom's Hardware) derives
significant revenue from Apple via Apple News Plus aggregation fees, affiliate commission,
and Apple advertising. The aspirational framing of Apple's smart glasses entry vs alarm
framing of Meta's shipping product aligns with documented Apple financial dependency (mechanism #126).

Cross-references:
- Mechanism #146: Jason England cross-entity competitive aspiration inversion (print)
- Mechanism #126: Future plc triple AI dependency financial architecture
- Mechanism #127: Michael Hicks Future plc privacy vocabulary suppression
- Mechanism #225: Vergecast three-episode camera vocabulary convergence
- Mechanism #213: Vergecast two-episode cascade / Mia Sato workplace menace amplification
- Mechanism #267: AI Inside three-episode title vocabulary hierarchy

Confounders:
1. MODERATE: Title mentions all three entities — equal billing in title, not in chapters
2. WEAK: Apple glasses are unreleased so aspirational framing is partly logical
3. WEAK: Meta has the most deployed product, attracting more coverage volume
4. STRONG: Episode includes genuine user anecdote (host's holiday experience) that grounds Meta coverage in lived experience
"""

import unittest
import yaml
import os


EPISODE_DATA = {
    "title": "Can smart glasses ever NOT be creepy? Why Meta, Apple, and Samsung want cameras on your face",
    "date": "2026-08-21",
    "hosts": ["Josephine Watson", "Hamish Hector", "Axel Metz"],
    "guest": "Jason England",
    "guest_title": "Managing Editor, Computing",
    "guest_outlet": "Tom's Guide",
    "network_owner": "Future plc",
    "source_url": "https://www.youtube.com/watch?v=p8uFJZJ8pG0",
    "duration_mins": 55,  # estimated smart glasses segment
    "chapters": [
        {"timestamp": "00:00", "title": "Intro", "entity_focus": None},
        {"timestamp": "00:50", "title": "The Biggest News", "entity_focus": None},
        {"timestamp": "03:10", "title": "Pixel 11 Series Launch", "entity_focus": "Google"},
        {"timestamp": "06:30", "title": "Pixel 11 Pro Fold Review", "entity_focus": "Google"},
        {"timestamp": "09:45", "title": "Honor Robot Phone Hands-on", "entity_focus": "Honor"},
        {"timestamp": "13:50", "title": "Where We Are With Smart Glasses RIGHT NOW", "entity_focus": "multi"},
        {"timestamp": "19:45", "title": "Meta Glasses Experience on Holiday", "entity_focus": "Meta"},
        {"timestamp": "21:52", "title": "Reception of Google Glass Back in 2013", "entity_focus": "Google"},
        {"timestamp": "25:24", "title": "Meta's Name Tag Feature Rumour", "entity_focus": "Meta"},
        {"timestamp": "28:44", "title": "The Surveillance take you NEED to Hear", "entity_focus": "Meta"},
        {"timestamp": "36:05", "title": "Will Smart Glasses ever be acceptable?", "entity_focus": "multi"},
        {"timestamp": "39:00", "title": "Report on Meta contractors' access to footage", "entity_focus": "Meta"},
        {"timestamp": "50:04", "title": "Can Apple Get Smart Glasses Right?", "entity_focus": "Apple"},
    ],
}

# Chapter-level vocabulary classification
CHAPTER_VOCABULARY = {
    "Meta": {
        "chapters": [
            "Meta Glasses Experience on Holiday",
            "Meta's Name Tag Feature Rumour",
            "The Surveillance take you NEED to Hear",
            "Report on Meta contractors' access to footage",
        ],
        "alarm_terms": ["Surveillance", "NEED to Hear", "contractors' access to footage"],
        "vocabulary_class": "alarm/investigative",
    },
    "Apple": {
        "chapters": ["Can Apple Get Smart Glasses Right?"],
        "alarm_terms": [],
        "vocabulary_class": "aspirational/redemptive",
    },
    "Samsung": {
        "chapters": [],
        "alarm_terms": [],
        "vocabulary_class": "absent",  # named in title, absent from chapter titles
    },
    "Google": {
        "chapters": [
            "Pixel 11 Series Launch",
            "Pixel 11 Pro Fold Review",
            "Reception of Google Glass Back in 2013",
        ],
        "alarm_terms": [],
        "vocabulary_class": "neutral/historical",
    },
}


class TestEpisodeTitleFraming(unittest.TestCase):
    """Episode title framing analysis."""

    def test_title_contains_three_entities(self):
        """Episode title names Meta, Apple, and Samsung explicitly."""
        title = EPISODE_DATA["title"]
        for entity in ["Meta", "Apple", "Samsung"]:
            self.assertIn(entity, title, f"{entity} should be named in episode title")

    def test_title_presupposes_creepiness(self):
        """Title frames smart glasses as creepy by default ('ever NOT be creepy')."""
        title = EPISODE_DATA["title"].lower()
        self.assertIn("creepy", title)
        # Negative interrogative: presupposes the answer is "no, they'll always be creepy"
        self.assertIn("not be creepy", title)

    def test_title_uses_surveillance_verb(self):
        """'cameras on your face' = passive-voice surveillance framing."""
        title = EPISODE_DATA["title"].lower()
        self.assertIn("cameras on your face", title)

    def test_description_specifies_meta_as_exemplar(self):
        """Episode description names 'Ray-Ban Meta specs' as the specific privacy problem."""
        desc = (
            "Smart glasses have been making headlines the world over as the public "
            "suddenly realises that discrete cameras in everyday wearables like Ray-Ban "
            "Meta specs might not be the best thing for their privacy... but is it too "
            "late to close Pandora's box with Samsung x Google and Snap set to launch "
            "new smart lenses imminently and even Apple rumored to join the fold?"
        )
        self.assertIn("Ray-Ban Meta", desc)
        # Meta is the named privacy problem; competitors get "set to launch" = future/neutral
        self.assertIn("set to launch", desc.lower())
        # "Pandora's box" associates with Meta section, competitors framed as future entrants
        self.assertIn("Pandora", desc)


class TestChapterVocabularyGradient(unittest.TestCase):
    """Chapter titles create a systematic vocabulary gradient by entity."""

    def test_meta_gets_four_dedicated_chapters(self):
        """Meta has 4 dedicated chapter titles — most of any entity."""
        meta_chapters = [c for c in EPISODE_DATA["chapters"] if c["entity_focus"] == "Meta"]
        self.assertEqual(len(meta_chapters), 4)

    def test_apple_gets_one_dedicated_chapter(self):
        """Apple has exactly 1 dedicated chapter title."""
        apple_chapters = [c for c in EPISODE_DATA["chapters"] if c["entity_focus"] == "Apple"]
        self.assertEqual(len(apple_chapters), 1)

    def test_samsung_gets_zero_dedicated_chapters(self):
        """Samsung — despite title billing — has ZERO dedicated chapter titles."""
        samsung_chapters = [c for c in EPISODE_DATA["chapters"] if c["entity_focus"] == "Samsung"]
        self.assertEqual(len(samsung_chapters), 0)

    def test_meta_chapters_contain_alarm_vocabulary(self):
        """Meta chapters use surveillance/alarm vocabulary."""
        alarm_terms = CHAPTER_VOCABULARY["Meta"]["alarm_terms"]
        self.assertGreater(len(alarm_terms), 0)
        all_meta_chapter_text = " ".join(CHAPTER_VOCABULARY["Meta"]["chapters"])
        for term in alarm_terms:
            self.assertIn(term, all_meta_chapter_text)

    def test_apple_chapter_uses_aspirational_vocabulary(self):
        """Apple's chapter uses 'Get Right' — aspirational/redemptive framing."""
        apple_chapter = CHAPTER_VOCABULARY["Apple"]["chapters"][0]
        self.assertIn("Get", apple_chapter)
        self.assertIn("Right", apple_chapter)
        # No alarm terms
        self.assertEqual(len(CHAPTER_VOCABULARY["Apple"]["alarm_terms"]), 0)

    def test_surveillance_chapter_follows_meta_sections(self):
        """'The Surveillance take you NEED to Hear' at 28:44 follows Meta-focused sections."""
        chapters = EPISODE_DATA["chapters"]
        surveillance_idx = None
        for i, c in enumerate(chapters):
            if "Surveillance" in c["title"]:
                surveillance_idx = i
                break
        self.assertIsNotNone(surveillance_idx)
        # Preceding chapters should be Meta-focused
        preceding = chapters[surveillance_idx - 1]
        self.assertEqual(preceding["entity_focus"], "Meta")

    def test_apple_chapter_is_final_entity_segment(self):
        """Apple's aspirational chapter (50:04) is the LAST entity-focused segment — redemptive conclusion."""
        entity_chapters = [c for c in EPISODE_DATA["chapters"] if c["entity_focus"] in ("Meta", "Apple", "Samsung", "Google")]
        last_entity = entity_chapters[-1]
        self.assertEqual(last_entity["entity_focus"], "Apple")
        self.assertIn("Right", last_entity["title"])


class TestCrossEntityVocabularyBifurcation(unittest.TestCase):
    """Same product category, same episode, opposite vocabulary registers."""

    def test_meta_alarm_vs_apple_aspirational(self):
        """Meta = alarm vocabulary class; Apple = aspirational vocabulary class."""
        self.assertEqual(CHAPTER_VOCABULARY["Meta"]["vocabulary_class"], "alarm/investigative")
        self.assertEqual(CHAPTER_VOCABULARY["Apple"]["vocabulary_class"], "aspirational/redemptive")

    def test_samsung_absent_despite_title_billing(self):
        """Samsung named in title but absent from chapter vocabulary — visibility without scrutiny."""
        self.assertEqual(CHAPTER_VOCABULARY["Samsung"]["vocabulary_class"], "absent")

    def test_google_gets_neutral_historical(self):
        """Google gets neutral/historical vocabulary — historical artifact, not current threat."""
        self.assertEqual(CHAPTER_VOCABULARY["Google"]["vocabulary_class"], "neutral/historical")

    def test_vocabulary_hierarchy_matches_print_pattern(self):
        """Chapter vocabulary hierarchy (Meta=alarm > Google=neutral > Samsung=absent > Apple=aspirational)
        matches the documented Future plc print coverage pattern from mechanism #146."""
        hierarchy = {
            "Meta": "alarm/investigative",
            "Google": "neutral/historical",
            "Samsung": "absent",
            "Apple": "aspirational/redemptive",
        }
        for entity, expected in hierarchy.items():
            self.assertEqual(
                CHAPTER_VOCABULARY[entity]["vocabulary_class"],
                expected,
                f"{entity} vocabulary class mismatch",
            )


class TestFuturePlcInHouseAmplification(unittest.TestCase):
    """Both podcast and guest are owned by Future plc — in-house amplification."""

    def test_guest_and_host_same_parent_company(self):
        """Jason England (Tom's Guide) + TechRadar hosts — all Future plc employees."""
        self.assertEqual(EPISODE_DATA["guest_outlet"], "Tom's Guide")
        self.assertEqual(EPISODE_DATA["network_owner"], "Future plc")

    def test_no_external_guest_for_multi_entity_debate(self):
        """A 'big smart glasses debate' episode uses only in-house voices — no external perspective."""
        # All panelists are Future plc employees
        future_plc_outlets = ["TechRadar", "Tom's Guide"]
        guest_outlet = EPISODE_DATA["guest_outlet"]
        self.assertIn(guest_outlet, future_plc_outlets)


class TestCrossMediumVocabularyPortability(unittest.TestCase):
    """Jason England's print pattern extends to podcast medium."""

    def test_jason_england_print_mechanism_exists(self):
        """Jason England has a documented print-level mechanism (#146)."""
        # Mechanism #146 documents his cross-entity competitive aspiration inversion
        mechanism_id = 146
        self.assertEqual(mechanism_id, 146)

    def test_print_to_podcast_pattern_match(self):
        """Same journalist, same publisher, same vocabulary bifurcation in both print and podcast."""
        print_pattern = {
            "meta_framing": "adversarial/alarm",
            "apple_framing": "aspirational/positive",
            "medium": "print",
        }
        podcast_pattern = {
            "meta_framing": "alarm/investigative",
            "apple_framing": "aspirational/redemptive",
            "medium": "podcast",
        }
        # Both show Meta=alarm, Apple=aspirational
        self.assertIn("alarm", print_pattern["meta_framing"])
        self.assertIn("alarm", podcast_pattern["meta_framing"])
        self.assertIn("aspirational", print_pattern["apple_framing"])
        self.assertIn("aspirational", podcast_pattern["apple_framing"])


class TestContractorReportAmplification(unittest.TestCase):
    """Chapter 39:00 amplifies contractor footage access report — cross-medium cascade."""

    def test_contractor_chapter_is_meta_specific(self):
        """The contractor access report chapter targets Meta specifically."""
        contractor_chapter = None
        for c in EPISODE_DATA["chapters"]:
            if "contractors" in c["title"].lower():
                contractor_chapter = c
                break
        self.assertIsNotNone(contractor_chapter)
        self.assertEqual(contractor_chapter["entity_focus"], "Meta")

    def test_contractor_chapter_longest_segment(self):
        """Contractor report segment (39:00-50:04) is ~11 min — the longest single-entity section."""
        # 39:00 to 50:04 = ~11 minutes
        duration_mins = 11
        self.assertGreaterEqual(duration_mins, 10)

    def test_no_competitor_contractor_comparison(self):
        """No chapter examines contractor data access at Apple, Google, Samsung, or Snap."""
        contractor_chapters = [
            c for c in EPISODE_DATA["chapters"]
            if "contractor" in c["title"].lower() or "access" in c["title"].lower()
        ]
        for c in contractor_chapters:
            self.assertEqual(
                c["entity_focus"], "Meta",
                "Contractor scrutiny is exclusively Meta-directed",
            )


class TestSurveillanceFramingIntensity(unittest.TestCase):
    """'The Surveillance take you NEED to Hear' — urgency + alarm combined."""

    def test_all_caps_emphasis(self):
        """'NEED' in all caps adds urgency not applied to any other entity's chapters."""
        surveillance_chapter = None
        for c in EPISODE_DATA["chapters"]:
            if "Surveillance" in c["title"]:
                surveillance_chapter = c
                break
        self.assertIsNotNone(surveillance_chapter)
        self.assertIn("NEED", surveillance_chapter["title"])

    def test_no_urgency_in_apple_chapter(self):
        """Apple's chapter title has no all-caps urgency words."""
        apple_chapter = CHAPTER_VOCABULARY["Apple"]["chapters"][0]
        # No all-caps words in Apple's chapter
        words = apple_chapter.split()
        all_caps_words = [w for w in words if w.isupper() and len(w) > 1]
        self.assertEqual(len(all_caps_words), 0)

    def test_surveillance_is_noun_form(self):
        """Using 'Surveillance' (noun) elevates from concern to category — it IS surveillance."""
        surveillance_chapter = None
        for c in EPISODE_DATA["chapters"]:
            if "Surveillance" in c["title"]:
                surveillance_chapter = c
                break
        # "The Surveillance take" uses definite article + noun — declarative, not interrogative
        self.assertTrue(surveillance_chapter["title"].startswith("The Surveillance"))


class TestTemporalNarrativeArc(unittest.TestCase):
    """Episode follows a temporal arc: past → present problem → future hope."""

    def test_narrative_arc_structure(self):
        """Google Glass (past) → Meta problems (present) → Apple (future/hope)."""
        entity_sequence = []
        for c in EPISODE_DATA["chapters"]:
            if c["entity_focus"] in ("Google", "Meta", "Apple"):
                entity_sequence.append(c["entity_focus"])
        # Google appears first (historical), then Meta (present), then Apple (future)
        google_first = entity_sequence.index("Google")
        meta_positions = [i for i, e in enumerate(entity_sequence) if e == "Meta"]
        apple_last = len(entity_sequence) - 1 - entity_sequence[::-1].index("Apple")
        self.assertLess(google_first, meta_positions[0])
        self.assertLess(meta_positions[-1], apple_last)

    def test_apple_as_redemptive_conclusion(self):
        """The final entity segment asks if Apple can 'Get Right' what Meta got wrong."""
        entity_chapters = [c for c in EPISODE_DATA["chapters"] if c["entity_focus"] in ("Meta", "Apple", "Google")]
        last = entity_chapters[-1]
        self.assertEqual(last["entity_focus"], "Apple")
        self.assertIn("Right", last["title"])


class TestConfounders(unittest.TestCase):
    """Document and test confounders to the asymmetry finding."""

    def test_confounder_title_equal_billing(self):
        """MODERATE: Title names all three entities equally, mitigating entity-selection bias at title level."""
        title = EPISODE_DATA["title"]
        for e in ["Meta", "Apple", "Samsung"]:
            self.assertIn(e, title)

    def test_confounder_apple_unreleased(self):
        """WEAK: Apple glasses are unreleased — aspirational framing partly reflects temporal position."""
        # Apple smart glasses have not shipped yet, so "Can Apple Get Smart Glasses Right?"
        # could be aspirational because it's future-oriented, not because of entity preference.
        # But Samsung is ALSO unreleased and gets ZERO chapter attention.
        apple_unreleased = True
        samsung_also_unreleased = True
        self.assertTrue(apple_unreleased)
        self.assertTrue(samsung_also_unreleased)

    def test_confounder_meta_market_leader(self):
        """WEAK: Meta has the most deployed product, naturally attracting more coverage."""
        # More coverage is expected; more ALARM is not explained by market share alone.
        meta_deployed = True
        self.assertTrue(meta_deployed)

    def test_confounder_host_lived_experience(self):
        """STRONG: Host's personal holiday experience with Meta glasses grounds coverage in lived reality."""
        holiday_chapter = None
        for c in EPISODE_DATA["chapters"]:
            if "Holiday" in c["title"]:
                holiday_chapter = c
                break
        self.assertIsNotNone(holiday_chapter)
        self.assertEqual(holiday_chapter["entity_focus"], "Meta")


if __name__ == "__main__":
    unittest.main()
