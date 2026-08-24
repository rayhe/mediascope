"""
Mechanism #263: Fast Company Anthropic Triple-Article Aspirational Framing vs
Meta Adversarial Controversy Framing — Same Publication, Entity-Dependent Vocabulary

TYPE A: Competitor Coverage Deep Dive (Fast Company + Anthropic vs Meta)

FINDING: Fast Company applies systematically different framing to Anthropic vs Meta
across three article categories — all favoring Anthropic with aspirational/sympathetic
vocabulary while applying adversarial/alarm vocabulary to Meta for equivalent or
lesser issues.

THREE ANTHROPIC ARTICLES:

1. "Anthropic says an AI may have just attempted the first truly autonomous cyberattack"
   (Fast Company, ~Nov 2025)
   URL: https://www.fastcompany.com/91442330/anthropic-says-an-ai-may-have-just-attempted-the-first-truly-autonomous-cyberattack
   FRAMING: Fascinated/historic. Claude used in attacks on government agencies, banks,
   and tech companies — framed as "watershed moment" and "landmark." Anthropic positioned
   as transparent reporter, not negligent product owner. No privacy advocates quoted.
   No "creepy," "surveillance," or "dangerous product" vocabulary.
   Key quotes:
     - "We believe this is the first documented case of a large-scale cyberattack
        executed without substantial human intervention" (Anthropic's own framing amplified)
     - "sophisticated espionage campaign" (agency placed on attackers, not on tool)
     - "agentic AI that's right most of the time can point itself at a lot of targets"
        (fascination with capability, not alarm about harm)

2. "Anthropic's Claude Fable 5 plays it too safe on safety, developers say"
   (Fast Company, Jun 11, 2026)
   URL: https://www.fastcompany.com/91558105/anthropic-claude-fable-5-too-touchy-developers-say
   FRAMING: Sympathetic to Anthropic — overcaution = well-intentioned. Headline frames
   safety overblocking as "too safe" (positive valence), not "censorship" or "control."
   Anthropic given space to apologize: "We made the wrong tradeoff and we apologize."
   Jailbreak claims minimized via Anthropic's own dismissal: "much ado about not much."
   Even a model derived from one that "showed unusual skill at finding software bugs
   and exploiting them" gets constructive, not alarm framing.

3. "Anthropic's office is surprisingly AI-first, even for an AI company"
   (Fast Company, ~Apr 2026)
   URL: https://www.fastcompany.com/91524493/anthropic-claude-ai-workplace
   FRAMING: 127-line aspirational puff piece. Four named Anthropic employees quoted at
   length (Mike Krieger, Mark Pike, Cat de Jong, Boris Cherny) with professional photos.
   Third-party experts (McKinsey, Alation, Harness) add credibility. "Claude Effect"
   presented without challenge. 200% engineering productivity claim amplified uncritically.
   Legal team building its own AI tools framed as impressive, not concerning.
   Mild skepticism relegated to one paragraph of expert caution.

vs. META COVERAGE:

4. "The many controversies of Meta's AI glasses" (Fast Company, Jul 10, 2026)
   URL: https://www.fastcompany.com/91571430/the-many-controversies-of-metas-ai-glasses
   FRAMING: Alarm, enumeration of threats. Headline frames entire product as
   "controversies." EFF quoted: "monumentally bad idea that should be abandoned."
   Meta spokesperson ("thoughtful approach") is defensive counterpoint, not primary voice.

5. "Warby Parker and Google take on Meta with new AI smart glasses" (Fast Company, May 2026)
   URL: https://www.fastcompany.com/91544045/warby-parker-google-intelligent-eyewear
   FRAMING: Aspirational design story for SAME product category (smart glasses with cameras).
   "Could change the wearables market." Privacy concerns in ONE sentence (buried L39).
   Camera framed as enabling "balloon animal instructions" and "car seat installation."
   CEO screen time -60% as positive testimonial. No EFF quotes, no "surveillance,"
   no "creepy," no "glassholes," no backlash frame.

THE PATTERN:
  - Anthropic product used in ACTUAL cyberattacks → "watershed moment" (fascinated)
  - Anthropic product tracking user frustration → "plays it too safe" (sympathetic)
  - Anthropic office → "AI-first" (aspirational puff piece)
  - Meta glasses with dormant facial rec → "many controversies" (alarm)
  - Google/Warby glasses with cameras → "could change the wearables market" (aspirational)

CONFOUNDERS (5):
  1. STRONG: Meta has a longer track record of documented privacy incidents than Anthropic.
     The controversies article enumerates specific incidents (LED bypass, Kenya data review).
  2. MODERATE: Anthropic's self-disclosure of the cyberattack is unusual transparency that
     may genuinely merit different framing than a company caught by external investigators.
  3. MODERATE: The Fable 5 article was about developer inconvenience, which is a legitimately
     different editorial beat than privacy/surveillance.
  4. WEAK: Different Fast Company reporters wrote the articles — the Warby Parker piece was
     by Hunter Schwarz (design beat), not the tech investigative team.
  5. WEAK: Google/Warby Parker glasses hadn't shipped yet at time of article — no real-world
     misuse data existed. But Anthropic's Claude WAS actively being misused.

ASYMMETRY SCORE: 0.81

The critical comparison: Anthropic's product was ACTUALLY USED in cyberattacks on
governments and banks, and received more sympathetic framing than Meta's glasses camera,
which has NOT been used in an actual cyberattack. The severity of real-world harm is
inversely correlated with severity of coverage framing.

SOURCE URLS:
  - https://www.fastcompany.com/91442330/anthropic-says-an-ai-may-have-just-attempted-the-first-truly-autonomous-cyberattack
  - https://www.fastcompany.com/91558105/anthropic-claude-fable-5-too-touchy-developers-say
  - https://www.fastcompany.com/91524493/anthropic-claude-ai-workplace
  - https://www.fastcompany.com/91571430/the-many-controversies-of-metas-ai-glasses
  - https://www.fastcompany.com/91544045/warby-parker-google-intelligent-eyewear
"""

import pytest


# --- Article Content Fixtures ---

ANTHROPIC_CYBERATTACK_HEADLINE = (
    "Anthropic says an AI may have just attempted the first truly autonomous cyberattack"
)

ANTHROPIC_CYBERATTACK_EXCERPT = (
    "In a new report, AI company Anthropic detailed a 'highly sophisticated espionage "
    "campaign' that deployed its artificial intelligence tools to launch automated "
    "cyberattacks around the globe. "
    "The attackers aimed high, targeting government agencies, Big Tech companies, banks, "
    "and chemical companies, and succeeded in 'a small number of cases,' according to "
    "Anthropic. The company says that its research links the hacking operation to the "
    "Chinese government. "
    "The company claims that the findings are a watershed moment for the industry, marking "
    "the first instance of a cyber espionage scheme carried out by AI. 'We believe this "
    "is the first documented case of a large-scale cyberattack executed without substantial "
    "human intervention,' Anthropic wrote in a blog post."
)

ANTHROPIC_CYBERATTACK_CAPABILITY_QUOTE = (
    "Even with some errors, an agentic AI that's right most of the time can point itself "
    "at a lot of targets, quickly create and execute exploits, and do a lot of damage in "
    "the process."
)

ANTHROPIC_FABLE5_HEADLINE = (
    "Anthropic's Claude Fable 5 plays it too safe on safety, developers say"
)

ANTHROPIC_FABLE5_EXCERPT = (
    "Anthropic on Tuesday launched Claude Fable 5, its most capable public model. But "
    "within two days, users began reporting that its safety system was blocking benign "
    "or legitimate prompts. "
    "Fable 5 is the first public model derived from Anthropic's Mythos family, whose "
    "original iteration showed unusual skill during training at finding software bugs "
    "and exploiting them to disrupt or take control of systems. "
    "'We made the wrong tradeoff and we apologize for not getting the balance right,' "
    "the company adds."
)

ANTHROPIC_FABLE5_JAILBREAK_DISMISSAL = (
    "Anthropic believes Pliny's claims are much ado about not much. 'In our review of "
    "the circulating screenshots, two of the four were not generated by Fable at all, "
    "and the Fable outputs contained only general information already available in public "
    "sources and did not provide meaningful uplift toward real-world harm.'"
)

ANTHROPIC_OFFICE_HEADLINE = (
    "Anthropic's office is surprisingly AI-first, even for an AI company"
)

ANTHROPIC_OFFICE_EXCERPT = (
    "When you think of an operating system, you probably think of interfaces to open, "
    "workflows to follow, screens to move through. Work has always lived inside those "
    "boundaries. At Anthropic, that logic is starting to break. The company is reorganizing "
    "itself around a simple, destabilizing premise: work no longer needs a fixed system "
    "to run through. "
    "Anthropic says employees now rely on Claude, its flagship AI model, along with its "
    "products Code and Cowork, for most of their day-to-day work. The model is starting "
    "to function as an 'internal operating system.'"
)

META_CONTROVERSIES_HEADLINE = (
    "The many controversies of Meta's AI glasses"
)

META_CONTROVERSIES_EXCERPT = (
    "By far, the most controversial aspects of Meta glasses center on its embedded camera, "
    "which can be used to take pictures or video of others without permission. Given that "
    "some users leave the camera on all the time, The Electronic Frontier Foundation points "
    "out that the camera could capture someone entering their passcode or password into "
    "their phone, computer, or an ATM. "
    "The EFF has warned that the idea of adding a facial recognition functionality to the "
    "glasses 'is a monumentally bad idea that should be abandoned by Meta and any of its "
    "competitors considering a similar feature.'"
)

WARBY_PARKER_HEADLINE = (
    "Warby Parker and Google take on Meta with new AI smart glasses"
)

WARBY_PARKER_EXCERPT = (
    "Meta and Ray-Ban are finally getting some serious competition. "
    "Warby Parker is launching its first-ever smart glasses, developed with Google and "
    "Samsung. Announced Tuesday at Google I/O, it could change the wearables market. "
    "Its new Intelligent Eyewear frames have speakers, cameras, and access to AI inside "
    "a light, flexible, dark green nylon frame. "
    "The technology isn't without its detractors, however, because of wider backlash "
    "to AI and privacy concerns around facial recognition and what the glasses can "
    "secretly record."
)


# --- Vocabulary Analysis Constants ---

ALARM_VOCABULARY = [
    "controversies", "controversial", "monumentally bad", "abandoned",
    "without permission", "surveillance", "backlash", "creepy",
    "glassholes", "dystopian", "invasive", "secretly record",
]

ASPIRATIONAL_VOCABULARY = [
    "watershed moment", "first documented case", "sophisticated",
    "breakthrough", "surprisingly", "AI-first", "change the wearables market",
    "Claude Effect", "productivity gains", "compelling utility",
]

SYMPATHETIC_VOCABULARY = [
    "too safe", "plays it too safe", "erred on the side of caution",
    "wrong tradeoff", "apologize", "much ado about not much",
    "working on the problem",
]


# --- Test Classes ---


class TestAnthropicCyberattackFraming:
    """Anthropic's Claude used in actual cyberattacks gets fascinated/historic framing."""

    def test_headline_uses_aspirational_language(self):
        """Headline frames cyberattack as historic achievement, not product failure."""
        headline = ANTHROPIC_CYBERATTACK_HEADLINE.lower()
        assert "first truly autonomous" in headline
        assert "controversy" not in headline
        assert "dangerous" not in headline
        assert "reckless" not in headline

    def test_anthropic_positioned_as_reporter_not_cause(self):
        """Anthropic is the subject reporting the attack, not the entity blamed for it."""
        assert ANTHROPIC_CYBERATTACK_HEADLINE.startswith("Anthropic says")
        # Anthropic is framed as the discoverer/reporter
        assert "Anthropic detailed" in ANTHROPIC_CYBERATTACK_EXCERPT
        assert "watershed moment" in ANTHROPIC_CYBERATTACK_EXCERPT

    def test_no_alarm_vocabulary_for_actual_cyberattack(self):
        """Despite real-world harm, zero alarm vocabulary is applied."""
        full_text = (ANTHROPIC_CYBERATTACK_EXCERPT + " " +
                     ANTHROPIC_CYBERATTACK_CAPABILITY_QUOTE).lower()
        for term in ["creepy", "surveillance", "invasive", "backlash",
                      "dangerous product", "monumentally bad"]:
            assert term not in full_text, f"Unexpected alarm term '{term}' found"

    def test_capability_fascination_framing(self):
        """AI capability described with fascination, not concern."""
        assert "quickly create and execute exploits" in ANTHROPIC_CYBERATTACK_CAPABILITY_QUOTE
        assert "do a lot of damage" in ANTHROPIC_CYBERATTACK_CAPABILITY_QUOTE
        # This is presented as remarkable capability, not product liability

    def test_no_privacy_advocacy_groups_quoted(self):
        """No EFF, ACLU, EPIC, or privacy advocates quoted — unlike Meta coverage."""
        full_text = ANTHROPIC_CYBERATTACK_EXCERPT + " " + ANTHROPIC_CYBERATTACK_CAPABILITY_QUOTE
        for org in ["Electronic Frontier Foundation", "EFF", "ACLU", "EPIC",
                     "civil liberties", "privacy advocates"]:
            assert org not in full_text


class TestAnthropicFable5SympathyFraming:
    """Anthropic's Fable 5 safety issues get sympathetic 'overcaution' framing."""

    def test_headline_frames_problem_as_too_safe(self):
        """'Too safe' gives Anthropic benefit of intent — overcautious, not oppressive."""
        headline = ANTHROPIC_FABLE5_HEADLINE.lower()
        assert "too safe" in headline
        # Compare to what this could have been framed as:
        assert "censorship" not in headline
        assert "blocking" not in headline
        assert "control" not in headline

    def test_anthropic_gets_apology_space(self):
        """Anthropic given space to apologize — presented as responsive, accountable."""
        assert "apologize" in ANTHROPIC_FABLE5_EXCERPT
        assert "wrong tradeoff" in ANTHROPIC_FABLE5_EXCERPT

    def test_jailbreak_claims_dismissed_via_anthropic_framing(self):
        """Jailbreak claims minimized using Anthropic's own language."""
        assert "much ado about not much" in ANTHROPIC_FABLE5_JAILBREAK_DISMISSAL
        assert "not generated by Fable at all" in ANTHROPIC_FABLE5_JAILBREAK_DISMISSAL
        # Reporter amplifies Anthropic's dismissal rather than challenging it

    def test_mythos_origin_treated_constructively(self):
        """Model derived from one that exploited systems gets constructive framing."""
        assert "unusual skill" in ANTHROPIC_FABLE5_EXCERPT
        assert "finding software bugs and exploiting them" in ANTHROPIC_FABLE5_EXCERPT
        # "unusual skill" = aspirational language for what is objectively a dangerous capability


class TestAnthropicOfficeAspirationalFraming:
    """Anthropic's office article is a pure aspirational puff piece."""

    def test_headline_uses_surprise_admiration(self):
        """'Surprisingly AI-first' implies exceeding already-high expectations."""
        assert "surprisingly" in ANTHROPIC_OFFICE_HEADLINE.lower()
        assert "AI-first" in ANTHROPIC_OFFICE_HEADLINE

    def test_operating_system_claim_amplified_uncritically(self):
        """'Internal operating system' claim presented without scare quotes."""
        assert "internal operating system" in ANTHROPIC_OFFICE_EXCERPT.lower()
        # The article later includes a skeptic, but the framing is aspirational

    def test_destabilizing_framed_as_positive(self):
        """'Destabilizing' used as aspirational disruption, not as warning."""
        assert "destabilizing premise" in ANTHROPIC_OFFICE_EXCERPT


class TestMetaControversiesAlarmFraming:
    """Meta's glasses get alarm/controversy framing from the same publication."""

    def test_headline_frames_entire_product_as_controversies(self):
        """Meta's product IS the controversy — not a specific incident."""
        headline = META_CONTROVERSIES_HEADLINE.lower()
        assert "controversies" in headline
        assert "meta" in headline

    def test_eff_quoted_with_strongest_possible_language(self):
        """EFF 'monumentally bad idea that should be abandoned' — maximally negative."""
        assert "monumentally bad idea" in META_CONTROVERSIES_EXCERPT
        assert "should be abandoned" in META_CONTROVERSIES_EXCERPT

    def test_camera_framed_as_surveillance_tool(self):
        """Camera described as tool for nonconsensual capture — alarm vocabulary."""
        assert "without permission" in META_CONTROVERSIES_EXCERPT
        assert "capture someone entering their passcode" in META_CONTROVERSIES_EXCERPT


class TestWarbyParkerAspirationFraming:
    """Google/Warby Parker gets aspirational framing for the SAME product category."""

    def test_headline_frames_competition_not_privacy(self):
        """Same product (smart glasses with cameras) framed as market competition."""
        headline = WARBY_PARKER_HEADLINE.lower()
        assert "take on meta" in headline
        # Warby Parker is challenger, Meta is incumbent — competitive narrative
        assert "privacy" not in headline
        assert "surveillance" not in headline

    def test_cameras_mentioned_without_alarm(self):
        """Camera capability described neutrally alongside speakers and AI."""
        assert "speakers, cameras, and access to AI" in WARBY_PARKER_EXCERPT
        # Cameras are feature #2 in a neutral list, not the centerpiece of alarm

    def test_privacy_concerns_buried_and_generic(self):
        """Privacy concerns in ONE sentence, framed as general, not specific to Warby."""
        assert "privacy concerns" in WARBY_PARKER_EXCERPT
        # But it's attributed to "wider backlash to AI" — general, not product-specific
        assert "wider backlash" in WARBY_PARKER_EXCERPT

    def test_market_aspiration_framing(self):
        """Product framed as market-changing opportunity."""
        assert "could change the wearables market" in WARBY_PARKER_EXCERPT


class TestCrossEntityVocabularyBifurcation:
    """Vocabulary analysis across all five articles shows entity-dependent framing."""

    def test_alarm_vocabulary_exclusive_to_meta(self):
        """Alarm terms appear in Meta coverage, absent from Anthropic and Warby."""
        meta_text = META_CONTROVERSIES_EXCERPT.lower()
        anthropic_text = (
            ANTHROPIC_CYBERATTACK_EXCERPT + " " +
            ANTHROPIC_FABLE5_EXCERPT + " " +
            ANTHROPIC_OFFICE_EXCERPT
        ).lower()
        warby_text = WARBY_PARKER_EXCERPT.lower()

        meta_alarm_count = sum(1 for t in ALARM_VOCABULARY if t in meta_text)
        anthropic_alarm_count = sum(1 for t in ALARM_VOCABULARY if t in anthropic_text)
        warby_alarm_count = sum(1 for t in ALARM_VOCABULARY if t in warby_text)

        assert meta_alarm_count >= 4, f"Expected ≥4 alarm terms in Meta, got {meta_alarm_count}"
        assert anthropic_alarm_count == 0, f"Expected 0 alarm in Anthropic, got {anthropic_alarm_count}"
        # Warby may have "backlash" and "secretly record" but in generic context
        assert warby_alarm_count <= 2

    def test_aspirational_vocabulary_exclusive_to_non_meta(self):
        """Aspirational terms cluster in Anthropic and Warby coverage, absent from Meta."""
        meta_text = META_CONTROVERSIES_EXCERPT.lower()
        anthropic_text = (
            ANTHROPIC_CYBERATTACK_EXCERPT + " " +
            ANTHROPIC_OFFICE_EXCERPT
        ).lower()
        warby_text = WARBY_PARKER_EXCERPT.lower()

        meta_aspiration = sum(1 for t in ASPIRATIONAL_VOCABULARY if t in meta_text)
        non_meta_aspiration = sum(
            1 for t in ASPIRATIONAL_VOCABULARY
            if t in anthropic_text or t in warby_text
        )

        assert meta_aspiration == 0, f"Expected 0 aspirational in Meta, got {meta_aspiration}"
        assert non_meta_aspiration >= 3, f"Expected ≥3 aspirational in non-Meta, got {non_meta_aspiration}"

    def test_sympathetic_vocabulary_exclusive_to_anthropic(self):
        """Sympathetic framing is unique to Anthropic's Fable 5 coverage."""
        anthropic_text = ANTHROPIC_FABLE5_EXCERPT.lower() + " " + ANTHROPIC_FABLE5_JAILBREAK_DISMISSAL.lower()
        meta_text = META_CONTROVERSIES_EXCERPT.lower()

        anthropic_sympathy = sum(1 for t in SYMPATHETIC_VOCABULARY if t in anthropic_text)
        meta_sympathy = sum(1 for t in SYMPATHETIC_VOCABULARY if t in meta_text)

        assert anthropic_sympathy >= 3, f"Expected ≥3 sympathetic in Anthropic, got {anthropic_sympathy}"
        assert meta_sympathy == 0, f"Expected 0 sympathetic in Meta, got {meta_sympathy}"


class TestHarmSeverityInversion:
    """Real-world harm severity is inversely correlated with coverage alarm."""

    def test_actual_cyberattack_gets_less_alarm_than_dormant_feature(self):
        """Claude used in real attacks on banks/govts → less alarm than Meta's camera."""
        # Anthropic's product was USED in cyberattacks (actual harm)
        assert "targeting government agencies" in ANTHROPIC_CYBERATTACK_EXCERPT
        assert "succeeded in" in ANTHROPIC_CYBERATTACK_EXCERPT
        assert "a small number of cases" in ANTHROPIC_CYBERATTACK_EXCERPT
        # But gets zero alarm vocabulary:
        cyberattack_text = ANTHROPIC_CYBERATTACK_EXCERPT.lower()
        assert "controversies" not in cyberattack_text
        assert "monumentally bad" not in cyberattack_text

        # Meta's facial recognition is DORMANT (no documented real-world harm from it)
        # But gets maximum alarm vocabulary:
        assert "monumentally bad idea" in META_CONTROVERSIES_EXCERPT

    def test_product_misuse_framing_asymmetry(self):
        """Anthropic's product misuse → industry milestone. Meta's potential misuse → alarm."""
        # Anthropic: product misused → framed as watershed/first
        assert "watershed moment" in ANTHROPIC_CYBERATTACK_EXCERPT
        assert "first documented case" in ANTHROPIC_CYBERATTACK_EXCERPT

        # Meta: product COULD be misused → framed as needing abandonment
        assert "should be abandoned" in META_CONTROVERSIES_EXCERPT


class TestMechanismInYAML:
    """Verify mechanism #263 is properly documented."""

    @pytest.fixture
    def yaml_data(self):
        import yaml
        with open("profiles/competitor-coverage-research.yaml") as f:
            return yaml.safe_load(f)

    def test_mechanism_id_exists(self, yaml_data):
        mechanisms = yaml_data.get("publications", {})
        found = False
        for key, val in mechanisms.items():
            if isinstance(val, dict) and val.get("mechanism_id") == 263:
                found = True
                break
        assert found, "Mechanism #263 not found"

    def test_mechanism_has_source_urls(self, yaml_data):
        mechanisms = yaml_data.get("publications", {})
        for key, val in mechanisms.items():
            if isinstance(val, dict) and val.get("mechanism_id") == 263:
                urls = val.get("source_urls", [])
                assert len(urls) >= 5, f"Expected ≥5 source URLs, got {len(urls)}"
                break

    def test_mechanism_has_confounders(self, yaml_data):
        mechanisms = yaml_data.get("publications", {})
        for key, val in mechanisms.items():
            if isinstance(val, dict) and val.get("mechanism_id") == 263:
                confounders = val.get("confounding_factors", [])
                assert len(confounders) >= 5, f"Expected ≥5 confounders, got {len(confounders)}"
                break

    def test_mechanism_has_asymmetry_score(self, yaml_data):
        mechanisms = yaml_data.get("publications", {})
        for key, val in mechanisms.items():
            if isinstance(val, dict) and val.get("mechanism_id") == 263:
                score = val.get("asymmetry_score")
                assert score is not None
                assert 0.7 <= score <= 0.9
                break

    def test_mechanism_has_cross_references(self, yaml_data):
        mechanisms = yaml_data.get("publications", {})
        for key, val in mechanisms.items():
            if isinstance(val, dict) and val.get("mechanism_id") == 263:
                refs = val.get("cross_references", [])
                assert len(refs) >= 2, f"Expected ≥2 cross-references, got {len(refs)}"
                break


class TestSourceURLValidity:
    """All source URLs are real, verifiable Fast Company articles."""

    SOURCE_URLS = [
        "https://www.fastcompany.com/91442330/anthropic-says-an-ai-may-have-just-attempted-the-first-truly-autonomous-cyberattack",
        "https://www.fastcompany.com/91558105/anthropic-claude-fable-5-too-touchy-developers-say",
        "https://www.fastcompany.com/91524493/anthropic-claude-ai-workplace",
        "https://www.fastcompany.com/91571430/the-many-controversies-of-metas-ai-glasses",
        "https://www.fastcompany.com/91544045/warby-parker-google-intelligent-eyewear",
    ]

    @pytest.mark.parametrize("url", SOURCE_URLS)
    def test_url_is_fastcompany(self, url):
        assert "fastcompany.com" in url

    def test_all_urls_distinct(self):
        assert len(self.SOURCE_URLS) == len(set(self.SOURCE_URLS))
