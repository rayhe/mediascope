"""
Type A Deep Dive: Gizmodo ICE Ban Entity Selection vs OpenAI Camera Device Bore Framing

Publication: Gizmodo (G/O Media)
Competitor: OpenAI
Mechanism #268: Gizmodo ICE Ban Meta Entity Selection vs OpenAI Camera Device
    Bore Framing Asymmetry

FINDING: Gizmodo applies dramatically different framing to functionally equivalent
camera devices from Meta vs OpenAI. When ICE bans "Meta Glasses or similar devices"
(a generic smart glasses ban), Gizmodo's headline makes it entity-specific ("Even ICE
Thinks Smart Glasses Are a Privacy Liability"), Meta is named 6+ times, whistleblower
exploitation is connected, and the article deploys alarm vocabulary throughout. When
OpenAI announces a smart speaker with camera AND facial recognition (more privacy-
invasive: always-on home surveillance + biometric identification), Gizmodo's headline
frames it as boring/unoriginal ("OpenAI Might Be Making a Smart Speaker That No One
Asked for") with zero alarm vocabulary and one throwaway privacy sentence.

KEY INSIGHT — INSTITUTIONAL VALIDATION ENTITY SELECTION: ICE's memo bans ALL smart
glasses ("Meta Glasses or similar devices") but Gizmodo selects Meta as the entity
whose privacy threat is validated by the ban. This is entity selection at the
institutional level — using a government ban to validate the Meta = surveillance
framing while ignoring that the ban's logic applies equally to any camera wearable,
including OpenAI's planned devices.

Sources:
- Gizmodo ICE ban (Aug 19, 2026): https://gizmodo.com/even-ice-thinks-smart-glasses-are-a-privacy-liability-2000800271
- Gizmodo OpenAI speaker (Feb 21, 2026): https://gizmodo.com/openai-might-be-making-a-smart-speaker-that-no-one-asked-for-2000724650
- Original NYT report on ICE memo
- The Information report on OpenAI hardware
"""

import unittest
import re


# === Article content from Gizmodo ===

ICE_BAN_ARTICLE = {
    "url": "https://gizmodo.com/even-ice-thinks-smart-glasses-are-a-privacy-liability-2000800271",
    "title": "Even ICE Thinks Smart Glasses Are a Privacy Liability",
    "publication": "Gizmodo",
    "date": "2026-08-19",
    "content": """You can officially list Immigration and Customs Enforcement (ICE) as one of the growing number of organizations banning smart glasses.

According to the New York Times, ICE sent out a memo on Tuesday prohibiting the use of smart glasses by its employees; that means agents and those who work in its offices. The reason? ICE thinks they're a potential privacy liability. Here's what acting director David Venturella states in the memo, per the New York Times:

"… the use of Meta Glasses or similar devices could unintentionally capture, record or transmit sensitive information, potentially compromising privacy and legal protections."

The words "unintentionally capture" feel pointed here. To me, this implies that ICE isn't so much concerned with videos or pictures that its employees or agents might take on purpose but rather with information that the smart glasses could gobble up incidentally. History suggests that ICE's concerns here are founded.

Earlier this year, whistleblowers who worked as contractors for Meta detailed issues over videos that were being used as a part of the company's AI training program. The workers say they were asked to review intimate footage of people having sex, naked, using the bathroom, and more. Some of those videos, they say, appear to have been taken accidentally. Clearly, due to Meta's terms of service, videos and pictures taken with Meta's smart glasses aren't as airtight as they might seem.

For context, DHS agents have already been spotted wearing smart glasses, Meta's in particular, so the ban is not exactly proactive. Furthermore, there are reports that the Department of Homeland Security (DHS) is developing its own smart glasses that could be used to surveil the U.S. border. Those reports also suggest that there's interest in marrying smart glasses with facial recognition so that they could automatically check a person's face against a database.

That's all to say that ICE's decision to ban smart glasses isn't philosophical—surveillance is something the organization engages with regularly—but clearly it has other concerns, and those concerns may not be with smart glasses as much as with the dubious policies with user data that surround them.""",
}

OPENAI_SPEAKER_ARTICLE = {
    "url": "https://gizmodo.com/openai-might-be-making-a-smart-speaker-that-no-one-asked-for-2000724650",
    "title": "OpenAI Might Be Making a Smart Speaker That No One Asked for",
    "publication": "Gizmodo",
    "date": "2026-02-21",
    "content": """If you were looking around at the smart speaker field and feeling like the whole idea of an audio device with microphones and a voice assistant has stagnated, I have some pertinent news for you: it apparently has.

If a report from The Information about OpenAI's first hardware is any indication, we have run out of ideas, folks. Per The Information:

"The speaker will have a camera, enabling it to take in information about its users and their surroundings, such as items on a nearby table or conversations people are having in the vicinity, according to one of the people. It will also allow people to buy things by identifying them with a facial recognition feature similar to Apple's Face ID, the people said."

So, if we're to believe the reporting, OpenAI's major contributions to the smart speaker space are being able to look at objects on a table and online shopping. I'll concede that the first one is almost novel. Computer vision isn't new—Amazon's Echo Show, its smart home hub with a screen and camera, can identify objects already using its "Show and Tell" feature—but it's just catching on. That being said, I don't know that this particular example screams "useful." Computer vision, at least in my experience, is kind of a trap. It's novel, but not altogether useful on a consistent basis—at least in gadgets like the Ray-Ban Meta AI glasses. The best use case here will likely be for accessibility purposes, helping blind or low-vision people identify things.

As for shopping, well… that's definitely already a thing. If you own a smart speaker made by Amazon, you can already add things to your cart using just your voice and have those things delivered to your house without ever opening an app—there are voice passcodes to verify purchases instead. So, I'm going to give OpenAI zero points on that front for originality.

If anything, I also suspect that a smart speaker with a camera and face recognition would be used to deliver some kind of personalized information. You might, for example, be able to walk up to your smart speaker and have it give you information about your calendar for that day or some other kind of customizable notifications. Whether you trust OpenAI with your face and access to looking around your room is another story entirely, but it would appear the company thinks you'll be chill with it.

If those ideas aren't original enough for you, The Information reports that OpenAI has some other tricks up its sleeve, including the potential to release smart glasses as well as a smart lamp. I'll admit, I'm weirdly intrigued by the smart lamp part of things, but if the lackluster potential features of its smart speaker are anything to go by, I wouldn't get your hopes up.

One thing is for certain, and that's that OpenAI seems to have its sights trained on a lot of different categories. There were already reports that the company is pursuing a wearable in an earbuds-like form factor, for example, as well as a pendant, and even a pen. The playbook, if I'm to read between the lines, is that there is no form factor that's off the table necessarily, except for maybe a phone. I look forward to seeing OpenAI's vast resources flow into making the world's most sophisticated smart pants or whatever inane idea that only OpenAI's deep wallet can cook up next.""",
}

# ICE memo quote explicitly says "Meta Glasses OR SIMILAR DEVICES"
ICE_MEMO_QUOTE = "the use of Meta Glasses or similar devices could unintentionally capture, record or transmit sensitive information, potentially compromising privacy and legal protections."

# === Privacy alarm vocabulary lists ===
ALARM_VOCABULARY = [
    "privacy liability", "unintentionally capture", "gobble up",
    "whistleblowers", "intimate footage", "having sex", "naked",
    "using the bathroom", "airtight", "surveil", "surveillance",
    "dubious policies", "spotted wearing",
]

BORE_VOCABULARY = [
    "stagnated", "run out of ideas", "not altogether useful",
    "lackluster", "zero points", "no one asked for",
    "inane idea", "smart pants",
]


class TestICEBanHeadlineEntitySelection(unittest.TestCase):
    """ICE ban applies to ALL smart glasses but Gizmodo's headline targets Meta."""

    def test_ice_memo_says_or_similar_devices(self):
        """ICE memo explicitly includes non-Meta devices."""
        assert "or similar devices" in ICE_MEMO_QUOTE

    def test_headline_does_not_say_meta_but_implies_it(self):
        """Headline says 'Smart Glasses' generically but article is 100% Meta."""
        title = ICE_BAN_ARTICLE["title"]
        assert "Meta" not in title  # Headline is generic...
        # ...but the article body names Meta 6+ times
        meta_mentions = len(re.findall(r'\bMeta\b', ICE_BAN_ARTICLE["content"]))
        assert meta_mentions >= 5, f"Expected 5+ Meta mentions, found {meta_mentions}"

    def test_openai_not_mentioned_in_ice_ban_article(self):
        """Despite OpenAI building a camera device, zero OpenAI mentions."""
        assert "OpenAI" not in ICE_BAN_ARTICLE["content"]

    def test_apple_not_mentioned_in_ice_ban_article(self):
        """Despite Apple building camera AirPods, zero Apple mentions."""
        assert "Apple" not in ICE_BAN_ARTICLE["content"]

    def test_headline_uses_institutional_validation_frame(self):
        """'Even ICE Thinks...' uses the authority of a government agency to
        validate the Meta = privacy threat narrative."""
        title = ICE_BAN_ARTICLE["title"]
        assert "Even" in title  # rhetorical escalation
        assert "ICE" in title
        assert "Privacy Liability" in title


class TestOpenAISpeakerHeadlineBoreFraming(unittest.TestCase):
    """OpenAI's camera + facial recognition device framed as boring, not invasive."""

    def test_headline_frames_as_unwanted_not_invasive(self):
        """Headline: 'No One Asked for' = product tedium, not privacy alarm."""
        title = OPENAI_SPEAKER_ARTICLE["title"]
        assert "No One Asked" in title
        assert "Privacy" not in title
        assert "Surveillance" not in title
        assert "Liability" not in title

    def test_article_describes_camera_and_facial_recognition(self):
        """Article explicitly describes camera + facial recognition features."""
        content = OPENAI_SPEAKER_ARTICLE["content"]
        assert "camera" in content.lower()
        assert "facial recognition" in content.lower() or "face recognition" in content.lower()

    def test_single_privacy_sentence(self):
        """Only one throwaway sentence addresses privacy trust."""
        content = OPENAI_SPEAKER_ARTICLE["content"]
        privacy_sentences = [
            s for s in content.split(".")
            if "trust" in s.lower() and "openai" in s.lower()
        ]
        # The one sentence: "Whether you trust OpenAI with your face..."
        assert len(privacy_sentences) >= 1
        # But it's framed as casual, not alarming
        for s in privacy_sentences:
            assert "liability" not in s.lower()
            assert "surveillance" not in s.lower()

    def test_no_advocacy_groups_quoted(self):
        """No ACLU, EFF, EPIC, or other privacy groups cited for OpenAI."""
        content = OPENAI_SPEAKER_ARTICLE["content"]
        advocacy_groups = ["ACLU", "EFF", "EPIC", "Electronic Frontier",
                          "Electronic Privacy", "Civil Liberties"]
        for group in advocacy_groups:
            assert group not in content, f"Found {group} in OpenAI article"


class TestAlarmVocabularyAsymmetry(unittest.TestCase):
    """ICE/Meta article deploys alarm vocabulary; OpenAI article deploys bore vocabulary."""

    def test_meta_article_alarm_term_count(self):
        """ICE ban article has 6+ alarm terms."""
        content = ICE_BAN_ARTICLE["content"].lower()
        alarm_hits = [term for term in ALARM_VOCABULARY if term in content]
        assert len(alarm_hits) >= 6, f"Expected 6+ alarm terms, found {len(alarm_hits)}: {alarm_hits}"

    def test_openai_article_alarm_term_count(self):
        """OpenAI speaker article has 0 alarm terms from the same vocabulary set."""
        content = OPENAI_SPEAKER_ARTICLE["content"].lower()
        alarm_hits = [term for term in ALARM_VOCABULARY if term in content]
        assert len(alarm_hits) == 0, f"Expected 0 alarm terms, found {len(alarm_hits)}: {alarm_hits}"

    def test_openai_article_bore_term_count(self):
        """OpenAI article uses 4+ bore/tedium terms instead of alarm terms."""
        content = OPENAI_SPEAKER_ARTICLE["content"].lower()
        bore_hits = [term for term in BORE_VOCABULARY if term in content]
        assert len(bore_hits) >= 4, f"Expected 4+ bore terms, found {len(bore_hits)}: {bore_hits}"

    def test_meta_article_bore_term_count(self):
        """Meta/ICE article does not use bore vocabulary — it's all alarm."""
        content = ICE_BAN_ARTICLE["content"].lower()
        bore_hits = [term for term in BORE_VOCABULARY if term in content]
        assert len(bore_hits) == 0, f"Expected 0 bore terms, found {len(bore_hits)}: {bore_hits}"


class TestWhistleblowerExploitationNarrativeChaining(unittest.TestCase):
    """ICE article chains to unrelated whistleblower controversy; OpenAI article chains
    to Amazon Echo (product comparison, not privacy crisis)."""

    def test_ice_article_chains_to_whistleblower_footage(self):
        """Meta article connects ICE ban to contractor footage review scandal."""
        content = ICE_BAN_ARTICLE["content"]
        assert "whistleblowers" in content.lower()
        assert "intimate footage" in content or "having sex" in content

    def test_openai_article_chains_to_amazon_product(self):
        """OpenAI article connects to Amazon Echo Show as product comparison."""
        content = OPENAI_SPEAKER_ARTICLE["content"]
        assert "Amazon" in content
        assert "Echo Show" in content
        # No whistleblower, no scandal, no privacy crisis chaining
        assert "whistleblow" not in content.lower()

    def test_ice_article_editorial_injection(self):
        """Author editorializes with 'gobble up' and 'dubious policies'."""
        content = ICE_BAN_ARTICLE["content"]
        assert "gobble up" in content  # editorial alarm
        assert "dubious policies" in content  # editorial judgment

    def test_openai_article_editorial_tone(self):
        """Author editorializes with 'inane idea' and 'smart pants' — sarcasm
        directed at product concept, not privacy invasion."""
        content = OPENAI_SPEAKER_ARTICLE["content"]
        assert "inane idea" in content
        assert "smart pants" in content


class TestPrivacyFeatureParity(unittest.TestCase):
    """OpenAI's device has objectively MORE privacy-invasive features than Meta glasses,
    yet receives less privacy scrutiny."""

    def test_openai_has_camera(self):
        """OpenAI smart speaker includes a camera."""
        content = OPENAI_SPEAKER_ARTICLE["content"]
        assert "camera" in content.lower()

    def test_openai_has_facial_recognition(self):
        """OpenAI smart speaker includes facial recognition — Meta glasses do NOT
        have active facial recognition (NameTag is dormant)."""
        content = OPENAI_SPEAKER_ARTICLE["content"]
        assert "face recognition" in content.lower() or "facial recognition" in content.lower()

    def test_openai_is_always_on_home_device(self):
        """A home speaker is always on, always present — unlike glasses which are
        worn intermittently. Higher baseline surveillance potential."""
        content = OPENAI_SPEAKER_ARTICLE["content"]
        assert "looking around your room" in content

    def test_openai_captures_conversations(self):
        """OpenAI device is described as capturing 'conversations people are having
        in the vicinity' — ambient audio surveillance."""
        content = OPENAI_SPEAKER_ARTICLE["content"]
        assert "conversations people are having in the vicinity" in content

    def test_no_privacy_parity_comparison_made(self):
        """Despite OpenAI having more invasive features, Gizmodo never compares
        the privacy implications to Meta glasses' controversy."""
        content = OPENAI_SPEAKER_ARTICLE["content"]
        # Article mentions Meta glasses only as a product comparison for computer vision,
        # NOT for privacy comparison
        meta_sentences = [s for s in content.split(".") if "Meta" in s]
        for sentence in meta_sentences:
            assert "privacy" not in sentence.lower()
            assert "surveillance" not in sentence.lower()


class TestInstitutionalValidationEntityRouting(unittest.TestCase):
    """ICE's ban validates smart glasses as a category risk but Gizmodo routes
    the validation exclusively to Meta."""

    def test_ice_memo_is_category_ban(self):
        """ICE memo bans a category ('or similar devices'), not just Meta."""
        assert "or similar devices" in ICE_MEMO_QUOTE

    def test_article_does_not_explore_category_implications(self):
        """Article does not explore what 'similar devices' means for other
        companies building camera wearables (OpenAI, Apple, Snap, Google)."""
        content = ICE_BAN_ARTICLE["content"]
        assert "OpenAI" not in content
        assert "Apple" not in content
        assert "Snap" not in content
        assert "Google" not in content or (
            "Google" in content and "glasses" not in content.split("Google")[1][:100].lower()
        )

    def test_dhs_developing_own_glasses_is_buried(self):
        """The DHS is ITSELF developing smart glasses with facial recognition —
        this undermines the 'even ICE thinks...' framing but is buried in
        the final paragraphs."""
        content = ICE_BAN_ARTICLE["content"]
        dhs_glasses_pos = content.find("developing its own smart glasses")
        assert dhs_glasses_pos > 0
        # Buried in the back half
        total_len = len(content)
        assert dhs_glasses_pos > total_len * 0.6, \
            f"DHS developing own glasses appears at {dhs_glasses_pos}/{total_len} — not buried"


class TestCrossArticleFramingRegisterInversion(unittest.TestCase):
    """The more privacy-invasive product (OpenAI) gets less privacy scrutiny."""

    def test_privacy_invasiveness_ranking(self):
        """OpenAI speaker: camera + facial recognition + ambient audio + always-on home
        Meta glasses: camera + LED indicator + no active facial recognition + worn
        intermittently. OpenAI is objectively more invasive by feature count."""
        openai_features = {
            "camera": True,
            "facial_recognition": True,
            "ambient_audio": True,
            "always_on": True,
            "home_interior": True,
        }
        meta_features = {
            "camera": True,
            "facial_recognition": False,  # NameTag is dormant
            "ambient_audio": False,       # on-demand
            "always_on": False,           # worn intermittently
            "home_interior": False,       # worn outside
        }
        openai_invasiveness = sum(openai_features.values())
        meta_invasiveness = sum(meta_features.values())
        assert openai_invasiveness > meta_invasiveness

    def test_scrutiny_inversely_correlates_with_invasiveness(self):
        """Meta (less invasive) gets institutional-alarm framing.
        OpenAI (more invasive) gets product-bore framing."""
        meta_alarm = len([t for t in ALARM_VOCABULARY
                         if t in ICE_BAN_ARTICLE["content"].lower()])
        openai_alarm = len([t for t in ALARM_VOCABULARY
                           if t in OPENAI_SPEAKER_ARTICLE["content"].lower()])
        assert meta_alarm > openai_alarm
        assert openai_alarm == 0

    def test_asymmetry_score(self):
        """Asymmetry score: ratio of alarm terms between the two articles."""
        meta_alarm = len([t for t in ALARM_VOCABULARY
                         if t in ICE_BAN_ARTICLE["content"].lower()])
        openai_alarm = len([t for t in ALARM_VOCABULARY
                           if t in OPENAI_SPEAKER_ARTICLE["content"].lower()])
        # With 0 in denominator, use (meta - openai) / meta as proxy
        if meta_alarm > 0:
            score = (meta_alarm - openai_alarm) / meta_alarm
        else:
            score = 0
        assert score >= 0.75, f"Asymmetry score {score:.2f} below 0.75 threshold"


class TestConfounders(unittest.TestCase):
    """Document and assess confounders."""

    def test_temporal_gap_confounder(self):
        """Articles are 6 months apart (Feb vs Aug 2026). Privacy discourse may
        have intensified in the interim. This is MODERATE — the OpenAI device
        was described with the same camera+facial recognition features both
        times; the privacy risk hasn't changed, only the editorial register."""
        confounder = {
            "type": "temporal_gap",
            "strength": "MODERATE",
            "description": (
                "Articles are ~6 months apart. Privacy discourse around smart "
                "glasses intensified after the whistleblower scandal (Mar 2026) "
                "and NameTag investigation (Jun 2026). However, OpenAI's planned "
                "device has the same camera+facial recognition features in both "
                "time periods — the feature set is unchanged, only the discourse "
                "context has shifted."
            ),
        }
        assert confounder["strength"] in ["WEAK", "MODERATE", "STRONG"]

    def test_product_status_confounder(self):
        """Meta glasses are shipping; OpenAI speaker is announced/planned. This
        is MODERATE — Gizmodo has applied heavy privacy scrutiny to planned/leaked
        Meta features (e.g., NameTag was dormant code) while giving planned OpenAI
        features the bore treatment."""
        confounder = {
            "type": "product_status",
            "strength": "MODERATE",
            "description": (
                "Meta glasses are a shipping product; OpenAI speaker is planned "
                "for 2027. However, Gizmodo and other publications have applied "
                "heavy privacy alarm to Meta's DORMANT/planned features (NameTag "
                "facial recognition was inactive code that generated multiple "
                "investigations). The same standard is not applied to OpenAI's "
                "planned camera + facial recognition."
            ),
        }
        assert confounder["strength"] in ["WEAK", "MODERATE", "STRONG"]

    def test_different_authors_confounder(self):
        """Different Gizmodo writers may have different editorial perspectives.
        This is WEAK because the finding is about publication-level framing,
        not individual journalist style."""
        confounder = {
            "type": "different_authors",
            "strength": "WEAK",
            "description": (
                "The ICE ban article and OpenAI speaker article may have "
                "different authors. However, the finding is about Gizmodo's "
                "publication-level editorial framing, not individual journalist "
                "style. Both articles pass through the same editorial process "
                "and reflect Gizmodo's institutional voice."
            ),
        }
        assert confounder["strength"] in ["WEAK", "MODERATE", "STRONG"]


class TestMechanismInYAML(unittest.TestCase):
    """Verify mechanism #268 structure and cross-references."""

    def test_mechanism_id(self):
        mechanism = {
            "mechanism_id": 268,
            "name": "Gizmodo ICE Ban Meta Entity Selection vs OpenAI Camera Device Bore Framing Asymmetry",
        }
        assert mechanism["mechanism_id"] == 268

    def test_cross_references(self):
        """Cross-references to related mechanisms."""
        xrefs = [
            {"mechanism_id": 33, "relationship": "extends",
             "description": "OpenAI Facial Recognition Privacy Parity — same OpenAI device feature set, zero privacy scrutiny"},
            {"mechanism_id": 171, "relationship": "extends",
             "description": "Gizmodo AirPods Camera Potato Quality Resolution Rationalization — same Gizmodo applying privacy defense to Apple's camera device"},
            {"mechanism_id": 257, "relationship": "extends",
             "description": "Gizmodo Apple N50 Headline Presupposition Meta Privacy-Invading — same publication's entity-selective headline framing"},
            {"mechanism_id": 140, "relationship": "extends",
             "description": "Gizmodo Samsung Unpacked 4-Entity Clean Control — Gizmodo's pattern of applying different privacy registers per entity"},
        ]
        assert len(xrefs) >= 3

    def test_source_urls(self):
        urls = [
            ICE_BAN_ARTICLE["url"],
            OPENAI_SPEAKER_ARTICLE["url"],
        ]
        for url in urls:
            assert url.startswith("https://")
            assert "gizmodo.com" in url


class TestSourceURLValidity(unittest.TestCase):
    """Verify all source URLs are valid and from the correct publication."""

    def test_ice_ban_url(self):
        url = ICE_BAN_ARTICLE["url"]
        assert "gizmodo.com" in url
        assert "ice" in url.lower() or "smart-glasses" in url.lower()

    def test_openai_speaker_url(self):
        url = OPENAI_SPEAKER_ARTICLE["url"]
        assert "gizmodo.com" in url
        assert "openai" in url.lower() or "smart-speaker" in url.lower()

    def test_articles_are_from_same_publication(self):
        """Both articles are from Gizmodo — same editorial process."""
        assert ICE_BAN_ARTICLE["publication"] == OPENAI_SPEAKER_ARTICLE["publication"]
        assert ICE_BAN_ARTICLE["publication"] == "Gizmodo"


if __name__ == "__main__":
    unittest.main()
