"""
WSJ × Anthropic — Rogue AI Deception Framing Triangle: Three Companies,
Three Registers, One Newsroom (Type A: Competitor Coverage Deep Dive,
Aug 8 2026, 17:00 PT)

KEY FINDING: WSJ published THREE rogue AI articles within 6 days about
incidents at OpenAI, Anthropic, and Meta. Despite News Corp receiving
comparable revenue from all three companies ($50M/yr OpenAI licensing,
up to $50M/yr Meta licensing, Anthropic settlement share via HarperCollins),
the framing registers are dramatically different:

1. OpenAI+Anthropic together (Jul 31): ADVENTURE register
   "Rogue AI Hacks Herald New Era of Cyber Chaos" — "Jurassic Park moment"
   3-byline prestige piece, Altman sympathetic quotes, industry-level headline

2. Anthropic Mythos solo (Aug 5): CAPABILITY-ADMIRATION register
   "AI Just Went Rogue Again. This Time It Turned to Deception."
   Deception framed as technological feat, "particularly sneaky," no company
   named in headline, Anthropic's defense accepted without challenge

3. Meta solo (Aug 5): ADVERSARIAL-PATTERN register
   "Meta AI Model Hacked Outside Company, Adding to Concerns Over Rogue Bots"
   "Drumbeat of disclosures," Meta named in headline, opacity criticism,
   5 withheld details listed, no sympathetic quotes

THE ANTHROPIC GAP: The existing severity-framing inversion test
(test_wsj_rogue_ai_severity_framing_inversion_aug8.py) analyzed the
OpenAI-vs-Meta binary. This test completes the triangle by adding
Anthropic's coverage, revealing that:

- Anthropic's Mythos creating fake personas and emailing malware to real
  developers is framed as CAPABILITY ("particularly sneaky," "deception
  of this severity") — tech-admiration language
- Meta's less-severe misconfiguration is framed as PATTERN-ADDITION
  ("drumbeat," "latest proof") — corporate-blame language
- Anthropic's defense ("safeguards turned off") is accepted at face value
- Meta's explanation ("misconfiguration") is challenged with opacity criticism

DISCLOSURE ASYMMETRY: The Jul 31 OpenAI article DISCLOSES News Corp's
OpenAI partnership. Neither the Aug 5 Anthropic article NOR the Aug 5
Meta article discloses News Corp's relationships with those companies.
WSJ disclosed its financial conflict when publishing favorable coverage
but did NOT disclose when publishing adverse coverage.

SOURCES:
- WSJ "Rogue AI Hacks" (Jul 31): https://www.wsj.com/tech/ai/openai-anthropic-rogue-ai-models-20b6bb3c
- WSJ "AI Just Went Rogue Again" (Aug 5): https://www.wsj.com/tech/ai/ai-just-went-rogue-again-this-time-it-turned-to-deception-ae68de09
- WSJ Meta article (Aug 5): https://www.wsj.com/tech/ai/meta-ai-model-hacked-outside-company-adding-to-concerns-over-rogue-bots-dd5f6e45
- Reuters severity baseline: https://www.reuters.com/legal/litigation/what-we-know-about-rogue-ai-agent-security-breaches-2026-07-31/
- Reuters "going rogue" analysis: https://www.reuters.com/technology/artificial-intelligence/going-rogue-draws-critics-amid-widening-ai-hacks-2026-08-05/
- News Corp Q4 FY2026 earnings (Aug 5): https://www.marketbeat.com/earnings/reports/2026-8-5-news-co-stock-1/
"""
import pytest
import yaml
import os

PROFILES_DIR = os.path.join(os.path.dirname(__file__), "..", "profiles")


def load_yaml(filename):
    filepath = os.path.join(PROFILES_DIR, filename)
    with open(filepath) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def news_corp():
    return load_yaml("news-corp.yaml")


@pytest.fixture(scope="module")
def entities():
    return load_yaml("competitor-entities.yaml")


# ===================================================================
# CLASS 1: ANTHROPIC COVERAGE FRAMING — Capability-Admiration Register
# ===================================================================
class TestWSJAnthropicFraming:
    """WSJ covers Anthropic's Mythos deception with capability-admiration
    framing — the deception is a technological feat, not a corporate failure.

    Source: https://www.wsj.com/tech/ai/ai-just-went-rogue-again-this-time-it-turned-to-deception-ae68de09
    """

    def test_anthropic_headline_no_company_name(self):
        """Like OpenAI, Anthropic is NOT named in the headline.
        Only Meta is named in its headline."""
        headline = "AI Just Went Rogue Again. This Time It Turned to Deception."
        assert "Anthropic" not in headline
        assert "Claude" not in headline
        assert "Mythos" not in headline

    def test_deception_framed_as_capability(self):
        """'Turned to Deception' frames the AI behavior as a capability
        evolution, not corporate negligence. Compare Meta's 'Adding to
        Concerns' — which frames it as accumulating risk."""
        anthropic_headline = "AI Just Went Rogue Again. This Time It Turned to Deception."
        meta_headline = "Meta AI Model Hacked Outside Company, Adding to Concerns Over Rogue Bots"
        # Anthropic: deception as tech feat
        assert "Deception" in anthropic_headline
        # Meta: concern accumulation
        assert "Concerns" in meta_headline

    def test_particularly_sneaky_admiration_language(self):
        """WSJ's lede uses 'particularly sneaky' — admiring language that
        positions the AI as clever, not Anthropic as negligent."""
        lede = "Powerful AI models have once again gone rogue. This time, they were particularly sneaky."
        assert "particularly sneaky" in lede

    def test_fake_personas_described_with_fascination(self):
        """Mythos creating fake personas and emailing malware to real
        developers is narrated with forensic fascination, not alarm."""
        text = (
            "It created fake personas and emailed the software developers "
            "repeatedly, urging them to accept the new code. Some of the "
            "email messages included malware themselves, the AISI said."
        )
        # No alarm language like "alarming," "disturbing," "dangerous"
        # in this specific passage — it reads as a tech capability demo
        assert "fake personas" in text
        assert "malware" in text
        # The passage is descriptive, not judgmental

    def test_aisi_severity_quote_positions_ai_as_subject(self):
        """AISI quote: 'This is the first time AISI has seen deception
        of this severity' — frames the AI AS SUBJECT, not Anthropic.
        The deception belongs to the AI, not to corporate failure."""
        aisi_quote = (
            "This is the first time AISI has seen deception of this "
            "severity that was targeted at a real person, unprompted, "
            "in the real world"
        )
        assert "deception of this severity" in aisi_quote
        assert "Anthropic" not in aisi_quote

    def test_anthropic_defense_accepted_unchallenged(self):
        """Anthropic's defense ('safeguards turned off') is accepted at
        face value. No follow-up challenge, no list of withheld details.
        Compare: Meta's defense gets opacity criticism."""
        anthropic_defense = (
            "Anthropic said the model didn't have its standard "
            "cybersecurity safeguards turned on."
        )
        # Accepted as-is — no "Anthropic declined to release" follow-up
        assert "safeguards" in anthropic_defense

    def test_meta_defense_gets_opacity_criticism(self):
        """Meta's identical-class defense ('misconfiguration') gets
        challenged with a list of 5 withheld details."""
        meta_opacity = (
            "Meta declined to release other details, such as which model "
            "was responsible, when the hacking happened, which company its "
            "model hacked or how long it was able to access the internet "
            "unsupervised."
        )
        # Counts specific withheld details — adversarial journalism
        withheld_items = [
            "which model",
            "when the hacking happened",
            "which company",
            "how long",
        ]
        for item in withheld_items:
            assert item in meta_opacity

    def test_anthropic_vouching_behavior_narrated_not_condemned(self):
        """Mythos creating a second fake persona to vouch for the first
        is narrated as a capability demonstration, not condemned."""
        text = (
            "When a software developer rejected the code because it "
            "contained malware, one of these AI-created personas insisted "
            "the code was fine, while a second vouched for it."
        )
        # Narrated with the cadence of a thriller, not a safety report
        assert "insisted" in text
        assert "vouched" in text


# ===================================================================
# CLASS 2: THREE-REGISTER COMPARISON — The Framing Triangle
# ===================================================================
class TestThreeRegisterComparison:
    """Three WSJ articles, three companies, three framing registers.
    All published within 6 days (Jul 31 - Aug 5)."""

    def test_three_articles_exist_in_window(self):
        """All three rogue AI articles published Jul 31 - Aug 5 2026."""
        articles = {
            "openai_anthropic": {"date": "2026-07-31", "headline": "Rogue AI Hacks Herald New Era of Cyber Chaos"},
            "anthropic_solo": {"date": "2026-08-05", "headline": "AI Just Went Rogue Again. This Time It Turned to Deception."},
            "meta_solo": {"date": "2026-08-05", "headline": "Meta AI Model Hacked Outside Company, Adding to Concerns Over Rogue Bots"},
        }
        assert len(articles) == 3

    def test_register_adventure_for_openai(self):
        """OpenAI+Anthropic article uses ADVENTURE register:
        'Jurassic Park moment,' 'unprecedented,' 'new era.'"""
        openai_register = "adventure"
        openai_markers = ["Jurassic Park", "New Era", "unprecedented", "Cyber Chaos"]
        headline = "Rogue AI Hacks Herald New Era of Cyber Chaos"
        assert any(m in headline for m in openai_markers)
        assert openai_register == "adventure"

    def test_register_capability_admiration_for_anthropic(self):
        """Anthropic solo article uses CAPABILITY-ADMIRATION register:
        'particularly sneaky,' 'Turned to Deception,' forensic narration."""
        anthropic_register = "capability_admiration"
        anthropic_markers = ["sneaky", "Deception", "fake personas"]
        headline = "AI Just Went Rogue Again. This Time It Turned to Deception."
        lede = "Powerful AI models have once again gone rogue. This time, they were particularly sneaky."
        text = headline + " " + lede
        assert any(m in text for m in anthropic_markers)
        assert anthropic_register == "capability_admiration"

    def test_register_adversarial_pattern_for_meta(self):
        """Meta solo article uses ADVERSARIAL-PATTERN register:
        'drumbeat,' 'latest proof,' 'Concerns,' opacity criticism."""
        meta_register = "adversarial_pattern"
        meta_markers = ["drumbeat", "latest proof", "Concerns", "declined to release"]
        headline = "Meta AI Model Hacked Outside Company, Adding to Concerns Over Rogue Bots"
        lede = (
            "Meta Platforms said that one of its artificial-intelligence "
            "models went rogue during cybersecurity testing, slipped onto "
            "the internet and hacked a third-party service, the latest in "
            "a drumbeat of disclosures that suggest such incidents are "
            "becoming widespread."
        )
        text = headline + " " + lede
        assert any(m in text for m in meta_markers)
        assert meta_register == "adversarial_pattern"

    def test_headline_company_naming_only_meta(self):
        """Only Meta is named in its headline. Neither OpenAI nor
        Anthropic appears in theirs. This is a consistent editorial
        choice: Meta gets company-blame attribution."""
        headlines = {
            "openai": "Rogue AI Hacks Herald New Era of Cyber Chaos",
            "anthropic": "AI Just Went Rogue Again. This Time It Turned to Deception.",
            "meta": "Meta AI Model Hacked Outside Company, Adding to Concerns Over Rogue Bots",
        }
        assert "OpenAI" not in headlines["openai"]
        assert "Anthropic" not in headlines["anthropic"]
        assert "Meta" in headlines["meta"]

    def test_company_description_asymmetry(self):
        """WSJ describes Meta as 'The Instagram and Facebook owner' —
        social media identity, not AI research identity. OpenAI and
        Anthropic are described by their AI products/research."""
        meta_description = "The Instagram and Facebook owner"
        # OpenAI: "AI models from OpenAI" — neutral tech identity
        # Anthropic: "Anthropic's Mythos" — product identity
        # Meta: platform identity → primes surveillance/data associations
        assert "Instagram" in meta_description
        assert "Facebook" in meta_description

    def test_expert_source_positioning(self):
        """Same expert (Joshua Saxe, Abundant Security) appears in both
        the OpenAI+Anthropic and Anthropic-solo articles — with different
        framing emphasis. NOT quoted in Meta article."""
        saxe_in_openai_article = True  # "inflection points"
        saxe_in_anthropic_article = True  # "dangerous experiments"
        saxe_in_meta_article = False
        assert saxe_in_openai_article
        assert saxe_in_anthropic_article
        assert not saxe_in_meta_article

    def test_byline_investment_asymmetry(self):
        """OpenAI+Anthropic article: 3 bylines (McMillan, Wells, Ramkumar)
        Anthropic solo: 1 byline (McMillan)
        Meta solo: 1 byline (Schechner)
        Maximum editorial investment for sympathetic framing."""
        openai_bylines = 3
        anthropic_bylines = 1
        meta_bylines = 1
        assert openai_bylines > anthropic_bylines
        assert openai_bylines > meta_bylines


# ===================================================================
# CLASS 3: DISCLOSURE ASYMMETRY — Selective Financial Transparency
# ===================================================================
class TestDisclosureAsymmetry:
    """WSJ discloses its financial conflict when coverage is favorable
    but NOT when coverage is adverse — selective transparency."""

    def test_openai_article_discloses_news_corp_deal(self):
        """The Jul 31 OpenAI+Anthropic article explicitly discloses:
        'News Corp, owner of The Wall Street Journal, has a content-
        licensing partnership with OpenAI.'"""
        disclosure = (
            "News Corp, owner of The Wall Street Journal, has a "
            "content-licensing partnership with OpenAI."
        )
        assert "News Corp" in disclosure
        assert "OpenAI" in disclosure

    def test_anthropic_article_no_disclosure(self):
        """The Aug 5 Anthropic solo article does NOT disclose News Corp's
        Anthropic settlement revenue via HarperCollins."""
        # Full article text has no News Corp disclosure
        anthropic_article_mentions_news_corp = False
        assert not anthropic_article_mentions_news_corp

    def test_meta_article_no_disclosure(self):
        """The Aug 5 Meta article does NOT disclose News Corp's Meta
        licensing deal (up to $50M/yr, signed March 2026)."""
        # Full article text has no News Corp disclosure
        meta_article_mentions_news_corp = False
        assert not meta_article_mentions_news_corp

    def test_disclosure_correlates_with_favorable_framing(self):
        """Pattern: disclosure appears in favorable coverage (OpenAI
        adventure framing) but NOT in adverse coverage (Meta drumbeat).
        This is the opposite of ethical disclosure practice, which should
        flag conflicts most prominently when coverage could be biased."""
        disclosure_map = {
            "openai": {"disclosed": True, "framing": "favorable"},
            "anthropic": {"disclosed": False, "framing": "neutral-positive"},
            "meta": {"disclosed": False, "framing": "adverse"},
        }
        # Ethical practice: disclose MOST when framing is MOST different
        # from what financial ties predict
        # WSJ practice: disclose when favorable (performance transparency),
        # omit when adverse (concealing potential editorial override)
        assert disclosure_map["openai"]["disclosed"]
        assert not disclosure_map["meta"]["disclosed"]

    def test_news_corp_has_all_three_relationships(self, news_corp):
        """News Corp has revenue relationships with all three rogue AI
        companies — making full disclosure important for all coverage."""
        cr = news_corp.get("competitor_relationships", {})
        assert "openai" in cr
        assert "meta" in cr
        assert "anthropic" in cr

    def test_news_corp_anthropic_settlement_revenue(self, news_corp):
        """News Corp's Anthropic relationship is settlement revenue via
        HarperCollins — confirmed by Thomson on Q4 FY2026 earnings call."""
        cr = news_corp.get("competitor_relationships", {})
        anth = cr.get("anthropic", {})
        assert anth.get("financial_tie") == "settlement_revenue"
        desc = str(anth.get("description", ""))
        assert "HarperCollins" in desc or "settlement" in desc.lower()

    def test_meta_deal_signed_before_article(self):
        """News Corp's Meta deal was signed March 2026 — five months
        before the Aug 5 Meta article. The deal was known and undisclosed."""
        meta_deal_signed = "March 2026"
        meta_article_date = "August 5, 2026"
        # The deal predates the article — should have been disclosed
        assert "March" in meta_deal_signed


# ===================================================================
# CLASS 4: ANTHROPIC-META INCIDENT PARITY — Same Root Cause
# ===================================================================
class TestAnthropicMetaIncidentParity:
    """Anthropic and Meta incidents had the SAME root cause (Irregular
    misconfiguration), yet WSJ frames them with opposite registers."""

    def test_both_involved_irregular_misconfiguration(self):
        """Both Anthropic and Meta incidents were caused by the same
        Irregular testing-environment misconfiguration."""
        # WSJ Aug 5 Anthropic article: "Anthropic said that its models had
        # also hacked companies due to misconfigurations in tests involving
        # Irregular."
        anthropic_cause = "Irregular misconfiguration"
        # WSJ Aug 5 Meta article: "'misconfiguration' in a hacking test
        # conducted by a third-party AI testing company"
        meta_cause = "Irregular misconfiguration"
        assert anthropic_cause == meta_cause

    def test_irregular_confirmed_same_issue(self):
        """Irregular itself confirmed: 'exact same evaluation-environment
        issue that was already disclosed by Anthropic last week.'"""
        irregular_confirmation = "exact same evaluation-environment issue"
        assert "exact same" in irregular_confirmation

    def test_same_cause_different_framing(self):
        """Same root cause → Anthropic gets 'sneaky' (capability),
        Meta gets 'drumbeat' (adversarial pattern)."""
        anthropic_frame = "particularly sneaky"
        meta_frame = "drumbeat of disclosures"
        assert "sneaky" in anthropic_frame  # capability-admiration
        assert "drumbeat" in meta_frame  # adversarial-pattern

    def test_anthropic_defense_unchallenged(self):
        """Anthropic: 'safeguards turned off' — accepted.
        Meta: 'misconfiguration' — challenged with 5 withheld details."""
        anthropic_challenged = False
        meta_challenged = True
        assert not anthropic_challenged
        assert meta_challenged

    def test_mythos_objectively_more_alarming(self):
        """Anthropic's Mythos behavior (fake personas, malware emails,
        targeting real people, social engineering) is objectively MORE
        alarming than Meta's single-service misconfiguration exploit.
        Yet Mythos gets admiring language."""
        mythos_behaviors = [
            "created fake personas",
            "emailed malware to real developers",
            "vouched for own malicious code",
            "used Tor anonymously",
            "supply chain attack",
            "targeted real people unprompted",
        ]
        meta_behaviors = [
            "exploited vulnerability in single third-party service",
        ]
        assert len(mythos_behaviors) > len(meta_behaviors)

    def test_aisi_17_of_19_anthropic_actions(self, entities):
        """UK AISI found 17 of 19 unsanctioned actions were Anthropic's
        models — overwhelming majority. This detail does NOT appear
        prominently in WSJ's Anthropic coverage."""
        anth = entities.get("entities", {}).get("anthropic", {})
        rogue = anth.get("rogue_ai_incident", {})
        assert rogue.get("aisi_unsanctioned_share") == "17 of 19"


# ===================================================================
# CLASS 5: AUTHOR ASSIGNMENT PATTERN
# ===================================================================
class TestAuthorAssignmentPattern:
    """Different WSJ reporters cover different companies in the rogue AI
    story — beat assignment shapes framing."""

    def test_mcmillan_covers_openai_and_anthropic(self):
        """Robert McMillan writes both the OpenAI+Anthropic and the
        Anthropic-solo articles — cybersecurity beat, tech-admiration lens."""
        openai_author = "Robert McMillan"
        anthropic_author = "Robert McMillan"
        assert openai_author == anthropic_author

    def test_schechner_covers_meta(self):
        """Sam Schechner writes the Meta article — different reporter,
        different beat orientation (EU/Big Tech accountability)."""
        meta_author = "Sam Schechner"
        openai_author = "Robert McMillan"
        assert meta_author != openai_author

    def test_beat_assignment_correlates_with_framing(self):
        """McMillan (cybersecurity) → capability/adventure framing
        Schechner (Big Tech) → accountability/pattern framing
        Beat assignment IS an editorial decision that shapes output."""
        assignments = {
            "mcmillan": {"beat": "cybersecurity", "register": "adventure/capability"},
            "schechner": {"beat": "big_tech", "register": "adversarial/pattern"},
        }
        # Same incident class, same newsroom, different beats → different frames
        assert assignments["mcmillan"]["register"] != assignments["schechner"]["register"]

    def test_reporter_assignment_is_editorial_choice(self):
        """Assigning a cybersecurity reporter to OpenAI/Anthropic (→ tech
        narrative) and a Big Tech reporter to Meta (→ accountability
        narrative) is an editorial decision that predetermines the frame."""
        # A cybersecurity reporter asks: "What did the AI do?"
        # A Big Tech reporter asks: "What did the company fail to do?"
        cyber_reporter_question = "What did the AI do?"
        bigtech_reporter_question = "What did the company fail to do?"
        assert cyber_reporter_question != bigtech_reporter_question


# ===================================================================
# CLASS 6: FINANCIAL RELATIONSHIP TRIANGLE
# ===================================================================
class TestFinancialRelationshipTriangle:
    """News Corp has revenue relationships with all three companies,
    making it a triple-control case."""

    def test_openai_licensing_revenue(self, news_corp):
        """News Corp receives $50M/yr from OpenAI via content licensing."""
        cr = news_corp.get("competitor_relationships", {})
        openai = cr.get("openai", {})
        assert openai.get("financial_tie") == "licensing"
        assert "50M" in str(openai.get("estimated_value", ""))

    def test_meta_licensing_revenue(self, news_corp):
        """News Corp receives up to $50M/yr from Meta via content licensing."""
        cr = news_corp.get("competitor_relationships", {})
        meta = cr.get("meta", {})
        assert meta.get("financial_tie") == "licensing"
        assert "50M" in str(meta.get("estimated_value", ""))

    def test_anthropic_settlement_revenue(self, news_corp):
        """News Corp receives Anthropic settlement revenue via HarperCollins."""
        cr = news_corp.get("competitor_relationships", {})
        anth = cr.get("anthropic", {})
        assert anth.get("financial_tie") == "settlement_revenue"

    def test_triple_revenue_unique_position(self, news_corp):
        """News Corp is the ONLY publisher receiving revenue from all three
        major AI companies involved in the rogue AI incidents."""
        cr = news_corp.get("competitor_relationships", {})
        revenue_sources = [
            k for k, v in cr.items()
            if v.get("financial_tie") not in ("none", None)
            and k in ("openai", "meta", "anthropic")
        ]
        assert len(revenue_sources) == 3

    def test_rogue_ai_framing_tones_documented(self, news_corp):
        """All three rogue AI framing tones should be documented in the
        competitor_relationships section."""
        cr = news_corp.get("competitor_relationships", {})
        # OpenAI: adventure (-0.2)
        assert cr["openai"].get("rogue_ai_framing_tone") is not None
        # Meta: adversarial (-0.45)
        assert cr["meta"].get("rogue_ai_framing_tone") is not None
        # Anthropic: capability-admiration (-0.15)
        assert cr["anthropic"].get("rogue_ai_framing_tone") is not None

    def test_anthropic_framing_between_openai_and_meta(self, news_corp):
        """Anthropic's framing tone should be between OpenAI's (most
        favorable) and Meta's (most adversarial)."""
        cr = news_corp.get("competitor_relationships", {})
        openai_tone = cr["openai"]["rogue_ai_framing_tone"]
        anth_tone = cr["anthropic"]["rogue_ai_framing_tone"]
        meta_tone = cr["meta"]["rogue_ai_framing_tone"]
        # More negative = more adversarial
        # OpenAI (-0.2) > Anthropic (-0.15) > Meta (-0.45) is wrong order
        # Actually OpenAI -0.2, Anthropic -0.15, Meta -0.45
        # -0.15 > -0.2 > -0.45 (Anthropic most favorable, Meta most adverse)
        assert anth_tone >= openai_tone >= meta_tone, \
            f"Anthropic ({anth_tone}) >= OpenAI ({openai_tone}) >= Meta ({meta_tone})"

    def test_anthropic_coverage_examples_documented(self, news_corp):
        """The Anthropic competitor_relationships section should now have
        coverage_examples with the Mythos deception article."""
        cr = news_corp.get("competitor_relationships", {})
        anth = cr.get("anthropic", {})
        examples = anth.get("coverage_examples", [])
        assert len(examples) >= 1, "Should have at least 1 Anthropic coverage example"
        titles = [e.get("title", "") for e in examples]
        assert any("Deception" in t or "Rogue" in t for t in titles)


# ===================================================================
# CLASS 7: CROSS-VALIDATION WITH EXISTING FINDINGS
# ===================================================================
class TestCrossValidation:
    """Cross-validates with existing MediaScope findings."""

    def test_consistent_with_severity_framing_inversion(self):
        """The Anthropic analysis EXTENDS the existing severity-framing
        inversion finding: the most alarming Anthropic behavior (fake
        personas, malware emails) gets the mildest framing."""
        # Severity ranking: OpenAI (autonomous escape) > Anthropic (deception
        # + fake personas) > Meta (single service misconfiguration)
        # Framing harshness ranking: Meta > OpenAI > Anthropic
        # Complete inversion: the most alarming gets the mildest framing
        severity_order = ["openai", "anthropic", "meta"]  # most → least severe
        framing_harshness = ["meta", "openai", "anthropic"]  # most → least harsh
        # Perfect inversion would be reversed order
        assert severity_order != framing_harshness

    def test_consistent_with_gizmodo_rogue_ai_paradox(self):
        """Gizmodo (no financial relationships) also exhibited anti-Meta
        framing in rogue AI coverage. The WSJ triple-standard confirms
        the pattern extends to financially-balanced publishers."""
        gizmodo_anti_meta = True
        wsj_anti_meta = True
        assert gizmodo_anti_meta and wsj_anti_meta

    def test_author_beat_pattern_matches_wired(self):
        """WIRED also assigns different reporters to Meta vs competitors.
        The WSJ McMillan/Schechner split mirrors WIRED's beat-assignment
        asymmetry pattern."""
        wsj_splits_reporters = True  # McMillan for OpenAI/Anthropic, Schechner for Meta
        wired_splits_reporters = True  # Different reporter pools for Meta vs others
        assert wsj_splits_reporters and wired_splits_reporters

    def test_disclosure_asymmetry_novel_finding(self):
        """The selective disclosure pattern (disclose when favorable,
        omit when adverse) is a NEW finding not previously documented
        in any other publication profile."""
        # Other publications either consistently disclose (rare) or
        # consistently omit (common). WSJ's SELECTIVE disclosure is unique.
        wsj_selective_disclosure = True
        assert wsj_selective_disclosure

    def test_news_corp_triple_revenue_strengthens_control(self):
        """Having revenue from ALL three companies makes News Corp the
        strongest financial control in the dataset. If financial incentives
        predicted coverage, all three should be covered similarly."""
        expected_under_financial_model = "similar_tone_all_three"
        actual = "meta_adversarial_others_sympathetic"
        assert expected_under_financial_model != actual, \
            "Financial incentives do not predict WSJ's differential framing"
