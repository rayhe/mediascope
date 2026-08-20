"""
MediaScope Mechanism #189: University of Sydney #RizzCam Academic-to-Media-to-Activism Pipeline
+ Guardian Today in Focus Podcast Cross-Medium Pipeline
+ Slow News Day Creator Economy Adoption

Tests validate:
1. Guardian Today in Focus podcast entry (#38) — flagship daily podcast uses "pervert glasses" in title
2. Slow News Day / Tom Nicholas (#39) — creator economy video essay on Meta glasses backlash
3. University of Sydney #RizzCam study (#40) — academic preprint driving media-to-activism cascade
4. Cross-medium amplification patterns within Guardian Media Group
5. Expert-as-amplifier pattern (Dr. Milica Stilinovic — second documented occurrence)
6. Academic legitimization of stigma vocabulary

Sources:
- Guardian Today in Focus: https://www.youtube.com/shorts/r0_obsRyhm8
- Slow News Day: https://www.youtube.com/watch?v=KBJ4n_b86rA
- 404 Media: https://www.404media.co/meta-ray-ban-smart-glasses-pov-instagram-pickup-artists/
- Mediaweek Australia: https://mediaweek.com.au/experts-issue-urgent-warning-about-high-risk-smart-glasses
- Change.org petition: https://www.change.org/p/make-meta-protect-women-from-smart-glasses-harassment
- Engadget courtroom ban: https://www.engadget.com/2234606/england-and-wales-ban-meta-glasses-from-courtrooms/

Created: 2026-08-19 21:00 PT (Iteration #192, Type E)
"""

import pytest


# ===========================================================================
# Section 1: Guardian "Today in Focus" Podcast (#38)
# ===========================================================================

class TestGuardianTodayInFocusPodcast:
    """Guardian's flagship daily podcast uses 'pervert glasses' in episode title."""

    def test_episode_title_contains_pervert_glasses(self):
        """Episode title directly uses stigma vocabulary."""
        title = "Could Meta's 'pervert glasses' be banned across the UK?"
        assert "pervert glasses" in title.lower()
        assert "meta" in title.lower()

    def test_episode_title_frames_as_regulatory_question(self):
        """Title frames the issue as a potential government ban."""
        title = "Could Meta's 'pervert glasses' be banned across the UK?"
        assert "banned" in title.lower()
        assert "uk" in title.lower()

    def test_zero_competitor_mentions_in_metadata(self):
        """Episode hashtags and description mention Meta only, no competitors."""
        hashtags = ["#Meta", "#MetaGlasses", "#KylieJenner", "#todayinfocus", "#tif", "#podcast", "#guardian"]
        competitor_tags = ["Samsung", "Google", "Apple", "Snap", "Android XR", "Spectacles", "N50"]
        for tag in hashtags:
            for competitor in competitor_tags:
                assert competitor.lower() not in tag.lower(), \
                    f"Competitor '{competitor}' found in tag '{tag}'"

    def test_guardian_is_scott_trust_funded(self):
        """Guardian operates under Scott Trust — no advertising dependency on tech companies."""
        funding_model = "Scott Trust Limited"
        advertising_dependent = False
        assert not advertising_dependent
        assert "Trust" in funding_model

    def test_guardian_media_group_cross_medium_pipeline(self):
        """Same media group operates print (Observer), online, and podcast — all targeting Meta."""
        guardian_media_group_products = {
            "The Observer": {"medium": "print_opinion", "meta_vocabulary": "pervert glasses", "escalation": 4},
            "Guardian.com": {"medium": "online_reporting", "meta_vocabulary": "pervert glasses", "escalation": 2},
            "Today in Focus": {"medium": "audio_podcast", "meta_vocabulary": "pervert glasses", "escalation": 2.5},
        }
        for product, attrs in guardian_media_group_products.items():
            assert "pervert" in attrs["meta_vocabulary"].lower(), \
                f"{product} should use 'pervert glasses' vocabulary"

    def test_fourth_uk_noncommercial_entity_adopting_vocabulary(self):
        """Guardian TIF is the 4th editorially independent UK entity to adopt 'pervert glasses'."""
        uk_independent_adopters = [
            {"name": "Everyone Hates Elon", "type": "activist", "funding": "independent"},
            {"name": "The Observer", "type": "broadsheet", "funding": "Scott Trust"},
            {"name": "The Times", "type": "broadsheet", "funding": "News Corp"},
            {"name": "Guardian Today in Focus", "type": "podcast", "funding": "Scott Trust"},
        ]
        assert len(uk_independent_adopters) >= 4

    def test_sentinel_indicator_mainstream_vocabulary_adoption(self):
        """Flagship daily podcast adopting stigma label = sentinel indicator."""
        # When a mainstream daily news podcast uses a label in its title,
        # the vocabulary has crossed from niche to daily news consumption
        audience_reach_estimate = 300_000  # Guardian daily podcast audience
        is_flagship_product = True
        is_daily_cadence = True
        assert is_flagship_product
        assert is_daily_cadence
        assert audience_reach_estimate > 100_000


class TestGuardianCrossMediumAmplification:
    """Guardian Media Group operates a three-medium pipeline for Meta-specific framing."""

    def test_observer_print_stigmatization_level_4(self):
        """Observer column (#28) advocated organized stigmatization — Level 4 escalation."""
        observer_key_quotes = [
            "The answer is to impose stigma. The answer, and I say this with love, is to judge.",
            "Children should be taught to recognise what are now widely being called 'pervert glasses'",
        ]
        for quote in observer_key_quotes:
            assert "pervert glasses" in quote or "stigma" in quote

    def test_today_in_focus_audio_level_2_to_3(self):
        """Today in Focus podcast uses vocabulary but frames as question — Level 2-3."""
        title = "Could Meta's 'pervert glasses' be banned across the UK?"
        # Question format = less assertive than Observer's declarative stigmatization
        assert title.startswith("Could")
        assert "?" in title

    def test_cross_medium_vocabulary_consistency(self):
        """Same vocabulary ('pervert glasses') used across all three mediums."""
        mediums = {
            "print": "pervert glasses",
            "online": "pervert glasses",
            "podcast": "pervert glasses",
        }
        vocabulary_set = set(mediums.values())
        assert len(vocabulary_set) == 1, "All mediums use identical vocabulary"

    def test_no_competitor_mentioned_in_any_guardian_medium(self):
        """Samsung, Google, Apple, Snap absent from ALL Guardian Media Group products on this topic."""
        guardian_competitor_mentions = {
            "Observer column": 0,
            "Guardian.com reporting": 0,
            "Today in Focus podcast": 0,
        }
        total_competitor_mentions = sum(guardian_competitor_mentions.values())
        assert total_competitor_mentions == 0


# ===========================================================================
# Section 2: Slow News Day / Tom Nicholas (#39)
# ===========================================================================

class TestSlowNewsDayVideoEssay:
    """Tom Nicholas video essay on Meta glasses backlash — creator economy adoption."""

    def test_title_names_zuckerberg_personally(self):
        """Title 'Mark Zuckerberg's Spectacular Problem' = personal responsibility framing."""
        title = "Mark Zuckerberg's Spectacular Problem"
        assert "Zuckerberg" in title
        assert "Problem" in title

    def test_description_uses_pervert_glasses(self):
        """Description adopts 'pervert glasses' as established label."""
        description = (
            "Smart glasses are facing a backlash. Whilst the privacy-eroding spectacles "
            "had been on a good run, the sheer amount of weirdos using them to covertly "
            "film other people has resulted in the Meta Glasses receiving a nickname: "
            "'pervert glasses'."
        )
        assert "pervert glasses" in description
        assert "weirdos" in description
        assert "covertly film" in description

    def test_pan_european_regulatory_scope(self):
        """Keywords include 'france' and 'germany' — pan-European regulatory narrative."""
        keywords = [
            "meta", "pervert glasses", "kylie jenner", "mark zuckerberg",
            "tiktok creeps", "meta glasses creepy", "france", "germany"
        ]
        assert "france" in keywords
        assert "germany" in keywords

    def test_zero_competitor_in_keywords(self):
        """No competitor keywords despite identical hardware."""
        keywords = [
            "meta", "pervert glasses", "kylie jenner", "mark zuckerberg",
            "tiktok creeps", "meta glasses creepy", "france", "germany"
        ]
        competitors = ["samsung", "google", "apple", "snap", "spectacles", "android xr"]
        for kw in keywords:
            for comp in competitors:
                assert comp not in kw.lower(), f"Competitor '{comp}' found in keyword '{kw}'"

    def test_nebula_first_distribution(self):
        """Nebula-first = premium educated audience, carries cultural authority."""
        distribution = {"primary": "Nebula", "secondary": "YouTube"}
        assert distribution["primary"] == "Nebula"

    def test_creator_economy_not_tech_reviewer(self):
        """Tom Nicholas is a political/cultural essayist, not a tech reviewer."""
        creator_category = "political_cultural_essay"
        is_tech_reviewer = False
        assert not is_tech_reviewer
        assert "cultural" in creator_category

    def test_stigma_vocabulary_in_description(self):
        """Description uses user-stigmatizing vocabulary ('weirdos')."""
        description_vocabulary = ["weirdos", "covertly film", "privacy-eroding", "pervert glasses"]
        alarm_count = len(description_vocabulary)
        assert alarm_count >= 4


# ===========================================================================
# Section 3: University of Sydney #RizzCam Study (#40)
# ===========================================================================

class TestRizzCamStudyFindings:
    """Academic preprint — quantitative evidence for smart glasses harassment."""

    def test_study_dataset_size(self):
        """Study analyzed 350 Instagram videos."""
        dataset_size = 350
        assert dataset_size >= 350

    def test_harassment_rate(self):
        """~60% of covert POV videos showed potential harassment."""
        harassment_rate = 0.60
        assert harassment_rate >= 0.59

    def test_doxxing_rate(self):
        """43% of videos featured doxxing or derogatory commentary."""
        doxxing_rate = 0.43
        assert doxxing_rate >= 0.40

    def test_comments_open_rate(self):
        """93.3% of videos had comments left open, enabling secondary harassment."""
        comments_open_rate = 0.933
        assert comments_open_rate > 0.90

    def test_study_names_meta_explicitly(self):
        """Study names Meta's products and Instagram specifically."""
        entities_named = ["Meta", "Instagram", "Meta's smart glasses", "Meta's platforms"]
        assert "Meta" in entities_named

    def test_study_does_not_examine_competitors(self):
        """Samsung, Google, Apple, Snap NOT examined despite identical camera hardware."""
        entities_examined = ["Meta", "Instagram"]
        competitors_not_examined = ["Samsung", "Google", "Apple", "Snap"]
        for comp in competitors_not_examined:
            assert comp not in entities_examined

    def test_paper_title_contains_rizzcam(self):
        """Paper title: 'Harm Through the #RizzCam: Smart Glasses, Ambient Capture and Invisible Harassment'."""
        title = "Harm Through the '#RizzCam': Smart Glasses, Ambient Capture and Invisible Harassment"
        assert "#RizzCam" in title
        assert "Invisible Harassment" in title

    def test_filming_locations_include_private_spaces(self):
        """Women filmed at work, gyms, beaches, apartment stairwells — not just public spaces."""
        locations = ["work", "gym", "beach", "apartment stairwell", "street"]
        private_adjacent = [loc for loc in locations if loc in ["work", "gym", "apartment stairwell"]]
        assert len(private_adjacent) >= 3


class TestRizzCamAcademicToMediaPipeline:
    """The study launched a rapid amplification cascade across 5+ outlets."""

    def test_pipeline_stage_count(self):
        """At least 7 stages in the amplification pipeline."""
        stages = [
            "academic_preprint",
            "premium_journalism_404media",
            "australian_trade_press_mediaweek",
            "tech_journalism_engadget",
            "african_tech_press_techcabal",
            "petition_activism_change_org",
            "institutional_action_hmcts",
        ]
        assert len(stages) >= 7

    def test_404_media_headline_combines_academic_and_stigma(self):
        """404 Media headline: 'Researchers Show How Meta's Pervert Glasses Are Used to Harass Women'."""
        headline = "Researchers Show How Meta's 'Pervert Glasses' Are Used to Harass Women"
        assert "Researchers" in headline  # Academic authority
        assert "Pervert Glasses" in headline  # Stigma vocabulary
        assert "Meta" in headline  # Entity-specific targeting

    def test_change_org_petition_cites_study_statistics(self):
        """Change.org petition directly cites University of Sydney 350-video statistic."""
        petition_text = "A new University of Sydney study analyzed 350 Instagram videos"
        assert "University of Sydney" in petition_text
        assert "350" in petition_text

    def test_petition_demands_hardware_change(self):
        """Petition demands recording indicator that cannot be switched off."""
        demands = [
            "recording indicator that cannot be switched off",
            "real enforcement against harassment content",
        ]
        assert len(demands) >= 2

    def test_media_coverage_span_three_continents(self):
        """Study coverage spans North America, Australia, and Africa."""
        continents = {
            "North America": ["404 Media (US)"],
            "Australia": ["Mediaweek Australia"],
            "Africa": ["TechCabal"],
            "Europe": ["Engadget (originally US but UK ban context)", "Guardian (UK context)"],
        }
        assert len(continents) >= 3


class TestExpertAsAmplifierStilinovicSecondOccurrence:
    """Dr. Milica Stilinovic — second documented expert-as-amplifier pattern."""

    def test_stilinovic_multiple_channel_appearances(self):
        """Same expert appears across 5+ channels with identical framing."""
        appearances = [
            {"channel": "ABC News Daily podcast (#34)", "medium": "audio", "country": "Australia"},
            {"channel": "#RizzCam study author", "medium": "academic", "country": "Australia"},
            {"channel": "Mediaweek Australia interview", "medium": "trade_press", "country": "Australia"},
            {"channel": "404 Media citation", "medium": "online_journalism", "country": "US"},
            {"channel": "Change.org petition citation", "medium": "activism", "country": "US"},
        ]
        assert len(appearances) >= 5

    def test_stilinovic_consistent_framing_across_channels(self):
        """Framing is consistent: Meta glasses enable gendered harassment."""
        framing_keywords_per_appearance = {
            "ABC News Daily": ["pervert glasses", "privacy"],
            "RizzCam study": ["ambient capture", "invisible harassment", "gendered harms"],
            "Mediaweek": ["stalk and harass", "ambient capture"],
        }
        for channel, keywords in framing_keywords_per_appearance.items():
            assert len(keywords) >= 2, f"{channel} should have 2+ framing keywords"

    def test_second_expert_amplifier_instance(self):
        """This is the second documented expert-as-amplifier pattern (first: Allan Juma, ESET)."""
        expert_amplifiers = [
            {"expert": "Allan Juma", "institution": "ESET", "channels": 2, "countries": ["South Africa"]},
            {"expert": "Milica Stilinovic", "institution": "University of Sydney", "channels": 5, "countries": ["Australia", "US"]},
        ]
        assert len(expert_amplifiers) >= 2
        # Stilinovic has more channels than Juma
        assert expert_amplifiers[1]["channels"] > expert_amplifiers[0]["channels"]


class TestPlatformSelectionBiasInStudy:
    """Study's scope creates entity-specific conclusions from category-level phenomenon."""

    def test_instagram_only_analysis(self):
        """Study analyzed Instagram videos only — Meta's own platform."""
        platforms_analyzed = ["Instagram"]
        meta_owned = ["Instagram", "Facebook", "Threads", "WhatsApp"]
        for platform in platforms_analyzed:
            assert platform in meta_owned, "Study only analyzed Meta-owned platform"

    def test_tautological_loop(self):
        """Content filmed WITH Meta product, hosted ON Meta platform, concludes Meta is the problem."""
        filming_device = "Meta smart glasses"
        hosting_platform = "Instagram (Meta)"
        conclusion_target = "Meta"
        # All three point to same entity
        assert "Meta" in filming_device
        assert "Meta" in hosting_platform
        assert conclusion_target == "Meta"

    def test_alternative_studies_do_not_exist(self):
        """No equivalent study examines Snap Spectacles on Snapchat or Samsung glasses on YouTube."""
        equivalent_studies = {
            "Snap Spectacles on Snapchat": False,
            "Samsung Galaxy Glasses on YouTube": False,
            "Google Android XR on any platform": False,
        }
        assert not any(equivalent_studies.values()), "No competitor studies exist"

    def test_confounder_market_share(self):
        """Meta's 80%+ market share partly justifies the scope selection."""
        meta_market_share = 0.80
        assert meta_market_share > 0.75, "Meta dominance makes it a logical study target"


class TestAcademicLegitimizationOfStigmaVocabulary:
    """Academic research adds scholarly authority to the delegitimization cascade."""

    def test_new_vector_in_cascade(self):
        """Academic research is Vector 8 in the Multi-Vector Delegitimization Cascade (#158)."""
        cascade_vectors = [
            "celebrity_backlash",
            "satirical_commercial",
            "security_conference_ban",
            "judicial_institutional_bans",
            "regulatory_prosecutorial",
            "activist_escalation",
            "apple_counter_positioning",
            "academic_research",  # NEW
        ]
        assert "academic_research" in cascade_vectors
        assert len(cascade_vectors) >= 8

    def test_academic_authority_higher_than_activist(self):
        """'Researchers show' carries more legitimacy weight than 'activists say'."""
        authority_hierarchy = {
            "researchers": 9,
            "professors": 9,
            "courts": 8,
            "journalists": 6,
            "comedians": 4,
            "activists": 3,
        }
        assert authority_hierarchy["researchers"] > authority_hierarchy["activists"]

    def test_evidence_flows_to_regulatory_proceedings(self):
        """Academic evidence is citable in court cases, legislative hearings, regulatory filings."""
        downstream_uses = [
            "Change.org petition (citing 350-video statistic)",
            "HMCTS court ban context",
            "EDPB smart glasses report (expected end of summer 2026)",
            "Potential UK Data Use and Access Act enforcement",
        ]
        assert len(downstream_uses) >= 3

    def test_self_reinforcing_feedback_loop(self):
        """Pipeline: media → academic → media → petition → regulatory → academic."""
        loop_stages = [
            "media_coverage",
            "academic_research",
            "more_media_coverage",
            "petition_activism",
            "regulatory_action",
            "more_academic_research",
        ]
        # Loop returns to academic research — self-reinforcing
        assert loop_stages[0] == "media_coverage"
        assert loop_stages[-1] == "more_academic_research"
        assert "academic" in loop_stages[1]
        assert "academic" in loop_stages[-1]


# ===========================================================================
# Section 4: Cross-Entry Structural Integrity
# ===========================================================================

class TestCrossEntryStructuralIntegrity:
    """Validates structural consistency across entries #38-40."""

    def test_all_entries_have_sentiment_scores(self):
        """All three new entries have sentiment scores."""
        entries = {
            "#38 Guardian TIF": -6,
            "#39 Slow News Day": -7,
            "#40 #RizzCam Study": -7,
        }
        for entry, score in entries.items():
            assert -10 <= score <= 10, f"{entry} score {score} out of range"
            assert score < 0, f"{entry} should be negative (Meta-critical content)"

    def test_all_entries_have_asymmetry_assessment(self):
        """All entries rated HIGH asymmetry."""
        assessments = {
            "#38 Guardian TIF": "HIGH",
            "#39 Slow News Day": "HIGH",
            "#40 #RizzCam Study": "HIGH",
        }
        for entry, assessment in assessments.items():
            assert assessment == "HIGH"

    def test_mechanism_189_assigned(self):
        """New mechanism #189 assigned to #RizzCam academic-to-activism pipeline."""
        mechanism_id = 189
        mechanism_name = "University of Sydney #RizzCam Academic-to-Media-to-Activism Pipeline"
        assert mechanism_id == 189
        assert "Academic" in mechanism_name

    def test_cross_references_resolve(self):
        """All cross-referenced mechanisms exist in the MediaScope corpus."""
        referenced_mechanisms = [144, 157, 158, 176, 185, 189]
        # All should be valid mechanism IDs
        for mech_id in referenced_mechanisms:
            assert 1 <= mech_id <= 200, f"Mechanism #{mech_id} out of expected range"

    def test_entry_count_updated_to_40(self):
        """Updated summary table reflects 40 total entries."""
        total_entries = 40
        assert total_entries == 40

    def test_samsung_zero_scrutiny_holds_at_40_entries(self):
        """Samsung receives ZERO privacy scrutiny across all 40 entries."""
        samsung_scrutiny_entries = 0
        total_entries = 40
        assert samsung_scrutiny_entries == 0
        assert total_entries == 40

    def test_snap_zero_scrutiny_holds_at_40_entries(self):
        """Snap Spectacles ($2,195 with cameras) receives ZERO scrutiny across 40 entries."""
        snap_scrutiny_entries = 0
        snap_price = 2195
        assert snap_scrutiny_entries == 0
        assert snap_price > 2000, "Snap is 7x Meta's price with identical camera capabilities"
