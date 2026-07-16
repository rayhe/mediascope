"""Tests for BuzzFeed smart glasses women's safety article (Jul 14, 2026).

Article: "Smart Glasses Are Changing How We See The World. But Are We Ready
For How They Can Be Misused?" — BuzzFeed, Becca Monaghan, July 14, 2026.

NOTE: BuzzFeed is not one of the 5 tracked publications.  Selected because
no fresh, unanalyzed article from a tracked publication was available for
the Jul 16 13:00 PT Type A iteration and the article covers Meta smart
glasses — a core toolkit domain.

Validates:
1. Entity extraction: Meta cluster, GDPR/EU Regulatory cluster, and gaps
   for UK institutional entities (Refuge, NPCC, Samuels Solicitors, ICO).
2. Framing device detection: 13 device types confirmed by toolkit; known
   gaps for assumed_consensus and sovereignty_framing.
3. Source extraction: Refuge affiliation bug ("BTEC introduction to
   incel-ism" parsed as affiliation), missing institutional sources.
4. Sentiment: VADER polarity inversion (scores +0.24 for a clearly
   negative article, manual assessment −0.55).
5. Consent/privacy framing: consent_alarm, default_burden_privacy,
   surveillance_creep detection on advocacy-style text.

Discovered in Type A iteration, Jul 16, 2026 13:00 PT.
"""

import pytest

from mediascope.analysis import analyze_text
from mediascope.analyze.framing import detect_framing_devices
from mediascope.analyze.sources import extract_sources


TITLE = (
    "Smart Glasses Are Changing How We See The World. But Are We "
    "Ready For How They Can Be Misused?"
)

# Representative excerpts rather than full article — enough for each test
# to exercise the targeted behavior.

ARTICLE = (
    "Every time a new bit of tech promises to change the world, women seem "
    "to be left dealing with the risks – and it's a conversation we're still "
    "avoiding.\n\n"
    "And yet, feeds are filled with women unknowingly being recorded by men "
    "while they're working, walking down the street, or simply trying to "
    "enjoy a night out.\n\n"
    "We're still debating whether secretly filming strangers for social media "
    "is creepy (it is) when the more uncomfortable question is why we're still "
    "acting surprised by the misuse of tech when it's used in ways developers "
    "didn't intend.\n\n"
    "Technology itself isn't the problem. The problem is that innovation often "
    "moves at lightning speed, while conversations about privacy, consent, "
    "and safety seem to be playing catch-up.  For the women who discover "
    "they've been recorded without their knowledge, that debate is anything "
    "but theoretical.\n\n"
    'Take the latest so-called "rizzing" trend on social media, where men '
    "approach women in public – from busy shopping streets to public-facing "
    "workplaces – asking for numbers under the guise of innocent interactions "
    "before uploading the footage online.\n\n"
    "Some women featured in these videos were not aware they were being "
    "recorded in the first place, particularly as smart glasses began "
    "appearing more widely.\n\n"
    "What's ironic is how some Brits wave the banner of \"protecting our "
    'women and children" when it suits their political agenda. Yet when '
    "women ask for something as basic as respect, consent, and common "
    "decency, suddenly it's treated as an overreaction.\n\n"
    "Instead of arguing about whether people can secretly record strangers, "
    "shouldn't we be asking why it's becoming normalised rather than being "
    "recognised for what it is – a sort of BTEC introduction to incel-ism.\n\n"
    "Women's charity Refuge reported a 62 per cent increase in referrals to "
    "its specialist Technology-Facilitated Abuse and Economic Empowerment "
    "team in 2025 alone. Among the emerging patterns is the weaponisation of "
    "smart accessories, including glasses used to secretly record people.\n\n"
    '"It is currently far too easy for perpetrators to access and weaponise '
    "smart accessories, and our frontline teams are seeing the devastating "
    'consequences of this abuse," they shared.\n\n'
    '"Enough is enough. As wearable technology becomes embedded in our lives, '
    "protections for survivors must keep pace. It is unacceptable for the "
    "safety and well-being of women and girls to be treated as an afterthought "
    "once a technology has been developed and distributed. Their safety must "
    "be a foundational principle shaping both the design of wearable technology "
    'and the regulatory frameworks that surround it," they added.\n\n'
    "Meta says, however, it does have safeguards in place, including a "
    "capture LED that cannot be switched off and a feature that automatically "
    "disables the camera if the recording indicator is blocked or tampered "
    "with.\n\n"
    '"Since the introduction of this safeguard, we\'ve seen some people go '
    "beyond using tape to sophisticated efforts to modify or destroy the "
    'capture LED," Meta acknowledges in its FAQs. "We are continuously '
    "improving our ability to detect tampering, and now we're updating the "
    "glasses to disable the camera if they detect the LED was physically "
    "tampered with or destroyed. No other kind of camera has done this, and "
    "we're proud to lead the industry forward.\"\n\n"
    "They also said these efforts extend across platforms, including Facebook "
    "Marketplace listings that advertise tampering services, adding that they "
    'will take action "up to banning accounts that do this".\n\n'
    '"We also take legal action against people or businesses that sell '
    "services designed for tampering with the capture LED — both on and off "
    'our own platforms," they said.\n\n'
    "The vast majority of people buying smart glasses won't misuse them – but "
    "that's not really the point. We don't design seatbelts because we expect "
    "everyone to crash; we design them because incidents happen.\n\n"
    "As part of its Violence Against Women and Girls Strategy, the government "
    "has committed to exploring what more can be done to encourage \"safety "
    'by design" in smart and connected technology.\n\n'
    '"Recording someone in public without consent to cause alarm, distress or '
    "for sexual gratification may constitute offences such as harassment, "
    "stalking, or voyeurism,\" a government spokesperson told BuzzFeed. "
    '"For cases involving intimate recording, we are already further '
    "strengthening protections for victims of intimate image abuse through "
    'new offences in the Crime and Policing Bill."\n\n'
    '"We will continue to engage with the Information Commissioner\'s Office '
    "to ensure regulation remains effective as technology evolves and that "
    "people's information rights are protected,\" they added.\n\n"
    "Legal experts at Samuels Solicitors say that depending on the situation, "
    "individuals may be able to bring claims for breach of privacy, misuse of "
    "private information, harassment, or unlawful data processing under UK "
    "GDPR.\n\n"
    "Harassment law can apply where someone is repeatedly filmed or targeted "
    "in a way that is distressing or intrusive, especially if that content is "
    "then posted online. In more serious cases, where footage is used to "
    "pressure, threaten, or coerce someone, offences such as blackmail may "
    "also come into play.\n\n"
    "A spokesperson for the National Police Chiefs' Council told BuzzFeed: "
    '"If anyone has any concerns with this behaviour, we encourage them to '
    "come forward at the earliest opportunity and report it to the police.\"\n\n"
    "They added that people should use the technology responsibly, and report "
    "incidents where they feel uncomfortable, distressed, or violated.\n\n"
    '"We designed our AI glasses with privacy and safety features built in '
    "from the start — informed by engagement with safety experts, including "
    "women's safety organisations,\" a Meta spokesperson told BuzzFeed.\n\n"
    '"Our glasses have always had an LED light that activates whenever '
    "someone captures a photo or video for their gallery. They also feature "
    "tamper detection technology, and we are updating the glasses to disable "
    "the camera if they detect the LED was physically tampered with or "
    'destroyed," they continued.\n\n'
    '"No other kind of camera has done this and we\'re proud to lead the '
    "industry forward. We have teams dedicated to ensuring our glasses feel "
    "great for wearers and the people around them, so we can continue "
    'delivering products that make everyday life better."\n\n'
    "The question isn't whether wearable technology is here to stay – it "
    "almost certainly is. The challenge is making sure safety features evolve "
    "alongside the technology, particularly as products enter the world and "
    "some people inevitably find new ways to exploit the gaps."
)


@pytest.fixture
def result():
    return analyze_text(ARTICLE, title=TITLE, target_entity="Meta")


# ===================================================================
# 1. Entity extraction
# ===================================================================


class TestEntityExtraction:
    """Verify entity detection for this article."""

    def test_meta_cluster_detected(self, result):
        """Meta should be detected and clustered correctly."""
        meta_entities = [
            e for e in result["entities"] if e["cluster"] == "Meta"
        ]
        assert len(meta_entities) >= 2, (
            f"Expected ≥2 Meta-cluster mentions. Found: {meta_entities}"
        )

    def test_facebook_clusters_with_meta(self, result):
        """'Facebook Marketplace' mention should cluster with Meta."""
        meta_entities = [
            e for e in result["entities"] if e["cluster"] == "Meta"
        ]
        entity_names = [e["entity"] for e in meta_entities]
        assert any("Facebook" in n for n in entity_names), (
            f"'Facebook' should cluster with Meta. Found: {entity_names}"
        )

    def test_gdpr_detected(self, result):
        """GDPR should be detected as EU Regulatory cluster."""
        gdpr_entities = [
            e for e in result["entities"]
            if "gdpr" in e["entity"].lower()
        ]
        assert len(gdpr_entities) >= 1, "GDPR should be detected"
        assert gdpr_entities[0]["cluster"] == "EU Regulatory"

    @pytest.mark.xfail(
        reason="Refuge is a UK charity not in entity database — gap",
        strict=False,
    )
    def test_refuge_charity_detected(self, result):
        """Refuge (UK domestic violence charity) should be detected."""
        entity_names = [e["entity"].lower() for e in result["entities"]]
        assert any("refuge" in n for n in entity_names), (
            f"Refuge not in entities. Found: {entity_names}"
        )

    @pytest.mark.xfail(
        reason="UK institutional entities (NPCC, ICO, Samuels) not tracked",
        strict=False,
    )
    def test_uk_institutional_entities(self, result):
        """UK institutional entities should be detected."""
        entity_names = " ".join(e["entity"] for e in result["entities"])
        missing = []
        for name in ["National Police", "Information Commissioner", "Samuels"]:
            if name not in entity_names:
                missing.append(name)
        assert not missing, f"Missing UK institutional entities: {missing}"


# ===================================================================
# 2. Framing device detection
# ===================================================================


class TestFramingDevices:
    """Verify framing device detection on advocacy-style article."""

    def test_rhetorical_question_detected(self, result):
        """'shouldn't we be asking' should trigger rhetorical_question."""
        rq = [
            d for d in result["framing_devices"]
            if d["device_type"] == "rhetorical_question"
        ]
        assert len(rq) >= 1, "Expected rhetorical_question for advocacy text"

    def test_loaded_language_detected(self, result):
        """Loaded terms ('weaponisation', 'secretly', 'misuse') should fire."""
        ll = [
            d for d in result["framing_devices"]
            if d["device_type"] == "loaded_language"
        ]
        assert len(ll) >= 3, (
            f"Expected ≥3 loaded_language hits for this article. Found: {len(ll)}"
        )

    def test_analogy_metaphor_seatbelt(self, result):
        """Seatbelt analogy should trigger analogy_metaphor."""
        am = [
            d for d in result["framing_devices"]
            if d["device_type"] == "analogy_metaphor"
        ]
        assert len(am) >= 1, "Seatbelt comparison should trigger analogy_metaphor"

    def test_power_asymmetry_detected(self, result):
        """Recording/consent power imbalance should trigger power_asymmetry."""
        pa = [
            d for d in result["framing_devices"]
            if d["device_type"] == "power_asymmetry"
        ]
        assert len(pa) >= 1

    def test_emotional_appeal_detected(self, result):
        """'devastating consequences', 'No other' should trigger."""
        ea = [
            d for d in result["framing_devices"]
            if d["device_type"] == "emotional_appeal"
        ]
        assert len(ea) >= 1

    def test_editorial_aside_detected(self, result):
        """'And yet' editorial interjection should trigger editorial_aside."""
        ea = [
            d for d in result["framing_devices"]
            if d["device_type"] == "editorial_aside"
        ]
        assert len(ea) >= 1

    def test_ironic_quotation_rizzing(self, result):
        """'rizzing' in scare quotes should trigger ironic_quotation."""
        iq = [
            d for d in result["framing_devices"]
            if d["device_type"] == "ironic_quotation"
        ]
        assert len(iq) >= 1, "'rizzing' should trigger ironic_quotation"

    def test_consent_alarm_detected(self, result):
        """'without their knowledge', 'without consent' should fire."""
        ca = [
            d for d in result["framing_devices"]
            if d["device_type"] == "consent_alarm"
        ]
        assert len(ca) >= 2, (
            f"Expected ≥2 consent_alarm hits. Found: {len(ca)}"
        )

    def test_surveillance_creep_detected(self, result):
        """Recording-without-consent patterns should trigger surveillance_creep."""
        sc = [
            d for d in result["framing_devices"]
            if d["device_type"] == "surveillance_creep"
        ]
        assert len(sc) >= 1

    def test_default_burden_privacy_detected(self, result):
        """Privacy-as-afterthought language should trigger default_burden_privacy."""
        dbp = [
            d for d in result["framing_devices"]
            if d["device_type"] == "default_burden_privacy"
        ]
        assert len(dbp) >= 1

    def test_catastrophizing_detected(self, result):
        """'devastating' should trigger catastrophizing."""
        cat = [
            d for d in result["framing_devices"]
            if d["device_type"] == "catastrophizing"
        ]
        assert len(cat) >= 1

    def test_litigation_framing_detected(self, result):
        """'legal action against' should trigger litigation_framing."""
        lf = [
            d for d in result["framing_devices"]
            if d["device_type"] == "litigation_framing"
        ]
        assert len(lf) >= 1

    @pytest.mark.xfail(
        reason="tempering_coda fires via detect_framing_devices() on full "
               "article text but is filtered out by analyze_text() pipeline — "
               "structural post-pass filtering discrepancy",
        strict=False,
    )
    def test_tempering_coda_detected(self, result):
        """Legal responsibilities language should trigger tempering_coda."""
        tc = [
            d for d in result["framing_devices"]
            if d["device_type"] == "tempering_coda"
        ]
        assert len(tc) >= 1

    def test_device_type_count(self, result):
        """Toolkit should detect ≥10 distinct device types for this article."""
        device_types = set(d["device_type"] for d in result["framing_devices"])
        assert len(device_types) >= 10, (
            f"Expected ≥10 device types. Found {len(device_types)}: {device_types}"
        )

    @pytest.mark.xfail(
        reason="assumed_consensus not detected — 'it is' parenthetical too "
               "short for pattern match",
        strict=False,
    )
    def test_assumed_consensus(self, result):
        """'(it is)' parenthetical verdict should trigger assumed_consensus."""
        ac = [
            d for d in result["framing_devices"]
            if d["device_type"] == "assumed_consensus"
        ]
        assert len(ac) >= 1

    @pytest.mark.xfail(
        reason="sovereignty_framing not detected — UK-centric 'protecting our "
               "women' language not matched by current patterns",
        strict=False,
    )
    def test_sovereignty_framing(self, result):
        """UK sovereignty language should trigger sovereignty_framing."""
        sf = [
            d for d in result["framing_devices"]
            if d["device_type"] == "sovereignty_framing"
        ]
        assert len(sf) >= 1


# ===================================================================
# 3. Source extraction
# ===================================================================


class TestSourceExtraction:
    """Verify source extraction for multi-source advocacy article."""

    def test_refuge_extracted(self, result):
        """Women's charity Refuge should be extracted as a source."""
        source_names = [s["name"].lower() for s in result["sources"]]
        assert any("refuge" in n for n in source_names), (
            f"Refuge should be in sources. Found: {source_names}"
        )

    @pytest.mark.xfail(
        reason="Bug: source affiliation parser bleeds across paragraph "
               "boundaries — 'BTEC introduction to incel-ism' from preceding "
               "paragraph parsed as Refuge's affiliation",
        strict=False,
    )
    def test_refuge_affiliation_not_btec(self, result):
        """Refuge's affiliation should NOT be 'BTEC introduction to incel-ism'.

        Bug: the toolkit parses the preceding editorial sentence's "BTEC
        introduction to incel-ism" phrase as Refuge's affiliation context.
        """
        refuge_sources = [
            s for s in result["sources"]
            if "refuge" in s["name"].lower()
        ]
        if not refuge_sources:
            pytest.skip("Refuge not extracted as source")
        aff = refuge_sources[0].get("affiliation", "")
        assert "btec" not in aff.lower() and "incel" not in aff.lower(), (
            f"Refuge affiliation is '{aff}' — should not contain "
            f"editorial text from a different paragraph"
        )

    def test_government_spokesperson_extracted(self, result):
        """Government spokesperson should be extracted."""
        source_names = [s["name"].lower() for s in result["sources"]]
        assert any(
            "government" in n and "spokesperson" in n for n in source_names
        ), f"Government spokesperson missing. Found: {source_names}"

    def test_meta_spokesperson_extracted(self, result):
        """Meta spokesperson should be extracted."""
        source_names = [s["name"].lower() for s in result["sources"]]
        assert any(
            "meta" in n and "spokesperson" in n for n in source_names
        ), f"Meta spokesperson missing. Found: {source_names}"

    def test_meta_spokesperson_affiliation(self, result):
        """Meta spokesperson's affiliation should be Meta."""
        meta_sources = [
            s for s in result["sources"]
            if "meta" in s["name"].lower() and "spokesperson" in s["name"].lower()
        ]
        assert len(meta_sources) >= 1
        assert meta_sources[0].get("affiliation") == "Meta"

    @pytest.mark.xfail(
        reason="Samuels Solicitors not extracted — institutional legal firm "
               "not recognized as quotable source",
        strict=False,
    )
    def test_samuels_solicitors_extracted(self, result):
        """'Legal experts at Samuels Solicitors say' should be a source."""
        source_names = [s["name"].lower() for s in result["sources"]]
        assert any("samuels" in n for n in source_names), (
            f"Samuels Solicitors missing. Found: {source_names}"
        )

    @pytest.mark.xfail(
        reason="NPCC not extracted as source — institutional suffix filter",
        strict=False,
    )
    def test_npcc_spokesperson_extracted(self, result):
        """NPCC spokesperson should be extracted."""
        source_names = " ".join(s["name"] for s in result["sources"])
        assert "National Police" in source_names or "NPCC" in source_names, (
            f"NPCC missing. Found: {source_names}"
        )


# ===================================================================
# 4. Sentiment analysis
# ===================================================================


class TestSentiment:
    """Verify sentiment scoring on advocacy-negative article."""

    def test_emotional_intensity_high(self, result):
        """Emotional intensity should be high (≥0.6) for advocacy article."""
        ei = result["sentiment"]["emotional_language_intensity"]
        assert ei >= 0.6, (
            f"Expected high emotional intensity ≥0.6, got {ei:.4f}"
        )

    @pytest.mark.xfail(
        reason="Known VADER polarity inversion: toolkit scores +0.24 for an "
               "article with manual assessment −0.55. Advocacy language uses "
               "positive-valence corporate quotes and indirect framing that "
               "confuses lexical sentiment scoring.",
        strict=False,
    )
    def test_overall_tone_negative(self, result):
        """Article is clearly negative toward Meta — tone should be < 0."""
        tone = result["sentiment"]["overall_tone"]
        assert tone < 0, (
            f"Expected negative tone for anti-Meta advocacy article. "
            f"Got {tone:.4f} (manual assessment: −0.55)"
        )

    @pytest.mark.xfail(
        reason="Known VADER polarity inversion: analyze_text pipeline scores "
               "+0.64 for a clearly negative advocacy article (manual −0.55). "
               "Corporate defense quotes with positive valence ('proud to "
               "lead the industry') overwhelm the negative advocacy framing.",
        strict=False,
    )
    def test_tone_not_strongly_positive(self, result):
        """Even if VADER overshoots, tone should not be strongly positive."""
        tone = result["sentiment"]["overall_tone"]
        assert tone < 0.5, (
            f"Tone {tone:.4f} is strongly positive — clearly wrong for this "
            f"advocacy-critical article"
        )


# ===================================================================
# 5. Specific framing patterns — advocacy article characteristics
# ===================================================================


class TestAdvocacyFramingPatterns:
    """Tests for framing patterns common in advocacy-style articles."""

    def test_ironic_quotation_protecting_women(self):
        """Scare-quoted 'protecting our women and children' should fire."""
        text = (
            'What\'s ironic is how some Brits wave the banner of "protecting '
            'our women and children" when it suits their political agenda.'
        )
        devices = detect_framing_devices(text)
        iq = [d for d in devices if d.device_type == "ironic_quotation"]
        assert len(iq) >= 1, (
            "Scare-quoted political phrase should trigger ironic_quotation"
        )

    def test_consent_alarm_without_knowledge(self):
        """'without their knowledge' should trigger consent_alarm."""
        text = (
            "For the women who discover they've been recorded without "
            "their knowledge, that debate is anything but theoretical."
        )
        devices = detect_framing_devices(text)
        ca = [d for d in devices if d.device_type == "consent_alarm"]
        assert len(ca) >= 1

    def test_seatbelt_analogy_standalone(self):
        """Seatbelt analogy as standalone passage."""
        text = (
            "We don't design seatbelts because we expect everyone to crash; "
            "we design them because incidents happen."
        )
        devices = detect_framing_devices(text)
        am = [d for d in devices if d.device_type == "analogy_metaphor"]
        assert len(am) >= 1

    def test_weaponisation_loaded_language(self):
        """'weaponisation' should trigger loaded_language."""
        text = (
            "Among the emerging patterns is the weaponisation of smart "
            "accessories, including glasses used to secretly record people."
        )
        devices = detect_framing_devices(text)
        ll = [d for d in devices if d.device_type == "loaded_language"]
        loaded_terms = [text[d.start:d.end].lower() for d in ll]
        assert any("weapon" in t for t in loaded_terms), (
            f"'weaponisation' should trigger loaded_language. "
            f"Found loaded terms: {loaded_terms}"
        )

    def test_devastating_catastrophizing(self):
        """'devastating consequences' should trigger catastrophizing."""
        text = (
            "our frontline teams are seeing the devastating consequences "
            "of this abuse"
        )
        devices = detect_framing_devices(text)
        cat = [d for d in devices if d.device_type == "catastrophizing"]
        assert len(cat) >= 1


# ===================================================================
# 6. Source affiliation bug — cross-paragraph bleed
# ===================================================================


class TestSourceAffiliationBleed:
    """Regression tests for affiliation parser bleeding across paragraphs."""

    @pytest.mark.xfail(
        reason="Bug: affiliation parser bleeds across paragraph boundaries — "
               "same root cause as test_refuge_affiliation_not_btec",
        strict=False,
    )
    def test_charity_affiliation_from_nearby_context(self):
        """When source is 'Women's charity Refuge', affiliation should NOT
        pull from preceding unrelated paragraph content."""
        text = (
            "shouldn't we be asking why it's becoming normalised rather "
            "than being recognised for what it is – a sort of BTEC "
            "introduction to incel-ism.\n\n"
            "Women's charity Refuge reported a 62 per cent increase in "
            "referrals to its specialist Technology-Facilitated Abuse and "
            "Economic Empowerment team in 2025 alone.\n\n"
            '"It is currently far too easy for perpetrators to access and '
            'weaponise smart accessories," they shared.'
        )
        sources = extract_sources(text)
        refuge_sources = [
            s for s in sources if "refuge" in s.name.lower()
        ]
        if not refuge_sources:
            pytest.skip("Refuge not extracted")
        aff = refuge_sources[0].affiliation or ""
        assert "btec" not in aff.lower(), (
            f"Affiliation '{aff}' bleeds from preceding paragraph"
        )

    def test_meta_affiliation_correct(self):
        """Meta spokesperson affiliation should be 'Meta', not surrounding text."""
        text = (
            '"We designed our AI glasses with privacy and safety features '
            "built in from the start — informed by engagement with safety "
            "experts, including women's safety organisations,\" a Meta "
            "spokesperson told BuzzFeed."
        )
        sources = extract_sources(text)
        meta_sources = [
            s for s in sources
            if "meta" in s.name.lower() and "spokesperson" in s.name.lower()
        ]
        assert len(meta_sources) >= 1
        assert meta_sources[0].affiliation == "Meta"
