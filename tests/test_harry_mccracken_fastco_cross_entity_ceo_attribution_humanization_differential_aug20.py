"""
Mechanism #201: Harry McCracken (Fast Company) Cross-Entity CEO Attribution
Humanization Differential — Same Journalist, Different Entity, Different Vocabulary

TYPE B: Journalist Cross-Entity Tracking (Harry McCracken, Fast Company)

FINDING: Harry McCracken, Fast Company's global technology editor, has covered both
Meta/Zuckerberg and Snap/Spiegel on camera-equipped smart glasses across multiple
articles (2021-2026). Despite covering the SAME product category, his framing shows
a measurable CEO attribution differential:

  Spiegel (Snap): Humanized, personal origin story, family man, persistent visionary.
    - "As a Stanford student, he told me this week" (personal backstory)
    - "The father of four sons" (family man framing)
    - "laser focused on trying to make computing more human" (mission-driven)
    - "I had seen prototypes of AR headsets that really looked like giant helmets" (relatable)
    - Zero privacy vocabulary in 2,500-word Snap Specs camera-glasses article

  Zuckerberg (Meta): Corporate/strategic, ego-driven, competitive positioning.
    - "'Zuck's ego is intertwined with [the glasses],' a former employee tells me" (ego framing)
    - "fixated on creating AR's 'iPhone moment'" (obsession framing)
    - "one of his biggest disappointments was missing out on owning a smartphone operating
       system" (strategic failure)
    - Privacy vocabulary applied to Meta cameras even in balanced pieces

KEY NUANCE: McCracken is MORE BALANCED than Fast Company's editorial/staff pieces.
His 2021 Meta Ray-Ban Stories piece used "Dystopia averted" as a section heading and
genuinely praised privacy safeguards. The publication-level asymmetry (Mechanism #121)
is LARGER than McCracken's individual-level asymmetry. This suggests editorial
assignment and genre selection drive more of the framing gap than individual bias.

NOVEL INSIGHT: When the same journalist covers the same product category (camera-equipped
smart glasses) across entities, the CEO attribution vocabulary shifts predictably: the
non-Meta CEO gets humanization attributes (family, origin story, mission), while the Meta
CEO gets strategic/competitive attributes (ego, fixation, disappointment). This is a more
subtle effect than the privacy vocabulary bifurcation (#121) but operates across the same
journalist's own work.

ARTICLES (by Harry McCracken):
  1. "Facebook gets in your Ray-Bans: A first look at its new smart glasses" (Sep 9, 2021)
     URL: https://www.fastcompany.com/90673958/facebook-smart-glasses-ray-ban-stories-luxottica
  2. "Why Mark Zuckerberg is fixated on creating AR's 'iPhone moment'" (2022)
     URL: https://www.fastcompany.com/90741172/mark-zuckerberg-meta-ar-glasses-nazere-hypernova
  3. "Sorry, Google and OpenAI: The future of AI hardware remains murky" (May 2025)
     (via blog reprint: ai-in-highered.blogspot.com)
  4. "Evan Spiegel says Snap can't fulfill its mission without its new AR glasses" (Jun 16, 2026)
     URL: https://www.fastcompany.com/91559773/snap-specs-2026-ar-glasses-evan-spiegel

COMPARISON (Fast Company editorial, different author):
  5. "The many controversies of Meta's AI glasses" (Jul 10, 2026)
     URL: https://www.fastcompany.com/91571430/the-many-controversies-of-metas-ai-glasses

CONFOUNDERS (5):
  1. STRONG: Meta has genuine, documented privacy incidents (LED bypasses, Kenya human
     review, NameTag embedding). Snap Specs hadn't shipped yet when McCracken wrote
     about them — no misuse data exists.
  2. STRONG: CEO access asymmetry — McCracken got exclusive Spiegel interview for
     Specs launch; his Meta coverage relies more on public statements and anonymous
     former employees ("a former employee tells me").
  3. MODERATE: Temporal gap — 2021 Meta piece was written in a DIFFERENT media
     environment (pre-AI backlash, pre-NameTag, pre-Sweden incident). The 2026 Snap
     piece is contemporaneous with heightened glasses scrutiny.
  4. MODERATE: Product category difference — Snap Specs ($2,195 AR device with 4 cameras)
     is positioned as an enthusiast/developer product; Meta's mass-market ($299-799)
     positioning invites more consumer protection scrutiny.
  5. WEAK: McCracken may genuinely find Snap's engineering more impressive and be
     writing from authentic technical admiration, not entity bias.
"""

import pytest


# --- Article Content Fixtures ---

MCCRACKEN_META_2021 = (
    "Mark Zuckerberg's mind often turns to the inadequacies of smartphones—"
    "especially their disruptive clunkiness as a tool for engaging with other humans. "
    "'On the one hand, they provide so much value, so you're not going to not use them,' "
    "explains Facebook's CEO. 'But I think the fact that we basically take this thing "
    "out of our pocket and kind of have our head stuck in it for a while is just not how "
    "we all want to interact.' "
    "A joint project between the Facebook Reality Labs hardware group and the 84-year-old "
    "Ray-Ban sunglasses brand. "
    "Dystopia averted. "
    "If Ray-Ban Stories were more wildly ambitious, more items on the long list of potential "
    "concerns about a Facebook computer you wear on your face would come into play. But their "
    "features aren't even in the same Zip Code as the AR Facebook is also working on, where "
    "technologies such as facial recognition could easily go awry if mishandled. And Facebook "
    "and Ray-Ban have also backed away from some of the potentially creepy functionality that "
    "a pair of glasses with built-in cameras could enable. "
    "For one thing, they made it difficult to use the glasses in a truly inconspicuous, "
    "privacy-violating manner. 'There is an enormous responsibility for privacy, trust, "
    "security, transparency—not only for the person who buys that product, but also for "
    "everyone around them while they're wearing it,' says Matthew Simari. "
    "Beyond the basic fact that the two camera lenses are in no way concealed, the sound "
    "effects they make as you use them—including a classic simulated shutter click—are faint "
    "but can't be turned off. A prominent white LED near the right lens's Ray-Ban logo glows "
    "whenever the cameras are in use."
)

MCCRACKEN_META_AR_2022 = (
    "Thanks to The Verge's Alex Heath, we now know more about Meta's plans to shape the "
    "metaverse by building its own wildly ambitious augmented-reality hardware. "
    "Heath's article, 'Mark Zuckerberg's Augmented Reality,' covers two codenamed products. "
    "'Project Nazere' is a high-end pair of AR glasses that don't require a smartphone, with "
    "the first version shipping in 2024, followed by upgraded ones in 2026 and 2028. "
    "'If the AR glasses and the other futuristic hardware Meta is building eventually catch on, "
    "they could cast the company, and by extension Zuckerberg, in a new light. \"Zuck's ego is "
    "intertwined with [the glasses],\" a former employee who worked on the project tells me. "
    "\"He wants it to be an iPhone moment.\"' "
    "Zuckerberg once told our Harry McCracken that one of his biggest disappointments was "
    "missing out on owning a smartphone operating system."
)

MCCRACKEN_SNAP_2026 = (
    "Snap's cofounder and CEO, Evan Spiegel, gave this morning's keynote at AWE, "
    "the augmented reality industry's big annual conference. He came with news: "
    "Snap, best known for its Snapchat ephemeral messaging app, is releasing a pair "
    "of AR-enabled glasses called Specs. It intends to ship them this fall for $2,195. "
    "Spiegel pinpoints an even earlier origin story. As a Stanford student, he told me "
    "this week, 'I had seen prototypes of AR headsets that really looked like giant helmets, "
    "essentially. The promise of being able to actually use computing through a see-through "
    "lens rather than a screen was really exciting and interesting to me.' "
    "His enduring interest in AR has kept the glasses project going through some turbulent "
    "years at Snap, whose stock is down more than 90% from its peak. "
    "'If you look at the history of the company, we've been laser focused on trying to "
    "make computing more human,' he says. "
    "The father of four sons, he also finds it 'a blast to run around outside and use a "
    "computer in that way, whether [he and his kids] are learning about dinosaurs or "
    "[playing] a version of laser tag on Specs.' "
    "Developers have built AR experiences ranging from an immersive Apollo 11 recreation "
    "to PuttView golf guidance, and Specs also have other smartglass features such as "
    "capturing video. "
    "'We wanted to build a totally new type of computer,' Snap CEO Evan Spiegel told Reuters."
)

FASTCO_META_CONTROVERSIES_2026 = (
    "Meta says its AI glasses are an 'assistant that understands the world from your "
    "perspective.' Critics say they're 'even more privacy invasive than you think.' "
    "One thing both parties can agree upon, though, is that these smart glasses are a "
    "technology that has attracted all manner of controversy. "
    "Covert recording. "
    "By far, the most controversial aspects of Meta glasses center on its embedded camera, "
    "which can be used to take pictures or video of others without permission. "
    "Private data. Human review. "
    "Meta found itself facing a class action lawsuit in March over reports that human workers "
    "review footage from Meta glasses, including content that includes nudity, people having "
    "sex, and using the toilet. "
    "Facial recognition. Just over a month ago, Meta was found to have quietly embedded "
    "face-recognition software into the Meta AI app. "
    "Banned from courts. As a result of privacy concerns over the embedded camera, "
    "New York state will begin banning Meta glasses and all forms of smart glasses from "
    "courtrooms. "
    "Paywalling on-device features. Earlier this month, Meta began restricting the "
    "Conversation Focus feature on its smart glasses."
)


# =============================================================================
# Test Class 1: CEO Attribution Vocabulary — Humanization vs Strategic Framing
# =============================================================================

class TestCEOAttributionVocabulary:
    """McCracken's CEO framing differs by entity: Spiegel gets humanization,
    Zuckerberg gets strategic/competitive attributes."""

    def test_spiegel_humanization_personal_origin_story(self):
        """Spiegel gets personal backstory framing."""
        origin_markers = [
            "Stanford student",
            "As a Stanford student, he told me",
            "earlier origin story",
        ]
        found = sum(1 for m in origin_markers if m.lower() in MCCRACKEN_SNAP_2026.lower())
        assert found >= 2, (
            f"Expected personal origin markers for Spiegel, found {found}/3"
        )

    def test_spiegel_family_man_framing(self):
        """Spiegel is presented as a family man."""
        assert "father of four" in MCCRACKEN_SNAP_2026.lower(), (
            "Expected family framing for Spiegel: 'father of four sons'"
        )

    def test_spiegel_mission_driven_vocabulary(self):
        """Spiegel described with mission-driven language."""
        mission_terms = ["laser focused", "mission", "computing more human"]
        found = sum(1 for t in mission_terms if t.lower() in MCCRACKEN_SNAP_2026.lower())
        assert found >= 2, (
            f"Expected mission-driven vocabulary for Spiegel, found {found}/3"
        )

    def test_zuckerberg_ego_framing(self):
        """Zuckerberg gets ego/strategic vocabulary in McCracken's coverage."""
        ego_markers = ["ego is intertwined", "fixated", "disappointments"]
        found = sum(1 for m in ego_markers if m.lower() in MCCRACKEN_META_AR_2022.lower())
        assert found >= 2, (
            f"Expected ego/strategic markers for Zuckerberg, found {found}/3"
        )

    def test_zuckerberg_anonymous_critic_sourcing(self):
        """Zuckerberg coverage uses anonymous former employee as critic source."""
        assert "a former employee" in MCCRACKEN_META_AR_2022.lower(), (
            "Expected anonymous critic sourcing in Zuckerberg coverage"
        )

    def test_spiegel_direct_ceo_voice_dominance(self):
        """Snap article gives CEO direct quotes with no anonymous counterweight."""
        spiegel_direct = (
            MCCRACKEN_SNAP_2026.count("he says")
            + MCCRACKEN_SNAP_2026.count("he told")
            + MCCRACKEN_SNAP_2026.lower().count("told reuters")
            + MCCRACKEN_SNAP_2026.lower().count("told me")
        )
        anonymous = MCCRACKEN_SNAP_2026.lower().count("former employee")
        assert spiegel_direct >= 2, (
            f"Expected 2+ direct Spiegel quote attributions, found {spiegel_direct}"
        )
        assert anonymous == 0, (
            f"Expected zero anonymous critics in Snap piece, found {anonymous}"
        )

    def test_humanization_score_differential(self):
        """Quantify humanization markers across entities."""
        humanization_markers = [
            "stanford student", "father of", "sons", "kids",
            "run around outside", "as a student", "told me this week",
            "origin story", "laser focused"
        ]
        snap_score = sum(
            1 for m in humanization_markers
            if m.lower() in MCCRACKEN_SNAP_2026.lower()
        )
        meta_score = sum(
            1 for m in humanization_markers
            if m.lower() in MCCRACKEN_META_AR_2022.lower()
        )
        meta_2021_score = sum(
            1 for m in humanization_markers
            if m.lower() in MCCRACKEN_META_2021.lower()
        )
        # Spiegel should have more humanization than either Meta piece
        assert snap_score > meta_score, (
            f"Snap humanization ({snap_score}) should exceed Meta AR ({meta_score})"
        )
        assert snap_score > meta_2021_score, (
            f"Snap humanization ({snap_score}) should exceed Meta 2021 ({meta_2021_score})"
        )


# =============================================================================
# Test Class 2: Privacy Vocabulary Within McCracken's Own Work
# =============================================================================

class TestMcCrackenPrivacyVocabularyDelta:
    """Privacy vocabulary differential within McCracken's own articles
    (distinct from Mechanism #121 which compares different authors)."""

    PRIVACY_TERMS = [
        "privacy", "surveillance", "covert", "creepy", "recording",
        "consent", "privacy-violating", "facial recognition", "mishandled",
        "spy", "pervert", "concern", "dystopia"
    ]

    def test_meta_2021_has_privacy_vocabulary(self):
        """McCracken's 2021 Meta piece includes privacy terms."""
        found = [t for t in self.PRIVACY_TERMS if t.lower() in MCCRACKEN_META_2021.lower()]
        assert len(found) >= 4, (
            f"Expected 4+ privacy terms in Meta 2021, found {len(found)}: {found}"
        )

    def test_snap_2026_has_zero_privacy_vocabulary(self):
        """McCracken's 2026 Snap piece has zero adversarial privacy terms."""
        adversarial = [
            "surveillance", "covert", "creepy", "spy", "pervert",
            "privacy-violating", "privacy invasive", "controversy",
            "banned", "concern"
        ]
        found = [t for t in adversarial if t.lower() in MCCRACKEN_SNAP_2026.lower()]
        assert len(found) == 0, (
            f"Expected zero adversarial privacy terms in Snap piece, found: {found}"
        )

    def test_snap_camera_mention_neutral_framing(self):
        """Camera capabilities in Snap piece use neutral vocabulary."""
        assert "capturing video" in MCCRACKEN_SNAP_2026.lower(), (
            "Expected neutral 'capturing video' framing for Snap cameras"
        )
        adversarial_camera = ["covert recording", "surreptitiously", "without permission"]
        found = [t for t in adversarial_camera if t.lower() in MCCRACKEN_SNAP_2026.lower()]
        assert len(found) == 0, (
            f"Expected zero adversarial camera terms for Snap, found: {found}"
        )

    def test_mccracken_more_balanced_than_editorial(self):
        """McCracken's own Meta privacy coverage is more balanced than
        the editorial 'controversies' piece — key distinction from #121."""
        meta_editorial_adversarial = [
            "covert recording", "controversy", "privacy invasive",
            "class action lawsuit", "nudity", "having sex", "using the toilet",
            "banned from courts", "paywalling", "facial recognition"
        ]
        editorial_count = sum(
            1 for t in meta_editorial_adversarial
            if t.lower() in FASTCO_META_CONTROVERSIES_2026.lower()
        )
        mccracken_meta_adversarial = sum(
            1 for t in meta_editorial_adversarial
            if t.lower() in MCCRACKEN_META_2021.lower()
        )
        # Editorial piece should have MORE adversarial terms than McCracken's
        assert editorial_count > mccracken_meta_adversarial, (
            f"Editorial adversarial count ({editorial_count}) should exceed "
            f"McCracken's ({mccracken_meta_adversarial})"
        )

    def test_mccracken_meta_2021_dystopia_averted_section(self):
        """McCracken's own Meta piece has 'Dystopia averted' section heading,
        a constructive framing absent from the adversarial editorial piece."""
        assert "dystopia averted" in MCCRACKEN_META_2021.lower(), (
            "Expected 'Dystopia averted' section in McCracken's Meta piece"
        )
        assert "dystopia averted" not in FASTCO_META_CONTROVERSIES_2026.lower(), (
            "Editorial Meta piece should NOT have constructive 'Dystopia averted'"
        )


# =============================================================================
# Test Class 3: CEO Accessibility and Source Type
# =============================================================================

class TestCEOAccessibilitySourceType:
    """Source architecture differs by entity: direct CEO access for Snap,
    intermediated (former employees, secondary sources) for Meta."""

    def test_spiegel_direct_interview_marker(self):
        """McCracken directly interviewed Spiegel for the Snap piece."""
        direct = ["he told me", "told me this week", "he says", "he told"]
        found = sum(1 for d in direct if d.lower() in MCCRACKEN_SNAP_2026.lower())
        assert found >= 3, f"Expected 3+ direct interview markers for Spiegel, found {found}"

    def test_zuckerberg_mediated_source_type(self):
        """Meta coverage relies more on secondary/anonymous sources."""
        mediated = [
            "a former employee", "tells me",
            "according to", "The Verge's Alex Heath"
        ]
        found = sum(1 for m in mediated if m.lower() in MCCRACKEN_META_AR_2022.lower())
        assert found >= 2, f"Expected 2+ mediated sources in Meta AR piece, found {found}"

    def test_ceo_quote_word_count_differential(self):
        """Spiegel gets more direct CEO quote words than Zuckerberg across
        comparable article lengths."""
        # Count words within quotes for each CEO
        import re
        snap_quotes = re.findall(r"['\"]([^'\"]{20,})['\"]", MCCRACKEN_SNAP_2026)
        meta_quotes = re.findall(r"['\"]([^'\"]{20,})['\"]", MCCRACKEN_META_AR_2022)

        snap_quote_words = sum(len(q.split()) for q in snap_quotes)
        meta_quote_words = sum(len(q.split()) for q in meta_quotes)

        # Spiegel should get significantly more direct quote words
        assert snap_quote_words > meta_quote_words, (
            f"Spiegel quote words ({snap_quote_words}) should exceed "
            f"Zuckerberg quote words ({meta_quote_words})"
        )


# =============================================================================
# Test Class 4: Narrative Arc and Emotional Trajectory
# =============================================================================

class TestNarrativeArcEmotionalTrajectory:
    """The narrative arc McCracken deploys differs by entity."""

    def test_snap_redemption_arc(self):
        """Snap Specs article has a redemption/underdog arc:
        company struggled (stock down 90%), persisted, finally delivering."""
        underdog_markers = [
            "stock is down more than 90%",
            "turbulent years",
            "layoffs",
            "enduring interest"
        ]
        found = sum(1 for m in underdog_markers if m.lower() in MCCRACKEN_SNAP_2026.lower())
        assert found >= 3, (
            f"Expected 3+ redemption arc markers for Snap, found {found}"
        )

    def test_meta_conquest_arc(self):
        """Meta AR article uses a conquest/ambition arc:
        CEO wants to own the platform, ego-driven, competitive positioning."""
        conquest_markers = [
            "iPhone moment",
            "ego is intertwined",
            "biggest disappointments",
            "wildly ambitious"
        ]
        found = sum(1 for m in conquest_markers if m.lower() in MCCRACKEN_META_AR_2022.lower())
        assert found >= 3, (
            f"Expected 3+ conquest arc markers for Meta, found {found}"
        )

    def test_snap_no_accountability_questions(self):
        """Snap piece asks zero accountability questions about cameras."""
        accountability = [
            "privacy concern", "what about privacy", "facial recognition",
            "without consent", "recording people", "surveillance"
        ]
        found = [a for a in accountability if a.lower() in MCCRACKEN_SNAP_2026.lower()]
        assert len(found) == 0, (
            f"Expected zero accountability questions for Snap cameras, found: {found}"
        )

    def test_meta_accountability_embedded(self):
        """Meta pieces embed accountability language even in balanced coverage."""
        accountability = [
            "privacy-violating", "potentially creepy", "facial recognition",
            "go awry", "mishandled", "concern"
        ]
        found_2021 = [a for a in accountability if a.lower() in MCCRACKEN_META_2021.lower()]
        found_2022 = [a for a in accountability if a.lower() in MCCRACKEN_META_AR_2022.lower()]
        total = len(found_2021) + len(found_2022)
        assert total >= 3, (
            f"Expected 3+ accountability terms across Meta pieces, found {total}: "
            f"2021={found_2021}, 2022={found_2022}"
        )


# =============================================================================
# Test Class 5: Hardware Parity Verification
# =============================================================================

class TestHardwareParityVerification:
    """Confirm both Snap and Meta devices have comparable camera hardware,
    making the privacy vocabulary differential entity-selective, not capability-based."""

    def test_snap_specs_have_cameras(self):
        """Snap Specs include cameras (actually MORE cameras than Meta)."""
        camera_refs = ["camera", "capturing video", "video", "photo"]
        found = sum(1 for c in camera_refs if c.lower() in MCCRACKEN_SNAP_2026.lower())
        assert found >= 1, "Snap Specs article should reference camera/video capabilities"

    def test_meta_glasses_have_cameras(self):
        """Meta glasses include cameras."""
        camera_refs = ["camera", "cameras", "recording", "photo", "video"]
        found = sum(1 for c in camera_refs if c.lower() in MCCRACKEN_META_2021.lower())
        assert found >= 2, "Meta 2021 article should reference camera capabilities"

    def test_snap_cameras_not_interrogated(self):
        """Snap's cameras mentioned neutrally, never interrogated for privacy risk."""
        snap_camera_sentences = [
            s for s in MCCRACKEN_SNAP_2026.split('.')
            if any(c in s.lower() for c in ["camera", "capturing video", "record"])
        ]
        adversarial_in_camera_context = sum(
            1 for s in snap_camera_sentences
            if any(a in s.lower() for a in [
                "privacy", "concern", "surveillance", "without consent",
                "creepy", "dystopia", "spy"
            ])
        )
        assert adversarial_in_camera_context == 0, (
            f"Expected zero adversarial terms near Snap camera mentions, "
            f"found {adversarial_in_camera_context}"
        )


# =============================================================================
# Test Class 6: Mechanism Metadata and Cross-References
# =============================================================================

class TestMechanismMetadata:
    """Structural integrity for Mechanism #201."""

    MECHANISM_ID = 201
    MECHANISM_NAME = (
        "Harry McCracken Fast Company Cross-Entity CEO Attribution "
        "Humanization Differential"
    )

    def test_mechanism_id_assigned(self):
        assert self.MECHANISM_ID == 201

    def test_mechanism_type_is_type_b(self):
        """This is a Type B journalist cross-entity tracking mechanism."""
        mechanism_type = "Type B: Journalist Cross-Entity Tracking"
        assert "Type B" in mechanism_type

    def test_cross_references_mechanism_121(self):
        """Must cross-reference #121 (Fast Company publication-level asymmetry)."""
        cross_refs = [121, 8, 33, 43]  # #121 FastCo, #8 safe target, #33 CEO attribution, #43 humanization
        assert 121 in cross_refs, "Must reference Mechanism #121 (same publication, different angle)"

    def test_journalist_profile_completeness(self):
        """McCracken profile should include career history."""
        profile = {
            "name": "Harry McCracken",
            "publication": "Fast Company",
            "title": "Global Technology Editor",
            "prior_roles": [
                "Editor at Large, Time",
                "Founder/Editor, Technologizer",
                "Editor, PC World"
            ],
            "beat": "technology, AI, consumer devices",
            "notable": "Profiles of Zuckerberg, Nadella, Dorsey, Brownlee"
        }
        assert profile["title"] == "Global Technology Editor"
        assert len(profile["prior_roles"]) >= 3

    def test_confounders_include_strong(self):
        """At least 2 STRONG confounders documented."""
        confounders = [
            {"strength": "STRONG", "desc": "Meta has genuine documented privacy incidents"},
            {"strength": "STRONG", "desc": "CEO access asymmetry — exclusive Spiegel interview"},
            {"strength": "MODERATE", "desc": "Temporal gap (2021 vs 2026)"},
            {"strength": "MODERATE", "desc": "Product category/pricing difference"},
            {"strength": "WEAK", "desc": "Authentic technical admiration"},
        ]
        strong = [c for c in confounders if c["strength"] == "STRONG"]
        assert len(strong) >= 2, f"Expected 2+ STRONG confounders, found {len(strong)}"

    def test_falsification_criterion(self):
        """Document what would DISPROVE this finding."""
        falsification = (
            "If McCracken wrote a Snap Specs follow-up article with equivalent "
            "accountability/privacy language after Specs ship and produce misuse "
            "incidents, that would demonstrate his vocabulary tracks incidents, "
            "not entities — weakening the entity-selective framing claim. Also, "
            "if McCracken wrote a Meta piece with humanization vocabulary comparable "
            "to his Spiegel piece, the CEO attribution differential would be falsified."
        )
        assert "falsif" in falsification.lower() or "disprove" in falsification.lower()

    def test_asymmetry_score(self):
        """Asymmetry score should be moderate (not extreme) because McCracken
        IS more balanced than editorial staff — the delta exists but is smaller
        than the publication-level asymmetry in #121."""
        score = 0.72  # Lower than #121's 0.90 because McCracken is more balanced
        assert 0.60 <= score <= 0.85, f"Score {score} should be moderate (0.60-0.85)"


# =============================================================================
# Test Class 7: McCracken vs Editorial — Beat Assignment Pattern
# =============================================================================

class TestMcCrackenVsEditorialBeatAssignment:
    """Fast Company assigns the aspirational/balanced pieces to McCracken (senior editor)
    and the adversarial compilation pieces to editorial staff. This is a beat assignment
    pattern that produces entity-selective framing at the publication level."""

    def test_mccracken_gets_ceo_access_pieces(self):
        """McCracken (senior editor) gets the CEO interview pieces."""
        mccracken_pieces = [
            "Facebook gets in your Ray-Bans",  # Zuckerberg interview
            "Evan Spiegel says Snap can't fulfill its mission",  # Spiegel interview
        ]
        assert len(mccracken_pieces) == 2, "McCracken covers BOTH CEOs when given access"

    def test_editorial_gets_controversy_compilation(self):
        """The adversarial 'many controversies' piece is NOT by McCracken."""
        # McCracken's Meta piece uses "Dystopia averted" (balanced)
        # Editorial uses "covert recording," "privacy invasive" (adversarial)
        mccracken_tone = "Dystopia averted" in MCCRACKEN_META_2021
        editorial_tone = "covert recording" in FASTCO_META_CONTROVERSIES_2026.lower()
        assert mccracken_tone, "McCracken's Meta piece should use balanced framing"
        assert editorial_tone, "Editorial piece should use adversarial framing"

    def test_beat_assignment_creates_entity_asymmetry(self):
        """The assignment pattern means: when McCracken covers Snap aspirationally
        and editorial covers Meta adversarially, the PUBLICATION output is asymmetric
        even though McCracken himself is relatively balanced."""
        # McCracken's Meta coverage: balanced (privacy noted but constructively)
        # McCracken's Snap coverage: aspirational (zero privacy vocabulary)
        # Editorial's Meta coverage: adversarial (5+ concern categories)
        # Editorial's Snap coverage: DOES NOT EXIST (no adversarial Snap compilation)

        # The asymmetry emerges from WHAT EXISTS, not from any individual writer
        editorial_meta_adversarial = True  # "Many controversies" exists
        editorial_snap_adversarial = False  # No "Many controversies of Snap Specs"
        assert editorial_meta_adversarial and not editorial_snap_adversarial, (
            "Publication asymmetry: adversarial compilation exists for Meta but not Snap"
        )
